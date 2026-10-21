# Google Cloud Professional Agentic Architect (PAA) — Practice Set 3

Custom Agents: Identity, Orchestration, and Registry

100 questions · Suggested practice duration: 180 minutes · Practice target: 80%

Tests 1–5 are focused learning tests. Test 6 is an expanded five-domain review, not an official exam replica. Related concepts recur.

Select ONE best answer for every question. Answer key follows all questions.

Original educational content, not actual, recalled, or copied Anthropic exam items.

## Questions

### 1. A shared retrieval index serves users from different business units. What must be applied before results enter the prompt?

Domain: Developing Custom Agents

- A. Filter retrieval using trusted metadata
- B. Filter retrieval by the requesting user's authorization
- C. Deduplicate near-identical retrieved chunks
- D. Use similarity scoring to retrieve candidate passages

### 2. A new chunking strategy increases retrieved evidence but lowers answer accuracy. What should be investigated?

Domain: Developing Custom Agents

- A. Evaluate tool-call trajectories, not only final text
- B. Score response correctness, completeness, and helpfulness
- C. Track token and tool cost per completed task
- D. Measure retrieval relevance and recall separately

### 3. An auditor asks which passage supported a specific sentence. What should the system provide?

Domain: Developing Custom Agents

- A. Use similarity scoring to retrieve candidate passages
- B. Rerank retrieved passages before generation
- C. Preserve source and chunk identifiers through the pipeline
- D. Ground the response in cited retrieved evidence

### 4. A superseded regulation remains retrievable because deletion never propagated. What should be fixed?

Domain: Developing Custom Agents

- A. Filter retrieval using trusted metadata
- B. Deduplicate near-identical retrieved chunks
- C. Rerank retrieved passages before generation
- D. Check index freshness and reindexing behavior

### 5. A model-based grader scores answers highly, but experts disagree on edge cases. What should be done?

Domain: Developing Custom Agents

- A. Use human review for unresolved or high-impact judgment
- B. Use a calibrated model-based autorater for scalable judgment
- C. Set explicit pass thresholds before evaluating
- D. Ground the response in cited retrieved evidence

### 6. A user can open a document but not a restricted section within it. What should retrieval enforce?

Domain: Developing Custom Agents

- A. Filter retrieval by the requesting user's authorization
- B. Constrain access with a principal access boundary policy
- C. Govern agent traffic through Agent Gateway
- D. Grant IAM roles to the agent identity, not to users' credentials

### 7. A team wants to know whether failures come from retrieval or generation. What should it measure separately?

Domain: Developing Custom Agents

- A. Evaluate tool-call trajectories, not only final text
- B. Score response correctness, completeness, and helpfulness
- C. Measure retrieval relevance and recall separately
- D. Set explicit pass thresholds before evaluating

### 8. A well-sourced answer recommends an action requiring approval. What is the next control?

Domain: Developing Custom Agents

- A. Score response correctness, completeness, and helpfulness
- B. Set explicit pass thresholds before evaluating
- C. Ground the response in cited retrieved evidence
- D. Use human review for unresolved or high-impact judgment

### 9. Metadata labels are inconsistent across two source systems. What should happen before relying on them for filtering?

Domain: Developing Custom Agents

- A. Deduplicate near-identical retrieved chunks
- B. Filter retrieval using trusted metadata
- C. Check index freshness and reindexing behavior
- D. Preserve source and chunk identifiers through the pipeline

### 10. An audit shows tool calls attributed to a generic shared account. What should be introduced?

Domain: Developing Custom Agents

- A. Give each agent its own managed identity
- B. Grant IAM roles to the agent identity, not to users' credentials
- C. Constrain access with a principal access boundary policy
- D. Use a dedicated service account with least privilege

### 11. An agent needs one bucket but its identity can read the whole project. What should be applied?

Domain: Developing Custom Agents

- A. Constrain access with a principal access boundary policy
- B. Grant the minimum permissions required for the task
- C. Use VPC Service Controls to establish a data perimeter
- D. Grant IAM roles to the agent identity, not to users' credentials

### 12. A tool must act on behalf of a signed-in user with limited scope. What should be used?

Domain: Developing Custom Agents

- A. Keep access tokens short-lived and narrowly scoped
- B. Use scoped OAuth 2.0 tokens for agent-to-tool calls
- C. Store secrets in Secret Manager rather than prompts or code
- D. Propagate the caller's identity to downstream tools

### 13. A downstream service needs to know which end user initiated a request. What must be propagated?

Domain: Developing Custom Agents

- A. Use a dedicated service account with least privilege
- B. Grant IAM roles to the agent identity, not to users' credentials
- C. Propagate the caller's identity to downstream tools
- D. Give each agent its own managed identity

### 14. A data perimeter blocks an unexpected service call from the agent. What should the team do?

Domain: Developing Custom Agents

- A. Constrain access with a principal access boundary policy
- B. Govern agent traffic through Agent Gateway
- C. Restrict outbound network access to approved destinations
- D. Use VPC Service Controls to establish a data perimeter

### 15. An agent's permissions have grown through temporary fixes. What should be done?

Domain: Developing Custom Agents

- A. Record agent actions and tool calls in audit logs
- B. Constrain access with a principal access boundary policy
- C. Grant the minimum permissions required for the task
- D. Grant IAM roles to the agent identity, not to users' credentials

### 16. A tool credential is embedded in source code and logs. What should happen?

Domain: Developing Custom Agents

- A. Store secrets in Secret Manager rather than prompts or code
- B. Give each agent its own managed identity
- C. Keep access tokens short-lived and narrowly scoped
- D. Use scoped OAuth 2.0 tokens for agent-to-tool calls

### 17. An agent can reach a dataset outside its business purpose even though its role permits it. What control addresses this?

Domain: Developing Custom Agents

- A. Govern agent traffic through Agent Gateway
- B. Register agents and capabilities in Agent Registry
- C. Grant IAM roles to the agent identity, not to users' credentials
- D. Constrain access with a principal access boundary policy

### 18. A platform team needs an inventory of approved agents and their owners. What should it maintain?

Domain: Developing Custom Agents

- A. Publish an Agent Card describing capabilities and endpoints
- B. Bundle related skills, tools, and configuration as a plugin
- C. Register agents and capabilities in Agent Registry
- D. Use MCP for standardized tool and resource access

### 19. An internal API should be callable by several agent frameworks through a standard interface. What should be built?

Domain: Developing Custom Agents

- A. Publish an Agent Card describing capabilities and endpoints
- B. Use MCP for standardized tool and resource access
- C. Use A2A for agent-to-agent interoperability
- D. Package reusable guidance and assets as a skill

### 20. A calling agent needs to decide whether a remote specialist can handle a task. What should it consult?

Domain: Developing Custom Agents

- A. Use MCP for standardized tool and resource access
- B. Use A2A for agent-to-agent interoperability
- C. Register agents and capabilities in Agent Registry
- D. Publish an Agent Card describing capabilities and endpoints

### 21. A set of agent capabilities must be versioned and distributed together. What should package them?

Domain: Developing Custom Agents

- A. Provide persistent coding guidance for a coding agent
- B. Package reusable guidance and assets as a skill
- C. Bundle related skills, tools, and configuration as a plugin
- D. Run deterministic logic when a lifecycle event fires

### 22. A new MCP server will expose a write operation. What must it enforce?

Domain: Developing Custom Agents

- A. Constrain access with a principal access boundary policy
- B. Use MCP for standardized tool and resource access
- C. Expose approved capabilities through an MCP server
- D. Govern agent traffic through Agent Gateway

### 23. A deprecated agent still has active credentials and registry visibility. What should be done?

Domain: Developing Custom Agents

- A. Record agent actions and tool calls in audit logs
- B. Give each agent its own managed identity
- C. Encode organizational policy in enforceable controls
- D. Register agents and capabilities in Agent Registry

### 24. A server needs to provide callable actions, reference documents, and reusable prompt templates. What MCP primitives map to these?

Domain: Developing Custom Agents

- A. Bundle related skills, tools, and configuration as a plugin
- B. Package reusable guidance and assets as a skill
- C. Use MCP for standardized tool and resource access
- D. Publish an Agent Card describing capabilities and endpoints

### 25. A remote agent advertises a capability that no longer works. What is the consequence?

Domain: Developing Custom Agents

- A. Register agents and capabilities in Agent Registry
- B. Use A2A for agent-to-agent interoperability
- C. Use MCP for standardized tool and resource access
- D. Publish an Agent Card describing capabilities and endpoints

### 26. Two agents from different vendors must exchange a long-running task. What should be evaluated?

Domain: Developing Custom Agents

- A. Use MCP for standardized tool and resource access
- B. Use A2A for agent-to-agent interoperability
- C. Publish an Agent Card describing capabilities and endpoints
- D. Register agents and capabilities in Agent Registry

### 27. An agent needs structured access to an internal database, not another agent. What protocol fits?

Domain: Developing Custom Agents

- A. Use MCP for standardized tool and resource access
- B. Use A2A for agent-to-agent interoperability
- C. Bundle related skills, tools, and configuration as a plugin
- D. Govern agent traffic through Agent Gateway

### 28. A calling agent cannot discover a remote agent's endpoint or skills. What is missing?

Domain: Developing Custom Agents

- A. Register agents and capabilities in Agent Registry
- B. Publish an Agent Card describing capabilities and endpoints
- C. Use MCP for standardized tool and resource access
- D. Use A2A for agent-to-agent interoperability

### 29. A remote agent must not exceed the authority delegated by the caller. What should be implemented?

Domain: Developing Custom Agents

- A. Use A2A for agent-to-agent interoperability
- B. Use scoped OAuth 2.0 tokens for agent-to-tool calls
- C. Constrain access with a principal access boundary policy
- D. Govern agent traffic through Agent Gateway

### 30. Several agent frameworks need the same tool contract. What should be standardized?

Domain: Developing Custom Agents

- A. Expose approved capabilities through an MCP server
- B. Package reusable guidance and assets as a skill
- C. Bundle related skills, tools, and configuration as a plugin
- D. Use MCP for standardized tool and resource access

### 31. A task must be delegated to a specialist and the result reconciled. What pattern fits?

Domain: Developing Custom Agents

- A. Transfer control with explicit context and state
- B. Use A2A for agent-to-agent interoperability
- C. Run agents in a fixed sequence
- D. Run independent agents concurrently

### 32. A remote agent's skills change, but callers keep sending obsolete task types. What should be updated?

Domain: Developing Custom Agents

- A. Publish an Agent Card describing capabilities and endpoints
- B. Record agent actions and tool calls in audit logs
- C. Register agents and capabilities in Agent Registry
- D. Govern agent traffic through Agent Gateway

### 33. A design says "use A2A to give the agent a weather lookup tool." What is the correction?

Domain: Developing Custom Agents

- A. Package reusable guidance and assets as a skill
- B. Use MCP for standardized tool and resource access
- C. Publish an Agent Card describing capabilities and endpoints
- D. Use A2A for agent-to-agent interoperability

### 34. A multi-agent system needs a standard way to represent task state and messages. What should be defined?

Domain: Developing Custom Agents

- A. Register agents and capabilities in Agent Registry
- B. Use A2A for agent-to-agent interoperability
- C. Govern agent traffic through Agent Gateway
- D. Use MCP for standardized tool and resource access

### 35. A request must be classified and sent to the right specialist. What pattern fits?

Domain: Developing Custom Agents

- A. Repeat work until a defined stop condition is met
- B. Route a request to the most suitable specialist agent
- C. Run independent agents concurrently
- D. Transfer control with explicit context and state

### 36. A specialist returns partial work to the orchestrator. What should accompany the return?

Domain: Developing Custom Agents

- A. Route a request to the most suitable specialist agent
- B. Use a graph workflow for branching dependencies
- C. Run agents in a fixed sequence
- D. Transfer control with explicit context and state

### 37. Four independent analyses must be combined. What pattern reduces total latency?

Domain: Developing Custom Agents

- A. Run independent agents concurrently
- B. Run agents in a fixed sequence
- C. Repeat work until a defined stop condition is met
- D. Use a graph workflow for branching dependencies

### 38. A process has conditional branches that converge at a human approval. What pattern fits?

Domain: Developing Custom Agents

- A. Repeat work until a defined stop condition is met
- B. Use a graph workflow for branching dependencies
- C. Run agents in a fixed sequence
- D. Run independent agents concurrently

### 39. A refinement loop has no maximum iteration count. What is the risk?

Domain: Developing Custom Agents

- A. Route a request to the most suitable specialist agent
- B. Run independent agents concurrently
- C. Repeat work until a defined stop condition is met
- D. Run agents in a fixed sequence

### 40. A high-risk request should not follow the standard automated path. What pattern fits?

Domain: Developing Custom Agents

- A. Route a request to the most suitable specialist agent
- B. Run agents in a fixed sequence
- C. Run independent agents concurrently
- D. Transfer control with explicit context and state

### 41. Two agents update the same record concurrently. What should be designed?

Domain: Developing Custom Agents

- A. Use a graph workflow for branching dependencies
- B. Repeat work until a defined stop condition is met
- C. Run agents in a fixed sequence
- D. Run independent agents concurrently

### 42. A multi-stage workflow loses the evidence gathered in earlier stages. What should carry it?

Domain: Developing Custom Agents

- A. Pass files and large outputs as artifacts
- B. Persist conversation and task state in a session
- C. Transfer control with explicit context and state
- D. Store durable user or domain memory in Memory Bank

### 43. A team wants managed agent hosting with integrated sessions and memory services. What should it evaluate?

Domain: Developing Custom Agents

- A. Use Cloud SQL for relational state and transactions
- B. Deploy to Agent Runtime for managed agent hosting
- C. Use GKE when you need cluster-level control and custom orchestration
- D. Deploy to Cloud Run for containerized request-driven services

### 44. A stateless container service must scale to zero between requests. What fits?

Domain: Developing Custom Agents

- A. Deploy to Agent Runtime for managed agent hosting
- B. Use Cloud Workstations for managed developer environments
- C. Use GKE when you need cluster-level control and custom orchestration
- D. Deploy to Cloud Run for containerized request-driven services

### 45. A workload requires custom networking, node pools, and scheduling. What fits?

Domain: Developing Custom Agents

- A. Deploy to Agent Runtime for managed agent hosting
- B. Deploy to Cloud Run for containerized request-driven services
- C. Keep the service stateless and externalize session data
- D. Use GKE when you need cluster-level control and custom orchestration

