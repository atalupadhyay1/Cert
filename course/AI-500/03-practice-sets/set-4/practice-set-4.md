# AI-500 — Practice Set 4

100 questions · Suggested practice duration: 180 minutes · Practice target: 80%

Select one answer unless the question says Select TWO. Answer key follows all questions.

Original educational content, not actual or recalled Microsoft exam items.

## Questions

### 1. A message is delivered twice to a purchase tool. Which mechanism should prevent a second purchase?

Domain: Develop multi-agent solutions in Azure

- A. Use a stable idempotency key and durable result tracking
- B. Use supported prompt-prefix caching
- C. Use bounded retries with backoff and jitter for transient failures
- D. Record structured audit events

### 2. A release plan uses separate blue and green instances and a controlled routing switch. Which pattern is this?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Maintain separate blue and green environments and switch traffic
- B. Deploy changes directly to all production users without gates
- C. Promote through development, test, acceptance, and production
- D. Release to a limited traffic cohort with health and quality gates

### 3. A team needs to prioritize issues using user reports and confirmed task outcomes. Which approach fits?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Use supported prompt-prefix caching
- B. Analyze user feedback with verified task outcomes
- C. Collect aggregate operational metrics
- D. Select the largest available model for every task

### 4. A platform must distinguish successful deployment from preserved task quality. Which assessment fits?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Use supported prompt-prefix caching
- B. Collect aggregate operational metrics
- C. Compare quality against a stable versioned baseline
- D. Monitor agent health and workflow failure patterns

### 5. A search tool returns content that attempts to override the system's policy. Which intervention fits?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Validate and screen tool responses before reuse
- B. Record structured audit events
- C. Inspect and constrain user input before agent processing
- D. Use supported prompt-prefix caching

### 6. A platform needs evidence that approved facts persist and unauthorized memories remain inaccessible. Which test category fits?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Measure relevance of retrieved evidence against labeled queries
- B. Evaluate whether generated claims are supported by supplied evidence
- C. Evaluate tool choice, arguments, outcomes, and side effects
- D. Evaluate memory retention, retrieval, isolation, and forgetting

### 7. A remote specialist already exposes an A2A-compatible endpoint. Which integration choice preserves its agent-facing contract?

Domain: Architect multi-agent solutions

- A. Use an embedding-based retrieval index
- B. Use Model Context Protocol (MCP)
- C. Use Agent2Agent (A2A) interoperability
- D. Use a versioned development container and dependency lock

### 8. A specialist receives a tool payload with contradictory totals. Which check should occur before use?

Domain: Develop multi-agent solutions in Azure

- A. Record structured audit events
- B. Select the largest available model for every task
- C. Use supported prompt-prefix caching
- D. Validate tool results against schema and domain constraints

### 9. An expiring certificate used by a tool integration must be replaced through a tested rollout. Which process fits?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Use supported prompt-prefix caching
- B. Fine-tune the underlying model
- C. Rotate secrets and update dependent applications safely
- D. Record structured audit events

### 10. A provider supports reusing processing for a repeated prompt prefix. Which cache type is this?

Domain: Develop multi-agent solutions in Azure

- A. Use an exact-input response cache
- B. Use a governed semantic response cache
- C. Use supported prompt-prefix caching
- D. Fine-tune the underlying model

### 11. An application prompt says read only, but its identity has broad management rights. Which enforcement should correct this?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Apply content safety filters
- B. Record structured audit events
- C. Apply narrowly scoped Azure RBAC assignments
- D. Specify each agent persona, scope, and escalation rules

### 12. An agent model is cheap per token but fails tools and retries often. Which selection approach addresses total suitability?

Domain: Architect multi-agent solutions

- A. Select the largest available model for every task
- B. Benchmark models against task capability and operational constraints
- C. Select only by lowest token price
- D. Fine-tune the underlying model

### 13. A reliability design must protect telemetry and specify safe escalation from alerts. Which TWO controls fit? (Select TWO.)

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Select the largest available model for every task
- B. Redact and access-control sensitive telemetry
- C. Define alerts with bounded remediation and escalation
- D. Allow unlimited autonomous retries and spawning
- E. Log every raw prompt and credential without filtering

### 14. A team must test actual interaction between its agent service and configured search endpoint. Which category fits?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Add curated input-output examples to the prompt
- B. Use supported prompt-prefix caching
- C. Use isolated unit tests for deterministic components
- D. Test interactions with configured external dependencies

### 15. A workflow platform wants each run's consumption associated with its authorized tenant. Which cost-management practice fits?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Select the largest available model for every task
- B. Collect aggregate operational metrics
- C. Attribute usage to tenants, projects, and workflow runs
- D. Use supported prompt-prefix caching

### 16. A tool connector repeatedly disconnects while generated text quality remains high. Which monitoring focus fits?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Evaluate whether generated claims are supported by supplied evidence
- B. Monitor agent health and workflow failure patterns
- C. Select only by lowest token price
- D. Add curated input-output examples to the prompt

### 17. A workflow mixes creative research with deterministic invoice calculations. Which design activity helps separate responsibilities?

Domain: Architect multi-agent solutions

- A. Use one broadly autonomous agent for the entire workflow
- B. Decompose the goal into bounded agent responsibilities and tools
- C. Increase the number of agents without changing responsibilities
- D. Fine-tune the underlying model

### 18. A platform wants to reject prohibited requests before they reach specialist agents. Which control fits?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Record structured audit events
- B. Use supported prompt-prefix caching
- C. Validate and screen the final response before delivery
- D. Inspect and constrain user input before agent processing

### 19. A workflow accumulates irrelevant messages and loses focus. Which context-management change fits?

Domain: Develop multi-agent solutions in Azure

- A. Assemble only relevant state, evidence, and tool results
- B. Use governed long-term memory
- C. Allow unlimited autonomous retries and spawning
- D. Select the largest available model for every task

### 20. A generic toxicity filter does not enforce a legal filing deadline rule. Which additional control fits?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Apply content safety filters
- B. Implement deterministic domain-specific policy checks
- C. Fine-tune the underlying model
- D. Add curated input-output examples to the prompt

### 21. A workflow averages 8,000 input tokens and 2,000 output tokens per run. It executes 120 runs. Ignoring caching and retries, how many total model tokens are processed?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. 1,200,000 tokens
- B. 10,000 tokens
- C. 960,000 tokens
- D. 240,000 tokens

### 22. Separate agents can summarize different documents without sharing intermediate results. Which pattern fits?

Domain: Architect multi-agent solutions

- A. Use parallel orchestration with a controlled join
- B. Use a controlled handoff between specialist agents
- C. Use one broadly autonomous agent for the entire workflow
- D. Use sequential orchestration

### 23. A platform needs repeatable identity, network, and resource configuration through automation. Which deployment practice fits?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Deploy versioned infrastructure as code through reviewed automation
- B. Version prompts and evaluate changes before promotion
- C. Add curated input-output examples to the prompt
- D. Deploy changes directly to all production users without gates

### 24. An evaluation team wants synthetic examples covering underrepresented workflow paths. Which approach is appropriate?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Generate and validate diverse synthetic evaluation cases
- B. Select the largest available model for every task
- C. Use supported prompt-prefix caching
- D. Allow unlimited autonomous retries and spawning

### 25. A platform receives expired or wrongly targeted access tokens at tool endpoints. Which validation is required?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Version prompts and evaluate changes before promotion
- B. Record structured audit events
- C. Validate OAuth access tokens and enforce audience and scopes
- D. Use an API key with secure storage and rotation

### 26. A platform review finds shared credentials and undefined memory retention. Which TWO architectural corrections fit? (Select TWO.)

Domain: Architect multi-agent solutions

- A. Use one highly privileged identity for all agents
- B. Allow unlimited autonomous retries and spawning
- C. Log every raw prompt and credential without filtering
- D. Use distinct scoped identities and verify every boundary
- E. Define retention, deletion, and tenant-isolation rules for state

### 27. An architect must define a research agent's autonomy and prohibited behaviors. Which design choice fits?

Domain: Architect multi-agent solutions

- A. Fine-tune the underlying model
- B. Specify each agent persona, scope, and escalation rules
- C. Apply narrowly scoped Azure RBAC assignments
- D. Collect aggregate operational metrics

### 28. An architect wants rate-limiting and authentication policy at the API entry layer. Which service fits?

Domain: Develop multi-agent solutions in Azure

- A. Use Azure Functions for a suitable event-driven tool
- B. Place appropriate policies at Azure API Management
- C. Use an embedding-based retrieval index
- D. Use Hugging Face Transformers for compatible model capabilities

### 29. A multi-agent system must distinguish team coordination data from reusable historical memories. Which design fits?

Domain: Architect multi-agent solutions

- A. Use one broadly autonomous agent for the entire workflow
- B. Use an embedding-based retrieval index
- C. Separate session state, shared team state, and long-term memory
- D. Use session-scoped short-term state

### 30. An integration needs resilience without overwhelming a recovering downstream service. Which retry strategy fits?

Domain: Develop multi-agent solutions in Azure

- A. Use bounded retries with backoff and jitter for transient failures
- B. Increase the number of agents without changing responsibilities
- C. Fine-tune the underlying model
- D. Allow unlimited autonomous retries and spawning

### 31. A routing agent needs examples of boundary cases supplied at inference time. Which technique fits?

Domain: Develop multi-agent solutions in Azure

- A. Select the largest available model for every task
- B. Add curated input-output examples to the prompt
- C. Use a supported fine-tuning strategy with curated data and held-out evaluation
- D. Use supported prompt-prefix caching

### 32. An agent release must rerun accepted behavior cases and automated quality checks. Which test category fits?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Increase the number of agents without changing responsibilities
- B. Run regression tests and automated agent evaluations
- C. Use isolated unit tests for deterministic components
- D. Use supported prompt-prefix caching

### 33. A team wants to add a compatible transformer model capability to its Python agent application. Which tooling fits?

Domain: Develop multi-agent solutions in Azure

- A. Place appropriate policies at Azure API Management
- B. Use Azure Logic Apps for suitable connector-based workflows
- C. Use Hugging Face Transformers for compatible model capabilities
- D. Use Model Context Protocol (MCP)

### 34. An application needs identity-based access from Azure compute without a long-lived credential in code. Which option fits?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Use an API key with secure storage and rotation
- B. Use an Azure managed identity where supported
- C. Use one highly privileged identity for all agents
- D. Compact context into a validated summary

### 35. An agent update must preserve prior correctness and safety behavior across tasks. Which test suite fits?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Select the largest available model for every task
- B. Add curated input-output examples to the prompt
- C. Fine-tune the underlying model
- D. Run a representative held-out prompt regression suite

### 36. A multi-tier service should preserve delegated user context for a compatible downstream API. Which authentication pattern fits?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Use an Azure managed identity where supported
- B. Use an API key with secure storage and rotation
- C. Use one highly privileged identity for all agents
- D. Use an on-behalf-of flow for delegated downstream access

