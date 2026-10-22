# Microsoft AI-103 — Full-Length Mock Exam 2

Azure AI Apps and Agents Developer Associate · 100 questions · 120 minutes · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 84 multiple-choice (selection count stated where needed), 16 multi-select, and 4 case studies of 3 questions. 8 of the multiple-choice items ask you to choose the correct candidate sequence. Hot-area, drag-and-drop UI, labs, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. A hospital plans an ambient documentation pilot and must confirm which models accept audio and text in its region. What should the team review?

Domain: Plan and manage an Azure AI solution

- A. Use a general-purpose large language model for complex reasoning
- B. Compare supported models in the Foundry model catalog
- C. Use a small language model for a narrow, high-volume task
- D. Train or deploy a task-specific model outside the prebuilt catalog

### 2. A triage classifier must return one of eight labels at low cost and low latency. Which model class should be evaluated first?

Domain: Plan and manage an Azure AI solution

- A. Use a small language model for a narrow, high-volume task
- B. Use a general-purpose large language model for complex reasoning
- C. Use a multimodal model for combined text, image, or audio input
- D. Train or deploy a task-specific model outside the prebuilt catalog

### 3. A scheduling assistant must recall the clinic a patient chose earlier in the same conversation. What should be used?

Domain: Plan and manage an Azure AI solution

- A. Connect an Azure AI Search index as agent knowledge
- B. Expose an OpenAPI operation as an agent tool
- C. Expose a typed function as an agent tool
- D. Use managed conversation state or memory for continuity

### 4. A clinical policy assistant must search 12,000 approved documents and expose them to an agent with citations. Which two components should be included? Select two.

Domain: Plan and manage an Azure AI solution

- A. Use a vector index for semantic retrieval
- B. Use managed conversation state or memory for continuity
- C. Train or deploy a task-specific model outside the prebuilt catalog
- D. Expose a typed function as an agent tool
- E. Connect an Azure AI Search index as agent knowledge

### 5. A hospital must move a triage assistant from pilot to production with reproducible infrastructure. Which sequence should the team follow?

Domain: Plan and manage an Azure AI solution

- A. Configure app → provision resources → deploy model → promote → evaluate
- B. Provision resources → deploy model → configure app connection → evaluate → promote
- C. Deploy model → promote → provision resources → evaluate → configure app
- D. Evaluate → provision resources → promote → deploy model → configure app

### 6. Protected health information must never traverse the public internet to the model endpoint. What should be configured?

Domain: Plan and manage an Azure AI solution

- A. Use private endpoints and disable public network access
- B. Use supported prompt or response caching where appropriate
- C. Manage AI resources with infrastructure as code and CI/CD
- D. Plan for model quota expressed in tokens and requests per minute

### 7. The documentation assistant is throttled only when about 40 clinicians dictate at the same moment. What should be re-planned first?

Domain: Plan and manage an Azure AI solution

- A. Track cost per accepted task, not only per token
- B. Use provisioned throughput for predictable high-volume workloads
- C. Plan for model quota expressed in tokens and requests per minute
- D. Monitor input and quality drift over time

### 8. Cost review shows that a long, unchanged policy preamble is resent on every request. Which optimization should be applied first?

Domain: Plan and manage an Azure AI solution

- A. Use provisioned throughput for predictable high-volume workloads
- B. Track cost per accepted task, not only per token
- C. Use batch processing for latency-tolerant bulk work
- D. Use supported prompt or response caching where appropriate

### 9. Transcription quality declines slowly after clinics install a new headset model. What should the team monitor?

Domain: Plan and manage an Azure AI solution

- A. Apply watermarks or provenance markers to generated media
- B. Monitor input and quality drift over time
- C. Track cost per accepted task, not only per token
- D. Plan for model quota expressed in tokens and requests per minute

### 10. A containerized app must authenticate to its Foundry resource without secrets in code or configuration. What should it use?

Domain: Plan and manage an Azure AI solution

- A. Authenticate with a managed identity instead of keys
- B. Shared connection string with an embedded secret
- C. Store secrets in Azure Key Vault when keys are unavoidable
- D. Long-lived API key pasted into configuration

### 11. A new service must read one index and nothing else, with no stored secrets. Which two actions should you take? Select two.

Domain: Plan and manage an Azure AI solution

- A. Use private endpoints and disable public network access
- B. Use least-privilege Azure RBAC roles for the workload identity
- C. Authenticate with a managed identity instead of keys
- D. Store secrets in Azure Key Vault when keys are unavoidable
- E. Configure content safety filters for harmful categories

### 12. An agent may send follow-up instructions directly to patients. Which two safeguards belong in the design? Select two.

Domain: Plan and manage an Azure AI solution

- A. Configure content safety filters for harmful categories
- B. Use supported prompt or response caching where appropriate
- C. Use a small language model for a narrow, high-volume task
- D. Require human approval before consequential actions
- E. Lower temperature for more deterministic extraction

### 13. Clinicians report that generated summaries occasionally omit a listed allergy. Which control fits best?

Domain: Plan and manage an Azure AI solution

- A. Route low-confidence or high-impact results to human review
- B. Enforce constraints in code and platform policy
- C. Require human approval before consequential actions
- D. Set agent oversight mode and tool-access constraints

### 14. An assistant must answer from the current approved formulary and show where each answer came from. Which approach fits?

Domain: Implement generative AI and agentic solutions

- A. Configure content safety filters for harmful categories
- B. Ground responses with retrieval-augmented generation
- C. Compare supported models in the Foundry model catalog
- D. Route requests to different models by task difficulty

### 15. A discharge workflow must extract medications, validate them against a formulary, then draft instructions. What should the design use?

Domain: Implement generative AI and agentic solutions

- A. One model call with no external retrieval or tool use
- B. Use a versioned prompt template with explicit variables
- C. Limit autonomy with scope, budget, and stop conditions
- D. Design multistep workflows with explicit checkpoints

### 16. An application must call only the models deployed to a specific approved Foundry project. What should it be configured with?

Domain: Implement generative AI and agentic solutions

- A. Store secrets in Azure Key Vault when keys are unavoidable
- B. Connect the application to the Foundry project endpoint
- C. Compare supported models in the Foundry model catalog
- D. Use an Azure AI Search indexer to pull source content

### 17. A Python service needs supported authentication, retries, and streaming for Foundry calls. What should it use?

Domain: Implement generative AI and agentic solutions

- A. Use a Foundry SDK or supported connector from application code
- B. Create and run deployments by hand in the portal
- C. Manage AI resources with infrastructure as code and CI/CD
- D. Use batch processing for latency-tolerant bulk work

### 18. A downstream record system consumes model output, and reviewers must verify each answer. Which two requirements matter most? Select two.

Domain: Implement generative AI and agentic solutions

- A. Apply watermarks or provenance markers to generated media
- B. Use provisioned throughput for predictable high-volume workloads
- C. Require citations tied to retrieved evidence
- D. Return a defined JSON schema for downstream systems
- E. Lower temperature for more deterministic extraction

### 19. An answer reads smoothly and stays on topic but asserts a formulary rule that was never retrieved. Which failure should be measured?

Domain: Implement generative AI and agentic solutions

- A. Detect fabricated or unsupported statements
- B. Evaluate structure and logical consistency of responses
- C. Measure whether retrieved content and answers address the question
- D. Detect tone and sentiment appropriate to the audience

### 20. An agent sends malformed arguments when booking appointments because the tool description is vague. What should be improved first?

Domain: Implement generative AI and agentic solutions

- A. Define narrow tool schemas with clear descriptions
- B. Use managed conversation state or memory for continuity
- C. Put stable behavior rules in the system message
- D. Use a versioned prompt template with explicit variables

### 21. Every agent turn must follow the same clinical tone and refusal policy. Where should that guidance live?

Domain: Implement generative AI and agentic solutions

- A. Enforce constraints in code and platform policy
- B. Use least-privilege Azure RBAC roles for the workload identity
- C. Configure content safety filters for harmful categories
- D. Put stable behavior rules in the system message

### 22. An agent must call an existing scheduling service that already publishes an OpenAPI specification. Which tool type fits best?

Domain: Implement generative AI and agentic solutions

- A. Ground responses with retrieval-augmented generation
- B. Expose an OpenAPI operation as an agent tool
- C. Use managed conversation state or memory for continuity
- D. Expose a typed function as an agent tool

### 23. A referral agent must keep a referral number across turns and look that referral up in a practice system. Which two capabilities are required? Select two.

Domain: Implement generative AI and agentic solutions

- A. Expose a typed function as an agent tool
- B. Apply watermarks or provenance markers to generated media
- C. Choose an embedding model suited to the content and language
- D. Use provisioned throughput for predictable high-volume workloads
- E. Persist conversation history in a thread or session

### 24. Which sequence correctly builds and releases a patient-facing scheduling agent?

Domain: Implement generative AI and agentic solutions

- A. Deploy with monitoring → define role and goal → configure tools → evaluate in sandbox → attach knowledge
- B. Configure tools → deploy with monitoring → define role and goal → attach knowledge → evaluate in sandbox
- C. Define role and goal → configure tools → attach knowledge → evaluate in sandbox → deploy with monitoring
- D. Attach knowledge → configure tools → deploy with monitoring → define role and goal → evaluate in sandbox

### 25. A triage agent must pass a conversation to a scheduling specialist while keeping context. Which pattern fits?

Domain: Implement generative AI and agentic solutions

- A. Transfer control between agents with explicit context
- B. Run agents in a fixed sequence
- C. Use self-critique or reflection to improve drafts
- D. Run independent agents concurrently

### 26. An agent fails only when a request requires two tool calls in sequence. What should be inspected to find the failing step?

Domain: Implement generative AI and agentic solutions

- A. Apply watermarks or provenance markers to generated media
- B. Use supported prompt or response caching where appropriate
- C. Enable tracing across agent, model, and tool calls
- D. Plan for model quota expressed in tokens and requests per minute

### 27. Structured extraction returns different values for identical repeated requests. Which setting should be reduced first?

Domain: Implement generative AI and agentic solutions

- A. Lower temperature for more deterministic extraction
- B. Use supported prompt or response caching where appropriate
- C. Route requests to different models by task difficulty
- D. Adjust top-p to control response diversity

### 28. A clinician must remove a visible patient name badge from an approved photo before a teaching deck. What should be used?

Domain: Implement computer vision solutions

- A. Edit a region of an image with a mask
- B. Generate concise or detailed image captions
- C. Apply prompt-driven image modifications
- D. Generate video from text or reference media

### 29. A patient-education team needs an original illustration of a healthy-plate diagram. Which capability applies?

Domain: Implement computer vision solutions

- A. Generate video from text or reference media
- B. Generate alt text aligned to accessibility guidance
- C. Edit a region of an image with a mask
- D. Generate images from text and reference media

### 30. A safety team must find the exact minute in recorded ward footage where a bed rail is lowered. What capability applies?

Domain: Implement computer vision solutions

- A. Apply prompt-driven image modifications
- B. Analyze video segments for events and content
- C. Edit generated video segments
- D. Generate concise or detailed image captions

### 31. A patient portal needs accessible image descriptions and answers about values shown in chart images. Which two capabilities apply? Select two.

Domain: Implement computer vision solutions

- A. Answer questions grounded in visual evidence
- B. Generate alt text aligned to accessibility guidance
- C. Apply watermarks or provenance markers to generated media
- D. Lower temperature for more deterministic extraction
- E. Use provisioned throughput for predictable high-volume workloads

### 32. A stock-photo library needs one short sentence describing each image for search. What should be generated?

Domain: Implement computer vision solutions

- A. Identify objects, components, or regions in visual content
- B. Return typed fields for automation
- C. Generate concise or detailed image captions
- D. Apply OCR to convert images and scans into usable text

### 33. Which sequence correctly processes a scanned referral image and routes uncertain values for review?

Domain: Implement computer vision solutions

- A. Upload image → validate format and size → send multimodal request → parse structured fields → route low-confidence values to review
- B. Parse structured fields → send multimodal request → upload image → validate format → review
- C. Validate format → review → upload image → parse structured fields → send multimodal request
- D. Send multimodal request → upload image → validate format → parse structured fields → review

### 34. Generated patient-education images must be screened for unsafe medical depictions before publication. Which control applies?

Domain: Implement computer vision solutions

- A. Apply watermarks or provenance markers to generated media
- B. Treat text embedded in images as untrusted input
- C. Enforce brand and usage rules for generated visuals
- D. Filter unsafe or disallowed visual content

### 35. A downstream records service requires fixed field names and types from each discharge summary. What should the prompt request?

Domain: Implement text analysis solutions

- A. Prompt for JSON that conforms to a supplied schema
- B. Generate summaries with explicit length and audience constraints
- C. Use Azure Translator or a language model for translation
- D. Identify topics or key phrases for navigation

### 36. A quality team reviews patient messages for disclosure risk and rising frustration. Which two analyses are relevant? Select two.

Domain: Implement text analysis solutions

- A. Generate summaries with explicit length and audience constraints
- B. Identify topics or key phrases for navigation
- C. Analyze sentiment and tone with an appropriate service
- D. Apply a custom glossary or terminology list
- E. Detect and redact sensitive personal data

### 37. Discharge instructions must appear in the patient's preferred language. Which capability applies?

Domain: Implement text analysis solutions

- A. Use Azure Translator or a language model for translation
- B. Generate summaries with explicit length and audience constraints
- C. Apply a custom glossary or terminology list
- D. Detect and redact sensitive personal data

### 38. Recorded consultations must become searchable text. Which capability is required?

Domain: Implement text analysis solutions

- A. Synthesize speech with Azure AI Speech
- B. Translate spoken language with speech translation
- C. Transcribe speech to text with Azure AI Speech
- D. Generate concise or detailed image captions

### 39. Dictation accuracy is poor for local drug names and clinician accents. What should be trained?

Domain: Implement text analysis solutions

- A. Synthesize speech with Azure AI Speech
- B. Apply a custom glossary or terminology list
- C. Use a custom speech model for specialized vocabulary
- D. Transcribe speech to text with Azure AI Speech

### 40. An extraction prompt misses specialty abbreviations used by only one hospital network. What should be added?

Domain: Implement text analysis solutions

- A. Detect and redact sensitive personal data
- B. Apply a custom glossary or terminology list
- C. Adapt prompts and models to domain terminology
- D. Use Azure Translator or a language model for translation

### 41. An index must stay synchronized with documents in a storage account without custom code. What should be used?

Domain: Implement information extraction solutions

- A. Push documents to an index through the data-plane API
- B. Apply OCR to convert images and scans into usable text
- C. Use an Azure AI Search indexer to pull source content
- D. Add an enrichment skillset to an indexing pipeline

### 42. Staff search by exact claim identifier and by paraphrased coverage questions. Which two features should be combined? Select two.

Domain: Implement information extraction solutions

- A. Apply semantic ranking to reorder search results
- B. Apply watermarks or provenance markers to generated media
- C. Lower temperature for more deterministic extraction
- D. Combine keyword and vector retrieval
- E. Use a vector index for semantic retrieval

### 43. An ingestion pipeline must extract entities and generate summaries while indexing. What should be added?

Domain: Implement information extraction solutions

- A. Add an enrichment skillset to an indexing pipeline
- B. Apply OCR to convert images and scans into usable text
- C. Use an Azure AI Search indexer to pull source content
- D. Push documents to an index through the data-plane API

### 44. Which sequence correctly builds a citable retrieval pipeline over clinical policy documents?

Domain: Implement information extraction solutions

- A. Ingest → extract text → chunk → embed → index → retrieve with citations
- B. Index → retrieve → ingest → chunk → embed → cite
- C. Ingest → retrieve → chunk → embed → index → cite
- D. Chunk → embed → ingest → retrieve → index → cite

### 45. A hospital must keep one documented model version in its data-residency region for the whole contract year. What should the team do?

Domain: Plan and manage an Azure AI solution

- A. Use a general-purpose large language model for complex reasoning
- B. Compare supported models in the Foundry model catalog
- C. Train or deploy a task-specific model outside the prebuilt catalog
- D. Pin the model version available in the required region

### 46. A clinic needs dictation transcription and form extraction within a month and has no labelled data. Which option should be assessed first?

Domain: Plan and manage an Azure AI solution

- A. Use a small language model for a narrow, high-volume task
- B. Train or deploy a task-specific model outside the prebuilt catalog
- C. Use Foundry Tools for prebuilt vision, speech, language, and extraction needs
- D. Use a general-purpose large language model for complex reasoning

### 47. An agent must call the electronic health record API that already publishes a machine-readable contract. Which tool type fits best?

Domain: Plan and manage an Azure AI solution

- A. Use managed conversation state or memory for continuity
- B. Connect an Azure AI Search index as agent knowledge
- C. Expose a typed function as an agent tool
- D. Expose an OpenAPI operation as an agent tool

### 48. A team wants to compare a candidate triage model against live behaviour without any patient seeing its output. What pattern fits?

Domain: Plan and manage an Azure AI solution

- A. Shift a small traffic percentage to the new version first
- B. Send mirrored production traffic to a candidate without returning its answers
- C. Use a standard pay-as-you-go model deployment for variable demand
- D. Use batch processing for latency-tolerant bulk work

