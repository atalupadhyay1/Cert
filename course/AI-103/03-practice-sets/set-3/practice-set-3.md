# Microsoft AI-103 — Full-Length Mock Exam 3

Azure AI Apps and Agents Developer Associate · 50 questions · 120 minutes · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 38 single-choice, 8 multi-select (selection count stated), 4 ordering items rendered as answer choices, and 2 case studies of 3 questions. Hot-area, drag-and-drop UI, labs, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. A bank must pin a model version that stays available in its primary and secondary regions. What should the team review before selection?

Domain: Plan and manage an Azure AI solution

- A. Compare supported models in the Foundry model catalog
- B. Train or deploy a task-specific model outside the prebuilt catalog
- C. Use a general-purpose large language model for complex reasoning
- D. Use a small language model for a narrow, high-volume task

### 2. A risk team needs a model tuned only on its own historical filings, with the weights kept inside the organization's control. Which option applies?

Domain: Plan and manage an Azure AI solution

- A. Use a small language model for a narrow, high-volume task
- B. Train or deploy a task-specific model outside the prebuilt catalog
- C. Use a multimodal model for combined text, image, or audio input
- D. Use a general-purpose large language model for complex reasoning

### 3. An assistant must return the regulatory circulars most similar in meaning to a complaint narrative. Which service performs that match?

Domain: Plan and manage an Azure AI solution

- A. Expose a typed function as an agent tool
- B. Use managed conversation state or memory for continuity
- C. Use a vector index for semantic retrieval
- D. Connect an Azure AI Search index as agent knowledge

### 4. A trading-support workload needs repeatable deployments and no public data-plane exposure. Which two actions should you take? Select two.

Domain: Plan and manage an Azure AI solution

- A. Use private endpoints and disable public network access
- B. Plan for model quota expressed in tokens and requests per minute
- C. Manage AI resources with infrastructure as code and CI/CD
- D. Use provisioned throughput for predictable high-volume workloads
- E. Use supported prompt or response caching where appropriate

### 5. A team must score two million historic claims overnight at minimum cost with no interactive latency requirement. Which deployment option fits?

Domain: Plan and manage an Azure AI solution

- A. Use a standard pay-as-you-go model deployment for variable demand
- B. Use batch processing for latency-tolerant bulk work
- C. Use provisioned throughput for predictable high-volume workloads
- D. Plan for model quota expressed in tokens and requests per minute

### 6. A payments assistant has steady, round-the-clock volume and cannot tolerate throttling. Which capacity option should be evaluated?

Domain: Plan and manage an Azure AI solution

- A. Use provisioned throughput for predictable high-volume workloads
- B. Use batch processing for latency-tolerant bulk work
- C. Use supported prompt or response caching where appropriate
- D. Use a standard pay-as-you-go model deployment for variable demand

### 7. Finance needs spend broken down by deployment, prompt size, and completion size. What should be enabled?

Domain: Plan and manage an Azure AI solution

- A. Track cost per accepted task, not only per token
- B. Monitor input and quality drift over time
- C. Plan for model quota expressed in tokens and requests per minute
- D. Track prompt, completion, and cached token usage

### 8. An on-call team must be paged when model latency breaches its service objective. What should be configured?

Domain: Plan and manage an Azure AI solution

- A. Preserve audit logs of changes, approvals, and tool actions
- B. Use Azure Monitor and Application Insights for telemetry
- C. Monitor input and quality drift over time
- D. Alert on latency, error rate, safety, and cost thresholds

### 9. A new model version must not silently break cases that previously failed. What should be run before promotion?

Domain: Plan and manage an Azure AI solution

- A. Compare variants with controlled traffic and shared metrics
- B. Re-run evaluation suites after meaningful changes
- C. Use evaluators for quality, safety, and groundedness
- D. Build a representative golden dataset from real tasks

### 10. A third-party connector secret must be rotated on a schedule and never stored in code. What should hold it?

Domain: Plan and manage an Azure AI solution

- A. Authenticate with a managed identity instead of keys
- B. Store secrets in Azure Key Vault when keys are unavoidable
- C. Use private endpoints and disable public network access
- D. Use least-privilege Azure RBAC roles for the workload identity

### 11. Security requires that the AI service cannot call unapproved external endpoints. What should be restricted?

Domain: Plan and manage an Azure AI solution

- A. Restrict outbound network access to approved destinations
- B. Private DNS resolution configured for the endpoint
- C. Use private endpoints and disable public network access
- D. Private networking with public access left enabled

### 12. Before launch, a team must actively probe the agent for jailbreaks and data-exfiltration prompts. What activity is this?

Domain: Plan and manage an Azure AI solution

- A. Preserve audit logs of changes, approvals, and tool actions
- B. Set agent oversight mode and tool-access constraints
- C. Enforce constraints in code and platform policy
- D. Test the solution with adversarial and boundary cases

### 13. A credit-decision assistant must block harmful content and keep a human accountable for outcomes. Which two controls are required? Select two.

Domain: Plan and manage an Azure AI solution

- A. Use supported prompt or response caching where appropriate
- B. Set agent oversight mode and tool-access constraints
- C. Lower temperature for more deterministic extraction
- D. Configure content safety filters for harmful categories
- E. Adjust top-p to control response diversity

### 14. Simple balance lookups must go to a cheap model while complex disputes use a stronger model. Which pattern fits?

Domain: Implement generative AI and agentic solutions

- A. Include representative examples in the prompt
- B. Route requests to different models by task difficulty
- C. Ground responses with retrieval-augmented generation
- D. Use a versioned prompt template with explicit variables

### 15. A model keeps mislabelling dispute categories despite clear instructions. What should be added to the prompt?

Domain: Implement generative AI and agentic solutions

- A. Include representative examples in the prompt
- B. Use a versioned prompt template with explicit variables
- C. Design multistep workflows with explicit checkpoints
- D. Use supported prompt or response caching where appropriate

### 16. A Java service needs supported authentication and retry behavior for Foundry calls. What should it use?

Domain: Implement generative AI and agentic solutions

- A. Use a Foundry SDK or supported connector from application code
- B. Create and run deployments by hand in the portal
- C. Manage AI resources with infrastructure as code and CI/CD
- D. Use batch processing for latency-tolerant bulk work

### 17. A browser client must call the model service using short-lived delegated credentials. What should the app issue?

Domain: Implement generative AI and agentic solutions

- A. Store secrets in Azure Key Vault when keys are unavoidable
- B. Authenticate with a managed identity instead of keys
- C. Connect the application to the Foundry project endpoint
- D. Use short-lived scoped access tokens for tool calls

### 18. A team must compare two prompt designs fairly and keep a stable benchmark over time. Which two practices are required? Select two.

Domain: Implement generative AI and agentic solutions

- A. Compare variants with controlled traffic and shared metrics
- B. Use provisioned throughput for predictable high-volume workloads
- C. Apply watermarks or provenance markers to generated media
- D. Lower temperature for more deterministic extraction
- E. Build a representative golden dataset from real tasks

### 19. A regulator asks for evidence that the assistant refuses prohibited financial advice. Which evaluation applies?

Domain: Implement generative AI and agentic solutions

- A. Evaluate structure and logical consistency of responses
- B. Detect tone and sentiment appropriate to the audience
- C. Measure whether retrieved content and answers address the question
- D. Evaluate harmful, biased, or policy-violating output

### 20. An agent passes an unvalidated account number to a payment tool. What should be tightened first?

Domain: Implement generative AI and agentic solutions

- A. Put stable behavior rules in the system message
- B. Use a versioned prompt template with explicit variables
- C. Define narrow tool schemas with clear descriptions
- D. Use managed conversation state or memory for continuity

### 21. Which sequence correctly describes a governed tool call from a claims agent?

Domain: Implement generative AI and agentic solutions

- A. App authorizes → model executes tool → result returns → app validates → model responds
- B. Model responds → app authorizes → tool executes → result returns → app validates
- C. Model executes tool → app validates → tool returns result → app authorizes → model responds
- D. Model requests tool → app validates and authorizes → tool executes → result returns → model responds

### 22. A claims agent must keep a claim number across turns and check its status in a core system. Which two capabilities are required? Select two.

Domain: Implement generative AI and agentic solutions

- A. Choose an embedding model suited to the content and language
- B. Persist conversation history in a thread or session
- C. Apply watermarks or provenance markers to generated media
- D. Use provisioned throughput for predictable high-volume workloads
- E. Expose a typed function as an agent tool

