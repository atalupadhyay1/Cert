# Google Cloud Professional Agentic Architect (PAA) — Practice Set 5

Securing and Governing Agentic Workflows

100 questions · Suggested practice duration: 180 minutes · Practice target: 80%

Tests 1–5 are focused learning tests. Test 6 is an expanded five-domain review, not an official exam replica. Related concepts recur.

Select ONE best answer for every question. Answer key follows all questions.

Original educational content, not actual, recalled, or copied Anthropic exam items.

## Questions

### 1. An agent calls a third-party API on behalf of a user. What should secure the call?

Domain: Securing and Governing Agentic Workflows

- A. Use scoped OAuth 2.0 tokens for agent-to-tool calls
- B. Use a dedicated service account with least privilege
- C. Grant IAM roles to the agent identity, not to users' credentials
- D. Keep access tokens short-lived and narrowly scoped

### 2. A tool token has broad scopes and a one-year lifetime. What should change?

Domain: Securing and Governing Agentic Workflows

- A. Record agent actions and tool calls in audit logs
- B. Store secrets in Secret Manager rather than prompts or code
- C. Use scoped OAuth 2.0 tokens for agent-to-tool calls
- D. Keep access tokens short-lived and narrowly scoped

### 3. An agent runs under a shared service account used by several systems. What is the main problem?

Domain: Securing and Governing Agentic Workflows

- A. Grant IAM roles to the agent identity, not to users' credentials
- B. Constrain access with a principal access boundary policy
- C. Use a dedicated service account with least privilege
- D. Give each agent its own managed identity

### 4. A platform wants each deployed agent to have distinct, auditable access. What should it use?

Domain: Securing and Governing Agentic Workflows

- A. Use a dedicated service account with least privilege
- B. Use scoped OAuth 2.0 tokens for agent-to-tool calls
- C. Give each agent its own managed identity
- D. Grant IAM roles to the agent identity, not to users' credentials

### 5. A downstream tool must apply the end user's permissions, not the agent's. What should be propagated?

Domain: Securing and Governing Agentic Workflows

- A. Govern agent traffic through Agent Gateway
- B. Use scoped OAuth 2.0 tokens for agent-to-tool calls
- C. Grant IAM roles to the agent identity, not to users' credentials
- D. Propagate the caller's identity to downstream tools

### 6. An agent requests a token with write access when it only reads. What principle is violated?

Domain: Securing and Governing Agentic Workflows

- A. Keep access tokens short-lived and narrowly scoped
- B. Inspect and de-identify sensitive data with Sensitive Data Protection
- C. Store secrets in Secret Manager rather than prompts or code
- D. Use scoped OAuth 2.0 tokens for agent-to-tool calls

### 7. An agent identity has project-level owner rights because setup was faster. What should happen?

Domain: Securing and Governing Agentic Workflows

- A. Give each agent its own managed identity
- B. Grant IAM roles to the agent identity, not to users' credentials
- C. Use a dedicated service account with least privilege
- D. Constrain access with a principal access boundary policy

### 8. A tool credential appears in an agent's prompt template. What should be done?

Domain: Securing and Governing Agentic Workflows

- A. Store secrets in Secret Manager rather than prompts or code
- B. Inspect and de-identify sensitive data with Sensitive Data Protection
- C. Record agent actions and tool calls in audit logs
- D. Redact or de-identify sensitive data before model exposure

### 9. A delegated token is accepted by a tool without checking audience or scope. What risk arises?

Domain: Securing and Governing Agentic Workflows

- A. Govern agent traffic through Agent Gateway
- B. Constrain access with a principal access boundary policy
- C. Use scoped OAuth 2.0 tokens for agent-to-tool calls
- D. Propagate the caller's identity to downstream tools

### 10. An agent must call a tool repeatedly during a long task. What token design is appropriate?

Domain: Securing and Governing Agentic Workflows

- A. Govern agent traffic through Agent Gateway
- B. Keep access tokens short-lived and narrowly scoped
- C. Record agent actions and tool calls in audit logs
- D. Grant IAM roles to the agent identity, not to users' credentials

### 11. A service account can list all storage buckets but needs one. What should be applied?

Domain: Securing and Governing Agentic Workflows

- A. Use a dedicated service account with least privilege
- B. Use VPC Service Controls to establish a data perimeter
- C. Grant IAM roles to the agent identity, not to users' credentials
- D. Grant the minimum permissions required for the task

### 12. A remote agent needs to know which user authorized a delegated task. What should the request include?

Domain: Securing and Governing Agentic Workflows

- A. Register agents and capabilities in Agent Registry
- B. Propagate the caller's identity to downstream tools
- C. Publish an Agent Card describing capabilities and endpoints
- D. Use A2A for agent-to-agent interoperability

### 13. A team wants to avoid storing plaintext API keys in configuration. What should it use?

Domain: Securing and Governing Agentic Workflows

- A. Redact or de-identify sensitive data before model exposure
- B. Inspect and de-identify sensitive data with Sensitive Data Protection
- C. Use customer-managed encryption keys where required
- D. Store secrets in Secret Manager rather than prompts or code

### 14. Permission changes for an agent are made without review. What control is missing?

Domain: Securing and Governing Agentic Workflows

- A. Grant IAM roles to the agent identity, not to users' credentials
- B. Record agent actions and tool calls in audit logs
- C. Govern agent traffic through Agent Gateway
- D. Constrain access with a principal access boundary policy

### 15. An agent impersonates a user without their consent. What is wrong?

Domain: Securing and Governing Agentic Workflows

- A. Grant IAM roles to the agent identity, not to users' credentials
- B. Propagate the caller's identity to downstream tools
- C. Use a dedicated service account with least privilege
- D. Use scoped OAuth 2.0 tokens for agent-to-tool calls

### 16. A tool receives a token in a URL query string that is logged. What should change?

Domain: Securing and Governing Agentic Workflows

- A. Restrict outbound network access to approved destinations
- B. Keep access tokens short-lived and narrowly scoped
- C. Use scoped OAuth 2.0 tokens for agent-to-tool calls
- D. Store secrets in Secret Manager rather than prompts or code

### 17. An agent has a legitimate role but should not reach data outside its business unit. What control fits?

Domain: Securing and Governing Agentic Workflows

- A. Grant IAM roles to the agent identity, not to users' credentials
- B. Use VPC Service Controls to establish a data perimeter
- C. Grant the minimum permissions required for the task
- D. Constrain access with a principal access boundary policy

### 18. An agent's permissions expanded during an incident and were never reduced. What should happen?

Domain: Securing and Governing Agentic Workflows

- A. Grant IAM roles to the agent identity, not to users' credentials
- B. Constrain access with a principal access boundary policy
- C. Record agent actions and tool calls in audit logs
- D. Grant the minimum permissions required for the task

### 19. A regulated workload must prevent data movement to unauthorized projects. What should be evaluated?

Domain: Securing and Governing Agentic Workflows

- A. Use VPC Service Controls to establish a data perimeter
- B. Restrict outbound network access to approved destinations
- C. Govern agent traffic through Agent Gateway
- D. Constrain access with a principal access boundary policy

### 20. A developer wants to bypass a principal access boundary to finish a task. What should happen?

Domain: Securing and Governing Agentic Workflows

- A. Register agents and capabilities in Agent Registry
- B. Constrain access with a principal access boundary policy
- C. Govern agent traffic through Agent Gateway
- D. Encode organizational policy in enforceable controls

### 21. An agent can delete logs that would otherwise record its actions. What is the concern?

Domain: Securing and Governing Agentic Workflows

- A. Grant IAM roles to the agent identity, not to users' credentials
- B. Grant the minimum permissions required for the task
- C. Constrain access with a principal access boundary policy
- D. Use a dedicated service account with least privilege

### 22. A principal access boundary is configured but not tested. What should be done?

Domain: Securing and Governing Agentic Workflows

- A. Constrain access with a principal access boundary policy
- B. Use scoped OAuth 2.0 tokens for agent-to-tool calls
- C. Grant IAM roles to the agent identity, not to users' credentials
- D. Use VPC Service Controls to establish a data perimeter

### 23. A role grants access to every dataset in a project. What should be used instead?

Domain: Securing and Governing Agentic Workflows

- A. Grant IAM roles to the agent identity, not to users' credentials
- B. Record agent actions and tool calls in audit logs
- C. Grant the minimum permissions required for the task
- D. Encode organizational policy in enforceable controls

### 24. An agent must call an approved external API from inside a perimeter. What should be configured?

Domain: Securing and Governing Agentic Workflows

- A. Inspect and de-identify sensitive data with Sensitive Data Protection
- B. Govern agent traffic through Agent Gateway
- C. Use VPC Service Controls to establish a data perimeter
- D. Restrict outbound network access to approved destinations

### 25. An organization wants boundaries that follow the agent identity across environments. What should it design?

Domain: Securing and Governing Agentic Workflows

- A. Constrain access with a principal access boundary policy
- B. Register agents and capabilities in Agent Registry
- C. Use a dedicated service account with least privilege
- D. Give each agent its own managed identity

### 26. A test agent shares production permissions. What should change?

Domain: Securing and Governing Agentic Workflows

- A. Constrain access with a principal access boundary policy
- B. Grant the minimum permissions required for the task
- C. Grant IAM roles to the agent identity, not to users' credentials
- D. Provision capacity for peak concurrency and quotas

### 27. Traffic from an agent to an internal service crosses a boundary unexpectedly. What should be investigated?

Domain: Securing and Governing Agentic Workflows

- A. Govern agent traffic through Agent Gateway
- B. Constrain access with a principal access boundary policy
- C. Grant IAM roles to the agent identity, not to users' credentials
- D. Use VPC Service Controls to establish a data perimeter

### 28. A permission review shows unused grants but no owner. What should be established?

Domain: Securing and Governing Agentic Workflows

- A. Encode organizational policy in enforceable controls
- B. Grant the minimum permissions required for the task
- C. Record agent actions and tool calls in audit logs
- D. Grant IAM roles to the agent identity, not to users' credentials

### 29. A team assumes VPC Service Controls encrypts data at rest. What should be clarified?

Domain: Securing and Governing Agentic Workflows

- A. Constrain access with a principal access boundary policy
- B. Use customer-managed encryption keys where required
- C. Inspect and de-identify sensitive data with Sensitive Data Protection
- D. Use VPC Service Controls to establish a data perimeter

### 30. A tool requires access that the boundary denies. What is the correct design response?

Domain: Securing and Governing Agentic Workflows

- A. Constrain access with a principal access boundary policy
- B. Grant the minimum permissions required for the task
- C. Govern agent traffic through Agent Gateway
- D. Register agents and capabilities in Agent Registry

### 31. An agent's boundary is tied to a human account that changes roles. What risk arises?

Domain: Securing and Governing Agentic Workflows

- A. Constrain access with a principal access boundary policy
- B. Grant IAM roles to the agent identity, not to users' credentials
- C. Give each agent its own managed identity
- D. Use scoped OAuth 2.0 tokens for agent-to-tool calls

### 32. A temporary elevated grant has no expiry. What should be added?

Domain: Securing and Governing Agentic Workflows

- A. Encode organizational policy in enforceable controls
- B. Grant the minimum permissions required for the task
- C. Record agent actions and tool calls in audit logs
- D. Provision capacity for peak concurrency and quotas

### 33. A boundary allows a broad API but the workflow needs one method. What should be narrowed?

Domain: Securing and Governing Agentic Workflows

- A. Use VPC Service Controls to establish a data perimeter
- B. Restrict outbound network access to approved destinations
- C. Constrain access with a principal access boundary policy
- D. Govern agent traffic through Agent Gateway

### 34. A security team wants centralized observation of agent-to-tool traffic. What should it deploy?

Domain: Securing and Governing Agentic Workflows

- A. Restrict outbound network access to approved destinations
- B. Grant IAM roles to the agent identity, not to users' credentials
- C. Govern agent traffic through Agent Gateway
- D. Record agent actions and tool calls in audit logs

### 35. An agent's outbound request contains customer data sent to an unapproved host. What control should catch it?

Domain: Securing and Governing Agentic Workflows

- A. Inspect and de-identify sensitive data with Sensitive Data Protection
- B. Use Cloud Logging, Cloud Trace, and Cloud Monitoring
- C. Record agent actions and tool calls in audit logs
- D. Govern agent traffic through Agent Gateway

### 36. A gateway allows an action because the caller is authenticated. Why is this insufficient?

Domain: Securing and Governing Agentic Workflows

- A. Use scoped OAuth 2.0 tokens for agent-to-tool calls
- B. Govern agent traffic through Agent Gateway
- C. Encode organizational policy in enforceable controls
- D. Constrain access with a principal access boundary policy

### 37. An investigation needs the sequence of agent tool calls across services. What should be available?

Domain: Securing and Governing Agentic Workflows

- A. Register agents and capabilities in Agent Registry
- B. Use Cloud Logging, Cloud Trace, and Cloud Monitoring
- C. Govern agent traffic through Agent Gateway
- D. Record agent actions and tool calls in audit logs

### 38. An agent can reach any internet host. What should be configured?

Domain: Securing and Governing Agentic Workflows

- A. Inspect and de-identify sensitive data with Sensitive Data Protection
- B. Use VPC Service Controls to establish a data perimeter
- C. Restrict outbound network access to approved destinations
- D. Govern agent traffic through Agent Gateway

### 39. A gateway blocks a request that matches a prompt-injection pattern. What should happen next?

Domain: Securing and Governing Agentic Workflows

- A. Enforce a policy check before a consequential action
- B. Govern agent traffic through Agent Gateway
- C. Require human approval before a consequential action
- D. Screen prompts and responses with Model Armor

