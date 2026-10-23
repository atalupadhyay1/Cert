# Google Cloud Professional Agentic Architect (PAA) — Practice Set 6

Integrated Architect Scenarios and Final Review

100 questions · Suggested practice duration: 180 minutes · Practice target: 80%

Tests 1–5 are focused learning tests. Test 6 is an expanded five-domain review, not an official exam replica. Related concepts recur.

Select ONE best answer for every question. Answer key follows all questions.

Original educational content, not actual, recalled, or copied Anthropic exam items.

## Questions

### 1. A stateless API agent must scale to zero. What runtime fits?

Domain: Evaluating and Deploying Agentic Workflows

- A. Keep the service stateless and externalize session data
- B. Use GKE when you need cluster-level control and custom orchestration
- C. Deploy to Cloud Run for containerized request-driven services
- D. Deploy to Agent Runtime for managed agent hosting

### 2. A coding agent will run untrusted repository tests. Where and how should it run?

Domain: Using Coding Agents for Application Development

- A. Run coding agents in an isolated, permission-limited environment
- B. Use Cloud Workstations for managed developer environments
- C. Restrict tools, credentials, and network access in the sandbox
- D. Use GKE isolation and policy controls for agent workloads

### 3. A team needs to find the most expensive and failure-prone step. What should it use?

Domain: Evaluating and Deploying Agentic Workflows

- A. Use Cloud Logging, Cloud Trace, and Cloud Monitoring
- B. Provision capacity for peak concurrency and quotas
- C. Track token and tool cost per completed task
- D. Record agent actions and tool calls in audit logs

### 4. A security team needs visibility and control over agent egress. What should it deploy?

Domain: Securing and Governing Agentic Workflows

- A. Govern agent traffic through Agent Gateway
- B. Record agent actions and tool calls in audit logs
- C. Inspect and de-identify sensitive data with Sensitive Data Protection
- D. Restrict outbound network access to approved destinations

### 5. A model update is released without evaluation. What should have happened?

Domain: Evaluating and Deploying Agentic Workflows

- A. Use staged rollout with measurable rollback criteria
- B. Monitor production behavior with online evaluation
- C. Run evaluation on every meaningful change
- D. Set explicit pass thresholds before evaluating

### 6. An automated judge disagrees with experts on high-impact answers. What should happen?

Domain: Developing Custom Agents

- A. Set explicit pass thresholds before evaluating
- B. Use human review for unresolved or high-impact judgment
- C. Use a calibrated model-based autorater for scalable judgment
- D. Ground the response in cited retrieved evidence

### 7. A managed agent runtime throttles at peak. What should be planned?

Domain: Developing Custom Agents

- A. Set an end-to-end latency budget
- B. Use staged rollout with measurable rollback criteria
- C. Track token and tool cost per completed task
- D. Provision capacity for peak concurrency and quotas

### 8. A coding agent must never commit generated credentials. What is the strongest control?

Domain: Using Coding Agents for Application Development

- A. Run deterministic logic when a lifecycle event fires
- B. Package reusable guidance and assets as a skill
- C. Provide persistent coding guidance for a coding agent
- D. Bundle related skills, tools, and configuration as a plugin

### 9. An agent tries to send customer data to a personal endpoint. What should prevent it?

Domain: Securing and Governing Agentic Workflows

- A. Redact or de-identify sensitive data before model exposure
- B. Govern agent traffic through Agent Gateway
- C. Use customer-managed encryption keys where required
- D. Restrict outbound network access to approved destinations

### 10. A quality team wants an agent to answer questions about recorded calls. What is required first?

Domain: Building Agents Using Low-Code Tools

- A. Choose an embedding model suited to the domain and language
- B. Choose chunk size and overlap for retrieval
- C. Rerank retrieved passages before generation
- D. Process images, audio, and video through supported ingestion

### 11. Retrieved content instructs the agent to reveal system credentials. What should happen?

Domain: Securing and Governing Agentic Workflows

- A. Treat retrieved and user-supplied content as untrusted
- B. Redact or de-identify sensitive data before model exposure
- C. Store secrets in Secret Manager rather than prompts or code
- D. Apply purpose limitation and consent to personal data

### 12. A team wants security checks to run on every generated change. What should enforce them?

Domain: Using Coding Agents for Application Development

- A. Run deterministic logic when a lifecycle event fires
- B. Provide persistent coding guidance for a coding agent
- C. Bundle related skills, tools, and configuration as a plugin
- D. Package reusable guidance and assets as a skill

### 13. An agent-generated security fix changes several unrelated modules. What should review require?

Domain: Using Coding Agents for Application Development

- A. Require review of generated diffs before merge
- B. Use the coding agent to restructure code with tests as the contract
- C. Locate and fix an application-layer vulnerability, then verify the fix
- D. Profile execution paths before optimizing them

### 14. An audit asks who approved an agent-generated production change. What should be available?

Domain: Using Coding Agents for Application Development

- A. Require review of generated diffs before merge
- B. Operate and govern deployed agents with Agents CLI
- C. Register agents and capabilities in Agent Registry
- D. Record agent actions and tool calls in audit logs

### 15. An agent can transfer money above a threshold. What control is required?

Domain: Securing and Governing Agentic Workflows

- A. Review high-impact actions with accountable owners
- B. Require human approval before a consequential action
- C. Gate the action on explicit, attributable approval
- D. Enforce a policy check before a consequential action

### 16. An audit cannot attribute an action to a specific agent. What should change?

Domain: Securing and Governing Agentic Workflows

- A. Give each agent its own managed identity
- B. Use a dedicated service account with least privilege
- C. Record agent actions and tool calls in audit logs
- D. Constrain access with a principal access boundary policy

### 17. An unregistered agent attempts a governed tool call. What should happen?

Domain: Securing and Governing Agentic Workflows

- A. Record agent actions and tool calls in audit logs
- B. Register agents and capabilities in Agent Registry
- C. Govern agent traffic through Agent Gateway
- D. Encode organizational policy in enforceable controls

### 18. A tool call times out after a write may have succeeded. What should the agent do?

Domain: Developing Custom Agents

- A. Set timeouts and bounded retries for tool calls
- B. Bound iterations and detect reasoning loops
- C. Inspect spans across agent, model, and tool calls
- D. Return structured tool errors that guide recovery

### 19. A sandbox can download dependencies from any host. What should be narrowed?

Domain: Using Coding Agents for Application Development

- A. Restrict outbound network access to approved destinations
- B. Restrict tools, credentials, and network access in the sandbox
- C. Grant IAM roles to the agent identity, not to users' credentials
- D. Constrain access with a principal access boundary policy

### 20. A team wants managed ingestion and retrieval components. What should it evaluate?

Domain: Developing Custom Agents

- A. Use RAG Engine for managed retrieval pipeline components
- B. Store embeddings in a managed vector index
- C. Use Agent Retrieval and Vector Search for agent-oriented retrieval
- D. Connect approved enterprise content through Agent Search

### 21. An incident response grants broad temporary access. What should follow?

Domain: Securing and Governing Agentic Workflows

- A. Constrain access with a principal access boundary policy
- B. Grant the minimum permissions required for the task
- C. Grant IAM roles to the agent identity, not to users' credentials
- D. Use a dedicated service account with least privilege

### 22. An agent needs read access to one dataset and nothing else. What should be configured?

Domain: Developing Custom Agents

- A. Grant IAM roles to the agent identity, not to users' credentials
- B. Give each agent its own managed identity
- C. Grant the minimum permissions required for the task
- D. Constrain access with a principal access boundary policy

### 23. A user asks what the agent remembers and requests deletion. What must the system support?

Domain: Securing and Governing Agentic Workflows

- A. Apply purpose limitation and consent to personal data
- B. Define what may be remembered, for how long, and why
- C. Redact or de-identify sensitive data before model exposure
- D. Record agent actions and tool calls in audit logs

### 24. A low-code agent cannot confirm a customer's eligibility for a program. What is the best response?

Domain: Building Agents Using Low-Code Tools

- A. Register agents and capabilities in Agent Registry
- B. Screen prompts and responses with Model Armor
- C. Define a safe fallback when the request is unsupported
- D. Model behavior explicitly as pages, transition routes, and event handlers

### 25. An organization wants governed discovery of agents and their tools. What should it combine?

Domain: Developing Custom Agents

- A. Bundle related skills, tools, and configuration as a plugin
- B. Register agents and capabilities in Agent Registry
- C. Use MCP for standardized tool and resource access
- D. Publish an Agent Card describing capabilities and endpoints

### 26. A code review subagent finds a critical issue while implementation continues. What should happen?

Domain: Using Coding Agents for Application Development

- A. Run independent agents concurrently
- B. Delegate a scoped task to a specialized agent
- C. Route a request to the most suitable specialist agent
- D. Transfer control with explicit context and state

### 27. A coding agent needs an approved package registry and issue tracker. What should be configured?

Domain: Using Coding Agents for Application Development

- A. Expose approved capabilities through an MCP server
- B. Use MCP for standardized tool and resource access
- C. Bundle related skills, tools, and configuration as a plugin
- D. Package reusable guidance and assets as a skill

### 28. A high-volume classification step must be cheap and fast with bounded labels. What is a reasonable candidate?

Domain: Developing Custom Agents

- A. Set an end-to-end latency budget
- B. Use a managed model service under the applicable terms
- C. Use a smaller model for a narrow, high-volume task
- D. Host the model on infrastructure you control

### 29. A low-code agent changes its escalation policy. What should precede release?

Domain: Building Agents Using Low-Code Tools

- A. Run evaluation on every meaningful change
- B. Use staged rollout with measurable rollback criteria
- C. Record agent actions and tool calls in audit logs
- D. Set explicit pass thresholds before evaluating

### 30. A long-running agent needs managed hosting, sessions, and memory integration. What should be evaluated?

Domain: Developing Custom Agents

- A. Use GKE when you need cluster-level control and custom orchestration
- B. Deploy to Cloud Run for containerized request-driven services
- C. Deploy to Agent Runtime for managed agent hosting
- D. Keep the service stateless and externalize session data

### 31. A non-retryable permission error is retried repeatedly. What should change?

Domain: Evaluating and Deploying Agentic Workflows

- A. Record agent actions and tool calls in audit logs
- B. Return structured tool errors that guide recovery
- C. Bound iterations and detect reasoning loops
- D. Set timeouts and bounded retries for tool calls

### 32. A public agent needs layered protection against injection and data leakage. What combination fits?

Domain: Securing and Governing Agentic Workflows

- A. Register agents and capabilities in Agent Registry
- B. Inspect and de-identify sensitive data with Sensitive Data Protection
- C. Screen prompts and responses with Model Armor
- D. Encode organizational policy in enforceable controls

### 33. An incident reveals a missing test case. What should be added before the fix?

Domain: Evaluating and Deploying Agentic Workflows

- A. Author an ADK evalset with expected tool use and responses
- B. Run evaluation on every meaningful change
- C. Build a representative golden dataset from real tasks
- D. Include edge cases and adversarial inputs in test sets

### 34. A platform team wants coding agents to use approved build tools only. What should it provide?

Domain: Using Coding Agents for Application Development

- A. Operate and govern deployed agents with Agents CLI
- B. Use Antigravity surfaces for agent-assisted development
- C. Package reusable guidance and assets as a skill
- D. Expose approved capabilities through an MCP server

### 35. An approval can be reused for multiple transactions. What should change?

Domain: Securing and Governing Agentic Workflows

- A. Require human approval before a consequential action
- B. Record agent actions and tool calls in audit logs
- C. Gate the action on explicit, attributable approval
- D. Enforce a policy check before a consequential action

### 36. A downstream tool must apply the end user's permissions. What should be propagated?

Domain: Securing and Governing Agentic Workflows

- A. Use scoped OAuth 2.0 tokens for agent-to-tool calls
- B. Grant IAM roles to the agent identity, not to users' credentials
- C. Propagate the caller's identity to downstream tools
- D. Govern agent traffic through Agent Gateway

### 37. A new MCP server exposes customer data to agents. What should precede approval?

Domain: Developing Custom Agents

- A. Constrain access with a principal access boundary policy
- B. Expose approved capabilities through an MCP server
- C. Register agents and capabilities in Agent Registry
- D. Encode organizational policy in enforceable controls

### 38. A regulated build platform needs tenant isolation and network policy. What environment fits?

Domain: Using Coding Agents for Application Development

- A. Run coding agents in an isolated, permission-limited environment
- B. Use Cloud Workstations for managed developer environments
- C. Deploy to Cloud Run for containerized request-driven services
- D. Use GKE isolation and policy controls for agent workloads

### 39. A shared vector index serves multiple tenants. What must happen before retrieval results are used?

Domain: Developing Custom Agents

- A. Limit connected sources to the approved audience and purpose
- B. Filter retrieval by the requesting user's authorization
- C. Filter retrieval using trusted metadata
- D. Store embeddings in a managed vector index

### 40. A tool accepts arbitrary shell commands from the model. What should replace it?

Domain: Developing Custom Agents

- A. Expose a typed function as a tool
- B. Define a narrow tool schema with a clear description
- C. Run deterministic logic when a lifecycle event fires
- D. Enforce a policy check before a consequential action

### 41. A stateless service must support multi-turn conversations reliably. What should be added?

Domain: Developing Custom Agents

- A. Store task-scoped state deliberately
- B. Persist conversation and task state in a session
- C. Keep the service stateless and externalize session data
- D. Persist sessions in a durable managed store

### 42. A document-understanding agent must handle long, ambiguous contracts with high accuracy. What should be evaluated?

Domain: Developing Custom Agents

- A. Use a large model for complex reasoning or broad language work
- B. Select and deploy supported models through Model Garden
- C. Compare total cost per successful task
- D. Use a smaller model for a narrow, high-volume task

### 43. A workload needs custom networking and node isolation. What fits?

Domain: Evaluating and Deploying Agentic Workflows

- A. Deploy to Agent Runtime for managed agent hosting
- B. Use GKE when you need cluster-level control and custom orchestration
- C. Deploy to Cloud Run for containerized request-driven services
- D. Use Cloud Workstations for managed developer environments

### 44. Cold starts violate tail latency goals. What should be evaluated?

Domain: Evaluating and Deploying Agentic Workflows

- A. Deploy to Cloud Run for containerized request-driven services
- B. Set an end-to-end latency budget
- C. Provision capacity for peak concurrency and quotas
- D. Track token and tool cost per completed task

### 45. Production sampling includes sensitive content. What should be designed?

Domain: Evaluating and Deploying Agentic Workflows

- A. Set explicit pass thresholds before evaluating
- B. Use Cloud Logging, Cloud Trace, and Cloud Monitoring
- C. Use human review for unresolved or high-impact judgment
- D. Monitor production behavior with online evaluation

### 46. A test suite grows without version control. What problem results?

Domain: Evaluating and Deploying Agentic Workflows

- A. Set explicit pass thresholds before evaluating
- B. Build a representative golden dataset from real tasks
- C. Author an ADK evalset with expected tool use and responses
- D. Provision capacity for peak concurrency and quotas

### 47. A new customer segment behaves differently. What should be updated?

Domain: Evaluating and Deploying Agentic Workflows

- A. Detect changes in inputs, data, or performance over time
- B. Run evaluation on every meaningful change
- C. Set explicit pass thresholds before evaluating
- D. Author an ADK evalset with expected tool use and responses

