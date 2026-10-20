# AI-500 — Practice Set 3

100 questions · Suggested practice duration: 180 minutes · Practice target: 80%

Select one answer unless the question says Select TWO. Answer key follows all questions.

Original educational content, not actual or recalled Microsoft exam items.

## Questions

### 1. A team wants to show the desired answer style inside each request rather than retrain. Which approach fits?

Domain: Develop multi-agent solutions in Azure

- A. Add curated input-output examples to the prompt
- B. Use supported prompt-prefix caching
- C. Use a supported fine-tuning strategy with curated data and held-out evaluation
- D. Select the largest available model for every task

### 2. A team wants to know whether the search stage returns useful evidence for labeled questions. Which evaluation fits?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Evaluate whether generated claims are supported by supplied evidence
- B. Use qualified human reviewers with a shared rubric
- C. Collect aggregate operational metrics
- D. Measure relevance of retrieved evidence against labeled queries

### 3. A team wants to speed execution without violating ordering requirements. Which optimization strategy fits?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Optimize the dependent critical path and parallelize independent work
- B. Allow unlimited autonomous retries and spawning
- C. Increase the number of agents without changing responsibilities
- D. Select the largest available model for every task

### 4. A team needs reproducible tests and rollback for agent instructions. Which prompt-management practice fits?

Domain: Develop multi-agent solutions in Azure

- A. Collect aggregate operational metrics
- B. Fine-tune the underlying model
- C. Version prompts and evaluate changes before promotion
- D. Increase the number of agents without changing responsibilities

### 5. An end-to-end completion objective is 99% over 10,000 eligible runs. Under a simple count-based definition, how many unsuccessful runs can occur while meeting the objective exactly?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Zero unsuccessful runs
- B. 1,000 unsuccessful runs
- C. 100 unsuccessful runs
- D. 10 unsuccessful runs

### 6. Two judge models disagree sharply with expert ratings. Which improvement process fits?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Collect aggregate operational metrics
- B. Use supported prompt-prefix caching
- C. Calibrate LLM-as-a-judge against expert-labeled cases
- D. Select the largest available model for every task

### 7. An agent receives weakly ordered search results although the right document is present. Which enhancement fits?

Domain: Develop multi-agent solutions in Azure

- A. Chunk documents into coherent retrievable passages
- B. Use supported prompt-prefix caching
- C. Rerank retrieved candidates before context selection
- D. Fine-tune the underlying model

### 8. A finance assistant needs deterministic validation of allowed transaction limits. Which guardrail fits?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Fine-tune the underlying model
- B. Implement deterministic domain-specific policy checks
- C. Add curated input-output examples to the prompt
- D. Apply content safety filters

### 9. An application repeatedly sends eligible identical reference instructions before varying requests. Which caching approach should be evaluated?

Domain: Develop multi-agent solutions in Azure

- A. Use an exact-input response cache
- B. Use a governed semantic response cache
- C. Fine-tune the underlying model
- D. Use supported prompt-prefix caching

### 10. A long-running assistant loses the link between project IDs and approved decisions. Which correction fits?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Fine-tune the underlying model
- B. Maintain stable entity IDs and validated factual state
- C. Diagnose summary drift
- D. Use supported prompt-prefix caching

### 11. An agent reaches its request-size limit but needs a concise representation of prior progress. Which context operation fits?

Domain: Develop multi-agent solutions in Azure

- A. Use governed long-term memory
- B. Increase the number of agents without changing responsibilities
- C. Fine-tune the underlying model
- D. Compact context into a validated summary

### 12. An enterprise wants centralized routing instead of unrestricted specialist-to-specialist conversations. Which topology fits?

Domain: Architect multi-agent solutions

- A. Use peer-to-peer coordination with bounded protocols
- B. Use a controlled handoff between specialist agents
- C. Use sequential orchestration
- D. Use hub-and-spoke coordination

### 13. A long conversation loses facts exactly when old turns are removed from the prompt. Which context issue fits?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Fine-tune the underlying model
- B. Diagnose sliding-window amnesia
- C. Diagnose summary drift
- D. Monitor changes in task inputs and agent behavior over time

### 14. An enterprise assistant receives a user token and needs a suitable downstream token in that user's context. Which flow fits?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Use one highly privileged identity for all agents
- B. Use an on-behalf-of flow for delegated downstream access
- C. Use an API key with secure storage and rotation
- D. Use an Azure managed identity where supported

### 15. A team deploys a full replacement environment before moving users from the old environment. Which strategy fits?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Maintain separate blue and green environments and switch traffic
- B. Promote through development, test, acceptance, and production
- C. Deploy changes directly to all production users without gates
- D. Release to a limited traffic cohort with health and quality gates

### 16. A company proposes telling the model to ignore unauthorized documents after retrieval. Which stronger retrieval control fits?

Domain: Develop multi-agent solutions in Azure

- A. Apply content safety filters
- B. Compact context into a validated summary
- C. Fine-tune the underlying model
- D. Apply server-side tenant and permission filters to retrieval

### 17. A production agent may recommend account deletion but must not execute it alone. Which design control fits?

Domain: Architect multi-agent solutions

- A. Apply content safety filters
- B. Record structured audit events
- C. Insert a human approval gate before the consequential action
- D. Compact context into a validated summary

### 18. A platform needs a tested way to return to an earlier compatible agent deployment. Which release capability fits?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Record structured audit events
- B. Restore a known-good compatible release and verify recovery
- C. Use supported prompt-prefix caching
- D. Version prompts and evaluate changes before promotion

### 19. Logs exist in every component but cannot be joined by execution. Which tracing decision addresses this?

Domain: Architect multi-agent solutions

- A. Propagate trace context across agents and tools
- B. Use an embedding-based retrieval index
- C. Configure actionable health and quality alerts
- D. Collect aggregate operational metrics

### 20. An assistant needs authoritative account balances, but vector similarity returns approximate past descriptions. Which correction fits?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Supplement vector recall with authoritative structured lookup
- B. Rerank retrieved candidates before context selection
- C. Use supported prompt-prefix caching
- D. Select the largest available model for every task

### 21. A queue delivers the same purchase message twice. Which pseudocode design best prevents duplicate purchases while allowing recovery after a worker restart?

Domain: Develop multi-agent solutions in Azure

- A. Use the message logical-action ID as a provider idempotency key and persist the result
- B. Track completed IDs only in a local Python set
- C. Generate a new random idempotency key on every retry
- D. Log the purchase after sending it and ignore duplicates

### 22. A specialist implementation requires compatible tokenizer and model classes from the Hugging Face ecosystem. Which library fits?

Domain: Develop multi-agent solutions in Azure

- A. Use Azure Logic Apps for suitable connector-based workflows
- B. Use Hugging Face Transformers for compatible model capabilities
- C. Use Model Context Protocol (MCP)
- D. Place appropriate policies at Azure API Management

### 23. A regulated platform requires explicit validation in separate lifecycle environments before release. Which methodology fits?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Maintain separate blue and green environments and switch traffic
- B. Use supported prompt-prefix caching
- C. Deploy changes directly to all production users without gates
- D. Promote through development, test, acceptance, and production

### 24. An agent recalls stale information after deletion requests. Which evaluation area should be targeted?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Evaluate tool choice, arguments, outcomes, and side effects
- B. Measure relevance of retrieved evidence against labeled queries
- C. Evaluate whether generated claims are supported by supplied evidence
- D. Evaluate memory retention, retrieval, isolation, and forgetting

### 25. A release strategy must preserve artifact identity while isolating environment permissions. Which TWO practices fit? (Select TWO.)

Domain: Secure, govern, and deploy multi-agent solutions

- A. Promote the same immutable versioned artifacts across environments
- B. Deploy changes directly to all production users without gates
- C. Use one highly privileged identity for all agents
- D. Allow unlimited autonomous retries and spawning
- E. Use separate environment identities and configuration

### 26. An enterprise needs separate agent authority and tenant-isolated retained knowledge. Which TWO foundations fit? (Select TWO.)

Domain: Architect multi-agent solutions

- A. Allow unlimited autonomous retries and spawning
- B. Use distinct scoped identities and verify every boundary
- C. Log every raw prompt and credential without filtering
- D. Define retention, deletion, and tenant-isolation rules for state
- E. Use one highly privileged identity for all agents

### 27. A coordinator consumes tools and agents from external providers. Which TWO controls should surround interoperability? (Select TWO.)

Domain: Develop multi-agent solutions in Azure

- A. Validate and treat remote results as untrusted input
- B. Use one highly privileged identity for all agents
- C. Authenticate remote endpoints and authorize delegated operations
- D. Log every raw prompt and credential without filtering
- E. Fine-tune the underlying model

### 28. A developer tests only the example that motivated an instruction edit. Which broader practice should be added?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Add curated input-output examples to the prompt
- B. Select the largest available model for every task
- C. Run a representative held-out prompt regression suite
- D. Fine-tune the underlying model

### 29. Two specialists disagree about which one may issue recommendations. Which specification should clarify their authority?

Domain: Architect multi-agent solutions

- A. Apply narrowly scoped Azure RBAC assignments
- B. Collect aggregate operational metrics
- C. Specify each agent persona, scope, and escalation rules
- D. Fine-tune the underlying model

### 30. An assistant must retrieve approved prior project decisions after its original session expires. Which memory class fits?

Domain: Architect multi-agent solutions

- A. Compact context into a validated summary
- B. Use session-scoped short-term state
- C. Use governed long-term memory
- D. Fine-tune the underlying model

### 31. An agent run has a long unexplained delay between two services. Which telemetry supports investigation?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Collect aggregate operational metrics
- B. Select the largest available model for every task
- C. Inspect correlated spans with version and token metadata
- D. Add curated input-output examples to the prompt

### 32. A supported model needs learned domain output conventions rather than daily factual updates. Which approach fits?

Domain: Develop multi-agent solutions in Azure

- A. Use a supported fine-tuning strategy with curated data and held-out evaluation
- B. Refresh the knowledge source and retrieval index
- C. Use supported prompt-prefix caching
- D. Increase the number of agents without changing responsibilities

### 33. A team owns the provider that serves tools and resources through MCP. Which side of the integration is this?

Domain: Develop multi-agent solutions in Azure

- A. Implement an MCP client that discovers and invokes permitted tools
- B. Implement an MCP server with explicit tool schemas and authorization
- C. Use supported prompt-prefix caching
- D. Use Agent2Agent (A2A) interoperability

### 34. A team needs consistent local tooling across developer machines and CI. Which environment practice fits?

Domain: Architect multi-agent solutions

- A. Fine-tune the underlying model
- B. Use a versioned development container and dependency lock
- C. Use Azure Container Apps for suitable containerized services
- D. Maintain reviewed repository AI instructions

### 35. An assistant receives positive ratings for confident but incorrect answers. Which feedback process is more reliable?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Use supported prompt-prefix caching
- B. Collect aggregate operational metrics
- C. Analyze user feedback with verified task outcomes
- D. Select the largest available model for every task