### 49. A pilot must notify owners before its monthly spend exceeds an agreed ceiling. What should be configured?

Domain: Plan and manage an Azure AI solution

- A. Alert on spend thresholds per deployment or project
- B. Plan for model quota expressed in tokens and requests per minute
- C. Track cost per accepted task, not only per token
- D. Track prompt, completion, and cached token usage

### 50. The assistant still cites a policy that was withdrawn last month. What should be monitored to prevent this?

Domain: Plan and manage an Azure AI solution

- A. Monitor groundedness and citation quality in production
- B. Monitor index freshness, failures, and document counts
- C. Use Azure Monitor and Application Insights for telemetry
- D. Monitor input and quality drift over time

### 51. Compliance forbids the clinical workload from calling any external endpoint outside an allowlist. What should be enforced?

Domain: Plan and manage an Azure AI solution

- A. Use private endpoints and disable public network access
- B. Restrict outbound network access to approved destinations
- C. Private networking with public access left enabled
- D. Use least-privilege Azure RBAC roles for the workload identity

### 52. A discharge decision must remain attributable to a named clinician, not to the model. Which principle applies?

Domain: Plan and manage an Azure AI solution

- A. Enforce constraints in code and platform policy
- B. Preserve audit logs of changes, approvals, and tool actions
- C. Require human approval before consequential actions
- D. Set agent oversight mode and tool-access constraints

### 53. A release must be blocked automatically when groundedness falls below the agreed threshold. What should be added?

Domain: Plan and manage an Azure AI solution

- A. Use staged rollout with measurable rollback criteria
- B. Manage AI resources with infrastructure as code and CI/CD
- C. Shift a small traffic percentage to the new version first
- D. Block promotion in the pipeline when evaluation thresholds fail

### 54. Ten years of scanned notes must be re-summarized once for migration, with no interactive requirement. Which deployment option fits?

Domain: Plan and manage an Azure AI solution

- A. Plan for model quota expressed in tokens and requests per minute
- B. Use a standard pay-as-you-go model deployment for variable demand
- C. Use batch processing for latency-tolerant bulk work
- D. Use provisioned throughput for predictable high-volume workloads

### 55. A clinical model must be selected from what is offered locally and must not change under the team. Which two practices are required? Select two.

Domain: Plan and manage an Azure AI solution

- A. Compare supported models in the Foundry model catalog
- B. Train or deploy a task-specific model outside the prebuilt catalog
- C. Use a standard pay-as-you-go model deployment for variable demand
- D. Pin the model version available in the required region
- E. Use batch processing for latency-tolerant bulk work

### 56. A ward assistant must be checked for unsupported statements and the team must hear about it quickly. Which two capabilities are required? Select two.

Domain: Plan and manage an Azure AI solution

- A. Alert on latency, error rate, safety, and cost thresholds
- B. Monitor groundedness and citation quality in production
- C. Apply watermarks or provenance markers to generated media
- D. Track cost per accepted task, not only per token
- E. Measure end-to-end latency across model, retrieval, and tools

### 57. The workload must not reach unapproved endpoints and each identity must have only its needed permissions. Which two controls are required? Select two.

Domain: Plan and manage an Azure AI solution

- A. Configure content safety filters for harmful categories
- B. Use private endpoints and disable public network access
- C. Restrict outbound network access to approved destinations
- D. Store secrets in Azure Key Vault when keys are unavoidable
- E. Use least-privilege Azure RBAC roles for the workload identity

### 58. Which sequence correctly releases a clinical summarization change through an evaluation gate?

Domain: Plan and manage an Azure AI solution

- A. Deploy a canary → commit change → promote after metrics hold → run the evaluation suite → block on failed thresholds
- B. Run the evaluation suite → deploy a canary → commit change → block on failed thresholds → promote after metrics hold
- C. Commit change → deploy a canary → promote after metrics hold → run the evaluation suite → block on failed thresholds
- D. Commit change → run the evaluation suite → block on failed thresholds → deploy a canary → promote after metrics hold

### 59. Retrieval keeps missing an allergy statement that spans two pages of the same note. What should be adjusted?

Domain: Implement generative AI and agentic solutions

- A. Set chunk overlap so facts spanning a boundary stay retrievable
- B. Choose an embedding model suited to the content and language
- C. Choose chunk size and overlap for retrieval quality
- D. Select evidence within the model's usable context

### 60. Guidance changes monthly, and clinicians must see which document supports each statement. Which approach fits?

Domain: Implement generative AI and agentic solutions

- A. Route requests to different models by task difficulty
- B. Ground responses with retrieval-augmented generation
- C. Include representative examples in the prompt
- D. Design multistep workflows with explicit checkpoints

### 61. A clinician-facing web app must call the model service with a short-lived delegated credential. What should it request?

Domain: Implement generative AI and agentic solutions

- A. Use a Foundry SDK or supported connector from application code
- B. Store secrets in Azure Key Vault when keys are unavoidable
- C. Use short-lived scoped access tokens for tool calls
- D. Authenticate with a managed identity instead of keys

### 62. Two summarization prompts must be compared on identical notes so the difference is attributable. What provides that?

Domain: Implement generative AI and agentic solutions

- A. Build a representative golden dataset from real tasks
- B. Use evaluators for quality, safety, and groundedness
- C. Compare variants with controlled traffic and shared metrics
- D. Re-run evaluation suites after meaningful changes

### 63. A model upgrade must not reintroduce a previously fixed hallucination case. What should run before release?

Domain: Implement generative AI and agentic solutions

- A. Build a representative golden dataset from real tasks
- B. Use evaluators for quality, safety, and groundedness
- C. Re-run evaluation suites after meaningful changes
- D. Evaluate harmful, biased, or policy-violating output

### 64. An agent must answer from a curated set of approved clinical guidelines without a custom pipeline. Which tool fits?

Domain: Implement generative AI and agentic solutions

- A. Use managed conversation state or memory for continuity
- B. Ground responses with retrieval-augmented generation
- C. Enable a sandboxed code interpreter tool for calculations
- D. Give the agent a file-search tool over approved document stores

### 65. A general triage agent must transfer a billing question to a specialist while preserving the conversation. Which pattern fits?

Domain: Implement generative AI and agentic solutions

- A. Use self-critique or reflection to improve drafts
- B. Transfer control between agents with explicit context
- C. Run independent agents concurrently
- D. Use a manager agent to coordinate specialists

### 66. A discharge summary must be self-reviewed for omissions before it is returned. Which pattern applies?

Domain: Implement generative AI and agentic solutions

- A. Run independent agents concurrently
- B. Use self-critique or reflection to improve drafts
- C. Run agents in a fixed sequence
- D. Transfer control between agents with explicit context

### 67. Extracted fields include trailing commentary that breaks the downstream parser. What should be specified?

Domain: Implement generative AI and agentic solutions

- A. Adjust top-p to control response diversity
- B. Set a stop sequence so generation ends at the intended boundary
- C. Use supported prompt or response caching where appropriate
- D. Lower temperature for more deterministic extraction

### 68. Generated patient instructions repeat the same phrasing and omit valid alternatives. Which parameter should be adjusted?

Domain: Implement generative AI and agentic solutions

- A. Adjust top-p to control response diversity
- B. Use supported prompt or response caching where appropriate
- C. Set a seed parameter for reproducible sampling where the provider supports it
- D. Lower temperature for more deterministic extraction

### 69. A clinical service must use maintained client behaviour and must store no credential. Which two choices are required? Select two.

Domain: Implement generative AI and agentic solutions

- A. Store secrets in Azure Key Vault when keys are unavoidable
- B. Use short-lived scoped access tokens for tool calls
- C. Create and run deployments by hand in the portal
- D. Use a Foundry SDK or supported connector from application code
- E. Authenticate with a managed identity instead of keys

### 70. A release must be scored for clinical accuracy and screened for unsafe advice. Which two practices are required? Select two.

Domain: Implement generative AI and agentic solutions

- A. Re-run evaluation suites after meaningful changes
- B. Build a representative golden dataset from real tasks
- C. Compare variants with controlled traffic and shared metrics
- D. Evaluate harmful, biased, or policy-violating output
- E. Use evaluators for quality, safety, and groundedness

### 71. A ward assistant must search approved guidance and remember the patient context across turns. Which two capabilities are required? Select two.

Domain: Implement generative AI and agentic solutions

- A. Give the agent a file-search tool over approved document stores
- B. Expose an OpenAPI operation as an agent tool
- C. Route requests to different models by task difficulty
- D. Enable a sandboxed code interpreter tool for calculations
- E. Persist conversation history in a thread or session

### 72. Which sequence correctly builds and releases a triage agent?

Domain: Implement generative AI and agentic solutions

- A. Attach knowledge → configure tools → deploy with monitoring → define role and goal → evaluate in sandbox
- B. Configure tools → deploy with monitoring → define role and goal → attach knowledge → evaluate in sandbox
- C. Deploy with monitoring → define role and goal → configure tools → evaluate in sandbox → attach knowledge
- D. Define role and goal → configure tools → attach knowledge → evaluate in sandbox → deploy with monitoring

### 73. Automated checks pass an illustration that clinicians still consider inappropriate for patients. What should be added?

Domain: Implement computer vision solutions

- A. Filter unsafe or disallowed visual content
- B. Enforce brand and usage rules for generated visuals
- C. Queue flagged generations for human moderation before release
- D. Apply watermarks or provenance markers to generated media

### 74. A clinical image library needs filterable descriptive tags for teaching search. What should be generated?

Domain: Implement computer vision solutions

- A. Answer questions grounded in visual evidence
- B. Generate alt text aligned to accessibility guidance
- C. Generate concise or detailed image captions
- D. Generate a set of descriptive tags for each image

### 75. A team must extract typed fields from scanned referrals with a configurable analyzer rather than a fixed prebuilt model. Which service fits?

Domain: Implement computer vision solutions

- A. Configure a Content Understanding analyzer for the content type
- B. Use a prebuilt document model for common document types
- C. Use Azure AI Document Intelligence for forms and documents
- D. Use Azure Content Understanding analyzers in Foundry Tools

### 76. Extracted referral text is jumbled because the two-column layout is read across both columns. What should be applied?

Domain: Implement computer vision solutions

- A. Preserve document layout, tables, and reading order
- B. Apply OCR to convert images and scans into usable text
- C. Preserve reading order across columns and sections
- D. Produce markdown representations for downstream reasoning

### 77. Referral packets mix tables, handwriting, and photos across pages, and the output must feed a reasoning model. Which two choices are required? Select two.

Domain: Implement computer vision solutions

- A. Return markdown for retrieval and reasoning pipelines
- B. Use single-task mode for a focused extraction scenario
- C. Generate concise or detailed image captions
- D. Use pro mode for complex multimodal content understanding
- E. Identify objects, components, or regions in visual content

### 78. Which sequence correctly processes a photographed referral and sends doubtful values for review?

Domain: Implement computer vision solutions

- A. Validate format → review → upload image → parse structured fields → send multimodal request
- B. Send multimodal request → upload image → validate format → parse structured fields → review
- C. Parse structured fields → send multimodal request → upload image → validate format → review
- D. Upload image → validate format and size → send multimodal request → parse structured fields → route low-confidence values to review

### 79. A regulator requires summaries that quote the exact source sentences. Which style fits?

Domain: Implement text analysis solutions

- A. Generate summaries with explicit length and audience constraints
- B. Generate an abstractive summary in new wording
- C. Select and return the most relevant source sentences
- D. Customize summaries and extraction for compliance needs

### 80. Patient names in another writing system must appear correctly on printed labels without changing meaning. Which capability applies?

Domain: Implement text analysis solutions

- A. Adapt prompts and models to domain terminology
- B. Apply a custom glossary or terminology list
- C. Use Azure Translator or a language model for translation
- D. Convert names between writing systems without translating meaning

### 81. A telephone service must use one consistent branded voice for all prompts. What should be selected?

Domain: Implement text analysis solutions

- A. Synthesize speech with Azure AI Speech
- B. Select a specific synthesis voice for consistent spoken output
- C. Apply a custom glossary or terminology list
- D. Use a custom speech model for specialized vocabulary

### 82. A patient-safety mailbox must detect personal data and rising distress in messages. Which two analyses are relevant? Select two.

Domain: Implement text analysis solutions

- A. Identify topics or key phrases for navigation
- B. Apply a custom glossary or terminology list
- C. Analyze sentiment and tone with an appropriate service
- D. Generate summaries with explicit length and audience constraints
- E. Detect and redact sensitive personal data

### 83. Newly generated discharge summaries must be searchable within seconds of creation. What should the application use?

Domain: Implement information extraction solutions

- A. Apply OCR to convert images and scans into usable text
- B. Push documents to an index through the data-plane API
- C. Use an Azure AI Search indexer to pull source content
- D. Add an enrichment skillset to an indexing pipeline

### 84. Searches for drug names return unrelated guidance because one document family dominates. What should be tuned and measured?

Domain: Implement information extraction solutions

- A. Apply semantic ranking to reorder search results
- B. Tune scoring and boosting against a labelled query set
- C. Combine keyword and vector retrieval
- D. Use a vector index for semantic retrieval

### 85. An eligibility clause is split across two indexed chunks and is not retrieved. What should be adjusted?

Domain: Implement information extraction solutions

- A. Add enrichment skills for text, image, and layout
- B. Choose chunk size and overlap for retrieval quality
- C. Set chunk overlap so facts spanning a boundary stay retrievable
- D. Add an enrichment skillset to an indexing pipeline

### 86. Analysts must filter by admission date and sort by length, but those fields are full-text only. What should change?

Domain: Implement information extraction solutions

- A. Configure a Content Understanding analyzer for the content type
- B. Use Azure AI Document Intelligence for forms and documents
- C. Define index fields, attributes, and searchable versus filterable behavior
- D. Return typed fields for automation

### 87. Scanned consent forms must keep checkbox and table relationships for later extraction. What should be applied?

Domain: Implement information extraction solutions

- A. Choose chunk size and overlap for retrieval quality
- B. Produce markdown representations for downstream reasoning
- C. Use an Azure AI Search indexer to pull source content
- D. Combine OCR with layout analysis for complex documents

### 88. Which sequence correctly builds a clinical document index?

Domain: Implement information extraction solutions

- A. Run the indexer → connect the data source → define the index schema → attach the enrichment skillset → validate relevance on sample queries
- B. Attach the enrichment skillset → connect the data source → validate relevance on sample queries → define the index schema → run the indexer
- C. Connect the data source → define the index schema → attach the enrichment skillset → run the indexer → validate relevance on sample queries
- D. Validate relevance on sample queries → run the indexer → connect the data source → define the index schema → attach the enrichment skillset

---

## Case study — BillingBot

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 89. Translated statements keep mangling approved plan names. What should be added?

Domain: Implement text analysis solutions

- A. Generate summaries with explicit length and audience constraints
- B. Identify topics or key phrases for navigation
- C. Analyze sentiment and tone with an appropriate service
- D. Apply a custom glossary or terminology list

### 90. Standard Explanation of Benefits forms arrive in a well-known layout with stable fields. What should be used first?

Domain: Implement information extraction solutions

- A. Use a prebuilt document model for common document types
- B. Train a custom extraction model on labeled documents
- C. Use Azure AI Document Intelligence for forms and documents
- D. Configure a Content Understanding analyzer for the content type

### 91. Extracted amounts occasionally disagree with the scanned value. What should route those fields to a person?

Domain: Implement information extraction solutions

- A. Analyze sentiment and tone with an appropriate service
- B. Use field-level confidence to route exceptions
- C. Measure whether retrieved content and answers address the question
- D. Generate summaries with explicit length and audience constraints

---

## Case study — ClinDoc

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 92. After go-live, summaries sometimes state medications that no source note contains. Which signal should be monitored?

Domain: Plan and manage an Azure AI solution

- A. Measure end-to-end latency across model, retrieval, and tools
- B. Monitor groundedness and citation quality in production
- C. Plan for model quota expressed in tokens and requests per minute
- D. Track cost per accepted task, not only per token

### 93. The assistant must confirm whether a patient has an appointment tomorrow before answering. Which capability performs that check?

Domain: Implement generative AI and agentic solutions

- A. Use managed conversation state or memory for continuity
- B. Expose a typed function as an agent tool
- C. Expose an OpenAPI operation as an agent tool
- D. Ground responses with retrieval-augmented generation

### 94. One request may need records, scheduling, and billing expertise. Which pattern should coordinate them?

Domain: Implement generative AI and agentic solutions

- A. Run independent agents concurrently
- B. Connect specialist agents as tools to an orchestrator
- C. Run agents in a fixed sequence
- D. Use a manager agent to coordinate specialists

---

## Case study — Lakeview Clinic

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 95. The agent keeps sending an unformatted patient identifier to the lookup tool. What should be tightened first?

Domain: Implement generative AI and agentic solutions

- A. Route requests to different models by task difficulty
- B. Put stable behavior rules in the system message
- C. Define narrow tool schemas with clear descriptions
- D. Use managed conversation state or memory for continuity

### 96. A patient asks a follow-up question ten minutes after the first, and the earlier answer must still be in scope. Which capability provides that?

Domain: Implement generative AI and agentic solutions