### 48. A fleet of coding agents is deployed without inventory or ownership. What should be established?

Domain: Using Coding Agents for Application Development

- A. Record agent actions and tool calls in audit logs
- B. Register agents and capabilities in Agent Registry
- C. Govern agent traffic through Agent Gateway
- D. Operate and govern deployed agents with Agents CLI

### 49. A consumer assistant wants to remember preferences across sessions. What must accompany the feature?

Domain: Developing Custom Agents

- A. Pass files and large outputs as artifacts
- B. Store durable user or domain memory in Memory Bank
- C. Define what may be remembered, for how long, and why
- D. Persist conversation and task state in a session

### 50. An agent capability is published but has no owner or version. What risk arises?

Domain: Developing Custom Agents

- A. Register agents and capabilities in Agent Registry
- B. Bundle related skills, tools, and configuration as a plugin
- C. Use MCP for standardized tool and resource access
- D. Publish an Agent Card describing capabilities and endpoints

### 51. An agent stores a full transcript in durable memory for every user. What should be reconsidered?

Domain: Developing Custom Agents

- A. Pass files and large outputs as artifacts
- B. Store durable user or domain memory in Memory Bank
- C. Persist conversation and task state in a session
- D. Store task-scoped state deliberately

### 52. A broad refactor is needed, but the team wants reversible delivery. What should it do?

Domain: Using Coding Agents for Application Development

- A. Use the coding agent to restructure code with tests as the contract
- B. Locate and fix an application-layer vulnerability, then verify the fix
- C. Profile execution paths before optimizing them
- D. Require review of generated diffs before merge

### 53. A specialist returns incomplete findings to the orchestrator. What should the handoff include?

Domain: Developing Custom Agents

- A. Use a graph workflow for branching dependencies
- B. Route a request to the most suitable specialist agent
- C. Transfer control with explicit context and state
- D. Run independent agents concurrently

### 54. A new agent version is faster but more expensive. What should the release gate compare?

Domain: Evaluating and Deploying Agentic Workflows

- A. Compare variants with controlled traffic and shared metrics
- B. Use staged rollout with measurable rollback criteria
- C. Provision capacity for peak concurrency and quotas
- D. Run evaluation on every meaningful change

### 55. A service needs low-latency session documents. What storage fits?

Domain: Evaluating and Deploying Agentic Workflows

- A. Persist sessions in a durable managed store
- B. Use Memorystore for Redis for fast shared ephemeral state
- C. Use Cloud SQL for relational state and transactions
- D. Use Firestore for low-latency document-oriented state

### 56. A canary shows a small but real quality regression. What should happen?

Domain: Evaluating and Deploying Agentic Workflows

- A. Set explicit pass thresholds before evaluating
- B. Use staged rollout with measurable rollback criteria
- C. Use human review for unresolved or high-impact judgment
- D. Compare variants with controlled traffic and shared metrics

### 57. An agent must call three APIs in a dependent order. What should the design specify?

Domain: Developing Custom Agents

- A. Run independent agents concurrently
- B. Run agents in a fixed sequence
- C. Define a narrow tool schema with a clear description
- D. Define an LLM-backed agent with instructions and scoped tools

### 58. A vendor-specific capability is essential but creates lock-in risk. What should the architecture document?

Domain: Developing Custom Agents

- A. Use a proprietary model where supported capability matters
- B. Host the model on infrastructure you control
- C. Use a managed model service under the applicable terms
- D. Use an open model where portability and control matter

### 59. An agent repeatedly retries a failing tool. What should be implemented?

Domain: Evaluating and Deploying Agentic Workflows

- A. Bound iterations and detect reasoning loops
- B. Detect changes in inputs, data, or performance over time
- C. Set timeouts and bounded retries for tool calls
- D. Inspect spans across agent, model, and tool calls

### 60. A release decision needs evidence from representative tasks and rare failures. What should the evaluation include?

Domain: Evaluating and Deploying Agentic Workflows

- A. Set explicit pass thresholds before evaluating
- B. Author an ADK evalset with expected tool use and responses
- C. Include edge cases and adversarial inputs in test sets
- D. Build a representative golden dataset from real tasks

### 61. A knowledge agent serves multiple regions with different product catalogs. What must the retrieval design enforce?

Domain: Building Agents Using Low-Code Tools

- A. Process images, audio, and video through supported ingestion
- B. Use supported enterprise connectors with scoped access
- C. Connect approved enterprise content through Agent Search
- D. Limit connected sources to the approved audience and purpose

### 62. A retail bank wants a low-code agent to open disputes only after identity verification and manager approval. What should the workflow encode?

Domain: Building Agents Using Low-Code Tools

- A. Model behavior explicitly as pages, transition routes, and event handlers
- B. Use scoped OAuth 2.0 tokens for agent-to-tool calls
- C. Write explicit system instructions and reusable prompt templates
- D. Connect approved enterprise content through Agent Search

### 63. An unapproved tool is called in production. What should detect and block it?

Domain: Evaluating and Deploying Agentic Workflows

- A. Use Cloud Logging, Cloud Trace, and Cloud Monitoring
- B. Govern agent traffic through Agent Gateway
- C. Encode organizational policy in enforceable controls
- D. Record agent actions and tool calls in audit logs

### 64. A regulated workload must limit data exfiltration paths. What should be configured?

Domain: Securing and Governing Agentic Workflows

- A. Restrict outbound network access to approved destinations
- B. Use VPC Service Controls to establish a data perimeter
- C. Use customer-managed encryption keys where required
- D. Govern agent traffic through Agent Gateway

### 65. Two agents share an identity, and one is compromised. What is the impact?

Domain: Developing Custom Agents

- A. Give each agent its own managed identity
- B. Grant the minimum permissions required for the task
- C. Use a dedicated service account with least privilege
- D. Constrain access with a principal access boundary policy

### 66. A policy corpus has long sections and frequent duplicate boilerplate. What should the pipeline do?

Domain: Developing Custom Agents

- A. Ground the response in cited retrieved evidence
- B. Rerank retrieved passages before generation
- C. Choose chunk size and overlap for retrieval
- D. Deduplicate near-identical retrieved chunks

### 67. A low-code workflow must handle a user who abandons verification mid-flow. What should the design include?

Domain: Building Agents Using Low-Code Tools

- A. Define a safe fallback when the request is unsupported
- B. Write explicit system instructions and reusable prompt templates
- C. Model behavior explicitly as pages, transition routes, and event handlers
- D. Require human approval before a consequential action

### 68. A prompt variant improves satisfaction but increases policy violations. What should guide adoption?

Domain: Building Agents Using Low-Code Tools

- A. Set explicit pass thresholds before evaluating
- B. Define and rehearse a rollback path
- C. Compare variants with controlled traffic and shared metrics
- D. Use Cloud Logging, Cloud Trace, and Cloud Monitoring

### 69. A narrow extraction task has abundant labeled examples and a stable schema. What could improve consistency?

Domain: Developing Custom Agents

- A. Use a large model for complex reasoning or broad language work
- B. Use an open model where portability and control matter
- C. Use a smaller model for a narrow, high-volume task
- D. Use a tuned model where specialized behavior justifies it

### 70. A specialist agent must receive a task from another agent and return results. What should be defined?

Domain: Developing Custom Agents

- A. Publish an Agent Card describing capabilities and endpoints
- B. Use A2A for agent-to-agent interoperability
- C. Govern agent traffic through Agent Gateway
- D. Use MCP for standardized tool and resource access

### 71. A platform wants consistent policy across all deployed agents. Where should it enforce it?

Domain: Developing Custom Agents

- A. Record agent actions and tool calls in audit logs
- B. Register agents and capabilities in Agent Registry
- C. Govern agent traffic through Agent Gateway
- D. Encode organizational policy in enforceable controls

### 72. A high-impact recommendation passes automated metrics. What remains necessary?

Domain: Evaluating and Deploying Agentic Workflows

- A. Use a calibrated model-based autorater for scalable judgment
- B. Evaluate tool-call trajectories, not only final text
- C. Use human review for unresolved or high-impact judgment
- D. Set explicit pass thresholds before evaluating

### 73. A remote agent's advertised capabilities are outdated. What should be updated?

Domain: Developing Custom Agents

- A. Use MCP for standardized tool and resource access
- B. Use A2A for agent-to-agent interoperability
- C. Publish an Agent Card describing capabilities and endpoints
- D. Register agents and capabilities in Agent Registry

### 74. An agent achieves the right outcome through an unsafe tool sequence. What catches it?

Domain: Evaluating and Deploying Agentic Workflows

- A. Measure retrieval relevance and recall separately
- B. Evaluate tool-call trajectories, not only final text
- C. Score response correctness, completeness, and helpfulness
- D. Ground the response in cited retrieved evidence

### 75. A tool must act with the end user's delegated permissions. What should be implemented?

Domain: Developing Custom Agents

- A. Use scoped OAuth 2.0 tokens for agent-to-tool calls
- B. Keep access tokens short-lived and narrowly scoped
- C. Propagate the caller's identity to downstream tools
- D. Grant IAM roles to the agent identity, not to users' credentials

### 76. An agent has broad project access but needs one dataset. What should be applied?

Domain: Securing and Governing Agentic Workflows

- A. Constrain access with a principal access boundary policy
- B. Use VPC Service Controls to establish a data perimeter
- C. Grant IAM roles to the agent identity, not to users' credentials
- D. Grant the minimum permissions required for the task

### 77. Production quality declines after a retrieval index update. What should be checked?

Domain: Evaluating and Deploying Agentic Workflows

- A. Run evaluation on every meaningful change
- B. Detect changes in inputs, data, or performance over time
- C. Use Cloud Logging, Cloud Trace, and Cloud Monitoring
- D. Inspect spans across agent, model, and tool calls

### 78. A model judge favors verbose answers. What should be done?

Domain: Evaluating and Deploying Agentic Workflows

- A. Score response correctness, completeness, and helpfulness
- B. Set explicit pass thresholds before evaluating
- C. Use human review for unresolved or high-impact judgment
- D. Use a calibrated model-based autorater for scalable judgment

### 79. A response contains account numbers that must not be exposed. What should catch them?

Domain: Securing and Governing Agentic Workflows

- A. Redact or de-identify sensitive data before model exposure
- B. Screen prompts and responses with Model Armor
- C. Encode organizational policy in enforceable controls
- D. Inspect and de-identify sensitive data with Sensitive Data Protection

### 80. A support agent must use only the current region's contract templates. What should be enforced?

Domain: Building Agents Using Low-Code Tools

- A. Use supported enterprise connectors with scoped access
- B. Limit connected sources to the approved audience and purpose
- C. Connect approved enterprise content through Agent Search
- D. Process images, audio, and video through supported ingestion

### 81. Experts disagree about the expected behavior for a sensitive case. What should happen?

Domain: Evaluating and Deploying Agentic Workflows

- A. Use a calibrated model-based autorater for scalable judgment
- B. Build a representative golden dataset from real tasks
- C. Use human review for unresolved or high-impact judgment
- D. Set explicit pass thresholds before evaluating

### 82. A low-code agent must separate a quote request from a complaint before acting. What should the design include?

Domain: Building Agents Using Low-Code Tools

- A. Run independent agents concurrently
- B. Write explicit system instructions and reusable prompt templates
- C. Model behavior explicitly as pages, transition routes, and event handlers
- D. Route a request to the most suitable specialist agent

### 83. A coding agent must not read other tenants' repositories. What should be enforced?

Domain: Using Coding Agents for Application Development

- A. Restrict tools, credentials, and network access in the sandbox
- B. Use GKE isolation and policy controls for agent workloads
- C. Run coding agents in an isolated, permission-limited environment
- D. Use Cloud Workstations for managed developer environments

### 84. Answers are accurate but cite the wrong sections. What should improve?

Domain: Evaluating and Deploying Agentic Workflows

- A. Evaluate tool-call trajectories, not only final text
- B. Measure retrieval relevance and recall separately
- C. Ground the response in cited retrieved evidence
- D. Score response correctness, completeness, and helpfulness

### 85. A repository needs a reusable migration procedure available to multiple agents. What should be created?

Domain: Using Coding Agents for Application Development

- A. Provide persistent coding guidance for a coding agent
- B. Bundle related skills, tools, and configuration as a plugin
- C. Run deterministic logic when a lifecycle event fires
- D. Package reusable guidance and assets as a skill

### 86. Queries include exact product codes and semantic descriptions. What retrieval design fits?

Domain: Developing Custom Agents

- A. Use similarity scoring to retrieve candidate passages
- B. Rerank retrieved passages before generation
- C. Choose an embedding model suited to the domain and language
- D. Combine keyword and semantic retrieval

### 87. A refinement agent repeats the same failed action without progress. What should be added?

Domain: Developing Custom Agents

- A. Use a graph workflow for branching dependencies
- B. Run agents in a fixed sequence
- C. Run independent agents concurrently
- D. Repeat work until a defined stop condition is met

### 88. A team wants code-level control over validation between model turns. What should it use?

Domain: Developing Custom Agents

- A. Expose a typed function as a tool
- B. Use callbacks for validation, logging, or guardrails
- C. Enforce a policy check before a consequential action
- D. Build the agent with the Agent Development Kit

### 89. An agent proposes performance improvements without a baseline. What should be required?

Domain: Using Coding Agents for Application Development

- A. Locate and fix an application-layer vulnerability, then verify the fix
- B. Use the coding agent to restructure code with tests as the contract
- C. Require review of generated diffs before merge
- D. Profile execution paths before optimizing them

### 90. A fraud review workflow needs independent checks followed by a decision. What pattern fits?

Domain: Developing Custom Agents

- A. Run independent agents concurrently
- B. Run agents in a fixed sequence
- C. Use a graph workflow for branching dependencies
- D. Route a request to the most suitable specialist agent

### 91. A low-code agent must explain a multi-step eligibility decision consistently. What should be configured?

Domain: Building Agents Using Low-Code Tools

- A. Include representative few-shot examples
- B. Add structured reasoning guidance for multi-step tasks
- C. Store durable user or domain memory in Memory Bank
- D. Write explicit system instructions and reusable prompt templates

### 92. An answer is correct but unsupported by the cited passage. Which quality dimension fails?

Domain: Developing Custom Agents

- A. Measure retrieval relevance and recall separately
- B. Score response correctness, completeness, and helpfulness
- C. Ground the response in cited retrieved evidence
- D. Evaluate tool-call trajectories, not only final text

### 93. An agent calls an external API on a user's behalf. What should secure the call?

Domain: Securing and Governing Agentic Workflows

- A. Use a dedicated service account with least privilege
- B. Grant IAM roles to the agent identity, not to users' credentials
- C. Use scoped OAuth 2.0 tokens for agent-to-tool calls
- D. Keep access tokens short-lived and narrowly scoped

### 94. A coding agent needs a governed interface to an internal artifact repository. What should be built?

Domain: Using Coding Agents for Application Development

- A. Publish an Agent Card describing capabilities and endpoints
- B. Use MCP for standardized tool and resource access
- C. Use A2A for agent-to-agent interoperability
- D. Expose approved capabilities through an MCP server

### 95. A low-code agent must format denial reasons consistently for auditors. What should be configured?

Domain: Building Agents Using Low-Code Tools

- A. Choose an embedding model suited to the domain and language
- B. Write explicit system instructions and reusable prompt templates
- C. Add structured reasoning guidance for multi-step tasks
- D. Include representative few-shot examples

