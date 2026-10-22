# Microsoft AI-103 — Full-Length Mock Exam 6

Azure AI Apps and Agents Developer Associate · 100 questions · 120 minutes · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 84 multiple-choice (selection count stated where needed), 16 multi-select, and 4 case studies of 3 questions. 8 of the multiple-choice items ask you to choose the correct candidate sequence. Hot-area, drag-and-drop UI, labs, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. A group must standardize on one model that supports text, image, and audio in every operating region. What should be checked first?

Domain: Plan and manage an Azure AI solution

- A. Use a small language model for a narrow, high-volume task
- B. Train or deploy a task-specific model outside the prebuilt catalog
- C. Use a general-purpose large language model for complex reasoning
- D. Compare supported models in the Foundry model catalog

### 2. A business unit wants a model adapted to its own ticket history while keeping the weights under its control. Which option applies?

Domain: Plan and manage an Azure AI solution

- A. Use a general-purpose large language model for complex reasoning
- B. Use a small language model for a narrow, high-volume task
- C. Train or deploy a task-specific model outside the prebuilt catalog
- D. Use a multimodal model for combined text, image, or audio input

### 3. A service desk agent must remember the asset tag discussed earlier in the session. What should be used?

Domain: Plan and manage an Azure AI solution

- A. Expose a typed function as an agent tool
- B. Use an Azure AI Search indexer to pull source content
- C. Use a vector index for semantic retrieval
- D. Use managed conversation state or memory for continuity

### 4. A group must release the same assistant to four subsidiaries with reproducible infrastructure. Which sequence should the team follow?

Domain: Plan and manage an Azure AI solution

- A. Deploy model → promote → provision resources → evaluate → configure app
- B. Evaluate → provision resources → promote → deploy model → configure app
- C. Provision resources → deploy model → configure app connection → evaluate → promote
- D. Configure app → provision resources → deploy model → promote → evaluate

### 5. Regulated subsidiaries require that model traffic never uses the public internet. What should be configured?

Domain: Plan and manage an Azure AI solution

- A. Manage AI resources with infrastructure as code and CI/CD
- B. Plan for model quota expressed in tokens and requests per minute
- C. Use private endpoints and disable public network access
- D. Track cost per accepted task, not only per token

### 6. The assistant is throttled at the start of each business day when every subsidiary logs in. What should be re-planned?

Domain: Plan and manage an Azure AI solution

- A. Use provisioned throughput for predictable high-volume workloads
- B. Plan for model quota expressed in tokens and requests per minute
- C. Track cost per accepted task, not only per token
- D. Monitor input and quality drift over time

### 7. A long, unchanged corporate policy block is resent with every request and dominates spend. What should be enabled?

Domain: Plan and manage an Azure AI solution

- A. Plan for model quota expressed in tokens and requests per minute
- B. Track cost per accepted task, not only per token
- C. Use supported prompt or response caching where appropriate
- D. Monitor input and quality drift over time

### 8. One operations team must see latency, errors, and refusals across all subsidiaries. What should be enabled?

Domain: Plan and manage an Azure AI solution

- A. Preserve audit logs of changes, approvals, and tool actions
- B. Alert on latency, error rate, safety, and cost thresholds
- C. Monitor input and quality drift over time
- D. Use Azure Monitor and Application Insights for telemetry

### 9. A shared model upgrade must not break cases that failed in the last release. What should be run first?

Domain: Plan and manage an Azure AI solution

- A. Build a representative golden dataset from real tasks
- B. Use evaluators for quality, safety, and groundedness
- C. Compare variants with controlled traffic and shared metrics
- D. Re-run evaluation suites after meaningful changes

### 10. Every subsidiary app must authenticate to Foundry without stored secrets. What should each app use?

Domain: Plan and manage an Azure AI solution

- A. Store secrets in Azure Key Vault when keys are unavoidable
- B. Long-lived API key pasted into configuration
- C. Shared connection string with an embedded secret
- D. Authenticate with a managed identity instead of keys

### 11. Consequential customer decisions may not be delegated entirely to the model. Which principle applies?

Domain: Plan and manage an Azure AI solution

- A. Enforce constraints in code and platform policy
- B. Set agent oversight mode and tool-access constraints
- C. Require human approval before consequential actions
- D. Preserve audit logs of changes, approvals, and tool actions

### 12. Each subsidiary must see only its own data and must reach Foundry privately. Which two actions should you take? Select two.

Domain: Plan and manage an Azure AI solution

- A. Configure content safety filters for harmful categories
- B. Store secrets in Azure Key Vault when keys are unavoidable
- C. Use supported prompt or response caching where appropriate
- D. Use least-privilege Azure RBAC roles for the workload identity
- E. Use private endpoints and disable public network access

### 13. A shared customer agent can issue goodwill credits. Which two controls belong in the design? Select two.

Domain: Plan and manage an Azure AI solution

- A. Use a small language model for a narrow, high-volume task
- B. Adjust top-p to control response diversity
- C. Configure content safety filters for harmful categories
- D. Lower temperature for more deterministic extraction
- E. Require human approval before consequential actions

### 14. The assistant must answer from current approved group policies and cite them. Which approach fits?

Domain: Implement generative AI and agentic solutions

- A. Route requests to different models by task difficulty
- B. Translate every request before retrieval
- C. Ground responses with retrieval-augmented generation
- D. Design multistep workflows with explicit checkpoints

### 15. A downstream system needs fixed fields and types from each answer before it can act. What should the model produce?

Domain: Implement generative AI and agentic solutions

- A. Return a defined JSON schema for downstream systems
- B. Use supported prompt or response caching where appropriate
- C. Use a versioned prompt template with explicit variables
- D. Design multistep workflows with explicit checkpoints

### 16. A workflow must classify a request, check entitlement, then respond, in that order. What should the design use?

Domain: Implement generative AI and agentic solutions

- A. Limit autonomy with scope, budget, and stop conditions
- B. One model call with no external retrieval or tool use
- C. Route requests to different models by task difficulty
- D. Design multistep workflows with explicit checkpoints

### 17. Four apps in different languages need supported authentication and retries for Foundry. What should they share?

Domain: Implement generative AI and agentic solutions

- A. Use batch processing for latency-tolerant bulk work
- B. Manage AI resources with infrastructure as code and CI/CD
- C. Use a Foundry SDK or supported connector from application code
- D. Create and run deployments by hand in the portal

### 18. Each subsidiary must call only the deployments approved for its own project. What should each app be configured with?

Domain: Implement generative AI and agentic solutions

- A. Connect the application to the Foundry project endpoint
- B. Use an Azure AI Search indexer to pull source content
- C. Compare supported models in the Foundry model catalog
- D. Store secrets in Azure Key Vault when keys are unavoidable

### 19. The group must compare two prompt designs fairly and keep a stable benchmark. Which two practices are required? Select two.

Domain: Implement generative AI and agentic solutions

- A. Compare variants with controlled traffic and shared metrics
- B. Lower temperature for more deterministic extraction
- C. Use provisioned throughput for predictable high-volume workloads
- D. Apply watermarks or provenance markers to generated media
- E. Build a representative golden dataset from real tasks

### 20. An answer is fluent and on topic but asserts a policy that was never retrieved. Which failure should be measured?

Domain: Implement generative AI and agentic solutions

- A. Detect fabricated or unsupported statements
- B. Evaluate structure and logical consistency of responses
- C. Measure whether retrieved content and answers address the question
- D. Detect tone and sentiment appropriate to the audience

### 21. Every turn must follow the same corporate tone and refusal policy. Where should that guidance live?

Domain: Implement generative AI and agentic solutions

- A. Enforce constraints in code and platform policy
- B. Put stable behavior rules in the system message
- C. Use least-privilege Azure RBAC roles for the workload identity
- D. Configure content safety filters for harmful categories

### 22. Which sequence correctly describes a governed tool call from the group service agent?

Domain: Implement generative AI and agentic solutions

- A. Model executes tool → app validates → tool returns result → app authorizes → model responds
- B. Model responds → app authorizes → tool executes → result returns → app validates
- C. Model requests tool → app validates and authorizes → tool executes → result returns → model responds
- D. App authorizes → model executes tool → result returns → app validates → model responds

### 23. An agent must read a customer's open incidents from a line-of-business API. Which capability performs that lookup?

Domain: Implement generative AI and agentic solutions

- A. Ground responses with retrieval-augmented generation
- B. Use managed conversation state or memory for continuity
- C. Expose an OpenAPI operation as an agent tool
- D. Expose a typed function as an agent tool

### 24. A coordinator must choose among billing, technical, and account specialists and merge their answers. Which pattern fits?

Domain: Implement generative AI and agentic solutions

- A. Use a manager agent to coordinate specialists
- B. Transfer control between agents with explicit context
- C. Use self-critique or reflection to improve drafts
- D. Run independent agents concurrently

### 25. An agent fails only when a request needs two sequential tool calls. What should be inspected?

Domain: Implement generative AI and agentic solutions

- A. Apply watermarks or provenance markers to generated media
- B. Enable tracing across agent, model, and tool calls
- C. Use supported prompt or response caching where appropriate
- D. Lower temperature for more deterministic extraction

### 26. The intent router returns different categories for the same submitted message on retry. Which setting should be lowered?

Domain: Implement generative AI and agentic solutions

- A. Lower temperature for more deterministic extraction
- B. Route requests to different models by task difficulty
- C. Adjust top-p to control response diversity
- D. Use supported prompt or response caching where appropriate

### 27. Operations must learn within minutes when refusal rates spike. What should be configured?

Domain: Implement generative AI and agentic solutions

- A. Use Azure Monitor and Application Insights for telemetry
- B. Alert on latency, error rate, safety, and cost thresholds
- C. Monitor input and quality drift over time
- D. Preserve audit logs of changes, approvals, and tool actions

### 28. A group needs an original illustration for a safety campaign. Which capability applies?

Domain: Implement computer vision solutions

- A. Generate video from text or reference media
- B. Generate alt text aligned to accessibility guidance
- C. Generate images from text and reference media
- D. Edit a region of an image with a mask

### 29. A photograph must have an outdated sign replaced while the people in it stay unchanged. What should be used?

Domain: Implement computer vision solutions

- A. Edit generated video segments
- B. Generate concise or detailed image captions
- C. Apply prompt-driven image modifications
- D. Edit a region of an image with a mask

### 30. A team must find the timestamp in recorded footage when a queue exceeds a threshold. Which capability applies?

Domain: Implement computer vision solutions

- A. Edit generated video segments
- B. Generate concise or detailed image captions
- C. Analyze video segments for events and content
- D. Generate video from text or reference media

### 31. The corporate site needs image descriptions for search and for screen readers. Which two capabilities apply? Select two.

Domain: Implement computer vision solutions

- A. Lower temperature for more deterministic extraction
- B. Generate concise or detailed image captions
- C. Apply watermarks or provenance markers to generated media
- D. Use provisioned throughput for predictable high-volume workloads
- E. Generate alt text aligned to accessibility guidance

### 32. Mixed supplier packets contain photos, tables, and handwriting across many pages. Which Content Understanding mode should be evaluated?

Domain: Implement computer vision solutions

- A. Train a custom extraction model on labeled documents
- B. Use single-task mode for a focused extraction scenario
- C. Use pro mode for complex multimodal content understanding
- D. Use Azure AI Document Intelligence for forms and documents

### 33. Generated images appear in external communications and must be identifiable and on-brand. Which two controls apply? Select two.

Domain: Implement computer vision solutions

- A. Enforce brand and usage rules for generated visuals
- B. Apply watermarks or provenance markers to generated media
- C. Lower temperature for more deterministic extraction
- D. Use supported prompt or response caching where appropriate
- E. Adjust top-p to control response diversity

### 34. An assistant reads scanned letters, one of which instructs it to reveal another customer's contract. What risk is this?

Domain: Implement computer vision solutions

- A. Filter unsafe or disallowed visual content
- B. Treat text embedded in images as untrusted input
- C. Generate concise or detailed image captions
- D. Apply watermarks or provenance markers to generated media

### 35. A ticketing system requires fixed field names and types from each complaint. What should the prompt request?

Domain: Implement text analysis solutions

- A. Generate summaries with explicit length and audience constraints
- B. Use Azure Translator or a language model for translation
- C. Identify topics or key phrases for navigation
- D. Prompt for JSON that conforms to a supplied schema

### 36. A shared mailbox must find personal data and detect rising frustration. Which two analyses apply? Select two.

Domain: Implement text analysis solutions

- A. Apply a custom glossary or terminology list
- B. Analyze sentiment and tone with an appropriate service
- C. Generate summaries with explicit length and audience constraints
- D. Identify topics or key phrases for navigation
- E. Detect and redact sensitive personal data

### 37. Translations keep mangling approved product and legal names. What should be configured?

Domain: Implement text analysis solutions

- A. Apply a custom glossary or terminology list
- B. Extract entities with defined types and boundaries
- C. Detect and redact sensitive personal data
- D. Use Azure Translator or a language model for translation

### 38. Notices must appear in ten languages while retaining statutory wording. Which two practices help? Select two.

Domain: Implement text analysis solutions

- A. Extract entities with defined types and boundaries
- B. Use Azure Translator or a language model for translation
- C. Identify topics or key phrases for navigation
- D. Customize summaries and extraction for compliance needs
- E. Generate summaries with explicit length and audience constraints

### 39. A customer speaks Portuguese and must hear an answer in Portuguese. Which sequence is correct?

Domain: Implement text analysis solutions

- A. Transcribe → synthesize speech → capture audio → translate → return audio
- B. Translate audio → transcribe → capture audio → synthesize → return audio
- C. Capture audio → synthesize speech → transcribe → translate → return audio
- D. Capture audio → transcribe → translate text → synthesize speech → return audio

### 40. Recorded service calls must become searchable transcripts. Which capability applies?

Domain: Implement text analysis solutions

- A. Translate spoken language with speech translation
- B. Synthesize speech with Azure AI Speech
- C. Transcribe speech to text with Azure AI Speech
- D. Generate concise or detailed image captions

### 41. Extraction misses internal abbreviations used by only one subsidiary. What should be added?

Domain: Implement text analysis solutions

- A. Adapt prompts and models to domain terminology
- B. Detect and redact sensitive personal data
- C. Apply a custom glossary or terminology list
- D. Use Azure Translator or a language model for translation

### 42. An index must follow documents added to storage without custom code. What should be used?

Domain: Implement information extraction solutions

- A. Add an enrichment skillset to an indexing pipeline
- B. Use an Azure AI Search indexer to pull source content
- C. Push documents to an index through the data-plane API
- D. Apply OCR to convert images and scans into usable text

### 43. Subsidiaries share one index, and each must see only its own approved documents. What must be enforced?

Domain: Implement information extraction solutions

- A. Verify index freshness and deletion propagation
- B. Combine keyword and vector retrieval
- C. Apply document-level security filters at query time
- D. Apply semantic ranking to reorder search results

### 44. Which sequence correctly builds a citable retrieval pipeline over group policies?

Domain: Implement information extraction solutions

- A. Ingest → retrieve → chunk → embed → index → cite
- B. Ingest → extract text → chunk → embed → index → retrieve with citations
- C. Chunk → embed → ingest → retrieve → index → cite
- D. Index → retrieve → ingest → chunk → embed → cite

### 45. A global group must keep one approved model version per jurisdiction for a year and cannot rely on latest. What should the team do?

Domain: Plan and manage an Azure AI solution

- A. Use a general-purpose large language model for complex reasoning
- B. Train or deploy a task-specific model outside the prebuilt catalog
- C. Compare supported models in the Foundry model catalog
- D. Pin the model version available in the required region

### 46. A subsidiary needs captioning and transcription this quarter and has no labelled data. What should be evaluated first?

Domain: Plan and manage an Azure AI solution

- A. Use a small language model for a narrow, high-volume task
- B. Use a general-purpose large language model for complex reasoning
- C. Train or deploy a task-specific model outside the prebuilt catalog
- D. Use Foundry Tools for prebuilt vision, speech, language, and extraction needs

### 47. An agent must call a group-wide inventory API whose operations are published as a machine-readable contract. Which tool type fits?

Domain: Plan and manage an Azure AI solution

- A. Connect an Azure AI Search index as agent knowledge
- B. Expose a typed function as an agent tool
- C. Expose an OpenAPI operation as an agent tool
- D. Use managed conversation state or memory for continuity

### 48. A shared release must be blocked automatically when groundedness on the group test set drops. What should be added?

Domain: Plan and manage an Azure AI solution

- A. Shift a small traffic percentage to the new version first
- B. Block promotion in the pipeline when evaluation thresholds fail
- C. Manage AI resources with infrastructure as code and CI/CD
- D. Use staged rollout with measurable rollback criteria