### 37. A retrieval rollout updates only the query encoder and matching quality collapses. Which correction fits?

Domain: Develop multi-agent solutions in Azure

- A. Rerank retrieved candidates before context selection
- B. Compact context into a validated summary
- C. Use supported prompt-prefix caching
- D. Re-embed content with a consistent compatible embedding configuration

### 38. A pipeline needs higher throughput without causing synchronized throttling retries. Which control fits?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Allow unlimited autonomous retries and spawning
- B. Coordinate concurrency, rate budgets, and backoff
- C. Fine-tune the underlying model
- D. Select the largest available model for every task

### 39. An agent graph contains independent branches that can overlap before a required join. Which performance approach fits?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Increase the number of agents without changing responsibilities
- B. Allow unlimited autonomous retries and spawning
- C. Optimize the dependent critical path and parallelize independent work
- D. Select the largest available model for every task

### 40. A team relies only on semantic recall to reconstruct precise entity relationships. Which stronger lookup design fits?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Rerank retrieved candidates before context selection
- B. Select the largest available model for every task
- C. Use supported prompt-prefix caching
- D. Supplement vector recall with authoritative structured lookup

### 41. A utility that constructs permission filters should be checked independently of the live search service. Which test fits?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Run adversarial testing early and throughout the lifecycle
- B. Release to a limited traffic cohort with health and quality gates
- C. Use isolated unit tests for deterministic components
- D. Test interactions with configured external dependencies

### 42. An enterprise wants to probe agent-tool attack paths throughout development. Which security practice fits?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Run adversarial testing early and throughout the lifecycle
- B. Use supported prompt-prefix caching
- C. Select the largest available model for every task
- D. Deploy changes directly to all production users without gates

### 43. Several agents use inconsistent references for the same account. Which continuity control should be introduced?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Use supported prompt-prefix caching
- B. Diagnose summary drift
- C. Fine-tune the underlying model
- D. Maintain stable entity IDs and validated factual state

### 44. A multi-agent synthesis includes statements absent from all supplied evidence. Which dimension should be assessed?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Select only by lowest token price
- B. Collect aggregate operational metrics
- C. Measure relevance of retrieved evidence against labeled queries
- D. Evaluate whether generated claims are supported by supplied evidence

### 45. An agent calls a prohibited tool and still produces an acceptable-looking final paragraph. Which evaluation fits?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Evaluate tool choice, arguments, outcomes, and side effects
- B. Evaluate whether generated claims are supported by supplied evidence
- C. Use qualified human reviewers with a shared rubric
- D. Measure relevance of retrieved evidence against labeled queries

### 46. An approval step should survive process restarts and validate that the request is still actionable. Which workflow design fits?

Domain: Develop multi-agent solutions in Azure

- A. Use supported prompt-prefix caching
- B. Add curated input-output examples to the prompt
- C. Record structured audit events
- D. Implement a controlled agent workflow with explicit review and resume

### 47. An enterprise needs a formal path from development through acceptance to production. Which environment strategy fits?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Promote through development, test, acceptance, and production
- B. Maintain separate blue and green environments and switch traffic
- C. Use supported prompt-prefix caching
- D. Deploy changes directly to all production users without gates

### 48. A platform's staging and production builds differ unexpectedly and use one privileged identity. Which TWO corrections fit? (Select TWO.)

Domain: Secure, govern, and deploy multi-agent solutions

- A. Deploy changes directly to all production users without gates
- B. Use separate environment identities and configuration
- C. Allow unlimited autonomous retries and spawning
- D. Use one highly privileged identity for all agents
- E. Promote the same immutable versioned artifacts across environments

### 49. An agent project behaves differently because developers install unpinned dependency versions. Which setup should be standardized?

Domain: Architect multi-agent solutions

- A. Fine-tune the underlying model
- B. Use a versioned development container and dependency lock
- C. Use Azure Container Apps for suitable containerized services
- D. Maintain reviewed repository AI instructions

### 50. An assistant receives external text that attempts to redefine its role. Which instruction design principle fits?

Domain: Develop multi-agent solutions in Azure

- A. Fine-tune the underlying model
- B. Use supported prompt-prefix caching
- C. Separate trusted instructions from untrusted content
- D. Record structured audit events

### 51. A team must reduce waste in model size and prompt tokens while preserving evidence. Which TWO actions fit? (Select TWO.)

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Benchmark a smaller adequate model for selected tasks
- B. Remove irrelevant context while preserving necessary evidence
- C. Allow unlimited autonomous retries and spawning
- D. Increase the number of agents without changing responsibilities
- E. Select the largest available model for every task

### 52. A lookup should reuse eligible responses when question wording differs but intent is equivalent. Which cache fits?

Domain: Develop multi-agent solutions in Azure

- A. Use an exact-input response cache
- B. Use a governed semantic response cache
- C. Use supported prompt-prefix caching
- D. Fine-tune the underlying model

### 53. A developer assumes a model's JSON tool proposal executes the API automatically. Which correction fits?

Domain: Develop multi-agent solutions in Azure

- A. Add curated input-output examples to the prompt
- B. Execute a validated function call in application code
- C. Fine-tune the underlying model
- D. Compact context into a validated summary

### 54. A platform must record and enforce required evidence before promoting an artifact. Which CI/CD approach fits?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Add curated input-output examples to the prompt
- B. Gate CI/CD on reviewed artifacts, security checks, and evaluations
- C. Deploy changes directly to all production users without gates
- D. Record structured audit events

### 55. A model-based scorer is assumed to be ground truth without comparison to humans. Which correction fits?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Use supported prompt-prefix caching
- B. Select the largest available model for every task
- C. Collect aggregate operational metrics
- D. Calibrate LLM-as-a-judge against expert-labeled cases

### 56. A multi-step workflow needs to replace verbose history with a verified concise account. Which technique fits?

Domain: Develop multi-agent solutions in Azure

- A. Use governed long-term memory
- B. Fine-tune the underlying model
- C. Increase the number of agents without changing responsibilities
- D. Compact context into a validated summary

### 57. A recurring research agent needs a governed store of validated findings across runs. Which state class fits?

Domain: Architect multi-agent solutions

- A. Use session-scoped short-term state
- B. Compact context into a validated summary
- C. Use governed long-term memory
- D. Fine-tune the underlying model

### 58. An agent cannot select a remedy until another agent has classified the incident. Which orchestration fits?

Domain: Architect multi-agent solutions

- A. Use parallel orchestration with a controlled join
- B. Use peer-to-peer coordination with bounded protocols
- C. Use sequential orchestration
- D. Use hub-and-spoke coordination

### 59. An architect must make an agent workflow understandable and interruptible for users. Which practice fits?

Domain: Architect multi-agent solutions

- A. Design clear AI disclosure, user control, and recovery paths
- B. Apply content safety filters
- C. Record structured audit events
- D. Fine-tune the underlying model

### 60. A tool ecosystem needs authorization before side effects and validation of returned content. Which TWO guardrails fit? (Select TWO.)

Domain: Secure, govern, and deploy multi-agent solutions

- A. Use supported prompt-prefix caching
- B. Record structured audit events
- C. Validate and screen the final response before delivery
- D. Validate and screen tool responses before reuse
- E. Authorize and validate the proposed tool action before execution

### 61. An agent host cannot reach a private-only dependency because name resolution is misconfigured. Which design area should be corrected?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Use supported private endpoints and correct private DNS
- B. Enable unrestricted public access to bypass private networking
- C. Fine-tune the underlying model
- D. Apply content safety filters

### 62. A team needs centralized error handling for its agent pipeline. Which reusable capability fits?

Domain: Develop multi-agent solutions in Azure

- A. Use reusable middleware for cross-cutting controls
- B. Add curated input-output examples to the prompt
- C. Fine-tune the underlying model
- D. Use an embedding-based retrieval index

### 63. A tool owner needs to publish schemas and reject unauthorized MCP invocations. Which component fits?

Domain: Develop multi-agent solutions in Azure

- A. Implement an MCP server with explicit tool schemas and authorization
- B. Use supported prompt-prefix caching
- C. Implement an MCP client that discovers and invokes permitted tools
- D. Use Agent2Agent (A2A) interoperability

### 64. An agent produces unsupported or disallowed content in its final message. Which final boundary should inspect it?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Inspect and constrain user input before agent processing
- B. Record structured audit events
- C. Validate and screen the final response before delivery
- D. Use supported prompt-prefix caching

### 65. An agent's tone and risk-sensitive advice need domain judgment. Which evaluation process fits?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Select only by lowest token price
- B. Collect aggregate operational metrics
- C. Use qualified human reviewers with a shared rubric
- D. Use supported prompt-prefix caching

### 66. An adaptation project needs to specify training data quality, update frequency, and regression gates. Which strategy fits?

Domain: Develop multi-agent solutions in Azure

- A. Increase the number of agents without changing responsibilities
- B. Use a supported fine-tuning strategy with curated data and held-out evaluation
- C. Use supported prompt-prefix caching
- D. Refresh the knowledge source and retrieval index

### 67. A multi-agent run consumes unlimited tokens and ignores user stop requests. Which TWO execution controls fit? (Select TWO.)

Domain: Develop multi-agent solutions in Azure

- A. Propagate cancellation through dependent branches
- B. Enforce per-run token, tool-call, and spawn budgets
- C. Increase the number of agents without changing responsibilities
- D. Use supported prompt-prefix caching
- E. Select the largest available model for every task

### 68. A memory store contains old project data that policy requires expiring. Which control fits?

Domain: Develop multi-agent solutions in Azure

- A. Re-embed content with a consistent compatible embedding configuration
- B. Use supported prompt-prefix caching
- C. Fine-tune the underlying model
- D. Apply purpose-based memory retention and deletion

### 69. An auditor asks which instruction revision produced a particular agent run. Which practice supplies this evidence?

Domain: Develop multi-agent solutions in Azure

- A. Version prompts and evaluate changes before promotion
- B. Collect aggregate operational metrics
- C. Fine-tune the underlying model
- D. Increase the number of agents without changing responsibilities

### 70. A refund action needs validation of identity, target, and amount before the API call. Which guardrail fits?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Record structured audit events
- B. Validate and screen the final response before delivery
- C. Use supported prompt-prefix caching
- D. Authorize and validate the proposed tool action before execution

### 71. A workflow must distinguish several similarly named projects across compacted history. Which state design fits?

Domain: Develop multi-agent solutions in Azure

- A. Compact context into a validated summary
- B. Use an embedding-based retrieval index
- C. Select the largest available model for every task
- D. Maintain stable entity IDs and validated factual state