### 40. A high-impact tool is called outside business hours. What should the gateway enforce?

Domain: Securing and Governing Agentic Workflows

- A. Govern agent traffic through Agent Gateway
- B. Review high-impact actions with accountable owners
- C. Record agent actions and tool calls in audit logs
- D. Encode organizational policy in enforceable controls

### 41. An unregistered agent attempts to call a governed tool. What should happen?

Domain: Securing and Governing Agentic Workflows

- A. Register agents and capabilities in Agent Registry
- B. Constrain access with a principal access boundary policy
- C. Govern agent traffic through Agent Gateway
- D. Grant IAM roles to the agent identity, not to users' credentials

### 42. Gateway logs contain full sensitive payloads. What should change?

Domain: Securing and Governing Agentic Workflows

- A. Track token and tool cost per completed task
- B. Record agent actions and tool calls in audit logs
- C. Use Cloud Logging, Cloud Trace, and Cloud Monitoring
- D. Govern agent traffic through Agent Gateway

### 43. A tool transfers funds above a threshold. What control should the gateway require?

Domain: Securing and Governing Agentic Workflows

- A. Encode organizational policy in enforceable controls
- B. Govern agent traffic through Agent Gateway
- C. Gate the action on explicit, attributable approval
- D. Require human approval before a consequential action

### 44. An agent tries to send data to a personal storage endpoint. What should prevent it?

Domain: Securing and Governing Agentic Workflows

- A. Store secrets in Secret Manager rather than prompts or code
- B. Govern agent traffic through Agent Gateway
- C. Inspect and de-identify sensitive data with Sensitive Data Protection
- D. Restrict outbound network access to approved destinations

### 45. A remote agent calls a local tool without appearing in inventory. What is missing?

Domain: Securing and Governing Agentic Workflows

- A. Govern agent traffic through Agent Gateway
- B. Record agent actions and tool calls in audit logs
- C. Register agents and capabilities in Agent Registry
- D. Publish an Agent Card describing capabilities and endpoints

### 46. A request contains sensitive data that policy forbids sending to an external tool. What should happen?

Domain: Securing and Governing Agentic Workflows

- A. Inspect and de-identify sensitive data with Sensitive Data Protection
- B. Encode organizational policy in enforceable controls
- C. Govern agent traffic through Agent Gateway
- D. Screen prompts and responses with Model Armor

### 47. A team wants to detect anomalous tool-call volume per agent. What should it monitor?

Domain: Securing and Governing Agentic Workflows

- A. Govern agent traffic through Agent Gateway
- B. Record agent actions and tool calls in audit logs
- C. Use Cloud Logging, Cloud Trace, and Cloud Monitoring
- D. Set explicit pass thresholds before evaluating

### 48. A gateway policy references a role that no longer exists. What should be done?

Domain: Securing and Governing Agentic Workflows

- A. Use scoped OAuth 2.0 tokens for agent-to-tool calls
- B. Govern agent traffic through Agent Gateway
- C. Grant IAM roles to the agent identity, not to users' credentials
- D. Constrain access with a principal access boundary policy

### 49. A new agent is deployed without gateway policy coverage. What risk arises?

Domain: Securing and Governing Agentic Workflows

- A. Encode organizational policy in enforceable controls
- B. Govern agent traffic through Agent Gateway
- C. Register agents and capabilities in Agent Registry
- D. Record agent actions and tool calls in audit logs

### 50. A blocked action is never reviewed. What operational gap exists?

Domain: Securing and Governing Agentic Workflows

- A. Govern agent traffic through Agent Gateway
- B. Require human approval before a consequential action
- C. Use Cloud Logging, Cloud Trace, and Cloud Monitoring
- D. Record agent actions and tool calls in audit logs

### 51. A public-facing agent receives prompts attempting jailbreaks. What layer should screen them?

Domain: Securing and Governing Agentic Workflows

- A. Govern agent traffic through Agent Gateway
- B. Enforce a policy check before a consequential action
- C. Screen prompts and responses with Model Armor
- D. Inspect and de-identify sensitive data with Sensitive Data Protection

### 52. A response may contain sensitive identifiers that policy forbids exposing. What should screen it?

Domain: Securing and Governing Agentic Workflows

- A. Inspect and de-identify sensitive data with Sensitive Data Protection
- B. Redact or de-identify sensitive data before model exposure
- C. Screen prompts and responses with Model Armor
- D. Use customer-managed encryption keys where required

### 53. An organization needs to know which agents and tools are approved for use. What should it maintain?

Domain: Securing and Governing Agentic Workflows

- A. Register agents and capabilities in Agent Registry
- B. Govern agent traffic through Agent Gateway
- C. Encode organizational policy in enforceable controls
- D. Record agent actions and tool calls in audit logs

### 54. A model safety filter blocks a legitimate business request. What should the team do?

Domain: Securing and Governing Agentic Workflows

- A. Encode organizational policy in enforceable controls
- B. Screen prompts and responses with Model Armor
- C. Enforce a policy check before a consequential action
- D. Require human approval before a consequential action

### 55. A written policy says agents must not email external domains. How should it be enforced?

Domain: Securing and Governing Agentic Workflows

- A. Govern agent traffic through Agent Gateway
- B. Register agents and capabilities in Agent Registry
- C. Enforce a policy check before a consequential action
- D. Encode organizational policy in enforceable controls

### 56. A dataset contains payment card numbers that must not enter model context. What should be applied?

Domain: Securing and Governing Agentic Workflows

- A. Use customer-managed encryption keys where required
- B. Redact or de-identify sensitive data before model exposure
- C. Screen prompts and responses with Model Armor
- D. Inspect and de-identify sensitive data with Sensitive Data Protection

### 57. A capability is registered without an accountable owner. What risk arises?

Domain: Securing and Governing Agentic Workflows

- A. Encode organizational policy in enforceable controls
- B. Register agents and capabilities in Agent Registry
- C. Record agent actions and tool calls in audit logs
- D. Publish an Agent Card describing capabilities and endpoints

### 58. A safety control blocks malicious content but not an authorized destructive action. What is the lesson?

Domain: Securing and Governing Agentic Workflows

- A. Require human approval before a consequential action
- B. Govern agent traffic through Agent Gateway
- C. Screen prompts and responses with Model Armor
- D. Enforce a policy check before a consequential action

### 59. An exception to agent policy is granted verbally. What should be done?

Domain: Securing and Governing Agentic Workflows

- A. Gate the action on explicit, attributable approval
- B. Record agent actions and tool calls in audit logs
- C. Review high-impact actions with accountable owners
- D. Encode organizational policy in enforceable controls

### 60. A response redacts names but leaves account numbers. What should improve?

Domain: Securing and Governing Agentic Workflows

- A. Keep access tokens short-lived and narrowly scoped
- B. Screen prompts and responses with Model Armor
- C. Inspect and de-identify sensitive data with Sensitive Data Protection
- D. Redact or de-identify sensitive data before model exposure

### 61. A retired agent remains in the registry with active permissions. What should happen?

Domain: Securing and Governing Agentic Workflows

- A. Encode organizational policy in enforceable controls
- B. Give each agent its own managed identity
- C. Register agents and capabilities in Agent Registry
- D. Govern agent traffic through Agent Gateway

### 62. A team wants defense in depth for prompt injection. What combination fits?

Domain: Securing and Governing Agentic Workflows

- A. Require human approval before a consequential action
- B. Enforce a policy check before a consequential action
- C. Screen prompts and responses with Model Armor
- D. Encode organizational policy in enforceable controls

### 63. A policy change is applied to one gateway route only. What should be verified?

Domain: Securing and Governing Agentic Workflows

- A. Govern agent traffic through Agent Gateway
- B. Encode organizational policy in enforceable controls
- C. Record agent actions and tool calls in audit logs
- D. Register agents and capabilities in Agent Registry

### 64. A safety tool returns a confidence score below the threshold. What should the workflow do?

Domain: Securing and Governing Agentic Workflows

- A. Encode organizational policy in enforceable controls
- B. Screen prompts and responses with Model Armor
- C. Inspect and de-identify sensitive data with Sensitive Data Protection
- D. Redact or de-identify sensitive data before model exposure

### 65. A compliance requirement specifies customer-managed keys for stored data. What should be configured?

Domain: Securing and Governing Agentic Workflows

- A. Use VPC Service Controls to establish a data perimeter
- B. Constrain access with a principal access boundary policy
- C. Inspect and de-identify sensitive data with Sensitive Data Protection
- D. Use customer-managed encryption keys where required

### 66. An MCP server is added without registry review. What governance step was skipped?

Domain: Securing and Governing Agentic Workflows

- A. Register agents and capabilities in Agent Registry
- B. Use MCP for standardized tool and resource access
- C. Bundle related skills, tools, and configuration as a plugin
- D. Publish an Agent Card describing capabilities and endpoints

### 67. Sensitive-data findings are logged with the raw values. What should change?

Domain: Securing and Governing Agentic Workflows

- A. Inspect and de-identify sensitive data with Sensitive Data Protection
- B. Record agent actions and tool calls in audit logs
- C. Encode organizational policy in enforceable controls
- D. Use human review for unresolved or high-impact judgment

### 68. An agent can issue refunds up to a high value. What control fits?

Domain: Securing and Governing Agentic Workflows

- A. Enforce a policy check before a consequential action
- B. Gate the action on explicit, attributable approval
- C. Require human approval before a consequential action
- D. Encode organizational policy in enforceable controls

### 69. A human approver receives only "approve refund?" with no context. What should be provided?

Domain: Securing and Governing Agentic Workflows

- A. Record agent actions and tool calls in audit logs
- B. Review high-impact actions with accountable owners
- C. Require human approval before a consequential action
- D. Enforce a policy check before a consequential action

### 70. An approval is recorded after the action has already executed. What is wrong?

Domain: Securing and Governing Agentic Workflows

- A. Enforce a policy check before a consequential action
- B. Require human approval before a consequential action
- C. Use scoped OAuth 2.0 tokens for agent-to-tool calls
- D. Gate the action on explicit, attributable approval

### 71. A destructive tool is available to an autonomous agent with no confirmation. What should be added?

Domain: Securing and Governing Agentic Workflows

- A. Encode organizational policy in enforceable controls
- B. Require human approval before a consequential action
- C. Govern agent traffic through Agent Gateway
- D. Enforce a policy check before a consequential action

### 72. An action affects a vulnerable customer group. What review approach fits?

Domain: Securing and Governing Agentic Workflows

- A. Require human approval before a consequential action
- B. Use a calibrated model-based autorater for scalable judgment
- C. Review high-impact actions with accountable owners
- D. Set explicit pass thresholds before evaluating

### 73. An approval token can be reused for multiple actions. What should change?

Domain: Securing and Governing Agentic Workflows

- A. Record agent actions and tool calls in audit logs
- B. Enforce a policy check before a consequential action
- C. Gate the action on explicit, attributable approval
- D. Require human approval before a consequential action

### 74. A team relies only on prompt instructions to prevent data exfiltration. What is missing?

Domain: Securing and Governing Agentic Workflows

- A. Govern agent traffic through Agent Gateway
- B. Encode organizational policy in enforceable controls
- C. Screen prompts and responses with Model Armor
- D. Enforce a policy check before a consequential action

### 75. A high-risk action has no defined approver. What should be established?

Domain: Securing and Governing Agentic Workflows

- A. Gate the action on explicit, attributable approval
- B. Review high-impact actions with accountable owners
- C. Register agents and capabilities in Agent Registry
- D. Require human approval before a consequential action

### 76. An agent's autonomy is increased without changing review controls. What should be done?

Domain: Securing and Governing Agentic Workflows

- A. Enforce a policy check before a consequential action
- B. Set explicit pass thresholds before evaluating
- C. Use staged rollout with measurable rollback criteria
- D. Require human approval before a consequential action

### 77. A reviewer approves an action outside their authority. What control failed?

Domain: Securing and Governing Agentic Workflows

- A. Record agent actions and tool calls in audit logs
- B. Require human approval before a consequential action
- C. Review high-impact actions with accountable owners
- D. Use human review for unresolved or high-impact judgment

### 78. A content filter blocks an entire category of legitimate requests. What should be done?

Domain: Securing and Governing Agentic Workflows

- A. Inspect and de-identify sensitive data with Sensitive Data Protection
- B. Govern agent traffic through Agent Gateway
- C. Encode organizational policy in enforceable controls
- D. Enforce a policy check before a consequential action

### 79. A system automatically approves actions when a model scores confidence high. Why is this risky?

Domain: Securing and Governing Agentic Workflows

- A. Use a calibrated model-based autorater for scalable judgment
- B. Gate the action on explicit, attributable approval
- C. Enforce a policy check before a consequential action
- D. Require human approval before a consequential action

### 80. A guardrail triggers but the event is not recorded. What should be added?

Domain: Securing and Governing Agentic Workflows

- A. Record agent actions and tool calls in audit logs
- B. Encode organizational policy in enforceable controls
- C. Enforce a policy check before a consequential action
- D. Review high-impact actions with accountable owners

### 81. A user approves an action through a channel that cannot verify identity. What is missing?

Domain: Securing and Governing Agentic Workflows

- A. Use scoped OAuth 2.0 tokens for agent-to-tool calls
- B. Require human approval before a consequential action
- C. Govern agent traffic through Agent Gateway
- D. Gate the action on explicit, attributable approval

### 82. A workflow has more approval steps than risk requires. What should be evaluated?

Domain: Securing and Governing Agentic Workflows