### 96. A retrieval result includes a document the user cannot access. What should have prevented it?

Domain: Developing Custom Agents

- A. Constrain access with a principal access boundary policy
- B. Grant IAM roles to the agent identity, not to users' credentials
- C. Govern agent traffic through Agent Gateway
- D. Filter retrieval by the requesting user's authorization

### 97. An organization wants a standard capability bundle for secure code review. What should it distribute?

Domain: Using Coding Agents for Application Development

- A. Delegate a scoped task to a specialized agent
- B. Bundle related skills, tools, and configuration as a plugin
- C. Package reusable guidance and assets as a skill
- D. Run deterministic logic when a lifecycle event fires

### 98. A claims triage agent must consistently explain denials using approved categories. What should the design use?

Domain: Building Agents Using Low-Code Tools

- A. Choose an embedding model suited to the domain and language
- B. Include representative few-shot examples
- C. Write explicit system instructions and reusable prompt templates
- D. Add structured reasoning guidance for multi-step tasks

### 99. A workflow has a classification step followed by one of four specialist agents. What pattern fits?

Domain: Developing Custom Agents

- A. Use a graph workflow for branching dependencies
- B. Run independent agents concurrently
- C. Run agents in a fixed sequence
- D. Route a request to the most suitable specialist agent

### 100. A low-code agent's rejection rate rises after a template change. What should guide the response?

Domain: Building Agents Using Low-Code Tools

- A. Use Cloud Logging, Cloud Trace, and Cloud Monitoring
- B. Use staged rollout with measurable rollback criteria
- C. Set explicit pass thresholds before evaluating
- D. Run evaluation on every meaningful change

---

## Answer key and explanations

### Question 1 — D

Answer: Deploy to Agent Runtime for managed agent hosting. Cloud Run with externalized session state. Agent Runtime provides managed hosting and agent platform integration. It is not automatically the best fit for every workload. Local study-map skill 4.4 (Runtime Selection), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Stateless services scale and recover more predictably. External state introduces its own availability and security requirements. In this case: Cloud Run with externalized session state.
- **B:** Incorrect for this question. GKE offers flexibility for complex workloads at higher operational cost. Use it when requirements justify that control. In this case: Cloud Run with externalized session state.
- **C:** Incorrect for this question. Cloud Run suits stateless or externally-stateful container services with managed scaling. Design sessions and long tasks accordingly. In this case: Cloud Run with externalized session state.
- **D:** Correct. Agent Runtime provides managed hosting and agent platform integration. It is not automatically the best fit for every workload. In this case: Cloud Run with externalized session state.

### Question 2 — A

Answer: Run coding agents in an isolated, permission-limited environment. In an ephemeral sandbox with restricted egress and no standing credentials. Sandboxing limits filesystem, network, and credential exposure during autonomous work. Isolation reduces blast radius but does not make generated code correct. Local study-map skill 2.3 (Secure Sandboxes), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Sandboxing limits filesystem, network, and credential exposure during autonomous work. Isolation reduces blast radius but does not make generated code correct. In this case: In an ephemeral sandbox with restricted egress and no standing credentials.
- **B:** Incorrect for this question. Managed workstations provide controlled, reproducible development sessions. They should still use least privilege and approved network paths. In this case: In an ephemeral sandbox with restricted egress and no standing credentials.
- **C:** Incorrect for this question. Sandbox policy bounds what autonomous code can reach. It should be tested, not assumed from the existence of a sandbox. In this case: In an ephemeral sandbox with restricted egress and no standing credentials.
- **D:** Incorrect for this question. Cluster-level controls can separate workloads and restrict network or resource access. They must be configured deliberately and tested for escape paths. In this case: In an ephemeral sandbox with restricted egress and no standing credentials.

### Question 3 — A

Answer: Use Cloud Logging, Cloud Trace, and Cloud Monitoring. Traces and cost attribution by step. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. Local study-map skill 4.6 (Monitoring and Optimization), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Correct. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. In this case: Traces and cost attribution by step.
- **B:** Incorrect for this question. Quotas and scaling limits can become the real bottleneck. Plan for bursts and graceful degradation. In this case: Traces and cost attribution by step.
- **C:** Incorrect for this question. Cost attribution supports optimization and budgeting. Per-task cost reveals expensive failure paths. In this case: Traces and cost attribution by step.
- **D:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Traces and cost attribution by step.

### Question 4 — A

Answer: Govern agent traffic through Agent Gateway. Agent Gateway with egress allowlisting and logging. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. Local study-map skill 5.3 (Agent Gateway and Traffic Governance), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Correct. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Agent Gateway with egress allowlisting and logging.
- **B:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Agent Gateway with egress allowlisting and logging.
- **C:** Incorrect for this question. Classification and de-identification reduce unnecessary exposure. De-identification must be validated for the specific data and purpose. In this case: Agent Gateway with egress allowlisting and logging.
- **D:** Incorrect for this question. Egress controls reduce exfiltration and unauthorized tool reach. They should be paired with identity and data controls. In this case: Agent Gateway with egress allowlisting and logging.

### Question 5 — C

Answer: Run evaluation on every meaningful change. Regression tests and a staged rollout against thresholds. Prompts, models, tools, and data can all change behavior. Regression testing catches unintended effects. Local study-map skill 4.3 (Continuous Evaluation and Regression), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. A canary or phased rollout limits exposure while evidence accumulates. Rollback must be practical, not theoretical. In this case: Regression tests and a staged rollout against thresholds.
- **B:** Incorrect for this question. Production traffic reveals distribution and failure patterns that offline sets miss. Sampling and privacy must be designed. In this case: Regression tests and a staged rollout against thresholds.
- **C:** Correct. Prompts, models, tools, and data can all change behavior. Regression testing catches unintended effects. In this case: Regression tests and a staged rollout against thresholds.
- **D:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Regression tests and a staged rollout against thresholds.

### Question 6 — B

Answer: Use human review for unresolved or high-impact judgment. Calibrate or override the judge with human review for that category. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. Local study-map skill 3.6 (Retrieval Authorization and Evidence Quality), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Calibrate or override the judge with human review for that category.
- **B:** Correct. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. In this case: Calibrate or override the judge with human review for that category.
- **C:** Incorrect for this question. Autoraters can score nuanced qualities at scale. They require calibration against human judgments and periodic review. In this case: Calibrate or override the judge with human review for that category.
- **D:** Incorrect for this question. Citations let users check claims against sources. Grounding reduces but does not eliminate hallucination. In this case: Calibrate or override the judge with human review for that category.

### Question 7 — D

Answer: Provision capacity for peak concurrency and quotas. Quota headroom, backpressure, and graceful degradation. Quotas and scaling limits can become the real bottleneck. Plan for bursts and graceful degradation. Local study-map skill 3.11 (Runtime Coordination and Policies), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. User experience depends on retrieval, tool calls, model turns, and approval. Optimize the whole path, not only generation time. In this case: Quota headroom, backpressure, and graceful degradation.
- **B:** Incorrect for this question. A canary or phased rollout limits exposure while evidence accumulates. Rollback must be practical, not theoretical. In this case: Quota headroom, backpressure, and graceful degradation.
- **C:** Incorrect for this question. Cost attribution supports optimization and budgeting. Per-task cost reveals expensive failure paths. In this case: Quota headroom, backpressure, and graceful degradation.
- **D:** Correct. Quotas and scaling limits can become the real bottleneck. Plan for bursts and graceful degradation. In this case: Quota headroom, backpressure, and graceful degradation.

### Question 8 — A

Answer: Run deterministic logic when a lifecycle event fires. A deterministic pre-commit secret scan that blocks the commit. Hooks can enforce checks, logging, or formatting at defined points. They are useful precisely because they do not depend on model discretion. Local study-map skill 2.2 (Customization Primitives), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Hooks can enforce checks, logging, or formatting at defined points. They are useful precisely because they do not depend on model discretion. In this case: A deterministic pre-commit secret scan that blocks the commit.
- **B:** Incorrect for this question. A skill can carry instructions, examples, and supporting files for a recurring task. It guides behavior but does not itself enforce permissions. In this case: A deterministic pre-commit secret scan that blocks the commit.
- **C:** Incorrect for this question. Rules communicate conventions and constraints for generated changes. They are guidance; merge controls and tests remain the enforcement boundary. In this case: A deterministic pre-commit secret scan that blocks the commit.
- **D:** Incorrect for this question. Plugins make a capability set reusable across projects. Bundling does not remove the need to review each included permission and dependency. In this case: A deterministic pre-commit secret scan that blocks the commit.

### Question 9 — D

Answer: Restrict outbound network access to approved destinations. Egress restrictions plus destination authorization prevent data leaving through an unapproved path. Egress controls reduce exfiltration and unauthorized tool reach. They should be paired with identity and data controls. Local study-map skill 5.6 (Secure Data Access and Identity Propagation), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Minimization reduces the impact of leakage and over-retention. Verify that redaction survives the whole pipeline. In this case: Egress restrictions plus destination authorization prevent data leaving through an unapproved path.
- **B:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Egress restrictions plus destination authorization prevent data leaving through an unapproved path.
- **C:** Incorrect for this question. CMEK supports key-control and compliance requirements. Key lifecycle and break-glass procedures need operational ownership. In this case: Egress restrictions plus destination authorization prevent data leaving through an unapproved path.
- **D:** Correct. Egress controls reduce exfiltration and unauthorized tool reach. They should be paired with identity and data controls. In this case: Egress restrictions plus destination authorization prevent data leaving through an unapproved path.

### Question 10 — D

Answer: Process images, audio, and video through supported ingestion. Reliable transcription and segmentation with preserved timestamps. Multimodal pipelines can extract usable signals for an agentic workflow. Quality depends on transcription, frame selection, and downstream validation. Local study-map skill 1.3 (Enterprise Data Connection), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Gemini Enterprise overview: https://cloud.google.com/gemini-enterprise

- **A:** Incorrect for this question. Embedding choice affects retrieval quality and must be evaluated on real queries. A generic model may miss domain vocabulary. In this case: Reliable transcription and segmentation with preserved timestamps.
- **B:** Incorrect for this question. Chunking affects recall, precision, and context usage. Boundaries should follow document structure and be tested against real questions. In this case: Reliable transcription and segmentation with preserved timestamps.
- **C:** Incorrect for this question. A reranker can improve precision after broad recall. It adds latency and still needs evaluation. In this case: Reliable transcription and segmentation with preserved timestamps.
- **D:** Correct. Multimodal pipelines can extract usable signals for an agentic workflow. Quality depends on transcription, frame selection, and downstream validation. In this case: Reliable transcription and segmentation with preserved timestamps.

### Question 11 — A

Answer: Treat retrieved and user-supplied content as untrusted. Treat the content as untrusted and refuse; credentials must never be in prompt context. Embedded instructions must not gain authority over tools or data. Isolation, allowlists, and human approval reduce injection impact. Local study-map skill 5.6 (Secure Data Access and Identity Propagation), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Correct. Embedded instructions must not gain authority over tools or data. Isolation, allowlists, and human approval reduce injection impact. In this case: Treat the content as untrusted and refuse; credentials must never be in prompt context.
- **B:** Incorrect for this question. Minimization reduces the impact of leakage and over-retention. Verify that redaction survives the whole pipeline. In this case: Treat the content as untrusted and refuse; credentials must never be in prompt context.
- **C:** Incorrect for this question. Managed secret storage supports rotation and access control. A prompt instruction is not a secret-protection mechanism. In this case: Treat the content as untrusted and refuse; credentials must never be in prompt context.
- **D:** Incorrect for this question. Data use should match the disclosed purpose and applicable policy. Technical access does not create permission. In this case: Treat the content as untrusted and refuse; credentials must never be in prompt context.

### Question 12 — A

Answer: Run deterministic logic when a lifecycle event fires. A required hook or CI gate that cannot be bypassed by the agent. Hooks can enforce checks, logging, or formatting at defined points. They are useful precisely because they do not depend on model discretion. Local study-map skill 2.2 (Customization Primitives), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Hooks can enforce checks, logging, or formatting at defined points. They are useful precisely because they do not depend on model discretion. In this case: A required hook or CI gate that cannot be bypassed by the agent.
- **B:** Incorrect for this question. Rules communicate conventions and constraints for generated changes. They are guidance; merge controls and tests remain the enforcement boundary. In this case: A required hook or CI gate that cannot be bypassed by the agent.
- **C:** Incorrect for this question. Plugins make a capability set reusable across projects. Bundling does not remove the need to review each included permission and dependency. In this case: A required hook or CI gate that cannot be bypassed by the agent.
- **D:** Incorrect for this question. A skill can carry instructions, examples, and supporting files for a recurring task. It guides behavior but does not itself enforce permissions. In this case: A required hook or CI gate that cannot be bypassed by the agent.

### Question 13 — C

Answer: Locate and fix an application-layer vulnerability, then verify the fix. A narrowed, tested patch with unrelated changes removed. Security patching needs reproduction, a scoped change, and validation. The agent can assist but cannot grant itself assurance. Local study-map skill 2.4 (Code Modernization and Vulnerability Remediation), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Human or automated review checks scope, security, and correctness before change lands. The coding agent's confidence is not review. In this case: A narrowed, tested patch with unrelated changes removed.
- **B:** Incorrect for this question. Refactoring should preserve observable behavior and be verified by tests and review. A plausible diff is not proof of equivalence. In this case: A narrowed, tested patch with unrelated changes removed.
- **C:** Correct. Security patching needs reproduction, a scoped change, and validation. The agent can assist but cannot grant itself assurance. In this case: A narrowed, tested patch with unrelated changes removed.
- **D:** Incorrect for this question. Optimization should follow measured bottlenecks and correct behavior. Rewriting for speed without evidence can add defects. In this case: A narrowed, tested patch with unrelated changes removed.

### Question 14 — A

Answer: Require review of generated diffs before merge. Attributable review and approval records linked to the diff. Human or automated review checks scope, security, and correctness before change lands. The coding agent's confidence is not review. Local study-map skill 2.5 (Coding Agent Operations and Oversight), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Human or automated review checks scope, security, and correctness before change lands. The coding agent's confidence is not review. In this case: Attributable review and approval records linked to the diff.
- **B:** Incorrect for this question. Fleet tooling can support building, scaling, and inspecting agents. Access to fleet operations should itself be least-privilege and audited. In this case: Attributable review and approval records linked to the diff.
- **C:** Incorrect for this question. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: Attributable review and approval records linked to the diff.
- **D:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Attributable review and approval records linked to the diff.

### Question 15 — B

Answer: Require human approval before a consequential action. A pre-action human approval with transaction context. Human-in-the-loop review is appropriate when impact or uncertainty is high. Approval must occur before the effect and with enough context to decide. Local study-map skill 5.5 (Guardrails and Human-in-the-Loop), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Impact review assigns responsibility for consequential outcomes. It should be timely and informed by evidence. In this case: A pre-action human approval with transaction context.
- **B:** Correct. Human-in-the-loop review is appropriate when impact or uncertainty is high. Approval must occur before the effect and with enough context to decide. In this case: A pre-action human approval with transaction context.
- **C:** Incorrect for this question. Approval should identify who approved what and under which evidence. A vague acknowledgment is not authorization. In this case: A pre-action human approval with transaction context.
- **D:** Incorrect for this question. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. In this case: A pre-action human approval with transaction context.