### 36. A project uses generated test scenarios but must screen unrealistic and duplicate items. Which data strategy fits?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Use supported prompt-prefix caching
- B. Generate and validate diverse synthetic evaluation cases
- C. Select the largest available model for every task
- D. Allow unlimited autonomous retries and spawning

### 37. An agent platform needs bounded total work and prompt shutdown of dependent tasks. Which TWO mechanisms fit? (Select TWO.)

Domain: Develop multi-agent solutions in Azure

- A. Use supported prompt-prefix caching
- B. Select the largest available model for every task
- C. Enforce per-run token, tool-call, and spawn budgets
- D. Increase the number of agents without changing responsibilities
- E. Propagate cancellation through dependent branches

### 38. An enterprise wants privacy-aware traces and a bounded response to recurring failures. Which TWO practices fit? (Select TWO.)

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Allow unlimited autonomous retries and spawning
- B. Select the largest available model for every task
- C. Define alerts with bounded remediation and escalation
- D. Log every raw prompt and credential without filtering
- E. Redact and access-control sensitive telemetry

### 39. A cost spike is caused by repeated delegation rather than a model price change. Which control fits?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Inspect token use and enforce loop and tool-call termination
- B. Increase the number of agents without changing responsibilities
- C. Select the largest available model for every task
- D. Select only by lowest token price

### 40. An interactive assistant must stop a stalled dependency within its time budget. Which design fits?

Domain: Develop multi-agent solutions in Azure

- A. Apply deadlines, cancellation, and a safe fallback
- B. Allow unlimited autonomous retries and spawning
- C. Select the largest available model for every task
- D. Use supported prompt-prefix caching

### 41. A system claims success even though the external action failed. Which evaluation should check this?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Measure relevance of retrieved evidence against labeled queries
- B. Evaluate tool choice, arguments, outcomes, and side effects
- C. Use qualified human reviewers with a shared rubric
- D. Evaluate whether generated claims are supported by supplied evidence

### 42. An assistant makes decisions without explaining limits or giving users a recovery path. Which design choice fits?

Domain: Architect multi-agent solutions

- A. Apply content safety filters
- B. Fine-tune the underlying model
- C. Record structured audit events
- D. Design clear AI disclosure, user control, and recovery paths

### 43. A report workflow requires extraction, then reconciliation, then narrative generation. Which pattern fits?

Domain: Architect multi-agent solutions

- A. Use parallel orchestration with a controlled join
- B. Use hub-and-spoke coordination
- C. Use sequential orchestration
- D. Use peer-to-peer coordination with bounded protocols

### 44. A platform needs to replace a service password and update authorized consumers. Which operation fits?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Record structured audit events
- B. Fine-tune the underlying model
- C. Rotate secrets and update dependent applications safely
- D. Use supported prompt-prefix caching

### 45. A network glitch causes a safe read operation to fail briefly. Which handling approach should be evaluated?

Domain: Develop multi-agent solutions in Azure

- A. Fine-tune the underlying model
- B. Increase the number of agents without changing responsibilities
- C. Allow unlimited autonomous retries and spawning
- D. Use bounded retries with backoff and jitter for transient failures

### 46. An audit requires traceable execution evidence and clearly defined inter-agent data contracts. Which TWO controls fit? (Select TWO.)

Domain: Architect multi-agent solutions

- A. Define typed inputs, outputs, and responsibility ownership
- B. Collect aggregate operational metrics
- C. Increase the number of agents without changing responsibilities
- D. Capture versioned replay inputs and sanitized execution events
- E. Select the largest available model for every task

### 47. A remote result includes malformed fields and hostile instructions. Which boundary should validate it?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Validate and screen tool responses before reuse
- B. Record structured audit events
- C. Inspect and constrain user input before agent processing
- D. Use supported prompt-prefix caching

### 48. The source context is accurate, but the summary adds unsupported facts. Which evaluation fits?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Collect aggregate operational metrics
- B. Select only by lowest token price
- C. Measure relevance of retrieved evidence against labeled queries
- D. Evaluate whether generated claims are supported by supplied evidence

### 49. A tool service needs only specific supported data operations at a limited resource scope. Which access control fits?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Apply narrowly scoped Azure RBAC assignments
- B. Apply content safety filters
- C. Specify each agent persona, scope, and escalation rules
- D. Record structured audit events

### 50. An agent action should trigger a configured connector-based approval process. Which Azure service fits?

Domain: Develop multi-agent solutions in Azure

- A. Use Azure Logic Apps for suitable connector-based workflows
- B. Use a versioned development container and dependency lock
- C. Re-embed content with a consistent compatible embedding configuration
- D. Use Hugging Face Transformers for compatible model capabilities

### 51. A stateful graph orchestration must support a durable investigation of where a run paused. Which implementation fits?

Domain: Develop multi-agent solutions in Azure

- A. Fine-tune the underlying model
- B. Use explicit state transitions and checkpoints in a graph workflow
- C. Use supported prompt-prefix caching
- D. Re-embed content with a consistent compatible embedding configuration

### 52. A release changes model behavior and worsens outcomes on stable reference tasks. Which detection approach fits?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Collect aggregate operational metrics
- B. Monitor agent health and workflow failure patterns
- C. Use supported prompt-prefix caching
- D. Compare quality against a stable versioned baseline

### 53. A platform must screen the completed user-facing answer before release. Which intervention fits?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Use supported prompt-prefix caching
- B. Record structured audit events
- C. Validate and screen the final response before delivery
- D. Inspect and constrain user input before agent processing

### 54. A form-filling agent needs temporary answers while one application is completed. Which memory design fits?

Domain: Architect multi-agent solutions

- A. Fine-tune the underlying model
- B. Use an embedding-based retrieval index
- C. Use governed long-term memory
- D. Use session-scoped short-term state

### 55. Automated overlap metrics miss serious context-dependent errors. Which evaluation method should complement them?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Use qualified human reviewers with a shared rubric
- B. Select only by lowest token price
- C. Use supported prompt-prefix caching
- D. Collect aggregate operational metrics

### 56. An assistant should connect to a remote MCP provider and process returned tool results. Which component fits?

Domain: Develop multi-agent solutions in Azure

- A. Implement an MCP server with explicit tool schemas and authorization
- B. Fine-tune the underlying model
- C. Implement an MCP client that discovers and invokes permitted tools
- D. Use Agent2Agent (A2A) interoperability

### 57. A regulated workflow needs acceptable quality, processing location, and latency. Which model-selection approach fits?

Domain: Architect multi-agent solutions

- A. Select only by lowest token price
- B. Fine-tune the underlying model
- C. Select the largest available model for every task
- D. Benchmark models against task capability and operational constraints

### 58. A tool service should authenticate to supported Azure resources without shipping a client secret. Which approach fits?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Use an API key with secure storage and rotation
- B. Use one highly privileged identity for all agents
- C. Compact context into a validated summary
- D. Use an Azure managed identity where supported

### 59. A document asks a model to reveal credentials while the model is only supposed to extract facts. Which defense fits?

Domain: Develop multi-agent solutions in Azure

- A. Use supported prompt-prefix caching
- B. Record structured audit events
- C. Fine-tune the underlying model
- D. Separate trusted instructions from untrusted content

### 60. A canary passes HTTP health checks but its evaluated task-success rate drops below the release gate. What should the rollout controller do?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Stop expansion and apply the defined rollback or investigation policy
- B. Disable the quality gate until the rollout finishes
- C. Expand because successful HTTP responses prove acceptable quality
- D. Route every user to the canary to obtain more data immediately

### 61. A user submits content that violates the application's intake policy. Which intervention stage is directly relevant?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Use supported prompt-prefix caching
- B. Validate and screen the final response before delivery
- C. Record structured audit events
- D. Inspect and constrain user input before agent processing

### 62. A team needs to ensure prompt edits preserve previously validated task outcomes. Which testing practice fits?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Increase the number of agents without changing responsibilities
- B. Run regression tests and automated agent evaluations
- C. Use supported prompt-prefix caching
- D. Use isolated unit tests for deterministic components

### 63. An agent release reaches users even when integration checks fail. Which process correction fits?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Deploy changes directly to all production users without gates
- B. Add curated input-output examples to the prompt
- C. Gate CI/CD on reviewed artifacts, security checks, and evaluations
- D. Record structured audit events

### 64. Authorization checks must run consistently around tool execution rather than depend on each prompt. Which implementation pattern fits?

Domain: Develop multi-agent solutions in Azure

- A. Add curated input-output examples to the prompt
- B. Use reusable middleware for cross-cutting controls
- C. Use an embedding-based retrieval index
- D. Fine-tune the underlying model

### 65. An assistant uses its largest model for simple tasks and forwards unnecessary history. Which TWO improvements should be tested? (Select TWO.)

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Increase the number of agents without changing responsibilities
- B. Remove irrelevant context while preserving necessary evidence
- C. Select the largest available model for every task
- D. Benchmark a smaller adequate model for selected tasks
- E. Allow unlimited autonomous retries and spawning

### 66. An ingestion pipeline must choose useful passage boundaries before embedding. Which operation is this?

Domain: Develop multi-agent solutions in Azure

- A. Use supported prompt-prefix caching
- B. Chunk documents into coherent retrievable passages
- C. Apply narrowly scoped Azure RBAC assignments
- D. Fine-tune the underlying model

### 67. A coordinator should prepare a bounded context packet for each subagent. Which implementation practice fits?

Domain: Develop multi-agent solutions in Azure

- A. Allow unlimited autonomous retries and spawning
- B. Use governed long-term memory
- C. Assemble only relevant state, evidence, and tool results
- D. Select the largest available model for every task

### 68. An enterprise needs different retention rules for sessions and long-lived knowledge. Which architecture fits?

Domain: Architect multi-agent solutions

- A. Use one broadly autonomous agent for the entire workflow
- B. Use an embedding-based retrieval index
- C. Use session-scoped short-term state
- D. Separate session state, shared team state, and long-term memory

### 69. An architect needs a compatible agent-to-agent collaboration interface across hosting boundaries. Which protocol fits?

Domain: Architect multi-agent solutions

- A. Use Model Context Protocol (MCP)
- B. Use Agent2Agent (A2A) interoperability
- C. Use an embedding-based retrieval index
- D. Use a versioned development container and dependency lock

### 70. A new embedding configuration changes dimensions and semantic space. What should happen to indexed content used with it?

Domain: Develop multi-agent solutions in Azure

- A. Rerank retrieved candidates before context selection
- B. Compact context into a validated summary
- C. Re-embed content with a consistent compatible embedding configuration
- D. Use supported prompt-prefix caching

### 71. A remote API must distinguish a valid token from one authorized for a particular action. Which enforcement fits?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Validate OAuth access tokens and enforce audience and scopes
- B. Record structured audit events
- C. Use an API key with secure storage and rotation
- D. Version prompts and evaluate changes before promotion