- A. Enforce a policy check before a consequential action
- B. Encode organizational policy in enforceable controls
- C. Review high-impact actions with accountable owners
- D. Set explicit pass thresholds before evaluating

### 83. An agent must not send external communications without review. What design fits?

Domain: Securing and Governing Agentic Workflows

- A. Gate the action on explicit, attributable approval
- B. Require human approval before a consequential action
- C. Screen prompts and responses with Model Armor
- D. Enforce a policy check before a consequential action

### 84. A post-incident review finds the agent acted within permissions but against intent. What should change?

Domain: Securing and Governing Agentic Workflows

- A. Use human review for unresolved or high-impact judgment
- B. Review high-impact actions with accountable owners
- C. Record agent actions and tool calls in audit logs
- D. Encode organizational policy in enforceable controls

### 85. A prompt includes customer personal data not needed for the task. What should happen?

Domain: Securing and Governing Agentic Workflows

- A. Redact or de-identify sensitive data before model exposure
- B. Inspect and de-identify sensitive data with Sensitive Data Protection
- C. Screen prompts and responses with Model Armor
- D. Store secrets in Secret Manager rather than prompts or code

### 86. Retrieved content contains instructions to ignore the system prompt. What should the design assume?

Domain: Securing and Governing Agentic Workflows

- A. Require human approval before a consequential action
- B. Treat retrieved and user-supplied content as untrusted
- C. Screen prompts and responses with Model Armor
- D. Enforce a policy check before a consequential action

### 87. A personalization feature wants to retain user preferences indefinitely. What should guide the design?

Domain: Securing and Governing Agentic Workflows

- A. Record agent actions and tool calls in audit logs
- B. Redact or de-identify sensitive data before model exposure
- C. Encode organizational policy in enforceable controls
- D. Apply purpose limitation and consent to personal data

### 88. A developer pastes an API key into a test prompt. What should happen?

Domain: Securing and Governing Agentic Workflows

- A. Keep access tokens short-lived and narrowly scoped
- B. Store secrets in Secret Manager rather than prompts or code
- C. Redact or de-identify sensitive data before model exposure
- D. Use customer-managed encryption keys where required

### 89. An agent can send retrieved documents to an external summarization service. What should be verified?

Domain: Securing and Governing Agentic Workflows

- A. Restrict outbound network access to approved destinations
- B. Redact or de-identify sensitive data before model exposure
- C. Encode organizational policy in enforceable controls
- D. Govern agent traffic through Agent Gateway

### 90. A regulation requires control over encryption keys for agent data at rest. What should be configured?

Domain: Securing and Governing Agentic Workflows

- A. Constrain access with a principal access boundary policy
- B. Inspect and de-identify sensitive data with Sensitive Data Protection
- C. Use VPC Service Controls to establish a data perimeter
- D. Use customer-managed encryption keys where required

### 91. De-identification removes names but leaves rare combinations of attributes. What risk remains?

Domain: Securing and Governing Agentic Workflows

- A. Redact or de-identify sensitive data before model exposure
- B. Record agent actions and tool calls in audit logs
- C. Apply purpose limitation and consent to personal data
- D. Inspect and de-identify sensitive data with Sensitive Data Protection

### 92. A malicious document asks the agent to call a delete tool. What should prevent harm?

Domain: Securing and Governing Agentic Workflows

- A. Enforce a policy check before a consequential action
- B. Require human approval before a consequential action
- C. Expose a typed function as a tool
- D. Treat retrieved and user-supplied content as untrusted

### 93. A user requests deletion of data remembered by an agent. What should the design support?

Domain: Securing and Governing Agentic Workflows

- A. Redact or de-identify sensitive data before model exposure
- B. Register agents and capabilities in Agent Registry
- C. Apply purpose limitation and consent to personal data
- D. Encode organizational policy in enforceable controls

### 94. An agent tries to upload a file to an unapproved bucket. What should block it?

Domain: Securing and Governing Agentic Workflows

- A. Redact or de-identify sensitive data before model exposure
- B. Govern agent traffic through Agent Gateway
- C. Restrict outbound network access to approved destinations
- D. Store secrets in Secret Manager rather than prompts or code

### 95. A response includes a sensitive token that should never be shown. What layer should catch it?

Domain: Securing and Governing Agentic Workflows

- A. Use customer-managed encryption keys where required
- B. Inspect and de-identify sensitive data with Sensitive Data Protection
- C. Redact or de-identify sensitive data before model exposure
- D. Screen prompts and responses with Model Armor

### 96. A user instructs the agent to ignore data-access policy for an urgent request. What should happen?

Domain: Securing and Governing Agentic Workflows

- A. Treat retrieved and user-supplied content as untrusted
- B. Use human review for unresolved or high-impact judgment
- C. Encode organizational policy in enforceable controls
- D. Enforce a policy check before a consequential action

### 97. A team wants to prove that personal data was minimized in evaluation samples. What should it retain?

Domain: Securing and Governing Agentic Workflows

- A. Inspect and de-identify sensitive data with Sensitive Data Protection
- B. Apply purpose limitation and consent to personal data
- C. Redact or de-identify sensitive data before model exposure
- D. Record agent actions and tool calls in audit logs

### 98. A rotation policy for agent credentials is undefined. What should be established?

Domain: Securing and Governing Agentic Workflows

- A. Store secrets in Secret Manager rather than prompts or code
- B. Keep access tokens short-lived and narrowly scoped
- C. Use scoped OAuth 2.0 tokens for agent-to-tool calls
- D. Use customer-managed encryption keys where required

### 99. A support transcript contains health information irrelevant to the request. What should be done?

Domain: Securing and Governing Agentic Workflows

- A. Redact or de-identify sensitive data before model exposure
- B. Screen prompts and responses with Model Armor
- C. Apply purpose limitation and consent to personal data
- D. Inspect and de-identify sensitive data with Sensitive Data Protection

### 100. An indirect prompt-injection attempt is detected in retrieved content. What should be recorded?

Domain: Securing and Governing Agentic Workflows

- A. Record agent actions and tool calls in audit logs
- B. Govern agent traffic through Agent Gateway
- C. Treat retrieved and user-supplied content as untrusted
- D. Encode organizational policy in enforceable controls

---

## Answer key and explanations

### Question 1 — A

Answer: Use scoped OAuth 2.0 tokens for agent-to-tool calls. A short-lived OAuth 2.0 token scoped to the required operation and audience. Short-lived, scoped tokens limit what a tool call can do. Token handling and refresh must avoid broad standing access. Local study-map skill 5.1 (Authentication and Secure Tool Execution), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Correct. Short-lived, scoped tokens limit what a tool call can do. Token handling and refresh must avoid broad standing access. In this case: A short-lived OAuth 2.0 token scoped to the required operation and audience.
- **B:** Incorrect for this question. A dedicated identity separates the agent from human accounts and limits blast radius. Roles still need review and periodic reduction. In this case: A short-lived OAuth 2.0 token scoped to the required operation and audience.
- **C:** Incorrect for this question. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: A short-lived OAuth 2.0 token scoped to the required operation and audience.
- **D:** Incorrect for this question. Short lifetimes and audience limits reduce misuse. Tokens should not be placed in prompts or logs. In this case: A short-lived OAuth 2.0 token scoped to the required operation and audience.

### Question 2 — D

Answer: Keep access tokens short-lived and narrowly scoped. Reduce scope and lifetime to what the workflow actually needs. Short lifetimes and audience limits reduce misuse. Tokens should not be placed in prompts or logs. Local study-map skill 5.1 (Authentication and Secure Tool Execution), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Reduce scope and lifetime to what the workflow actually needs.
- **B:** Incorrect for this question. Managed secret storage supports rotation and access control. A prompt instruction is not a secret-protection mechanism. In this case: Reduce scope and lifetime to what the workflow actually needs.
- **C:** Incorrect for this question. Short-lived, scoped tokens limit what a tool call can do. Token handling and refresh must avoid broad standing access. In this case: Reduce scope and lifetime to what the workflow actually needs.
- **D:** Correct. Short lifetimes and audience limits reduce misuse. Tokens should not be placed in prompts or logs. In this case: Reduce scope and lifetime to what the workflow actually needs.

### Question 3 — C

Answer: Use a dedicated service account with least privilege. Actions cannot be attributed, and compromise affects every system sharing it. A dedicated identity separates the agent from human accounts and limits blast radius. Roles still need review and periodic reduction. Local study-map skill 5.1 (Authentication and Secure Tool Execution), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: Actions cannot be attributed, and compromise affects every system sharing it.
- **B:** Incorrect for this question. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: Actions cannot be attributed, and compromise affects every system sharing it.
- **C:** Correct. A dedicated identity separates the agent from human accounts and limits blast radius. Roles still need review and periodic reduction. In this case: Actions cannot be attributed, and compromise affects every system sharing it.
- **D:** Incorrect for this question. Distinct identity makes access attributable and auditable. Sharing a human or broad service identity weakens least privilege. In this case: Actions cannot be attributed, and compromise affects every system sharing it.

### Question 4 — C

Answer: Give each agent its own managed identity. A dedicated managed identity per agent. Distinct identity makes access attributable and auditable. Sharing a human or broad service identity weakens least privilege. Local study-map skill 5.1 (Authentication and Secure Tool Execution), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. A dedicated identity separates the agent from human accounts and limits blast radius. Roles still need review and periodic reduction. In this case: A dedicated managed identity per agent.
- **B:** Incorrect for this question. Short-lived, scoped tokens limit what a tool call can do. Token handling and refresh must avoid broad standing access. In this case: A dedicated managed identity per agent.
- **C:** Correct. Distinct identity makes access attributable and auditable. Sharing a human or broad service identity weakens least privilege. In this case: A dedicated managed identity per agent.
- **D:** Incorrect for this question. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: A dedicated managed identity per agent.

### Question 5 — D

Answer: Propagate the caller's identity to downstream tools. Verified user identity with scoped delegated authority. Downstream authorization needs the actual principal, not a generic agent identity. Delegation must be explicit and scoped. Local study-map skill 5.1 (Authentication and Secure Tool Execution), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Verified user identity with scoped delegated authority.
- **B:** Incorrect for this question. Short-lived, scoped tokens limit what a tool call can do. Token handling and refresh must avoid broad standing access. In this case: Verified user identity with scoped delegated authority.
- **C:** Incorrect for this question. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: Verified user identity with scoped delegated authority.
- **D:** Correct. Downstream authorization needs the actual principal, not a generic agent identity. Delegation must be explicit and scoped. In this case: Verified user identity with scoped delegated authority.

### Question 6 — D

Answer: Use scoped OAuth 2.0 tokens for agent-to-tool calls. The token should carry only the minimum scope needed for the intended read operation. Short-lived, scoped tokens limit what a tool call can do. Token handling and refresh must avoid broad standing access. Local study-map skill 5.1 (Authentication and Secure Tool Execution), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Short lifetimes and audience limits reduce misuse. Tokens should not be placed in prompts or logs. In this case: The token should carry only the minimum scope needed for the intended read operation.
- **B:** Incorrect for this question. Classification and de-identification reduce unnecessary exposure. De-identification must be validated for the specific data and purpose. In this case: The token should carry only the minimum scope needed for the intended read operation.
- **C:** Incorrect for this question. Managed secret storage supports rotation and access control. A prompt instruction is not a secret-protection mechanism. In this case: The token should carry only the minimum scope needed for the intended read operation.
- **D:** Correct. Short-lived, scoped tokens limit what a tool call can do. Token handling and refresh must avoid broad standing access. In this case: The token should carry only the minimum scope needed for the intended read operation.

### Question 7 — B

Answer: Grant IAM roles to the agent identity, not to users' credentials. Replace broad roles with narrowly scoped permissions. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. Local study-map skill 5.1 (Authentication and Secure Tool Execution), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Distinct identity makes access attributable and auditable. Sharing a human or broad service identity weakens least privilege. In this case: Replace broad roles with narrowly scoped permissions.
- **B:** Correct. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: Replace broad roles with narrowly scoped permissions.
- **C:** Incorrect for this question. A dedicated identity separates the agent from human accounts and limits blast radius. Roles still need review and periodic reduction. In this case: Replace broad roles with narrowly scoped permissions.
- **D:** Incorrect for this question. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: Replace broad roles with narrowly scoped permissions.

### Question 8 — A

Answer: Store secrets in Secret Manager rather than prompts or code. Remove it, move it to managed secret storage, and rotate it. Managed secret storage supports rotation and access control. A prompt instruction is not a secret-protection mechanism. Local study-map skill 5.1 (Authentication and Secure Tool Execution), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Correct. Managed secret storage supports rotation and access control. A prompt instruction is not a secret-protection mechanism. In this case: Remove it, move it to managed secret storage, and rotate it.
- **B:** Incorrect for this question. Classification and de-identification reduce unnecessary exposure. De-identification must be validated for the specific data and purpose. In this case: Remove it, move it to managed secret storage, and rotate it.
- **C:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Remove it, move it to managed secret storage, and rotate it.
- **D:** Incorrect for this question. Minimization reduces the impact of leakage and over-retention. Verify that redaction survives the whole pipeline. In this case: Remove it, move it to managed secret storage, and rotate it.

### Question 9 — C

Answer: Use scoped OAuth 2.0 tokens for agent-to-tool calls. Token misuse beyond the intended service or action. Short-lived, scoped tokens limit what a tool call can do. Token handling and refresh must avoid broad standing access. Local study-map skill 5.1 (Authentication and Secure Tool Execution), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Token misuse beyond the intended service or action.
- **B:** Incorrect for this question. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: Token misuse beyond the intended service or action.
- **C:** Correct. Short-lived, scoped tokens limit what a tool call can do. Token handling and refresh must avoid broad standing access. In this case: Token misuse beyond the intended service or action.
- **D:** Incorrect for this question. Downstream authorization needs the actual principal, not a generic agent identity. Delegation must be explicit and scoped. In this case: Token misuse beyond the intended service or action.