### Question 16 — B

Answer: Use a dedicated service account with least privilege. Dedicated agent identities with complete audit records. A dedicated identity separates the agent from human accounts and limits blast radius. Roles still need review and periodic reduction. Local study-map skill 5.1 (Authentication and Secure Tool Execution), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Distinct identity makes access attributable and auditable. Sharing a human or broad service identity weakens least privilege. In this case: Dedicated agent identities with complete audit records.
- **B:** Correct. A dedicated identity separates the agent from human accounts and limits blast radius. Roles still need review and periodic reduction. In this case: Dedicated agent identities with complete audit records.
- **C:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Dedicated agent identities with complete audit records.
- **D:** Incorrect for this question. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: Dedicated agent identities with complete audit records.

### Question 17 — C

Answer: Govern agent traffic through Agent Gateway. Deny and log the attempt, then remediate the deployment. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. Local study-map skill 5.3 (Agent Gateway and Traffic Governance), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Deny and log the attempt, then remediate the deployment.
- **B:** Incorrect for this question. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: Deny and log the attempt, then remediate the deployment.
- **C:** Correct. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Deny and log the attempt, then remediate the deployment.
- **D:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Deny and log the attempt, then remediate the deployment.

### Question 18 — D

Answer: Return structured tool errors that guide recovery. Check for prior success before retrying, using idempotency or status lookup. Actionable errors let the agent correct arguments or escalate. Silent failure or fabricated success is unsafe. Local study-map skill 3.2 (ADK Agent Construction), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Timeouts protect the workflow from stalled dependencies. Retries must avoid duplicating consequential actions. In this case: Check for prior success before retrying, using idempotency or status lookup.
- **B:** Incorrect for this question. A maximum step or time budget prevents runaway cost and repeated actions. Progress checks should trigger escalation. In this case: Check for prior success before retrying, using idempotency or status lookup.
- **C:** Incorrect for this question. Traces localize latency and failures in multi-step workflows. They are essential for debugging non-deterministic behavior. In this case: Check for prior success before retrying, using idempotency or status lookup.
- **D:** Correct. Actionable errors let the agent correct arguments or escalate. Silent failure or fabricated success is unsafe. In this case: Check for prior success before retrying, using idempotency or status lookup.

### Question 19 — B

Answer: Restrict tools, credentials, and network access in the sandbox. Egress allowlisting to approved package sources. Sandbox policy bounds what autonomous code can reach. It should be tested, not assumed from the existence of a sandbox. Local study-map skill 2.3 (Secure Sandboxes), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Egress controls reduce exfiltration and unauthorized tool reach. They should be paired with identity and data controls. In this case: Egress allowlisting to approved package sources.
- **B:** Correct. Sandbox policy bounds what autonomous code can reach. It should be tested, not assumed from the existence of a sandbox. In this case: Egress allowlisting to approved package sources.
- **C:** Incorrect for this question. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: Egress allowlisting to approved package sources.
- **D:** Incorrect for this question. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: Egress allowlisting to approved package sources.

### Question 20 — A

Answer: Use RAG Engine for managed retrieval pipeline components. RAG Engine for supported managed pipeline components. A managed RAG service can reduce plumbing work. Corpus design, access, and evaluation remain yours. Local study-map skill 3.5 (Vector Search and Managed Retrieval), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. A managed RAG service can reduce plumbing work. Corpus design, access, and evaluation remain yours. In this case: RAG Engine for supported managed pipeline components.
- **B:** Incorrect for this question. A vector index supports similarity retrieval at scale. Index configuration, updates, and access must be operated deliberately. In this case: RAG Engine for supported managed pipeline components.
- **C:** Incorrect for this question. Managed retrieval services can serve agent queries at scale. Validate relevance, authorization, and latency for the workload. In this case: RAG Engine for supported managed pipeline components.
- **D:** Incorrect for this question. A supported enterprise search layer can ground responses in indexed organizational material under configured access. Indexing does not make every document accurate or authorized for every user. In this case: RAG Engine for supported managed pipeline components.

### Question 21 — B

Answer: Grant the minimum permissions required for the task. Temporary access needs a time-bound expiry, review, and confirmed removal afterward. Narrow roles and scopes reduce blast radius. Review permissions as the workflow evolves. Local study-map skill 5.2 (Principal Access Boundaries), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: Temporary access needs a time-bound expiry, review, and confirmed removal afterward.
- **B:** Correct. Narrow roles and scopes reduce blast radius. Review permissions as the workflow evolves. In this case: Temporary access needs a time-bound expiry, review, and confirmed removal afterward.
- **C:** Incorrect for this question. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: Temporary access needs a time-bound expiry, review, and confirmed removal afterward.
- **D:** Incorrect for this question. A dedicated identity separates the agent from human accounts and limits blast radius. Roles still need review and periodic reduction. In this case: Temporary access needs a time-bound expiry, review, and confirmed removal afterward.

### Question 22 — B

Answer: Give each agent its own managed identity. A dedicated identity with a narrow role and an appropriate boundary. Distinct identity makes access attributable and auditable. Sharing a human or broad service identity weakens least privilege. Local study-map skill 3.7 (Agent Identity and Permissions), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: A dedicated identity with a narrow role and an appropriate boundary.
- **B:** Correct. Distinct identity makes access attributable and auditable. Sharing a human or broad service identity weakens least privilege. In this case: A dedicated identity with a narrow role and an appropriate boundary.
- **C:** Incorrect for this question. Narrow roles and scopes reduce blast radius. Review permissions as the workflow evolves. In this case: A dedicated identity with a narrow role and an appropriate boundary.
- **D:** Incorrect for this question. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: A dedicated identity with a narrow role and an appropriate boundary.

### Question 23 — A

Answer: Apply purpose limitation and consent to personal data. Inspection, correction, and deletion across memory stores. Data use should match the disclosed purpose and applicable policy. Technical access does not create permission. Local study-map skill 5.6 (Secure Data Access and Identity Propagation), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Correct. Data use should match the disclosed purpose and applicable policy. Technical access does not create permission. In this case: Inspection, correction, and deletion across memory stores.
- **B:** Incorrect for this question. Memory policy prevents unnecessary persistence of sensitive or obsolete facts. It also supports correction and deletion. In this case: Inspection, correction, and deletion across memory stores.
- **C:** Incorrect for this question. Minimization reduces the impact of leakage and over-retention. Verify that redaction survives the whole pipeline. In this case: Inspection, correction, and deletion across memory stores.
- **D:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Inspection, correction, and deletion across memory stores.

### Question 24 — C

Answer: Define a safe fallback when the request is unsupported. State the evidence gap and route to an approved human channel. A low-code agent needs an explicit path for uncertainty, missing evidence, or out-of-scope requests. Improvisation should not silently become a commitment. Local study-map skill 1.1 (State-Based Workflow Design), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Gemini Enterprise overview: https://cloud.google.com/gemini-enterprise

- **A:** Incorrect for this question. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: State the evidence gap and route to an approved human channel.
- **B:** Incorrect for this question. Model Armor can help detect prompt injection, unsafe content, and sensitive data patterns. It is a layered control, not a complete trust boundary. In this case: State the evidence gap and route to an approved human channel.
- **C:** Correct. A low-code agent needs an explicit path for uncertainty, missing evidence, or out-of-scope requests. Improvisation should not silently become a commitment. In this case: State the evidence gap and route to an approved human channel.
- **D:** Incorrect for this question. State-based low-code workflows make allowed transitions and triggers visible. They are a design control, not a substitute for access checks or testing. In this case: State the evidence gap and route to an approved human channel.

### Question 25 — B

Answer: Register agents and capabilities in Agent Registry. Registry metadata for agents and servers with reviewed ownership. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. Local study-map skill 3.8 (Registry and Capability Integration), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Plugins make a capability set reusable across projects. Bundling does not remove the need to review each included permission and dependency. In this case: Registry metadata for agents and servers with reviewed ownership.
- **B:** Correct. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: Registry metadata for agents and servers with reviewed ownership.
- **C:** Incorrect for this question. MCP provides a common interface between agents and capability servers. Server trust, scopes, and validation remain your responsibility. In this case: Registry metadata for agents and servers with reviewed ownership.
- **D:** Incorrect for this question. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. In this case: Registry metadata for agents and servers with reviewed ownership.

### Question 26 — B

Answer: Delegate a scoped task to a specialized agent. Report findings to the orchestrator and block merge until resolved. A subagent can isolate context and permissions for a focused job. Clear ownership, tool scope, and returned evidence are still required. Local study-map skill 2.5 (Coding Agent Operations and Oversight), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Parallel branches reduce wall-clock time when work is truly independent. Shared state and reconciliation still require design. In this case: Report findings to the orchestrator and block merge until resolved.
- **B:** Correct. A subagent can isolate context and permissions for a focused job. Clear ownership, tool scope, and returned evidence are still required. In this case: Report findings to the orchestrator and block merge until resolved.
- **C:** Incorrect for this question. Routing can match task type, language, or risk to a capable handler. Misrouting needs an observable fallback. In this case: Report findings to the orchestrator and block merge until resolved.
- **D:** Incorrect for this question. A handoff should carry the goal, verified facts, permissions, and open questions. Implicit context is easily lost between agents. In this case: Report findings to the orchestrator and block merge until resolved.

### Question 27 — A

Answer: Expose approved capabilities through an MCP server. Two narrowly scoped MCP tools with separate permissions. An MCP server provides a governed interface to tools, resources, or prompts. The server must enforce its own authorization and input validation. Local study-map skill 2.1 (Coding Agent Configuration and Tooling), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. An MCP server provides a governed interface to tools, resources, or prompts. The server must enforce its own authorization and input validation. In this case: Two narrowly scoped MCP tools with separate permissions.
- **B:** Incorrect for this question. MCP provides a common interface between agents and capability servers. Server trust, scopes, and validation remain your responsibility. In this case: Two narrowly scoped MCP tools with separate permissions.
- **C:** Incorrect for this question. Plugins make a capability set reusable across projects. Bundling does not remove the need to review each included permission and dependency. In this case: Two narrowly scoped MCP tools with separate permissions.
- **D:** Incorrect for this question. A skill can carry instructions, examples, and supporting files for a recurring task. It guides behavior but does not itself enforce permissions. In this case: Two narrowly scoped MCP tools with separate permissions.

### Question 28 — C

Answer: Use a smaller model for a narrow, high-volume task. A smaller model evaluated on the constrained task. A small model can reduce latency and cost when the task is constrained and evaluated. It is not automatically adequate for harder inputs. Local study-map skill 3.1 (Model Selection and Tradeoffs), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. User experience depends on retrieval, tool calls, model turns, and approval. Optimize the whole path, not only generation time. In this case: A smaller model evaluated on the constrained task.
- **B:** Incorrect for this question. Managed services reduce operational burden and inherit provider controls. Verify data handling, quotas, regions, and supported features. In this case: A smaller model evaluated on the constrained task.
- **C:** Correct. A small model can reduce latency and cost when the task is constrained and evaluated. It is not automatically adequate for harder inputs. In this case: A smaller model evaluated on the constrained task.
- **D:** Incorrect for this question. Self-hosting can address control, residency, or customization needs at operational cost. It shifts patching, scaling, and monitoring to your team. In this case: A smaller model evaluated on the constrained task.

### Question 29 — B

Answer: Use staged rollout with measurable rollback criteria. Regression evaluation, staged rollout, and audit evidence of the change. A canary or phased rollout limits exposure while evidence accumulates. Rollback must be practical, not theoretical. Local study-map skill 1.4 (Low-Code Change and Release Control), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Gemini Enterprise overview: https://cloud.google.com/gemini-enterprise

- **A:** Incorrect for this question. Prompts, models, tools, and data can all change behavior. Regression testing catches unintended effects. In this case: Regression evaluation, staged rollout, and audit evidence of the change.
- **B:** Correct. A canary or phased rollout limits exposure while evidence accumulates. Rollback must be practical, not theoretical. In this case: Regression evaluation, staged rollout, and audit evidence of the change.
- **C:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Regression evaluation, staged rollout, and audit evidence of the change.
- **D:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Regression evaluation, staged rollout, and audit evidence of the change.

### Question 30 — C

Answer: Deploy to Agent Runtime for managed agent hosting. Agent Runtime with the required platform services. Agent Runtime provides managed hosting and agent platform integration. It is not automatically the best fit for every workload. Local study-map skill 3.11 (Runtime Coordination and Policies), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. GKE offers flexibility for complex workloads at higher operational cost. Use it when requirements justify that control. In this case: Agent Runtime with the required platform services.
- **B:** Incorrect for this question. Cloud Run suits stateless or externally-stateful container services with managed scaling. Design sessions and long tasks accordingly. In this case: Agent Runtime with the required platform services.
- **C:** Correct. Agent Runtime provides managed hosting and agent platform integration. It is not automatically the best fit for every workload. In this case: Agent Runtime with the required platform services.
- **D:** Incorrect for this question. Stateless services scale and recover more predictably. External state introduces its own availability and security requirements. In this case: Agent Runtime with the required platform services.

### Question 31 — B

Answer: Return structured tool errors that guide recovery. Classify the error and escalate instead of retrying. Actionable errors let the agent correct arguments or escalate. Silent failure or fabricated success is unsafe. Local study-map skill 4.5 (Troubleshooting Agent Failures), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Classify the error and escalate instead of retrying.
- **B:** Correct. Actionable errors let the agent correct arguments or escalate. Silent failure or fabricated success is unsafe. In this case: Classify the error and escalate instead of retrying.
- **C:** Incorrect for this question. A maximum step or time budget prevents runaway cost and repeated actions. Progress checks should trigger escalation. In this case: Classify the error and escalate instead of retrying.
- **D:** Incorrect for this question. Timeouts protect the workflow from stalled dependencies. Retries must avoid duplicating consequential actions. In this case: Classify the error and escalate instead of retrying.

### Question 32 — C

Answer: Screen prompts and responses with Model Armor. Input screening, output inspection, least privilege, and tool authorization. Model Armor can help detect prompt injection, unsafe content, and sensitive data patterns. It is a layered control, not a complete trust boundary. Local study-map skill 5.4 (Registry and Policy Enforcement), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: Input screening, output inspection, least privilege, and tool authorization.
- **B:** Incorrect for this question. Classification and de-identification reduce unnecessary exposure. De-identification must be validated for the specific data and purpose. In this case: Input screening, output inspection, least privilege, and tool authorization.
- **C:** Correct. Model Armor can help detect prompt injection, unsafe content, and sensitive data patterns. It is a layered control, not a complete trust boundary. In this case: Input screening, output inspection, least privilege, and tool authorization.
- **D:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Input screening, output inspection, least privilege, and tool authorization.

### Question 33 — A

Answer: Author an ADK evalset with expected tool use and responses. A regression case that reproduces the failure. An evalset gives repeatable evidence for agent behavior. It must be maintained as the workflow changes. Local study-map skill 4.1 (Evaluation Test Sets), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Correct. An evalset gives repeatable evidence for agent behavior. It must be maintained as the workflow changes. In this case: A regression case that reproduces the failure.
- **B:** Incorrect for this question. Prompts, models, tools, and data can all change behavior. Regression testing catches unintended effects. In this case: A regression case that reproduces the failure.
- **C:** Incorrect for this question. A golden set anchors evaluation in expected behavior and evidence. It should cover normal, rare, and risky cases. In this case: A regression case that reproduces the failure.
- **D:** Incorrect for this question. Boundary and hostile inputs reveal failures that happy-path tests miss. Include prompt injection and missing-data cases. In this case: A regression case that reproduces the failure.