### 49. The group wants a candidate assistant compared with live answers without any customer seeing them. What pattern fits?

Domain: Plan and manage an Azure AI solution

- A. Shift a small traffic percentage to the new version first
- B. Send mirrored production traffic to a candidate without returning its answers
- C. Use batch processing for latency-tolerant bulk work
- D. Use a standard pay-as-you-go model deployment for variable demand

### 50. The group finance team wants warning before a business unit's monthly AI spend exceeds its budget. What should be configured?

Domain: Plan and manage an Azure AI solution

- A. Track prompt, completion, and cached token usage
- B. Track cost per accepted task, not only per token
- C. Plan for model quota expressed in tokens and requests per minute
- D. Alert on spend thresholds per deployment or project

### 51. Subsidiaries are shown a group policy that was withdrawn last week. What should be monitored?

Domain: Plan and manage an Azure AI solution

- A. Monitor index freshness, failures, and document counts
- B. Monitor input and quality drift over time
- C. Monitor groundedness and citation quality in production
- D. Use Azure Monitor and Application Insights for telemetry

### 52. The group workload may reach only approved services in each region. What should be enforced?

Domain: Plan and manage an Azure AI solution

- A. Private networking with public access left enabled
- B. Restrict outbound network access to approved destinations
- C. Use least-privilege Azure RBAC roles for the workload identity
- D. Use private endpoints and disable public network access

### 53. A group-level pricing exception must remain attributable to a named commercial owner. Which principle applies?

Domain: Plan and manage an Azure AI solution

- A. Set agent oversight mode and tool-access constraints
- B. Enforce constraints in code and platform policy
- C. Require human approval before consequential actions
- D. Preserve audit logs of changes, approvals, and tool actions

### 54. Six years of group correspondence must be re-summarized once for a records migration. Which deployment option fits?

Domain: Plan and manage an Azure AI solution

- A. Use batch processing for latency-tolerant bulk work
- B. Plan for model quota expressed in tokens and requests per minute
- C. Use a standard pay-as-you-go model deployment for variable demand
- D. Use provisioned throughput for predictable high-volume workloads

### 55. A shared model must be chosen per jurisdiction and must not change during a fiscal audit. Which two practices are required? Select two.

Domain: Plan and manage an Azure AI solution

- A. Use batch processing for latency-tolerant bulk work
- B. Pin the model version available in the required region
- C. Compare supported models in the Foundry model catalog
- D. Train or deploy a task-specific model outside the prebuilt catalog
- E. Use a standard pay-as-you-go model deployment for variable demand

### 56. The group assistant must be checked for unsupported claims and regional teams must hear quickly. Which two capabilities are required? Select two.

Domain: Plan and manage an Azure AI solution

- A. Apply watermarks or provenance markers to generated media
- B. Measure end-to-end latency across model, retrieval, and tools
- C. Alert on latency, error rate, safety, and cost thresholds
- D. Monitor groundedness and citation quality in production
- E. Track cost per accepted task, not only per token

### 57. Each subsidiary must be unable to call unapproved services and must hold only its own permissions. Which two controls are required? Select two.

Domain: Plan and manage an Azure AI solution

- A. Restrict outbound network access to approved destinations
- B. Configure content safety filters for harmful categories
- C. Store secrets in Azure Key Vault when keys are unavoidable
- D. Use least-privilege Azure RBAC roles for the workload identity
- E. Use private endpoints and disable public network access

### 58. Which sequence correctly releases a group-wide change through an evaluation gate?

Domain: Plan and manage an Azure AI solution

- A. Commit change → deploy a canary → promote after metrics hold → run the evaluation suite → block on failed thresholds
- B. Run the evaluation suite → deploy a canary → commit change → block on failed thresholds → promote after metrics hold
- C. Deploy a canary → commit change → promote after metrics hold → run the evaluation suite → block on failed thresholds
- D. Commit change → run the evaluation suite → block on failed thresholds → deploy a canary → promote after metrics hold

### 59. A warranty term split across two sections is never retrieved. What should be adjusted?

Domain: Implement generative AI and agentic solutions

- A. Choose an embedding model suited to the content and language
- B. Set chunk overlap so facts spanning a boundary stay retrievable
- C. Select evidence within the model's usable context
- D. Choose chunk size and overlap for retrieval quality

### 60. Group policy changes monthly and every answer must cite the controlled document. Which approach fits?

Domain: Implement generative AI and agentic solutions

- A. Ground responses with retrieval-augmented generation
- B. Route requests to different models by task difficulty
- C. Include representative examples in the prompt
- D. Design multistep workflows with explicit checkpoints

### 61. A subsidiary web app must call the model service with a short-lived delegated credential. What should it request?

Domain: Implement generative AI and agentic solutions

- A. Use a Foundry SDK or supported connector from application code
- B. Store secrets in Azure Key Vault when keys are unavoidable
- C. Authenticate with a managed identity instead of keys
- D. Use short-lived scoped access tokens for tool calls

### 62. Four prompt variants must be compared on identical group cases. What provides that?

Domain: Implement generative AI and agentic solutions

- A. Build a representative golden dataset from real tasks
- B. Re-run evaluation suites after meaningful changes
- C. Use evaluators for quality, safety, and groundedness
- D. Compare variants with controlled traffic and shared metrics

### 63. A group upgrade must not restore a packaging advice error that was fixed last quarter. What should run first?

Domain: Implement generative AI and agentic solutions

- A. Evaluate harmful, biased, or policy-violating output
- B. Use evaluators for quality, safety, and groundedness
- C. Build a representative golden dataset from real tasks
- D. Re-run evaluation suites after meaningful changes

### 64. The agent keeps submitting a warranty claim reference without its region prefix. What should be tightened first?

Domain: Implement generative AI and agentic solutions

- A. Put stable behavior rules in the system message
- B. Use managed conversation state or memory for continuity
- C. Define narrow tool schemas with clear descriptions
- D. Route requests to different models by task difficulty

### 65. A group assistant must transfer a customs question to the trade specialist with context. Which pattern fits?

Domain: Implement generative AI and agentic solutions

- A. Run independent agents concurrently
- B. Transfer control between agents with explicit context
- C. Use a manager agent to coordinate specialists
- D. Use self-critique or reflection to improve drafts

### 66. Three independent credit checks must finish inside two seconds. Which pattern fits?

Domain: Implement generative AI and agentic solutions

- A. Use self-critique or reflection to improve drafts
- B. Run agents in a fixed sequence
- C. Run independent agents concurrently
- D. Use a manager agent to coordinate specialists

### 67. Generated rebate records include prose that breaks the parser. What should be specified?

Domain: Implement generative AI and agentic solutions

- A. Use supported prompt or response caching where appropriate
- B. Lower temperature for more deterministic extraction
- C. Adjust top-p to control response diversity
- D. Set a stop sequence so generation ends at the intended boundary

### 68. Supplier letters repeat identical phrasing and never vary. Which parameter should be adjusted?

Domain: Implement generative AI and agentic solutions

- A. Adjust top-p to control response diversity
- B. Lower temperature for more deterministic extraction
- C. Use supported prompt or response caching where appropriate
- D. Set a seed parameter for reproducible sampling where the provider supports it

### 69. A subsidiary service must use maintained client behaviour and store no credential. Which two choices are required? Select two.

Domain: Implement generative AI and agentic solutions

- A. Use a Foundry SDK or supported connector from application code
- B. Create and run deployments by hand in the portal
- C. Authenticate with a managed identity instead of keys
- D. Use short-lived scoped access tokens for tool calls
- E. Store secrets in Azure Key Vault when keys are unavoidable

### 70. A group release must be scored for accuracy and screened for unsafe commercial advice. Which two practices are required? Select two.

Domain: Implement generative AI and agentic solutions

- A. Use evaluators for quality, safety, and groundedness
- B. Re-run evaluation suites after meaningful changes
- C. Build a representative golden dataset from real tasks
- D. Evaluate harmful, biased, or policy-violating output
- E. Compare variants with controlled traffic and shared metrics

### 71. A warranty agent must search approved terms and compute settlement amounts reliably. Which two tools are required? Select two.

Domain: Implement generative AI and agentic solutions

- A. Expose an OpenAPI operation as an agent tool
- B. Enable a sandboxed code interpreter tool for calculations
- C. Give the agent a file-search tool over approved document stores
- D. Use managed conversation state or memory for continuity
- E. Route requests to different models by task difficulty

### 72. Which sequence correctly builds and releases a group warranty agent?

Domain: Implement generative AI and agentic solutions

- A. Configure tools → deploy with monitoring → define role and goal → attach knowledge → evaluate in sandbox
- B. Define role and goal → configure tools → attach knowledge → evaluate in sandbox → deploy with monitoring
- C. Attach knowledge → configure tools → deploy with monitoring → define role and goal → evaluate in sandbox
- D. Deploy with monitoring → define role and goal → configure tools → evaluate in sandbox → attach knowledge

### 73. A generated campaign image passes automated checks but regional teams consider it culturally inappropriate. What should be added?

Domain: Implement computer vision solutions

- A. Enforce brand and usage rules for generated visuals
- B. Queue flagged generations for human moderation before release
- C. Filter unsafe or disallowed visual content
- D. Apply watermarks or provenance markers to generated media

### 74. A group product archive needs filterable descriptive tags across markets. What should be generated?

Domain: Implement computer vision solutions

- A. Generate a set of descriptive tags for each image
- B. Generate concise or detailed image captions
- C. Answer questions grounded in visual evidence
- D. Generate alt text aligned to accessibility guidance

### 75. Extracted supplier contracts are scrambled because the layout is read incorrectly. What should be applied?

Domain: Implement computer vision solutions

- A. Preserve reading order across columns and sections
- B. Produce markdown representations for downstream reasoning
- C. Apply OCR to convert images and scans into usable text
- D. Preserve document layout, tables, and reading order

### 76. A team needs a configurable analyzer over mixed contracts and correspondence rather than a fixed prebuilt model. Which service fits?

Domain: Implement computer vision solutions

- A. Use Azure Content Understanding analyzers in Foundry Tools
- B. Use Azure AI Document Intelligence for forms and documents
- C. Configure a Content Understanding analyzer for the content type
- D. Use a prebuilt document model for common document types

### 77. Supplier packets mix tables, stamps, and photos, and output must feed a reasoning model. Which two choices are required? Select two.

Domain: Implement computer vision solutions

- A. Identify objects, components, or regions in visual content
- B. Return markdown for retrieval and reasoning pipelines
- C. Generate concise or detailed image captions
- D. Use single-task mode for a focused extraction scenario
- E. Use pro mode for complex multimodal content understanding

### 78. Which sequence correctly processes a scanned claim packet and routes doubtful values to a person?

Domain: Implement computer vision solutions

- A. Upload image → validate format and size → send multimodal request → parse structured fields → route low-confidence values to review
- B. Validate format → review → upload image → parse structured fields → send multimodal request
- C. Send multimodal request → upload image → validate format → parse structured fields → review
- D. Parse structured fields → send multimodal request → upload image → validate format → review

### 79. Group audit requires summaries that quote exact contract sentences. Which style fits?

Domain: Implement text analysis solutions

- A. Generate summaries with explicit length and audience constraints
- B. Generate an abstractive summary in new wording
- C. Select and return the most relevant source sentences
- D. Customize summaries and extraction for compliance needs

### 80. Supplier and payee names in another writing system must print correctly on remittance advice without changing their meaning. Which capability applies?

Domain: Implement text analysis solutions

- A. Apply a custom glossary or terminology list
- B. Adapt prompts and models to domain terminology
- C. Use Azure Translator or a language model for translation
- D. Convert names between writing systems without translating meaning

### 81. A group contact line must use one consistent voice across markets. What should be selected?

Domain: Implement text analysis solutions

- A. Use a custom speech model for specialized vocabulary
- B. Synthesize speech with Azure AI Speech
- C. Select a specific synthesis voice for consistent spoken output
- D. Apply a custom glossary or terminology list

### 82. Group analysts need a quick topical index of what each claim file covers. Which capability applies?

Domain: Implement text analysis solutions

- A. Extract entities with defined types and boundaries
- B. Identify topics or key phrases for navigation
- C. Extract key phrases to summarize what a document covers
- D. Generate summaries with explicit length and audience constraints

### 83. A group mailbox must detect personal data and rising frustration. Which two analyses are relevant? Select two.

Domain: Implement text analysis solutions

- A. Detect and redact sensitive personal data
- B. Analyze sentiment and tone with an appropriate service
- C. Apply a custom glossary or terminology list
- D. Identify topics or key phrases for navigation
- E. Generate summaries with explicit length and audience constraints

### 84. Searches for a SKU return unrelated campaign pages because one family dominates. What should be tuned and measured?

Domain: Implement information extraction solutions

- A. Use a vector index for semantic retrieval
- B. Combine keyword and vector retrieval
- C. Apply semantic ranking to reorder search results
- D. Tune scoring and boosting against a labelled query set

### 85. Each indexed group policy must gain extracted obligations and a generated abstract. What produces that?

Domain: Implement information extraction solutions

- A. Return markdown for retrieval and reasoning pipelines
- B. Add enrichment skills for text, image, and layout
- C. Add an enrichment skillset to an indexing pipeline
- D. Use an Azure AI Search indexer to pull source content

### 86. Buyers must filter by contract year and sort by value, but those fields are full-text only. What should change?

Domain: Implement information extraction solutions

- A. Define index fields, attributes, and searchable versus filterable behavior
- B. Use Azure AI Document Intelligence for forms and documents
- C. Return typed fields for automation
- D. Configure a Content Understanding analyzer for the content type

### 87. Scanned contracts must preserve schedule relationships for extraction. What should be applied?

Domain: Implement information extraction solutions

- A. Combine OCR with layout analysis for complex documents
- B. Use an Azure AI Search indexer to pull source content
- C. Choose chunk size and overlap for retrieval quality
- D. Produce markdown representations for downstream reasoning

### 88. Which sequence correctly builds a group policy index?

Domain: Implement information extraction solutions

- A. Run the indexer → connect the data source → define the index schema → attach the enrichment skillset → validate relevance on sample queries
- B. Connect the data source → define the index schema → attach the enrichment skillset → run the indexer → validate relevance on sample queries
- C. Validate relevance on sample queries → run the indexer → connect the data source → define the index schema → attach the enrichment skillset
- D. Attach the enrichment skillset → connect the data source → validate relevance on sample queries → define the index schema → run the indexer

---

## Case study — GlobalMart

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 89. A category manager needs margin percentages computed across extracted supplier lines. Which tool is required?

Domain: Implement generative AI and agentic solutions

- A. Expose an OpenAPI operation as an agent tool
- B. Give the agent a file-search tool over approved document stores
- C. Use managed conversation state or memory for continuity
- D. Enable a sandboxed code interpreter tool for calculations

### 90. An order status request fails only after the second tool call. What should be inspected?

Domain: Implement generative AI and agentic solutions

- A. Apply watermarks or provenance markers to generated media
- B. Use supported prompt or response caching where appropriate
- C. Lower temperature for more deterministic extraction
- D. Enable tracing across agent, model, and tool calls

### 91. Newly generated supplier notices must be searchable within seconds. What should the application use?

Domain: Implement information extraction solutions

- A. Push documents to an index through the data-plane API
- B. Add an enrichment skillset to an indexing pipeline
- C. Use an Azure AI Search indexer to pull source content
- D. Apply OCR to convert images and scans into usable text

---

## Case study — GroupAssist

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 92. One subsidiary runs continuous, predictable volume and cannot tolerate throttling. Which capacity option should be evaluated?

Domain: Plan and manage an Azure AI solution

- A. Use batch processing for latency-tolerant bulk work
- B. Use a standard pay-as-you-go model deployment for variable demand
- C. Use provisioned throughput for predictable high-volume workloads
- D. Use supported prompt or response caching where appropriate

### 93. Auditors must verify each answer against an approved policy page. Which capability makes that possible?

Domain: Implement generative AI and agentic solutions

- A. Apply watermarks or provenance markers to generated media
- B. Require citations tied to retrieved evidence
- C. Lower temperature for more deterministic extraction
- D. Use supported prompt or response caching where appropriate

### 94. Long policy evidence crowds out the question and the model starts drifting. What should be configured?

Domain: Implement information extraction solutions

- A. Rerank retrieved passages before generation
- B. Select evidence within the model's usable context
- C. Use a vector index for semantic retrieval
- D. Remove near-duplicate evidence before ranking

---

## Case study — NovaRetail

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 95. A franchisee returns to the same claim after a break and the assistant must recall the claim number. Which capability is required?