### 72. A workflow's stored summaries increasingly disagree with its original event history. Which issue is this?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Monitor changes in task inputs and agent behavior over time
- B. Fine-tune the underlying model
- C. Diagnose summary drift
- D. Diagnose sliding-window amnesia

### 73. An enterprise needs centralized credential lifecycle management for agent tools. Which Azure service fits?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Embed one shared long-lived credential in every prompt
- B. Use supported prompt-prefix caching
- C. Use an embedding-based retrieval index
- D. Store and retrieve secrets through Azure Key Vault

### 74. An existing agent endpoint returns task results to a sensitive workflow. Which TWO practices protect the integration? (Select TWO.)

Domain: Develop multi-agent solutions in Azure

- A. Fine-tune the underlying model
- B. Use one highly privileged identity for all agents
- C. Validate and treat remote results as untrusted input
- D. Log every raw prompt and credential without filtering
- E. Authenticate remote endpoints and authorize delegated operations

### 75. A platform needs to monitor customer-perceived reliability across several services. Which indicator strategy fits?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Measure end-to-end service-level indicators against objectives
- B. Collect aggregate operational metrics
- C. Use qualified human reviewers with a shared rubric
- D. Use supported prompt-prefix caching

### 76. A knowledge index needs smaller coherent units rather than whole books. Which preprocessing step fits?

Domain: Develop multi-agent solutions in Azure

- A. Fine-tune the underlying model
- B. Chunk documents into coherent retrievable passages
- C. Apply narrowly scoped Azure RBAC assignments
- D. Use supported prompt-prefix caching

### 77. An assistant fails to recall earlier details that are no longer supplied to the model. Which context limitation is illustrated?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Fine-tune the underlying model
- B. Monitor changes in task inputs and agent behavior over time
- C. Diagnose sliding-window amnesia
- D. Diagnose summary drift

### 78. An architect must store active conversation context but avoid unnecessary future reuse. Which memory class fits?

Domain: Architect multi-agent solutions

- A. Use governed long-term memory
- B. Use an embedding-based retrieval index
- C. Fine-tune the underlying model
- D. Use session-scoped short-term state

### 79. A release changes a tool schema from v1 to v2 and persists v2 workflow state. Reverting only the prompt still fails. What should the rollback plan have included?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Only a larger context window
- B. A compatible artifact set and an explicit state compatibility or migration plan
- C. Only disabling logs
- D. Only the previous prompt text

### 80. A developer needs the token usage and execution path of a specific failed task. Which evidence fits?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Collect aggregate operational metrics
- B. Inspect correlated spans with version and token metadata
- C. Select the largest available model for every task
- D. Add curated input-output examples to the prompt

### 81. A workflow update must preserve a trustworthy quality gate and identifiable prompt revisions. Which TWO practices fit? (Select TWO.)

Domain: Develop multi-agent solutions in Azure

- A. Allow unlimited autonomous retries and spawning
- B. Increase the number of agents without changing responsibilities
- C. Select the largest available model for every task
- D. Keep independent evaluation data and gate model changes
- E. Version prompts and evaluate changes before promotion

### 82. An agent workflow crosses hosting boundaries and needs end-to-end investigation. Which telemetry architecture fits?

Domain: Architect multi-agent solutions

- A. Use an embedding-based retrieval index
- B. Collect aggregate operational metrics
- C. Configure actionable health and quality alerts
- D. Propagate trace context across agents and tools

### 83. A tool server already exists; the new agent must act as its protocol consumer. Which implementation fits?

Domain: Develop multi-agent solutions in Azure

- A. Implement an MCP client that discovers and invokes permitted tools
- B. Implement an MCP server with explicit tool schemas and authorization
- C. Fine-tune the underlying model
- D. Use Agent2Agent (A2A) interoperability

### 84. A company wants to avoid a different tool integration format for each compatible client. Which protocol fits?

Domain: Architect multi-agent solutions

- A. Fine-tune the underlying model
- B. Expose a task-specific REST API
- C. Use Model Context Protocol (MCP)
- D. Use Agent2Agent (A2A) interoperability

### 85. A knowledge assistant must handle precise names and conceptual questions in the same corpus. Which approach fits?

Domain: Develop multi-agent solutions in Azure

- A. Fine-tune the underlying model
- B. Combine lexical and vector retrieval
- C. Compact context into a validated summary
- D. Use an embedding-based retrieval index

### 86. A team wants a supported workflow integration rather than writing every SaaS connector itself. Which service fits?

Domain: Develop multi-agent solutions in Azure

- A. Use a versioned development container and dependency lock
- B. Use Azure Logic Apps for suitable connector-based workflows
- C. Use Hugging Face Transformers for compatible model capabilities
- D. Re-embed content with a consistent compatible embedding configuration

### 87. A platform passes happy-path tests but has no evidence of safe fallback behavior. Which evaluation fits?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Add curated input-output examples to the prompt
- B. Select the largest available model for every task
- C. Evaluate whether generated claims are supported by supplied evidence
- D. Evaluate recovery, safe failure, and task completion under faults

### 88. A solution stores secrets centrally but grants all workloads broad retrieval and ignores rotation. Which TWO corrections fit? (Select TWO.)

Domain: Secure, govern, and deploy multi-agent solutions

- A. Embed one shared long-lived credential in every prompt
- B. Grant only required secret access to each workload
- C. Log every raw prompt and credential without filtering
- D. Use one highly privileged identity for all agents
- E. Rotate secrets and update dependent applications safely

### 89. Code review: a search filter uses tenant_id taken directly from request JSON. A signed-in user changes that JSON to another tenant. What is the most important correction?

Domain: Develop multi-agent solutions in Azure

- A. Derive the allowed tenant scope from trusted identity and enforce it in the server-side query
- B. Use a larger embedding model
- C. Ask the model to ignore results belonging to other tenants
- D. Filter the final answer only for tenant names

### 90. A purchasing assistant must pause before submitting a high-value order. Which control should the architect include?

Domain: Architect multi-agent solutions

- A. Apply content safety filters
- B. Compact context into a validated summary
- C. Insert a human approval gate before the consequential action
- D. Record structured audit events

### 91. A retrieval team wants a second relevance assessment before context assembly. Which technique fits?

Domain: Develop multi-agent solutions in Azure

- A. Use supported prompt-prefix caching
- B. Fine-tune the underlying model
- C. Rerank retrieved candidates before context selection
- D. Chunk documents into coherent retrievable passages

### 92. An agent graph loses progress when its host restarts. Which state-management capability is needed?

Domain: Develop multi-agent solutions in Azure

- A. Re-embed content with a consistent compatible embedding configuration
- B. Fine-tune the underlying model
- C. Use supported prompt-prefix caching
- D. Use explicit state transitions and checkpoints in a graph workflow

### 93. A coordinator selects subagents and merges their results into a final response. Which pattern is this?

Domain: Architect multi-agent solutions

- A. Use hub-and-spoke coordination
- B. Use a controlled handoff between specialist agents
- C. Use peer-to-peer coordination with bounded protocols
- D. Use sequential orchestration

### 94. An orchestrator should provide each specialist only the latest relevant task facts. Which context approach fits?

Domain: Develop multi-agent solutions in Azure

- A. Inject relevant authorized context at request time
- B. Use supported prompt-prefix caching
- C. Fine-tune the underlying model
- D. Compact context into a validated summary

### 95. A company compares managed containers, functions, and Kubernetes for its agent services. Which selection basis is appropriate?

Domain: Architect multi-agent solutions

- A. Use Azure Container Apps for suitable containerized services
- B. Select compute using workload, scaling, network, and reliability requirements
- C. Use Azure Functions for a suitable event-driven tool
- D. Use Azure Kubernetes Service when cluster-level control is required

### 96. A workload must avoid exhausting connections during multi-agent fan-out. Which control fits?

Domain: Develop multi-agent solutions in Azure

- A. Fine-tune the underlying model
- B. Select the largest available model for every task
- C. Bound concurrent agent and tool execution
- D. Allow unlimited autonomous retries and spawning

### 97. A risky change needs limited initial exposure rather than an immediate full traffic switch. Which deployment approach fits?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Maintain separate blue and green environments and switch traffic
- B. Promote through development, test, acceptance, and production
- C. Deploy changes directly to all production users without gates
- D. Release to a limited traffic cohort with health and quality gates

### 98. A platform must support replay investigation and independently testable agent boundaries. Which TWO design choices fit? (Select TWO.)

Domain: Architect multi-agent solutions

- A. Capture versioned replay inputs and sanitized execution events
- B. Increase the number of agents without changing responsibilities
- C. Select the largest available model for every task
- D. Define typed inputs, outputs, and responsibility ownership
- E. Collect aggregate operational metrics

### 99. A slow service consumes all workflow time without a defined failure path. Which control fits?

Domain: Develop multi-agent solutions in Azure

- A. Use supported prompt-prefix caching
- B. Apply deadlines, cancellation, and a safe fallback
- C. Select the largest available model for every task
- D. Allow unlimited autonomous retries and spawning

### 100. A knowledge assistant misses answer-bearing documents before generation begins. Which evaluation targets the failure?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Measure relevance of retrieved evidence against labeled queries
- B. Use qualified human reviewers with a shared rubric
- C. Evaluate whether generated claims are supported by supplied evidence
- D. Collect aggregate operational metrics

---

## Answer key and explanations

### Question 1 — A

Answer: Use a stable idempotency key and durable result tracking. When an operation may already have committed, a stable logical-action identifier prevents duplicate effects on retry. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#build-and-integrate-tool-ecosystems Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Correct. Prevents repeated requests for the same logical action from producing duplicate external effects.
- **B:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **C:** Incorrect for this requirement. Limits repeat attempts and avoids synchronized retry storms; non-idempotent operations require duplicate protection.
- **D:** Incorrect for this requirement. Supports accountability after and during execution but does not by itself stop an unapproved action.

### Question 2 — A

Answer: Maintain separate blue and green environments and switch traffic. Two prepared environments with traffic switching characterize blue/green; partial cohort exposure is a different strategy. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#deploy-multi-agent-solutions-to-azure Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Correct. Supports promotion and rollback by moving traffic between prepared environments, subject to state and compatibility planning.
- **B:** Incorrect for this requirement. Removes staged evidence and increases exposure to unreviewed errors.
- **C:** Incorrect for this requirement. Separates lifecycle stages with explicit validation and approval gates rather than treating a development success as production acceptance.
- **D:** Incorrect for this requirement. Limits initial exposure and expands only after measured outcomes meet criteria.

### Question 3 — B

Answer: Analyze user feedback with verified task outcomes. User signals should be connected to verified outcomes and reviewed before they drive changes. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#optimize-prompt-and-model-performance-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **B:** Correct. Turns real-world signals into reviewed improvements instead of equating popularity or raw engagement with correctness.
- **C:** Incorrect for this requirement. Shows rates, latency, and resource trends but does not alone reconstruct a particular cross-service execution.
- **D:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.