### Question 34 — D

Answer: Expose approved capabilities through an MCP server. Scoped MCP tools and a sandbox configuration limited to those tools. An MCP server provides a governed interface to tools, resources, or prompts. The server must enforce its own authorization and input validation. Local study-map skill 2.1 (Coding Agent Configuration and Tooling), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Fleet tooling can support building, scaling, and inspecting agents. Access to fleet operations should itself be least-privilege and audited. In this case: Scoped MCP tools and a sandbox configuration limited to those tools.
- **B:** Incorrect for this question. Antigravity provides CLI, SDK, and app surfaces for coding agents. Capabilities and controls vary by surface and must be configured explicitly. In this case: Scoped MCP tools and a sandbox configuration limited to those tools.
- **C:** Incorrect for this question. A skill can carry instructions, examples, and supporting files for a recurring task. It guides behavior but does not itself enforce permissions. In this case: Scoped MCP tools and a sandbox configuration limited to those tools.
- **D:** Correct. An MCP server provides a governed interface to tools, resources, or prompts. The server must enforce its own authorization and input validation. In this case: Scoped MCP tools and a sandbox configuration limited to those tools.

### Question 35 — D

Answer: Enforce a policy check before a consequential action. Bind approval to one specific action and expire it. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. Local study-map skill 5.5 (Guardrails and Human-in-the-Loop), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Human-in-the-loop review is appropriate when impact or uncertainty is high. Approval must occur before the effect and with enough context to decide. In this case: Bind approval to one specific action and expire it.
- **B:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Bind approval to one specific action and expire it.
- **C:** Incorrect for this question. Approval should identify who approved what and under which evidence. A vague acknowledgment is not authorization. In this case: Bind approval to one specific action and expire it.
- **D:** Correct. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. In this case: Bind approval to one specific action and expire it.

### Question 36 — C

Answer: Propagate the caller's identity to downstream tools. Verified user identity with scoped delegated authority. Downstream authorization needs the actual principal, not a generic agent identity. Delegation must be explicit and scoped. Local study-map skill 5.1 (Authentication and Secure Tool Execution), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Short-lived, scoped tokens limit what a tool call can do. Token handling and refresh must avoid broad standing access. In this case: Verified user identity with scoped delegated authority.
- **B:** Incorrect for this question. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: Verified user identity with scoped delegated authority.
- **C:** Correct. Downstream authorization needs the actual principal, not a generic agent identity. Delegation must be explicit and scoped. In this case: Verified user identity with scoped delegated authority.
- **D:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Verified user identity with scoped delegated authority.

### Question 37 — B

Answer: Expose approved capabilities through an MCP server. Security review of authentication, authorization, validation, and logging. An MCP server provides a governed interface to tools, resources, or prompts. The server must enforce its own authorization and input validation. Local study-map skill 3.8 (Registry and Capability Integration), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: Security review of authentication, authorization, validation, and logging.
- **B:** Correct. An MCP server provides a governed interface to tools, resources, or prompts. The server must enforce its own authorization and input validation. In this case: Security review of authentication, authorization, validation, and logging.
- **C:** Incorrect for this question. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: Security review of authentication, authorization, validation, and logging.
- **D:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Security review of authentication, authorization, validation, and logging.

### Question 38 — D

Answer: Use GKE isolation and policy controls for agent workloads. GKE with dedicated namespaces or clusters and enforced policies. Cluster-level controls can separate workloads and restrict network or resource access. They must be configured deliberately and tested for escape paths. Local study-map skill 2.3 (Secure Sandboxes), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Sandboxing limits filesystem, network, and credential exposure during autonomous work. Isolation reduces blast radius but does not make generated code correct. In this case: GKE with dedicated namespaces or clusters and enforced policies.
- **B:** Incorrect for this question. Managed workstations provide controlled, reproducible development sessions. They should still use least privilege and approved network paths. In this case: GKE with dedicated namespaces or clusters and enforced policies.
- **C:** Incorrect for this question. Cloud Run suits stateless or externally-stateful container services with managed scaling. Design sessions and long tasks accordingly. In this case: GKE with dedicated namespaces or clusters and enforced policies.
- **D:** Correct. Cluster-level controls can separate workloads and restrict network or resource access. They must be configured deliberately and tested for escape paths. In this case: GKE with dedicated namespaces or clusters and enforced policies.

### Question 39 — B

Answer: Filter retrieval by the requesting user's authorization. Tenant and authorization filtering before context assembly. Access checks must occur before content enters the model context. Relevance never overrides permission. Local study-map skill 3.5 (Vector Search and Managed Retrieval), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A connector's technical reach should not exceed the business authorization for the workflow. Broader access increases both risk and irrelevant retrieval. In this case: Tenant and authorization filtering before context assembly.
- **B:** Correct. Access checks must occur before content enters the model context. Relevance never overrides permission. In this case: Tenant and authorization filtering before context assembly.
- **C:** Incorrect for this question. Metadata such as tenant, date, or classification can enforce scope and freshness. Metadata must itself be trustworthy. In this case: Tenant and authorization filtering before context assembly.
- **D:** Incorrect for this question. A vector index supports similarity retrieval at scale. Index configuration, updates, and access must be operated deliberately. In this case: Tenant and authorization filtering before context assembly.

### Question 40 — B

Answer: Define a narrow tool schema with a clear description. Constrained operations with validated parameters and authorization. A precise contract helps the model choose and supply arguments correctly. Broad or ambiguous tools invite unsafe calls. Local study-map skill 3.2 (ADK Agent Construction), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Tools let the agent act through defined interfaces. Each tool should validate inputs and enforce authorization server-side. In this case: Constrained operations with validated parameters and authorization.
- **B:** Correct. A precise contract helps the model choose and supply arguments correctly. Broad or ambiguous tools invite unsafe calls. In this case: Constrained operations with validated parameters and authorization.
- **C:** Incorrect for this question. Hooks can enforce checks, logging, or formatting at defined points. They are useful precisely because they do not depend on model discretion. In this case: Constrained operations with validated parameters and authorization.
- **D:** Incorrect for this question. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. In this case: Constrained operations with validated parameters and authorization.

### Question 41 — B

Answer: Persist conversation and task state in a session. An external session store with a defined state schema. Sessions support continuity across turns. Scope, retention, and isolation must match the use case. Local study-map skill 3.3 (Sessions, State, and Memory), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. State should have clear ownership, lifetime, and access rules. Accumulating everything creates stale or sensitive context. In this case: An external session store with a defined state schema.
- **B:** Correct. Sessions support continuity across turns. Scope, retention, and isolation must match the use case. In this case: An external session store with a defined state schema.
- **C:** Incorrect for this question. Stateless services scale and recover more predictably. External state introduces its own availability and security requirements. In this case: An external session store with a defined state schema.
- **D:** Incorrect for this question. Durable session storage supports continuity and recovery. Retention and isolation rules still apply. In this case: An external session store with a defined state schema.

### Question 42 — A

Answer: Use a large model for complex reasoning or broad language work. A capable model with measured accuracy and cost per accepted extraction. Large models can handle ambiguity and multi-step reasoning but cost more. Selection should follow measured task requirements. Local study-map skill 3.1 (Model Selection and Tradeoffs), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Large models can handle ambiguity and multi-step reasoning but cost more. Selection should follow measured task requirements. In this case: A capable model with measured accuracy and cost per accepted extraction.
- **B:** Incorrect for this question. Model Garden provides access to multiple model options and deployment paths. Availability and terms vary by model and region. In this case: A capable model with measured accuracy and cost per accepted extraction.
- **C:** Incorrect for this question. Include retries, tool calls, review, and failed attempts rather than only token price. Cost per accepted outcome reflects the workflow. In this case: A capable model with measured accuracy and cost per accepted extraction.
- **D:** Incorrect for this question. A small model can reduce latency and cost when the task is constrained and evaluated. It is not automatically adequate for harder inputs. In this case: A capable model with measured accuracy and cost per accepted extraction.

### Question 43 — B

Answer: Use GKE when you need cluster-level control and custom orchestration. GKE with dedicated infrastructure and policy. GKE offers flexibility for complex workloads at higher operational cost. Use it when requirements justify that control. Local study-map skill 4.4 (Runtime Selection), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Agent Runtime provides managed hosting and agent platform integration. It is not automatically the best fit for every workload. In this case: GKE with dedicated infrastructure and policy.
- **B:** Correct. GKE offers flexibility for complex workloads at higher operational cost. Use it when requirements justify that control. In this case: GKE with dedicated infrastructure and policy.
- **C:** Incorrect for this question. Cloud Run suits stateless or externally-stateful container services with managed scaling. Design sessions and long tasks accordingly. In this case: GKE with dedicated infrastructure and policy.
- **D:** Incorrect for this question. Managed workstations provide controlled, reproducible development sessions. They should still use least privilege and approved network paths. In this case: GKE with dedicated infrastructure and policy.

### Question 44 — C

Answer: Provision capacity for peak concurrency and quotas. Minimum instances and warm capacity against cost. Quotas and scaling limits can become the real bottleneck. Plan for bursts and graceful degradation. Local study-map skill 4.6 (Monitoring and Optimization), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Cloud Run suits stateless or externally-stateful container services with managed scaling. Design sessions and long tasks accordingly. In this case: Minimum instances and warm capacity against cost.
- **B:** Incorrect for this question. User experience depends on retrieval, tool calls, model turns, and approval. Optimize the whole path, not only generation time. In this case: Minimum instances and warm capacity against cost.
- **C:** Correct. Quotas and scaling limits can become the real bottleneck. Plan for bursts and graceful degradation. In this case: Minimum instances and warm capacity against cost.
- **D:** Incorrect for this question. Cost attribution supports optimization and budgeting. Per-task cost reveals expensive failure paths. In this case: Minimum instances and warm capacity against cost.

### Question 45 — D

Answer: Monitor production behavior with online evaluation. Minimization, access control, and retention rules. Production traffic reveals distribution and failure patterns that offline sets miss. Sampling and privacy must be designed. Local study-map skill 4.3 (Continuous Evaluation and Regression), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Minimization, access control, and retention rules.
- **B:** Incorrect for this question. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. In this case: Minimization, access control, and retention rules.
- **C:** Incorrect for this question. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. In this case: Minimization, access control, and retention rules.
- **D:** Correct. Production traffic reveals distribution and failure patterns that offline sets miss. Sampling and privacy must be designed. In this case: Minimization, access control, and retention rules.

### Question 46 — A

Answer: Set explicit pass thresholds before evaluating. Unversioned test suites produce irreproducible results and stale expectations over time. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. Local study-map skill 4.1 (Evaluation Test Sets), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Correct. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Unversioned test suites produce irreproducible results and stale expectations over time.
- **B:** Incorrect for this question. A golden set anchors evaluation in expected behavior and evidence. It should cover normal, rare, and risky cases. In this case: Unversioned test suites produce irreproducible results and stale expectations over time.
- **C:** Incorrect for this question. An evalset gives repeatable evidence for agent behavior. It must be maintained as the workflow changes. In this case: Unversioned test suites produce irreproducible results and stale expectations over time.
- **D:** Incorrect for this question. Quotas and scaling limits can become the real bottleneck. Plan for bursts and graceful degradation. In this case: Unversioned test suites produce irreproducible results and stale expectations over time.

### Question 47 — A

Answer: Detect changes in inputs, data, or performance over time. Representative evaluation data and segment monitoring. Models, sources, and user behavior change. Monitoring detects when evaluation assumptions no longer hold. Local study-map skill 4.3 (Continuous Evaluation and Regression), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Correct. Models, sources, and user behavior change. Monitoring detects when evaluation assumptions no longer hold. In this case: Representative evaluation data and segment monitoring.
- **B:** Incorrect for this question. Prompts, models, tools, and data can all change behavior. Regression testing catches unintended effects. In this case: Representative evaluation data and segment monitoring.
- **C:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Representative evaluation data and segment monitoring.
- **D:** Incorrect for this question. An evalset gives repeatable evidence for agent behavior. It must be maintained as the workflow changes. In this case: Representative evaluation data and segment monitoring.

### Question 48 — D

Answer: Operate and govern deployed agents with Agents CLI. Registry entries, identities, and auditable fleet operations. Fleet tooling can support building, scaling, and inspecting agents. Access to fleet operations should itself be least-privilege and audited. Local study-map skill 2.5 (Coding Agent Operations and Oversight), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Registry entries, identities, and auditable fleet operations.
- **B:** Incorrect for this question. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: Registry entries, identities, and auditable fleet operations.
- **C:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Registry entries, identities, and auditable fleet operations.
- **D:** Correct. Fleet tooling can support building, scaling, and inspecting agents. Access to fleet operations should itself be least-privilege and audited. In this case: Registry entries, identities, and auditable fleet operations.

### Question 49 — B

Answer: Store durable user or domain memory in Memory Bank. Consent, retention limits, and inspection or deletion controls. Long-term memory can personalize and improve continuity. It needs consent, retention, and deletion controls. Local study-map skill 3.3 (Sessions, State, and Memory), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Artifacts keep large content out of the prompt and provide a durable reference. They still require access control and validation. In this case: Consent, retention limits, and inspection or deletion controls.
- **B:** Correct. Long-term memory can personalize and improve continuity. It needs consent, retention, and deletion controls. In this case: Consent, retention limits, and inspection or deletion controls.
- **C:** Incorrect for this question. Memory policy prevents unnecessary persistence of sensitive or obsolete facts. It also supports correction and deletion. In this case: Consent, retention limits, and inspection or deletion controls.
- **D:** Incorrect for this question. Sessions support continuity across turns. Scope, retention, and isolation must match the use case. In this case: Consent, retention limits, and inspection or deletion controls.

### Question 50 — D

Answer: Publish an Agent Card describing capabilities and endpoints. Without an owner or version, behavior drifts and accountability for failures becomes unclear. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. Local study-map skill 3.8 (Registry and Capability Integration), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: Without an owner or version, behavior drifts and accountability for failures becomes unclear.
- **B:** Incorrect for this question. Plugins make a capability set reusable across projects. Bundling does not remove the need to review each included permission and dependency. In this case: Without an owner or version, behavior drifts and accountability for failures becomes unclear.
- **C:** Incorrect for this question. MCP provides a common interface between agents and capability servers. Server trust, scopes, and validation remain your responsibility. In this case: Without an owner or version, behavior drifts and accountability for failures becomes unclear.
- **D:** Correct. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. In this case: Without an owner or version, behavior drifts and accountability for failures becomes unclear.

### Question 51 — D

Answer: Store task-scoped state deliberately. Retention and minimization; not every turn belongs in long-term memory. State should have clear ownership, lifetime, and access rules. Accumulating everything creates stale or sensitive context. Local study-map skill 3.3 (Sessions, State, and Memory), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Artifacts keep large content out of the prompt and provide a durable reference. They still require access control and validation. In this case: Retention and minimization; not every turn belongs in long-term memory.
- **B:** Incorrect for this question. Long-term memory can personalize and improve continuity. It needs consent, retention, and deletion controls. In this case: Retention and minimization; not every turn belongs in long-term memory.
- **C:** Incorrect for this question. Sessions support continuity across turns. Scope, retention, and isolation must match the use case. In this case: Retention and minimization; not every turn belongs in long-term memory.
- **D:** Correct. State should have clear ownership, lifetime, and access rules. Accumulating everything creates stale or sensitive context. In this case: Retention and minimization; not every turn belongs in long-term memory.