Domain: Implement generative AI and agentic solutions

- A. Choose an embedding model suited to the content and language
- B. Use provisioned throughput for predictable high-volume workloads
- C. Persist conversation history in a thread or session
- D. Apply watermarks or provenance markers to generated media

### 96. Store call transcripts misread local product codes that drive warranty routing. What should be trained?

Domain: Implement text analysis solutions

- A. Use a custom speech model for specialized vocabulary
- B. Apply a custom glossary or terminology list
- C. Synthesize speech with Azure AI Speech
- D. Transcribe speech to text with Azure AI Speech

### 97. Scanned supplier values are sometimes misread. What should route those values to a person?

Domain: Implement information extraction solutions

- A. Analyze sentiment and tone with an appropriate service
- B. Generate summaries with explicit length and audience constraints
- C. Measure whether retrieved content and answers address the question
- D. Use field-level confidence to route exceptions

---

## Case study — WarrantyDesk

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 98. A warranty agent must keep a case number across turns and check it in a claims system. Which two capabilities are required? Select two.

Domain: Implement generative AI and agentic solutions

- A. Choose an embedding model suited to the content and language
- B. Apply watermarks or provenance markers to generated media
- C. Expose a typed function as an agent tool
- D. Use provisioned throughput for predictable high-volume workloads
- E. Persist conversation history in a thread or session

### 99. One subsidiary uses a proprietary claim form that no prebuilt model covers. What should be built?

Domain: Implement information extraction solutions

- A. Use Azure AI Document Intelligence for forms and documents
- B. Train a custom extraction model on labeled documents
- C. Configure a Content Understanding analyzer for the content type
- D. Use a prebuilt document model for common document types

### 100. Every indexed policy must gain extracted entities and a summary during ingestion. Which component defines those steps?

Domain: Implement information extraction solutions

- A. Apply OCR to convert images and scans into usable text
- B. Push documents to an index through the data-plane API
- C. Add an enrichment skillset to an indexing pipeline
- D. Add enrichment skills for text, image, and layout

---

## Answer key and explanations

### Question 1 — D