### 46. Session data is stored in process memory and lost during rolling deployments. What should change?

Domain: Developing Custom Agents

- A. Pass files and large outputs as artifacts
- B. Use Memorystore for Redis for fast shared ephemeral state
- C. Keep the service stateless and externalize session data
- D. Persist sessions in a durable managed store

### 47. Several agents must follow the same tool-use policy. Where should it be enforced?

Domain: Developing Custom Agents

- A. Review high-impact actions with accountable owners
- B. Enforce a policy check before a consequential action
- C. Encode organizational policy in enforceable controls
- D. Require human approval before a consequential action

### 48. A conversational service needs low-latency per-session documents. What storage fits?

Domain: Developing Custom Agents

- A. Use Memorystore for Redis for fast shared ephemeral state
- B. Use Firestore for low-latency document-oriented state
- C. Persist sessions in a durable managed store
- D. Use Cloud SQL for relational state and transactions

### 49. An agent hits quota limits at peak concurrency. What should be planned?

Domain: Developing Custom Agents

- A. Provision capacity for peak concurrency and quotas
- B. Track token and tool cost per completed task
- C. Use staged rollout with measurable rollback criteria
- D. Set an end-to-end latency budget

### 50. A batch agent runs long asynchronous jobs. What should be evaluated?

Domain: Developing Custom Agents

- A. Set timeouts and bounded retries for tool calls
- B. Deploy to Cloud Run for containerized request-driven services
- C. Deploy to Agent Runtime for managed agent hosting
- D. Use GKE when you need cluster-level control and custom orchestration

### 51. A response is well cited but omits a required exception stated in a retrieved clause. What failed?

Domain: Developing Custom Agents

- A. Ground the response in cited retrieved evidence
- B. Evaluate tool-call trajectories, not only final text
- C. Score response correctness, completeness, and helpfulness
- D. Use a calibrated model-based autorater for scalable judgment

### 52. A relevant document is missing because of an overly strict metadata filter. What should be reviewed?

Domain: Developing Custom Agents

- A. Measure retrieval relevance and recall separately
- B. Filter retrieval by the requesting user's authorization
- C. Filter retrieval using trusted metadata
- D. Score response correctness, completeness, and helpfulness

### 53. An automated groundedness score is high for an answer built on an unreliable source. What is missing?

Domain: Developing Custom Agents

- A. Use a calibrated model-based autorater for scalable judgment
- B. Ground the response in cited retrieved evidence
- C. Set explicit pass thresholds before evaluating
- D. Use human review for unresolved or high-impact judgment

### 54. A retrieval service caches results without user context. What risk arises?

Domain: Developing Custom Agents

- A. Grant IAM roles to the agent identity, not to users' credentials
- B. Constrain access with a principal access boundary policy
- C. Govern agent traffic through Agent Gateway
- D. Filter retrieval by the requesting user's authorization

### 55. Two sources contradict each other and both are valid for different dates. What should the answer do?

Domain: Developing Custom Agents

- A. Ground the response in cited retrieved evidence
- B. Rerank retrieved passages before generation
- C. Preserve source and chunk identifiers through the pipeline
- D. Deduplicate near-identical retrieved chunks

### 56. A team wants to know whether a new chunking strategy caused better answers. What should it isolate?

Domain: Developing Custom Agents

- A. Measure retrieval relevance and recall separately
- B. Score response correctness, completeness, and helpfulness
- C. Track token and tool cost per completed task
- D. Evaluate tool-call trajectories, not only final text

### 57. A document's classification changed after indexing. What should happen?

Domain: Developing Custom Agents

- A. Filter retrieval by the requesting user's authorization
- B. Filter retrieval using trusted metadata
- C. Check index freshness and reindexing behavior
- D. Preserve source and chunk identifiers through the pipeline

### 58. A high-stakes answer is accurate but recommends an irreversible action. What control remains?

Domain: Developing Custom Agents

- A. Ground the response in cited retrieved evidence
- B. Use human review for unresolved or high-impact judgment
- C. Set explicit pass thresholds before evaluating
- D. Score response correctness, completeness, and helpfulness

### 59. A new agent is deployed with the default compute identity. What should change?

Domain: Developing Custom Agents

- A. Constrain access with a principal access boundary policy
- B. Give each agent its own managed identity
- C. Use scoped OAuth 2.0 tokens for agent-to-tool calls
- D. Grant IAM roles to the agent identity, not to users' credentials

### 60. A tool needs to call a Google API on behalf of a service, not a user. What identity pattern fits?

Domain: Developing Custom Agents

- A. Keep access tokens short-lived and narrowly scoped
- B. Use scoped OAuth 2.0 tokens for agent-to-tool calls
- C. Store secrets in Secret Manager rather than prompts or code
- D. Propagate the caller's identity to downstream tools

### 61. A boundary denies a resource the agent legitimately needs in production but not in test. What should be reviewed?

Domain: Developing Custom Agents

- A. Grant IAM roles to the agent identity, not to users' credentials
- B. Use VPC Service Controls to establish a data perimeter
- C. Constrain access with a principal access boundary policy
- D. Grant the minimum permissions required for the task

### 62. An agent identity is deleted while its credentials remain valid. What should happen?

Domain: Developing Custom Agents

- A. Give each agent its own managed identity
- B. Grant IAM roles to the agent identity, not to users' credentials
- C. Use a dedicated service account with least privilege
- D. Record agent actions and tool calls in audit logs

### 63. A remote agent calls a local tool but does not pass caller identity. What can go wrong?

Domain: Developing Custom Agents

- A. Govern agent traffic through Agent Gateway
- B. Propagate the caller's identity to downstream tools
- C. Publish an Agent Card describing capabilities and endpoints
- D. Use scoped OAuth 2.0 tokens for agent-to-tool calls

### 64. An agent role includes permissions inherited from a broad group. What should be checked?

Domain: Developing Custom Agents

- A. Constrain access with a principal access boundary policy
- B. Grant the minimum permissions required for the task
- C. Encode organizational policy in enforceable controls
- D. Grant IAM roles to the agent identity, not to users' credentials

### 65. A compliance review needs evidence of every identity used by an agent. What should be available?

Domain: Developing Custom Agents

- A. Record agent actions and tool calls in audit logs
- B. Register agents and capabilities in Agent Registry
- C. Give each agent its own managed identity
- D. Grant IAM roles to the agent identity, not to users' credentials

### 66. A boundary allows access to a dataset through one API but not another. What should be verified?

Domain: Developing Custom Agents

- A. Govern agent traffic through Agent Gateway
- B. Use scoped OAuth 2.0 tokens for agent-to-tool calls
- C. Constrain access with a principal access boundary policy
- D. Restrict outbound network access to approved destinations

### 67. An MCP server exposes a tool that returns raw database errors. What should change?

Domain: Developing Custom Agents

- A. Publish an Agent Card describing capabilities and endpoints
- B. Bundle related skills, tools, and configuration as a plugin
- C. Use MCP for standardized tool and resource access
- D. Expose approved capabilities through an MCP server

### 68. Two teams register agents with the same name. What should the registry enforce?

Domain: Developing Custom Agents

- A. Record agent actions and tool calls in audit logs
- B. Register agents and capabilities in Agent Registry
- C. Publish an Agent Card describing capabilities and endpoints
- D. Encode organizational policy in enforceable controls

### 69. An MCP server accepts unauthenticated requests from any agent. What should be added?

Domain: Developing Custom Agents

- A. Expose approved capabilities through an MCP server
- B. Use scoped OAuth 2.0 tokens for agent-to-tool calls
- C. Use MCP for standardized tool and resource access
- D. Constrain access with a principal access boundary policy

### 70. A plugin bundles a tool with broad data access. What should review verify?

Domain: Developing Custom Agents

- A. Provide persistent coding guidance for a coding agent
- B. Run deterministic logic when a lifecycle event fires
- C. Bundle related skills, tools, and configuration as a plugin
- D. Package reusable guidance and assets as a skill

### 71. A remote agent has no published security scheme. What should callers do?

Domain: Developing Custom Agents

- A. Register agents and capabilities in Agent Registry
- B. Use A2A for agent-to-agent interoperability
- C. Publish an Agent Card describing capabilities and endpoints
- D. Use MCP for standardized tool and resource access

### 72. A registry entry points to a decommissioned endpoint. What should happen?

Domain: Developing Custom Agents

- A. Govern agent traffic through Agent Gateway
- B. Encode organizational policy in enforceable controls
- C. Record agent actions and tool calls in audit logs
- D. Register agents and capabilities in Agent Registry

### 73. An MCP server returns content from an untrusted external source. What should the agent do?

Domain: Developing Custom Agents

- A. Govern agent traffic through Agent Gateway
- B. Screen prompts and responses with Model Armor
- C. Inspect and de-identify sensitive data with Sensitive Data Protection
- D. Use MCP for standardized tool and resource access

### 74. A capability is distributed as a plugin without version pinning. What risk arises?

Domain: Developing Custom Agents

- A. Bundle related skills, tools, and configuration as a plugin
- B. Package reusable guidance and assets as a skill
- C. Publish an Agent Card describing capabilities and endpoints
- D. Register agents and capabilities in Agent Registry

### 75. A remote agent requires delegated user authority. What should the request carry?

Domain: Developing Custom Agents

- A. Publish an Agent Card describing capabilities and endpoints
- B. Use scoped OAuth 2.0 tokens for agent-to-tool calls
- C. Use A2A for agent-to-agent interoperability
- D. Govern agent traffic through Agent Gateway

### 76. An A2A task needs progress updates and a final result. What should the contract define?

Domain: Developing Custom Agents

- A. Use MCP for standardized tool and resource access
- B. Use A2A for agent-to-agent interoperability
- C. Register agents and capabilities in Agent Registry
- D. Publish an Agent Card describing capabilities and endpoints

### 77. A remote agent claims capabilities broader than its authorization. What is the risk?

Domain: Developing Custom Agents

- A. Use MCP for standardized tool and resource access
- B. Bundle related skills, tools, and configuration as a plugin
- C. Use A2A for agent-to-agent interoperability
- D. Publish an Agent Card describing capabilities and endpoints

### 78. A remote agent is outside the organization's trust boundary. What should be enforced?

Domain: Developing Custom Agents

- A. Govern agent traffic through Agent Gateway
- B. Encode organizational policy in enforceable controls
- C. Constrain access with a principal access boundary policy
- D. Use A2A for agent-to-agent interoperability

### 79. A tool server must distinguish read and write permissions. What should it enforce?

Domain: Developing Custom Agents

- A. Expose approved capabilities through an MCP server
- B. Propagate the caller's identity to downstream tools
- C. Use scoped OAuth 2.0 tokens for agent-to-tool calls
- D. Use MCP for standardized tool and resource access

### 80. A task delegates to a remote agent that cannot complete it. What should the contract provide?

Domain: Developing Custom Agents

- A. Transfer control with explicit context and state
- B. Run agents in a fixed sequence
- C. Use A2A for agent-to-agent interoperability
- D. Run independent agents concurrently

### 81. A remote agent silently changes its endpoint. What should be monitored?

Domain: Developing Custom Agents

- A. Record agent actions and tool calls in audit logs
- B. Register agents and capabilities in Agent Registry
- C. Publish an Agent Card describing capabilities and endpoints
- D. Govern agent traffic through Agent Gateway

### 82. A protocol message contains instructions that attempt to escalate privileges. What should happen?

Domain: Developing Custom Agents

- A. Use MCP for standardized tool and resource access
- B. Use A2A for agent-to-agent interoperability
- C. Publish an Agent Card describing capabilities and endpoints
- D. Screen prompts and responses with Model Armor

### 83. A request needs two specialists whose results must be merged. What pattern fits?

Domain: Developing Custom Agents

- A. Transfer control with explicit context and state
- B. Route a request to the most suitable specialist agent
- C. Use a graph workflow for branching dependencies
- D. Run independent agents concurrently

### 84. A workflow must stop and wait for a human decision before continuing. What state design fits?

Domain: Developing Custom Agents

- A. Run independent agents concurrently
- B. Use a graph workflow for branching dependencies
- C. Repeat work until a defined stop condition is met
- D. Run agents in a fixed sequence

### 85. A retry loop repeatedly sends the same failing request to a specialist. What should change?

Domain: Developing Custom Agents

- A. Run independent agents concurrently
- B. Repeat work until a defined stop condition is met
- C. Route a request to the most suitable specialist agent
- D. Transfer control with explicit context and state

### 86. An agent hands off a task without the original constraints. What should the handoff include?

Domain: Developing Custom Agents

- A. Run agents in a fixed sequence
- B. Transfer control with explicit context and state
- C. Route a request to the most suitable specialist agent
- D. Use a graph workflow for branching dependencies

### 87. A workflow's graph has a cycle with no exit condition. What should be added?

Domain: Developing Custom Agents

- A. Use a graph workflow for branching dependencies
- B. Run independent agents concurrently
- C. Run agents in a fixed sequence
- D. Repeat work until a defined stop condition is met

### 88. A router sends high-risk cases to the same fast path as low-risk ones. What should change?

Domain: Developing Custom Agents

- A. Route a request to the most suitable specialist agent
- B. Run independent agents concurrently
- C. Run agents in a fixed sequence
- D. Transfer control with explicit context and state

### 89. Two parallel agents produce conflicting recommendations. What should the workflow do?

Domain: Developing Custom Agents

- A. Run agents in a fixed sequence
- B. Use a graph workflow for branching dependencies
- C. Transfer control with explicit context and state
- D. Run independent agents concurrently

### 90. A planner and executor exchange tasks indefinitely. What should bound the interaction?

Domain: Developing Custom Agents

- A. Route a request to the most suitable specialist agent
- B. Run independent agents concurrently
- C. Repeat work until a defined stop condition is met
- D. Run agents in a fixed sequence

### 91. A handoff includes a large dataset by pasting it into the prompt. What is the better approach?

Domain: Developing Custom Agents

- A. Transfer control with explicit context and state
- B. Persist conversation and task state in a session
- C. Store durable user or domain memory in Memory Bank
- D. Pass files and large outputs as artifacts

### 92. A managed agent runtime is selected for a simple stateless service. What trade-off should be reviewed?

Domain: Developing Custom Agents

- A. Deploy to Cloud Run for containerized request-driven services
- B. Deploy to Agent Runtime for managed agent hosting
- C. Use GKE when you need cluster-level control and custom orchestration
- D. Provision capacity for peak concurrency and quotas