### Question 10 — B

Answer: Keep access tokens short-lived and narrowly scoped. Short-lived tokens refreshed through a controlled mechanism. Short lifetimes and audience limits reduce misuse. Tokens should not be placed in prompts or logs. Local study-map skill 5.1 (Authentication and Secure Tool Execution), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Short-lived tokens refreshed through a controlled mechanism.
- **B:** Correct. Short lifetimes and audience limits reduce misuse. Tokens should not be placed in prompts or logs. In this case: Short-lived tokens refreshed through a controlled mechanism.
- **C:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Short-lived tokens refreshed through a controlled mechanism.
- **D:** Incorrect for this question. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: Short-lived tokens refreshed through a controlled mechanism.

### Question 11 — A

Answer: Use a dedicated service account with least privilege. A role scoped to the specific bucket or object prefix. A dedicated identity separates the agent from human accounts and limits blast radius. Roles still need review and periodic reduction. Local study-map skill 5.1 (Authentication and Secure Tool Execution), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Correct. A dedicated identity separates the agent from human accounts and limits blast radius. Roles still need review and periodic reduction. In this case: A role scoped to the specific bucket or object prefix.
- **B:** Incorrect for this question. A service perimeter can reduce exfiltration paths for supported services. It complements, rather than replaces, IAM and application checks. In this case: A role scoped to the specific bucket or object prefix.
- **C:** Incorrect for this question. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: A role scoped to the specific bucket or object prefix.
- **D:** Incorrect for this question. Narrow roles and scopes reduce blast radius. Review permissions as the workflow evolves. In this case: A role scoped to the specific bucket or object prefix.

### Question 12 — B

Answer: Propagate the caller's identity to downstream tools. Authenticated caller identity and explicit delegation scope. Downstream authorization needs the actual principal, not a generic agent identity. Delegation must be explicit and scoped. Local study-map skill 5.1 (Authentication and Secure Tool Execution), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: Authenticated caller identity and explicit delegation scope.
- **B:** Correct. Downstream authorization needs the actual principal, not a generic agent identity. Delegation must be explicit and scoped. In this case: Authenticated caller identity and explicit delegation scope.
- **C:** Incorrect for this question. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. In this case: Authenticated caller identity and explicit delegation scope.
- **D:** Incorrect for this question. A2A supports discovery and task exchange between agents that may be built on different stacks. Trust and authorization still need explicit design. In this case: Authenticated caller identity and explicit delegation scope.

### Question 13 — D

Answer: Store secrets in Secret Manager rather than prompts or code. Secret Manager with access controls and rotation. Managed secret storage supports rotation and access control. A prompt instruction is not a secret-protection mechanism. Local study-map skill 5.1 (Authentication and Secure Tool Execution), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Minimization reduces the impact of leakage and over-retention. Verify that redaction survives the whole pipeline. In this case: Secret Manager with access controls and rotation.
- **B:** Incorrect for this question. Classification and de-identification reduce unnecessary exposure. De-identification must be validated for the specific data and purpose. In this case: Secret Manager with access controls and rotation.
- **C:** Incorrect for this question. CMEK supports key-control and compliance requirements. Key lifecycle and break-glass procedures need operational ownership. In this case: Secret Manager with access controls and rotation.
- **D:** Correct. Managed secret storage supports rotation and access control. A prompt instruction is not a secret-protection mechanism. In this case: Secret Manager with access controls and rotation.

### Question 14 — A

Answer: Grant IAM roles to the agent identity, not to users' credentials. Change review and audit for identity and role modifications. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. Local study-map skill 5.1 (Authentication and Secure Tool Execution), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Correct. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: Change review and audit for identity and role modifications.
- **B:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Change review and audit for identity and role modifications.
- **C:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Change review and audit for identity and role modifications.
- **D:** Incorrect for this question. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: Change review and audit for identity and role modifications.

### Question 15 — D

Answer: Use scoped OAuth 2.0 tokens for agent-to-tool calls. Delegation requires explicit authorization and scoped consent. Short-lived, scoped tokens limit what a tool call can do. Token handling and refresh must avoid broad standing access. Local study-map skill 5.1 (Authentication and Secure Tool Execution), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: Delegation requires explicit authorization and scoped consent.
- **B:** Incorrect for this question. Downstream authorization needs the actual principal, not a generic agent identity. Delegation must be explicit and scoped. In this case: Delegation requires explicit authorization and scoped consent.
- **C:** Incorrect for this question. A dedicated identity separates the agent from human accounts and limits blast radius. Roles still need review and periodic reduction. In this case: Delegation requires explicit authorization and scoped consent.
- **D:** Correct. Short-lived, scoped tokens limit what a tool call can do. Token handling and refresh must avoid broad standing access. In this case: Delegation requires explicit authorization and scoped consent.

### Question 16 — B

Answer: Keep access tokens short-lived and narrowly scoped. Pass credentials in a protected channel and exclude them from logs. Short lifetimes and audience limits reduce misuse. Tokens should not be placed in prompts or logs. Local study-map skill 5.1 (Authentication and Secure Tool Execution), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Egress controls reduce exfiltration and unauthorized tool reach. They should be paired with identity and data controls. In this case: Pass credentials in a protected channel and exclude them from logs.
- **B:** Correct. Short lifetimes and audience limits reduce misuse. Tokens should not be placed in prompts or logs. In this case: Pass credentials in a protected channel and exclude them from logs.
- **C:** Incorrect for this question. Short-lived, scoped tokens limit what a tool call can do. Token handling and refresh must avoid broad standing access. In this case: Pass credentials in a protected channel and exclude them from logs.
- **D:** Incorrect for this question. Managed secret storage supports rotation and access control. A prompt instruction is not a secret-protection mechanism. In this case: Pass credentials in a protected channel and exclude them from logs.

### Question 17 — D

Answer: Constrain access with a principal access boundary policy. A principal access boundary scoped to approved resources. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. Local study-map skill 5.2 (Principal Access Boundaries), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: A principal access boundary scoped to approved resources.
- **B:** Incorrect for this question. A service perimeter can reduce exfiltration paths for supported services. It complements, rather than replaces, IAM and application checks. In this case: A principal access boundary scoped to approved resources.
- **C:** Incorrect for this question. Narrow roles and scopes reduce blast radius. Review permissions as the workflow evolves. In this case: A principal access boundary scoped to approved resources.
- **D:** Correct. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: A principal access boundary scoped to approved resources.

### Question 18 — D

Answer: Grant the minimum permissions required for the task. Review and remove unnecessary grants after the incident. Narrow roles and scopes reduce blast radius. Review permissions as the workflow evolves. Local study-map skill 5.2 (Principal Access Boundaries), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: Review and remove unnecessary grants after the incident.
- **B:** Incorrect for this question. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: Review and remove unnecessary grants after the incident.
- **C:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Review and remove unnecessary grants after the incident.
- **D:** Correct. Narrow roles and scopes reduce blast radius. Review permissions as the workflow evolves. In this case: Review and remove unnecessary grants after the incident.

### Question 19 — A

Answer: Use VPC Service Controls to establish a data perimeter. A service perimeter with appropriate ingress and egress rules. A service perimeter can reduce exfiltration paths for supported services. It complements, rather than replaces, IAM and application checks. Local study-map skill 5.2 (Principal Access Boundaries), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Correct. A service perimeter can reduce exfiltration paths for supported services. It complements, rather than replaces, IAM and application checks. In this case: A service perimeter with appropriate ingress and egress rules.
- **B:** Incorrect for this question. Egress controls reduce exfiltration and unauthorized tool reach. They should be paired with identity and data controls. In this case: A service perimeter with appropriate ingress and egress rules.
- **C:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: A service perimeter with appropriate ingress and egress rules.
- **D:** Incorrect for this question. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: A service perimeter with appropriate ingress and egress rules.

### Question 20 — B

Answer: Constrain access with a principal access boundary policy. Do not bypass the control; use the approved exception process. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. Local study-map skill 5.2 (Principal Access Boundaries), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: Do not bypass the control; use the approved exception process.
- **B:** Correct. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: Do not bypass the control; use the approved exception process.
- **C:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Do not bypass the control; use the approved exception process.
- **D:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Do not bypass the control; use the approved exception process.

### Question 21 — B

Answer: Grant the minimum permissions required for the task. Separation of duties and tamper-resistant audit are missing. Narrow roles and scopes reduce blast radius. Review permissions as the workflow evolves. Local study-map skill 5.2 (Principal Access Boundaries), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: Separation of duties and tamper-resistant audit are missing.
- **B:** Correct. Narrow roles and scopes reduce blast radius. Review permissions as the workflow evolves. In this case: Separation of duties and tamper-resistant audit are missing.
- **C:** Incorrect for this question. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: Separation of duties and tamper-resistant audit are missing.
- **D:** Incorrect for this question. A dedicated identity separates the agent from human accounts and limits blast radius. Roles still need review and periodic reduction. In this case: Separation of duties and tamper-resistant audit are missing.

### Question 22 — A

Answer: Constrain access with a principal access boundary policy. Verify with representative allowed and denied access attempts. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. Local study-map skill 5.2 (Principal Access Boundaries), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Correct. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: Verify with representative allowed and denied access attempts.
- **B:** Incorrect for this question. Short-lived, scoped tokens limit what a tool call can do. Token handling and refresh must avoid broad standing access. In this case: Verify with representative allowed and denied access attempts.
- **C:** Incorrect for this question. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: Verify with representative allowed and denied access attempts.
- **D:** Incorrect for this question. A service perimeter can reduce exfiltration paths for supported services. It complements, rather than replaces, IAM and application checks. In this case: Verify with representative allowed and denied access attempts.

### Question 23 — A

Answer: Grant IAM roles to the agent identity, not to users' credentials. Grant resource-level or dataset-level permissions instead of project-wide access. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. Local study-map skill 5.2 (Principal Access Boundaries), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Correct. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: Grant resource-level or dataset-level permissions instead of project-wide access.
- **B:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Grant resource-level or dataset-level permissions instead of project-wide access.
- **C:** Incorrect for this question. Narrow roles and scopes reduce blast radius. Review permissions as the workflow evolves. In this case: Grant resource-level or dataset-level permissions instead of project-wide access.
- **D:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Grant resource-level or dataset-level permissions instead of project-wide access.

### Question 24 — C

Answer: Use VPC Service Controls to establish a data perimeter. A documented, narrow egress path through approved controls. A service perimeter can reduce exfiltration paths for supported services. It complements, rather than replaces, IAM and application checks. Local study-map skill 5.2 (Principal Access Boundaries), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Classification and de-identification reduce unnecessary exposure. De-identification must be validated for the specific data and purpose. In this case: A documented, narrow egress path through approved controls.
- **B:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: A documented, narrow egress path through approved controls.
- **C:** Correct. A service perimeter can reduce exfiltration paths for supported services. It complements, rather than replaces, IAM and application checks. In this case: A documented, narrow egress path through approved controls.
- **D:** Incorrect for this question. Egress controls reduce exfiltration and unauthorized tool reach. They should be paired with identity and data controls. In this case: A documented, narrow egress path through approved controls.

### Question 25 — A

Answer: Constrain access with a principal access boundary policy. Environment-specific identities and boundaries with consistent policy intent. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. Local study-map skill 5.2 (Principal Access Boundaries), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Correct. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: Environment-specific identities and boundaries with consistent policy intent.
- **B:** Incorrect for this question. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: Environment-specific identities and boundaries with consistent policy intent.
- **C:** Incorrect for this question. A dedicated identity separates the agent from human accounts and limits blast radius. Roles still need review and periodic reduction. In this case: Environment-specific identities and boundaries with consistent policy intent.
- **D:** Incorrect for this question. Distinct identity makes access attributable and auditable. Sharing a human or broad service identity weakens least privilege. In this case: Environment-specific identities and boundaries with consistent policy intent.

### Question 26 — B

Answer: Grant the minimum permissions required for the task. Separate test identities and permissions from production. Narrow roles and scopes reduce blast radius. Review permissions as the workflow evolves. Local study-map skill 5.2 (Principal Access Boundaries), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: Separate test identities and permissions from production.
- **B:** Correct. Narrow roles and scopes reduce blast radius. Review permissions as the workflow evolves. In this case: Separate test identities and permissions from production.
- **C:** Incorrect for this question. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: Separate test identities and permissions from production.
- **D:** Incorrect for this question. Quotas and scaling limits can become the real bottleneck. Plan for bursts and graceful degradation. In this case: Separate test identities and permissions from production.

### Question 27 — A

Answer: Govern agent traffic through Agent Gateway. Whether the service is in scope and whether the path is approved. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. Local study-map skill 5.2 (Principal Access Boundaries), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Correct. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Whether the service is in scope and whether the path is approved.
- **B:** Incorrect for this question. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: Whether the service is in scope and whether the path is approved.
- **C:** Incorrect for this question. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: Whether the service is in scope and whether the path is approved.
- **D:** Incorrect for this question. A service perimeter can reduce exfiltration paths for supported services. It complements, rather than replaces, IAM and application checks. In this case: Whether the service is in scope and whether the path is approved.

### Question 28 — D