### 72. A regulated deployment requires supported service traffic to stay on the approved private path. Which approach fits?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Use supported private endpoints and correct private DNS
- B. Fine-tune the underlying model
- C. Enable unrestricted public access to bypass private networking
- D. Apply content safety filters

### 73. A developer trains and tests on the same examples while editing unversioned prompts. Which TWO changes fit? (Select TWO.)

Domain: Develop multi-agent solutions in Azure

- A. Increase the number of agents without changing responsibilities
- B. Version prompts and evaluate changes before promotion
- C. Allow unlimited autonomous retries and spawning
- D. Select the largest available model for every task
- E. Keep independent evaluation data and gate model changes

### 74. A knowledge service should expose resources to compatible AI applications using a tool-oriented protocol. Which standard fits?

Domain: Architect multi-agent solutions

- A. Use Model Context Protocol (MCP)
- B. Expose a task-specific REST API
- C. Fine-tune the underlying model
- D. Use Agent2Agent (A2A) interoperability

### 75. A function-call response names a tool and arguments. Which trusted action should follow before treating the operation as complete?

Domain: Develop multi-agent solutions in Azure

- A. Execute a validated function call in application code
- B. Compact context into a validated summary
- C. Add curated input-output examples to the prompt
- D. Fine-tune the underlying model

### 76. A proposed hosting platform cannot meet an agent's runtime constraints. Which design approach should guide reconsideration?

Domain: Architect multi-agent solutions

- A. Use Azure Container Apps for suitable containerized services
- B. Select compute using workload, scaling, network, and reliability requirements
- C. Use Azure Kubernetes Service when cluster-level control is required
- D. Use Azure Functions for a suitable event-driven tool

### 77. A platform needs a governed API facade for external tool endpoints. Which Azure capability fits?

Domain: Develop multi-agent solutions in Azure

- A. Use Azure Functions for a suitable event-driven tool
- B. Place appropriate policies at Azure API Management
- C. Use Hugging Face Transformers for compatible model capabilities
- D. Use an embedding-based retrieval index

### 78. A company needs per-project quotas and internal chargeback for agent usage. Which design fits?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Collect aggregate operational metrics
- B. Select the largest available model for every task
- C. Use supported prompt-prefix caching
- D. Attribute usage to tenants, projects, and workflow runs

### 79. An enterprise must reduce secret exposure and manage credential lifetime. Which TWO controls fit? (Select TWO.)

Domain: Secure, govern, and deploy multi-agent solutions

- A. Use one highly privileged identity for all agents
- B. Embed one shared long-lived credential in every prompt
- C. Log every raw prompt and credential without filtering
- D. Grant only required secret access to each workload
- E. Rotate secrets and update dependent applications safely

### 80. A team needs to test the agent when a dependency times out or returns malformed data. Which evaluation strategy fits?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Select the largest available model for every task
- B. Add curated input-output examples to the prompt
- C. Evaluate whether generated claims are supported by supplied evidence
- D. Evaluate recovery, safe failure, and task completion under faults

### 81. A team currently stores API secrets in repository configuration. Which managed secret store fits?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Embed one shared long-lived credential in every prompt
- B. Use supported prompt-prefix caching
- C. Use an embedding-based retrieval index
- D. Store and retrieve secrets through Azure Key Vault

### 82. A workflow needs challenging tests of guardrail bypass attempts using supported Foundry capabilities. Which approach fits?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Select the largest available model for every task
- B. Use supported prompt-prefix caching
- C. Run adversarial testing early and throughout the lifecycle
- D. Deploy changes directly to all production users without gates

### 83. An assistant loses track of which invoice belongs to which supplier after handoff. Which practice fits?

Domain: Develop multi-agent solutions in Azure

- A. Maintain stable entity IDs and validated factual state
- B. Use an embedding-based retrieval index
- C. Compact context into a validated summary
- D. Select the largest available model for every task

### 84. A team stores every past conversation indefinitely despite purpose restrictions. Which lifecycle correction fits?

Domain: Develop multi-agent solutions in Azure

- A. Re-embed content with a consistent compatible embedding configuration
- B. Apply purpose-based memory retention and deletion
- C. Fine-tune the underlying model
- D. Use supported prompt-prefix caching

### 85. A tool returns a malformed date that a downstream agent would treat as valid. Which control is needed?

Domain: Develop multi-agent solutions in Azure

- A. Record structured audit events
- B. Use supported prompt-prefix caching
- C. Validate tool results against schema and domain constraints
- D. Select the largest available model for every task

### 86. A support system can reuse some validated answers for meaning-equivalent queries. Which cache should be evaluated with safeguards?

Domain: Develop multi-agent solutions in Azure

- A. Use supported prompt-prefix caching
- B. Fine-tune the underlying model
- C. Use an exact-input response cache
- D. Use a governed semantic response cache

### 87. A RAG pipeline misses literal clause IDs when using vectors alone. Which retrieval combination should be evaluated?

Domain: Develop multi-agent solutions in Azure

- A. Fine-tune the underlying model
- B. Use an embedding-based retrieval index
- C. Combine lexical and vector retrieval
- D. Compact context into a validated summary

### 88. Repeated summaries omit qualifications until a conditional statement becomes absolute. Which diagnosis fits?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Fine-tune the underlying model
- B. Diagnose summary drift
- C. Diagnose sliding-window amnesia
- D. Monitor changes in task inputs and agent behavior over time

### 89. An agent workflow cannot rely only on final answer screening for tool safety. Which TWO tool-boundary controls fit? (Select TWO.)

Domain: Secure, govern, and deploy multi-agent solutions

- A. Validate and screen the final response before delivery
- B. Use supported prompt-prefix caching
- C. Record structured audit events
- D. Validate and screen tool responses before reuse
- E. Authorize and validate the proposed tool action before execution

### 90. A coordinator needs a maximum number of simultaneous specialist calls. Which scaling mechanism fits?

Domain: Develop multi-agent solutions in Azure

- A. Fine-tune the underlying model
- B. Allow unlimited autonomous retries and spawning
- C. Bound concurrent agent and tool execution
- D. Select the largest available model for every task

### 91. A due-diligence workflow has several independent evidence checks followed by aggregation. Which orchestration fits?

Domain: Architect multi-agent solutions

- A. Use parallel orchestration with a controlled join
- B. Use a controlled handoff between specialist agents
- C. Use sequential orchestration
- D. Use one broadly autonomous agent for the entire workflow

### 92. A team needs durable human intervention in an agent orchestration, including rejection. Which design fits?

Domain: Develop multi-agent solutions in Azure

- A. Add curated input-output examples to the prompt
- B. Implement a controlled agent workflow with explicit review and resume
- C. Record structured audit events
- D. Use supported prompt-prefix caching

### 93. A team proposes adding agents before identifying the tasks each must own. What should the architect do first?

Domain: Architect multi-agent solutions

- A. Increase the number of agents without changing responsibilities
- B. Fine-tune the underlying model
- C. Decompose the goal into bounded agent responsibilities and tools
- D. Use one broadly autonomous agent for the entire workflow

### 94. An enterprise wants predictable environment provisioning with recorded configuration changes. Which approach fits?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Version prompts and evaluate changes before promotion
- B. Deploy versioned infrastructure as code through reviewed automation
- C. Deploy changes directly to all production users without gates
- D. Add curated input-output examples to the prompt

### 95. A policy assistant needs newly published approved terms during generation. Which strategy fits?

Domain: Develop multi-agent solutions in Azure

- A. Inject relevant authorized context at request time
- B. Fine-tune the underlying model
- C. Use supported prompt-prefix caching
- D. Compact context into a validated summary

### 96. A tool wrapper's input normalization needs direct verification of boundary values. Which test fits?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Run adversarial testing early and throughout the lifecycle
- B. Use isolated unit tests for deterministic components
- C. Test interactions with configured external dependencies
- D. Release to a limited traffic cohort with health and quality gates

### 97. A tool dependency has strict request limits shared across agents. Which scheduling approach fits?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Coordinate concurrency, rate budgets, and backoff
- B. Select the largest available model for every task
- C. Fine-tune the underlying model
- D. Allow unlimited autonomous retries and spawning

### 98. A model proposes an order amount above an enforceable business limit. Which intervention is needed?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Use supported prompt-prefix caching
- B. Record structured audit events
- C. Validate and screen the final response before delivery
- D. Authorize and validate the proposed tool action before execution

### 99. A workflow needs verification of live authentication and network connectivity to its dependencies. Which test fits?

Domain: Secure, govern, and deploy multi-agent solutions

- A. Test interactions with configured external dependencies
- B. Add curated input-output examples to the prompt
- C. Use supported prompt-prefix caching
- D. Use isolated unit tests for deterministic components

### 100. A platform needs to detect recurrent worker failures and failed orchestration steps. Which monitoring category fits?

Domain: Evaluate, optimize, and monitor multi-agent solutions

- A. Add curated input-output examples to the prompt
- B. Monitor agent health and workflow failure patterns
- C. Evaluate whether generated claims are supported by supplied evidence
- D. Select only by lowest token price

---

## Answer key and explanations

### Question 1 — A

Answer: Add curated input-output examples to the prompt. A few demonstrations in context can clarify expected behavior without a training job. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-advanced-prompt-engineering-strategies-in-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Correct. Demonstrates desired behavior in context without modifying learned model weights.
- **B:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **C:** Incorrect for this requirement. Adapts learned behavior when justified, with defined data quality, refresh triggers, and regression checks.
- **D:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.

### Question 2 — D

Answer: Measure relevance of retrieved evidence against labeled queries. Search relevance is evaluated independently of whether a generator faithfully uses the retrieved evidence. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-evaluation-and-validation-strategies-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Incorrect for this requirement. Checks faithfulness to available context, not merely fluent language or relevant retrieved documents.
- **B:** Incorrect for this requirement. Evaluates nuanced correctness, usefulness, and safety while documenting reviewer disagreement and escalation.
- **C:** Incorrect for this requirement. Shows rates, latency, and resource trends but does not alone reconstruct a particular cross-service execution.
- **D:** Correct. Evaluates whether search returns useful source material separately from whether generation uses it correctly.

### Question 3 — A

Answer: Optimize the dependent critical path and parallelize independent work. Only independent work can be safely overlapped; dependent stages still determine the critical path. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#optimize-prompt-and-model-performance-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Correct. Focuses on steps determining end-to-end duration while respecting task dependencies and resource constraints.
- **B:** Incorrect for this requirement. Can cause runaway cost, load, and repeated side effects rather than providing reliable convergence.
- **C:** Incorrect for this requirement. Adds coordination work without resolving unclear ownership, contracts, or workflow design.
- **D:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.

### Question 4 — C

Answer: Version prompts and evaluate changes before promotion. Prompt changes require identifiable versions and evaluation so regressions can be attributed and rolled back. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-advanced-prompt-engineering-strategies-in-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Shows rates, latency, and resource trends but does not alone reconstruct a particular cross-service execution.
- **B:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **C:** Correct. Makes instruction changes reproducible, comparable, and reversible.
- **D:** Incorrect for this requirement. Adds coordination work without resolving unclear ownership, contracts, or workflow design.

