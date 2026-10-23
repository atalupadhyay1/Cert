# Microsoft AI-103 — Full-Length Mock Exam 3

Azure AI Apps and Agents Developer Associate · 100 questions · 120 minutes · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 84 multiple-choice (selection count stated where needed), 16 multi-select, and 4 case studies of 3 questions. 8 of the multiple-choice items ask you to choose the correct candidate sequence. Hot-area, drag-and-drop UI, labs, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. A bank must pin a model version that stays available in its primary and secondary regions. What should the team review before selection?

Domain: Plan and manage an Azure AI solution

- A. Compare supported models in the Foundry model catalog
- B. Use a general-purpose large language model for complex reasoning
- C. Use a small language model for a narrow, high-volume task
- D. Train or deploy a task-specific model outside the prebuilt catalog

### 2. A risk team needs a model tuned only on its own historical filings, with the weights kept inside the organization's control. Which option applies?

Domain: Plan and manage an Azure AI solution

- A. Use a multimodal model for combined text, image, or audio input
- B. Use a small language model for a narrow, high-volume task
- C. Train or deploy a task-specific model outside the prebuilt catalog
- D. Use a general-purpose large language model for complex reasoning

### 3. An assistant must return the regulatory circulars most similar in meaning to a complaint narrative. Which service performs that match?

Domain: Plan and manage an Azure AI solution

- A. Use a vector index for semantic retrieval
- B. Connect an Azure AI Search index as agent knowledge
- C. Use managed conversation state or memory for continuity
- D. Expose a typed function as an agent tool

### 4. A trading-support workload needs repeatable deployments and no public data-plane exposure. Which two actions should you take? Select two.

Domain: Plan and manage an Azure AI solution

- A. Use supported prompt or response caching where appropriate
- B. Plan for model quota expressed in tokens and requests per minute
- C. Use provisioned throughput for predictable high-volume workloads
- D. Use private endpoints and disable public network access
- E. Manage AI resources with infrastructure as code and CI/CD

### 5. A team must score two million historic claims overnight at minimum cost with no interactive latency requirement. Which deployment option fits?

Domain: Plan and manage an Azure AI solution

- A. Use provisioned throughput for predictable high-volume workloads
- B. Plan for model quota expressed in tokens and requests per minute
- C. Use a standard pay-as-you-go model deployment for variable demand
- D. Use batch processing for latency-tolerant bulk work

### 6. A payments assistant has steady, round-the-clock volume and cannot tolerate throttling. Which capacity option should be evaluated?

Domain: Plan and manage an Azure AI solution

- A. Use batch processing for latency-tolerant bulk work
- B. Use provisioned throughput for predictable high-volume workloads
- C. Use supported prompt or response caching where appropriate
- D. Use a standard pay-as-you-go model deployment for variable demand

### 7. Finance needs spend broken down by deployment, prompt size, and completion size. What should be enabled?

Domain: Plan and manage an Azure AI solution

- A. Plan for model quota expressed in tokens and requests per minute
- B. Track cost per accepted task, not only per token
- C. Monitor input and quality drift over time
- D. Track prompt, completion, and cached token usage

### 8. An on-call team must be paged when model latency breaches its service objective. What should be configured?

Domain: Plan and manage an Azure AI solution

- A. Monitor input and quality drift over time
- B. Use Azure Monitor and Application Insights for telemetry
- C. Alert on latency, error rate, safety, and cost thresholds
- D. Preserve audit logs of changes, approvals, and tool actions

### 9. A new model version must not silently break cases that previously failed. What should be run before promotion?

Domain: Plan and manage an Azure AI solution

- A. Compare variants with controlled traffic and shared metrics
- B. Use evaluators for quality, safety, and groundedness
- C. Build a representative golden dataset from real tasks
- D. Re-run evaluation suites after meaningful changes

### 10. A third-party connector secret must be rotated on a schedule and never stored in code. What should hold it?

Domain: Plan and manage an Azure AI solution

- A. Use least-privilege Azure RBAC roles for the workload identity
- B. Use private endpoints and disable public network access
- C. Authenticate with a managed identity instead of keys
- D. Store secrets in Azure Key Vault when keys are unavoidable

### 11. Security requires that the AI service cannot call unapproved external endpoints. What should be restricted?

Domain: Plan and manage an Azure AI solution

- A. Private networking with public access left enabled
- B. Private DNS resolution configured for the endpoint
- C. Restrict outbound network access to approved destinations
- D. Use private endpoints and disable public network access

### 12. Before launch, a team must actively probe the agent for jailbreaks and data-exfiltration prompts. What activity is this?

Domain: Plan and manage an Azure AI solution

- A. Test the solution with adversarial and boundary cases
- B. Enforce constraints in code and platform policy
- C. Set agent oversight mode and tool-access constraints
- D. Preserve audit logs of changes, approvals, and tool actions

### 13. A credit-decision assistant must block harmful content and keep a human accountable for outcomes. Which two controls are required? Select two.

Domain: Plan and manage an Azure AI solution

- A. Adjust top-p to control response diversity
- B. Use supported prompt or response caching where appropriate
- C. Set agent oversight mode and tool-access constraints
- D. Configure content safety filters for harmful categories
- E. Lower temperature for more deterministic extraction

### 14. Simple balance lookups must go to a cheap model while complex disputes use a stronger model. Which pattern fits?

Domain: Implement generative AI and agentic solutions

- A. Ground responses with retrieval-augmented generation
- B. Include representative examples in the prompt
- C. Route requests to different models by task difficulty
- D. Use a versioned prompt template with explicit variables

### 15. A model keeps mislabelling dispute categories despite clear instructions. What should be added to the prompt?

Domain: Implement generative AI and agentic solutions

- A. Use supported prompt or response caching where appropriate
- B. Design multistep workflows with explicit checkpoints
- C. Use a versioned prompt template with explicit variables
- D. Include representative examples in the prompt

### 16. A Java service needs supported authentication and retry behavior for Foundry calls. What should it use?

Domain: Implement generative AI and agentic solutions

- A. Create and run deployments by hand in the portal
- B. Use batch processing for latency-tolerant bulk work
- C. Use a Foundry SDK or supported connector from application code
- D. Manage AI resources with infrastructure as code and CI/CD

### 17. A browser client must call the model service using short-lived delegated credentials. What should the app issue?

Domain: Implement generative AI and agentic solutions

- A. Connect the application to the Foundry project endpoint
- B. Authenticate with a managed identity instead of keys
- C. Use short-lived scoped access tokens for tool calls
- D. Store secrets in Azure Key Vault when keys are unavoidable

### 18. A team must compare two prompt designs fairly and keep a stable benchmark over time. Which two practices are required? Select two.

Domain: Implement generative AI and agentic solutions

- A. Apply watermarks or provenance markers to generated media
- B. Lower temperature for more deterministic extraction
- C. Compare variants with controlled traffic and shared metrics
- D. Use provisioned throughput for predictable high-volume workloads
- E. Build a representative golden dataset from real tasks

### 19. A regulator asks for evidence that the assistant refuses prohibited financial advice. Which evaluation applies?

Domain: Implement generative AI and agentic solutions

- A. Measure whether retrieved content and answers address the question
- B. Evaluate structure and logical consistency of responses
- C. Detect tone and sentiment appropriate to the audience
- D. Evaluate harmful, biased, or policy-violating output

### 20. An agent passes an unvalidated account number to a payment tool. What should be tightened first?

Domain: Implement generative AI and agentic solutions

- A. Use managed conversation state or memory for continuity
- B. Use a versioned prompt template with explicit variables
- C. Define narrow tool schemas with clear descriptions
- D. Put stable behavior rules in the system message

### 21. Which sequence correctly describes a governed tool call from a claims agent?

Domain: Implement generative AI and agentic solutions

- A. App authorizes → model executes tool → result returns → app validates → model responds
- B. Model requests tool → app validates and authorizes → tool executes → result returns → model responds
- C. Model responds → app authorizes → tool executes → result returns → app validates
- D. Model executes tool → app validates → tool returns result → app authorizes → model responds

### 22. A claims agent must keep a claim number across turns and check its status in a core system. Which two capabilities are required? Select two.

Domain: Implement generative AI and agentic solutions

- A. Persist conversation history in a thread or session
- B. Apply watermarks or provenance markers to generated media
- C. Expose a typed function as an agent tool
- D. Use provisioned throughput for predictable high-volume workloads
- E. Choose an embedding model suited to the content and language

### 23. Three independent checks must run at the same time and be merged into one decision. Which pattern fits?

Domain: Implement generative AI and agentic solutions

- A. Use self-critique or reflection to improve drafts
- B. Transfer control between agents with explicit context
- C. Run agents in a fixed sequence
- D. Run independent agents concurrently

### 24. An agent must critique and improve its own draft before returning it. Which pattern applies?

Domain: Implement generative AI and agentic solutions

- A. Transfer control between agents with explicit context
- B. Use self-critique or reflection to improve drafts
- C. Run independent agents concurrently
- D. Run agents in a fixed sequence

### 25. Which sequence correctly handles a production alert about failing agent responses?

Domain: Implement generative AI and agentic solutions

- A. Apply fix → detect alert → inspect traces → isolate the failing step → verify with regression evaluation
- B. Verify with regression evaluation → apply fix → detect alert → isolate the failing step → inspect traces
- C. Isolate the failing step → apply fix → detect alert → verify with regression evaluation → inspect traces
- D. Detect alert → inspect traces → isolate the failing step → apply fix → verify with regression evaluation

### 26. Outputs become repetitive and omit valid alternative phrasings. Which sampling parameter should be adjusted?

Domain: Implement generative AI and agentic solutions

- A. Evaluate structure and logical consistency of responses
- B. Adjust top-p to control response diversity
- C. Measure whether retrieved content and answers address the question
- D. Use supported prompt or response caching where appropriate

### 27. The same lengthy compliance preamble is sent with every request and dominates cost. What should be enabled?

Domain: Implement generative AI and agentic solutions

- A. Require citations tied to retrieved evidence
- B. Apply watermarks or provenance markers to generated media
- C. Use supported prompt or response caching where appropriate
- D. Use Azure Monitor and Application Insights for telemetry

### 28. A marketing photo shows an outdated card design that must be replaced while the model stays untouched. What should be used?

Domain: Implement computer vision solutions

- A. Edit a region of an image with a mask
- B. Apply prompt-driven image modifications
- C. Generate video from text or reference media
- D. Generate concise or detailed image captions

### 29. An insurer needs a short original animation explaining a claims process. Which capability applies?

Domain: Implement computer vision solutions

- A. Generate concise or detailed image captions
- B. Apply prompt-driven image modifications
- C. Generate video from text or reference media
- D. Edit generated video segments

### 30. A generated demo clip must be trimmed and its burned-in caption corrected. What capability applies?

Domain: Implement computer vision solutions

- A. Apply prompt-driven image modifications
- B. Edit generated video segments
- C. Analyze video segments for events and content
- D. Edit a region of an image with a mask

### 31. A statements portal needs short image descriptions for search and screen readers. Which two capabilities apply? Select two.

Domain: Implement computer vision solutions

- A. Apply watermarks or provenance markers to generated media
- B. Generate alt text aligned to accessibility guidance
- C. Lower temperature for more deterministic extraction
- D. Generate concise or detailed image captions
- E. Use provisioned throughput for predictable high-volume workloads

### 32. A back-office job reads one field from thousands of uniform, machine-printed forms. Which Content Understanding mode is most cost-effective?

Domain: Implement computer vision solutions

- A. Use Azure AI Document Intelligence for forms and documents
- B. Use pro mode for complex multimodal content understanding
- C. Use single-task mode for a focused extraction scenario
- D. Train a custom extraction model on labeled documents

### 33. A scanned table's columns are scrambled into meaningless text. What should be applied?

Domain: Implement computer vision solutions

- A. Produce markdown representations for downstream reasoning
- B. Preserve document layout, tables, and reading order
- C. Preserve reading order across columns and sections
- D. Apply OCR to convert images and scans into usable text

### 34. Generated marketing imagery must be identifiable as synthetic and must follow brand rules. Which two controls apply? Select two.

Domain: Implement computer vision solutions

- A. Lower temperature for more deterministic extraction
- B. Use supported prompt or response caching where appropriate
- C. Apply watermarks or provenance markers to generated media
- D. Enforce brand and usage rules for generated visuals
- E. Adjust top-p to control response diversity

### 35. Analysts need a two-paragraph digest of a 40-page complaint file. Which task applies?

Domain: Implement text analysis solutions

- A. Generate summaries with explicit length and audience constraints
- B. Extract entities with defined types and boundaries
- C. Use Azure Translator or a language model for translation
- D. Identify topics or key phrases for navigation

### 36. A contact-centre team needs automatic tagging of complaint subjects and detection of anger. Which two analyses apply? Select two.

Domain: Implement text analysis solutions

- A. Generate concise or detailed image captions
- B. Identify topics or key phrases for navigation
- C. Apply watermarks or provenance markers to generated media
- D. Generate alt text aligned to accessibility guidance
- E. Analyze sentiment and tone with an appropriate service

### 37. Product names and legal phrases are inconsistently translated across notices. What should be configured?

Domain: Implement text analysis solutions

- A. Use Azure Translator or a language model for translation
- B. Detect and redact sensitive personal data
- C. Apply a custom glossary or terminology list
- D. Extract entities with defined types and boundaries

### 38. A policyholder speaks only Spanish and must receive an English explanation by phone. Which sequence is correct?

Domain: Implement text analysis solutions

- A. Transcribe → synthesize speech → capture audio → translate → return audio
- B. Translate audio → transcribe → capture audio → synthesize → return audio
- C. Capture audio → transcribe → translate text → synthesize speech → return audio
- D. Capture audio → synthesize speech → transcribe → translate → return audio

### 39. Summaries for regulators must preserve citations and mandatory disclosures. Which approach fits?

Domain: Implement text analysis solutions

- A. Extract entities with defined types and boundaries
- B. Customize summaries and extraction for compliance needs
- C. Identify topics or key phrases for navigation
- D. Generate summaries with explicit length and audience constraints

### 40. A customer closes an account and must disappear from search results immediately. What must be implemented?

Domain: Implement information extraction solutions

- A. Propagate source deletions to indexes and caches
- B. Use an Azure AI Search indexer to pull source content
- C. Push documents to an index through the data-plane API
- D. Ingest content through supported indexers or APIs

### 41. Staff search by exact policy number and by described coverage, and each region sees only its own circulars. Which two features are required? Select two.

Domain: Implement information extraction solutions

- A. Apply document-level security filters at query time
- B. Combine keyword and vector retrieval
- C. Verify index freshness and deletion propagation
- D. Select evidence within the model's usable context
- E. Apply semantic ranking to reorder search results

### 42. An indexing pipeline must add extracted entities and written summaries to every document during ingestion. Which component defines those steps?

Domain: Implement information extraction solutions

- A. Add an enrichment skillset to an indexing pipeline
- B. Push documents to an index through the data-plane API
- C. Use supported prompt or response caching where appropriate
- D. Apply OCR to convert images and scans into usable text

### 43. Which sequence correctly builds a citable retrieval pipeline over regulatory documents?

Domain: Implement information extraction solutions

- A. Ingest → extract text → chunk → embed → index → retrieve with citations
- B. Chunk → embed → ingest → retrieve → index → cite
- C. Ingest → retrieve → chunk → embed → index → cite
- D. Index → retrieve → ingest → chunk → embed → cite

### 44. Retrieved evidence crowds out the instructions, and the model starts ignoring the question. What should be configured?

Domain: Implement information extraction solutions

- A. Remove near-duplicate evidence before ranking
- B. Use a vector index for semantic retrieval
- C. Rerank retrieved passages before generation
- D. Select evidence within the model's usable context

### 45. A bank must keep one audited model version in a single jurisdiction for the life of the contract. What should the team do?

Domain: Plan and manage an Azure AI solution

- A. Train or deploy a task-specific model outside the prebuilt catalog
- B. Compare supported models in the Foundry model catalog
- C. Use a general-purpose large language model for complex reasoning
- D. Pin the model version available in the required region

### 46. An insurance team needs document extraction and speech transcription this quarter and has no labelled corpus. What should be evaluated first?

Domain: Plan and manage an Azure AI solution

- A. Train or deploy a task-specific model outside the prebuilt catalog
- B. Use a general-purpose large language model for complex reasoning
- C. Use Foundry Tools for prebuilt vision, speech, language, and extraction needs
- D. Use a small language model for a narrow, high-volume task

### 47. An agent must call a core banking API that publishes a machine-readable contract. Which tool type fits?

Domain: Plan and manage an Azure AI solution

- A. Expose an OpenAPI operation as an agent tool
- B. Use managed conversation state or memory for continuity
- C. Connect an Azure AI Search index as agent knowledge
- D. Expose a typed function as an agent tool

### 48. A fraud model release must be blocked automatically when recall on a fixed test set drops. What should be added?