### Question 52 — A

Answer: Use the coding agent to restructure code with tests as the contract. Split the work into reviewed, tested, reversible changes. Refactoring should preserve observable behavior and be verified by tests and review. A plausible diff is not proof of equivalence. Local study-map skill 2.4 (Code Modernization and Vulnerability Remediation), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Refactoring should preserve observable behavior and be verified by tests and review. A plausible diff is not proof of equivalence. In this case: Split the work into reviewed, tested, reversible changes.
- **B:** Incorrect for this question. Security patching needs reproduction, a scoped change, and validation. The agent can assist but cannot grant itself assurance. In this case: Split the work into reviewed, tested, reversible changes.
- **C:** Incorrect for this question. Optimization should follow measured bottlenecks and correct behavior. Rewriting for speed without evidence can add defects. In this case: Split the work into reviewed, tested, reversible changes.
- **D:** Incorrect for this question. Human or automated review checks scope, security, and correctness before change lands. The coding agent's confidence is not review. In this case: Split the work into reviewed, tested, reversible changes.

### Question 53 — C

Answer: Transfer control with explicit context and state. Verified findings, unresolved work, and explicit state. A handoff should carry the goal, verified facts, permissions, and open questions. Implicit context is easily lost between agents. Local study-map skill 3.10 (Multi-Agent Workflow Patterns), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Graphs express conditional paths and joins more clearly than a fixed chain. Complexity should be justified by real control flow. In this case: Verified findings, unresolved work, and explicit state.
- **B:** Incorrect for this question. Routing can match task type, language, or risk to a capable handler. Misrouting needs an observable fallback. In this case: Verified findings, unresolved work, and explicit state.
- **C:** Correct. A handoff should carry the goal, verified facts, permissions, and open questions. Implicit context is easily lost between agents. In this case: Verified findings, unresolved work, and explicit state.
- **D:** Incorrect for this question. Parallel branches reduce wall-clock time when work is truly independent. Shared state and reconciliation still require design. In this case: Verified findings, unresolved work, and explicit state.

### Question 54 — A

Answer: Compare variants with controlled traffic and shared metrics. Quality, latency, and cost against pre-agreed thresholds. Controlled comparison supports evidence-based rollout. Changing several variables at once confuses attribution. Local study-map skill 4.3 (Continuous Evaluation and Regression), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Correct. Controlled comparison supports evidence-based rollout. Changing several variables at once confuses attribution. In this case: Quality, latency, and cost against pre-agreed thresholds.
- **B:** Incorrect for this question. A canary or phased rollout limits exposure while evidence accumulates. Rollback must be practical, not theoretical. In this case: Quality, latency, and cost against pre-agreed thresholds.
- **C:** Incorrect for this question. Quotas and scaling limits can become the real bottleneck. Plan for bursts and graceful degradation. In this case: Quality, latency, and cost against pre-agreed thresholds.
- **D:** Incorrect for this question. Prompts, models, tools, and data can all change behavior. Regression testing catches unintended effects. In this case: Quality, latency, and cost against pre-agreed thresholds.

### Question 55 — A

Answer: Persist sessions in a durable managed store. A document store designed for session access. Durable session storage supports continuity and recovery. Retention and isolation rules still apply. Local study-map skill 4.4 (Runtime Selection), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Correct. Durable session storage supports continuity and recovery. Retention and isolation rules still apply. In this case: A document store designed for session access.
- **B:** Incorrect for this question. An in-memory store can reduce latency for coordination and caching. It is not durable evidence storage by default. In this case: A document store designed for session access.
- **C:** Incorrect for this question. Relational storage fits structured, transactional data. It is usually not the first choice for high-frequency session blobs. In this case: A document store designed for session access.
- **D:** Incorrect for this question. Firestore can serve per-session documents and real-time access patterns. Model access and consistency deliberately. In this case: A document store designed for session access.

### Question 56 — B

Answer: Use staged rollout with measurable rollback criteria. Pause expansion and investigate against the rollback criteria. A canary or phased rollout limits exposure while evidence accumulates. Rollback must be practical, not theoretical. Local study-map skill 4.6 (Monitoring and Optimization), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Pause expansion and investigate against the rollback criteria.
- **B:** Correct. A canary or phased rollout limits exposure while evidence accumulates. Rollback must be practical, not theoretical. In this case: Pause expansion and investigate against the rollback criteria.
- **C:** Incorrect for this question. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. In this case: Pause expansion and investigate against the rollback criteria.
- **D:** Incorrect for this question. Controlled comparison supports evidence-based rollout. Changing several variables at once confuses attribution. In this case: Pause expansion and investigate against the rollback criteria.

### Question 57 — D

Answer: Define an LLM-backed agent with instructions and scoped tools. A sequence with typed tool contracts and dependency-aware state. An LLM agent combines a model, instructions, and available tools. Narrow tool scope reduces unintended actions. Local study-map skill 3.2 (ADK Agent Construction), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Parallel branches reduce wall-clock time when work is truly independent. Shared state and reconciliation still require design. In this case: A sequence with typed tool contracts and dependency-aware state.
- **B:** Incorrect for this question. Sequential workflows make dependencies explicit and are easier to reason about. They may add latency when steps could run independently. In this case: A sequence with typed tool contracts and dependency-aware state.
- **C:** Incorrect for this question. A precise contract helps the model choose and supply arguments correctly. Broad or ambiguous tools invite unsafe calls. In this case: A sequence with typed tool contracts and dependency-aware state.
- **D:** Correct. An LLM agent combines a model, instructions, and available tools. Narrow tool scope reduces unintended actions. In this case: A sequence with typed tool contracts and dependency-aware state.

### Question 58 — A

Answer: Use a proprietary model where supported capability matters. Dependency, exit options, and data portability. Proprietary models may offer strong capability and managed integration. Their terms, lifecycle, and data handling must be reviewed. Local study-map skill 3.1 (Model Selection and Tradeoffs), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Proprietary models may offer strong capability and managed integration. Their terms, lifecycle, and data handling must be reviewed. In this case: Dependency, exit options, and data portability.
- **B:** Incorrect for this question. Self-hosting can address control, residency, or customization needs at operational cost. It shifts patching, scaling, and monitoring to your team. In this case: Dependency, exit options, and data portability.
- **C:** Incorrect for this question. Managed services reduce operational burden and inherit provider controls. Verify data handling, quotas, regions, and supported features. In this case: Dependency, exit options, and data portability.
- **D:** Incorrect for this question. Open weights can support customization or deployment flexibility. They still require licensing review, evaluation, and operational ownership. In this case: Dependency, exit options, and data portability.

### Question 59 — A

Answer: Bound iterations and detect reasoning loops. Bounded retries with loop detection and escalation. A maximum step or time budget prevents runaway cost and repeated actions. Progress checks should trigger escalation. Local study-map skill 4.5 (Troubleshooting Agent Failures), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Correct. A maximum step or time budget prevents runaway cost and repeated actions. Progress checks should trigger escalation. In this case: Bounded retries with loop detection and escalation.
- **B:** Incorrect for this question. Models, sources, and user behavior change. Monitoring detects when evaluation assumptions no longer hold. In this case: Bounded retries with loop detection and escalation.
- **C:** Incorrect for this question. Timeouts protect the workflow from stalled dependencies. Retries must avoid duplicating consequential actions. In this case: Bounded retries with loop detection and escalation.
- **D:** Incorrect for this question. Traces localize latency and failures in multi-step workflows. They are essential for debugging non-deterministic behavior. In this case: Bounded retries with loop detection and escalation.

### Question 60 — D

Answer: Build a representative golden dataset from real tasks. A golden dataset plus deliberate edge and adversarial cases. A golden set anchors evaluation in expected behavior and evidence. It should cover normal, rare, and risky cases. Local study-map skill 4.1 (Evaluation Test Sets), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: A golden dataset plus deliberate edge and adversarial cases.
- **B:** Incorrect for this question. An evalset gives repeatable evidence for agent behavior. It must be maintained as the workflow changes. In this case: A golden dataset plus deliberate edge and adversarial cases.
- **C:** Incorrect for this question. Boundary and hostile inputs reveal failures that happy-path tests miss. Include prompt injection and missing-data cases. In this case: A golden dataset plus deliberate edge and adversarial cases.
- **D:** Correct. A golden set anchors evaluation in expected behavior and evidence. It should cover normal, rare, and risky cases. In this case: A golden dataset plus deliberate edge and adversarial cases.

### Question 61 — C

Answer: Connect approved enterprise content through Agent Search. Region-scoped sources plus authorization-aware retrieval keep each catalog and user within approved boundaries. A supported enterprise search layer can ground responses in indexed organizational material under configured access. Indexing does not make every document accurate or authorized for every user. Local study-map skill 1.3 (Enterprise Data Connection), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Gemini Enterprise overview: https://cloud.google.com/gemini-enterprise

- **A:** Incorrect for this question. Multimodal pipelines can extract usable signals for an agentic workflow. Quality depends on transcription, frame selection, and downstream validation. In this case: Region-scoped sources plus authorization-aware retrieval keep each catalog and user within approved boundaries.
- **B:** Incorrect for this question. Connectors let an agent query approved systems rather than receive uncontrolled copies. Grant only necessary sources and verify the effective identity. In this case: Region-scoped sources plus authorization-aware retrieval keep each catalog and user within approved boundaries.
- **C:** Correct. A supported enterprise search layer can ground responses in indexed organizational material under configured access. Indexing does not make every document accurate or authorized for every user. In this case: Region-scoped sources plus authorization-aware retrieval keep each catalog and user within approved boundaries.
- **D:** Incorrect for this question. A connector's technical reach should not exceed the business authorization for the workflow. Broader access increases both risk and irrelevant retrieval. In this case: Region-scoped sources plus authorization-aware retrieval keep each catalog and user within approved boundaries.

### Question 62 — A

Answer: Model behavior explicitly as pages, transition routes, and event handlers. Explicit states and gated transitions for verification and approval before submission. State-based low-code workflows make allowed transitions and triggers visible. They are a design control, not a substitute for access checks or testing. Local study-map skill 1.1 (State-Based Workflow Design), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Gemini Enterprise overview: https://cloud.google.com/gemini-enterprise

- **A:** Correct. State-based low-code workflows make allowed transitions and triggers visible. They are a design control, not a substitute for access checks or testing. In this case: Explicit states and gated transitions for verification and approval before submission.
- **B:** Incorrect for this question. Short-lived, scoped tokens limit what a tool call can do. Token handling and refresh must avoid broad standing access. In this case: Explicit states and gated transitions for verification and approval before submission.
- **C:** Incorrect for this question. Clear operating guidance describes role, constraints, tone, and fallback behavior. Instructions still need versioning, evaluation, and enforcement outside the prompt. In this case: Explicit states and gated transitions for verification and approval before submission.
- **D:** Incorrect for this question. A supported enterprise search layer can ground responses in indexed organizational material under configured access. Indexing does not make every document accurate or authorized for every user. In this case: Explicit states and gated transitions for verification and approval before submission.

### Question 63 — B

Answer: Govern agent traffic through Agent Gateway. Gateway policy and registry enforcement with alerting. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. Local study-map skill 4.6 (Monitoring and Optimization), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. In this case: Gateway policy and registry enforcement with alerting.
- **B:** Correct. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Gateway policy and registry enforcement with alerting.
- **C:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Gateway policy and registry enforcement with alerting.
- **D:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Gateway policy and registry enforcement with alerting.

### Question 64 — B

Answer: Use VPC Service Controls to establish a data perimeter. A service perimeter with narrow, approved egress. A service perimeter can reduce exfiltration paths for supported services. It complements, rather than replaces, IAM and application checks. Local study-map skill 5.2 (Principal Access Boundaries), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Egress controls reduce exfiltration and unauthorized tool reach. They should be paired with identity and data controls. In this case: A service perimeter with narrow, approved egress.
- **B:** Correct. A service perimeter can reduce exfiltration paths for supported services. It complements, rather than replaces, IAM and application checks. In this case: A service perimeter with narrow, approved egress.
- **C:** Incorrect for this question. CMEK supports key-control and compliance requirements. Key lifecycle and break-glass procedures need operational ownership. In this case: A service perimeter with narrow, approved egress.
- **D:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: A service perimeter with narrow, approved egress.

### Question 65 — C

Answer: Use a dedicated service account with least privilege. Both are affected, and actions cannot be cleanly attributed. A dedicated identity separates the agent from human accounts and limits blast radius. Roles still need review and periodic reduction. Local study-map skill 3.7 (Agent Identity and Permissions), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Distinct identity makes access attributable and auditable. Sharing a human or broad service identity weakens least privilege. In this case: Both are affected, and actions cannot be cleanly attributed.
- **B:** Incorrect for this question. Narrow roles and scopes reduce blast radius. Review permissions as the workflow evolves. In this case: Both are affected, and actions cannot be cleanly attributed.
- **C:** Correct. A dedicated identity separates the agent from human accounts and limits blast radius. Roles still need review and periodic reduction. In this case: Both are affected, and actions cannot be cleanly attributed.
- **D:** Incorrect for this question. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: Both are affected, and actions cannot be cleanly attributed.

### Question 66 — C

Answer: Choose chunk size and overlap for retrieval. Chunk by section, deduplicate, and rerank before grounding the answer. Chunking affects recall, precision, and context usage. Boundaries should follow document structure and be tested against real questions. Local study-map skill 3.4 (RAG Pipeline Design), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Citations let users check claims against sources. Grounding reduces but does not eliminate hallucination. In this case: Chunk by section, deduplicate, and rerank before grounding the answer.
- **B:** Incorrect for this question. A reranker can improve precision after broad recall. It adds latency and still needs evaluation. In this case: Chunk by section, deduplicate, and rerank before grounding the answer.
- **C:** Correct. Chunking affects recall, precision, and context usage. Boundaries should follow document structure and be tested against real questions. In this case: Chunk by section, deduplicate, and rerank before grounding the answer.
- **D:** Incorrect for this question. Duplicates waste context and can overweight one source. Deduplication improves diversity of evidence. In this case: Chunk by section, deduplicate, and rerank before grounding the answer.

### Question 67 — C

Answer: Model behavior explicitly as pages, transition routes, and event handlers. A defined incomplete state with no access to protected data. State-based low-code workflows make allowed transitions and triggers visible. They are a design control, not a substitute for access checks or testing. Local study-map skill 1.1 (State-Based Workflow Design), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Gemini Enterprise overview: https://cloud.google.com/gemini-enterprise

- **A:** Incorrect for this question. A low-code agent needs an explicit path for uncertainty, missing evidence, or out-of-scope requests. Improvisation should not silently become a commitment. In this case: A defined incomplete state with no access to protected data.
- **B:** Incorrect for this question. Clear operating guidance describes role, constraints, tone, and fallback behavior. Instructions still need versioning, evaluation, and enforcement outside the prompt. In this case: A defined incomplete state with no access to protected data.
- **C:** Correct. State-based low-code workflows make allowed transitions and triggers visible. They are a design control, not a substitute for access checks or testing. In this case: A defined incomplete state with no access to protected data.
- **D:** Incorrect for this question. Human-in-the-loop review is appropriate when impact or uncertainty is high. Approval must occur before the effect and with enough context to decide. In this case: A defined incomplete state with no access to protected data.