### Question 5 — C

Answer: 100 unsuccessful runs. The count-based error allowance is (1-0.99) times 10,000. Real SLO definitions must specify eligible events, windows, and exclusions. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-observability-and-monitoring-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Incorrect for this requirement. A 99% objective allows a limited unsuccessful fraction under this definition.
- **B:** Incorrect for this requirement. A thousand unsuccessful runs would leave only 90% successful completion.
- **C:** Correct. A 1% unsuccessful fraction of 10,000 is 100.
- **D:** Incorrect for this requirement. Ten failures would correspond to a 0.1% unsuccessful fraction, not the full 1% allowance.

### Question 6 — C

Answer: Calibrate LLM-as-a-judge against expert-labeled cases. Automated judges can be biased or wrong; calibration and ongoing audits are required. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#optimize-prompt-and-model-performance-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Incorrect for this requirement. Shows rates, latency, and resource trends but does not alone reconstruct a particular cross-service execution.
- **B:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **C:** Correct. Measures agreement, bias, and failure modes of automated judging rather than treating judge output as unquestionable truth.
- **D:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.

### Question 7 — C

Answer: Rerank retrieved candidates before context selection. A relevance rescoring stage can reorder candidates that were already retrieved. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-agent-memory-context-management-and-knowledge-integration Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Controls retrieval granularity; excessive size wastes context, while tiny isolated chunks can lose meaning.
- **B:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **C:** Correct. Improves ordering within a candidate set; it cannot recover a document never retrieved.
- **D:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.

### Question 8 — B

Answer: Implement deterministic domain-specific policy checks. Explicit business constraints require trusted domain checks; a generic content category filter does not enforce numeric or transactional policy. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-guardrails-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **B:** Correct. Enforces explicit business constraints such as allowed amounts or prohibited operations in trusted code rather than relying only on generic toxicity filters.
- **C:** Incorrect for this requirement. Demonstrates desired behavior in context without modifying learned model weights.
- **D:** Incorrect for this requirement. Can reduce supported harmful content but does not replace consent, permissions, human review, or all domain-specific policies.

### Question 9 — D

Answer: Use supported prompt-prefix caching. Repeated eligible prompt prefixes can benefit from provider-supported processing reuse; this does not imply final-answer reuse. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#implement-multi-agent-orchestration Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Reuses prior results for a matching cache key when authorization and freshness permit, rather than matching approximate meaning.
- **B:** Incorrect for this requirement. Can reuse meaning-equivalent responses only when permissions, tenant scope, freshness, and task semantics allow it.
- **C:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **D:** Correct. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.

### Question 10 — B

Answer: Maintain stable entity IDs and validated factual state. Entity continuity requires stable identity and factual state across transitions, not merely more similar text. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#optimize-prompt-and-model-performance-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **B:** Correct. Preserves identity and critical facts across summaries and agent transitions rather than relying on ambiguous names alone.
- **C:** Incorrect for this requirement. Identifies accumulated distortion when repeated summarization alters or omits important facts.
- **D:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.

### Question 11 — D

Answer: Compact context into a validated summary. Compaction reduces active context while requiring validation of important facts and links to authoritative state. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-agent-memory-context-management-and-knowledge-integration Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Persists approved information beyond a session with access, retention, deletion, and relevance controls.
- **B:** Incorrect for this requirement. Adds coordination work without resolving unclear ownership, contracts, or workflow design.
- **C:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **D:** Correct. Reduces active context size but can omit details; important facts need preservation and verification.

### Question 12 — D

Answer: Use hub-and-spoke coordination. A single coordinator responsible for dispatch and aggregation is characteristic of hub-and-spoke. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-logical-architecture-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/

- **A:** Incorrect for this requirement. Allows agents to communicate directly, but requires explicit ownership, convergence, and safety controls.
- **B:** Incorrect for this requirement. Transfers task responsibility to the appropriate specialist with explicit context and termination rules.
- **C:** Incorrect for this requirement. Passes work through dependent stages where later tasks require earlier outputs.
- **D:** Correct. Centralizes dispatch and aggregation through a coordinator while specialists handle bounded work.

### Question 13 — B

Answer: Diagnose sliding-window amnesia. Facts can disappear when older messages leave the active window even if no memory summary has changed. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#optimize-prompt-and-model-performance-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **B:** Correct. Identifies loss of earlier information as it drops out of active context; this is distinct from a model weight update.
- **C:** Incorrect for this requirement. Identifies accumulated distortion when repeated summarization alters or omits important facts.
- **D:** Incorrect for this requirement. Detects shifts in operating conditions or behavioral patterns that can require investigation and reassessment.

### Question 14 — B

Answer: Use an on-behalf-of flow for delegated downstream access. When downstream authorization must reflect the signed-in user, a supported delegated OBO flow differs from app-only identity. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-security-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Incorrect for this requirement. Simplifies credential sharing but removes per-agent isolation and increases the impact of compromise.
- **B:** Correct. Exchanges a user assertion through the middle tier for an appropriate downstream token, preserving delegated user context where supported.
- **C:** Incorrect for this requirement. Can authenticate supported service access but is a secret and generally does not carry a delegated user identity by itself.
- **D:** Incorrect for this requirement. Lets an Azure workload obtain identity-based access without embedding a long-lived application secret; resource authorization is still required.

### Question 15 — A

Answer: Maintain separate blue and green environments and switch traffic. Two prepared environments with traffic switching characterize blue/green; partial cohort exposure is a different strategy. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#deploy-multi-agent-solutions-to-azure Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Correct. Supports promotion and rollback by moving traffic between prepared environments, subject to state and compatibility planning.
- **B:** Incorrect for this requirement. Separates lifecycle stages with explicit validation and approval gates rather than treating a development success as production acceptance.
- **C:** Incorrect for this requirement. Removes staged evidence and increases exposure to unreviewed errors.
- **D:** Incorrect for this requirement. Limits initial exposure and expands only after measured outcomes meet criteria.

### Question 16 — D

Answer: Apply server-side tenant and permission filters to retrieval. Access constraints must be enforced by trusted retrieval controls before restricted content reaches a model. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-agent-memory-context-management-and-knowledge-integration Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Can reduce supported harmful content but does not replace consent, permissions, human review, or all domain-specific policies.
- **B:** Incorrect for this requirement. Reduces active context size but can omit details; important facts need preservation and verification.
- **C:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **D:** Correct. Constrains candidate documents using trusted identity and access metadata rather than allowing the model to decide access.

### Question 17 — C

Answer: Insert a human approval gate before the consequential action. A pre-action approval gate controls consequential autonomy; recording the action afterward is insufficient. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-logical-architecture-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/

- **A:** Incorrect for this requirement. Can reduce supported harmful content but does not replace consent, permissions, human review, or all domain-specific policies.
- **B:** Incorrect for this requirement. Supports accountability after and during execution but does not by itself stop an unapproved action.
- **C:** Correct. Allows a qualified person to approve, reject, or amend a proposed action before it causes an external effect.
- **D:** Incorrect for this requirement. Reduces active context size but can omit details; important facts need preservation and verification.

### Question 18 — B

Answer: Restore a known-good compatible release and verify recovery. Recovery must restore a compatible set of components and verify service behavior, not only change one instruction string. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#deploy-multi-agent-solutions-to-azure Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Incorrect for this requirement. Supports accountability after and during execution but does not by itself stop an unapproved action.
- **B:** Correct. Requires versioned artifacts and configuration, state compatibility, and operational checks; a prompt-only revert may be insufficient.
- **C:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **D:** Incorrect for this requirement. Makes instruction changes reproducible, comparable, and reversible.

### Question 19 — A

Answer: Propagate trace context across agents and tools. Cross-service trace context is needed to connect individual agent and tool operations into one execution. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#specify-technology-components-to-include-in-a-multi-agent-solution Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/

- **A:** Correct. Correlates spans across service boundaries to reconstruct an end-to-end execution path.
- **B:** Incorrect for this requirement. Supports semantic lookup but is not automatically an authoritative transactional store for every workflow state.
- **C:** Incorrect for this requirement. Detects defined conditions and triggers response but does not itself retain all evidence required for deterministic investigation.
- **D:** Incorrect for this requirement. Shows rates, latency, and resource trends but does not alone reconstruct a particular cross-service execution.

### Question 20 — A

Answer: Supplement vector recall with authoritative structured lookup. Exact relationships and authoritative facts may require structured lookup rather than nearest-neighbor similarity alone. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#optimize-prompt-and-model-performance-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Correct. Addresses exact facts, dates, counts, or entity relationships that semantic similarity alone may fail to recover reliably.
- **B:** Incorrect for this requirement. Improves ordering within a candidate set; it cannot recover a document never retrieved.
- **C:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **D:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.

### Question 21 — A

Answer: Use the message logical-action ID as a provider idempotency key and persist the result. Duplicate protection must survive retries and restarts and align with the external side-effect boundary. Do not assume at-least-once delivery means exactly-once execution. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#build-and-integrate-tool-ecosystems Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Correct. A stable ID and durable outcome allow repeated delivery to map to one logical operation, subject to provider guarantees.
- **B:** Incorrect for this requirement. Process-local state is lost on restart and is not a shared durable duplicate boundary.
- **C:** Incorrect for this requirement. Different keys make the provider treat retries as distinct operations.
- **D:** Incorrect for this requirement. Logging alone does not prevent repeated external effects or handle a crash between the effect and the log.

### Question 22 — B

Answer: Use Hugging Face Transformers for compatible model capabilities. The requested capability is compatible model and pipeline tooling, not API policy or integration-protocol hosting. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#implement-multi-agent-orchestration Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Coordinates supported connectors and integration steps, including approval patterns where configured; it is not a model-training library.
- **B:** Correct. Provides model and pipeline tooling for supported architectures; it is not a replacement for agent authorization or orchestration design.
- **C:** Incorrect for this requirement. Provides a standard interface for exposing tools, resources, and prompts to compatible clients; security remains a separate design duty.
- **D:** Incorrect for this requirement. Provides an API governance layer for authentication, traffic management, and policies; it does not by itself grant downstream data permissions.

### Question 23 — D

Answer: Promote through development, test, acceptance, and production. Environment stages separate development from progressively validated production promotion. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#deploy-multi-agent-solutions-to-azure Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Incorrect for this requirement. Supports promotion and rollback by moving traffic between prepared environments, subject to state and compatibility planning.
- **B:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **C:** Incorrect for this requirement. Removes staged evidence and increases exposure to unreviewed errors.
- **D:** Correct. Separates lifecycle stages with explicit validation and approval gates rather than treating a development success as production acceptance.

### Question 24 — D