Answer: Grant IAM roles to the agent identity, not to users' credentials. Named ownership and periodic access review. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. Local study-map skill 5.2 (Principal Access Boundaries), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Named ownership and periodic access review.
- **B:** Incorrect for this question. Narrow roles and scopes reduce blast radius. Review permissions as the workflow evolves. In this case: Named ownership and periodic access review.
- **C:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Named ownership and periodic access review.
- **D:** Correct. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: Named ownership and periodic access review.

### Question 29 — D

Answer: Use VPC Service Controls to establish a data perimeter. Perimeter controls reduce exfiltration paths; encryption requires separate configuration. A service perimeter can reduce exfiltration paths for supported services. It complements, rather than replaces, IAM and application checks. Local study-map skill 5.2 (Principal Access Boundaries), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: Perimeter controls reduce exfiltration paths; encryption requires separate configuration.
- **B:** Incorrect for this question. CMEK supports key-control and compliance requirements. Key lifecycle and break-glass procedures need operational ownership. In this case: Perimeter controls reduce exfiltration paths; encryption requires separate configuration.
- **C:** Incorrect for this question. Classification and de-identification reduce unnecessary exposure. De-identification must be validated for the specific data and purpose. In this case: Perimeter controls reduce exfiltration paths; encryption requires separate configuration.
- **D:** Correct. A service perimeter can reduce exfiltration paths for supported services. It complements, rather than replaces, IAM and application checks. In this case: Perimeter controls reduce exfiltration paths; encryption requires separate configuration.

### Question 30 — A

Answer: Constrain access with a principal access boundary policy. Evaluate the requirement and adjust the boundary or tool scope through approval. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. Local study-map skill 5.2 (Principal Access Boundaries), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Correct. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: Evaluate the requirement and adjust the boundary or tool scope through approval.
- **B:** Incorrect for this question. Narrow roles and scopes reduce blast radius. Review permissions as the workflow evolves. In this case: Evaluate the requirement and adjust the boundary or tool scope through approval.
- **C:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Evaluate the requirement and adjust the boundary or tool scope through approval.
- **D:** Incorrect for this question. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: Evaluate the requirement and adjust the boundary or tool scope through approval.

### Question 31 — C

Answer: Give each agent its own managed identity. Access changes unpredictably; use a dedicated agent identity. Distinct identity makes access attributable and auditable. Sharing a human or broad service identity weakens least privilege. Local study-map skill 5.2 (Principal Access Boundaries), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: Access changes unpredictably; use a dedicated agent identity.
- **B:** Incorrect for this question. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: Access changes unpredictably; use a dedicated agent identity.
- **C:** Correct. Distinct identity makes access attributable and auditable. Sharing a human or broad service identity weakens least privilege. In this case: Access changes unpredictably; use a dedicated agent identity.
- **D:** Incorrect for this question. Short-lived, scoped tokens limit what a tool call can do. Token handling and refresh must avoid broad standing access. In this case: Access changes unpredictably; use a dedicated agent identity.

### Question 32 — B

Answer: Grant the minimum permissions required for the task. A time-bound expiry and automatic review. Narrow roles and scopes reduce blast radius. Review permissions as the workflow evolves. Local study-map skill 5.2 (Principal Access Boundaries), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: A time-bound expiry and automatic review.
- **B:** Correct. Narrow roles and scopes reduce blast radius. Review permissions as the workflow evolves. In this case: A time-bound expiry and automatic review.
- **C:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: A time-bound expiry and automatic review.
- **D:** Incorrect for this question. Quotas and scaling limits can become the real bottleneck. Plan for bursts and graceful degradation. In this case: A time-bound expiry and automatic review.

### Question 33 — C

Answer: Constrain access with a principal access boundary policy. The permitted operation and destination, not only the service. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. Local study-map skill 5.2 (Principal Access Boundaries), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. A service perimeter can reduce exfiltration paths for supported services. It complements, rather than replaces, IAM and application checks. In this case: The permitted operation and destination, not only the service.
- **B:** Incorrect for this question. Egress controls reduce exfiltration and unauthorized tool reach. They should be paired with identity and data controls. In this case: The permitted operation and destination, not only the service.
- **C:** Correct. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: The permitted operation and destination, not only the service.
- **D:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: The permitted operation and destination, not only the service.

### Question 34 — C

Answer: Govern agent traffic through Agent Gateway. Agent Gateway with logging and policy enforcement. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. Local study-map skill 5.3 (Agent Gateway and Traffic Governance), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Egress controls reduce exfiltration and unauthorized tool reach. They should be paired with identity and data controls. In this case: Agent Gateway with logging and policy enforcement.
- **B:** Incorrect for this question. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: Agent Gateway with logging and policy enforcement.
- **C:** Correct. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Agent Gateway with logging and policy enforcement.
- **D:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Agent Gateway with logging and policy enforcement.

### Question 35 — C

Answer: Record agent actions and tool calls in audit logs. Egress restrictions and gateway inspection before the request leaves. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. Local study-map skill 5.3 (Agent Gateway and Traffic Governance), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Classification and de-identification reduce unnecessary exposure. De-identification must be validated for the specific data and purpose. In this case: Egress restrictions and gateway inspection before the request leaves.
- **B:** Incorrect for this question. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. In this case: Egress restrictions and gateway inspection before the request leaves.
- **C:** Correct. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Egress restrictions and gateway inspection before the request leaves.
- **D:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Egress restrictions and gateway inspection before the request leaves.

### Question 36 — B

Answer: Govern agent traffic through Agent Gateway. Authentication does not establish authorization for that specific action. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. Local study-map skill 5.3 (Agent Gateway and Traffic Governance), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Short-lived, scoped tokens limit what a tool call can do. Token handling and refresh must avoid broad standing access. In this case: Authentication does not establish authorization for that specific action.
- **B:** Correct. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Authentication does not establish authorization for that specific action.
- **C:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Authentication does not establish authorization for that specific action.
- **D:** Incorrect for this question. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: Authentication does not establish authorization for that specific action.

### Question 37 — D

Answer: Record agent actions and tool calls in audit logs. Correlated gateway and trace logs with agent identity. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. Local study-map skill 5.3 (Agent Gateway and Traffic Governance), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: Correlated gateway and trace logs with agent identity.
- **B:** Incorrect for this question. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. In this case: Correlated gateway and trace logs with agent identity.
- **C:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Correlated gateway and trace logs with agent identity.
- **D:** Correct. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Correlated gateway and trace logs with agent identity.

### Question 38 — C

Answer: Restrict outbound network access to approved destinations. An allowlist of approved destinations with monitored egress. Egress controls reduce exfiltration and unauthorized tool reach. They should be paired with identity and data controls. Local study-map skill 5.3 (Agent Gateway and Traffic Governance), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Classification and de-identification reduce unnecessary exposure. De-identification must be validated for the specific data and purpose. In this case: An allowlist of approved destinations with monitored egress.
- **B:** Incorrect for this question. A service perimeter can reduce exfiltration paths for supported services. It complements, rather than replaces, IAM and application checks. In this case: An allowlist of approved destinations with monitored egress.
- **C:** Correct. Egress controls reduce exfiltration and unauthorized tool reach. They should be paired with identity and data controls. In this case: An allowlist of approved destinations with monitored egress.
- **D:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: An allowlist of approved destinations with monitored egress.

### Question 39 — B

Answer: Govern agent traffic through Agent Gateway. Log the event, return a safe response, and alert if the pattern persists. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. Local study-map skill 5.3 (Agent Gateway and Traffic Governance), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. In this case: Log the event, return a safe response, and alert if the pattern persists.
- **B:** Correct. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Log the event, return a safe response, and alert if the pattern persists.
- **C:** Incorrect for this question. Human-in-the-loop review is appropriate when impact or uncertainty is high. Approval must occur before the effect and with enough context to decide. In this case: Log the event, return a safe response, and alert if the pattern persists.
- **D:** Incorrect for this question. Model Armor can help detect prompt injection, unsafe content, and sensitive data patterns. It is a layered control, not a complete trust boundary. In this case: Log the event, return a safe response, and alert if the pattern persists.

### Question 40 — C

Answer: Record agent actions and tool calls in audit logs. Policy-appropriate gating or alerting for the action and time window. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. Local study-map skill 5.3 (Agent Gateway and Traffic Governance), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Policy-appropriate gating or alerting for the action and time window.
- **B:** Incorrect for this question. Impact review assigns responsibility for consequential outcomes. It should be timely and informed by evidence. In this case: Policy-appropriate gating or alerting for the action and time window.
- **C:** Correct. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Policy-appropriate gating or alerting for the action and time window.
- **D:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Policy-appropriate gating or alerting for the action and time window.

### Question 41 — C

Answer: Govern agent traffic through Agent Gateway. Deny the call and record the attempt. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. Local study-map skill 5.3 (Agent Gateway and Traffic Governance), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: Deny the call and record the attempt.
- **B:** Incorrect for this question. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: Deny the call and record the attempt.
- **C:** Correct. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Deny the call and record the attempt.
- **D:** Incorrect for this question. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: Deny the call and record the attempt.

### Question 42 — C

Answer: Use Cloud Logging, Cloud Trace, and Cloud Monitoring. Log metadata and redacted content under retention policy. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. Local study-map skill 5.3 (Agent Gateway and Traffic Governance), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Cost attribution supports optimization and budgeting. Per-task cost reveals expensive failure paths. In this case: Log metadata and redacted content under retention policy.
- **B:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Log metadata and redacted content under retention policy.
- **C:** Correct. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. In this case: Log metadata and redacted content under retention policy.
- **D:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Log metadata and redacted content under retention policy.

### Question 43 — B

Answer: Govern agent traffic through Agent Gateway. An approval decision tied to the specific transaction. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. Local study-map skill 5.3 (Agent Gateway and Traffic Governance), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: An approval decision tied to the specific transaction.
- **B:** Correct. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: An approval decision tied to the specific transaction.
- **C:** Incorrect for this question. Approval should identify who approved what and under which evidence. A vague acknowledgment is not authorization. In this case: An approval decision tied to the specific transaction.
- **D:** Incorrect for this question. Human-in-the-loop review is appropriate when impact or uncertainty is high. Approval must occur before the effect and with enough context to decide. In this case: An approval decision tied to the specific transaction.

### Question 44 — D

Answer: Restrict outbound network access to approved destinations. Egress policy and destination allowlisting prevent connections to unapproved external hosts. Egress controls reduce exfiltration and unauthorized tool reach. They should be paired with identity and data controls. Local study-map skill 5.3 (Agent Gateway and Traffic Governance), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Managed secret storage supports rotation and access control. A prompt instruction is not a secret-protection mechanism. In this case: Egress policy and destination allowlisting prevent connections to unapproved external hosts.
- **B:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Egress policy and destination allowlisting prevent connections to unapproved external hosts.
- **C:** Incorrect for this question. Classification and de-identification reduce unnecessary exposure. De-identification must be validated for the specific data and purpose. In this case: Egress policy and destination allowlisting prevent connections to unapproved external hosts.
- **D:** Correct. Egress controls reduce exfiltration and unauthorized tool reach. They should be paired with identity and data controls. In this case: Egress policy and destination allowlisting prevent connections to unapproved external hosts.

### Question 45 — B

Answer: Record agent actions and tool calls in audit logs. Registry visibility and gateway policy for remote callers. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. Local study-map skill 5.3 (Agent Gateway and Traffic Governance), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Registry visibility and gateway policy for remote callers.
- **B:** Correct. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Registry visibility and gateway policy for remote callers.
- **C:** Incorrect for this question. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: Registry visibility and gateway policy for remote callers.
- **D:** Incorrect for this question. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. In this case: Registry visibility and gateway policy for remote callers.

### Question 46 — C

Answer: Govern agent traffic through Agent Gateway. Inspect and block or redact before the request leaves the boundary. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. Local study-map skill 5.3 (Agent Gateway and Traffic Governance), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Classification and de-identification reduce unnecessary exposure. De-identification must be validated for the specific data and purpose. In this case: Inspect and block or redact before the request leaves the boundary.
- **B:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Inspect and block or redact before the request leaves the boundary.
- **C:** Correct. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Inspect and block or redact before the request leaves the boundary.
- **D:** Incorrect for this question. Model Armor can help detect prompt injection, unsafe content, and sensitive data patterns. It is a layered control, not a complete trust boundary. In this case: Inspect and block or redact before the request leaves the boundary.

### Question 47 — C

Answer: Use Cloud Logging, Cloud Trace, and Cloud Monitoring. Per-agent call rates and deviations from baseline. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. Local study-map skill 5.3 (Agent Gateway and Traffic Governance), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Per-agent call rates and deviations from baseline.
- **B:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Per-agent call rates and deviations from baseline.
- **C:** Correct. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. In this case: Per-agent call rates and deviations from baseline.
- **D:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Per-agent call rates and deviations from baseline.

### Question 48 — B

Answer: Govern agent traffic through Agent Gateway. Update the policy and test the affected paths. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. Local study-map skill 5.3 (Agent Gateway and Traffic Governance), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Short-lived, scoped tokens limit what a tool call can do. Token handling and refresh must avoid broad standing access. In this case: Update the policy and test the affected paths.
- **B:** Correct. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Update the policy and test the affected paths.
- **C:** Incorrect for this question. Correct identity attribution supports audit and policy. Impersonating a user without authorization is not a convenience feature. In this case: Update the policy and test the affected paths.
- **D:** Incorrect for this question. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: Update the policy and test the affected paths.

### Question 49 — B