### 93. A request-driven agent exceeds serverless timeout limits during long tools. What should be designed?

Domain: Developing Custom Agents

- A. Deploy to Agent Runtime for managed agent hosting
- B. Use GKE when you need cluster-level control and custom orchestration
- C. Set timeouts and bounded retries for tool calls
- D. Deploy to Cloud Run for containerized request-driven services

### 94. A service needs conversation state shared across regions. What should be designed?

Domain: Developing Custom Agents

- A. Use Memorystore for Redis for fast shared ephemeral state
- B. Use Firestore for low-latency document-oriented state
- C. Keep the service stateless and externalize session data
- D. Persist sessions in a durable managed store

### 95. An agent policy is enforced only inside the agent code. What is the risk?

Domain: Developing Custom Agents

- A. Register agents and capabilities in Agent Registry
- B. Encode organizational policy in enforceable controls
- C. Govern agent traffic through Agent Gateway
- D. Give each agent its own managed identity

### 96. A new agent version increases per-request model calls. What should be evaluated before rollout?

Domain: Developing Custom Agents

- A. Provision capacity for peak concurrency and quotas
- B. Use staged rollout with measurable rollback criteria
- C. Set an end-to-end latency budget
- D. Track token and tool cost per completed task

### 97. A team needs GPUs for self-hosted model inference inside its cluster. What fits?

Domain: Developing Custom Agents

- A. Use GKE when you need cluster-level control and custom orchestration
- B. Use Cloud SQL for relational state and transactions
- C. Deploy to Cloud Run for containerized request-driven services
- D. Deploy to Agent Runtime for managed agent hosting

### 98. A shared cache holds session data without encryption or TTL. What should be configured?

Domain: Developing Custom Agents

- A. Use Cloud Storage for large artifacts and source documents
- B. Persist sessions in a durable managed store
- C. Use BigQuery for governed analytical access to enterprise data
- D. Use Memorystore for Redis for fast shared ephemeral state

### 99. A managed runtime imposes concurrency limits lower than expected traffic. What should be planned?

Domain: Developing Custom Agents

- A. Deploy to Agent Runtime for managed agent hosting
- B. Provision capacity for peak concurrency and quotas
- C. Keep the service stateless and externalize session data
- D. Deploy to Cloud Run for containerized request-driven services

### 100. An agent bypasses a shared policy by calling a tool directly. What should be changed?

Domain: Developing Custom Agents

- A. Encode organizational policy in enforceable controls
- B. Record agent actions and tool calls in audit logs
- C. Govern agent traffic through Agent Gateway
- D. Enforce a policy check before a consequential action

---

## Answer key and explanations

### Question 1 — B

Answer: Filter retrieval by the requesting user's authorization. Authorization and tenant filters based on the requesting identity. Access checks must occur before content enters the model context. Relevance never overrides permission. Local study-map skill 3.6 (Retrieval Authorization and Evidence Quality), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Metadata such as tenant, date, or classification can enforce scope and freshness. Metadata must itself be trustworthy. In this case: Authorization and tenant filters based on the requesting identity.
- **B:** Correct. Access checks must occur before content enters the model context. Relevance never overrides permission. In this case: Authorization and tenant filters based on the requesting identity.
- **C:** Incorrect for this question. Duplicates waste context and can overweight one source. Deduplication improves diversity of evidence. In this case: Authorization and tenant filters based on the requesting identity.
- **D:** Incorrect for this question. Similarity ranking surfaces potentially relevant content. It does not prove relevance or factual support. In this case: Authorization and tenant filters based on the requesting identity.

### Question 2 — D

Answer: Measure retrieval relevance and recall separately. Whether irrelevant or conflicting passages are crowding out the needed evidence. Generation cannot compensate for missing evidence. Retrieval metrics localize pipeline failures. Local study-map skill 3.6 (Retrieval Authorization and Evidence Quality), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A correct answer can hide an unsafe or wasteful action sequence. Trajectory checks verify which tools were called and with what arguments. In this case: Whether irrelevant or conflicting passages are crowding out the needed evidence.
- **B:** Incorrect for this question. Response metrics assess what the user receives. They should be tied to explicit task criteria. In this case: Whether irrelevant or conflicting passages are crowding out the needed evidence.
- **C:** Incorrect for this question. Cost attribution supports optimization and budgeting. Per-task cost reveals expensive failure paths. In this case: Whether irrelevant or conflicting passages are crowding out the needed evidence.
- **D:** Correct. Generation cannot compensate for missing evidence. Retrieval metrics localize pipeline failures. In this case: Whether irrelevant or conflicting passages are crowding out the needed evidence.

### Question 3 — D

Answer: Ground the response in cited retrieved evidence. A claim-level citation tied to a preserved chunk identifier. Citations let users check claims against sources. Grounding reduces but does not eliminate hallucination. Local study-map skill 3.6 (Retrieval Authorization and Evidence Quality), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Similarity ranking surfaces potentially relevant content. It does not prove relevance or factual support. In this case: A claim-level citation tied to a preserved chunk identifier.
- **B:** Incorrect for this question. A reranker can improve precision after broad recall. It adds latency and still needs evaluation. In this case: A claim-level citation tied to a preserved chunk identifier.
- **C:** Incorrect for this question. Identifiers support citation, debugging, and access checks. Losing them makes evidence untraceable. In this case: A claim-level citation tied to a preserved chunk identifier.
- **D:** Correct. Citations let users check claims against sources. Grounding reduces but does not eliminate hallucination. In this case: A claim-level citation tied to a preserved chunk identifier.

### Question 4 — D

Answer: Check index freshness and reindexing behavior. Source-to-index deletion handling and freshness verification. Stale indexes produce outdated answers. Define update frequency and verify that deletions propagate. Local study-map skill 3.6 (Retrieval Authorization and Evidence Quality), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Metadata such as tenant, date, or classification can enforce scope and freshness. Metadata must itself be trustworthy. In this case: Source-to-index deletion handling and freshness verification.
- **B:** Incorrect for this question. Duplicates waste context and can overweight one source. Deduplication improves diversity of evidence. In this case: Source-to-index deletion handling and freshness verification.
- **C:** Incorrect for this question. A reranker can improve precision after broad recall. It adds latency and still needs evaluation. In this case: Source-to-index deletion handling and freshness verification.
- **D:** Correct. Stale indexes produce outdated answers. Define update frequency and verify that deletions propagate. In this case: Source-to-index deletion handling and freshness verification.

### Question 5 — A

Answer: Use human review for unresolved or high-impact judgment. Calibrate the autorater against human judgments and adjust thresholds. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. Local study-map skill 3.6 (Retrieval Authorization and Evidence Quality), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. In this case: Calibrate the autorater against human judgments and adjust thresholds.
- **B:** Incorrect for this question. Autoraters can score nuanced qualities at scale. They require calibration against human judgments and periodic review. In this case: Calibrate the autorater against human judgments and adjust thresholds.
- **C:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Calibrate the autorater against human judgments and adjust thresholds.
- **D:** Incorrect for this question. Citations let users check claims against sources. Grounding reduces but does not eliminate hallucination. In this case: Calibrate the autorater against human judgments and adjust thresholds.

### Question 6 — A

Answer: Filter retrieval by the requesting user's authorization. Section-level authorization before content is assembled into context. Access checks must occur before content enters the model context. Relevance never overrides permission. Local study-map skill 3.6 (Retrieval Authorization and Evidence Quality), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Access checks must occur before content enters the model context. Relevance never overrides permission. In this case: Section-level authorization before content is assembled into context.
- **B:** Incorrect for this question. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: Section-level authorization before content is assembled into context.
- **C:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Section-level authorization before content is assembled into context.
- **D:** Incorrect for this question. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: Section-level authorization before content is assembled into context.

### Question 7 — C

Answer: Measure retrieval relevance and recall separately. Retrieval relevance and recall alongside response correctness. Generation cannot compensate for missing evidence. Retrieval metrics localize pipeline failures. Local study-map skill 3.6 (Retrieval Authorization and Evidence Quality), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A correct answer can hide an unsafe or wasteful action sequence. Trajectory checks verify which tools were called and with what arguments. In this case: Retrieval relevance and recall alongside response correctness.
- **B:** Incorrect for this question. Response metrics assess what the user receives. They should be tied to explicit task criteria. In this case: Retrieval relevance and recall alongside response correctness.
- **C:** Correct. Generation cannot compensate for missing evidence. Retrieval metrics localize pipeline failures. In this case: Retrieval relevance and recall alongside response correctness.
- **D:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Retrieval relevance and recall alongside response correctness.

### Question 8 — C

Answer: Ground the response in cited retrieved evidence. Route the recommendation to the accountable approver before execution. Citations let users check claims against sources. Grounding reduces but does not eliminate hallucination. Local study-map skill 3.6 (Retrieval Authorization and Evidence Quality), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Response metrics assess what the user receives. They should be tied to explicit task criteria. In this case: Route the recommendation to the accountable approver before execution.
- **B:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Route the recommendation to the accountable approver before execution.
- **C:** Correct. Citations let users check claims against sources. Grounding reduces but does not eliminate hallucination. In this case: Route the recommendation to the accountable approver before execution.
- **D:** Incorrect for this question. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. In this case: Route the recommendation to the accountable approver before execution.

### Question 9 — B

Answer: Filter retrieval using trusted metadata. Normalize and validate metadata, or exclude unfilterable content. Metadata such as tenant, date, or classification can enforce scope and freshness. Metadata must itself be trustworthy. Local study-map skill 3.6 (Retrieval Authorization and Evidence Quality), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Duplicates waste context and can overweight one source. Deduplication improves diversity of evidence. In this case: Normalize and validate metadata, or exclude unfilterable content.
- **B:** Correct. Metadata such as tenant, date, or classification can enforce scope and freshness. Metadata must itself be trustworthy. In this case: Normalize and validate metadata, or exclude unfilterable content.
- **C:** Incorrect for this question. Stale indexes produce outdated answers. Define update frequency and verify that deletions propagate. In this case: Normalize and validate metadata, or exclude unfilterable content.
- **D:** Incorrect for this question. Identifiers support citation, debugging, and access checks. Losing them makes evidence untraceable. In this case: Normalize and validate metadata, or exclude unfilterable content.

### Question 10 — A

Answer: Give each agent its own managed identity. Distinct agent identities with attributable authorization. Distinct identity makes access attributable and auditable. Sharing a human or broad service identity weakens least privilege. Local study-map skill 3.7 (Agent Identity and Permissions), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Distinct identity makes access attributable and auditable. Sharing a human or broad service identity weakens least privilege. In this case: Distinct agent identities with attributable authorization.
- **B:** Incorrect for this question. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: Distinct agent identities with attributable authorization.
- **C:** Incorrect for this question. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: Distinct agent identities with attributable authorization.
- **D:** Incorrect for this question. A dedicated identity separates the agent from human accounts and limits blast radius. Roles still need review and periodic reduction. In this case: Distinct agent identities with attributable authorization.

### Question 11 — A

Answer: Constrain access with a principal access boundary policy. A narrow role on the specific resource and a boundary that limits reach. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. Local study-map skill 3.7 (Agent Identity and Permissions), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: A narrow role on the specific resource and a boundary that limits reach.
- **B:** Incorrect for this question. Narrow roles and scopes reduce blast radius. Review permissions as the workflow evolves. In this case: A narrow role on the specific resource and a boundary that limits reach.
- **C:** Incorrect for this question. A service perimeter can reduce exfiltration paths for supported services. It complements, rather than replaces, IAM and application checks. In this case: A narrow role on the specific resource and a boundary that limits reach.
- **D:** Incorrect for this question. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: A narrow role on the specific resource and a boundary that limits reach.

### Question 12 — B

Answer: Use scoped OAuth 2.0 tokens for agent-to-tool calls. A short-lived, scoped token representing the delegated authority. Short-lived, scoped tokens limit what a tool call can do. Token handling and refresh must avoid broad standing access. Local study-map skill 3.7 (Agent Identity and Permissions), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Short lifetimes and audience limits reduce misuse. Tokens should not be placed in prompts or logs. In this case: A short-lived, scoped token representing the delegated authority.
- **B:** Correct. Short-lived, scoped tokens limit what a tool call can do. Token handling and refresh must avoid broad standing access. In this case: A short-lived, scoped token representing the delegated authority.
- **C:** Incorrect for this question. Managed secret storage supports rotation and access control. A prompt instruction is not a secret-protection mechanism. In this case: A short-lived, scoped token representing the delegated authority.
- **D:** Incorrect for this question. Downstream authorization needs the actual principal, not a generic agent identity. Delegation must be explicit and scoped. In this case: A short-lived, scoped token representing the delegated authority.

### Question 13 — C

Answer: Propagate the caller's identity to downstream tools. Verified caller identity through the tool chain. Downstream authorization needs the actual principal, not a generic agent identity. Delegation must be explicit and scoped. Local study-map skill 3.7 (Agent Identity and Permissions), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A dedicated identity separates the agent from human accounts and limits blast radius. Roles still need review and periodic reduction. In this case: Verified caller identity through the tool chain.
- **B:** Incorrect for this question. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: Verified caller identity through the tool chain.
- **C:** Correct. Downstream authorization needs the actual principal, not a generic agent identity. Delegation must be explicit and scoped. In this case: Verified caller identity through the tool chain.
- **D:** Incorrect for this question. Distinct identity makes access attributable and auditable. Sharing a human or broad service identity weakens least privilege. In this case: Verified caller identity through the tool chain.

### Question 14 — D

Answer: Use VPC Service Controls to establish a data perimeter. Investigate the required path and update the boundary through approved change control. A service perimeter can reduce exfiltration paths for supported services. It complements, rather than replaces, IAM and application checks. Local study-map skill 3.7 (Agent Identity and Permissions), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: Investigate the required path and update the boundary through approved change control.
- **B:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Investigate the required path and update the boundary through approved change control.
- **C:** Incorrect for this question. Egress controls reduce exfiltration and unauthorized tool reach. They should be paired with identity and data controls. In this case: Investigate the required path and update the boundary through approved change control.
- **D:** Correct. A service perimeter can reduce exfiltration paths for supported services. It complements, rather than replaces, IAM and application checks. In this case: Investigate the required path and update the boundary through approved change control.

### Question 15 — C