- A. Persist conversation history in a thread or session
- B. Apply watermarks or provenance markers to generated media
- C. Use provisioned throughput for predictable high-volume workloads
- D. Choose an embedding model suited to the content and language

### 97. A request fails only when the agent needs two tool calls in sequence. What should be inspected?

Domain: Implement generative AI and agentic solutions

- A. Use supported prompt or response caching where appropriate
- B. Apply watermarks or provenance markers to generated media
- C. Lower temperature for more deterministic extraction
- D. Enable tracing across agent, model, and tool calls

---

## Case study — Meridian Health

The next 3 questions refer to this scenario. Read the full scenario before answering; case-study items are scored individually.

### 98. Dictation accuracy is poor for local drug names and the team has labelled audio. What should be trained?

Domain: Implement text analysis solutions

- A. Apply a custom glossary or terminology list
- B. Transcribe speech to text with Azure AI Speech
- C. Use a custom speech model for specialized vocabulary
- D. Synthesize speech with Azure AI Speech

### 99. Reviewers need a quick topical index of what each complaint packet covers. Which capability applies?

Domain: Implement text analysis solutions

- A. Identify topics or key phrases for navigation
- B. Extract key phrases to summarize what a document covers
- C. Generate summaries with explicit length and audience constraints
- D. Extract entities with defined types and boundaries

### 100. Extracted amounts are sometimes misread from faxed forms. What should route those values to a person?

Domain: Implement information extraction solutions

- A. Use field-level confidence to route exceptions
- B. Generate summaries with explicit length and audience constraints
- C. Analyze sentiment and tone with an appropriate service
- D. Measure whether retrieved content and answers address the question

---

## Answer key and explanations

### Question 1 — B