Answer: Govern agent traffic through Agent Gateway. Unmonitored or unauthorized traffic; require registration and policy before deployment. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. Local study-map skill 5.3 (Agent Gateway and Traffic Governance), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Unmonitored or unauthorized traffic; require registration and policy before deployment.
- **B:** Correct. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Unmonitored or unauthorized traffic; require registration and policy before deployment.
- **C:** Incorrect for this question. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: Unmonitored or unauthorized traffic; require registration and policy before deployment.
- **D:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Unmonitored or unauthorized traffic; require registration and policy before deployment.

### Question 50 — D

Answer: Record agent actions and tool calls in audit logs. No alerting or review path for denied high-risk attempts. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. Local study-map skill 5.3 (Agent Gateway and Traffic Governance), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: No alerting or review path for denied high-risk attempts.
- **B:** Incorrect for this question. Human-in-the-loop review is appropriate when impact or uncertainty is high. Approval must occur before the effect and with enough context to decide. In this case: No alerting or review path for denied high-risk attempts.
- **C:** Incorrect for this question. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. In this case: No alerting or review path for denied high-risk attempts.
- **D:** Correct. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: No alerting or review path for denied high-risk attempts.

### Question 51 — C

Answer: Screen prompts and responses with Model Armor. Model Armor or an equivalent input safety control. Model Armor can help detect prompt injection, unsafe content, and sensitive data patterns. It is a layered control, not a complete trust boundary. Local study-map skill 5.4 (Registry and Policy Enforcement), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Model Armor or an equivalent input safety control.
- **B:** Incorrect for this question. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. In this case: Model Armor or an equivalent input safety control.
- **C:** Correct. Model Armor can help detect prompt injection, unsafe content, and sensitive data patterns. It is a layered control, not a complete trust boundary. In this case: Model Armor or an equivalent input safety control.
- **D:** Incorrect for this question. Classification and de-identification reduce unnecessary exposure. De-identification must be validated for the specific data and purpose. In this case: Model Armor or an equivalent input safety control.

### Question 52 — A

Answer: Inspect and de-identify sensitive data with Sensitive Data Protection. Sensitive Data Protection inspection and redaction before delivery. Classification and de-identification reduce unnecessary exposure. De-identification must be validated for the specific data and purpose. Local study-map skill 5.4 (Registry and Policy Enforcement), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Correct. Classification and de-identification reduce unnecessary exposure. De-identification must be validated for the specific data and purpose. In this case: Sensitive Data Protection inspection and redaction before delivery.
- **B:** Incorrect for this question. Minimization reduces the impact of leakage and over-retention. Verify that redaction survives the whole pipeline. In this case: Sensitive Data Protection inspection and redaction before delivery.
- **C:** Incorrect for this question. Model Armor can help detect prompt injection, unsafe content, and sensitive data patterns. It is a layered control, not a complete trust boundary. In this case: Sensitive Data Protection inspection and redaction before delivery.
- **D:** Incorrect for this question. CMEK supports key-control and compliance requirements. Key lifecycle and break-glass procedures need operational ownership. In this case: Sensitive Data Protection inspection and redaction before delivery.

### Question 53 — A

Answer: Register agents and capabilities in Agent Registry. A registry with ownership, capability, and approval status. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. Local study-map skill 5.4 (Registry and Policy Enforcement), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Correct. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: A registry with ownership, capability, and approval status.
- **B:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: A registry with ownership, capability, and approval status.
- **C:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: A registry with ownership, capability, and approval status.
- **D:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: A registry with ownership, capability, and approval status.

### Question 54 — B

Answer: Screen prompts and responses with Model Armor. Review the policy and exception process rather than disable all protections. Model Armor can help detect prompt injection, unsafe content, and sensitive data patterns. It is a layered control, not a complete trust boundary. Local study-map skill 5.4 (Registry and Policy Enforcement), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Review the policy and exception process rather than disable all protections.
- **B:** Correct. Model Armor can help detect prompt injection, unsafe content, and sensitive data patterns. It is a layered control, not a complete trust boundary. In this case: Review the policy and exception process rather than disable all protections.
- **C:** Incorrect for this question. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. In this case: Review the policy and exception process rather than disable all protections.
- **D:** Incorrect for this question. Human-in-the-loop review is appropriate when impact or uncertainty is high. Approval must occur before the effect and with enough context to decide. In this case: Review the policy and exception process rather than disable all protections.

### Question 55 — D

Answer: Encode organizational policy in enforceable controls. Restrict the tool and egress path in code and gateway policy. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. Local study-map skill 5.4 (Registry and Policy Enforcement), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Restrict the tool and egress path in code and gateway policy.
- **B:** Incorrect for this question. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: Restrict the tool and egress path in code and gateway policy.
- **C:** Incorrect for this question. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. In this case: Restrict the tool and egress path in code and gateway policy.
- **D:** Correct. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Restrict the tool and egress path in code and gateway policy.

### Question 56 — D

Answer: Inspect and de-identify sensitive data with Sensitive Data Protection. Detection and de-identification before model exposure. Classification and de-identification reduce unnecessary exposure. De-identification must be validated for the specific data and purpose. Local study-map skill 5.4 (Registry and Policy Enforcement), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. CMEK supports key-control and compliance requirements. Key lifecycle and break-glass procedures need operational ownership. In this case: Detection and de-identification before model exposure.
- **B:** Incorrect for this question. Minimization reduces the impact of leakage and over-retention. Verify that redaction survives the whole pipeline. In this case: Detection and de-identification before model exposure.
- **C:** Incorrect for this question. Model Armor can help detect prompt injection, unsafe content, and sensitive data patterns. It is a layered control, not a complete trust boundary. In this case: Detection and de-identification before model exposure.
- **D:** Correct. Classification and de-identification reduce unnecessary exposure. De-identification must be validated for the specific data and purpose. In this case: Detection and de-identification before model exposure.

### Question 57 — B

Answer: Register agents and capabilities in Agent Registry. No one maintains or retires it, and governance becomes unclear. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. Local study-map skill 5.4 (Registry and Policy Enforcement), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: No one maintains or retires it, and governance becomes unclear.
- **B:** Correct. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: No one maintains or retires it, and governance becomes unclear.
- **C:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: No one maintains or retires it, and governance becomes unclear.
- **D:** Incorrect for this question. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. In this case: No one maintains or retires it, and governance becomes unclear.

### Question 58 — C

Answer: Screen prompts and responses with Model Armor. Safety filtering and authorization are different layers; enforce both. Model Armor can help detect prompt injection, unsafe content, and sensitive data patterns. It is a layered control, not a complete trust boundary. Local study-map skill 5.4 (Registry and Policy Enforcement), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Human-in-the-loop review is appropriate when impact or uncertainty is high. Approval must occur before the effect and with enough context to decide. In this case: Safety filtering and authorization are different layers; enforce both.
- **B:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Safety filtering and authorization are different layers; enforce both.
- **C:** Correct. Model Armor can help detect prompt injection, unsafe content, and sensitive data patterns. It is a layered control, not a complete trust boundary. In this case: Safety filtering and authorization are different layers; enforce both.
- **D:** Incorrect for this question. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. In this case: Safety filtering and authorization are different layers; enforce both.

### Question 59 — D

Answer: Encode organizational policy in enforceable controls. Record a formal, time-bound exception with an accountable approver. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. Local study-map skill 5.4 (Registry and Policy Enforcement), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Approval should identify who approved what and under which evidence. A vague acknowledgment is not authorization. In this case: Record a formal, time-bound exception with an accountable approver.
- **B:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Record a formal, time-bound exception with an accountable approver.
- **C:** Incorrect for this question. Impact review assigns responsibility for consequential outcomes. It should be timely and informed by evidence. In this case: Record a formal, time-bound exception with an accountable approver.
- **D:** Correct. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Record a formal, time-bound exception with an accountable approver.

### Question 60 — C

Answer: Inspect and de-identify sensitive data with Sensitive Data Protection. Complete sensitive-data detection across the relevant categories. Classification and de-identification reduce unnecessary exposure. De-identification must be validated for the specific data and purpose. Local study-map skill 5.4 (Registry and Policy Enforcement), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Short lifetimes and audience limits reduce misuse. Tokens should not be placed in prompts or logs. In this case: Complete sensitive-data detection across the relevant categories.
- **B:** Incorrect for this question. Model Armor can help detect prompt injection, unsafe content, and sensitive data patterns. It is a layered control, not a complete trust boundary. In this case: Complete sensitive-data detection across the relevant categories.
- **C:** Correct. Classification and de-identification reduce unnecessary exposure. De-identification must be validated for the specific data and purpose. In this case: Complete sensitive-data detection across the relevant categories.
- **D:** Incorrect for this question. Minimization reduces the impact of leakage and over-retention. Verify that redaction survives the whole pipeline. In this case: Complete sensitive-data detection across the relevant categories.

### Question 61 — C

Answer: Register agents and capabilities in Agent Registry. Remove or mark it retired and revoke its access. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. Local study-map skill 5.4 (Registry and Policy Enforcement), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Remove or mark it retired and revoke its access.
- **B:** Incorrect for this question. Distinct identity makes access attributable and auditable. Sharing a human or broad service identity weakens least privilege. In this case: Remove or mark it retired and revoke its access.
- **C:** Correct. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: Remove or mark it retired and revoke its access.
- **D:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Remove or mark it retired and revoke its access.

### Question 62 — B

Answer: Enforce a policy check before a consequential action. Input screening, instruction isolation, least privilege, and approval for high-impact tools. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. Local study-map skill 5.4 (Registry and Policy Enforcement), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Human-in-the-loop review is appropriate when impact or uncertainty is high. Approval must occur before the effect and with enough context to decide. In this case: Input screening, instruction isolation, least privilege, and approval for high-impact tools.
- **B:** Correct. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. In this case: Input screening, instruction isolation, least privilege, and approval for high-impact tools.
- **C:** Incorrect for this question. Model Armor can help detect prompt injection, unsafe content, and sensitive data patterns. It is a layered control, not a complete trust boundary. In this case: Input screening, instruction isolation, least privilege, and approval for high-impact tools.
- **D:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Input screening, instruction isolation, least privilege, and approval for high-impact tools.

### Question 63 — B

Answer: Encode organizational policy in enforceable controls. All routes and agents covered by the policy intent. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. Local study-map skill 5.4 (Registry and Policy Enforcement), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: All routes and agents covered by the policy intent.
- **B:** Correct. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: All routes and agents covered by the policy intent.
- **C:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: All routes and agents covered by the policy intent.
- **D:** Incorrect for this question. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: All routes and agents covered by the policy intent.

### Question 64 — B

Answer: Screen prompts and responses with Model Armor. Apply the defined fallback or review path rather than silently continue. Model Armor can help detect prompt injection, unsafe content, and sensitive data patterns. It is a layered control, not a complete trust boundary. Local study-map skill 5.4 (Registry and Policy Enforcement), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Apply the defined fallback or review path rather than silently continue.
- **B:** Correct. Model Armor can help detect prompt injection, unsafe content, and sensitive data patterns. It is a layered control, not a complete trust boundary. In this case: Apply the defined fallback or review path rather than silently continue.
- **C:** Incorrect for this question. Classification and de-identification reduce unnecessary exposure. De-identification must be validated for the specific data and purpose. In this case: Apply the defined fallback or review path rather than silently continue.
- **D:** Incorrect for this question. Minimization reduces the impact of leakage and over-retention. Verify that redaction survives the whole pipeline. In this case: Apply the defined fallback or review path rather than silently continue.

### Question 65 — D

Answer: Use customer-managed encryption keys where required. CMEK on the relevant storage services with key lifecycle ownership. CMEK supports key-control and compliance requirements. Key lifecycle and break-glass procedures need operational ownership. Local study-map skill 5.4 (Registry and Policy Enforcement), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. A service perimeter can reduce exfiltration paths for supported services. It complements, rather than replaces, IAM and application checks. In this case: CMEK on the relevant storage services with key lifecycle ownership.
- **B:** Incorrect for this question. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: CMEK on the relevant storage services with key lifecycle ownership.
- **C:** Incorrect for this question. Classification and de-identification reduce unnecessary exposure. De-identification must be validated for the specific data and purpose. In this case: CMEK on the relevant storage services with key lifecycle ownership.
- **D:** Correct. CMEK supports key-control and compliance requirements. Key lifecycle and break-glass procedures need operational ownership. In this case: CMEK on the relevant storage services with key lifecycle ownership.

### Question 66 — A

Answer: Register agents and capabilities in Agent Registry. Approval and metadata review of the new capability. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. Local study-map skill 5.4 (Registry and Policy Enforcement), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Correct. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: Approval and metadata review of the new capability.
- **B:** Incorrect for this question. MCP provides a common interface between agents and capability servers. Server trust, scopes, and validation remain your responsibility. In this case: Approval and metadata review of the new capability.
- **C:** Incorrect for this question. Plugins make a capability set reusable across projects. Bundling does not remove the need to review each included permission and dependency. In this case: Approval and metadata review of the new capability.
- **D:** Incorrect for this question. An Agent Card helps other agents discover what a remote agent can do. It is descriptive metadata, not an authorization grant. In this case: Approval and metadata review of the new capability.

### Question 67 — A

Answer: Inspect and de-identify sensitive data with Sensitive Data Protection. Log only the necessary finding metadata, not the sensitive content. Classification and de-identification reduce unnecessary exposure. De-identification must be validated for the specific data and purpose. Local study-map skill 5.4 (Registry and Policy Enforcement), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Correct. Classification and de-identification reduce unnecessary exposure. De-identification must be validated for the specific data and purpose. In this case: Log only the necessary finding metadata, not the sensitive content.
- **B:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Log only the necessary finding metadata, not the sensitive content.
- **C:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Log only the necessary finding metadata, not the sensitive content.
- **D:** Incorrect for this question. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. In this case: Log only the necessary finding metadata, not the sensitive content.