Answer: Grant the minimum permissions required for the task. Review and reduce permissions to the current required set. Narrow roles and scopes reduce blast radius. Review permissions as the workflow evolves. Local study-map skill 3.7 (Agent Identity and Permissions), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Review and reduce permissions to the current required set.
- **B:** Incorrect for this question. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: Review and reduce permissions to the current required set.
- **C:** Correct. Narrow roles and scopes reduce blast radius. Review permissions as the workflow evolves. In this case: Review and reduce permissions to the current required set.
- **D:** Incorrect for this question. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: Review and reduce permissions to the current required set.

### Question 16 — A

Answer: Store secrets in Secret Manager rather than prompts or code. Move it to managed secret storage, rotate it, and remove it from logs. Managed secret storage supports rotation and access control. A prompt instruction is not a secret-protection mechanism. Local study-map skill 3.7 (Agent Identity and Permissions), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Managed secret storage supports rotation and access control. A prompt instruction is not a secret-protection mechanism. In this case: Move it to managed secret storage, rotate it, and remove it from logs.
- **B:** Incorrect for this question. Distinct identity makes access attributable and auditable. Sharing a human or broad service identity weakens least privilege. In this case: Move it to managed secret storage, rotate it, and remove it from logs.
- **C:** Incorrect for this question. Short lifetimes and audience limits reduce misuse. Tokens should not be placed in prompts or logs. In this case: Move it to managed secret storage, rotate it, and remove it from logs.
- **D:** Incorrect for this question. Short-lived, scoped tokens limit what a tool call can do. Token handling and refresh must avoid broad standing access. In this case: Move it to managed secret storage, rotate it, and remove it from logs.

### Question 17 — D

Answer: Constrain access with a principal access boundary policy. A principal access boundary that constrains the identity to approved resources. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. Local study-map skill 3.7 (Agent Identity and Permissions), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: A principal access boundary that constrains the identity to approved resources.
- **B:** Incorrect for this question. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: A principal access boundary that constrains the identity to approved resources.
- **C:** Incorrect for this question. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: A principal access boundary that constrains the identity to approved resources.
- **D:** Correct. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: A principal access boundary that constrains the identity to approved resources.

### Question 18 — C

Answer: Register agents and capabilities in Agent Registry. Agent Registry entries with ownership and capability metadata. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. Local study-map skill 3.8 (Registry and Capability Integration), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. In this case: Agent Registry entries with ownership and capability metadata.
- **B:** Incorrect for this question. Plugins make a capability set reusable across projects. Bundling does not remove the need to review each included permission and dependency. In this case: Agent Registry entries with ownership and capability metadata.
- **C:** Correct. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: Agent Registry entries with ownership and capability metadata.
- **D:** Incorrect for this question. MCP provides a common interface between agents and capability servers. Server trust, scopes, and validation remain your responsibility. In this case: Agent Registry entries with ownership and capability metadata.

### Question 19 — B

Answer: Use MCP for standardized tool and resource access. An MCP server with scoped tools and validation. MCP provides a common interface between agents and capability servers. Server trust, scopes, and validation remain your responsibility. Local study-map skill 3.8 (Registry and Capability Integration), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. In this case: An MCP server with scoped tools and validation.
- **B:** Correct. MCP provides a common interface between agents and capability servers. Server trust, scopes, and validation remain your responsibility. In this case: An MCP server with scoped tools and validation.
- **C:** Incorrect for this question. A2A supports discovery and task exchange between agents that may be built on different stacks. Trust and authorization still need explicit design. In this case: An MCP server with scoped tools and validation.
- **D:** Incorrect for this question. A skill can carry instructions, examples, and supporting files for a recurring task. It guides behavior but does not itself enforce permissions. In this case: An MCP server with scoped tools and validation.

### Question 20 — D

Answer: Publish an Agent Card describing capabilities and endpoints. The remote agent's Agent Card and approved registry metadata. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. Local study-map skill 3.8 (Registry and Capability Integration), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. MCP provides a common interface between agents and capability servers. Server trust, scopes, and validation remain your responsibility. In this case: The remote agent's Agent Card and approved registry metadata.
- **B:** Incorrect for this question. A2A supports discovery and task exchange between agents that may be built on different stacks. Trust and authorization still need explicit design. In this case: The remote agent's Agent Card and approved registry metadata.
- **C:** Incorrect for this question. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: The remote agent's Agent Card and approved registry metadata.
- **D:** Correct. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. In this case: The remote agent's Agent Card and approved registry metadata.

### Question 21 — C

Answer: Bundle related skills, tools, and configuration as a plugin. A versioned plugin with reviewed dependencies. Plugins make a capability set reusable across projects. Bundling does not remove the need to review each included permission and dependency. Local study-map skill 3.8 (Registry and Capability Integration), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Rules communicate conventions and constraints for generated changes. They are guidance; merge controls and tests remain the enforcement boundary. In this case: A versioned plugin with reviewed dependencies.
- **B:** Incorrect for this question. A skill can carry instructions, examples, and supporting files for a recurring task. It guides behavior but does not itself enforce permissions. In this case: A versioned plugin with reviewed dependencies.
- **C:** Correct. Plugins make a capability set reusable across projects. Bundling does not remove the need to review each included permission and dependency. In this case: A versioned plugin with reviewed dependencies.
- **D:** Incorrect for this question. Hooks can enforce checks, logging, or formatting at defined points. They are useful precisely because they do not depend on model discretion. In this case: A versioned plugin with reviewed dependencies.

### Question 22 — C

Answer: Expose approved capabilities through an MCP server. Caller authorization, input validation, and an audit trail. An MCP server provides a governed interface to tools, resources, or prompts. The server must enforce its own authorization and input validation. Local study-map skill 3.8 (Registry and Capability Integration), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: Caller authorization, input validation, and an audit trail.
- **B:** Incorrect for this question. MCP provides a common interface between agents and capability servers. Server trust, scopes, and validation remain your responsibility. In this case: Caller authorization, input validation, and an audit trail.
- **C:** Correct. An MCP server provides a governed interface to tools, resources, or prompts. The server must enforce its own authorization and input validation. In this case: Caller authorization, input validation, and an audit trail.
- **D:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Caller authorization, input validation, and an audit trail.

### Question 23 — D

Answer: Register agents and capabilities in Agent Registry. Retire the registry entry and revoke its access. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. Local study-map skill 3.8 (Registry and Capability Integration), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Retire the registry entry and revoke its access.
- **B:** Incorrect for this question. Distinct identity makes access attributable and auditable. Sharing a human or broad service identity weakens least privilege. In this case: Retire the registry entry and revoke its access.
- **C:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Retire the registry entry and revoke its access.
- **D:** Correct. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: Retire the registry entry and revoke its access.

### Question 24 — C

Answer: Use MCP for standardized tool and resource access. The MCP primitives map to tools for actions, resources for content, and prompts for reusable templates. MCP provides a common interface between agents and capability servers. Server trust, scopes, and validation remain your responsibility. Local study-map skill 3.8 (Registry and Capability Integration), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Plugins make a capability set reusable across projects. Bundling does not remove the need to review each included permission and dependency. In this case: The MCP primitives map to tools for actions, resources for content, and prompts for reusable templates.
- **B:** Incorrect for this question. A skill can carry instructions, examples, and supporting files for a recurring task. It guides behavior but does not itself enforce permissions. In this case: The MCP primitives map to tools for actions, resources for content, and prompts for reusable templates.
- **C:** Correct. MCP provides a common interface between agents and capability servers. Server trust, scopes, and validation remain your responsibility. In this case: The MCP primitives map to tools for actions, resources for content, and prompts for reusable templates.
- **D:** Incorrect for this question. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. In this case: The MCP primitives map to tools for actions, resources for content, and prompts for reusable templates.

### Question 25 — D

Answer: Publish an Agent Card describing capabilities and endpoints. Callers may route tasks incorrectly, so capability metadata must be maintained and tested. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. Local study-map skill 3.8 (Registry and Capability Integration), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: Callers may route tasks incorrectly, so capability metadata must be maintained and tested.
- **B:** Incorrect for this question. A2A supports discovery and task exchange between agents that may be built on different stacks. Trust and authorization still need explicit design. In this case: Callers may route tasks incorrectly, so capability metadata must be maintained and tested.
- **C:** Incorrect for this question. MCP provides a common interface between agents and capability servers. Server trust, scopes, and validation remain your responsibility. In this case: Callers may route tasks incorrectly, so capability metadata must be maintained and tested.
- **D:** Correct. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. In this case: Callers may route tasks incorrectly, so capability metadata must be maintained and tested.

### Question 26 — B

Answer: Use A2A for agent-to-agent interoperability. A2A task exchange with explicit status and result handling. A2A supports discovery and task exchange between agents that may be built on different stacks. Trust and authorization still need explicit design. Local study-map skill 3.9 (Agent-to-Agent Protocols), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. MCP provides a common interface between agents and capability servers. Server trust, scopes, and validation remain your responsibility. In this case: A2A task exchange with explicit status and result handling.
- **B:** Correct. A2A supports discovery and task exchange between agents that may be built on different stacks. Trust and authorization still need explicit design. In this case: A2A task exchange with explicit status and result handling.
- **C:** Incorrect for this question. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. In this case: A2A task exchange with explicit status and result handling.
- **D:** Incorrect for this question. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: A2A task exchange with explicit status and result handling.

### Question 27 — A

Answer: Use MCP for standardized tool and resource access. MCP tools exposed by a governed server. MCP provides a common interface between agents and capability servers. Server trust, scopes, and validation remain your responsibility. Local study-map skill 3.9 (Agent-to-Agent Protocols), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. MCP provides a common interface between agents and capability servers. Server trust, scopes, and validation remain your responsibility. In this case: MCP tools exposed by a governed server.
- **B:** Incorrect for this question. A2A supports discovery and task exchange between agents that may be built on different stacks. Trust and authorization still need explicit design. In this case: MCP tools exposed by a governed server.
- **C:** Incorrect for this question. Plugins make a capability set reusable across projects. Bundling does not remove the need to review each included permission and dependency. In this case: MCP tools exposed by a governed server.
- **D:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: MCP tools exposed by a governed server.

### Question 28 — B

Answer: Publish an Agent Card describing capabilities and endpoints. Callers need published Agent Card metadata to discover the remote endpoint and supported skills. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. Local study-map skill 3.9 (Agent-to-Agent Protocols), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: Callers need published Agent Card metadata to discover the remote endpoint and supported skills.
- **B:** Correct. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. In this case: Callers need published Agent Card metadata to discover the remote endpoint and supported skills.
- **C:** Incorrect for this question. MCP provides a common interface between agents and capability servers. Server trust, scopes, and validation remain your responsibility. In this case: Callers need published Agent Card metadata to discover the remote endpoint and supported skills.
- **D:** Incorrect for this question. A2A supports discovery and task exchange between agents that may be built on different stacks. Trust and authorization still need explicit design. In this case: Callers need published Agent Card metadata to discover the remote endpoint and supported skills.

### Question 29 — A

Answer: Use A2A for agent-to-agent interoperability. Scoped delegation and authorization at the remote boundary. A2A supports discovery and task exchange between agents that may be built on different stacks. Trust and authorization still need explicit design. Local study-map skill 3.9 (Agent-to-Agent Protocols), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. A2A supports discovery and task exchange between agents that may be built on different stacks. Trust and authorization still need explicit design. In this case: Scoped delegation and authorization at the remote boundary.
- **B:** Incorrect for this question. Short-lived, scoped tokens limit what a tool call can do. Token handling and refresh must avoid broad standing access. In this case: Scoped delegation and authorization at the remote boundary.
- **C:** Incorrect for this question. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: Scoped delegation and authorization at the remote boundary.
- **D:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Scoped delegation and authorization at the remote boundary.

### Question 30 — D

Answer: Use MCP for standardized tool and resource access. An MCP server exposing a consistent interface. MCP provides a common interface between agents and capability servers. Server trust, scopes, and validation remain your responsibility. Local study-map skill 3.9 (Agent-to-Agent Protocols), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. An MCP server provides a governed interface to tools, resources, or prompts. The server must enforce its own authorization and input validation. In this case: An MCP server exposing a consistent interface.
- **B:** Incorrect for this question. A skill can carry instructions, examples, and supporting files for a recurring task. It guides behavior but does not itself enforce permissions. In this case: An MCP server exposing a consistent interface.
- **C:** Incorrect for this question. Plugins make a capability set reusable across projects. Bundling does not remove the need to review each included permission and dependency. In this case: An MCP server exposing a consistent interface.
- **D:** Correct. MCP provides a common interface between agents and capability servers. Server trust, scopes, and validation remain your responsibility. In this case: An MCP server exposing a consistent interface.

### Question 31 — B

Answer: Use A2A for agent-to-agent interoperability. An agent-to-agent exchange with explicit result handling. A2A supports discovery and task exchange between agents that may be built on different stacks. Trust and authorization still need explicit design. Local study-map skill 3.9 (Agent-to-Agent Protocols), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A handoff should carry the goal, verified facts, permissions, and open questions. Implicit context is easily lost between agents. In this case: An agent-to-agent exchange with explicit result handling.
- **B:** Correct. A2A supports discovery and task exchange between agents that may be built on different stacks. Trust and authorization still need explicit design. In this case: An agent-to-agent exchange with explicit result handling.
- **C:** Incorrect for this question. Sequential workflows make dependencies explicit and are easier to reason about. They may add latency when steps could run independently. In this case: An agent-to-agent exchange with explicit result handling.
- **D:** Incorrect for this question. Parallel branches reduce wall-clock time when work is truly independent. Shared state and reconciliation still require design. In this case: An agent-to-agent exchange with explicit result handling.

### Question 32 — A

Answer: Publish an Agent Card describing capabilities and endpoints. Its Agent Card and registry entry. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. Local study-map skill 3.9 (Agent-to-Agent Protocols), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. In this case: Its Agent Card and registry entry.
- **B:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Its Agent Card and registry entry.
- **C:** Incorrect for this question. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: Its Agent Card and registry entry.
- **D:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Its Agent Card and registry entry.

### Question 33 — B

Answer: Use MCP for standardized tool and resource access. Tool access belongs to MCP; A2A is for agent interoperability. MCP provides a common interface between agents and capability servers. Server trust, scopes, and validation remain your responsibility. Local study-map skill 3.9 (Agent-to-Agent Protocols), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A skill can carry instructions, examples, and supporting files for a recurring task. It guides behavior but does not itself enforce permissions. In this case: Tool access belongs to MCP; A2A is for agent interoperability.
- **B:** Correct. MCP provides a common interface between agents and capability servers. Server trust, scopes, and validation remain your responsibility. In this case: Tool access belongs to MCP; A2A is for agent interoperability.
- **C:** Incorrect for this question. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. In this case: Tool access belongs to MCP; A2A is for agent interoperability.
- **D:** Incorrect for this question. A2A supports discovery and task exchange between agents that may be built on different stacks. Trust and authorization still need explicit design. In this case: Tool access belongs to MCP; A2A is for agent interoperability.

