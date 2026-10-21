# Microsoft AI-103 — Full-Length Mock Exam 2

Azure AI Apps and Agents Developer Associate · 50 questions · 120 minutes · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 38 single-choice, 8 multi-select (selection count stated), 4 ordering items rendered as answer choices, and 2 case studies of 3 questions. Hot-area, drag-and-drop UI, labs, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. A hospital plans an ambient documentation pilot and must confirm which models accept audio and text in its region. What should the team review?

Domain: Plan and manage an Azure AI solution

- A. Compare supported models in the Foundry model catalog
- B. Use a general-purpose large language model for complex reasoning
- C. Train or deploy a task-specific model outside the prebuilt catalog
- D. Use a small language model for a narrow, high-volume task

### 2. A triage classifier must return one of eight labels at low cost and low latency. Which model class should be evaluated first?

Domain: Plan and manage an Azure AI solution

- A. Use a small language model for a narrow, high-volume task
- B. Use a general-purpose large language model for complex reasoning
- C. Use a multimodal model for combined text, image, or audio input
- D. Train or deploy a task-specific model outside the prebuilt catalog

### 3. A scheduling assistant must recall the clinic a patient chose earlier in the same conversation. What should be used?

Domain: Plan and manage an Azure AI solution

- A. Expose an OpenAPI operation as an agent tool
- B. Use managed conversation state or memory for continuity
- C. Connect an Azure AI Search index as agent knowledge
- D. Expose a typed function as an agent tool

### 4. A clinical policy assistant must search 12,000 approved documents and expose them to an agent with citations. Which two components should be included? Select two.

Domain: Plan and manage an Azure AI solution

- A. Train or deploy a task-specific model outside the prebuilt catalog
- B. Use managed conversation state or memory for continuity
- C. Connect an Azure AI Search index as agent knowledge
- D. Use a vector index for semantic retrieval
- E. Expose a typed function as an agent tool

### 5. A hospital must move a triage assistant from pilot to production with reproducible infrastructure. Which sequence should the team follow?

Domain: Plan and manage an Azure AI solution

- A. Provision resources → deploy model → configure app connection → evaluate → promote
- B. Evaluate → provision resources → promote → deploy model → configure app
- C. Configure app → provision resources → deploy model → promote → evaluate
- D. Deploy model → promote → provision resources → evaluate → configure app

### 6. Protected health information must never traverse the public internet to the model endpoint. What should be configured?

Domain: Plan and manage an Azure AI solution

- A. Plan for model quota expressed in tokens and requests per minute
- B. Manage AI resources with infrastructure as code and CI/CD
- C. Use private endpoints and disable public network access
- D. Use supported prompt or response caching where appropriate

### 7. The documentation assistant is throttled only when about 40 clinicians dictate at the same moment. What should be re-planned first?

Domain: Plan and manage an Azure AI solution

- A. Monitor input and quality drift over time
- B. Use provisioned throughput for predictable high-volume workloads
- C. Track cost per accepted task, not only per token
- D. Plan for model quota expressed in tokens and requests per minute

### 8. Cost review shows that a long, unchanged policy preamble is resent on every request. Which optimization should be applied first?

Domain: Plan and manage an Azure AI solution

- A. Use batch processing for latency-tolerant bulk work
- B. Use supported prompt or response caching where appropriate
- C. Use provisioned throughput for predictable high-volume workloads
- D. Track cost per accepted task, not only per token

### 9. Transcription quality declines slowly after clinics install a new headset model. What should the team monitor?

Domain: Plan and manage an Azure AI solution

- A. Plan for model quota expressed in tokens and requests per minute
- B. Track cost per accepted task, not only per token
- C. Monitor input and quality drift over time
- D. Apply watermarks or provenance markers to generated media

### 10. A containerized app must authenticate to its Foundry resource without secrets in code or configuration. What should it use?

Domain: Plan and manage an Azure AI solution

- A. Shared connection string with an embedded secret
- B. Long-lived API key pasted into configuration
- C. Authenticate with a managed identity instead of keys
- D. Store secrets in Azure Key Vault when keys are unavoidable

### 11. A new service must read one index and nothing else, with no stored secrets. Which two actions should you take? Select two.

Domain: Plan and manage an Azure AI solution

- A. Configure content safety filters for harmful categories
- B. Store secrets in Azure Key Vault when keys are unavoidable
- C. Use least-privilege Azure RBAC roles for the workload identity
- D. Use private endpoints and disable public network access
- E. Authenticate with a managed identity instead of keys

### 12. An agent may send follow-up instructions directly to patients. Which two safeguards belong in the design? Select two.

Domain: Plan and manage an Azure AI solution

- A. Require human approval before consequential actions
- B. Use supported prompt or response caching where appropriate
- C. Configure content safety filters for harmful categories
- D. Use a small language model for a narrow, high-volume task
- E. Lower temperature for more deterministic extraction

### 13. Clinicians report that generated summaries occasionally omit a listed allergy. Which control fits best?

Domain: Plan and manage an Azure AI solution

- A. Require human approval before consequential actions
- B. Enforce constraints in code and platform policy
- C. Route low-confidence or high-impact results to human review
- D. Set agent oversight mode and tool-access constraints

### 14. An assistant must answer from the current approved formulary and show where each answer came from. Which approach fits?

Domain: Implement generative AI and agentic solutions

- A. Route requests to different models by task difficulty
- B. Configure content safety filters for harmful categories
- C. Compare supported models in the Foundry model catalog
- D. Ground responses with retrieval-augmented generation

### 15. A discharge workflow must extract medications, validate them against a formulary, then draft instructions. What should the design use?

Domain: Implement generative AI and agentic solutions

- A. Design multistep workflows with explicit checkpoints
- B. One model call with no external retrieval or tool use
- C. Use a versioned prompt template with explicit variables
- D. Limit autonomy with scope, budget, and stop conditions

### 16. An application must call only the models deployed to a specific approved Foundry project. What should it be configured with?

Domain: Implement generative AI and agentic solutions

- A. Compare supported models in the Foundry model catalog
- B. Store secrets in Azure Key Vault when keys are unavoidable
- C. Connect the application to the Foundry project endpoint
- D. Use an Azure AI Search indexer to pull source content

### 17. A Python service needs supported authentication, retries, and streaming for Foundry calls. What should it use?

Domain: Implement generative AI and agentic solutions

- A. Use batch processing for latency-tolerant bulk work
- B. Use a Foundry SDK or supported connector from application code
- C. Create and run deployments by hand in the portal
- D. Manage AI resources with infrastructure as code and CI/CD

### 18. A downstream record system consumes model output, and reviewers must verify each answer. Which two requirements matter most? Select two.

Domain: Implement generative AI and agentic solutions

- A. Require citations tied to retrieved evidence
- B. Lower temperature for more deterministic extraction
- C. Use provisioned throughput for predictable high-volume workloads
- D. Apply watermarks or provenance markers to generated media
- E. Return a defined JSON schema for downstream systems

### 19. An answer reads smoothly and stays on topic but asserts a formulary rule that was never retrieved. Which failure should be measured?

Domain: Implement generative AI and agentic solutions

- A. Evaluate structure and logical consistency of responses
- B. Detect fabricated or unsupported statements
- C. Measure whether retrieved content and answers address the question
- D. Detect tone and sentiment appropriate to the audience

### 20. An agent sends malformed arguments when booking appointments because the tool description is vague. What should be improved first?

Domain: Implement generative AI and agentic solutions

- A. Define narrow tool schemas with clear descriptions
- B. Put stable behavior rules in the system message
- C. Use a versioned prompt template with explicit variables
- D. Use managed conversation state or memory for continuity

### 21. Every agent turn must follow the same clinical tone and refusal policy. Where should that guidance live?

Domain: Implement generative AI and agentic solutions

- A. Configure content safety filters for harmful categories
- B. Enforce constraints in code and platform policy
- C. Put stable behavior rules in the system message
- D. Use least-privilege Azure RBAC roles for the workload identity

### 22. An agent must call an existing scheduling service that already publishes an OpenAPI specification. Which tool type fits best?

Domain: Implement generative AI and agentic solutions

- A. Expose a typed function as an agent tool
- B. Use managed conversation state or memory for continuity
- C. Ground responses with retrieval-augmented generation
- D. Expose an OpenAPI operation as an agent tool

### 23. A referral agent must keep a referral number across turns and look that referral up in a practice system. Which two capabilities are required? Select two.