### Question 68 — A

Answer: Enforce a policy check before a consequential action. Require human approval above a defined threshold. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. Local study-map skill 5.5 (Guardrails and Human-in-the-Loop), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Correct. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. In this case: Require human approval above a defined threshold.
- **B:** Incorrect for this question. Approval should identify who approved what and under which evidence. A vague acknowledgment is not authorization. In this case: Require human approval above a defined threshold.
- **C:** Incorrect for this question. Human-in-the-loop review is appropriate when impact or uncertainty is high. Approval must occur before the effect and with enough context to decide. In this case: Require human approval above a defined threshold.
- **D:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Require human approval above a defined threshold.

### Question 69 — C

Answer: Require human approval before a consequential action. The evidence, amount, customer impact, and policy basis for the decision. Human-in-the-loop review is appropriate when impact or uncertainty is high. Approval must occur before the effect and with enough context to decide. Local study-map skill 5.5 (Guardrails and Human-in-the-Loop), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: The evidence, amount, customer impact, and policy basis for the decision.
- **B:** Incorrect for this question. Impact review assigns responsibility for consequential outcomes. It should be timely and informed by evidence. In this case: The evidence, amount, customer impact, and policy basis for the decision.
- **C:** Correct. Human-in-the-loop review is appropriate when impact or uncertainty is high. Approval must occur before the effect and with enough context to decide. In this case: The evidence, amount, customer impact, and policy basis for the decision.
- **D:** Incorrect for this question. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. In this case: The evidence, amount, customer impact, and policy basis for the decision.

### Question 70 — D

Answer: Gate the action on explicit, attributable approval. The gate must precede the effect, not document it afterward. Approval should identify who approved what and under which evidence. A vague acknowledgment is not authorization. Local study-map skill 5.5 (Guardrails and Human-in-the-Loop), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. In this case: The gate must precede the effect, not document it afterward.
- **B:** Incorrect for this question. Human-in-the-loop review is appropriate when impact or uncertainty is high. Approval must occur before the effect and with enough context to decide. In this case: The gate must precede the effect, not document it afterward.
- **C:** Incorrect for this question. Short-lived, scoped tokens limit what a tool call can do. Token handling and refresh must avoid broad standing access. In this case: The gate must precede the effect, not document it afterward.
- **D:** Correct. Approval should identify who approved what and under which evidence. A vague acknowledgment is not authorization. In this case: The gate must precede the effect, not document it afterward.

### Question 71 — D

Answer: Enforce a policy check before a consequential action. A pre-action guardrail requiring explicit confirmation or approval. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. Local study-map skill 5.5 (Guardrails and Human-in-the-Loop), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: A pre-action guardrail requiring explicit confirmation or approval.
- **B:** Incorrect for this question. Human-in-the-loop review is appropriate when impact or uncertainty is high. Approval must occur before the effect and with enough context to decide. In this case: A pre-action guardrail requiring explicit confirmation or approval.
- **C:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: A pre-action guardrail requiring explicit confirmation or approval.
- **D:** Correct. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. In this case: A pre-action guardrail requiring explicit confirmation or approval.

### Question 72 — C

Answer: Review high-impact actions with accountable owners. Accountable human review with relevant policy expertise. Impact review assigns responsibility for consequential outcomes. It should be timely and informed by evidence. Local study-map skill 5.5 (Guardrails and Human-in-the-Loop), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Human-in-the-loop review is appropriate when impact or uncertainty is high. Approval must occur before the effect and with enough context to decide. In this case: Accountable human review with relevant policy expertise.
- **B:** Incorrect for this question. Autoraters can score nuanced qualities at scale. They require calibration against human judgments and periodic review. In this case: Accountable human review with relevant policy expertise.
- **C:** Correct. Impact review assigns responsibility for consequential outcomes. It should be timely and informed by evidence. In this case: Accountable human review with relevant policy expertise.
- **D:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Accountable human review with relevant policy expertise.

### Question 73 — D

Answer: Require human approval before a consequential action. Bind approval to the specific action and make it single-use. Human-in-the-loop review is appropriate when impact or uncertainty is high. Approval must occur before the effect and with enough context to decide. Local study-map skill 5.5 (Guardrails and Human-in-the-Loop), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Bind approval to the specific action and make it single-use.
- **B:** Incorrect for this question. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. In this case: Bind approval to the specific action and make it single-use.
- **C:** Incorrect for this question. Approval should identify who approved what and under which evidence. A vague acknowledgment is not authorization. In this case: Bind approval to the specific action and make it single-use.
- **D:** Correct. Human-in-the-loop review is appropriate when impact or uncertainty is high. Approval must occur before the effect and with enough context to decide. In this case: Bind approval to the specific action and make it single-use.

### Question 74 — D

Answer: Enforce a policy check before a consequential action. Technical controls on tools, egress, and authorization. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. Local study-map skill 5.5 (Guardrails and Human-in-the-Loop), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Technical controls on tools, egress, and authorization.
- **B:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Technical controls on tools, egress, and authorization.
- **C:** Incorrect for this question. Model Armor can help detect prompt injection, unsafe content, and sensitive data patterns. It is a layered control, not a complete trust boundary. In this case: Technical controls on tools, egress, and authorization.
- **D:** Correct. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. In this case: Technical controls on tools, egress, and authorization.

### Question 75 — A

Answer: Gate the action on explicit, attributable approval. A named accountable role and escalation path. Approval should identify who approved what and under which evidence. A vague acknowledgment is not authorization. Local study-map skill 5.5 (Guardrails and Human-in-the-Loop), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Correct. Approval should identify who approved what and under which evidence. A vague acknowledgment is not authorization. In this case: A named accountable role and escalation path.
- **B:** Incorrect for this question. Impact review assigns responsibility for consequential outcomes. It should be timely and informed by evidence. In this case: A named accountable role and escalation path.
- **C:** Incorrect for this question. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: A named accountable role and escalation path.
- **D:** Incorrect for this question. Human-in-the-loop review is appropriate when impact or uncertainty is high. Approval must occur before the effect and with enough context to decide. In this case: A named accountable role and escalation path.

### Question 76 — A

Answer: Enforce a policy check before a consequential action. Reassess risk and approval thresholds for the new autonomy level. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. Local study-map skill 5.5 (Guardrails and Human-in-the-Loop), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Correct. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. In this case: Reassess risk and approval thresholds for the new autonomy level.
- **B:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Reassess risk and approval thresholds for the new autonomy level.
- **C:** Incorrect for this question. A canary or phased rollout limits exposure while evidence accumulates. Rollback must be practical, not theoretical. In this case: Reassess risk and approval thresholds for the new autonomy level.
- **D:** Incorrect for this question. Human-in-the-loop review is appropriate when impact or uncertainty is high. Approval must occur before the effect and with enough context to decide. In this case: Reassess risk and approval thresholds for the new autonomy level.

### Question 77 — C

Answer: Review high-impact actions with accountable owners. Approval authority was not verified against the action. Impact review assigns responsibility for consequential outcomes. It should be timely and informed by evidence. Local study-map skill 5.5 (Guardrails and Human-in-the-Loop), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Approval authority was not verified against the action.
- **B:** Incorrect for this question. Human-in-the-loop review is appropriate when impact or uncertainty is high. Approval must occur before the effect and with enough context to decide. In this case: Approval authority was not verified against the action.
- **C:** Correct. Impact review assigns responsibility for consequential outcomes. It should be timely and informed by evidence. In this case: Approval authority was not verified against the action.
- **D:** Incorrect for this question. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. In this case: Approval authority was not verified against the action.

### Question 78 — D

Answer: Enforce a policy check before a consequential action. Tune the policy with evidence and provide an approved exception path. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. Local study-map skill 5.5 (Guardrails and Human-in-the-Loop), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Classification and de-identification reduce unnecessary exposure. De-identification must be validated for the specific data and purpose. In this case: Tune the policy with evidence and provide an approved exception path.
- **B:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Tune the policy with evidence and provide an approved exception path.
- **C:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Tune the policy with evidence and provide an approved exception path.
- **D:** Correct. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. In this case: Tune the policy with evidence and provide an approved exception path.

### Question 79 — D

Answer: Require human approval before a consequential action. Model confidence is not authorization or evidence of correctness. Human-in-the-loop review is appropriate when impact or uncertainty is high. Approval must occur before the effect and with enough context to decide. Local study-map skill 5.5 (Guardrails and Human-in-the-Loop), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Autoraters can score nuanced qualities at scale. They require calibration against human judgments and periodic review. In this case: Model confidence is not authorization or evidence of correctness.
- **B:** Incorrect for this question. Approval should identify who approved what and under which evidence. A vague acknowledgment is not authorization. In this case: Model confidence is not authorization or evidence of correctness.
- **C:** Incorrect for this question. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. In this case: Model confidence is not authorization or evidence of correctness.
- **D:** Correct. Human-in-the-loop review is appropriate when impact or uncertainty is high. Approval must occur before the effect and with enough context to decide. In this case: Model confidence is not authorization or evidence of correctness.

### Question 80 — C

Answer: Enforce a policy check before a consequential action. Audit logging of the trigger, decision, and outcome. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. Local study-map skill 5.5 (Guardrails and Human-in-the-Loop), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Audit logging of the trigger, decision, and outcome.
- **B:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Audit logging of the trigger, decision, and outcome.
- **C:** Correct. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. In this case: Audit logging of the trigger, decision, and outcome.
- **D:** Incorrect for this question. Impact review assigns responsibility for consequential outcomes. It should be timely and informed by evidence. In this case: Audit logging of the trigger, decision, and outcome.

### Question 81 — B

Answer: Require human approval before a consequential action. Approval must be authenticated, attributable, and bound to the specific action being approved. Human-in-the-loop review is appropriate when impact or uncertainty is high. Approval must occur before the effect and with enough context to decide. Local study-map skill 5.5 (Guardrails and Human-in-the-Loop), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Short-lived, scoped tokens limit what a tool call can do. Token handling and refresh must avoid broad standing access. In this case: Approval must be authenticated, attributable, and bound to the specific action being approved.
- **B:** Correct. Human-in-the-loop review is appropriate when impact or uncertainty is high. Approval must occur before the effect and with enough context to decide. In this case: Approval must be authenticated, attributable, and bound to the specific action being approved.
- **C:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Approval must be authenticated, attributable, and bound to the specific action being approved.
- **D:** Incorrect for this question. Approval should identify who approved what and under which evidence. A vague acknowledgment is not authorization. In this case: Approval must be authenticated, attributable, and bound to the specific action being approved.

### Question 82 — A

Answer: Enforce a policy check before a consequential action. Whether each control is proportionate and adds real safety. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. Local study-map skill 5.5 (Guardrails and Human-in-the-Loop), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Correct. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. In this case: Whether each control is proportionate and adds real safety.
- **B:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Whether each control is proportionate and adds real safety.
- **C:** Incorrect for this question. Impact review assigns responsibility for consequential outcomes. It should be timely and informed by evidence. In this case: Whether each control is proportionate and adds real safety.
- **D:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Whether each control is proportionate and adds real safety.

### Question 83 — A

Answer: Gate the action on explicit, attributable approval. Draft internally, require approval, then send through a controlled tool. Approval should identify who approved what and under which evidence. A vague acknowledgment is not authorization. Local study-map skill 5.5 (Guardrails and Human-in-the-Loop), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Correct. Approval should identify who approved what and under which evidence. A vague acknowledgment is not authorization. In this case: Draft internally, require approval, then send through a controlled tool.
- **B:** Incorrect for this question. Human-in-the-loop review is appropriate when impact or uncertainty is high. Approval must occur before the effect and with enough context to decide. In this case: Draft internally, require approval, then send through a controlled tool.
- **C:** Incorrect for this question. Model Armor can help detect prompt injection, unsafe content, and sensitive data patterns. It is a layered control, not a complete trust boundary. In this case: Draft internally, require approval, then send through a controlled tool.
- **D:** Incorrect for this question. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. In this case: Draft internally, require approval, then send through a controlled tool.

### Question 84 — B

Answer: Review high-impact actions with accountable owners. Tighten intent-level guardrails, tool scope, and approval criteria. Impact review assigns responsibility for consequential outcomes. It should be timely and informed by evidence. Local study-map skill 5.5 (Guardrails and Human-in-the-Loop), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. In this case: Tighten intent-level guardrails, tool scope, and approval criteria.
- **B:** Correct. Impact review assigns responsibility for consequential outcomes. It should be timely and informed by evidence. In this case: Tighten intent-level guardrails, tool scope, and approval criteria.
- **C:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Tighten intent-level guardrails, tool scope, and approval criteria.
- **D:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Tighten intent-level guardrails, tool scope, and approval criteria.

### Question 85 — A

Answer: Redact or de-identify sensitive data before model exposure. Minimize or redact the data before it reaches the model. Minimization reduces the impact of leakage and over-retention. Verify that redaction survives the whole pipeline. Local study-map skill 5.6 (Secure Data Access and Identity Propagation), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Correct. Minimization reduces the impact of leakage and over-retention. Verify that redaction survives the whole pipeline. In this case: Minimize or redact the data before it reaches the model.
- **B:** Incorrect for this question. Classification and de-identification reduce unnecessary exposure. De-identification must be validated for the specific data and purpose. In this case: Minimize or redact the data before it reaches the model.
- **C:** Incorrect for this question. Model Armor can help detect prompt injection, unsafe content, and sensitive data patterns. It is a layered control, not a complete trust boundary. In this case: Minimize or redact the data before it reaches the model.
- **D:** Incorrect for this question. Managed secret storage supports rotation and access control. A prompt instruction is not a secret-protection mechanism. In this case: Minimize or redact the data before it reaches the model.

