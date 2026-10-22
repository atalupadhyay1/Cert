# Microsoft AI-103 — Full-Length Mock Exam 4

Azure AI Apps and Agents Developer Associate · 100 questions · 120 minutes · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 76 single-choice, 16 multi-select (selection count stated), 8 ordering items rendered as answer choices, and 4 case studies of 3 questions. Hot-area, drag-and-drop UI, labs, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. A plant wants a vision-capable model available in the same region as its factory data. What should the architects confirm first?

Domain: Plan and manage an Azure AI solution

- A. Use a small language model for a narrow, high-volume task
- B. Compare supported models in the Foundry model catalog
- C. Train or deploy a task-specific model outside the prebuilt catalog
- D. Use a general-purpose large language model for complex reasoning

### 2. Technicians upload a photo of a wiring harness together with a text question. Which model capability handles one request with both inputs?

Domain: Plan and manage an Azure AI solution

- A. Use Foundry Tools for prebuilt vision, speech, language, and extraction needs
- B. Use a small language model for a narrow, high-volume task
- C. Train or deploy a task-specific model outside the prebuilt catalog
- D. Use a multimodal model for combined text, image, or audio input

### 3. A maintenance agent must query the enterprise asset system for the next service date. Which capability performs that lookup?

Domain: Plan and manage an Azure AI solution

- A. Expose a typed function as an agent tool
- B. Use managed conversation state or memory for continuity
- C. Connect an Azure AI Search index as agent knowledge
- D. Expose an OpenAPI operation as an agent tool

### 4. A shift-handover assistant must remember the machines already discussed in the current session. What should be used?

Domain: Plan and manage an Azure AI solution

- A. Expose a typed function as an agent tool
- B. Use managed conversation state or memory for continuity
- C. Use a vector index for semantic retrieval
- D. Use an Azure AI Search indexer to pull source content

### 5. A manufacturer must release the same inspection assistant to three plants reproducibly. Which sequence should the team follow?

Domain: Plan and manage an Azure AI solution

- A. Deploy model → promote → provision resources → evaluate → configure app
- B. Evaluate → provision resources → promote → deploy model → configure app
- C. Configure app → provision resources → deploy model → promote → evaluate
- D. Provision resources → deploy model → configure app connection → evaluate → promote

### 6. Production telemetry must not reach the model endpoint across the public internet. What should be configured?

Domain: Plan and manage an Azure AI solution

- A. Track cost per accepted task, not only per token
- B. Plan for model quota expressed in tokens and requests per minute
- C. Use private endpoints and disable public network access
- D. Manage AI resources with infrastructure as code and CI/CD

### 7. Line-side tablets receive throttling errors at shift change when hundreds of scans start together. What should be adjusted?

Domain: Plan and manage an Azure AI solution

- A. Use provisioned throughput for predictable high-volume workloads
- B. Plan for model quota expressed in tokens and requests per minute
- C. Monitor input and quality drift over time
- D. Track cost per accepted task, not only per token

### 8. Monthly spend grows faster than usage because long manuals are re-sent for every question. Which optimization applies first?

Domain: Plan and manage an Azure AI solution

- A. Track prompt, completion, and cached token usage
- B. Plan for model quota expressed in tokens and requests per minute
- C. Track cost per accepted task, not only per token
- D. Use supported prompt or response caching where appropriate

### 9. Operations needs a single dashboard of model latency, error rate, and refusal rate. What should be enabled?

Domain: Plan and manage an Azure AI solution

- A. Preserve audit logs of changes, approvals, and tool actions
- B. Alert on latency, error rate, safety, and cost thresholds
- C. Use Azure Monitor and Application Insights for telemetry
- D. Monitor input and quality drift over time

### 10. Quality degrades as new equipment is photographed, and engineers must learn quickly. Which two capabilities are needed? Select two.

Domain: Plan and manage an Azure AI solution

- A. Track cost per accepted task, not only per token
- B. Alert on latency, error rate, safety, and cost thresholds
- C. Use supported prompt or response caching where appropriate
- D. Plan for model quota expressed in tokens and requests per minute
- E. Monitor input and quality drift over time

### 11. A plant app must call Foundry without stored secrets and with only read access to one index. Which two actions should you take? Select two.

Domain: Plan and manage an Azure AI solution

- A. Use private endpoints and disable public network access
- B. Configure content safety filters for harmful categories
- C. Authenticate with a managed identity instead of keys
- D. Store secrets in Azure Key Vault when keys are unavoidable
- E. Use least-privilege Azure RBAC roles for the workload identity

### 12. A safety assistant must never propose bypassing a lockout procedure, even if asked directly. Which control applies?

Domain: Plan and manage an Azure AI solution

- A. Set agent oversight mode and tool-access constraints
- B. Enforce constraints in code and platform policy
- C. Preserve audit logs of changes, approvals, and tool actions
- D. Require human approval before consequential actions

### 13. A code assistant reproduces a licensed vendor routine verbatim in suggestions. Which control addresses this?

Domain: Plan and manage an Azure AI solution

- A. Detect protected or copyrighted material in output
- B. Enforce brand and usage rules for generated visuals
- C. Configure content safety filters for harmful categories
- D. Apply watermarks or provenance markers to generated media

### 14. A maintenance assistant must answer from the current approved service bulletins and cite them. Which approach fits?

Domain: Implement generative AI and agentic solutions

- A. Translate every request before retrieval
- B. Design multistep workflows with explicit checkpoints
- C. Ground responses with retrieval-augmented generation
- D. Route requests to different models by task difficulty

### 15. A work-order system needs fixed fields and types from each technician note. What should the model produce?

Domain: Implement generative AI and agentic solutions

- A. Use supported prompt or response caching where appropriate
- B. Use a versioned prompt template with explicit variables
- C. Design multistep workflows with explicit checkpoints
- D. Return a defined JSON schema for downstream systems

### 16. A quality workflow must read a gauge photo, check the reading against limits, then file a deviation. What should the design use?

Domain: Implement generative AI and agentic solutions

- A. Design multistep workflows with explicit checkpoints
- B. Limit autonomy with scope, budget, and stop conditions
- C. One model call with no external retrieval or tool use
- D. Route requests to different models by task difficulty

### 17. A .NET service needs supported authentication and retry handling for Foundry calls. What should it use?

Domain: Implement generative AI and agentic solutions

- A. Manage AI resources with infrastructure as code and CI/CD
- B. Use batch processing for latency-tolerant bulk work
- C. Use a Foundry SDK or supported connector from application code
- D. Create and run deployments by hand in the portal

### 18. An application must call only the deployments approved for one Foundry project. What should it be configured with?

Domain: Implement generative AI and agentic solutions

- A. Store secrets in Azure Key Vault when keys are unavoidable
- B. Connect the application to the Foundry project endpoint
- C. Compare supported models in the Foundry model catalog
- D. Use an Azure AI Search indexer to pull source content

### 19. A team must keep a stable accuracy benchmark and ensure no earlier defect case regresses. Which two practices are required? Select two.

Domain: Implement generative AI and agentic solutions

- A. Lower temperature for more deterministic extraction
- B. Re-run evaluation suites after meaningful changes
- C. Build a representative golden dataset from real tasks
- D. Use provisioned throughput for predictable high-volume workloads
- E. Apply watermarks or provenance markers to generated media

### 20. Two prompt variants must be scored on the same labelled inspection cases before release. What should be run?

Domain: Implement generative AI and agentic solutions

- A. Alert on latency, error rate, safety, and cost thresholds
- B. Use evaluators for quality, safety, and groundedness
- C. Preserve audit logs of changes, approvals, and tool actions
- D. Use Azure Monitor and Application Insights for telemetry

### 21. An agent sends a machine identifier in the wrong format to a scheduling tool. What should be tightened first?

Domain: Implement generative AI and agentic solutions

- A. Put stable behavior rules in the system message
- B. Use managed conversation state or memory for continuity
- C. Define narrow tool schemas with clear descriptions
- D. Use a versioned prompt template with explicit variables

### 22. A shift agent must keep a consistent role and remember the line under discussion. Which two components provide that? Select two.

Domain: Implement generative AI and agentic solutions

- A. Put stable behavior rules in the system message
- B. Define narrow tool schemas with clear descriptions
- C. Expose an OpenAPI operation as an agent tool
- D. Ground responses with retrieval-augmented generation
- E. Use managed conversation state or memory for continuity

### 23. A warehouse agent must call an inventory service that already publishes an OpenAPI contract. Which tool type fits?

Domain: Implement generative AI and agentic solutions

- A. Ground responses with retrieval-augmented generation
- B. Expose a typed function as an agent tool
- C. Use managed conversation state or memory for continuity
- D. Expose an OpenAPI operation as an agent tool

### 24. A deviation must be classified, then escalated, then documented in that fixed order. Which pattern fits?

Domain: Implement generative AI and agentic solutions

- A. Run independent agents concurrently
- B. Run agents in a fixed sequence
- C. Use a manager agent to coordinate specialists
- D. Use self-critique or reflection to improve drafts

### 25. A coordinator must choose among maintenance, quality, and logistics specialists and merge their answers. Which pattern fits?

Domain: Implement generative AI and agentic solutions

- A. Use self-critique or reflection to improve drafts
- B. Transfer control between agents with explicit context
- C. Use a manager agent to coordinate specialists
- D. Run independent agents concurrently

### 26. Which sequence correctly handles an alert about failing defect detection?

Domain: Implement generative AI and agentic solutions

- A. Verify with regression evaluation → apply fix → detect alert → isolate the failing step → inspect traces
- B. Apply fix → detect alert → inspect traces → isolate the failing step → verify with regression evaluation
- C. Detect alert → inspect traces → isolate the failing step → apply fix → verify with regression evaluation
- D. Isolate the failing step → apply fix → detect alert → verify with regression evaluation → inspect traces

### 27. Single-field extraction returns different values on identical repeat requests. Which setting should be lowered first?

Domain: Implement generative AI and agentic solutions

- A. Adjust top-p to control response diversity
- B. Lower temperature for more deterministic extraction
- C. Route requests to different models by task difficulty
- D. Use supported prompt or response caching where appropriate

### 28. A training team needs an original diagram of a safe lockout procedure. Which capability applies?

Domain: Implement computer vision solutions

- A. Generate alt text aligned to accessibility guidance
- B. Generate video from text or reference media
- C. Edit a region of an image with a mask
- D. Generate images from text and reference media

### 29. A photo of a new machine must have an outdated safety label removed while everything else stays intact. What should be used?

Domain: Implement computer vision solutions

- A. Edit generated video segments
- B. Edit a region of an image with a mask
- C. Apply prompt-driven image modifications
- D. Generate concise or detailed image captions

### 30. Investigators must find the timestamp in recorded footage when a conveyor stops. Which capability applies?

Domain: Implement computer vision solutions

- A. Generate video from text or reference media
- B. Analyze video segments for events and content
- C. Generate concise or detailed image captions
- D. Edit generated video segments

### 31. Which sequence correctly processes inspection photos and routes uncertain readings to a person?

Domain: Implement computer vision solutions

- A. Parse structured fields → send multimodal request → upload image → validate format → review
- B. Validate format → review → upload image → parse structured fields → send multimodal request
- C. Send multimodal request → upload image → validate format → parse structured fields → review
- D. Upload image → validate format and size → send multimodal request → parse structured fields → route low-confidence values to review

### 32. A parts catalogue needs accessible image descriptions and answers about gauge values in photos. Which two capabilities apply? Select two.

Domain: Implement computer vision solutions

- A. Generate concise or detailed image captions
- B. Lower temperature for more deterministic extraction
- C. Answer questions grounded in visual evidence
- D. Apply watermarks or provenance markers to generated media
- E. Generate alt text aligned to accessibility guidance

### 33. Inspection packets mix photos, tables, and handwriting across several pages. Which Content Understanding mode should be evaluated?

Domain: Implement computer vision solutions

- A. Train a custom extraction model on labeled documents
- B. Use single-task mode for a focused extraction scenario
- C. Use pro mode for complex multimodal content understanding
- D. Use Azure AI Document Intelligence for forms and documents

### 34. Generated images appear in supplier-facing material and must be safe and on-brand. Which two controls apply? Select two.

Domain: Implement computer vision solutions

- A. Enforce brand and usage rules for generated visuals
- B. Lower temperature for more deterministic extraction
- C. Apply watermarks or provenance markers to generated media
- D. Adjust top-p to control response diversity
- E. Filter unsafe or disallowed visual content

### 35. A quality system requires fixed field names and types from each incident email. What should the prompt request?

Domain: Implement text analysis solutions

- A. Identify topics or key phrases for navigation
- B. Prompt for JSON that conforms to a supplied schema
- C. Generate summaries with explicit length and audience constraints
- D. Use Azure Translator or a language model for translation

### 36. A safety mailbox must detect personal data and rising frustration in reports. Which two analyses apply? Select two.

Domain: Implement text analysis solutions

- A. Identify topics or key phrases for navigation
- B. Detect and redact sensitive personal data
- C. Generate summaries with explicit length and audience constraints
- D. Apply a custom glossary or terminology list
- E. Analyze sentiment and tone with an appropriate service

### 37. Machine translation keeps mistranslating approved part names into another language. What should be configured?

Domain: Implement text analysis solutions

- A. Use Azure Translator or a language model for translation
- B. Detect and redact sensitive personal data
- C. Apply a custom glossary or terminology list
- D. Extract entities with defined types and boundaries

### 38. Recorded shift briefings must become searchable text. Which capability applies?

Domain: Implement text analysis solutions

- A. Synthesize speech with Azure AI Speech
- B. Use a multimodal model to reason over audio content
- C. Transcribe speech to text with Azure AI Speech
- D. Translate spoken language with speech translation

### 39. Hands-free reporting is inaccurate because of plant noise and local product names. What should be trained?

Domain: Implement text analysis solutions

- A. Apply a custom glossary or terminology list
- B. Use a custom speech model for specialized vocabulary
- C. Transcribe speech to text with Azure AI Speech
- D. Synthesize speech with Azure AI Speech

### 40. Supervisors need a short digest of a long incident investigation. Which task applies?

Domain: Implement text analysis solutions

- A. Identify topics or key phrases for navigation
- B. Extract entities with defined types and boundaries
- C. Generate summaries with explicit length and audience constraints
- D. Use Azure Translator or a language model for translation

### 41. Regulated incident summaries must keep required disclosures and understand plant-specific terms. Which two practices help? Select two.

Domain: Implement text analysis solutions

- A. Identify topics or key phrases for navigation
- B. Analyze sentiment and tone with an appropriate service
- C. Adapt prompts and models to domain terminology
- D. Use Azure Translator or a language model for translation
- E. Customize summaries and extraction for compliance needs

### 42. A search index must follow documents added to a storage account without custom code. What should be used?

Domain: Implement information extraction solutions

- A. Apply OCR to convert images and scans into usable text
- B. Add an enrichment skillset to an indexing pipeline
- C. Use an Azure AI Search indexer to pull source content
- D. Push documents to an index through the data-plane API

### 43. Newly generated inspection reports must be searchable within seconds. What should the application use?

Domain: Implement information extraction solutions

- A. Push documents to an index through the data-plane API
- B. Propagate source deletions to indexes and caches
- C. Use an Azure AI Search indexer to pull source content
- D. Ingest content through supported indexers or APIs

### 44. Which sequence correctly builds a citable retrieval pipeline over maintenance manuals?

Domain: Implement information extraction solutions

- A. Ingest → extract text → chunk → embed → index → retrieve with citations
- B. Index → retrieve → ingest → chunk → embed → cite
- C. Chunk → embed → ingest → retrieve → index → cite
- D. Ingest → retrieve → chunk → embed → index → cite

### 45. A plant must keep one validated inspection model version in its operating region for a full audit cycle. What should the team do?

Domain: Plan and manage an Azure AI solution

- A. Pin the model version available in the required region
- B. Use a general-purpose large language model for complex reasoning
- C. Compare supported models in the Foundry model catalog
- D. Train or deploy a task-specific model outside the prebuilt catalog

### 46. A factory wants image captioning and speech transcription this quarter with no labelled dataset. What should be assessed first?

Domain: Plan and manage an Azure AI solution

- A. Use Foundry Tools for prebuilt vision, speech, language, and extraction needs
- B. Train or deploy a task-specific model outside the prebuilt catalog
- C. Use a general-purpose large language model for complex reasoning
- D. Use a small language model for a narrow, high-volume task

### 47. An agent must query the maintenance system whose operations are already published as a machine-readable contract. Which tool type fits?

Domain: Plan and manage an Azure AI solution

- A. Use managed conversation state or memory for continuity
- B. Expose an OpenAPI operation as an agent tool
- C. Expose a typed function as an agent tool
- D. Connect an Azure AI Search index as agent knowledge

### 48. An inspection model must not reach the line when defect recall drops on a fixed test set. What should be added?