### Question 34 — B

Answer: Use A2A for agent-to-agent interoperability. An interoperable task and message contract within the chosen protocol. A2A supports discovery and task exchange between agents that may be built on different stacks. Trust and authorization still need explicit design. Local study-map skill 3.9 (Agent-to-Agent Protocols), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: An interoperable task and message contract within the chosen protocol.
- **B:** Correct. A2A supports discovery and task exchange between agents that may be built on different stacks. Trust and authorization still need explicit design. In this case: An interoperable task and message contract within the chosen protocol.
- **C:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: An interoperable task and message contract within the chosen protocol.
- **D:** Incorrect for this question. MCP provides a common interface between agents and capability servers. Server trust, scopes, and validation remain your responsibility. In this case: An interoperable task and message contract within the chosen protocol.

### Question 35 — B

Answer: Route a request to the most suitable specialist agent. Routing based on the classification result. Routing can match task type, language, or risk to a capable handler. Misrouting needs an observable fallback. Local study-map skill 3.10 (Multi-Agent Workflow Patterns), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Loops can refine output or poll a system, but need iteration limits and progress checks. Unbounded loops waste cost and can repeat unsafe actions. In this case: Routing based on the classification result.
- **B:** Correct. Routing can match task type, language, or risk to a capable handler. Misrouting needs an observable fallback. In this case: Routing based on the classification result.
- **C:** Incorrect for this question. Parallel branches reduce wall-clock time when work is truly independent. Shared state and reconciliation still require design. In this case: Routing based on the classification result.
- **D:** Incorrect for this question. A handoff should carry the goal, verified facts, permissions, and open questions. Implicit context is easily lost between agents. In this case: Routing based on the classification result.

### Question 36 — D

Answer: Transfer control with explicit context and state. Verified findings, remaining work, and explicit state. A handoff should carry the goal, verified facts, permissions, and open questions. Implicit context is easily lost between agents. Local study-map skill 3.10 (Multi-Agent Workflow Patterns), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Routing can match task type, language, or risk to a capable handler. Misrouting needs an observable fallback. In this case: Verified findings, remaining work, and explicit state.
- **B:** Incorrect for this question. Graphs express conditional paths and joins more clearly than a fixed chain. Complexity should be justified by real control flow. In this case: Verified findings, remaining work, and explicit state.
- **C:** Incorrect for this question. Sequential workflows make dependencies explicit and are easier to reason about. They may add latency when steps could run independently. In this case: Verified findings, remaining work, and explicit state.
- **D:** Correct. A handoff should carry the goal, verified facts, permissions, and open questions. Implicit context is easily lost between agents. In this case: Verified findings, remaining work, and explicit state.

### Question 37 — A

Answer: Run independent agents concurrently. Parallel execution with a join before synthesis. Parallel branches reduce wall-clock time when work is truly independent. Shared state and reconciliation still require design. Local study-map skill 3.10 (Multi-Agent Workflow Patterns), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Parallel branches reduce wall-clock time when work is truly independent. Shared state and reconciliation still require design. In this case: Parallel execution with a join before synthesis.
- **B:** Incorrect for this question. Sequential workflows make dependencies explicit and are easier to reason about. They may add latency when steps could run independently. In this case: Parallel execution with a join before synthesis.
- **C:** Incorrect for this question. Loops can refine output or poll a system, but need iteration limits and progress checks. Unbounded loops waste cost and can repeat unsafe actions. In this case: Parallel execution with a join before synthesis.
- **D:** Incorrect for this question. Graphs express conditional paths and joins more clearly than a fixed chain. Complexity should be justified by real control flow. In this case: Parallel execution with a join before synthesis.

### Question 38 — B

Answer: Use a graph workflow for branching dependencies. A graph with explicit branch and join semantics. Graphs express conditional paths and joins more clearly than a fixed chain. Complexity should be justified by real control flow. Local study-map skill 3.10 (Multi-Agent Workflow Patterns), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Loops can refine output or poll a system, but need iteration limits and progress checks. Unbounded loops waste cost and can repeat unsafe actions. In this case: A graph with explicit branch and join semantics.
- **B:** Correct. Graphs express conditional paths and joins more clearly than a fixed chain. Complexity should be justified by real control flow. In this case: A graph with explicit branch and join semantics.
- **C:** Incorrect for this question. Sequential workflows make dependencies explicit and are easier to reason about. They may add latency when steps could run independently. In this case: A graph with explicit branch and join semantics.
- **D:** Incorrect for this question. Parallel branches reduce wall-clock time when work is truly independent. Shared state and reconciliation still require design. In this case: A graph with explicit branch and join semantics.

### Question 39 — C

Answer: Repeat work until a defined stop condition is met. Runaway cost and repeated unsafe actions; bound the loop and escalate. Loops can refine output or poll a system, but need iteration limits and progress checks. Unbounded loops waste cost and can repeat unsafe actions. Local study-map skill 3.10 (Multi-Agent Workflow Patterns), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Routing can match task type, language, or risk to a capable handler. Misrouting needs an observable fallback. In this case: Runaway cost and repeated unsafe actions; bound the loop and escalate.
- **B:** Incorrect for this question. Parallel branches reduce wall-clock time when work is truly independent. Shared state and reconciliation still require design. In this case: Runaway cost and repeated unsafe actions; bound the loop and escalate.
- **C:** Correct. Loops can refine output or poll a system, but need iteration limits and progress checks. Unbounded loops waste cost and can repeat unsafe actions. In this case: Runaway cost and repeated unsafe actions; bound the loop and escalate.
- **D:** Incorrect for this question. Sequential workflows make dependencies explicit and are easier to reason about. They may add latency when steps could run independently. In this case: Runaway cost and repeated unsafe actions; bound the loop and escalate.

### Question 40 — A

Answer: Route a request to the most suitable specialist agent. Risk-based routing to a controlled human-review path. Routing can match task type, language, or risk to a capable handler. Misrouting needs an observable fallback. Local study-map skill 3.10 (Multi-Agent Workflow Patterns), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Routing can match task type, language, or risk to a capable handler. Misrouting needs an observable fallback. In this case: Risk-based routing to a controlled human-review path.
- **B:** Incorrect for this question. Sequential workflows make dependencies explicit and are easier to reason about. They may add latency when steps could run independently. In this case: Risk-based routing to a controlled human-review path.
- **C:** Incorrect for this question. Parallel branches reduce wall-clock time when work is truly independent. Shared state and reconciliation still require design. In this case: Risk-based routing to a controlled human-review path.
- **D:** Incorrect for this question. A handoff should carry the goal, verified facts, permissions, and open questions. Implicit context is easily lost between agents. In this case: Risk-based routing to a controlled human-review path.

### Question 41 — D

Answer: Run independent agents concurrently. Coordinated access with conflict detection or serialization. Parallel branches reduce wall-clock time when work is truly independent. Shared state and reconciliation still require design. Local study-map skill 3.10 (Multi-Agent Workflow Patterns), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Graphs express conditional paths and joins more clearly than a fixed chain. Complexity should be justified by real control flow. In this case: Coordinated access with conflict detection or serialization.
- **B:** Incorrect for this question. Loops can refine output or poll a system, but need iteration limits and progress checks. Unbounded loops waste cost and can repeat unsafe actions. In this case: Coordinated access with conflict detection or serialization.
- **C:** Incorrect for this question. Sequential workflows make dependencies explicit and are easier to reason about. They may add latency when steps could run independently. In this case: Coordinated access with conflict detection or serialization.
- **D:** Correct. Parallel branches reduce wall-clock time when work is truly independent. Shared state and reconciliation still require design. In this case: Coordinated access with conflict detection or serialization.

### Question 42 — C

Answer: Transfer control with explicit context and state. An explicit shared session or state contract with ownership. A handoff should carry the goal, verified facts, permissions, and open questions. Implicit context is easily lost between agents. Local study-map skill 3.10 (Multi-Agent Workflow Patterns), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Artifacts keep large content out of the prompt and provide a durable reference. They still require access control and validation. In this case: An explicit shared session or state contract with ownership.
- **B:** Incorrect for this question. Sessions support continuity across turns. Scope, retention, and isolation must match the use case. In this case: An explicit shared session or state contract with ownership.
- **C:** Correct. A handoff should carry the goal, verified facts, permissions, and open questions. Implicit context is easily lost between agents. In this case: An explicit shared session or state contract with ownership.
- **D:** Incorrect for this question. Long-term memory can personalize and improve continuity. It needs consent, retention, and deletion controls. In this case: An explicit shared session or state contract with ownership.

### Question 43 — B

Answer: Deploy to Agent Runtime for managed agent hosting. Agent Runtime for the supported managed path. Agent Runtime provides managed hosting and agent platform integration. It is not automatically the best fit for every workload. Local study-map skill 3.11 (Runtime Coordination and Policies), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Relational storage fits structured, transactional data. It is usually not the first choice for high-frequency session blobs. In this case: Agent Runtime for the supported managed path.
- **B:** Correct. Agent Runtime provides managed hosting and agent platform integration. It is not automatically the best fit for every workload. In this case: Agent Runtime for the supported managed path.
- **C:** Incorrect for this question. GKE offers flexibility for complex workloads at higher operational cost. Use it when requirements justify that control. In this case: Agent Runtime for the supported managed path.
- **D:** Incorrect for this question. Cloud Run suits stateless or externally-stateful container services with managed scaling. Design sessions and long tasks accordingly. In this case: Agent Runtime for the supported managed path.

### Question 44 — D

Answer: Deploy to Cloud Run for containerized request-driven services. Cloud Run with externalized session storage. Cloud Run suits stateless or externally-stateful container services with managed scaling. Design sessions and long tasks accordingly. Local study-map skill 3.11 (Runtime Coordination and Policies), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Agent Runtime provides managed hosting and agent platform integration. It is not automatically the best fit for every workload. In this case: Cloud Run with externalized session storage.
- **B:** Incorrect for this question. Managed workstations provide controlled, reproducible development sessions. They should still use least privilege and approved network paths. In this case: Cloud Run with externalized session storage.
- **C:** Incorrect for this question. GKE offers flexibility for complex workloads at higher operational cost. Use it when requirements justify that control. In this case: Cloud Run with externalized session storage.
- **D:** Correct. Cloud Run suits stateless or externally-stateful container services with managed scaling. Design sessions and long tasks accordingly. In this case: Cloud Run with externalized session storage.

### Question 45 — D

Answer: Use GKE when you need cluster-level control and custom orchestration. GKE with dedicated infrastructure and policies. GKE offers flexibility for complex workloads at higher operational cost. Use it when requirements justify that control. Local study-map skill 3.11 (Runtime Coordination and Policies), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Agent Runtime provides managed hosting and agent platform integration. It is not automatically the best fit for every workload. In this case: GKE with dedicated infrastructure and policies.
- **B:** Incorrect for this question. Cloud Run suits stateless or externally-stateful container services with managed scaling. Design sessions and long tasks accordingly. In this case: GKE with dedicated infrastructure and policies.
- **C:** Incorrect for this question. Stateless services scale and recover more predictably. External state introduces its own availability and security requirements. In this case: GKE with dedicated infrastructure and policies.
- **D:** Correct. GKE offers flexibility for complex workloads at higher operational cost. Use it when requirements justify that control. In this case: GKE with dedicated infrastructure and policies.

### Question 46 — C

Answer: Keep the service stateless and externalize session data. Externalize session state to a durable shared store. Stateless services scale and recover more predictably. External state introduces its own availability and security requirements. Local study-map skill 3.11 (Runtime Coordination and Policies), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Artifacts keep large content out of the prompt and provide a durable reference. They still require access control and validation. In this case: Externalize session state to a durable shared store.
- **B:** Incorrect for this question. An in-memory store can reduce latency for coordination and caching. It is not durable evidence storage by default. In this case: Externalize session state to a durable shared store.
- **C:** Correct. Stateless services scale and recover more predictably. External state introduces its own availability and security requirements. In this case: Externalize session state to a durable shared store.
- **D:** Incorrect for this question. Durable session storage supports continuity and recovery. Retention and isolation rules still apply. In this case: Externalize session state to a durable shared store.

### Question 47 — C

Answer: Encode organizational policy in enforceable controls. Shared platform and code controls rather than duplicated prompt text. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. Local study-map skill 3.11 (Runtime Coordination and Policies), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Impact review assigns responsibility for consequential outcomes. It should be timely and informed by evidence. In this case: Shared platform and code controls rather than duplicated prompt text.
- **B:** Incorrect for this question. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. In this case: Shared platform and code controls rather than duplicated prompt text.
- **C:** Correct. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Shared platform and code controls rather than duplicated prompt text.
- **D:** Incorrect for this question. Human-in-the-loop review is appropriate when impact or uncertainty is high. Approval must occur before the effect and with enough context to decide. In this case: Shared platform and code controls rather than duplicated prompt text.

### Question 48 — C

Answer: Persist sessions in a durable managed store. A document-oriented store designed for session data. Durable session storage supports continuity and recovery. Retention and isolation rules still apply. Local study-map skill 3.11 (Runtime Coordination and Policies), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. An in-memory store can reduce latency for coordination and caching. It is not durable evidence storage by default. In this case: A document-oriented store designed for session data.
- **B:** Incorrect for this question. Firestore can serve per-session documents and real-time access patterns. Model access and consistency deliberately. In this case: A document-oriented store designed for session data.
- **C:** Correct. Durable session storage supports continuity and recovery. Retention and isolation rules still apply. In this case: A document-oriented store designed for session data.
- **D:** Incorrect for this question. Relational storage fits structured, transactional data. It is usually not the first choice for high-frequency session blobs. In this case: A document-oriented store designed for session data.

### Question 49 — A