Domain: Plan and manage an Azure AI solution

- A. Block promotion in the pipeline when evaluation thresholds fail
- B. Use staged rollout with measurable rollback criteria
- C. Shift a small traffic percentage to the new version first
- D. Manage AI resources with infrastructure as code and CI/CD

### 49. A team wants to compare a new scoring model with production without affecting a single decision. What pattern fits?

Domain: Plan and manage an Azure AI solution

- A. Use a standard pay-as-you-go model deployment for variable demand
- B. Send mirrored production traffic to a candidate without returning its answers
- C. Shift a small traffic percentage to the new version first
- D. Use batch processing for latency-tolerant bulk work

### 50. The trading desk wants warning before a project's daily spend exceeds its budget. What should be configured?

Domain: Plan and manage an Azure AI solution

- A. Track cost per accepted task, not only per token
- B. Alert on spend thresholds per deployment or project
- C. Plan for model quota expressed in tokens and requests per minute
- D. Track prompt, completion, and cached token usage

### 51. Answers cite a compliance circular that the legal team retired last week. What should be monitored?

Domain: Plan and manage an Azure AI solution

- A. Monitor index freshness, failures, and document counts
- B. Monitor input and quality drift over time
- C. Monitor groundedness and citation quality in production
- D. Use Azure Monitor and Application Insights for telemetry

### 52. The workload may reach only an approved set of external services. What should be enforced?

Domain: Plan and manage an Azure AI solution

- A. Private networking with public access left enabled
- B. Use private endpoints and disable public network access
- C. Use least-privilege Azure RBAC roles for the workload identity
- D. Restrict outbound network access to approved destinations

### 53. A credit decline must be attributable to an accountable officer, not the model. Which principle applies?

Domain: Plan and manage an Azure AI solution

- A. Set agent oversight mode and tool-access constraints
- B. Preserve audit logs of changes, approvals, and tool actions
- C. Require human approval before consequential actions
- D. Enforce constraints in code and platform policy

### 54. Five years of historical statements must be reclassified once for migration. Which deployment option fits?

Domain: Plan and manage an Azure AI solution

- A. Use a standard pay-as-you-go model deployment for variable demand
- B. Use provisioned throughput for predictable high-volume workloads
- C. Use batch processing for latency-tolerant bulk work
- D. Plan for model quota expressed in tokens and requests per minute

### 55. A regulated model must come from the local catalog and must not change unexpectedly. Which two practices are required? Select two.

Domain: Plan and manage an Azure AI solution

- A. Use a standard pay-as-you-go model deployment for variable demand
- B. Use batch processing for latency-tolerant bulk work
- C. Train or deploy a task-specific model outside the prebuilt catalog
- D. Compare supported models in the Foundry model catalog
- E. Pin the model version available in the required region

### 56. A credit assistant must be checked for unsupported claims and the team must be warned promptly. Which two capabilities are required? Select two.

Domain: Plan and manage an Azure AI solution

- A. Monitor groundedness and citation quality in production
- B. Track cost per accepted task, not only per token
- C. Apply watermarks or provenance markers to generated media
- D. Measure end-to-end latency across model, retrieval, and tools
- E. Alert on latency, error rate, safety, and cost thresholds

### 57. The scoring service must not reach unapproved endpoints and must hold only its required permissions. Which two controls are required? Select two.

Domain: Plan and manage an Azure AI solution

- A. Use private endpoints and disable public network access
- B. Store secrets in Azure Key Vault when keys are unavoidable
- C. Use least-privilege Azure RBAC roles for the workload identity
- D. Configure content safety filters for harmful categories
- E. Restrict outbound network access to approved destinations

### 58. Which sequence correctly releases a scoring change with an evaluation gate?

Domain: Plan and manage an Azure AI solution

- A. Deploy a canary → commit change → promote after metrics hold → run the evaluation suite → block on failed thresholds
- B. Run the evaluation suite → deploy a canary → commit change → block on failed thresholds → promote after metrics hold
- C. Commit change → run the evaluation suite → block on failed thresholds → deploy a canary → promote after metrics hold
- D. Commit change → deploy a canary → promote after metrics hold → run the evaluation suite → block on failed thresholds

### 59. A disclosure requirement that spans two sections is never retrieved. What should be adjusted?

Domain: Implement generative AI and agentic solutions

- A. Set chunk overlap so facts spanning a boundary stay retrievable
- B. Choose an embedding model suited to the content and language
- C. Select evidence within the model's usable context
- D. Choose chunk size and overlap for retrieval quality

### 60. Regulatory text changes monthly and every answer must cite the circular used. Which approach fits?

Domain: Implement generative AI and agentic solutions

- A. Ground responses with retrieval-augmented generation
- B. Design multistep workflows with explicit checkpoints
- C. Route requests to different models by task difficulty
- D. Include representative examples in the prompt

### 61. A customer portal must call the model service with a short-lived delegated credential. What should it request?

Domain: Implement generative AI and agentic solutions

- A. Use a Foundry SDK or supported connector from application code
- B. Authenticate with a managed identity instead of keys
- C. Store secrets in Azure Key Vault when keys are unavoidable
- D. Use short-lived scoped access tokens for tool calls

### 62. Two extraction prompts must be compared on identical documents so only the prompt differs. What provides that?

Domain: Implement generative AI and agentic solutions

- A. Re-run evaluation suites after meaningful changes
- B. Build a representative golden dataset from real tasks
- C. Compare variants with controlled traffic and shared metrics
- D. Use evaluators for quality, safety, and groundedness

### 63. A model upgrade must not restore a previously fixed misclassification. What should run first?

Domain: Implement generative AI and agentic solutions

- A. Use evaluators for quality, safety, and groundedness
- B. Re-run evaluation suites after meaningful changes
- C. Evaluate harmful, biased, or policy-violating output
- D. Build a representative golden dataset from real tasks

### 64. The agent submits a free-text account reference to a payment tool. What should be tightened first?

Domain: Implement generative AI and agentic solutions

- A. Define narrow tool schemas with clear descriptions
- B. Put stable behavior rules in the system message
- C. Use managed conversation state or memory for continuity
- D. Route requests to different models by task difficulty

### 65. A general banking agent must transfer a dispute to the disputes specialist while keeping context. Which pattern fits?

Domain: Implement generative AI and agentic solutions

- A. Use self-critique or reflection to improve drafts
- B. Run independent agents concurrently
- C. Use a manager agent to coordinate specialists
- D. Transfer control between agents with explicit context

### 66. Three independent sanctions checks must complete within a two-second budget. Which pattern fits?

Domain: Implement generative AI and agentic solutions

- A. Run agents in a fixed sequence
- B. Run independent agents concurrently
- C. Use a manager agent to coordinate specialists
- D. Use self-critique or reflection to improve drafts

### 67. Generated ledger entries include prose that breaks the parser. What should be specified?

Domain: Implement generative AI and agentic solutions

- A. Set a stop sequence so generation ends at the intended boundary
- B. Adjust top-p to control response diversity
- C. Lower temperature for more deterministic extraction
- D. Use supported prompt or response caching where appropriate

### 68. Drafted client letters repeat the same sentence structure and never vary. Which parameter should be adjusted?

Domain: Implement generative AI and agentic solutions

- A. Adjust top-p to control response diversity
- B. Lower temperature for more deterministic extraction
- C. Set a seed parameter for reproducible sampling where the provider supports it
- D. Use supported prompt or response caching where appropriate

### 69. A trading service must use maintained client behaviour and hold no stored credential. Which two choices are required? Select two.

Domain: Implement generative AI and agentic solutions

- A. Create and run deployments by hand in the portal
- B. Store secrets in Azure Key Vault when keys are unavoidable
- C. Use short-lived scoped access tokens for tool calls
- D. Use a Foundry SDK or supported connector from application code
- E. Authenticate with a managed identity instead of keys

### 70. A release must be scored for accuracy and screened for prohibited financial advice. Which two practices are required? Select two.

Domain: Implement generative AI and agentic solutions

- A. Re-run evaluation suites after meaningful changes
- B. Compare variants with controlled traffic and shared metrics
- C. Evaluate harmful, biased, or policy-violating output
- D. Use evaluators for quality, safety, and groundedness
- E. Build a representative golden dataset from real tasks

### 71. A claims agent must search approved policy documents and compute payout totals reliably. Which two tools are required? Select two.

Domain: Implement generative AI and agentic solutions

- A. Use managed conversation state or memory for continuity
- B. Route requests to different models by task difficulty
- C. Expose an OpenAPI operation as an agent tool
- D. Give the agent a file-search tool over approved document stores
- E. Enable a sandboxed code interpreter tool for calculations

### 72. Which sequence correctly builds and releases a dispute agent?

Domain: Implement generative AI and agentic solutions

- A. Attach knowledge → configure tools → deploy with monitoring → define role and goal → evaluate in sandbox
- B. Define role and goal → configure tools → attach knowledge → evaluate in sandbox → deploy with monitoring
- C. Deploy with monitoring → define role and goal → configure tools → evaluate in sandbox → attach knowledge
- D. Configure tools → deploy with monitoring → define role and goal → attach knowledge → evaluate in sandbox

### 73. A generated chart is technically correct but misleading in context, and automated filters pass it. What should be added?

Domain: Implement computer vision solutions

- A. Apply watermarks or provenance markers to generated media
- B. Queue flagged generations for human moderation before release
- C. Enforce brand and usage rules for generated visuals
- D. Filter unsafe or disallowed visual content

### 74. A marketing library needs filterable descriptive tags for thousands of images. What should be generated?

Domain: Implement computer vision solutions

- A. Answer questions grounded in visual evidence
- B. Generate alt text aligned to accessibility guidance
- C. Generate a set of descriptive tags for each image
- D. Generate concise or detailed image captions

### 75. Extracted statement text is scrambled because the layout is read column by column incorrectly. What should be applied?

Domain: Implement computer vision solutions

- A. Preserve document layout, tables, and reading order
- B. Apply OCR to convert images and scans into usable text
- C. Preserve reading order across columns and sections
- D. Produce markdown representations for downstream reasoning

### 76. A team needs a configurable analyzer over mixed statements and correspondence rather than a fixed prebuilt model. Which service fits?

Domain: Implement computer vision solutions

- A. Configure a Content Understanding analyzer for the content type
- B. Use Azure Content Understanding analyzers in Foundry Tools
- C. Use Azure AI Document Intelligence for forms and documents
- D. Use a prebuilt document model for common document types

### 77. Statements mix tables, signatures, and photos across pages, and output must feed a reasoning model. Which two choices are required? Select two.

Domain: Implement computer vision solutions

- A. Identify objects, components, or regions in visual content
- B. Generate concise or detailed image captions
- C. Use pro mode for complex multimodal content understanding
- D. Use single-task mode for a focused extraction scenario
- E. Return markdown for retrieval and reasoning pipelines

### 78. Which sequence correctly processes a scanned statement and routes doubtful amounts for review?

Domain: Implement computer vision solutions

- A. Upload image → validate format and size → send multimodal request → parse structured fields → route low-confidence values to review
- B. Validate format → review → upload image → parse structured fields → send multimodal request
- C. Parse structured fields → send multimodal request → upload image → validate format → review
- D. Send multimodal request → upload image → validate format → parse structured fields → review

### 79. An audit requires summaries that quote exact source sentences. Which style fits?

Domain: Implement text analysis solutions

- A. Generate an abstractive summary in new wording
- B. Customize summaries and extraction for compliance needs
- C. Generate summaries with explicit length and audience constraints
- D. Select and return the most relevant source sentences

### 80. Beneficiary names in another writing system must print correctly without translating meaning. Which capability applies?

Domain: Implement text analysis solutions

- A. Use Azure Translator or a language model for translation
- B. Adapt prompts and models to domain terminology
- C. Convert names between writing systems without translating meaning
- D. Apply a custom glossary or terminology list

### 81. A collections phone line must use one consistent branded voice. What should be selected?

Domain: Implement text analysis solutions

- A. Apply a custom glossary or terminology list
- B. Synthesize speech with Azure AI Speech
- C. Use a custom speech model for specialized vocabulary
- D. Select a specific synthesis voice for consistent spoken output

### 82. Analysts need a quick topical index of what each complaint file covers. Which capability applies?

Domain: Implement text analysis solutions

- A. Extract key phrases to summarize what a document covers
- B. Generate summaries with explicit length and audience constraints
- C. Identify topics or key phrases for navigation
- D. Extract entities with defined types and boundaries

### 83. A conduct mailbox must detect personal data and rising aggression. Which two analyses are relevant? Select two.

Domain: Implement text analysis solutions

- A. Apply a custom glossary or terminology list
- B. Analyze sentiment and tone with an appropriate service
- C. Detect and redact sensitive personal data
- D. Identify topics or key phrases for navigation
- E. Generate summaries with explicit length and audience constraints

### 84. Searches for a policy code return unrelated marketing content because one family dominates. What should be tuned and measured?

Domain: Implement information extraction solutions

- A. Apply semantic ranking to reorder search results
- B. Tune scoring and boosting against a labelled query set
- C. Use a vector index for semantic retrieval
- D. Combine keyword and vector retrieval

### 85. Each indexed circular must gain extracted obligations and a generated abstract. What produces that?

Domain: Implement information extraction solutions

- A. Use an Azure AI Search indexer to pull source content
- B. Return markdown for retrieval and reasoning pipelines
- C. Add an enrichment skillset to an indexing pipeline
- D. Add enrichment skills for text, image, and layout

### 86. Investigators must filter by filing date and sort by amount, but those fields are full-text only. What should change?

Domain: Implement information extraction solutions

- A. Use Azure AI Document Intelligence for forms and documents
- B. Define index fields, attributes, and searchable versus filterable behavior
- C. Return typed fields for automation
- D. Configure a Content Understanding analyzer for the content type

### 87. Scanned agreements must preserve signature block relationships for extraction. What should be applied?

Domain: Implement information extraction solutions

- A. Choose chunk size and overlap for retrieval quality
- B. Produce markdown representations for downstream reasoning
- C. Use an Azure AI Search indexer to pull source content
- D. Combine OCR with layout analysis for complex documents

### 88. Which sequence correctly stands up a regulatory document index?

Domain: Implement information extraction solutions

- A. Validate relevance on sample queries → run the indexer → connect the data source → define the index schema → attach the enrichment skillset
- B. Connect the data source → define the index schema → attach the enrichment skillset → run the indexer → validate relevance on sample queries
- C. Run the indexer → connect the data source → define the index schema → attach the enrichment skillset → validate relevance on sample queries
- D. Attach the enrichment skillset → connect the data source → validate relevance on sample queries → define the index schema → run the indexer

---

## Case study — FraudDesk

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 89. Investigators in two regions must not see each other's case notes. Which control enforces that separation?

Domain: Plan and manage an Azure AI solution

- A. Store secrets in Azure Key Vault when keys are unavoidable
- B. Restrict outbound network access to approved destinations
- C. Apply document-level security filters at query time
- D. Use least-privilege Azure RBAC roles for the workload identity

### 90. The team needs comparable groundedness scores for two retrieval configurations. What should they run?

Domain: Implement generative AI and agentic solutions

- A. Alert on latency, error rate, safety, and cost thresholds
- B. Use Azure Monitor and Application Insights for telemetry
- C. Preserve audit logs of changes, approvals, and tool actions
- D. Use evaluators for quality, safety, and groundedness

### 91. A request fails only after the second tool call. What should be inspected first?

Domain: Implement generative AI and agentic solutions

- A. Use supported prompt or response caching where appropriate
- B. Lower temperature for more deterministic extraction
- C. Enable tracing across agent, model, and tool calls
- D. Apply watermarks or provenance markers to generated media

---

## Case study — LedgerOne

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 92. An auditor asks for totals across two thousand extracted line items, and text-based arithmetic is unreliable. Which tool is required?

Domain: Implement generative AI and agentic solutions

- A. Enable a sandboxed code interpreter tool for calculations
- B. Expose an OpenAPI operation as an agent tool
- C. Use managed conversation state or memory for continuity
- D. Give the agent a file-search tool over approved document stores

### 93. A payment request fails only after the second tool call. What should be inspected?

Domain: Implement generative AI and agentic solutions

- A. Use supported prompt or response caching where appropriate
- B. Enable tracing across agent, model, and tool calls
- C. Apply watermarks or provenance markers to generated media
- D. Lower temperature for more deterministic extraction

### 94. Newly generated client letters must be searchable within seconds. What should the application use?

Domain: Implement information extraction solutions

- A. Push documents to an index through the data-plane API
- B. Use an Azure AI Search indexer to pull source content
- C. Add an enrichment skillset to an indexing pipeline
- D. Apply OCR to convert images and scans into usable text

---

## Case study — LoanDocs

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 95. Applicants may request that decision letters be read aloud over the phone. Which capability applies?

Domain: Implement text analysis solutions