Domain: Plan and manage an Azure AI solution

- A. Block promotion in the pipeline when evaluation thresholds fail
- B. Manage AI resources with infrastructure as code and CI/CD
- C. Shift a small traffic percentage to the new version first
- D. Use staged rollout with measurable rollback criteria

### 49. Engineers want a candidate detector scored against live camera feeds without affecting sorting. What pattern fits?

Domain: Plan and manage an Azure AI solution

- A. Send mirrored production traffic to a candidate without returning its answers
- B. Use a standard pay-as-you-go model deployment for variable demand
- C. Shift a small traffic percentage to the new version first
- D. Use batch processing for latency-tolerant bulk work

### 50. The plant manager wants warning before a pilot's monthly AI spend exceeds its cap. What should be configured?

Domain: Plan and manage an Azure AI solution

- A. Plan for model quota expressed in tokens and requests per minute
- B. Track prompt, completion, and cached token usage
- C. Track cost per accepted task, not only per token
- D. Alert on spend thresholds per deployment or project

### 51. Technicians are shown a maintenance procedure that was superseded last month. What should be monitored?

Domain: Plan and manage an Azure AI solution

- A. Monitor input and quality drift over time
- B. Monitor index freshness, failures, and document counts
- C. Use Azure Monitor and Application Insights for telemetry
- D. Monitor groundedness and citation quality in production

### 52. The line workload may reach only approved plant services. What should be enforced?

Domain: Plan and manage an Azure AI solution

- A. Use least-privilege Azure RBAC roles for the workload identity
- B. Restrict outbound network access to approved destinations
- C. Use private endpoints and disable public network access
- D. Private networking with public access left enabled

### 53. A safety interlock override must remain attributable to a named engineer. Which principle applies?

Domain: Plan and manage an Azure AI solution

- A. Set agent oversight mode and tool-access constraints
- B. Enforce constraints in code and platform policy
- C. Require human approval before consequential actions
- D. Preserve audit logs of changes, approvals, and tool actions

### 54. Four years of archived inspection photos must be re-scored once for trend analysis. Which deployment option fits?

Domain: Plan and manage an Azure AI solution

- A. Use provisioned throughput for predictable high-volume workloads
- B. Plan for model quota expressed in tokens and requests per minute
- C. Use batch processing for latency-tolerant bulk work
- D. Use a standard pay-as-you-go model deployment for variable demand

### 55. A vision model must be sourced locally and must not change during a production audit window. Which two practices are required? Select two.

Domain: Plan and manage an Azure AI solution

- A. Use batch processing for latency-tolerant bulk work
- B. Compare supported models in the Foundry model catalog
- C. Train or deploy a task-specific model outside the prebuilt catalog
- D. Pin the model version available in the required region
- E. Use a standard pay-as-you-go model deployment for variable demand

### 56. A maintenance assistant must be checked for unsupported instructions and the team warned quickly. Which two capabilities are required? Select two.

Domain: Plan and manage an Azure AI solution

- A. Track cost per accepted task, not only per token
- B. Monitor groundedness and citation quality in production
- C. Apply watermarks or provenance markers to generated media
- D. Alert on latency, error rate, safety, and cost thresholds
- E. Measure end-to-end latency across model, retrieval, and tools

### 57. The inspection service must not call unapproved endpoints and must hold only its needed permissions. Which two controls are required? Select two.

Domain: Plan and manage an Azure AI solution

- A. Use least-privilege Azure RBAC roles for the workload identity
- B. Configure content safety filters for harmful categories
- C. Restrict outbound network access to approved destinations
- D. Store secrets in Azure Key Vault when keys are unavoidable
- E. Use private endpoints and disable public network access

### 58. Which sequence correctly releases a detector update through an evaluation gate?

Domain: Plan and manage an Azure AI solution

- A. Deploy a canary → commit change → promote after metrics hold → run the evaluation suite → block on failed thresholds
- B. Run the evaluation suite → deploy a canary → commit change → block on failed thresholds → promote after metrics hold
- C. Commit change → deploy a canary → promote after metrics hold → run the evaluation suite → block on failed thresholds
- D. Commit change → run the evaluation suite → block on failed thresholds → deploy a canary → promote after metrics hold

### 59. A torque specification split across two pages is never retrieved. What should be adjusted?

Domain: Implement generative AI and agentic solutions

- A. Set chunk overlap so facts spanning a boundary stay retrievable
- B. Choose chunk size and overlap for retrieval quality
- C. Choose an embedding model suited to the content and language
- D. Select evidence within the model's usable context

### 60. Procedures change weekly and every instruction must cite the approved manual. Which approach fits?

Domain: Implement generative AI and agentic solutions

- A. Ground responses with retrieval-augmented generation
- B. Design multistep workflows with explicit checkpoints
- C. Route requests to different models by task difficulty
- D. Include representative examples in the prompt

### 61. A shop-floor tablet app must call the model service with a short-lived delegated credential. What should it request?

Domain: Implement generative AI and agentic solutions

- A. Use a Foundry SDK or supported connector from application code
- B. Authenticate with a managed identity instead of keys
- C. Use short-lived scoped access tokens for tool calls
- D. Store secrets in Azure Key Vault when keys are unavoidable

### 62. Two defect-classification prompts must be compared over identical images. What provides that?

Domain: Implement generative AI and agentic solutions

- A. Build a representative golden dataset from real tasks
- B. Use evaluators for quality, safety, and groundedness
- C. Compare variants with controlled traffic and shared metrics
- D. Re-run evaluation suites after meaningful changes

### 63. A detector upgrade must not restore a defect class that was previously fixed. What should run first?

Domain: Implement generative AI and agentic solutions

- A. Re-run evaluation suites after meaningful changes
- B. Use evaluators for quality, safety, and groundedness
- C. Build a representative golden dataset from real tasks
- D. Evaluate harmful, biased, or policy-violating output

### 64. The agent submits a machine identifier in the wrong format to a scheduling tool. What should be tightened first?

Domain: Implement generative AI and agentic solutions

- A. Define narrow tool schemas with clear descriptions
- B. Use managed conversation state or memory for continuity
- C. Put stable behavior rules in the system message
- D. Route requests to different models by task difficulty

### 65. A general plant assistant must transfer a vibration anomaly to the reliability specialist with context. Which pattern fits?

Domain: Implement generative AI and agentic solutions

- A. Use self-critique or reflection to improve drafts
- B. Use a manager agent to coordinate specialists
- C. Run independent agents concurrently
- D. Transfer control between agents with explicit context

### 66. Three independent sensor checks must finish inside one cycle time. Which pattern fits?

Domain: Implement generative AI and agentic solutions

- A. Run independent agents concurrently
- B. Use self-critique or reflection to improve drafts
- C. Run agents in a fixed sequence
- D. Use a manager agent to coordinate specialists

### 67. Generated work orders include commentary that breaks the downstream parser. What should be specified?

Domain: Implement generative AI and agentic solutions

- A. Use supported prompt or response caching where appropriate
- B. Lower temperature for more deterministic extraction
- C. Set a stop sequence so generation ends at the intended boundary
- D. Adjust top-p to control response diversity

### 68. Shift reports repeat identical phrasing and never vary. Which parameter should be adjusted?

Domain: Implement generative AI and agentic solutions

- A. Adjust top-p to control response diversity
- B. Set a seed parameter for reproducible sampling where the provider supports it
- C. Lower temperature for more deterministic extraction
- D. Use supported prompt or response caching where appropriate

### 69. A plant service must use maintained client behaviour and hold no stored credential. Which two choices are required? Select two.

Domain: Implement generative AI and agentic solutions

- A. Create and run deployments by hand in the portal
- B. Authenticate with a managed identity instead of keys
- C. Use short-lived scoped access tokens for tool calls
- D. Store secrets in Azure Key Vault when keys are unavoidable
- E. Use a Foundry SDK or supported connector from application code

### 70. A detector release must be scored for accuracy and screened for unsafe recommendations. Which two practices are required? Select two.

Domain: Implement generative AI and agentic solutions

- A. Compare variants with controlled traffic and shared metrics
- B. Build a representative golden dataset from real tasks
- C. Re-run evaluation suites after meaningful changes
- D. Evaluate harmful, biased, or policy-violating output
- E. Use evaluators for quality, safety, and groundedness

### 71. A quality agent must search approved specifications and compute tolerance results reliably. Which two tools are required? Select two.

Domain: Implement generative AI and agentic solutions

- A. Give the agent a file-search tool over approved document stores
- B. Route requests to different models by task difficulty
- C. Enable a sandboxed code interpreter tool for calculations
- D. Use managed conversation state or memory for continuity
- E. Expose an OpenAPI operation as an agent tool

### 72. Which sequence correctly builds and releases a maintenance agent?

Domain: Implement generative AI and agentic solutions

- A. Define role and goal → configure tools → attach knowledge → evaluate in sandbox → deploy with monitoring
- B. Configure tools → deploy with monitoring → define role and goal → attach knowledge → evaluate in sandbox
- C. Deploy with monitoring → define role and goal → configure tools → evaluate in sandbox → attach knowledge
- D. Attach knowledge → configure tools → deploy with monitoring → define role and goal → evaluate in sandbox

### 73. A generated safety poster passes automated checks but supervisors consider it alarming. What should be added?

Domain: Implement computer vision solutions

- A. Enforce brand and usage rules for generated visuals
- B. Filter unsafe or disallowed visual content
- C. Apply watermarks or provenance markers to generated media
- D. Queue flagged generations for human moderation before release

### 74. A defect archive needs filterable descriptive tags for engineers. What should be generated?

Domain: Implement computer vision solutions

- A. Generate alt text aligned to accessibility guidance
- B. Generate a set of descriptive tags for each image
- C. Answer questions grounded in visual evidence
- D. Generate concise or detailed image captions

### 75. Extracted inspection sheets are scrambled because the layout is read incorrectly. What should be applied?

Domain: Implement computer vision solutions

- A. Apply OCR to convert images and scans into usable text
- B. Preserve reading order across columns and sections
- C. Preserve document layout, tables, and reading order
- D. Produce markdown representations for downstream reasoning

### 76. A team needs a configurable analyzer over mixed inspection reports and photos rather than a fixed prebuilt model. Which service fits?

Domain: Implement computer vision solutions

- A. Configure a Content Understanding analyzer for the content type
- B. Use Azure AI Document Intelligence for forms and documents
- C. Use Azure Content Understanding analyzers in Foundry Tools
- D. Use a prebuilt document model for common document types

### 77. Inspection packets mix photos, tables, and handwriting, and the output must feed a reasoning model. Which two choices are required? Select two.

Domain: Implement computer vision solutions

- A. Use single-task mode for a focused extraction scenario
- B. Return markdown for retrieval and reasoning pipelines
- C. Identify objects, components, or regions in visual content
- D. Generate concise or detailed image captions
- E. Use pro mode for complex multimodal content understanding

### 78. Which sequence correctly processes a photographed gauge and routes doubtful readings to a person?

Domain: Implement computer vision solutions

- A. Parse structured fields → send multimodal request → upload image → validate format → review
- B. Send multimodal request → upload image → validate format → parse structured fields → review
- C. Validate format → review → upload image → parse structured fields → send multimodal request
- D. Upload image → validate format and size → send multimodal request → parse structured fields → route low-confidence values to review

### 79. An auditor requires incident summaries that quote exact source sentences. Which style fits?

Domain: Implement text analysis solutions

- A. Generate summaries with explicit length and audience constraints
- B. Select and return the most relevant source sentences
- C. Customize summaries and extraction for compliance needs
- D. Generate an abstractive summary in new wording

### 80. Supplier names in another writing system must print correctly without translating meaning. Which capability applies?

Domain: Implement text analysis solutions

- A. Adapt prompts and models to domain terminology
- B. Use Azure Translator or a language model for translation
- C. Apply a custom glossary or terminology list
- D. Convert names between writing systems without translating meaning

### 81. A hands-free station must use one consistent voice for all prompts. What should be selected?

Domain: Implement text analysis solutions

- A. Synthesize speech with Azure AI Speech
- B. Use a custom speech model for specialized vocabulary
- C. Select a specific synthesis voice for consistent spoken output
- D. Apply a custom glossary or terminology list

### 82. Supervisors need a quick topical index of what each incident file covers. Which capability applies?

Domain: Implement text analysis solutions

- A. Extract entities with defined types and boundaries
- B. Generate summaries with explicit length and audience constraints
- C. Extract key phrases to summarize what a document covers
- D. Identify topics or key phrases for navigation

### 83. A safety mailbox must detect personal data and rising frustration. Which two analyses are relevant? Select two.

Domain: Implement text analysis solutions

- A. Apply a custom glossary or terminology list
- B. Identify topics or key phrases for navigation
- C. Analyze sentiment and tone with an appropriate service
- D. Generate summaries with explicit length and audience constraints
- E. Detect and redact sensitive personal data

### 84. Searches for a part number return unrelated manuals because one document family dominates. What should be tuned and measured?

Domain: Implement information extraction solutions

- A. Apply semantic ranking to reorder search results
- B. Use a vector index for semantic retrieval
- C. Combine keyword and vector retrieval
- D. Tune scoring and boosting against a labelled query set

### 85. Each indexed manual must gain extracted components and a generated abstract. What produces that?

Domain: Implement information extraction solutions

- A. Add an enrichment skillset to an indexing pipeline
- B. Return markdown for retrieval and reasoning pipelines
- C. Use an Azure AI Search indexer to pull source content
- D. Add enrichment skills for text, image, and layout

### 86. Engineers must filter by inspection date and sort by severity, but those fields are full-text only. What should change?

Domain: Implement information extraction solutions

- A. Use Azure AI Document Intelligence for forms and documents
- B. Return typed fields for automation
- C. Configure a Content Understanding analyzer for the content type
- D. Define index fields, attributes, and searchable versus filterable behavior

### 87. Scanned drawings must preserve dimension callout relationships for extraction. What should be applied?

Domain: Implement information extraction solutions

- A. Produce markdown representations for downstream reasoning
- B. Choose chunk size and overlap for retrieval quality
- C. Combine OCR with layout analysis for complex documents
- D. Use an Azure AI Search indexer to pull source content

### 88. Which sequence correctly builds a maintenance knowledge index?

Domain: Implement information extraction solutions

- A. Run the indexer → connect the data source → define the index schema → attach the enrichment skillset → validate relevance on sample queries
- B. Attach the enrichment skillset → connect the data source → validate relevance on sample queries → define the index schema → run the indexer
- C. Connect the data source → define the index schema → attach the enrichment skillset → run the indexer → validate relevance on sample queries
- D. Validate relevance on sample queries → run the indexer → connect the data source → define the index schema → attach the enrichment skillset

---

## Case study — Apex Motors

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 89. A technician resumes the same line issue after lunch and the assistant must recall the machine tag. Which capability is required?

Domain: Implement generative AI and agentic solutions

- A. Persist conversation history in a thread or session
- B. Use provisioned throughput for predictable high-volume workloads
- C. Choose an embedding model suited to the content and language
- D. Apply watermarks or provenance markers to generated media

### 90. Voice reporting misreads part numbers that are critical for traceability. What should be trained?

Domain: Implement text analysis solutions

- A. Transcribe speech to text with Azure AI Speech
- B. Use a custom speech model for specialized vocabulary
- C. Synthesize speech with Azure AI Speech
- D. Apply a custom glossary or terminology list

### 91. Scanned measurements are sometimes misread. What should route those values to a person?

Domain: Implement information extraction solutions

- A. Measure whether retrieved content and answers address the question
- B. Generate summaries with explicit length and audience constraints
- C. Analyze sentiment and tone with an appropriate service
- D. Use field-level confidence to route exceptions

---

## Case study — Fabrikam Plant

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 92. The plant uses a proprietary inspection form with no standard equivalent. What should be built?

Domain: Implement information extraction solutions

- A. Use a prebuilt document model for common document types
- B. Configure a Content Understanding analyzer for the content type
- C. Use Azure AI Document Intelligence for forms and documents
- D. Train a custom extraction model on labeled documents

### 93. Contractors must only retrieve documents approved for their plant. What should be enforced?

Domain: Implement information extraction solutions

- A. Combine keyword and vector retrieval
- B. Verify index freshness and deletion propagation
- C. Apply semantic ranking to reorder search results
- D. Apply document-level security filters at query time

### 94. Each indexed manual must gain extracted entities and a generated summary. What performs that work?

Domain: Implement information extraction solutions

- A. Apply OCR to convert images and scans into usable text
- B. Add enrichment skills for text, image, and layout
- C. Add an enrichment skillset to an indexing pipeline
- D. Use an Azure AI Search indexer to pull source content

---

## Case study — Ironworks Plant

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 95. An engineer needs yield percentages computed across extracted shift records, and text arithmetic is unreliable. Which tool is required?