Answer: Provision capacity for peak concurrency and quotas. Capacity headroom, quota increases, and graceful degradation. Quotas and scaling limits can become the real bottleneck. Plan for bursts and graceful degradation. Local study-map skill 3.11 (Runtime Coordination and Policies), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Quotas and scaling limits can become the real bottleneck. Plan for bursts and graceful degradation. In this case: Capacity headroom, quota increases, and graceful degradation.
- **B:** Incorrect for this question. Cost attribution supports optimization and budgeting. Per-task cost reveals expensive failure paths. In this case: Capacity headroom, quota increases, and graceful degradation.
- **C:** Incorrect for this question. A canary or phased rollout limits exposure while evidence accumulates. Rollback must be practical, not theoretical. In this case: Capacity headroom, quota increases, and graceful degradation.
- **D:** Incorrect for this question. User experience depends on retrieval, tool calls, model turns, and approval. Optimize the whole path, not only generation time. In this case: Capacity headroom, quota increases, and graceful degradation.

### Question 50 — C

Answer: Deploy to Agent Runtime for managed agent hosting. A runtime and execution model suited to long-running work. Agent Runtime provides managed hosting and agent platform integration. It is not automatically the best fit for every workload. Local study-map skill 3.11 (Runtime Coordination and Policies), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Timeouts protect the workflow from stalled dependencies. Retries must avoid duplicating consequential actions. In this case: A runtime and execution model suited to long-running work.
- **B:** Incorrect for this question. Cloud Run suits stateless or externally-stateful container services with managed scaling. Design sessions and long tasks accordingly. In this case: A runtime and execution model suited to long-running work.
- **C:** Correct. Agent Runtime provides managed hosting and agent platform integration. It is not automatically the best fit for every workload. In this case: A runtime and execution model suited to long-running work.
- **D:** Incorrect for this question. GKE offers flexibility for complex workloads at higher operational cost. Use it when requirements justify that control. In this case: A runtime and execution model suited to long-running work.

### Question 51 — A

Answer: Ground the response in cited retrieved evidence. Completeness and faithful use of the retrieved evidence. Citations let users check claims against sources. Grounding reduces but does not eliminate hallucination. Local study-map skill 3.6 (Retrieval Authorization and Evidence Quality), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Citations let users check claims against sources. Grounding reduces but does not eliminate hallucination. In this case: Completeness and faithful use of the retrieved evidence.
- **B:** Incorrect for this question. A correct answer can hide an unsafe or wasteful action sequence. Trajectory checks verify which tools were called and with what arguments. In this case: Completeness and faithful use of the retrieved evidence.
- **C:** Incorrect for this question. Response metrics assess what the user receives. They should be tied to explicit task criteria. In this case: Completeness and faithful use of the retrieved evidence.
- **D:** Incorrect for this question. Autoraters can score nuanced qualities at scale. They require calibration against human judgments and periodic review. In this case: Completeness and faithful use of the retrieved evidence.

### Question 52 — A

Answer: Measure retrieval relevance and recall separately. Whether the filter reflects actual access and applicability requirements. Generation cannot compensate for missing evidence. Retrieval metrics localize pipeline failures. Local study-map skill 3.6 (Retrieval Authorization and Evidence Quality), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Generation cannot compensate for missing evidence. Retrieval metrics localize pipeline failures. In this case: Whether the filter reflects actual access and applicability requirements.
- **B:** Incorrect for this question. Access checks must occur before content enters the model context. Relevance never overrides permission. In this case: Whether the filter reflects actual access and applicability requirements.
- **C:** Incorrect for this question. Metadata such as tenant, date, or classification can enforce scope and freshness. Metadata must itself be trustworthy. In this case: Whether the filter reflects actual access and applicability requirements.
- **D:** Incorrect for this question. Response metrics assess what the user receives. They should be tied to explicit task criteria. In this case: Whether the filter reflects actual access and applicability requirements.

### Question 53 — D

Answer: Use human review for unresolved or high-impact judgment. Source-quality assessment in addition to citation support. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. Local study-map skill 3.6 (Retrieval Authorization and Evidence Quality), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Autoraters can score nuanced qualities at scale. They require calibration against human judgments and periodic review. In this case: Source-quality assessment in addition to citation support.
- **B:** Incorrect for this question. Citations let users check claims against sources. Grounding reduces but does not eliminate hallucination. In this case: Source-quality assessment in addition to citation support.
- **C:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Source-quality assessment in addition to citation support.
- **D:** Correct. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. In this case: Source-quality assessment in addition to citation support.

### Question 54 — D

Answer: Filter retrieval by the requesting user's authorization. One user's authorized results may be served to another. Access checks must occur before content enters the model context. Relevance never overrides permission. Local study-map skill 3.6 (Retrieval Authorization and Evidence Quality), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: One user's authorized results may be served to another.
- **B:** Incorrect for this question. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: One user's authorized results may be served to another.
- **C:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: One user's authorized results may be served to another.
- **D:** Correct. Access checks must occur before content enters the model context. Relevance never overrides permission. In this case: One user's authorized results may be served to another.

### Question 55 — C

Answer: Preserve source and chunk identifiers through the pipeline. Explain the date-dependent difference and cite both. Identifiers support citation, debugging, and access checks. Losing them makes evidence untraceable. Local study-map skill 3.6 (Retrieval Authorization and Evidence Quality), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Citations let users check claims against sources. Grounding reduces but does not eliminate hallucination. In this case: Explain the date-dependent difference and cite both.
- **B:** Incorrect for this question. A reranker can improve precision after broad recall. It adds latency and still needs evaluation. In this case: Explain the date-dependent difference and cite both.
- **C:** Correct. Identifiers support citation, debugging, and access checks. Losing them makes evidence untraceable. In this case: Explain the date-dependent difference and cite both.
- **D:** Incorrect for this question. Duplicates waste context and can overweight one source. Deduplication improves diversity of evidence. In this case: Explain the date-dependent difference and cite both.

### Question 56 — A

Answer: Measure retrieval relevance and recall separately. Retrieval metrics on a fixed query set before judging response quality. Generation cannot compensate for missing evidence. Retrieval metrics localize pipeline failures. Local study-map skill 3.6 (Retrieval Authorization and Evidence Quality), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Generation cannot compensate for missing evidence. Retrieval metrics localize pipeline failures. In this case: Retrieval metrics on a fixed query set before judging response quality.
- **B:** Incorrect for this question. Response metrics assess what the user receives. They should be tied to explicit task criteria. In this case: Retrieval metrics on a fixed query set before judging response quality.
- **C:** Incorrect for this question. Cost attribution supports optimization and budgeting. Per-task cost reveals expensive failure paths. In this case: Retrieval metrics on a fixed query set before judging response quality.
- **D:** Incorrect for this question. A correct answer can hide an unsafe or wasteful action sequence. Trajectory checks verify which tools were called and with what arguments. In this case: Retrieval metrics on a fixed query set before judging response quality.

### Question 57 — B

Answer: Filter retrieval using trusted metadata. Reindex or update metadata promptly so filters reflect the new classification. Metadata such as tenant, date, or classification can enforce scope and freshness. Metadata must itself be trustworthy. Local study-map skill 3.6 (Retrieval Authorization and Evidence Quality), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Access checks must occur before content enters the model context. Relevance never overrides permission. In this case: Reindex or update metadata promptly so filters reflect the new classification.
- **B:** Correct. Metadata such as tenant, date, or classification can enforce scope and freshness. Metadata must itself be trustworthy. In this case: Reindex or update metadata promptly so filters reflect the new classification.
- **C:** Incorrect for this question. Stale indexes produce outdated answers. Define update frequency and verify that deletions propagate. In this case: Reindex or update metadata promptly so filters reflect the new classification.
- **D:** Incorrect for this question. Identifiers support citation, debugging, and access checks. Losing them makes evidence untraceable. In this case: Reindex or update metadata promptly so filters reflect the new classification.

### Question 58 — B

Answer: Use human review for unresolved or high-impact judgment. The irreversible recommendation still requires accountable human approval before execution. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. Local study-map skill 3.6 (Retrieval Authorization and Evidence Quality), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Citations let users check claims against sources. Grounding reduces but does not eliminate hallucination. In this case: The irreversible recommendation still requires accountable human approval before execution.
- **B:** Correct. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. In this case: The irreversible recommendation still requires accountable human approval before execution.
- **C:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: The irreversible recommendation still requires accountable human approval before execution.
- **D:** Incorrect for this question. Response metrics assess what the user receives. They should be tied to explicit task criteria. In this case: The irreversible recommendation still requires accountable human approval before execution.

### Question 59 — B

Answer: Give each agent its own managed identity. Replace the default identity with a dedicated agent identity limited to required permissions. Distinct identity makes access attributable and auditable. Sharing a human or broad service identity weakens least privilege. Local study-map skill 3.7 (Agent Identity and Permissions), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: Replace the default identity with a dedicated agent identity limited to required permissions.
- **B:** Correct. Distinct identity makes access attributable and auditable. Sharing a human or broad service identity weakens least privilege. In this case: Replace the default identity with a dedicated agent identity limited to required permissions.
- **C:** Incorrect for this question. Short-lived, scoped tokens limit what a tool call can do. Token handling and refresh must avoid broad standing access. In this case: Replace the default identity with a dedicated agent identity limited to required permissions.
- **D:** Incorrect for this question. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: Replace the default identity with a dedicated agent identity limited to required permissions.

### Question 60 — B

Answer: Use scoped OAuth 2.0 tokens for agent-to-tool calls. A dedicated service identity with short-lived credentials. Short-lived, scoped tokens limit what a tool call can do. Token handling and refresh must avoid broad standing access. Local study-map skill 3.7 (Agent Identity and Permissions), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Short lifetimes and audience limits reduce misuse. Tokens should not be placed in prompts or logs. In this case: A dedicated service identity with short-lived credentials.
- **B:** Correct. Short-lived, scoped tokens limit what a tool call can do. Token handling and refresh must avoid broad standing access. In this case: A dedicated service identity with short-lived credentials.
- **C:** Incorrect for this question. Managed secret storage supports rotation and access control. A prompt instruction is not a secret-protection mechanism. In this case: A dedicated service identity with short-lived credentials.
- **D:** Incorrect for this question. Downstream authorization needs the actual principal, not a generic agent identity. Delegation must be explicit and scoped. In this case: A dedicated service identity with short-lived credentials.

### Question 61 — C

Answer: Constrain access with a principal access boundary policy. Use environment-specific permissions and boundary scope rather than widening production access. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. Local study-map skill 3.7 (Agent Identity and Permissions), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: Use environment-specific permissions and boundary scope rather than widening production access.
- **B:** Incorrect for this question. A service perimeter can reduce exfiltration paths for supported services. It complements, rather than replaces, IAM and application checks. In this case: Use environment-specific permissions and boundary scope rather than widening production access.
- **C:** Correct. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: Use environment-specific permissions and boundary scope rather than widening production access.
- **D:** Incorrect for this question. Narrow roles and scopes reduce blast radius. Review permissions as the workflow evolves. In this case: Use environment-specific permissions and boundary scope rather than widening production access.

### Question 62 — C

Answer: Use a dedicated service account with least privilege. Revoke and rotate credentials immediately and verify no residual access. A dedicated identity separates the agent from human accounts and limits blast radius. Roles still need review and periodic reduction. Local study-map skill 3.7 (Agent Identity and Permissions), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Distinct identity makes access attributable and auditable. Sharing a human or broad service identity weakens least privilege. In this case: Revoke and rotate credentials immediately and verify no residual access.
- **B:** Incorrect for this question. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: Revoke and rotate credentials immediately and verify no residual access.
- **C:** Correct. A dedicated identity separates the agent from human accounts and limits blast radius. Roles still need review and periodic reduction. In this case: Revoke and rotate credentials immediately and verify no residual access.
- **D:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Revoke and rotate credentials immediately and verify no residual access.

### Question 63 — B

Answer: Propagate the caller's identity to downstream tools. The tool cannot apply user-specific authorization and may over-permit. Downstream authorization needs the actual principal, not a generic agent identity. Delegation must be explicit and scoped. Local study-map skill 3.7 (Agent Identity and Permissions), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: The tool cannot apply user-specific authorization and may over-permit.
- **B:** Correct. Downstream authorization needs the actual principal, not a generic agent identity. Delegation must be explicit and scoped. In this case: The tool cannot apply user-specific authorization and may over-permit.
- **C:** Incorrect for this question. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. In this case: The tool cannot apply user-specific authorization and may over-permit.
- **D:** Incorrect for this question. Short-lived, scoped tokens limit what a tool call can do. Token handling and refresh must avoid broad standing access. In this case: The tool cannot apply user-specific authorization and may over-permit.

### Question 64 — B

Answer: Grant the minimum permissions required for the task. Effective permissions, not only directly granted roles. Narrow roles and scopes reduce blast radius. Review permissions as the workflow evolves. Local study-map skill 3.7 (Agent Identity and Permissions), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: Effective permissions, not only directly granted roles.
- **B:** Correct. Narrow roles and scopes reduce blast radius. Review permissions as the workflow evolves. In this case: Effective permissions, not only directly granted roles.
- **C:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Effective permissions, not only directly granted roles.
- **D:** Incorrect for this question. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: Effective permissions, not only directly granted roles.

### Question 65 — D

Answer: Grant IAM roles to the agent identity, not to users' credentials. Registry and audit records mapping agents to identities and actions. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. Local study-map skill 3.7 (Agent Identity and Permissions), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Registry and audit records mapping agents to identities and actions.
- **B:** Incorrect for this question. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: Registry and audit records mapping agents to identities and actions.
- **C:** Incorrect for this question. Distinct identity makes access attributable and auditable. Sharing a human or broad service identity weakens least privilege. In this case: Registry and audit records mapping agents to identities and actions.
- **D:** Correct. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: Registry and audit records mapping agents to identities and actions.

### Question 66 — C

Answer: Constrain access with a principal access boundary policy. That all tool paths used by the agent are covered as intended. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. Local study-map skill 3.7 (Agent Identity and Permissions), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: That all tool paths used by the agent are covered as intended.
- **B:** Incorrect for this question. Short-lived, scoped tokens limit what a tool call can do. Token handling and refresh must avoid broad standing access. In this case: That all tool paths used by the agent are covered as intended.
- **C:** Correct. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: That all tool paths used by the agent are covered as intended.
- **D:** Incorrect for this question. Egress controls reduce exfiltration and unauthorized tool reach. They should be paired with identity and data controls. In this case: That all tool paths used by the agent are covered as intended.

### Question 67 — C