### Question 4 — C

Answer: Compare quality against a stable versioned baseline. A versioned baseline detects a change in task quality even when availability and response speed are unchanged. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-observability-and-monitoring-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **B:** Incorrect for this requirement. Shows rates, latency, and resource trends but does not alone reconstruct a particular cross-service execution.
- **C:** Correct. Detects worsened task outcomes after changes; a healthy process or fast response does not establish answer quality.
- **D:** Incorrect for this requirement. Separates worker availability and recurrent failure conditions from content-quality scoring alone.

### Question 5 — A

Answer: Validate and screen tool responses before reuse. External tool responses form a separate trust boundary and need checks before they influence later decisions. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-guardrails-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Correct. Checks external output structure and policy and treats embedded instructions as untrusted before it reaches another agent.
- **B:** Incorrect for this requirement. Supports accountability after and during execution but does not by itself stop an unapproved action.
- **C:** Incorrect for this requirement. Applies configured input-side controls, while downstream boundaries and output checks still remain necessary.
- **D:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.

### Question 6 — D

Answer: Evaluate memory retention, retrieval, isolation, and forgetting. Memory needs tests for correct recall and prohibited reuse, not only tests of current document retrieval. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-evaluation-and-validation-strategies-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Incorrect for this requirement. Evaluates whether search returns useful source material separately from whether generation uses it correctly.
- **B:** Incorrect for this requirement. Checks faithfulness to available context, not merely fluent language or relevant retrieved documents.
- **C:** Incorrect for this requirement. Tests whether the right authorized operation was invoked correctly and produced the intended result.
- **D:** Correct. Tests whether relevant authorized facts are recalled and prohibited or expired information is not reused.

### Question 7 — C

Answer: Use Agent2Agent (A2A) interoperability. Collaborating with a remote agent through an agent-facing contract calls for A2A rather than treating every peer as a raw resource server. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-logical-architecture-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/

- **A:** Incorrect for this requirement. Supports semantic lookup but is not automatically an authoritative transactional store for every workflow state.
- **B:** Incorrect for this requirement. Provides a standard interface for exposing tools, resources, and prompts to compatible clients; security remains a separate design duty.
- **C:** Correct. Supports collaboration with compatible remote agents through defined agent-facing contracts; it is not identical to a tool-resource interface.
- **D:** Incorrect for this requirement. Improves environment reproducibility; it does not by itself determine production architecture or access policies.

### Question 8 — D

Answer: Validate tool results against schema and domain constraints. Successful transport does not prove the payload is well-formed, plausible, or safe for downstream decisions. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#build-and-integrate-tool-ecosystems Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Supports accountability after and during execution but does not by itself stop an unapproved action.
- **B:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.
- **C:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **D:** Correct. Checks structure, types, ranges, and semantic consistency before downstream use; HTTP success alone is insufficient.

### Question 9 — C

Answer: Rotate secrets and update dependent applications safely. Credential lifecycle changes require coordinated application updates and revocation, not just a log entry or model change. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-security-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **B:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **C:** Correct. Changes credentials through a tested lifecycle with controlled overlap or rollout where supported, rather than retaining a leaked value.
- **D:** Incorrect for this requirement. Supports accountability after and during execution but does not by itself stop an unapproved action.

### Question 10 — C

Answer: Use supported prompt-prefix caching. Repeated eligible prompt prefixes can benefit from provider-supported processing reuse; this does not imply final-answer reuse. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#implement-multi-agent-orchestration Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Reuses prior results for a matching cache key when authorization and freshness permit, rather than matching approximate meaning.
- **B:** Incorrect for this requirement. Can reuse meaning-equivalent responses only when permissions, tenant scope, freshness, and task semantics allow it.
- **C:** Correct. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **D:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.

### Question 11 — C

Answer: Apply narrowly scoped Azure RBAC assignments. Resource access must be granted at the necessary principal and scope; behavioral instructions do not enforce Azure permissions. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-security-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Incorrect for this requirement. Can reduce supported harmful content but does not replace consent, permissions, human review, or all domain-specific policies.
- **B:** Incorrect for this requirement. Supports accountability after and during execution but does not by itself stop an unapproved action.
- **C:** Correct. Authorizes supported Azure resource operations for principals at appropriate scopes; it does not describe the full behavioral role of an agent.
- **D:** Incorrect for this requirement. Defines role, allowable behavior, autonomy, and boundaries, while enforcement still requires application controls.

### Question 12 — B

Answer: Benchmark models against task capability and operational constraints. Model choice requires task-specific evidence and operational fit rather than a single price or size ranking. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-logical-architecture-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/

- **A:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.
- **B:** Correct. Matches measured reasoning, modality, context, latency, cost, and deployment requirements instead of choosing only by size.
- **C:** Incorrect for this requirement. Ignores quality, retry cost, tool reliability, latency, and other business constraints.
- **D:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.

### Question 13 — B, C

Answer: Redact and access-control sensitive telemetry; Define alerts with bounded remediation and escalation. Useful monitoring requires protected telemetry and controlled incident response rather than unrestricted logs or loops. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-observability-and-monitoring-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.
- **B:** Correct. Preserves useful investigation evidence while avoiding unnecessary exposure of prompts, personal information, and secrets.
- **C:** Correct. Links detection to a controlled response with limits and human handoff rather than unchecked restart or retry loops.
- **D:** Incorrect for this requirement. Can cause runaway cost, load, and repeated side effects rather than providing reliable convergence.
- **E:** Incorrect for this requirement. Creates avoidable sensitive-data exposure and violates data-minimization and secret-handling requirements.

### Question 14 — D

Answer: Test interactions with configured external dependencies. Real component boundaries need contract, identity, networking, and dependency tests beyond isolated mocks. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#deploy-multi-agent-solutions-to-azure Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Incorrect for this requirement. Demonstrates desired behavior in context without modifying learned model weights.
- **B:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **C:** Incorrect for this requirement. Tests functions and logic in isolation, often with fakes or mocks; it does not prove live service integration.
- **D:** Correct. Verifies real contracts, authentication, networking, and service behavior across component boundaries.

### Question 15 — C

Answer: Attribute usage to tenants, projects, and workflow runs. Usage attribution needs trusted tenant and project metadata to support budgets and fair allocations. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-observability-and-monitoring-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.
- **B:** Incorrect for this requirement. Shows rates, latency, and resource trends but does not alone reconstruct a particular cross-service execution.
- **C:** Correct. Enables quotas, allocations, and chargeback using governed usage metadata instead of inferring all costs from one shared total.
- **D:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.

### Question 16 — B

Answer: Monitor agent health and workflow failure patterns. Availability and repeated operational failures need health and failure-pattern telemetry, not only language-quality evaluation. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-observability-and-monitoring-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Incorrect for this requirement. Checks faithfulness to available context, not merely fluent language or relevant retrieved documents.
- **B:** Correct. Separates worker availability and recurrent failure conditions from content-quality scoring alone.
- **C:** Incorrect for this requirement. Ignores quality, retry cost, tool reliability, latency, and other business constraints.
- **D:** Incorrect for this requirement. Demonstrates desired behavior in context without modifying learned model weights.

### Question 17 — B

Answer: Decompose the goal into bounded agent responsibilities and tools. Independent responsibilities and deterministic tools should be identified before adding autonomous workers. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-logical-architecture-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/

- **A:** Incorrect for this requirement. Can simplify coordination but does not establish the independently bounded specialist responsibilities required in this scenario.
- **B:** Correct. Defines who performs each task and which deterministic operations are exposed, instead of giving every agent the whole problem.
- **C:** Incorrect for this requirement. Adds coordination work without resolving unclear ownership, contracts, or workflow design.
- **D:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.

### Question 18 — D

Answer: Inspect and constrain user input before agent processing. Input-side intervention can reject or constrain risky incoming requests before they drive agent processing. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-guardrails-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Incorrect for this requirement. Supports accountability after and during execution but does not by itself stop an unapproved action.
- **B:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **C:** Incorrect for this requirement. Applies final output controls but cannot undo an unauthorized side effect that has already occurred.
- **D:** Correct. Applies configured input-side controls, while downstream boundaries and output checks still remain necessary.

### Question 19 — A

Answer: Assemble only relevant state, evidence, and tool results. Useful context is selected and budgeted, not built by blindly forwarding every conversation and tool result. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-agent-memory-context-management-and-knowledge-integration Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Correct. Builds useful request context within a token budget instead of forwarding every prior message.
- **B:** Incorrect for this requirement. Persists approved information beyond a session with access, retention, deletion, and relevance controls.
- **C:** Incorrect for this requirement. Can cause runaway cost, load, and repeated side effects rather than providing reliable convergence.
- **D:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.

### Question 20 — B

Answer: Implement deterministic domain-specific policy checks. Explicit business constraints require trusted domain checks; a generic content category filter does not enforce numeric or transactional policy. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-guardrails-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Incorrect for this requirement. Can reduce supported harmful content but does not replace consent, permissions, human review, or all domain-specific policies.
- **B:** Correct. Enforces explicit business constraints such as allowed amounts or prohibited operations in trusted code rather than relying only on generic toxicity filters.
- **C:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **D:** Incorrect for this requirement. Demonstrates desired behavior in context without modifying learned model weights.

### Question 21 — A

Answer: 1,200,000 tokens. Aggregate both input and output token volumes across runs. Monetary cost still depends on their separate prices and any applicable caching or other usage rules. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-observability-and-monitoring-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Correct. Each run uses 10,000 tokens, so 120 runs use 1,200,000.
- **B:** Incorrect for this requirement. This counts one run rather than all 120.
- **C:** Incorrect for this requirement. This counts only the input tokens.
- **D:** Incorrect for this requirement. This counts only the output tokens.

### Question 22 — A

Answer: Use parallel orchestration with a controlled join. Independent tasks can run concurrently; join logic should combine their completed outputs. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-logical-architecture-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/

- **A:** Correct. Runs independent branches concurrently and combines their results after completion.
- **B:** Incorrect for this requirement. Transfers task responsibility to the appropriate specialist with explicit context and termination rules.
- **C:** Incorrect for this requirement. Can simplify coordination but does not establish the independently bounded specialist responsibilities required in this scenario.
- **D:** Incorrect for this requirement. Passes work through dependent stages where later tasks require earlier outputs.

### Question 23 — A

Answer: Deploy versioned infrastructure as code through reviewed automation. Reviewed infrastructure definitions improve reproducibility across environments and make deployment configuration auditable. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#deploy-multi-agent-solutions-to-azure Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Correct. Makes environment configuration reproducible and auditable, with environment-specific identity and policy settings.
- **B:** Incorrect for this requirement. Makes instruction changes reproducible, comparable, and reversible.
- **C:** Incorrect for this requirement. Demonstrates desired behavior in context without modifying learned model weights.
- **D:** Incorrect for this requirement. Removes staged evidence and increases exposure to unreviewed errors.