Answer: Evaluate memory retention, retrieval, isolation, and forgetting. Memory needs tests for correct recall and prohibited reuse, not only tests of current document retrieval. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-evaluation-and-validation-strategies-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Incorrect for this requirement. Tests whether the right authorized operation was invoked correctly and produced the intended result.
- **B:** Incorrect for this requirement. Evaluates whether search returns useful source material separately from whether generation uses it correctly.
- **C:** Incorrect for this requirement. Checks faithfulness to available context, not merely fluent language or relevant retrieved documents.
- **D:** Correct. Tests whether relevant authorized facts are recalled and prohibited or expired information is not reused.

### Question 25 — A, E

Answer: Promote the same immutable versioned artifacts across environments; Use separate environment identities and configuration. Identifiable artifacts and separate environment authority reduce release drift and accidental production effects. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#deploy-multi-agent-solutions-to-azure Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Correct. Reduces unreviewed differences by tracking code, prompt, model, tool schema, and deployment configuration versions.
- **B:** Incorrect for this requirement. Removes staged evidence and increases exposure to unreviewed errors.
- **C:** Incorrect for this requirement. Simplifies credential sharing but removes per-agent isolation and increases the impact of compromise.
- **D:** Incorrect for this requirement. Can cause runaway cost, load, and repeated side effects rather than providing reliable convergence.
- **E:** Correct. Prevents development or test access from inheriting production authority and reduces accidental cross-environment effects.

### Question 26 — B, D

Answer: Use distinct scoped identities and verify every boundary; Define retention, deletion, and tenant-isolation rules for state. Scoped identities constrain access, while state lifecycle and isolation policies constrain persistent data use. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#specify-technology-components-to-include-in-a-multi-agent-solution Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/

- **A:** Incorrect for this requirement. Can cause runaway cost, load, and repeated side effects rather than providing reliable convergence.
- **B:** Correct. Reduces lateral movement by treating each agent and service interaction as an independently authorized access decision.
- **C:** Incorrect for this requirement. Creates avoidable sensitive-data exposure and violates data-minimization and secret-handling requirements.
- **D:** Correct. Establishes who may use stored information and for how long, instead of assuming persistence implies permission.
- **E:** Incorrect for this requirement. Simplifies credential sharing but removes per-agent isolation and increases the impact of compromise.

### Question 27 — A, C

Answer: Authenticate remote endpoints and authorize delegated operations; Validate and treat remote results as untrusted input. Protocol compatibility does not establish caller permission or make remote outputs trustworthy. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#implement-multi-agent-orchestration Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Correct. Checks returned structure and content and prevents remote output from overriding trusted instructions or permissions.
- **B:** Incorrect for this requirement. Simplifies credential sharing but removes per-agent isolation and increases the impact of compromise.
- **C:** Correct. Checks the identity, audience, and scope of agent or tool calls instead of trusting interoperability alone.
- **D:** Incorrect for this requirement. Creates avoidable sensitive-data exposure and violates data-minimization and secret-handling requirements.
- **E:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.

### Question 28 — C

Answer: Run a representative held-out prompt regression suite. A versioned independent test suite reveals regressions across representative cases rather than only author-selected examples. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-evaluation-and-validation-strategies-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Incorrect for this requirement. Demonstrates desired behavior in context without modifying learned model weights.
- **B:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.
- **C:** Correct. Compares instruction or model changes on independent realistic cases, including difficult and safety-relevant inputs.
- **D:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.

### Question 29 — C

Answer: Specify each agent persona, scope, and escalation rules. Behavioral scope and escalation must be specified for each role; resource permissions alone do not define its purpose. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-logical-architecture-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/

- **A:** Incorrect for this requirement. Authorizes supported Azure resource operations for principals at appropriate scopes; it does not describe the full behavioral role of an agent.
- **B:** Incorrect for this requirement. Shows rates, latency, and resource trends but does not alone reconstruct a particular cross-service execution.
- **C:** Correct. Defines role, allowable behavior, autonomy, and boundaries, while enforcement still requires application controls.
- **D:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.

### Question 30 — C

Answer: Use governed long-term memory. Approved persistent knowledge or preferences need governed long-term memory rather than reliance on an active context window. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-logical-architecture-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/

- **A:** Incorrect for this requirement. Reduces active context size but can omit details; important facts need preservation and verification.
- **B:** Incorrect for this requirement. Retains information for an active interaction or workflow rather than serving as unrestricted persistent cross-session memory.
- **C:** Correct. Persists approved information beyond a session with access, retention, deletion, and relevance controls.
- **D:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.

### Question 31 — C

Answer: Inspect correlated spans with version and token metadata. Correlated spans connect a particular run to its latency, version, tokens, and tool steps. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-observability-and-monitoring-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Incorrect for this requirement. Shows rates, latency, and resource trends but does not alone reconstruct a particular cross-service execution.
- **B:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.
- **C:** Correct. Connects latency, usage, prompts, and tool execution to a particular run, subject to privacy controls.
- **D:** Incorrect for this requirement. Demonstrates desired behavior in context without modifying learned model weights.

### Question 32 — A

Answer: Use a supported fine-tuning strategy with curated data and held-out evaluation. Persistent task behavior may justify supported fine-tuning; the decision needs curated examples, refresh triggers, and independent evaluation. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-advanced-prompt-engineering-strategies-in-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Correct. Adapts learned behavior when justified, with defined data quality, refresh triggers, and regression checks.
- **B:** Incorrect for this requirement. Addresses changing external facts without repeatedly training those facts into model weights.
- **C:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **D:** Incorrect for this requirement. Adds coordination work without resolving unclear ownership, contracts, or workflow design.

### Question 33 — B

Answer: Implement an MCP server with explicit tool schemas and authorization. The provider side exposes capabilities through MCP while enforcing contracts and access. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#build-and-integrate-tool-ecosystems Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Consumes the server interface and handles tool results under application policy; discovery is not permission to execute every tool.
- **B:** Correct. Exposes supported tools and resources through MCP while validating arguments and enforcing caller permissions.
- **C:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **D:** Incorrect for this requirement. Supports collaboration with compatible remote agents through defined agent-facing contracts; it is not identical to a tool-resource interface.

### Question 34 — B

Answer: Use a versioned development container and dependency lock. A reproducible development environment and dependency lock reduce local setup drift; production hosting solves a different problem. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#specify-technology-components-to-include-in-a-multi-agent-solution Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/

- **A:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **B:** Correct. Improves environment reproducibility; it does not by itself determine production architecture or access policies.
- **C:** Incorrect for this requirement. Provides managed container hosting and supported scaling features, subject to runtime and connectivity requirements.
- **D:** Incorrect for this requirement. Communicates coding conventions and boundaries to development assistants; it is not a runtime authorization system.

### Question 35 — C

Answer: Analyze user feedback with verified task outcomes. User signals should be connected to verified outcomes and reviewed before they drive changes. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#optimize-prompt-and-model-performance-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **B:** Incorrect for this requirement. Shows rates, latency, and resource trends but does not alone reconstruct a particular cross-service execution.
- **C:** Correct. Turns real-world signals into reviewed improvements instead of equating popularity or raw engagement with correctness.
- **D:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.

### Question 36 — B

Answer: Generate and validate diverse synthetic evaluation cases. Generated tests expand coverage only after validation; synthetic labels and examples can introduce new errors or blind spots. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#optimize-prompt-and-model-performance-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **B:** Correct. Expands test coverage while checking labels, realism, duplicates, and gaps; generated examples are not automatically valid.
- **C:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.
- **D:** Incorrect for this requirement. Can cause runaway cost, load, and repeated side effects rather than providing reliable convergence.

### Question 37 — C, E

Answer: Enforce per-run token, tool-call, and spawn budgets; Propagate cancellation through dependent branches. Global work budgets and cancellation propagation control runaway delegation across the whole run. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#implement-multi-agent-orchestration Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **B:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.
- **C:** Correct. Creates explicit termination and cost boundaries across the whole workflow, including delegated work.
- **D:** Incorrect for this requirement. Adds coordination work without resolving unclear ownership, contracts, or workflow design.
- **E:** Correct. Stops unnecessary downstream work after a user cancels, a deadline expires, or the workflow reaches a terminal condition.

### Question 38 — C, E

Answer: Redact and access-control sensitive telemetry; Define alerts with bounded remediation and escalation. Useful monitoring requires protected telemetry and controlled incident response rather than unrestricted logs or loops. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-observability-and-monitoring-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Incorrect for this requirement. Can cause runaway cost, load, and repeated side effects rather than providing reliable convergence.
- **B:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.
- **C:** Correct. Links detection to a controlled response with limits and human handoff rather than unchecked restart or retry loops.
- **D:** Incorrect for this requirement. Creates avoidable sensitive-data exposure and violates data-minimization and secret-handling requirements.
- **E:** Correct. Preserves useful investigation evidence while avoiding unnecessary exposure of prompts, personal information, and secrets.

### Question 39 — A

Answer: Inspect token use and enforce loop and tool-call termination. Repeated generation and tool loops can dominate cost even when unit token price is low. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-observability-and-monitoring-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Correct. Locates repeated generation or delegation and applies finite execution budgets rather than treating cost as only model price.
- **B:** Incorrect for this requirement. Adds coordination work without resolving unclear ownership, contracts, or workflow design.
- **C:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.
- **D:** Incorrect for this requirement. Ignores quality, retry cost, tool reliability, latency, and other business constraints.

### Question 40 — A

Answer: Apply deadlines, cancellation, and a safe fallback. A deadline and safe failure path bound work that cannot complete in time. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#build-and-integrate-tool-ecosystems Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Correct. Bounds stalled work and defines a failure path instead of allowing dependent steps to wait indefinitely.
- **B:** Incorrect for this requirement. Can cause runaway cost, load, and repeated side effects rather than providing reliable convergence.
- **C:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.
- **D:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.

### Question 41 — B

Answer: Evaluate tool choice, arguments, outcomes, and side effects. A tool workflow needs outcome and side-effect checks; a plausible final explanation can hide an incorrect operation. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-evaluation-and-validation-strategies-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Incorrect for this requirement. Evaluates whether search returns useful source material separately from whether generation uses it correctly.
- **B:** Correct. Tests whether the right authorized operation was invoked correctly and produced the intended result.
- **C:** Incorrect for this requirement. Evaluates nuanced correctness, usefulness, and safety while documenting reviewer disagreement and escalation.
- **D:** Incorrect for this requirement. Checks faithfulness to available context, not merely fluent language or relevant retrieved documents.

### Question 42 — D

Answer: Design clear AI disclosure, user control, and recovery paths. Human-AI experience includes understandable boundaries and user control, not only technical filtering. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-logical-architecture-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/

- **A:** Incorrect for this requirement. Can reduce supported harmful content but does not replace consent, permissions, human review, or all domain-specific policies.
- **B:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **C:** Incorrect for this requirement. Supports accountability after and during execution but does not by itself stop an unapproved action.
- **D:** Correct. Supports the human-AI experience by communicating limits and allowing correction, cancellation, and escalation.