Answer: Compare supported models in the Foundry model catalog. The catalog records modality support, regional availability, and lifecycle for each model. The catalog shows supported models with capability, modality, region, and lifecycle details. Verify availability for your subscription and region before designing around one model. Local study-map skill 1.1 (Selecting Foundry Models and Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Small models can reduce latency and cost for constrained classification or extraction. Confirm quality on representative data before standardizing. Why the correct answer wins: The catalog records modality support, regional availability, and lifecycle for each model.
- **B:** Incorrect for this question. A custom model is justified when supported prebuilt options cannot meet a defined requirement. It adds data, evaluation, and lifecycle obligations. Why the correct answer wins: The catalog records modality support, regional availability, and lifecycle for each model.
- **C:** Incorrect for this question. Large models handle ambiguity and multi-step reasoning better in many cases, at higher cost and latency. Select with measured evidence rather than brand preference. Why the correct answer wins: The catalog records modality support, regional availability, and lifecycle for each model.
- **D:** Correct. The catalog shows supported models with capability, modality, region, and lifecycle details. Verify availability for your subscription and region before designing around one model. In this case: The catalog records modality support, regional availability, and lifecycle for each model.

### Question 2 — C

Answer: Train or deploy a task-specific model outside the prebuilt catalog. A custom or fine-tuned model is trained on organization data under its governance. A custom model is justified when supported prebuilt options cannot meet a defined requirement. It adds data, evaluation, and lifecycle obligations. Local study-map skill 1.1 (Selecting Foundry Models and Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Large models handle ambiguity and multi-step reasoning better in many cases, at higher cost and latency. Select with measured evidence rather than brand preference. Why the correct answer wins: A custom or fine-tuned model is trained on organization data under its governance.
- **B:** Incorrect for this question. Small models can reduce latency and cost for constrained classification or extraction. Confirm quality on representative data before standardizing. Why the correct answer wins: A custom or fine-tuned model is trained on organization data under its governance.
- **C:** Correct. A custom model is justified when supported prebuilt options cannot meet a defined requirement. It adds data, evaluation, and lifecycle obligations. In this case: A custom or fine-tuned model is trained on organization data under its governance.
- **D:** Incorrect for this question. Multimodal models accept more than one content type in a request. Validate extraction and grounding quality for each modality used. Why the correct answer wins: A custom or fine-tuned model is trained on organization data under its governance.

### Question 3 — D

Answer: Use managed conversation state or memory for continuity. Conversation state keeps previous turns available to the agent. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Local study-map skill 1.2 (Retrieval, Memory, Tool, and Knowledge Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. Why the correct answer wins: Conversation state keeps previous turns available to the agent.
- **B:** Incorrect for this question. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. Why the correct answer wins: Conversation state keeps previous turns available to the agent.
- **C:** Incorrect for this question. Embeddings support similarity search over meaning rather than exact terms. Vector search still needs chunking, filtering, and evaluation. Why the correct answer wins: Conversation state keeps previous turns available to the agent.
- **D:** Correct. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. In this case: Conversation state keeps previous turns available to the agent.

### Question 4 — C

Answer: Provision resources → deploy model → configure app connection → evaluate → promote. Provisioning and deployment come first, configuration follows, and evaluation gates promotion. Provisioning and deployment precede app configuration, and evaluation gates promotion. Local study-map skill 1.3 (Infrastructure, Deployment, and CI/CD), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Promotion before provisioning and evaluation skips the controls that make deployment safe. Why the correct answer wins: Provisioning and deployment come first, configuration follows, and evaluation gates promotion.
- **B:** Incorrect for this question. Evaluation before any deployment or configuration has nothing meaningful to assess. Why the correct answer wins: Provisioning and deployment come first, configuration follows, and evaluation gates promotion.
- **C:** Correct. Provisioning and deployment precede app configuration, and evaluation gates promotion. In this case: Provisioning and deployment come first, configuration follows, and evaluation gates promotion.
- **D:** Incorrect for this question. Evaluation after promotion cannot gate the release. Why the correct answer wins: Provisioning and deployment come first, configuration follows, and evaluation gates promotion.

### Question 5 — C

Answer: Use private endpoints and disable public network access. A private endpoint keeps model traffic on the private network path. Private connectivity keeps service traffic on approved network paths. Pair it with private DNS so clients resolve the private address. Local study-map skill 1.3 (Infrastructure, Deployment, and CI/CD), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Repeatable deployments reduce configuration drift. Include model deployments, indexes, and connections in review and promotion. Why the correct answer wins: A private endpoint keeps model traffic on the private network path.
- **B:** Incorrect for this question. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. Why the correct answer wins: A private endpoint keeps model traffic on the private network path.
- **C:** Correct. Private connectivity keeps service traffic on approved network paths. Pair it with private DNS so clients resolve the private address. In this case: A private endpoint keeps model traffic on the private network path.
- **D:** Incorrect for this question. Retries, tool calls, evaluation, and review contribute to unit economics. Per-outcome cost supports better optimization. Why the correct answer wins: A private endpoint keeps model traffic on the private network path.

### Question 6 — B

Answer: Plan for model quota expressed in tokens and requests per minute. Request and token quota must cover the real peak concurrency. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. Local study-map skill 1.4 (Quotas, Scaling, and Cost), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: Request and token quota must cover the real peak concurrency.
- **B:** Correct. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. In this case: Request and token quota must cover the real peak concurrency.
- **C:** Incorrect for this question. Retries, tool calls, evaluation, and review contribute to unit economics. Per-outcome cost supports better optimization. Why the correct answer wins: Request and token quota must cover the real peak concurrency.
- **D:** Incorrect for this question. User behavior, data, and models change. Rolling baselines reveal degradation that a one-time evaluation misses. Why the correct answer wins: Request and token quota must cover the real peak concurrency.

### Question 7 — B

Answer: Track cost per accepted task, not only per token. Prompt caching reuses the repeated policy prefix instead of re-billing it. Retries, tool calls, evaluation, and review contribute to unit economics. Per-outcome cost supports better optimization. Local study-map skill 1.4 (Quotas, Scaling, and Cost), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. Why the correct answer wins: Prompt caching reuses the repeated policy prefix instead of re-billing it.
- **B:** Correct. Retries, tool calls, evaluation, and review contribute to unit economics. Per-outcome cost supports better optimization. In this case: Prompt caching reuses the repeated policy prefix instead of re-billing it.
- **C:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Prompt caching reuses the repeated policy prefix instead of re-billing it.
- **D:** Incorrect for this question. User behavior, data, and models change. Rolling baselines reveal degradation that a one-time evaluation misses. Why the correct answer wins: Prompt caching reuses the repeated policy prefix instead of re-billing it.

### Question 8 — D

Answer: Use Azure Monitor and Application Insights for telemetry. Platform monitoring centralizes metrics and logs for operations. Central telemetry captures latency, errors, dependencies, and custom events. Redact sensitive content before logging. Local study-map skill 1.5 (Monitoring Performance, Drift, Safety, and Grounding), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Audit evidence supports investigation and accountability. Protect log integrity and retention. Why the correct answer wins: Platform monitoring centralizes metrics and logs for operations.
- **B:** Incorrect for this question. Alerts turn monitoring into action. Route them to an accountable owner with a runbook. Why the correct answer wins: Platform monitoring centralizes metrics and logs for operations.
- **C:** Incorrect for this question. User behavior, data, and models change. Rolling baselines reveal degradation that a one-time evaluation misses. Why the correct answer wins: Platform monitoring centralizes metrics and logs for operations.
- **D:** Correct. Central telemetry captures latency, errors, dependencies, and custom events. Redact sensitive content before logging. In this case: Platform monitoring centralizes metrics and logs for operations.

### Question 9 — D

Answer: Re-run evaluation suites after meaningful changes. Regression evaluation re-runs known failure cases against the candidate. Prompts, models, indexes, and tools all affect behavior. Regression tests catch unintended effects. Local study-map skill 1.5 (Monitoring Performance, Drift, Safety, and Grounding), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. A golden set anchors evaluation in expected behavior. Include edge cases and high-risk scenarios. Why the correct answer wins: Regression evaluation re-runs known failure cases against the candidate.
- **B:** Incorrect for this question. Evaluators provide repeatable signals across models and prompts. They must be calibrated against human judgment for high-impact work. Why the correct answer wins: Regression evaluation re-runs known failure cases against the candidate.
- **C:** Incorrect for this question. Controlled comparison supports evidence-based change. Avoid changing several variables at once. Why the correct answer wins: Regression evaluation re-runs known failure cases against the candidate.
- **D:** Correct. Prompts, models, indexes, and tools all affect behavior. Regression tests catch unintended effects. In this case: Regression evaluation re-runs known failure cases against the candidate.

### Question 10 — D

Answer: Authenticate with a managed identity instead of keys. A managed identity obtains Entra ID tokens without stored credentials. Managed identities avoid embedded secrets and support role-based access. Assign only required data-plane roles. Local study-map skill 1.6 (Security, Identity, and Networking), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. A managed secret store supports rotation and access control. Secrets should never appear in prompts, code, or logs. Why the correct answer wins: A managed identity obtains Entra ID tokens without stored credentials.
- **B:** Incorrect for this question. Static keys are easily leaked, hard to rotate across services, and provide no per-identity authorization. Why the correct answer wins: A managed identity obtains Entra ID tokens without stored credentials.
- **C:** Incorrect for this question. A shared secret grants broad access, cannot be scoped per workload, and complicates rotation and auditing. Why the correct answer wins: A managed identity obtains Entra ID tokens without stored credentials.
- **D:** Correct. Managed identities avoid embedded secrets and support role-based access. Assign only required data-plane roles. In this case: A managed identity obtains Entra ID tokens without stored credentials.

### Question 11 — B

Answer: Set agent oversight mode and tool-access constraints. Human oversight keeps consequential decisions accountable to people. Oversight settings bound what an agent may do autonomously. They should be tested against realistic misuse and failure. Local study-map skill 1.7 (Responsible AI Controls and Oversight), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Guardrails are technical controls, not prompt suggestions. Validate inputs, authorize tools, and limit egress. Why the correct answer wins: Human oversight keeps consequential decisions accountable to people.
- **B:** Correct. Oversight settings bound what an agent may do autonomously. They should be tested against realistic misuse and failure. In this case: Human oversight keeps consequential decisions accountable to people.
- **C:** Incorrect for this question. Approval must occur before the effect and identify who approved what. A model confidence score is not approval. Why the correct answer wins: Human oversight keeps consequential decisions accountable to people.
- **D:** Incorrect for this question. Audit evidence supports investigation and accountability. Protect log integrity and retention. Why the correct answer wins: Human oversight keeps consequential decisions accountable to people.

### Question 12 — D, E

Answers: Use least-privilege Azure RBAC roles for the workload identity; Use private endpoints and disable public network access. Least-privilege role assignment scopes access, and private endpoints remove public exposure. Roles should match the operations the app or agent performs. Broad contributor access increases blast radius. Private connectivity keeps service traffic on approved network paths. Pair it with private DNS so clients resolve the private address. Local study-map skill 1.6 (Security, Identity, and Networking), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Filters assign severity and can block or annotate content. Thresholds should reflect the use case and applicable policy. Why the correct answer wins: Least-privilege role assignment scopes access, and private endpoints remove public exposure.
- **B:** Incorrect for this question. A managed secret store supports rotation and access control. Secrets should never appear in prompts, code, or logs. Why the correct answer wins: Least-privilege role assignment scopes access, and private endpoints remove public exposure.
- **C:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Least-privilege role assignment scopes access, and private endpoints remove public exposure.
- **D:** Correct. Roles should match the operations the app or agent performs. Broad contributor access increases blast radius. In this case: Least-privilege role assignment scopes access, and private endpoints remove public exposure.
- **E:** Correct. Private connectivity keeps service traffic on approved network paths. Pair it with private DNS so clients resolve the private address. In this case: Least-privilege role assignment scopes access, and private endpoints remove public exposure.

### Question 13 — C, E

Answers: Configure content safety filters for harmful categories; Require human approval before consequential actions. Content filters reduce harmful output, and approval gates control credit issuance. Filters assign severity and can block or annotate content. Thresholds should reflect the use case and applicable policy. Approval must occur before the effect and identify who approved what. A model confidence score is not approval. Local study-map skill 1.7 (Responsible AI Controls and Oversight), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Small models can reduce latency and cost for constrained classification or extraction. Confirm quality on representative data before standardizing. Why the correct answer wins: Content filters reduce harmful output, and approval gates control credit issuance.
- **B:** Incorrect for this question. Top-p narrows or broadens token sampling. Tune with evaluation rather than by intuition. Why the correct answer wins: Content filters reduce harmful output, and approval gates control credit issuance.
- **C:** Correct. Filters assign severity and can block or annotate content. Thresholds should reflect the use case and applicable policy. In this case: Content filters reduce harmful output, and approval gates control credit issuance.
- **D:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Content filters reduce harmful output, and approval gates control credit issuance.
- **E:** Correct. Approval must occur before the effect and identify who approved what. A model confidence score is not approval. In this case: Content filters reduce harmful output, and approval gates control credit issuance.

### Question 14 — C

Answer: Ground responses with retrieval-augmented generation. RAG retrieves current approved evidence and supports citations. RAG supplies selected source content at request time so answers can cite current evidence. It reduces but does not eliminate fabrication. Local study-map skill 2.1 (Building Generative Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Routing can balance quality and cost. Fallback and evaluation are required. Why the correct answer wins: RAG retrieves current approved evidence and supports citations.
- **B:** Incorrect for this question. Translating the request does not replace retrieval, grounding, or validation, so it cannot satisfy an evidence or citation requirement. Why the correct answer wins: RAG retrieves current approved evidence and supports citations.
- **C:** Correct. RAG supplies selected source content at request time so answers can cite current evidence. It reduces but does not eliminate fabrication. In this case: RAG retrieves current approved evidence and supports citations.
- **D:** Incorrect for this question. Checkpoints validate intermediate results before later steps depend on them. This limits error propagation. Why the correct answer wins: RAG retrieves current approved evidence and supports citations.

### Question 15 — A

Answer: Return a defined JSON schema for downstream systems. Schema-constrained output supports validation and automation. Structured output supports validation and automation. Schema validity does not prove semantic correctness. Local study-map skill 2.1 (Building Generative Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Structured output supports validation and automation. Schema validity does not prove semantic correctness. In this case: Schema-constrained output supports validation and automation.
- **B:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Schema-constrained output supports validation and automation.
- **C:** Incorrect for this question. Templates improve consistency and reviewability. Version them and test changes. Why the correct answer wins: Schema-constrained output supports validation and automation.
- **D:** Incorrect for this question. Checkpoints validate intermediate results before later steps depend on them. This limits error propagation. Why the correct answer wins: Schema-constrained output supports validation and automation.

### Question 16 — D

Answer: Design multistep workflows with explicit checkpoints. Explicit stages with checkpoints keep unverified steps from completing. Checkpoints validate intermediate results before later steps depend on them. This limits error propagation. Local study-map skill 2.1 (Building Generative Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Autonomous workflows need bounded actions and escalation. Unbounded loops and broad tools increase risk. Why the correct answer wins: Explicit stages with checkpoints keep unverified steps from completing.
- **B:** Incorrect for this question. A single call cannot validate intermediate results or fetch authoritative evidence, so it is unsuitable for multi-stage or grounded workflows. Why the correct answer wins: Explicit stages with checkpoints keep unverified steps from completing.
- **C:** Incorrect for this question. Routing can balance quality and cost. Fallback and evaluation are required. Why the correct answer wins: Explicit stages with checkpoints keep unverified steps from completing.
- **D:** Correct. Checkpoints validate intermediate results before later steps depend on them. This limits error propagation. In this case: Explicit stages with checkpoints keep unverified steps from completing.

### Question 17 — C

Answer: Use a Foundry SDK or supported connector from application code. A supported Foundry SDK provides maintained client behaviour per language. SDKs provide supported request and response patterns. Pin versions and handle retries, timeouts, and errors explicitly. Local study-map skill 2.2 (Foundry SDK and Project Integration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Batch deployments can lower cost for large asynchronous jobs. They are unsuitable for interactive agent turns. Why the correct answer wins: A supported Foundry SDK provides maintained client behaviour per language.
- **B:** Incorrect for this question. Repeatable deployments reduce configuration drift. Include model deployments, indexes, and connections in review and promotion. Why the correct answer wins: A supported Foundry SDK provides maintained client behaviour per language.
- **C:** Correct. SDKs provide supported request and response patterns. Pin versions and handle retries, timeouts, and errors explicitly. In this case: A supported Foundry SDK provides maintained client behaviour per language.
- **D:** Incorrect for this question. Manual portal changes work for exploration but are slow, undocumented, and hard to reproduce, so they are a poor fit for governed release processes. Why the correct answer wins: A supported Foundry SDK provides maintained client behaviour per language.

### Question 18 — A

Answer: Connect the application to the Foundry project endpoint. The project endpoint binds the client to that project and its deployments. Project endpoints and SDK clients bind an app to approved models and resources. Use identity-based authentication and environment-specific configuration. Local study-map skill 2.2 (Foundry SDK and Project Integration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Project endpoints and SDK clients bind an app to approved models and resources. Use identity-based authentication and environment-specific configuration. In this case: The project endpoint binds the client to that project and its deployments.
- **B:** Incorrect for this question. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. Why the correct answer wins: The project endpoint binds the client to that project and its deployments.
- **C:** Incorrect for this question. The catalog shows supported models with capability, modality, region, and lifecycle details. Verify availability for your subscription and region before designing around one model. Why the correct answer wins: The project endpoint binds the client to that project and its deployments.
- **D:** Incorrect for this question. A managed secret store supports rotation and access control. Secrets should never appear in prompts, code, or logs. Why the correct answer wins: The project endpoint binds the client to that project and its deployments.

### Question 19 — A, E

Answers: Build a representative golden dataset from real tasks; Compare variants with controlled traffic and shared metrics. A golden dataset holds the benchmark, and an A/B test compares variants against it. A golden set anchors evaluation in expected behavior. Include edge cases and high-risk scenarios. Controlled comparison supports evidence-based change. Avoid changing several variables at once. Local study-map skill 2.3 (Evaluating Models and Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Controlled comparison supports evidence-based change. Avoid changing several variables at once. In this case: A golden dataset holds the benchmark, and an A/B test compares variants against it.
- **B:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: A golden dataset holds the benchmark, and an A/B test compares variants against it.
- **C:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: A golden dataset holds the benchmark, and an A/B test compares variants against it.
- **D:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: A golden dataset holds the benchmark, and an A/B test compares variants against it.
- **E:** Correct. A golden set anchors evaluation in expected behavior. Include edge cases and high-risk scenarios. In this case: A golden dataset holds the benchmark, and an A/B test compares variants against it.

### Question 20 — A

Answer: Detect fabricated or unsupported statements. Fabrication measures claims unsupported by evidence. Fabrication checks compare claims with evidence. Fluency and confidence are not evidence of accuracy. Local study-map skill 2.3 (Evaluating Models and Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Fabrication checks compare claims with evidence. Fluency and confidence are not evidence of accuracy. In this case: Fabrication measures claims unsupported by evidence.
- **B:** Incorrect for this question. Coherence checks readability and internal consistency. It does not establish factual accuracy. Why the correct answer wins: Fabrication measures claims unsupported by evidence.
- **C:** Incorrect for this question. Relevance covers both retrieval and response usefulness. A correct but off-topic answer still fails. Why the correct answer wins: Fabrication measures claims unsupported by evidence.
- **D:** Incorrect for this question. Tone analysis supports brand and customer communication. Context and culture affect interpretation. Why the correct answer wins: Fabrication measures claims unsupported by evidence.

### Question 21 — B

Answer: Put stable behavior rules in the system message. The system message carries persistent behavioural guidance. System messages define role and constraints. They are not a security boundary against injection. Local study-map skill 2.4 (Agent Roles, Goals, and Tool Schemas), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Guardrails are technical controls, not prompt suggestions. Validate inputs, authorize tools, and limit egress. Why the correct answer wins: The system message carries persistent behavioural guidance.
- **B:** Correct. System messages define role and constraints. They are not a security boundary against injection. In this case: The system message carries persistent behavioural guidance.
- **C:** Incorrect for this question. Roles should match the operations the app or agent performs. Broad contributor access increases blast radius. Why the correct answer wins: The system message carries persistent behavioural guidance.
- **D:** Incorrect for this question. Filters assign severity and can block or annotate content. Thresholds should reflect the use case and applicable policy. Why the correct answer wins: The system message carries persistent behavioural guidance.

### Question 22 — C

Answer: Model requests tool → app validates and authorizes → tool executes → result returns → model responds. The application validates and authorizes the call before any tool executes. Tool execution authority belongs to the application, which validates and authorizes before acting. Local study-map skill 2.5 (Agent Tools, Retrieval, Memory, and Function Calling), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. The model cannot execute the tool, and authorization after execution is too late. Why the correct answer wins: The application validates and authorizes the call before any tool executes.
- **B:** Incorrect for this question. The response cannot precede the tool action and validation. Why the correct answer wins: The application validates and authorizes the call before any tool executes.
- **C:** Correct. Tool execution authority belongs to the application, which validates and authorizes before acting. In this case: The application validates and authorizes the call before any tool executes.
- **D:** Incorrect for this question. Execution must follow validation, and the model is not the execution boundary. Why the correct answer wins: The application validates and authorizes the call before any tool executes.

### Question 23 — D

Answer: Expose a typed function as an agent tool. A function tool calls the business API under application authorization. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. Local study-map skill 2.5 (Agent Tools, Retrieval, Memory, and Function Calling), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. RAG supplies selected source content at request time so answers can cite current evidence. It reduces but does not eliminate fabrication. Why the correct answer wins: A function tool calls the business API under application authorization.
- **B:** Incorrect for this question. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Why the correct answer wins: A function tool calls the business API under application authorization.
- **C:** Incorrect for this question. OpenAPI tools describe supported HTTP operations for agent use. Narrow operations, validate inputs, and authenticate the caller. Why the correct answer wins: A function tool calls the business API under application authorization.
- **D:** Correct. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. In this case: A function tool calls the business API under application authorization.

### Question 24 — A

Answer: Use a manager agent to coordinate specialists. A manager agent routes to specialists and consolidates their replies. A manager routes tasks and merges results. Clear responsibility and failure handling are required. Local study-map skill 2.6 (Multi-Agent Orchestration and Safeguards), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. A manager routes tasks and merges results. Clear responsibility and failure handling are required. In this case: A manager agent routes to specialists and consolidates their replies.
- **B:** Incorrect for this question. Handoffs should carry goal, evidence, permissions, and open questions. Implicit context is easily lost. Why the correct answer wins: A manager agent routes to specialists and consolidates their replies.
- **C:** Incorrect for this question. Reflection can catch omissions and inconsistencies. It can also reinforce errors, so validate against evidence. Why the correct answer wins: A manager agent routes to specialists and consolidates their replies.
- **D:** Incorrect for this question. Parallel execution reduces wall-clock time for independent work. Reconciliation still requires design. Why the correct answer wins: A manager agent routes to specialists and consolidates their replies.

### Question 25 — B

Answer: Enable tracing across agent, model, and tool calls. Traces show the ordered model and tool calls so the failing step can be found. Traces localize failures and latency in multi-step workflows. Correlate them with evaluation results and deployment versions. Local study-map skill 2.7 (Agent Monitoring and Error Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Traces show the ordered model and tool calls so the failing step can be found.
- **B:** Correct. Traces localize failures and latency in multi-step workflows. Correlate them with evaluation results and deployment versions. In this case: Traces show the ordered model and tool calls so the failing step can be found.
- **C:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Traces show the ordered model and tool calls so the failing step can be found.
- **D:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Traces show the ordered model and tool calls so the failing step can be found.

### Question 26 — A

Answer: Lower temperature for more deterministic extraction. A lower temperature reduces sampling variability so identical prompts return stable labels. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Local study-map skill 2.8 (Generation Tuning and Observability), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Lower temperature reduces sampling variability. It does not guarantee factual correctness. In this case: A lower temperature reduces sampling variability so identical prompts return stable labels.
- **B:** Incorrect for this question. Routing can balance quality and cost. Fallback and evaluation are required. Why the correct answer wins: A lower temperature reduces sampling variability so identical prompts return stable labels.
- **C:** Incorrect for this question. Top-p narrows or broadens token sampling. Tune with evaluation rather than by intuition. Why the correct answer wins: A lower temperature reduces sampling variability so identical prompts return stable labels.
- **D:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: A lower temperature reduces sampling variability so identical prompts return stable labels.

### Question 27 — B

Answer: Alert on latency, error rate, safety, and cost thresholds. Alert rules notify the team when a monitored metric crosses a threshold. Alerts turn monitoring into action. Route them to an accountable owner with a runbook. Local study-map skill 2.7 (Agent Monitoring and Error Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Central telemetry captures latency, errors, dependencies, and custom events. Redact sensitive content before logging. Why the correct answer wins: Alert rules notify the team when a monitored metric crosses a threshold.
- **B:** Correct. Alerts turn monitoring into action. Route them to an accountable owner with a runbook. In this case: Alert rules notify the team when a monitored metric crosses a threshold.
- **C:** Incorrect for this question. User behavior, data, and models change. Rolling baselines reveal degradation that a one-time evaluation misses. Why the correct answer wins: Alert rules notify the team when a monitored metric crosses a threshold.
- **D:** Incorrect for this question. Audit evidence supports investigation and accountability. Protect log integrity and retention. Why the correct answer wins: Alert rules notify the team when a monitored metric crosses a threshold.

### Question 28 — C

Answer: Generate images from text and reference media. Image generation produces a new illustration from a description. Image generation supports creative and product workflows. Apply policy, watermarking, and provenance controls. Local study-map skill 3.1 (Image Generation and Editing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Video generation creates clips from prompts or images. Duration, consistency, and safety require review. Why the correct answer wins: Image generation produces a new illustration from a description.
- **B:** Incorrect for this question. Alt text should convey purpose and essential content, not decorative detail. Human review is still needed for critical pages. Why the correct answer wins: Image generation produces a new illustration from a description.
- **C:** Correct. Image generation supports creative and product workflows. Apply policy, watermarking, and provenance controls. In this case: Image generation produces a new illustration from a description.
- **D:** Incorrect for this question. Inpainting changes a selected area while preserving the rest. Validate identity, brand, and safety constraints. Why the correct answer wins: Image generation produces a new illustration from a description.

### Question 29 — C

Answer: Apply prompt-driven image modifications. Targeted image editing changes the selected element only. Prompt-based edits can alter style or content. Review outputs for unintended changes and policy violations. Local study-map skill 3.1 (Image Generation and Editing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Video editing can revise scenes or timing. Preserve provenance and review for harmful manipulation. Why the correct answer wins: Targeted image editing changes the selected element only.
- **B:** Incorrect for this question. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Why the correct answer wins: Targeted image editing changes the selected element only.
- **C:** Correct. Prompt-based edits can alter style or content. Review outputs for unintended changes and policy violations. In this case: Targeted image editing changes the selected element only.
- **D:** Incorrect for this question. Inpainting changes a selected area while preserving the rest. Validate identity, brand, and safety constraints. Why the correct answer wins: Targeted image editing changes the selected element only.

### Question 30 — C

Answer: Analyze video segments for events and content. Video analysis locates events and timestamps in existing footage. Video analysis can summarize or detect events across time. Sampling strategy affects coverage and cost. Local study-map skill 3.2 (Video Generation and Editing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Video editing can revise scenes or timing. Preserve provenance and review for harmful manipulation. Why the correct answer wins: Video analysis locates events and timestamps in existing footage.
- **B:** Incorrect for this question. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Why the correct answer wins: Video analysis locates events and timestamps in existing footage.
- **C:** Correct. Video analysis can summarize or detect events across time. Sampling strategy affects coverage and cost. In this case: Video analysis locates events and timestamps in existing footage.
- **D:** Incorrect for this question. Video generation creates clips from prompts or images. Duration, consistency, and safety require review. Why the correct answer wins: Video analysis locates events and timestamps in existing footage.

### Question 31 — B, E

Answers: Generate concise or detailed image captions; Generate alt text aligned to accessibility guidance. Captions help discovery, and alt text supports assistive technology. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Alt text should convey purpose and essential content, not decorative detail. Human review is still needed for critical pages. Local study-map skill 3.3 (Multimodal Understanding and Accessibility), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Captions help discovery, and alt text supports assistive technology.
- **B:** Correct. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. In this case: Captions help discovery, and alt text supports assistive technology.
- **C:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Captions help discovery, and alt text supports assistive technology.
- **D:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: Captions help discovery, and alt text supports assistive technology.
- **E:** Correct. Alt text should convey purpose and essential content, not decorative detail. Human review is still needed for critical pages. In this case: Captions help discovery, and alt text supports assistive technology.

### Question 32 — C

Answer: Use pro mode for complex multimodal content understanding. Pro mode handles complex multi-page multimodal documents. Pro mode handles more demanding layouts and multimodal inputs at higher cost. Use it where simpler modes fail requirements. Local study-map skill 3.4 (Visual Extraction and Video Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Custom models fit specialized forms not covered by prebuilts. They require representative labels and retraining discipline. Why the correct answer wins: Pro mode handles complex multi-page multimodal documents.
- **B:** Incorrect for this question. Single-task analyzers target one content type or objective. They may be simpler and cheaper than general pro-mode pipelines. Why the correct answer wins: Pro mode handles complex multi-page multimodal documents.
- **C:** Correct. Pro mode handles more demanding layouts and multimodal inputs at higher cost. Use it where simpler modes fail requirements. In this case: Pro mode handles complex multi-page multimodal documents.
- **D:** Incorrect for this question. Document Intelligence provides prebuilt and custom extraction for structured documents. Validate field accuracy on representative samples. Why the correct answer wins: Pro mode handles complex multi-page multimodal documents.

### Question 33 — A, B

Answers: Enforce brand and usage rules for generated visuals; Apply watermarks or provenance markers to generated media. Brand policy constrains approved visual usage, and watermarking identifies synthetic media. Brand controls define permitted logos, styles, and claims. Technical generation must still pass approval. Watermarks support disclosure and traceability. They do not replace usage policy or review. Local study-map skill 3.5 (Multimodal Responsible AI), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Correct. Brand controls define permitted logos, styles, and claims. Technical generation must still pass approval. In this case: Brand policy constrains approved visual usage, and watermarking identifies synthetic media.
- **B:** Correct. Watermarks support disclosure and traceability. They do not replace usage policy or review. In this case: Brand policy constrains approved visual usage, and watermarking identifies synthetic media.
- **C:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Brand policy constrains approved visual usage, and watermarking identifies synthetic media.
- **D:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Brand policy constrains approved visual usage, and watermarking identifies synthetic media.
- **E:** Incorrect for this question. Top-p narrows or broadens token sampling. Tune with evaluation rather than by intuition. Why the correct answer wins: Brand policy constrains approved visual usage, and watermarking identifies synthetic media.

### Question 34 — B

Answer: Treat text embedded in images as untrusted input. Text embedded in a document is an indirect prompt injection attempt. Visible instructions in images can attempt to manipulate an agent. Isolate, detect, and never let image text grant authority. Local study-map skill 3.5 (Multimodal Responsible AI), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Image and video safety filters reduce exposure to harmful content. Thresholds and human escalation should match policy. Why the correct answer wins: Text embedded in a document is an indirect prompt injection attempt.
- **B:** Correct. Visible instructions in images can attempt to manipulate an agent. Isolate, detect, and never let image text grant authority. In this case: Text embedded in a document is an indirect prompt injection attempt.
- **C:** Incorrect for this question. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Why the correct answer wins: Text embedded in a document is an indirect prompt injection attempt.
- **D:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Text embedded in a document is an indirect prompt injection attempt.

### Question 35 — D

Answer: Prompt for JSON that conforms to a supplied schema. Schema-constrained JSON supports validation and automation. Schema-guided generation improves machine readability. Validate values against source evidence and business rules. Local study-map skill 4.1 (Language Model Text Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Why the correct answer wins: Schema-constrained JSON supports validation and automation.
- **B:** Incorrect for this question. Translation should preserve meaning, names, and formatting. Evaluate domain terminology and low-resource languages. Why the correct answer wins: Schema-constrained JSON supports validation and automation.
- **C:** Incorrect for this question. Topic extraction supports discovery and grouping. It is not a substitute for an authoritative taxonomy. Why the correct answer wins: Schema-constrained JSON supports validation and automation.
- **D:** Correct. Schema-guided generation improves machine readability. Validate values against source evidence and business rules. In this case: Schema-constrained JSON supports validation and automation.

### Question 36 — B, E

Answers: Detect and redact sensitive personal data; Analyze sentiment and tone with an appropriate service. PII detection finds personal data, and sentiment detects frustration. Sensitive Data Protection or language PII detection can identify and mask data. Verify that redaction covers every path where content flows. Sentiment analysis can support triage and monitoring. Domain and language variation require validation. Local study-map skill 4.1 (Language Model Text Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Why the correct answer wins: PII detection finds personal data, and sentiment detects frustration.
- **B:** Correct. Sentiment analysis can support triage and monitoring. Domain and language variation require validation. In this case: PII detection finds personal data, and sentiment detects frustration.
- **C:** Incorrect for this question. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Why the correct answer wins: PII detection finds personal data, and sentiment detects frustration.
- **D:** Incorrect for this question. Topic extraction supports discovery and grouping. It is not a substitute for an authoritative taxonomy. Why the correct answer wins: PII detection finds personal data, and sentiment detects frustration.
- **E:** Correct. Sensitive Data Protection or language PII detection can identify and mask data. Verify that redaction covers every path where content flows. In this case: PII detection finds personal data, and sentiment detects frustration.

### Question 37 — A

Answer: Apply a custom glossary or terminology list. A glossary enforces approved term mappings across languages. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Local study-map skill 4.2 (Translation), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Correct. Glossaries keep product and legal terms consistent. Terms still need human validation in context. In this case: A glossary enforces approved term mappings across languages.
- **B:** Incorrect for this question. Entity extraction turns text into structured facts. Ambiguous mentions need resolution and validation. Why the correct answer wins: A glossary enforces approved term mappings across languages.
- **C:** Incorrect for this question. Sensitive Data Protection or language PII detection can identify and mask data. Verify that redaction covers every path where content flows. Why the correct answer wins: A glossary enforces approved term mappings across languages.
- **D:** Incorrect for this question. Translation should preserve meaning, names, and formatting. Evaluate domain terminology and low-resource languages. Why the correct answer wins: A glossary enforces approved term mappings across languages.

### Question 38 — B, D

Answers: Use Azure Translator or a language model for translation; Customize summaries and extraction for compliance needs. Translation localizes content, and compliance framing preserves required wording. Translation should preserve meaning, names, and formatting. Evaluate domain terminology and low-resource languages. Compliance work requires precise citation, retention, and review. Generic summarization is insufficient without controls. Local study-map skill 4.2 (Translation), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Entity extraction turns text into structured facts. Ambiguous mentions need resolution and validation. Why the correct answer wins: Translation localizes content, and compliance framing preserves required wording.
- **B:** Correct. Translation should preserve meaning, names, and formatting. Evaluate domain terminology and low-resource languages. In this case: Translation localizes content, and compliance framing preserves required wording.
- **C:** Incorrect for this question. Topic extraction supports discovery and grouping. It is not a substitute for an authoritative taxonomy. Why the correct answer wins: Translation localizes content, and compliance framing preserves required wording.
- **D:** Correct. Compliance work requires precise citation, retention, and review. Generic summarization is insufficient without controls. In this case: Translation localizes content, and compliance framing preserves required wording.
- **E:** Incorrect for this question. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Why the correct answer wins: Translation localizes content, and compliance framing preserves required wording.

### Question 39 — D

Answer: Capture audio → transcribe → translate text → synthesize speech → return audio. Speech translation transcribes, translates, then synthesizes the target-language reply. Speech translation transcribes first, translates the text, then synthesizes the target-language audio. Local study-map skill 4.3 (Speech Solutions), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Capture must come first, and synthesis must follow translation. Why the correct answer wins: Speech translation transcribes, translates, then synthesizes the target-language reply.
- **B:** Incorrect for this question. Audio must be captured before it can be transcribed or translated. Why the correct answer wins: Speech translation transcribes, translates, then synthesizes the target-language reply.
- **C:** Incorrect for this question. Synthesis cannot precede transcription and translation. Why the correct answer wins: Speech translation transcribes, translates, then synthesizes the target-language reply.
- **D:** Correct. Speech translation transcribes first, translates the text, then synthesizes the target-language audio. In this case: Speech translation transcribes, translates, then synthesizes the target-language reply.

### Question 40 — C

Answer: Transcribe speech to text with Azure AI Speech. Speech-to-text transcribes audio into searchable text. Speech-to-text enables voice agents and transcript analysis. Audio quality, accents, and domain terms affect accuracy. Local study-map skill 4.3 (Speech Solutions), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Speech translation combines recognition and translation. Preserve timing and speaker context where needed. Why the correct answer wins: Speech-to-text transcribes audio into searchable text.
- **B:** Incorrect for this question. Text-to-speech supports voice responses and accessibility. Voice, prosody, and latency affect usability. Why the correct answer wins: Speech-to-text transcribes audio into searchable text.
- **C:** Correct. Speech-to-text enables voice agents and transcript analysis. Audio quality, accents, and domain terms affect accuracy. In this case: Speech-to-text transcribes audio into searchable text.
- **D:** Incorrect for this question. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Why the correct answer wins: Speech-to-text transcribes audio into searchable text.

### Question 41 — A

Answer: Adapt prompts and models to domain terminology. A validated domain lexicon teaches local terminology to the extraction step. Domain adaptation improves consistency and recall. Validate against expert-created expected outputs. Local study-map skill 4.4 (Domain Customization), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Correct. Domain adaptation improves consistency and recall. Validate against expert-created expected outputs. In this case: A validated domain lexicon teaches local terminology to the extraction step.
- **B:** Incorrect for this question. Sensitive Data Protection or language PII detection can identify and mask data. Verify that redaction covers every path where content flows. Why the correct answer wins: A validated domain lexicon teaches local terminology to the extraction step.
- **C:** Incorrect for this question. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Why the correct answer wins: A validated domain lexicon teaches local terminology to the extraction step.
- **D:** Incorrect for this question. Translation should preserve meaning, names, and formatting. Evaluate domain terminology and low-resource languages. Why the correct answer wins: A validated domain lexicon teaches local terminology to the extraction step.

### Question 42 — B

Answer: Use an Azure AI Search indexer to pull source content. An indexer pulls source documents and tracks changes. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. Local study-map skill 5.1 (Content Ingestion and Indexing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. Skillsets can OCR, split, embed, and extract during indexing. Each skill adds latency, cost, and failure modes. Why the correct answer wins: An indexer pulls source documents and tracks changes.
- **B:** Correct. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. In this case: An indexer pulls source documents and tracks changes.
- **C:** Incorrect for this question. Push ingestion supports near-real-time updates from applications. The app owns batching, retries, and deletion. Why the correct answer wins: An indexer pulls source documents and tracks changes.
- **D:** Incorrect for this question. OCR unlocks text in scans and screenshots. Layout and table structure may still require specialized extraction. Why the correct answer wins: An indexer pulls source documents and tracks changes.

### Question 43 — C

Answer: Apply document-level security filters at query time. Document-level security filters restrict results before content reaches the model. Filters restrict results to content the user may see. They must be enforced before content reaches the model. Local study-map skill 5.2 (Search and Grounding Configuration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. Stale content produces outdated answers. Define refresh expectations and test deletion behavior. Why the correct answer wins: Document-level security filters restrict results before content reaches the model.
- **B:** Incorrect for this question. Hybrid search covers exact identifiers and paraphrased meaning together. Fusion and ranking need testing on representative queries. Why the correct answer wins: Document-level security filters restrict results before content reaches the model.
- **C:** Correct. Filters restrict results to content the user may see. They must be enforced before content reaches the model. In this case: Document-level security filters restrict results before content reaches the model.
- **D:** Incorrect for this question. A semantic ranker can improve relevance for natural-language queries. It adds cost and latency and should be measured against a baseline. Why the correct answer wins: Document-level security filters restrict results before content reaches the model.

### Question 44 — B

Answer: Ingest → extract text → chunk → embed → index → retrieve with citations. Extraction, chunking, embedding, and indexing precede retrieval and citation. The supported RAG ingestion order produces searchable, citable evidence. Retrieval cannot work before content is extracted, chunked, embedded, and indexed. Local study-map skill 5.4 (RAG Ingestion and OCR), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. Retrieval before chunking, embedding, and indexing has nothing searchable to return. Why the correct answer wins: Extraction, chunking, embedding, and indexing precede retrieval and citation.
- **B:** Correct. The supported RAG ingestion order produces searchable, citable evidence. Retrieval cannot work before content is extracted, chunked, embedded, and indexed. In this case: Extraction, chunking, embedding, and indexing precede retrieval and citation.
- **C:** Incorrect for this question. Retrieval is attempted before the index exists and source ingestion is incomplete. Why the correct answer wins: Extraction, chunking, embedding, and indexing precede retrieval and citation.
- **D:** Incorrect for this question. Indexing before extraction or embedding creates an empty or unusable index. Why the correct answer wins: Extraction, chunking, embedding, and indexing precede retrieval and citation.

### Question 45 — D

Answer: Pin the model version available in the required region. Pinning a version available in each jurisdiction satisfies residency and stability. A pinned version keeps behavior stable and satisfies residency, at the cost of slower access to newer capabilities. Local study-map skill 1.1 (Selecting Foundry Models and Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Large models handle ambiguity and multi-step reasoning better in many cases, at higher cost and latency. Select with measured evidence rather than brand preference. Why the correct answer wins: Pinning a version available in each jurisdiction satisfies residency and stability.
- **B:** Incorrect for this question. A custom model is justified when supported prebuilt options cannot meet a defined requirement. It adds data, evaluation, and lifecycle obligations. Why the correct answer wins: Pinning a version available in each jurisdiction satisfies residency and stability.
- **C:** Incorrect for this question. The catalog shows supported models with capability, modality, region, and lifecycle details. Verify availability for your subscription and region before designing around one model. Why the correct answer wins: Pinning a version available in each jurisdiction satisfies residency and stability.
- **D:** Correct. A pinned version keeps behavior stable and satisfies residency, at the cost of slower access to newer capabilities. In this case: Pinning a version available in each jurisdiction satisfies residency and stability.

### Question 46 — D

Answer: Use Foundry Tools for prebuilt vision, speech, language, and extraction needs. Prebuilt managed capabilities need no training corpus. Prebuilt managed capabilities can reduce custom model work where their behavior and limits fit the task. They are not a substitute for task-specific validation. Local study-map skill 1.1 (Selecting Foundry Models and Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Small models can reduce latency and cost for constrained classification or extraction. Confirm quality on representative data before standardizing. Why the correct answer wins: Prebuilt managed capabilities need no training corpus.
- **B:** Incorrect for this question. Large models handle ambiguity and multi-step reasoning better in many cases, at higher cost and latency. Select with measured evidence rather than brand preference. Why the correct answer wins: Prebuilt managed capabilities need no training corpus.
- **C:** Incorrect for this question. A custom model is justified when supported prebuilt options cannot meet a defined requirement. It adds data, evaluation, and lifecycle obligations. Why the correct answer wins: Prebuilt managed capabilities need no training corpus.
- **D:** Correct. Prebuilt managed capabilities can reduce custom model work where their behavior and limits fit the task. They are not a substitute for task-specific validation. In this case: Prebuilt managed capabilities need no training corpus.

### Question 47 — C

Answer: Expose an OpenAPI operation as an agent tool. An OpenAPI tool reuses the published contract. OpenAPI tools describe supported HTTP operations for agent use. Narrow operations, validate inputs, and authenticate the caller. Local study-map skill 1.2 (Retrieval, Memory, Tool, and Knowledge Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. An index gives an agent curated, searchable evidence under configured access. Index content and permissions require ongoing ownership. Why the correct answer wins: An OpenAPI tool reuses the published contract.
- **B:** Incorrect for this question. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. Why the correct answer wins: An OpenAPI tool reuses the published contract.
- **C:** Correct. OpenAPI tools describe supported HTTP operations for agent use. Narrow operations, validate inputs, and authenticate the caller. In this case: An OpenAPI tool reuses the published contract.
- **D:** Incorrect for this question. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Why the correct answer wins: An OpenAPI tool reuses the published contract.

### Question 48 — B

Answer: Block promotion in the pipeline when evaluation thresholds fail. An evaluation gate blocks promotion on a measured threshold. An automated gate turns an evaluation result into a release decision. Thresholds need ownership or the gate becomes noise. Local study-map skill 1.3 (Infrastructure, Deployment, and CI/CD), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. A canary limits blast radius and produces real signal before full rollout. It needs a rollback criterion defined in advance. Why the correct answer wins: An evaluation gate blocks promotion on a measured threshold.
- **B:** Correct. An automated gate turns an evaluation result into a release decision. Thresholds need ownership or the gate becomes noise. In this case: An evaluation gate blocks promotion on a measured threshold.
- **C:** Incorrect for this question. Repeatable deployments reduce configuration drift. Include model deployments, indexes, and connections in review and promotion. Why the correct answer wins: An evaluation gate blocks promotion on a measured threshold.
- **D:** Incorrect for this question. Canary or phased rollout limits exposure. Rollback must be tested, not just documented. Why the correct answer wins: An evaluation gate blocks promotion on a measured threshold.

### Question 49 — B

Answer: Send mirrored production traffic to a candidate without returning its answers. Shadow deployment mirrors traffic and discards candidate output. Shadow traffic compares a candidate against live behavior with no user impact. It requires careful handling of side-effecting calls. Local study-map skill 1.3 (Infrastructure, Deployment, and CI/CD), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. A canary limits blast radius and produces real signal before full rollout. It needs a rollback criterion defined in advance. Why the correct answer wins: Shadow deployment mirrors traffic and discards candidate output.
- **B:** Correct. Shadow traffic compares a candidate against live behavior with no user impact. It requires careful handling of side-effecting calls. In this case: Shadow deployment mirrors traffic and discards candidate output.
- **C:** Incorrect for this question. Batch deployments can lower cost for large asynchronous jobs. They are unsuitable for interactive agent turns. Why the correct answer wins: Shadow deployment mirrors traffic and discards candidate output.
- **D:** Incorrect for this question. Standard deployments bill per token and scale within quota. They suit spiky or early workloads. Why the correct answer wins: Shadow deployment mirrors traffic and discards candidate output.

### Question 50 — D

Answer: Alert on spend thresholds per deployment or project. A spend alert notifies owners as usage crosses a threshold. Spend alerts catch runaway usage before the invoice does. They are detection, not a hard spending cap. Local study-map skill 1.4 (Quotas, Scaling, and Cost), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Token analytics supports cost and performance tuning. Attribute usage to features and tenants where possible. Why the correct answer wins: A spend alert notifies owners as usage crosses a threshold.
- **B:** Incorrect for this question. Retries, tool calls, evaluation, and review contribute to unit economics. Per-outcome cost supports better optimization. Why the correct answer wins: A spend alert notifies owners as usage crosses a threshold.
- **C:** Incorrect for this question. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. Why the correct answer wins: A spend alert notifies owners as usage crosses a threshold.
- **D:** Correct. Spend alerts catch runaway usage before the invoice does. They are detection, not a hard spending cap. In this case: A spend alert notifies owners as usage crosses a threshold.

### Question 51 — A

Answer: Monitor index freshness, failures, and document counts. Index health checks catch stale content. Stale or partially indexed content produces confident but wrong answers. Alert on ingestion and deletion failures. Local study-map skill 1.5 (Monitoring Performance, Drift, Safety, and Grounding), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. Stale or partially indexed content produces confident but wrong answers. Alert on ingestion and deletion failures. In this case: Index health checks catch stale content.
- **B:** Incorrect for this question. User behavior, data, and models change. Rolling baselines reveal degradation that a one-time evaluation misses. Why the correct answer wins: Index health checks catch stale content.
- **C:** Incorrect for this question. Groundedness checks whether claims are supported by retrieved evidence. Sampling and human review complement automated scores. Why the correct answer wins: Index health checks catch stale content.
- **D:** Incorrect for this question. Central telemetry captures latency, errors, dependencies, and custom events. Redact sensitive content before logging. Why the correct answer wins: Index health checks catch stale content.

### Question 52 — B

Answer: Restrict outbound network access to approved destinations. Egress rules restrict which external destinations the workload can reach, which is exactly the control the policy demands. Egress controls reduce exfiltration and unauthorized tool reach. Combine with identity and data controls. Local study-map skill 1.6 (Security, Identity, and Networking), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Leaving the public path open defeats the purpose of a private networking design because traffic can still bypass the private route. Why the correct answer wins: Egress rules restrict which external destinations the workload can reach, which is exactly the control the policy demands.
- **B:** Correct. Egress controls reduce exfiltration and unauthorized tool reach. Combine with identity and data controls. In this case: Egress rules restrict which external destinations the workload can reach, which is exactly the control the policy demands.
- **C:** Incorrect for this question. Roles should match the operations the app or agent performs. Broad contributor access increases blast radius. Why the correct answer wins: Egress rules restrict which external destinations the workload can reach, which is exactly the control the policy demands.
- **D:** Incorrect for this question. Private connectivity keeps service traffic on approved network paths. Pair it with private DNS so clients resolve the private address. Why the correct answer wins: Egress rules restrict which external destinations the workload can reach, which is exactly the control the policy demands.

### Question 53 — A

Answer: Set agent oversight mode and tool-access constraints. Human oversight keeps consequential decisions accountable. Oversight settings bound what an agent may do autonomously. They should be tested against realistic misuse and failure. Local study-map skill 1.7 (Responsible AI Controls and Oversight), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. Oversight settings bound what an agent may do autonomously. They should be tested against realistic misuse and failure. In this case: Human oversight keeps consequential decisions accountable.
- **B:** Incorrect for this question. Guardrails are technical controls, not prompt suggestions. Validate inputs, authorize tools, and limit egress. Why the correct answer wins: Human oversight keeps consequential decisions accountable.
- **C:** Incorrect for this question. Approval must occur before the effect and identify who approved what. A model confidence score is not approval. Why the correct answer wins: Human oversight keeps consequential decisions accountable.
- **D:** Incorrect for this question. Audit evidence supports investigation and accountability. Protect log integrity and retention. Why the correct answer wins: Human oversight keeps consequential decisions accountable.

### Question 54 — A

Answer: Use batch processing for latency-tolerant bulk work. Batch deployment suits large asynchronous jobs. Batch deployments can lower cost for large asynchronous jobs. They are unsuitable for interactive agent turns. Local study-map skill 1.4 (Quotas, Scaling, and Cost), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. Batch deployments can lower cost for large asynchronous jobs. They are unsuitable for interactive agent turns. In this case: Batch deployment suits large asynchronous jobs.
- **B:** Incorrect for this question. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. Why the correct answer wins: Batch deployment suits large asynchronous jobs.
- **C:** Incorrect for this question. Standard deployments bill per token and scale within quota. They suit spiky or early workloads. Why the correct answer wins: Batch deployment suits large asynchronous jobs.
- **D:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: Batch deployment suits large asynchronous jobs.

### Question 55 — B, C

Answers: Compare supported models in the Foundry model catalog; Pin the model version available in the required region. Catalog review confirms availability, and pinning prevents silent change. The catalog shows supported models with capability, modality, region, and lifecycle details. Verify availability for your subscription and region before designing around one model. A pinned version keeps behavior stable and satisfies residency, at the cost of slower access to newer capabilities. Local study-map skill 1.1 (Selecting Foundry Models and Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Batch deployments can lower cost for large asynchronous jobs. They are unsuitable for interactive agent turns. Why the correct answer wins: Catalog review confirms availability, and pinning prevents silent change.
- **B:** Correct. A pinned version keeps behavior stable and satisfies residency, at the cost of slower access to newer capabilities. In this case: Catalog review confirms availability, and pinning prevents silent change.
- **C:** Correct. The catalog shows supported models with capability, modality, region, and lifecycle details. Verify availability for your subscription and region before designing around one model. In this case: Catalog review confirms availability, and pinning prevents silent change.
- **D:** Incorrect for this question. A custom model is justified when supported prebuilt options cannot meet a defined requirement. It adds data, evaluation, and lifecycle obligations. Why the correct answer wins: Catalog review confirms availability, and pinning prevents silent change.
- **E:** Incorrect for this question. Standard deployments bill per token and scale within quota. They suit spiky or early workloads. Why the correct answer wins: Catalog review confirms availability, and pinning prevents silent change.

### Question 56 — C, D

Answers: Monitor groundedness and citation quality in production; Alert on latency, error rate, safety, and cost thresholds. Groundedness monitoring detects unsupported answers, and alerting notifies teams. Groundedness checks whether claims are supported by retrieved evidence. Sampling and human review complement automated scores. Alerts turn monitoring into action. Route them to an accountable owner with a runbook. Local study-map skill 1.5 (Monitoring Performance, Drift, Safety, and Grounding), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Groundedness monitoring detects unsupported answers, and alerting notifies teams.
- **B:** Incorrect for this question. Users experience the whole path, not only generation. Optimize the dominant contributor. Why the correct answer wins: Groundedness monitoring detects unsupported answers, and alerting notifies teams.
- **C:** Correct. Alerts turn monitoring into action. Route them to an accountable owner with a runbook. In this case: Groundedness monitoring detects unsupported answers, and alerting notifies teams.
- **D:** Correct. Groundedness checks whether claims are supported by retrieved evidence. Sampling and human review complement automated scores. In this case: Groundedness monitoring detects unsupported answers, and alerting notifies teams.
- **E:** Incorrect for this question. Retries, tool calls, evaluation, and review contribute to unit economics. Per-outcome cost supports better optimization. Why the correct answer wins: Groundedness monitoring detects unsupported answers, and alerting notifies teams.

### Question 57 — A, D

Answers: Restrict outbound network access to approved destinations; Use least-privilege Azure RBAC roles for the workload identity. Egress restrictions bound destinations, and least privilege bounds actions. Egress controls reduce exfiltration and unauthorized tool reach. Combine with identity and data controls. Roles should match the operations the app or agent performs. Broad contributor access increases blast radius. Local study-map skill 1.6 (Security, Identity, and Networking), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. Egress controls reduce exfiltration and unauthorized tool reach. Combine with identity and data controls. In this case: Egress restrictions bound destinations, and least privilege bounds actions.
- **B:** Incorrect for this question. Filters assign severity and can block or annotate content. Thresholds should reflect the use case and applicable policy. Why the correct answer wins: Egress restrictions bound destinations, and least privilege bounds actions.
- **C:** Incorrect for this question. A managed secret store supports rotation and access control. Secrets should never appear in prompts, code, or logs. Why the correct answer wins: Egress restrictions bound destinations, and least privilege bounds actions.
- **D:** Correct. Roles should match the operations the app or agent performs. Broad contributor access increases blast radius. In this case: Egress restrictions bound destinations, and least privilege bounds actions.
- **E:** Incorrect for this question. Private connectivity keeps service traffic on approved network paths. Pair it with private DNS so clients resolve the private address. Why the correct answer wins: Egress restrictions bound destinations, and least privilege bounds actions.

### Question 58 — D

Answer: Commit change → run the evaluation suite → block on failed thresholds → deploy a canary → promote after metrics hold. Evaluation runs before deployment, its thresholds gate promotion, and a canary limits exposure before full release. An evaluation gate before deployment, followed by a canary, keeps unmeasured changes away from all users. Local study-map skill 1.3 (Infrastructure, Deployment, and CI/CD), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Evaluation after promotion cannot prevent a failed change from reaching everyone. Why the correct answer wins: Evaluation runs before deployment, its thresholds gate promotion, and a canary limits exposure before full release.
- **B:** Incorrect for this question. The change must exist before it can be evaluated or deployed. Why the correct answer wins: Evaluation runs before deployment, its thresholds gate promotion, and a canary limits exposure before full release.
- **C:** Incorrect for this question. Deployment cannot precede the change, and evaluation must gate promotion rather than follow it. Why the correct answer wins: Evaluation runs before deployment, its thresholds gate promotion, and a canary limits exposure before full release.
- **D:** Correct. An evaluation gate before deployment, followed by a canary, keeps unmeasured changes away from all users. In this case: Evaluation runs before deployment, its thresholds gate promotion, and a canary limits exposure before full release.

### Question 59 — B

Answer: Set chunk overlap so facts spanning a boundary stay retrievable. Overlap preserves facts across chunk boundaries. Overlap preserves context across chunk edges at the cost of duplicated index storage and more near-duplicate hits. Local study-map skill 2.1 (Building Generative Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Embeddings determine semantic similarity behavior. Evaluate retrieval quality before and after changes. Why the correct answer wins: Overlap preserves facts across chunk boundaries.
- **B:** Correct. Overlap preserves context across chunk edges at the cost of duplicated index storage and more near-duplicate hits. In this case: Overlap preserves facts across chunk boundaries.
- **C:** Incorrect for this question. More retrieved text is not always better. Order and compress evidence to preserve decisive facts. Why the correct answer wins: Overlap preserves facts across chunk boundaries.
- **D:** Incorrect for this question. Chunking affects recall, precision, and context use. Respect document structure and test against real questions. Why the correct answer wins: Overlap preserves facts across chunk boundaries.

### Question 60 — A

Answer: Ground responses with retrieval-augmented generation. Retrieval supplies current evidence with citations. RAG supplies selected source content at request time so answers can cite current evidence. It reduces but does not eliminate fabrication. Local study-map skill 2.1 (Building Generative Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. RAG supplies selected source content at request time so answers can cite current evidence. It reduces but does not eliminate fabrication. In this case: Retrieval supplies current evidence with citations.
- **B:** Incorrect for this question. Routing can balance quality and cost. Fallback and evaluation are required. Why the correct answer wins: Retrieval supplies current evidence with citations.
- **C:** Incorrect for this question. Examples clarify format and boundaries. They do not guarantee correctness on unseen inputs. Why the correct answer wins: Retrieval supplies current evidence with citations.
- **D:** Incorrect for this question. Checkpoints validate intermediate results before later steps depend on them. This limits error propagation. Why the correct answer wins: Retrieval supplies current evidence with citations.

### Question 61 — D

Answer: Use short-lived scoped access tokens for tool calls. A scoped access token avoids long-lived secrets. Short-lived credentials reduce misuse risk. Never place tokens in prompts or logs. Local study-map skill 2.2 (Foundry SDK and Project Integration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. SDKs provide supported request and response patterns. Pin versions and handle retries, timeouts, and errors explicitly. Why the correct answer wins: A scoped access token avoids long-lived secrets.
- **B:** Incorrect for this question. A managed secret store supports rotation and access control. Secrets should never appear in prompts, code, or logs. Why the correct answer wins: A scoped access token avoids long-lived secrets.
- **C:** Incorrect for this question. Managed identities avoid embedded secrets and support role-based access. Assign only required data-plane roles. Why the correct answer wins: A scoped access token avoids long-lived secrets.
- **D:** Correct. Short-lived credentials reduce misuse risk. Never place tokens in prompts or logs. In this case: A scoped access token avoids long-lived secrets.

### Question 62 — A

Answer: Build a representative golden dataset from real tasks. A golden dataset fixes the inputs. A golden set anchors evaluation in expected behavior. Include edge cases and high-risk scenarios. Local study-map skill 2.3 (Evaluating Models and Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. A golden set anchors evaluation in expected behavior. Include edge cases and high-risk scenarios. In this case: A golden dataset fixes the inputs.
- **B:** Incorrect for this question. Prompts, models, indexes, and tools all affect behavior. Regression tests catch unintended effects. Why the correct answer wins: A golden dataset fixes the inputs.
- **C:** Incorrect for this question. Evaluators provide repeatable signals across models and prompts. They must be calibrated against human judgment for high-impact work. Why the correct answer wins: A golden dataset fixes the inputs.
- **D:** Incorrect for this question. Controlled comparison supports evidence-based change. Avoid changing several variables at once. Why the correct answer wins: A golden dataset fixes the inputs.

### Question 63 — D

Answer: Re-run evaluation suites after meaningful changes. Regression evaluation re-runs previously failing cases against the candidate, so a fixed defect cannot silently return. Prompts, models, indexes, and tools all affect behavior. Regression tests catch unintended effects. Local study-map skill 2.3 (Evaluating Models and Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Safety evaluation complements content filters. Use representative adversarial inputs. Why the correct answer wins: Regression evaluation re-runs previously failing cases against the candidate, so a fixed defect cannot silently return.
- **B:** Incorrect for this question. Evaluators provide repeatable signals across models and prompts. They must be calibrated against human judgment for high-impact work. Why the correct answer wins: Regression evaluation re-runs previously failing cases against the candidate, so a fixed defect cannot silently return.
- **C:** Incorrect for this question. A golden set anchors evaluation in expected behavior. Include edge cases and high-risk scenarios. Why the correct answer wins: Regression evaluation re-runs previously failing cases against the candidate, so a fixed defect cannot silently return.
- **D:** Correct. Prompts, models, indexes, and tools all affect behavior. Regression tests catch unintended effects. In this case: Regression evaluation re-runs previously failing cases against the candidate, so a fixed defect cannot silently return.

### Question 64 — C

Answer: Define narrow tool schemas with clear descriptions. A typed schema constrains the arguments. Precise schemas help the model choose tools and arguments correctly. Broad or ambiguous tools invite unsafe calls. Local study-map skill 2.4 (Agent Roles, Goals, and Tool Schemas), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. System messages define role and constraints. They are not a security boundary against injection. Why the correct answer wins: A typed schema constrains the arguments.
- **B:** Incorrect for this question. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Why the correct answer wins: A typed schema constrains the arguments.
- **C:** Correct. Precise schemas help the model choose tools and arguments correctly. Broad or ambiguous tools invite unsafe calls. In this case: A typed schema constrains the arguments.
- **D:** Incorrect for this question. Routing can balance quality and cost. Fallback and evaluation are required. Why the correct answer wins: A typed schema constrains the arguments.

### Question 65 — B

Answer: Transfer control between agents with explicit context. Handoff transfers control and conversation context to the specialist agent without losing the thread. Handoffs should carry goal, evidence, permissions, and open questions. Implicit context is easily lost. Local study-map skill 2.6 (Multi-Agent Orchestration and Safeguards), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Parallel execution reduces wall-clock time for independent work. Reconciliation still requires design. Why the correct answer wins: Handoff transfers control and conversation context to the specialist agent without losing the thread.
- **B:** Correct. Handoffs should carry goal, evidence, permissions, and open questions. Implicit context is easily lost. In this case: Handoff transfers control and conversation context to the specialist agent without losing the thread.
- **C:** Incorrect for this question. A manager routes tasks and merges results. Clear responsibility and failure handling are required. Why the correct answer wins: Handoff transfers control and conversation context to the specialist agent without losing the thread.
- **D:** Incorrect for this question. Reflection can catch omissions and inconsistencies. It can also reinforce errors, so validate against evidence. Why the correct answer wins: Handoff transfers control and conversation context to the specialist agent without losing the thread.

### Question 66 — C

Answer: Run independent agents concurrently. Parallel execution runs the independent checks at the same time, which is what makes the latency target achievable. Parallel execution reduces wall-clock time for independent work. Reconciliation still requires design. Local study-map skill 2.6 (Multi-Agent Orchestration and Safeguards), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Reflection can catch omissions and inconsistencies. It can also reinforce errors, so validate against evidence. Why the correct answer wins: Parallel execution runs the independent checks at the same time, which is what makes the latency target achievable.
- **B:** Incorrect for this question. Sequential orchestration makes dependencies explicit. It may add latency where steps could run concurrently. Why the correct answer wins: Parallel execution runs the independent checks at the same time, which is what makes the latency target achievable.
- **C:** Correct. Parallel execution reduces wall-clock time for independent work. Reconciliation still requires design. In this case: Parallel execution runs the independent checks at the same time, which is what makes the latency target achievable.
- **D:** Incorrect for this question. A manager routes tasks and merges results. Clear responsibility and failure handling are required. Why the correct answer wins: Parallel execution runs the independent checks at the same time, which is what makes the latency target achievable.

### Question 67 — D

Answer: Set a stop sequence so generation ends at the intended boundary. A stop sequence ends generation at the boundary. A stop sequence truncates output at a defined marker, which keeps parsers from receiving trailing commentary. It must not appear inside legitimate content. Local study-map skill 2.8 (Generation Tuning and Observability), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: A stop sequence ends generation at the boundary.
- **B:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: A stop sequence ends generation at the boundary.
- **C:** Incorrect for this question. Top-p narrows or broadens token sampling. Tune with evaluation rather than by intuition. Why the correct answer wins: A stop sequence ends generation at the boundary.
- **D:** Correct. A stop sequence truncates output at a defined marker, which keeps parsers from receiving trailing commentary. It must not appear inside legitimate content. In this case: A stop sequence ends generation at the boundary.

### Question 68 — A

Answer: Adjust top-p to control response diversity. Nucleus sampling widens the candidate set. Top-p narrows or broadens token sampling. Tune with evaluation rather than by intuition. Local study-map skill 2.8 (Generation Tuning and Observability), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Top-p narrows or broadens token sampling. Tune with evaluation rather than by intuition. In this case: Nucleus sampling widens the candidate set.
- **B:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Nucleus sampling widens the candidate set.
- **C:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Nucleus sampling widens the candidate set.
- **D:** Incorrect for this question. A seed makes repeated sampling closer to reproducible, but it remains best effort and does not replace deterministic extraction settings. Why the correct answer wins: Nucleus sampling widens the candidate set.

### Question 69 — A, C

Answers: Use a Foundry SDK or supported connector from application code; Authenticate with a managed identity instead of keys. A supported SDK handles retries, and a managed identity removes stored secrets. SDKs provide supported request and response patterns. Pin versions and handle retries, timeouts, and errors explicitly. Managed identities avoid embedded secrets and support role-based access. Assign only required data-plane roles. Local study-map skill 2.2 (Foundry SDK and Project Integration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. SDKs provide supported request and response patterns. Pin versions and handle retries, timeouts, and errors explicitly. In this case: A supported SDK handles retries, and a managed identity removes stored secrets.
- **B:** Incorrect for this question. Manual portal changes work for exploration but are slow, undocumented, and hard to reproduce, so they are a poor fit for governed release processes. Why the correct answer wins: A supported SDK handles retries, and a managed identity removes stored secrets.
- **C:** Correct. Managed identities avoid embedded secrets and support role-based access. Assign only required data-plane roles. In this case: A supported SDK handles retries, and a managed identity removes stored secrets.
- **D:** Incorrect for this question. Short-lived credentials reduce misuse risk. Never place tokens in prompts or logs. Why the correct answer wins: A supported SDK handles retries, and a managed identity removes stored secrets.
- **E:** Incorrect for this question. A managed secret store supports rotation and access control. Secrets should never appear in prompts, code, or logs. Why the correct answer wins: A supported SDK handles retries, and a managed identity removes stored secrets.

### Question 70 — A, D

Answers: Use evaluators for quality, safety, and groundedness; Evaluate harmful, biased, or policy-violating output. Quality evaluation scores correctness, and safety evaluation screens unsafe output. Evaluators provide repeatable signals across models and prompts. They must be calibrated against human judgment for high-impact work. Safety evaluation complements content filters. Use representative adversarial inputs. Local study-map skill 2.3 (Evaluating Models and Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Evaluators provide repeatable signals across models and prompts. They must be calibrated against human judgment for high-impact work. In this case: Quality evaluation scores correctness, and safety evaluation screens unsafe output.
- **B:** Incorrect for this question. Prompts, models, indexes, and tools all affect behavior. Regression tests catch unintended effects. Why the correct answer wins: Quality evaluation scores correctness, and safety evaluation screens unsafe output.
- **C:** Incorrect for this question. A golden set anchors evaluation in expected behavior. Include edge cases and high-risk scenarios. Why the correct answer wins: Quality evaluation scores correctness, and safety evaluation screens unsafe output.
- **D:** Correct. Safety evaluation complements content filters. Use representative adversarial inputs. In this case: Quality evaluation scores correctness, and safety evaluation screens unsafe output.
- **E:** Incorrect for this question. Controlled comparison supports evidence-based change. Avoid changing several variables at once. Why the correct answer wins: Quality evaluation scores correctness, and safety evaluation screens unsafe output.

### Question 71 — B, C

Answers: Give the agent a file-search tool over approved document stores; Enable a sandboxed code interpreter tool for calculations. File search supplies approved evidence, and an interpreter performs arithmetic. A file tool retrieves from curated stores under configured access. It still depends on indexing quality and permission filters. Code execution handles quantitative work the model cannot do reliably in text. The sandbox must be isolated and output must be validated. Local study-map skill 2.5 (Agent Tools, Retrieval, Memory, and Function Calling), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. OpenAPI tools describe supported HTTP operations for agent use. Narrow operations, validate inputs, and authenticate the caller. Why the correct answer wins: File search supplies approved evidence, and an interpreter performs arithmetic.
- **B:** Correct. Code execution handles quantitative work the model cannot do reliably in text. The sandbox must be isolated and output must be validated. In this case: File search supplies approved evidence, and an interpreter performs arithmetic.
- **C:** Correct. A file tool retrieves from curated stores under configured access. It still depends on indexing quality and permission filters. In this case: File search supplies approved evidence, and an interpreter performs arithmetic.
- **D:** Incorrect for this question. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Why the correct answer wins: File search supplies approved evidence, and an interpreter performs arithmetic.
- **E:** Incorrect for this question. Routing can balance quality and cost. Fallback and evaluation are required. Why the correct answer wins: File search supplies approved evidence, and an interpreter performs arithmetic.

### Question 72 — B

Answer: Define role and goal → configure tools → attach knowledge → evaluate in sandbox → deploy with monitoring. Role, tools, evaluation, then deployment with monitoring. An agent is defined before it is connected to tools and knowledge, and evaluation precedes deployment. Local study-map skill 2.6 (Multi-Agent Orchestration and Safeguards), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Tools configured before the role exists, and evaluation after deployment gates nothing. Why the correct answer wins: Role, tools, evaluation, then deployment with monitoring.
- **B:** Correct. An agent is defined before it is connected to tools and knowledge, and evaluation precedes deployment. In this case: Role, tools, evaluation, then deployment with monitoring.
- **C:** Incorrect for this question. The agent must be defined first, and evaluation must precede deployment. Why the correct answer wins: Role, tools, evaluation, then deployment with monitoring.
- **D:** Incorrect for this question. Deployment before the agent is defined, connected, or evaluated removes every control. Why the correct answer wins: Role, tools, evaluation, then deployment with monitoring.

### Question 73 — B

Answer: Queue flagged generations for human moderation before release. Human moderation before release catches contextual problems. Human moderation catches context that automated filters miss, at the cost of latency and reviewer load. Local study-map skill 3.1 (Image Generation and Editing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Brand controls define permitted logos, styles, and claims. Technical generation must still pass approval. Why the correct answer wins: Human moderation before release catches contextual problems.
- **B:** Correct. Human moderation catches context that automated filters miss, at the cost of latency and reviewer load. In this case: Human moderation before release catches contextual problems.
- **C:** Incorrect for this question. Image and video safety filters reduce exposure to harmful content. Thresholds and human escalation should match policy. Why the correct answer wins: Human moderation before release catches contextual problems.
- **D:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Human moderation before release catches contextual problems.

### Question 74 — A

Answer: Generate a set of descriptive tags for each image. Generated tags make the library filterable and searchable, which is what the editors asked for. Tags support filtering and search across large image libraries. Tag vocabulary should be governed so synonyms do not fragment results. Local study-map skill 3.3 (Multimodal Understanding and Accessibility), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Correct. Tags support filtering and search across large image libraries. Tag vocabulary should be governed so synonyms do not fragment results. In this case: Generated tags make the library filterable and searchable, which is what the editors asked for.
- **B:** Incorrect for this question. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Why the correct answer wins: Generated tags make the library filterable and searchable, which is what the editors asked for.
- **C:** Incorrect for this question. Visual question answering should cite the relevant region or content. Avoid answering beyond what the image supports. Why the correct answer wins: Generated tags make the library filterable and searchable, which is what the editors asked for.
- **D:** Incorrect for this question. Alt text should convey purpose and essential content, not decorative detail. Human review is still needed for critical pages. Why the correct answer wins: Generated tags make the library filterable and searchable, which is what the editors asked for.

### Question 75 — A

Answer: Preserve reading order across columns and sections. Reading-order analysis restores the intended sequence. Reading order affects comprehension and extraction. Incorrect order can invert meaning in contracts and forms. Local study-map skill 3.4 (Visual Extraction and Video Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Correct. Reading order affects comprehension and extraction. Incorrect order can invert meaning in contracts and forms. In this case: Reading-order analysis restores the intended sequence.
- **B:** Incorrect for this question. Markdown preserves headings, tables, and lists in a model-friendly form. Validate that critical values survive conversion. Why the correct answer wins: Reading-order analysis restores the intended sequence.
- **C:** Incorrect for this question. OCR unlocks text in scans and screenshots. Layout and table structure may still require specialized extraction. Why the correct answer wins: Reading-order analysis restores the intended sequence.
- **D:** Incorrect for this question. Layout awareness improves extraction from forms and multi-column documents. Flattening to plain text can destroy meaning. Why the correct answer wins: Reading-order analysis restores the intended sequence.

### Question 76 — A

Answer: Use Azure Content Understanding analyzers in Foundry Tools. Content Understanding analyzers are configured per content type. Content Understanding extracts structure and fields from documents, images, audio, and video. Analyzer design and validation determine quality. Local study-map skill 3.4 (Visual Extraction and Video Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Correct. Content Understanding extracts structure and fields from documents, images, audio, and video. Analyzer design and validation determine quality. In this case: Content Understanding analyzers are configured per content type.
- **B:** Incorrect for this question. Document Intelligence provides prebuilt and custom extraction for structured documents. Validate field accuracy on representative samples. Why the correct answer wins: Content Understanding analyzers are configured per content type.
- **C:** Incorrect for this question. Analyzers define what to extract and how to return it. Version and test them like application code. Why the correct answer wins: Content Understanding analyzers are configured per content type.
- **D:** Incorrect for this question. Prebuilt models cover invoices, receipts, IDs, and similar formats. Check supported locales and field coverage. Why the correct answer wins: Content Understanding analyzers are configured per content type.

### Question 77 — B, E

Answers: Use pro mode for complex multimodal content understanding; Return markdown for retrieval and reasoning pipelines. Pro mode handles complex packets, and markdown suits downstream reasoning. Pro mode handles more demanding layouts and multimodal inputs at higher cost. Use it where simpler modes fail requirements. Markdown preserves structure and is easy for models to consume. Validate tables and key values. Local study-map skill 3.4 (Visual Extraction and Video Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Detection returns locations and labels for visual elements. Validate classes and thresholds against the use case. Why the correct answer wins: Pro mode handles complex packets, and markdown suits downstream reasoning.
- **B:** Correct. Markdown preserves structure and is easy for models to consume. Validate tables and key values. In this case: Pro mode handles complex packets, and markdown suits downstream reasoning.
- **C:** Incorrect for this question. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Why the correct answer wins: Pro mode handles complex packets, and markdown suits downstream reasoning.
- **D:** Incorrect for this question. Single-task analyzers target one content type or objective. They may be simpler and cheaper than general pro-mode pipelines. Why the correct answer wins: Pro mode handles complex packets, and markdown suits downstream reasoning.
- **E:** Correct. Pro mode handles more demanding layouts and multimodal inputs at higher cost. Use it where simpler modes fail requirements. In this case: Pro mode handles complex packets, and markdown suits downstream reasoning.

### Question 78 — A

Answer: Upload image → validate format and size → send multimodal request → parse structured fields → route low-confidence values to review. Input validation precedes the model call, output is parsed into fields, and low-confidence values go to human review. Validation and structured parsing bracket the multimodal call, and low-confidence output goes to people. Local study-map skill 3.5 (Multimodal Responsible AI), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Correct. Validation and structured parsing bracket the multimodal call, and low-confidence output goes to people. In this case: Input validation precedes the model call, output is parsed into fields, and low-confidence values go to human review.
- **B:** Incorrect for this question. Review cannot precede the request, and parsing must follow the response. Why the correct answer wins: Input validation precedes the model call, output is parsed into fields, and low-confidence values go to human review.
- **C:** Incorrect for this question. A request cannot precede the upload, and validation must come before the call. Why the correct answer wins: Input validation precedes the model call, output is parsed into fields, and low-confidence values go to human review.
- **D:** Incorrect for this question. Parsing requires a response, which requires an uploaded and validated image. Why the correct answer wins: Input validation precedes the model call, output is parsed into fields, and low-confidence values go to human review.

### Question 79 — C

Answer: Select and return the most relevant source sentences. Extractive summaries return source sentences verbatim, so every statement remains quotable and auditable. Extractive summaries stay verbatim and therefore auditable, at the cost of readability and length. Local study-map skill 4.1 (Language Model Text Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Why the correct answer wins: Extractive summaries return source sentences verbatim, so every statement remains quotable and auditable.
- **B:** Incorrect for this question. Abstractive summaries read naturally and compress long text, but they can introduce statements that the source does not support. Why the correct answer wins: Extractive summaries return source sentences verbatim, so every statement remains quotable and auditable.
- **C:** Correct. Extractive summaries stay verbatim and therefore auditable, at the cost of readability and length. In this case: Extractive summaries return source sentences verbatim, so every statement remains quotable and auditable.
- **D:** Incorrect for this question. Compliance work requires precise citation, retention, and review. Generic summarization is insufficient without controls. Why the correct answer wins: Extractive summaries return source sentences verbatim, so every statement remains quotable and auditable.

### Question 80 — D

Answer: Convert names between writing systems without translating meaning. Transliteration preserves pronunciation across writing systems. Transliteration preserves pronunciation for names and addresses. It is not a substitute for translating meaning-bearing text. Local study-map skill 4.2 (Translation), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Why the correct answer wins: Transliteration preserves pronunciation across writing systems.
- **B:** Incorrect for this question. Domain adaptation improves consistency and recall. Validate against expert-created expected outputs. Why the correct answer wins: Transliteration preserves pronunciation across writing systems.
- **C:** Incorrect for this question. Translation should preserve meaning, names, and formatting. Evaluate domain terminology and low-resource languages. Why the correct answer wins: Transliteration preserves pronunciation across writing systems.
- **D:** Correct. Transliteration preserves pronunciation for names and addresses. It is not a substitute for translating meaning-bearing text. In this case: Transliteration preserves pronunciation across writing systems.

### Question 81 — C

Answer: Select a specific synthesis voice for consistent spoken output. A specific synthesis voice keeps the channel consistent. A named voice keeps a phone or kiosk channel recognizable across prompts. Voice availability and language coverage vary by region. Local study-map skill 4.3 (Speech Solutions), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Custom speech can improve recognition of domain terms. It requires representative audio and ongoing evaluation. Why the correct answer wins: A specific synthesis voice keeps the channel consistent.
- **B:** Incorrect for this question. Text-to-speech supports voice responses and accessibility. Voice, prosody, and latency affect usability. Why the correct answer wins: A specific synthesis voice keeps the channel consistent.
- **C:** Correct. A named voice keeps a phone or kiosk channel recognizable across prompts. Voice availability and language coverage vary by region. In this case: A specific synthesis voice keeps the channel consistent.
- **D:** Incorrect for this question. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Why the correct answer wins: A specific synthesis voice keeps the channel consistent.

### Question 82 — C

Answer: Extract key phrases to summarize what a document covers. Key-phrase extraction surfaces the salient topics in each document, which supports navigation and triage. Key phrases support navigation, tagging, and clustering. They are not a substitute for a required structured field. Local study-map skill 4.1 (Language Model Text Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Entity extraction turns text into structured facts. Ambiguous mentions need resolution and validation. Why the correct answer wins: Key-phrase extraction surfaces the salient topics in each document, which supports navigation and triage.
- **B:** Incorrect for this question. Topic extraction supports discovery and grouping. It is not a substitute for an authoritative taxonomy. Why the correct answer wins: Key-phrase extraction surfaces the salient topics in each document, which supports navigation and triage.
- **C:** Correct. Key phrases support navigation, tagging, and clustering. They are not a substitute for a required structured field. In this case: Key-phrase extraction surfaces the salient topics in each document, which supports navigation and triage.
- **D:** Incorrect for this question. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Why the correct answer wins: Key-phrase extraction surfaces the salient topics in each document, which supports navigation and triage.

### Question 83 — A, B

Answers: Detect and redact sensitive personal data; Analyze sentiment and tone with an appropriate service. PII detection finds personal data, and sentiment detects frustration. Sensitive Data Protection or language PII detection can identify and mask data. Verify that redaction covers every path where content flows. Sentiment analysis can support triage and monitoring. Domain and language variation require validation. Local study-map skill 4.1 (Language Model Text Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Correct. Sensitive Data Protection or language PII detection can identify and mask data. Verify that redaction covers every path where content flows. In this case: PII detection finds personal data, and sentiment detects frustration.
- **B:** Correct. Sentiment analysis can support triage and monitoring. Domain and language variation require validation. In this case: PII detection finds personal data, and sentiment detects frustration.
- **C:** Incorrect for this question. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Why the correct answer wins: PII detection finds personal data, and sentiment detects frustration.
- **D:** Incorrect for this question. Topic extraction supports discovery and grouping. It is not a substitute for an authoritative taxonomy. Why the correct answer wins: PII detection finds personal data, and sentiment detects frustration.
- **E:** Incorrect for this question. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Why the correct answer wins: PII detection finds personal data, and sentiment detects frustration.

### Question 84 — D

Answer: Tune scoring and boosting against a labelled query set. Scoring changes must be measured on a labelled query set. Boosting and scoring changes should be measured on real queries. Untested tuning usually trades one query class for another. Local study-map skill 5.2 (Search and Grounding Configuration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. Embeddings support similarity search over meaning rather than exact terms. Vector search still needs chunking, filtering, and evaluation. Why the correct answer wins: Scoring changes must be measured on a labelled query set.
- **B:** Incorrect for this question. Hybrid search covers exact identifiers and paraphrased meaning together. Fusion and ranking need testing on representative queries. Why the correct answer wins: Scoring changes must be measured on a labelled query set.
- **C:** Incorrect for this question. A semantic ranker can improve relevance for natural-language queries. It adds cost and latency and should be measured against a baseline. Why the correct answer wins: Scoring changes must be measured on a labelled query set.
- **D:** Correct. Boosting and scoring changes should be measured on real queries. Untested tuning usually trades one query class for another. In this case: Scoring changes must be measured on a labelled query set.

### Question 85 — B

Answer: Add enrichment skills for text, image, and layout. Enrichment adds derived content during indexing. A skillset can extract entities, captions, and structure during indexing. Enrichment adds cost and failure points that need monitoring. Local study-map skill 5.3 (Enrichment Skills), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. Markdown preserves structure and is easy for models to consume. Validate tables and key values. Why the correct answer wins: Enrichment adds derived content during indexing.
- **B:** Correct. A skillset can extract entities, captions, and structure during indexing. Enrichment adds cost and failure points that need monitoring. In this case: Enrichment adds derived content during indexing.
- **C:** Incorrect for this question. Skillsets can OCR, split, embed, and extract during indexing. Each skill adds latency, cost, and failure modes. Why the correct answer wins: Enrichment adds derived content during indexing.
- **D:** Incorrect for this question. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. Why the correct answer wins: Enrichment adds derived content during indexing.

### Question 86 — A

Answer: Define index fields, attributes, and searchable versus filterable behavior. Field attributes control filtering and sorting. Field attributes decide what can be filtered, sorted, faceted, or retrieved, so schema choices constrain query design later. Local study-map skill 5.6 (Document and Content Extraction), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Correct. Field attributes decide what can be filtered, sorted, faceted, or retrieved, so schema choices constrain query design later. In this case: Field attributes control filtering and sorting.
- **B:** Incorrect for this question. Document Intelligence provides prebuilt and custom extraction for structured documents. Validate field accuracy on representative samples. Why the correct answer wins: Field attributes control filtering and sorting.
- **C:** Incorrect for this question. Typed fields feed downstream systems directly. Add validation and confidence thresholds before automated action. Why the correct answer wins: Field attributes control filtering and sorting.
- **D:** Incorrect for this question. Analyzers define what to extract and how to return it. Version and test them like application code. Why the correct answer wins: Field attributes control filtering and sorting.

### Question 87 — A

Answer: Combine OCR with layout analysis for complex documents. OCR with layout analysis preserves relationships. OCR supplies text while layout analysis preserves relationships. Together they support tables and multi-column forms. Local study-map skill 5.4 (RAG Ingestion and OCR), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Correct. OCR supplies text while layout analysis preserves relationships. Together they support tables and multi-column forms. In this case: OCR with layout analysis preserves relationships.
- **B:** Incorrect for this question. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. Why the correct answer wins: OCR with layout analysis preserves relationships.
- **C:** Incorrect for this question. Chunking affects recall, precision, and context use. Respect document structure and test against real questions. Why the correct answer wins: OCR with layout analysis preserves relationships.
- **D:** Incorrect for this question. Markdown preserves headings, tables, and lists in a model-friendly form. Validate that critical values survive conversion. Why the correct answer wins: OCR with layout analysis preserves relationships.

### Question 88 — B

Answer: Connect the data source → define the index schema → attach the enrichment skillset → run the indexer → validate relevance on sample queries. The source is connected, the schema defined, enrichment attached, the indexer run, and relevance validated on sample queries. Schema and enrichment must exist before indexing runs, and relevance is checked after the index is populated. Local study-map skill 5.2 (Search and Grounding Configuration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. An indexer cannot run before the source and schema exist. Why the correct answer wins: The source is connected, the schema defined, enrichment attached, the indexer run, and relevance validated on sample queries.
- **B:** Correct. Schema and enrichment must exist before indexing runs, and relevance is checked after the index is populated. In this case: The source is connected, the schema defined, enrichment attached, the indexer run, and relevance validated on sample queries.
- **C:** Incorrect for this question. Relevance cannot be validated on an index that was never populated. Why the correct answer wins: The source is connected, the schema defined, enrichment attached, the indexer run, and relevance validated on sample queries.
- **D:** Incorrect for this question. The schema must exist before enrichment and relevance testing. Why the correct answer wins: The source is connected, the schema defined, enrichment attached, the indexer run, and relevance validated on sample queries.

### Question 89 — D

Answer: Enable a sandboxed code interpreter tool for calculations. A sandboxed interpreter computes from the supplied data, which is far more reliable than arithmetic performed in generated text. Code execution handles quantitative work the model cannot do reliably in text. The sandbox must be isolated and output must be validated. Local study-map skill 2.5 (Agent Tools, Retrieval, Memory, and Function Calling), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. OpenAPI tools describe supported HTTP operations for agent use. Narrow operations, validate inputs, and authenticate the caller. Why the correct answer wins: A sandboxed interpreter computes from the supplied data, which is far more reliable than arithmetic performed in generated text.
- **B:** Incorrect for this question. A file tool retrieves from curated stores under configured access. It still depends on indexing quality and permission filters. Why the correct answer wins: A sandboxed interpreter computes from the supplied data, which is far more reliable than arithmetic performed in generated text.
- **C:** Incorrect for this question. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Why the correct answer wins: A sandboxed interpreter computes from the supplied data, which is far more reliable than arithmetic performed in generated text.
- **D:** Correct. Code execution handles quantitative work the model cannot do reliably in text. The sandbox must be isolated and output must be validated. In this case: A sandboxed interpreter computes from the supplied data, which is far more reliable than arithmetic performed in generated text.

### Question 90 — D

Answer: Enable tracing across agent, model, and tool calls. Traces show the ordered model and tool calls. Traces localize failures and latency in multi-step workflows. Correlate them with evaluation results and deployment versions. Local study-map skill 2.7 (Agent Monitoring and Error Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Traces show the ordered model and tool calls.
- **B:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Traces show the ordered model and tool calls.
- **C:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Traces show the ordered model and tool calls.
- **D:** Correct. Traces localize failures and latency in multi-step workflows. Correlate them with evaluation results and deployment versions. In this case: Traces show the ordered model and tool calls.

### Question 91 — A

Answer: Push documents to an index through the data-plane API. Push ingestion indexes documents as they are written. Push ingestion supports near-real-time updates from applications. The app owns batching, retries, and deletion. Local study-map skill 5.1 (Content Ingestion and Indexing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Correct. Push ingestion supports near-real-time updates from applications. The app owns batching, retries, and deletion. In this case: Push ingestion indexes documents as they are written.
- **B:** Incorrect for this question. Skillsets can OCR, split, embed, and extract during indexing. Each skill adds latency, cost, and failure modes. Why the correct answer wins: Push ingestion indexes documents as they are written.
- **C:** Incorrect for this question. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. Why the correct answer wins: Push ingestion indexes documents as they are written.
- **D:** Incorrect for this question. OCR unlocks text in scans and screenshots. Layout and table structure may still require specialized extraction. Why the correct answer wins: Push ingestion indexes documents as they are written.

### Question 92 — C

Answer: Use provisioned throughput for predictable high-volume workloads. Provisioned throughput reserves capacity for predictable continuous demand. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Local study-map skill 1.4 (Quotas, Scaling, and Cost), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Batch deployments can lower cost for large asynchronous jobs. They are unsuitable for interactive agent turns. Why the correct answer wins: Provisioned throughput reserves capacity for predictable continuous demand.
- **B:** Incorrect for this question. Standard deployments bill per token and scale within quota. They suit spiky or early workloads. Why the correct answer wins: Provisioned throughput reserves capacity for predictable continuous demand.
- **C:** Correct. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. In this case: Provisioned throughput reserves capacity for predictable continuous demand.
- **D:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Provisioned throughput reserves capacity for predictable continuous demand.

### Question 93 — B

Answer: Require citations tied to retrieved evidence. Citations tie each answer to the evidence that supports it. Citations let users verify claims and support auditing. Preserve source and chunk identifiers through the pipeline. Local study-map skill 2.3 (Evaluating Models and Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Citations tie each answer to the evidence that supports it.
- **B:** Correct. Citations let users verify claims and support auditing. Preserve source and chunk identifiers through the pipeline. In this case: Citations tie each answer to the evidence that supports it.
- **C:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Citations tie each answer to the evidence that supports it.
- **D:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Citations tie each answer to the evidence that supports it.

### Question 94 — B

Answer: Select evidence within the model's usable context. The context budget limits how much retrieved evidence enters the prompt. More retrieved text is not always better. Order and compress evidence to preserve decisive facts. Local study-map skill 5.5 (Retrieval Integration with Agents), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. Reranking improves precision after broad recall. It adds latency and must be evaluated. Why the correct answer wins: The context budget limits how much retrieved evidence enters the prompt.
- **B:** Correct. More retrieved text is not always better. Order and compress evidence to preserve decisive facts. In this case: The context budget limits how much retrieved evidence enters the prompt.
- **C:** Incorrect for this question. Embeddings support similarity search over meaning rather than exact terms. Vector search still needs chunking, filtering, and evaluation. Why the correct answer wins: The context budget limits how much retrieved evidence enters the prompt.
- **D:** Incorrect for this question. De-duplication frees context space that duplicates would otherwise consume, so the most informative evidence survives the budget. Why the correct answer wins: The context budget limits how much retrieved evidence enters the prompt.

### Question 95 — C

Answer: Persist conversation history in a thread or session. Conversation state keeps earlier context across turns. Threads support continuity across turns. Apply retention and access controls to stored history. Local study-map skill 2.2 (Foundry SDK and Project Integration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Embeddings determine semantic similarity behavior. Evaluate retrieval quality before and after changes. Why the correct answer wins: Conversation state keeps earlier context across turns.
- **B:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: Conversation state keeps earlier context across turns.
- **C:** Correct. Threads support continuity across turns. Apply retention and access controls to stored history. In this case: Conversation state keeps earlier context across turns.
- **D:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Conversation state keeps earlier context across turns.

### Question 96 — A

Answer: Use a custom speech model for specialized vocabulary. A custom speech model adapts vocabulary to the domain. Custom speech can improve recognition of domain terms. It requires representative audio and ongoing evaluation. Local study-map skill 4.3 (Speech Solutions), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Correct. Custom speech can improve recognition of domain terms. It requires representative audio and ongoing evaluation. In this case: A custom speech model adapts vocabulary to the domain.
- **B:** Incorrect for this question. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Why the correct answer wins: A custom speech model adapts vocabulary to the domain.
- **C:** Incorrect for this question. Text-to-speech supports voice responses and accessibility. Voice, prosody, and latency affect usability. Why the correct answer wins: A custom speech model adapts vocabulary to the domain.
- **D:** Incorrect for this question. Speech-to-text enables voice agents and transcript analysis. Audio quality, accents, and domain terms affect accuracy. Why the correct answer wins: A custom speech model adapts vocabulary to the domain.

### Question 97 — D

Answer: Use field-level confidence to route exceptions. Field-level confidence sends uncertain values to review. Low-confidence fields should be reviewed rather than accepted. Thresholds depend on downstream impact. Local study-map skill 5.6 (Document and Content Extraction), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. Sentiment analysis can support triage and monitoring. Domain and language variation require validation. Why the correct answer wins: Field-level confidence sends uncertain values to review.
- **B:** Incorrect for this question. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Why the correct answer wins: Field-level confidence sends uncertain values to review.
- **C:** Incorrect for this question. Relevance covers both retrieval and response usefulness. A correct but off-topic answer still fails. Why the correct answer wins: Field-level confidence sends uncertain values to review.
- **D:** Correct. Low-confidence fields should be reviewed rather than accepted. Thresholds depend on downstream impact. In this case: Field-level confidence sends uncertain values to review.

### Question 98 — C, E

Answers: Persist conversation history in a thread or session; Expose a typed function as an agent tool. Conversation state preserves the case number, and a function tool performs the lookup. Threads support continuity across turns. Apply retention and access controls to stored history. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. Local study-map skill 2.5 (Agent Tools, Retrieval, Memory, and Function Calling), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Embeddings determine semantic similarity behavior. Evaluate retrieval quality before and after changes. Why the correct answer wins: Conversation state preserves the case number, and a function tool performs the lookup.
- **B:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Conversation state preserves the case number, and a function tool performs the lookup.
- **C:** Correct. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. In this case: Conversation state preserves the case number, and a function tool performs the lookup.
- **D:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: Conversation state preserves the case number, and a function tool performs the lookup.
- **E:** Correct. Threads support continuity across turns. Apply retention and access controls to stored history. In this case: Conversation state preserves the case number, and a function tool performs the lookup.

### Question 99 — B

Answer: Train a custom extraction model on labeled documents. A custom extraction model targets a proprietary layout. Custom models fit specialized forms not covered by prebuilts. They require representative labels and retraining discipline. Local study-map skill 5.6 (Document and Content Extraction), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. Document Intelligence provides prebuilt and custom extraction for structured documents. Validate field accuracy on representative samples. Why the correct answer wins: A custom extraction model targets a proprietary layout.
- **B:** Correct. Custom models fit specialized forms not covered by prebuilts. They require representative labels and retraining discipline. In this case: A custom extraction model targets a proprietary layout.
- **C:** Incorrect for this question. Analyzers define what to extract and how to return it. Version and test them like application code. Why the correct answer wins: A custom extraction model targets a proprietary layout.
- **D:** Incorrect for this question. Prebuilt models cover invoices, receipts, IDs, and similar formats. Check supported locales and field coverage. Why the correct answer wins: A custom extraction model targets a proprietary layout.

### Question 100 — C

Answer: Add an enrichment skillset to an indexing pipeline. A skillset defines the enrichment steps applied during indexing. Skillsets can OCR, split, embed, and extract during indexing. Each skill adds latency, cost, and failure modes. Local study-map skill 5.3 (Enrichment Skills), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. OCR unlocks text in scans and screenshots. Layout and table structure may still require specialized extraction. Why the correct answer wins: A skillset defines the enrichment steps applied during indexing.
- **B:** Incorrect for this question. Push ingestion supports near-real-time updates from applications. The app owns batching, retries, and deletion. Why the correct answer wins: A skillset defines the enrichment steps applied during indexing.
- **C:** Correct. Skillsets can OCR, split, embed, and extract during indexing. Each skill adds latency, cost, and failure modes. In this case: A skillset defines the enrichment steps applied during indexing.
- **D:** Incorrect for this question. A skillset can extract entities, captions, and structure during indexing. Enrichment adds cost and failure points that need monitoring. Why the correct answer wins: A skillset defines the enrichment steps applied during indexing.