### Question 24 — A

Answer: Generate and validate diverse synthetic evaluation cases. Generated tests expand coverage only after validation; synthetic labels and examples can introduce new errors or blind spots. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#optimize-prompt-and-model-performance-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Correct. Expands test coverage while checking labels, realism, duplicates, and gaps; generated examples are not automatically valid.
- **B:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.
- **C:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **D:** Incorrect for this requirement. Can cause runaway cost, load, and repeated side effects rather than providing reliable convergence.

### Question 25 — C

Answer: Validate OAuth access tokens and enforce audience and scopes. A receiving API must verify token validity and intended audience and enforce permissions for the operation. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-security-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Incorrect for this requirement. Makes instruction changes reproducible, comparable, and reversible.
- **B:** Incorrect for this requirement. Supports accountability after and during execution but does not by itself stop an unapproved action.
- **C:** Correct. Checks that a token is valid for the receiving API and the requested operation; possession of any token is not sufficient.
- **D:** Incorrect for this requirement. Can authenticate supported service access but is a secret and generally does not carry a delegated user identity by itself.

### Question 26 — D, E

Answer: Use distinct scoped identities and verify every boundary; Define retention, deletion, and tenant-isolation rules for state. Scoped identities constrain access, while state lifecycle and isolation policies constrain persistent data use. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#specify-technology-components-to-include-in-a-multi-agent-solution Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/

- **A:** Incorrect for this requirement. Simplifies credential sharing but removes per-agent isolation and increases the impact of compromise.
- **B:** Incorrect for this requirement. Can cause runaway cost, load, and repeated side effects rather than providing reliable convergence.
- **C:** Incorrect for this requirement. Creates avoidable sensitive-data exposure and violates data-minimization and secret-handling requirements.
- **D:** Correct. Reduces lateral movement by treating each agent and service interaction as an independently authorized access decision.
- **E:** Correct. Establishes who may use stored information and for how long, instead of assuming persistence implies permission.

### Question 27 — B

Answer: Specify each agent persona, scope, and escalation rules. Behavioral scope and escalation must be specified for each role; resource permissions alone do not define its purpose. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-logical-architecture-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/

- **A:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **B:** Correct. Defines role, allowable behavior, autonomy, and boundaries, while enforcement still requires application controls.
- **C:** Incorrect for this requirement. Authorizes supported Azure resource operations for principals at appropriate scopes; it does not describe the full behavioral role of an agent.
- **D:** Incorrect for this requirement. Shows rates, latency, and resource trends but does not alone reconstruct a particular cross-service execution.

### Question 28 — B

Answer: Place appropriate policies at Azure API Management. API policy enforcement and request governance are gateway responsibilities, separate from model training and tool execution. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#build-and-integrate-tool-ecosystems Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Fits bounded event-driven operations when execution, hosting, networking, and scaling limits meet the workload.
- **B:** Correct. Provides an API governance layer for authentication, traffic management, and policies; it does not by itself grant downstream data permissions.
- **C:** Incorrect for this requirement. Supports semantic lookup but is not automatically an authoritative transactional store for every workflow state.
- **D:** Incorrect for this requirement. Provides model and pipeline tooling for supported architectures; it is not a replacement for agent authorization or orchestration design.

### Question 29 — C

Answer: Separate session state, shared team state, and long-term memory. Different state classes need distinct persistence, consistency, access, and lifecycle policies. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#specify-technology-components-to-include-in-a-multi-agent-solution Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/

- **A:** Incorrect for this requirement. Can simplify coordination but does not establish the independently bounded specialist responsibilities required in this scenario.
- **B:** Incorrect for this requirement. Supports semantic lookup but is not automatically an authoritative transactional store for every workflow state.
- **C:** Correct. Assigns each state class suitable persistence, consistency, isolation, and lifecycle controls.
- **D:** Incorrect for this requirement. Retains information for an active interaction or workflow rather than serving as unrestricted persistent cross-session memory.

### Question 30 — A

Answer: Use bounded retries with backoff and jitter for transient failures. Transient failures may justify limited retries with backoff, not unlimited repeats or changes to model weights. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#build-and-integrate-tool-ecosystems Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Correct. Limits repeat attempts and avoids synchronized retry storms; non-idempotent operations require duplicate protection.
- **B:** Incorrect for this requirement. Adds coordination work without resolving unclear ownership, contracts, or workflow design.
- **C:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **D:** Incorrect for this requirement. Can cause runaway cost, load, and repeated side effects rather than providing reliable convergence.

### Question 31 — B

Answer: Add curated input-output examples to the prompt. A few demonstrations in context can clarify expected behavior without a training job. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-advanced-prompt-engineering-strategies-in-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.
- **B:** Correct. Demonstrates desired behavior in context without modifying learned model weights.
- **C:** Incorrect for this requirement. Adapts learned behavior when justified, with defined data quality, refresh triggers, and regression checks.
- **D:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.

### Question 32 — B

Answer: Run regression tests and automated agent evaluations. Release checks should preserve previously accepted agent behavior across code, model, prompt, and tool changes. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#deploy-multi-agent-solutions-to-azure Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Incorrect for this requirement. Adds coordination work without resolving unclear ownership, contracts, or workflow design.
- **B:** Correct. Checks that previously accepted behavior and quality are preserved after prompt, model, tool, or code changes.
- **C:** Incorrect for this requirement. Tests functions and logic in isolation, often with fakes or mocks; it does not prove live service integration.
- **D:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.

### Question 33 — C

Answer: Use Hugging Face Transformers for compatible model capabilities. The requested capability is compatible model and pipeline tooling, not API policy or integration-protocol hosting. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#implement-multi-agent-orchestration Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Provides an API governance layer for authentication, traffic management, and policies; it does not by itself grant downstream data permissions.
- **B:** Incorrect for this requirement. Coordinates supported connectors and integration steps, including approval patterns where configured; it is not a model-training library.
- **C:** Correct. Provides model and pipeline tooling for supported architectures; it is not a replacement for agent authorization or orchestration design.
- **D:** Incorrect for this requirement. Provides a standard interface for exposing tools, resources, and prompts to compatible clients; security remains a separate design duty.

### Question 34 — B

Answer: Use an Azure managed identity where supported. Supported workload identity avoids embedding application credentials, while a separate authorization assignment still limits resource access. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-security-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Incorrect for this requirement. Can authenticate supported service access but is a secret and generally does not carry a delegated user identity by itself.
- **B:** Correct. Lets an Azure workload obtain identity-based access without embedding a long-lived application secret; resource authorization is still required.
- **C:** Incorrect for this requirement. Simplifies credential sharing but removes per-agent isolation and increases the impact of compromise.
- **D:** Incorrect for this requirement. Reduces active context size but can omit details; important facts need preservation and verification.

### Question 35 — D

Answer: Run a representative held-out prompt regression suite. A versioned independent test suite reveals regressions across representative cases rather than only author-selected examples. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-evaluation-and-validation-strategies-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.
- **B:** Incorrect for this requirement. Demonstrates desired behavior in context without modifying learned model weights.
- **C:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **D:** Correct. Compares instruction or model changes on independent realistic cases, including difficult and safety-relevant inputs.

### Question 36 — D

Answer: Use an on-behalf-of flow for delegated downstream access. When downstream authorization must reflect the signed-in user, a supported delegated OBO flow differs from app-only identity. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-security-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Incorrect for this requirement. Lets an Azure workload obtain identity-based access without embedding a long-lived application secret; resource authorization is still required.
- **B:** Incorrect for this requirement. Can authenticate supported service access but is a secret and generally does not carry a delegated user identity by itself.
- **C:** Incorrect for this requirement. Simplifies credential sharing but removes per-agent isolation and increases the impact of compromise.
- **D:** Correct. Exchanges a user assertion through the middle tier for an appropriate downstream token, preserving delegated user context where supported.

### Question 37 — D

Answer: Re-embed content with a consistent compatible embedding configuration. Query and document vectors need a compatible embedding space; changing the model may require reindexing. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-agent-memory-context-management-and-knowledge-integration Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Improves ordering within a candidate set; it cannot recover a document never retrieved.
- **B:** Incorrect for this requirement. Reduces active context size but can omit details; important facts need preservation and verification.
- **C:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **D:** Correct. Keeps query and document representations in the same semantic space; mixing incompatible model versions can break relevance.

### Question 38 — B

Answer: Coordinate concurrency, rate budgets, and backoff. Excess concurrency can increase throttling, so throughput optimization must respect downstream rate budgets. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#optimize-prompt-and-model-performance-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Incorrect for this requirement. Can cause runaway cost, load, and repeated side effects rather than providing reliable convergence.
- **B:** Correct. Controls request pressure on limited services; unconstrained parallelism can increase throttling and latency.
- **C:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **D:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.

### Question 39 — C

Answer: Optimize the dependent critical path and parallelize independent work. Only independent work can be safely overlapped; dependent stages still determine the critical path. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#optimize-prompt-and-model-performance-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Incorrect for this requirement. Adds coordination work without resolving unclear ownership, contracts, or workflow design.
- **B:** Incorrect for this requirement. Can cause runaway cost, load, and repeated side effects rather than providing reliable convergence.
- **C:** Correct. Focuses on steps determining end-to-end duration while respecting task dependencies and resource constraints.
- **D:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.

### Question 40 — D

Answer: Supplement vector recall with authoritative structured lookup. Exact relationships and authoritative facts may require structured lookup rather than nearest-neighbor similarity alone. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#optimize-prompt-and-model-performance-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Incorrect for this requirement. Improves ordering within a candidate set; it cannot recover a document never retrieved.
- **B:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.
- **C:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **D:** Correct. Addresses exact facts, dates, counts, or entity relationships that semantic similarity alone may fail to recover reliably.

### Question 41 — C

Answer: Use isolated unit tests for deterministic components. Isolated deterministic logic can be tested with controlled dependencies; this does not replace live integration checks. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#deploy-multi-agent-solutions-to-azure Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Incorrect for this requirement. Uses challenging and misuse-oriented tests, including supported Foundry red-teaming capabilities, to discover risks before and after release.
- **B:** Incorrect for this requirement. Limits initial exposure and expands only after measured outcomes meet criteria.
- **C:** Correct. Tests functions and logic in isolation, often with fakes or mocks; it does not prove live service integration.
- **D:** Incorrect for this requirement. Verifies real contracts, authentication, networking, and service behavior across component boundaries.

### Question 42 — A

Answer: Run adversarial testing early and throughout the lifecycle. Adversarial evaluation should begin before release and continue as the system changes; it does not establish an absolute safety guarantee. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-security-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Correct. Uses challenging and misuse-oriented tests, including supported Foundry red-teaming capabilities, to discover risks before and after release.
- **B:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **C:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.
- **D:** Incorrect for this requirement. Removes staged evidence and increases exposure to unreviewed errors.