### Question 43 — C

Answer: Use sequential orchestration. Later stages require validated outputs from earlier stages, making a dependency-ordered flow appropriate. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-logical-architecture-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/

- **A:** Incorrect for this requirement. Runs independent branches concurrently and combines their results after completion.
- **B:** Incorrect for this requirement. Centralizes dispatch and aggregation through a coordinator while specialists handle bounded work.
- **C:** Correct. Passes work through dependent stages where later tasks require earlier outputs.
- **D:** Incorrect for this requirement. Allows agents to communicate directly, but requires explicit ownership, convergence, and safety controls.

### Question 44 — C

Answer: Rotate secrets and update dependent applications safely. Credential lifecycle changes require coordinated application updates and revocation, not just a log entry or model change. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-security-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Incorrect for this requirement. Supports accountability after and during execution but does not by itself stop an unapproved action.
- **B:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **C:** Correct. Changes credentials through a tested lifecycle with controlled overlap or rollout where supported, rather than retaining a leaked value.
- **D:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.

### Question 45 — D

Answer: Use bounded retries with backoff and jitter for transient failures. Transient failures may justify limited retries with backoff, not unlimited repeats or changes to model weights. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#build-and-integrate-tool-ecosystems Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **B:** Incorrect for this requirement. Adds coordination work without resolving unclear ownership, contracts, or workflow design.
- **C:** Incorrect for this requirement. Can cause runaway cost, load, and repeated side effects rather than providing reliable convergence.
- **D:** Correct. Limits repeat attempts and avoids synchronized retry storms; non-idempotent operations require duplicate protection.

### Question 46 — A, D

Answer: Capture versioned replay inputs and sanitized execution events; Define typed inputs, outputs, and responsibility ownership. Versioned sanitized evidence supports replay, and typed contracts make boundary behavior explicit and testable. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#specify-technology-components-to-include-in-a-multi-agent-solution Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/

- **A:** Correct. Makes exchanges testable and reduces ambiguity at agent boundaries; runtime validation remains necessary.
- **B:** Incorrect for this requirement. Shows rates, latency, and resource trends but does not alone reconstruct a particular cross-service execution.
- **C:** Incorrect for this requirement. Adds coordination work without resolving unclear ownership, contracts, or workflow design.
- **D:** Correct. Supports reproducible investigation by recording necessary inputs, versions, and tool outcomes without exposing prohibited data.
- **E:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.

### Question 47 — A

Answer: Validate and screen tool responses before reuse. External tool responses form a separate trust boundary and need checks before they influence later decisions. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-guardrails-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Correct. Checks external output structure and policy and treats embedded instructions as untrusted before it reaches another agent.
- **B:** Incorrect for this requirement. Supports accountability after and during execution but does not by itself stop an unapproved action.
- **C:** Incorrect for this requirement. Applies configured input-side controls, while downstream boundaries and output checks still remain necessary.
- **D:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.

### Question 48 — D

Answer: Evaluate whether generated claims are supported by supplied evidence. Relevant retrieval does not guarantee the final answer is supported; generated claims need evidence checking. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-evaluation-and-validation-strategies-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Incorrect for this requirement. Shows rates, latency, and resource trends but does not alone reconstruct a particular cross-service execution.
- **B:** Incorrect for this requirement. Ignores quality, retry cost, tool reliability, latency, and other business constraints.
- **C:** Incorrect for this requirement. Evaluates whether search returns useful source material separately from whether generation uses it correctly.
- **D:** Correct. Checks faithfulness to available context, not merely fluent language or relevant retrieved documents.

### Question 49 — A

Answer: Apply narrowly scoped Azure RBAC assignments. Resource access must be granted at the necessary principal and scope; behavioral instructions do not enforce Azure permissions. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-security-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Correct. Authorizes supported Azure resource operations for principals at appropriate scopes; it does not describe the full behavioral role of an agent.
- **B:** Incorrect for this requirement. Can reduce supported harmful content but does not replace consent, permissions, human review, or all domain-specific policies.
- **C:** Incorrect for this requirement. Defines role, allowable behavior, autonomy, and boundaries, while enforcement still requires application controls.
- **D:** Incorrect for this requirement. Supports accountability after and during execution but does not by itself stop an unapproved action.

### Question 50 — A

Answer: Use Azure Logic Apps for suitable connector-based workflows. A supported connector-based integration workflow suits Logic Apps when its triggers, actions, and operational limits fit. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#build-and-integrate-tool-ecosystems Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Correct. Coordinates supported connectors and integration steps, including approval patterns where configured; it is not a model-training library.
- **B:** Incorrect for this requirement. Improves environment reproducibility; it does not by itself determine production architecture or access policies.
- **C:** Incorrect for this requirement. Keeps query and document representations in the same semantic space; mixing incompatible model versions can break relevance.
- **D:** Incorrect for this requirement. Provides model and pipeline tooling for supported architectures; it is not a replacement for agent authorization or orchestration design.

### Question 51 — B

Answer: Use explicit state transitions and checkpoints in a graph workflow. Explicit graph state and checkpoints support controlled continuation, while side effects and access still require separate safeguards. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#implement-multi-agent-orchestration Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **B:** Correct. Supports stateful orchestration and controlled resumption; checkpointed state must still be secured and external side effects made safe.
- **C:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **D:** Incorrect for this requirement. Keeps query and document representations in the same semantic space; mixing incompatible model versions can break relevance.

### Question 52 — D

Answer: Compare quality against a stable versioned baseline. A versioned baseline detects a change in task quality even when availability and response speed are unchanged. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-observability-and-monitoring-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Incorrect for this requirement. Shows rates, latency, and resource trends but does not alone reconstruct a particular cross-service execution.
- **B:** Incorrect for this requirement. Separates worker availability and recurrent failure conditions from content-quality scoring alone.
- **C:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **D:** Correct. Detects worsened task outcomes after changes; a healthy process or fast response does not establish answer quality.

### Question 53 — C

Answer: Validate and screen the final response before delivery. Final delivery is its own intervention point, though it does not replace controls before tool effects. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-guardrails-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **B:** Incorrect for this requirement. Supports accountability after and during execution but does not by itself stop an unapproved action.
- **C:** Correct. Applies final output controls but cannot undo an unauthorized side effect that has already occurred.
- **D:** Incorrect for this requirement. Applies configured input-side controls, while downstream boundaries and output checks still remain necessary.

### Question 54 — D

Answer: Use session-scoped short-term state. Temporary interaction state should be scoped to the session instead of being persisted as general memory. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-logical-architecture-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/

- **A:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **B:** Incorrect for this requirement. Supports semantic lookup but is not automatically an authoritative transactional store for every workflow state.
- **C:** Incorrect for this requirement. Persists approved information beyond a session with access, retention, deletion, and relevance controls.
- **D:** Correct. Retains information for an active interaction or workflow rather than serving as unrestricted persistent cross-session memory.

### Question 55 — A

Answer: Use qualified human reviewers with a shared rubric. Nuanced evaluations require a consistent rubric and qualified judgment; operational statistics alone cannot assess them. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-evaluation-and-validation-strategies-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Correct. Evaluates nuanced correctness, usefulness, and safety while documenting reviewer disagreement and escalation.
- **B:** Incorrect for this requirement. Ignores quality, retry cost, tool reliability, latency, and other business constraints.
- **C:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **D:** Incorrect for this requirement. Shows rates, latency, and resource trends but does not alone reconstruct a particular cross-service execution.

### Question 56 — C

Answer: Implement an MCP client that discovers and invokes permitted tools. The consumer side discovers and invokes permitted MCP capabilities, handling responses under application policy. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#build-and-integrate-tool-ecosystems Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Exposes supported tools and resources through MCP while validating arguments and enforcing caller permissions.
- **B:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **C:** Correct. Consumes the server interface and handles tool results under application policy; discovery is not permission to execute every tool.
- **D:** Incorrect for this requirement. Supports collaboration with compatible remote agents through defined agent-facing contracts; it is not identical to a tool-resource interface.

### Question 57 — D

Answer: Benchmark models against task capability and operational constraints. Model choice requires task-specific evidence and operational fit rather than a single price or size ranking. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-logical-architecture-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/

- **A:** Incorrect for this requirement. Ignores quality, retry cost, tool reliability, latency, and other business constraints.
- **B:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **C:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.
- **D:** Correct. Matches measured reasoning, modality, context, latency, cost, and deployment requirements instead of choosing only by size.

### Question 58 — D

Answer: Use an Azure managed identity where supported. Supported workload identity avoids embedding application credentials, while a separate authorization assignment still limits resource access. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-security-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Incorrect for this requirement. Can authenticate supported service access but is a secret and generally does not carry a delegated user identity by itself.
- **B:** Incorrect for this requirement. Simplifies credential sharing but removes per-agent isolation and increases the impact of compromise.
- **C:** Incorrect for this requirement. Reduces active context size but can omit details; important facts need preservation and verification.
- **D:** Correct. Lets an Azure workload obtain identity-based access without embedding a long-lived application secret; resource authorization is still required.

### Question 59 — D

Answer: Separate trusted instructions from untrusted content. Untrusted documents should not acquire instruction authority merely because they appear in a model context. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-advanced-prompt-engineering-strategies-in-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **B:** Incorrect for this requirement. Supports accountability after and during execution but does not by itself stop an unapproved action.
- **C:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **D:** Correct. Reduces instruction confusion by treating retrieved or user-supplied material as data; enforcement still needs layered controls.

### Question 60 — A

Answer: Stop expansion and apply the defined rollback or investigation policy. A production gate should include relevant quality and safety outcomes as well as health. Follow the pre-approved response policy instead of silently redefining acceptance. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#deploy-multi-agent-solutions-to-azure Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Correct. Task quality is a release condition even when the service process remains healthy.
- **B:** Incorrect for this requirement. Bypassing the gate defeats the purpose of limiting initial exposure.
- **C:** Incorrect for this requirement. Transport availability does not prove correct task outcomes.
- **D:** Incorrect for this requirement. Expanding exposure after a failed gate increases user risk.

### Question 61 — D

Answer: Inspect and constrain user input before agent processing. Input-side intervention can reject or constrain risky incoming requests before they drive agent processing. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-guardrails-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **B:** Incorrect for this requirement. Applies final output controls but cannot undo an unauthorized side effect that has already occurred.
- **C:** Incorrect for this requirement. Supports accountability after and during execution but does not by itself stop an unapproved action.
- **D:** Correct. Applies configured input-side controls, while downstream boundaries and output checks still remain necessary.

### Question 62 — B

Answer: Run regression tests and automated agent evaluations. Release checks should preserve previously accepted agent behavior across code, model, prompt, and tool changes. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#deploy-multi-agent-solutions-to-azure Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Incorrect for this requirement. Adds coordination work without resolving unclear ownership, contracts, or workflow design.
- **B:** Correct. Checks that previously accepted behavior and quality are preserved after prompt, model, tool, or code changes.
- **C:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **D:** Incorrect for this requirement. Tests functions and logic in isolation, often with fakes or mocks; it does not prove live service integration.