### 23. Three independent checks must run at the same time and be merged into one decision. Which pattern fits?

Domain: Implement generative AI and agentic solutions

- A. Transfer control between agents with explicit context
- B. Run independent agents concurrently
- C. Run agents in a fixed sequence
- D. Use self-critique or reflection to improve drafts

### 24. An agent must critique and improve its own draft before returning it. Which pattern applies?

Domain: Implement generative AI and agentic solutions

- A. Run independent agents concurrently
- B. Transfer control between agents with explicit context
- C. Use self-critique or reflection to improve drafts
- D. Run agents in a fixed sequence

### 25. Which sequence correctly handles a production alert about failing agent responses?

Domain: Implement generative AI and agentic solutions

- A. Detect alert → inspect traces → isolate the failing step → apply fix → verify with regression evaluation
- B. Verify with regression evaluation → apply fix → detect alert → isolate the failing step → inspect traces
- C. Isolate the failing step → apply fix → detect alert → verify with regression evaluation → inspect traces
- D. Apply fix → detect alert → inspect traces → isolate the failing step → verify with regression evaluation

### 26. Outputs become repetitive and omit valid alternative phrasings. Which sampling parameter should be adjusted?

Domain: Implement generative AI and agentic solutions

- A. Measure whether retrieved content and answers address the question
- B. Evaluate structure and logical consistency of responses
- C. Use supported prompt or response caching where appropriate
- D. Adjust top-p to control response diversity

### 27. The same lengthy compliance preamble is sent with every request and dominates cost. What should be enabled?

Domain: Implement generative AI and agentic solutions

- A. Require citations tied to retrieved evidence
- B. Apply watermarks or provenance markers to generated media
- C. Use Azure Monitor and Application Insights for telemetry
- D. Use supported prompt or response caching where appropriate

### 28. A marketing photo shows an outdated card design that must be replaced while the model stays untouched. What should be used?

Domain: Implement computer vision solutions

- A. Generate concise or detailed image captions
- B. Edit a region of an image with a mask
- C. Generate video from text or reference media
- D. Apply prompt-driven image modifications

### 29. An insurer needs a short original animation explaining a claims process. Which capability applies?

Domain: Implement computer vision solutions

- A. Edit generated video segments
- B. Generate video from text or reference media
- C. Generate concise or detailed image captions
- D. Apply prompt-driven image modifications

### 30. A generated demo clip must be trimmed and its burned-in caption corrected. What capability applies?

Domain: Implement computer vision solutions

- A. Analyze video segments for events and content
- B. Edit generated video segments
- C. Apply prompt-driven image modifications
- D. Edit a region of an image with a mask

### 31. A statements portal needs short image descriptions for search and screen readers. Which two capabilities apply? Select two.

Domain: Implement computer vision solutions

- A. Generate concise or detailed image captions
- B. Use provisioned throughput for predictable high-volume workloads
- C. Lower temperature for more deterministic extraction
- D. Generate alt text aligned to accessibility guidance
- E. Apply watermarks or provenance markers to generated media

### 32. A back-office job reads one field from thousands of uniform, machine-printed forms. Which Content Understanding mode is most cost-effective?

Domain: Implement computer vision solutions

- A. Use single-task mode for a focused extraction scenario
- B. Train a custom extraction model on labeled documents
- C. Use Azure AI Document Intelligence for forms and documents
- D. Use pro mode for complex multimodal content understanding

### 33. A scanned table's columns are scrambled into meaningless text. What should be applied?

Domain: Implement computer vision solutions

- A. Produce markdown representations for downstream reasoning
- B. Preserve reading order across columns and sections
- C. Apply OCR to convert images and scans into usable text
- D. Preserve document layout, tables, and reading order

### 34. Generated marketing imagery must be identifiable as synthetic and must follow brand rules. Which two controls apply? Select two.

Domain: Implement computer vision solutions

- A. Enforce brand and usage rules for generated visuals
- B. Apply watermarks or provenance markers to generated media
- C. Adjust top-p to control response diversity
- D. Use supported prompt or response caching where appropriate
- E. Lower temperature for more deterministic extraction

### 35. Analysts need a two-paragraph digest of a 40-page complaint file. Which task applies?

Domain: Implement text analysis solutions

- A. Extract entities with defined types and boundaries
- B. Identify topics or key phrases for navigation
- C. Generate summaries with explicit length and audience constraints
- D. Use Azure Translator or a language model for translation

### 36. A contact-centre team needs automatic tagging of complaint subjects and detection of anger. Which two analyses apply? Select two.

Domain: Implement text analysis solutions

- A. Apply watermarks or provenance markers to generated media
- B. Generate alt text aligned to accessibility guidance
- C. Generate concise or detailed image captions
- D. Identify topics or key phrases for navigation
- E. Analyze sentiment and tone with an appropriate service

### 37. Product names and legal phrases are inconsistently translated across notices. What should be configured?

Domain: Implement text analysis solutions

- A. Use Azure Translator or a language model for translation
- B. Detect and redact sensitive personal data
- C. Apply a custom glossary or terminology list
- D. Extract entities with defined types and boundaries

### 38. A policyholder speaks only Spanish and must receive an English explanation by phone. Which sequence is correct?

Domain: Implement text analysis solutions

- A. Capture audio → synthesize speech → transcribe → translate → return audio
- B. Transcribe → synthesize speech → capture audio → translate → return audio
- C. Capture audio → transcribe → translate text → synthesize speech → return audio
- D. Translate audio → transcribe → capture audio → synthesize → return audio

### 39. Summaries for regulators must preserve citations and mandatory disclosures. Which approach fits?

Domain: Implement text analysis solutions

- A. Extract entities with defined types and boundaries
- B. Generate summaries with explicit length and audience constraints
- C. Customize summaries and extraction for compliance needs
- D. Identify topics or key phrases for navigation

### 40. A customer closes an account and must disappear from search results immediately. What must be implemented?

Domain: Implement information extraction solutions

- A. Push documents to an index through the data-plane API
- B. Use an Azure AI Search indexer to pull source content
- C. Propagate source deletions to indexes and caches
- D. Ingest content through supported indexers or APIs

### 41. Staff search by exact policy number and by described coverage, and each region sees only its own circulars. Which two features are required? Select two.

Domain: Implement information extraction solutions

- A. Verify index freshness and deletion propagation
- B. Combine keyword and vector retrieval
- C. Apply document-level security filters at query time
- D. Apply semantic ranking to reorder search results
- E. Select evidence within the model's usable context

### 42. An indexing pipeline must add extracted entities and written summaries to every document during ingestion. Which component defines those steps?

Domain: Implement information extraction solutions

- A. Add an enrichment skillset to an indexing pipeline
- B. Apply OCR to convert images and scans into usable text
- C. Push documents to an index through the data-plane API
- D. Use supported prompt or response caching where appropriate

### 43. Which sequence correctly builds a citable retrieval pipeline over regulatory documents?

Domain: Implement information extraction solutions

- A. Ingest → extract text → chunk → embed → index → retrieve with citations
- B. Ingest → retrieve → chunk → embed → index → cite
- C. Chunk → embed → ingest → retrieve → index → cite
- D. Index → retrieve → ingest → chunk → embed → cite

### 44. Retrieved evidence crowds out the instructions, and the model starts ignoring the question. What should be configured?

Domain: Implement information extraction solutions

- A. Use a vector index for semantic retrieval
- B. Select evidence within the model's usable context
- C. Remove near-duplicate evidence before ranking
- D. Rerank retrieved passages before generation

---

## Case study — FraudDesk

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 45. Investigators in two regions must not see each other's case notes. Which control enforces that separation?

Domain: Plan and manage an Azure AI solution

- A. Use least-privilege Azure RBAC roles for the workload identity
- B. Store secrets in Azure Key Vault when keys are unavoidable
- C. Apply document-level security filters at query time
- D. Restrict outbound network access to approved destinations

### 46. The team needs comparable groundedness scores for two retrieval configurations. What should they run?

Domain: Implement generative AI and agentic solutions

- A. Preserve audit logs of changes, approvals, and tool actions
- B. Use evaluators for quality, safety, and groundedness
- C. Use Azure Monitor and Application Insights for telemetry
- D. Alert on latency, error rate, safety, and cost thresholds

### 47. A request fails only after the second tool call. What should be inspected first?

Domain: Implement generative AI and agentic solutions

- A. Enable tracing across agent, model, and tool calls
- B. Use supported prompt or response caching where appropriate
- C. Lower temperature for more deterministic extraction
- D. Apply watermarks or provenance markers to generated media