### Question 43 — D

Answer: Maintain stable entity IDs and validated factual state. Entity continuity requires stable identity and factual state across transitions, not merely more similar text. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#optimize-prompt-and-model-performance-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **B:** Incorrect for this requirement. Identifies accumulated distortion when repeated summarization alters or omits important facts.
- **C:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **D:** Correct. Preserves identity and critical facts across summaries and agent transitions rather than relying on ambiguous names alone.

### Question 44 — D

Answer: Evaluate whether generated claims are supported by supplied evidence. Relevant retrieval does not guarantee the final answer is supported; generated claims need evidence checking. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-evaluation-and-validation-strategies-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Incorrect for this requirement. Ignores quality, retry cost, tool reliability, latency, and other business constraints.
- **B:** Incorrect for this requirement. Shows rates, latency, and resource trends but does not alone reconstruct a particular cross-service execution.
- **C:** Incorrect for this requirement. Evaluates whether search returns useful source material separately from whether generation uses it correctly.
- **D:** Correct. Checks faithfulness to available context, not merely fluent language or relevant retrieved documents.

### Question 45 — A

Answer: Evaluate tool choice, arguments, outcomes, and side effects. A tool workflow needs outcome and side-effect checks; a plausible final explanation can hide an incorrect operation. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-evaluation-and-validation-strategies-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Correct. Tests whether the right authorized operation was invoked correctly and produced the intended result.
- **B:** Incorrect for this requirement. Checks faithfulness to available context, not merely fluent language or relevant retrieved documents.
- **C:** Incorrect for this requirement. Evaluates nuanced correctness, usefulness, and safety while documenting reviewer disagreement and escalation.
- **D:** Incorrect for this requirement. Evaluates whether search returns useful source material separately from whether generation uses it correctly.

### Question 46 — D

Answer: Implement a controlled agent workflow with explicit review and resume. A human checkpoint must pause action, preserve correlation, and resume only after a valid decision and authorization check. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#implement-multi-agent-orchestration Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **B:** Incorrect for this requirement. Demonstrates desired behavior in context without modifying learned model weights.
- **C:** Incorrect for this requirement. Supports accountability after and during execution but does not by itself stop an unapproved action.
- **D:** Correct. Coordinates agent steps and human intervention in a framework-supported workflow, with durable correlation and revalidation before action.

### Question 47 — A

Answer: Promote through development, test, acceptance, and production. Environment stages separate development from progressively validated production promotion. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#deploy-multi-agent-solutions-to-azure Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Correct. Separates lifecycle stages with explicit validation and approval gates rather than treating a development success as production acceptance.
- **B:** Incorrect for this requirement. Supports promotion and rollback by moving traffic between prepared environments, subject to state and compatibility planning.
- **C:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **D:** Incorrect for this requirement. Removes staged evidence and increases exposure to unreviewed errors.

### Question 48 — B, E

Answer: Promote the same immutable versioned artifacts across environments; Use separate environment identities and configuration. Identifiable artifacts and separate environment authority reduce release drift and accidental production effects. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#deploy-multi-agent-solutions-to-azure Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Incorrect for this requirement. Removes staged evidence and increases exposure to unreviewed errors.
- **B:** Correct. Prevents development or test access from inheriting production authority and reduces accidental cross-environment effects.
- **C:** Incorrect for this requirement. Can cause runaway cost, load, and repeated side effects rather than providing reliable convergence.
- **D:** Incorrect for this requirement. Simplifies credential sharing but removes per-agent isolation and increases the impact of compromise.
- **E:** Correct. Reduces unreviewed differences by tracking code, prompt, model, tool schema, and deployment configuration versions.

### Question 49 — B

Answer: Use a versioned development container and dependency lock. A reproducible development environment and dependency lock reduce local setup drift; production hosting solves a different problem. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#specify-technology-components-to-include-in-a-multi-agent-solution Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/

- **A:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **B:** Correct. Improves environment reproducibility; it does not by itself determine production architecture or access policies.
- **C:** Incorrect for this requirement. Provides managed container hosting and supported scaling features, subject to runtime and connectivity requirements.
- **D:** Incorrect for this requirement. Communicates coding conventions and boundaries to development assistants; it is not a runtime authorization system.

### Question 50 — C

Answer: Separate trusted instructions from untrusted content. Untrusted documents should not acquire instruction authority merely because they appear in a model context. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-advanced-prompt-engineering-strategies-in-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **B:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **C:** Correct. Reduces instruction confusion by treating retrieved or user-supplied material as data; enforcement still needs layered controls.
- **D:** Incorrect for this requirement. Supports accountability after and during execution but does not by itself stop an unapproved action.

### Question 51 — A, B

Answer: Benchmark a smaller adequate model for selected tasks; Remove irrelevant context while preserving necessary evidence. Model fit and context efficiency can reduce cost, but both changes must preserve measured quality and safety. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#optimize-prompt-and-model-performance-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Correct. May reduce inference cost and latency if measured quality, safety, and tool reliability remain acceptable.
- **B:** Correct. Reduces wasted tokens and can improve focus, but must not discard required facts or policy constraints.
- **C:** Incorrect for this requirement. Can cause runaway cost, load, and repeated side effects rather than providing reliable convergence.
- **D:** Incorrect for this requirement. Adds coordination work without resolving unclear ownership, contracts, or workflow design.
- **E:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.

### Question 52 — B

Answer: Use a governed semantic response cache. Meaning-equivalent response reuse needs a governed similarity cache with strict access and freshness boundaries. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#implement-multi-agent-orchestration Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Reuses prior results for a matching cache key when authorization and freshness permit, rather than matching approximate meaning.
- **B:** Correct. Can reuse meaning-equivalent responses only when permissions, tenant scope, freshness, and task semantics allow it.
- **C:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **D:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.

### Question 53 — B

Answer: Execute a validated function call in application code. A model-produced tool request is a proposal; authorized application code must validate and execute it. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#build-and-integrate-tool-ecosystems Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Demonstrates desired behavior in context without modifying learned model weights.
- **B:** Correct. The model proposes structured tool arguments, while trusted code authorizes and performs the operation.
- **C:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **D:** Incorrect for this requirement. Reduces active context size but can omit details; important facts need preservation and verification.

### Question 54 — B

Answer: Gate CI/CD on reviewed artifacts, security checks, and evaluations. CI/CD should require reviewed artifacts and passing checks before promotion rather than treating successful packaging as acceptance. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#deploy-multi-agent-solutions-to-azure Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Incorrect for this requirement. Demonstrates desired behavior in context without modifying learned model weights.
- **B:** Correct. Automates build and release evidence while preventing failed checks from silently promoting a release.
- **C:** Incorrect for this requirement. Removes staged evidence and increases exposure to unreviewed errors.
- **D:** Incorrect for this requirement. Supports accountability after and during execution but does not by itself stop an unapproved action.

### Question 55 — D

Answer: Calibrate LLM-as-a-judge against expert-labeled cases. Automated judges can be biased or wrong; calibration and ongoing audits are required. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#optimize-prompt-and-model-performance-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **B:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.
- **C:** Incorrect for this requirement. Shows rates, latency, and resource trends but does not alone reconstruct a particular cross-service execution.
- **D:** Correct. Measures agreement, bias, and failure modes of automated judging rather than treating judge output as unquestionable truth.

### Question 56 — D

Answer: Compact context into a validated summary. Compaction reduces active context while requiring validation of important facts and links to authoritative state. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-agent-memory-context-management-and-knowledge-integration Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Persists approved information beyond a session with access, retention, deletion, and relevance controls.
- **B:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **C:** Incorrect for this requirement. Adds coordination work without resolving unclear ownership, contracts, or workflow design.
- **D:** Correct. Reduces active context size but can omit details; important facts need preservation and verification.

### Question 57 — C

Answer: Use governed long-term memory. Approved persistent knowledge or preferences need governed long-term memory rather than reliance on an active context window. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-logical-architecture-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/

- **A:** Incorrect for this requirement. Retains information for an active interaction or workflow rather than serving as unrestricted persistent cross-session memory.
- **B:** Incorrect for this requirement. Reduces active context size but can omit details; important facts need preservation and verification.
- **C:** Correct. Persists approved information beyond a session with access, retention, deletion, and relevance controls.
- **D:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.

### Question 58 — C

Answer: Use sequential orchestration. Later stages require validated outputs from earlier stages, making a dependency-ordered flow appropriate. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-logical-architecture-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/

- **A:** Incorrect for this requirement. Runs independent branches concurrently and combines their results after completion.
- **B:** Incorrect for this requirement. Allows agents to communicate directly, but requires explicit ownership, convergence, and safety controls.
- **C:** Correct. Passes work through dependent stages where later tasks require earlier outputs.
- **D:** Incorrect for this requirement. Centralizes dispatch and aggregation through a coordinator while specialists handle bounded work.

### Question 59 — A

Answer: Design clear AI disclosure, user control, and recovery paths. Human-AI experience includes understandable boundaries and user control, not only technical filtering. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-logical-architecture-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/

- **A:** Correct. Supports the human-AI experience by communicating limits and allowing correction, cancellation, and escalation.
- **B:** Incorrect for this requirement. Can reduce supported harmful content but does not replace consent, permissions, human review, or all domain-specific policies.
- **C:** Incorrect for this requirement. Supports accountability after and during execution but does not by itself stop an unapproved action.
- **D:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.

### Question 60 — D, E

Answer: Authorize and validate the proposed tool action before execution; Validate and screen tool responses before reuse. The requested controls apply immediately around tool execution, not only to final user-facing text. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-guardrails-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **B:** Incorrect for this requirement. Supports accountability after and during execution but does not by itself stop an unapproved action.
- **C:** Incorrect for this requirement. Applies final output controls but cannot undo an unauthorized side effect that has already occurred.
- **D:** Correct. Checks external output structure and policy and treats embedded instructions as untrusted before it reaches another agent.
- **E:** Correct. Checks caller authority, arguments, target, and domain restrictions before an external effect occurs.

### Question 61 — A

Answer: Use supported private endpoints and correct private DNS. Private connectivity requires consistent endpoint, DNS, route, and access configuration rather than merely a private-looking URL. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-security-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Correct. Provides private connectivity to supported services when network routes, DNS, and public-access settings are configured consistently.
- **B:** Incorrect for this requirement. May bypass a connection problem by removing intended isolation, but does not satisfy a private-only design.
- **C:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **D:** Incorrect for this requirement. Can reduce supported harmful content but does not replace consent, permissions, human review, or all domain-specific policies.

### Question 62 — A