Domain: Implement generative AI and agentic solutions

- A. Choose an embedding model suited to the content and language
- B. Apply watermarks or provenance markers to generated media
- C. Use provisioned throughput for predictable high-volume workloads
- D. Expose a typed function as an agent tool
- E. Persist conversation history in a thread or session

### 24. Which sequence correctly builds and releases a patient-facing scheduling agent?

Domain: Implement generative AI and agentic solutions

- A. Deploy with monitoring → define role and goal → configure tools → evaluate in sandbox → attach knowledge
- B. Define role and goal → configure tools → attach knowledge → evaluate in sandbox → deploy with monitoring
- C. Configure tools → deploy with monitoring → define role and goal → attach knowledge → evaluate in sandbox
- D. Attach knowledge → configure tools → deploy with monitoring → define role and goal → evaluate in sandbox

### 25. A triage agent must pass a conversation to a scheduling specialist while keeping context. Which pattern fits?

Domain: Implement generative AI and agentic solutions

- A. Transfer control between agents with explicit context
- B. Use self-critique or reflection to improve drafts
- C. Run independent agents concurrently
- D. Run agents in a fixed sequence

### 26. An agent fails only when a request requires two tool calls in sequence. What should be inspected to find the failing step?

Domain: Implement generative AI and agentic solutions

- A. Use supported prompt or response caching where appropriate
- B. Apply watermarks or provenance markers to generated media
- C. Enable tracing across agent, model, and tool calls
- D. Plan for model quota expressed in tokens and requests per minute

### 27. Structured extraction returns different values for identical repeated requests. Which setting should be reduced first?

Domain: Implement generative AI and agentic solutions

- A. Adjust top-p to control response diversity
- B. Lower temperature for more deterministic extraction
- C. Route requests to different models by task difficulty
- D. Use supported prompt or response caching where appropriate

### 28. A clinician must remove a visible patient name badge from an approved photo before a teaching deck. What should be used?

Domain: Implement computer vision solutions

- A. Generate concise or detailed image captions
- B. Apply prompt-driven image modifications
- C. Edit a region of an image with a mask
- D. Generate video from text or reference media

### 29. A patient-education team needs an original illustration of a healthy-plate diagram. Which capability applies?

Domain: Implement computer vision solutions

- A. Generate video from text or reference media
- B. Generate alt text aligned to accessibility guidance
- C. Generate images from text and reference media
- D. Edit a region of an image with a mask

### 30. A safety team must find the exact minute in recorded ward footage where a bed rail is lowered. What capability applies?

Domain: Implement computer vision solutions

- A. Edit generated video segments
- B. Analyze video segments for events and content
- C. Apply prompt-driven image modifications
- D. Generate concise or detailed image captions

### 31. A patient portal needs accessible image descriptions and answers about values shown in chart images. Which two capabilities apply? Select two.

Domain: Implement computer vision solutions

- A. Lower temperature for more deterministic extraction
- B. Generate alt text aligned to accessibility guidance
- C. Use provisioned throughput for predictable high-volume workloads
- D. Apply watermarks or provenance markers to generated media
- E. Answer questions grounded in visual evidence

### 32. A stock-photo library needs one short sentence describing each image for search. What should be generated?

Domain: Implement computer vision solutions

- A. Identify objects, components, or regions in visual content
- B. Return typed fields for automation
- C. Generate concise or detailed image captions
- D. Apply OCR to convert images and scans into usable text

### 33. Which sequence correctly processes a scanned referral image and routes uncertain values for review?

Domain: Implement computer vision solutions

- A. Parse structured fields → send multimodal request → upload image → validate format → review
- B. Upload image → validate format and size → send multimodal request → parse structured fields → route low-confidence values to review
- C. Send multimodal request → upload image → validate format → parse structured fields → review
- D. Validate format → review → upload image → parse structured fields → send multimodal request

### 34. Generated patient-education images must be screened for unsafe medical depictions before publication. Which control applies?

Domain: Implement computer vision solutions

- A. Enforce brand and usage rules for generated visuals
- B. Treat text embedded in images as untrusted input
- C. Apply watermarks or provenance markers to generated media
- D. Filter unsafe or disallowed visual content

### 35. A downstream records service requires fixed field names and types from each discharge summary. What should the prompt request?

Domain: Implement text analysis solutions

- A. Prompt for JSON that conforms to a supplied schema
- B. Generate summaries with explicit length and audience constraints
- C. Identify topics or key phrases for navigation
- D. Use Azure Translator or a language model for translation

### 36. A quality team reviews patient messages for disclosure risk and rising frustration. Which two analyses are relevant? Select two.

Domain: Implement text analysis solutions

- A. Analyze sentiment and tone with an appropriate service
- B. Identify topics or key phrases for navigation
- C. Apply a custom glossary or terminology list
- D. Generate summaries with explicit length and audience constraints
- E. Detect and redact sensitive personal data

### 37. Discharge instructions must appear in the patient's preferred language. Which capability applies?

Domain: Implement text analysis solutions

- A. Use Azure Translator or a language model for translation
- B. Apply a custom glossary or terminology list
- C. Detect and redact sensitive personal data
- D. Generate summaries with explicit length and audience constraints

### 38. Recorded consultations must become searchable text. Which capability is required?

Domain: Implement text analysis solutions

- A. Generate concise or detailed image captions
- B. Synthesize speech with Azure AI Speech
- C. Translate spoken language with speech translation
- D. Transcribe speech to text with Azure AI Speech

### 39. Dictation accuracy is poor for local drug names and clinician accents. What should be trained?

Domain: Implement text analysis solutions

- A. Use a custom speech model for specialized vocabulary
- B. Transcribe speech to text with Azure AI Speech
- C. Apply a custom glossary or terminology list
- D. Synthesize speech with Azure AI Speech

### 40. An extraction prompt misses specialty abbreviations used by only one hospital network. What should be added?

Domain: Implement text analysis solutions

- A. Apply a custom glossary or terminology list
- B. Adapt prompts and models to domain terminology
- C. Detect and redact sensitive personal data
- D. Use Azure Translator or a language model for translation

### 41. An index must stay synchronized with documents in a storage account without custom code. What should be used?

Domain: Implement information extraction solutions

- A. Use an Azure AI Search indexer to pull source content
- B. Add an enrichment skillset to an indexing pipeline
- C. Apply OCR to convert images and scans into usable text
- D. Push documents to an index through the data-plane API

### 42. Staff search by exact claim identifier and by paraphrased coverage questions. Which two features should be combined? Select two.

Domain: Implement information extraction solutions

- A. Combine keyword and vector retrieval
- B. Use a vector index for semantic retrieval
- C. Apply semantic ranking to reorder search results
- D. Apply watermarks or provenance markers to generated media
- E. Lower temperature for more deterministic extraction

### 43. An ingestion pipeline must extract entities and generate summaries while indexing. What should be added?

Domain: Implement information extraction solutions

- A. Push documents to an index through the data-plane API
- B. Add an enrichment skillset to an indexing pipeline
- C. Use an Azure AI Search indexer to pull source content
- D. Apply OCR to convert images and scans into usable text

### 44. Which sequence correctly builds a citable retrieval pipeline over clinical policy documents?

Domain: Implement information extraction solutions

- A. Ingest → retrieve → chunk → embed → index → cite
- B. Chunk → embed → ingest → retrieve → index → cite
- C. Ingest → extract text → chunk → embed → index → retrieve with citations
- D. Index → retrieve → ingest → chunk → embed → cite

---

## Case study — BillingBot

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 45. Translated statements keep mangling approved plan names. What should be added?

Domain: Implement text analysis solutions

- A. Identify topics or key phrases for navigation
- B. Analyze sentiment and tone with an appropriate service
- C. Generate summaries with explicit length and audience constraints
- D. Apply a custom glossary or terminology list

### 46. Standard Explanation of Benefits forms arrive in a well-known layout with stable fields. What should be used first?

Domain: Implement information extraction solutions

- A. Use a prebuilt document model for common document types
- B. Use Azure AI Document Intelligence for forms and documents
- C. Configure a Content Understanding analyzer for the content type
- D. Train a custom extraction model on labeled documents

### 47. Extracted amounts occasionally disagree with the scanned value. What should route those fields to a person?

Domain: Implement information extraction solutions

- A. Generate summaries with explicit length and audience constraints
- B. Measure whether retrieved content and answers address the question
- C. Analyze sentiment and tone with an appropriate service
- D. Use field-level confidence to route exceptions