Answer: Compare supported models in the Foundry model catalog. The model catalog lists modality support, regional availability, and lifecycle status before selection. The catalog shows supported models with capability, modality, region, and lifecycle details. Verify availability for your subscription and region before designing around one model. Local study-map skill 1.1 (Selecting Foundry Models and Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Large models handle ambiguity and multi-step reasoning better in many cases, at higher cost and latency. Select with measured evidence rather than brand preference. Why the correct answer wins: The model catalog lists modality support, regional availability, and lifecycle status before selection.
- **B:** Correct. The catalog shows supported models with capability, modality, region, and lifecycle details. Verify availability for your subscription and region before designing around one model. In this case: The model catalog lists modality support, regional availability, and lifecycle status before selection.
- **C:** Incorrect for this question. Small models can reduce latency and cost for constrained classification or extraction. Confirm quality on representative data before standardizing. Why the correct answer wins: The model catalog lists modality support, regional availability, and lifecycle status before selection.
- **D:** Incorrect for this question. A custom model is justified when supported prebuilt options cannot meet a defined requirement. It adds data, evaluation, and lifecycle obligations. Why the correct answer wins: The model catalog lists modality support, regional availability, and lifecycle status before selection.

### Question 2 — A

Answer: Use a small language model for a narrow, high-volume task. A small language model is the reasonable starting point for narrow classification with tight cost limits. Small models can reduce latency and cost for constrained classification or extraction. Confirm quality on representative data before standardizing. Local study-map skill 1.1 (Selecting Foundry Models and Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. Small models can reduce latency and cost for constrained classification or extraction. Confirm quality on representative data before standardizing. In this case: A small language model is the reasonable starting point for narrow classification with tight cost limits.
- **B:** Incorrect for this question. Large models handle ambiguity and multi-step reasoning better in many cases, at higher cost and latency. Select with measured evidence rather than brand preference. Why the correct answer wins: A small language model is the reasonable starting point for narrow classification with tight cost limits.
- **C:** Incorrect for this question. Multimodal models accept more than one content type in a request. Validate extraction and grounding quality for each modality used. Why the correct answer wins: A small language model is the reasonable starting point for narrow classification with tight cost limits.
- **D:** Incorrect for this question. A custom model is justified when supported prebuilt options cannot meet a defined requirement. It adds data, evaluation, and lifecycle obligations. Why the correct answer wins: A small language model is the reasonable starting point for narrow classification with tight cost limits.

### Question 3 — D

Answer: Use managed conversation state or memory for continuity. Managed conversation state or memory carries the earlier choice across turns. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Local study-map skill 1.2 (Retrieval, Memory, Tool, and Knowledge Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. An index gives an agent curated, searchable evidence under configured access. Index content and permissions require ongoing ownership. Why the correct answer wins: Managed conversation state or memory carries the earlier choice across turns.
- **B:** Incorrect for this question. OpenAPI tools describe supported HTTP operations for agent use. Narrow operations, validate inputs, and authenticate the caller. Why the correct answer wins: Managed conversation state or memory carries the earlier choice across turns.
- **C:** Incorrect for this question. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. Why the correct answer wins: Managed conversation state or memory carries the earlier choice across turns.
- **D:** Correct. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. In this case: Managed conversation state or memory carries the earlier choice across turns.

### Question 4 — A, E

Answers: Use a vector index for semantic retrieval; Connect an Azure AI Search index as agent knowledge. A vector index supplies semantic retrieval, and a knowledge index exposes that content to the agent. Embeddings support similarity search over meaning rather than exact terms. Vector search still needs chunking, filtering, and evaluation. An index gives an agent curated, searchable evidence under configured access. Index content and permissions require ongoing ownership. Local study-map skill 1.2 (Retrieval, Memory, Tool, and Knowledge Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. Embeddings support similarity search over meaning rather than exact terms. Vector search still needs chunking, filtering, and evaluation. In this case: A vector index supplies semantic retrieval, and a knowledge index exposes that content to the agent.
- **B:** Incorrect for this question. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Why the correct answer wins: A vector index supplies semantic retrieval, and a knowledge index exposes that content to the agent.
- **C:** Incorrect for this question. A custom model is justified when supported prebuilt options cannot meet a defined requirement. It adds data, evaluation, and lifecycle obligations. Why the correct answer wins: A vector index supplies semantic retrieval, and a knowledge index exposes that content to the agent.
- **D:** Incorrect for this question. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. Why the correct answer wins: A vector index supplies semantic retrieval, and a knowledge index exposes that content to the agent.
- **E:** Correct. An index gives an agent curated, searchable evidence under configured access. Index content and permissions require ongoing ownership. In this case: A vector index supplies semantic retrieval, and a knowledge index exposes that content to the agent.

### Question 5 — B

Answer: Provision resources → deploy model → configure app connection → evaluate → promote. Resources and deployment come first, app configuration follows, and evaluation gates promotion. Provisioning and deployment precede app configuration, and evaluation gates promotion. Local study-map skill 1.3 (Infrastructure, Deployment, and CI/CD), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Evaluation after promotion cannot gate the release. Why the correct answer wins: Resources and deployment come first, app configuration follows, and evaluation gates promotion.
- **B:** Correct. Provisioning and deployment precede app configuration, and evaluation gates promotion. In this case: Resources and deployment come first, app configuration follows, and evaluation gates promotion.
- **C:** Incorrect for this question. Promotion before provisioning and evaluation skips the controls that make deployment safe. Why the correct answer wins: Resources and deployment come first, app configuration follows, and evaluation gates promotion.
- **D:** Incorrect for this question. Evaluation before any deployment or configuration has nothing meaningful to assess. Why the correct answer wins: Resources and deployment come first, app configuration follows, and evaluation gates promotion.

### Question 6 — A

Answer: Use private endpoints and disable public network access. A private endpoint with public access disabled keeps model traffic on the private network path. Private connectivity keeps service traffic on approved network paths. Pair it with private DNS so clients resolve the private address. Local study-map skill 1.3 (Infrastructure, Deployment, and CI/CD), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. Private connectivity keeps service traffic on approved network paths. Pair it with private DNS so clients resolve the private address. In this case: A private endpoint with public access disabled keeps model traffic on the private network path.
- **B:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: A private endpoint with public access disabled keeps model traffic on the private network path.
- **C:** Incorrect for this question. Repeatable deployments reduce configuration drift. Include model deployments, indexes, and connections in review and promotion. Why the correct answer wins: A private endpoint with public access disabled keeps model traffic on the private network path.
- **D:** Incorrect for this question. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. Why the correct answer wins: A private endpoint with public access disabled keeps model traffic on the private network path.

### Question 7 — C

Answer: Plan for model quota expressed in tokens and requests per minute. Request and token quota must cover realistic peak concurrency. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. Local study-map skill 1.4 (Quotas, Scaling, and Cost), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Retries, tool calls, evaluation, and review contribute to unit economics. Per-outcome cost supports better optimization. Why the correct answer wins: Request and token quota must cover realistic peak concurrency.
- **B:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: Request and token quota must cover realistic peak concurrency.
- **C:** Correct. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. In this case: Request and token quota must cover realistic peak concurrency.
- **D:** Incorrect for this question. User behavior, data, and models change. Rolling baselines reveal degradation that a one-time evaluation misses. Why the correct answer wins: Request and token quota must cover realistic peak concurrency.

### Question 8 — D

Answer: Use supported prompt or response caching where appropriate. Prompt caching reuses the repeated preamble instead of re-billing it on each call. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Local study-map skill 1.4 (Quotas, Scaling, and Cost), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: Prompt caching reuses the repeated preamble instead of re-billing it on each call.
- **B:** Incorrect for this question. Retries, tool calls, evaluation, and review contribute to unit economics. Per-outcome cost supports better optimization. Why the correct answer wins: Prompt caching reuses the repeated preamble instead of re-billing it on each call.
- **C:** Incorrect for this question. Batch deployments can lower cost for large asynchronous jobs. They are unsuitable for interactive agent turns. Why the correct answer wins: Prompt caching reuses the repeated preamble instead of re-billing it on each call.
- **D:** Correct. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. In this case: Prompt caching reuses the repeated preamble instead of re-billing it on each call.

### Question 9 — B

Answer: Monitor input and quality drift over time. Input drift in audio characteristics explains quality changes that code changes do not. User behavior, data, and models change. Rolling baselines reveal degradation that a one-time evaluation misses. Local study-map skill 1.5 (Monitoring Performance, Drift, Safety, and Grounding), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Input drift in audio characteristics explains quality changes that code changes do not.
- **B:** Correct. User behavior, data, and models change. Rolling baselines reveal degradation that a one-time evaluation misses. In this case: Input drift in audio characteristics explains quality changes that code changes do not.
- **C:** Incorrect for this question. Retries, tool calls, evaluation, and review contribute to unit economics. Per-outcome cost supports better optimization. Why the correct answer wins: Input drift in audio characteristics explains quality changes that code changes do not.
- **D:** Incorrect for this question. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. Why the correct answer wins: Input drift in audio characteristics explains quality changes that code changes do not.

### Question 10 — A

Answer: Authenticate with a managed identity instead of keys. A managed identity obtains Entra ID tokens without stored credentials. Managed identities avoid embedded secrets and support role-based access. Assign only required data-plane roles. Local study-map skill 1.6 (Security, Identity, and Networking), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. Managed identities avoid embedded secrets and support role-based access. Assign only required data-plane roles. In this case: A managed identity obtains Entra ID tokens without stored credentials.
- **B:** Incorrect for this question. A shared secret grants broad access, cannot be scoped per workload, and complicates rotation and auditing. Why the correct answer wins: A managed identity obtains Entra ID tokens without stored credentials.
- **C:** Incorrect for this question. A managed secret store supports rotation and access control. Secrets should never appear in prompts, code, or logs. Why the correct answer wins: A managed identity obtains Entra ID tokens without stored credentials.
- **D:** Incorrect for this question. Static keys are easily leaked, hard to rotate across services, and provide no per-identity authorization. Why the correct answer wins: A managed identity obtains Entra ID tokens without stored credentials.

### Question 11 — B, C

Answers: Authenticate with a managed identity instead of keys; Use least-privilege Azure RBAC roles for the workload identity. Use a managed identity for authentication and a least-privilege role for authorization. Managed identities avoid embedded secrets and support role-based access. Assign only required data-plane roles. Roles should match the operations the app or agent performs. Broad contributor access increases blast radius. Local study-map skill 1.6 (Security, Identity, and Networking), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Private connectivity keeps service traffic on approved network paths. Pair it with private DNS so clients resolve the private address. Why the correct answer wins: Use a managed identity for authentication and a least-privilege role for authorization.
- **B:** Correct. Roles should match the operations the app or agent performs. Broad contributor access increases blast radius. In this case: Use a managed identity for authentication and a least-privilege role for authorization.
- **C:** Correct. Managed identities avoid embedded secrets and support role-based access. Assign only required data-plane roles. In this case: Use a managed identity for authentication and a least-privilege role for authorization.
- **D:** Incorrect for this question. A managed secret store supports rotation and access control. Secrets should never appear in prompts, code, or logs. Why the correct answer wins: Use a managed identity for authentication and a least-privilege role for authorization.
- **E:** Incorrect for this question. Filters assign severity and can block or annotate content. Thresholds should reflect the use case and applicable policy. Why the correct answer wins: Use a managed identity for authentication and a least-privilege role for authorization.

### Question 12 — A, D

Answers: Configure content safety filters for harmful categories; Require human approval before consequential actions. Content filters reduce harmful output, and approval gates control outbound patient messages. Filters assign severity and can block or annotate content. Thresholds should reflect the use case and applicable policy. Approval must occur before the effect and identify who approved what. A model confidence score is not approval. Local study-map skill 1.7 (Responsible AI Controls and Oversight), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. Filters assign severity and can block or annotate content. Thresholds should reflect the use case and applicable policy. In this case: Content filters reduce harmful output, and approval gates control outbound patient messages.
- **B:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Content filters reduce harmful output, and approval gates control outbound patient messages.
- **C:** Incorrect for this question. Small models can reduce latency and cost for constrained classification or extraction. Confirm quality on representative data before standardizing. Why the correct answer wins: Content filters reduce harmful output, and approval gates control outbound patient messages.
- **D:** Correct. Approval must occur before the effect and identify who approved what. A model confidence score is not approval. In this case: Content filters reduce harmful output, and approval gates control outbound patient messages.
- **E:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Content filters reduce harmful output, and approval gates control outbound patient messages.

### Question 13 — A

Answer: Route low-confidence or high-impact results to human review. Allergy content is high-risk, so uncertain summaries must be reviewed by a clinician before use. Review targets uncertainty and consequence rather than every item. Define who decides and what evidence they receive. Local study-map skill 1.7 (Responsible AI Controls and Oversight), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. Review targets uncertainty and consequence rather than every item. Define who decides and what evidence they receive. In this case: Allergy content is high-risk, so uncertain summaries must be reviewed by a clinician before use.
- **B:** Incorrect for this question. Guardrails are technical controls, not prompt suggestions. Validate inputs, authorize tools, and limit egress. Why the correct answer wins: Allergy content is high-risk, so uncertain summaries must be reviewed by a clinician before use.
- **C:** Incorrect for this question. Approval must occur before the effect and identify who approved what. A model confidence score is not approval. Why the correct answer wins: Allergy content is high-risk, so uncertain summaries must be reviewed by a clinician before use.
- **D:** Incorrect for this question. Oversight settings bound what an agent may do autonomously. They should be tested against realistic misuse and failure. Why the correct answer wins: Allergy content is high-risk, so uncertain summaries must be reviewed by a clinician before use.

### Question 14 — B

Answer: Ground responses with retrieval-augmented generation. RAG retrieves approved current evidence and supports source citations. RAG supplies selected source content at request time so answers can cite current evidence. It reduces but does not eliminate fabrication. Local study-map skill 2.1 (Building Generative Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Filters assign severity and can block or annotate content. Thresholds should reflect the use case and applicable policy. Why the correct answer wins: RAG retrieves approved current evidence and supports source citations.
- **B:** Correct. RAG supplies selected source content at request time so answers can cite current evidence. It reduces but does not eliminate fabrication. In this case: RAG retrieves approved current evidence and supports source citations.
- **C:** Incorrect for this question. The catalog shows supported models with capability, modality, region, and lifecycle details. Verify availability for your subscription and region before designing around one model. Why the correct answer wins: RAG retrieves approved current evidence and supports source citations.
- **D:** Incorrect for this question. Routing can balance quality and cost. Fallback and evaluation are required. Why the correct answer wins: RAG retrieves approved current evidence and supports source citations.

### Question 15 — D

Answer: Design multistep workflows with explicit checkpoints. Staged steps with validation checkpoints stop unverified extraction from reaching patients. Checkpoints validate intermediate results before later steps depend on them. This limits error propagation. Local study-map skill 2.1 (Building Generative Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. A single call cannot validate intermediate results or fetch authoritative evidence, so it is unsuitable for multi-stage or grounded workflows. Why the correct answer wins: Staged steps with validation checkpoints stop unverified extraction from reaching patients.
- **B:** Incorrect for this question. Templates improve consistency and reviewability. Version them and test changes. Why the correct answer wins: Staged steps with validation checkpoints stop unverified extraction from reaching patients.
- **C:** Incorrect for this question. Autonomous workflows need bounded actions and escalation. Unbounded loops and broad tools increase risk. Why the correct answer wins: Staged steps with validation checkpoints stop unverified extraction from reaching patients.
- **D:** Correct. Checkpoints validate intermediate results before later steps depend on them. This limits error propagation. In this case: Staged steps with validation checkpoints stop unverified extraction from reaching patients.

### Question 16 — B

Answer: Connect the application to the Foundry project endpoint. The project endpoint binds the client to the approved project and its deployments. Project endpoints and SDK clients bind an app to approved models and resources. Use identity-based authentication and environment-specific configuration. Local study-map skill 2.2 (Foundry SDK and Project Integration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. A managed secret store supports rotation and access control. Secrets should never appear in prompts, code, or logs. Why the correct answer wins: The project endpoint binds the client to the approved project and its deployments.
- **B:** Correct. Project endpoints and SDK clients bind an app to approved models and resources. Use identity-based authentication and environment-specific configuration. In this case: The project endpoint binds the client to the approved project and its deployments.
- **C:** Incorrect for this question. The catalog shows supported models with capability, modality, region, and lifecycle details. Verify availability for your subscription and region before designing around one model. Why the correct answer wins: The project endpoint binds the client to the approved project and its deployments.
- **D:** Incorrect for this question. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. Why the correct answer wins: The project endpoint binds the client to the approved project and its deployments.

### Question 17 — A

Answer: Use a Foundry SDK or supported connector from application code. A supported Foundry SDK provides maintained client behavior instead of hand-built HTTP calls. SDKs provide supported request and response patterns. Pin versions and handle retries, timeouts, and errors explicitly. Local study-map skill 2.2 (Foundry SDK and Project Integration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. SDKs provide supported request and response patterns. Pin versions and handle retries, timeouts, and errors explicitly. In this case: A supported Foundry SDK provides maintained client behavior instead of hand-built HTTP calls.
- **B:** Incorrect for this question. Manual portal changes work for exploration but are slow, undocumented, and hard to reproduce, so they are a poor fit for governed release processes. Why the correct answer wins: A supported Foundry SDK provides maintained client behavior instead of hand-built HTTP calls.
- **C:** Incorrect for this question. Repeatable deployments reduce configuration drift. Include model deployments, indexes, and connections in review and promotion. Why the correct answer wins: A supported Foundry SDK provides maintained client behavior instead of hand-built HTTP calls.
- **D:** Incorrect for this question. Batch deployments can lower cost for large asynchronous jobs. They are unsuitable for interactive agent turns. Why the correct answer wins: A supported Foundry SDK provides maintained client behavior instead of hand-built HTTP calls.

### Question 18 — C, D

Answers: Require citations tied to retrieved evidence; Return a defined JSON schema for downstream systems. Citations support verification, and structured output supports reliable record creation. Citations let users verify claims and support auditing. Preserve source and chunk identifiers through the pipeline. Structured output supports validation and automation. Schema validity does not prove semantic correctness. Local study-map skill 2.3 (Evaluating Models and Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Citations support verification, and structured output supports reliable record creation.
- **B:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: Citations support verification, and structured output supports reliable record creation.
- **C:** Correct. Citations let users verify claims and support auditing. Preserve source and chunk identifiers through the pipeline. In this case: Citations support verification, and structured output supports reliable record creation.
- **D:** Correct. Structured output supports validation and automation. Schema validity does not prove semantic correctness. In this case: Citations support verification, and structured output supports reliable record creation.
- **E:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Citations support verification, and structured output supports reliable record creation.

### Question 19 — A

Answer: Detect fabricated or unsupported statements. Fabrication measures claims unsupported by evidence, which fluency does not detect. Fabrication checks compare claims with evidence. Fluency and confidence are not evidence of accuracy. Local study-map skill 2.3 (Evaluating Models and Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Fabrication checks compare claims with evidence. Fluency and confidence are not evidence of accuracy. In this case: Fabrication measures claims unsupported by evidence, which fluency does not detect.
- **B:** Incorrect for this question. Coherence checks readability and internal consistency. It does not establish factual accuracy. Why the correct answer wins: Fabrication measures claims unsupported by evidence, which fluency does not detect.
- **C:** Incorrect for this question. Relevance covers both retrieval and response usefulness. A correct but off-topic answer still fails. Why the correct answer wins: Fabrication measures claims unsupported by evidence, which fluency does not detect.
- **D:** Incorrect for this question. Tone analysis supports brand and customer communication. Context and culture affect interpretation. Why the correct answer wins: Fabrication measures claims unsupported by evidence, which fluency does not detect.

### Question 20 — A

Answer: Define narrow tool schemas with clear descriptions. A precise, narrow tool schema helps the model choose and populate arguments correctly. Precise schemas help the model choose tools and arguments correctly. Broad or ambiguous tools invite unsafe calls. Local study-map skill 2.4 (Agent Roles, Goals, and Tool Schemas), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Precise schemas help the model choose tools and arguments correctly. Broad or ambiguous tools invite unsafe calls. In this case: A precise, narrow tool schema helps the model choose and populate arguments correctly.
- **B:** Incorrect for this question. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Why the correct answer wins: A precise, narrow tool schema helps the model choose and populate arguments correctly.
- **C:** Incorrect for this question. System messages define role and constraints. They are not a security boundary against injection. Why the correct answer wins: A precise, narrow tool schema helps the model choose and populate arguments correctly.
- **D:** Incorrect for this question. Templates improve consistency and reviewability. Version them and test changes. Why the correct answer wins: A precise, narrow tool schema helps the model choose and populate arguments correctly.

### Question 21 — D

Answer: Put stable behavior rules in the system message. The system message carries persistent behavioral guidance, though it is not an authorization control. System messages define role and constraints. They are not a security boundary against injection. Local study-map skill 2.4 (Agent Roles, Goals, and Tool Schemas), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Guardrails are technical controls, not prompt suggestions. Validate inputs, authorize tools, and limit egress. Why the correct answer wins: The system message carries persistent behavioral guidance, though it is not an authorization control.
- **B:** Incorrect for this question. Roles should match the operations the app or agent performs. Broad contributor access increases blast radius. Why the correct answer wins: The system message carries persistent behavioral guidance, though it is not an authorization control.
- **C:** Incorrect for this question. Filters assign severity and can block or annotate content. Thresholds should reflect the use case and applicable policy. Why the correct answer wins: The system message carries persistent behavioral guidance, though it is not an authorization control.
- **D:** Correct. System messages define role and constraints. They are not a security boundary against injection. In this case: The system message carries persistent behavioral guidance, though it is not an authorization control.

### Question 22 — B

Answer: Expose an OpenAPI operation as an agent tool. An OpenAPI tool reuses the published contract without hand-written function wrappers. OpenAPI tools describe supported HTTP operations for agent use. Narrow operations, validate inputs, and authenticate the caller. Local study-map skill 2.5 (Agent Tools, Retrieval, Memory, and Function Calling), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. RAG supplies selected source content at request time so answers can cite current evidence. It reduces but does not eliminate fabrication. Why the correct answer wins: An OpenAPI tool reuses the published contract without hand-written function wrappers.
- **B:** Correct. OpenAPI tools describe supported HTTP operations for agent use. Narrow operations, validate inputs, and authenticate the caller. In this case: An OpenAPI tool reuses the published contract without hand-written function wrappers.
- **C:** Incorrect for this question. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Why the correct answer wins: An OpenAPI tool reuses the published contract without hand-written function wrappers.
- **D:** Incorrect for this question. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. Why the correct answer wins: An OpenAPI tool reuses the published contract without hand-written function wrappers.

### Question 23 — A, E

Answers: Persist conversation history in a thread or session; Expose a typed function as an agent tool. Conversation state preserves the referral number, and a function tool performs the lookup. Threads support continuity across turns. Apply retention and access controls to stored history. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. Local study-map skill 2.5 (Agent Tools, Retrieval, Memory, and Function Calling), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. In this case: Conversation state preserves the referral number, and a function tool performs the lookup.
- **B:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Conversation state preserves the referral number, and a function tool performs the lookup.
- **C:** Incorrect for this question. Embeddings determine semantic similarity behavior. Evaluate retrieval quality before and after changes. Why the correct answer wins: Conversation state preserves the referral number, and a function tool performs the lookup.
- **D:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: Conversation state preserves the referral number, and a function tool performs the lookup.
- **E:** Correct. Threads support continuity across turns. Apply retention and access controls to stored history. In this case: Conversation state preserves the referral number, and a function tool performs the lookup.

### Question 24 — C

Answer: Define role and goal → configure tools → attach knowledge → evaluate in sandbox → deploy with monitoring. The role is defined first, tools and knowledge follow, and evaluation precedes deployment. An agent is defined before it is connected to tools and knowledge, and evaluation precedes deployment. Local study-map skill 2.6 (Multi-Agent Orchestration and Safeguards), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Deployment before the agent is defined, connected, or evaluated removes every control. Why the correct answer wins: The role is defined first, tools and knowledge follow, and evaluation precedes deployment.
- **B:** Incorrect for this question. Tools configured before the role exists, and evaluation after deployment gates nothing. Why the correct answer wins: The role is defined first, tools and knowledge follow, and evaluation precedes deployment.
- **C:** Correct. An agent is defined before it is connected to tools and knowledge, and evaluation precedes deployment. In this case: The role is defined first, tools and knowledge follow, and evaluation precedes deployment.
- **D:** Incorrect for this question. The agent must be defined first, and evaluation must precede deployment. Why the correct answer wins: The role is defined first, tools and knowledge follow, and evaluation precedes deployment.

### Question 25 — A

Answer: Transfer control between agents with explicit context. Handoff transfers control and context to the specialist agent. Handoffs should carry goal, evidence, permissions, and open questions. Implicit context is easily lost. Local study-map skill 2.6 (Multi-Agent Orchestration and Safeguards), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Handoffs should carry goal, evidence, permissions, and open questions. Implicit context is easily lost. In this case: Handoff transfers control and context to the specialist agent.
- **B:** Incorrect for this question. Sequential orchestration makes dependencies explicit. It may add latency where steps could run concurrently. Why the correct answer wins: Handoff transfers control and context to the specialist agent.
- **C:** Incorrect for this question. Reflection can catch omissions and inconsistencies. It can also reinforce errors, so validate against evidence. Why the correct answer wins: Handoff transfers control and context to the specialist agent.
- **D:** Incorrect for this question. Parallel execution reduces wall-clock time for independent work. Reconciliation still requires design. Why the correct answer wins: Handoff transfers control and context to the specialist agent.

### Question 26 — C

Answer: Enable tracing across agent, model, and tool calls. Distributed tracing shows each model and tool call in order. Traces localize failures and latency in multi-step workflows. Correlate them with evaluation results and deployment versions. Local study-map skill 2.7 (Agent Monitoring and Error Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Distributed tracing shows each model and tool call in order.
- **B:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Distributed tracing shows each model and tool call in order.
- **C:** Correct. Traces localize failures and latency in multi-step workflows. Correlate them with evaluation results and deployment versions. In this case: Distributed tracing shows each model and tool call in order.
- **D:** Incorrect for this question. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. Why the correct answer wins: Distributed tracing shows each model and tool call in order.

### Question 27 — A

Answer: Lower temperature for more deterministic extraction. Lower temperature reduces sampling variability for deterministic extraction. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Local study-map skill 2.8 (Generation Tuning and Observability), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Lower temperature reduces sampling variability. It does not guarantee factual correctness. In this case: Lower temperature reduces sampling variability for deterministic extraction.
- **B:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Lower temperature reduces sampling variability for deterministic extraction.
- **C:** Incorrect for this question. Routing can balance quality and cost. Fallback and evaluation are required. Why the correct answer wins: Lower temperature reduces sampling variability for deterministic extraction.
- **D:** Incorrect for this question. Top-p narrows or broadens token sampling. Tune with evaluation rather than by intuition. Why the correct answer wins: Lower temperature reduces sampling variability for deterministic extraction.

### Question 28 — C

Answer: Apply prompt-driven image modifications. Targeted image editing removes the badge while leaving the rest of the photo intact. Prompt-based edits can alter style or content. Review outputs for unintended changes and policy violations. Local study-map skill 3.1 (Image Generation and Editing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Inpainting changes a selected area while preserving the rest. Validate identity, brand, and safety constraints. Why the correct answer wins: Targeted image editing removes the badge while leaving the rest of the photo intact.
- **B:** Incorrect for this question. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Why the correct answer wins: Targeted image editing removes the badge while leaving the rest of the photo intact.
- **C:** Correct. Prompt-based edits can alter style or content. Review outputs for unintended changes and policy violations. In this case: Targeted image editing removes the badge while leaving the rest of the photo intact.
- **D:** Incorrect for this question. Video generation creates clips from prompts or images. Duration, consistency, and safety require review. Why the correct answer wins: Targeted image editing removes the badge while leaving the rest of the photo intact.

### Question 29 — D

Answer: Generate images from text and reference media. Image generation produces a new illustration from a description. Image generation supports creative and product workflows. Apply policy, watermarking, and provenance controls. Local study-map skill 3.1 (Image Generation and Editing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Video generation creates clips from prompts or images. Duration, consistency, and safety require review. Why the correct answer wins: Image generation produces a new illustration from a description.
- **B:** Incorrect for this question. Alt text should convey purpose and essential content, not decorative detail. Human review is still needed for critical pages. Why the correct answer wins: Image generation produces a new illustration from a description.
- **C:** Incorrect for this question. Inpainting changes a selected area while preserving the rest. Validate identity, brand, and safety constraints. Why the correct answer wins: Image generation produces a new illustration from a description.
- **D:** Correct. Image generation supports creative and product workflows. Apply policy, watermarking, and provenance controls. In this case: Image generation produces a new illustration from a description.

### Question 30 — B

Answer: Analyze video segments for events and content. Video analysis locates events and timestamps within recorded footage. Video analysis can summarize or detect events across time. Sampling strategy affects coverage and cost. Local study-map skill 3.2 (Video Generation and Editing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Prompt-based edits can alter style or content. Review outputs for unintended changes and policy violations. Why the correct answer wins: Video analysis locates events and timestamps within recorded footage.
- **B:** Correct. Video analysis can summarize or detect events across time. Sampling strategy affects coverage and cost. In this case: Video analysis locates events and timestamps within recorded footage.
- **C:** Incorrect for this question. Video editing can revise scenes or timing. Preserve provenance and review for harmful manipulation. Why the correct answer wins: Video analysis locates events and timestamps within recorded footage.
- **D:** Incorrect for this question. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Why the correct answer wins: Video analysis locates events and timestamps within recorded footage.

### Question 31 — A, B

Answers: Generate alt text aligned to accessibility guidance; Answer questions grounded in visual evidence. Alt text serves accessibility, and visual question answering grounds answers in the chart content. Alt text should convey purpose and essential content, not decorative detail. Human review is still needed for critical pages. Visual question answering should cite the relevant region or content. Avoid answering beyond what the image supports. Local study-map skill 3.3 (Multimodal Understanding and Accessibility), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Correct. Visual question answering should cite the relevant region or content. Avoid answering beyond what the image supports. In this case: Alt text serves accessibility, and visual question answering grounds answers in the chart content.
- **B:** Correct. Alt text should convey purpose and essential content, not decorative detail. Human review is still needed for critical pages. In this case: Alt text serves accessibility, and visual question answering grounds answers in the chart content.
- **C:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Alt text serves accessibility, and visual question answering grounds answers in the chart content.
- **D:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Alt text serves accessibility, and visual question answering grounds answers in the chart content.
- **E:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: Alt text serves accessibility, and visual question answering grounds answers in the chart content.

### Question 32 — C

Answer: Generate concise or detailed image captions. A caption produces a concise natural-language description. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Local study-map skill 3.3 (Multimodal Understanding and Accessibility), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Detection returns locations and labels for visual elements. Validate classes and thresholds against the use case. Why the correct answer wins: A caption produces a concise natural-language description.
- **B:** Incorrect for this question. Typed fields feed downstream systems directly. Add validation and confidence thresholds before automated action. Why the correct answer wins: A caption produces a concise natural-language description.
- **C:** Correct. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. In this case: A caption produces a concise natural-language description.
- **D:** Incorrect for this question. OCR unlocks text in scans and screenshots. Layout and table structure may still require specialized extraction. Why the correct answer wins: A caption produces a concise natural-language description.

### Question 33 — A

Answer: Upload image → validate format and size → send multimodal request → parse structured fields → route low-confidence values to review. Validation brackets the multimodal call, and low-confidence output goes to people. Validation and structured parsing bracket the multimodal call, and low-confidence output goes to people. Local study-map skill 3.4 (Visual Extraction and Video Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Correct. Validation and structured parsing bracket the multimodal call, and low-confidence output goes to people. In this case: Validation brackets the multimodal call, and low-confidence output goes to people.
- **B:** Incorrect for this question. Parsing requires a response, which requires an uploaded and validated image. Why the correct answer wins: Validation brackets the multimodal call, and low-confidence output goes to people.
- **C:** Incorrect for this question. Review cannot precede the request, and parsing must follow the response. Why the correct answer wins: Validation brackets the multimodal call, and low-confidence output goes to people.
- **D:** Incorrect for this question. A request cannot precede the upload, and validation must come before the call. Why the correct answer wins: Validation brackets the multimodal call, and low-confidence output goes to people.

### Question 34 — D

Answer: Filter unsafe or disallowed visual content. A visual safety filter blocks or flags unsafe generated imagery. Image and video safety filters reduce exposure to harmful content. Thresholds and human escalation should match policy. Local study-map skill 3.5 (Multimodal Responsible AI), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: A visual safety filter blocks or flags unsafe generated imagery.
- **B:** Incorrect for this question. Visible instructions in images can attempt to manipulate an agent. Isolate, detect, and never let image text grant authority. Why the correct answer wins: A visual safety filter blocks or flags unsafe generated imagery.
- **C:** Incorrect for this question. Brand controls define permitted logos, styles, and claims. Technical generation must still pass approval. Why the correct answer wins: A visual safety filter blocks or flags unsafe generated imagery.
- **D:** Correct. Image and video safety filters reduce exposure to harmful content. Thresholds and human escalation should match policy. In this case: A visual safety filter blocks or flags unsafe generated imagery.

### Question 35 — A

Answer: Prompt for JSON that conforms to a supplied schema. Schema-constrained JSON supports validation and automated record creation. Schema-guided generation improves machine readability. Validate values against source evidence and business rules. Local study-map skill 4.1 (Language Model Text Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Correct. Schema-guided generation improves machine readability. Validate values against source evidence and business rules. In this case: Schema-constrained JSON supports validation and automated record creation.
- **B:** Incorrect for this question. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Why the correct answer wins: Schema-constrained JSON supports validation and automated record creation.
- **C:** Incorrect for this question. Translation should preserve meaning, names, and formatting. Evaluate domain terminology and low-resource languages. Why the correct answer wins: Schema-constrained JSON supports validation and automated record creation.
- **D:** Incorrect for this question. Topic extraction supports discovery and grouping. It is not a substitute for an authoritative taxonomy. Why the correct answer wins: Schema-constrained JSON supports validation and automated record creation.

### Question 36 — C, E

Answers: Detect and redact sensitive personal data; Analyze sentiment and tone with an appropriate service. PII detection addresses disclosure risk, and sentiment surfaces frustration. Sensitive Data Protection or language PII detection can identify and mask data. Verify that redaction covers every path where content flows. Sentiment analysis can support triage and monitoring. Domain and language variation require validation. Local study-map skill 4.1 (Language Model Text Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Why the correct answer wins: PII detection addresses disclosure risk, and sentiment surfaces frustration.
- **B:** Incorrect for this question. Topic extraction supports discovery and grouping. It is not a substitute for an authoritative taxonomy. Why the correct answer wins: PII detection addresses disclosure risk, and sentiment surfaces frustration.
- **C:** Correct. Sentiment analysis can support triage and monitoring. Domain and language variation require validation. In this case: PII detection addresses disclosure risk, and sentiment surfaces frustration.
- **D:** Incorrect for this question. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Why the correct answer wins: PII detection addresses disclosure risk, and sentiment surfaces frustration.
- **E:** Correct. Sensitive Data Protection or language PII detection can identify and mask data. Verify that redaction covers every path where content flows. In this case: PII detection addresses disclosure risk, and sentiment surfaces frustration.

### Question 37 — A

Answer: Use Azure Translator or a language model for translation. Machine translation renders approved text into the target language. Translation should preserve meaning, names, and formatting. Evaluate domain terminology and low-resource languages. Local study-map skill 4.2 (Translation), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Correct. Translation should preserve meaning, names, and formatting. Evaluate domain terminology and low-resource languages. In this case: Machine translation renders approved text into the target language.
- **B:** Incorrect for this question. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Why the correct answer wins: Machine translation renders approved text into the target language.
- **C:** Incorrect for this question. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Why the correct answer wins: Machine translation renders approved text into the target language.
- **D:** Incorrect for this question. Sensitive Data Protection or language PII detection can identify and mask data. Verify that redaction covers every path where content flows. Why the correct answer wins: Machine translation renders approved text into the target language.

### Question 38 — C

Answer: Transcribe speech to text with Azure AI Speech. Speech-to-text transcribes recordings into searchable content. Speech-to-text enables voice agents and transcript analysis. Audio quality, accents, and domain terms affect accuracy. Local study-map skill 4.3 (Speech Solutions), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Text-to-speech supports voice responses and accessibility. Voice, prosody, and latency affect usability. Why the correct answer wins: Speech-to-text transcribes recordings into searchable content.
- **B:** Incorrect for this question. Speech translation combines recognition and translation. Preserve timing and speaker context where needed. Why the correct answer wins: Speech-to-text transcribes recordings into searchable content.
- **C:** Correct. Speech-to-text enables voice agents and transcript analysis. Audio quality, accents, and domain terms affect accuracy. In this case: Speech-to-text transcribes recordings into searchable content.
- **D:** Incorrect for this question. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Why the correct answer wins: Speech-to-text transcribes recordings into searchable content.

### Question 39 — C

Answer: Use a custom speech model for specialized vocabulary. A custom speech model adapts acoustic and language behavior to the domain. Custom speech can improve recognition of domain terms. It requires representative audio and ongoing evaluation. Local study-map skill 4.3 (Speech Solutions), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Text-to-speech supports voice responses and accessibility. Voice, prosody, and latency affect usability. Why the correct answer wins: A custom speech model adapts acoustic and language behavior to the domain.
- **B:** Incorrect for this question. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Why the correct answer wins: A custom speech model adapts acoustic and language behavior to the domain.
- **C:** Correct. Custom speech can improve recognition of domain terms. It requires representative audio and ongoing evaluation. In this case: A custom speech model adapts acoustic and language behavior to the domain.
- **D:** Incorrect for this question. Speech-to-text enables voice agents and transcript analysis. Audio quality, accents, and domain terms affect accuracy. Why the correct answer wins: A custom speech model adapts acoustic and language behavior to the domain.

### Question 40 — C

Answer: Adapt prompts and models to domain terminology. A validated domain lexicon teaches local terminology to the extraction step. Domain adaptation improves consistency and recall. Validate against expert-created expected outputs. Local study-map skill 4.4 (Domain Customization), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Sensitive Data Protection or language PII detection can identify and mask data. Verify that redaction covers every path where content flows. Why the correct answer wins: A validated domain lexicon teaches local terminology to the extraction step.
- **B:** Incorrect for this question. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Why the correct answer wins: A validated domain lexicon teaches local terminology to the extraction step.
- **C:** Correct. Domain adaptation improves consistency and recall. Validate against expert-created expected outputs. In this case: A validated domain lexicon teaches local terminology to the extraction step.
- **D:** Incorrect for this question. Translation should preserve meaning, names, and formatting. Evaluate domain terminology and low-resource languages. Why the correct answer wins: A validated domain lexicon teaches local terminology to the extraction step.

### Question 41 — C

Answer: Use an Azure AI Search indexer to pull source content. An indexer pulls content on a schedule and tracks source changes. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. Local study-map skill 5.1 (Content Ingestion and Indexing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. Push ingestion supports near-real-time updates from applications. The app owns batching, retries, and deletion. Why the correct answer wins: An indexer pulls content on a schedule and tracks source changes.
- **B:** Incorrect for this question. OCR unlocks text in scans and screenshots. Layout and table structure may still require specialized extraction. Why the correct answer wins: An indexer pulls content on a schedule and tracks source changes.
- **C:** Correct. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. In this case: An indexer pulls content on a schedule and tracks source changes.
- **D:** Incorrect for this question. Skillsets can OCR, split, embed, and extract during indexing. Each skill adds latency, cost, and failure modes. Why the correct answer wins: An indexer pulls content on a schedule and tracks source changes.

### Question 42 — A, D

Answers: Combine keyword and vector retrieval; Apply semantic ranking to reorder search results. Hybrid search covers exact and semantic matching, and semantic ranking improves ordering. Hybrid search covers exact identifiers and paraphrased meaning together. Fusion and ranking need testing on representative queries. A semantic ranker can improve relevance for natural-language queries. It adds cost and latency and should be measured against a baseline. Local study-map skill 5.2 (Search and Grounding Configuration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Correct. A semantic ranker can improve relevance for natural-language queries. It adds cost and latency and should be measured against a baseline. In this case: Hybrid search covers exact and semantic matching, and semantic ranking improves ordering.
- **B:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Hybrid search covers exact and semantic matching, and semantic ranking improves ordering.
- **C:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Hybrid search covers exact and semantic matching, and semantic ranking improves ordering.
- **D:** Correct. Hybrid search covers exact identifiers and paraphrased meaning together. Fusion and ranking need testing on representative queries. In this case: Hybrid search covers exact and semantic matching, and semantic ranking improves ordering.
- **E:** Incorrect for this question. Embeddings support similarity search over meaning rather than exact terms. Vector search still needs chunking, filtering, and evaluation. Why the correct answer wins: Hybrid search covers exact and semantic matching, and semantic ranking improves ordering.

### Question 43 — A

Answer: Add an enrichment skillset to an indexing pipeline. An enrichment skillset applies extraction and generation steps during indexing. Skillsets can OCR, split, embed, and extract during indexing. Each skill adds latency, cost, and failure modes. Local study-map skill 5.3 (Enrichment Skills), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Correct. Skillsets can OCR, split, embed, and extract during indexing. Each skill adds latency, cost, and failure modes. In this case: An enrichment skillset applies extraction and generation steps during indexing.
- **B:** Incorrect for this question. OCR unlocks text in scans and screenshots. Layout and table structure may still require specialized extraction. Why the correct answer wins: An enrichment skillset applies extraction and generation steps during indexing.
- **C:** Incorrect for this question. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. Why the correct answer wins: An enrichment skillset applies extraction and generation steps during indexing.
- **D:** Incorrect for this question. Push ingestion supports near-real-time updates from applications. The app owns batching, retries, and deletion. Why the correct answer wins: An enrichment skillset applies extraction and generation steps during indexing.

### Question 44 — A

Answer: Ingest → extract text → chunk → embed → index → retrieve with citations. Extraction, chunking, embedding, and indexing all precede retrieval and citation. The supported RAG ingestion order produces searchable, citable evidence. Retrieval cannot work before content is extracted, chunked, embedded, and indexed. Local study-map skill 5.4 (RAG Ingestion and OCR), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Correct. The supported RAG ingestion order produces searchable, citable evidence. Retrieval cannot work before content is extracted, chunked, embedded, and indexed. In this case: Extraction, chunking, embedding, and indexing all precede retrieval and citation.
- **B:** Incorrect for this question. Indexing before extraction or embedding creates an empty or unusable index. Why the correct answer wins: Extraction, chunking, embedding, and indexing all precede retrieval and citation.
- **C:** Incorrect for this question. Retrieval before chunking, embedding, and indexing has nothing searchable to return. Why the correct answer wins: Extraction, chunking, embedding, and indexing all precede retrieval and citation.
- **D:** Incorrect for this question. Retrieval is attempted before the index exists and source ingestion is incomplete. Why the correct answer wins: Extraction, chunking, embedding, and indexing all precede retrieval and citation.

### Question 45 — D

Answer: Pin the model version available in the required region. Pinning a version that exists in the required region satisfies both stability and residency. A pinned version keeps behavior stable and satisfies residency, at the cost of slower access to newer capabilities. Local study-map skill 1.1 (Selecting Foundry Models and Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Large models handle ambiguity and multi-step reasoning better in many cases, at higher cost and latency. Select with measured evidence rather than brand preference. Why the correct answer wins: Pinning a version that exists in the required region satisfies both stability and residency.
- **B:** Incorrect for this question. The catalog shows supported models with capability, modality, region, and lifecycle details. Verify availability for your subscription and region before designing around one model. Why the correct answer wins: Pinning a version that exists in the required region satisfies both stability and residency.
- **C:** Incorrect for this question. A custom model is justified when supported prebuilt options cannot meet a defined requirement. It adds data, evaluation, and lifecycle obligations. Why the correct answer wins: Pinning a version that exists in the required region satisfies both stability and residency.
- **D:** Correct. A pinned version keeps behavior stable and satisfies residency, at the cost of slower access to newer capabilities. In this case: Pinning a version that exists in the required region satisfies both stability and residency.

### Question 46 — C

Answer: Use Foundry Tools for prebuilt vision, speech, language, and extraction needs. Prebuilt managed capabilities deliver both without a training dataset. Prebuilt managed capabilities can reduce custom model work where their behavior and limits fit the task. They are not a substitute for task-specific validation. Local study-map skill 1.1 (Selecting Foundry Models and Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Small models can reduce latency and cost for constrained classification or extraction. Confirm quality on representative data before standardizing. Why the correct answer wins: Prebuilt managed capabilities deliver both without a training dataset.
- **B:** Incorrect for this question. A custom model is justified when supported prebuilt options cannot meet a defined requirement. It adds data, evaluation, and lifecycle obligations. Why the correct answer wins: Prebuilt managed capabilities deliver both without a training dataset.
- **C:** Correct. Prebuilt managed capabilities can reduce custom model work where their behavior and limits fit the task. They are not a substitute for task-specific validation. In this case: Prebuilt managed capabilities deliver both without a training dataset.
- **D:** Incorrect for this question. Large models handle ambiguity and multi-step reasoning better in many cases, at higher cost and latency. Select with measured evidence rather than brand preference. Why the correct answer wins: Prebuilt managed capabilities deliver both without a training dataset.

### Question 47 — D

Answer: Expose an OpenAPI operation as an agent tool. An OpenAPI tool reuses the published contract rather than hand-written wrappers. OpenAPI tools describe supported HTTP operations for agent use. Narrow operations, validate inputs, and authenticate the caller. Local study-map skill 1.2 (Retrieval, Memory, Tool, and Knowledge Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Why the correct answer wins: An OpenAPI tool reuses the published contract rather than hand-written wrappers.
- **B:** Incorrect for this question. An index gives an agent curated, searchable evidence under configured access. Index content and permissions require ongoing ownership. Why the correct answer wins: An OpenAPI tool reuses the published contract rather than hand-written wrappers.
- **C:** Incorrect for this question. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. Why the correct answer wins: An OpenAPI tool reuses the published contract rather than hand-written wrappers.
- **D:** Correct. OpenAPI tools describe supported HTTP operations for agent use. Narrow operations, validate inputs, and authenticate the caller. In this case: An OpenAPI tool reuses the published contract rather than hand-written wrappers.

### Question 48 — B

Answer: Send mirrored production traffic to a candidate without returning its answers. Shadow deployment mirrors traffic and discards the candidate's responses. Shadow traffic compares a candidate against live behavior with no user impact. It requires careful handling of side-effecting calls. Local study-map skill 1.3 (Infrastructure, Deployment, and CI/CD), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. A canary limits blast radius and produces real signal before full rollout. It needs a rollback criterion defined in advance. Why the correct answer wins: Shadow deployment mirrors traffic and discards the candidate's responses.
- **B:** Correct. Shadow traffic compares a candidate against live behavior with no user impact. It requires careful handling of side-effecting calls. In this case: Shadow deployment mirrors traffic and discards the candidate's responses.
- **C:** Incorrect for this question. Standard deployments bill per token and scale within quota. They suit spiky or early workloads. Why the correct answer wins: Shadow deployment mirrors traffic and discards the candidate's responses.
- **D:** Incorrect for this question. Batch deployments can lower cost for large asynchronous jobs. They are unsuitable for interactive agent turns. Why the correct answer wins: Shadow deployment mirrors traffic and discards the candidate's responses.

### Question 49 — A

Answer: Alert on spend thresholds per deployment or project. A spend alert notifies owners when usage crosses a threshold. Spend alerts catch runaway usage before the invoice does. They are detection, not a hard spending cap. Local study-map skill 1.4 (Quotas, Scaling, and Cost), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. Spend alerts catch runaway usage before the invoice does. They are detection, not a hard spending cap. In this case: A spend alert notifies owners when usage crosses a threshold.
- **B:** Incorrect for this question. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. Why the correct answer wins: A spend alert notifies owners when usage crosses a threshold.
- **C:** Incorrect for this question. Retries, tool calls, evaluation, and review contribute to unit economics. Per-outcome cost supports better optimization. Why the correct answer wins: A spend alert notifies owners when usage crosses a threshold.
- **D:** Incorrect for this question. Token analytics supports cost and performance tuning. Attribute usage to features and tenants where possible. Why the correct answer wins: A spend alert notifies owners when usage crosses a threshold.

### Question 50 — B

Answer: Monitor index freshness, failures, and document counts. Index health checks reveal stale content and failed updates. Stale or partially indexed content produces confident but wrong answers. Alert on ingestion and deletion failures. Local study-map skill 1.5 (Monitoring Performance, Drift, Safety, and Grounding), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Groundedness checks whether claims are supported by retrieved evidence. Sampling and human review complement automated scores. Why the correct answer wins: Index health checks reveal stale content and failed updates.
- **B:** Correct. Stale or partially indexed content produces confident but wrong answers. Alert on ingestion and deletion failures. In this case: Index health checks reveal stale content and failed updates.
- **C:** Incorrect for this question. Central telemetry captures latency, errors, dependencies, and custom events. Redact sensitive content before logging. Why the correct answer wins: Index health checks reveal stale content and failed updates.
- **D:** Incorrect for this question. User behavior, data, and models change. Rolling baselines reveal degradation that a one-time evaluation misses. Why the correct answer wins: Index health checks reveal stale content and failed updates.

### Question 51 — B

Answer: Restrict outbound network access to approved destinations. Egress rules restrict which external destinations the workload can reach, which is exactly the control the policy demands. Egress controls reduce exfiltration and unauthorized tool reach. Combine with identity and data controls. Local study-map skill 1.6 (Security, Identity, and Networking), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Private connectivity keeps service traffic on approved network paths. Pair it with private DNS so clients resolve the private address. Why the correct answer wins: Egress rules restrict which external destinations the workload can reach, which is exactly the control the policy demands.
- **B:** Correct. Egress controls reduce exfiltration and unauthorized tool reach. Combine with identity and data controls. In this case: Egress rules restrict which external destinations the workload can reach, which is exactly the control the policy demands.
- **C:** Incorrect for this question. Leaving the public path open defeats the purpose of a private networking design because traffic can still bypass the private route. Why the correct answer wins: Egress rules restrict which external destinations the workload can reach, which is exactly the control the policy demands.
- **D:** Incorrect for this question. Roles should match the operations the app or agent performs. Broad contributor access increases blast radius. Why the correct answer wins: Egress rules restrict which external destinations the workload can reach, which is exactly the control the policy demands.

### Question 52 — D

Answer: Set agent oversight mode and tool-access constraints. Human oversight keeps consequential decisions accountable. Oversight settings bound what an agent may do autonomously. They should be tested against realistic misuse and failure. Local study-map skill 1.7 (Responsible AI Controls and Oversight), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Guardrails are technical controls, not prompt suggestions. Validate inputs, authorize tools, and limit egress. Why the correct answer wins: Human oversight keeps consequential decisions accountable.
- **B:** Incorrect for this question. Audit evidence supports investigation and accountability. Protect log integrity and retention. Why the correct answer wins: Human oversight keeps consequential decisions accountable.
- **C:** Incorrect for this question. Approval must occur before the effect and identify who approved what. A model confidence score is not approval. Why the correct answer wins: Human oversight keeps consequential decisions accountable.
- **D:** Correct. Oversight settings bound what an agent may do autonomously. They should be tested against realistic misuse and failure. In this case: Human oversight keeps consequential decisions accountable.

### Question 53 — D

Answer: Block promotion in the pipeline when evaluation thresholds fail. An evaluation gate converts a measured result into a release decision. An automated gate turns an evaluation result into a release decision. Thresholds need ownership or the gate becomes noise. Local study-map skill 1.3 (Infrastructure, Deployment, and CI/CD), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Canary or phased rollout limits exposure. Rollback must be tested, not just documented. Why the correct answer wins: An evaluation gate converts a measured result into a release decision.
- **B:** Incorrect for this question. Repeatable deployments reduce configuration drift. Include model deployments, indexes, and connections in review and promotion. Why the correct answer wins: An evaluation gate converts a measured result into a release decision.
- **C:** Incorrect for this question. A canary limits blast radius and produces real signal before full rollout. It needs a rollback criterion defined in advance. Why the correct answer wins: An evaluation gate converts a measured result into a release decision.
- **D:** Correct. An automated gate turns an evaluation result into a release decision. Thresholds need ownership or the gate becomes noise. In this case: An evaluation gate converts a measured result into a release decision.

### Question 54 — C

Answer: Use batch processing for latency-tolerant bulk work. Batch deployment suits large asynchronous jobs. Batch deployments can lower cost for large asynchronous jobs. They are unsuitable for interactive agent turns. Local study-map skill 1.4 (Quotas, Scaling, and Cost), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. Why the correct answer wins: Batch deployment suits large asynchronous jobs.
- **B:** Incorrect for this question. Standard deployments bill per token and scale within quota. They suit spiky or early workloads. Why the correct answer wins: Batch deployment suits large asynchronous jobs.
- **C:** Correct. Batch deployments can lower cost for large asynchronous jobs. They are unsuitable for interactive agent turns. In this case: Batch deployment suits large asynchronous jobs.
- **D:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: Batch deployment suits large asynchronous jobs.

### Question 55 — A, D

Answers: Compare supported models in the Foundry model catalog; Pin the model version available in the required region. Catalog review confirms local availability, and version pinning prevents silent change. The catalog shows supported models with capability, modality, region, and lifecycle details. Verify availability for your subscription and region before designing around one model. A pinned version keeps behavior stable and satisfies residency, at the cost of slower access to newer capabilities. Local study-map skill 1.1 (Selecting Foundry Models and Services), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. The catalog shows supported models with capability, modality, region, and lifecycle details. Verify availability for your subscription and region before designing around one model. In this case: Catalog review confirms local availability, and version pinning prevents silent change.
- **B:** Incorrect for this question. A custom model is justified when supported prebuilt options cannot meet a defined requirement. It adds data, evaluation, and lifecycle obligations. Why the correct answer wins: Catalog review confirms local availability, and version pinning prevents silent change.
- **C:** Incorrect for this question. Standard deployments bill per token and scale within quota. They suit spiky or early workloads. Why the correct answer wins: Catalog review confirms local availability, and version pinning prevents silent change.
- **D:** Correct. A pinned version keeps behavior stable and satisfies residency, at the cost of slower access to newer capabilities. In this case: Catalog review confirms local availability, and version pinning prevents silent change.
- **E:** Incorrect for this question. Batch deployments can lower cost for large asynchronous jobs. They are unsuitable for interactive agent turns. Why the correct answer wins: Catalog review confirms local availability, and version pinning prevents silent change.

### Question 56 — A, B

Answers: Monitor groundedness and citation quality in production; Alert on latency, error rate, safety, and cost thresholds. Groundedness monitoring detects unsupported answers, and alerting notifies the team. Groundedness checks whether claims are supported by retrieved evidence. Sampling and human review complement automated scores. Alerts turn monitoring into action. Route them to an accountable owner with a runbook. Local study-map skill 1.5 (Monitoring Performance, Drift, Safety, and Grounding), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Correct. Alerts turn monitoring into action. Route them to an accountable owner with a runbook. In this case: Groundedness monitoring detects unsupported answers, and alerting notifies the team.
- **B:** Correct. Groundedness checks whether claims are supported by retrieved evidence. Sampling and human review complement automated scores. In this case: Groundedness monitoring detects unsupported answers, and alerting notifies the team.
- **C:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Groundedness monitoring detects unsupported answers, and alerting notifies the team.
- **D:** Incorrect for this question. Retries, tool calls, evaluation, and review contribute to unit economics. Per-outcome cost supports better optimization. Why the correct answer wins: Groundedness monitoring detects unsupported answers, and alerting notifies the team.
- **E:** Incorrect for this question. Users experience the whole path, not only generation. Optimize the dominant contributor. Why the correct answer wins: Groundedness monitoring detects unsupported answers, and alerting notifies the team.

### Question 57 — C, E

Answers: Restrict outbound network access to approved destinations; Use least-privilege Azure RBAC roles for the workload identity. Egress restrictions bound destinations, and least-privilege roles bound actions. Egress controls reduce exfiltration and unauthorized tool reach. Combine with identity and data controls. Roles should match the operations the app or agent performs. Broad contributor access increases blast radius. Local study-map skill 1.6 (Security, Identity, and Networking), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Filters assign severity and can block or annotate content. Thresholds should reflect the use case and applicable policy. Why the correct answer wins: Egress restrictions bound destinations, and least-privilege roles bound actions.
- **B:** Incorrect for this question. Private connectivity keeps service traffic on approved network paths. Pair it with private DNS so clients resolve the private address. Why the correct answer wins: Egress restrictions bound destinations, and least-privilege roles bound actions.
- **C:** Correct. Egress controls reduce exfiltration and unauthorized tool reach. Combine with identity and data controls. In this case: Egress restrictions bound destinations, and least-privilege roles bound actions.
- **D:** Incorrect for this question. A managed secret store supports rotation and access control. Secrets should never appear in prompts, code, or logs. Why the correct answer wins: Egress restrictions bound destinations, and least-privilege roles bound actions.
- **E:** Correct. Roles should match the operations the app or agent performs. Broad contributor access increases blast radius. In this case: Egress restrictions bound destinations, and least-privilege roles bound actions.

### Question 58 — D

Answer: Commit change → run the evaluation suite → block on failed thresholds → deploy a canary → promote after metrics hold. Evaluation gates deployment, then a canary precedes full promotion. An evaluation gate before deployment, followed by a canary, keeps unmeasured changes away from all users. Local study-map skill 1.3 (Infrastructure, Deployment, and CI/CD), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Deployment cannot precede the change, and evaluation must gate promotion rather than follow it. Why the correct answer wins: Evaluation gates deployment, then a canary precedes full promotion.
- **B:** Incorrect for this question. The change must exist before it can be evaluated or deployed. Why the correct answer wins: Evaluation gates deployment, then a canary precedes full promotion.
- **C:** Incorrect for this question. Evaluation after promotion cannot prevent a failed change from reaching everyone. Why the correct answer wins: Evaluation gates deployment, then a canary precedes full promotion.
- **D:** Correct. An evaluation gate before deployment, followed by a canary, keeps unmeasured changes away from all users. In this case: Evaluation gates deployment, then a canary precedes full promotion.

### Question 59 — A

Answer: Set chunk overlap so facts spanning a boundary stay retrievable. Overlap keeps facts that straddle a chunk boundary retrievable. Overlap preserves context across chunk edges at the cost of duplicated index storage and more near-duplicate hits. Local study-map skill 2.1 (Building Generative Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Overlap preserves context across chunk edges at the cost of duplicated index storage and more near-duplicate hits. In this case: Overlap keeps facts that straddle a chunk boundary retrievable.
- **B:** Incorrect for this question. Embeddings determine semantic similarity behavior. Evaluate retrieval quality before and after changes. Why the correct answer wins: Overlap keeps facts that straddle a chunk boundary retrievable.
- **C:** Incorrect for this question. Chunking affects recall, precision, and context use. Respect document structure and test against real questions. Why the correct answer wins: Overlap keeps facts that straddle a chunk boundary retrievable.
- **D:** Incorrect for this question. More retrieved text is not always better. Order and compress evidence to preserve decisive facts. Why the correct answer wins: Overlap keeps facts that straddle a chunk boundary retrievable.

### Question 60 — B

Answer: Ground responses with retrieval-augmented generation. Retrieval supplies current evidence with citations. RAG supplies selected source content at request time so answers can cite current evidence. It reduces but does not eliminate fabrication. Local study-map skill 2.1 (Building Generative Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Routing can balance quality and cost. Fallback and evaluation are required. Why the correct answer wins: Retrieval supplies current evidence with citations.
- **B:** Correct. RAG supplies selected source content at request time so answers can cite current evidence. It reduces but does not eliminate fabrication. In this case: Retrieval supplies current evidence with citations.
- **C:** Incorrect for this question. Examples clarify format and boundaries. They do not guarantee correctness on unseen inputs. Why the correct answer wins: Retrieval supplies current evidence with citations.
- **D:** Incorrect for this question. Checkpoints validate intermediate results before later steps depend on them. This limits error propagation. Why the correct answer wins: Retrieval supplies current evidence with citations.

### Question 61 — C

Answer: Use short-lived scoped access tokens for tool calls. A scoped access token limits the session and avoids long-lived secrets. Short-lived credentials reduce misuse risk. Never place tokens in prompts or logs. Local study-map skill 2.2 (Foundry SDK and Project Integration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. SDKs provide supported request and response patterns. Pin versions and handle retries, timeouts, and errors explicitly. Why the correct answer wins: A scoped access token limits the session and avoids long-lived secrets.
- **B:** Incorrect for this question. A managed secret store supports rotation and access control. Secrets should never appear in prompts, code, or logs. Why the correct answer wins: A scoped access token limits the session and avoids long-lived secrets.
- **C:** Correct. Short-lived credentials reduce misuse risk. Never place tokens in prompts or logs. In this case: A scoped access token limits the session and avoids long-lived secrets.
- **D:** Incorrect for this question. Managed identities avoid embedded secrets and support role-based access. Assign only required data-plane roles. Why the correct answer wins: A scoped access token limits the session and avoids long-lived secrets.

### Question 62 — A

Answer: Build a representative golden dataset from real tasks. A golden dataset fixes the inputs for a controlled comparison. A golden set anchors evaluation in expected behavior. Include edge cases and high-risk scenarios. Local study-map skill 2.3 (Evaluating Models and Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. A golden set anchors evaluation in expected behavior. Include edge cases and high-risk scenarios. In this case: A golden dataset fixes the inputs for a controlled comparison.
- **B:** Incorrect for this question. Evaluators provide repeatable signals across models and prompts. They must be calibrated against human judgment for high-impact work. Why the correct answer wins: A golden dataset fixes the inputs for a controlled comparison.
- **C:** Incorrect for this question. Controlled comparison supports evidence-based change. Avoid changing several variables at once. Why the correct answer wins: A golden dataset fixes the inputs for a controlled comparison.
- **D:** Incorrect for this question. Prompts, models, indexes, and tools all affect behavior. Regression tests catch unintended effects. Why the correct answer wins: A golden dataset fixes the inputs for a controlled comparison.

### Question 63 — C

Answer: Re-run evaluation suites after meaningful changes. Regression evaluation re-runs previously failing cases against the candidate, so a fixed defect cannot silently return. Prompts, models, indexes, and tools all affect behavior. Regression tests catch unintended effects. Local study-map skill 2.3 (Evaluating Models and Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. A golden set anchors evaluation in expected behavior. Include edge cases and high-risk scenarios. Why the correct answer wins: Regression evaluation re-runs previously failing cases against the candidate, so a fixed defect cannot silently return.
- **B:** Incorrect for this question. Evaluators provide repeatable signals across models and prompts. They must be calibrated against human judgment for high-impact work. Why the correct answer wins: Regression evaluation re-runs previously failing cases against the candidate, so a fixed defect cannot silently return.
- **C:** Correct. Prompts, models, indexes, and tools all affect behavior. Regression tests catch unintended effects. In this case: Regression evaluation re-runs previously failing cases against the candidate, so a fixed defect cannot silently return.
- **D:** Incorrect for this question. Safety evaluation complements content filters. Use representative adversarial inputs. Why the correct answer wins: Regression evaluation re-runs previously failing cases against the candidate, so a fixed defect cannot silently return.

### Question 64 — D

Answer: Give the agent a file-search tool over approved document stores. A file-search tool retrieves from curated stores under configured access. A file tool retrieves from curated stores under configured access. It still depends on indexing quality and permission filters. Local study-map skill 2.5 (Agent Tools, Retrieval, Memory, and Function Calling), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Why the correct answer wins: A file-search tool retrieves from curated stores under configured access.
- **B:** Incorrect for this question. RAG supplies selected source content at request time so answers can cite current evidence. It reduces but does not eliminate fabrication. Why the correct answer wins: A file-search tool retrieves from curated stores under configured access.
- **C:** Incorrect for this question. Code execution handles quantitative work the model cannot do reliably in text. The sandbox must be isolated and output must be validated. Why the correct answer wins: A file-search tool retrieves from curated stores under configured access.
- **D:** Correct. A file tool retrieves from curated stores under configured access. It still depends on indexing quality and permission filters. In this case: A file-search tool retrieves from curated stores under configured access.

### Question 65 — B

Answer: Transfer control between agents with explicit context. Handoff transfers control and context to the specialist. Handoffs should carry goal, evidence, permissions, and open questions. Implicit context is easily lost. Local study-map skill 2.6 (Multi-Agent Orchestration and Safeguards), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Reflection can catch omissions and inconsistencies. It can also reinforce errors, so validate against evidence. Why the correct answer wins: Handoff transfers control and context to the specialist.
- **B:** Correct. Handoffs should carry goal, evidence, permissions, and open questions. Implicit context is easily lost. In this case: Handoff transfers control and context to the specialist.
- **C:** Incorrect for this question. Parallel execution reduces wall-clock time for independent work. Reconciliation still requires design. Why the correct answer wins: Handoff transfers control and context to the specialist.
- **D:** Incorrect for this question. A manager routes tasks and merges results. Clear responsibility and failure handling are required. Why the correct answer wins: Handoff transfers control and context to the specialist.

### Question 66 — B

Answer: Use self-critique or reflection to improve drafts. Reflection adds a revision step before delivery. Reflection can catch omissions and inconsistencies. It can also reinforce errors, so validate against evidence. Local study-map skill 2.6 (Multi-Agent Orchestration and Safeguards), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Parallel execution reduces wall-clock time for independent work. Reconciliation still requires design. Why the correct answer wins: Reflection adds a revision step before delivery.
- **B:** Correct. Reflection can catch omissions and inconsistencies. It can also reinforce errors, so validate against evidence. In this case: Reflection adds a revision step before delivery.
- **C:** Incorrect for this question. Sequential orchestration makes dependencies explicit. It may add latency where steps could run concurrently. Why the correct answer wins: Reflection adds a revision step before delivery.
- **D:** Incorrect for this question. Handoffs should carry goal, evidence, permissions, and open questions. Implicit context is easily lost. Why the correct answer wins: Reflection adds a revision step before delivery.

### Question 67 — B

Answer: Set a stop sequence so generation ends at the intended boundary. A stop sequence ends generation at the intended boundary. A stop sequence truncates output at a defined marker, which keeps parsers from receiving trailing commentary. It must not appear inside legitimate content. Local study-map skill 2.8 (Generation Tuning and Observability), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Top-p narrows or broadens token sampling. Tune with evaluation rather than by intuition. Why the correct answer wins: A stop sequence ends generation at the intended boundary.
- **B:** Correct. A stop sequence truncates output at a defined marker, which keeps parsers from receiving trailing commentary. It must not appear inside legitimate content. In this case: A stop sequence ends generation at the intended boundary.
- **C:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: A stop sequence ends generation at the intended boundary.
- **D:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: A stop sequence ends generation at the intended boundary.

### Question 68 — A

Answer: Adjust top-p to control response diversity. Nucleus sampling widens the candidate set. Top-p narrows or broadens token sampling. Tune with evaluation rather than by intuition. Local study-map skill 2.8 (Generation Tuning and Observability), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Top-p narrows or broadens token sampling. Tune with evaluation rather than by intuition. In this case: Nucleus sampling widens the candidate set.
- **B:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Nucleus sampling widens the candidate set.
- **C:** Incorrect for this question. A seed makes repeated sampling closer to reproducible, but it remains best effort and does not replace deterministic extraction settings. Why the correct answer wins: Nucleus sampling widens the candidate set.
- **D:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Nucleus sampling widens the candidate set.

### Question 69 — D, E

Answers: Use a Foundry SDK or supported connector from application code; Authenticate with a managed identity instead of keys. A supported SDK handles retries and streaming, and a managed identity removes stored secrets. SDKs provide supported request and response patterns. Pin versions and handle retries, timeouts, and errors explicitly. Managed identities avoid embedded secrets and support role-based access. Assign only required data-plane roles. Local study-map skill 2.2 (Foundry SDK and Project Integration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. A managed secret store supports rotation and access control. Secrets should never appear in prompts, code, or logs. Why the correct answer wins: A supported SDK handles retries and streaming, and a managed identity removes stored secrets.
- **B:** Incorrect for this question. Short-lived credentials reduce misuse risk. Never place tokens in prompts or logs. Why the correct answer wins: A supported SDK handles retries and streaming, and a managed identity removes stored secrets.
- **C:** Incorrect for this question. Manual portal changes work for exploration but are slow, undocumented, and hard to reproduce, so they are a poor fit for governed release processes. Why the correct answer wins: A supported SDK handles retries and streaming, and a managed identity removes stored secrets.
- **D:** Correct. SDKs provide supported request and response patterns. Pin versions and handle retries, timeouts, and errors explicitly. In this case: A supported SDK handles retries and streaming, and a managed identity removes stored secrets.
- **E:** Correct. Managed identities avoid embedded secrets and support role-based access. Assign only required data-plane roles. In this case: A supported SDK handles retries and streaming, and a managed identity removes stored secrets.

### Question 70 — D, E

Answers: Use evaluators for quality, safety, and groundedness; Evaluate harmful, biased, or policy-violating output. Quality evaluation scores correctness, and safety evaluation screens harmful output. Evaluators provide repeatable signals across models and prompts. They must be calibrated against human judgment for high-impact work. Safety evaluation complements content filters. Use representative adversarial inputs. Local study-map skill 2.3 (Evaluating Models and Applications), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Prompts, models, indexes, and tools all affect behavior. Regression tests catch unintended effects. Why the correct answer wins: Quality evaluation scores correctness, and safety evaluation screens harmful output.
- **B:** Incorrect for this question. A golden set anchors evaluation in expected behavior. Include edge cases and high-risk scenarios. Why the correct answer wins: Quality evaluation scores correctness, and safety evaluation screens harmful output.
- **C:** Incorrect for this question. Controlled comparison supports evidence-based change. Avoid changing several variables at once. Why the correct answer wins: Quality evaluation scores correctness, and safety evaluation screens harmful output.
- **D:** Correct. Safety evaluation complements content filters. Use representative adversarial inputs. In this case: Quality evaluation scores correctness, and safety evaluation screens harmful output.
- **E:** Correct. Evaluators provide repeatable signals across models and prompts. They must be calibrated against human judgment for high-impact work. In this case: Quality evaluation scores correctness, and safety evaluation screens harmful output.

### Question 71 — A, E

Answers: Give the agent a file-search tool over approved document stores; Persist conversation history in a thread or session. File search supplies approved evidence, and conversation state preserves context. A file tool retrieves from curated stores under configured access. It still depends on indexing quality and permission filters. Threads support continuity across turns. Apply retention and access controls to stored history. Local study-map skill 2.5 (Agent Tools, Retrieval, Memory, and Function Calling), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. A file tool retrieves from curated stores under configured access. It still depends on indexing quality and permission filters. In this case: File search supplies approved evidence, and conversation state preserves context.
- **B:** Incorrect for this question. OpenAPI tools describe supported HTTP operations for agent use. Narrow operations, validate inputs, and authenticate the caller. Why the correct answer wins: File search supplies approved evidence, and conversation state preserves context.
- **C:** Incorrect for this question. Routing can balance quality and cost. Fallback and evaluation are required. Why the correct answer wins: File search supplies approved evidence, and conversation state preserves context.
- **D:** Incorrect for this question. Code execution handles quantitative work the model cannot do reliably in text. The sandbox must be isolated and output must be validated. Why the correct answer wins: File search supplies approved evidence, and conversation state preserves context.
- **E:** Correct. Threads support continuity across turns. Apply retention and access controls to stored history. In this case: File search supplies approved evidence, and conversation state preserves context.

### Question 72 — D

Answer: Define role and goal → configure tools → attach knowledge → evaluate in sandbox → deploy with monitoring. Role, tools and knowledge, evaluation, then deployment with monitoring. An agent is defined before it is connected to tools and knowledge, and evaluation precedes deployment. Local study-map skill 2.6 (Multi-Agent Orchestration and Safeguards), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. The agent must be defined first, and evaluation must precede deployment. Why the correct answer wins: Role, tools and knowledge, evaluation, then deployment with monitoring.
- **B:** Incorrect for this question. Tools configured before the role exists, and evaluation after deployment gates nothing. Why the correct answer wins: Role, tools and knowledge, evaluation, then deployment with monitoring.
- **C:** Incorrect for this question. Deployment before the agent is defined, connected, or evaluated removes every control. Why the correct answer wins: Role, tools and knowledge, evaluation, then deployment with monitoring.
- **D:** Correct. An agent is defined before it is connected to tools and knowledge, and evaluation precedes deployment. In this case: Role, tools and knowledge, evaluation, then deployment with monitoring.

### Question 73 — C

Answer: Queue flagged generations for human moderation before release. Human moderation before release catches contextual problems. Human moderation catches context that automated filters miss, at the cost of latency and reviewer load. Local study-map skill 3.1 (Image Generation and Editing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Image and video safety filters reduce exposure to harmful content. Thresholds and human escalation should match policy. Why the correct answer wins: Human moderation before release catches contextual problems.
- **B:** Incorrect for this question. Brand controls define permitted logos, styles, and claims. Technical generation must still pass approval. Why the correct answer wins: Human moderation before release catches contextual problems.
- **C:** Correct. Human moderation catches context that automated filters miss, at the cost of latency and reviewer load. In this case: Human moderation before release catches contextual problems.
- **D:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Human moderation before release catches contextual problems.

### Question 74 — D

Answer: Generate a set of descriptive tags for each image. Tag sets support filtering across large libraries. Tags support filtering and search across large image libraries. Tag vocabulary should be governed so synonyms do not fragment results. Local study-map skill 3.3 (Multimodal Understanding and Accessibility), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Visual question answering should cite the relevant region or content. Avoid answering beyond what the image supports. Why the correct answer wins: Tag sets support filtering across large libraries.
- **B:** Incorrect for this question. Alt text should convey purpose and essential content, not decorative detail. Human review is still needed for critical pages. Why the correct answer wins: Tag sets support filtering across large libraries.
- **C:** Incorrect for this question. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Why the correct answer wins: Tag sets support filtering across large libraries.
- **D:** Correct. Tags support filtering and search across large image libraries. Tag vocabulary should be governed so synonyms do not fragment results. In this case: Tag sets support filtering across large libraries.

### Question 75 — D

Answer: Use Azure Content Understanding analyzers in Foundry Tools. Content Understanding analyzers are configured for the content type. Content Understanding extracts structure and fields from documents, images, audio, and video. Analyzer design and validation determine quality. Local study-map skill 3.4 (Visual Extraction and Video Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Analyzers define what to extract and how to return it. Version and test them like application code. Why the correct answer wins: Content Understanding analyzers are configured for the content type.
- **B:** Incorrect for this question. Prebuilt models cover invoices, receipts, IDs, and similar formats. Check supported locales and field coverage. Why the correct answer wins: Content Understanding analyzers are configured for the content type.
- **C:** Incorrect for this question. Document Intelligence provides prebuilt and custom extraction for structured documents. Validate field accuracy on representative samples. Why the correct answer wins: Content Understanding analyzers are configured for the content type.
- **D:** Correct. Content Understanding extracts structure and fields from documents, images, audio, and video. Analyzer design and validation determine quality. In this case: Content Understanding analyzers are configured for the content type.

### Question 76 — C

Answer: Preserve reading order across columns and sections. Reading-order analysis reconstructs the intended sequence. Reading order affects comprehension and extraction. Incorrect order can invert meaning in contracts and forms. Local study-map skill 3.4 (Visual Extraction and Video Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Layout awareness improves extraction from forms and multi-column documents. Flattening to plain text can destroy meaning. Why the correct answer wins: Reading-order analysis reconstructs the intended sequence.
- **B:** Incorrect for this question. OCR unlocks text in scans and screenshots. Layout and table structure may still require specialized extraction. Why the correct answer wins: Reading-order analysis reconstructs the intended sequence.
- **C:** Correct. Reading order affects comprehension and extraction. Incorrect order can invert meaning in contracts and forms. In this case: Reading-order analysis reconstructs the intended sequence.
- **D:** Incorrect for this question. Markdown preserves headings, tables, and lists in a model-friendly form. Validate that critical values survive conversion. Why the correct answer wins: Reading-order analysis reconstructs the intended sequence.

### Question 77 — A, D

Answers: Use pro mode for complex multimodal content understanding; Return markdown for retrieval and reasoning pipelines. Pro mode handles complex multimodal packets, and markdown output suits downstream reasoning. Pro mode handles more demanding layouts and multimodal inputs at higher cost. Use it where simpler modes fail requirements. Markdown preserves structure and is easy for models to consume. Validate tables and key values. Local study-map skill 3.4 (Visual Extraction and Video Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Correct. Markdown preserves structure and is easy for models to consume. Validate tables and key values. In this case: Pro mode handles complex multimodal packets, and markdown output suits downstream reasoning.
- **B:** Incorrect for this question. Single-task analyzers target one content type or objective. They may be simpler and cheaper than general pro-mode pipelines. Why the correct answer wins: Pro mode handles complex multimodal packets, and markdown output suits downstream reasoning.
- **C:** Incorrect for this question. Captions describe visual content for users or downstream systems. Match detail to the audience and purpose. Why the correct answer wins: Pro mode handles complex multimodal packets, and markdown output suits downstream reasoning.
- **D:** Correct. Pro mode handles more demanding layouts and multimodal inputs at higher cost. Use it where simpler modes fail requirements. In this case: Pro mode handles complex multimodal packets, and markdown output suits downstream reasoning.
- **E:** Incorrect for this question. Detection returns locations and labels for visual elements. Validate classes and thresholds against the use case. Why the correct answer wins: Pro mode handles complex multimodal packets, and markdown output suits downstream reasoning.

### Question 78 — D

Answer: Upload image → validate format and size → send multimodal request → parse structured fields → route low-confidence values to review. Validation brackets the model call, and low-confidence values go to people. Validation and structured parsing bracket the multimodal call, and low-confidence output goes to people. Local study-map skill 3.5 (Multimodal Responsible AI), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Vision and Content Understanding documentation: https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/

- **A:** Incorrect for this question. Review cannot precede the request, and parsing must follow the response. Why the correct answer wins: Validation brackets the model call, and low-confidence values go to people.
- **B:** Incorrect for this question. A request cannot precede the upload, and validation must come before the call. Why the correct answer wins: Validation brackets the model call, and low-confidence values go to people.
- **C:** Incorrect for this question. Parsing requires a response, which requires an uploaded and validated image. Why the correct answer wins: Validation brackets the model call, and low-confidence values go to people.
- **D:** Correct. Validation and structured parsing bracket the multimodal call, and low-confidence output goes to people. In this case: Validation brackets the model call, and low-confidence values go to people.

### Question 79 — C

Answer: Select and return the most relevant source sentences. Extractive summaries stay verbatim and auditable. Extractive summaries stay verbatim and therefore auditable, at the cost of readability and length. Local study-map skill 4.1 (Language Model Text Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Why the correct answer wins: Extractive summaries stay verbatim and auditable.
- **B:** Incorrect for this question. Abstractive summaries read naturally and compress long text, but they can introduce statements that the source does not support. Why the correct answer wins: Extractive summaries stay verbatim and auditable.
- **C:** Correct. Extractive summaries stay verbatim and therefore auditable, at the cost of readability and length. In this case: Extractive summaries stay verbatim and auditable.
- **D:** Incorrect for this question. Compliance work requires precise citation, retention, and review. Generic summarization is insufficient without controls. Why the correct answer wins: Extractive summaries stay verbatim and auditable.

### Question 80 — D

Answer: Convert names between writing systems without translating meaning. Transliteration preserves pronunciation across writing systems. Transliteration preserves pronunciation for names and addresses. It is not a substitute for translating meaning-bearing text. Local study-map skill 4.2 (Translation), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Domain adaptation improves consistency and recall. Validate against expert-created expected outputs. Why the correct answer wins: Transliteration preserves pronunciation across writing systems.
- **B:** Incorrect for this question. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Why the correct answer wins: Transliteration preserves pronunciation across writing systems.
- **C:** Incorrect for this question. Translation should preserve meaning, names, and formatting. Evaluate domain terminology and low-resource languages. Why the correct answer wins: Transliteration preserves pronunciation across writing systems.
- **D:** Correct. Transliteration preserves pronunciation for names and addresses. It is not a substitute for translating meaning-bearing text. In this case: Transliteration preserves pronunciation across writing systems.

### Question 81 — B

Answer: Select a specific synthesis voice for consistent spoken output. A specific synthesis voice keeps the spoken channel consistent. A named voice keeps a phone or kiosk channel recognizable across prompts. Voice availability and language coverage vary by region. Local study-map skill 4.3 (Speech Solutions), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Text-to-speech supports voice responses and accessibility. Voice, prosody, and latency affect usability. Why the correct answer wins: A specific synthesis voice keeps the spoken channel consistent.
- **B:** Correct. A named voice keeps a phone or kiosk channel recognizable across prompts. Voice availability and language coverage vary by region. In this case: A specific synthesis voice keeps the spoken channel consistent.
- **C:** Incorrect for this question. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Why the correct answer wins: A specific synthesis voice keeps the spoken channel consistent.
- **D:** Incorrect for this question. Custom speech can improve recognition of domain terms. It requires representative audio and ongoing evaluation. Why the correct answer wins: A specific synthesis voice keeps the spoken channel consistent.

### Question 82 — C, E

Answers: Detect and redact sensitive personal data; Analyze sentiment and tone with an appropriate service. PII detection finds personal data, and sentiment surfaces distress. Sensitive Data Protection or language PII detection can identify and mask data. Verify that redaction covers every path where content flows. Sentiment analysis can support triage and monitoring. Domain and language variation require validation. Local study-map skill 4.1 (Language Model Text Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Topic extraction supports discovery and grouping. It is not a substitute for an authoritative taxonomy. Why the correct answer wins: PII detection finds personal data, and sentiment surfaces distress.
- **B:** Incorrect for this question. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Why the correct answer wins: PII detection finds personal data, and sentiment surfaces distress.
- **C:** Correct. Sentiment analysis can support triage and monitoring. Domain and language variation require validation. In this case: PII detection finds personal data, and sentiment surfaces distress.
- **D:** Incorrect for this question. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Why the correct answer wins: PII detection finds personal data, and sentiment surfaces distress.
- **E:** Correct. Sensitive Data Protection or language PII detection can identify and mask data. Verify that redaction covers every path where content flows. In this case: PII detection finds personal data, and sentiment surfaces distress.

### Question 83 — B

Answer: Push documents to an index through the data-plane API. Push ingestion sends documents to the index as soon as they are written. Push ingestion supports near-real-time updates from applications. The app owns batching, retries, and deletion. Local study-map skill 5.1 (Content Ingestion and Indexing), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. OCR unlocks text in scans and screenshots. Layout and table structure may still require specialized extraction. Why the correct answer wins: Push ingestion sends documents to the index as soon as they are written.
- **B:** Correct. Push ingestion supports near-real-time updates from applications. The app owns batching, retries, and deletion. In this case: Push ingestion sends documents to the index as soon as they are written.
- **C:** Incorrect for this question. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. Why the correct answer wins: Push ingestion sends documents to the index as soon as they are written.
- **D:** Incorrect for this question. Skillsets can OCR, split, embed, and extract during indexing. Each skill adds latency, cost, and failure modes. Why the correct answer wins: Push ingestion sends documents to the index as soon as they are written.

### Question 84 — B

Answer: Tune scoring and boosting against a labelled query set. Scoring and boosting must be tuned against a labelled query set. Boosting and scoring changes should be measured on real queries. Untested tuning usually trades one query class for another. Local study-map skill 5.2 (Search and Grounding Configuration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. A semantic ranker can improve relevance for natural-language queries. It adds cost and latency and should be measured against a baseline. Why the correct answer wins: Scoring and boosting must be tuned against a labelled query set.
- **B:** Correct. Boosting and scoring changes should be measured on real queries. Untested tuning usually trades one query class for another. In this case: Scoring and boosting must be tuned against a labelled query set.
- **C:** Incorrect for this question. Hybrid search covers exact identifiers and paraphrased meaning together. Fusion and ranking need testing on representative queries. Why the correct answer wins: Scoring and boosting must be tuned against a labelled query set.
- **D:** Incorrect for this question. Embeddings support similarity search over meaning rather than exact terms. Vector search still needs chunking, filtering, and evaluation. Why the correct answer wins: Scoring and boosting must be tuned against a labelled query set.

### Question 85 — C

Answer: Set chunk overlap so facts spanning a boundary stay retrievable. Chunk overlap keeps facts that straddle a boundary retrievable, at the cost of duplicated index storage. Overlap preserves context across chunk edges at the cost of duplicated index storage and more near-duplicate hits. Local study-map skill 5.3 (Enrichment Skills), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. A skillset can extract entities, captions, and structure during indexing. Enrichment adds cost and failure points that need monitoring. Why the correct answer wins: Chunk overlap keeps facts that straddle a boundary retrievable, at the cost of duplicated index storage.
- **B:** Incorrect for this question. Chunking affects recall, precision, and context use. Respect document structure and test against real questions. Why the correct answer wins: Chunk overlap keeps facts that straddle a boundary retrievable, at the cost of duplicated index storage.
- **C:** Correct. Overlap preserves context across chunk edges at the cost of duplicated index storage and more near-duplicate hits. In this case: Chunk overlap keeps facts that straddle a boundary retrievable, at the cost of duplicated index storage.
- **D:** Incorrect for this question. Skillsets can OCR, split, embed, and extract during indexing. Each skill adds latency, cost, and failure modes. Why the correct answer wins: Chunk overlap keeps facts that straddle a boundary retrievable, at the cost of duplicated index storage.

### Question 86 — C

Answer: Define index fields, attributes, and searchable versus filterable behavior. Field attributes control filtering and sorting. Field attributes decide what can be filtered, sorted, faceted, or retrieved, so schema choices constrain query design later. Local study-map skill 5.6 (Document and Content Extraction), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. Analyzers define what to extract and how to return it. Version and test them like application code. Why the correct answer wins: Field attributes control filtering and sorting.
- **B:** Incorrect for this question. Document Intelligence provides prebuilt and custom extraction for structured documents. Validate field accuracy on representative samples. Why the correct answer wins: Field attributes control filtering and sorting.
- **C:** Correct. Field attributes decide what can be filtered, sorted, faceted, or retrieved, so schema choices constrain query design later. In this case: Field attributes control filtering and sorting.
- **D:** Incorrect for this question. Typed fields feed downstream systems directly. Add validation and confidence thresholds before automated action. Why the correct answer wins: Field attributes control filtering and sorting.

### Question 87 — D

Answer: Combine OCR with layout analysis for complex documents. OCR with layout analysis preserves relationships that plain OCR loses. OCR supplies text while layout analysis preserves relationships. Together they support tables and multi-column forms. Local study-map skill 5.4 (RAG Ingestion and OCR), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. Chunking affects recall, precision, and context use. Respect document structure and test against real questions. Why the correct answer wins: OCR with layout analysis preserves relationships that plain OCR loses.
- **B:** Incorrect for this question. Markdown preserves headings, tables, and lists in a model-friendly form. Validate that critical values survive conversion. Why the correct answer wins: OCR with layout analysis preserves relationships that plain OCR loses.
- **C:** Incorrect for this question. Indexers automate ingestion and can run on a schedule. Monitor failures, deletions, and field mappings. Why the correct answer wins: OCR with layout analysis preserves relationships that plain OCR loses.
- **D:** Correct. OCR supplies text while layout analysis preserves relationships. Together they support tables and multi-column forms. In this case: OCR with layout analysis preserves relationships that plain OCR loses.

### Question 88 — C

Answer: Connect the data source → define the index schema → attach the enrichment skillset → run the indexer → validate relevance on sample queries. Source, schema, enrichment, indexing, then relevance validation. Schema and enrichment must exist before indexing runs, and relevance is checked after the index is populated. Local study-map skill 5.2 (Search and Grounding Configuration), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. An indexer cannot run before the source and schema exist. Why the correct answer wins: Source, schema, enrichment, indexing, then relevance validation.
- **B:** Incorrect for this question. The schema must exist before enrichment and relevance testing. Why the correct answer wins: Source, schema, enrichment, indexing, then relevance validation.
- **C:** Correct. Schema and enrichment must exist before indexing runs, and relevance is checked after the index is populated. In this case: Source, schema, enrichment, indexing, then relevance validation.
- **D:** Incorrect for this question. Relevance cannot be validated on an index that was never populated. Why the correct answer wins: Source, schema, enrichment, indexing, then relevance validation.

### Question 89 — D

Answer: Apply a custom glossary or terminology list. A glossary enforces approved terminology across languages. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Local study-map skill 4.2 (Translation), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Why the correct answer wins: A glossary enforces approved terminology across languages.
- **B:** Incorrect for this question. Topic extraction supports discovery and grouping. It is not a substitute for an authoritative taxonomy. Why the correct answer wins: A glossary enforces approved terminology across languages.
- **C:** Incorrect for this question. Sentiment analysis can support triage and monitoring. Domain and language variation require validation. Why the correct answer wins: A glossary enforces approved terminology across languages.
- **D:** Correct. Glossaries keep product and legal terms consistent. Terms still need human validation in context. In this case: A glossary enforces approved terminology across languages.

### Question 90 — A

Answer: Use a prebuilt document model for common document types. A prebuilt document model fits common, stable document types without custom training. Prebuilt models cover invoices, receipts, IDs, and similar formats. Check supported locales and field coverage. Local study-map skill 5.6 (Document and Content Extraction), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Correct. Prebuilt models cover invoices, receipts, IDs, and similar formats. Check supported locales and field coverage. In this case: A prebuilt document model fits common, stable document types without custom training.
- **B:** Incorrect for this question. Custom models fit specialized forms not covered by prebuilts. They require representative labels and retraining discipline. Why the correct answer wins: A prebuilt document model fits common, stable document types without custom training.
- **C:** Incorrect for this question. Document Intelligence provides prebuilt and custom extraction for structured documents. Validate field accuracy on representative samples. Why the correct answer wins: A prebuilt document model fits common, stable document types without custom training.
- **D:** Incorrect for this question. Analyzers define what to extract and how to return it. Version and test them like application code. Why the correct answer wins: A prebuilt document model fits common, stable document types without custom training.

### Question 91 — B

Answer: Use field-level confidence to route exceptions. Field-level confidence thresholds send uncertain values to human review. Low-confidence fields should be reviewed rather than accepted. Thresholds depend on downstream impact. Local study-map skill 5.6 (Document and Content Extraction), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Incorrect for this question. Sentiment analysis can support triage and monitoring. Domain and language variation require validation. Why the correct answer wins: Field-level confidence thresholds send uncertain values to human review.
- **B:** Correct. Low-confidence fields should be reviewed rather than accepted. Thresholds depend on downstream impact. In this case: Field-level confidence thresholds send uncertain values to human review.
- **C:** Incorrect for this question. Relevance covers both retrieval and response usefulness. A correct but off-topic answer still fails. Why the correct answer wins: Field-level confidence thresholds send uncertain values to human review.
- **D:** Incorrect for this question. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Why the correct answer wins: Field-level confidence thresholds send uncertain values to human review.

### Question 92 — B

Answer: Monitor groundedness and citation quality in production. Groundedness monitoring detects statements unsupported by retrieved clinical evidence. Groundedness checks whether claims are supported by retrieved evidence. Sampling and human review complement automated scores. Local study-map skill 1.5 (Monitoring Performance, Drift, Safety, and Grounding), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/

- **A:** Incorrect for this question. Users experience the whole path, not only generation. Optimize the dominant contributor. Why the correct answer wins: Groundedness monitoring detects statements unsupported by retrieved clinical evidence.
- **B:** Correct. Groundedness checks whether claims are supported by retrieved evidence. Sampling and human review complement automated scores. In this case: Groundedness monitoring detects statements unsupported by retrieved clinical evidence.
- **C:** Incorrect for this question. Quota limits throughput regardless of application capacity. Request increases in advance and plan graceful degradation. Why the correct answer wins: Groundedness monitoring detects statements unsupported by retrieved clinical evidence.
- **D:** Incorrect for this question. Retries, tool calls, evaluation, and review contribute to unit economics. Per-outcome cost supports better optimization. Why the correct answer wins: Groundedness monitoring detects statements unsupported by retrieved clinical evidence.

### Question 93 — B

Answer: Expose a typed function as an agent tool. A function tool calls the scheduling system under application authorization. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. Local study-map skill 2.5 (Agent Tools, Retrieval, Memory, and Function Calling), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Why the correct answer wins: A function tool calls the scheduling system under application authorization.
- **B:** Correct. Function tools let the agent request a defined operation with structured arguments. Authorization and input validation must be enforced server-side. In this case: A function tool calls the scheduling system under application authorization.
- **C:** Incorrect for this question. OpenAPI tools describe supported HTTP operations for agent use. Narrow operations, validate inputs, and authenticate the caller. Why the correct answer wins: A function tool calls the scheduling system under application authorization.
- **D:** Incorrect for this question. RAG supplies selected source content at request time so answers can cite current evidence. It reduces but does not eliminate fabrication. Why the correct answer wins: A function tool calls the scheduling system under application authorization.

### Question 94 — D

Answer: Use a manager agent to coordinate specialists. A manager agent routes the request to specialists and consolidates their replies. A manager routes tasks and merges results. Clear responsibility and failure handling are required. Local study-map skill 2.6 (Multi-Agent Orchestration and Safeguards), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Parallel execution reduces wall-clock time for independent work. Reconciliation still requires design. Why the correct answer wins: A manager agent routes the request to specialists and consolidates their replies.
- **B:** Incorrect for this question. Connected agents let one agent delegate to another. Authorization and result validation remain necessary. Why the correct answer wins: A manager agent routes the request to specialists and consolidates their replies.
- **C:** Incorrect for this question. Sequential orchestration makes dependencies explicit. It may add latency where steps could run concurrently. Why the correct answer wins: A manager agent routes the request to specialists and consolidates their replies.
- **D:** Correct. A manager routes tasks and merges results. Clear responsibility and failure handling are required. In this case: A manager agent routes the request to specialists and consolidates their replies.

### Question 95 — C

Answer: Define narrow tool schemas with clear descriptions. A typed schema constrains the arguments before the call. Precise schemas help the model choose tools and arguments correctly. Broad or ambiguous tools invite unsafe calls. Local study-map skill 2.4 (Agent Roles, Goals, and Tool Schemas), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Routing can balance quality and cost. Fallback and evaluation are required. Why the correct answer wins: A typed schema constrains the arguments before the call.
- **B:** Incorrect for this question. System messages define role and constraints. They are not a security boundary against injection. Why the correct answer wins: A typed schema constrains the arguments before the call.
- **C:** Correct. Precise schemas help the model choose tools and arguments correctly. Broad or ambiguous tools invite unsafe calls. In this case: A typed schema constrains the arguments before the call.
- **D:** Incorrect for this question. Managed state supports multi-turn continuity without rebuilding history manually. Retention, isolation, and user control still need design. Why the correct answer wins: A typed schema constrains the arguments before the call.

### Question 96 — A

Answer: Persist conversation history in a thread or session. Conversation state keeps earlier turns available for the same thread. Threads support continuity across turns. Apply retention and access controls to stored history. Local study-map skill 2.5 (Agent Tools, Retrieval, Memory, and Function Calling), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Correct. Threads support continuity across turns. Apply retention and access controls to stored history. In this case: Conversation state keeps earlier turns available for the same thread.
- **B:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Conversation state keeps earlier turns available for the same thread.
- **C:** Incorrect for this question. Provisioned capacity reserves throughput at a committed cost. It fits stable demand, not unpredictable spikes. Why the correct answer wins: Conversation state keeps earlier turns available for the same thread.
- **D:** Incorrect for this question. Embeddings determine semantic similarity behavior. Evaluate retrieval quality before and after changes. Why the correct answer wins: Conversation state keeps earlier turns available for the same thread.

### Question 97 — D

Answer: Enable tracing across agent, model, and tool calls. Traces show each model and tool call in order. Traces localize failures and latency in multi-step workflows. Correlate them with evaluation results and deployment versions. Local study-map skill 2.7 (Agent Monitoring and Error Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Foundry Agent Service documentation: https://learn.microsoft.com/en-us/azure/ai-foundry/agents/

- **A:** Incorrect for this question. Caching can reduce cost and latency for repeated content. Validate correctness and invalidation behavior. Why the correct answer wins: Traces show each model and tool call in order.
- **B:** Incorrect for this question. Watermarks support disclosure and traceability. They do not replace usage policy or review. Why the correct answer wins: Traces show each model and tool call in order.
- **C:** Incorrect for this question. Lower temperature reduces sampling variability. It does not guarantee factual correctness. Why the correct answer wins: Traces show each model and tool call in order.
- **D:** Correct. Traces localize failures and latency in multi-step workflows. Correlate them with evaluation results and deployment versions. In this case: Traces show each model and tool call in order.

### Question 98 — C

Answer: Use a custom speech model for specialized vocabulary. A custom speech model adapts acoustic and language behaviour to the domain. Custom speech can improve recognition of domain terms. It requires representative audio and ongoing evaluation. Local study-map skill 4.3 (Speech Solutions), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Glossaries keep product and legal terms consistent. Terms still need human validation in context. Why the correct answer wins: A custom speech model adapts acoustic and language behaviour to the domain.
- **B:** Incorrect for this question. Speech-to-text enables voice agents and transcript analysis. Audio quality, accents, and domain terms affect accuracy. Why the correct answer wins: A custom speech model adapts acoustic and language behaviour to the domain.
- **C:** Correct. Custom speech can improve recognition of domain terms. It requires representative audio and ongoing evaluation. In this case: A custom speech model adapts acoustic and language behaviour to the domain.
- **D:** Incorrect for this question. Text-to-speech supports voice responses and accessibility. Voice, prosody, and latency affect usability. Why the correct answer wins: A custom speech model adapts acoustic and language behaviour to the domain.

### Question 99 — B

Answer: Extract key phrases to summarize what a document covers. Key-phrase extraction surfaces salient topics for navigation. Key phrases support navigation, tagging, and clustering. They are not a substitute for a required structured field. Local study-map skill 4.1 (Language Model Text Analysis), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Language, Speech, and Translator documentation: https://learn.microsoft.com/en-us/azure/ai-services/

- **A:** Incorrect for this question. Topic extraction supports discovery and grouping. It is not a substitute for an authoritative taxonomy. Why the correct answer wins: Key-phrase extraction surfaces salient topics for navigation.
- **B:** Correct. Key phrases support navigation, tagging, and clustering. They are not a substitute for a required structured field. In this case: Key-phrase extraction surfaces salient topics for navigation.
- **C:** Incorrect for this question. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Why the correct answer wins: Key-phrase extraction surfaces salient topics for navigation.
- **D:** Incorrect for this question. Entity extraction turns text into structured facts. Ambiguous mentions need resolution and validation. Why the correct answer wins: Key-phrase extraction surfaces salient topics for navigation.

### Question 100 — A

Answer: Use field-level confidence to route exceptions. Field-level confidence thresholds send uncertain values to human review. Low-confidence fields should be reviewed rather than accepted. Thresholds depend on downstream impact. Local study-map skill 5.6 (Document and Content Extraction), mapped to the official guide: Microsoft AI-103 study guide, skills measured as of April 16, 2026 Primary reference: Azure AI Search documentation: https://learn.microsoft.com/en-us/azure/search/

- **A:** Correct. Low-confidence fields should be reviewed rather than accepted. Thresholds depend on downstream impact. In this case: Field-level confidence thresholds send uncertain values to human review.
- **B:** Incorrect for this question. Summaries should preserve required facts and caveats. Fluency does not prove completeness. Why the correct answer wins: Field-level confidence thresholds send uncertain values to human review.
- **C:** Incorrect for this question. Sentiment analysis can support triage and monitoring. Domain and language variation require validation. Why the correct answer wins: Field-level confidence thresholds send uncertain values to human review.
- **D:** Incorrect for this question. Relevance covers both retrieval and response usefulness. A correct but off-topic answer still fails. Why the correct answer wins: Field-level confidence thresholds send uncertain values to human review.