### Question 86 — B

Answer: Treat retrieved and user-supplied content as untrusted. Retrieved content is untrusted and cannot grant authority. Embedded instructions must not gain authority over tools or data. Isolation, allowlists, and human approval reduce injection impact. Local study-map skill 5.6 (Secure Data Access and Identity Propagation), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Human-in-the-loop review is appropriate when impact or uncertainty is high. Approval must occur before the effect and with enough context to decide. In this case: Retrieved content is untrusted and cannot grant authority.
- **B:** Correct. Embedded instructions must not gain authority over tools or data. Isolation, allowlists, and human approval reduce injection impact. In this case: Retrieved content is untrusted and cannot grant authority.
- **C:** Incorrect for this question. Model Armor can help detect prompt injection, unsafe content, and sensitive data patterns. It is a layered control, not a complete trust boundary. In this case: Retrieved content is untrusted and cannot grant authority.
- **D:** Incorrect for this question. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. In this case: Retrieved content is untrusted and cannot grant authority.

### Question 87 — D

Answer: Apply purpose limitation and consent to personal data. Purpose limitation, consent, and defined retention. Data use should match the disclosed purpose and applicable policy. Technical access does not create permission. Local study-map skill 5.6 (Secure Data Access and Identity Propagation), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Purpose limitation, consent, and defined retention.
- **B:** Incorrect for this question. Minimization reduces the impact of leakage and over-retention. Verify that redaction survives the whole pipeline. In this case: Purpose limitation, consent, and defined retention.
- **C:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Purpose limitation, consent, and defined retention.
- **D:** Correct. Data use should match the disclosed purpose and applicable policy. Technical access does not create permission. In this case: Purpose limitation, consent, and defined retention.

### Question 88 — B

Answer: Store secrets in Secret Manager rather than prompts or code. Remove it, rotate the key, and use managed secret storage. Managed secret storage supports rotation and access control. A prompt instruction is not a secret-protection mechanism. Local study-map skill 5.6 (Secure Data Access and Identity Propagation), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Short lifetimes and audience limits reduce misuse. Tokens should not be placed in prompts or logs. In this case: Remove it, rotate the key, and use managed secret storage.
- **B:** Correct. Managed secret storage supports rotation and access control. A prompt instruction is not a secret-protection mechanism. In this case: Remove it, rotate the key, and use managed secret storage.
- **C:** Incorrect for this question. Minimization reduces the impact of leakage and over-retention. Verify that redaction survives the whole pipeline. In this case: Remove it, rotate the key, and use managed secret storage.
- **D:** Incorrect for this question. CMEK supports key-control and compliance requirements. Key lifecycle and break-glass procedures need operational ownership. In this case: Remove it, rotate the key, and use managed secret storage.

### Question 89 — A

Answer: Restrict outbound network access to approved destinations. Whether the destination and data are approved, with egress and redaction controls. Egress controls reduce exfiltration and unauthorized tool reach. They should be paired with identity and data controls. Local study-map skill 5.6 (Secure Data Access and Identity Propagation), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Correct. Egress controls reduce exfiltration and unauthorized tool reach. They should be paired with identity and data controls. In this case: Whether the destination and data are approved, with egress and redaction controls.
- **B:** Incorrect for this question. Minimization reduces the impact of leakage and over-retention. Verify that redaction survives the whole pipeline. In this case: Whether the destination and data are approved, with egress and redaction controls.
- **C:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Whether the destination and data are approved, with egress and redaction controls.
- **D:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Whether the destination and data are approved, with egress and redaction controls.

### Question 90 — D

Answer: Use customer-managed encryption keys where required. CMEK with documented key lifecycle and access separation. CMEK supports key-control and compliance requirements. Key lifecycle and break-glass procedures need operational ownership. Local study-map skill 5.6 (Secure Data Access and Identity Propagation), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. A PAB limits what an identity can reach even if other permissions exist. It should be tested against the agent's real tool paths. In this case: CMEK with documented key lifecycle and access separation.
- **B:** Incorrect for this question. Classification and de-identification reduce unnecessary exposure. De-identification must be validated for the specific data and purpose. In this case: CMEK with documented key lifecycle and access separation.
- **C:** Incorrect for this question. A service perimeter can reduce exfiltration paths for supported services. It complements, rather than replaces, IAM and application checks. In this case: CMEK with documented key lifecycle and access separation.
- **D:** Correct. CMEK supports key-control and compliance requirements. Key lifecycle and break-glass procedures need operational ownership. In this case: CMEK with documented key lifecycle and access separation.

### Question 91 — A

Answer: Redact or de-identify sensitive data before model exposure. Rare combinations of indirect identifiers can still reidentify people after names are removed. Minimization reduces the impact of leakage and over-retention. Verify that redaction survives the whole pipeline. Local study-map skill 5.6 (Secure Data Access and Identity Propagation), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Correct. Minimization reduces the impact of leakage and over-retention. Verify that redaction survives the whole pipeline. In this case: Rare combinations of indirect identifiers can still reidentify people after names are removed.
- **B:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Rare combinations of indirect identifiers can still reidentify people after names are removed.
- **C:** Incorrect for this question. Data use should match the disclosed purpose and applicable policy. Technical access does not create permission. In this case: Rare combinations of indirect identifiers can still reidentify people after names are removed.
- **D:** Incorrect for this question. Classification and de-identification reduce unnecessary exposure. De-identification must be validated for the specific data and purpose. In this case: Rare combinations of indirect identifiers can still reidentify people after names are removed.

### Question 92 — D

Answer: Treat retrieved and user-supplied content as untrusted. Tool authorization and approval requirements outside the document text. Embedded instructions must not gain authority over tools or data. Isolation, allowlists, and human approval reduce injection impact. Local study-map skill 5.6 (Secure Data Access and Identity Propagation), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. In this case: Tool authorization and approval requirements outside the document text.
- **B:** Incorrect for this question. Human-in-the-loop review is appropriate when impact or uncertainty is high. Approval must occur before the effect and with enough context to decide. In this case: Tool authorization and approval requirements outside the document text.
- **C:** Incorrect for this question. Tools let the agent act through defined interfaces. Each tool should validate inputs and enforce authorization server-side. In this case: Tool authorization and approval requirements outside the document text.
- **D:** Correct. Embedded instructions must not gain authority over tools or data. Isolation, allowlists, and human approval reduce injection impact. In this case: Tool authorization and approval requirements outside the document text.

### Question 93 — C

Answer: Apply purpose limitation and consent to personal data. Deletion across memory, session, and derived stores under policy. Data use should match the disclosed purpose and applicable policy. Technical access does not create permission. Local study-map skill 5.6 (Secure Data Access and Identity Propagation), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Minimization reduces the impact of leakage and over-retention. Verify that redaction survives the whole pipeline. In this case: Deletion across memory, session, and derived stores under policy.
- **B:** Incorrect for this question. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: Deletion across memory, session, and derived stores under policy.
- **C:** Correct. Data use should match the disclosed purpose and applicable policy. Technical access does not create permission. In this case: Deletion across memory, session, and derived stores under policy.
- **D:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Deletion across memory, session, and derived stores under policy.

### Question 94 — C

Answer: Restrict outbound network access to approved destinations. Egress restrictions plus destination authorization prevent data leaving through an unapproved path. Egress controls reduce exfiltration and unauthorized tool reach. They should be paired with identity and data controls. Local study-map skill 5.6 (Secure Data Access and Identity Propagation), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Minimization reduces the impact of leakage and over-retention. Verify that redaction survives the whole pipeline. In this case: Egress restrictions plus destination authorization prevent data leaving through an unapproved path.
- **B:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Egress restrictions plus destination authorization prevent data leaving through an unapproved path.
- **C:** Correct. Egress controls reduce exfiltration and unauthorized tool reach. They should be paired with identity and data controls. In this case: Egress restrictions plus destination authorization prevent data leaving through an unapproved path.
- **D:** Incorrect for this question. Managed secret storage supports rotation and access control. A prompt instruction is not a secret-protection mechanism. In this case: Egress restrictions plus destination authorization prevent data leaving through an unapproved path.

### Question 95 — B

Answer: Inspect and de-identify sensitive data with Sensitive Data Protection. Output inspection and redaction before delivery. Classification and de-identification reduce unnecessary exposure. De-identification must be validated for the specific data and purpose. Local study-map skill 5.6 (Secure Data Access and Identity Propagation), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. CMEK supports key-control and compliance requirements. Key lifecycle and break-glass procedures need operational ownership. In this case: Output inspection and redaction before delivery.
- **B:** Correct. Classification and de-identification reduce unnecessary exposure. De-identification must be validated for the specific data and purpose. In this case: Output inspection and redaction before delivery.
- **C:** Incorrect for this question. Minimization reduces the impact of leakage and over-retention. Verify that redaction survives the whole pipeline. In this case: Output inspection and redaction before delivery.
- **D:** Incorrect for this question. Model Armor can help detect prompt injection, unsafe content, and sensitive data patterns. It is a layered control, not a complete trust boundary. In this case: Output inspection and redaction before delivery.

### Question 96 — A

Answer: Treat retrieved and user-supplied content as untrusted. Policy remains in force; escalate through the approved exception path. Embedded instructions must not gain authority over tools or data. Isolation, allowlists, and human approval reduce injection impact. Local study-map skill 5.6 (Secure Data Access and Identity Propagation), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Correct. Embedded instructions must not gain authority over tools or data. Isolation, allowlists, and human approval reduce injection impact. In this case: Policy remains in force; escalate through the approved exception path.
- **B:** Incorrect for this question. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. In this case: Policy remains in force; escalate through the approved exception path.
- **C:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Policy remains in force; escalate through the approved exception path.
- **D:** Incorrect for this question. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. In this case: Policy remains in force; escalate through the approved exception path.

### Question 97 — B

Answer: Apply purpose limitation and consent to personal data. Documented minimization decisions and non-sensitive evidence. Data use should match the disclosed purpose and applicable policy. Technical access does not create permission. Local study-map skill 5.6 (Secure Data Access and Identity Propagation), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Classification and de-identification reduce unnecessary exposure. De-identification must be validated for the specific data and purpose. In this case: Documented minimization decisions and non-sensitive evidence.
- **B:** Correct. Data use should match the disclosed purpose and applicable policy. Technical access does not create permission. In this case: Documented minimization decisions and non-sensitive evidence.
- **C:** Incorrect for this question. Minimization reduces the impact of leakage and over-retention. Verify that redaction survives the whole pipeline. In this case: Documented minimization decisions and non-sensitive evidence.
- **D:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Documented minimization decisions and non-sensitive evidence.

### Question 98 — A

Answer: Store secrets in Secret Manager rather than prompts or code. Ownership, rotation cadence, and emergency revocation procedures. Managed secret storage supports rotation and access control. A prompt instruction is not a secret-protection mechanism. Local study-map skill 5.6 (Secure Data Access and Identity Propagation), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Correct. Managed secret storage supports rotation and access control. A prompt instruction is not a secret-protection mechanism. In this case: Ownership, rotation cadence, and emergency revocation procedures.
- **B:** Incorrect for this question. Short lifetimes and audience limits reduce misuse. Tokens should not be placed in prompts or logs. In this case: Ownership, rotation cadence, and emergency revocation procedures.
- **C:** Incorrect for this question. Short-lived, scoped tokens limit what a tool call can do. Token handling and refresh must avoid broad standing access. In this case: Ownership, rotation cadence, and emergency revocation procedures.
- **D:** Incorrect for this question. CMEK supports key-control and compliance requirements. Key lifecycle and break-glass procedures need operational ownership. In this case: Ownership, rotation cadence, and emergency revocation procedures.

### Question 99 — A

Answer: Redact or de-identify sensitive data before model exposure. Remove unnecessary sensitive content before model processing. Minimization reduces the impact of leakage and over-retention. Verify that redaction survives the whole pipeline. Local study-map skill 5.6 (Secure Data Access and Identity Propagation), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Correct. Minimization reduces the impact of leakage and over-retention. Verify that redaction survives the whole pipeline. In this case: Remove unnecessary sensitive content before model processing.
- **B:** Incorrect for this question. Model Armor can help detect prompt injection, unsafe content, and sensitive data patterns. It is a layered control, not a complete trust boundary. In this case: Remove unnecessary sensitive content before model processing.
- **C:** Incorrect for this question. Data use should match the disclosed purpose and applicable policy. Technical access does not create permission. In this case: Remove unnecessary sensitive content before model processing.
- **D:** Incorrect for this question. Classification and de-identification reduce unnecessary exposure. De-identification must be validated for the specific data and purpose. In this case: Remove unnecessary sensitive content before model processing.

### Question 100 — C

Answer: Treat retrieved and user-supplied content as untrusted. The source, detection, action taken, and affected workflow. Embedded instructions must not gain authority over tools or data. Isolation, allowlists, and human approval reduce injection impact. Local study-map skill 5.6 (Secure Data Access and Identity Propagation), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Google Cloud security documentation: https://cloud.google.com/security-command-center/docs/model-armor-overview

- **A:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: The source, detection, action taken, and affected workflow.
- **B:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: The source, detection, action taken, and affected workflow.
- **C:** Correct. Embedded instructions must not gain authority over tools or data. Isolation, allowlists, and human approval reduce injection impact. In this case: The source, detection, action taken, and affected workflow.
- **D:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: The source, detection, action taken, and affected workflow.