Answer: Use reusable middleware for cross-cutting controls. Reusable cross-cutting behavior belongs in controlled middleware rather than being duplicated or entrusted only to model text. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#implement-multi-agent-orchestration Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Correct. Centralizes concerns such as authorization, trace enrichment, and exception handling without duplicating them in every agent.
- **B:** Incorrect for this requirement. Demonstrates desired behavior in context without modifying learned model weights.
- **C:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **D:** Incorrect for this requirement. Supports semantic lookup but is not automatically an authoritative transactional store for every workflow state.

### Question 63 — A

Answer: Implement an MCP server with explicit tool schemas and authorization. The provider side exposes capabilities through MCP while enforcing contracts and access. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#build-and-integrate-tool-ecosystems Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Correct. Exposes supported tools and resources through MCP while validating arguments and enforcing caller permissions.
- **B:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **C:** Incorrect for this requirement. Consumes the server interface and handles tool results under application policy; discovery is not permission to execute every tool.
- **D:** Incorrect for this requirement. Supports collaboration with compatible remote agents through defined agent-facing contracts; it is not identical to a tool-resource interface.

### Question 64 — C

Answer: Validate and screen the final response before delivery. Final delivery is its own intervention point, though it does not replace controls before tool effects. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-guardrails-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Incorrect for this requirement. Applies configured input-side controls, while downstream boundaries and output checks still remain necessary.
- **B:** Incorrect for this requirement. Supports accountability after and during execution but does not by itself stop an unapproved action.
- **C:** Correct. Applies final output controls but cannot undo an unauthorized side effect that has already occurred.
- **D:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.

### Question 65 — C

Answer: Use qualified human reviewers with a shared rubric. Nuanced evaluations require a consistent rubric and qualified judgment; operational statistics alone cannot assess them. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-evaluation-and-validation-strategies-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Incorrect for this requirement. Ignores quality, retry cost, tool reliability, latency, and other business constraints.
- **B:** Incorrect for this requirement. Shows rates, latency, and resource trends but does not alone reconstruct a particular cross-service execution.
- **C:** Correct. Evaluates nuanced correctness, usefulness, and safety while documenting reviewer disagreement and escalation.
- **D:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.

### Question 66 — B

Answer: Use a supported fine-tuning strategy with curated data and held-out evaluation. Persistent task behavior may justify supported fine-tuning; the decision needs curated examples, refresh triggers, and independent evaluation. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-advanced-prompt-engineering-strategies-in-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Adds coordination work without resolving unclear ownership, contracts, or workflow design.
- **B:** Correct. Adapts learned behavior when justified, with defined data quality, refresh triggers, and regression checks.
- **C:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **D:** Incorrect for this requirement. Addresses changing external facts without repeatedly training those facts into model weights.

### Question 67 — A, B

Answer: Enforce per-run token, tool-call, and spawn budgets; Propagate cancellation through dependent branches. Global work budgets and cancellation propagation control runaway delegation across the whole run. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#implement-multi-agent-orchestration Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Correct. Stops unnecessary downstream work after a user cancels, a deadline expires, or the workflow reaches a terminal condition.
- **B:** Correct. Creates explicit termination and cost boundaries across the whole workflow, including delegated work.
- **C:** Incorrect for this requirement. Adds coordination work without resolving unclear ownership, contracts, or workflow design.
- **D:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **E:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.

### Question 68 — D

Answer: Apply purpose-based memory retention and deletion. Persisted memory remains subject to approved purpose and retention; storage does not create indefinite permission. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-agent-memory-context-management-and-knowledge-integration Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Keeps query and document representations in the same semantic space; mixing incompatible model versions can break relevance.
- **B:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **C:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **D:** Correct. Expires or deletes retained information according to policy rather than assuming all remembered content remains authorized forever.

### Question 69 — A

Answer: Version prompts and evaluate changes before promotion. Prompt changes require identifiable versions and evaluation so regressions can be attributed and rolled back. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-advanced-prompt-engineering-strategies-in-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Correct. Makes instruction changes reproducible, comparable, and reversible.
- **B:** Incorrect for this requirement. Shows rates, latency, and resource trends but does not alone reconstruct a particular cross-service execution.
- **C:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **D:** Incorrect for this requirement. Adds coordination work without resolving unclear ownership, contracts, or workflow design.

### Question 70 — D

Answer: Authorize and validate the proposed tool action before execution. Authorization and business validation must occur before the external action; final text screening is too late. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-guardrails-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Incorrect for this requirement. Supports accountability after and during execution but does not by itself stop an unapproved action.
- **B:** Incorrect for this requirement. Applies final output controls but cannot undo an unauthorized side effect that has already occurred.
- **C:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **D:** Correct. Checks caller authority, arguments, target, and domain restrictions before an external effect occurs.

### Question 71 — D

Answer: Maintain stable entity IDs and validated factual state. Stable identifiers and verified factual state prevent confusion when similar entities appear across handoffs. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-agent-memory-context-management-and-knowledge-integration Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Reduces active context size but can omit details; important facts need preservation and verification.
- **B:** Incorrect for this requirement. Supports semantic lookup but is not automatically an authoritative transactional store for every workflow state.
- **C:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.
- **D:** Correct. Preserves identity and critical facts across summaries and agent transitions rather than relying on ambiguous names alone.

### Question 72 — C

Answer: Diagnose summary drift. Repeated compaction can distort retained facts; authoritative state and summary checks help detect this. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#optimize-prompt-and-model-performance-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Incorrect for this requirement. Detects shifts in operating conditions or behavioral patterns that can require investigation and reassessment.
- **B:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **C:** Correct. Identifies accumulated distortion when repeated summarization alters or omits important facts.
- **D:** Incorrect for this requirement. Identifies loss of earlier information as it drops out of active context; this is distinct from a model weight update.

### Question 73 — D

Answer: Store and retrieve secrets through Azure Key Vault. Secrets need governed storage and authorized retrieval rather than inclusion in prompts, source files, or semantic memory. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-security-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Incorrect for this requirement. Exposes a powerful secret across model interactions and removes per-workload access separation.
- **B:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **C:** Incorrect for this requirement. Supports semantic lookup but is not automatically an authoritative transactional store for every workflow state.
- **D:** Correct. Centralizes supported secrets, keys, and certificates with controlled access and lifecycle management.

### Question 74 — C, E

Answer: Authenticate remote endpoints and authorize delegated operations; Validate and treat remote results as untrusted input. Protocol compatibility does not establish caller permission or make remote outputs trustworthy. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#implement-multi-agent-orchestration Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **B:** Incorrect for this requirement. Simplifies credential sharing but removes per-agent isolation and increases the impact of compromise.
- **C:** Correct. Checks returned structure and content and prevents remote output from overriding trusted instructions or permissions.
- **D:** Incorrect for this requirement. Creates avoidable sensitive-data exposure and violates data-minimization and secret-handling requirements.
- **E:** Correct. Checks the identity, audience, and scope of agent or tool calls instead of trusting interoperability alone.

### Question 75 — A

Answer: Measure end-to-end service-level indicators against objectives. Successful end-to-end outcomes matter; individually healthy components can still form an unreliable workflow. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-observability-and-monitoring-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Correct. Checks availability, latency, and successful completion from the workflow perspective rather than relying only on component uptime.
- **B:** Incorrect for this requirement. Shows rates, latency, and resource trends but does not alone reconstruct a particular cross-service execution.
- **C:** Incorrect for this requirement. Evaluates nuanced correctness, usefulness, and safety while documenting reviewer disagreement and escalation.
- **D:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.

### Question 76 — B

Answer: Chunk documents into coherent retrievable passages. Retrievable passage size and boundaries determine whether evidence is both focused and sufficiently contextual. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-agent-memory-context-management-and-knowledge-integration Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **B:** Correct. Controls retrieval granularity; excessive size wastes context, while tiny isolated chunks can lose meaning.
- **C:** Incorrect for this requirement. Authorizes supported Azure resource operations for principals at appropriate scopes; it does not describe the full behavioral role of an agent.
- **D:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.

### Question 77 — C

Answer: Diagnose sliding-window amnesia. Facts can disappear when older messages leave the active window even if no memory summary has changed. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#optimize-prompt-and-model-performance-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **B:** Incorrect for this requirement. Detects shifts in operating conditions or behavioral patterns that can require investigation and reassessment.
- **C:** Correct. Identifies loss of earlier information as it drops out of active context; this is distinct from a model weight update.
- **D:** Incorrect for this requirement. Identifies accumulated distortion when repeated summarization alters or omits important facts.

### Question 78 — D

Answer: Use session-scoped short-term state. Temporary interaction state should be scoped to the session instead of being persisted as general memory. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-logical-architecture-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/

- **A:** Incorrect for this requirement. Persists approved information beyond a session with access, retention, deletion, and relevance controls.
- **B:** Incorrect for this requirement. Supports semantic lookup but is not automatically an authoritative transactional store for every workflow state.
- **C:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **D:** Correct. Retains information for an active interaction or workflow rather than serving as unrestricted persistent cross-session memory.

### Question 79 — B

Answer: A compatible artifact set and an explicit state compatibility or migration plan. Rollback is a system operation, not necessarily a single-file revert. Test recovery with persisted in-flight state and external side effects before relying on it. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#deploy-multi-agent-solutions-to-azure Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Incorrect for this requirement. More context does not restore a broken tool or state contract.
- **B:** Correct. Code, prompt, tool contract, and durable state must work together during recovery.
- **C:** Incorrect for this requirement. Removing evidence does not repair compatibility and harms investigation.
- **D:** Incorrect for this requirement. The observed failure involves additional incompatible components.

### Question 80 — B

Answer: Inspect correlated spans with version and token metadata. Correlated spans connect a particular run to its latency, version, tokens, and tool steps. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-observability-and-monitoring-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Incorrect for this requirement. Shows rates, latency, and resource trends but does not alone reconstruct a particular cross-service execution.
- **B:** Correct. Connects latency, usage, prompts, and tool execution to a particular run, subject to privacy controls.
- **C:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.
- **D:** Incorrect for this requirement. Demonstrates desired behavior in context without modifying learned model weights.

### Question 81 — D, E

Answer: Keep independent evaluation data and gate model changes; Version prompts and evaluate changes before promotion. Independent evaluation and versioned instructions make behavioral changes measurable and reversible. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-advanced-prompt-engineering-strategies-in-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Can cause runaway cost, load, and repeated side effects rather than providing reliable convergence.
- **B:** Incorrect for this requirement. Adds coordination work without resolving unclear ownership, contracts, or workflow design.
- **C:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.
- **D:** Correct. Measures generalization and regression without using the same examples to train and certify a change.
- **E:** Correct. Makes instruction changes reproducible, comparable, and reversible.

### Question 82 — D

Answer: Propagate trace context across agents and tools. Cross-service trace context is needed to connect individual agent and tool operations into one execution. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#specify-technology-components-to-include-in-a-multi-agent-solution Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/