Domain: Implement generative AI and agentic solutions

- A. Expose an OpenAPI operation as an agent tool
- B. Use managed conversation state or memory for continuity
- C. Give the agent a file-search tool over approved document stores
- D. Enable a sandboxed code interpreter tool for calculations

### 96. A work-order request fails only after the second tool call. What should be inspected?

Domain: Implement generative AI and agentic solutions

- A. Lower temperature for more deterministic extraction
- B. Apply watermarks or provenance markers to generated media
- C. Use supported prompt or response caching where appropriate
- D. Enable tracing across agent, model, and tool calls

### 97. Newly generated inspection reports must be searchable within seconds. What should the application use?

Domain: Implement information extraction solutions

- A. Push documents to an index through the data-plane API
- B. Apply OCR to convert images and scans into usable text
- C. Use an Azure AI Search indexer to pull source content
- D. Add an enrichment skillset to an indexing pipeline

---

## Case study — LineSight

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 98. A plant runs continuous 24-hour inspection inference with steady volume and cannot tolerate throttling. Which capacity option should be evaluated?

Domain: Plan and manage an Azure AI solution

- A. Use batch processing for latency-tolerant bulk work
- B. Use provisioned throughput for predictable high-volume workloads
- C. Use a standard pay-as-you-go model deployment for variable demand
- D. Use supported prompt or response caching where appropriate

### 99. A defect request fails only after the second tool call. What should be inspected first?

Domain: Implement generative AI and agentic solutions

- A. Enable tracing across agent, model, and tool calls
- B. Lower temperature for more deterministic extraction
- C. Apply watermarks or provenance markers to generated media
- D. Use supported prompt or response caching where appropriate

### 100. The agent must keep the work-order number across turns while checking status. Which capability is required?

Domain: Implement generative AI and agentic solutions

- A. Use provisioned throughput for predictable high-volume workloads
- B. Apply watermarks or provenance markers to generated media
- C. Choose an embedding model suited to the content and language
- D. Persist conversation history in a thread or session

---

## Answer key and explanations

### Question 1 — B