---

## Case study — LoanDocs

The next three questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 48. Applicants may request that decision letters be read aloud over the phone. Which capability applies?

Domain: Implement text analysis solutions

- A. Use a custom speech model for specialized vocabulary
- B. Transcribe speech to text with Azure AI Speech
- C. Synthesize speech with Azure AI Speech
- D. Use a multimodal model to reason over audio content

### 49. Scanned letters use regional abbreviations that the extraction prompt ignores. What should be added?

Domain: Implement text analysis solutions

- A. Detect and redact sensitive personal data
- B. Use Azure Translator or a language model for translation
- C. Adapt prompts and models to domain terminology
- D. Apply a custom glossary or terminology list

### 50. A lender receives its own proprietary application form with no standard equivalent. What should be built?

Domain: Implement information extraction solutions

- A. Configure a Content Understanding analyzer for the content type
- B. Train a custom extraction model on labeled documents
- C. Use a prebuilt document model for common document types
- D. Use single-task mode for a focused extraction scenario

---

## Answer key and explanations

### Question 1 — A

Answer: Compare supported models in the Foundry model catalog. The model catalog shows regional availability and version lifecycle commitments. The catalog shows supported models with capability, modality, region, and lifecycle details. Verify availability for your subscription and region before designing around one model. Local study-map skill 1.1 (Selecting Foundry Models and Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. The catalog shows supported models with capability, modality, region, and lifecycle details. Verify availability for your subscription and region before designing around one model. In this case: The model catalog shows regional availability and version lifecycle commitments.
- **B:** Incorrect for this question. A custom model is justified when supported prebuilt options cannot meet a defined requirement. It adds data, evaluation, and lifecycle obligations. Why the correct answer wins: The model catalog shows regional availability and version lifecycle commitments.
- **C:** Incorrect for this question. Large models handle ambiguity and multi-step reasoning better in many cases, at higher cost and latency. Select with measured evidence rather than brand preference. Why the correct answer wins: The model catalog shows regional availability and version lifecycle commitments.
- **D:** Incorrect for this question. Small models can reduce latency and cost for constrained classification or extraction. Confirm quality on representative data before standardizing. Why the correct answer wins: The model catalog shows regional availability and version lifecycle commitments.

### Question 2 — B

Answer: Train or deploy a task-specific model outside the prebuilt catalog. A custom or fine-tuned model is trained on organization-specific data under its governance. A custom model is justified when supported prebuilt options cannot meet a defined requirement. It adds data, evaluation, and lifecycle obligations. Local study-map skill 1.1 (Selecting Foundry Models and Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Small models can reduce latency and cost for constrained classification or extraction. Confirm quality on representative data before standardizing. Why the correct answer wins: A custom or fine-tuned model is trained on organization-specific data under its governance.
- **B:** Correct. A custom model is justified when supported prebuilt options cannot meet a defined requirement. It adds data, evaluation, and lifecycle obligations. In this case: A custom or fine-tuned model is trained on organization-specific data under its governance.
- **C:** Incorrect for this question. Multimodal models accept more than one content type in a request. Validate extraction and grounding quality for each modality used. Why the correct answer wins: A custom or fine-tuned model is trained on organization-specific data under its governance.
- **D:** Incorrect for this question. Large models handle ambiguity and multi-step reasoning better in many cases, at higher cost and latency. Select with measured evidence rather than brand preference. Why the correct answer wins: A custom or fine-tuned model is trained on organization-specific data under its governance.

### Question 3 — C

Answer: Use a vector index for semantic retrieval. A vector index compares embeddings and returns semantically similar content. Embeddings support similarity search over meaning rather than exact terms. Vector search still needs chunking, filtering, and evaluation. Local study-map skill 1.2 (Retrieval, Memory, Tool, and Knowledge Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. Why the correct answer wins: A vector index compares embeddings and returns semantically similar content.
- **B:** Incorrect for this question. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Why the correct answer wins: A vector index compares embeddings and returns semantically similar content.
- **C:** Correct. Embeddings support similarity search over meaning rather than exact terms. Vector search still needs chunking, filtering, and evaluation. In this case: A vector index compares embeddings and returns semantically similar content.
- **D:** Incorrect for this question. An index gives an agent curated, searchable evidence under configured access. Index content and permissions require ongoing ownership. Why the correct answer wins: A vector index compares embeddings and returns semantically similar content.

### Question 4 — A, C

Answers: Manage AI resources with infrastructure as code and CI/CD; Use private endpoints and disable public network access. Infrastructure as code provides repeatability, and private endpoints remove public exposure. Repeatable deployments reduce configuration drift. Include model deployments, indexes, and connections in review and promotion. Private connectivity keeps service traffic on approved network paths. Pair it with private DNS so clients resolve the private address. Local study-map skill 1.3 (Infrastructure, Deployment, and CI/CD), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. Private connectivity keeps service traffic on approved network paths. Pair it with private DNS so clients resolve the private address. In this case: Infrastructure as code provides repeatability, and private endpoints remove public exposure.
- **B:** Incorrect for this question. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. Why the correct answer wins: Infrastructure as code provides repeatability, and private endpoints remove public exposure.
- **C:** Correct. Repeatable deployments reduce configuration drift. Include model deployments, indexes, and connections in review and promotion. In this case: Infrastructure as code provides repeatability, and private endpoints remove public exposure.
- **D:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: Infrastructure as code provides repeatability, and private endpoints remove public exposure.
- **E:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Infrastructure as code provides repeatability, and private endpoints remove public exposure.

### Question 5 — B

Answer: Use batch processing for latency-tolerant bulk work. Batch deployment suits large asynchronous jobs that tolerate delay. Batch deployments can lower cost for large asynchronous jobs. They are unsuitable for interactive agent turns. Local study-map skill 1.3 (Infrastructure, Deployment, and CI/CD), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Standard deployments bill per token and scale within quota. They suit spiky or early workloads. Why the correct answer wins: Batch deployment suits large asynchronous jobs that tolerate delay.
- **B:** Correct. Batch deployments can lower cost for large asynchronous jobs. They are unsuitable for interactive agent turns. In this case: Batch deployment suits large asynchronous jobs that tolerate delay.
- **C:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: Batch deployment suits large asynchronous jobs that tolerate delay.
- **D:** Incorrect for this question. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. Why the correct answer wins: Batch deployment suits large asynchronous jobs that tolerate delay.

### Question 6 — A

Answer: Use provisioned throughput for predictable high-volume workloads. Provisioned throughput reserves capacity for predictable continuous demand. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Local study-map skill 1.4 (Quotas, Scaling, and Cost), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. In this case: Provisioned throughput reserves capacity for predictable continuous demand.
- **B:** Incorrect for this question. Batch deployments can lower cost for large asynchronous jobs. They are unsuitable for interactive agent turns. Why the correct answer wins: Provisioned throughput reserves capacity for predictable continuous demand.
- **C:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Provisioned throughput reserves capacity for predictable continuous demand.
- **D:** Incorrect for this question. Standard deployments bill per token and scale within quota. They suit spiky or early workloads. Why the correct answer wins: Provisioned throughput reserves capacity for predictable continuous demand.

### Question 7 — D

Answer: Track prompt, completion, and cached token usage. Token analytics attributes consumption so cost can be optimized per workload. Token analytics supports cost and performance tuning. Attribute usage to features and tenants where possible. Local study-map skill 1.4 (Quotas, Scaling, and Cost), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Retries, tool calls, evaluation, and review contribute to unit economics. Per-outcome cost supports better optimization. Why the correct answer wins: Token analytics attributes consumption so cost can be optimized per workload.
- **B:** Incorrect for this question. User behavior, data, and models change. Rolling baselines reveal degradation that a one-time evaluation misses. Why the correct answer wins: Token analytics attributes consumption so cost can be optimized per workload.
- **C:** Incorrect for this question. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. Why the correct answer wins: Token analytics attributes consumption so cost can be optimized per workload.
- **D:** Correct. Token analytics supports cost and performance tuning. Attribute usage to features and tenants where possible. In this case: Token analytics attributes consumption so cost can be optimized per workload.

### Question 8 — D

Answer: Alert on latency, error rate, safety, and cost thresholds. Alert rules trigger notifications when a monitored metric crosses a threshold. Alerts turn monitoring into action. Route them to an accountable owner with a runbook. Local study-map skill 1.5 (Monitoring Performance, Drift, Safety, and Grounding), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Audit evidence supports investigation and accountability. Protect log integrity and retention. Why the correct answer wins: Alert rules trigger notifications when a monitored metric crosses a threshold.
- **B:** Incorrect for this question. Central telemetry captures latency, errors, dependencies, and custom events. Redact sensitive content before logging. Why the correct answer wins: Alert rules trigger notifications when a monitored metric crosses a threshold.
- **C:** Incorrect for this question. User behavior, data, and models change. Rolling baselines reveal degradation that a one-time evaluation misses. Why the correct answer wins: Alert rules trigger notifications when a monitored metric crosses a threshold.
- **D:** Correct. Alerts turn monitoring into action. Route them to an accountable owner with a runbook. In this case: Alert rules trigger notifications when a monitored metric crosses a threshold.

### Question 9 — B

Answer: Re-run evaluation suites after meaningful changes. Regression evaluation re-runs known failure cases against the candidate version. Prompts, models, indexes, and tools all affect behavior. Regression tests catch unintended effects. Local study-map skill 1.5 (Monitoring Performance, Drift, Safety, and Grounding), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Controlled comparison supports evidence-based change. Avoid changing several variables at once. Why the correct answer wins: Regression evaluation re-runs known failure cases against the candidate version.
- **B:** Correct. Prompts, models, indexes, and tools all affect behavior. Regression tests catch unintended effects. In this case: Regression evaluation re-runs known failure cases against the candidate version.
- **C:** Incorrect for this question. Evaluators provide repeatable signals across models and prompts. They must be calibrated against human judgment for high-impact work. Why the correct answer wins: Regression evaluation re-runs known failure cases against the candidate version.
- **D:** Incorrect for this question. A golden set anchors evaluation in expected behavior. Include edge cases and high-risk scenarios. Why the correct answer wins: Regression evaluation re-runs known failure cases against the candidate version.

### Question 10 — B

Answer: Store secrets in Azure Key Vault when keys are unavoidable. A key vault stores and rotates secrets under access policy and audit. A managed secret store supports rotation and access control. Secrets should never appear in prompts, code, or logs. Local study-map skill 1.6 (Security, Identity, and Networking), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Managed identities avoid embedded secrets and support role-based access. Assign only required data-plane roles. Why the correct answer wins: A key vault stores and rotates secrets under access policy and audit.
- **B:** Correct. A managed secret store supports rotation and access control. Secrets should never appear in prompts, code, or logs. In this case: A key vault stores and rotates secrets under access policy and audit.
- **C:** Incorrect for this question. Private connectivity keeps service traffic on approved network paths. Pair it with private DNS so clients resolve the private address. Why the correct answer wins: A key vault stores and rotates secrets under access policy and audit.
- **D:** Incorrect for this question. Roles should match the operations the app or agent performs. Broad contributor access increases blast radius. Why the correct answer wins: A key vault stores and rotates secrets under access policy and audit.

### Question 11 — A

Answer: Restrict outbound network access to approved destinations. Egress controls limit outbound destinations from the workload. Egress controls reduce exfiltration and unauthorized tool reach. Combine with identity and data controls. Local study-map skill 1.6 (Security, Identity, and Networking), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. Egress controls reduce exfiltration and unauthorized tool reach. Combine with identity and data controls. In this case: Egress controls limit outbound destinations from the workload.
- **B:** Incorrect for this question. Name resolution alone does not block public access, so it must be paired with a private endpoint and public access disabled. Why the correct answer wins: Egress controls limit outbound destinations from the workload.
- **C:** Incorrect for this question. Private connectivity keeps service traffic on approved network paths. Pair it with private DNS so clients resolve the private address. Why the correct answer wins: Egress controls limit outbound destinations from the workload.
- **D:** Incorrect for this question. Leaving the public path open defeats the purpose of a private networking design because traffic can still bypass the private route. Why the correct answer wins: Egress controls limit outbound destinations from the workload.

### Question 12 — D

Answer: Test the solution with adversarial and boundary cases. Red teaming deliberately attacks the system to find safety weaknesses before users do. Red-team cases expose prompt injection, data leakage, and unsafe tool use. Findings should become regression tests. Local study-map skill 1.7 (Responsible AI Controls and Oversight), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Audit evidence supports investigation and accountability. Protect log integrity and retention. Why the correct answer wins: Red teaming deliberately attacks the system to find safety weaknesses before users do.
- **B:** Incorrect for this question. Oversight settings bound what an agent may do autonomously. They should be tested against realistic misuse and failure. Why the correct answer wins: Red teaming deliberately attacks the system to find safety weaknesses before users do.
- **C:** Incorrect for this question. Guardrails are technical controls, not prompt suggestions. Validate inputs, authorize tools, and limit egress. Why the correct answer wins: Red teaming deliberately attacks the system to find safety weaknesses before users do.
- **D:** Correct. Red-team cases expose prompt injection, data leakage, and unsafe tool use. Findings should become regression tests. In this case: Red teaming deliberately attacks the system to find safety weaknesses before users do.

### Question 13 — B, D

Answers: Configure content safety filters for harmful categories; Set agent oversight mode and tool-access constraints. Content filters reduce harmful output, and human oversight keeps decisions attributable. Filters assign severity and can block or annotate content. Thresholds should reflect the use case and applicable policy. Oversight settings bound what an agent may do autonomously. They should be tested against realistic misuse and failure. Local study-map skill 1.7 (Responsible AI Controls and Oversight), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Content filters reduce harmful output, and human oversight keeps decisions attributable.
- **B:** Correct. Oversight settings bound what an agent may do autonomously. They should be tested against realistic misuse and failure. In this case: Content filters reduce harmful output, and human oversight keeps decisions attributable.
- **C:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Content filters reduce harmful output, and human oversight keeps decisions attributable.
- **D:** Correct. Filters assign severity and can block or annotate content. Thresholds should reflect the use case and applicable policy. In this case: Content filters reduce harmful output, and human oversight keeps decisions attributable.
- **E:** Incorrect for this question. Top-p narrows or broadens token sampling. Tune with evaluation rather than by intuition. Why the correct answer wins: Content filters reduce harmful output, and human oversight keeps decisions attributable.

### Question 14 — B

Answer: Route requests to different models by task difficulty. A router sends each request to the appropriate model by complexity and cost. Routing can balance quality and cost. Fallback and evaluation are required. Local study-map skill 2.1 (Building Generative Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Examples clarify format and boundaries. They do not guarantee correctness on unseen inputs. Why the correct answer wins: A router sends each request to the appropriate model by complexity and cost.
- **B:** Correct. Routing can balance quality and cost. Fallback and evaluation are required. In this case: A router sends each request to the appropriate model by complexity and cost.
- **C:** Incorrect for this question. RAG supplies selected source content at request time so answers can cite current evidence. It reduces but does not eliminate fabrication. Why the correct answer wins: A router sends each request to the appropriate model by complexity and cost.
- **D:** Incorrect for this question. Templates improve consistency and reviewability. Version them and test changes. Why the correct answer wins: A router sends each request to the appropriate model by complexity and cost.

### Question 15 — A

Answer: Include representative examples in the prompt. A few labeled examples show the model the expected categorization pattern. Examples clarify format and boundaries. They do not guarantee correctness on unseen inputs. Local study-map skill 2.1 (Building Generative Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Examples clarify format and boundaries. They do not guarantee correctness on unseen inputs. In this case: A few labeled examples show the model the expected categorization pattern.
- **B:** Incorrect for this question. Templates improve consistency and reviewability. Version them and test changes. Why the correct answer wins: A few labeled examples show the model the expected categorization pattern.
- **C:** Incorrect for this question. Checkpoints validate intermediate results before later steps depend on them. This limits error propagation. Why the correct answer wins: A few labeled examples show the model the expected categorization pattern.
- **D:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: A few labeled examples show the model the expected categorization pattern.

### Question 16 — A

Answer: Use a Foundry SDK or supported connector from application code. A supported Foundry SDK provides maintained client behavior rather than raw HTTP calls. SDKs provide supported request and response patterns. Pin versions and handle retries, timeouts, and errors explicitly. Local study-map skill 2.2 (Foundry SDK and Project Integration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. SDKs provide supported request and response patterns. Pin versions and handle retries, timeouts, and errors explicitly. In this case: A supported Foundry SDK provides maintained client behavior rather than raw HTTP calls.
- **B:** Incorrect for this question. Manual portal changes work for exploration but are slow, undocumented, and hard to reproduce, so they are a poor fit for governed release processes. Why the correct answer wins: A supported Foundry SDK provides maintained client behavior rather than raw HTTP calls.
- **C:** Incorrect for this question. Repeatable deployments reduce configuration drift. Include model deployments, indexes, and connections in review and promotion. Why the correct answer wins: A supported Foundry SDK provides maintained client behavior rather than raw HTTP calls.
- **D:** Incorrect for this question. Batch deployments can lower cost for large asynchronous jobs. They are unsuitable for interactive agent turns. Why the correct answer wins: A supported Foundry SDK provides maintained client behavior rather than raw HTTP calls.

### Question 17 — D

Answer: Use short-lived scoped access tokens for tool calls. A short-lived access token scopes the browser session without embedding long-term secrets. Short-lived credentials reduce misuse risk. Never place tokens in prompts or logs. Local study-map skill 2.2 (Foundry SDK and Project Integration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. A managed secret store supports rotation and access control. Secrets should never appear in prompts, code, or logs. Why the correct answer wins: A short-lived access token scopes the browser session without embedding long-term secrets.
- **B:** Incorrect for this question. Managed identities avoid embedded secrets and support role-based access. Assign only required data-plane roles. Why the correct answer wins: A short-lived access token scopes the browser session without embedding long-term secrets.
- **C:** Incorrect for this question. Project endpoints and SDK clients bind an app to approved models and resources. Use identity-based authentication and environment-specific configuration. Why the correct answer wins: A short-lived access token scopes the browser session without embedding long-term secrets.
- **D:** Correct. Short-lived credentials reduce misuse risk. Never place tokens in prompts or logs. In this case: A short-lived access token scopes the browser session without embedding long-term secrets.

### Question 18 — A, E

Answers: Build a representative golden dataset from real tasks; Compare variants with controlled traffic and shared metrics. A golden dataset provides a stable benchmark, and an A/B test compares variants on it. A golden set anchors evaluation in expected behavior. Include edge cases and high-risk scenarios. Controlled comparison supports evidence-based change. Avoid changing several variables at once. Local study-map skill 2.3 (Evaluating Models and Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Controlled comparison supports evidence-based change. Avoid changing several variables at once. In this case: A golden dataset provides a stable benchmark, and an A/B test compares variants on it.
- **B:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: A golden dataset provides a stable benchmark, and an A/B test compares variants on it.
- **C:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: A golden dataset provides a stable benchmark, and an A/B test compares variants on it.
- **D:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: A golden dataset provides a stable benchmark, and an A/B test compares variants on it.
- **E:** Correct. A golden set anchors evaluation in expected behavior. Include edge cases and high-risk scenarios. In this case: A golden dataset provides a stable benchmark, and an A/B test compares variants on it.

### Question 19 — D

Answer: Evaluate harmful, biased, or policy-violating output. Safety evaluation measures harmful or prohibited responses against defined criteria. Safety evaluation complements content filters. Use representative adversarial inputs. Local study-map skill 2.3 (Evaluating Models and Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Coherence checks readability and internal consistency. It does not establish factual accuracy. Why the correct answer wins: Safety evaluation measures harmful or prohibited responses against defined criteria.
- **B:** Incorrect for this question. Tone analysis supports brand and customer communication. Context and culture affect interpretation. Why the correct answer wins: Safety evaluation measures harmful or prohibited responses against defined criteria.
- **C:** Incorrect for this question. Relevance covers both retrieval and response usefulness. A correct but off-topic answer still fails. Why the correct answer wins: Safety evaluation measures harmful or prohibited responses against defined criteria.
- **D:** Correct. Safety evaluation complements content filters. Use representative adversarial inputs. In this case: Safety evaluation measures harmful or prohibited responses against defined criteria.

### Question 20 — C

Answer: Define narrow tool schemas with clear descriptions. A strict tool schema with typed parameters prevents malformed or ambiguous arguments. Precise schemas help the model choose tools and arguments correctly. Broad or ambiguous tools invite unsafe calls. Local study-map skill 2.4 (Agent Roles, Goals, and Tool Schemas), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. System messages define role and constraints. They are not a security boundary against injection. Why the correct answer wins: A strict tool schema with typed parameters prevents malformed or ambiguous arguments.
- **B:** Incorrect for this question. Templates improve consistency and reviewability. Version them and test changes. Why the correct answer wins: A strict tool schema with typed parameters prevents malformed or ambiguous arguments.
- **C:** Correct. Precise schemas help the model choose tools and arguments correctly. Broad or ambiguous tools invite unsafe calls. In this case: A strict tool schema with typed parameters prevents malformed or ambiguous arguments.
- **D:** Incorrect for this question. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Why the correct answer wins: A strict tool schema with typed parameters prevents malformed or ambiguous arguments.

### Question 21 — D

Answer: Model requests tool → app validates and authorizes → tool executes → result returns → model responds. The application validates and authorizes the call before any tool executes. Tool execution authority belongs to the application, which validates and authorizes before acting. Local study-map skill 2.5 (Agent Tools, Retrieval, Memory, and Function Calling), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Execution must follow validation, and the model is not the execution boundary. Why the correct answer wins: The application validates and authorizes the call before any tool executes.
- **B:** Incorrect for this question. The response cannot precede the tool action and validation. Why the correct answer wins: The application validates and authorizes the call before any tool executes.
- **C:** Incorrect for this question. The model cannot execute the tool, and authorization after execution is too late. Why the correct answer wins: The application validates and authorizes the call before any tool executes.
- **D:** Correct. Tool execution authority belongs to the application, which validates and authorizes before acting. In this case: The application validates and authorizes the call before any tool executes.

### Question 22 — B, E

Answers: Persist conversation history in a thread or session; Expose a typed function as an agent tool. Conversation state preserves the claim number, and a function tool performs the lookup. Threads support continuity across turns. Apply retention and access controls to stored history. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. Local study-map skill 2.5 (Agent Tools, Retrieval, Memory, and Function Calling), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Embeddings determine semantic similarity behavior. Evaluate retrieval quality before and after changes. Why the correct answer wins: Conversation state preserves the claim number, and a function tool performs the lookup.
- **B:** Correct. Threads support continuity across turns. Apply retention and access controls to stored history. In this case: Conversation state preserves the claim number, and a function tool performs the lookup.
- **C:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Conversation state preserves the claim number, and a function tool performs the lookup.
- **D:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: Conversation state preserves the claim number, and a function tool performs the lookup.
- **E:** Correct. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. In this case: Conversation state preserves the claim number, and a function tool performs the lookup.

### Question 23 — B

Answer: Run independent agents concurrently. A parallel agent pattern runs independent work concurrently and combines the results. Parallel execution reduces wall-clock time for independent work. Reconciliation still requires design. Local study-map skill 2.6 (Multi-Agent Orchestration and Safeguards), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Handoffs should carry goal, evidence, permissions, and open questions. Implicit context is easily lost. Why the correct answer wins: A parallel agent pattern runs independent work concurrently and combines the results.
- **B:** Correct. Parallel execution reduces wall-clock time for independent work. Reconciliation still requires design. In this case: A parallel agent pattern runs independent work concurrently and combines the results.
- **C:** Incorrect for this question. Sequential orchestration makes dependencies explicit. It may add latency where steps could run concurrently. Why the correct answer wins: A parallel agent pattern runs independent work concurrently and combines the results.
- **D:** Incorrect for this question. Reflection can catch omissions and inconsistencies. It can also reinforce errors, so validate against evidence. Why the correct answer wins: A parallel agent pattern runs independent work concurrently and combines the results.

### Question 24 — C

Answer: Use self-critique or reflection to improve drafts. Reflection adds a self-review step that revises the draft before delivery. Reflection can catch omissions and inconsistencies. It can also reinforce errors, so validate against evidence. Local study-map skill 2.6 (Multi-Agent Orchestration and Safeguards), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Parallel execution reduces wall-clock time for independent work. Reconciliation still requires design. Why the correct answer wins: Reflection adds a self-review step that revises the draft before delivery.
- **B:** Incorrect for this question. Handoffs should carry goal, evidence, permissions, and open questions. Implicit context is easily lost. Why the correct answer wins: Reflection adds a self-review step that revises the draft before delivery.
- **C:** Correct. Reflection can catch omissions and inconsistencies. It can also reinforce errors, so validate against evidence. In this case: Reflection adds a self-review step that revises the draft before delivery.
- **D:** Incorrect for this question. Sequential orchestration makes dependencies explicit. It may add latency where steps could run concurrently. Why the correct answer wins: Reflection adds a self-review step that revises the draft before delivery.

### Question 25 — A

Answer: Detect alert → inspect traces → isolate the failing step → apply fix → verify with regression evaluation. Triage moves from the alert to traces, then a targeted fix verified by regression evaluation. Triage moves from signal to evidence to a targeted fix, then proves the fix with regression tests. Local study-map skill 2.7 (Agent Monitoring and Error Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Triage moves from signal to evidence to a targeted fix, then proves the fix with regression tests. In this case: Triage moves from the alert to traces, then a targeted fix verified by regression evaluation.
- **B:** Incorrect for this question. Verification before a fix and before diagnosis proves nothing. Why the correct answer wins: Triage moves from the alert to traces, then a targeted fix verified by regression evaluation.
- **C:** Incorrect for this question. The alert must be detected first, and traces must be inspected before the step is isolated. Why the correct answer wins: Triage moves from the alert to traces, then a targeted fix verified by regression evaluation.
- **D:** Incorrect for this question. A fix cannot precede detection and diagnosis. Why the correct answer wins: Triage moves from the alert to traces, then a targeted fix verified by regression evaluation.

### Question 26 — D

Answer: Adjust top-p to control response diversity. Nucleus sampling controls diversity by limiting the cumulative probability considered. Top-p narrows or broadens token sampling. Tune with evaluation rather than by intuition. Local study-map skill 2.8 (Generation Tuning and Observability), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Relevance covers both retrieval and response usefulness. A correct but off-topic answer still fails. Why the correct answer wins: Nucleus sampling controls diversity by limiting the cumulative probability considered.
- **B:** Incorrect for this question. Coherence checks readability and internal consistency. It does not establish factual accuracy. Why the correct answer wins: Nucleus sampling controls diversity by limiting the cumulative probability considered.
- **C:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Nucleus sampling controls diversity by limiting the cumulative probability considered.
- **D:** Correct. Top-p narrows or broadens token sampling. Tune with evaluation rather than by intuition. In this case: Nucleus sampling controls diversity by limiting the cumulative probability considered.

### Question 27 — D

Answer: Use supported prompt or response caching where appropriate. Prompt caching reuses repeated prefix content instead of reprocessing it. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Local study-map skill 2.8 (Generation Tuning and Observability), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Citations let users verify claims and support auditing. Preserve source and chunk identifiers through the pipeline. Why the correct answer wins: Prompt caching reuses repeated prefix content instead of reprocessing it.
- **B:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Prompt caching reuses repeated prefix content instead of reprocessing it.
- **C:** Incorrect for this question. Central telemetry captures latency, errors, dependencies, and custom events. Redact sensitive content before logging. Why the correct answer wins: Prompt caching reuses repeated prefix content instead of reprocessing it.
- **D:** Correct. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. In this case: Prompt caching reuses repeated prefix content instead of reprocessing it.

### Question 28 — D

Answer: Apply prompt-driven image modifications. Targeted image editing changes the selected element and preserves the subject. Prompt-based edits can alter style or content. Review outputs for unintended changes and policy violations. Local study-map skill 3.1 (Image Generation and Editing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Why the correct answer wins: Targeted image editing changes the selected element and preserves the subject.
- **B:** Incorrect for this question. Inpainting changes a selected area while preserving the rest. Validate identity, brand, and safety constraints. Why the correct answer wins: Targeted image editing changes the selected element and preserves the subject.
- **C:** Incorrect for this question. Video generation creates clips from prompts or images. Duration, consistency, and safety require review. Why the correct answer wins: Targeted image editing changes the selected element and preserves the subject.
- **D:** Correct. Prompt-based edits can alter style or content. Review outputs for unintended changes and policy violations. In this case: Targeted image editing changes the selected element and preserves the subject.

### Question 29 — B

Answer: Generate video from text or reference media. Video generation creates new footage from a description. Video generation creates clips from prompts or images. Duration, consistency, and safety require review. Local study-map skill 3.2 (Video Generation and Editing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Video editing can revise scenes or timing. Preserve provenance and review for harmful manipulation. Why the correct answer wins: Video generation creates new footage from a description.
- **B:** Correct. Video generation creates clips from prompts or images. Duration, consistency, and safety require review. In this case: Video generation creates new footage from a description.
- **C:** Incorrect for this question. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Why the correct answer wins: Video generation creates new footage from a description.
- **D:** Incorrect for this question. Prompt-based edits can alter style or content. Review outputs for unintended changes and policy violations. Why the correct answer wins: Video generation creates new footage from a description.

### Question 30 — B

Answer: Edit generated video segments. Video editing changes existing generated segments and captions. Video editing can revise scenes or timing. Preserve provenance and review for harmful manipulation. Local study-map skill 3.2 (Video Generation and Editing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Video analysis can summarize or detect events across time. Sampling strategy affects coverage and cost. Why the correct answer wins: Video editing changes existing generated segments and captions.
- **B:** Correct. Video editing can revise scenes or timing. Preserve provenance and review for harmful manipulation. In this case: Video editing changes existing generated segments and captions.
- **C:** Incorrect for this question. Prompt-based edits can alter style or content. Review outputs for unintended changes and policy violations. Why the correct answer wins: Video editing changes existing generated segments and captions.
- **D:** Incorrect for this question. Inpainting changes a selected area while preserving the rest. Validate identity, brand, and safety constraints. Why the correct answer wins: Video editing changes existing generated segments and captions.

### Question 31 — A, D

Answers: Generate concise or detailed image captions; Generate alt text aligned to accessibility guidance. Captions describe content for search, and alt text serves assistive technology. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Alt text should convey purpose and essential content, not decorative detail. Human review is still needed for critical pages. Local study-map skill 3.3 (Multimodal Understanding and Accessibility), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Correct. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. In this case: Captions describe content for search, and alt text serves assistive technology.
- **B:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: Captions describe content for search, and alt text serves assistive technology.
- **C:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Captions describe content for search, and alt text serves assistive technology.
- **D:** Correct. Alt text should convey purpose and essential content, not decorative detail. Human review is still needed for critical pages. In this case: Captions describe content for search, and alt text serves assistive technology.
- **E:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Captions describe content for search, and alt text serves assistive technology.

### Question 32 — A

Answer: Use single-task mode for a focused extraction scenario. The single-task mode targets a focused extraction at lower cost than full pro mode. Single-task analyzers target one content type or objective. They may be simpler and cheaper than general pro-mode pipelines. Local study-map skill 3.4 (Visual Extraction and Video Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Correct. Single-task analyzers target one content type or objective. They may be simpler and cheaper than general pro-mode pipelines. In this case: The single-task mode targets a focused extraction at lower cost than full pro mode.
- **B:** Incorrect for this question. Custom models fit specialized forms not covered by prebuilts. They require representative labels and retraining discipline. Why the correct answer wins: The single-task mode targets a focused extraction at lower cost than full pro mode.
- **C:** Incorrect for this question. Document Intelligence provides prebuilt and custom extraction for structured documents. Validate field accuracy on representative samples. Why the correct answer wins: The single-task mode targets a focused extraction at lower cost than full pro mode.
- **D:** Incorrect for this question. Pro mode handles more demanding layouts and multimodal inputs at higher cost. Use it where simpler modes fail requirements. Why the correct answer wins: The single-task mode targets a focused extraction at lower cost than full pro mode.

### Question 33 — D

Answer: Preserve document layout, tables, and reading order. Layout analysis preserves table cells and relationships that plain OCR flattens. Layout awareness improves extraction from forms and multi-column documents. Flattening to plain text can destroy meaning. Local study-map skill 3.4 (Visual Extraction and Video Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Markdown preserves headings, tables, and lists in a model-friendly form. Validate that critical values survive conversion. Why the correct answer wins: Layout analysis preserves table cells and relationships that plain OCR flattens.
- **B:** Incorrect for this question. Reading order affects comprehension and extraction. Incorrect order can invert meaning in contracts and forms. Why the correct answer wins: Layout analysis preserves table cells and relationships that plain OCR flattens.
- **C:** Incorrect for this question. OCR unlocks text in scans and screenshots. Layout and table structure may still require specialized extraction. Why the correct answer wins: Layout analysis preserves table cells and relationships that plain OCR flattens.
- **D:** Correct. Layout awareness improves extraction from forms and multi-column documents. Flattening to plain text can destroy meaning. In this case: Layout analysis preserves table cells and relationships that plain OCR flattens.

### Question 34 — A, B

Answers: Enforce brand and usage rules for generated visuals; Apply watermarks or provenance markers to generated media. Watermarking identifies synthetic media, and brand policy constrains approved visual usage. Brand controls define permitted logos, styles, and claims. Technical generation must still pass approval. Watermarks support disclosure and traceability. They do not replace usage policy or review. Local study-map skill 3.5 (Multimodal Responsible AI), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Correct. Brand controls define permitted logos, styles, and claims. Technical generation must still pass approval. In this case: Watermarking identifies synthetic media, and brand policy constrains approved visual usage.
- **B:** Correct. Watermarks support disclosure and traceability. They do not replace usage policy or review. In this case: Watermarking identifies synthetic media, and brand policy constrains approved visual usage.
- **C:** Incorrect for this question. Top-p narrows or broadens token sampling. Tune with evaluation rather than by intuition. Why the correct answer wins: Watermarking identifies synthetic media, and brand policy constrains approved visual usage.
- **D:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Watermarking identifies synthetic media, and brand policy constrains approved visual usage.
- **E:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Watermarking identifies synthetic media, and brand policy constrains approved visual usage.

### Question 35 — C

Answer: Generate summaries with explicit length and audience constraints. Summarization condenses long content into a shorter form. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Local study-map skill 4.1 (Language Model Text Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Entity extraction turns text into structured facts. Ambiguous mentions need resolution and validation. Why the correct answer wins: Summarization condenses long content into a shorter form.
- **B:** Incorrect for this question. Topic extraction supports discovery and grouping. It is not a substitute for an authoritative taxonomy. Why the correct answer wins: Summarization condenses long content into a shorter form.
- **C:** Correct. Summaries should preserve required facts and caveats. Fluency does not prove completeness. In this case: Summarization condenses long content into a shorter form.
- **D:** Incorrect for this question. Translation should preserve meaning, names, and formatting. Evaluate domain terminology and low-resource languages. Why the correct answer wins: Summarization condenses long content into a shorter form.

### Question 36 — D, E

Answers: Analyze sentiment and tone with an appropriate service; Identify topics or key phrases for navigation. Topic detection tags subjects, and sentiment detects emotional escalation. Sentiment analysis can support triage and monitoring. Domain and language variation require validation. Topic extraction supports discovery and grouping. It is not a substitute for an authoritative taxonomy. Local study-map skill 4.1 (Language Model Text Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Topic detection tags subjects, and sentiment detects emotional escalation.
- **B:** Incorrect for this question. Alt text should convey purpose and essential content, not decorative detail. Human review is still needed for critical pages. Why the correct answer wins: Topic detection tags subjects, and sentiment detects emotional escalation.
- **C:** Incorrect for this question. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Why the correct answer wins: Topic detection tags subjects, and sentiment detects emotional escalation.
- **D:** Correct. Topic extraction supports discovery and grouping. It is not a substitute for an authoritative taxonomy. In this case: Topic detection tags subjects, and sentiment detects emotional escalation.
- **E:** Correct. Sentiment analysis can support triage and monitoring. Domain and language variation require validation. In this case: Topic detection tags subjects, and sentiment detects emotional escalation.

### Question 37 — C

Answer: Apply a custom glossary or terminology list. A glossary enforces approved term mappings across languages. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Local study-map skill 4.2 (Translation), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Translation should preserve meaning, names, and formatting. Evaluate domain terminology and low-resource languages. Why the correct answer wins: A glossary enforces approved term mappings across languages.
- **B:** Incorrect for this question. Sensitive Data Protection or language PII detection can identify and mask data. Verify that redaction covers every path where content flows. Why the correct answer wins: A glossary enforces approved term mappings across languages.
- **C:** Correct. Glossaries keep product and legal terms consistent. Terms still need human validation in context. In this case: A glossary enforces approved term mappings across languages.
- **D:** Incorrect for this question. Entity extraction turns text into structured facts. Ambiguous mentions need resolution and validation. Why the correct answer wins: A glossary enforces approved term mappings across languages.

### Question 38 — C

Answer: Capture audio → transcribe → translate text → synthesize speech → return audio. Speech translation transcribes, translates the text, then synthesizes the target-language reply. Speech translation transcribes first, translates the text, then synthesizes the target-language audio. Local study-map skill 4.3 (Speech Solutions), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Synthesis cannot precede transcription and translation. Why the correct answer wins: Speech translation transcribes, translates the text, then synthesizes the target-language reply.
- **B:** Incorrect for this question. Capture must come first, and synthesis must follow translation. Why the correct answer wins: Speech translation transcribes, translates the text, then synthesizes the target-language reply.
- **C:** Correct. Speech translation transcribes first, translates the text, then synthesizes the target-language audio. In this case: Speech translation transcribes, translates the text, then synthesizes the target-language reply.
- **D:** Incorrect for this question. Audio must be captured before it can be transcribed or translated. Why the correct answer wins: Speech translation transcribes, translates the text, then synthesizes the target-language reply.

### Question 39 — C

Answer: Customize summaries and extraction for compliance needs. Domain-specific compliance summarization enforces citation and disclosure requirements. Compliance work requires precise citation, retention, and review. Generic summarization is insufficient without controls. Local study-map skill 4.4 (Domain Customization), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Entity extraction turns text into structured facts. Ambiguous mentions need resolution and validation. Why the correct answer wins: Domain-specific compliance summarization enforces citation and disclosure requirements.
- **B:** Incorrect for this question. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Why the correct answer wins: Domain-specific compliance summarization enforces citation and disclosure requirements.
- **C:** Correct. Compliance work requires precise citation, retention, and review. Generic summarization is insufficient without controls. In this case: Domain-specific compliance summarization enforces citation and disclosure requirements.
- **D:** Incorrect for this question. Topic extraction supports discovery and grouping. It is not a substitute for an authoritative taxonomy. Why the correct answer wins: Domain-specific compliance summarization enforces citation and disclosure requirements.

### Question 40 — C

Answer: Propagate source deletions to indexes and caches. Deletion propagation removes withdrawn documents from the index. Removed content must stop appearing in answers. Test deletion propagation explicitly. Local study-map skill 5.1 (Content Ingestion and Indexing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. Push ingestion supports near-real-time updates from applications. The app owns batching, retries, and deletion. Why the correct answer wins: Deletion propagation removes withdrawn documents from the index.
- **B:** Incorrect for this question. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. Why the correct answer wins: Deletion propagation removes withdrawn documents from the index.
- **C:** Correct. Removed content must stop appearing in answers. Test deletion propagation explicitly. In this case: Deletion propagation removes withdrawn documents from the index.
- **D:** Incorrect for this question. Ingestion moves source content into a searchable index. Handle failures, updates, and deletions explicitly. Why the correct answer wins: Deletion propagation removes withdrawn documents from the index.

### Question 41 — B, C

Answers: Apply document-level security filters at query time; Combine keyword and vector retrieval. Document-level security filters enforce regional separation, and hybrid search covers exact and semantic queries. Filters restrict results to content the user may see. They must be enforced before content reaches the model. Hybrid search covers exact identifiers and paraphrased meaning together. Fusion and ranking need testing on representative queries. Local study-map skill 5.2 (Search and Grounding Configuration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. Stale content produces outdated answers. Define refresh expectations and test deletion behavior. Why the correct answer wins: Document-level security filters enforce regional separation, and hybrid search covers exact and semantic queries.
- **B:** Correct. Hybrid search covers exact identifiers and paraphrased meaning together. Fusion and ranking need testing on representative queries. In this case: Document-level security filters enforce regional separation, and hybrid search covers exact and semantic queries.
- **C:** Correct. Filters restrict results to content the user may see. They must be enforced before content reaches the model. In this case: Document-level security filters enforce regional separation, and hybrid search covers exact and semantic queries.
- **D:** Incorrect for this question. A semantic ranker can improve relevance for natural-language queries. It adds cost and latency and should be measured against a baseline. Why the correct answer wins: Document-level security filters enforce regional separation, and hybrid search covers exact and semantic queries.
- **E:** Incorrect for this question. More retrieved text is not always better. Order and compress evidence to preserve decisive facts. Why the correct answer wins: Document-level security filters enforce regional separation, and hybrid search covers exact and semantic queries.

### Question 42 — A

Answer: Add an enrichment skillset to an indexing pipeline. A skillset defines the enrichment steps that run during indexing. Skillsets can OCR, split, embed, and extract during indexing. Each skill adds latency, cost, and failure modes. Local study-map skill 5.3 (Enrichment Skills), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Correct. Skillsets can OCR, split, embed, and extract during indexing. Each skill adds latency, cost, and failure modes. In this case: A skillset defines the enrichment steps that run during indexing.
- **B:** Incorrect for this question. OCR unlocks text in scans and screenshots. Layout and table structure may still require specialized extraction. Why the correct answer wins: A skillset defines the enrichment steps that run during indexing.
- **C:** Incorrect for this question. Push ingestion supports near-real-time updates from applications. The app owns batching, retries, and deletion. Why the correct answer wins: A skillset defines the enrichment steps that run during indexing.
- **D:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: A skillset defines the enrichment steps that run during indexing.

### Question 43 — A

Answer: Ingest → extract text → chunk → embed → index → retrieve with citations. Extraction, chunking, embedding, and indexing all precede retrieval and citation. The supported RAG ingestion order produces searchable, citable evidence. Retrieval cannot work before content is extracted, chunked, embedded, and indexed. Local study-map skill 5.4 (RAG Ingestion and OCR), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Correct. The supported RAG ingestion order produces searchable, citable evidence. Retrieval cannot work before content is extracted, chunked, embedded, and indexed. In this case: Extraction, chunking, embedding, and indexing all precede retrieval and citation.
- **B:** Incorrect for this question. Retrieval before chunking, embedding, and indexing has nothing searchable to return. Why the correct answer wins: Extraction, chunking, embedding, and indexing all precede retrieval and citation.
- **C:** Incorrect for this question. Retrieval is attempted before the index exists and source ingestion is incomplete. Why the correct answer wins: Extraction, chunking, embedding, and indexing all precede retrieval and citation.
- **D:** Incorrect for this question. Indexing before extraction or embedding creates an empty or unusable index. Why the correct answer wins: Extraction, chunking, embedding, and indexing all precede retrieval and citation.

### Question 44 — B

Answer: Select evidence within the model's usable context. The context budget controls how much retrieved evidence is placed in the prompt. More retrieved text is not always better. Order and compress evidence to preserve decisive facts. Local study-map skill 5.5 (Retrieval Integration with Agents), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. Embeddings support similarity search over meaning rather than exact terms. Vector search still needs chunking, filtering, and evaluation. Why the correct answer wins: The context budget controls how much retrieved evidence is placed in the prompt.
- **B:** Correct. More retrieved text is not always better. Order and compress evidence to preserve decisive facts. In this case: The context budget controls how much retrieved evidence is placed in the prompt.
- **C:** Incorrect for this question. De-duplication frees context space that duplicates would otherwise consume, so the most informative evidence survives the budget. Why the correct answer wins: The context budget controls how much retrieved evidence is placed in the prompt.
- **D:** Incorrect for this question. Reranking improves precision after broad recall. It adds latency and must be evaluated. Why the correct answer wins: The context budget controls how much retrieved evidence is placed in the prompt.

### Question 45 — A

Answer: Use least-privilege Azure RBAC roles for the workload identity. Role-based access control restricts each identity to its authorized region and data scope. Roles should match the operations the app or agent performs. Broad contributor access increases blast radius. Local study-map skill 1.6 (Security, Identity, and Networking), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. Roles should match the operations the app or agent performs. Broad contributor access increases blast radius. In this case: Role-based access control restricts each identity to its authorized region and data scope.
- **B:** Incorrect for this question. A managed secret store supports rotation and access control. Secrets should never appear in prompts, code, or logs. Why the correct answer wins: Role-based access control restricts each identity to its authorized region and data scope.
- **C:** Incorrect for this question. Filters restrict results to content the user may see. They must be enforced before content reaches the model. Why the correct answer wins: Role-based access control restricts each identity to its authorized region and data scope.
- **D:** Incorrect for this question. Egress controls reduce exfiltration and unauthorized tool reach. Combine with identity and data controls. Why the correct answer wins: Role-based access control restricts each identity to its authorized region and data scope.

### Question 46 — B

Answer: Use evaluators for quality, safety, and groundedness. Evaluators produce comparable quality signals across configurations. Evaluators provide repeatable signals across models and prompts. They must be calibrated against human judgment for high-impact work. Local study-map skill 2.3 (Evaluating Models and Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Audit evidence supports investigation and accountability. Protect log integrity and retention. Why the correct answer wins: Evaluators produce comparable quality signals across configurations.
- **B:** Correct. Evaluators provide repeatable signals across models and prompts. They must be calibrated against human judgment for high-impact work. In this case: Evaluators produce comparable quality signals across configurations.
- **C:** Incorrect for this question. Central telemetry captures latency, errors, dependencies, and custom events. Redact sensitive content before logging. Why the correct answer wins: Evaluators produce comparable quality signals across configurations.
- **D:** Incorrect for this question. Alerts turn monitoring into action. Route them to an accountable owner with a runbook. Why the correct answer wins: Evaluators produce comparable quality signals across configurations.

### Question 47 — A

Answer: Enable tracing across agent, model, and tool calls. Traces show the ordered model and tool calls so the failing step can be located. Traces localize failures and latency in multi-step workflows. Correlate them with evaluation results and deployment versions. Local study-map skill 2.7 (Agent Monitoring and Error Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Traces localize failures and latency in multi-step workflows. Correlate them with evaluation results and deployment versions. In this case: Traces show the ordered model and tool calls so the failing step can be located.
- **B:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Traces show the ordered model and tool calls so the failing step can be located.
- **C:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Traces show the ordered model and tool calls so the failing step can be located.
- **D:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Traces show the ordered model and tool calls so the failing step can be located.

### Question 48 — C

Answer: Synthesize speech with Azure AI Speech. Text-to-speech synthesizes spoken output from generated text. Text-to-speech supports voice responses and accessibility. Voice, prosody, and latency affect usability. Local study-map skill 4.3 (Speech Solutions), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Custom speech can improve recognition of domain terms. It requires representative audio and ongoing evaluation. Why the correct answer wins: Text-to-speech synthesizes spoken output from generated text.
- **B:** Incorrect for this question. Speech-to-text enables voice agents and transcript analysis. Audio quality, accents, and domain terms affect accuracy. Why the correct answer wins: Text-to-speech synthesizes spoken output from generated text.
- **C:** Correct. Text-to-speech supports voice responses and accessibility. Voice, prosody, and latency affect usability. In this case: Text-to-speech synthesizes spoken output from generated text.
- **D:** Incorrect for this question. Audio-capable models can summarize or answer questions about recordings. Verify transcription quality and evidence grounding. Why the correct answer wins: Text-to-speech synthesizes spoken output from generated text.

### Question 49 — C

Answer: Adapt prompts and models to domain terminology. A validated domain lexicon teaches local terminology to the extraction step. Domain adaptation improves consistency and recall. Validate against expert-created expected outputs. Local study-map skill 4.4 (Domain Customization), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Sensitive Data Protection or language PII detection can identify and mask data. Verify that redaction covers every path where content flows. Why the correct answer wins: A validated domain lexicon teaches local terminology to the extraction step.
- **B:** Incorrect for this question. Translation should preserve meaning, names, and formatting. Evaluate domain terminology and low-resource languages. Why the correct answer wins: A validated domain lexicon teaches local terminology to the extraction step.
- **C:** Correct. Domain adaptation improves consistency and recall. Validate against expert-created expected outputs. In this case: A validated domain lexicon teaches local terminology to the extraction step.
- **D:** Incorrect for this question. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Why the correct answer wins: A validated domain lexicon teaches local terminology to the extraction step.

### Question 50 — B

Answer: Train a custom extraction model on labeled documents. A custom extraction model targets a proprietary document layout that no prebuilt model covers. Custom models fit specialized forms not covered by prebuilts. They require representative labels and retraining discipline. Local study-map skill 5.6 (Document and Content Extraction), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. Analyzers define what to extract and how to return it. Version and test them like application code. Why the correct answer wins: A custom extraction model targets a proprietary document layout that no prebuilt model covers.
- **B:** Correct. Custom models fit specialized forms not covered by prebuilts. They require representative labels and retraining discipline. In this case: A custom extraction model targets a proprietary document layout that no prebuilt model covers.
- **C:** Incorrect for this question. Prebuilt models cover invoices, receipts, IDs, and similar formats. Check supported locales and field coverage. Why the correct answer wins: A custom extraction model targets a proprietary document layout that no prebuilt model covers.
- **D:** Incorrect for this question. Single-task analyzers target one content type or objective. They may be simpler and cheaper than general pro-mode pipelines. Why the correct answer wins: A custom extraction model targets a proprietary document layout that no prebuilt model covers.