Answer: Use MCP for standardized tool and resource access. Return safe, structured errors without internal details. MCP provides a common interface between agents and capability servers. Server trust, scopes, and validation remain your responsibility. Local study-map skill 3.8 (Registry and Capability Integration), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. In this case: Return safe, structured errors without internal details.
- **B:** Incorrect for this question. Plugins make a capability set reusable across projects. Bundling does not remove the need to review each included permission and dependency. In this case: Return safe, structured errors without internal details.
- **C:** Correct. MCP provides a common interface between agents and capability servers. Server trust, scopes, and validation remain your responsibility. In this case: Return safe, structured errors without internal details.
- **D:** Incorrect for this question. An MCP server provides a governed interface to tools, resources, or prompts. The server must enforce its own authorization and input validation. In this case: Return safe, structured errors without internal details.

### Question 68 — B

Answer: Register agents and capabilities in Agent Registry. Unique identifiers, ownership, and version metadata. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. Local study-map skill 3.8 (Registry and Capability Integration), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Unique identifiers, ownership, and version metadata.
- **B:** Correct. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: Unique identifiers, ownership, and version metadata.
- **C:** Incorrect for this question. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. In this case: Unique identifiers, ownership, and version metadata.
- **D:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Unique identifiers, ownership, and version metadata.

### Question 69 — A

Answer: Expose approved capabilities through an MCP server. The server must authenticate callers and authorize each tool invocation separately. An MCP server provides a governed interface to tools, resources, or prompts. The server must enforce its own authorization and input validation. Local study-map skill 3.8 (Registry and Capability Integration), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. An MCP server provides a governed interface to tools, resources, or prompts. The server must enforce its own authorization and input validation. In this case: The server must authenticate callers and authorize each tool invocation separately.
- **B:** Incorrect for this question. Short-lived, scoped tokens limit what a tool call can do. Token handling and refresh must avoid broad standing access. In this case: The server must authenticate callers and authorize each tool invocation separately.
- **C:** Incorrect for this question. MCP provides a common interface between agents and capability servers. Server trust, scopes, and validation remain your responsibility. In this case: The server must authenticate callers and authorize each tool invocation separately.
- **D:** Incorrect for this question. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: The server must authenticate callers and authorize each tool invocation separately.

### Question 70 — D

Answer: Package reusable guidance and assets as a skill. The tool's scope, credential use, and necessity. A skill can carry instructions, examples, and supporting files for a recurring task. It guides behavior but does not itself enforce permissions. Local study-map skill 3.8 (Registry and Capability Integration), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Rules communicate conventions and constraints for generated changes. They are guidance; merge controls and tests remain the enforcement boundary. In this case: The tool's scope, credential use, and necessity.
- **B:** Incorrect for this question. Hooks can enforce checks, logging, or formatting at defined points. They are useful precisely because they do not depend on model discretion. In this case: The tool's scope, credential use, and necessity.
- **C:** Incorrect for this question. Plugins make a capability set reusable across projects. Bundling does not remove the need to review each included permission and dependency. In this case: The tool's scope, credential use, and necessity.
- **D:** Correct. A skill can carry instructions, examples, and supporting files for a recurring task. It guides behavior but does not itself enforce permissions. In this case: The tool's scope, credential use, and necessity.

### Question 71 — C

Answer: Publish an Agent Card describing capabilities and endpoints. Treat it as untrusted and require an approved trust and auth path. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. Local study-map skill 3.8 (Registry and Capability Integration), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: Treat it as untrusted and require an approved trust and auth path.
- **B:** Incorrect for this question. A2A supports discovery and task exchange between agents that may be built on different stacks. Trust and authorization still need explicit design. In this case: Treat it as untrusted and require an approved trust and auth path.
- **C:** Correct. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. In this case: Treat it as untrusted and require an approved trust and auth path.
- **D:** Incorrect for this question. MCP provides a common interface between agents and capability servers. Server trust, scopes, and validation remain your responsibility. In this case: Treat it as untrusted and require an approved trust and auth path.

### Question 72 — D

Answer: Register agents and capabilities in Agent Registry. Update or retire the entry and prevent stale routing. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. Local study-map skill 3.8 (Registry and Capability Integration), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Update or retire the entry and prevent stale routing.
- **B:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Update or retire the entry and prevent stale routing.
- **C:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Update or retire the entry and prevent stale routing.
- **D:** Correct. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: Update or retire the entry and prevent stale routing.

### Question 73 — D

Answer: Use MCP for standardized tool and resource access. Treat it as untrusted data and screen or validate before acting on it. MCP provides a common interface between agents and capability servers. Server trust, scopes, and validation remain your responsibility. Local study-map skill 3.8 (Registry and Capability Integration), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Treat it as untrusted data and screen or validate before acting on it.
- **B:** Incorrect for this question. Model Armor can help detect prompt injection, unsafe content, and sensitive data patterns. It is a layered control, not a complete trust boundary. In this case: Treat it as untrusted data and screen or validate before acting on it.
- **C:** Incorrect for this question. Classification and de-identification reduce unnecessary exposure. De-identification must be validated for the specific data and purpose. In this case: Treat it as untrusted data and screen or validate before acting on it.
- **D:** Correct. MCP provides a common interface between agents and capability servers. Server trust, scopes, and validation remain your responsibility. In this case: Treat it as untrusted data and screen or validate before acting on it.

### Question 74 — A

Answer: Bundle related skills, tools, and configuration as a plugin. Unexpected behavior changes when dependencies update. Plugins make a capability set reusable across projects. Bundling does not remove the need to review each included permission and dependency. Local study-map skill 3.8 (Registry and Capability Integration), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Plugins make a capability set reusable across projects. Bundling does not remove the need to review each included permission and dependency. In this case: Unexpected behavior changes when dependencies update.
- **B:** Incorrect for this question. A skill can carry instructions, examples, and supporting files for a recurring task. It guides behavior but does not itself enforce permissions. In this case: Unexpected behavior changes when dependencies update.
- **C:** Incorrect for this question. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. In this case: Unexpected behavior changes when dependencies update.
- **D:** Incorrect for this question. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: Unexpected behavior changes when dependencies update.

### Question 75 — C

Answer: Use A2A for agent-to-agent interoperability. A scoped credential and verified caller identity. A2A supports discovery and task exchange between agents that may be built on different stacks. Trust and authorization still need explicit design. Local study-map skill 3.9 (Agent-to-Agent Protocols), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. In this case: A scoped credential and verified caller identity.
- **B:** Incorrect for this question. Short-lived, scoped tokens limit what a tool call can do. Token handling and refresh must avoid broad standing access. In this case: A scoped credential and verified caller identity.
- **C:** Correct. A2A supports discovery and task exchange between agents that may be built on different stacks. Trust and authorization still need explicit design. In this case: A scoped credential and verified caller identity.
- **D:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: A scoped credential and verified caller identity.

### Question 76 — A

Answer: Use MCP for standardized tool and resource access. Task states, message formats, and terminal outcomes. MCP provides a common interface between agents and capability servers. Server trust, scopes, and validation remain your responsibility. Local study-map skill 3.9 (Agent-to-Agent Protocols), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. MCP provides a common interface between agents and capability servers. Server trust, scopes, and validation remain your responsibility. In this case: Task states, message formats, and terminal outcomes.
- **B:** Incorrect for this question. A2A supports discovery and task exchange between agents that may be built on different stacks. Trust and authorization still need explicit design. In this case: Task states, message formats, and terminal outcomes.
- **C:** Incorrect for this question. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: Task states, message formats, and terminal outcomes.
- **D:** Incorrect for this question. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. In this case: Task states, message formats, and terminal outcomes.

### Question 77 — D

Answer: Publish an Agent Card describing capabilities and endpoints. Callers may request actions it cannot legally perform, causing failures or misuse. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. Local study-map skill 3.9 (Agent-to-Agent Protocols), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. MCP provides a common interface between agents and capability servers. Server trust, scopes, and validation remain your responsibility. In this case: Callers may request actions it cannot legally perform, causing failures or misuse.
- **B:** Incorrect for this question. Plugins make a capability set reusable across projects. Bundling does not remove the need to review each included permission and dependency. In this case: Callers may request actions it cannot legally perform, causing failures or misuse.
- **C:** Incorrect for this question. A2A supports discovery and task exchange between agents that may be built on different stacks. Trust and authorization still need explicit design. In this case: Callers may request actions it cannot legally perform, causing failures or misuse.
- **D:** Correct. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. In this case: Callers may request actions it cannot legally perform, causing failures or misuse.

### Question 78 — D

Answer: Use A2A for agent-to-agent interoperability. Explicit trust, authentication, and data-sharing limits. A2A supports discovery and task exchange between agents that may be built on different stacks. Trust and authorization still need explicit design. Local study-map skill 3.9 (Agent-to-Agent Protocols), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Explicit trust, authentication, and data-sharing limits.
- **B:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Explicit trust, authentication, and data-sharing limits.
- **C:** Incorrect for this question. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: Explicit trust, authentication, and data-sharing limits.
- **D:** Correct. A2A supports discovery and task exchange between agents that may be built on different stacks. Trust and authorization still need explicit design. In this case: Explicit trust, authentication, and data-sharing limits.

### Question 79 — D

Answer: Use MCP for standardized tool and resource access. Per-tool scopes bound to the caller's authorization. MCP provides a common interface between agents and capability servers. Server trust, scopes, and validation remain your responsibility. Local study-map skill 3.9 (Agent-to-Agent Protocols), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. An MCP server provides a governed interface to tools, resources, or prompts. The server must enforce its own authorization and input validation. In this case: Per-tool scopes bound to the caller's authorization.
- **B:** Incorrect for this question. Downstream authorization needs the actual principal, not a generic agent identity. Delegation must be explicit and scoped. In this case: Per-tool scopes bound to the caller's authorization.
- **C:** Incorrect for this question. Short-lived, scoped tokens limit what a tool call can do. Token handling and refresh must avoid broad standing access. In this case: Per-tool scopes bound to the caller's authorization.
- **D:** Correct. MCP provides a common interface between agents and capability servers. Server trust, scopes, and validation remain your responsibility. In this case: Per-tool scopes bound to the caller's authorization.

### Question 80 — C

Answer: Use A2A for agent-to-agent interoperability. A clear failure or partial-result state the caller can act on. A2A supports discovery and task exchange between agents that may be built on different stacks. Trust and authorization still need explicit design. Local study-map skill 3.9 (Agent-to-Agent Protocols), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A handoff should carry the goal, verified facts, permissions, and open questions. Implicit context is easily lost between agents. In this case: A clear failure or partial-result state the caller can act on.
- **B:** Incorrect for this question. Sequential workflows make dependencies explicit and are easier to reason about. They may add latency when steps could run independently. In this case: A clear failure or partial-result state the caller can act on.
- **C:** Correct. A2A supports discovery and task exchange between agents that may be built on different stacks. Trust and authorization still need explicit design. In this case: A clear failure or partial-result state the caller can act on.
- **D:** Incorrect for this question. Parallel branches reduce wall-clock time when work is truly independent. Shared state and reconciliation still require design. In this case: A clear failure or partial-result state the caller can act on.

### Question 81 — C

Answer: Publish an Agent Card describing capabilities and endpoints. Registry and Agent Card changes with alerting on unexpected updates. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. Local study-map skill 3.9 (Agent-to-Agent Protocols), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Registry and Agent Card changes with alerting on unexpected updates.
- **B:** Incorrect for this question. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: Registry and Agent Card changes with alerting on unexpected updates.
- **C:** Correct. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. In this case: Registry and Agent Card changes with alerting on unexpected updates.
- **D:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Registry and Agent Card changes with alerting on unexpected updates.

### Question 82 — A

Answer: Use MCP for standardized tool and resource access. Reject the request and enforce authorization outside the message content. MCP provides a common interface between agents and capability servers. Server trust, scopes, and validation remain your responsibility. Local study-map skill 3.9 (Agent-to-Agent Protocols), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. MCP provides a common interface between agents and capability servers. Server trust, scopes, and validation remain your responsibility. In this case: Reject the request and enforce authorization outside the message content.
- **B:** Incorrect for this question. A2A supports discovery and task exchange between agents that may be built on different stacks. Trust and authorization still need explicit design. In this case: Reject the request and enforce authorization outside the message content.
- **C:** Incorrect for this question. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. In this case: Reject the request and enforce authorization outside the message content.
- **D:** Incorrect for this question. Model Armor can help detect prompt injection, unsafe content, and sensitive data patterns. It is a layered control, not a complete trust boundary. In this case: Reject the request and enforce authorization outside the message content.

### Question 83 — B

Answer: Route a request to the most suitable specialist agent. Parallel delegation followed by a defined merge step. Routing can match task type, language, or risk to a capable handler. Misrouting needs an observable fallback. Local study-map skill 3.10 (Multi-Agent Workflow Patterns), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A handoff should carry the goal, verified facts, permissions, and open questions. Implicit context is easily lost between agents. In this case: Parallel delegation followed by a defined merge step.
- **B:** Correct. Routing can match task type, language, or risk to a capable handler. Misrouting needs an observable fallback. In this case: Parallel delegation followed by a defined merge step.
- **C:** Incorrect for this question. Graphs express conditional paths and joins more clearly than a fixed chain. Complexity should be justified by real control flow. In this case: Parallel delegation followed by a defined merge step.
- **D:** Incorrect for this question. Parallel branches reduce wall-clock time when work is truly independent. Shared state and reconciliation still require design. In this case: Parallel delegation followed by a defined merge step.

### Question 84 — D

Answer: Run agents in a fixed sequence. An explicit pending-approval state that blocks the next step. Sequential workflows make dependencies explicit and are easier to reason about. They may add latency when steps could run independently. Local study-map skill 3.10 (Multi-Agent Workflow Patterns), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Parallel branches reduce wall-clock time when work is truly independent. Shared state and reconciliation still require design. In this case: An explicit pending-approval state that blocks the next step.
- **B:** Incorrect for this question. Graphs express conditional paths and joins more clearly than a fixed chain. Complexity should be justified by real control flow. In this case: An explicit pending-approval state that blocks the next step.
- **C:** Incorrect for this question. Loops can refine output or poll a system, but need iteration limits and progress checks. Unbounded loops waste cost and can repeat unsafe actions. In this case: An explicit pending-approval state that blocks the next step.
- **D:** Correct. Sequential workflows make dependencies explicit and are easier to reason about. They may add latency when steps could run independently. In this case: An explicit pending-approval state that blocks the next step.

### Question 85 — B