### Question 63 — C

Answer: Gate CI/CD on reviewed artifacts, security checks, and evaluations. CI/CD should require reviewed artifacts and passing checks before promotion rather than treating successful packaging as acceptance. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#deploy-multi-agent-solutions-to-azure Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Incorrect for this requirement. Removes staged evidence and increases exposure to unreviewed errors.
- **B:** Incorrect for this requirement. Demonstrates desired behavior in context without modifying learned model weights.
- **C:** Correct. Automates build and release evidence while preventing failed checks from silently promoting a release.
- **D:** Incorrect for this requirement. Supports accountability after and during execution but does not by itself stop an unapproved action.

### Question 64 — B

Answer: Use reusable middleware for cross-cutting controls. Reusable cross-cutting behavior belongs in controlled middleware rather than being duplicated or entrusted only to model text. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#implement-multi-agent-orchestration Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Demonstrates desired behavior in context without modifying learned model weights.
- **B:** Correct. Centralizes concerns such as authorization, trace enrichment, and exception handling without duplicating them in every agent.
- **C:** Incorrect for this requirement. Supports semantic lookup but is not automatically an authoritative transactional store for every workflow state.
- **D:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.

### Question 65 — B, D

Answer: Benchmark a smaller adequate model for selected tasks; Remove irrelevant context while preserving necessary evidence. Model fit and context efficiency can reduce cost, but both changes must preserve measured quality and safety. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#optimize-prompt-and-model-performance-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Incorrect for this requirement. Adds coordination work without resolving unclear ownership, contracts, or workflow design.
- **B:** Correct. Reduces wasted tokens and can improve focus, but must not discard required facts or policy constraints.
- **C:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.
- **D:** Correct. May reduce inference cost and latency if measured quality, safety, and tool reliability remain acceptable.
- **E:** Incorrect for this requirement. Can cause runaway cost, load, and repeated side effects rather than providing reliable convergence.

### Question 66 — B

Answer: Chunk documents into coherent retrievable passages. Retrievable passage size and boundaries determine whether evidence is both focused and sufficiently contextual. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-agent-memory-context-management-and-knowledge-integration Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **B:** Correct. Controls retrieval granularity; excessive size wastes context, while tiny isolated chunks can lose meaning.
- **C:** Incorrect for this requirement. Authorizes supported Azure resource operations for principals at appropriate scopes; it does not describe the full behavioral role of an agent.
- **D:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.

### Question 67 — C

Answer: Assemble only relevant state, evidence, and tool results. Useful context is selected and budgeted, not built by blindly forwarding every conversation and tool result. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-agent-memory-context-management-and-knowledge-integration Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Can cause runaway cost, load, and repeated side effects rather than providing reliable convergence.
- **B:** Incorrect for this requirement. Persists approved information beyond a session with access, retention, deletion, and relevance controls.
- **C:** Correct. Builds useful request context within a token budget instead of forwarding every prior message.
- **D:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.

### Question 68 — D

Answer: Separate session state, shared team state, and long-term memory. Different state classes need distinct persistence, consistency, access, and lifecycle policies. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#specify-technology-components-to-include-in-a-multi-agent-solution Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/

- **A:** Incorrect for this requirement. Can simplify coordination but does not establish the independently bounded specialist responsibilities required in this scenario.
- **B:** Incorrect for this requirement. Supports semantic lookup but is not automatically an authoritative transactional store for every workflow state.
- **C:** Incorrect for this requirement. Retains information for an active interaction or workflow rather than serving as unrestricted persistent cross-session memory.
- **D:** Correct. Assigns each state class suitable persistence, consistency, isolation, and lifecycle controls.

### Question 69 — B

Answer: Use Agent2Agent (A2A) interoperability. Collaborating with a remote agent through an agent-facing contract calls for A2A rather than treating every peer as a raw resource server. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-logical-architecture-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/

- **A:** Incorrect for this requirement. Provides a standard interface for exposing tools, resources, and prompts to compatible clients; security remains a separate design duty.
- **B:** Correct. Supports collaboration with compatible remote agents through defined agent-facing contracts; it is not identical to a tool-resource interface.
- **C:** Incorrect for this requirement. Supports semantic lookup but is not automatically an authoritative transactional store for every workflow state.
- **D:** Incorrect for this requirement. Improves environment reproducibility; it does not by itself determine production architecture or access policies.

### Question 70 — C

Answer: Re-embed content with a consistent compatible embedding configuration. Query and document vectors need a compatible embedding space; changing the model may require reindexing. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-agent-memory-context-management-and-knowledge-integration Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Improves ordering within a candidate set; it cannot recover a document never retrieved.
- **B:** Incorrect for this requirement. Reduces active context size but can omit details; important facts need preservation and verification.
- **C:** Correct. Keeps query and document representations in the same semantic space; mixing incompatible model versions can break relevance.
- **D:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.

### Question 71 — A

Answer: Validate OAuth access tokens and enforce audience and scopes. A receiving API must verify token validity and intended audience and enforce permissions for the operation. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-security-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Correct. Checks that a token is valid for the receiving API and the requested operation; possession of any token is not sufficient.
- **B:** Incorrect for this requirement. Supports accountability after and during execution but does not by itself stop an unapproved action.
- **C:** Incorrect for this requirement. Can authenticate supported service access but is a secret and generally does not carry a delegated user identity by itself.
- **D:** Incorrect for this requirement. Makes instruction changes reproducible, comparable, and reversible.

### Question 72 — A

Answer: Use supported private endpoints and correct private DNS. Private connectivity requires consistent endpoint, DNS, route, and access configuration rather than merely a private-looking URL. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-security-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Correct. Provides private connectivity to supported services when network routes, DNS, and public-access settings are configured consistently.
- **B:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **C:** Incorrect for this requirement. May bypass a connection problem by removing intended isolation, but does not satisfy a private-only design.
- **D:** Incorrect for this requirement. Can reduce supported harmful content but does not replace consent, permissions, human review, or all domain-specific policies.

### Question 73 — B, E

Answer: Keep independent evaluation data and gate model changes; Version prompts and evaluate changes before promotion. Independent evaluation and versioned instructions make behavioral changes measurable and reversible. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-advanced-prompt-engineering-strategies-in-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Adds coordination work without resolving unclear ownership, contracts, or workflow design.
- **B:** Correct. Makes instruction changes reproducible, comparable, and reversible.
- **C:** Incorrect for this requirement. Can cause runaway cost, load, and repeated side effects rather than providing reliable convergence.
- **D:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.
- **E:** Correct. Measures generalization and regression without using the same examples to train and certify a change.

### Question 74 — A

Answer: Use Model Context Protocol (MCP). The requirement is a standard tool-resource interface, not delegation to another independent agent. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-logical-architecture-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/

- **A:** Correct. Provides a standard interface for exposing tools, resources, and prompts to compatible clients; security remains a separate design duty.
- **B:** Incorrect for this requirement. Provides a conventional HTTP contract but does not inherently implement a requested agent or MCP interoperability standard.
- **C:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **D:** Incorrect for this requirement. Supports collaboration with compatible remote agents through defined agent-facing contracts; it is not identical to a tool-resource interface.

### Question 75 — A

Answer: Execute a validated function call in application code. A model-produced tool request is a proposal; authorized application code must validate and execute it. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#build-and-integrate-tool-ecosystems Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Correct. The model proposes structured tool arguments, while trusted code authorizes and performs the operation.
- **B:** Incorrect for this requirement. Reduces active context size but can omit details; important facts need preservation and verification.
- **C:** Incorrect for this requirement. Demonstrates desired behavior in context without modifying learned model weights.
- **D:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.

### Question 76 — B

Answer: Select compute using workload, scaling, network, and reliability requirements. Compute selection must follow execution and operational constraints; naming one service without those requirements is insufficient. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#specify-technology-components-to-include-in-a-multi-agent-solution Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/

- **A:** Incorrect for this requirement. Provides managed container hosting and supported scaling features, subject to runtime and connectivity requirements.
- **B:** Correct. Evaluates hosting constraints and operational needs rather than assuming a single compute type fits every agent.
- **C:** Incorrect for this requirement. Provides Kubernetes control and ecosystem flexibility with additional operational responsibility.
- **D:** Incorrect for this requirement. Fits bounded event-driven operations when execution, hosting, networking, and scaling limits meet the workload.

### Question 77 — B

Answer: Place appropriate policies at Azure API Management. API policy enforcement and request governance are gateway responsibilities, separate from model training and tool execution. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#build-and-integrate-tool-ecosystems Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Fits bounded event-driven operations when execution, hosting, networking, and scaling limits meet the workload.
- **B:** Correct. Provides an API governance layer for authentication, traffic management, and policies; it does not by itself grant downstream data permissions.
- **C:** Incorrect for this requirement. Provides model and pipeline tooling for supported architectures; it is not a replacement for agent authorization or orchestration design.
- **D:** Incorrect for this requirement. Supports semantic lookup but is not automatically an authoritative transactional store for every workflow state.

### Question 78 — D

Answer: Attribute usage to tenants, projects, and workflow runs. Usage attribution needs trusted tenant and project metadata to support budgets and fair allocations. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-observability-and-monitoring-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Incorrect for this requirement. Shows rates, latency, and resource trends but does not alone reconstruct a particular cross-service execution.
- **B:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.
- **C:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **D:** Correct. Enables quotas, allocations, and chargeback using governed usage metadata instead of inferring all costs from one shared total.

### Question 79 — D, E

Answer: Grant only required secret access to each workload; Rotate secrets and update dependent applications safely. Secret access must be scoped and credentials managed through a tested replacement lifecycle. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-security-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Incorrect for this requirement. Simplifies credential sharing but removes per-agent isolation and increases the impact of compromise.
- **B:** Incorrect for this requirement. Exposes a powerful secret across model interactions and removes per-workload access separation.
- **C:** Incorrect for this requirement. Creates avoidable sensitive-data exposure and violates data-minimization and secret-handling requirements.
- **D:** Correct. Limits the scope of credential retrieval rather than allowing every agent to read all stored secrets.
- **E:** Correct. Changes credentials through a tested lifecycle with controlled overlap or rollout where supported, rather than retaining a leaked value.

### Question 80 — D

Answer: Evaluate recovery, safe failure, and task completion under faults. A production evaluation must test recovery and partial failure, not just correct answers when every dependency succeeds. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-evaluation-and-validation-strategies-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.
- **B:** Incorrect for this requirement. Demonstrates desired behavior in context without modifying learned model weights.
- **C:** Incorrect for this requirement. Checks faithfulness to available context, not merely fluent language or relevant retrieved documents.
- **D:** Correct. Tests behavior under unavailable tools and partial failures, not just successful-path answers.

### Question 81 — D