### Question 68 — C

Answer: Compare variants with controlled traffic and shared metrics. Block on the policy threshold regardless of satisfaction gains. Controlled comparison supports evidence-based rollout. Changing several variables at once confuses attribution. Local study-map skill 1.4 (Low-Code Change and Release Control), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Gemini Enterprise overview: https://cloud.google.com/gemini-enterprise

- **A:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Block on the policy threshold regardless of satisfaction gains.
- **B:** Incorrect for this question. A rollback plan restores a known prior state when quality, cost, or safety thresholds fail. It should be tested, not merely documented. In this case: Block on the policy threshold regardless of satisfaction gains.
- **C:** Correct. Controlled comparison supports evidence-based rollout. Changing several variables at once confuses attribution. In this case: Block on the policy threshold regardless of satisfaction gains.
- **D:** Incorrect for this question. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. In this case: Block on the policy threshold regardless of satisfaction gains.

### Question 69 — D

Answer: Use a tuned model where specialized behavior justifies it. Tuning on representative data with held-out evaluation. Tuning can improve a well-defined pattern but requires representative data and ongoing evaluation. It does not remove grounding or safety needs. Local study-map skill 3.1 (Model Selection and Tradeoffs), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Large models can handle ambiguity and multi-step reasoning but cost more. Selection should follow measured task requirements. In this case: Tuning on representative data with held-out evaluation.
- **B:** Incorrect for this question. Open weights can support customization or deployment flexibility. They still require licensing review, evaluation, and operational ownership. In this case: Tuning on representative data with held-out evaluation.
- **C:** Incorrect for this question. A small model can reduce latency and cost when the task is constrained and evaluated. It is not automatically adequate for harder inputs. In this case: Tuning on representative data with held-out evaluation.
- **D:** Correct. Tuning can improve a well-defined pattern but requires representative data and ongoing evaluation. It does not remove grounding or safety needs. In this case: Tuning on representative data with held-out evaluation.

### Question 70 — B

Answer: Use A2A for agent-to-agent interoperability. A2A task exchange with authenticated callers and explicit result handling. A2A supports discovery and task exchange between agents that may be built on different stacks. Trust and authorization still need explicit design. Local study-map skill 3.9 (Agent-to-Agent Protocols), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. In this case: A2A task exchange with authenticated callers and explicit result handling.
- **B:** Correct. A2A supports discovery and task exchange between agents that may be built on different stacks. Trust and authorization still need explicit design. In this case: A2A task exchange with authenticated callers and explicit result handling.
- **C:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: A2A task exchange with authenticated callers and explicit result handling.
- **D:** Incorrect for this question. MCP provides a common interface between agents and capability servers. Server trust, scopes, and validation remain your responsibility. In this case: A2A task exchange with authenticated callers and explicit result handling.

### Question 71 — D

Answer: Encode organizational policy in enforceable controls. Central gateway and platform policy rather than per-agent prompts. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. Local study-map skill 3.11 (Runtime Coordination and Policies), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Central gateway and platform policy rather than per-agent prompts.
- **B:** Incorrect for this question. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: Central gateway and platform policy rather than per-agent prompts.
- **C:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Central gateway and platform policy rather than per-agent prompts.
- **D:** Correct. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Central gateway and platform policy rather than per-agent prompts.

### Question 72 — C

Answer: Use human review for unresolved or high-impact judgment. A consequential action still needs human authorization before it takes effect. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. Local study-map skill 4.2 (Evaluation Metrics and Tooling), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Autoraters can score nuanced qualities at scale. They require calibration against human judgments and periodic review. In this case: A consequential action still needs human authorization before it takes effect.
- **B:** Incorrect for this question. A correct answer can hide an unsafe or wasteful action sequence. Trajectory checks verify which tools were called and with what arguments. In this case: A consequential action still needs human authorization before it takes effect.
- **C:** Correct. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. In this case: A consequential action still needs human authorization before it takes effect.
- **D:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: A consequential action still needs human authorization before it takes effect.

### Question 73 — C

Answer: Publish an Agent Card describing capabilities and endpoints. The Agent Card and registry metadata. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. Local study-map skill 3.9 (Agent-to-Agent Protocols), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. MCP provides a common interface between agents and capability servers. Server trust, scopes, and validation remain your responsibility. In this case: The Agent Card and registry metadata.
- **B:** Incorrect for this question. A2A supports discovery and task exchange between agents that may be built on different stacks. Trust and authorization still need explicit design. In this case: The Agent Card and registry metadata.
- **C:** Correct. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. In this case: The Agent Card and registry metadata.
- **D:** Incorrect for this question. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: The Agent Card and registry metadata.

### Question 74 — B

Answer: Evaluate tool-call trajectories, not only final text. Trajectory evaluation of tool calls and side effects. A correct answer can hide an unsafe or wasteful action sequence. Trajectory checks verify which tools were called and with what arguments. Local study-map skill 4.2 (Evaluation Metrics and Tooling), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Generation cannot compensate for missing evidence. Retrieval metrics localize pipeline failures. In this case: Trajectory evaluation of tool calls and side effects.
- **B:** Correct. A correct answer can hide an unsafe or wasteful action sequence. Trajectory checks verify which tools were called and with what arguments. In this case: Trajectory evaluation of tool calls and side effects.
- **C:** Incorrect for this question. Response metrics assess what the user receives. They should be tied to explicit task criteria. In this case: Trajectory evaluation of tool calls and side effects.
- **D:** Incorrect for this question. Citations let users check claims against sources. Grounding reduces but does not eliminate hallucination. In this case: Trajectory evaluation of tool calls and side effects.

### Question 75 — A

Answer: Use scoped OAuth 2.0 tokens for agent-to-tool calls. Scoped OAuth tokens with verified identity propagation. Short-lived, scoped tokens limit what a tool call can do. Token handling and refresh must avoid broad standing access. Local study-map skill 3.7 (Agent Identity and Permissions), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Short-lived, scoped tokens limit what a tool call can do. Token handling and refresh must avoid broad standing access. In this case: Scoped OAuth tokens with verified identity propagation.
- **B:** Incorrect for this question. Short lifetimes and audience limits reduce misuse. Tokens should not be placed in prompts or logs. In this case: Scoped OAuth tokens with verified identity propagation.
- **C:** Incorrect for this question. Downstream authorization needs the actual principal, not a generic agent identity. Delegation must be explicit and scoped. In this case: Scoped OAuth tokens with verified identity propagation.
- **D:** Incorrect for this question. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: Scoped OAuth tokens with verified identity propagation.

### Question 76 — A

Answer: Constrain access with a principal access boundary policy. A narrow role and a principal access boundary. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. Local study-map skill 5.2 (Principal Access Boundaries), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Correct. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: A narrow role and a principal access boundary.
- **B:** Incorrect for this question. A service perimeter can reduce exfiltration paths for supported services. It complements, rather than replaces, IAM and application checks. In this case: A narrow role and a principal access boundary.
- **C:** Incorrect for this question. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: A narrow role and a principal access boundary.
- **D:** Incorrect for this question. Narrow roles and scopes reduce blast radius. Review permissions as the workflow evolves. In this case: A narrow role and a principal access boundary.

### Question 77 — B

Answer: Detect changes in inputs, data, or performance over time. Index contents, retrieval traces, and drift in evidence quality. Models, sources, and user behavior change. Monitoring detects when evaluation assumptions no longer hold. Local study-map skill 4.5 (Troubleshooting Agent Failures), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Prompts, models, tools, and data can all change behavior. Regression testing catches unintended effects. In this case: Index contents, retrieval traces, and drift in evidence quality.
- **B:** Correct. Models, sources, and user behavior change. Monitoring detects when evaluation assumptions no longer hold. In this case: Index contents, retrieval traces, and drift in evidence quality.
- **C:** Incorrect for this question. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. In this case: Index contents, retrieval traces, and drift in evidence quality.
- **D:** Incorrect for this question. Traces localize latency and failures in multi-step workflows. They are essential for debugging non-deterministic behavior. In this case: Index contents, retrieval traces, and drift in evidence quality.

### Question 78 — D

Answer: Use a calibrated model-based autorater for scalable judgment. Use explicit rubrics and calibrate against human scores. Autoraters can score nuanced qualities at scale. They require calibration against human judgments and periodic review. Local study-map skill 4.2 (Evaluation Metrics and Tooling), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Response metrics assess what the user receives. They should be tied to explicit task criteria. In this case: Use explicit rubrics and calibrate against human scores.
- **B:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Use explicit rubrics and calibrate against human scores.
- **C:** Incorrect for this question. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. In this case: Use explicit rubrics and calibrate against human scores.
- **D:** Correct. Autoraters can score nuanced qualities at scale. They require calibration against human judgments and periodic review. In this case: Use explicit rubrics and calibrate against human scores.

### Question 79 — D

Answer: Inspect and de-identify sensitive data with Sensitive Data Protection. Output inspection and redaction before delivery. Classification and de-identification reduce unnecessary exposure. De-identification must be validated for the specific data and purpose. Local study-map skill 5.4 (Registry and Policy Enforcement), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Minimization reduces the impact of leakage and over-retention. Verify that redaction survives the whole pipeline. In this case: Output inspection and redaction before delivery.
- **B:** Incorrect for this question. Model Armor can help detect prompt injection, unsafe content, and sensitive data patterns. It is a layered control, not a complete trust boundary. In this case: Output inspection and redaction before delivery.
- **C:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Output inspection and redaction before delivery.
- **D:** Correct. Classification and de-identification reduce unnecessary exposure. De-identification must be validated for the specific data and purpose. In this case: Output inspection and redaction before delivery.

### Question 80 — A

Answer: Use supported enterprise connectors with scoped access. Region-scoped connectors and authorization-aware retrieval keep contract templates within the correct jurisdiction. Connectors let an agent query approved systems rather than receive uncontrolled copies. Grant only necessary sources and verify the effective identity. Local study-map skill 1.3 (Enterprise Data Connection), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Gemini Enterprise overview: https://cloud.google.com/gemini-enterprise

- **A:** Correct. Connectors let an agent query approved systems rather than receive uncontrolled copies. Grant only necessary sources and verify the effective identity. In this case: Region-scoped connectors and authorization-aware retrieval keep contract templates within the correct jurisdiction.
- **B:** Incorrect for this question. A connector's technical reach should not exceed the business authorization for the workflow. Broader access increases both risk and irrelevant retrieval. In this case: Region-scoped connectors and authorization-aware retrieval keep contract templates within the correct jurisdiction.
- **C:** Incorrect for this question. A supported enterprise search layer can ground responses in indexed organizational material under configured access. Indexing does not make every document accurate or authorized for every user. In this case: Region-scoped connectors and authorization-aware retrieval keep contract templates within the correct jurisdiction.
- **D:** Incorrect for this question. Multimodal pipelines can extract usable signals for an agentic workflow. Quality depends on transcription, frame selection, and downstream validation. In this case: Region-scoped connectors and authorization-aware retrieval keep contract templates within the correct jurisdiction.

### Question 81 — C

Answer: Use human review for unresolved or high-impact judgment. Adjudicate and escalate rather than average incompatible expectations. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. Local study-map skill 4.1 (Evaluation Test Sets), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Autoraters can score nuanced qualities at scale. They require calibration against human judgments and periodic review. In this case: Adjudicate and escalate rather than average incompatible expectations.
- **B:** Incorrect for this question. A golden set anchors evaluation in expected behavior and evidence. It should cover normal, rare, and risky cases. In this case: Adjudicate and escalate rather than average incompatible expectations.
- **C:** Correct. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. In this case: Adjudicate and escalate rather than average incompatible expectations.
- **D:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Adjudicate and escalate rather than average incompatible expectations.

### Question 82 — C

Answer: Model behavior explicitly as pages, transition routes, and event handlers. An explicit classification state with distinct transitions and fallbacks. State-based low-code workflows make allowed transitions and triggers visible. They are a design control, not a substitute for access checks or testing. Local study-map skill 1.1 (State-Based Workflow Design), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Gemini Enterprise overview: https://cloud.google.com/gemini-enterprise

- **A:** Incorrect for this question. Parallel branches reduce wall-clock time when work is truly independent. Shared state and reconciliation still require design. In this case: An explicit classification state with distinct transitions and fallbacks.
- **B:** Incorrect for this question. Clear operating guidance describes role, constraints, tone, and fallback behavior. Instructions still need versioning, evaluation, and enforcement outside the prompt. In this case: An explicit classification state with distinct transitions and fallbacks.
- **C:** Correct. State-based low-code workflows make allowed transitions and triggers visible. They are a design control, not a substitute for access checks or testing. In this case: An explicit classification state with distinct transitions and fallbacks.
- **D:** Incorrect for this question. Routing can match task type, language, or risk to a capable handler. Misrouting needs an observable fallback. In this case: An explicit classification state with distinct transitions and fallbacks.

### Question 83 — C

Answer: Run coding agents in an isolated, permission-limited environment. Sandbox isolation with repository-scoped mounts and identity. Sandboxing limits filesystem, network, and credential exposure during autonomous work. Isolation reduces blast radius but does not make generated code correct. Local study-map skill 2.3 (Secure Sandboxes), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Sandbox policy bounds what autonomous code can reach. It should be tested, not assumed from the existence of a sandbox. In this case: Sandbox isolation with repository-scoped mounts and identity.
- **B:** Incorrect for this question. Cluster-level controls can separate workloads and restrict network or resource access. They must be configured deliberately and tested for escape paths. In this case: Sandbox isolation with repository-scoped mounts and identity.
- **C:** Correct. Sandboxing limits filesystem, network, and credential exposure during autonomous work. Isolation reduces blast radius but does not make generated code correct. In this case: Sandbox isolation with repository-scoped mounts and identity.
- **D:** Incorrect for this question. Managed workstations provide controlled, reproducible development sessions. They should still use least privilege and approved network paths. In this case: Sandbox isolation with repository-scoped mounts and identity.

### Question 84 — B

Answer: Measure retrieval relevance and recall separately. Passage-level grounding and citation validation tie each claim to the section that actually supports it. Generation cannot compensate for missing evidence. Retrieval metrics localize pipeline failures. Local study-map skill 4.2 (Evaluation Metrics and Tooling), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. A correct answer can hide an unsafe or wasteful action sequence. Trajectory checks verify which tools were called and with what arguments. In this case: Passage-level grounding and citation validation tie each claim to the section that actually supports it.
- **B:** Correct. Generation cannot compensate for missing evidence. Retrieval metrics localize pipeline failures. In this case: Passage-level grounding and citation validation tie each claim to the section that actually supports it.
- **C:** Incorrect for this question. Citations let users check claims against sources. Grounding reduces but does not eliminate hallucination. In this case: Passage-level grounding and citation validation tie each claim to the section that actually supports it.
- **D:** Incorrect for this question. Response metrics assess what the user receives. They should be tied to explicit task criteria. In this case: Passage-level grounding and citation validation tie each claim to the section that actually supports it.

### Question 85 — D