Answer: Compare supported models in the Foundry model catalog. The catalog shows which models support vision in each region before design is fixed. The catalog shows supported models with capability, modality, region, and lifecycle details. Verify availability for your subscription and region before designing around one model. Local study-map skill 1.1 (Selecting Foundry Models and Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Small models can reduce latency and cost for constrained classification or extraction. Confirm quality on representative data before standardizing. Why the correct answer wins: The catalog shows which models support vision in each region before design is fixed.
- **B:** Correct. The catalog shows supported models with capability, modality, region, and lifecycle details. Verify availability for your subscription and region before designing around one model. In this case: The catalog shows which models support vision in each region before design is fixed.
- **C:** Incorrect for this question. A custom model is justified when supported prebuilt options cannot meet a defined requirement. It adds data, evaluation, and lifecycle obligations. Why the correct answer wins: The catalog shows which models support vision in each region before design is fixed.
- **D:** Incorrect for this question. Large models handle ambiguity and multi-step reasoning better in many cases, at higher cost and latency. Select with measured evidence rather than brand preference. Why the correct answer wins: The catalog shows which models support vision in each region before design is fixed.

### Question 2 — D

Answer: Use a multimodal model for combined text, image, or audio input. A multimodal model accepts image and text in the same request. Multimodal models accept more than one content type in a request. Validate extraction and grounding quality for each modality used. Local study-map skill 1.1 (Selecting Foundry Models and Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Prebuilt managed capabilities can reduce custom model work where their behavior and limits fit the task. They are not a substitute for task-specific validation. Why the correct answer wins: A multimodal model accepts image and text in the same request.
- **B:** Incorrect for this question. Small models can reduce latency and cost for constrained classification or extraction. Confirm quality on representative data before standardizing. Why the correct answer wins: A multimodal model accepts image and text in the same request.
- **C:** Incorrect for this question. A custom model is justified when supported prebuilt options cannot meet a defined requirement. It adds data, evaluation, and lifecycle obligations. Why the correct answer wins: A multimodal model accepts image and text in the same request.
- **D:** Correct. Multimodal models accept more than one content type in a request. Validate extraction and grounding quality for each modality used. In this case: A multimodal model accepts image and text in the same request.

### Question 3 — A

Answer: Expose a typed function as an agent tool. A function tool calls the asset system under the application's authorization. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. Local study-map skill 1.2 (Retrieval, Memory, Tool, and Knowledge Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. In this case: A function tool calls the asset system under the application's authorization.
- **B:** Incorrect for this question. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Why the correct answer wins: A function tool calls the asset system under the application's authorization.
- **C:** Incorrect for this question. An index gives an agent curated, searchable evidence under configured access. Index content and permissions require ongoing ownership. Why the correct answer wins: A function tool calls the asset system under the application's authorization.
- **D:** Incorrect for this question. OpenAPI tools describe supported HTTP operations for agent use. Narrow operations, validate inputs, and authenticate the caller. Why the correct answer wins: A function tool calls the asset system under the application's authorization.

### Question 4 — B

Answer: Use managed conversation state or memory for continuity. Managed conversation state keeps prior turns available to the agent. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Local study-map skill 1.2 (Retrieval, Memory, Tool, and Knowledge Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. Why the correct answer wins: Managed conversation state keeps prior turns available to the agent.
- **B:** Correct. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. In this case: Managed conversation state keeps prior turns available to the agent.
- **C:** Incorrect for this question. Embeddings support similarity search over meaning rather than exact terms. Vector search still needs chunking, filtering, and evaluation. Why the correct answer wins: Managed conversation state keeps prior turns available to the agent.
- **D:** Incorrect for this question. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. Why the correct answer wins: Managed conversation state keeps prior turns available to the agent.

### Question 5 — D

Answer: Provision resources → deploy model → configure app connection → evaluate → promote. Provisioning and deployment precede configuration, and evaluation gates promotion. Provisioning and deployment precede app configuration, and evaluation gates promotion. Local study-map skill 1.3 (Infrastructure, Deployment, and CI/CD), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Promotion before provisioning and evaluation skips the controls that make deployment safe. Why the correct answer wins: Provisioning and deployment precede configuration, and evaluation gates promotion.
- **B:** Incorrect for this question. Evaluation before any deployment or configuration has nothing meaningful to assess. Why the correct answer wins: Provisioning and deployment precede configuration, and evaluation gates promotion.
- **C:** Incorrect for this question. Evaluation after promotion cannot gate the release. Why the correct answer wins: Provisioning and deployment precede configuration, and evaluation gates promotion.
- **D:** Correct. Provisioning and deployment precede app configuration, and evaluation gates promotion. In this case: Provisioning and deployment precede configuration, and evaluation gates promotion.

### Question 6 — C

Answer: Use private endpoints and disable public network access. A private endpoint keeps model traffic on the private network path. Private connectivity keeps service traffic on approved network paths. Pair it with private DNS so clients resolve the private address. Local study-map skill 1.3 (Infrastructure, Deployment, and CI/CD), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Retries, tool calls, evaluation, and review contribute to unit economics. Per-outcome cost supports better optimization. Why the correct answer wins: A private endpoint keeps model traffic on the private network path.
- **B:** Incorrect for this question. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. Why the correct answer wins: A private endpoint keeps model traffic on the private network path.
- **C:** Correct. Private connectivity keeps service traffic on approved network paths. Pair it with private DNS so clients resolve the private address. In this case: A private endpoint keeps model traffic on the private network path.
- **D:** Incorrect for this question. Repeatable deployments reduce configuration drift. Include model deployments, indexes, and connections in review and promotion. Why the correct answer wins: A private endpoint keeps model traffic on the private network path.

### Question 7 — B

Answer: Plan for model quota expressed in tokens and requests per minute. Request and token quota must cover the real peak concurrency of each shift. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. Local study-map skill 1.4 (Quotas, Scaling, and Cost), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: Request and token quota must cover the real peak concurrency of each shift.
- **B:** Correct. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. In this case: Request and token quota must cover the real peak concurrency of each shift.
- **C:** Incorrect for this question. User behavior, data, and models change. Rolling baselines reveal degradation that a one-time evaluation misses. Why the correct answer wins: Request and token quota must cover the real peak concurrency of each shift.
- **D:** Incorrect for this question. Retries, tool calls, evaluation, and review contribute to unit economics. Per-outcome cost supports better optimization. Why the correct answer wins: Request and token quota must cover the real peak concurrency of each shift.

### Question 8 — C

Answer: Track cost per accepted task, not only per token. Caching repeated manual content avoids re-billing identical prefix tokens. Retries, tool calls, evaluation, and review contribute to unit economics. Per-outcome cost supports better optimization. Local study-map skill 1.4 (Quotas, Scaling, and Cost), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Token analytics supports cost and performance tuning. Attribute usage to features and tenants where possible. Why the correct answer wins: Caching repeated manual content avoids re-billing identical prefix tokens.
- **B:** Incorrect for this question. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. Why the correct answer wins: Caching repeated manual content avoids re-billing identical prefix tokens.
- **C:** Correct. Retries, tool calls, evaluation, and review contribute to unit economics. Per-outcome cost supports better optimization. In this case: Caching repeated manual content avoids re-billing identical prefix tokens.
- **D:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Caching repeated manual content avoids re-billing identical prefix tokens.

### Question 9 — C

Answer: Use Azure Monitor and Application Insights for telemetry. Platform monitoring collects metrics and logs for operational visibility. Central telemetry captures latency, errors, dependencies, and custom events. Redact sensitive content before logging. Local study-map skill 1.5 (Monitoring Performance, Drift, Safety, and Grounding), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Audit evidence supports investigation and accountability. Protect log integrity and retention. Why the correct answer wins: Platform monitoring collects metrics and logs for operational visibility.
- **B:** Incorrect for this question. Alerts turn monitoring into action. Route them to an accountable owner with a runbook. Why the correct answer wins: Platform monitoring collects metrics and logs for operational visibility.
- **C:** Correct. Central telemetry captures latency, errors, dependencies, and custom events. Redact sensitive content before logging. In this case: Platform monitoring collects metrics and logs for operational visibility.
- **D:** Incorrect for this question. User behavior, data, and models change. Rolling baselines reveal degradation that a one-time evaluation misses. Why the correct answer wins: Platform monitoring collects metrics and logs for operational visibility.

### Question 10 — B, E

Answers: Monitor input and quality drift over time; Alert on latency, error rate, safety, and cost thresholds. Drift detection identifies distribution change, and alerting notifies the team when it occurs. User behavior, data, and models change. Rolling baselines reveal degradation that a one-time evaluation misses. Alerts turn monitoring into action. Route them to an accountable owner with a runbook. Local study-map skill 1.5 (Monitoring Performance, Drift, Safety, and Grounding), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Retries, tool calls, evaluation, and review contribute to unit economics. Per-outcome cost supports better optimization. Why the correct answer wins: Drift detection identifies distribution change, and alerting notifies the team when it occurs.
- **B:** Correct. Alerts turn monitoring into action. Route them to an accountable owner with a runbook. In this case: Drift detection identifies distribution change, and alerting notifies the team when it occurs.
- **C:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Drift detection identifies distribution change, and alerting notifies the team when it occurs.
- **D:** Incorrect for this question. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. Why the correct answer wins: Drift detection identifies distribution change, and alerting notifies the team when it occurs.
- **E:** Correct. User behavior, data, and models change. Rolling baselines reveal degradation that a one-time evaluation misses. In this case: Drift detection identifies distribution change, and alerting notifies the team when it occurs.

### Question 11 — C, E

Answers: Authenticate with a managed identity instead of keys; Use least-privilege Azure RBAC roles for the workload identity. A managed identity removes stored credentials, and a least-privilege role limits permissions. Managed identities avoid embedded secrets and support role-based access. Assign only required data-plane roles. Roles should match the operations the app or agent performs. Broad contributor access increases blast radius. Local study-map skill 1.6 (Security, Identity, and Networking), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Private connectivity keeps service traffic on approved network paths. Pair it with private DNS so clients resolve the private address. Why the correct answer wins: A managed identity removes stored credentials, and a least-privilege role limits permissions.
- **B:** Incorrect for this question. Filters assign severity and can block or annotate content. Thresholds should reflect the use case and applicable policy. Why the correct answer wins: A managed identity removes stored credentials, and a least-privilege role limits permissions.
- **C:** Correct. Managed identities avoid embedded secrets and support role-based access. Assign only required data-plane roles. In this case: A managed identity removes stored credentials, and a least-privilege role limits permissions.
- **D:** Incorrect for this question. A managed secret store supports rotation and access control. Secrets should never appear in prompts, code, or logs. Why the correct answer wins: A managed identity removes stored credentials, and a least-privilege role limits permissions.
- **E:** Correct. Roles should match the operations the app or agent performs. Broad contributor access increases blast radius. In this case: A managed identity removes stored credentials, and a least-privilege role limits permissions.

### Question 12 — B

Answer: Enforce constraints in code and platform policy. A guardrail constrains the assistant's behaviour for defined prohibited topics. Guardrails are technical controls, not prompt suggestions. Validate inputs, authorize tools, and limit egress. Local study-map skill 1.7 (Responsible AI Controls and Oversight), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Oversight settings bound what an agent may do autonomously. They should be tested against realistic misuse and failure. Why the correct answer wins: A guardrail constrains the assistant's behaviour for defined prohibited topics.
- **B:** Correct. Guardrails are technical controls, not prompt suggestions. Validate inputs, authorize tools, and limit egress. In this case: A guardrail constrains the assistant's behaviour for defined prohibited topics.
- **C:** Incorrect for this question. Audit evidence supports investigation and accountability. Protect log integrity and retention. Why the correct answer wins: A guardrail constrains the assistant's behaviour for defined prohibited topics.
- **D:** Incorrect for this question. Approval must occur before the effect and identify who approved what. A model confidence score is not approval. Why the correct answer wins: A guardrail constrains the assistant's behaviour for defined prohibited topics.

### Question 13 — A

Answer: Detect protected or copyrighted material in output. Protected-material detection flags or blocks known copyrighted output. Detection can reduce distribution risk for generated content. Policy and licensing review still apply. Local study-map skill 1.7 (Responsible AI Controls and Oversight), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. Detection can reduce distribution risk for generated content. Policy and licensing review still apply. In this case: Protected-material detection flags or blocks known copyrighted output.
- **B:** Incorrect for this question. Brand controls define permitted logos, styles, and claims. Technical generation must still pass approval. Why the correct answer wins: Protected-material detection flags or blocks known copyrighted output.
- **C:** Incorrect for this question. Filters assign severity and can block or annotate content. Thresholds should reflect the use case and applicable policy. Why the correct answer wins: Protected-material detection flags or blocks known copyrighted output.
- **D:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Protected-material detection flags or blocks known copyrighted output.

### Question 14 — C

Answer: Ground responses with retrieval-augmented generation. RAG retrieves current approved evidence and supports citations. RAG supplies selected source content at request time so answers can cite current evidence. It reduces but does not eliminate fabrication. Local study-map skill 2.1 (Building Generative Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Translating the request does not replace retrieval, grounding, or validation, so it cannot satisfy an evidence or citation requirement. Why the correct answer wins: RAG retrieves current approved evidence and supports citations.
- **B:** Incorrect for this question. Checkpoints validate intermediate results before later steps depend on them. This limits error propagation. Why the correct answer wins: RAG retrieves current approved evidence and supports citations.
- **C:** Correct. RAG supplies selected source content at request time so answers can cite current evidence. It reduces but does not eliminate fabrication. In this case: RAG retrieves current approved evidence and supports citations.
- **D:** Incorrect for this question. Routing can balance quality and cost. Fallback and evaluation are required. Why the correct answer wins: RAG retrieves current approved evidence and supports citations.

### Question 15 — D

Answer: Return a defined JSON schema for downstream systems. Schema-constrained output supports automated validation and record creation. Structured output supports validation and automation. Schema validity does not prove semantic correctness. Local study-map skill 2.1 (Building Generative Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Schema-constrained output supports automated validation and record creation.
- **B:** Incorrect for this question. Templates improve consistency and reviewability. Version them and test changes. Why the correct answer wins: Schema-constrained output supports automated validation and record creation.
- **C:** Incorrect for this question. Checkpoints validate intermediate results before later steps depend on them. This limits error propagation. Why the correct answer wins: Schema-constrained output supports automated validation and record creation.
- **D:** Correct. Structured output supports validation and automation. Schema validity does not prove semantic correctness. In this case: Schema-constrained output supports automated validation and record creation.

### Question 16 — A

Answer: Design multistep workflows with explicit checkpoints. Explicit stages with validation before any downstream action. Checkpoints validate intermediate results before later steps depend on them. This limits error propagation. Local study-map skill 2.1 (Building Generative Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Checkpoints validate intermediate results before later steps depend on them. This limits error propagation. In this case: Explicit stages with validation before any downstream action.
- **B:** Incorrect for this question. Autonomous workflows need bounded actions and escalation. Unbounded loops and broad tools increase risk. Why the correct answer wins: Explicit stages with validation before any downstream action.
- **C:** Incorrect for this question. A single call cannot validate intermediate results or fetch authoritative evidence, so it is unsuitable for multi-stage or grounded workflows. Why the correct answer wins: Explicit stages with validation before any downstream action.
- **D:** Incorrect for this question. Routing can balance quality and cost. Fallback and evaluation are required. Why the correct answer wins: Explicit stages with validation before any downstream action.

### Question 17 — C

Answer: Use a Foundry SDK or supported connector from application code. A supported Foundry SDK provides maintained client behaviour instead of raw HTTP calls. SDKs provide supported request and response patterns. Pin versions and handle retries, timeouts, and errors explicitly. Local study-map skill 2.2 (Foundry SDK and Project Integration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Repeatable deployments reduce configuration drift. Include model deployments, indexes, and connections in review and promotion. Why the correct answer wins: A supported Foundry SDK provides maintained client behaviour instead of raw HTTP calls.
- **B:** Incorrect for this question. Batch deployments can lower cost for large asynchronous jobs. They are unsuitable for interactive agent turns. Why the correct answer wins: A supported Foundry SDK provides maintained client behaviour instead of raw HTTP calls.
- **C:** Correct. SDKs provide supported request and response patterns. Pin versions and handle retries, timeouts, and errors explicitly. In this case: A supported Foundry SDK provides maintained client behaviour instead of raw HTTP calls.
- **D:** Incorrect for this question. Manual portal changes work for exploration but are slow, undocumented, and hard to reproduce, so they are a poor fit for governed release processes. Why the correct answer wins: A supported Foundry SDK provides maintained client behaviour instead of raw HTTP calls.

### Question 18 — B

Answer: Connect the application to the Foundry project endpoint. The project endpoint binds the client to that project and its deployments. Project endpoints and SDK clients bind an app to approved models and resources. Use identity-based authentication and environment-specific configuration. Local study-map skill 2.2 (Foundry SDK and Project Integration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. A managed secret store supports rotation and access control. Secrets should never appear in prompts, code, or logs. Why the correct answer wins: The project endpoint binds the client to that project and its deployments.
- **B:** Correct. Project endpoints and SDK clients bind an app to approved models and resources. Use identity-based authentication and environment-specific configuration. In this case: The project endpoint binds the client to that project and its deployments.
- **C:** Incorrect for this question. The catalog shows supported models with capability, modality, region, and lifecycle details. Verify availability for your subscription and region before designing around one model. Why the correct answer wins: The project endpoint binds the client to that project and its deployments.
- **D:** Incorrect for this question. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. Why the correct answer wins: The project endpoint binds the client to that project and its deployments.

### Question 19 — B, C

Answers: Build a representative golden dataset from real tasks; Re-run evaluation suites after meaningful changes. A golden dataset holds the benchmark, and regression evaluation rechecks known failure cases. A golden set anchors evaluation in expected behavior. Include edge cases and high-risk scenarios. Prompts, models, indexes, and tools all affect behavior. Regression tests catch unintended effects. Local study-map skill 2.3 (Evaluating Models and Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: A golden dataset holds the benchmark, and regression evaluation rechecks known failure cases.
- **B:** Correct. Prompts, models, indexes, and tools all affect behavior. Regression tests catch unintended effects. In this case: A golden dataset holds the benchmark, and regression evaluation rechecks known failure cases.
- **C:** Correct. A golden set anchors evaluation in expected behavior. Include edge cases and high-risk scenarios. In this case: A golden dataset holds the benchmark, and regression evaluation rechecks known failure cases.
- **D:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: A golden dataset holds the benchmark, and regression evaluation rechecks known failure cases.
- **E:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: A golden dataset holds the benchmark, and regression evaluation rechecks known failure cases.

### Question 20 — B

Answer: Use evaluators for quality, safety, and groundedness. Evaluators produce comparable quality scores across variants. Evaluators provide repeatable signals across models and prompts. They must be calibrated against human judgment for high-impact work. Local study-map skill 2.3 (Evaluating Models and Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Alerts turn monitoring into action. Route them to an accountable owner with a runbook. Why the correct answer wins: Evaluators produce comparable quality scores across variants.
- **B:** Correct. Evaluators provide repeatable signals across models and prompts. They must be calibrated against human judgment for high-impact work. In this case: Evaluators produce comparable quality scores across variants.
- **C:** Incorrect for this question. Audit evidence supports investigation and accountability. Protect log integrity and retention. Why the correct answer wins: Evaluators produce comparable quality scores across variants.
- **D:** Incorrect for this question. Central telemetry captures latency, errors, dependencies, and custom events. Redact sensitive content before logging. Why the correct answer wins: Evaluators produce comparable quality scores across variants.

### Question 21 — C

Answer: Define narrow tool schemas with clear descriptions. A precise tool schema with typed parameters prevents malformed arguments. Precise schemas help the model choose tools and arguments correctly. Broad or ambiguous tools invite unsafe calls. Local study-map skill 2.4 (Agent Roles, Goals, and Tool Schemas), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. System messages define role and constraints. They are not a security boundary against injection. Why the correct answer wins: A precise tool schema with typed parameters prevents malformed arguments.
- **B:** Incorrect for this question. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Why the correct answer wins: A precise tool schema with typed parameters prevents malformed arguments.
- **C:** Correct. Precise schemas help the model choose tools and arguments correctly. Broad or ambiguous tools invite unsafe calls. In this case: A precise tool schema with typed parameters prevents malformed arguments.
- **D:** Incorrect for this question. Templates improve consistency and reviewability. Version them and test changes. Why the correct answer wins: A precise tool schema with typed parameters prevents malformed arguments.

### Question 22 — A, E

Answers: Put stable behavior rules in the system message; Use managed conversation state or memory for continuity. The system message sets persistent behaviour, and conversation memory retains context. System messages define role and constraints. They are not a security boundary against injection. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Local study-map skill 2.4 (Agent Roles, Goals, and Tool Schemas), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. System messages define role and constraints. They are not a security boundary against injection. In this case: The system message sets persistent behaviour, and conversation memory retains context.
- **B:** Incorrect for this question. Precise schemas help the model choose tools and arguments correctly. Broad or ambiguous tools invite unsafe calls. Why the correct answer wins: The system message sets persistent behaviour, and conversation memory retains context.
- **C:** Incorrect for this question. OpenAPI tools describe supported HTTP operations for agent use. Narrow operations, validate inputs, and authenticate the caller. Why the correct answer wins: The system message sets persistent behaviour, and conversation memory retains context.
- **D:** Incorrect for this question. RAG supplies selected source content at request time so answers can cite current evidence. It reduces but does not eliminate fabrication. Why the correct answer wins: The system message sets persistent behaviour, and conversation memory retains context.
- **E:** Correct. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. In this case: The system message sets persistent behaviour, and conversation memory retains context.

### Question 23 — D

Answer: Expose an OpenAPI operation as an agent tool. An OpenAPI tool reuses the published contract without hand-written wrappers. OpenAPI tools describe supported HTTP operations for agent use. Narrow operations, validate inputs, and authenticate the caller. Local study-map skill 2.5 (Agent Tools, Retrieval, Memory, and Function Calling), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. RAG supplies selected source content at request time so answers can cite current evidence. It reduces but does not eliminate fabrication. Why the correct answer wins: An OpenAPI tool reuses the published contract without hand-written wrappers.
- **B:** Incorrect for this question. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. Why the correct answer wins: An OpenAPI tool reuses the published contract without hand-written wrappers.
- **C:** Incorrect for this question. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Why the correct answer wins: An OpenAPI tool reuses the published contract without hand-written wrappers.
- **D:** Correct. OpenAPI tools describe supported HTTP operations for agent use. Narrow operations, validate inputs, and authenticate the caller. In this case: An OpenAPI tool reuses the published contract without hand-written wrappers.

### Question 24 — B

Answer: Run agents in a fixed sequence. A sequential pattern runs stages in a defined order, with each stage using the previous output. Sequential orchestration makes dependencies explicit. It may add latency where steps could run concurrently. Local study-map skill 2.6 (Multi-Agent Orchestration and Safeguards), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Parallel execution reduces wall-clock time for independent work. Reconciliation still requires design. Why the correct answer wins: A sequential pattern runs stages in a defined order, with each stage using the previous output.
- **B:** Correct. Sequential orchestration makes dependencies explicit. It may add latency where steps could run concurrently. In this case: A sequential pattern runs stages in a defined order, with each stage using the previous output.
- **C:** Incorrect for this question. A manager routes tasks and merges results. Clear responsibility and failure handling are required. Why the correct answer wins: A sequential pattern runs stages in a defined order, with each stage using the previous output.
- **D:** Incorrect for this question. Reflection can catch omissions and inconsistencies. It can also reinforce errors, so validate against evidence. Why the correct answer wins: A sequential pattern runs stages in a defined order, with each stage using the previous output.

### Question 25 — C

Answer: Use a manager agent to coordinate specialists. A manager agent routes to specialists and consolidates their replies. A manager routes tasks and merges results. Clear responsibility and failure handling are required. Local study-map skill 2.6 (Multi-Agent Orchestration and Safeguards), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Reflection can catch omissions and inconsistencies. It can also reinforce errors, so validate against evidence. Why the correct answer wins: A manager agent routes to specialists and consolidates their replies.
- **B:** Incorrect for this question. Handoffs should carry goal, evidence, permissions, and open questions. Implicit context is easily lost. Why the correct answer wins: A manager agent routes to specialists and consolidates their replies.
- **C:** Correct. A manager routes tasks and merges results. Clear responsibility and failure handling are required. In this case: A manager agent routes to specialists and consolidates their replies.
- **D:** Incorrect for this question. Parallel execution reduces wall-clock time for independent work. Reconciliation still requires design. Why the correct answer wins: A manager agent routes to specialists and consolidates their replies.

### Question 26 — C

Answer: Detect alert → inspect traces → isolate the failing step → apply fix → verify with regression evaluation. Alert, traces, isolation, fix, then regression verification in that order. Triage moves from signal to evidence to a targeted fix, then proves the fix with regression tests. Local study-map skill 2.7 (Agent Monitoring and Error Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Verification before a fix and before diagnosis proves nothing. Why the correct answer wins: Alert, traces, isolation, fix, then regression verification in that order.
- **B:** Incorrect for this question. A fix cannot precede detection and diagnosis. Why the correct answer wins: Alert, traces, isolation, fix, then regression verification in that order.
- **C:** Correct. Triage moves from signal to evidence to a targeted fix, then proves the fix with regression tests. In this case: Alert, traces, isolation, fix, then regression verification in that order.
- **D:** Incorrect for this question. The alert must be detected first, and traces must be inspected before the step is isolated. Why the correct answer wins: Alert, traces, isolation, fix, then regression verification in that order.

### Question 27 — B

Answer: Lower temperature for more deterministic extraction. Lower temperature reduces sampling variability for deterministic extraction. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Local study-map skill 2.8 (Generation Tuning and Observability), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Top-p narrows or broadens token sampling. Tune with evaluation rather than by intuition. Why the correct answer wins: Lower temperature reduces sampling variability for deterministic extraction.
- **B:** Correct. Lower temperature reduces sampling variability. It does not guarantee factual correctness. In this case: Lower temperature reduces sampling variability for deterministic extraction.
- **C:** Incorrect for this question. Routing can balance quality and cost. Fallback and evaluation are required. Why the correct answer wins: Lower temperature reduces sampling variability for deterministic extraction.
- **D:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Lower temperature reduces sampling variability for deterministic extraction.

### Question 28 — D

Answer: Generate images from text and reference media. Image generation produces a new illustration from a description. Image generation supports creative and product workflows. Apply policy, watermarking, and provenance controls. Local study-map skill 3.1 (Image Generation and Editing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Alt text should convey purpose and essential content, not decorative detail. Human review is still needed for critical pages. Why the correct answer wins: Image generation produces a new illustration from a description.
- **B:** Incorrect for this question. Video generation creates clips from prompts or images. Duration, consistency, and safety require review. Why the correct answer wins: Image generation produces a new illustration from a description.
- **C:** Incorrect for this question. Inpainting changes a selected area while preserving the rest. Validate identity, brand, and safety constraints. Why the correct answer wins: Image generation produces a new illustration from a description.
- **D:** Correct. Image generation supports creative and product workflows. Apply policy, watermarking, and provenance controls. In this case: Image generation produces a new illustration from a description.

### Question 29 — B

Answer: Edit a region of an image with a mask. Mask-based inpainting edits only the selected region. Inpainting changes a selected area while preserving the rest. Validate identity, brand, and safety constraints. Local study-map skill 3.1 (Image Generation and Editing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Video editing can revise scenes or timing. Preserve provenance and review for harmful manipulation. Why the correct answer wins: Mask-based inpainting edits only the selected region.
- **B:** Correct. Inpainting changes a selected area while preserving the rest. Validate identity, brand, and safety constraints. In this case: Mask-based inpainting edits only the selected region.
- **C:** Incorrect for this question. Prompt-based edits can alter style or content. Review outputs for unintended changes and policy violations. Why the correct answer wins: Mask-based inpainting edits only the selected region.
- **D:** Incorrect for this question. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Why the correct answer wins: Mask-based inpainting edits only the selected region.

### Question 30 — B

Answer: Analyze video segments for events and content. Video analysis locates events and timestamps within existing footage. Video analysis can summarize or detect events across time. Sampling strategy affects coverage and cost. Local study-map skill 3.2 (Video Generation and Editing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Video generation creates clips from prompts or images. Duration, consistency, and safety require review. Why the correct answer wins: Video analysis locates events and timestamps within existing footage.
- **B:** Correct. Video analysis can summarize or detect events across time. Sampling strategy affects coverage and cost. In this case: Video analysis locates events and timestamps within existing footage.
- **C:** Incorrect for this question. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Why the correct answer wins: Video analysis locates events and timestamps within existing footage.
- **D:** Incorrect for this question. Video editing can revise scenes or timing. Preserve provenance and review for harmful manipulation. Why the correct answer wins: Video analysis locates events and timestamps within existing footage.

### Question 31 — D

Answer: Upload image → validate format and size → send multimodal request → parse structured fields → route low-confidence values to review. Validation brackets the multimodal call, and low-confidence results go to review. Validation and structured parsing bracket the multimodal call, and low-confidence output goes to people. Local study-map skill 3.4 (Visual Extraction and Video Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Parsing requires a response, which requires an uploaded and validated image. Why the correct answer wins: Validation brackets the multimodal call, and low-confidence results go to review.
- **B:** Incorrect for this question. Review cannot precede the request, and parsing must follow the response. Why the correct answer wins: Validation brackets the multimodal call, and low-confidence results go to review.
- **C:** Incorrect for this question. A request cannot precede the upload, and validation must come before the call. Why the correct answer wins: Validation brackets the multimodal call, and low-confidence results go to review.
- **D:** Correct. Validation and structured parsing bracket the multimodal call, and low-confidence output goes to people. In this case: Validation brackets the multimodal call, and low-confidence results go to review.

### Question 32 — C, E

Answers: Answer questions grounded in visual evidence; Generate alt text aligned to accessibility guidance. Alt text serves accessibility, and visual question answering grounds answers in image content. Visual question answering should cite the relevant region or content. Avoid answering beyond what the image supports. Alt text should convey purpose and essential content, not decorative detail. Human review is still needed for critical pages. Local study-map skill 3.3 (Multimodal Understanding and Accessibility), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Why the correct answer wins: Alt text serves accessibility, and visual question answering grounds answers in image content.
- **B:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Alt text serves accessibility, and visual question answering grounds answers in image content.
- **C:** Correct. Visual question answering should cite the relevant region or content. Avoid answering beyond what the image supports. In this case: Alt text serves accessibility, and visual question answering grounds answers in image content.
- **D:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Alt text serves accessibility, and visual question answering grounds answers in image content.
- **E:** Correct. Alt text should convey purpose and essential content, not decorative detail. Human review is still needed for critical pages. In this case: Alt text serves accessibility, and visual question answering grounds answers in image content.

### Question 33 — C

Answer: Use pro mode for complex multimodal content understanding. Pro mode handles complex multi-page multimodal content. Pro mode handles more demanding layouts and multimodal inputs at higher cost. Use it where simpler modes fail requirements. Local study-map skill 3.4 (Visual Extraction and Video Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Custom models fit specialized forms not covered by prebuilts. They require representative labels and retraining discipline. Why the correct answer wins: Pro mode handles complex multi-page multimodal content.
- **B:** Incorrect for this question. Single-task analyzers target one content type or objective. They may be simpler and cheaper than general pro-mode pipelines. Why the correct answer wins: Pro mode handles complex multi-page multimodal content.
- **C:** Correct. Pro mode handles more demanding layouts and multimodal inputs at higher cost. Use it where simpler modes fail requirements. In this case: Pro mode handles complex multi-page multimodal content.
- **D:** Incorrect for this question. Document Intelligence provides prebuilt and custom extraction for structured documents. Validate field accuracy on representative samples. Why the correct answer wins: Pro mode handles complex multi-page multimodal content.

### Question 34 — A, E

Answers: Enforce brand and usage rules for generated visuals; Filter unsafe or disallowed visual content. Brand policy constrains approved visual usage, and visual filters block unsafe imagery. Brand controls define permitted logos, styles, and claims. Technical generation must still pass approval. Image and video safety filters reduce exposure to harmful content. Thresholds and human escalation should match policy. Local study-map skill 3.5 (Multimodal Responsible AI), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Correct. Brand controls define permitted logos, styles, and claims. Technical generation must still pass approval. In this case: Brand policy constrains approved visual usage, and visual filters block unsafe imagery.
- **B:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Brand policy constrains approved visual usage, and visual filters block unsafe imagery.
- **C:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Brand policy constrains approved visual usage, and visual filters block unsafe imagery.
- **D:** Incorrect for this question. Top-p narrows or broadens token sampling. Tune with evaluation rather than by intuition. Why the correct answer wins: Brand policy constrains approved visual usage, and visual filters block unsafe imagery.
- **E:** Correct. Image and video safety filters reduce exposure to harmful content. Thresholds and human escalation should match policy. In this case: Brand policy constrains approved visual usage, and visual filters block unsafe imagery.

### Question 35 — B

Answer: Prompt for JSON that conforms to a supplied schema. Schema-constrained JSON supports validation and automation. Schema-guided generation improves machine readability. Validate values against source evidence and business rules. Local study-map skill 4.1 (Language Model Text Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Topic extraction supports discovery and grouping. It is not a substitute for an authoritative taxonomy. Why the correct answer wins: Schema-constrained JSON supports validation and automation.
- **B:** Correct. Schema-guided generation improves machine readability. Validate values against source evidence and business rules. In this case: Schema-constrained JSON supports validation and automation.
- **C:** Incorrect for this question. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Why the correct answer wins: Schema-constrained JSON supports validation and automation.
- **D:** Incorrect for this question. Translation should preserve meaning, names, and formatting. Evaluate domain terminology and low-resource languages. Why the correct answer wins: Schema-constrained JSON supports validation and automation.

### Question 36 — B, E

Answers: Detect and redact sensitive personal data; Analyze sentiment and tone with an appropriate service. PII detection finds personal data, and sentiment detects frustration. Sensitive Data Protection or language PII detection can identify and mask data. Verify that redaction covers every path where content flows. Sentiment analysis can support triage and monitoring. Domain and language variation require validation. Local study-map skill 4.1 (Language Model Text Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Topic extraction supports discovery and grouping. It is not a substitute for an authoritative taxonomy. Why the correct answer wins: PII detection finds personal data, and sentiment detects frustration.
- **B:** Correct. Sensitive Data Protection or language PII detection can identify and mask data. Verify that redaction covers every path where content flows. In this case: PII detection finds personal data, and sentiment detects frustration.
- **C:** Incorrect for this question. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Why the correct answer wins: PII detection finds personal data, and sentiment detects frustration.
- **D:** Incorrect for this question. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Why the correct answer wins: PII detection finds personal data, and sentiment detects frustration.
- **E:** Correct. Sentiment analysis can support triage and monitoring. Domain and language variation require validation. In this case: PII detection finds personal data, and sentiment detects frustration.

### Question 37 — C

Answer: Apply a custom glossary or terminology list. A glossary enforces approved term mappings. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Local study-map skill 4.2 (Translation), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Translation should preserve meaning, names, and formatting. Evaluate domain terminology and low-resource languages. Why the correct answer wins: A glossary enforces approved term mappings.
- **B:** Incorrect for this question. Sensitive Data Protection or language PII detection can identify and mask data. Verify that redaction covers every path where content flows. Why the correct answer wins: A glossary enforces approved term mappings.
- **C:** Correct. Glossaries keep product and legal terms consistent. Terms still need human validation in context. In this case: A glossary enforces approved term mappings.
- **D:** Incorrect for this question. Entity extraction turns text into structured facts. Ambiguous mentions need resolution and validation. Why the correct answer wins: A glossary enforces approved term mappings.

### Question 38 — C

Answer: Transcribe speech to text with Azure AI Speech. Speech-to-text transcribes audio into searchable content. Speech-to-text enables voice agents and transcript analysis. Audio quality, accents, and domain terms affect accuracy. Local study-map skill 4.3 (Speech Solutions), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Text-to-speech supports voice responses and accessibility. Voice, prosody, and latency affect usability. Why the correct answer wins: Speech-to-text transcribes audio into searchable content.
- **B:** Incorrect for this question. Audio-capable models can summarize or answer questions about recordings. Verify transcription quality and evidence grounding. Why the correct answer wins: Speech-to-text transcribes audio into searchable content.
- **C:** Correct. Speech-to-text enables voice agents and transcript analysis. Audio quality, accents, and domain terms affect accuracy. In this case: Speech-to-text transcribes audio into searchable content.
- **D:** Incorrect for this question. Speech translation combines recognition and translation. Preserve timing and speaker context where needed. Why the correct answer wins: Speech-to-text transcribes audio into searchable content.

### Question 39 — B

Answer: Use a custom speech model for specialized vocabulary. A custom speech model adapts to the acoustics and vocabulary of the environment. Custom speech can improve recognition of domain terms. It requires representative audio and ongoing evaluation. Local study-map skill 4.3 (Speech Solutions), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Why the correct answer wins: A custom speech model adapts to the acoustics and vocabulary of the environment.
- **B:** Correct. Custom speech can improve recognition of domain terms. It requires representative audio and ongoing evaluation. In this case: A custom speech model adapts to the acoustics and vocabulary of the environment.
- **C:** Incorrect for this question. Speech-to-text enables voice agents and transcript analysis. Audio quality, accents, and domain terms affect accuracy. Why the correct answer wins: A custom speech model adapts to the acoustics and vocabulary of the environment.
- **D:** Incorrect for this question. Text-to-speech supports voice responses and accessibility. Voice, prosody, and latency affect usability. Why the correct answer wins: A custom speech model adapts to the acoustics and vocabulary of the environment.

### Question 40 — C

Answer: Generate summaries with explicit length and audience constraints. Summarization condenses long content into a shorter form. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Local study-map skill 4.4 (Domain Customization), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Topic extraction supports discovery and grouping. It is not a substitute for an authoritative taxonomy. Why the correct answer wins: Summarization condenses long content into a shorter form.
- **B:** Incorrect for this question. Entity extraction turns text into structured facts. Ambiguous mentions need resolution and validation. Why the correct answer wins: Summarization condenses long content into a shorter form.
- **C:** Correct. Summaries should preserve required facts and caveats. Fluency does not prove completeness. In this case: Summarization condenses long content into a shorter form.
- **D:** Incorrect for this question. Translation should preserve meaning, names, and formatting. Evaluate domain terminology and low-resource languages. Why the correct answer wins: Summarization condenses long content into a shorter form.

### Question 41 — C, E

Answers: Customize summaries and extraction for compliance needs; Adapt prompts and models to domain terminology. Compliance summarization preserves required disclosures, and a domain lexicon captures local terminology. Compliance work requires precise citation, retention, and review. Generic summarization is insufficient without controls. Domain adaptation improves consistency and recall. Validate against expert-created expected outputs. Local study-map skill 4.4 (Domain Customization), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Topic extraction supports discovery and grouping. It is not a substitute for an authoritative taxonomy. Why the correct answer wins: Compliance summarization preserves required disclosures, and a domain lexicon captures local terminology.
- **B:** Incorrect for this question. Sentiment analysis can support triage and monitoring. Domain and language variation require validation. Why the correct answer wins: Compliance summarization preserves required disclosures, and a domain lexicon captures local terminology.
- **C:** Correct. Domain adaptation improves consistency and recall. Validate against expert-created expected outputs. In this case: Compliance summarization preserves required disclosures, and a domain lexicon captures local terminology.
- **D:** Incorrect for this question. Translation should preserve meaning, names, and formatting. Evaluate domain terminology and low-resource languages. Why the correct answer wins: Compliance summarization preserves required disclosures, and a domain lexicon captures local terminology.
- **E:** Correct. Compliance work requires precise citation, retention, and review. Generic summarization is insufficient without controls. In this case: Compliance summarization preserves required disclosures, and a domain lexicon captures local terminology.

### Question 42 — C

Answer: Use an Azure AI Search indexer to pull source content. An indexer pulls source documents and tracks changes on a schedule. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. Local study-map skill 5.1 (Content Ingestion and Indexing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. OCR unlocks text in scans and screenshots. Layout and table structure may still require specialized extraction. Why the correct answer wins: An indexer pulls source documents and tracks changes on a schedule.
- **B:** Incorrect for this question. Skillsets can OCR, split, embed, and extract during indexing. Each skill adds latency, cost, and failure modes. Why the correct answer wins: An indexer pulls source documents and tracks changes on a schedule.
- **C:** Correct. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. In this case: An indexer pulls source documents and tracks changes on a schedule.
- **D:** Incorrect for this question. Push ingestion supports near-real-time updates from applications. The app owns batching, retries, and deletion. Why the correct answer wins: An indexer pulls source documents and tracks changes on a schedule.

### Question 43 — A

Answer: Push documents to an index through the data-plane API. Push ingestion sends documents to the index as soon as they are created. Push ingestion supports near-real-time updates from applications. The app owns batching, retries, and deletion. Local study-map skill 5.1 (Content Ingestion and Indexing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Correct. Push ingestion supports near-real-time updates from applications. The app owns batching, retries, and deletion. In this case: Push ingestion sends documents to the index as soon as they are created.
- **B:** Incorrect for this question. Removed content must stop appearing in answers. Test deletion propagation explicitly. Why the correct answer wins: Push ingestion sends documents to the index as soon as they are created.
- **C:** Incorrect for this question. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. Why the correct answer wins: Push ingestion sends documents to the index as soon as they are created.
- **D:** Incorrect for this question. Ingestion moves source content into a searchable index. Handle failures, updates, and deletions explicitly. Why the correct answer wins: Push ingestion sends documents to the index as soon as they are created.

### Question 44 — A

Answer: Ingest → extract text → chunk → embed → index → retrieve with citations. Extraction, chunking, embedding, and indexing precede retrieval and citation. The supported RAG ingestion order produces searchable, citable evidence. Retrieval cannot work before content is extracted, chunked, embedded, and indexed. Local study-map skill 5.4 (RAG Ingestion and OCR), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Correct. The supported RAG ingestion order produces searchable, citable evidence. Retrieval cannot work before content is extracted, chunked, embedded, and indexed. In this case: Extraction, chunking, embedding, and indexing precede retrieval and citation.
- **B:** Incorrect for this question. Indexing before extraction or embedding creates an empty or unusable index. Why the correct answer wins: Extraction, chunking, embedding, and indexing precede retrieval and citation.
- **C:** Incorrect for this question. Retrieval is attempted before the index exists and source ingestion is incomplete. Why the correct answer wins: Extraction, chunking, embedding, and indexing precede retrieval and citation.
- **D:** Incorrect for this question. Retrieval before chunking, embedding, and indexing has nothing searchable to return. Why the correct answer wins: Extraction, chunking, embedding, and indexing precede retrieval and citation.

### Question 45 — A

Answer: Pin the model version available in the required region. Pinning a version available in the region keeps behaviour stable and satisfies residency. A pinned version keeps behavior stable and satisfies residency, at the cost of slower access to newer capabilities. Local study-map skill 1.1 (Selecting Foundry Models and Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. A pinned version keeps behavior stable and satisfies residency, at the cost of slower access to newer capabilities. In this case: Pinning a version available in the region keeps behaviour stable and satisfies residency.
- **B:** Incorrect for this question. Large models handle ambiguity and multi-step reasoning better in many cases, at higher cost and latency. Select with measured evidence rather than brand preference. Why the correct answer wins: Pinning a version available in the region keeps behaviour stable and satisfies residency.
- **C:** Incorrect for this question. The catalog shows supported models with capability, modality, region, and lifecycle details. Verify availability for your subscription and region before designing around one model. Why the correct answer wins: Pinning a version available in the region keeps behaviour stable and satisfies residency.
- **D:** Incorrect for this question. A custom model is justified when supported prebuilt options cannot meet a defined requirement. It adds data, evaluation, and lifecycle obligations. Why the correct answer wins: Pinning a version available in the region keeps behaviour stable and satisfies residency.

### Question 46 — A

Answer: Use Foundry Tools for prebuilt vision, speech, language, and extraction needs. Prebuilt managed capabilities need no training corpus. Prebuilt managed capabilities can reduce custom model work where their behavior and limits fit the task. They are not a substitute for task-specific validation. Local study-map skill 1.1 (Selecting Foundry Models and Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. Prebuilt managed capabilities can reduce custom model work where their behavior and limits fit the task. They are not a substitute for task-specific validation. In this case: Prebuilt managed capabilities need no training corpus.
- **B:** Incorrect for this question. A custom model is justified when supported prebuilt options cannot meet a defined requirement. It adds data, evaluation, and lifecycle obligations. Why the correct answer wins: Prebuilt managed capabilities need no training corpus.
- **C:** Incorrect for this question. Large models handle ambiguity and multi-step reasoning better in many cases, at higher cost and latency. Select with measured evidence rather than brand preference. Why the correct answer wins: Prebuilt managed capabilities need no training corpus.
- **D:** Incorrect for this question. Small models can reduce latency and cost for constrained classification or extraction. Confirm quality on representative data before standardizing. Why the correct answer wins: Prebuilt managed capabilities need no training corpus.

### Question 47 — B

Answer: Expose an OpenAPI operation as an agent tool. An OpenAPI tool reuses the published contract. OpenAPI tools describe supported HTTP operations for agent use. Narrow operations, validate inputs, and authenticate the caller. Local study-map skill 1.2 (Retrieval, Memory, Tool, and Knowledge Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Why the correct answer wins: An OpenAPI tool reuses the published contract.
- **B:** Correct. OpenAPI tools describe supported HTTP operations for agent use. Narrow operations, validate inputs, and authenticate the caller. In this case: An OpenAPI tool reuses the published contract.
- **C:** Incorrect for this question. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. Why the correct answer wins: An OpenAPI tool reuses the published contract.
- **D:** Incorrect for this question. An index gives an agent curated, searchable evidence under configured access. Index content and permissions require ongoing ownership. Why the correct answer wins: An OpenAPI tool reuses the published contract.

### Question 48 — A

Answer: Block promotion in the pipeline when evaluation thresholds fail. An evaluation gate blocks promotion on a measured threshold. An automated gate turns an evaluation result into a release decision. Thresholds need ownership or the gate becomes noise. Local study-map skill 1.3 (Infrastructure, Deployment, and CI/CD), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. An automated gate turns an evaluation result into a release decision. Thresholds need ownership or the gate becomes noise. In this case: An evaluation gate blocks promotion on a measured threshold.
- **B:** Incorrect for this question. Repeatable deployments reduce configuration drift. Include model deployments, indexes, and connections in review and promotion. Why the correct answer wins: An evaluation gate blocks promotion on a measured threshold.
- **C:** Incorrect for this question. A canary limits blast radius and produces real signal before full rollout. It needs a rollback criterion defined in advance. Why the correct answer wins: An evaluation gate blocks promotion on a measured threshold.
- **D:** Incorrect for this question. Canary or phased rollout limits exposure. Rollback must be tested, not just documented. Why the correct answer wins: An evaluation gate blocks promotion on a measured threshold.

### Question 49 — A

Answer: Send mirrored production traffic to a candidate without returning its answers. Shadow deployment mirrors traffic and discards candidate output. Shadow traffic compares a candidate against live behavior with no user impact. It requires careful handling of side-effecting calls. Local study-map skill 1.3 (Infrastructure, Deployment, and CI/CD), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. Shadow traffic compares a candidate against live behavior with no user impact. It requires careful handling of side-effecting calls. In this case: Shadow deployment mirrors traffic and discards candidate output.
- **B:** Incorrect for this question. Standard deployments bill per token and scale within quota. They suit spiky or early workloads. Why the correct answer wins: Shadow deployment mirrors traffic and discards candidate output.
- **C:** Incorrect for this question. A canary limits blast radius and produces real signal before full rollout. It needs a rollback criterion defined in advance. Why the correct answer wins: Shadow deployment mirrors traffic and discards candidate output.
- **D:** Incorrect for this question. Batch deployments can lower cost for large asynchronous jobs. They are unsuitable for interactive agent turns. Why the correct answer wins: Shadow deployment mirrors traffic and discards candidate output.

### Question 50 — D

Answer: Alert on spend thresholds per deployment or project. A spend alert notifies owners as usage crosses a threshold. Spend alerts catch runaway usage before the invoice does. They are detection, not a hard spending cap. Local study-map skill 1.4 (Quotas, Scaling, and Cost), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. Why the correct answer wins: A spend alert notifies owners as usage crosses a threshold.
- **B:** Incorrect for this question. Token analytics supports cost and performance tuning. Attribute usage to features and tenants where possible. Why the correct answer wins: A spend alert notifies owners as usage crosses a threshold.
- **C:** Incorrect for this question. Retries, tool calls, evaluation, and review contribute to unit economics. Per-outcome cost supports better optimization. Why the correct answer wins: A spend alert notifies owners as usage crosses a threshold.
- **D:** Correct. Spend alerts catch runaway usage before the invoice does. They are detection, not a hard spending cap. In this case: A spend alert notifies owners as usage crosses a threshold.

### Question 51 — B

Answer: Monitor index freshness, failures, and document counts. Index health checks catch stale content. Stale or partially indexed content produces confident but wrong answers. Alert on ingestion and deletion failures. Local study-map skill 1.5 (Monitoring Performance, Drift, Safety, and Grounding), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. User behavior, data, and models change. Rolling baselines reveal degradation that a one-time evaluation misses. Why the correct answer wins: Index health checks catch stale content.
- **B:** Correct. Stale or partially indexed content produces confident but wrong answers. Alert on ingestion and deletion failures. In this case: Index health checks catch stale content.
- **C:** Incorrect for this question. Central telemetry captures latency, errors, dependencies, and custom events. Redact sensitive content before logging. Why the correct answer wins: Index health checks catch stale content.
- **D:** Incorrect for this question. Groundedness checks whether claims are supported by retrieved evidence. Sampling and human review complement automated scores. Why the correct answer wins: Index health checks catch stale content.

### Question 52 — B

Answer: Restrict outbound network access to approved destinations. Egress rules restrict which external destinations the workload can reach, which is exactly the control the policy demands. Egress controls reduce exfiltration and unauthorized tool reach. Combine with identity and data controls. Local study-map skill 1.6 (Security, Identity, and Networking), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Roles should match the operations the app or agent performs. Broad contributor access increases blast radius. Why the correct answer wins: Egress rules restrict which external destinations the workload can reach, which is exactly the control the policy demands.
- **B:** Correct. Egress controls reduce exfiltration and unauthorized tool reach. Combine with identity and data controls. In this case: Egress rules restrict which external destinations the workload can reach, which is exactly the control the policy demands.
- **C:** Incorrect for this question. Private connectivity keeps service traffic on approved network paths. Pair it with private DNS so clients resolve the private address. Why the correct answer wins: Egress rules restrict which external destinations the workload can reach, which is exactly the control the policy demands.
- **D:** Incorrect for this question. Leaving the public path open defeats the purpose of a private networking design because traffic can still bypass the private route. Why the correct answer wins: Egress rules restrict which external destinations the workload can reach, which is exactly the control the policy demands.

### Question 53 — A

Answer: Set agent oversight mode and tool-access constraints. Human oversight keeps consequential actions accountable. Oversight settings bound what an agent may do autonomously. They should be tested against realistic misuse and failure. Local study-map skill 1.7 (Responsible AI Controls and Oversight), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. Oversight settings bound what an agent may do autonomously. They should be tested against realistic misuse and failure. In this case: Human oversight keeps consequential actions accountable.
- **B:** Incorrect for this question. Guardrails are technical controls, not prompt suggestions. Validate inputs, authorize tools, and limit egress. Why the correct answer wins: Human oversight keeps consequential actions accountable.
- **C:** Incorrect for this question. Approval must occur before the effect and identify who approved what. A model confidence score is not approval. Why the correct answer wins: Human oversight keeps consequential actions accountable.
- **D:** Incorrect for this question. Audit evidence supports investigation and accountability. Protect log integrity and retention. Why the correct answer wins: Human oversight keeps consequential actions accountable.

### Question 54 — C

Answer: Use batch processing for latency-tolerant bulk work. Batch deployment suits large asynchronous jobs. Batch deployments can lower cost for large asynchronous jobs. They are unsuitable for interactive agent turns. Local study-map skill 1.4 (Quotas, Scaling, and Cost), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: Batch deployment suits large asynchronous jobs.
- **B:** Incorrect for this question. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. Why the correct answer wins: Batch deployment suits large asynchronous jobs.
- **C:** Correct. Batch deployments can lower cost for large asynchronous jobs. They are unsuitable for interactive agent turns. In this case: Batch deployment suits large asynchronous jobs.
- **D:** Incorrect for this question. Standard deployments bill per token and scale within quota. They suit spiky or early workloads. Why the correct answer wins: Batch deployment suits large asynchronous jobs.

### Question 55 — B, D

Answers: Compare supported models in the Foundry model catalog; Pin the model version available in the required region. Catalog review confirms local availability, and pinning prevents silent change. The catalog shows supported models with capability, modality, region, and lifecycle details. Verify availability for your subscription and region before designing around one model. A pinned version keeps behavior stable and satisfies residency, at the cost of slower access to newer capabilities. Local study-map skill 1.1 (Selecting Foundry Models and Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Batch deployments can lower cost for large asynchronous jobs. They are unsuitable for interactive agent turns. Why the correct answer wins: Catalog review confirms local availability, and pinning prevents silent change.
- **B:** Correct. The catalog shows supported models with capability, modality, region, and lifecycle details. Verify availability for your subscription and region before designing around one model. In this case: Catalog review confirms local availability, and pinning prevents silent change.
- **C:** Incorrect for this question. A custom model is justified when supported prebuilt options cannot meet a defined requirement. It adds data, evaluation, and lifecycle obligations. Why the correct answer wins: Catalog review confirms local availability, and pinning prevents silent change.
- **D:** Correct. A pinned version keeps behavior stable and satisfies residency, at the cost of slower access to newer capabilities. In this case: Catalog review confirms local availability, and pinning prevents silent change.
- **E:** Incorrect for this question. Standard deployments bill per token and scale within quota. They suit spiky or early workloads. Why the correct answer wins: Catalog review confirms local availability, and pinning prevents silent change.

### Question 56 — B, D

Answers: Monitor groundedness and citation quality in production; Alert on latency, error rate, safety, and cost thresholds. Groundedness monitoring detects unsupported answers, and alerting notifies the team. Groundedness checks whether claims are supported by retrieved evidence. Sampling and human review complement automated scores. Alerts turn monitoring into action. Route them to an accountable owner with a runbook. Local study-map skill 1.5 (Monitoring Performance, Drift, Safety, and Grounding), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Retries, tool calls, evaluation, and review contribute to unit economics. Per-outcome cost supports better optimization. Why the correct answer wins: Groundedness monitoring detects unsupported answers, and alerting notifies the team.
- **B:** Correct. Groundedness checks whether claims are supported by retrieved evidence. Sampling and human review complement automated scores. In this case: Groundedness monitoring detects unsupported answers, and alerting notifies the team.
- **C:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Groundedness monitoring detects unsupported answers, and alerting notifies the team.
- **D:** Correct. Alerts turn monitoring into action. Route them to an accountable owner with a runbook. In this case: Groundedness monitoring detects unsupported answers, and alerting notifies the team.
- **E:** Incorrect for this question. Users experience the whole path, not only generation. Optimize the dominant contributor. Why the correct answer wins: Groundedness monitoring detects unsupported answers, and alerting notifies the team.

### Question 57 — A, C

Answers: Restrict outbound network access to approved destinations; Use least-privilege Azure RBAC roles for the workload identity. Egress restrictions bound destinations, and least privilege bounds actions. Egress controls reduce exfiltration and unauthorized tool reach. Combine with identity and data controls. Roles should match the operations the app or agent performs. Broad contributor access increases blast radius. Local study-map skill 1.6 (Security, Identity, and Networking), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. Roles should match the operations the app or agent performs. Broad contributor access increases blast radius. In this case: Egress restrictions bound destinations, and least privilege bounds actions.
- **B:** Incorrect for this question. Filters assign severity and can block or annotate content. Thresholds should reflect the use case and applicable policy. Why the correct answer wins: Egress restrictions bound destinations, and least privilege bounds actions.
- **C:** Correct. Egress controls reduce exfiltration and unauthorized tool reach. Combine with identity and data controls. In this case: Egress restrictions bound destinations, and least privilege bounds actions.
- **D:** Incorrect for this question. A managed secret store supports rotation and access control. Secrets should never appear in prompts, code, or logs. Why the correct answer wins: Egress restrictions bound destinations, and least privilege bounds actions.
- **E:** Incorrect for this question. Private connectivity keeps service traffic on approved network paths. Pair it with private DNS so clients resolve the private address. Why the correct answer wins: Egress restrictions bound destinations, and least privilege bounds actions.

### Question 58 — D

Answer: Commit change → run the evaluation suite → block on failed thresholds → deploy a canary → promote after metrics hold. Evaluation runs before deployment, its thresholds gate promotion, and a canary limits exposure before full release. An evaluation gate before deployment, followed by a canary, keeps unmeasured changes away from all users. Local study-map skill 1.3 (Infrastructure, Deployment, and CI/CD), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Deployment cannot precede the change, and evaluation must gate promotion rather than follow it. Why the correct answer wins: Evaluation runs before deployment, its thresholds gate promotion, and a canary limits exposure before full release.
- **B:** Incorrect for this question. The change must exist before it can be evaluated or deployed. Why the correct answer wins: Evaluation runs before deployment, its thresholds gate promotion, and a canary limits exposure before full release.
- **C:** Incorrect for this question. Evaluation after promotion cannot prevent a failed change from reaching everyone. Why the correct answer wins: Evaluation runs before deployment, its thresholds gate promotion, and a canary limits exposure before full release.
- **D:** Correct. An evaluation gate before deployment, followed by a canary, keeps unmeasured changes away from all users. In this case: Evaluation runs before deployment, its thresholds gate promotion, and a canary limits exposure before full release.

### Question 59 — A

Answer: Set chunk overlap so facts spanning a boundary stay retrievable. Overlap preserves facts across chunk boundaries. Overlap preserves context across chunk edges at the cost of duplicated index storage and more near-duplicate hits. Local study-map skill 2.1 (Building Generative Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Overlap preserves context across chunk edges at the cost of duplicated index storage and more near-duplicate hits. In this case: Overlap preserves facts across chunk boundaries.
- **B:** Incorrect for this question. Chunking affects recall, precision, and context use. Respect document structure and test against real questions. Why the correct answer wins: Overlap preserves facts across chunk boundaries.
- **C:** Incorrect for this question. Embeddings determine semantic similarity behavior. Evaluate retrieval quality before and after changes. Why the correct answer wins: Overlap preserves facts across chunk boundaries.
- **D:** Incorrect for this question. More retrieved text is not always better. Order and compress evidence to preserve decisive facts. Why the correct answer wins: Overlap preserves facts across chunk boundaries.

### Question 60 — A

Answer: Ground responses with retrieval-augmented generation. Retrieval supplies current evidence with citations. RAG supplies selected source content at request time so answers can cite current evidence. It reduces but does not eliminate fabrication. Local study-map skill 2.1 (Building Generative Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. RAG supplies selected source content at request time so answers can cite current evidence. It reduces but does not eliminate fabrication. In this case: Retrieval supplies current evidence with citations.
- **B:** Incorrect for this question. Checkpoints validate intermediate results before later steps depend on them. This limits error propagation. Why the correct answer wins: Retrieval supplies current evidence with citations.
- **C:** Incorrect for this question. Routing can balance quality and cost. Fallback and evaluation are required. Why the correct answer wins: Retrieval supplies current evidence with citations.
- **D:** Incorrect for this question. Examples clarify format and boundaries. They do not guarantee correctness on unseen inputs. Why the correct answer wins: Retrieval supplies current evidence with citations.

### Question 61 — C

Answer: Use short-lived scoped access tokens for tool calls. A scoped access token avoids long-lived secrets. Short-lived credentials reduce misuse risk. Never place tokens in prompts or logs. Local study-map skill 2.2 (Foundry SDK and Project Integration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. SDKs provide supported request and response patterns. Pin versions and handle retries, timeouts, and errors explicitly. Why the correct answer wins: A scoped access token avoids long-lived secrets.
- **B:** Incorrect for this question. Managed identities avoid embedded secrets and support role-based access. Assign only required data-plane roles. Why the correct answer wins: A scoped access token avoids long-lived secrets.
- **C:** Correct. Short-lived credentials reduce misuse risk. Never place tokens in prompts or logs. In this case: A scoped access token avoids long-lived secrets.
- **D:** Incorrect for this question. A managed secret store supports rotation and access control. Secrets should never appear in prompts, code, or logs. Why the correct answer wins: A scoped access token avoids long-lived secrets.

### Question 62 — A

Answer: Build a representative golden dataset from real tasks. A golden dataset fixes the inputs. A golden set anchors evaluation in expected behavior. Include edge cases and high-risk scenarios. Local study-map skill 2.3 (Evaluating Models and Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. A golden set anchors evaluation in expected behavior. Include edge cases and high-risk scenarios. In this case: A golden dataset fixes the inputs.
- **B:** Incorrect for this question. Evaluators provide repeatable signals across models and prompts. They must be calibrated against human judgment for high-impact work. Why the correct answer wins: A golden dataset fixes the inputs.
- **C:** Incorrect for this question. Controlled comparison supports evidence-based change. Avoid changing several variables at once. Why the correct answer wins: A golden dataset fixes the inputs.
- **D:** Incorrect for this question. Prompts, models, indexes, and tools all affect behavior. Regression tests catch unintended effects. Why the correct answer wins: A golden dataset fixes the inputs.

### Question 63 — A

Answer: Re-run evaluation suites after meaningful changes. Regression evaluation re-runs previously failing cases against the candidate, so a fixed defect cannot silently return. Prompts, models, indexes, and tools all affect behavior. Regression tests catch unintended effects. Local study-map skill 2.3 (Evaluating Models and Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Prompts, models, indexes, and tools all affect behavior. Regression tests catch unintended effects. In this case: Regression evaluation re-runs previously failing cases against the candidate, so a fixed defect cannot silently return.
- **B:** Incorrect for this question. Evaluators provide repeatable signals across models and prompts. They must be calibrated against human judgment for high-impact work. Why the correct answer wins: Regression evaluation re-runs previously failing cases against the candidate, so a fixed defect cannot silently return.
- **C:** Incorrect for this question. A golden set anchors evaluation in expected behavior. Include edge cases and high-risk scenarios. Why the correct answer wins: Regression evaluation re-runs previously failing cases against the candidate, so a fixed defect cannot silently return.
- **D:** Incorrect for this question. Safety evaluation complements content filters. Use representative adversarial inputs. Why the correct answer wins: Regression evaluation re-runs previously failing cases against the candidate, so a fixed defect cannot silently return.

### Question 64 — A

Answer: Define narrow tool schemas with clear descriptions. A typed schema constrains the arguments. Precise schemas help the model choose tools and arguments correctly. Broad or ambiguous tools invite unsafe calls. Local study-map skill 2.4 (Agent Roles, Goals, and Tool Schemas), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Precise schemas help the model choose tools and arguments correctly. Broad or ambiguous tools invite unsafe calls. In this case: A typed schema constrains the arguments.
- **B:** Incorrect for this question. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Why the correct answer wins: A typed schema constrains the arguments.
- **C:** Incorrect for this question. System messages define role and constraints. They are not a security boundary against injection. Why the correct answer wins: A typed schema constrains the arguments.
- **D:** Incorrect for this question. Routing can balance quality and cost. Fallback and evaluation are required. Why the correct answer wins: A typed schema constrains the arguments.

### Question 65 — D

Answer: Transfer control between agents with explicit context. Handoff transfers control and conversation context to the specialist agent without losing the thread. Handoffs should carry goal, evidence, permissions, and open questions. Implicit context is easily lost. Local study-map skill 2.6 (Multi-Agent Orchestration and Safeguards), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Reflection can catch omissions and inconsistencies. It can also reinforce errors, so validate against evidence. Why the correct answer wins: Handoff transfers control and conversation context to the specialist agent without losing the thread.
- **B:** Incorrect for this question. A manager routes tasks and merges results. Clear responsibility and failure handling are required. Why the correct answer wins: Handoff transfers control and conversation context to the specialist agent without losing the thread.
- **C:** Incorrect for this question. Parallel execution reduces wall-clock time for independent work. Reconciliation still requires design. Why the correct answer wins: Handoff transfers control and conversation context to the specialist agent without losing the thread.
- **D:** Correct. Handoffs should carry goal, evidence, permissions, and open questions. Implicit context is easily lost. In this case: Handoff transfers control and conversation context to the specialist agent without losing the thread.

### Question 66 — A

Answer: Run independent agents concurrently. Parallel execution runs the independent checks at the same time, which is what makes the latency target achievable. Parallel execution reduces wall-clock time for independent work. Reconciliation still requires design. Local study-map skill 2.6 (Multi-Agent Orchestration and Safeguards), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Parallel execution reduces wall-clock time for independent work. Reconciliation still requires design. In this case: Parallel execution runs the independent checks at the same time, which is what makes the latency target achievable.
- **B:** Incorrect for this question. Reflection can catch omissions and inconsistencies. It can also reinforce errors, so validate against evidence. Why the correct answer wins: Parallel execution runs the independent checks at the same time, which is what makes the latency target achievable.
- **C:** Incorrect for this question. Sequential orchestration makes dependencies explicit. It may add latency where steps could run concurrently. Why the correct answer wins: Parallel execution runs the independent checks at the same time, which is what makes the latency target achievable.
- **D:** Incorrect for this question. A manager routes tasks and merges results. Clear responsibility and failure handling are required. Why the correct answer wins: Parallel execution runs the independent checks at the same time, which is what makes the latency target achievable.

### Question 67 — C

Answer: Set a stop sequence so generation ends at the intended boundary. A stop sequence ends generation at the boundary. A stop sequence truncates output at a defined marker, which keeps parsers from receiving trailing commentary. It must not appear inside legitimate content. Local study-map skill 2.8 (Generation Tuning and Observability), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: A stop sequence ends generation at the boundary.
- **B:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: A stop sequence ends generation at the boundary.
- **C:** Correct. A stop sequence truncates output at a defined marker, which keeps parsers from receiving trailing commentary. It must not appear inside legitimate content. In this case: A stop sequence ends generation at the boundary.
- **D:** Incorrect for this question. Top-p narrows or broadens token sampling. Tune with evaluation rather than by intuition. Why the correct answer wins: A stop sequence ends generation at the boundary.

### Question 68 — A

Answer: Adjust top-p to control response diversity. Nucleus sampling widens the candidate set. Top-p narrows or broadens token sampling. Tune with evaluation rather than by intuition. Local study-map skill 2.8 (Generation Tuning and Observability), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Top-p narrows or broadens token sampling. Tune with evaluation rather than by intuition. In this case: Nucleus sampling widens the candidate set.
- **B:** Incorrect for this question. A seed makes repeated sampling closer to reproducible, but it remains best effort and does not replace deterministic extraction settings. Why the correct answer wins: Nucleus sampling widens the candidate set.
- **C:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Nucleus sampling widens the candidate set.
- **D:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Nucleus sampling widens the candidate set.

### Question 69 — B, E

Answers: Use a Foundry SDK or supported connector from application code; Authenticate with a managed identity instead of keys. A supported SDK handles retries, and a managed identity removes stored secrets. SDKs provide supported request and response patterns. Pin versions and handle retries, timeouts, and errors explicitly. Managed identities avoid embedded secrets and support role-based access. Assign only required data-plane roles. Local study-map skill 2.2 (Foundry SDK and Project Integration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Manual portal changes work for exploration but are slow, undocumented, and hard to reproduce, so they are a poor fit for governed release processes. Why the correct answer wins: A supported SDK handles retries, and a managed identity removes stored secrets.
- **B:** Correct. Managed identities avoid embedded secrets and support role-based access. Assign only required data-plane roles. In this case: A supported SDK handles retries, and a managed identity removes stored secrets.
- **C:** Incorrect for this question. Short-lived credentials reduce misuse risk. Never place tokens in prompts or logs. Why the correct answer wins: A supported SDK handles retries, and a managed identity removes stored secrets.
- **D:** Incorrect for this question. A managed secret store supports rotation and access control. Secrets should never appear in prompts, code, or logs. Why the correct answer wins: A supported SDK handles retries, and a managed identity removes stored secrets.
- **E:** Correct. SDKs provide supported request and response patterns. Pin versions and handle retries, timeouts, and errors explicitly. In this case: A supported SDK handles retries, and a managed identity removes stored secrets.

### Question 70 — D, E

Answers: Use evaluators for quality, safety, and groundedness; Evaluate harmful, biased, or policy-violating output. Quality evaluation scores correctness, and safety evaluation screens unsafe output. Evaluators provide repeatable signals across models and prompts. They must be calibrated against human judgment for high-impact work. Safety evaluation complements content filters. Use representative adversarial inputs. Local study-map skill 2.3 (Evaluating Models and Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Controlled comparison supports evidence-based change. Avoid changing several variables at once. Why the correct answer wins: Quality evaluation scores correctness, and safety evaluation screens unsafe output.
- **B:** Incorrect for this question. A golden set anchors evaluation in expected behavior. Include edge cases and high-risk scenarios. Why the correct answer wins: Quality evaluation scores correctness, and safety evaluation screens unsafe output.
- **C:** Incorrect for this question. Prompts, models, indexes, and tools all affect behavior. Regression tests catch unintended effects. Why the correct answer wins: Quality evaluation scores correctness, and safety evaluation screens unsafe output.
- **D:** Correct. Safety evaluation complements content filters. Use representative adversarial inputs. In this case: Quality evaluation scores correctness, and safety evaluation screens unsafe output.
- **E:** Correct. Evaluators provide repeatable signals across models and prompts. They must be calibrated against human judgment for high-impact work. In this case: Quality evaluation scores correctness, and safety evaluation screens unsafe output.

### Question 71 — A, C

Answers: Give the agent a file-search tool over approved document stores; Enable a sandboxed code interpreter tool for calculations. File search supplies approved evidence, and an interpreter performs arithmetic. A file tool retrieves from curated stores under configured access. It still depends on indexing quality and permission filters. Code execution handles quantitative work the model cannot do reliably in text. The sandbox must be isolated and output must be validated. Local study-map skill 2.5 (Agent Tools, Retrieval, Memory, and Function Calling), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. A file tool retrieves from curated stores under configured access. It still depends on indexing quality and permission filters. In this case: File search supplies approved evidence, and an interpreter performs arithmetic.
- **B:** Incorrect for this question. Routing can balance quality and cost. Fallback and evaluation are required. Why the correct answer wins: File search supplies approved evidence, and an interpreter performs arithmetic.
- **C:** Correct. Code execution handles quantitative work the model cannot do reliably in text. The sandbox must be isolated and output must be validated. In this case: File search supplies approved evidence, and an interpreter performs arithmetic.
- **D:** Incorrect for this question. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Why the correct answer wins: File search supplies approved evidence, and an interpreter performs arithmetic.
- **E:** Incorrect for this question. OpenAPI tools describe supported HTTP operations for agent use. Narrow operations, validate inputs, and authenticate the caller. Why the correct answer wins: File search supplies approved evidence, and an interpreter performs arithmetic.

### Question 72 — A

Answer: Define role and goal → configure tools → attach knowledge → evaluate in sandbox → deploy with monitoring. Role, tools, evaluation, then deployment with monitoring. An agent is defined before it is connected to tools and knowledge, and evaluation precedes deployment. Local study-map skill 2.6 (Multi-Agent Orchestration and Safeguards), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. An agent is defined before it is connected to tools and knowledge, and evaluation precedes deployment. In this case: Role, tools, evaluation, then deployment with monitoring.
- **B:** Incorrect for this question. Tools configured before the role exists, and evaluation after deployment gates nothing. Why the correct answer wins: Role, tools, evaluation, then deployment with monitoring.
- **C:** Incorrect for this question. Deployment before the agent is defined, connected, or evaluated removes every control. Why the correct answer wins: Role, tools, evaluation, then deployment with monitoring.
- **D:** Incorrect for this question. The agent must be defined first, and evaluation must precede deployment. Why the correct answer wins: Role, tools, evaluation, then deployment with monitoring.

### Question 73 — D

Answer: Queue flagged generations for human moderation before release. Human moderation before release catches contextual problems. Human moderation catches context that automated filters miss, at the cost of latency and reviewer load. Local study-map skill 3.1 (Image Generation and Editing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Brand controls define permitted logos, styles, and claims. Technical generation must still pass approval. Why the correct answer wins: Human moderation before release catches contextual problems.
- **B:** Incorrect for this question. Image and video safety filters reduce exposure to harmful content. Thresholds and human escalation should match policy. Why the correct answer wins: Human moderation before release catches contextual problems.
- **C:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Human moderation before release catches contextual problems.
- **D:** Correct. Human moderation catches context that automated filters miss, at the cost of latency and reviewer load. In this case: Human moderation before release catches contextual problems.

### Question 74 — B

Answer: Generate a set of descriptive tags for each image. Generated tags make the library filterable and searchable, which is what the editors asked for. Tags support filtering and search across large image libraries. Tag vocabulary should be governed so synonyms do not fragment results. Local study-map skill 3.3 (Multimodal Understanding and Accessibility), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Alt text should convey purpose and essential content, not decorative detail. Human review is still needed for critical pages. Why the correct answer wins: Generated tags make the library filterable and searchable, which is what the editors asked for.
- **B:** Correct. Tags support filtering and search across large image libraries. Tag vocabulary should be governed so synonyms do not fragment results. In this case: Generated tags make the library filterable and searchable, which is what the editors asked for.
- **C:** Incorrect for this question. Visual question answering should cite the relevant region or content. Avoid answering beyond what the image supports. Why the correct answer wins: Generated tags make the library filterable and searchable, which is what the editors asked for.
- **D:** Incorrect for this question. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Why the correct answer wins: Generated tags make the library filterable and searchable, which is what the editors asked for.

### Question 75 — B

Answer: Preserve reading order across columns and sections. Reading-order analysis restores the intended sequence. Reading order affects comprehension and extraction. Incorrect order can invert meaning in contracts and forms. Local study-map skill 3.4 (Visual Extraction and Video Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. OCR unlocks text in scans and screenshots. Layout and table structure may still require specialized extraction. Why the correct answer wins: Reading-order analysis restores the intended sequence.
- **B:** Correct. Reading order affects comprehension and extraction. Incorrect order can invert meaning in contracts and forms. In this case: Reading-order analysis restores the intended sequence.
- **C:** Incorrect for this question. Layout awareness improves extraction from forms and multi-column documents. Flattening to plain text can destroy meaning. Why the correct answer wins: Reading-order analysis restores the intended sequence.
- **D:** Incorrect for this question. Markdown preserves headings, tables, and lists in a model-friendly form. Validate that critical values survive conversion. Why the correct answer wins: Reading-order analysis restores the intended sequence.

### Question 76 — C

Answer: Use Azure Content Understanding analyzers in Foundry Tools. Content Understanding analyzers are configured per content type. Content Understanding extracts structure and fields from documents, images, audio, and video. Analyzer design and validation determine quality. Local study-map skill 3.4 (Visual Extraction and Video Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Analyzers define what to extract and how to return it. Version and test them like application code. Why the correct answer wins: Content Understanding analyzers are configured per content type.
- **B:** Incorrect for this question. Document Intelligence provides prebuilt and custom extraction for structured documents. Validate field accuracy on representative samples. Why the correct answer wins: Content Understanding analyzers are configured per content type.
- **C:** Correct. Content Understanding extracts structure and fields from documents, images, audio, and video. Analyzer design and validation determine quality. In this case: Content Understanding analyzers are configured per content type.
- **D:** Incorrect for this question. Prebuilt models cover invoices, receipts, IDs, and similar formats. Check supported locales and field coverage. Why the correct answer wins: Content Understanding analyzers are configured per content type.

### Question 77 — B, E

Answers: Use pro mode for complex multimodal content understanding; Return markdown for retrieval and reasoning pipelines. Pro mode handles complex packets, and markdown suits downstream reasoning. Pro mode handles more demanding layouts and multimodal inputs at higher cost. Use it where simpler modes fail requirements. Markdown preserves structure and is easy for models to consume. Validate tables and key values. Local study-map skill 3.4 (Visual Extraction and Video Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Single-task analyzers target one content type or objective. They may be simpler and cheaper than general pro-mode pipelines. Why the correct answer wins: Pro mode handles complex packets, and markdown suits downstream reasoning.
- **B:** Correct. Markdown preserves structure and is easy for models to consume. Validate tables and key values. In this case: Pro mode handles complex packets, and markdown suits downstream reasoning.
- **C:** Incorrect for this question. Detection returns locations and labels for visual elements. Validate classes and thresholds against the use case. Why the correct answer wins: Pro mode handles complex packets, and markdown suits downstream reasoning.
- **D:** Incorrect for this question. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Why the correct answer wins: Pro mode handles complex packets, and markdown suits downstream reasoning.
- **E:** Correct. Pro mode handles more demanding layouts and multimodal inputs at higher cost. Use it where simpler modes fail requirements. In this case: Pro mode handles complex packets, and markdown suits downstream reasoning.

### Question 78 — D

Answer: Upload image → validate format and size → send multimodal request → parse structured fields → route low-confidence values to review. Input validation precedes the model call, output is parsed into fields, and low-confidence values go to human review. Validation and structured parsing bracket the multimodal call, and low-confidence output goes to people. Local study-map skill 3.5 (Multimodal Responsible AI), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Parsing requires a response, which requires an uploaded and validated image. Why the correct answer wins: Input validation precedes the model call, output is parsed into fields, and low-confidence values go to human review.
- **B:** Incorrect for this question. A request cannot precede the upload, and validation must come before the call. Why the correct answer wins: Input validation precedes the model call, output is parsed into fields, and low-confidence values go to human review.
- **C:** Incorrect for this question. Review cannot precede the request, and parsing must follow the response. Why the correct answer wins: Input validation precedes the model call, output is parsed into fields, and low-confidence values go to human review.
- **D:** Correct. Validation and structured parsing bracket the multimodal call, and low-confidence output goes to people. In this case: Input validation precedes the model call, output is parsed into fields, and low-confidence values go to human review.

### Question 79 — B

Answer: Select and return the most relevant source sentences. Extractive summaries return source sentences verbatim, so every statement remains quotable and auditable. Extractive summaries stay verbatim and therefore auditable, at the cost of readability and length. Local study-map skill 4.1 (Language Model Text Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Why the correct answer wins: Extractive summaries return source sentences verbatim, so every statement remains quotable and auditable.
- **B:** Correct. Extractive summaries stay verbatim and therefore auditable, at the cost of readability and length. In this case: Extractive summaries return source sentences verbatim, so every statement remains quotable and auditable.
- **C:** Incorrect for this question. Compliance work requires precise citation, retention, and review. Generic summarization is insufficient without controls. Why the correct answer wins: Extractive summaries return source sentences verbatim, so every statement remains quotable and auditable.
- **D:** Incorrect for this question. Abstractive summaries read naturally and compress long text, but they can introduce statements that the source does not support. Why the correct answer wins: Extractive summaries return source sentences verbatim, so every statement remains quotable and auditable.

### Question 80 — D

Answer: Convert names between writing systems without translating meaning. Transliteration preserves pronunciation across writing systems. Transliteration preserves pronunciation for names and addresses. It is not a substitute for translating meaning-bearing text. Local study-map skill 4.2 (Translation), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Domain adaptation improves consistency and recall. Validate against expert-created expected outputs. Why the correct answer wins: Transliteration preserves pronunciation across writing systems.
- **B:** Incorrect for this question. Translation should preserve meaning, names, and formatting. Evaluate domain terminology and low-resource languages. Why the correct answer wins: Transliteration preserves pronunciation across writing systems.
- **C:** Incorrect for this question. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Why the correct answer wins: Transliteration preserves pronunciation across writing systems.
- **D:** Correct. Transliteration preserves pronunciation for names and addresses. It is not a substitute for translating meaning-bearing text. In this case: Transliteration preserves pronunciation across writing systems.

### Question 81 — C

Answer: Select a specific synthesis voice for consistent spoken output. A specific synthesis voice keeps the channel consistent. A named voice keeps a phone or kiosk channel recognizable across prompts. Voice availability and language coverage vary by region. Local study-map skill 4.3 (Speech Solutions), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Text-to-speech supports voice responses and accessibility. Voice, prosody, and latency affect usability. Why the correct answer wins: A specific synthesis voice keeps the channel consistent.
- **B:** Incorrect for this question. Custom speech can improve recognition of domain terms. It requires representative audio and ongoing evaluation. Why the correct answer wins: A specific synthesis voice keeps the channel consistent.
- **C:** Correct. A named voice keeps a phone or kiosk channel recognizable across prompts. Voice availability and language coverage vary by region. In this case: A specific synthesis voice keeps the channel consistent.
- **D:** Incorrect for this question. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Why the correct answer wins: A specific synthesis voice keeps the channel consistent.

### Question 82 — C

Answer: Extract key phrases to summarize what a document covers. Key-phrase extraction surfaces the salient topics in each document, which supports navigation and triage. Key phrases support navigation, tagging, and clustering. They are not a substitute for a required structured field. Local study-map skill 4.1 (Language Model Text Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Entity extraction turns text into structured facts. Ambiguous mentions need resolution and validation. Why the correct answer wins: Key-phrase extraction surfaces the salient topics in each document, which supports navigation and triage.
- **B:** Incorrect for this question. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Why the correct answer wins: Key-phrase extraction surfaces the salient topics in each document, which supports navigation and triage.
- **C:** Correct. Key phrases support navigation, tagging, and clustering. They are not a substitute for a required structured field. In this case: Key-phrase extraction surfaces the salient topics in each document, which supports navigation and triage.
- **D:** Incorrect for this question. Topic extraction supports discovery and grouping. It is not a substitute for an authoritative taxonomy. Why the correct answer wins: Key-phrase extraction surfaces the salient topics in each document, which supports navigation and triage.

### Question 83 — C, E

Answers: Detect and redact sensitive personal data; Analyze sentiment and tone with an appropriate service. PII detection finds personal data, and sentiment detects frustration. Sensitive Data Protection or language PII detection can identify and mask data. Verify that redaction covers every path where content flows. Sentiment analysis can support triage and monitoring. Domain and language variation require validation. Local study-map skill 4.1 (Language Model Text Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Why the correct answer wins: PII detection finds personal data, and sentiment detects frustration.
- **B:** Incorrect for this question. Topic extraction supports discovery and grouping. It is not a substitute for an authoritative taxonomy. Why the correct answer wins: PII detection finds personal data, and sentiment detects frustration.
- **C:** Correct. Sentiment analysis can support triage and monitoring. Domain and language variation require validation. In this case: PII detection finds personal data, and sentiment detects frustration.
- **D:** Incorrect for this question. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Why the correct answer wins: PII detection finds personal data, and sentiment detects frustration.
- **E:** Correct. Sensitive Data Protection or language PII detection can identify and mask data. Verify that redaction covers every path where content flows. In this case: PII detection finds personal data, and sentiment detects frustration.

### Question 84 — D

Answer: Tune scoring and boosting against a labelled query set. Scoring changes must be measured on a labelled query set. Boosting and scoring changes should be measured on real queries. Untested tuning usually trades one query class for another. Local study-map skill 5.2 (Search and Grounding Configuration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. A semantic ranker can improve relevance for natural-language queries. It adds cost and latency and should be measured against a baseline. Why the correct answer wins: Scoring changes must be measured on a labelled query set.
- **B:** Incorrect for this question. Embeddings support similarity search over meaning rather than exact terms. Vector search still needs chunking, filtering, and evaluation. Why the correct answer wins: Scoring changes must be measured on a labelled query set.
- **C:** Incorrect for this question. Hybrid search covers exact identifiers and paraphrased meaning together. Fusion and ranking need testing on representative queries. Why the correct answer wins: Scoring changes must be measured on a labelled query set.
- **D:** Correct. Boosting and scoring changes should be measured on real queries. Untested tuning usually trades one query class for another. In this case: Scoring changes must be measured on a labelled query set.

### Question 85 — D

Answer: Add enrichment skills for text, image, and layout. Enrichment adds derived content during indexing. A skillset can extract entities, captions, and structure during indexing. Enrichment adds cost and failure points that need monitoring. Local study-map skill 5.3 (Enrichment Skills), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. Skillsets can OCR, split, embed, and extract during indexing. Each skill adds latency, cost, and failure modes. Why the correct answer wins: Enrichment adds derived content during indexing.
- **B:** Incorrect for this question. Markdown preserves structure and is easy for models to consume. Validate tables and key values. Why the correct answer wins: Enrichment adds derived content during indexing.
- **C:** Incorrect for this question. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. Why the correct answer wins: Enrichment adds derived content during indexing.
- **D:** Correct. A skillset can extract entities, captions, and structure during indexing. Enrichment adds cost and failure points that need monitoring. In this case: Enrichment adds derived content during indexing.

### Question 86 — D

Answer: Define index fields, attributes, and searchable versus filterable behavior. Field attributes control filtering and sorting. Field attributes decide what can be filtered, sorted, faceted, or retrieved, so schema choices constrain query design later. Local study-map skill 5.6 (Document and Content Extraction), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. Document Intelligence provides prebuilt and custom extraction for structured documents. Validate field accuracy on representative samples. Why the correct answer wins: Field attributes control filtering and sorting.
- **B:** Incorrect for this question. Typed fields feed downstream systems directly. Add validation and confidence thresholds before automated action. Why the correct answer wins: Field attributes control filtering and sorting.
- **C:** Incorrect for this question. Analyzers define what to extract and how to return it. Version and test them like application code. Why the correct answer wins: Field attributes control filtering and sorting.
- **D:** Correct. Field attributes decide what can be filtered, sorted, faceted, or retrieved, so schema choices constrain query design later. In this case: Field attributes control filtering and sorting.

### Question 87 — C

Answer: Combine OCR with layout analysis for complex documents. OCR with layout analysis preserves relationships. OCR supplies text while layout analysis preserves relationships. Together they support tables and multi-column forms. Local study-map skill 5.4 (RAG Ingestion and OCR), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. Markdown preserves headings, tables, and lists in a model-friendly form. Validate that critical values survive conversion. Why the correct answer wins: OCR with layout analysis preserves relationships.
- **B:** Incorrect for this question. Chunking affects recall, precision, and context use. Respect document structure and test against real questions. Why the correct answer wins: OCR with layout analysis preserves relationships.
- **C:** Correct. OCR supplies text while layout analysis preserves relationships. Together they support tables and multi-column forms. In this case: OCR with layout analysis preserves relationships.
- **D:** Incorrect for this question. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. Why the correct answer wins: OCR with layout analysis preserves relationships.

### Question 88 — C

Answer: Connect the data source → define the index schema → attach the enrichment skillset → run the indexer → validate relevance on sample queries. The source is connected, the schema defined, enrichment attached, the indexer run, and relevance validated on sample queries. Schema and enrichment must exist before indexing runs, and relevance is checked after the index is populated. Local study-map skill 5.2 (Search and Grounding Configuration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. An indexer cannot run before the source and schema exist. Why the correct answer wins: The source is connected, the schema defined, enrichment attached, the indexer run, and relevance validated on sample queries.
- **B:** Incorrect for this question. The schema must exist before enrichment and relevance testing. Why the correct answer wins: The source is connected, the schema defined, enrichment attached, the indexer run, and relevance validated on sample queries.
- **C:** Correct. Schema and enrichment must exist before indexing runs, and relevance is checked after the index is populated. In this case: The source is connected, the schema defined, enrichment attached, the indexer run, and relevance validated on sample queries.
- **D:** Incorrect for this question. Relevance cannot be validated on an index that was never populated. Why the correct answer wins: The source is connected, the schema defined, enrichment attached, the indexer run, and relevance validated on sample queries.

### Question 89 — A

Answer: Persist conversation history in a thread or session. Conversation state keeps earlier context across turns. Threads support continuity across turns. Apply retention and access controls to stored history. Local study-map skill 2.2 (Foundry SDK and Project Integration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Threads support continuity across turns. Apply retention and access controls to stored history. In this case: Conversation state keeps earlier context across turns.
- **B:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: Conversation state keeps earlier context across turns.
- **C:** Incorrect for this question. Embeddings determine semantic similarity behavior. Evaluate retrieval quality before and after changes. Why the correct answer wins: Conversation state keeps earlier context across turns.
- **D:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Conversation state keeps earlier context across turns.

### Question 90 — B

Answer: Use a custom speech model for specialized vocabulary. A custom speech model adapts vocabulary to the domain. Custom speech can improve recognition of domain terms. It requires representative audio and ongoing evaluation. Local study-map skill 4.3 (Speech Solutions), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Speech-to-text enables voice agents and transcript analysis. Audio quality, accents, and domain terms affect accuracy. Why the correct answer wins: A custom speech model adapts vocabulary to the domain.
- **B:** Correct. Custom speech can improve recognition of domain terms. It requires representative audio and ongoing evaluation. In this case: A custom speech model adapts vocabulary to the domain.
- **C:** Incorrect for this question. Text-to-speech supports voice responses and accessibility. Voice, prosody, and latency affect usability. Why the correct answer wins: A custom speech model adapts vocabulary to the domain.
- **D:** Incorrect for this question. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Why the correct answer wins: A custom speech model adapts vocabulary to the domain.

### Question 91 — D

Answer: Use field-level confidence to route exceptions. Field-level confidence sends uncertain values to review. Low-confidence fields should be reviewed rather than accepted. Thresholds depend on downstream impact. Local study-map skill 5.6 (Document and Content Extraction), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. Relevance covers both retrieval and response usefulness. A correct but off-topic answer still fails. Why the correct answer wins: Field-level confidence sends uncertain values to review.
- **B:** Incorrect for this question. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Why the correct answer wins: Field-level confidence sends uncertain values to review.
- **C:** Incorrect for this question. Sentiment analysis can support triage and monitoring. Domain and language variation require validation. Why the correct answer wins: Field-level confidence sends uncertain values to review.
- **D:** Correct. Low-confidence fields should be reviewed rather than accepted. Thresholds depend on downstream impact. In this case: Field-level confidence sends uncertain values to review.

### Question 92 — D

Answer: Train a custom extraction model on labeled documents. A custom extraction model targets a proprietary layout. Custom models fit specialized forms not covered by prebuilts. They require representative labels and retraining discipline. Local study-map skill 5.6 (Document and Content Extraction), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. Prebuilt models cover invoices, receipts, IDs, and similar formats. Check supported locales and field coverage. Why the correct answer wins: A custom extraction model targets a proprietary layout.
- **B:** Incorrect for this question. Analyzers define what to extract and how to return it. Version and test them like application code. Why the correct answer wins: A custom extraction model targets a proprietary layout.
- **C:** Incorrect for this question. Document Intelligence provides prebuilt and custom extraction for structured documents. Validate field accuracy on representative samples. Why the correct answer wins: A custom extraction model targets a proprietary layout.
- **D:** Correct. Custom models fit specialized forms not covered by prebuilts. They require representative labels and retraining discipline. In this case: A custom extraction model targets a proprietary layout.

### Question 93 — D

Answer: Apply document-level security filters at query time. Document-level security filters restrict results to the caller's authorized scope. Filters restrict results to content the user may see. They must be enforced before content reaches the model. Local study-map skill 5.2 (Search and Grounding Configuration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. Hybrid search covers exact identifiers and paraphrased meaning together. Fusion and ranking need testing on representative queries. Why the correct answer wins: Document-level security filters restrict results to the caller's authorized scope.
- **B:** Incorrect for this question. Stale content produces outdated answers. Define refresh expectations and test deletion behavior. Why the correct answer wins: Document-level security filters restrict results to the caller's authorized scope.
- **C:** Incorrect for this question. A semantic ranker can improve relevance for natural-language queries. It adds cost and latency and should be measured against a baseline. Why the correct answer wins: Document-level security filters restrict results to the caller's authorized scope.
- **D:** Correct. Filters restrict results to content the user may see. They must be enforced before content reaches the model. In this case: Document-level security filters restrict results to the caller's authorized scope.

### Question 94 — B

Answer: Add enrichment skills for text, image, and layout. Enrichment adds derived content to documents during indexing. A skillset can extract entities, captions, and structure during indexing. Enrichment adds cost and failure points that need monitoring. Local study-map skill 5.3 (Enrichment Skills), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. OCR unlocks text in scans and screenshots. Layout and table structure may still require specialized extraction. Why the correct answer wins: Enrichment adds derived content to documents during indexing.
- **B:** Correct. A skillset can extract entities, captions, and structure during indexing. Enrichment adds cost and failure points that need monitoring. In this case: Enrichment adds derived content to documents during indexing.
- **C:** Incorrect for this question. Skillsets can OCR, split, embed, and extract during indexing. Each skill adds latency, cost, and failure modes. Why the correct answer wins: Enrichment adds derived content to documents during indexing.
- **D:** Incorrect for this question. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. Why the correct answer wins: Enrichment adds derived content to documents during indexing.

### Question 95 — D

Answer: Enable a sandboxed code interpreter tool for calculations. A sandboxed interpreter computes from the supplied data, which is far more reliable than arithmetic performed in generated text. Code execution handles quantitative work the model cannot do reliably in text. The sandbox must be isolated and output must be validated. Local study-map skill 2.5 (Agent Tools, Retrieval, Memory, and Function Calling), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. OpenAPI tools describe supported HTTP operations for agent use. Narrow operations, validate inputs, and authenticate the caller. Why the correct answer wins: A sandboxed interpreter computes from the supplied data, which is far more reliable than arithmetic performed in generated text.
- **B:** Incorrect for this question. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Why the correct answer wins: A sandboxed interpreter computes from the supplied data, which is far more reliable than arithmetic performed in generated text.
- **C:** Incorrect for this question. A file tool retrieves from curated stores under configured access. It still depends on indexing quality and permission filters. Why the correct answer wins: A sandboxed interpreter computes from the supplied data, which is far more reliable than arithmetic performed in generated text.
- **D:** Correct. Code execution handles quantitative work the model cannot do reliably in text. The sandbox must be isolated and output must be validated. In this case: A sandboxed interpreter computes from the supplied data, which is far more reliable than arithmetic performed in generated text.

### Question 96 — D

Answer: Enable tracing across agent, model, and tool calls. Traces show the ordered model and tool calls. Traces localize failures and latency in multi-step workflows. Correlate them with evaluation results and deployment versions. Local study-map skill 2.7 (Agent Monitoring and Error Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Traces show the ordered model and tool calls.
- **B:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Traces show the ordered model and tool calls.
- **C:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Traces show the ordered model and tool calls.
- **D:** Correct. Traces localize failures and latency in multi-step workflows. Correlate them with evaluation results and deployment versions. In this case: Traces show the ordered model and tool calls.

### Question 97 — A

Answer: Push documents to an index through the data-plane API. Push ingestion indexes documents as they are written. Push ingestion supports near-real-time updates from applications. The app owns batching, retries, and deletion. Local study-map skill 5.1 (Content Ingestion and Indexing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Correct. Push ingestion supports near-real-time updates from applications. The app owns batching, retries, and deletion. In this case: Push ingestion indexes documents as they are written.
- **B:** Incorrect for this question. OCR unlocks text in scans and screenshots. Layout and table structure may still require specialized extraction. Why the correct answer wins: Push ingestion indexes documents as they are written.
- **C:** Incorrect for this question. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. Why the correct answer wins: Push ingestion indexes documents as they are written.
- **D:** Incorrect for this question. Skillsets can OCR, split, embed, and extract during indexing. Each skill adds latency, cost, and failure modes. Why the correct answer wins: Push ingestion indexes documents as they are written.

### Question 98 — B

Answer: Use provisioned throughput for predictable high-volume workloads. Provisioned throughput reserves capacity for predictable continuous demand. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Local study-map skill 1.4 (Quotas, Scaling, and Cost), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Batch deployments can lower cost for large asynchronous jobs. They are unsuitable for interactive agent turns. Why the correct answer wins: Provisioned throughput reserves capacity for predictable continuous demand.
- **B:** Correct. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. In this case: Provisioned throughput reserves capacity for predictable continuous demand.
- **C:** Incorrect for this question. Standard deployments bill per token and scale within quota. They suit spiky or early workloads. Why the correct answer wins: Provisioned throughput reserves capacity for predictable continuous demand.
- **D:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Provisioned throughput reserves capacity for predictable continuous demand.

### Question 99 — A

Answer: Enable tracing across agent, model, and tool calls. Traces show each model and tool call in order, locating the failing step. Traces localize failures and latency in multi-step workflows. Correlate them with evaluation results and deployment versions. Local study-map skill 2.7 (Agent Monitoring and Error Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Traces localize failures and latency in multi-step workflows. Correlate them with evaluation results and deployment versions. In this case: Traces show each model and tool call in order, locating the failing step.
- **B:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Traces show each model and tool call in order, locating the failing step.
- **C:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Traces show each model and tool call in order, locating the failing step.
- **D:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Traces show each model and tool call in order, locating the failing step.

### Question 100 — D

Answer: Persist conversation history in a thread or session. Conversation state preserves identifiers across turns without resending everything. Threads support continuity across turns. Apply retention and access controls to stored history. Local study-map skill 2.5 (Agent Tools, Retrieval, Memory, and Function Calling), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: Conversation state preserves identifiers across turns without resending everything.
- **B:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Conversation state preserves identifiers across turns without resending everything.
- **C:** Incorrect for this question. Embeddings determine semantic similarity behavior. Evaluate retrieval quality before and after changes. Why the correct answer wins: Conversation state preserves identifiers across turns without resending everything.
- **D:** Correct. Threads support continuity across turns. Apply retention and access controls to stored history. In this case: Conversation state preserves identifiers across turns without resending everything.