- A. Use a custom speech model for specialized vocabulary
- B. Transcribe speech to text with Azure AI Speech
- C. Synthesize speech with Azure AI Speech
- D. Use a multimodal model to reason over audio content

### 96. Scanned letters use regional abbreviations that the extraction prompt ignores. What should be added?

Domain: Implement text analysis solutions

- A. Detect and redact sensitive personal data
- B. Use Azure Translator or a language model for translation
- C. Adapt prompts and models to domain terminology
- D. Apply a custom glossary or terminology list

### 97. A lender receives its own proprietary application form with no standard equivalent. What should be built?

Domain: Implement information extraction solutions

- A. Configure a Content Understanding analyzer for the content type
- B. Train a custom extraction model on labeled documents
- C. Use a prebuilt document model for common document types
- D. Use single-task mode for a focused extraction scenario

---

## Case study — VaultTrust

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 98. An adviser returns to the same client file the next day and the assistant must recall the case reference. Which capability is required?

Domain: Implement generative AI and agentic solutions

- A. Persist conversation history in a thread or session
- B. Use provisioned throughput for predictable high-volume workloads
- C. Choose an embedding model suited to the content and language
- D. Apply watermarks or provenance markers to generated media

### 99. Adviser dictation misreads product codes that matter for compliance. What should be trained?

Domain: Implement text analysis solutions

- A. Transcribe speech to text with Azure AI Speech
- B. Synthesize speech with Azure AI Speech
- C. Apply a custom glossary or terminology list
- D. Use a custom speech model for specialized vocabulary

### 100. Scanned amounts are sometimes misread. What should route those values to a person?

Domain: Implement information extraction solutions

- A. Generate summaries with explicit length and audience constraints
- B. Measure whether retrieved content and answers address the question
- C. Analyze sentiment and tone with an appropriate service
- D. Use field-level confidence to route exceptions

---

## Answer key and explanations

### Question 1 — A