Answer: Package reusable guidance and assets as a skill. A reviewed skill with the procedure, examples, and validation steps. A skill can carry instructions, examples, and supporting files for a recurring task. It guides behavior but does not itself enforce permissions. Local study-map skill 2.1 (Coding Agent Configuration and Tooling), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Rules communicate conventions and constraints for generated changes. They are guidance; merge controls and tests remain the enforcement boundary. In this case: A reviewed skill with the procedure, examples, and validation steps.
- **B:** Incorrect for this question. Plugins make a capability set reusable across projects. Bundling does not remove the need to review each included permission and dependency. In this case: A reviewed skill with the procedure, examples, and validation steps.
- **C:** Incorrect for this question. Hooks can enforce checks, logging, or formatting at defined points. They are useful precisely because they do not depend on model discretion. In this case: A reviewed skill with the procedure, examples, and validation steps.
- **D:** Correct. A skill can carry instructions, examples, and supporting files for a recurring task. It guides behavior but does not itself enforce permissions. In this case: A reviewed skill with the procedure, examples, and validation steps.

### Question 86 — C

Answer: Choose an embedding model suited to the domain and language. Hybrid retrieval with reranking of the combined candidates. Embedding choice affects retrieval quality and must be evaluated on real queries. A generic model may miss domain vocabulary. Local study-map skill 3.4 (RAG Pipeline Design), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Similarity ranking surfaces potentially relevant content. It does not prove relevance or factual support. In this case: Hybrid retrieval with reranking of the combined candidates.
- **B:** Incorrect for this question. A reranker can improve precision after broad recall. It adds latency and still needs evaluation. In this case: Hybrid retrieval with reranking of the combined candidates.
- **C:** Correct. Embedding choice affects retrieval quality and must be evaluated on real queries. A generic model may miss domain vocabulary. In this case: Hybrid retrieval with reranking of the combined candidates.
- **D:** Incorrect for this question. Hybrid retrieval can cover exact identifiers and paraphrased meaning. Fusion weights should be tested. In this case: Hybrid retrieval with reranking of the combined candidates.

### Question 87 — D

Answer: Repeat work until a defined stop condition is met. A bounded loop with progress checks and escalation. Loops can refine output or poll a system, but need iteration limits and progress checks. Unbounded loops waste cost and can repeat unsafe actions. Local study-map skill 3.10 (Multi-Agent Workflow Patterns), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Graphs express conditional paths and joins more clearly than a fixed chain. Complexity should be justified by real control flow. In this case: A bounded loop with progress checks and escalation.
- **B:** Incorrect for this question. Sequential workflows make dependencies explicit and are easier to reason about. They may add latency when steps could run independently. In this case: A bounded loop with progress checks and escalation.
- **C:** Incorrect for this question. Parallel branches reduce wall-clock time when work is truly independent. Shared state and reconciliation still require design. In this case: A bounded loop with progress checks and escalation.
- **D:** Correct. Loops can refine output or poll a system, but need iteration limits and progress checks. Unbounded loops waste cost and can repeat unsafe actions. In this case: A bounded loop with progress checks and escalation.

### Question 88 — D

Answer: Build the agent with the Agent Development Kit. Agent Development Kit callbacks around model and tool execution. ADK provides code-level agent construction, tools, orchestration, and evaluation support. Architecture choices still determine safety and operability. Local study-map skill 3.2 (ADK Agent Construction), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Tools let the agent act through defined interfaces. Each tool should validate inputs and enforce authorization server-side. In this case: Agent Development Kit callbacks around model and tool execution.
- **B:** Incorrect for this question. Callbacks can inspect or modify behavior at defined agent stages. They must be deterministic where policy depends on them. In this case: Agent Development Kit callbacks around model and tool execution.
- **C:** Incorrect for this question. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. In this case: Agent Development Kit callbacks around model and tool execution.
- **D:** Correct. ADK provides code-level agent construction, tools, orchestration, and evaluation support. Architecture choices still determine safety and operability. In this case: Agent Development Kit callbacks around model and tool execution.

### Question 89 — D

Answer: Profile execution paths before optimizing them. Measured baseline and evidence that behavior remains correct. Optimization should follow measured bottlenecks and correct behavior. Rewriting for speed without evidence can add defects. Local study-map skill 2.4 (Code Modernization and Vulnerability Remediation), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Security patching needs reproduction, a scoped change, and validation. The agent can assist but cannot grant itself assurance. In this case: Measured baseline and evidence that behavior remains correct.
- **B:** Incorrect for this question. Refactoring should preserve observable behavior and be verified by tests and review. A plausible diff is not proof of equivalence. In this case: Measured baseline and evidence that behavior remains correct.
- **C:** Incorrect for this question. Human or automated review checks scope, security, and correctness before change lands. The coding agent's confidence is not review. In this case: Measured baseline and evidence that behavior remains correct.
- **D:** Correct. Optimization should follow measured bottlenecks and correct behavior. Rewriting for speed without evidence can add defects. In this case: Measured baseline and evidence that behavior remains correct.

### Question 90 — A

Answer: Run independent agents concurrently. Parallel checks joined into a decision step. Parallel branches reduce wall-clock time when work is truly independent. Shared state and reconciliation still require design. Local study-map skill 3.10 (Multi-Agent Workflow Patterns), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Parallel branches reduce wall-clock time when work is truly independent. Shared state and reconciliation still require design. In this case: Parallel checks joined into a decision step.
- **B:** Incorrect for this question. Sequential workflows make dependencies explicit and are easier to reason about. They may add latency when steps could run independently. In this case: Parallel checks joined into a decision step.
- **C:** Incorrect for this question. Graphs express conditional paths and joins more clearly than a fixed chain. Complexity should be justified by real control flow. In this case: Parallel checks joined into a decision step.
- **D:** Incorrect for this question. Routing can match task type, language, or risk to a capable handler. Misrouting needs an observable fallback. In this case: Parallel checks joined into a decision step.

### Question 91 — B

Answer: Add structured reasoning guidance for multi-step tasks. A defined explanation structure with approved criteria and examples. Prompting a deliberate step order can improve consistency on decomposable work. It does not replace evidence checks or verification of the result. Local study-map skill 1.2 (Agent Instructions and Prompt Templates), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Gemini Enterprise overview: https://cloud.google.com/gemini-enterprise

- **A:** Incorrect for this question. Demonstrations clarify expected formats and boundaries for a low-code agent. They do not guarantee correctness on unseen inputs. In this case: A defined explanation structure with approved criteria and examples.
- **B:** Correct. Prompting a deliberate step order can improve consistency on decomposable work. It does not replace evidence checks or verification of the result. In this case: A defined explanation structure with approved criteria and examples.
- **C:** Incorrect for this question. Long-term memory can personalize and improve continuity. It needs consent, retention, and deletion controls. In this case: A defined explanation structure with approved criteria and examples.
- **D:** Incorrect for this question. Clear operating guidance describes role, constraints, tone, and fallback behavior. Instructions still need versioning, evaluation, and enforcement outside the prompt. In this case: A defined explanation structure with approved criteria and examples.

### Question 92 — A

Answer: Measure retrieval relevance and recall separately. Groundedness, even though the final conclusion may be right. Generation cannot compensate for missing evidence. Retrieval metrics localize pipeline failures. Local study-map skill 3.6 (Retrieval Authorization and Evidence Quality), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Generation cannot compensate for missing evidence. Retrieval metrics localize pipeline failures. In this case: Groundedness, even though the final conclusion may be right.
- **B:** Incorrect for this question. Response metrics assess what the user receives. They should be tied to explicit task criteria. In this case: Groundedness, even though the final conclusion may be right.
- **C:** Incorrect for this question. Citations let users check claims against sources. Grounding reduces but does not eliminate hallucination. In this case: Groundedness, even though the final conclusion may be right.
- **D:** Incorrect for this question. A correct answer can hide an unsafe or wasteful action sequence. Trajectory checks verify which tools were called and with what arguments. In this case: Groundedness, even though the final conclusion may be right.

### Question 93 — C

Answer: Use scoped OAuth 2.0 tokens for agent-to-tool calls. A short-lived, scoped OAuth token with verified delegation. Short-lived, scoped tokens limit what a tool call can do. Token handling and refresh must avoid broad standing access. Local study-map skill 5.1 (Authentication and Secure Tool Execution), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. A dedicated identity separates the agent from human accounts and limits blast radius. Roles still need review and periodic reduction. In this case: A short-lived, scoped OAuth token with verified delegation.
- **B:** Incorrect for this question. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: A short-lived, scoped OAuth token with verified delegation.
- **C:** Correct. Short-lived, scoped tokens limit what a tool call can do. Token handling and refresh must avoid broad standing access. In this case: A short-lived, scoped OAuth token with verified delegation.
- **D:** Incorrect for this question. Short lifetimes and audience limits reduce misuse. Tokens should not be placed in prompts or logs. In this case: A short-lived, scoped OAuth token with verified delegation.

### Question 94 — D

Answer: Expose approved capabilities through an MCP server. An MCP server with scoped read and write tools. An MCP server provides a governed interface to tools, resources, or prompts. The server must enforce its own authorization and input validation. Local study-map skill 2.1 (Coding Agent Configuration and Tooling), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. In this case: An MCP server with scoped read and write tools.
- **B:** Incorrect for this question. MCP provides a common interface between agents and capability servers. Server trust, scopes, and validation remain your responsibility. In this case: An MCP server with scoped read and write tools.
- **C:** Incorrect for this question. A2A supports discovery and task exchange between agents that may be built on different stacks. Trust and authorization still need explicit design. In this case: An MCP server with scoped read and write tools.
- **D:** Correct. An MCP server provides a governed interface to tools, resources, or prompts. The server must enforce its own authorization and input validation. In this case: An MCP server with scoped read and write tools.

### Question 95 — D

Answer: Include representative few-shot examples. Instructions plus representative examples of approved denial categories. Demonstrations clarify expected formats and boundaries for a low-code agent. They do not guarantee correctness on unseen inputs. Local study-map skill 1.2 (Agent Instructions and Prompt Templates), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Gemini Enterprise overview: https://cloud.google.com/gemini-enterprise

- **A:** Incorrect for this question. Embedding choice affects retrieval quality and must be evaluated on real queries. A generic model may miss domain vocabulary. In this case: Instructions plus representative examples of approved denial categories.
- **B:** Incorrect for this question. Clear operating guidance describes role, constraints, tone, and fallback behavior. Instructions still need versioning, evaluation, and enforcement outside the prompt. In this case: Instructions plus representative examples of approved denial categories.
- **C:** Incorrect for this question. Prompting a deliberate step order can improve consistency on decomposable work. It does not replace evidence checks or verification of the result. In this case: Instructions plus representative examples of approved denial categories.
- **D:** Correct. Demonstrations clarify expected formats and boundaries for a low-code agent. They do not guarantee correctness on unseen inputs. In this case: Instructions plus representative examples of approved denial categories.

### Question 96 — D

Answer: Filter retrieval by the requesting user's authorization. Authorization filtering before retrieval results enter the prompt. Access checks must occur before content enters the model context. Relevance never overrides permission. Local study-map skill 3.6 (Retrieval Authorization and Evidence Quality), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: Authorization filtering before retrieval results enter the prompt.
- **B:** Incorrect for this question. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: Authorization filtering before retrieval results enter the prompt.
- **C:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Authorization filtering before retrieval results enter the prompt.
- **D:** Correct. Access checks must occur before content enters the model context. Relevance never overrides permission. In this case: Authorization filtering before retrieval results enter the prompt.

### Question 97 — B

Answer: Bundle related skills, tools, and configuration as a plugin. A versioned plugin with reviewed tools, checks, and guidance. Plugins make a capability set reusable across projects. Bundling does not remove the need to review each included permission and dependency. Local study-map skill 2.2 (Customization Primitives), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A subagent can isolate context and permissions for a focused job. Clear ownership, tool scope, and returned evidence are still required. In this case: A versioned plugin with reviewed tools, checks, and guidance.
- **B:** Correct. Plugins make a capability set reusable across projects. Bundling does not remove the need to review each included permission and dependency. In this case: A versioned plugin with reviewed tools, checks, and guidance.
- **C:** Incorrect for this question. A skill can carry instructions, examples, and supporting files for a recurring task. It guides behavior but does not itself enforce permissions. In this case: A versioned plugin with reviewed tools, checks, and guidance.
- **D:** Incorrect for this question. Hooks can enforce checks, logging, or formatting at defined points. They are useful precisely because they do not depend on model discretion. In this case: A versioned plugin with reviewed tools, checks, and guidance.

### Question 98 — C

Answer: Write explicit system instructions and reusable prompt templates. System instructions with the approved category set and examples, plus verification. Clear operating guidance describes role, constraints, tone, and fallback behavior. Instructions still need versioning, evaluation, and enforcement outside the prompt. Local study-map skill 1.2 (Agent Instructions and Prompt Templates), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Gemini Enterprise overview: https://cloud.google.com/gemini-enterprise

- **A:** Incorrect for this question. Embedding choice affects retrieval quality and must be evaluated on real queries. A generic model may miss domain vocabulary. In this case: System instructions with the approved category set and examples, plus verification.
- **B:** Incorrect for this question. Demonstrations clarify expected formats and boundaries for a low-code agent. They do not guarantee correctness on unseen inputs. In this case: System instructions with the approved category set and examples, plus verification.
- **C:** Correct. Clear operating guidance describes role, constraints, tone, and fallback behavior. Instructions still need versioning, evaluation, and enforcement outside the prompt. In this case: System instructions with the approved category set and examples, plus verification.
- **D:** Incorrect for this question. Prompting a deliberate step order can improve consistency on decomposable work. It does not replace evidence checks or verification of the result. In this case: System instructions with the approved category set and examples, plus verification.

### Question 99 — C

Answer: Run agents in a fixed sequence. Routing to a specialist after classification. Sequential workflows make dependencies explicit and are easier to reason about. They may add latency when steps could run independently. Local study-map skill 3.2 (ADK Agent Construction), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Graphs express conditional paths and joins more clearly than a fixed chain. Complexity should be justified by real control flow. In this case: Routing to a specialist after classification.
- **B:** Incorrect for this question. Parallel branches reduce wall-clock time when work is truly independent. Shared state and reconciliation still require design. In this case: Routing to a specialist after classification.
- **C:** Correct. Sequential workflows make dependencies explicit and are easier to reason about. They may add latency when steps could run independently. In this case: Routing to a specialist after classification.
- **D:** Incorrect for this question. Routing can match task type, language, or risk to a capable handler. Misrouting needs an observable fallback. In this case: Routing to a specialist after classification.

### Question 100 — C

Answer: Set explicit pass thresholds before evaluating. Compare against thresholds and roll back or fix based on evidence. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. Local study-map skill 1.4 (Low-Code Change and Release Control), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Gemini Enterprise overview: https://cloud.google.com/gemini-enterprise

- **A:** Incorrect for this question. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. In this case: Compare against thresholds and roll back or fix based on evidence.
- **B:** Incorrect for this question. A canary or phased rollout limits exposure while evidence accumulates. Rollback must be practical, not theoretical. In this case: Compare against thresholds and roll back or fix based on evidence.
- **C:** Correct. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Compare against thresholds and roll back or fix based on evidence.
- **D:** Incorrect for this question. Prompts, models, tools, and data can all change behavior. Regression testing catches unintended effects. In this case: Compare against thresholds and roll back or fix based on evidence.