- **A:** Incorrect for this requirement. Supports semantic lookup but is not automatically an authoritative transactional store for every workflow state.
- **B:** Incorrect for this requirement. Shows rates, latency, and resource trends but does not alone reconstruct a particular cross-service execution.
- **C:** Incorrect for this requirement. Detects defined conditions and triggers response but does not itself retain all evidence required for deterministic investigation.
- **D:** Correct. Correlates spans across service boundaries to reconstruct an end-to-end execution path.

### Question 83 — A

Answer: Implement an MCP client that discovers and invokes permitted tools. The consumer side discovers and invokes permitted MCP capabilities, handling responses under application policy. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#build-and-integrate-tool-ecosystems Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Correct. Consumes the server interface and handles tool results under application policy; discovery is not permission to execute every tool.
- **B:** Incorrect for this requirement. Exposes supported tools and resources through MCP while validating arguments and enforcing caller permissions.
- **C:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **D:** Incorrect for this requirement. Supports collaboration with compatible remote agents through defined agent-facing contracts; it is not identical to a tool-resource interface.

### Question 84 — C

Answer: Use Model Context Protocol (MCP). The requirement is a standard tool-resource interface, not delegation to another independent agent. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-logical-architecture-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/

- **A:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **B:** Incorrect for this requirement. Provides a conventional HTTP contract but does not inherently implement a requested agent or MCP interoperability standard.
- **C:** Correct. Provides a standard interface for exposing tools, resources, and prompts to compatible clients; security remains a separate design duty.
- **D:** Incorrect for this requirement. Supports collaboration with compatible remote agents through defined agent-facing contracts; it is not identical to a tool-resource interface.

### Question 85 — B

Answer: Combine lexical and vector retrieval. Exact identifiers benefit from lexical matching, while paraphrases benefit from semantic matching. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-agent-memory-context-management-and-knowledge-integration Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **B:** Correct. Can match both exact identifiers and semantic paraphrases; it still needs relevance evaluation and permissions.
- **C:** Incorrect for this requirement. Reduces active context size but can omit details; important facts need preservation and verification.
- **D:** Incorrect for this requirement. Supports semantic lookup but is not automatically an authoritative transactional store for every workflow state.

### Question 86 — B

Answer: Use Azure Logic Apps for suitable connector-based workflows. A supported connector-based integration workflow suits Logic Apps when its triggers, actions, and operational limits fit. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#build-and-integrate-tool-ecosystems Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Improves environment reproducibility; it does not by itself determine production architecture or access policies.
- **B:** Correct. Coordinates supported connectors and integration steps, including approval patterns where configured; it is not a model-training library.
- **C:** Incorrect for this requirement. Provides model and pipeline tooling for supported architectures; it is not a replacement for agent authorization or orchestration design.
- **D:** Incorrect for this requirement. Keeps query and document representations in the same semantic space; mixing incompatible model versions can break relevance.

### Question 87 — D

Answer: Evaluate recovery, safe failure, and task completion under faults. A production evaluation must test recovery and partial failure, not just correct answers when every dependency succeeds. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-evaluation-and-validation-strategies-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Incorrect for this requirement. Demonstrates desired behavior in context without modifying learned model weights.
- **B:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.
- **C:** Incorrect for this requirement. Checks faithfulness to available context, not merely fluent language or relevant retrieved documents.
- **D:** Correct. Tests behavior under unavailable tools and partial failures, not just successful-path answers.

### Question 88 — B, E

Answer: Grant only required secret access to each workload; Rotate secrets and update dependent applications safely. Secret access must be scoped and credentials managed through a tested replacement lifecycle. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-security-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Incorrect for this requirement. Exposes a powerful secret across model interactions and removes per-workload access separation.
- **B:** Correct. Limits the scope of credential retrieval rather than allowing every agent to read all stored secrets.
- **C:** Incorrect for this requirement. Creates avoidable sensitive-data exposure and violates data-minimization and secret-handling requirements.
- **D:** Incorrect for this requirement. Simplifies credential sharing but removes per-agent isolation and increases the impact of compromise.
- **E:** Correct. Changes credentials through a tested lifecycle with controlled overlap or rollout where supported, rather than retaining a leaked value.

### Question 89 — A

Answer: Derive the allowed tenant scope from trusted identity and enforce it in the server-side query. Trusted authorization must constrain retrieval before restricted evidence enters model context. A user-supplied tenant parameter is not proof of permission. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-agent-memory-context-management-and-knowledge-integration Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Correct. The security boundary must use an authenticated authorization context rather than caller-controlled ownership claims.
- **B:** Incorrect for this requirement. Embedding quality does not establish tenant authorization.
- **C:** Incorrect for this requirement. Unauthorized content would already have reached the model and the instruction is not an access control.
- **D:** Incorrect for this requirement. Removing names cannot reliably remove restricted facts or prevent retrieval exposure.

### Question 90 — C

Answer: Insert a human approval gate before the consequential action. A pre-action approval gate controls consequential autonomy; recording the action afterward is insufficient. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-logical-architecture-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/

- **A:** Incorrect for this requirement. Can reduce supported harmful content but does not replace consent, permissions, human review, or all domain-specific policies.
- **B:** Incorrect for this requirement. Reduces active context size but can omit details; important facts need preservation and verification.
- **C:** Correct. Allows a qualified person to approve, reject, or amend a proposed action before it causes an external effect.
- **D:** Incorrect for this requirement. Supports accountability after and during execution but does not by itself stop an unapproved action.

### Question 91 — C

Answer: Rerank retrieved candidates before context selection. A relevance rescoring stage can reorder candidates that were already retrieved. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-agent-memory-context-management-and-knowledge-integration Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **B:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **C:** Correct. Improves ordering within a candidate set; it cannot recover a document never retrieved.
- **D:** Incorrect for this requirement. Controls retrieval granularity; excessive size wastes context, while tiny isolated chunks can lose meaning.

### Question 92 — D

Answer: Use explicit state transitions and checkpoints in a graph workflow. Explicit graph state and checkpoints support controlled continuation, while side effects and access still require separate safeguards. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#implement-multi-agent-orchestration Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Keeps query and document representations in the same semantic space; mixing incompatible model versions can break relevance.
- **B:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **C:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **D:** Correct. Supports stateful orchestration and controlled resumption; checkpointed state must still be secured and external side effects made safe.

### Question 93 — A

Answer: Use hub-and-spoke coordination. A single coordinator responsible for dispatch and aggregation is characteristic of hub-and-spoke. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-logical-architecture-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/

- **A:** Correct. Centralizes dispatch and aggregation through a coordinator while specialists handle bounded work.
- **B:** Incorrect for this requirement. Transfers task responsibility to the appropriate specialist with explicit context and termination rules.
- **C:** Incorrect for this requirement. Allows agents to communicate directly, but requires explicit ownership, convergence, and safety controls.
- **D:** Incorrect for this requirement. Passes work through dependent stages where later tasks require earlier outputs.

### Question 94 — A

Answer: Inject relevant authorized context at request time. Task-specific current information should be injected at inference after authorization, not assumed to exist in model weights. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-advanced-prompt-engineering-strategies-in-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Correct. Supplies current task information during inference without treating it as permanently learned knowledge.
- **B:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **C:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **D:** Incorrect for this requirement. Reduces active context size but can omit details; important facts need preservation and verification.

### Question 95 — B

Answer: Select compute using workload, scaling, network, and reliability requirements. Compute selection must follow execution and operational constraints; naming one service without those requirements is insufficient. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#specify-technology-components-to-include-in-a-multi-agent-solution Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/

- **A:** Incorrect for this requirement. Provides managed container hosting and supported scaling features, subject to runtime and connectivity requirements.
- **B:** Correct. Evaluates hosting constraints and operational needs rather than assuming a single compute type fits every agent.
- **C:** Incorrect for this requirement. Fits bounded event-driven operations when execution, hosting, networking, and scaling limits meet the workload.
- **D:** Incorrect for this requirement. Provides Kubernetes control and ecosystem flexibility with additional operational responsibility.

### Question 96 — C

Answer: Bound concurrent agent and tool execution. A semaphore or worker limit should constrain simultaneous work to available capacity and downstream quotas. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#implement-multi-agent-orchestration Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **B:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.
- **C:** Correct. Limits simultaneous work according to capacity and downstream quotas instead of spawning unbounded tasks.
- **D:** Incorrect for this requirement. Can cause runaway cost, load, and repeated side effects rather than providing reliable convergence.

### Question 97 — D

Answer: Release to a limited traffic cohort with health and quality gates. A limited initial traffic cohort reduces exposure and allows measured expansion based on defined outcomes. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#deploy-multi-agent-solutions-to-azure Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Incorrect for this requirement. Supports promotion and rollback by moving traffic between prepared environments, subject to state and compatibility planning.
- **B:** Incorrect for this requirement. Separates lifecycle stages with explicit validation and approval gates rather than treating a development success as production acceptance.
- **C:** Incorrect for this requirement. Removes staged evidence and increases exposure to unreviewed errors.
- **D:** Correct. Limits initial exposure and expands only after measured outcomes meet criteria.

### Question 98 — A, D

Answer: Capture versioned replay inputs and sanitized execution events; Define typed inputs, outputs, and responsibility ownership. Versioned sanitized evidence supports replay, and typed contracts make boundary behavior explicit and testable. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#specify-technology-components-to-include-in-a-multi-agent-solution Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/

- **A:** Correct. Supports reproducible investigation by recording necessary inputs, versions, and tool outcomes without exposing prohibited data.
- **B:** Incorrect for this requirement. Adds coordination work without resolving unclear ownership, contracts, or workflow design.
- **C:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.
- **D:** Correct. Makes exchanges testable and reduces ambiguity at agent boundaries; runtime validation remains necessary.
- **E:** Incorrect for this requirement. Shows rates, latency, and resource trends but does not alone reconstruct a particular cross-service execution.

### Question 99 — B

Answer: Apply deadlines, cancellation, and a safe fallback. A deadline and safe failure path bound work that cannot complete in time. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#build-and-integrate-tool-ecosystems Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **B:** Correct. Bounds stalled work and defines a failure path instead of allowing dependent steps to wait indefinitely.
- **C:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.
- **D:** Incorrect for this requirement. Can cause runaway cost, load, and repeated side effects rather than providing reliable convergence.

### Question 100 — A

Answer: Measure relevance of retrieved evidence against labeled queries. Search relevance is evaluated independently of whether a generator faithfully uses the retrieved evidence. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-evaluation-and-validation-strategies-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Correct. Evaluates whether search returns useful source material separately from whether generation uses it correctly.
- **B:** Incorrect for this requirement. Evaluates nuanced correctness, usefulness, and safety while documenting reviewer disagreement and escalation.
- **C:** Incorrect for this requirement. Checks faithfulness to available context, not merely fluent language or relevant retrieved documents.
- **D:** Incorrect for this requirement. Shows rates, latency, and resource trends but does not alone reconstruct a particular cross-service execution.