Answer: Compare supported models in the Foundry model catalog. The model catalog shows regional availability and version lifecycle commitments. The catalog shows supported models with capability, modality, region, and lifecycle details. Verify availability for your subscription and region before designing around one model. Local study-map skill 1.1 (Selecting Foundry Models and Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. The catalog shows supported models with capability, modality, region, and lifecycle details. Verify availability for your subscription and region before designing around one model. In this case: The model catalog shows regional availability and version lifecycle commitments.
- **B:** Incorrect for this question. Large models handle ambiguity and multi-step reasoning better in many cases, at higher cost and latency. Select with measured evidence rather than brand preference. Why the correct answer wins: The model catalog shows regional availability and version lifecycle commitments.
- **C:** Incorrect for this question. Small models can reduce latency and cost for constrained classification or extraction. Confirm quality on representative data before standardizing. Why the correct answer wins: The model catalog shows regional availability and version lifecycle commitments.
- **D:** Incorrect for this question. A custom model is justified when supported prebuilt options cannot meet a defined requirement. It adds data, evaluation, and lifecycle obligations. Why the correct answer wins: The model catalog shows regional availability and version lifecycle commitments.

### Question 2 — C

Answer: Train or deploy a task-specific model outside the prebuilt catalog. A custom or fine-tuned model is trained on organization-specific data under its governance. A custom model is justified when supported prebuilt options cannot meet a defined requirement. It adds data, evaluation, and lifecycle obligations. Local study-map skill 1.1 (Selecting Foundry Models and Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Multimodal models accept more than one content type in a request. Validate extraction and grounding quality for each modality used. Why the correct answer wins: A custom or fine-tuned model is trained on organization-specific data under its governance.
- **B:** Incorrect for this question. Small models can reduce latency and cost for constrained classification or extraction. Confirm quality on representative data before standardizing. Why the correct answer wins: A custom or fine-tuned model is trained on organization-specific data under its governance.
- **C:** Correct. A custom model is justified when supported prebuilt options cannot meet a defined requirement. It adds data, evaluation, and lifecycle obligations. In this case: A custom or fine-tuned model is trained on organization-specific data under its governance.
- **D:** Incorrect for this question. Large models handle ambiguity and multi-step reasoning better in many cases, at higher cost and latency. Select with measured evidence rather than brand preference. Why the correct answer wins: A custom or fine-tuned model is trained on organization-specific data under its governance.

### Question 3 — A

Answer: Use a vector index for semantic retrieval. A vector index compares embeddings and returns semantically similar content. Embeddings support similarity search over meaning rather than exact terms. Vector search still needs chunking, filtering, and evaluation. Local study-map skill 1.2 (Retrieval, Memory, Tool, and Knowledge Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. Embeddings support similarity search over meaning rather than exact terms. Vector search still needs chunking, filtering, and evaluation. In this case: A vector index compares embeddings and returns semantically similar content.
- **B:** Incorrect for this question. An index gives an agent curated, searchable evidence under configured access. Index content and permissions require ongoing ownership. Why the correct answer wins: A vector index compares embeddings and returns semantically similar content.
- **C:** Incorrect for this question. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Why the correct answer wins: A vector index compares embeddings and returns semantically similar content.
- **D:** Incorrect for this question. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. Why the correct answer wins: A vector index compares embeddings and returns semantically similar content.

### Question 4 — D, E

Answers: Manage AI resources with infrastructure as code and CI/CD; Use private endpoints and disable public network access. Infrastructure as code provides repeatability, and private endpoints remove public exposure. Repeatable deployments reduce configuration drift. Include model deployments, indexes, and connections in review and promotion. Private connectivity keeps service traffic on approved network paths. Pair it with private DNS so clients resolve the private address. Local study-map skill 1.3 (Infrastructure, Deployment, and CI/CD), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Infrastructure as code provides repeatability, and private endpoints remove public exposure.
- **B:** Incorrect for this question. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. Why the correct answer wins: Infrastructure as code provides repeatability, and private endpoints remove public exposure.
- **C:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: Infrastructure as code provides repeatability, and private endpoints remove public exposure.
- **D:** Correct. Private connectivity keeps service traffic on approved network paths. Pair it with private DNS so clients resolve the private address. In this case: Infrastructure as code provides repeatability, and private endpoints remove public exposure.
- **E:** Correct. Repeatable deployments reduce configuration drift. Include model deployments, indexes, and connections in review and promotion. In this case: Infrastructure as code provides repeatability, and private endpoints remove public exposure.

### Question 5 — D

Answer: Use batch processing for latency-tolerant bulk work. Batch deployment suits large asynchronous jobs that tolerate delay. Batch deployments can lower cost for large asynchronous jobs. They are unsuitable for interactive agent turns. Local study-map skill 1.3 (Infrastructure, Deployment, and CI/CD), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: Batch deployment suits large asynchronous jobs that tolerate delay.
- **B:** Incorrect for this question. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. Why the correct answer wins: Batch deployment suits large asynchronous jobs that tolerate delay.
- **C:** Incorrect for this question. Standard deployments bill per token and scale within quota. They suit spiky or early workloads. Why the correct answer wins: Batch deployment suits large asynchronous jobs that tolerate delay.
- **D:** Correct. Batch deployments can lower cost for large asynchronous jobs. They are unsuitable for interactive agent turns. In this case: Batch deployment suits large asynchronous jobs that tolerate delay.

### Question 6 — B

Answer: Use provisioned throughput for predictable high-volume workloads. Provisioned throughput reserves capacity for predictable continuous demand. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Local study-map skill 1.4 (Quotas, Scaling, and Cost), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Batch deployments can lower cost for large asynchronous jobs. They are unsuitable for interactive agent turns. Why the correct answer wins: Provisioned throughput reserves capacity for predictable continuous demand.
- **B:** Correct. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. In this case: Provisioned throughput reserves capacity for predictable continuous demand.
- **C:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Provisioned throughput reserves capacity for predictable continuous demand.
- **D:** Incorrect for this question. Standard deployments bill per token and scale within quota. They suit spiky or early workloads. Why the correct answer wins: Provisioned throughput reserves capacity for predictable continuous demand.

### Question 7 — D

Answer: Track prompt, completion, and cached token usage. Token analytics attributes consumption so cost can be optimized per workload. Token analytics supports cost and performance tuning. Attribute usage to features and tenants where possible. Local study-map skill 1.4 (Quotas, Scaling, and Cost), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. Why the correct answer wins: Token analytics attributes consumption so cost can be optimized per workload.
- **B:** Incorrect for this question. Retries, tool calls, evaluation, and review contribute to unit economics. Per-outcome cost supports better optimization. Why the correct answer wins: Token analytics attributes consumption so cost can be optimized per workload.
- **C:** Incorrect for this question. User behavior, data, and models change. Rolling baselines reveal degradation that a one-time evaluation misses. Why the correct answer wins: Token analytics attributes consumption so cost can be optimized per workload.
- **D:** Correct. Token analytics supports cost and performance tuning. Attribute usage to features and tenants where possible. In this case: Token analytics attributes consumption so cost can be optimized per workload.

### Question 8 — C

Answer: Alert on latency, error rate, safety, and cost thresholds. Alert rules trigger notifications when a monitored metric crosses a threshold. Alerts turn monitoring into action. Route them to an accountable owner with a runbook. Local study-map skill 1.5 (Monitoring Performance, Drift, Safety, and Grounding), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. User behavior, data, and models change. Rolling baselines reveal degradation that a one-time evaluation misses. Why the correct answer wins: Alert rules trigger notifications when a monitored metric crosses a threshold.
- **B:** Incorrect for this question. Central telemetry captures latency, errors, dependencies, and custom events. Redact sensitive content before logging. Why the correct answer wins: Alert rules trigger notifications when a monitored metric crosses a threshold.
- **C:** Correct. Alerts turn monitoring into action. Route them to an accountable owner with a runbook. In this case: Alert rules trigger notifications when a monitored metric crosses a threshold.
- **D:** Incorrect for this question. Audit evidence supports investigation and accountability. Protect log integrity and retention. Why the correct answer wins: Alert rules trigger notifications when a monitored metric crosses a threshold.

### Question 9 — D

Answer: Re-run evaluation suites after meaningful changes. Regression evaluation re-runs known failure cases against the candidate version. Prompts, models, indexes, and tools all affect behavior. Regression tests catch unintended effects. Local study-map skill 1.5 (Monitoring Performance, Drift, Safety, and Grounding), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Controlled comparison supports evidence-based change. Avoid changing several variables at once. Why the correct answer wins: Regression evaluation re-runs known failure cases against the candidate version.
- **B:** Incorrect for this question. Evaluators provide repeatable signals across models and prompts. They must be calibrated against human judgment for high-impact work. Why the correct answer wins: Regression evaluation re-runs known failure cases against the candidate version.
- **C:** Incorrect for this question. A golden set anchors evaluation in expected behavior. Include edge cases and high-risk scenarios. Why the correct answer wins: Regression evaluation re-runs known failure cases against the candidate version.
- **D:** Correct. Prompts, models, indexes, and tools all affect behavior. Regression tests catch unintended effects. In this case: Regression evaluation re-runs known failure cases against the candidate version.

### Question 10 — D

Answer: Store secrets in Azure Key Vault when keys are unavoidable. A key vault stores and rotates secrets under access policy and audit. A managed secret store supports rotation and access control. Secrets should never appear in prompts, code, or logs. Local study-map skill 1.6 (Security, Identity, and Networking), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Roles should match the operations the app or agent performs. Broad contributor access increases blast radius. Why the correct answer wins: A key vault stores and rotates secrets under access policy and audit.
- **B:** Incorrect for this question. Private connectivity keeps service traffic on approved network paths. Pair it with private DNS so clients resolve the private address. Why the correct answer wins: A key vault stores and rotates secrets under access policy and audit.
- **C:** Incorrect for this question. Managed identities avoid embedded secrets and support role-based access. Assign only required data-plane roles. Why the correct answer wins: A key vault stores and rotates secrets under access policy and audit.
- **D:** Correct. A managed secret store supports rotation and access control. Secrets should never appear in prompts, code, or logs. In this case: A key vault stores and rotates secrets under access policy and audit.

### Question 11 — C

Answer: Restrict outbound network access to approved destinations. Egress controls limit outbound destinations from the workload. Egress controls reduce exfiltration and unauthorized tool reach. Combine with identity and data controls. Local study-map skill 1.6 (Security, Identity, and Networking), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Leaving the public path open defeats the purpose of a private networking design because traffic can still bypass the private route. Why the correct answer wins: Egress controls limit outbound destinations from the workload.
- **B:** Incorrect for this question. Name resolution alone does not block public access, so it must be paired with a private endpoint and public access disabled. Why the correct answer wins: Egress controls limit outbound destinations from the workload.
- **C:** Correct. Egress controls reduce exfiltration and unauthorized tool reach. Combine with identity and data controls. In this case: Egress controls limit outbound destinations from the workload.
- **D:** Incorrect for this question. Private connectivity keeps service traffic on approved network paths. Pair it with private DNS so clients resolve the private address. Why the correct answer wins: Egress controls limit outbound destinations from the workload.

### Question 12 — A

Answer: Test the solution with adversarial and boundary cases. Red teaming deliberately attacks the system to find safety weaknesses before users do. Red-team cases expose prompt injection, data leakage, and unsafe tool use. Findings should become regression tests. Local study-map skill 1.7 (Responsible AI Controls and Oversight), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. Red-team cases expose prompt injection, data leakage, and unsafe tool use. Findings should become regression tests. In this case: Red teaming deliberately attacks the system to find safety weaknesses before users do.
- **B:** Incorrect for this question. Guardrails are technical controls, not prompt suggestions. Validate inputs, authorize tools, and limit egress. Why the correct answer wins: Red teaming deliberately attacks the system to find safety weaknesses before users do.
- **C:** Incorrect for this question. Oversight settings bound what an agent may do autonomously. They should be tested against realistic misuse and failure. Why the correct answer wins: Red teaming deliberately attacks the system to find safety weaknesses before users do.
- **D:** Incorrect for this question. Audit evidence supports investigation and accountability. Protect log integrity and retention. Why the correct answer wins: Red teaming deliberately attacks the system to find safety weaknesses before users do.

### Question 13 — C, D

Answers: Configure content safety filters for harmful categories; Set agent oversight mode and tool-access constraints. Content filters reduce harmful output, and human oversight keeps decisions attributable. Filters assign severity and can block or annotate content. Thresholds should reflect the use case and applicable policy. Oversight settings bound what an agent may do autonomously. They should be tested against realistic misuse and failure. Local study-map skill 1.7 (Responsible AI Controls and Oversight), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Top-p narrows or broadens token sampling. Tune with evaluation rather than by intuition. Why the correct answer wins: Content filters reduce harmful output, and human oversight keeps decisions attributable.
- **B:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Content filters reduce harmful output, and human oversight keeps decisions attributable.
- **C:** Correct. Oversight settings bound what an agent may do autonomously. They should be tested against realistic misuse and failure. In this case: Content filters reduce harmful output, and human oversight keeps decisions attributable.
- **D:** Correct. Filters assign severity and can block or annotate content. Thresholds should reflect the use case and applicable policy. In this case: Content filters reduce harmful output, and human oversight keeps decisions attributable.
- **E:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Content filters reduce harmful output, and human oversight keeps decisions attributable.

### Question 14 — C

Answer: Route requests to different models by task difficulty. A router sends each request to the appropriate model by complexity and cost. Routing can balance quality and cost. Fallback and evaluation are required. Local study-map skill 2.1 (Building Generative Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. RAG supplies selected source content at request time so answers can cite current evidence. It reduces but does not eliminate fabrication. Why the correct answer wins: A router sends each request to the appropriate model by complexity and cost.
- **B:** Incorrect for this question. Examples clarify format and boundaries. They do not guarantee correctness on unseen inputs. Why the correct answer wins: A router sends each request to the appropriate model by complexity and cost.
- **C:** Correct. Routing can balance quality and cost. Fallback and evaluation are required. In this case: A router sends each request to the appropriate model by complexity and cost.
- **D:** Incorrect for this question. Templates improve consistency and reviewability. Version them and test changes. Why the correct answer wins: A router sends each request to the appropriate model by complexity and cost.

### Question 15 — D

Answer: Include representative examples in the prompt. A few labeled examples show the model the expected categorization pattern. Examples clarify format and boundaries. They do not guarantee correctness on unseen inputs. Local study-map skill 2.1 (Building Generative Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: A few labeled examples show the model the expected categorization pattern.
- **B:** Incorrect for this question. Checkpoints validate intermediate results before later steps depend on them. This limits error propagation. Why the correct answer wins: A few labeled examples show the model the expected categorization pattern.
- **C:** Incorrect for this question. Templates improve consistency and reviewability. Version them and test changes. Why the correct answer wins: A few labeled examples show the model the expected categorization pattern.
- **D:** Correct. Examples clarify format and boundaries. They do not guarantee correctness on unseen inputs. In this case: A few labeled examples show the model the expected categorization pattern.

### Question 16 — C

Answer: Use a Foundry SDK or supported connector from application code. A supported Foundry SDK provides maintained client behavior rather than raw HTTP calls. SDKs provide supported request and response patterns. Pin versions and handle retries, timeouts, and errors explicitly. Local study-map skill 2.2 (Foundry SDK and Project Integration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Manual portal changes work for exploration but are slow, undocumented, and hard to reproduce, so they are a poor fit for governed release processes. Why the correct answer wins: A supported Foundry SDK provides maintained client behavior rather than raw HTTP calls.
- **B:** Incorrect for this question. Batch deployments can lower cost for large asynchronous jobs. They are unsuitable for interactive agent turns. Why the correct answer wins: A supported Foundry SDK provides maintained client behavior rather than raw HTTP calls.
- **C:** Correct. SDKs provide supported request and response patterns. Pin versions and handle retries, timeouts, and errors explicitly. In this case: A supported Foundry SDK provides maintained client behavior rather than raw HTTP calls.
- **D:** Incorrect for this question. Repeatable deployments reduce configuration drift. Include model deployments, indexes, and connections in review and promotion. Why the correct answer wins: A supported Foundry SDK provides maintained client behavior rather than raw HTTP calls.

### Question 17 — C

Answer: Use short-lived scoped access tokens for tool calls. A short-lived access token scopes the browser session without embedding long-term secrets. Short-lived credentials reduce misuse risk. Never place tokens in prompts or logs. Local study-map skill 2.2 (Foundry SDK and Project Integration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Project endpoints and SDK clients bind an app to approved models and resources. Use identity-based authentication and environment-specific configuration. Why the correct answer wins: A short-lived access token scopes the browser session without embedding long-term secrets.
- **B:** Incorrect for this question. Managed identities avoid embedded secrets and support role-based access. Assign only required data-plane roles. Why the correct answer wins: A short-lived access token scopes the browser session without embedding long-term secrets.
- **C:** Correct. Short-lived credentials reduce misuse risk. Never place tokens in prompts or logs. In this case: A short-lived access token scopes the browser session without embedding long-term secrets.
- **D:** Incorrect for this question. A managed secret store supports rotation and access control. Secrets should never appear in prompts, code, or logs. Why the correct answer wins: A short-lived access token scopes the browser session without embedding long-term secrets.

### Question 18 — C, E

Answers: Build a representative golden dataset from real tasks; Compare variants with controlled traffic and shared metrics. A golden dataset provides a stable benchmark, and an A/B test compares variants on it. A golden set anchors evaluation in expected behavior. Include edge cases and high-risk scenarios. Controlled comparison supports evidence-based change. Avoid changing several variables at once. Local study-map skill 2.3 (Evaluating Models and Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: A golden dataset provides a stable benchmark, and an A/B test compares variants on it.
- **B:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: A golden dataset provides a stable benchmark, and an A/B test compares variants on it.
- **C:** Correct. Controlled comparison supports evidence-based change. Avoid changing several variables at once. In this case: A golden dataset provides a stable benchmark, and an A/B test compares variants on it.
- **D:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: A golden dataset provides a stable benchmark, and an A/B test compares variants on it.
- **E:** Correct. A golden set anchors evaluation in expected behavior. Include edge cases and high-risk scenarios. In this case: A golden dataset provides a stable benchmark, and an A/B test compares variants on it.

### Question 19 — D

Answer: Evaluate harmful, biased, or policy-violating output. Safety evaluation measures harmful or prohibited responses against defined criteria. Safety evaluation complements content filters. Use representative adversarial inputs. Local study-map skill 2.3 (Evaluating Models and Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Relevance covers both retrieval and response usefulness. A correct but off-topic answer still fails. Why the correct answer wins: Safety evaluation measures harmful or prohibited responses against defined criteria.
- **B:** Incorrect for this question. Coherence checks readability and internal consistency. It does not establish factual accuracy. Why the correct answer wins: Safety evaluation measures harmful or prohibited responses against defined criteria.
- **C:** Incorrect for this question. Tone analysis supports brand and customer communication. Context and culture affect interpretation. Why the correct answer wins: Safety evaluation measures harmful or prohibited responses against defined criteria.
- **D:** Correct. Safety evaluation complements content filters. Use representative adversarial inputs. In this case: Safety evaluation measures harmful or prohibited responses against defined criteria.

### Question 20 — C

Answer: Define narrow tool schemas with clear descriptions. A strict tool schema with typed parameters prevents malformed or ambiguous arguments. Precise schemas help the model choose tools and arguments correctly. Broad or ambiguous tools invite unsafe calls. Local study-map skill 2.4 (Agent Roles, Goals, and Tool Schemas), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Why the correct answer wins: A strict tool schema with typed parameters prevents malformed or ambiguous arguments.
- **B:** Incorrect for this question. Templates improve consistency and reviewability. Version them and test changes. Why the correct answer wins: A strict tool schema with typed parameters prevents malformed or ambiguous arguments.
- **C:** Correct. Precise schemas help the model choose tools and arguments correctly. Broad or ambiguous tools invite unsafe calls. In this case: A strict tool schema with typed parameters prevents malformed or ambiguous arguments.
- **D:** Incorrect for this question. System messages define role and constraints. They are not a security boundary against injection. Why the correct answer wins: A strict tool schema with typed parameters prevents malformed or ambiguous arguments.

### Question 21 — B

Answer: Model requests tool → app validates and authorizes → tool executes → result returns → model responds. The application validates and authorizes the call before any tool executes. Tool execution authority belongs to the application, which validates and authorizes before acting. Local study-map skill 2.5 (Agent Tools, Retrieval, Memory, and Function Calling), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Execution must follow validation, and the model is not the execution boundary. Why the correct answer wins: The application validates and authorizes the call before any tool executes.
- **B:** Correct. Tool execution authority belongs to the application, which validates and authorizes before acting. In this case: The application validates and authorizes the call before any tool executes.
- **C:** Incorrect for this question. The response cannot precede the tool action and validation. Why the correct answer wins: The application validates and authorizes the call before any tool executes.
- **D:** Incorrect for this question. The model cannot execute the tool, and authorization after execution is too late. Why the correct answer wins: The application validates and authorizes the call before any tool executes.

### Question 22 — A, C

Answers: Persist conversation history in a thread or session; Expose a typed function as an agent tool. Conversation state preserves the claim number, and a function tool performs the lookup. Threads support continuity across turns. Apply retention and access controls to stored history. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. Local study-map skill 2.5 (Agent Tools, Retrieval, Memory, and Function Calling), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Threads support continuity across turns. Apply retention and access controls to stored history. In this case: Conversation state preserves the claim number, and a function tool performs the lookup.
- **B:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Conversation state preserves the claim number, and a function tool performs the lookup.
- **C:** Correct. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. In this case: Conversation state preserves the claim number, and a function tool performs the lookup.
- **D:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: Conversation state preserves the claim number, and a function tool performs the lookup.
- **E:** Incorrect for this question. Embeddings determine semantic similarity behavior. Evaluate retrieval quality before and after changes. Why the correct answer wins: Conversation state preserves the claim number, and a function tool performs the lookup.

### Question 23 — D

Answer: Run independent agents concurrently. A parallel agent pattern runs independent work concurrently and combines the results. Parallel execution reduces wall-clock time for independent work. Reconciliation still requires design. Local study-map skill 2.6 (Multi-Agent Orchestration and Safeguards), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Reflection can catch omissions and inconsistencies. It can also reinforce errors, so validate against evidence. Why the correct answer wins: A parallel agent pattern runs independent work concurrently and combines the results.
- **B:** Incorrect for this question. Handoffs should carry goal, evidence, permissions, and open questions. Implicit context is easily lost. Why the correct answer wins: A parallel agent pattern runs independent work concurrently and combines the results.
- **C:** Incorrect for this question. Sequential orchestration makes dependencies explicit. It may add latency where steps could run concurrently. Why the correct answer wins: A parallel agent pattern runs independent work concurrently and combines the results.
- **D:** Correct. Parallel execution reduces wall-clock time for independent work. Reconciliation still requires design. In this case: A parallel agent pattern runs independent work concurrently and combines the results.

### Question 24 — B

Answer: Use self-critique or reflection to improve drafts. Reflection adds a self-review step that revises the draft before delivery. Reflection can catch omissions and inconsistencies. It can also reinforce errors, so validate against evidence. Local study-map skill 2.6 (Multi-Agent Orchestration and Safeguards), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Handoffs should carry goal, evidence, permissions, and open questions. Implicit context is easily lost. Why the correct answer wins: Reflection adds a self-review step that revises the draft before delivery.
- **B:** Correct. Reflection can catch omissions and inconsistencies. It can also reinforce errors, so validate against evidence. In this case: Reflection adds a self-review step that revises the draft before delivery.
- **C:** Incorrect for this question. Parallel execution reduces wall-clock time for independent work. Reconciliation still requires design. Why the correct answer wins: Reflection adds a self-review step that revises the draft before delivery.
- **D:** Incorrect for this question. Sequential orchestration makes dependencies explicit. It may add latency where steps could run concurrently. Why the correct answer wins: Reflection adds a self-review step that revises the draft before delivery.

### Question 25 — D

Answer: Detect alert → inspect traces → isolate the failing step → apply fix → verify with regression evaluation. Triage moves from the alert to traces, then a targeted fix verified by regression evaluation. Triage moves from signal to evidence to a targeted fix, then proves the fix with regression tests. Local study-map skill 2.7 (Agent Monitoring and Error Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. A fix cannot precede detection and diagnosis. Why the correct answer wins: Triage moves from the alert to traces, then a targeted fix verified by regression evaluation.
- **B:** Incorrect for this question. Verification before a fix and before diagnosis proves nothing. Why the correct answer wins: Triage moves from the alert to traces, then a targeted fix verified by regression evaluation.
- **C:** Incorrect for this question. The alert must be detected first, and traces must be inspected before the step is isolated. Why the correct answer wins: Triage moves from the alert to traces, then a targeted fix verified by regression evaluation.
- **D:** Correct. Triage moves from signal to evidence to a targeted fix, then proves the fix with regression tests. In this case: Triage moves from the alert to traces, then a targeted fix verified by regression evaluation.

### Question 26 — B

Answer: Adjust top-p to control response diversity. Nucleus sampling controls diversity by limiting the cumulative probability considered. Top-p narrows or broadens token sampling. Tune with evaluation rather than by intuition. Local study-map skill 2.8 (Generation Tuning and Observability), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Coherence checks readability and internal consistency. It does not establish factual accuracy. Why the correct answer wins: Nucleus sampling controls diversity by limiting the cumulative probability considered.
- **B:** Correct. Top-p narrows or broadens token sampling. Tune with evaluation rather than by intuition. In this case: Nucleus sampling controls diversity by limiting the cumulative probability considered.
- **C:** Incorrect for this question. Relevance covers both retrieval and response usefulness. A correct but off-topic answer still fails. Why the correct answer wins: Nucleus sampling controls diversity by limiting the cumulative probability considered.
- **D:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Nucleus sampling controls diversity by limiting the cumulative probability considered.

### Question 27 — C

Answer: Use supported prompt or response caching where appropriate. Prompt caching reuses repeated prefix content instead of reprocessing it. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Local study-map skill 2.8 (Generation Tuning and Observability), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Citations let users verify claims and support auditing. Preserve source and chunk identifiers through the pipeline. Why the correct answer wins: Prompt caching reuses repeated prefix content instead of reprocessing it.
- **B:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Prompt caching reuses repeated prefix content instead of reprocessing it.
- **C:** Correct. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. In this case: Prompt caching reuses repeated prefix content instead of reprocessing it.
- **D:** Incorrect for this question. Central telemetry captures latency, errors, dependencies, and custom events. Redact sensitive content before logging. Why the correct answer wins: Prompt caching reuses repeated prefix content instead of reprocessing it.

### Question 28 — B

Answer: Apply prompt-driven image modifications. Targeted image editing changes the selected element and preserves the subject. Prompt-based edits can alter style or content. Review outputs for unintended changes and policy violations. Local study-map skill 3.1 (Image Generation and Editing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Inpainting changes a selected area while preserving the rest. Validate identity, brand, and safety constraints. Why the correct answer wins: Targeted image editing changes the selected element and preserves the subject.
- **B:** Correct. Prompt-based edits can alter style or content. Review outputs for unintended changes and policy violations. In this case: Targeted image editing changes the selected element and preserves the subject.
- **C:** Incorrect for this question. Video generation creates clips from prompts or images. Duration, consistency, and safety require review. Why the correct answer wins: Targeted image editing changes the selected element and preserves the subject.
- **D:** Incorrect for this question. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Why the correct answer wins: Targeted image editing changes the selected element and preserves the subject.

### Question 29 — C

Answer: Generate video from text or reference media. Video generation creates new footage from a description. Video generation creates clips from prompts or images. Duration, consistency, and safety require review. Local study-map skill 3.2 (Video Generation and Editing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Why the correct answer wins: Video generation creates new footage from a description.
- **B:** Incorrect for this question. Prompt-based edits can alter style or content. Review outputs for unintended changes and policy violations. Why the correct answer wins: Video generation creates new footage from a description.
- **C:** Correct. Video generation creates clips from prompts or images. Duration, consistency, and safety require review. In this case: Video generation creates new footage from a description.
- **D:** Incorrect for this question. Video editing can revise scenes or timing. Preserve provenance and review for harmful manipulation. Why the correct answer wins: Video generation creates new footage from a description.

### Question 30 — B

Answer: Edit generated video segments. Video editing changes existing generated segments and captions. Video editing can revise scenes or timing. Preserve provenance and review for harmful manipulation. Local study-map skill 3.2 (Video Generation and Editing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Prompt-based edits can alter style or content. Review outputs for unintended changes and policy violations. Why the correct answer wins: Video editing changes existing generated segments and captions.
- **B:** Correct. Video editing can revise scenes or timing. Preserve provenance and review for harmful manipulation. In this case: Video editing changes existing generated segments and captions.
- **C:** Incorrect for this question. Video analysis can summarize or detect events across time. Sampling strategy affects coverage and cost. Why the correct answer wins: Video editing changes existing generated segments and captions.
- **D:** Incorrect for this question. Inpainting changes a selected area while preserving the rest. Validate identity, brand, and safety constraints. Why the correct answer wins: Video editing changes existing generated segments and captions.

### Question 31 — B, D

Answers: Generate concise or detailed image captions; Generate alt text aligned to accessibility guidance. Captions describe content for search, and alt text serves assistive technology. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Alt text should convey purpose and essential content, not decorative detail. Human review is still needed for critical pages. Local study-map skill 3.3 (Multimodal Understanding and Accessibility), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Captions describe content for search, and alt text serves assistive technology.
- **B:** Correct. Alt text should convey purpose and essential content, not decorative detail. Human review is still needed for critical pages. In this case: Captions describe content for search, and alt text serves assistive technology.
- **C:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Captions describe content for search, and alt text serves assistive technology.
- **D:** Correct. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. In this case: Captions describe content for search, and alt text serves assistive technology.
- **E:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: Captions describe content for search, and alt text serves assistive technology.

### Question 32 — C

Answer: Use single-task mode for a focused extraction scenario. The single-task mode targets a focused extraction at lower cost than full pro mode. Single-task analyzers target one content type or objective. They may be simpler and cheaper than general pro-mode pipelines. Local study-map skill 3.4 (Visual Extraction and Video Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Document Intelligence provides prebuilt and custom extraction for structured documents. Validate field accuracy on representative samples. Why the correct answer wins: The single-task mode targets a focused extraction at lower cost than full pro mode.
- **B:** Incorrect for this question. Pro mode handles more demanding layouts and multimodal inputs at higher cost. Use it where simpler modes fail requirements. Why the correct answer wins: The single-task mode targets a focused extraction at lower cost than full pro mode.
- **C:** Correct. Single-task analyzers target one content type or objective. They may be simpler and cheaper than general pro-mode pipelines. In this case: The single-task mode targets a focused extraction at lower cost than full pro mode.
- **D:** Incorrect for this question. Custom models fit specialized forms not covered by prebuilts. They require representative labels and retraining discipline. Why the correct answer wins: The single-task mode targets a focused extraction at lower cost than full pro mode.

### Question 33 — B

Answer: Preserve document layout, tables, and reading order. Layout analysis preserves table cells and relationships that plain OCR flattens. Layout awareness improves extraction from forms and multi-column documents. Flattening to plain text can destroy meaning. Local study-map skill 3.4 (Visual Extraction and Video Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Markdown preserves headings, tables, and lists in a model-friendly form. Validate that critical values survive conversion. Why the correct answer wins: Layout analysis preserves table cells and relationships that plain OCR flattens.
- **B:** Correct. Layout awareness improves extraction from forms and multi-column documents. Flattening to plain text can destroy meaning. In this case: Layout analysis preserves table cells and relationships that plain OCR flattens.
- **C:** Incorrect for this question. Reading order affects comprehension and extraction. Incorrect order can invert meaning in contracts and forms. Why the correct answer wins: Layout analysis preserves table cells and relationships that plain OCR flattens.
- **D:** Incorrect for this question. OCR unlocks text in scans and screenshots. Layout and table structure may still require specialized extraction. Why the correct answer wins: Layout analysis preserves table cells and relationships that plain OCR flattens.

### Question 34 — C, D

Answers: Enforce brand and usage rules for generated visuals; Apply watermarks or provenance markers to generated media. Watermarking identifies synthetic media, and brand policy constrains approved visual usage. Brand controls define permitted logos, styles, and claims. Technical generation must still pass approval. Watermarks support disclosure and traceability. They do not replace usage policy or review. Local study-map skill 3.5 (Multimodal Responsible AI), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Watermarking identifies synthetic media, and brand policy constrains approved visual usage.
- **B:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Watermarking identifies synthetic media, and brand policy constrains approved visual usage.
- **C:** Correct. Watermarks support disclosure and traceability. They do not replace usage policy or review. In this case: Watermarking identifies synthetic media, and brand policy constrains approved visual usage.
- **D:** Correct. Brand controls define permitted logos, styles, and claims. Technical generation must still pass approval. In this case: Watermarking identifies synthetic media, and brand policy constrains approved visual usage.
- **E:** Incorrect for this question. Top-p narrows or broadens token sampling. Tune with evaluation rather than by intuition. Why the correct answer wins: Watermarking identifies synthetic media, and brand policy constrains approved visual usage.

### Question 35 — A

Answer: Generate summaries with explicit length and audience constraints. Summarization condenses long content into a shorter form. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Local study-map skill 4.1 (Language Model Text Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Correct. Summaries should preserve required facts and caveats. Fluency does not prove completeness. In this case: Summarization condenses long content into a shorter form.
- **B:** Incorrect for this question. Entity extraction turns text into structured facts. Ambiguous mentions need resolution and validation. Why the correct answer wins: Summarization condenses long content into a shorter form.
- **C:** Incorrect for this question. Translation should preserve meaning, names, and formatting. Evaluate domain terminology and low-resource languages. Why the correct answer wins: Summarization condenses long content into a shorter form.
- **D:** Incorrect for this question. Topic extraction supports discovery and grouping. It is not a substitute for an authoritative taxonomy. Why the correct answer wins: Summarization condenses long content into a shorter form.

### Question 36 — B, E

Answers: Analyze sentiment and tone with an appropriate service; Identify topics or key phrases for navigation. Topic detection tags subjects, and sentiment detects emotional escalation. Sentiment analysis can support triage and monitoring. Domain and language variation require validation. Topic extraction supports discovery and grouping. It is not a substitute for an authoritative taxonomy. Local study-map skill 4.1 (Language Model Text Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Why the correct answer wins: Topic detection tags subjects, and sentiment detects emotional escalation.
- **B:** Correct. Topic extraction supports discovery and grouping. It is not a substitute for an authoritative taxonomy. In this case: Topic detection tags subjects, and sentiment detects emotional escalation.
- **C:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Topic detection tags subjects, and sentiment detects emotional escalation.
- **D:** Incorrect for this question. Alt text should convey purpose and essential content, not decorative detail. Human review is still needed for critical pages. Why the correct answer wins: Topic detection tags subjects, and sentiment detects emotional escalation.
- **E:** Correct. Sentiment analysis can support triage and monitoring. Domain and language variation require validation. In this case: Topic detection tags subjects, and sentiment detects emotional escalation.

### Question 37 — C

Answer: Apply a custom glossary or terminology list. A glossary enforces approved term mappings across languages. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Local study-map skill 4.2 (Translation), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Translation should preserve meaning, names, and formatting. Evaluate domain terminology and low-resource languages. Why the correct answer wins: A glossary enforces approved term mappings across languages.
- **B:** Incorrect for this question. Sensitive Data Protection or language PII detection can identify and mask data. Verify that redaction covers every path where content flows. Why the correct answer wins: A glossary enforces approved term mappings across languages.
- **C:** Correct. Glossaries keep product and legal terms consistent. Terms still need human validation in context. In this case: A glossary enforces approved term mappings across languages.
- **D:** Incorrect for this question. Entity extraction turns text into structured facts. Ambiguous mentions need resolution and validation. Why the correct answer wins: A glossary enforces approved term mappings across languages.

### Question 38 — C

Answer: Capture audio → transcribe → translate text → synthesize speech → return audio. Speech translation transcribes, translates the text, then synthesizes the target-language reply. Speech translation transcribes first, translates the text, then synthesizes the target-language audio. Local study-map skill 4.3 (Speech Solutions), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Capture must come first, and synthesis must follow translation. Why the correct answer wins: Speech translation transcribes, translates the text, then synthesizes the target-language reply.
- **B:** Incorrect for this question. Audio must be captured before it can be transcribed or translated. Why the correct answer wins: Speech translation transcribes, translates the text, then synthesizes the target-language reply.
- **C:** Correct. Speech translation transcribes first, translates the text, then synthesizes the target-language audio. In this case: Speech translation transcribes, translates the text, then synthesizes the target-language reply.
- **D:** Incorrect for this question. Synthesis cannot precede transcription and translation. Why the correct answer wins: Speech translation transcribes, translates the text, then synthesizes the target-language reply.

### Question 39 — B

Answer: Customize summaries and extraction for compliance needs. Domain-specific compliance summarization enforces citation and disclosure requirements. Compliance work requires precise citation, retention, and review. Generic summarization is insufficient without controls. Local study-map skill 4.4 (Domain Customization), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Entity extraction turns text into structured facts. Ambiguous mentions need resolution and validation. Why the correct answer wins: Domain-specific compliance summarization enforces citation and disclosure requirements.
- **B:** Correct. Compliance work requires precise citation, retention, and review. Generic summarization is insufficient without controls. In this case: Domain-specific compliance summarization enforces citation and disclosure requirements.
- **C:** Incorrect for this question. Topic extraction supports discovery and grouping. It is not a substitute for an authoritative taxonomy. Why the correct answer wins: Domain-specific compliance summarization enforces citation and disclosure requirements.
- **D:** Incorrect for this question. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Why the correct answer wins: Domain-specific compliance summarization enforces citation and disclosure requirements.

### Question 40 — A

Answer: Propagate source deletions to indexes and caches. Deletion propagation removes withdrawn documents from the index. Removed content must stop appearing in answers. Test deletion propagation explicitly. Local study-map skill 5.1 (Content Ingestion and Indexing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Correct. Removed content must stop appearing in answers. Test deletion propagation explicitly. In this case: Deletion propagation removes withdrawn documents from the index.
- **B:** Incorrect for this question. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. Why the correct answer wins: Deletion propagation removes withdrawn documents from the index.
- **C:** Incorrect for this question. Push ingestion supports near-real-time updates from applications. The app owns batching, retries, and deletion. Why the correct answer wins: Deletion propagation removes withdrawn documents from the index.
- **D:** Incorrect for this question. Ingestion moves source content into a searchable index. Handle failures, updates, and deletions explicitly. Why the correct answer wins: Deletion propagation removes withdrawn documents from the index.

### Question 41 — A, B

Answers: Apply document-level security filters at query time; Combine keyword and vector retrieval. Document-level security filters enforce regional separation, and hybrid search covers exact and semantic queries. Filters restrict results to content the user may see. They must be enforced before content reaches the model. Hybrid search covers exact identifiers and paraphrased meaning together. Fusion and ranking need testing on representative queries. Local study-map skill 5.2 (Search and Grounding Configuration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Correct. Filters restrict results to content the user may see. They must be enforced before content reaches the model. In this case: Document-level security filters enforce regional separation, and hybrid search covers exact and semantic queries.
- **B:** Correct. Hybrid search covers exact identifiers and paraphrased meaning together. Fusion and ranking need testing on representative queries. In this case: Document-level security filters enforce regional separation, and hybrid search covers exact and semantic queries.
- **C:** Incorrect for this question. Stale content produces outdated answers. Define refresh expectations and test deletion behavior. Why the correct answer wins: Document-level security filters enforce regional separation, and hybrid search covers exact and semantic queries.
- **D:** Incorrect for this question. More retrieved text is not always better. Order and compress evidence to preserve decisive facts. Why the correct answer wins: Document-level security filters enforce regional separation, and hybrid search covers exact and semantic queries.
- **E:** Incorrect for this question. A semantic ranker can improve relevance for natural-language queries. It adds cost and latency and should be measured against a baseline. Why the correct answer wins: Document-level security filters enforce regional separation, and hybrid search covers exact and semantic queries.

### Question 42 — A

Answer: Add an enrichment skillset to an indexing pipeline. A skillset defines the enrichment steps that run during indexing. Skillsets can OCR, split, embed, and extract during indexing. Each skill adds latency, cost, and failure modes. Local study-map skill 5.3 (Enrichment Skills), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Correct. Skillsets can OCR, split, embed, and extract during indexing. Each skill adds latency, cost, and failure modes. In this case: A skillset defines the enrichment steps that run during indexing.
- **B:** Incorrect for this question. Push ingestion supports near-real-time updates from applications. The app owns batching, retries, and deletion. Why the correct answer wins: A skillset defines the enrichment steps that run during indexing.
- **C:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: A skillset defines the enrichment steps that run during indexing.
- **D:** Incorrect for this question. OCR unlocks text in scans and screenshots. Layout and table structure may still require specialized extraction. Why the correct answer wins: A skillset defines the enrichment steps that run during indexing.

### Question 43 — A

Answer: Ingest → extract text → chunk → embed → index → retrieve with citations. Extraction, chunking, embedding, and indexing all precede retrieval and citation. The supported RAG ingestion order produces searchable, citable evidence. Retrieval cannot work before content is extracted, chunked, embedded, and indexed. Local study-map skill 5.4 (RAG Ingestion and OCR), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Correct. The supported RAG ingestion order produces searchable, citable evidence. Retrieval cannot work before content is extracted, chunked, embedded, and indexed. In this case: Extraction, chunking, embedding, and indexing all precede retrieval and citation.
- **B:** Incorrect for this question. Retrieval is attempted before the index exists and source ingestion is incomplete. Why the correct answer wins: Extraction, chunking, embedding, and indexing all precede retrieval and citation.
- **C:** Incorrect for this question. Retrieval before chunking, embedding, and indexing has nothing searchable to return. Why the correct answer wins: Extraction, chunking, embedding, and indexing all precede retrieval and citation.
- **D:** Incorrect for this question. Indexing before extraction or embedding creates an empty or unusable index. Why the correct answer wins: Extraction, chunking, embedding, and indexing all precede retrieval and citation.

### Question 44 — D

Answer: Select evidence within the model's usable context. The context budget controls how much retrieved evidence is placed in the prompt. More retrieved text is not always better. Order and compress evidence to preserve decisive facts. Local study-map skill 5.5 (Retrieval Integration with Agents), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. De-duplication frees context space that duplicates would otherwise consume, so the most informative evidence survives the budget. Why the correct answer wins: The context budget controls how much retrieved evidence is placed in the prompt.
- **B:** Incorrect for this question. Embeddings support similarity search over meaning rather than exact terms. Vector search still needs chunking, filtering, and evaluation. Why the correct answer wins: The context budget controls how much retrieved evidence is placed in the prompt.
- **C:** Incorrect for this question. Reranking improves precision after broad recall. It adds latency and must be evaluated. Why the correct answer wins: The context budget controls how much retrieved evidence is placed in the prompt.
- **D:** Correct. More retrieved text is not always better. Order and compress evidence to preserve decisive facts. In this case: The context budget controls how much retrieved evidence is placed in the prompt.

### Question 45 — D

Answer: Pin the model version available in the required region. Pinning a version offered in that region satisfies residency and stability together. A pinned version keeps behavior stable and satisfies residency, at the cost of slower access to newer capabilities. Local study-map skill 1.1 (Selecting Foundry Models and Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. A custom model is justified when supported prebuilt options cannot meet a defined requirement. It adds data, evaluation, and lifecycle obligations. Why the correct answer wins: Pinning a version offered in that region satisfies residency and stability together.
- **B:** Incorrect for this question. The catalog shows supported models with capability, modality, region, and lifecycle details. Verify availability for your subscription and region before designing around one model. Why the correct answer wins: Pinning a version offered in that region satisfies residency and stability together.
- **C:** Incorrect for this question. Large models handle ambiguity and multi-step reasoning better in many cases, at higher cost and latency. Select with measured evidence rather than brand preference. Why the correct answer wins: Pinning a version offered in that region satisfies residency and stability together.
- **D:** Correct. A pinned version keeps behavior stable and satisfies residency, at the cost of slower access to newer capabilities. In this case: Pinning a version offered in that region satisfies residency and stability together.

### Question 46 — C

Answer: Use Foundry Tools for prebuilt vision, speech, language, and extraction needs. Prebuilt managed capabilities avoid a training dataset. Prebuilt managed capabilities can reduce custom model work where their behavior and limits fit the task. They are not a substitute for task-specific validation. Local study-map skill 1.1 (Selecting Foundry Models and Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. A custom model is justified when supported prebuilt options cannot meet a defined requirement. It adds data, evaluation, and lifecycle obligations. Why the correct answer wins: Prebuilt managed capabilities avoid a training dataset.
- **B:** Incorrect for this question. Large models handle ambiguity and multi-step reasoning better in many cases, at higher cost and latency. Select with measured evidence rather than brand preference. Why the correct answer wins: Prebuilt managed capabilities avoid a training dataset.
- **C:** Correct. Prebuilt managed capabilities can reduce custom model work where their behavior and limits fit the task. They are not a substitute for task-specific validation. In this case: Prebuilt managed capabilities avoid a training dataset.
- **D:** Incorrect for this question. Small models can reduce latency and cost for constrained classification or extraction. Confirm quality on representative data before standardizing. Why the correct answer wins: Prebuilt managed capabilities avoid a training dataset.

### Question 47 — A

Answer: Expose an OpenAPI operation as an agent tool. An OpenAPI tool reuses the published contract. OpenAPI tools describe supported HTTP operations for agent use. Narrow operations, validate inputs, and authenticate the caller. Local study-map skill 1.2 (Retrieval, Memory, Tool, and Knowledge Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. OpenAPI tools describe supported HTTP operations for agent use. Narrow operations, validate inputs, and authenticate the caller. In this case: An OpenAPI tool reuses the published contract.
- **B:** Incorrect for this question. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Why the correct answer wins: An OpenAPI tool reuses the published contract.
- **C:** Incorrect for this question. An index gives an agent curated, searchable evidence under configured access. Index content and permissions require ongoing ownership. Why the correct answer wins: An OpenAPI tool reuses the published contract.
- **D:** Incorrect for this question. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. Why the correct answer wins: An OpenAPI tool reuses the published contract.

### Question 48 — A

Answer: Block promotion in the pipeline when evaluation thresholds fail. An evaluation gate blocks promotion on a measured threshold. An automated gate turns an evaluation result into a release decision. Thresholds need ownership or the gate becomes noise. Local study-map skill 1.3 (Infrastructure, Deployment, and CI/CD), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. An automated gate turns an evaluation result into a release decision. Thresholds need ownership or the gate becomes noise. In this case: An evaluation gate blocks promotion on a measured threshold.
- **B:** Incorrect for this question. Canary or phased rollout limits exposure. Rollback must be tested, not just documented. Why the correct answer wins: An evaluation gate blocks promotion on a measured threshold.
- **C:** Incorrect for this question. A canary limits blast radius and produces real signal before full rollout. It needs a rollback criterion defined in advance. Why the correct answer wins: An evaluation gate blocks promotion on a measured threshold.
- **D:** Incorrect for this question. Repeatable deployments reduce configuration drift. Include model deployments, indexes, and connections in review and promotion. Why the correct answer wins: An evaluation gate blocks promotion on a measured threshold.

### Question 49 — B

Answer: Send mirrored production traffic to a candidate without returning its answers. Shadow deployment mirrors traffic and discards candidate output. Shadow traffic compares a candidate against live behavior with no user impact. It requires careful handling of side-effecting calls. Local study-map skill 1.3 (Infrastructure, Deployment, and CI/CD), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Standard deployments bill per token and scale within quota. They suit spiky or early workloads. Why the correct answer wins: Shadow deployment mirrors traffic and discards candidate output.
- **B:** Correct. Shadow traffic compares a candidate against live behavior with no user impact. It requires careful handling of side-effecting calls. In this case: Shadow deployment mirrors traffic and discards candidate output.
- **C:** Incorrect for this question. A canary limits blast radius and produces real signal before full rollout. It needs a rollback criterion defined in advance. Why the correct answer wins: Shadow deployment mirrors traffic and discards candidate output.
- **D:** Incorrect for this question. Batch deployments can lower cost for large asynchronous jobs. They are unsuitable for interactive agent turns. Why the correct answer wins: Shadow deployment mirrors traffic and discards candidate output.

### Question 50 — B

Answer: Alert on spend thresholds per deployment or project. A spend alert notifies owners as usage crosses a threshold. Spend alerts catch runaway usage before the invoice does. They are detection, not a hard spending cap. Local study-map skill 1.4 (Quotas, Scaling, and Cost), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Retries, tool calls, evaluation, and review contribute to unit economics. Per-outcome cost supports better optimization. Why the correct answer wins: A spend alert notifies owners as usage crosses a threshold.
- **B:** Correct. Spend alerts catch runaway usage before the invoice does. They are detection, not a hard spending cap. In this case: A spend alert notifies owners as usage crosses a threshold.
- **C:** Incorrect for this question. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. Why the correct answer wins: A spend alert notifies owners as usage crosses a threshold.
- **D:** Incorrect for this question. Token analytics supports cost and performance tuning. Attribute usage to features and tenants where possible. Why the correct answer wins: A spend alert notifies owners as usage crosses a threshold.

### Question 51 — A

Answer: Monitor index freshness, failures, and document counts. Index health checks catch stale content. Stale or partially indexed content produces confident but wrong answers. Alert on ingestion and deletion failures. Local study-map skill 1.5 (Monitoring Performance, Drift, Safety, and Grounding), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. Stale or partially indexed content produces confident but wrong answers. Alert on ingestion and deletion failures. In this case: Index health checks catch stale content.
- **B:** Incorrect for this question. User behavior, data, and models change. Rolling baselines reveal degradation that a one-time evaluation misses. Why the correct answer wins: Index health checks catch stale content.
- **C:** Incorrect for this question. Groundedness checks whether claims are supported by retrieved evidence. Sampling and human review complement automated scores. Why the correct answer wins: Index health checks catch stale content.
- **D:** Incorrect for this question. Central telemetry captures latency, errors, dependencies, and custom events. Redact sensitive content before logging. Why the correct answer wins: Index health checks catch stale content.

### Question 52 — D

Answer: Restrict outbound network access to approved destinations. Egress rules restrict which external destinations the workload can reach, which is exactly the control the policy demands. Egress controls reduce exfiltration and unauthorized tool reach. Combine with identity and data controls. Local study-map skill 1.6 (Security, Identity, and Networking), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Leaving the public path open defeats the purpose of a private networking design because traffic can still bypass the private route. Why the correct answer wins: Egress rules restrict which external destinations the workload can reach, which is exactly the control the policy demands.
- **B:** Incorrect for this question. Private connectivity keeps service traffic on approved network paths. Pair it with private DNS so clients resolve the private address. Why the correct answer wins: Egress rules restrict which external destinations the workload can reach, which is exactly the control the policy demands.
- **C:** Incorrect for this question. Roles should match the operations the app or agent performs. Broad contributor access increases blast radius. Why the correct answer wins: Egress rules restrict which external destinations the workload can reach, which is exactly the control the policy demands.
- **D:** Correct. Egress controls reduce exfiltration and unauthorized tool reach. Combine with identity and data controls. In this case: Egress rules restrict which external destinations the workload can reach, which is exactly the control the policy demands.

### Question 53 — A

Answer: Set agent oversight mode and tool-access constraints. Human oversight keeps consequential decisions attributable. Oversight settings bound what an agent may do autonomously. They should be tested against realistic misuse and failure. Local study-map skill 1.7 (Responsible AI Controls and Oversight), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. Oversight settings bound what an agent may do autonomously. They should be tested against realistic misuse and failure. In this case: Human oversight keeps consequential decisions attributable.
- **B:** Incorrect for this question. Audit evidence supports investigation and accountability. Protect log integrity and retention. Why the correct answer wins: Human oversight keeps consequential decisions attributable.
- **C:** Incorrect for this question. Approval must occur before the effect and identify who approved what. A model confidence score is not approval. Why the correct answer wins: Human oversight keeps consequential decisions attributable.
- **D:** Incorrect for this question. Guardrails are technical controls, not prompt suggestions. Validate inputs, authorize tools, and limit egress. Why the correct answer wins: Human oversight keeps consequential decisions attributable.

### Question 54 — C

Answer: Use batch processing for latency-tolerant bulk work. Batch deployment suits large asynchronous jobs. Batch deployments can lower cost for large asynchronous jobs. They are unsuitable for interactive agent turns. Local study-map skill 1.4 (Quotas, Scaling, and Cost), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Standard deployments bill per token and scale within quota. They suit spiky or early workloads. Why the correct answer wins: Batch deployment suits large asynchronous jobs.
- **B:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: Batch deployment suits large asynchronous jobs.
- **C:** Correct. Batch deployments can lower cost for large asynchronous jobs. They are unsuitable for interactive agent turns. In this case: Batch deployment suits large asynchronous jobs.
- **D:** Incorrect for this question. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. Why the correct answer wins: Batch deployment suits large asynchronous jobs.

### Question 55 — D, E

Answers: Compare supported models in the Foundry model catalog; Pin the model version available in the required region. Catalog review confirms availability, and pinning keeps behaviour stable. The catalog shows supported models with capability, modality, region, and lifecycle details. Verify availability for your subscription and region before designing around one model. A pinned version keeps behavior stable and satisfies residency, at the cost of slower access to newer capabilities. Local study-map skill 1.1 (Selecting Foundry Models and Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Standard deployments bill per token and scale within quota. They suit spiky or early workloads. Why the correct answer wins: Catalog review confirms availability, and pinning keeps behaviour stable.
- **B:** Incorrect for this question. Batch deployments can lower cost for large asynchronous jobs. They are unsuitable for interactive agent turns. Why the correct answer wins: Catalog review confirms availability, and pinning keeps behaviour stable.
- **C:** Incorrect for this question. A custom model is justified when supported prebuilt options cannot meet a defined requirement. It adds data, evaluation, and lifecycle obligations. Why the correct answer wins: Catalog review confirms availability, and pinning keeps behaviour stable.
- **D:** Correct. The catalog shows supported models with capability, modality, region, and lifecycle details. Verify availability for your subscription and region before designing around one model. In this case: Catalog review confirms availability, and pinning keeps behaviour stable.
- **E:** Correct. A pinned version keeps behavior stable and satisfies residency, at the cost of slower access to newer capabilities. In this case: Catalog review confirms availability, and pinning keeps behaviour stable.

### Question 56 — A, E

Answers: Monitor groundedness and citation quality in production; Alert on latency, error rate, safety, and cost thresholds. Groundedness monitoring detects unsupported answers, and alerting notifies owners. Groundedness checks whether claims are supported by retrieved evidence. Sampling and human review complement automated scores. Alerts turn monitoring into action. Route them to an accountable owner with a runbook. Local study-map skill 1.5 (Monitoring Performance, Drift, Safety, and Grounding), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. Groundedness checks whether claims are supported by retrieved evidence. Sampling and human review complement automated scores. In this case: Groundedness monitoring detects unsupported answers, and alerting notifies owners.
- **B:** Incorrect for this question. Retries, tool calls, evaluation, and review contribute to unit economics. Per-outcome cost supports better optimization. Why the correct answer wins: Groundedness monitoring detects unsupported answers, and alerting notifies owners.
- **C:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Groundedness monitoring detects unsupported answers, and alerting notifies owners.
- **D:** Incorrect for this question. Users experience the whole path, not only generation. Optimize the dominant contributor. Why the correct answer wins: Groundedness monitoring detects unsupported answers, and alerting notifies owners.
- **E:** Correct. Alerts turn monitoring into action. Route them to an accountable owner with a runbook. In this case: Groundedness monitoring detects unsupported answers, and alerting notifies owners.

### Question 57 — C, E

Answers: Restrict outbound network access to approved destinations; Use least-privilege Azure RBAC roles for the workload identity. Egress restrictions bound destinations, and least privilege bounds actions. Egress controls reduce exfiltration and unauthorized tool reach. Combine with identity and data controls. Roles should match the operations the app or agent performs. Broad contributor access increases blast radius. Local study-map skill 1.6 (Security, Identity, and Networking), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Private connectivity keeps service traffic on approved network paths. Pair it with private DNS so clients resolve the private address. Why the correct answer wins: Egress restrictions bound destinations, and least privilege bounds actions.
- **B:** Incorrect for this question. A managed secret store supports rotation and access control. Secrets should never appear in prompts, code, or logs. Why the correct answer wins: Egress restrictions bound destinations, and least privilege bounds actions.
- **C:** Correct. Roles should match the operations the app or agent performs. Broad contributor access increases blast radius. In this case: Egress restrictions bound destinations, and least privilege bounds actions.
- **D:** Incorrect for this question. Filters assign severity and can block or annotate content. Thresholds should reflect the use case and applicable policy. Why the correct answer wins: Egress restrictions bound destinations, and least privilege bounds actions.
- **E:** Correct. Egress controls reduce exfiltration and unauthorized tool reach. Combine with identity and data controls. In this case: Egress restrictions bound destinations, and least privilege bounds actions.

### Question 58 — C

Answer: Commit change → run the evaluation suite → block on failed thresholds → deploy a canary → promote after metrics hold. Evaluation runs before deployment, its thresholds gate promotion, and a canary limits exposure before full release. An evaluation gate before deployment, followed by a canary, keeps unmeasured changes away from all users. Local study-map skill 1.3 (Infrastructure, Deployment, and CI/CD), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Deployment cannot precede the change, and evaluation must gate promotion rather than follow it. Why the correct answer wins: Evaluation runs before deployment, its thresholds gate promotion, and a canary limits exposure before full release.
- **B:** Incorrect for this question. The change must exist before it can be evaluated or deployed. Why the correct answer wins: Evaluation runs before deployment, its thresholds gate promotion, and a canary limits exposure before full release.
- **C:** Correct. An evaluation gate before deployment, followed by a canary, keeps unmeasured changes away from all users. In this case: Evaluation runs before deployment, its thresholds gate promotion, and a canary limits exposure before full release.
- **D:** Incorrect for this question. Evaluation after promotion cannot prevent a failed change from reaching everyone. Why the correct answer wins: Evaluation runs before deployment, its thresholds gate promotion, and a canary limits exposure before full release.

### Question 59 — A

Answer: Set chunk overlap so facts spanning a boundary stay retrievable. Overlap preserves facts across chunk boundaries. Overlap preserves context across chunk edges at the cost of duplicated index storage and more near-duplicate hits. Local study-map skill 2.1 (Building Generative Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Overlap preserves context across chunk edges at the cost of duplicated index storage and more near-duplicate hits. In this case: Overlap preserves facts across chunk boundaries.
- **B:** Incorrect for this question. Embeddings determine semantic similarity behavior. Evaluate retrieval quality before and after changes. Why the correct answer wins: Overlap preserves facts across chunk boundaries.
- **C:** Incorrect for this question. More retrieved text is not always better. Order and compress evidence to preserve decisive facts. Why the correct answer wins: Overlap preserves facts across chunk boundaries.
- **D:** Incorrect for this question. Chunking affects recall, precision, and context use. Respect document structure and test against real questions. Why the correct answer wins: Overlap preserves facts across chunk boundaries.

### Question 60 — A

Answer: Ground responses with retrieval-augmented generation. Retrieval supplies current evidence with citations. RAG supplies selected source content at request time so answers can cite current evidence. It reduces but does not eliminate fabrication. Local study-map skill 2.1 (Building Generative Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. RAG supplies selected source content at request time so answers can cite current evidence. It reduces but does not eliminate fabrication. In this case: Retrieval supplies current evidence with citations.
- **B:** Incorrect for this question. Checkpoints validate intermediate results before later steps depend on them. This limits error propagation. Why the correct answer wins: Retrieval supplies current evidence with citations.
- **C:** Incorrect for this question. Routing can balance quality and cost. Fallback and evaluation are required. Why the correct answer wins: Retrieval supplies current evidence with citations.
- **D:** Incorrect for this question. Examples clarify format and boundaries. They do not guarantee correctness on unseen inputs. Why the correct answer wins: Retrieval supplies current evidence with citations.

### Question 61 — D

Answer: Use short-lived scoped access tokens for tool calls. A scoped access token avoids long-lived secrets. Short-lived credentials reduce misuse risk. Never place tokens in prompts or logs. Local study-map skill 2.2 (Foundry SDK and Project Integration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. SDKs provide supported request and response patterns. Pin versions and handle retries, timeouts, and errors explicitly. Why the correct answer wins: A scoped access token avoids long-lived secrets.
- **B:** Incorrect for this question. Managed identities avoid embedded secrets and support role-based access. Assign only required data-plane roles. Why the correct answer wins: A scoped access token avoids long-lived secrets.
- **C:** Incorrect for this question. A managed secret store supports rotation and access control. Secrets should never appear in prompts, code, or logs. Why the correct answer wins: A scoped access token avoids long-lived secrets.
- **D:** Correct. Short-lived credentials reduce misuse risk. Never place tokens in prompts or logs. In this case: A scoped access token avoids long-lived secrets.

### Question 62 — B

Answer: Build a representative golden dataset from real tasks. A golden dataset fixes the inputs. A golden set anchors evaluation in expected behavior. Include edge cases and high-risk scenarios. Local study-map skill 2.3 (Evaluating Models and Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Prompts, models, indexes, and tools all affect behavior. Regression tests catch unintended effects. Why the correct answer wins: A golden dataset fixes the inputs.
- **B:** Correct. A golden set anchors evaluation in expected behavior. Include edge cases and high-risk scenarios. In this case: A golden dataset fixes the inputs.
- **C:** Incorrect for this question. Controlled comparison supports evidence-based change. Avoid changing several variables at once. Why the correct answer wins: A golden dataset fixes the inputs.
- **D:** Incorrect for this question. Evaluators provide repeatable signals across models and prompts. They must be calibrated against human judgment for high-impact work. Why the correct answer wins: A golden dataset fixes the inputs.

### Question 63 — B

Answer: Re-run evaluation suites after meaningful changes. Regression evaluation re-runs previously failing cases against the candidate, so a fixed defect cannot silently return. Prompts, models, indexes, and tools all affect behavior. Regression tests catch unintended effects. Local study-map skill 2.3 (Evaluating Models and Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Evaluators provide repeatable signals across models and prompts. They must be calibrated against human judgment for high-impact work. Why the correct answer wins: Regression evaluation re-runs previously failing cases against the candidate, so a fixed defect cannot silently return.
- **B:** Correct. Prompts, models, indexes, and tools all affect behavior. Regression tests catch unintended effects. In this case: Regression evaluation re-runs previously failing cases against the candidate, so a fixed defect cannot silently return.
- **C:** Incorrect for this question. Safety evaluation complements content filters. Use representative adversarial inputs. Why the correct answer wins: Regression evaluation re-runs previously failing cases against the candidate, so a fixed defect cannot silently return.
- **D:** Incorrect for this question. A golden set anchors evaluation in expected behavior. Include edge cases and high-risk scenarios. Why the correct answer wins: Regression evaluation re-runs previously failing cases against the candidate, so a fixed defect cannot silently return.

### Question 64 — A

Answer: Define narrow tool schemas with clear descriptions. A typed schema constrains the arguments. Precise schemas help the model choose tools and arguments correctly. Broad or ambiguous tools invite unsafe calls. Local study-map skill 2.4 (Agent Roles, Goals, and Tool Schemas), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Precise schemas help the model choose tools and arguments correctly. Broad or ambiguous tools invite unsafe calls. In this case: A typed schema constrains the arguments.
- **B:** Incorrect for this question. System messages define role and constraints. They are not a security boundary against injection. Why the correct answer wins: A typed schema constrains the arguments.
- **C:** Incorrect for this question. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Why the correct answer wins: A typed schema constrains the arguments.
- **D:** Incorrect for this question. Routing can balance quality and cost. Fallback and evaluation are required. Why the correct answer wins: A typed schema constrains the arguments.

### Question 65 — D

Answer: Transfer control between agents with explicit context. Handoff moves control and context to the specialist. Handoffs should carry goal, evidence, permissions, and open questions. Implicit context is easily lost. Local study-map skill 2.6 (Multi-Agent Orchestration and Safeguards), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Reflection can catch omissions and inconsistencies. It can also reinforce errors, so validate against evidence. Why the correct answer wins: Handoff moves control and context to the specialist.
- **B:** Incorrect for this question. Parallel execution reduces wall-clock time for independent work. Reconciliation still requires design. Why the correct answer wins: Handoff moves control and context to the specialist.
- **C:** Incorrect for this question. A manager routes tasks and merges results. Clear responsibility and failure handling are required. Why the correct answer wins: Handoff moves control and context to the specialist.
- **D:** Correct. Handoffs should carry goal, evidence, permissions, and open questions. Implicit context is easily lost. In this case: Handoff moves control and context to the specialist.

### Question 66 — B

Answer: Run independent agents concurrently. Parallel execution runs the independent checks at the same time, which is what makes the latency target achievable. Parallel execution reduces wall-clock time for independent work. Reconciliation still requires design. Local study-map skill 2.6 (Multi-Agent Orchestration and Safeguards), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Sequential orchestration makes dependencies explicit. It may add latency where steps could run concurrently. Why the correct answer wins: Parallel execution runs the independent checks at the same time, which is what makes the latency target achievable.
- **B:** Correct. Parallel execution reduces wall-clock time for independent work. Reconciliation still requires design. In this case: Parallel execution runs the independent checks at the same time, which is what makes the latency target achievable.
- **C:** Incorrect for this question. A manager routes tasks and merges results. Clear responsibility and failure handling are required. Why the correct answer wins: Parallel execution runs the independent checks at the same time, which is what makes the latency target achievable.
- **D:** Incorrect for this question. Reflection can catch omissions and inconsistencies. It can also reinforce errors, so validate against evidence. Why the correct answer wins: Parallel execution runs the independent checks at the same time, which is what makes the latency target achievable.

### Question 67 — A

Answer: Set a stop sequence so generation ends at the intended boundary. A stop sequence ends generation at the boundary. A stop sequence truncates output at a defined marker, which keeps parsers from receiving trailing commentary. It must not appear inside legitimate content. Local study-map skill 2.8 (Generation Tuning and Observability), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. A stop sequence truncates output at a defined marker, which keeps parsers from receiving trailing commentary. It must not appear inside legitimate content. In this case: A stop sequence ends generation at the boundary.
- **B:** Incorrect for this question. Top-p narrows or broadens token sampling. Tune with evaluation rather than by intuition. Why the correct answer wins: A stop sequence ends generation at the boundary.
- **C:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: A stop sequence ends generation at the boundary.
- **D:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: A stop sequence ends generation at the boundary.

### Question 68 — A

Answer: Adjust top-p to control response diversity. Nucleus sampling widens the candidate set. Top-p narrows or broadens token sampling. Tune with evaluation rather than by intuition. Local study-map skill 2.8 (Generation Tuning and Observability), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Top-p narrows or broadens token sampling. Tune with evaluation rather than by intuition. In this case: Nucleus sampling widens the candidate set.
- **B:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Nucleus sampling widens the candidate set.
- **C:** Incorrect for this question. A seed makes repeated sampling closer to reproducible, but it remains best effort and does not replace deterministic extraction settings. Why the correct answer wins: Nucleus sampling widens the candidate set.
- **D:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Nucleus sampling widens the candidate set.

### Question 69 — D, E

Answers: Use a Foundry SDK or supported connector from application code; Authenticate with a managed identity instead of keys. A supported SDK handles retries, and a managed identity removes stored secrets. SDKs provide supported request and response patterns. Pin versions and handle retries, timeouts, and errors explicitly. Managed identities avoid embedded secrets and support role-based access. Assign only required data-plane roles. Local study-map skill 2.2 (Foundry SDK and Project Integration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Manual portal changes work for exploration but are slow, undocumented, and hard to reproduce, so they are a poor fit for governed release processes. Why the correct answer wins: A supported SDK handles retries, and a managed identity removes stored secrets.
- **B:** Incorrect for this question. A managed secret store supports rotation and access control. Secrets should never appear in prompts, code, or logs. Why the correct answer wins: A supported SDK handles retries, and a managed identity removes stored secrets.
- **C:** Incorrect for this question. Short-lived credentials reduce misuse risk. Never place tokens in prompts or logs. Why the correct answer wins: A supported SDK handles retries, and a managed identity removes stored secrets.
- **D:** Correct. SDKs provide supported request and response patterns. Pin versions and handle retries, timeouts, and errors explicitly. In this case: A supported SDK handles retries, and a managed identity removes stored secrets.
- **E:** Correct. Managed identities avoid embedded secrets and support role-based access. Assign only required data-plane roles. In this case: A supported SDK handles retries, and a managed identity removes stored secrets.

### Question 70 — C, D

Answers: Use evaluators for quality, safety, and groundedness; Evaluate harmful, biased, or policy-violating output. Quality evaluation scores correctness, and safety evaluation screens prohibited advice. Evaluators provide repeatable signals across models and prompts. They must be calibrated against human judgment for high-impact work. Safety evaluation complements content filters. Use representative adversarial inputs. Local study-map skill 2.3 (Evaluating Models and Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Prompts, models, indexes, and tools all affect behavior. Regression tests catch unintended effects. Why the correct answer wins: Quality evaluation scores correctness, and safety evaluation screens prohibited advice.
- **B:** Incorrect for this question. Controlled comparison supports evidence-based change. Avoid changing several variables at once. Why the correct answer wins: Quality evaluation scores correctness, and safety evaluation screens prohibited advice.
- **C:** Correct. Safety evaluation complements content filters. Use representative adversarial inputs. In this case: Quality evaluation scores correctness, and safety evaluation screens prohibited advice.
- **D:** Correct. Evaluators provide repeatable signals across models and prompts. They must be calibrated against human judgment for high-impact work. In this case: Quality evaluation scores correctness, and safety evaluation screens prohibited advice.
- **E:** Incorrect for this question. A golden set anchors evaluation in expected behavior. Include edge cases and high-risk scenarios. Why the correct answer wins: Quality evaluation scores correctness, and safety evaluation screens prohibited advice.

### Question 71 — D, E

Answers: Give the agent a file-search tool over approved document stores; Enable a sandboxed code interpreter tool for calculations. File search supplies approved evidence, and an interpreter performs arithmetic. A file tool retrieves from curated stores under configured access. It still depends on indexing quality and permission filters. Code execution handles quantitative work the model cannot do reliably in text. The sandbox must be isolated and output must be validated. Local study-map skill 2.5 (Agent Tools, Retrieval, Memory, and Function Calling), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Why the correct answer wins: File search supplies approved evidence, and an interpreter performs arithmetic.
- **B:** Incorrect for this question. Routing can balance quality and cost. Fallback and evaluation are required. Why the correct answer wins: File search supplies approved evidence, and an interpreter performs arithmetic.
- **C:** Incorrect for this question. OpenAPI tools describe supported HTTP operations for agent use. Narrow operations, validate inputs, and authenticate the caller. Why the correct answer wins: File search supplies approved evidence, and an interpreter performs arithmetic.
- **D:** Correct. A file tool retrieves from curated stores under configured access. It still depends on indexing quality and permission filters. In this case: File search supplies approved evidence, and an interpreter performs arithmetic.
- **E:** Correct. Code execution handles quantitative work the model cannot do reliably in text. The sandbox must be isolated and output must be validated. In this case: File search supplies approved evidence, and an interpreter performs arithmetic.

### Question 72 — B

Answer: Define role and goal → configure tools → attach knowledge → evaluate in sandbox → deploy with monitoring. Role, tools, evaluation, then deployment with monitoring. An agent is defined before it is connected to tools and knowledge, and evaluation precedes deployment. Local study-map skill 2.6 (Multi-Agent Orchestration and Safeguards), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. The agent must be defined first, and evaluation must precede deployment. Why the correct answer wins: Role, tools, evaluation, then deployment with monitoring.
- **B:** Correct. An agent is defined before it is connected to tools and knowledge, and evaluation precedes deployment. In this case: Role, tools, evaluation, then deployment with monitoring.
- **C:** Incorrect for this question. Deployment before the agent is defined, connected, or evaluated removes every control. Why the correct answer wins: Role, tools, evaluation, then deployment with monitoring.
- **D:** Incorrect for this question. Tools configured before the role exists, and evaluation after deployment gates nothing. Why the correct answer wins: Role, tools, evaluation, then deployment with monitoring.

### Question 73 — B

Answer: Queue flagged generations for human moderation before release. Human moderation before publication catches contextual problems. Human moderation catches context that automated filters miss, at the cost of latency and reviewer load. Local study-map skill 3.1 (Image Generation and Editing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Human moderation before publication catches contextual problems.
- **B:** Correct. Human moderation catches context that automated filters miss, at the cost of latency and reviewer load. In this case: Human moderation before publication catches contextual problems.
- **C:** Incorrect for this question. Brand controls define permitted logos, styles, and claims. Technical generation must still pass approval. Why the correct answer wins: Human moderation before publication catches contextual problems.
- **D:** Incorrect for this question. Image and video safety filters reduce exposure to harmful content. Thresholds and human escalation should match policy. Why the correct answer wins: Human moderation before publication catches contextual problems.

### Question 74 — C

Answer: Generate a set of descriptive tags for each image. Generated tags make the library filterable and searchable, which is what the editors asked for. Tags support filtering and search across large image libraries. Tag vocabulary should be governed so synonyms do not fragment results. Local study-map skill 3.3 (Multimodal Understanding and Accessibility), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Visual question answering should cite the relevant region or content. Avoid answering beyond what the image supports. Why the correct answer wins: Generated tags make the library filterable and searchable, which is what the editors asked for.
- **B:** Incorrect for this question. Alt text should convey purpose and essential content, not decorative detail. Human review is still needed for critical pages. Why the correct answer wins: Generated tags make the library filterable and searchable, which is what the editors asked for.
- **C:** Correct. Tags support filtering and search across large image libraries. Tag vocabulary should be governed so synonyms do not fragment results. In this case: Generated tags make the library filterable and searchable, which is what the editors asked for.
- **D:** Incorrect for this question. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Why the correct answer wins: Generated tags make the library filterable and searchable, which is what the editors asked for.

### Question 75 — C

Answer: Preserve reading order across columns and sections. Reading-order analysis restores the intended sequence. Reading order affects comprehension and extraction. Incorrect order can invert meaning in contracts and forms. Local study-map skill 3.4 (Visual Extraction and Video Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Layout awareness improves extraction from forms and multi-column documents. Flattening to plain text can destroy meaning. Why the correct answer wins: Reading-order analysis restores the intended sequence.
- **B:** Incorrect for this question. OCR unlocks text in scans and screenshots. Layout and table structure may still require specialized extraction. Why the correct answer wins: Reading-order analysis restores the intended sequence.
- **C:** Correct. Reading order affects comprehension and extraction. Incorrect order can invert meaning in contracts and forms. In this case: Reading-order analysis restores the intended sequence.
- **D:** Incorrect for this question. Markdown preserves headings, tables, and lists in a model-friendly form. Validate that critical values survive conversion. Why the correct answer wins: Reading-order analysis restores the intended sequence.

### Question 76 — B

Answer: Use Azure Content Understanding analyzers in Foundry Tools. Content Understanding analyzers are configured per content type. Content Understanding extracts structure and fields from documents, images, audio, and video. Analyzer design and validation determine quality. Local study-map skill 3.4 (Visual Extraction and Video Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Analyzers define what to extract and how to return it. Version and test them like application code. Why the correct answer wins: Content Understanding analyzers are configured per content type.
- **B:** Correct. Content Understanding extracts structure and fields from documents, images, audio, and video. Analyzer design and validation determine quality. In this case: Content Understanding analyzers are configured per content type.
- **C:** Incorrect for this question. Document Intelligence provides prebuilt and custom extraction for structured documents. Validate field accuracy on representative samples. Why the correct answer wins: Content Understanding analyzers are configured per content type.
- **D:** Incorrect for this question. Prebuilt models cover invoices, receipts, IDs, and similar formats. Check supported locales and field coverage. Why the correct answer wins: Content Understanding analyzers are configured per content type.

### Question 77 — C, E

Answers: Use pro mode for complex multimodal content understanding; Return markdown for retrieval and reasoning pipelines. Pro mode handles complex packets, and markdown suits downstream reasoning. Pro mode handles more demanding layouts and multimodal inputs at higher cost. Use it where simpler modes fail requirements. Markdown preserves structure and is easy for models to consume. Validate tables and key values. Local study-map skill 3.4 (Visual Extraction and Video Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Detection returns locations and labels for visual elements. Validate classes and thresholds against the use case. Why the correct answer wins: Pro mode handles complex packets, and markdown suits downstream reasoning.
- **B:** Incorrect for this question. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Why the correct answer wins: Pro mode handles complex packets, and markdown suits downstream reasoning.
- **C:** Correct. Pro mode handles more demanding layouts and multimodal inputs at higher cost. Use it where simpler modes fail requirements. In this case: Pro mode handles complex packets, and markdown suits downstream reasoning.
- **D:** Incorrect for this question. Single-task analyzers target one content type or objective. They may be simpler and cheaper than general pro-mode pipelines. Why the correct answer wins: Pro mode handles complex packets, and markdown suits downstream reasoning.
- **E:** Correct. Markdown preserves structure and is easy for models to consume. Validate tables and key values. In this case: Pro mode handles complex packets, and markdown suits downstream reasoning.

### Question 78 — A

Answer: Upload image → validate format and size → send multimodal request → parse structured fields → route low-confidence values to review. Input validation precedes the model call, output is parsed into fields, and low-confidence values go to human review. Validation and structured parsing bracket the multimodal call, and low-confidence output goes to people. Local study-map skill 3.5 (Multimodal Responsible AI), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Correct. Validation and structured parsing bracket the multimodal call, and low-confidence output goes to people. In this case: Input validation precedes the model call, output is parsed into fields, and low-confidence values go to human review.
- **B:** Incorrect for this question. Review cannot precede the request, and parsing must follow the response. Why the correct answer wins: Input validation precedes the model call, output is parsed into fields, and low-confidence values go to human review.
- **C:** Incorrect for this question. Parsing requires a response, which requires an uploaded and validated image. Why the correct answer wins: Input validation precedes the model call, output is parsed into fields, and low-confidence values go to human review.
- **D:** Incorrect for this question. A request cannot precede the upload, and validation must come before the call. Why the correct answer wins: Input validation precedes the model call, output is parsed into fields, and low-confidence values go to human review.

### Question 79 — D

Answer: Select and return the most relevant source sentences. Extractive summaries return source sentences verbatim, so every statement remains quotable and auditable. Extractive summaries stay verbatim and therefore auditable, at the cost of readability and length. Local study-map skill 4.1 (Language Model Text Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Abstractive summaries read naturally and compress long text, but they can introduce statements that the source does not support. Why the correct answer wins: Extractive summaries return source sentences verbatim, so every statement remains quotable and auditable.
- **B:** Incorrect for this question. Compliance work requires precise citation, retention, and review. Generic summarization is insufficient without controls. Why the correct answer wins: Extractive summaries return source sentences verbatim, so every statement remains quotable and auditable.
- **C:** Incorrect for this question. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Why the correct answer wins: Extractive summaries return source sentences verbatim, so every statement remains quotable and auditable.
- **D:** Correct. Extractive summaries stay verbatim and therefore auditable, at the cost of readability and length. In this case: Extractive summaries return source sentences verbatim, so every statement remains quotable and auditable.

### Question 80 — C

Answer: Convert names between writing systems without translating meaning. Transliteration preserves pronunciation across writing systems. Transliteration preserves pronunciation for names and addresses. It is not a substitute for translating meaning-bearing text. Local study-map skill 4.2 (Translation), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Translation should preserve meaning, names, and formatting. Evaluate domain terminology and low-resource languages. Why the correct answer wins: Transliteration preserves pronunciation across writing systems.
- **B:** Incorrect for this question. Domain adaptation improves consistency and recall. Validate against expert-created expected outputs. Why the correct answer wins: Transliteration preserves pronunciation across writing systems.
- **C:** Correct. Transliteration preserves pronunciation for names and addresses. It is not a substitute for translating meaning-bearing text. In this case: Transliteration preserves pronunciation across writing systems.
- **D:** Incorrect for this question. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Why the correct answer wins: Transliteration preserves pronunciation across writing systems.

### Question 81 — D

Answer: Select a specific synthesis voice for consistent spoken output. A specific synthesis voice keeps the channel consistent. A named voice keeps a phone or kiosk channel recognizable across prompts. Voice availability and language coverage vary by region. Local study-map skill 4.3 (Speech Solutions), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Why the correct answer wins: A specific synthesis voice keeps the channel consistent.
- **B:** Incorrect for this question. Text-to-speech supports voice responses and accessibility. Voice, prosody, and latency affect usability. Why the correct answer wins: A specific synthesis voice keeps the channel consistent.
- **C:** Incorrect for this question. Custom speech can improve recognition of domain terms. It requires representative audio and ongoing evaluation. Why the correct answer wins: A specific synthesis voice keeps the channel consistent.
- **D:** Correct. A named voice keeps a phone or kiosk channel recognizable across prompts. Voice availability and language coverage vary by region. In this case: A specific synthesis voice keeps the channel consistent.

### Question 82 — A

Answer: Extract key phrases to summarize what a document covers. Key-phrase extraction surfaces the salient topics in each document, which supports navigation and triage. Key phrases support navigation, tagging, and clustering. They are not a substitute for a required structured field. Local study-map skill 4.1 (Language Model Text Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Correct. Key phrases support navigation, tagging, and clustering. They are not a substitute for a required structured field. In this case: Key-phrase extraction surfaces the salient topics in each document, which supports navigation and triage.
- **B:** Incorrect for this question. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Why the correct answer wins: Key-phrase extraction surfaces the salient topics in each document, which supports navigation and triage.
- **C:** Incorrect for this question. Topic extraction supports discovery and grouping. It is not a substitute for an authoritative taxonomy. Why the correct answer wins: Key-phrase extraction surfaces the salient topics in each document, which supports navigation and triage.
- **D:** Incorrect for this question. Entity extraction turns text into structured facts. Ambiguous mentions need resolution and validation. Why the correct answer wins: Key-phrase extraction surfaces the salient topics in each document, which supports navigation and triage.

### Question 83 — B, C

Answers: Detect and redact sensitive personal data; Analyze sentiment and tone with an appropriate service. PII detection finds personal data, and sentiment detects escalation. Sensitive Data Protection or language PII detection can identify and mask data. Verify that redaction covers every path where content flows. Sentiment analysis can support triage and monitoring. Domain and language variation require validation. Local study-map skill 4.1 (Language Model Text Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Why the correct answer wins: PII detection finds personal data, and sentiment detects escalation.
- **B:** Correct. Sentiment analysis can support triage and monitoring. Domain and language variation require validation. In this case: PII detection finds personal data, and sentiment detects escalation.
- **C:** Correct. Sensitive Data Protection or language PII detection can identify and mask data. Verify that redaction covers every path where content flows. In this case: PII detection finds personal data, and sentiment detects escalation.
- **D:** Incorrect for this question. Topic extraction supports discovery and grouping. It is not a substitute for an authoritative taxonomy. Why the correct answer wins: PII detection finds personal data, and sentiment detects escalation.
- **E:** Incorrect for this question. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Why the correct answer wins: PII detection finds personal data, and sentiment detects escalation.

### Question 84 — B

Answer: Tune scoring and boosting against a labelled query set. Scoring changes must be measured on a labelled query set. Boosting and scoring changes should be measured on real queries. Untested tuning usually trades one query class for another. Local study-map skill 5.2 (Search and Grounding Configuration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. A semantic ranker can improve relevance for natural-language queries. It adds cost and latency and should be measured against a baseline. Why the correct answer wins: Scoring changes must be measured on a labelled query set.
- **B:** Correct. Boosting and scoring changes should be measured on real queries. Untested tuning usually trades one query class for another. In this case: Scoring changes must be measured on a labelled query set.
- **C:** Incorrect for this question. Embeddings support similarity search over meaning rather than exact terms. Vector search still needs chunking, filtering, and evaluation. Why the correct answer wins: Scoring changes must be measured on a labelled query set.
- **D:** Incorrect for this question. Hybrid search covers exact identifiers and paraphrased meaning together. Fusion and ranking need testing on representative queries. Why the correct answer wins: Scoring changes must be measured on a labelled query set.

### Question 85 — D

Answer: Add enrichment skills for text, image, and layout. Enrichment adds derived content during indexing. A skillset can extract entities, captions, and structure during indexing. Enrichment adds cost and failure points that need monitoring. Local study-map skill 5.3 (Enrichment Skills), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. Why the correct answer wins: Enrichment adds derived content during indexing.
- **B:** Incorrect for this question. Markdown preserves structure and is easy for models to consume. Validate tables and key values. Why the correct answer wins: Enrichment adds derived content during indexing.
- **C:** Incorrect for this question. Skillsets can OCR, split, embed, and extract during indexing. Each skill adds latency, cost, and failure modes. Why the correct answer wins: Enrichment adds derived content during indexing.
- **D:** Correct. A skillset can extract entities, captions, and structure during indexing. Enrichment adds cost and failure points that need monitoring. In this case: Enrichment adds derived content during indexing.

### Question 86 — B

Answer: Define index fields, attributes, and searchable versus filterable behavior. Field attributes control filtering and sorting. Field attributes decide what can be filtered, sorted, faceted, or retrieved, so schema choices constrain query design later. Local study-map skill 5.6 (Document and Content Extraction), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. Document Intelligence provides prebuilt and custom extraction for structured documents. Validate field accuracy on representative samples. Why the correct answer wins: Field attributes control filtering and sorting.
- **B:** Correct. Field attributes decide what can be filtered, sorted, faceted, or retrieved, so schema choices constrain query design later. In this case: Field attributes control filtering and sorting.
- **C:** Incorrect for this question. Typed fields feed downstream systems directly. Add validation and confidence thresholds before automated action. Why the correct answer wins: Field attributes control filtering and sorting.
- **D:** Incorrect for this question. Analyzers define what to extract and how to return it. Version and test them like application code. Why the correct answer wins: Field attributes control filtering and sorting.

### Question 87 — D

Answer: Combine OCR with layout analysis for complex documents. OCR with layout analysis preserves relationships. OCR supplies text while layout analysis preserves relationships. Together they support tables and multi-column forms. Local study-map skill 5.4 (RAG Ingestion and OCR), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. Chunking affects recall, precision, and context use. Respect document structure and test against real questions. Why the correct answer wins: OCR with layout analysis preserves relationships.
- **B:** Incorrect for this question. Markdown preserves headings, tables, and lists in a model-friendly form. Validate that critical values survive conversion. Why the correct answer wins: OCR with layout analysis preserves relationships.
- **C:** Incorrect for this question. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. Why the correct answer wins: OCR with layout analysis preserves relationships.
- **D:** Correct. OCR supplies text while layout analysis preserves relationships. Together they support tables and multi-column forms. In this case: OCR with layout analysis preserves relationships.

### Question 88 — B

Answer: Connect the data source → define the index schema → attach the enrichment skillset → run the indexer → validate relevance on sample queries. The source is connected, the schema defined, enrichment attached, the indexer run, and relevance validated on sample queries. Schema and enrichment must exist before indexing runs, and relevance is checked after the index is populated. Local study-map skill 5.2 (Search and Grounding Configuration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. Relevance cannot be validated on an index that was never populated. Why the correct answer wins: The source is connected, the schema defined, enrichment attached, the indexer run, and relevance validated on sample queries.
- **B:** Correct. Schema and enrichment must exist before indexing runs, and relevance is checked after the index is populated. In this case: The source is connected, the schema defined, enrichment attached, the indexer run, and relevance validated on sample queries.
- **C:** Incorrect for this question. An indexer cannot run before the source and schema exist. Why the correct answer wins: The source is connected, the schema defined, enrichment attached, the indexer run, and relevance validated on sample queries.
- **D:** Incorrect for this question. The schema must exist before enrichment and relevance testing. Why the correct answer wins: The source is connected, the schema defined, enrichment attached, the indexer run, and relevance validated on sample queries.

### Question 89 — D

Answer: Use least-privilege Azure RBAC roles for the workload identity. Role-based access control restricts each identity to its authorized region and data scope. Roles should match the operations the app or agent performs. Broad contributor access increases blast radius. Local study-map skill 1.6 (Security, Identity, and Networking), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. A managed secret store supports rotation and access control. Secrets should never appear in prompts, code, or logs. Why the correct answer wins: Role-based access control restricts each identity to its authorized region and data scope.
- **B:** Incorrect for this question. Egress controls reduce exfiltration and unauthorized tool reach. Combine with identity and data controls. Why the correct answer wins: Role-based access control restricts each identity to its authorized region and data scope.
- **C:** Incorrect for this question. Filters restrict results to content the user may see. They must be enforced before content reaches the model. Why the correct answer wins: Role-based access control restricts each identity to its authorized region and data scope.
- **D:** Correct. Roles should match the operations the app or agent performs. Broad contributor access increases blast radius. In this case: Role-based access control restricts each identity to its authorized region and data scope.

### Question 90 — D

Answer: Use evaluators for quality, safety, and groundedness. Evaluators produce comparable quality signals across configurations. Evaluators provide repeatable signals across models and prompts. They must be calibrated against human judgment for high-impact work. Local study-map skill 2.3 (Evaluating Models and Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Alerts turn monitoring into action. Route them to an accountable owner with a runbook. Why the correct answer wins: Evaluators produce comparable quality signals across configurations.
- **B:** Incorrect for this question. Central telemetry captures latency, errors, dependencies, and custom events. Redact sensitive content before logging. Why the correct answer wins: Evaluators produce comparable quality signals across configurations.
- **C:** Incorrect for this question. Audit evidence supports investigation and accountability. Protect log integrity and retention. Why the correct answer wins: Evaluators produce comparable quality signals across configurations.
- **D:** Correct. Evaluators provide repeatable signals across models and prompts. They must be calibrated against human judgment for high-impact work. In this case: Evaluators produce comparable quality signals across configurations.

### Question 91 — C

Answer: Enable tracing across agent, model, and tool calls. Traces show the ordered model and tool calls so the failing step can be located. Traces localize failures and latency in multi-step workflows. Correlate them with evaluation results and deployment versions. Local study-map skill 2.7 (Agent Monitoring and Error Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Traces show the ordered model and tool calls so the failing step can be located.
- **B:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Traces show the ordered model and tool calls so the failing step can be located.
- **C:** Correct. Traces localize failures and latency in multi-step workflows. Correlate them with evaluation results and deployment versions. In this case: Traces show the ordered model and tool calls so the failing step can be located.
- **D:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Traces show the ordered model and tool calls so the failing step can be located.

### Question 92 — A

Answer: Enable a sandboxed code interpreter tool for calculations. A sandboxed interpreter computes deterministically from the supplied data. Code execution handles quantitative work the model cannot do reliably in text. The sandbox must be isolated and output must be validated. Local study-map skill 2.5 (Agent Tools, Retrieval, Memory, and Function Calling), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Code execution handles quantitative work the model cannot do reliably in text. The sandbox must be isolated and output must be validated. In this case: A sandboxed interpreter computes deterministically from the supplied data.
- **B:** Incorrect for this question. OpenAPI tools describe supported HTTP operations for agent use. Narrow operations, validate inputs, and authenticate the caller. Why the correct answer wins: A sandboxed interpreter computes deterministically from the supplied data.
- **C:** Incorrect for this question. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Why the correct answer wins: A sandboxed interpreter computes deterministically from the supplied data.
- **D:** Incorrect for this question. A file tool retrieves from curated stores under configured access. It still depends on indexing quality and permission filters. Why the correct answer wins: A sandboxed interpreter computes deterministically from the supplied data.

### Question 93 — B

Answer: Enable tracing across agent, model, and tool calls. Traces show the ordered model and tool calls. Traces localize failures and latency in multi-step workflows. Correlate them with evaluation results and deployment versions. Local study-map skill 2.7 (Agent Monitoring and Error Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Traces show the ordered model and tool calls.
- **B:** Correct. Traces localize failures and latency in multi-step workflows. Correlate them with evaluation results and deployment versions. In this case: Traces show the ordered model and tool calls.
- **C:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Traces show the ordered model and tool calls.
- **D:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Traces show the ordered model and tool calls.

### Question 94 — A

Answer: Push documents to an index through the data-plane API. Push ingestion indexes documents as they are written. Push ingestion supports near-real-time updates from applications. The app owns batching, retries, and deletion. Local study-map skill 5.1 (Content Ingestion and Indexing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Correct. Push ingestion supports near-real-time updates from applications. The app owns batching, retries, and deletion. In this case: Push ingestion indexes documents as they are written.
- **B:** Incorrect for this question. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. Why the correct answer wins: Push ingestion indexes documents as they are written.
- **C:** Incorrect for this question. Skillsets can OCR, split, embed, and extract during indexing. Each skill adds latency, cost, and failure modes. Why the correct answer wins: Push ingestion indexes documents as they are written.
- **D:** Incorrect for this question. OCR unlocks text in scans and screenshots. Layout and table structure may still require specialized extraction. Why the correct answer wins: Push ingestion indexes documents as they are written.

### Question 95 — C

Answer: Synthesize speech with Azure AI Speech. Text-to-speech synthesizes spoken output from generated text. Text-to-speech supports voice responses and accessibility. Voice, prosody, and latency affect usability. Local study-map skill 4.3 (Speech Solutions), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Custom speech can improve recognition of domain terms. It requires representative audio and ongoing evaluation. Why the correct answer wins: Text-to-speech synthesizes spoken output from generated text.
- **B:** Incorrect for this question. Speech-to-text enables voice agents and transcript analysis. Audio quality, accents, and domain terms affect accuracy. Why the correct answer wins: Text-to-speech synthesizes spoken output from generated text.
- **C:** Correct. Text-to-speech supports voice responses and accessibility. Voice, prosody, and latency affect usability. In this case: Text-to-speech synthesizes spoken output from generated text.
- **D:** Incorrect for this question. Audio-capable models can summarize or answer questions about recordings. Verify transcription quality and evidence grounding. Why the correct answer wins: Text-to-speech synthesizes spoken output from generated text.

### Question 96 — C

Answer: Adapt prompts and models to domain terminology. A validated domain lexicon teaches local terminology to the extraction step. Domain adaptation improves consistency and recall. Validate against expert-created expected outputs. Local study-map skill 4.4 (Domain Customization), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Sensitive Data Protection or language PII detection can identify and mask data. Verify that redaction covers every path where content flows. Why the correct answer wins: A validated domain lexicon teaches local terminology to the extraction step.
- **B:** Incorrect for this question. Translation should preserve meaning, names, and formatting. Evaluate domain terminology and low-resource languages. Why the correct answer wins: A validated domain lexicon teaches local terminology to the extraction step.
- **C:** Correct. Domain adaptation improves consistency and recall. Validate against expert-created expected outputs. In this case: A validated domain lexicon teaches local terminology to the extraction step.
- **D:** Incorrect for this question. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Why the correct answer wins: A validated domain lexicon teaches local terminology to the extraction step.

### Question 97 — B

Answer: Train a custom extraction model on labeled documents. A custom extraction model targets a proprietary document layout that no prebuilt model covers. Custom models fit specialized forms not covered by prebuilts. They require representative labels and retraining discipline. Local study-map skill 5.6 (Document and Content Extraction), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. Analyzers define what to extract and how to return it. Version and test them like application code. Why the correct answer wins: A custom extraction model targets a proprietary document layout that no prebuilt model covers.
- **B:** Correct. Custom models fit specialized forms not covered by prebuilts. They require representative labels and retraining discipline. In this case: A custom extraction model targets a proprietary document layout that no prebuilt model covers.
- **C:** Incorrect for this question. Prebuilt models cover invoices, receipts, IDs, and similar formats. Check supported locales and field coverage. Why the correct answer wins: A custom extraction model targets a proprietary document layout that no prebuilt model covers.
- **D:** Incorrect for this question. Single-task analyzers target one content type or objective. They may be simpler and cheaper than general pro-mode pipelines. Why the correct answer wins: A custom extraction model targets a proprietary document layout that no prebuilt model covers.

### Question 98 — A

Answer: Persist conversation history in a thread or session. Conversation state keeps the earlier context available across turns. Threads support continuity across turns. Apply retention and access controls to stored history. Local study-map skill 2.2 (Foundry SDK and Project Integration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Threads support continuity across turns. Apply retention and access controls to stored history. In this case: Conversation state keeps the earlier context available across turns.
- **B:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: Conversation state keeps the earlier context available across turns.
- **C:** Incorrect for this question. Embeddings determine semantic similarity behavior. Evaluate retrieval quality before and after changes. Why the correct answer wins: Conversation state keeps the earlier context available across turns.
- **D:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Conversation state keeps the earlier context available across turns.

### Question 99 — D

Answer: Use a custom speech model for specialized vocabulary. A custom speech model adapts vocabulary to the domain. Custom speech can improve recognition of domain terms. It requires representative audio and ongoing evaluation. Local study-map skill 4.3 (Speech Solutions), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Speech-to-text enables voice agents and transcript analysis. Audio quality, accents, and domain terms affect accuracy. Why the correct answer wins: A custom speech model adapts vocabulary to the domain.
- **B:** Incorrect for this question. Text-to-speech supports voice responses and accessibility. Voice, prosody, and latency affect usability. Why the correct answer wins: A custom speech model adapts vocabulary to the domain.
- **C:** Incorrect for this question. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Why the correct answer wins: A custom speech model adapts vocabulary to the domain.
- **D:** Correct. Custom speech can improve recognition of domain terms. It requires representative audio and ongoing evaluation. In this case: A custom speech model adapts vocabulary to the domain.

### Question 100 — D

Answer: Use field-level confidence to route exceptions. Field-level confidence sends uncertain values to review. Low-confidence fields should be reviewed rather than accepted. Thresholds depend on downstream impact. Local study-map skill 5.6 (Document and Content Extraction), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Why the correct answer wins: Field-level confidence sends uncertain values to review.
- **B:** Incorrect for this question. Relevance covers both retrieval and response usefulness. A correct but off-topic answer still fails. Why the correct answer wins: Field-level confidence sends uncertain values to review.
- **C:** Incorrect for this question. Sentiment analysis can support triage and monitoring. Domain and language variation require validation. Why the correct answer wins: Field-level confidence sends uncertain values to review.
- **D:** Correct. Low-confidence fields should be reviewed rather than accepted. Thresholds depend on downstream impact. In this case: Field-level confidence sends uncertain values to review.