---

## Case study — ClinDoc

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 48. After go-live, summaries sometimes state medications that no source note contains. Which signal should be monitored?

Domain: Plan and manage an Azure AI solution

- A. Track cost per accepted task, not only per token
- B. Plan for model quota expressed in tokens and requests per minute
- C. Measure end-to-end latency across model, retrieval, and tools
- D. Monitor groundedness and citation quality in production

### 49. The assistant must confirm whether a patient has an appointment tomorrow before answering. Which capability performs that check?

Domain: Implement generative AI and agentic solutions

- A. Expose an OpenAPI operation as an agent tool
- B. Use managed conversation state or memory for continuity
- C. Ground responses with retrieval-augmented generation
- D. Expose a typed function as an agent tool

### 50. One request may need records, scheduling, and billing expertise. Which pattern should coordinate them?

Domain: Implement generative AI and agentic solutions

- A. Run agents in a fixed sequence
- B. Connect specialist agents as tools to an orchestrator
- C. Run independent agents concurrently
- D. Use a manager agent to coordinate specialists

---

## Answer key and explanations

### Question 1 — A

Answer: Compare supported models in the Foundry model catalog. The model catalog lists modality support, regional availability, and lifecycle status before selection. The catalog shows supported models with capability, modality, region, and lifecycle details. Verify availability for your subscription and region before designing around one model. Local study-map skill 1.1 (Selecting Foundry Models and Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. The catalog shows supported models with capability, modality, region, and lifecycle details. Verify availability for your subscription and region before designing around one model. In this case: The model catalog lists modality support, regional availability, and lifecycle status before selection.
- **B:** Incorrect for this question. Large models handle ambiguity and multi-step reasoning better in many cases, at higher cost and latency. Select with measured evidence rather than brand preference. Why the correct answer wins: The model catalog lists modality support, regional availability, and lifecycle status before selection.
- **C:** Incorrect for this question. A custom model is justified when supported prebuilt options cannot meet a defined requirement. It adds data, evaluation, and lifecycle obligations. Why the correct answer wins: The model catalog lists modality support, regional availability, and lifecycle status before selection.
- **D:** Incorrect for this question. Small models can reduce latency and cost for constrained classification or extraction. Confirm quality on representative data before standardizing. Why the correct answer wins: The model catalog lists modality support, regional availability, and lifecycle status before selection.

### Question 2 — A

Answer: Use a small language model for a narrow, high-volume task. A small language model is the reasonable starting point for narrow classification with tight cost limits. Small models can reduce latency and cost for constrained classification or extraction. Confirm quality on representative data before standardizing. Local study-map skill 1.1 (Selecting Foundry Models and Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. Small models can reduce latency and cost for constrained classification or extraction. Confirm quality on representative data before standardizing. In this case: A small language model is the reasonable starting point for narrow classification with tight cost limits.
- **B:** Incorrect for this question. Large models handle ambiguity and multi-step reasoning better in many cases, at higher cost and latency. Select with measured evidence rather than brand preference. Why the correct answer wins: A small language model is the reasonable starting point for narrow classification with tight cost limits.
- **C:** Incorrect for this question. Multimodal models accept more than one content type in a request. Validate extraction and grounding quality for each modality used. Why the correct answer wins: A small language model is the reasonable starting point for narrow classification with tight cost limits.
- **D:** Incorrect for this question. A custom model is justified when supported prebuilt options cannot meet a defined requirement. It adds data, evaluation, and lifecycle obligations. Why the correct answer wins: A small language model is the reasonable starting point for narrow classification with tight cost limits.

### Question 3 — B

Answer: Use managed conversation state or memory for continuity. Managed conversation state or memory carries the earlier choice across turns. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Local study-map skill 1.2 (Retrieval, Memory, Tool, and Knowledge Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. OpenAPI tools describe supported HTTP operations for agent use. Narrow operations, validate inputs, and authenticate the caller. Why the correct answer wins: Managed conversation state or memory carries the earlier choice across turns.
- **B:** Correct. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. In this case: Managed conversation state or memory carries the earlier choice across turns.
- **C:** Incorrect for this question. An index gives an agent curated, searchable evidence under configured access. Index content and permissions require ongoing ownership. Why the correct answer wins: Managed conversation state or memory carries the earlier choice across turns.
- **D:** Incorrect for this question. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. Why the correct answer wins: Managed conversation state or memory carries the earlier choice across turns.

### Question 4 — C, D

Answers: Use a vector index for semantic retrieval; Connect an Azure AI Search index as agent knowledge. A vector index supplies semantic retrieval, and a knowledge index exposes that content to the agent. Embeddings support similarity search over meaning rather than exact terms. Vector search still needs chunking, filtering, and evaluation. An index gives an agent curated, searchable evidence under configured access. Index content and permissions require ongoing ownership. Local study-map skill 1.2 (Retrieval, Memory, Tool, and Knowledge Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. A custom model is justified when supported prebuilt options cannot meet a defined requirement. It adds data, evaluation, and lifecycle obligations. Why the correct answer wins: A vector index supplies semantic retrieval, and a knowledge index exposes that content to the agent.
- **B:** Incorrect for this question. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Why the correct answer wins: A vector index supplies semantic retrieval, and a knowledge index exposes that content to the agent.
- **C:** Correct. An index gives an agent curated, searchable evidence under configured access. Index content and permissions require ongoing ownership. In this case: A vector index supplies semantic retrieval, and a knowledge index exposes that content to the agent.
- **D:** Correct. Embeddings support similarity search over meaning rather than exact terms. Vector search still needs chunking, filtering, and evaluation. In this case: A vector index supplies semantic retrieval, and a knowledge index exposes that content to the agent.
- **E:** Incorrect for this question. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. Why the correct answer wins: A vector index supplies semantic retrieval, and a knowledge index exposes that content to the agent.

### Question 5 — A

Answer: Provision resources → deploy model → configure app connection → evaluate → promote. Resources and deployment come first, app configuration follows, and evaluation gates promotion. Provisioning and deployment precede app configuration, and evaluation gates promotion. Local study-map skill 1.3 (Infrastructure, Deployment, and CI/CD), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. Provisioning and deployment precede app configuration, and evaluation gates promotion. In this case: Resources and deployment come first, app configuration follows, and evaluation gates promotion.
- **B:** Incorrect for this question. Evaluation before any deployment or configuration has nothing meaningful to assess. Why the correct answer wins: Resources and deployment come first, app configuration follows, and evaluation gates promotion.
- **C:** Incorrect for this question. Evaluation after promotion cannot gate the release. Why the correct answer wins: Resources and deployment come first, app configuration follows, and evaluation gates promotion.
- **D:** Incorrect for this question. Promotion before provisioning and evaluation skips the controls that make deployment safe. Why the correct answer wins: Resources and deployment come first, app configuration follows, and evaluation gates promotion.

### Question 6 — C

Answer: Use private endpoints and disable public network access. A private endpoint with public access disabled keeps model traffic on the private network path. Private connectivity keeps service traffic on approved network paths. Pair it with private DNS so clients resolve the private address. Local study-map skill 1.3 (Infrastructure, Deployment, and CI/CD), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. Why the correct answer wins: A private endpoint with public access disabled keeps model traffic on the private network path.
- **B:** Incorrect for this question. Repeatable deployments reduce configuration drift. Include model deployments, indexes, and connections in review and promotion. Why the correct answer wins: A private endpoint with public access disabled keeps model traffic on the private network path.
- **C:** Correct. Private connectivity keeps service traffic on approved network paths. Pair it with private DNS so clients resolve the private address. In this case: A private endpoint with public access disabled keeps model traffic on the private network path.
- **D:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: A private endpoint with public access disabled keeps model traffic on the private network path.

### Question 7 — D

Answer: Plan for model quota expressed in tokens and requests per minute. Request and token quota must cover realistic peak concurrency. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. Local study-map skill 1.4 (Quotas, Scaling, and Cost), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. User behavior, data, and models change. Rolling baselines reveal degradation that a one-time evaluation misses. Why the correct answer wins: Request and token quota must cover realistic peak concurrency.
- **B:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: Request and token quota must cover realistic peak concurrency.
- **C:** Incorrect for this question. Retries, tool calls, evaluation, and review contribute to unit economics. Per-outcome cost supports better optimization. Why the correct answer wins: Request and token quota must cover realistic peak concurrency.
- **D:** Correct. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. In this case: Request and token quota must cover realistic peak concurrency.

### Question 8 — B

Answer: Use supported prompt or response caching where appropriate. Prompt caching reuses the repeated preamble instead of re-billing it on each call. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Local study-map skill 1.4 (Quotas, Scaling, and Cost), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Batch deployments can lower cost for large asynchronous jobs. They are unsuitable for interactive agent turns. Why the correct answer wins: Prompt caching reuses the repeated preamble instead of re-billing it on each call.
- **B:** Correct. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. In this case: Prompt caching reuses the repeated preamble instead of re-billing it on each call.
- **C:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: Prompt caching reuses the repeated preamble instead of re-billing it on each call.
- **D:** Incorrect for this question. Retries, tool calls, evaluation, and review contribute to unit economics. Per-outcome cost supports better optimization. Why the correct answer wins: Prompt caching reuses the repeated preamble instead of re-billing it on each call.

### Question 9 — C

Answer: Monitor input and quality drift over time. Input drift in audio characteristics explains quality changes that code changes do not. User behavior, data, and models change. Rolling baselines reveal degradation that a one-time evaluation misses. Local study-map skill 1.5 (Monitoring Performance, Drift, Safety, and Grounding), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. Why the correct answer wins: Input drift in audio characteristics explains quality changes that code changes do not.
- **B:** Incorrect for this question. Retries, tool calls, evaluation, and review contribute to unit economics. Per-outcome cost supports better optimization. Why the correct answer wins: Input drift in audio characteristics explains quality changes that code changes do not.
- **C:** Correct. User behavior, data, and models change. Rolling baselines reveal degradation that a one-time evaluation misses. In this case: Input drift in audio characteristics explains quality changes that code changes do not.
- **D:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Input drift in audio characteristics explains quality changes that code changes do not.

### Question 10 — C

Answer: Authenticate with a managed identity instead of keys. A managed identity obtains Entra ID tokens without stored credentials. Managed identities avoid embedded secrets and support role-based access. Assign only required data-plane roles. Local study-map skill 1.6 (Security, Identity, and Networking), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. A shared secret grants broad access, cannot be scoped per workload, and complicates rotation and auditing. Why the correct answer wins: A managed identity obtains Entra ID tokens without stored credentials.
- **B:** Incorrect for this question. Static keys are easily leaked, hard to rotate across services, and provide no per-identity authorization. Why the correct answer wins: A managed identity obtains Entra ID tokens without stored credentials.
- **C:** Correct. Managed identities avoid embedded secrets and support role-based access. Assign only required data-plane roles. In this case: A managed identity obtains Entra ID tokens without stored credentials.
- **D:** Incorrect for this question. A managed secret store supports rotation and access control. Secrets should never appear in prompts, code, or logs. Why the correct answer wins: A managed identity obtains Entra ID tokens without stored credentials.

### Question 11 — C, E

Answers: Authenticate with a managed identity instead of keys; Use least-privilege Azure RBAC roles for the workload identity. Use a managed identity for authentication and a least-privilege role for authorization. Managed identities avoid embedded secrets and support role-based access. Assign only required data-plane roles. Roles should match the operations the app or agent performs. Broad contributor access increases blast radius. Local study-map skill 1.6 (Security, Identity, and Networking), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Filters assign severity and can block or annotate content. Thresholds should reflect the use case and applicable policy. Why the correct answer wins: Use a managed identity for authentication and a least-privilege role for authorization.
- **B:** Incorrect for this question. A managed secret store supports rotation and access control. Secrets should never appear in prompts, code, or logs. Why the correct answer wins: Use a managed identity for authentication and a least-privilege role for authorization.
- **C:** Correct. Roles should match the operations the app or agent performs. Broad contributor access increases blast radius. In this case: Use a managed identity for authentication and a least-privilege role for authorization.
- **D:** Incorrect for this question. Private connectivity keeps service traffic on approved network paths. Pair it with private DNS so clients resolve the private address. Why the correct answer wins: Use a managed identity for authentication and a least-privilege role for authorization.
- **E:** Correct. Managed identities avoid embedded secrets and support role-based access. Assign only required data-plane roles. In this case: Use a managed identity for authentication and a least-privilege role for authorization.

### Question 12 — A, C

Answers: Configure content safety filters for harmful categories; Require human approval before consequential actions. Content filters reduce harmful output, and approval gates control outbound patient messages. Filters assign severity and can block or annotate content. Thresholds should reflect the use case and applicable policy. Approval must occur before the effect and identify who approved what. A model confidence score is not approval. Local study-map skill 1.7 (Responsible AI Controls and Oversight), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. Approval must occur before the effect and identify who approved what. A model confidence score is not approval. In this case: Content filters reduce harmful output, and approval gates control outbound patient messages.
- **B:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Content filters reduce harmful output, and approval gates control outbound patient messages.
- **C:** Correct. Filters assign severity and can block or annotate content. Thresholds should reflect the use case and applicable policy. In this case: Content filters reduce harmful output, and approval gates control outbound patient messages.
- **D:** Incorrect for this question. Small models can reduce latency and cost for constrained classification or extraction. Confirm quality on representative data before standardizing. Why the correct answer wins: Content filters reduce harmful output, and approval gates control outbound patient messages.
- **E:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Content filters reduce harmful output, and approval gates control outbound patient messages.

### Question 13 — C

Answer: Route low-confidence or high-impact results to human review. Allergy content is high-risk, so uncertain summaries must be reviewed by a clinician before use. Review targets uncertainty and consequence rather than every item. Define who decides and what evidence they receive. Local study-map skill 1.7 (Responsible AI Controls and Oversight), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Approval must occur before the effect and identify who approved what. A model confidence score is not approval. Why the correct answer wins: Allergy content is high-risk, so uncertain summaries must be reviewed by a clinician before use.
- **B:** Incorrect for this question. Guardrails are technical controls, not prompt suggestions. Validate inputs, authorize tools, and limit egress. Why the correct answer wins: Allergy content is high-risk, so uncertain summaries must be reviewed by a clinician before use.
- **C:** Correct. Review targets uncertainty and consequence rather than every item. Define who decides and what evidence they receive. In this case: Allergy content is high-risk, so uncertain summaries must be reviewed by a clinician before use.
- **D:** Incorrect for this question. Oversight settings bound what an agent may do autonomously. They should be tested against realistic misuse and failure. Why the correct answer wins: Allergy content is high-risk, so uncertain summaries must be reviewed by a clinician before use.

### Question 14 — D

Answer: Ground responses with retrieval-augmented generation. RAG retrieves approved current evidence and supports source citations. RAG supplies selected source content at request time so answers can cite current evidence. It reduces but does not eliminate fabrication. Local study-map skill 2.1 (Building Generative Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Routing can balance quality and cost. Fallback and evaluation are required. Why the correct answer wins: RAG retrieves approved current evidence and supports source citations.
- **B:** Incorrect for this question. Filters assign severity and can block or annotate content. Thresholds should reflect the use case and applicable policy. Why the correct answer wins: RAG retrieves approved current evidence and supports source citations.
- **C:** Incorrect for this question. The catalog shows supported models with capability, modality, region, and lifecycle details. Verify availability for your subscription and region before designing around one model. Why the correct answer wins: RAG retrieves approved current evidence and supports source citations.
- **D:** Correct. RAG supplies selected source content at request time so answers can cite current evidence. It reduces but does not eliminate fabrication. In this case: RAG retrieves approved current evidence and supports source citations.

### Question 15 — A

Answer: Design multistep workflows with explicit checkpoints. Staged steps with validation checkpoints stop unverified extraction from reaching patients. Checkpoints validate intermediate results before later steps depend on them. This limits error propagation. Local study-map skill 2.1 (Building Generative Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Checkpoints validate intermediate results before later steps depend on them. This limits error propagation. In this case: Staged steps with validation checkpoints stop unverified extraction from reaching patients.
- **B:** Incorrect for this question. A single call cannot validate intermediate results or fetch authoritative evidence, so it is unsuitable for multi-stage or grounded workflows. Why the correct answer wins: Staged steps with validation checkpoints stop unverified extraction from reaching patients.
- **C:** Incorrect for this question. Templates improve consistency and reviewability. Version them and test changes. Why the correct answer wins: Staged steps with validation checkpoints stop unverified extraction from reaching patients.
- **D:** Incorrect for this question. Autonomous workflows need bounded actions and escalation. Unbounded loops and broad tools increase risk. Why the correct answer wins: Staged steps with validation checkpoints stop unverified extraction from reaching patients.

### Question 16 — C

Answer: Connect the application to the Foundry project endpoint. The project endpoint binds the client to the approved project and its deployments. Project endpoints and SDK clients bind an app to approved models and resources. Use identity-based authentication and environment-specific configuration. Local study-map skill 2.2 (Foundry SDK and Project Integration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. The catalog shows supported models with capability, modality, region, and lifecycle details. Verify availability for your subscription and region before designing around one model. Why the correct answer wins: The project endpoint binds the client to the approved project and its deployments.
- **B:** Incorrect for this question. A managed secret store supports rotation and access control. Secrets should never appear in prompts, code, or logs. Why the correct answer wins: The project endpoint binds the client to the approved project and its deployments.
- **C:** Correct. Project endpoints and SDK clients bind an app to approved models and resources. Use identity-based authentication and environment-specific configuration. In this case: The project endpoint binds the client to the approved project and its deployments.
- **D:** Incorrect for this question. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. Why the correct answer wins: The project endpoint binds the client to the approved project and its deployments.

### Question 17 — B

Answer: Use a Foundry SDK or supported connector from application code. A supported Foundry SDK provides maintained client behavior instead of hand-built HTTP calls. SDKs provide supported request and response patterns. Pin versions and handle retries, timeouts, and errors explicitly. Local study-map skill 2.2 (Foundry SDK and Project Integration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Batch deployments can lower cost for large asynchronous jobs. They are unsuitable for interactive agent turns. Why the correct answer wins: A supported Foundry SDK provides maintained client behavior instead of hand-built HTTP calls.
- **B:** Correct. SDKs provide supported request and response patterns. Pin versions and handle retries, timeouts, and errors explicitly. In this case: A supported Foundry SDK provides maintained client behavior instead of hand-built HTTP calls.
- **C:** Incorrect for this question. Manual portal changes work for exploration but are slow, undocumented, and hard to reproduce, so they are a poor fit for governed release processes. Why the correct answer wins: A supported Foundry SDK provides maintained client behavior instead of hand-built HTTP calls.
- **D:** Incorrect for this question. Repeatable deployments reduce configuration drift. Include model deployments, indexes, and connections in review and promotion. Why the correct answer wins: A supported Foundry SDK provides maintained client behavior instead of hand-built HTTP calls.

### Question 18 — A, E

Answers: Require citations tied to retrieved evidence; Return a defined JSON schema for downstream systems. Citations support verification, and structured output supports reliable record creation. Citations let users verify claims and support auditing. Preserve source and chunk identifiers through the pipeline. Structured output supports validation and automation. Schema validity does not prove semantic correctness. Local study-map skill 2.3 (Evaluating Models and Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Citations let users verify claims and support auditing. Preserve source and chunk identifiers through the pipeline. In this case: Citations support verification, and structured output supports reliable record creation.
- **B:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Citations support verification, and structured output supports reliable record creation.
- **C:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: Citations support verification, and structured output supports reliable record creation.
- **D:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Citations support verification, and structured output supports reliable record creation.
- **E:** Correct. Structured output supports validation and automation. Schema validity does not prove semantic correctness. In this case: Citations support verification, and structured output supports reliable record creation.

### Question 19 — B

Answer: Detect fabricated or unsupported statements. Fabrication measures claims unsupported by evidence, which fluency does not detect. Fabrication checks compare claims with evidence. Fluency and confidence are not evidence of accuracy. Local study-map skill 2.3 (Evaluating Models and Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Coherence checks readability and internal consistency. It does not establish factual accuracy. Why the correct answer wins: Fabrication measures claims unsupported by evidence, which fluency does not detect.
- **B:** Correct. Fabrication checks compare claims with evidence. Fluency and confidence are not evidence of accuracy. In this case: Fabrication measures claims unsupported by evidence, which fluency does not detect.
- **C:** Incorrect for this question. Relevance covers both retrieval and response usefulness. A correct but off-topic answer still fails. Why the correct answer wins: Fabrication measures claims unsupported by evidence, which fluency does not detect.
- **D:** Incorrect for this question. Tone analysis supports brand and customer communication. Context and culture affect interpretation. Why the correct answer wins: Fabrication measures claims unsupported by evidence, which fluency does not detect.

### Question 20 — A

Answer: Define narrow tool schemas with clear descriptions. A precise, narrow tool schema helps the model choose and populate arguments correctly. Precise schemas help the model choose tools and arguments correctly. Broad or ambiguous tools invite unsafe calls. Local study-map skill 2.4 (Agent Roles, Goals, and Tool Schemas), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Precise schemas help the model choose tools and arguments correctly. Broad or ambiguous tools invite unsafe calls. In this case: A precise, narrow tool schema helps the model choose and populate arguments correctly.
- **B:** Incorrect for this question. System messages define role and constraints. They are not a security boundary against injection. Why the correct answer wins: A precise, narrow tool schema helps the model choose and populate arguments correctly.
- **C:** Incorrect for this question. Templates improve consistency and reviewability. Version them and test changes. Why the correct answer wins: A precise, narrow tool schema helps the model choose and populate arguments correctly.
- **D:** Incorrect for this question. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Why the correct answer wins: A precise, narrow tool schema helps the model choose and populate arguments correctly.

### Question 21 — C

Answer: Put stable behavior rules in the system message. The system message carries persistent behavioral guidance, though it is not an authorization control. System messages define role and constraints. They are not a security boundary against injection. Local study-map skill 2.4 (Agent Roles, Goals, and Tool Schemas), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Filters assign severity and can block or annotate content. Thresholds should reflect the use case and applicable policy. Why the correct answer wins: The system message carries persistent behavioral guidance, though it is not an authorization control.
- **B:** Incorrect for this question. Guardrails are technical controls, not prompt suggestions. Validate inputs, authorize tools, and limit egress. Why the correct answer wins: The system message carries persistent behavioral guidance, though it is not an authorization control.
- **C:** Correct. System messages define role and constraints. They are not a security boundary against injection. In this case: The system message carries persistent behavioral guidance, though it is not an authorization control.
- **D:** Incorrect for this question. Roles should match the operations the app or agent performs. Broad contributor access increases blast radius. Why the correct answer wins: The system message carries persistent behavioral guidance, though it is not an authorization control.

### Question 22 — D

Answer: Expose an OpenAPI operation as an agent tool. An OpenAPI tool reuses the published contract without hand-written function wrappers. OpenAPI tools describe supported HTTP operations for agent use. Narrow operations, validate inputs, and authenticate the caller. Local study-map skill 2.5 (Agent Tools, Retrieval, Memory, and Function Calling), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. Why the correct answer wins: An OpenAPI tool reuses the published contract without hand-written function wrappers.
- **B:** Incorrect for this question. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Why the correct answer wins: An OpenAPI tool reuses the published contract without hand-written function wrappers.
- **C:** Incorrect for this question. RAG supplies selected source content at request time so answers can cite current evidence. It reduces but does not eliminate fabrication. Why the correct answer wins: An OpenAPI tool reuses the published contract without hand-written function wrappers.
- **D:** Correct. OpenAPI tools describe supported HTTP operations for agent use. Narrow operations, validate inputs, and authenticate the caller. In this case: An OpenAPI tool reuses the published contract without hand-written function wrappers.

### Question 23 — D, E

Answers: Persist conversation history in a thread or session; Expose a typed function as an agent tool. Conversation state preserves the referral number, and a function tool performs the lookup. Threads support continuity across turns. Apply retention and access controls to stored history. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. Local study-map skill 2.5 (Agent Tools, Retrieval, Memory, and Function Calling), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Embeddings determine semantic similarity behavior. Evaluate retrieval quality before and after changes. Why the correct answer wins: Conversation state preserves the referral number, and a function tool performs the lookup.
- **B:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Conversation state preserves the referral number, and a function tool performs the lookup.
- **C:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: Conversation state preserves the referral number, and a function tool performs the lookup.
- **D:** Correct. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. In this case: Conversation state preserves the referral number, and a function tool performs the lookup.
- **E:** Correct. Threads support continuity across turns. Apply retention and access controls to stored history. In this case: Conversation state preserves the referral number, and a function tool performs the lookup.

### Question 24 — B

Answer: Define role and goal → configure tools → attach knowledge → evaluate in sandbox → deploy with monitoring. The role is defined first, tools and knowledge follow, and evaluation precedes deployment. An agent is defined before it is connected to tools and knowledge, and evaluation precedes deployment. Local study-map skill 2.6 (Multi-Agent Orchestration and Safeguards), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Deployment before the agent is defined, connected, or evaluated removes every control. Why the correct answer wins: The role is defined first, tools and knowledge follow, and evaluation precedes deployment.
- **B:** Correct. An agent is defined before it is connected to tools and knowledge, and evaluation precedes deployment. In this case: The role is defined first, tools and knowledge follow, and evaluation precedes deployment.
- **C:** Incorrect for this question. Tools configured before the role exists, and evaluation after deployment gates nothing. Why the correct answer wins: The role is defined first, tools and knowledge follow, and evaluation precedes deployment.
- **D:** Incorrect for this question. The agent must be defined first, and evaluation must precede deployment. Why the correct answer wins: The role is defined first, tools and knowledge follow, and evaluation precedes deployment.

### Question 25 — A

Answer: Transfer control between agents with explicit context. Handoff transfers control and context to the specialist agent. Handoffs should carry goal, evidence, permissions, and open questions. Implicit context is easily lost. Local study-map skill 2.6 (Multi-Agent Orchestration and Safeguards), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Handoffs should carry goal, evidence, permissions, and open questions. Implicit context is easily lost. In this case: Handoff transfers control and context to the specialist agent.
- **B:** Incorrect for this question. Reflection can catch omissions and inconsistencies. It can also reinforce errors, so validate against evidence. Why the correct answer wins: Handoff transfers control and context to the specialist agent.
- **C:** Incorrect for this question. Parallel execution reduces wall-clock time for independent work. Reconciliation still requires design. Why the correct answer wins: Handoff transfers control and context to the specialist agent.
- **D:** Incorrect for this question. Sequential orchestration makes dependencies explicit. It may add latency where steps could run concurrently. Why the correct answer wins: Handoff transfers control and context to the specialist agent.

### Question 26 — C

Answer: Enable tracing across agent, model, and tool calls. Distributed tracing shows each model and tool call in order. Traces localize failures and latency in multi-step workflows. Correlate them with evaluation results and deployment versions. Local study-map skill 2.7 (Agent Monitoring and Error Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Distributed tracing shows each model and tool call in order.
- **B:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Distributed tracing shows each model and tool call in order.
- **C:** Correct. Traces localize failures and latency in multi-step workflows. Correlate them with evaluation results and deployment versions. In this case: Distributed tracing shows each model and tool call in order.
- **D:** Incorrect for this question. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. Why the correct answer wins: Distributed tracing shows each model and tool call in order.

### Question 27 — B

Answer: Lower temperature for more deterministic extraction. Lower temperature reduces sampling variability for deterministic extraction. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Local study-map skill 2.8 (Generation Tuning and Observability), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Top-p narrows or broadens token sampling. Tune with evaluation rather than by intuition. Why the correct answer wins: Lower temperature reduces sampling variability for deterministic extraction.
- **B:** Correct. Lower temperature reduces sampling variability. It does not guarantee factual correctness. In this case: Lower temperature reduces sampling variability for deterministic extraction.
- **C:** Incorrect for this question. Routing can balance quality and cost. Fallback and evaluation are required. Why the correct answer wins: Lower temperature reduces sampling variability for deterministic extraction.
- **D:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Lower temperature reduces sampling variability for deterministic extraction.

### Question 28 — B

Answer: Apply prompt-driven image modifications. Targeted image editing removes the badge while leaving the rest of the photo intact. Prompt-based edits can alter style or content. Review outputs for unintended changes and policy violations. Local study-map skill 3.1 (Image Generation and Editing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Why the correct answer wins: Targeted image editing removes the badge while leaving the rest of the photo intact.
- **B:** Correct. Prompt-based edits can alter style or content. Review outputs for unintended changes and policy violations. In this case: Targeted image editing removes the badge while leaving the rest of the photo intact.
- **C:** Incorrect for this question. Inpainting changes a selected area while preserving the rest. Validate identity, brand, and safety constraints. Why the correct answer wins: Targeted image editing removes the badge while leaving the rest of the photo intact.
- **D:** Incorrect for this question. Video generation creates clips from prompts or images. Duration, consistency, and safety require review. Why the correct answer wins: Targeted image editing removes the badge while leaving the rest of the photo intact.

### Question 29 — C

Answer: Generate images from text and reference media. Image generation produces a new illustration from a description. Image generation supports creative and product workflows. Apply policy, watermarking, and provenance controls. Local study-map skill 3.1 (Image Generation and Editing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Video generation creates clips from prompts or images. Duration, consistency, and safety require review. Why the correct answer wins: Image generation produces a new illustration from a description.
- **B:** Incorrect for this question. Alt text should convey purpose and essential content, not decorative detail. Human review is still needed for critical pages. Why the correct answer wins: Image generation produces a new illustration from a description.
- **C:** Correct. Image generation supports creative and product workflows. Apply policy, watermarking, and provenance controls. In this case: Image generation produces a new illustration from a description.
- **D:** Incorrect for this question. Inpainting changes a selected area while preserving the rest. Validate identity, brand, and safety constraints. Why the correct answer wins: Image generation produces a new illustration from a description.

### Question 30 — B

Answer: Analyze video segments for events and content. Video analysis locates events and timestamps within recorded footage. Video analysis can summarize or detect events across time. Sampling strategy affects coverage and cost. Local study-map skill 3.2 (Video Generation and Editing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Video editing can revise scenes or timing. Preserve provenance and review for harmful manipulation. Why the correct answer wins: Video analysis locates events and timestamps within recorded footage.
- **B:** Correct. Video analysis can summarize or detect events across time. Sampling strategy affects coverage and cost. In this case: Video analysis locates events and timestamps within recorded footage.
- **C:** Incorrect for this question. Prompt-based edits can alter style or content. Review outputs for unintended changes and policy violations. Why the correct answer wins: Video analysis locates events and timestamps within recorded footage.
- **D:** Incorrect for this question. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Why the correct answer wins: Video analysis locates events and timestamps within recorded footage.

### Question 31 — B, E

Answers: Generate alt text aligned to accessibility guidance; Answer questions grounded in visual evidence. Alt text serves accessibility, and visual question answering grounds answers in the chart content. Alt text should convey purpose and essential content, not decorative detail. Human review is still needed for critical pages. Visual question answering should cite the relevant region or content. Avoid answering beyond what the image supports. Local study-map skill 3.3 (Multimodal Understanding and Accessibility), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Alt text serves accessibility, and visual question answering grounds answers in the chart content.
- **B:** Correct. Alt text should convey purpose and essential content, not decorative detail. Human review is still needed for critical pages. In this case: Alt text serves accessibility, and visual question answering grounds answers in the chart content.
- **C:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: Alt text serves accessibility, and visual question answering grounds answers in the chart content.
- **D:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Alt text serves accessibility, and visual question answering grounds answers in the chart content.
- **E:** Correct. Visual question answering should cite the relevant region or content. Avoid answering beyond what the image supports. In this case: Alt text serves accessibility, and visual question answering grounds answers in the chart content.

### Question 32 — C

Answer: Generate concise or detailed image captions. A caption produces a concise natural-language description. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Local study-map skill 3.3 (Multimodal Understanding and Accessibility), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Detection returns locations and labels for visual elements. Validate classes and thresholds against the use case. Why the correct answer wins: A caption produces a concise natural-language description.
- **B:** Incorrect for this question. Typed fields feed downstream systems directly. Add validation and confidence thresholds before automated action. Why the correct answer wins: A caption produces a concise natural-language description.
- **C:** Correct. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. In this case: A caption produces a concise natural-language description.
- **D:** Incorrect for this question. OCR unlocks text in scans and screenshots. Layout and table structure may still require specialized extraction. Why the correct answer wins: A caption produces a concise natural-language description.

### Question 33 — B

Answer: Upload image → validate format and size → send multimodal request → parse structured fields → route low-confidence values to review. Validation brackets the multimodal call, and low-confidence output goes to people. Validation and structured parsing bracket the multimodal call, and low-confidence output goes to people. Local study-map skill 3.4 (Visual Extraction and Video Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Parsing requires a response, which requires an uploaded and validated image. Why the correct answer wins: Validation brackets the multimodal call, and low-confidence output goes to people.
- **B:** Correct. Validation and structured parsing bracket the multimodal call, and low-confidence output goes to people. In this case: Validation brackets the multimodal call, and low-confidence output goes to people.
- **C:** Incorrect for this question. A request cannot precede the upload, and validation must come before the call. Why the correct answer wins: Validation brackets the multimodal call, and low-confidence output goes to people.
- **D:** Incorrect for this question. Review cannot precede the request, and parsing must follow the response. Why the correct answer wins: Validation brackets the multimodal call, and low-confidence output goes to people.

### Question 34 — D

Answer: Filter unsafe or disallowed visual content. A visual safety filter blocks or flags unsafe generated imagery. Image and video safety filters reduce exposure to harmful content. Thresholds and human escalation should match policy. Local study-map skill 3.5 (Multimodal Responsible AI), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Brand controls define permitted logos, styles, and claims. Technical generation must still pass approval. Why the correct answer wins: A visual safety filter blocks or flags unsafe generated imagery.
- **B:** Incorrect for this question. Visible instructions in images can attempt to manipulate an agent. Isolate, detect, and never let image text grant authority. Why the correct answer wins: A visual safety filter blocks or flags unsafe generated imagery.
- **C:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: A visual safety filter blocks or flags unsafe generated imagery.
- **D:** Correct. Image and video safety filters reduce exposure to harmful content. Thresholds and human escalation should match policy. In this case: A visual safety filter blocks or flags unsafe generated imagery.

### Question 35 — A

Answer: Prompt for JSON that conforms to a supplied schema. Schema-constrained JSON supports validation and automated record creation. Schema-guided generation improves machine readability. Validate values against source evidence and business rules. Local study-map skill 4.1 (Language Model Text Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Correct. Schema-guided generation improves machine readability. Validate values against source evidence and business rules. In this case: Schema-constrained JSON supports validation and automated record creation.
- **B:** Incorrect for this question. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Why the correct answer wins: Schema-constrained JSON supports validation and automated record creation.
- **C:** Incorrect for this question. Topic extraction supports discovery and grouping. It is not a substitute for an authoritative taxonomy. Why the correct answer wins: Schema-constrained JSON supports validation and automated record creation.
- **D:** Incorrect for this question. Translation should preserve meaning, names, and formatting. Evaluate domain terminology and low-resource languages. Why the correct answer wins: Schema-constrained JSON supports validation and automated record creation.

### Question 36 — A, E

Answers: Detect and redact sensitive personal data; Analyze sentiment and tone with an appropriate service. PII detection addresses disclosure risk, and sentiment surfaces frustration. Sensitive Data Protection or language PII detection can identify and mask data. Verify that redaction covers every path where content flows. Sentiment analysis can support triage and monitoring. Domain and language variation require validation. Local study-map skill 4.1 (Language Model Text Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Correct. Sentiment analysis can support triage and monitoring. Domain and language variation require validation. In this case: PII detection addresses disclosure risk, and sentiment surfaces frustration.
- **B:** Incorrect for this question. Topic extraction supports discovery and grouping. It is not a substitute for an authoritative taxonomy. Why the correct answer wins: PII detection addresses disclosure risk, and sentiment surfaces frustration.
- **C:** Incorrect for this question. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Why the correct answer wins: PII detection addresses disclosure risk, and sentiment surfaces frustration.
- **D:** Incorrect for this question. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Why the correct answer wins: PII detection addresses disclosure risk, and sentiment surfaces frustration.
- **E:** Correct. Sensitive Data Protection or language PII detection can identify and mask data. Verify that redaction covers every path where content flows. In this case: PII detection addresses disclosure risk, and sentiment surfaces frustration.

### Question 37 — A

Answer: Use Azure Translator or a language model for translation. Machine translation renders approved text into the target language. Translation should preserve meaning, names, and formatting. Evaluate domain terminology and low-resource languages. Local study-map skill 4.2 (Translation), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Correct. Translation should preserve meaning, names, and formatting. Evaluate domain terminology and low-resource languages. In this case: Machine translation renders approved text into the target language.
- **B:** Incorrect for this question. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Why the correct answer wins: Machine translation renders approved text into the target language.
- **C:** Incorrect for this question. Sensitive Data Protection or language PII detection can identify and mask data. Verify that redaction covers every path where content flows. Why the correct answer wins: Machine translation renders approved text into the target language.
- **D:** Incorrect for this question. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Why the correct answer wins: Machine translation renders approved text into the target language.

### Question 38 — D

Answer: Transcribe speech to text with Azure AI Speech. Speech-to-text transcribes recordings into searchable content. Speech-to-text enables voice agents and transcript analysis. Audio quality, accents, and domain terms affect accuracy. Local study-map skill 4.3 (Speech Solutions), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Why the correct answer wins: Speech-to-text transcribes recordings into searchable content.
- **B:** Incorrect for this question. Text-to-speech supports voice responses and accessibility. Voice, prosody, and latency affect usability. Why the correct answer wins: Speech-to-text transcribes recordings into searchable content.
- **C:** Incorrect for this question. Speech translation combines recognition and translation. Preserve timing and speaker context where needed. Why the correct answer wins: Speech-to-text transcribes recordings into searchable content.
- **D:** Correct. Speech-to-text enables voice agents and transcript analysis. Audio quality, accents, and domain terms affect accuracy. In this case: Speech-to-text transcribes recordings into searchable content.

### Question 39 — A

Answer: Use a custom speech model for specialized vocabulary. A custom speech model adapts acoustic and language behavior to the domain. Custom speech can improve recognition of domain terms. It requires representative audio and ongoing evaluation. Local study-map skill 4.3 (Speech Solutions), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Correct. Custom speech can improve recognition of domain terms. It requires representative audio and ongoing evaluation. In this case: A custom speech model adapts acoustic and language behavior to the domain.
- **B:** Incorrect for this question. Speech-to-text enables voice agents and transcript analysis. Audio quality, accents, and domain terms affect accuracy. Why the correct answer wins: A custom speech model adapts acoustic and language behavior to the domain.
- **C:** Incorrect for this question. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Why the correct answer wins: A custom speech model adapts acoustic and language behavior to the domain.
- **D:** Incorrect for this question. Text-to-speech supports voice responses and accessibility. Voice, prosody, and latency affect usability. Why the correct answer wins: A custom speech model adapts acoustic and language behavior to the domain.

### Question 40 — B

Answer: Adapt prompts and models to domain terminology. A validated domain lexicon teaches local terminology to the extraction step. Domain adaptation improves consistency and recall. Validate against expert-created expected outputs. Local study-map skill 4.4 (Domain Customization), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Why the correct answer wins: A validated domain lexicon teaches local terminology to the extraction step.
- **B:** Correct. Domain adaptation improves consistency and recall. Validate against expert-created expected outputs. In this case: A validated domain lexicon teaches local terminology to the extraction step.
- **C:** Incorrect for this question. Sensitive Data Protection or language PII detection can identify and mask data. Verify that redaction covers every path where content flows. Why the correct answer wins: A validated domain lexicon teaches local terminology to the extraction step.
- **D:** Incorrect for this question. Translation should preserve meaning, names, and formatting. Evaluate domain terminology and low-resource languages. Why the correct answer wins: A validated domain lexicon teaches local terminology to the extraction step.

### Question 41 — A

Answer: Use an Azure AI Search indexer to pull source content. An indexer pulls content on a schedule and tracks source changes. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. Local study-map skill 5.1 (Content Ingestion and Indexing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Correct. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. In this case: An indexer pulls content on a schedule and tracks source changes.
- **B:** Incorrect for this question. Skillsets can OCR, split, embed, and extract during indexing. Each skill adds latency, cost, and failure modes. Why the correct answer wins: An indexer pulls content on a schedule and tracks source changes.
- **C:** Incorrect for this question. OCR unlocks text in scans and screenshots. Layout and table structure may still require specialized extraction. Why the correct answer wins: An indexer pulls content on a schedule and tracks source changes.
- **D:** Incorrect for this question. Push ingestion supports near-real-time updates from applications. The app owns batching, retries, and deletion. Why the correct answer wins: An indexer pulls content on a schedule and tracks source changes.

### Question 42 — A, C

Answers: Combine keyword and vector retrieval; Apply semantic ranking to reorder search results. Hybrid search covers exact and semantic matching, and semantic ranking improves ordering. Hybrid search covers exact identifiers and paraphrased meaning together. Fusion and ranking need testing on representative queries. A semantic ranker can improve relevance for natural-language queries. It adds cost and latency and should be measured against a baseline. Local study-map skill 5.2 (Search and Grounding Configuration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Correct. Hybrid search covers exact identifiers and paraphrased meaning together. Fusion and ranking need testing on representative queries. In this case: Hybrid search covers exact and semantic matching, and semantic ranking improves ordering.
- **B:** Incorrect for this question. Embeddings support similarity search over meaning rather than exact terms. Vector search still needs chunking, filtering, and evaluation. Why the correct answer wins: Hybrid search covers exact and semantic matching, and semantic ranking improves ordering.
- **C:** Correct. A semantic ranker can improve relevance for natural-language queries. It adds cost and latency and should be measured against a baseline. In this case: Hybrid search covers exact and semantic matching, and semantic ranking improves ordering.
- **D:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Hybrid search covers exact and semantic matching, and semantic ranking improves ordering.
- **E:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Hybrid search covers exact and semantic matching, and semantic ranking improves ordering.

### Question 43 — B

Answer: Add an enrichment skillset to an indexing pipeline. An enrichment skillset applies extraction and generation steps during indexing. Skillsets can OCR, split, embed, and extract during indexing. Each skill adds latency, cost, and failure modes. Local study-map skill 5.3 (Enrichment Skills), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. Push ingestion supports near-real-time updates from applications. The app owns batching, retries, and deletion. Why the correct answer wins: An enrichment skillset applies extraction and generation steps during indexing.
- **B:** Correct. Skillsets can OCR, split, embed, and extract during indexing. Each skill adds latency, cost, and failure modes. In this case: An enrichment skillset applies extraction and generation steps during indexing.
- **C:** Incorrect for this question. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. Why the correct answer wins: An enrichment skillset applies extraction and generation steps during indexing.
- **D:** Incorrect for this question. OCR unlocks text in scans and screenshots. Layout and table structure may still require specialized extraction. Why the correct answer wins: An enrichment skillset applies extraction and generation steps during indexing.

### Question 44 — C

Answer: Ingest → extract text → chunk → embed → index → retrieve with citations. Extraction, chunking, embedding, and indexing all precede retrieval and citation. The supported RAG ingestion order produces searchable, citable evidence. Retrieval cannot work before content is extracted, chunked, embedded, and indexed. Local study-map skill 5.4 (RAG Ingestion and OCR), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. Retrieval before chunking, embedding, and indexing has nothing searchable to return. Why the correct answer wins: Extraction, chunking, embedding, and indexing all precede retrieval and citation.
- **B:** Incorrect for this question. Retrieval is attempted before the index exists and source ingestion is incomplete. Why the correct answer wins: Extraction, chunking, embedding, and indexing all precede retrieval and citation.
- **C:** Correct. The supported RAG ingestion order produces searchable, citable evidence. Retrieval cannot work before content is extracted, chunked, embedded, and indexed. In this case: Extraction, chunking, embedding, and indexing all precede retrieval and citation.
- **D:** Incorrect for this question. Indexing before extraction or embedding creates an empty or unusable index. Why the correct answer wins: Extraction, chunking, embedding, and indexing all precede retrieval and citation.

### Question 45 — D

Answer: Apply a custom glossary or terminology list. A glossary enforces approved terminology across languages. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Local study-map skill 4.2 (Translation), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Topic extraction supports discovery and grouping. It is not a substitute for an authoritative taxonomy. Why the correct answer wins: A glossary enforces approved terminology across languages.
- **B:** Incorrect for this question. Sentiment analysis can support triage and monitoring. Domain and language variation require validation. Why the correct answer wins: A glossary enforces approved terminology across languages.
- **C:** Incorrect for this question. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Why the correct answer wins: A glossary enforces approved terminology across languages.
- **D:** Correct. Glossaries keep product and legal terms consistent. Terms still need human validation in context. In this case: A glossary enforces approved terminology across languages.

### Question 46 — A

Answer: Use a prebuilt document model for common document types. A prebuilt document model fits common, stable document types without custom training. Prebuilt models cover invoices, receipts, IDs, and similar formats. Check supported locales and field coverage. Local study-map skill 5.6 (Document and Content Extraction), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Correct. Prebuilt models cover invoices, receipts, IDs, and similar formats. Check supported locales and field coverage. In this case: A prebuilt document model fits common, stable document types without custom training.
- **B:** Incorrect for this question. Document Intelligence provides prebuilt and custom extraction for structured documents. Validate field accuracy on representative samples. Why the correct answer wins: A prebuilt document model fits common, stable document types without custom training.
- **C:** Incorrect for this question. Analyzers define what to extract and how to return it. Version and test them like application code. Why the correct answer wins: A prebuilt document model fits common, stable document types without custom training.
- **D:** Incorrect for this question. Custom models fit specialized forms not covered by prebuilts. They require representative labels and retraining discipline. Why the correct answer wins: A prebuilt document model fits common, stable document types without custom training.

### Question 47 — D

Answer: Use field-level confidence to route exceptions. Field-level confidence thresholds send uncertain values to human review. Low-confidence fields should be reviewed rather than accepted. Thresholds depend on downstream impact. Local study-map skill 5.6 (Document and Content Extraction), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Why the correct answer wins: Field-level confidence thresholds send uncertain values to human review.
- **B:** Incorrect for this question. Relevance covers both retrieval and response usefulness. A correct but off-topic answer still fails. Why the correct answer wins: Field-level confidence thresholds send uncertain values to human review.
- **C:** Incorrect for this question. Sentiment analysis can support triage and monitoring. Domain and language variation require validation. Why the correct answer wins: Field-level confidence thresholds send uncertain values to human review.
- **D:** Correct. Low-confidence fields should be reviewed rather than accepted. Thresholds depend on downstream impact. In this case: Field-level confidence thresholds send uncertain values to human review.

### Question 48 — D

Answer: Monitor groundedness and citation quality in production. Groundedness monitoring detects statements unsupported by retrieved clinical evidence. Groundedness checks whether claims are supported by retrieved evidence. Sampling and human review complement automated scores. Local study-map skill 1.5 (Monitoring Performance, Drift, Safety, and Grounding), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Retries, tool calls, evaluation, and review contribute to unit economics. Per-outcome cost supports better optimization. Why the correct answer wins: Groundedness monitoring detects statements unsupported by retrieved clinical evidence.
- **B:** Incorrect for this question. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. Why the correct answer wins: Groundedness monitoring detects statements unsupported by retrieved clinical evidence.
- **C:** Incorrect for this question. Users experience the whole path, not only generation. Optimize the dominant contributor. Why the correct answer wins: Groundedness monitoring detects statements unsupported by retrieved clinical evidence.
- **D:** Correct. Groundedness checks whether claims are supported by retrieved evidence. Sampling and human review complement automated scores. In this case: Groundedness monitoring detects statements unsupported by retrieved clinical evidence.

### Question 49 — D

Answer: Expose a typed function as an agent tool. A function tool calls the scheduling system under application authorization. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. Local study-map skill 2.5 (Agent Tools, Retrieval, Memory, and Function Calling), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. OpenAPI tools describe supported HTTP operations for agent use. Narrow operations, validate inputs, and authenticate the caller. Why the correct answer wins: A function tool calls the scheduling system under application authorization.
- **B:** Incorrect for this question. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Why the correct answer wins: A function tool calls the scheduling system under application authorization.
- **C:** Incorrect for this question. RAG supplies selected source content at request time so answers can cite current evidence. It reduces but does not eliminate fabrication. Why the correct answer wins: A function tool calls the scheduling system under application authorization.
- **D:** Correct. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. In this case: A function tool calls the scheduling system under application authorization.

### Question 50 — D

Answer: Use a manager agent to coordinate specialists. A manager agent routes the request to specialists and consolidates their replies. A manager routes tasks and merges results. Clear responsibility and failure handling are required. Local study-map skill 2.6 (Multi-Agent Orchestration and Safeguards), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Sequential orchestration makes dependencies explicit. It may add latency where steps could run concurrently. Why the correct answer wins: A manager agent routes the request to specialists and consolidates their replies.
- **B:** Incorrect for this question. Connected agents let one agent delegate to another. Authorization and result validation remain necessary. Why the correct answer wins: A manager agent routes the request to specialists and consolidates their replies.
- **C:** Incorrect for this question. Parallel execution reduces wall-clock time for independent work. Reconciliation still requires design. Why the correct answer wins: A manager agent routes the request to specialists and consolidates their replies.
- **D:** Correct. A manager routes tasks and merges results. Clear responsibility and failure handling are required. In this case: A manager agent routes the request to specialists and consolidates their replies.