Answer: Store and retrieve secrets through Azure Key Vault. Secrets need governed storage and authorized retrieval rather than inclusion in prompts, source files, or semantic memory. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-security-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Incorrect for this requirement. Exposes a powerful secret across model interactions and removes per-workload access separation.
- **B:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **C:** Incorrect for this requirement. Supports semantic lookup but is not automatically an authoritative transactional store for every workflow state.
- **D:** Correct. Centralizes supported secrets, keys, and certificates with controlled access and lifecycle management.

### Question 82 — C

Answer: Run adversarial testing early and throughout the lifecycle. Adversarial evaluation should begin before release and continue as the system changes; it does not establish an absolute safety guarantee. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-security-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.
- **B:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **C:** Correct. Uses challenging and misuse-oriented tests, including supported Foundry red-teaming capabilities, to discover risks before and after release.
- **D:** Incorrect for this requirement. Removes staged evidence and increases exposure to unreviewed errors.

### Question 83 — A

Answer: Maintain stable entity IDs and validated factual state. Stable identifiers and verified factual state prevent confusion when similar entities appear across handoffs. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-agent-memory-context-management-and-knowledge-integration Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Correct. Preserves identity and critical facts across summaries and agent transitions rather than relying on ambiguous names alone.
- **B:** Incorrect for this requirement. Supports semantic lookup but is not automatically an authoritative transactional store for every workflow state.
- **C:** Incorrect for this requirement. Reduces active context size but can omit details; important facts need preservation and verification.
- **D:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.

### Question 84 — B

Answer: Apply purpose-based memory retention and deletion. Persisted memory remains subject to approved purpose and retention; storage does not create indefinite permission. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-agent-memory-context-management-and-knowledge-integration Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Keeps query and document representations in the same semantic space; mixing incompatible model versions can break relevance.
- **B:** Correct. Expires or deletes retained information according to policy rather than assuming all remembered content remains authorized forever.
- **C:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **D:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.

### Question 85 — C

Answer: Validate tool results against schema and domain constraints. Successful transport does not prove the payload is well-formed, plausible, or safe for downstream decisions. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#build-and-integrate-tool-ecosystems Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Supports accountability after and during execution but does not by itself stop an unapproved action.
- **B:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **C:** Correct. Checks structure, types, ranges, and semantic consistency before downstream use; HTTP success alone is insufficient.
- **D:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.

### Question 86 — D

Answer: Use a governed semantic response cache. Meaning-equivalent response reuse needs a governed similarity cache with strict access and freshness boundaries. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#implement-multi-agent-orchestration Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **B:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **C:** Incorrect for this requirement. Reuses prior results for a matching cache key when authorization and freshness permit, rather than matching approximate meaning.
- **D:** Correct. Can reuse meaning-equivalent responses only when permissions, tenant scope, freshness, and task semantics allow it.

### Question 87 — C

Answer: Combine lexical and vector retrieval. Exact identifiers benefit from lexical matching, while paraphrases benefit from semantic matching. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-agent-memory-context-management-and-knowledge-integration Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **B:** Incorrect for this requirement. Supports semantic lookup but is not automatically an authoritative transactional store for every workflow state.
- **C:** Correct. Can match both exact identifiers and semantic paraphrases; it still needs relevance evaluation and permissions.
- **D:** Incorrect for this requirement. Reduces active context size but can omit details; important facts need preservation and verification.

### Question 88 — B

Answer: Diagnose summary drift. Repeated compaction can distort retained facts; authoritative state and summary checks help detect this. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#optimize-prompt-and-model-performance-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **B:** Correct. Identifies accumulated distortion when repeated summarization alters or omits important facts.
- **C:** Incorrect for this requirement. Identifies loss of earlier information as it drops out of active context; this is distinct from a model weight update.
- **D:** Incorrect for this requirement. Detects shifts in operating conditions or behavioral patterns that can require investigation and reassessment.

### Question 89 — D, E

Answer: Authorize and validate the proposed tool action before execution; Validate and screen tool responses before reuse. The requested controls apply immediately around tool execution, not only to final user-facing text. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-guardrails-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Incorrect for this requirement. Applies final output controls but cannot undo an unauthorized side effect that has already occurred.
- **B:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **C:** Incorrect for this requirement. Supports accountability after and during execution but does not by itself stop an unapproved action.
- **D:** Correct. Checks external output structure and policy and treats embedded instructions as untrusted before it reaches another agent.
- **E:** Correct. Checks caller authority, arguments, target, and domain restrictions before an external effect occurs.

### Question 90 — C

Answer: Bound concurrent agent and tool execution. A semaphore or worker limit should constrain simultaneous work to available capacity and downstream quotas. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#implement-multi-agent-orchestration Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **B:** Incorrect for this requirement. Can cause runaway cost, load, and repeated side effects rather than providing reliable convergence.
- **C:** Correct. Limits simultaneous work according to capacity and downstream quotas instead of spawning unbounded tasks.
- **D:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.

### Question 91 — A

Answer: Use parallel orchestration with a controlled join. Independent tasks can run concurrently; join logic should combine their completed outputs. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-logical-architecture-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/

- **A:** Correct. Runs independent branches concurrently and combines their results after completion.
- **B:** Incorrect for this requirement. Transfers task responsibility to the appropriate specialist with explicit context and termination rules.
- **C:** Incorrect for this requirement. Passes work through dependent stages where later tasks require earlier outputs.
- **D:** Incorrect for this requirement. Can simplify coordination but does not establish the independently bounded specialist responsibilities required in this scenario.

### Question 92 — B

Answer: Implement a controlled agent workflow with explicit review and resume. A human checkpoint must pause action, preserve correlation, and resume only after a valid decision and authorization check. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#implement-multi-agent-orchestration Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Incorrect for this requirement. Demonstrates desired behavior in context without modifying learned model weights.
- **B:** Correct. Coordinates agent steps and human intervention in a framework-supported workflow, with durable correlation and revalidation before action.
- **C:** Incorrect for this requirement. Supports accountability after and during execution but does not by itself stop an unapproved action.
- **D:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.

### Question 93 — C

Answer: Decompose the goal into bounded agent responsibilities and tools. Independent responsibilities and deterministic tools should be identified before adding autonomous workers. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-logical-architecture-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-1-architect-production-grade-multi-agent-ai-solutions/

- **A:** Incorrect for this requirement. Adds coordination work without resolving unclear ownership, contracts, or workflow design.
- **B:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **C:** Correct. Defines who performs each task and which deterministic operations are exposed, instead of giving every agent the whole problem.
- **D:** Incorrect for this requirement. Can simplify coordination but does not establish the independently bounded specialist responsibilities required in this scenario.

### Question 94 — B

Answer: Deploy versioned infrastructure as code through reviewed automation. Reviewed infrastructure definitions improve reproducibility across environments and make deployment configuration auditable. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#deploy-multi-agent-solutions-to-azure Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Incorrect for this requirement. Makes instruction changes reproducible, comparable, and reversible.
- **B:** Correct. Makes environment configuration reproducible and auditable, with environment-specific identity and policy settings.
- **C:** Incorrect for this requirement. Removes staged evidence and increases exposure to unreviewed errors.
- **D:** Incorrect for this requirement. Demonstrates desired behavior in context without modifying learned model weights.

### Question 95 — A

Answer: Inject relevant authorized context at request time. Task-specific current information should be injected at inference after authorization, not assumed to exist in model weights. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-advanced-prompt-engineering-strategies-in-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-2-build-production-grade-multi-agent-capabilities-microsoft-foundry/

- **A:** Correct. Supplies current task information during inference without treating it as permanently learned knowledge.
- **B:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **C:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **D:** Incorrect for this requirement. Reduces active context size but can omit details; important facts need preservation and verification.

### Question 96 — B

Answer: Use isolated unit tests for deterministic components. Isolated deterministic logic can be tested with controlled dependencies; this does not replace live integration checks. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#deploy-multi-agent-solutions-to-azure Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Incorrect for this requirement. Uses challenging and misuse-oriented tests, including supported Foundry red-teaming capabilities, to discover risks before and after release.
- **B:** Correct. Tests functions and logic in isolation, often with fakes or mocks; it does not prove live service integration.
- **C:** Incorrect for this requirement. Verifies real contracts, authentication, networking, and service behavior across component boundaries.
- **D:** Incorrect for this requirement. Limits initial exposure and expands only after measured outcomes meet criteria.

### Question 97 — A

Answer: Coordinate concurrency, rate budgets, and backoff. Excess concurrency can increase throttling, so throughput optimization must respect downstream rate budgets. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#optimize-prompt-and-model-performance-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Correct. Controls request pressure on limited services; unconstrained parallelism can increase throttling and latency.
- **B:** Incorrect for this requirement. May increase cost and latency and does not establish that capability, geography, or quality requirements are met.
- **C:** Incorrect for this requirement. Updates learned model behavior using training examples; it does not itself define workflow boundaries, permissions, or coordination.
- **D:** Incorrect for this requirement. Can cause runaway cost, load, and repeated side effects rather than providing reliable convergence.

### Question 98 — D

Answer: Authorize and validate the proposed tool action before execution. Authorization and business validation must occur before the external action; final text screening is too late. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-guardrails-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **B:** Incorrect for this requirement. Supports accountability after and during execution but does not by itself stop an unapproved action.
- **C:** Incorrect for this requirement. Applies final output controls but cannot undo an unauthorized side effect that has already occurred.
- **D:** Correct. Checks caller authority, arguments, target, and domain restrictions before an external effect occurs.

### Question 99 — A

Answer: Test interactions with configured external dependencies. Real component boundaries need contract, identity, networking, and dependency tests beyond isolated mocks. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#deploy-multi-agent-solutions-to-azure Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-3-deploy-govern-agentic-ai-solutions-azure/

- **A:** Correct. Verifies real contracts, authentication, networking, and service behavior across component boundaries.
- **B:** Incorrect for this requirement. Demonstrates desired behavior in context without modifying learned model weights.
- **C:** Incorrect for this requirement. Can reuse processing of repeated eligible prefixes under provider-specific rules; it is not a cache of arbitrary final answers.
- **D:** Incorrect for this requirement. Tests functions and logic in isolation, often with fakes or mocks; it does not prove live service integration.

### Question 100 — B

Answer: Monitor agent health and workflow failure patterns. Availability and repeated operational failures need health and failure-pattern telemetry, not only language-quality evaluation. Microsoft Learn reference: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500#design-and-implement-observability-and-monitoring-for-multi-agent-solutions Related learning path: https://learn.microsoft.com/en-us/training/paths/aaai-4-monitor-evaluate-operate-multi-agent-ai-solutions-azure/

- **A:** Incorrect for this requirement. Demonstrates desired behavior in context without modifying learned model weights.
- **B:** Correct. Separates worker availability and recurrent failure conditions from content-quality scoring alone.
- **C:** Incorrect for this requirement. Checks faithfulness to available context, not merely fluent language or relevant retrieved documents.
- **D:** Incorrect for this requirement. Ignores quality, retry cost, tool reliability, latency, and other business constraints.