Answer: Repeat work until a defined stop condition is met. Change the input or escalate after a bounded number of attempts. Loops can refine output or poll a system, but need iteration limits and progress checks. Unbounded loops waste cost and can repeat unsafe actions. Local study-map skill 3.10 (Multi-Agent Workflow Patterns), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Parallel branches reduce wall-clock time when work is truly independent. Shared state and reconciliation still require design. In this case: Change the input or escalate after a bounded number of attempts.
- **B:** Correct. Loops can refine output or poll a system, but need iteration limits and progress checks. Unbounded loops waste cost and can repeat unsafe actions. In this case: Change the input or escalate after a bounded number of attempts.
- **C:** Incorrect for this question. Routing can match task type, language, or risk to a capable handler. Misrouting needs an observable fallback. In this case: Change the input or escalate after a bounded number of attempts.
- **D:** Incorrect for this question. A handoff should carry the goal, verified facts, permissions, and open questions. Implicit context is easily lost between agents. In this case: Change the input or escalate after a bounded number of attempts.

### Question 86 — B

Answer: Transfer control with explicit context and state. The goal, constraints, evidence, and current state. A handoff should carry the goal, verified facts, permissions, and open questions. Implicit context is easily lost between agents. Local study-map skill 3.10 (Multi-Agent Workflow Patterns), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Sequential workflows make dependencies explicit and are easier to reason about. They may add latency when steps could run independently. In this case: The goal, constraints, evidence, and current state.
- **B:** Correct. A handoff should carry the goal, verified facts, permissions, and open questions. Implicit context is easily lost between agents. In this case: The goal, constraints, evidence, and current state.
- **C:** Incorrect for this question. Routing can match task type, language, or risk to a capable handler. Misrouting needs an observable fallback. In this case: The goal, constraints, evidence, and current state.
- **D:** Incorrect for this question. Graphs express conditional paths and joins more clearly than a fixed chain. Complexity should be justified by real control flow. In this case: The goal, constraints, evidence, and current state.

### Question 87 — A

Answer: Use a graph workflow for branching dependencies. A bounded termination condition and failure path. Graphs express conditional paths and joins more clearly than a fixed chain. Complexity should be justified by real control flow. Local study-map skill 3.10 (Multi-Agent Workflow Patterns), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Graphs express conditional paths and joins more clearly than a fixed chain. Complexity should be justified by real control flow. In this case: A bounded termination condition and failure path.
- **B:** Incorrect for this question. Parallel branches reduce wall-clock time when work is truly independent. Shared state and reconciliation still require design. In this case: A bounded termination condition and failure path.
- **C:** Incorrect for this question. Sequential workflows make dependencies explicit and are easier to reason about. They may add latency when steps could run independently. In this case: A bounded termination condition and failure path.
- **D:** Incorrect for this question. Loops can refine output or poll a system, but need iteration limits and progress checks. Unbounded loops waste cost and can repeat unsafe actions. In this case: A bounded termination condition and failure path.

### Question 88 — A

Answer: Route a request to the most suitable specialist agent. Route by risk to an appropriate review path. Routing can match task type, language, or risk to a capable handler. Misrouting needs an observable fallback. Local study-map skill 3.10 (Multi-Agent Workflow Patterns), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Routing can match task type, language, or risk to a capable handler. Misrouting needs an observable fallback. In this case: Route by risk to an appropriate review path.
- **B:** Incorrect for this question. Parallel branches reduce wall-clock time when work is truly independent. Shared state and reconciliation still require design. In this case: Route by risk to an appropriate review path.
- **C:** Incorrect for this question. Sequential workflows make dependencies explicit and are easier to reason about. They may add latency when steps could run independently. In this case: Route by risk to an appropriate review path.
- **D:** Incorrect for this question. A handoff should carry the goal, verified facts, permissions, and open questions. Implicit context is easily lost between agents. In this case: Route by risk to an appropriate review path.

### Question 89 — D

Answer: Run independent agents concurrently. Apply an explicit reconciliation rule or escalate. Parallel branches reduce wall-clock time when work is truly independent. Shared state and reconciliation still require design. Local study-map skill 3.10 (Multi-Agent Workflow Patterns), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Sequential workflows make dependencies explicit and are easier to reason about. They may add latency when steps could run independently. In this case: Apply an explicit reconciliation rule or escalate.
- **B:** Incorrect for this question. Graphs express conditional paths and joins more clearly than a fixed chain. Complexity should be justified by real control flow. In this case: Apply an explicit reconciliation rule or escalate.
- **C:** Incorrect for this question. A handoff should carry the goal, verified facts, permissions, and open questions. Implicit context is easily lost between agents. In this case: Apply an explicit reconciliation rule or escalate.
- **D:** Correct. Parallel branches reduce wall-clock time when work is truly independent. Shared state and reconciliation still require design. In this case: Apply an explicit reconciliation rule or escalate.

### Question 90 — C

Answer: Repeat work until a defined stop condition is met. A maximum turn count, progress check, and escalation. Loops can refine output or poll a system, but need iteration limits and progress checks. Unbounded loops waste cost and can repeat unsafe actions. Local study-map skill 3.10 (Multi-Agent Workflow Patterns), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Routing can match task type, language, or risk to a capable handler. Misrouting needs an observable fallback. In this case: A maximum turn count, progress check, and escalation.
- **B:** Incorrect for this question. Parallel branches reduce wall-clock time when work is truly independent. Shared state and reconciliation still require design. In this case: A maximum turn count, progress check, and escalation.
- **C:** Correct. Loops can refine output or poll a system, but need iteration limits and progress checks. Unbounded loops waste cost and can repeat unsafe actions. In this case: A maximum turn count, progress check, and escalation.
- **D:** Incorrect for this question. Sequential workflows make dependencies explicit and are easier to reason about. They may add latency when steps could run independently. In this case: A maximum turn count, progress check, and escalation.

### Question 91 — A

Answer: Transfer control with explicit context and state. Pass a scoped artifact reference with access controls. A handoff should carry the goal, verified facts, permissions, and open questions. Implicit context is easily lost between agents. Local study-map skill 3.10 (Multi-Agent Workflow Patterns), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. A handoff should carry the goal, verified facts, permissions, and open questions. Implicit context is easily lost between agents. In this case: Pass a scoped artifact reference with access controls.
- **B:** Incorrect for this question. Sessions support continuity across turns. Scope, retention, and isolation must match the use case. In this case: Pass a scoped artifact reference with access controls.
- **C:** Incorrect for this question. Long-term memory can personalize and improve continuity. It needs consent, retention, and deletion controls. In this case: Pass a scoped artifact reference with access controls.
- **D:** Incorrect for this question. Artifacts keep large content out of the prompt and provide a durable reference. They still require access control and validation. In this case: Pass a scoped artifact reference with access controls.

### Question 92 — B

Answer: Deploy to Agent Runtime for managed agent hosting. Whether managed agent features justify the cost and operational model. Agent Runtime provides managed hosting and agent platform integration. It is not automatically the best fit for every workload. Local study-map skill 3.11 (Runtime Coordination and Policies), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Cloud Run suits stateless or externally-stateful container services with managed scaling. Design sessions and long tasks accordingly. In this case: Whether managed agent features justify the cost and operational model.
- **B:** Correct. Agent Runtime provides managed hosting and agent platform integration. It is not automatically the best fit for every workload. In this case: Whether managed agent features justify the cost and operational model.
- **C:** Incorrect for this question. GKE offers flexibility for complex workloads at higher operational cost. Use it when requirements justify that control. In this case: Whether managed agent features justify the cost and operational model.
- **D:** Incorrect for this question. Quotas and scaling limits can become the real bottleneck. Plan for bursts and graceful degradation. In this case: Whether managed agent features justify the cost and operational model.

### Question 93 — D

Answer: Deploy to Cloud Run for containerized request-driven services. Asynchronous work with job status and polling or callbacks. Cloud Run suits stateless or externally-stateful container services with managed scaling. Design sessions and long tasks accordingly. Local study-map skill 3.11 (Runtime Coordination and Policies), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Agent Runtime provides managed hosting and agent platform integration. It is not automatically the best fit for every workload. In this case: Asynchronous work with job status and polling or callbacks.
- **B:** Incorrect for this question. GKE offers flexibility for complex workloads at higher operational cost. Use it when requirements justify that control. In this case: Asynchronous work with job status and polling or callbacks.
- **C:** Incorrect for this question. Timeouts protect the workflow from stalled dependencies. Retries must avoid duplicating consequential actions. In this case: Asynchronous work with job status and polling or callbacks.
- **D:** Correct. Cloud Run suits stateless or externally-stateful container services with managed scaling. Design sessions and long tasks accordingly. In this case: Asynchronous work with job status and polling or callbacks.

### Question 94 — C

Answer: Keep the service stateless and externalize session data. A durable, replicated or regional session strategy with consistency rules. Stateless services scale and recover more predictably. External state introduces its own availability and security requirements. Local study-map skill 3.11 (Runtime Coordination and Policies), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. An in-memory store can reduce latency for coordination and caching. It is not durable evidence storage by default. In this case: A durable, replicated or regional session strategy with consistency rules.
- **B:** Incorrect for this question. Firestore can serve per-session documents and real-time access patterns. Model access and consistency deliberately. In this case: A durable, replicated or regional session strategy with consistency rules.
- **C:** Correct. Stateless services scale and recover more predictably. External state introduces its own availability and security requirements. In this case: A durable, replicated or regional session strategy with consistency rules.
- **D:** Incorrect for this question. Durable session storage supports continuity and recovery. Retention and isolation rules still apply. In this case: A durable, replicated or regional session strategy with consistency rules.

### Question 95 — B

Answer: Encode organizational policy in enforceable controls. Alternative tool paths may bypass it; enforce at shared platform layers too. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. Local study-map skill 3.11 (Runtime Coordination and Policies), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: Alternative tool paths may bypass it; enforce at shared platform layers too.
- **B:** Correct. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Alternative tool paths may bypass it; enforce at shared platform layers too.
- **C:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Alternative tool paths may bypass it; enforce at shared platform layers too.
- **D:** Incorrect for this question. Distinct identity makes access attributable and auditable. Sharing a human or broad service identity weakens least privilege. In this case: Alternative tool paths may bypass it; enforce at shared platform layers too.

### Question 96 — A

Answer: Provision capacity for peak concurrency and quotas. Cost, latency, and quality against the prior baseline. Quotas and scaling limits can become the real bottleneck. Plan for bursts and graceful degradation. Local study-map skill 3.11 (Runtime Coordination and Policies), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Quotas and scaling limits can become the real bottleneck. Plan for bursts and graceful degradation. In this case: Cost, latency, and quality against the prior baseline.
- **B:** Incorrect for this question. A canary or phased rollout limits exposure while evidence accumulates. Rollback must be practical, not theoretical. In this case: Cost, latency, and quality against the prior baseline.
- **C:** Incorrect for this question. User experience depends on retrieval, tool calls, model turns, and approval. Optimize the whole path, not only generation time. In this case: Cost, latency, and quality against the prior baseline.
- **D:** Incorrect for this question. Cost attribution supports optimization and budgeting. Per-task cost reveals expensive failure paths. In this case: Cost, latency, and quality against the prior baseline.

### Question 97 — A

Answer: Use GKE when you need cluster-level control and custom orchestration. GKE with appropriate accelerator node pools. GKE offers flexibility for complex workloads at higher operational cost. Use it when requirements justify that control. Local study-map skill 3.11 (Runtime Coordination and Policies), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. GKE offers flexibility for complex workloads at higher operational cost. Use it when requirements justify that control. In this case: GKE with appropriate accelerator node pools.
- **B:** Incorrect for this question. Relational storage fits structured, transactional data. It is usually not the first choice for high-frequency session blobs. In this case: GKE with appropriate accelerator node pools.
- **C:** Incorrect for this question. Cloud Run suits stateless or externally-stateful container services with managed scaling. Design sessions and long tasks accordingly. In this case: GKE with appropriate accelerator node pools.
- **D:** Incorrect for this question. Agent Runtime provides managed hosting and agent platform integration. It is not automatically the best fit for every workload. In this case: GKE with appropriate accelerator node pools.

### Question 98 — B

Answer: Persist sessions in a durable managed store. Encryption, access control, and expiry appropriate to the data. Durable session storage supports continuity and recovery. Retention and isolation rules still apply. Local study-map skill 3.11 (Runtime Coordination and Policies), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Incorrect for this question. Object storage is appropriate for files, models, and large outputs. Apply lifecycle and access controls. In this case: Encryption, access control, and expiry appropriate to the data.
- **B:** Correct. Durable session storage supports continuity and recovery. Retention and isolation rules still apply. In this case: Encryption, access control, and expiry appropriate to the data.
- **C:** Incorrect for this question. BigQuery can support analytics and controlled data sharing. Agent queries still need authorization and cost limits. In this case: Encryption, access control, and expiry appropriate to the data.
- **D:** Incorrect for this question. An in-memory store can reduce latency for coordination and caching. It is not durable evidence storage by default. In this case: Encryption, access control, and expiry appropriate to the data.

### Question 99 — A

Answer: Deploy to Agent Runtime for managed agent hosting. Manage concurrency with queueing, backpressure, and approved quota adjustments. Agent Runtime provides managed hosting and agent platform integration. It is not automatically the best fit for every workload. Local study-map skill 3.11 (Runtime Coordination and Policies), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Agent Runtime provides managed hosting and agent platform integration. It is not automatically the best fit for every workload. In this case: Manage concurrency with queueing, backpressure, and approved quota adjustments.
- **B:** Incorrect for this question. Quotas and scaling limits can become the real bottleneck. Plan for bursts and graceful degradation. In this case: Manage concurrency with queueing, backpressure, and approved quota adjustments.
- **C:** Incorrect for this question. Stateless services scale and recover more predictably. External state introduces its own availability and security requirements. In this case: Manage concurrency with queueing, backpressure, and approved quota adjustments.
- **D:** Incorrect for this question. Cloud Run suits stateless or externally-stateful container services with managed scaling. Design sessions and long tasks accordingly. In this case: Manage concurrency with queueing, backpressure, and approved quota adjustments.

### Question 100 — A

Answer: Encode organizational policy in enforceable controls. Route tool access through enforced policy controls and restrict direct paths. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. Local study-map skill 3.11 (Runtime Coordination and Policies), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Agent Development Kit documentation: https://google.github.io/adk-docs/

- **A:** Correct. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Route tool access through enforced policy controls and restrict direct paths.
- **B:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Route tool access through enforced policy controls and restrict direct paths.
- **C:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Route tool access through enforced policy controls and restrict direct paths.
- **D:** Incorrect for this question. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. In this case: Route tool access through enforced policy controls and restrict direct paths.
