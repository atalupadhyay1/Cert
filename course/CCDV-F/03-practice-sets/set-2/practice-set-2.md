# Claude Certified Developer – Foundations (CCDV-F) — Practice Set 2

Agents, Workflows, Tools and MCPs

100 questions · Suggested practice duration: 200 minutes · Practice target: 80%

Tests 1–5 are focused learning tests. Test 6 is an expanded blueprint-proportioned review, not an official exam replica. Related concepts recur.

Select ONE best answer for every question. Answer key follows all questions.

Original educational content, not actual, recalled, or copied Anthropic exam items.

## Questions

### 1. A document workflow always validates, transforms, then publishes approved records. Which architecture fits predictable dependencies?

Domain: Agents and Workflows

- A. Route coordination through an orchestrator
- B. Select specialists according to the actual task
- C. Map the problem and revise subtasks as evidence emerges
- D. Use a predictable sequence of specialized stages

### 2. A diagnostic assistant must decide each investigation step from the previous observation. Which architecture fits?

Domain: Agents and Workflows

- A. Wait for validated prerequisite outputs
- B. Map the problem and revise subtasks as evidence emerges
- C. Run independent branches concurrently and join checked results
- D. Use a predictable sequence of specialized stages

### 3. A supervisor invokes all available specialists for even trivial requests. What routing principle should change?

Domain: Agents and Workflows

- A. Assign distinct scopes and explicit coverage responsibilities
- B. Select specialists according to the actual task
- C. Use a predictable sequence of specialized stages
- D. Route coordination through an orchestrator

### 4. Several workers repeatedly inspect the same source while missing required categories. What assignment design helps?

Domain: Agents and Workflows

- A. Run independent branches concurrently and join checked results
- B. Assign distinct scopes and explicit coverage responsibilities
- C. Route coordination through an orchestrator
- D. Evaluate coverage and delegate targeted follow-up work

### 5. A team needs centralized delegation, result aggregation, and recovery decisions across workers. What topology fits?

Domain: Agents and Workflows

- A. Use a predictable sequence of specialized stages
- B. Route coordination through an orchestrator
- C. Fork an independent branch from a valid shared baseline
- D. Run independent branches concurrently and join checked results

### 6. Two independent read-only checks can run within available capacity. What scheduling may reduce task duration?

Domain: Agents and Workflows

- A. Resume the identified session when its context remains valid
- B. Wait for validated prerequisite outputs
- C. Run independent branches concurrently and join checked results
- D. Use a predictable sequence of specialized stages

### 7. A downstream action needs a verified output that does not yet exist. How should dependencies be scheduled?

Domain: Agents and Workflows

- A. Select specialists according to the actual task
- B. Run independent branches concurrently and join checked results
- C. Fork an independent branch from a valid shared baseline
- D. Wait for validated prerequisite outputs

### 8. Every worker returns, but the requested comparison is unsupported. What should the supervisor assess?

Domain: Agents and Workflows

- A. Evaluate coverage and delegate targeted follow-up work
- B. Enforce task, iteration, and spending safeguards
- C. Assign distinct scopes and explicit coverage responsibilities
- D. Use a predictable sequence of specialized stages

### 9. A team chooses an autonomous agent for a task with a simple stable transformation. What should guide architecture selection?

Domain: Agents and Workflows

- A. Select the least costly configuration that meets required outcomes
- B. Choose a framework for needed orchestration semantics
- C. Translate business goals into measurable functional and operational requirements
- D. Compare hosting responsibility, control, and service constraints

### 10. A specialist lacks a critical constraint discussed only with its parent. What should delegation include?

Domain: Agents and Workflows

- A. Configure the subagent description, prompt, and tool scope
- B. Pass relevant evidence and constraints explicitly
- C. Route coordination through an orchestrator
- D. Enable the version-appropriate subagent invocation tool

### 11. Two subagents have identical selection descriptions despite different expertise. What configuration should improve?

Domain: Agents and Workflows

- A. Pass relevant evidence and constraints explicitly
- B. Enable the version-appropriate subagent invocation tool
- C. Configure the subagent description, prompt, and tool scope
- D. Give each specialist only task-relevant tools

### 12. An agent keeps calling valid tools without making progress. What bounds the overall workflow?

Domain: Agents and Workflows

- A. Inspect stop_reason and dispatch the appropriate branch
- B. Handle the output limit as an incomplete response
- C. Enforce task, iteration, and spending safeguards
- D. Treat end_turn as the end of the current assistant turn

### 13. A workflow must transfer unresolved work to someone without transcript access. What artifact supports continuity?

Domain: Agents and Workflows

- A. Pass relevant evidence and constraints explicitly
- B. Create a structured handoff with facts, status, and next actions
- C. Persist concise codebase findings with file and symbol pointers
- D. Persist structured task state and pending actions

### 14. A business prerequisite must hold despite occasional instruction noncompliance. What should enforce it?

Domain: Agents and Workflows

- A. Enforce prerequisites in trusted execution code
- B. Use representative few-shot examples with boundaries
- C. Configure the subagent description, prompt, and tool scope
- D. State explicit reportable and non-reportable criteria

### 15. An agent must survive process restart with pending external actions. What durable capability is needed?

Domain: Agents and Workflows

- A. Persist structured task state and pending actions
- B. Resume the identified session when its context remains valid
- C. Treat end_turn as the end of the current assistant turn
- D. Pass relevant evidence and constraints explicitly

### 16. Local workers validate components separately but miss incompatible interfaces between them. What review is missing?

Domain: Agents and Workflows

- A. Run independent branches concurrently and join checked results
- B. Configure the subagent description, prompt, and tool scope
- C. Assign distinct scopes and explicit coverage responsibilities
- D. Add a cross-file or cross-component integration pass

### 17. A simple factual lookup does not need a report-writing agent. Which orchestration strategy avoids unnecessary cost?

Domain: Agents and Workflows

- A. Route coordination through an orchestrator
- B. Select specialists according to the actual task
- C. Assign distinct scopes and explicit coverage responsibilities
- D. Use a predictable sequence of specialized stages

### 18. Two alternative designs should branch from the same verified analysis without sharing later conversation changes. What pattern fits?

Domain: Agents and Workflows

- A. Persist structured task state and pending actions
- B. Resume the identified session when its context remains valid
- C. Fork an independent branch from a valid shared baseline
- D. Start a fresh session with a checked structured summary

### 19. A legacy investigation reveals new dependencies at each stage. What planning approach should respond to discoveries?

Domain: Agents and Workflows

- A. Wait for validated prerequisite outputs
- B. Run independent branches concurrently and join checked results
- C. Use a predictable sequence of specialized stages
- D. Map the problem and revise subtasks as evidence emerges

### 20. A completed-looking draft omits a required evidence source. What should happen before acceptance?

Domain: Agents and Workflows

- A. Assign distinct scopes and explicit coverage responsibilities
- B. Evaluate coverage and delegate targeted follow-up work
- C. Enforce task, iteration, and spending safeguards
- D. Treat end_turn as the end of the current assistant turn

### 21. A custom harness stops whenever assistant text appears, skipping a requested tool. What should control dispatch?

Domain: Agents and Workflows

- A. Handle the output limit as an incomplete response
- B. Enforce task, iteration, and spending safeguards
- C. Treat end_turn as the end of the current assistant turn
- D. Inspect stop_reason and dispatch the appropriate branch

### 22. A tool returns accurate data, but the next model call never includes it. What must the harness provide?

Domain: Agents and Workflows

- A. Dispatch response content according to each block type
- B. Append the assistant tool-use blocks and matching tool results
- C. Use the final assembled message and completion status
- D. Persist structured task state and pending actions

### 23. A destructive operation must be rejected before it runs. Which interception stage fits?

Domain: Agents and Workflows

- A. State explicit reportable and non-reportable criteria
- B. Record detected_pattern and dismissal reasons
- C. Use pre-execution tool interception for blocking policy checks
- D. Normalize tool observations before model consumption

### 24. Connected tools return equivalent dates in inconsistent formats. What processing can help model interpretation?

Domain: Agents and Workflows

- A. Require authorized approval before the consequential action
- B. Enforce prerequisites in trusted execution code
- C. Normalize tool observations before model consumption
- D. Use pre-execution tool interception for blocking policy checks

### 25. A team compares self-hosted and provider-managed agent deployment. What decision should it evaluate?

Domain: Agents and Workflows

- A. Compare hosting responsibility, control, and service constraints
- B. Separate environment configuration from application logic
- C. Choose a framework for needed orchestration semantics
- D. Use a provider-specific adapter behind a stable application interface

### 26. Configured specialists never run because the harness omits its installed SDK's invocation mechanism. What should be checked?

Domain: Agents and Workflows

- A. Give each specialist only task-relevant tools
- B. Configure the subagent description, prompt, and tool scope
- C. Pass relevant evidence and constraints explicitly
- D. Enable the version-appropriate subagent invocation tool

### 27. A model proposes an action outside the user's permissions. What should remain authoritative?

Domain: Agents and Workflows

- A. Enforce prerequisites in trusted execution code
- B. State explicit reportable and non-reportable criteria
- C. Require authorized approval before the consequential action
- D. Use representative few-shot examples with boundaries

### 28. A tool continuation fails after the client rewrites protocol-protected content. What should the harness respect?

Domain: Agents and Workflows

- A. Append the assistant tool-use blocks and matching tool results
- B. Dispatch response content according to each block type
- C. Supply the relevant conversation state on subsequent requests
- D. Preserve protocol-required blocks through tool continuations

### 29. A network retry may repeat an already committed write. What integration behavior reduces duplicate effects?

Domain: Agents and Workflows

- A. Use a durable idempotency key for the same logical action
- B. Enforce task, iteration, and spending safeguards
- C. Persist structured task state and pending actions
- D. Resume the identified session when its context remains valid

### 30. A tool may never respond, blocking the custom agent indefinitely. What control is needed?

Domain: Agents and Workflows

- A. Set explicit deadlines and classify timeout outcomes
- B. Retry a transient failure with bounded backoff
- C. Cancel local work and reconcile any external operation separately
- D. Coordinate retries across SDK and application layers

### 31. A specialist should inspect code but never modify files. What should its construction specify?

Domain: Agents and Workflows

- A. Enable the version-appropriate subagent invocation tool
- B. Assign distinct scopes and explicit coverage responsibilities
- C. Pass relevant evidence and constraints explicitly
- D. Configure the subagent description, prompt, and tool scope

### 32. An agent may prepare a transaction, but a qualified person must approve commitment. What gate fits?

Domain: Agents and Workflows

- A. Create a structured handoff with facts, status, and next actions
- B. Persist structured task state and pending actions
- C. Require authorized approval before the consequential action
- D. Enforce prerequisites in trusted execution code

### 33. A long-running agent should resume consistently after interruption. Where should recovery information be recorded?

Domain: Agents and Workflows

- A. Checkpoint durable state at safe workflow boundaries
- B. Resume the identified session when its context remains valid
- C. Resume from a checked manifest of worker states and artifacts
- D. Persist structured task state and pending actions

### 34. The client cancels a request after a tool may have modified a remote record. What should be handled separately?

Domain: Agents and Workflows

- A. Set explicit deadlines and classify timeout outcomes
- B. Cancel local work and reconcile any external operation separately
- C. Validate and commit business changes through a controlled boundary
- D. Use a durable idempotency key for the same logical action

### 35. An SDK agent behaves differently from a custom loop using similar instructions. What diagnostic evidence helps compare them?

Domain: Agents and Workflows

- A. Use a versioned representative held-out evaluation set
- B. Propagate correlation identifiers across requests and tools
- C. Inspect a redacted end-to-end request and tool trace
- D. Use controlled stubs for repeatable failure-path tests

### 36. A team compares LangGraph, Strands, and PydanticAI. What should determine the choice?

Domain: Agents and Workflows

- A. Choose a framework for needed orchestration semantics
- B. Compare hosting responsibility, control, and service constraints
- C. Select the least costly configuration that meets required outcomes
- D. Use a provider-specific adapter behind a stable application interface

### 37. A graph workflow must restart after a crash without repeating committed work blindly. What capability matters?

Domain: Agents and Workflows

- A. Checkpoint durable state at safe workflow boundaries
- B. Resume the identified session when its context remains valid
- C. Persist structured task state and pending actions
- D. Supply the relevant conversation state on subsequent requests

### 38. A fresh worker receives only 'use the previous analysis' without actual findings. What pattern needs correction?

Domain: Agents and Workflows

- A. Pass relevant evidence and constraints explicitly
- B. Persist structured task state and pending actions
- C. Supply the relevant conversation state on subsequent requests
- D. Configure the subagent description, prompt, and tool scope

### 39. A framework supports parallel nodes, but two tasks have no dependencies. What scheduling pattern may help?

Domain: Agents and Workflows

- A. Use a predictable sequence of specialized stages
- B. Fork an independent branch from a valid shared baseline
- C. Wait for validated prerequisite outputs
- D. Run independent branches concurrently and join checked results

### 40. A graph starts synthesis before evidence collection finishes. Which relationship should be enforced?

Domain: Agents and Workflows

- A. Map the problem and revise subtasks as evidence emerges
- B. Select specialists according to the actual task
- C. Wait for validated prerequisite outputs
- D. Run independent branches concurrently and join checked results

### 41. A long exploratory agent starts referring to generic code patterns instead of discovered symbols. What memory aid helps?

Domain: Agents and Workflows

- A. Compact context while preserving checked facts and open issues
- B. Preserve exact transactional facts outside lossy summaries
- C. Persist concise codebase findings with file and symbol pointers
- D. Supply the relevant conversation state on subsequent requests

### 42. Old discovery output consumes context even though its verified conclusions can be retained concisely. What operation may help?

Domain: Agents and Workflows

- A. Preserve exact transactional facts outside lossy summaries
- B. Reduce tool output to relevant fields with provenance
- C. Compact context while preserving checked facts and open issues
- D. Present key findings early and organize supporting details

### 43. A developer assumes choosing an agent framework automatically makes tool execution safe. What selection principle is correct?

Domain: Agents and Workflows

- A. Compare hosting responsibility, control, and service constraints
- B. Choose a framework for needed orchestration semantics
- C. Enforce prerequisites in trusted execution code
- D. Layer prevention, detection, approval, and recovery controls

### 44. A multi-worker pattern is slower because every worker performs the complete original task. What decomposition change helps?

Domain: Agents and Workflows

- A. Run independent branches concurrently and join checked results
- B. Assign distinct scopes and explicit coverage responsibilities
- C. Route coordination through an orchestrator
- D. Evaluate coverage and delegate targeted follow-up work

### 45. Most stored tool observations became obsolete after major source changes. What context strategy fits?

Domain: Agents and Workflows

- A. Tell the resumed agent what changed and recheck affected evidence
- B. Resume the identified session when its context remains valid
- C. Compact context while preserving checked facts and open issues
- D. Start a fresh session with a checked structured summary

### 46. A worker fails after gathering partial evidence. What should orchestration receive?

Domain: Agents and Workflows

- A. Represent a successful query with no matches explicitly
- B. Annotate evidence coverage and unavailable sources
- C. Return a structured tool error with category and retryability
- D. Return structured failure context and partial results

### 47. Two agents repeatedly delegate the same unresolved task to each other. What system-level safeguard is needed?

Domain: Agents and Workflows

- A. Enforce task, iteration, and spending safeguards
- B. Inspect stop_reason and dispatch the appropriate branch
- C. Treat end_turn as the end of the current assistant turn
- D. Checkpoint durable state at safe workflow boundaries

### 48. A stateful framework can route based on intermediate results. Which strategy uses that flexibility appropriately?

Domain: Agents and Workflows

- A. Route coordination through an orchestrator
- B. Select specialists according to the actual task
- C. Use a predictable sequence of specialized stages
- D. Assign distinct scopes and explicit coverage responsibilities

### 49. Persistent behavior is implemented by loading saved task facts into each request. What does this represent?

Domain: Agents and Workflows

- A. Persist structured task state and pending actions
- B. Resume the identified session when its context remains valid
- C. Supply the relevant conversation state on subsequent requests
- D. Pass relevant evidence and constraints explicitly

### 50. A supervisor must determine whether combined worker outputs answer the actual request. What evaluation should occur?

Domain: Agents and Workflows

- A. Assign distinct scopes and explicit coverage responsibilities
- B. Use a predictable sequence of specialized stages
- C. Evaluate coverage and delegate targeted follow-up work
- D. Route coordination through an orchestrator

### 51. Two necessary tools have overlapping vague descriptions and are chosen inconsistently. What interface improvement is most direct?

Domain: Tools and MCPs

- A. Define and validate a precise input schema
- B. Expose a supported MCP resource catalog
- C. Give each specialist only task-relevant tools
- D. Clarify tool purpose, inputs, outputs, and boundaries

### 52. A tool expects a typed record identifier but receives unrelated free-form text. What should define and validate the input?

Domain: Tools and MCPs

- A. Give each specialist only task-relevant tools
- B. Define and validate a precise input schema
- C. Clarify tool purpose, inputs, outputs, and boundaries
- D. Expose a supported MCP resource catalog

### 53. A failed operation returns an empty list that looks like a successful search. What should replace that response?

Domain: Tools and MCPs

- A. Append the assistant tool-use blocks and matching tool results
- B. Return a structured tool error with category and retryability
- C. Represent a successful query with no matches explicitly
- D. Clarify tool purpose, inputs, outputs, and boundaries

### 54. A tool rejects an invalid date format while the service is healthy. What recovery fits?

Domain: Tools and MCPs

- A. Stop the unauthorized operation and use an approved access path
- B. Retry a transient failure with bounded backoff
- C. Correct invalid arguments before retrying
- D. Explain the non-retryable business-rule outcome

### 55. A resource denies access to the current identity. What handling should apply?

Domain: Tools and MCPs

- A. Correct invalid arguments before retrying
- B. Retry a transient failure with bounded backoff
- C. Stop the unauthorized operation and use an approved access path
- D. Represent a successful query with no matches explicitly

### 56. A tool reports temporary overload with a permitted retry interval. What recovery is suitable?

Domain: Tools and MCPs

- A. Explain the non-retryable business-rule outcome
- B. Correct invalid arguments before retrying
- C. Stop the unauthorized operation and use an approved access path
- D. Retry a transient failure with bounded backoff

### 57. A valid request fails a documented eligibility rule. What outcome should the tool communicate?

Domain: Tools and MCPs

- A. Explain the non-retryable business-rule outcome
- B. Correct invalid arguments before retrying
- C. Retry a transient failure with bounded backoff
- D. Represent a successful query with no matches explicitly

### 58. An authorized search completes normally with zero results. How should it be represented?

Domain: Tools and MCPs

- A. Represent a successful query with no matches explicitly
- B. Stop the unauthorized operation and use an approved access path
- C. Retry a transient failure with bounded backoff
- D. Return a structured tool error with category and retryability

### 59. A narrow specialist receives dozens of unrelated action tools. What configuration should improve?

Domain: Tools and MCPs

- A. Expose a supported MCP resource catalog
- B. Give each specialist only task-relevant tools
- C. Check connected-server discovery and effective availability
- D. Clarify tool purpose, inputs, outputs, and boundaries

### 60. A document loader should only access approved sources. What interface design supports this?

Domain: Tools and MCPs

- A. Give each specialist only task-relevant tools
- B. Expose a constrained domain-specific operation
- C. Define and validate a precise input schema
- D. Clarify tool purpose, inputs, outputs, and boundaries

### 61. One named schema tool must be selected for this turn. Which selection control fits?

Domain: Tools and MCPs

- A. Use tool_choice with type auto
- B. Give each specialist only task-relevant tools
- C. Use tool_choice with type any
- D. Force the required named tool for that turn

### 62. A request must use one of several extraction tools but the model should choose which. What mode fits?

Domain: Tools and MCPs

- A. Use tool_choice with type auto
- B. Use tool_choice with type any
- C. Give each specialist only task-relevant tools
- D. Force the required named tool for that turn

### 63. A simple explanatory request may not need an external operation. What tool-choice setting permits direct text?

Domain: Tools and MCPs

- A. Use tool_choice with type any
- B. Force the required named tool for that turn
- C. Use tool_choice with type auto
- D. Give each specialist only task-relevant tools

### 64. A forced tool call has disallowed business arguments. What should determine execution permission?

Domain: Tools and MCPs

- A. Clarify tool purpose, inputs, outputs, and boundaries
- B. Use tool_choice with type any
- C. Force the required named tool for that turn
- D. Enforce prerequisites in trusted execution code

### 65. One application needs a small private lookup function with no separate shared protocol service. What implementation may suffice?

Domain: Tools and MCPs

- A. Implement a protocol-compatible server for approved capabilities
- B. Use an existing built-in tool when its scope fits
- C. Implement an application-local tool for a specific integration
- D. Put an on-demand workflow in a project skill

### 66. Claude requests a client-side tool. Who must execute it and return the observation in a custom harness?

Domain: Tools and MCPs

- A. Append the assistant tool-use blocks and matching tool results
- B. Clarify tool purpose, inputs, outputs, and boundaries
- C. Return a structured tool error with category and retryability
- D. Define and validate a precise input schema

### 67. A provider offers a server-executed tool unavailable through another host. What integration concern matters?

Domain: Tools and MCPs

- A. Use a provider-specific adapter behind a stable application interface
- B. Use an existing built-in tool when its scope fits
- C. Have an MCP client connect to the server and invoke permitted capabilities
- D. Implement an application-local tool for a specific integration

### 68. A specialist can resolve a transient failure within its own recovery budget. What strategy reduces coordinator noise?

Domain: Tools and MCPs

- A. Recover transiently within the worker, then report unresolved failure
- B. Return a structured tool error with category and retryability
- C. Represent a successful query with no matches explicitly
- D. Return structured failure context and partial results

### 69. Good descriptions still misroute calls because a system keyword rule points to an old tool. What should be examined?

Domain: Tools and MCPs

- A. Define and validate a precise input schema
- B. Clarify tool purpose, inputs, outputs, and boundaries
- C. Give each specialist only task-relevant tools
- D. Inspect conflicting routing instructions as well as tool descriptions

### 70. A tool proposes a high-impact irreversible operation that requires human sign-off. What should precede execution?

Domain: Tools and MCPs

- A. Enforce prerequisites in trusted execution code
- B. Create a structured handoff with facts, status, and next actions
- C. Require authorized approval before the consequential action
- D. State explicit reportable and non-reportable criteria

### 71. An application needs to discover and invoke approved server capabilities over MCP. Which component performs that connection role?

Domain: Tools and MCPs

- A. Have an MCP client connect to the server and invoke permitted capabilities
- B. Expose a reusable prompt template through MCP
- C. Expose a supported MCP resource catalog
- D. Implement a protocol-compatible server for approved capabilities

### 72. A development team must author a protocol-compatible endpoint exposing approved operations and content. What component is being built?

Domain: Tools and MCPs

- A. Put an on-demand workflow in a project skill
- B. Use an existing built-in tool when its scope fits
- C. Implement an application-local tool for a specific integration
- D. Implement a protocol-compatible server for approved capabilities

### 73. An integration should expose a read-only document catalog, not execute an action. Which MCP primitive fits?

Domain: Tools and MCPs

- A. Clarify tool purpose, inputs, outputs, and boundaries
- B. Expose a reusable prompt template through MCP
- C. Implement an application-local tool for a specific integration
- D. Expose a supported MCP resource catalog

### 74. An MCP integration needs a reusable user-invoked interaction template. Which primitive fits?

Domain: Tools and MCPs

- A. Expose a reusable prompt template through MCP
- B. Expose a supported MCP resource catalog
- C. Implement an application-local tool for a specific integration
- D. Clarify tool purpose, inputs, outputs, and boundaries

### 75. A local subprocess MCP server writes diagnostic chatter to protocol stdout and breaks parsing. Which transport rule matters?

Domain: Tools and MCPs

- A. Use a supported network MCP transport with explicit authentication
- B. Use stdio for a suitable local subprocess MCP connection
- C. Use WebSockets for an explicitly bidirectional persistent channel
- D. Apply HTTP method, status, authentication, and payload contracts

### 76. A remotely deployed MCP server needs network access, authentication, and TLS. What transport design should be verified?

Domain: Tools and MCPs

- A. Have an MCP client connect to the server and invoke permitted capabilities
- B. Use a supported network MCP transport with explicit authentication
- C. Use stdio for a suitable local subprocess MCP connection
- D. Use WebSockets for an explicitly bidirectional persistent channel

### 77. A configured server connects unsuccessfully and none of its tools appear. What should be diagnosed?

Domain: Tools and MCPs

- A. Expose a supported MCP resource catalog
- B. Check connected-server discovery and effective availability
- C. Clarify tool purpose, inputs, outputs, and boundaries
- D. Have an MCP client connect to the server and invoke permitted capabilities

### 78. Approved server setup should be reviewed and shared with repository contributors. Which configuration scope fits?

Domain: Tools and MCPs

- A. Use user-scoped MCP configuration for personal servers
- B. Check connected-server discovery and effective availability
- C. Use project-scoped .mcp.json for shared server configuration
- D. Expose a supported MCP resource catalog

### 79. A shared server configuration needs credentials without committing a token. What authentication pattern helps?

Domain: Tools and MCPs

- A. Reference runtime environment variables instead of committing tokens
- B. Expose a supported MCP resource catalog
- C. Use project-scoped .mcp.json for shared server configuration
- D. Use user-scoped MCP configuration for personal servers

### 80. One developer wants an experimental server without changing project teammates' tools. Which scope fits?

Domain: Tools and MCPs

- A. Check connected-server discovery and effective availability
- B. Use project-scoped .mcp.json for shared server configuration
- C. Expose a supported MCP resource catalog
- D. Use user-scoped MCP configuration for personal servers

### 81. A new MCP tool accepts structured arguments. What must server implementation validate beyond discovery?

Domain: Tools and MCPs

- A. Clarify tool purpose, inputs, outputs, and boundaries
- B. Define and validate a precise input schema
- C. Return a structured tool error with category and retryability
- D. Expose a supported MCP resource catalog

### 82. A server execution error is returned as ordinary content without failure metadata. What response contract should improve?

Domain: Tools and MCPs

- A. Expose a supported MCP resource catalog
- B. Represent a successful query with no matches explicitly
- C. Clarify tool purpose, inputs, outputs, and boundaries
- D. Return a structured tool error with category and retryability

### 83. A local client launches its server as a subprocess and uses standard streams. Which transport category is this?

Domain: Tools and MCPs

- A. Use a supported network MCP transport with explicit authentication
- B. Use WebSockets for an explicitly bidirectional persistent channel
- C. Use stdio for a suitable local subprocess MCP connection
- D. Apply HTTP method, status, authentication, and payload contracts

### 84. An agent needs database schema metadata before planning an authorized query. Which MCP capability can expose that content?

Domain: Tools and MCPs

- A. Expose a supported MCP resource catalog
- B. Expose a reusable prompt template through MCP
- C. Implement an application-local tool for a specific integration
- D. Clarify tool purpose, inputs, outputs, and boundaries

### 85. A maintained integration already supports a standard service. What should precede implementing an equivalent server?

Domain: Tools and MCPs

- A. Use an existing built-in tool when its scope fits
- B. Implement an application-local tool for a specific integration
- C. Evaluate a maintained existing integration before writing a custom server
- D. Implement a protocol-compatible server for approved capabilities

### 86. A task only needs supported local filename discovery. What should be considered before creating a custom service?

Domain: Tools and MCPs

- A. Implement a protocol-compatible server for approved capabilities
- B. Put an on-demand workflow in a project skill
- C. Implement an application-local tool for a specific integration
- D. Use an existing built-in tool when its scope fits

### 87. A team needs reusable procedural guidance over existing approved tools, not a new backend operation. What extension fits?

Domain: Tools and MCPs

- A. Implement a protocol-compatible server for approved capabilities
- B. Put an on-demand workflow in a project skill
- C. Implement an application-local tool for a specific integration
- D. Expose a supported MCP resource catalog

### 88. A single app needs a new authenticated business operation in its own harness. What may be the simplest integration type?

Domain: Tools and MCPs

- A. Implement an application-local tool for a specific integration
- B. Use an existing built-in tool when its scope fits
- C. Put an on-demand workflow in a project skill
- D. Expose a reusable prompt template through MCP

### 89. Multiple independently deployed clients require a governed protocol endpoint with stable capability contracts. What implementation category fits?

Domain: Tools and MCPs

- A. Put an on-demand workflow in a project skill
- B. Use an existing built-in tool when its scope fits
- C. Expose a reusable prompt template through MCP
- D. Implement a protocol-compatible server for approved capabilities

### 90. A capability's purpose is providing a content catalog rather than performing a mutation. Which type is appropriate?

Domain: Tools and MCPs

- A. Implement an application-local tool for a specific integration
- B. Expose a reusable prompt template through MCP
- C. Expose a supported MCP resource catalog
- D. Use an existing built-in tool when its scope fits

### 91. A server should offer an explicit reusable prompt template through MCP. Which capability matches that interface?

Domain: Tools and MCPs

- A. Put an on-demand workflow in a project skill
- B. Implement an application-local tool for a specific integration
- C. Expose a reusable prompt template through MCP
- D. Expose a supported MCP resource catalog

### 92. The agent must locate a symbol inside repository contents. Which built-in operation is most direct?

Domain: Tools and MCPs

- A. Use Glob for filename or path-pattern discovery
- B. Use Bash for an authorized command with bounded execution
- C. Use Grep for content-pattern searches
- D. Use Read to inspect current file contents

### 93. The agent knows only a filename pattern and needs matching paths. Which operation fits?

Domain: Tools and MCPs

- A. Use Grep for content-pattern searches
- B. Use Edit with a verified unique anchor
- C. Use Read to inspect current file contents
- D. Use Glob for filename or path-pattern discovery

### 94. An agent must inspect a current file before deriving a safe modification. Which operation comes first?

Domain: Tools and MCPs

- A. Use Read to inspect current file contents
- B. Read the current file and write a checked replacement
- C. Use Bash for an authorized command with bounded execution
- D. Use Edit with a verified unique anchor

### 95. A single verified unique anchor identifies a small change. What targeted operation fits?

Domain: Tools and MCPs

- A. Use Bash for an authorized command with bounded execution
- B. Use Edit with a verified unique anchor
- C. Read the current file and write a checked replacement
- D. Use Read to inspect current file contents

### 96. A targeted replacement is ambiguous, but current full content can be preserved and checked. What fallback may fit?

Domain: Tools and MCPs

- A. Read the current file and write a checked replacement
- B. Use Grep for content-pattern searches
- C. Use Edit with a verified unique anchor
- D. Use Glob for filename or path-pattern discovery

### 97. An authorized step requires running the actual repository test command. What built-in category fits?

Domain: Tools and MCPs

- A. Use Read to inspect current file contents
- B. Use Bash for an authorized command with bounded execution
- C. Use Glob for filename or path-pattern discovery
- D. Use Grep for content-pattern searches

### 98. A new customization exposes operations outside the intended specialist role. What effective boundary should be corrected?

Domain: Tools and MCPs

- A. Separate genuinely different tasks into clearly bounded tools
- B. Expose a supported MCP resource catalog
- C. Give each specialist only task-relevant tools
- D. Clarify tool purpose, inputs, outputs, and boundaries

### 99. An extension bundles executable tools and should not be treated as harmless text. What engineering practice applies?

Domain: Tools and MCPs

- A. Put an on-demand workflow in a project skill
- B. Pin compatible model, SDK, prompt, and dependency versions
- C. Separate environment configuration from application logic
- D. Version and review plugin dependencies and permissions

### 100. A team chooses between built-ins, a skill, a local tool, and MCP. What should determine the choice?

Domain: Tools and MCPs

- A. Select the least costly configuration that meets required outcomes
- B. Compare hosting responsibility, control, and service constraints
- C. Choose a framework for needed orchestration semantics
- D. Translate business goals into measurable functional and operational requirements

---

## Answer key and explanations

### Question 1 — D

Answer: Use a predictable sequence of specialized stages. A fixed chain is appropriate when the required steps are known and stable. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. Local study-map skill 1.1 (Agent Architecture), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. A coordinator manages decomposition, routing, error handling, and aggregation in a hub-and-spoke design. Specialists need not communicate through uncontrolled peer channels. In this case: A fixed chain is appropriate when the required steps are known and stable.
- **B:** Incorrect for this question. Dynamic routing avoids invoking every specialist for a simple request. Selection should follow coverage needs, not a fixed ritual. In this case: A fixed chain is appropriate when the required steps are known and stable.
- **C:** Incorrect for this question. Open-ended investigation benefits from exploration, prioritized hypotheses, and revised decomposition rather than an exhaustive fixed script chosen before evidence. In this case: A fixed chain is appropriate when the required steps are known and stable.
- **D:** Correct. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: A fixed chain is appropriate when the required steps are known and stable.

### Question 2 — B

Answer: Map the problem and revise subtasks as evidence emerges. Evidence-dependent next actions require adaptive decomposition rather than a fixed exhaustive script. Open-ended investigation benefits from exploration, prioritized hypotheses, and revised decomposition rather than an exhaustive fixed script chosen before evidence. Local study-map skill 1.1 (Agent Architecture), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: Evidence-dependent next actions require adaptive decomposition rather than a fixed exhaustive script.
- **B:** Correct. Open-ended investigation benefits from exploration, prioritized hypotheses, and revised decomposition rather than an exhaustive fixed script chosen before evidence. In this case: Evidence-dependent next actions require adaptive decomposition rather than a fixed exhaustive script.
- **C:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Evidence-dependent next actions require adaptive decomposition rather than a fixed exhaustive script.
- **D:** Incorrect for this question. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: Evidence-dependent next actions require adaptive decomposition rather than a fixed exhaustive script.

### Question 3 — B

Answer: Select specialists according to the actual task. Select specialists according to actual needs instead of executing a ritual pipeline. Dynamic routing avoids invoking every specialist for a simple request. Selection should follow coverage needs, not a fixed ritual. Local study-map skill 1.1 (Agent Architecture), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. In this case: Select specialists according to actual needs instead of executing a ritual pipeline.
- **B:** Correct. Dynamic routing avoids invoking every specialist for a simple request. Selection should follow coverage needs, not a fixed ritual. In this case: Select specialists according to actual needs instead of executing a ritual pipeline.
- **C:** Incorrect for this question. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: Select specialists according to actual needs instead of executing a ritual pipeline.
- **D:** Incorrect for this question. A coordinator manages decomposition, routing, error handling, and aggregation in a hub-and-spoke design. Specialists need not communicate through uncontrolled peer channels. In this case: Select specialists according to actual needs instead of executing a ritual pipeline.

### Question 4 — B

Answer: Assign distinct scopes and explicit coverage responsibilities. Give distinct coverage responsibilities and check their combined scope against requirements. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. Local study-map skill 1.1 (Agent Architecture), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Give distinct coverage responsibilities and check their combined scope against requirements.
- **B:** Correct. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. In this case: Give distinct coverage responsibilities and check their combined scope against requirements.
- **C:** Incorrect for this question. A coordinator manages decomposition, routing, error handling, and aggregation in a hub-and-spoke design. Specialists need not communicate through uncontrolled peer channels. In this case: Give distinct coverage responsibilities and check their combined scope against requirements.
- **D:** Incorrect for this question. The coordinator compares results with requirements, identifies missing evidence, and commissions focused work rather than blindly repeating the whole pipeline. In this case: Give distinct coverage responsibilities and check their combined scope against requirements.

### Question 5 — B

Answer: Route coordination through an orchestrator. Coordinator-based routing supports consistent information flow and error handling. A coordinator manages decomposition, routing, error handling, and aggregation in a hub-and-spoke design. Specialists need not communicate through uncontrolled peer channels. Local study-map skill 1.1 (Agent Architecture), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: Coordinator-based routing supports consistent information flow and error handling.
- **B:** Correct. A coordinator manages decomposition, routing, error handling, and aggregation in a hub-and-spoke design. Specialists need not communicate through uncontrolled peer channels. In this case: Coordinator-based routing supports consistent information flow and error handling.
- **C:** Incorrect for this question. Forking supports divergent explorations without overwriting the original conversation. It does not itself isolate external files or undo side effects. In this case: Coordinator-based routing supports consistent information flow and error handling.
- **D:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Coordinator-based routing supports consistent information flow and error handling.

### Question 6 — C

Answer: Run independent branches concurrently and join checked results. Independent branches can execute concurrently before a checked join. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. Local study-map skill 1.1 (Agent Architecture), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Independent branches can execute concurrently before a checked join.
- **B:** Incorrect for this question. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: Independent branches can execute concurrently before a checked join.
- **C:** Correct. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Independent branches can execute concurrently before a checked join.
- **D:** Incorrect for this question. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: Independent branches can execute concurrently before a checked join.

### Question 7 — D

Answer: Wait for validated prerequisite outputs. Wait for validated prerequisite data before invoking the dependent action. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. Local study-map skill 1.1 (Agent Architecture), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. Dynamic routing avoids invoking every specialist for a simple request. Selection should follow coverage needs, not a fixed ritual. In this case: Wait for validated prerequisite data before invoking the dependent action.
- **B:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Wait for validated prerequisite data before invoking the dependent action.
- **C:** Incorrect for this question. Forking supports divergent explorations without overwriting the original conversation. It does not itself isolate external files or undo side effects. In this case: Wait for validated prerequisite data before invoking the dependent action.
- **D:** Correct. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: Wait for validated prerequisite data before invoking the dependent action.

### Question 8 — A

Answer: Evaluate coverage and delegate targeted follow-up work. Worker completion does not establish evidential coverage of the user's goal. The coordinator compares results with requirements, identifies missing evidence, and commissions focused work rather than blindly repeating the whole pipeline. Local study-map skill 1.1 (Agent Architecture), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Correct. The coordinator compares results with requirements, identifies missing evidence, and commissions focused work rather than blindly repeating the whole pipeline. In this case: Worker completion does not establish evidential coverage of the user's goal.
- **B:** Incorrect for this question. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. In this case: Worker completion does not establish evidential coverage of the user's goal.
- **C:** Incorrect for this question. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. In this case: Worker completion does not establish evidential coverage of the user's goal.
- **D:** Incorrect for this question. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: Worker completion does not establish evidential coverage of the user's goal.

### Question 9 — C

Answer: Translate business goals into measurable functional and operational requirements. The task's actual behavior and constraints determine whether autonomy is necessary. Specify behavior, latency, throughput, data constraints, failure policy, and acceptance criteria. A model or framework choice is not a substitute for requirements. Local study-map skill 1.1 (Agent Architecture), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. In this case: The task's actual behavior and constraints determine whether autonomy is necessary.
- **B:** Incorrect for this question. Evaluate state graphs, typed validation, tracing, ecosystem, and deployment fit across frameworks such as LangGraph, Strands, or PydanticAI. A framework does not guarantee safety or correctness. In this case: The task's actual behavior and constraints determine whether autonomy is necessary.
- **C:** Correct. Specify behavior, latency, throughput, data constraints, failure policy, and acceptance criteria. A model or framework choice is not a substitute for requirements. In this case: The task's actual behavior and constraints determine whether autonomy is necessary.
- **D:** Incorrect for this question. Self-hosting and managed deployment place different responsibilities on operations, networking, identity, and lifecycle. Availability and supported features must be verified. In this case: The task's actual behavior and constraints determine whether autonomy is necessary.

### Question 10 — B

Answer: Pass relevant evidence and constraints explicitly. Pass task-relevant evidence and restrictions explicitly instead of assume shared hidden context. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. Local study-map skill 1.1 (Agent Architecture), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: Pass task-relevant evidence and restrictions explicitly instead of assume shared hidden context.
- **B:** Correct. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Pass task-relevant evidence and restrictions explicitly instead of assume shared hidden context.
- **C:** Incorrect for this question. A coordinator manages decomposition, routing, error handling, and aggregation in a hub-and-spoke design. Specialists need not communicate through uncontrolled peer channels. In this case: Pass task-relevant evidence and restrictions explicitly instead of assume shared hidden context.
- **D:** Incorrect for this question. Delegation requires a permitted launcher under the installed SDK contract. Check Agent versus legacy Task identifiers rather than assume all versions accept the same names. In this case: Pass task-relevant evidence and restrictions explicitly instead of assume shared hidden context.

### Question 11 — C

Answer: Configure the subagent description, prompt, and tool scope. Clarify when each worker should be chosen separately from its internal task prompt. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. Local study-map skill 1.1 (Agent Architecture), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Clarify when each worker should be chosen separately from its internal task prompt.
- **B:** Incorrect for this question. Delegation requires a permitted launcher under the installed SDK contract. Check Agent versus legacy Task identifiers rather than assume all versions accept the same names. In this case: Clarify when each worker should be chosen separately from its internal task prompt.
- **C:** Correct. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: Clarify when each worker should be chosen separately from its internal task prompt.
- **D:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Clarify when each worker should be chosen separately from its internal task prompt.

### Question 12 — C

Answer: Enforce task, iteration, and spending safeguards. Enforce task-level attempts and spending limits independently of protocol continuation. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. Local study-map skill 1.1 (Agent Architecture), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. The loop follows protocol stop reasons, executes permitted requested tools, and returns observations before continuing. Text appearing in a response does not establish completion. In this case: Enforce task-level attempts and spending limits independently of protocol continuation.
- **B:** Incorrect for this question. A max_tokens stop can leave content incomplete. Inspect the response and recover appropriately instead of treating it as normal completion. In this case: Enforce task-level attempts and spending limits independently of protocol continuation.
- **C:** Correct. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. In this case: Enforce task-level attempts and spending limits independently of protocol continuation.
- **D:** Incorrect for this question. This indicates ordinary turn completion, not that every business objective or external action succeeded. Application acceptance checks still apply. In this case: Enforce task-level attempts and spending limits independently of protocol continuation.

### Question 13 — B

Answer: Create a structured handoff with facts, status, and next actions. Send verified facts, attempted steps, unresolved issues, and recommended next actions. The recipient needs verified identifiers, completed work, unresolved issues, supporting evidence, and recommended actions, especially when the full transcript is unavailable. Local study-map skill 1.1 (Agent Architecture), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Send verified facts, attempted steps, unresolved issues, and recommended next actions.
- **B:** Correct. The recipient needs verified identifiers, completed work, unresolved issues, supporting evidence, and recommended actions, especially when the full transcript is unavailable. In this case: Send verified facts, attempted steps, unresolved issues, and recommended next actions.
- **C:** Incorrect for this question. Durable notes counter context degradation and support later verification. Record source versions or change cues so notes are not mistaken for permanently current truth. In this case: Send verified facts, attempted steps, unresolved issues, and recommended next actions.
- **D:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Send verified facts, attempted steps, unresolved issues, and recommended next actions.

### Question 14 — A

Answer: Enforce prerequisites in trusted execution code. Trusted execution checks should block actions whose prerequisites are unsatisfied. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. Local study-map skill 1.1 (Agent Architecture), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Correct. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Trusted execution checks should block actions whose prerequisites are unsatisfied.
- **B:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Trusted execution checks should block actions whose prerequisites are unsatisfied.
- **C:** Incorrect for this question. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: Trusted execution checks should block actions whose prerequisites are unsatisfied.
- **D:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Trusted execution checks should block actions whose prerequisites are unsatisfied.

### Question 15 — A

Answer: Persist structured task state and pending actions. Persist progress and uncertain operations instead of rely on conversational recollection. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. Local study-map skill 1.1 (Agent Architecture), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Correct. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Persist progress and uncertain operations instead of rely on conversational recollection.
- **B:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Persist progress and uncertain operations instead of rely on conversational recollection.
- **C:** Incorrect for this question. This indicates ordinary turn completion, not that every business objective or external action succeeded. Application acceptance checks still apply. In this case: Persist progress and uncertain operations instead of rely on conversational recollection.
- **D:** Incorrect for this question. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Persist progress and uncertain operations instead of rely on conversational recollection.

### Question 16 — D

Answer: Add a cross-file or cross-component integration pass. Cross-component analysis checks assumptions beyond individual local outputs. Local review finds local defects; a separate integration pass checks interactions, interfaces, and data flow across boundaries. Local study-map skill 1.1 (Agent Architecture), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Cross-component analysis checks assumptions beyond individual local outputs.
- **B:** Incorrect for this question. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: Cross-component analysis checks assumptions beyond individual local outputs.
- **C:** Incorrect for this question. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. In this case: Cross-component analysis checks assumptions beyond individual local outputs.
- **D:** Correct. Local review finds local defects; a separate integration pass checks interactions, interfaces, and data flow across boundaries. In this case: Cross-component analysis checks assumptions beyond individual local outputs.

### Question 17 — B

Answer: Select specialists according to the actual task. Invoke only the specialist path justified by the requested result. Dynamic routing avoids invoking every specialist for a simple request. Selection should follow coverage needs, not a fixed ritual. Local study-map skill 1.1 (Agent Architecture), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. A coordinator manages decomposition, routing, error handling, and aggregation in a hub-and-spoke design. Specialists need not communicate through uncontrolled peer channels. In this case: Invoke only the specialist path justified by the requested result.
- **B:** Correct. Dynamic routing avoids invoking every specialist for a simple request. Selection should follow coverage needs, not a fixed ritual. In this case: Invoke only the specialist path justified by the requested result.
- **C:** Incorrect for this question. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. In this case: Invoke only the specialist path justified by the requested result.
- **D:** Incorrect for this question. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: Invoke only the specialist path justified by the requested result.

### Question 18 — C

Answer: Fork an independent branch from a valid shared baseline. Fork separate conversational explorations while controlling shared external effects independently. Forking supports divergent explorations without overwriting the original conversation. It does not itself isolate external files or undo side effects. Local study-map skill 1.1 (Agent Architecture), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Fork separate conversational explorations while controlling shared external effects independently.
- **B:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Fork separate conversational explorations while controlling shared external effects independently.
- **C:** Correct. Forking supports divergent explorations without overwriting the original conversation. It does not itself isolate external files or undo side effects. In this case: Fork separate conversational explorations while controlling shared external effects independently.
- **D:** Incorrect for this question. A new context can avoid stale tool results when assumptions changed widely. Preserve verified facts, relevant constraints, and pointers rather than import all obsolete history. In this case: Fork separate conversational explorations while controlling shared external effects independently.

### Question 19 — D

Answer: Map the problem and revise subtasks as evidence emerges. Revise subtasks as evidence emerges rather than ignore new findings. Open-ended investigation benefits from exploration, prioritized hypotheses, and revised decomposition rather than an exhaustive fixed script chosen before evidence. Local study-map skill 1.1 (Agent Architecture), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: Revise subtasks as evidence emerges rather than ignore new findings.
- **B:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Revise subtasks as evidence emerges rather than ignore new findings.
- **C:** Incorrect for this question. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: Revise subtasks as evidence emerges rather than ignore new findings.
- **D:** Correct. Open-ended investigation benefits from exploration, prioritized hypotheses, and revised decomposition rather than an exhaustive fixed script chosen before evidence. In this case: Revise subtasks as evidence emerges rather than ignore new findings.

### Question 20 — B

Answer: Evaluate coverage and delegate targeted follow-up work. Commission targeted missing work instead of equate polished text with sufficient coverage. The coordinator compares results with requirements, identifies missing evidence, and commissions focused work rather than blindly repeating the whole pipeline. Local study-map skill 1.1 (Agent Architecture), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. In this case: Commission targeted missing work instead of equate polished text with sufficient coverage.
- **B:** Correct. The coordinator compares results with requirements, identifies missing evidence, and commissions focused work rather than blindly repeating the whole pipeline. In this case: Commission targeted missing work instead of equate polished text with sufficient coverage.
- **C:** Incorrect for this question. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. In this case: Commission targeted missing work instead of equate polished text with sufficient coverage.
- **D:** Incorrect for this question. This indicates ordinary turn completion, not that every business objective or external action succeeded. Application acceptance checks still apply. In this case: Commission targeted missing work instead of equate polished text with sufficient coverage.

### Question 21 — D

Answer: Inspect stop_reason and dispatch the appropriate branch. Use documented protocol state rather than infer completion from ordinary commentary. The loop follows protocol stop reasons, executes permitted requested tools, and returns observations before continuing. Text appearing in a response does not establish completion. Local study-map skill 1.2 (Agent Construction with Claude), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. A max_tokens stop can leave content incomplete. Inspect the response and recover appropriately instead of treating it as normal completion. In this case: Use documented protocol state rather than infer completion from ordinary commentary.
- **B:** Incorrect for this question. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. In this case: Use documented protocol state rather than infer completion from ordinary commentary.
- **C:** Incorrect for this question. This indicates ordinary turn completion, not that every business objective or external action succeeded. Application acceptance checks still apply. In this case: Use documented protocol state rather than infer completion from ordinary commentary.
- **D:** Correct. The loop follows protocol stop reasons, executes permitted requested tools, and returns observations before continuing. Text appearing in a response does not establish completion. In this case: Use documented protocol state rather than infer completion from ordinary commentary.

### Question 22 — B

Answer: Append the assistant tool-use blocks and matching tool results. Return matching observations in the valid continuation history so decisions use real results. Client-tool observations must be returned with the correct tool-use identifiers in a valid message sequence so Claude can use actual results. Local study-map skill 1.2 (Agent Construction with Claude), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. A response can contain text, tool use, thinking, or other supported blocks. Do not assume content is one string or that the first block is always displayable text. In this case: Return matching observations in the valid continuation history so decisions use real results.
- **B:** Correct. Client-tool observations must be returned with the correct tool-use identifiers in a valid message sequence so Claude can use actual results. In this case: Return matching observations in the valid continuation history so decisions use real results.
- **C:** Incorrect for this question. SDK accumulation helpers can provide the complete message. Inspect termination and errors before treating the resulting object as accepted application output. In this case: Return matching observations in the valid continuation history so decisions use real results.
- **D:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Return matching observations in the valid continuation history so decisions use real results.

### Question 23 — C

Answer: Use pre-execution tool interception for blocking policy checks. Pre-execution checks can block the effect before it occurs. An appropriate pre-tool hook or equivalent trusted gate can deny a disallowed action before it runs. Hook implementation and failure handling must be tested. Local study-map skill 1.2 (Agent Construction with Claude), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Pre-execution checks can block the effect before it occurs.
- **B:** Incorrect for this question. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: Pre-execution checks can block the effect before it occurs.
- **C:** Correct. An appropriate pre-tool hook or equivalent trusted gate can deny a disallowed action before it runs. Hook implementation and failure handling must be tested. In this case: Pre-execution checks can block the effect before it occurs.
- **D:** Incorrect for this question. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. In this case: Pre-execution checks can block the effect before it occurs.

### Question 24 — C

Answer: Normalize tool observations before model consumption. Normalize observations while preserving meaning, units, and source evidence. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. Local study-map skill 1.2 (Agent Construction with Claude), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. Review must gate the external effect, be tied to the intended action, and use current authority. A later audit cannot reliably reverse a completed effect. In this case: Normalize observations while preserving meaning, units, and source evidence.
- **B:** Incorrect for this question. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Normalize observations while preserving meaning, units, and source evidence.
- **C:** Correct. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. In this case: Normalize observations while preserving meaning, units, and source evidence.
- **D:** Incorrect for this question. An appropriate pre-tool hook or equivalent trusted gate can deny a disallowed action before it runs. Hook implementation and failure handling must be tested. In this case: Normalize observations while preserving meaning, units, and source evidence.

### Question 25 — A

Answer: Compare hosting responsibility, control, and service constraints. Hosting choices shift operational control, responsibility, and supported-service constraints. Self-hosting and managed deployment place different responsibilities on operations, networking, identity, and lifecycle. Availability and supported features must be verified. Local study-map skill 1.2 (Agent Construction with Claude), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Correct. Self-hosting and managed deployment place different responsibilities on operations, networking, identity, and lifecycle. Availability and supported features must be verified. In this case: Hosting choices shift operational control, responsibility, and supported-service constraints.
- **B:** Incorrect for this question. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: Hosting choices shift operational control, responsibility, and supported-service constraints.
- **C:** Incorrect for this question. Evaluate state graphs, typed validation, tracing, ecosystem, and deployment fit across frameworks such as LangGraph, Strands, or PydanticAI. A framework does not guarantee safety or correctness. In this case: Hosting choices shift operational control, responsibility, and supported-service constraints.
- **D:** Incorrect for this question. Different hosting providers can use distinct authentication, endpoints, identifiers, and supported features. Normalize the application contract without assuming identical wire protocols. In this case: Hosting choices shift operational control, responsibility, and supported-service constraints.

### Question 26 — D

Answer: Enable the version-appropriate subagent invocation tool. Delegation requires the permitted launcher supported by the actual SDK release. Delegation requires a permitted launcher under the installed SDK contract. Check Agent versus legacy Task identifiers rather than assume all versions accept the same names. Local study-map skill 1.2 (Agent Construction with Claude), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Delegation requires the permitted launcher supported by the actual SDK release.
- **B:** Incorrect for this question. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: Delegation requires the permitted launcher supported by the actual SDK release.
- **C:** Incorrect for this question. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Delegation requires the permitted launcher supported by the actual SDK release.
- **D:** Correct. Delegation requires a permitted launcher under the installed SDK contract. Check Agent versus legacy Task identifiers rather than assume all versions accept the same names. In this case: Delegation requires the permitted launcher supported by the actual SDK release.

### Question 27 — A

Answer: Enforce prerequisites in trusted execution code. Trusted execution must authorize the actual target and action independently of model wording. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. Local study-map skill 1.2 (Agent Construction with Claude), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Correct. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Trusted execution must authorize the actual target and action independently of model wording.
- **B:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Trusted execution must authorize the actual target and action independently of model wording.
- **C:** Incorrect for this question. Review must gate the external effect, be tied to the intended action, and use current authority. A later audit cannot reliably reverse a completed effect. In this case: Trusted execution must authorize the actual target and action independently of model wording.
- **D:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Trusted execution must authorize the actual target and action independently of model wording.

### Question 28 — D

Answer: Preserve protocol-required blocks through tool continuations. Keep version-required blocks intact rather than invent or edit continuation state. When a model or feature requires returned context or signed thinking blocks, follow that version-specific contract. Do not edit signed blocks or manufacture hidden reasoning. Local study-map skill 1.2 (Agent Construction with Claude), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. Client-tool observations must be returned with the correct tool-use identifiers in a valid message sequence so Claude can use actual results. In this case: Keep version-required blocks intact rather than invent or edit continuation state.
- **B:** Incorrect for this question. A response can contain text, tool use, thinking, or other supported blocks. Do not assume content is one string or that the first block is always displayable text. In this case: Keep version-required blocks intact rather than invent or edit continuation state.
- **C:** Incorrect for this question. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. In this case: Keep version-required blocks intact rather than invent or edit continuation state.
- **D:** Correct. When a model or feature requires returned context or signed thinking blocks, follow that version-specific contract. Do not edit signed blocks or manufacture hidden reasoning. In this case: Keep version-required blocks intact rather than invent or edit continuation state.

### Question 29 — A

Answer: Use a durable idempotency key for the same logical action. Use durable logical-action identity where the external system supports idempotent handling. Where supported, repeated requests for one operation should resolve to one intended external effect. Generating a new key for each retry defeats duplicate protection. Local study-map skill 1.2 (Agent Construction with Claude), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Correct. Where supported, repeated requests for one operation should resolve to one intended external effect. Generating a new key for each retry defeats duplicate protection. In this case: Use durable logical-action identity where the external system supports idempotent handling.
- **B:** Incorrect for this question. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. In this case: Use durable logical-action identity where the external system supports idempotent handling.
- **C:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Use durable logical-action identity where the external system supports idempotent handling.
- **D:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Use durable logical-action identity where the external system supports idempotent handling.

### Question 30 — A

Answer: Set explicit deadlines and classify timeout outcomes. Explicit dependency and task deadlines bound waits and clarify failure behavior. Bound user and dependency waits. A timeout is an uncertain execution outcome for mutations and may require status reconciliation rather than blind retry. Local study-map skill 1.2 (Agent Construction with Claude), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Correct. Bound user and dependency waits. A timeout is an uncertain execution outcome for mutations and may require status reconciliation rather than blind retry. In this case: Explicit dependency and task deadlines bound waits and clarify failure behavior.
- **B:** Incorrect for this question. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: Explicit dependency and task deadlines bound waits and clarify failure behavior.
- **C:** Incorrect for this question. Local cancellation limits waiting or computation but does not guarantee the server stopped or a remote side effect was rolled back. In this case: Explicit dependency and task deadlines bound waits and clarify failure behavior.
- **D:** Incorrect for this question. Nested automatic retries can multiply attempts and latency. Set a shared attempt or elapsed-time budget and inspect SDK defaults. In this case: Explicit dependency and task deadlines bound waits and clarify failure behavior.

### Question 31 — D

Answer: Configure the subagent description, prompt, and tool scope. The worker's role and effective tools must match read-oriented responsibilities. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. Local study-map skill 1.2 (Agent Construction with Claude), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. Delegation requires a permitted launcher under the installed SDK contract. Check Agent versus legacy Task identifiers rather than assume all versions accept the same names. In this case: The worker's role and effective tools must match read-oriented responsibilities.
- **B:** Incorrect for this question. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. In this case: The worker's role and effective tools must match read-oriented responsibilities.
- **C:** Incorrect for this question. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: The worker's role and effective tools must match read-oriented responsibilities.
- **D:** Correct. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: The worker's role and effective tools must match read-oriented responsibilities.

### Question 32 — C

Answer: Require authorized approval before the consequential action. Bind authorized human approval to the current proposed action before execution. Review must gate the external effect, be tied to the intended action, and use current authority. A later audit cannot reliably reverse a completed effect. Local study-map skill 1.2 (Agent Construction with Claude), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. The recipient needs verified identifiers, completed work, unresolved issues, supporting evidence, and recommended actions, especially when the full transcript is unavailable. In this case: Bind authorized human approval to the current proposed action before execution.
- **B:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Bind authorized human approval to the current proposed action before execution.
- **C:** Correct. Review must gate the external effect, be tied to the intended action, and use current authority. A later audit cannot reliably reverse a completed effect. In this case: Bind authorized human approval to the current proposed action before execution.
- **D:** Incorrect for this question. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Bind authorized human approval to the current proposed action before execution.

### Question 33 — A

Answer: Checkpoint durable state at safe workflow boundaries. Checkpoint progress and pending actions at safe durable boundaries. Recovery needs committed progress, pending actions, evidence versions, and consistent artifacts. Checkpointing conversation text alone does not establish transaction completion. Local study-map skill 1.2 (Agent Construction with Claude), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Correct. Recovery needs committed progress, pending actions, evidence versions, and consistent artifacts. Checkpointing conversation text alone does not establish transaction completion. In this case: Checkpoint progress and pending actions at safe durable boundaries.
- **B:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Checkpoint progress and pending actions at safe durable boundaries.
- **C:** Incorrect for this question. Recovery needs known state locations, completion status, source versions, and pending work. Do not infer completion merely because an output file exists. In this case: Checkpoint progress and pending actions at safe durable boundaries.
- **D:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Checkpoint progress and pending actions at safe durable boundaries.

### Question 34 — B

Answer: Cancel local work and reconcile any external operation separately. Local cancellation does not establish that the remote operation was undone. Local cancellation limits waiting or computation but does not guarantee the server stopped or a remote side effect was rolled back. Local study-map skill 1.2 (Agent Construction with Claude), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. Bound user and dependency waits. A timeout is an uncertain execution outcome for mutations and may require status reconciliation rather than blind retry. In this case: Local cancellation does not establish that the remote operation was undone.
- **B:** Correct. Local cancellation limits waiting or computation but does not guarantee the server stopped or a remote side effect was rolled back. In this case: Local cancellation does not establish that the remote operation was undone.
- **C:** Incorrect for this question. Separate a generated proposal from an authorized atomic or otherwise well-coordinated business effect. Define conflict handling and rollback or compensation behavior. In this case: Local cancellation does not establish that the remote operation was undone.
- **D:** Incorrect for this question. Where supported, repeated requests for one operation should resolve to one intended external effect. Generating a new key for each retry defeats duplicate protection. In this case: Local cancellation does not establish that the remote operation was undone.

### Question 35 — C

Answer: Inspect a redacted end-to-end request and tool trace. Inspect actual requests, tool dispatch, observations, and termination boundaries. Correlate the actual request, model response, tool execution, retries, and validation results. Diagnose the first failing boundary rather than infer cause from the final prose. Local study-map skill 1.2 (Agent Construction with Claude), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Inspect actual requests, tool dispatch, observations, and termination boundaries.
- **B:** Incorrect for this question. Link a user task to provider requests, worker runs, and actions without using sensitive content as an identifier. Protect telemetry access and retention. In this case: Inspect actual requests, tool dispatch, observations, and termination boundaries.
- **C:** Correct. Correlate the actual request, model response, tool execution, retries, and validation results. Diagnose the first failing boundary rather than infer cause from the final prose. In this case: Inspect actual requests, tool dispatch, observations, and termination boundaries.
- **D:** Incorrect for this question. Inject timeouts, malformed responses, and provider failures without live side effects. Combine with contract and representative integration tests rather than infer complete correctness from mocks. In this case: Inspect actual requests, tool dispatch, observations, and termination boundaries.

### Question 36 — A

Answer: Choose a framework for needed orchestration semantics. Evaluate needed state, validation, orchestration, tracing, and deployment semantics rather than popularity. Evaluate state graphs, typed validation, tracing, ecosystem, and deployment fit across frameworks such as LangGraph, Strands, or PydanticAI. A framework does not guarantee safety or correctness. Local study-map skill 1.3 (Agent Patterns and Frameworks), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Correct. Evaluate state graphs, typed validation, tracing, ecosystem, and deployment fit across frameworks such as LangGraph, Strands, or PydanticAI. A framework does not guarantee safety or correctness. In this case: Evaluate needed state, validation, orchestration, tracing, and deployment semantics rather than popularity.
- **B:** Incorrect for this question. Self-hosting and managed deployment place different responsibilities on operations, networking, identity, and lifecycle. Availability and supported features must be verified. In this case: Evaluate needed state, validation, orchestration, tracing, and deployment semantics rather than popularity.
- **C:** Incorrect for this question. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. In this case: Evaluate needed state, validation, orchestration, tracing, and deployment semantics rather than popularity.
- **D:** Incorrect for this question. Different hosting providers can use distinct authentication, endpoints, identifiers, and supported features. Normalize the application contract without assuming identical wire protocols. In this case: Evaluate needed state, validation, orchestration, tracing, and deployment semantics rather than popularity.

### Question 37 — A

Answer: Checkpoint durable state at safe workflow boundaries. Durable checkpoints must distinguish completed work from pending or uncertain effects. Recovery needs committed progress, pending actions, evidence versions, and consistent artifacts. Checkpointing conversation text alone does not establish transaction completion. Local study-map skill 1.3 (Agent Patterns and Frameworks), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Correct. Recovery needs committed progress, pending actions, evidence versions, and consistent artifacts. Checkpointing conversation text alone does not establish transaction completion. In this case: Durable checkpoints must distinguish completed work from pending or uncertain effects.
- **B:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Durable checkpoints must distinguish completed work from pending or uncertain effects.
- **C:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Durable checkpoints must distinguish completed work from pending or uncertain effects.
- **D:** Incorrect for this question. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. In this case: Durable checkpoints must distinguish completed work from pending or uncertain effects.

### Question 38 — A

Answer: Pass relevant evidence and constraints explicitly. Explicit context passing is necessary when relevant history is not automatically available. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. Local study-map skill 1.3 (Agent Patterns and Frameworks), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Correct. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Explicit context passing is necessary when relevant history is not automatically available.
- **B:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Explicit context passing is necessary when relevant history is not automatically available.
- **C:** Incorrect for this question. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. In this case: Explicit context passing is necessary when relevant history is not automatically available.
- **D:** Incorrect for this question. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: Explicit context passing is necessary when relevant history is not automatically available.

### Question 39 — D

Answer: Run independent branches concurrently and join checked results. Independent work may run concurrently under bounded resource and access rules. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. Local study-map skill 1.3 (Agent Patterns and Frameworks), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: Independent work may run concurrently under bounded resource and access rules.
- **B:** Incorrect for this question. Forking supports divergent explorations without overwriting the original conversation. It does not itself isolate external files or undo side effects. In this case: Independent work may run concurrently under bounded resource and access rules.
- **C:** Incorrect for this question. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: Independent work may run concurrently under bounded resource and access rules.
- **D:** Correct. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Independent work may run concurrently under bounded resource and access rules.

### Question 40 — C

Answer: Wait for validated prerequisite outputs. Synthesis depends on validated evidence and must wait for its prerequisites. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. Local study-map skill 1.3 (Agent Patterns and Frameworks), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. Open-ended investigation benefits from exploration, prioritized hypotheses, and revised decomposition rather than an exhaustive fixed script chosen before evidence. In this case: Synthesis depends on validated evidence and must wait for its prerequisites.
- **B:** Incorrect for this question. Dynamic routing avoids invoking every specialist for a simple request. Selection should follow coverage needs, not a fixed ritual. In this case: Synthesis depends on validated evidence and must wait for its prerequisites.
- **C:** Correct. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: Synthesis depends on validated evidence and must wait for its prerequisites.
- **D:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Synthesis depends on validated evidence and must wait for its prerequisites.

### Question 41 — C

Answer: Persist concise codebase findings with file and symbol pointers. Keep concise checked findings with source pointers that can be revalidated. Durable notes counter context degradation and support later verification. Record source versions or change cues so notes are not mistaken for permanently current truth. Local study-map skill 1.3 (Agent Patterns and Frameworks), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Keep concise checked findings with source pointers that can be revalidated.
- **B:** Incorrect for this question. Keep verified amounts, identifiers, dates, and commitments in structured state. General summaries can omit details that later decisions depend on. In this case: Keep concise checked findings with source pointers that can be revalidated.
- **C:** Correct. Durable notes counter context degradation and support later verification. Record source versions or change cues so notes are not mistaken for permanently current truth. In this case: Keep concise checked findings with source pointers that can be revalidated.
- **D:** Incorrect for this question. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. In this case: Keep concise checked findings with source pointers that can be revalidated.

### Question 42 — C

Answer: Compact context while preserving checked facts and open issues. Compact accumulated history while preserving critical facts and unresolved issues. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. Local study-map skill 1.3 (Agent Patterns and Frameworks), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. Keep verified amounts, identifiers, dates, and commitments in structured state. General summaries can omit details that later decisions depend on. In this case: Compact accumulated history while preserving critical facts and unresolved issues.
- **B:** Incorrect for this question. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: Compact accumulated history while preserving critical facts and unresolved issues.
- **C:** Correct. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Compact accumulated history while preserving critical facts and unresolved issues.
- **D:** Incorrect for this question. A structured overview and clear sections help reduce long-input position effects. Placement is a mitigation, not proof that every fact will be used. In this case: Compact accumulated history while preserving critical facts and unresolved issues.

### Question 43 — B

Answer: Choose a framework for needed orchestration semantics. Framework capabilities must be evaluated; authorization and safety still require deliberate implementation. Evaluate state graphs, typed validation, tracing, ecosystem, and deployment fit across frameworks such as LangGraph, Strands, or PydanticAI. A framework does not guarantee safety or correctness. Local study-map skill 1.3 (Agent Patterns and Frameworks), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. Self-hosting and managed deployment place different responsibilities on operations, networking, identity, and lifecycle. Availability and supported features must be verified. In this case: Framework capabilities must be evaluated; authorization and safety still require deliberate implementation.
- **B:** Correct. Evaluate state graphs, typed validation, tracing, ecosystem, and deployment fit across frameworks such as LangGraph, Strands, or PydanticAI. A framework does not guarantee safety or correctness. In this case: Framework capabilities must be evaluated; authorization and safety still require deliberate implementation.
- **C:** Incorrect for this question. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Framework capabilities must be evaluated; authorization and safety still require deliberate implementation.
- **D:** Incorrect for this question. No one prompt or content filter covers all attack paths. Combine least privilege, trusted checks, telemetry, tests, and incident response. In this case: Framework capabilities must be evaluated; authorization and safety still require deliberate implementation.

### Question 44 — B

Answer: Assign distinct scopes and explicit coverage responsibilities. Assign focused responsibilities rather than duplicate all work across specialists. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. Local study-map skill 1.3 (Agent Patterns and Frameworks), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Assign focused responsibilities rather than duplicate all work across specialists.
- **B:** Correct. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. In this case: Assign focused responsibilities rather than duplicate all work across specialists.
- **C:** Incorrect for this question. A coordinator manages decomposition, routing, error handling, and aggregation in a hub-and-spoke design. Specialists need not communicate through uncontrolled peer channels. In this case: Assign focused responsibilities rather than duplicate all work across specialists.
- **D:** Incorrect for this question. The coordinator compares results with requirements, identifies missing evidence, and commissions focused work rather than blindly repeating the whole pipeline. In this case: Assign focused responsibilities rather than duplicate all work across specialists.

### Question 45 — D

Answer: Start a fresh session with a checked structured summary. Start from a checked current summary rather than reuse stale evidence wholesale. A new context can avoid stale tool results when assumptions changed widely. Preserve verified facts, relevant constraints, and pointers rather than import all obsolete history. Local study-map skill 1.3 (Agent Patterns and Frameworks), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. Targeted re-analysis works when most prior context remains useful. Explicit change information prevents reliance on stale file or tool observations. In this case: Start from a checked current summary rather than reuse stale evidence wholesale.
- **B:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Start from a checked current summary rather than reuse stale evidence wholesale.
- **C:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Start from a checked current summary rather than reuse stale evidence wholesale.
- **D:** Correct. A new context can avoid stale tool results when assumptions changed widely. Preserve verified facts, relevant constraints, and pointers rather than import all obsolete history. In this case: Start from a checked current summary rather than reuse stale evidence wholesale.

### Question 46 — D

Answer: Return structured failure context and partial results. Preserve failure type, attempts, partial results, and possible alternatives for recovery. The coordinator needs failure type, attempted operation, useful outputs, and alternatives. A failure must not be disguised as a successful empty search. Local study-map skill 1.3 (Agent Patterns and Frameworks), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. In this case: Preserve failure type, attempts, partial results, and possible alternatives for recovery.
- **B:** Incorrect for this question. A report can proceed with supported partial results if it clearly distinguishes established conclusions from gaps. Silence falsely implies complete coverage. In this case: Preserve failure type, attempts, partial results, and possible alternatives for recovery.
- **C:** Incorrect for this question. An error contract should identify failure class, recoverability, and useful context. MCP isError marks an execution failure; it should not disguise a valid empty result. In this case: Preserve failure type, attempts, partial results, and possible alternatives for recovery.
- **D:** Correct. The coordinator needs failure type, attempted operation, useful outputs, and alternatives. A failure must not be disguised as a successful empty search. In this case: Preserve failure type, attempts, partial results, and possible alternatives for recovery.

### Question 47 — A

Answer: Enforce task, iteration, and spending safeguards. Bound delegation depth, task attempts, and spending rather than permit endless coordination. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. Local study-map skill 1.3 (Agent Patterns and Frameworks), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Correct. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. In this case: Bound delegation depth, task attempts, and spending rather than permit endless coordination.
- **B:** Incorrect for this question. The loop follows protocol stop reasons, executes permitted requested tools, and returns observations before continuing. Text appearing in a response does not establish completion. In this case: Bound delegation depth, task attempts, and spending rather than permit endless coordination.
- **C:** Incorrect for this question. This indicates ordinary turn completion, not that every business objective or external action succeeded. Application acceptance checks still apply. In this case: Bound delegation depth, task attempts, and spending rather than permit endless coordination.
- **D:** Incorrect for this question. Recovery needs committed progress, pending actions, evidence versions, and consistent artifacts. Checkpointing conversation text alone does not establish transaction completion. In this case: Bound delegation depth, task attempts, and spending rather than permit endless coordination.

### Question 48 — B

Answer: Select specialists according to the actual task. Choose subsequent specialists according to observed task needs rather than a fixed universal sequence. Dynamic routing avoids invoking every specialist for a simple request. Selection should follow coverage needs, not a fixed ritual. Local study-map skill 1.3 (Agent Patterns and Frameworks), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. A coordinator manages decomposition, routing, error handling, and aggregation in a hub-and-spoke design. Specialists need not communicate through uncontrolled peer channels. In this case: Choose subsequent specialists according to observed task needs rather than a fixed universal sequence.
- **B:** Correct. Dynamic routing avoids invoking every specialist for a simple request. Selection should follow coverage needs, not a fixed ritual. In this case: Choose subsequent specialists according to observed task needs rather than a fixed universal sequence.
- **C:** Incorrect for this question. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: Choose subsequent specialists according to observed task needs rather than a fixed universal sequence.
- **D:** Incorrect for this question. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. In this case: Choose subsequent specialists according to observed task needs rather than a fixed universal sequence.

### Question 49 — A

Answer: Persist structured task state and pending actions. Application state supplies memory without implying permanent model-weight learning. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. Local study-map skill 1.3 (Agent Patterns and Frameworks), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Correct. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Application state supplies memory without implying permanent model-weight learning.
- **B:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Application state supplies memory without implying permanent model-weight learning.
- **C:** Incorrect for this question. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. In this case: Application state supplies memory without implying permanent model-weight learning.
- **D:** Incorrect for this question. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Application state supplies memory without implying permanent model-weight learning.

### Question 50 — C

Answer: Evaluate coverage and delegate targeted follow-up work. Check evidential coverage and unresolved conflicts rather than accept every returned artifact automatically. The coordinator compares results with requirements, identifies missing evidence, and commissions focused work rather than blindly repeating the whole pipeline. Local study-map skill 1.3 (Agent Patterns and Frameworks), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. In this case: Check evidential coverage and unresolved conflicts rather than accept every returned artifact automatically.
- **B:** Incorrect for this question. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: Check evidential coverage and unresolved conflicts rather than accept every returned artifact automatically.
- **C:** Correct. The coordinator compares results with requirements, identifies missing evidence, and commissions focused work rather than blindly repeating the whole pipeline. In this case: Check evidential coverage and unresolved conflicts rather than accept every returned artifact automatically.
- **D:** Incorrect for this question. A coordinator manages decomposition, routing, error handling, and aggregation in a hub-and-spoke design. Specialists need not communicate through uncontrolled peer channels. In this case: Check evidential coverage and unresolved conflicts rather than accept every returned artifact automatically.

### Question 51 — D

Answer: Clarify tool purpose, inputs, outputs, and boundaries. Describe distinct purposes, inputs, outputs, and boundaries so selection is informed. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. Local study-map skill 8.1 (Tool Implementation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. In this case: Describe distinct purposes, inputs, outputs, and boundaries so selection is informed.
- **B:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Describe distinct purposes, inputs, outputs, and boundaries so selection is informed.
- **C:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Describe distinct purposes, inputs, outputs, and boundaries so selection is informed.
- **D:** Correct. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Describe distinct purposes, inputs, outputs, and boundaries so selection is informed.

### Question 52 — B

Answer: Define and validate a precise input schema. A precise schema expresses the required argument shape before semantic and authorization checks. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. Local study-map skill 8.1 (Tool Implementation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: A precise schema expresses the required argument shape before semantic and authorization checks.
- **B:** Correct. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. In this case: A precise schema expresses the required argument shape before semantic and authorization checks.
- **C:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: A precise schema expresses the required argument shape before semantic and authorization checks.
- **D:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: A precise schema expresses the required argument shape before semantic and authorization checks.

### Question 53 — B

Answer: Return a structured tool error with category and retryability. Structured error metadata must distinguish failure from valid no-match results. An error contract should identify failure class, recoverability, and useful context. MCP isError marks an execution failure; it should not disguise a valid empty result. Local study-map skill 8.1 (Tool Implementation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Client-tool observations must be returned with the correct tool-use identifiers in a valid message sequence so Claude can use actual results. In this case: Structured error metadata must distinguish failure from valid no-match results.
- **B:** Correct. An error contract should identify failure class, recoverability, and useful context. MCP isError marks an execution failure; it should not disguise a valid empty result. In this case: Structured error metadata must distinguish failure from valid no-match results.
- **C:** Incorrect for this question. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. In this case: Structured error metadata must distinguish failure from valid no-match results.
- **D:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Structured error metadata must distinguish failure from valid no-match results.

### Question 54 — C

Answer: Correct invalid arguments before retrying. Correct the malformed argument rather than retry the identical request. A validation failure points to an input defect. Repeating identical invalid arguments is not recovery. Local study-map skill 8.1 (Tool Implementation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Permission denial does not justify trying alternate credentials or leaking restricted content. Recover only through explicitly authorized mechanisms. In this case: Correct the malformed argument rather than retry the identical request.
- **B:** Incorrect for this question. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: Correct the malformed argument rather than retry the identical request.
- **C:** Correct. A validation failure points to an input defect. Repeating identical invalid arguments is not recovery. In this case: Correct the malformed argument rather than retry the identical request.
- **D:** Incorrect for this question. A policy rejection is not normally fixed by repeating the same operation. Communicate the reason and legitimate next steps without evasion. In this case: Correct the malformed argument rather than retry the identical request.

### Question 55 — C

Answer: Stop the unauthorized operation and use an approved access path. Stop unauthorized access and use only approved mechanisms for resolving permissions. Permission denial does not justify trying alternate credentials or leaking restricted content. Recover only through explicitly authorized mechanisms. Local study-map skill 8.1 (Tool Implementation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. A validation failure points to an input defect. Repeating identical invalid arguments is not recovery. In this case: Stop unauthorized access and use only approved mechanisms for resolving permissions.
- **B:** Incorrect for this question. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: Stop unauthorized access and use only approved mechanisms for resolving permissions.
- **C:** Correct. Permission denial does not justify trying alternate credentials or leaking restricted content. Recover only through explicitly authorized mechanisms. In this case: Stop unauthorized access and use only approved mechanisms for resolving permissions.
- **D:** Incorrect for this question. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. In this case: Stop unauthorized access and use only approved mechanisms for resolving permissions.

### Question 56 — D

Answer: Retry a transient failure with bounded backoff. Use bounded delayed retry according to service guidance and action safety. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. Local study-map skill 8.1 (Tool Implementation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. A policy rejection is not normally fixed by repeating the same operation. Communicate the reason and legitimate next steps without evasion. In this case: Use bounded delayed retry according to service guidance and action safety.
- **B:** Incorrect for this question. A validation failure points to an input defect. Repeating identical invalid arguments is not recovery. In this case: Use bounded delayed retry according to service guidance and action safety.
- **C:** Incorrect for this question. Permission denial does not justify trying alternate credentials or leaking restricted content. Recover only through explicitly authorized mechanisms. In this case: Use bounded delayed retry according to service guidance and action safety.
- **D:** Correct. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: Use bounded delayed retry according to service guidance and action safety.

### Question 57 — A

Answer: Explain the non-retryable business-rule outcome. A business rejection is normally non-retryable without a legitimate change in circumstances. A policy rejection is not normally fixed by repeating the same operation. Communicate the reason and legitimate next steps without evasion. Local study-map skill 8.1 (Tool Implementation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. A policy rejection is not normally fixed by repeating the same operation. Communicate the reason and legitimate next steps without evasion. In this case: A business rejection is normally non-retryable without a legitimate change in circumstances.
- **B:** Incorrect for this question. A validation failure points to an input defect. Repeating identical invalid arguments is not recovery. In this case: A business rejection is normally non-retryable without a legitimate change in circumstances.
- **C:** Incorrect for this question. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: A business rejection is normally non-retryable without a legitimate change in circumstances.
- **D:** Incorrect for this question. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. In this case: A business rejection is normally non-retryable without a legitimate change in circumstances.

### Question 58 — A

Answer: Represent a successful query with no matches explicitly. Successful emptiness must not be confused with a transport or permission failure. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. Local study-map skill 8.1 (Tool Implementation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. In this case: Successful emptiness must not be confused with a transport or permission failure.
- **B:** Incorrect for this question. Permission denial does not justify trying alternate credentials or leaking restricted content. Recover only through explicitly authorized mechanisms. In this case: Successful emptiness must not be confused with a transport or permission failure.
- **C:** Incorrect for this question. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: Successful emptiness must not be confused with a transport or permission failure.
- **D:** Incorrect for this question. An error contract should identify failure class, recoverability, and useful context. MCP isError marks an execution failure; it should not disguise a valid empty result. In this case: Successful emptiness must not be confused with a transport or permission failure.

### Question 59 — B

Answer: Give each specialist only task-relevant tools. Limit effective tools to the specialist's role to reduce confusion and excess authority. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. Local study-map skill 8.1 (Tool Implementation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Limit effective tools to the specialist's role to reduce confusion and excess authority.
- **B:** Correct. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Limit effective tools to the specialist's role to reduce confusion and excess authority.
- **C:** Incorrect for this question. Configured servers can expose tools together when connected, but server failure, approval, filtering, and permissions can affect what is actually usable. In this case: Limit effective tools to the specialist's role to reduce confusion and excess authority.
- **D:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Limit effective tools to the specialist's role to reduce confusion and excess authority.

### Question 60 — B

Answer: Expose a constrained domain-specific operation. Constrain and validate the actual operation rather than allow arbitrary destinations. A narrow operation can enforce permitted sources, destinations, or actions more reliably than a general arbitrary-command or unrestricted-fetch interface. Local study-map skill 8.1 (Tool Implementation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Constrain and validate the actual operation rather than allow arbitrary destinations.
- **B:** Correct. A narrow operation can enforce permitted sources, destinations, or actions more reliably than a general arbitrary-command or unrestricted-fetch interface. In this case: Constrain and validate the actual operation rather than allow arbitrary destinations.
- **C:** Incorrect for this question. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. In this case: Constrain and validate the actual operation rather than allow arbitrary destinations.
- **D:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Constrain and validate the actual operation rather than allow arbitrary destinations.

### Question 61 — D

Answer: Force the required named tool for that turn. Forced named selection differs from merely requiring any available tool. Where supported, named tool selection requires the specified tool. Additional workflow ordering and authorization still belong in application code. Local study-map skill 8.1 (Tool Implementation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Auto permits either a tool call or an ordinary response. It cannot guarantee extraction through a tool on every request. In this case: Forced named selection differs from merely requiring any available tool.
- **B:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Forced named selection differs from merely requiring any available tool.
- **C:** Incorrect for this question. Where supported, any requires a tool selection but leaves the specific tool to the model. It does not guarantee that a particular named tool runs. In this case: Forced named selection differs from merely requiring any available tool.
- **D:** Correct. Where supported, named tool selection requires the specified tool. Additional workflow ordering and authorization still belong in application code. In this case: Forced named selection differs from merely requiring any available tool.

### Question 62 — B

Answer: Use tool_choice with type any. Any requires a tool call without selecting the same named tool in advance. Where supported, any requires a tool selection but leaves the specific tool to the model. It does not guarantee that a particular named tool runs. Local study-map skill 8.1 (Tool Implementation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Auto permits either a tool call or an ordinary response. It cannot guarantee extraction through a tool on every request. In this case: Any requires a tool call without selecting the same named tool in advance.
- **B:** Correct. Where supported, any requires a tool selection but leaves the specific tool to the model. It does not guarantee that a particular named tool runs. In this case: Any requires a tool call without selecting the same named tool in advance.
- **C:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Any requires a tool call without selecting the same named tool in advance.
- **D:** Incorrect for this question. Where supported, named tool selection requires the specified tool. Additional workflow ordering and authorization still belong in application code. In this case: Any requires a tool call without selecting the same named tool in advance.

### Question 63 — C

Answer: Use tool_choice with type auto. Auto allows conversational output when a tool is not needed. Auto permits either a tool call or an ordinary response. It cannot guarantee extraction through a tool on every request. Local study-map skill 8.1 (Tool Implementation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Where supported, any requires a tool selection but leaves the specific tool to the model. It does not guarantee that a particular named tool runs. In this case: Auto allows conversational output when a tool is not needed.
- **B:** Incorrect for this question. Where supported, named tool selection requires the specified tool. Additional workflow ordering and authorization still belong in application code. In this case: Auto allows conversational output when a tool is not needed.
- **C:** Correct. Auto permits either a tool call or an ordinary response. It cannot guarantee extraction through a tool on every request. In this case: Auto allows conversational output when a tool is not needed.
- **D:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Auto allows conversational output when a tool is not needed.

### Question 64 — D

Answer: Enforce prerequisites in trusted execution code. Tool selection never replaces trusted validation and authorization of the actual action. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. Local study-map skill 8.1 (Tool Implementation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Tool selection never replaces trusted validation and authorization of the actual action.
- **B:** Incorrect for this question. Where supported, any requires a tool selection but leaves the specific tool to the model. It does not guarantee that a particular named tool runs. In this case: Tool selection never replaces trusted validation and authorization of the actual action.
- **C:** Incorrect for this question. Where supported, named tool selection requires the specified tool. Additional workflow ordering and authorization still belong in application code. In this case: Tool selection never replaces trusted validation and authorization of the actual action.
- **D:** Correct. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Tool selection never replaces trusted validation and authorization of the actual action.

### Question 65 — C

Answer: Implement an application-local tool for a specific integration. An application-local tool can meet a focused integration need without additional MCP deployment. A local function tool can fit the needs of one application without deploying an MCP service. Still define schemas, authorization, error behavior, and tests. Local study-map skill 8.1 (Tool Implementation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. An MCP server exposes tools, resources, or prompts over supported transports and owns clear contracts. Reuse and security require deliberate deployment and permission design. In this case: An application-local tool can meet a focused integration need without additional MCP deployment.
- **B:** Incorrect for this question. Built-in tools can avoid unnecessary custom integration for supported local operations. They do not automatically reach arbitrary private services or bypass permissions. In this case: An application-local tool can meet a focused integration need without additional MCP deployment.
- **C:** Correct. A local function tool can fit the needs of one application without deploying an MCP service. Still define schemas, authorization, error behavior, and tests. In this case: An application-local tool can meet a focused integration need without additional MCP deployment.
- **D:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: An application-local tool can meet a focused integration need without additional MCP deployment.

### Question 66 — A

Answer: Append the assistant tool-use blocks and matching tool results. The application dispatches permitted client-tool calls and supplies matching results. Client-tool observations must be returned with the correct tool-use identifiers in a valid message sequence so Claude can use actual results. Local study-map skill 8.1 (Tool Implementation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Client-tool observations must be returned with the correct tool-use identifiers in a valid message sequence so Claude can use actual results. In this case: The application dispatches permitted client-tool calls and supplies matching results.
- **B:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: The application dispatches permitted client-tool calls and supplies matching results.
- **C:** Incorrect for this question. An error contract should identify failure class, recoverability, and useful context. MCP isError marks an execution failure; it should not disguise a valid empty result. In this case: The application dispatches permitted client-tool calls and supplies matching results.
- **D:** Incorrect for this question. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. In this case: The application dispatches permitted client-tool calls and supplies matching results.

### Question 67 — A

Answer: Use a provider-specific adapter behind a stable application interface. Client-side and server-side capabilities depend on the actual provider contract. Different hosting providers can use distinct authentication, endpoints, identifiers, and supported features. Normalize the application contract without assuming identical wire protocols. Local study-map skill 8.1 (Tool Implementation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Different hosting providers can use distinct authentication, endpoints, identifiers, and supported features. Normalize the application contract without assuming identical wire protocols. In this case: Client-side and server-side capabilities depend on the actual provider contract.
- **B:** Incorrect for this question. Built-in tools can avoid unnecessary custom integration for supported local operations. They do not automatically reach arbitrary private services or bypass permissions. In this case: Client-side and server-side capabilities depend on the actual provider contract.
- **C:** Incorrect for this question. The client discovers and calls server-exposed capabilities under supported protocol and authorization. A model does not independently contact every backend without an integration. In this case: Client-side and server-side capabilities depend on the actual provider contract.
- **D:** Incorrect for this question. A local function tool can fit the needs of one application without deploying an MCP service. Still define schemas, authorization, error behavior, and tests. In this case: Client-side and server-side capabilities depend on the actual provider contract.

### Question 68 — A

Answer: Recover transiently within the worker, then report unresolved failure. Recover locally when permitted, then report unresolved failure with useful context. Bounded local recovery reduces coordinator noise. Exhausted recovery should preserve attempts, partial results, and alternatives rather than silently disappear. Local study-map skill 8.1 (Tool Implementation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Bounded local recovery reduces coordinator noise. Exhausted recovery should preserve attempts, partial results, and alternatives rather than silently disappear. In this case: Recover locally when permitted, then report unresolved failure with useful context.
- **B:** Incorrect for this question. An error contract should identify failure class, recoverability, and useful context. MCP isError marks an execution failure; it should not disguise a valid empty result. In this case: Recover locally when permitted, then report unresolved failure with useful context.
- **C:** Incorrect for this question. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. In this case: Recover locally when permitted, then report unresolved failure with useful context.
- **D:** Incorrect for this question. The coordinator needs failure type, attempted operation, useful outputs, and alternatives. A failure must not be disguised as a successful empty search. In this case: Recover locally when permitted, then report unresolved failure with useful context.

### Question 69 — D

Answer: Inspect conflicting routing instructions as well as tool descriptions. Routing instructions can conflict with otherwise accurate interface descriptions. System-prompt keywords can misroute requests even when tool contracts are reasonable. Diagnose both instruction and interface effects. Local study-map skill 8.1 (Tool Implementation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. In this case: Routing instructions can conflict with otherwise accurate interface descriptions.
- **B:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Routing instructions can conflict with otherwise accurate interface descriptions.
- **C:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Routing instructions can conflict with otherwise accurate interface descriptions.
- **D:** Correct. System-prompt keywords can misroute requests even when tool contracts are reasonable. Diagnose both instruction and interface effects. In this case: Routing instructions can conflict with otherwise accurate interface descriptions.

### Question 70 — C

Answer: Require authorized approval before the consequential action. An authorized approval tied to the current action must gate its external effect. Review must gate the external effect, be tied to the intended action, and use current authority. A later audit cannot reliably reverse a completed effect. Local study-map skill 8.1 (Tool Implementation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: An authorized approval tied to the current action must gate its external effect.
- **B:** Incorrect for this question. The recipient needs verified identifiers, completed work, unresolved issues, supporting evidence, and recommended actions, especially when the full transcript is unavailable. In this case: An authorized approval tied to the current action must gate its external effect.
- **C:** Correct. Review must gate the external effect, be tied to the intended action, and use current authority. A later audit cannot reliably reverse a completed effect. In this case: An authorized approval tied to the current action must gate its external effect.
- **D:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: An authorized approval tied to the current action must gate its external effect.

### Question 71 — A

Answer: Have an MCP client connect to the server and invoke permitted capabilities. The MCP client connects and invokes capabilities under the protocol and access rules. The client discovers and calls server-exposed capabilities under supported protocol and authorization. A model does not independently contact every backend without an integration. Local study-map skill 8.2 (MCP Server Development), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. The client discovers and calls server-exposed capabilities under supported protocol and authorization. A model does not independently contact every backend without an integration. In this case: The MCP client connects and invokes capabilities under the protocol and access rules.
- **B:** Incorrect for this question. MCP prompts package reusable interaction templates. They differ from resources providing content and tools executing operations. In this case: The MCP client connects and invokes capabilities under the protocol and access rules.
- **C:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: The MCP client connects and invokes capabilities under the protocol and access rules.
- **D:** Incorrect for this question. An MCP server exposes tools, resources, or prompts over supported transports and owns clear contracts. Reuse and security require deliberate deployment and permission design. In this case: The MCP client connects and invokes capabilities under the protocol and access rules.

### Question 72 — D

Answer: Implement a protocol-compatible server for approved capabilities. An MCP server defines and serves capabilities using supported protocol contracts. An MCP server exposes tools, resources, or prompts over supported transports and owns clear contracts. Reuse and security require deliberate deployment and permission design. Local study-map skill 8.2 (MCP Server Development), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: An MCP server defines and serves capabilities using supported protocol contracts.
- **B:** Incorrect for this question. Built-in tools can avoid unnecessary custom integration for supported local operations. They do not automatically reach arbitrary private services or bypass permissions. In this case: An MCP server defines and serves capabilities using supported protocol contracts.
- **C:** Incorrect for this question. A local function tool can fit the needs of one application without deploying an MCP service. Still define schemas, authorization, error behavior, and tests. In this case: An MCP server defines and serves capabilities using supported protocol contracts.
- **D:** Correct. An MCP server exposes tools, resources, or prompts over supported transports and owns clear contracts. Reuse and security require deliberate deployment and permission design. In this case: An MCP server defines and serves capabilities using supported protocol contracts.

### Question 73 — D

Answer: Expose a supported MCP resource catalog. Resources can present content and metadata separately from tool operations. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. Local study-map skill 8.2 (MCP Server Development), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Resources can present content and metadata separately from tool operations.
- **B:** Incorrect for this question. MCP prompts package reusable interaction templates. They differ from resources providing content and tools executing operations. In this case: Resources can present content and metadata separately from tool operations.
- **C:** Incorrect for this question. A local function tool can fit the needs of one application without deploying an MCP service. Still define schemas, authorization, error behavior, and tests. In this case: Resources can present content and metadata separately from tool operations.
- **D:** Correct. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Resources can present content and metadata separately from tool operations.

### Question 74 — A

Answer: Expose a reusable prompt template through MCP. Prompts package reusable interaction patterns rather than execute backend actions. MCP prompts package reusable interaction templates. They differ from resources providing content and tools executing operations. Local study-map skill 8.2 (MCP Server Development), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. MCP prompts package reusable interaction templates. They differ from resources providing content and tools executing operations. In this case: Prompts package reusable interaction patterns rather than execute backend actions.
- **B:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Prompts package reusable interaction patterns rather than execute backend actions.
- **C:** Incorrect for this question. A local function tool can fit the needs of one application without deploying an MCP service. Still define schemas, authorization, error behavior, and tests. In this case: Prompts package reusable interaction patterns rather than execute backend actions.
- **D:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Prompts package reusable interaction patterns rather than execute backend actions.

### Question 75 — B

Answer: Use stdio for a suitable local subprocess MCP connection. Keep stdio protocol messages separate from diagnostics such as stderr logging. Protocol messages use the standard streams defined by the transport. Keep diagnostic logging off protocol stdout so clients can parse messages reliably. Local study-map skill 8.2 (MCP Server Development), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Network deployment requires the protocol version, transport, authentication, TLS, and session handling to match. Do not assume arbitrary raw sockets are interchangeable with MCP. In this case: Keep stdio protocol messages separate from diagnostics such as stderr logging.
- **B:** Correct. Protocol messages use the standard streams defined by the transport. Keep diagnostic logging off protocol stdout so clients can parse messages reliably. In this case: Keep stdio protocol messages separate from diagnostics such as stderr logging.
- **C:** Incorrect for this question. WebSockets can fit bidirectional application communication, but the documented standard Messages streaming interface is SSE. Do not confuse a transport choice with model capability. In this case: Keep stdio protocol messages separate from diagnostics such as stderr logging.
- **D:** Incorrect for this question. A REST integration must respect its actual endpoint contract. HTTP 200 does not establish that the requested business operation succeeded semantically. In this case: Keep stdio protocol messages separate from diagnostics such as stderr logging.

### Question 76 — B

Answer: Use a supported network MCP transport with explicit authentication. Use the supported network MCP protocol and security contract rather than arbitrary sockets. Network deployment requires the protocol version, transport, authentication, TLS, and session handling to match. Do not assume arbitrary raw sockets are interchangeable with MCP. Local study-map skill 8.2 (MCP Server Development), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. The client discovers and calls server-exposed capabilities under supported protocol and authorization. A model does not independently contact every backend without an integration. In this case: Use the supported network MCP protocol and security contract rather than arbitrary sockets.
- **B:** Correct. Network deployment requires the protocol version, transport, authentication, TLS, and session handling to match. Do not assume arbitrary raw sockets are interchangeable with MCP. In this case: Use the supported network MCP protocol and security contract rather than arbitrary sockets.
- **C:** Incorrect for this question. Protocol messages use the standard streams defined by the transport. Keep diagnostic logging off protocol stdout so clients can parse messages reliably. In this case: Use the supported network MCP protocol and security contract rather than arbitrary sockets.
- **D:** Incorrect for this question. WebSockets can fit bidirectional application communication, but the documented standard Messages streaming interface is SSE. Do not confuse a transport choice with model capability. In this case: Use the supported network MCP protocol and security contract rather than arbitrary sockets.

### Question 77 — B

Answer: Check connected-server discovery and effective availability. Connection, discovery, approvals, and effective permissions determine usable capabilities. Configured servers can expose tools together when connected, but server failure, approval, filtering, and permissions can affect what is actually usable. Local study-map skill 8.2 (MCP Server Development), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Connection, discovery, approvals, and effective permissions determine usable capabilities.
- **B:** Correct. Configured servers can expose tools together when connected, but server failure, approval, filtering, and permissions can affect what is actually usable. In this case: Connection, discovery, approvals, and effective permissions determine usable capabilities.
- **C:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Connection, discovery, approvals, and effective permissions determine usable capabilities.
- **D:** Incorrect for this question. The client discovers and calls server-exposed capabilities under supported protocol and authorization. A model does not independently contact every backend without an integration. In this case: Connection, discovery, approvals, and effective permissions determine usable capabilities.

### Question 78 — C

Answer: Use project-scoped .mcp.json for shared server configuration. Project-scoped MCP configuration distributes shared setup without embedding actual secrets. Versioned project configuration can distribute team tooling. Keep real credentials outside Git and check approvals and environment requirements. Local study-map skill 8.2 (MCP Server Development), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. The guide describes user-scoped configuration in ~/.claude.json for personal tooling. Personal configuration is not automatically shared through the repository. In this case: Project-scoped MCP configuration distributes shared setup without embedding actual secrets.
- **B:** Incorrect for this question. Configured servers can expose tools together when connected, but server failure, approval, filtering, and permissions can affect what is actually usable. In this case: Project-scoped MCP configuration distributes shared setup without embedding actual secrets.
- **C:** Correct. Versioned project configuration can distribute team tooling. Keep real credentials outside Git and check approvals and environment requirements. In this case: Project-scoped MCP configuration distributes shared setup without embedding actual secrets.
- **D:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Project-scoped MCP configuration distributes shared setup without embedding actual secrets.

### Question 79 — A

Answer: Reference runtime environment variables instead of committing tokens. Reference approved runtime secret values rather than store literal credentials in Git. Environment expansion can keep literal secrets out of project files. Supply credentials through an approved secret path and protect logs as well. Local study-map skill 8.2 (MCP Server Development), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Environment expansion can keep literal secrets out of project files. Supply credentials through an approved secret path and protect logs as well. In this case: Reference approved runtime secret values rather than store literal credentials in Git.
- **B:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Reference approved runtime secret values rather than store literal credentials in Git.
- **C:** Incorrect for this question. Versioned project configuration can distribute team tooling. Keep real credentials outside Git and check approvals and environment requirements. In this case: Reference approved runtime secret values rather than store literal credentials in Git.
- **D:** Incorrect for this question. The guide describes user-scoped configuration in ~/.claude.json for personal tooling. Personal configuration is not automatically shared through the repository. In this case: Reference approved runtime secret values rather than store literal credentials in Git.

### Question 80 — D

Answer: Use user-scoped MCP configuration for personal servers. Personal server setup should remain user-scoped rather than alter shared project configuration. The guide describes user-scoped configuration in ~/.claude.json for personal tooling. Personal configuration is not automatically shared through the repository. Local study-map skill 8.2 (MCP Server Development), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Configured servers can expose tools together when connected, but server failure, approval, filtering, and permissions can affect what is actually usable. In this case: Personal server setup should remain user-scoped rather than alter shared project configuration.
- **B:** Incorrect for this question. Versioned project configuration can distribute team tooling. Keep real credentials outside Git and check approvals and environment requirements. In this case: Personal server setup should remain user-scoped rather than alter shared project configuration.
- **C:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Personal server setup should remain user-scoped rather than alter shared project configuration.
- **D:** Correct. The guide describes user-scoped configuration in ~/.claude.json for personal tooling. Personal configuration is not automatically shared through the repository. In this case: Personal server setup should remain user-scoped rather than alter shared project configuration.

### Question 81 — B

Answer: Define and validate a precise input schema. Discovery alone does not establish valid arguments, permissions, or business semantics. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. Local study-map skill 8.2 (MCP Server Development), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Discovery alone does not establish valid arguments, permissions, or business semantics.
- **B:** Correct. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. In this case: Discovery alone does not establish valid arguments, permissions, or business semantics.
- **C:** Incorrect for this question. An error contract should identify failure class, recoverability, and useful context. MCP isError marks an execution failure; it should not disguise a valid empty result. In this case: Discovery alone does not establish valid arguments, permissions, or business semantics.
- **D:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Discovery alone does not establish valid arguments, permissions, or business semantics.

### Question 82 — D

Answer: Return a structured tool error with category and retryability. Use the appropriate error signal and recoverability details instead of disguise failure. An error contract should identify failure class, recoverability, and useful context. MCP isError marks an execution failure; it should not disguise a valid empty result. Local study-map skill 8.2 (MCP Server Development), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Use the appropriate error signal and recoverability details instead of disguise failure.
- **B:** Incorrect for this question. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. In this case: Use the appropriate error signal and recoverability details instead of disguise failure.
- **C:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Use the appropriate error signal and recoverability details instead of disguise failure.
- **D:** Correct. An error contract should identify failure class, recoverability, and useful context. MCP isError marks an execution failure; it should not disguise a valid empty result. In this case: Use the appropriate error signal and recoverability details instead of disguise failure.

### Question 83 — C

Answer: Use stdio for a suitable local subprocess MCP connection. The connection follows stdio framing rather than require a network WebSocket channel. Protocol messages use the standard streams defined by the transport. Keep diagnostic logging off protocol stdout so clients can parse messages reliably. Local study-map skill 8.2 (MCP Server Development), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Network deployment requires the protocol version, transport, authentication, TLS, and session handling to match. Do not assume arbitrary raw sockets are interchangeable with MCP. In this case: The connection follows stdio framing rather than require a network WebSocket channel.
- **B:** Incorrect for this question. WebSockets can fit bidirectional application communication, but the documented standard Messages streaming interface is SSE. Do not confuse a transport choice with model capability. In this case: The connection follows stdio framing rather than require a network WebSocket channel.
- **C:** Correct. Protocol messages use the standard streams defined by the transport. Keep diagnostic logging off protocol stdout so clients can parse messages reliably. In this case: The connection follows stdio framing rather than require a network WebSocket channel.
- **D:** Incorrect for this question. A REST integration must respect its actual endpoint contract. HTTP 200 does not establish that the requested business operation succeeded semantically. In this case: The connection follows stdio framing rather than require a network WebSocket channel.

### Question 84 — A

Answer: Expose a supported MCP resource catalog. A resource catalog can provide metadata without pretending to execute the query. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. Local study-map skill 8.2 (MCP Server Development), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: A resource catalog can provide metadata without pretending to execute the query.
- **B:** Incorrect for this question. MCP prompts package reusable interaction templates. They differ from resources providing content and tools executing operations. In this case: A resource catalog can provide metadata without pretending to execute the query.
- **C:** Incorrect for this question. A local function tool can fit the needs of one application without deploying an MCP service. Still define schemas, authorization, error behavior, and tests. In this case: A resource catalog can provide metadata without pretending to execute the query.
- **D:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: A resource catalog can provide metadata without pretending to execute the query.

### Question 85 — C

Answer: Evaluate a maintained existing integration before writing a custom server. Evaluate the existing integration's security, maintenance, and fit before deciding to duplicate it. A suitable standard integration may reduce work. Assess security, permissions, maintenance, and requirements before adoption; custom tools remain appropriate for unique workflows. Local study-map skill 8.2 (MCP Server Development), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Built-in tools can avoid unnecessary custom integration for supported local operations. They do not automatically reach arbitrary private services or bypass permissions. In this case: Evaluate the existing integration's security, maintenance, and fit before deciding to duplicate it.
- **B:** Incorrect for this question. A local function tool can fit the needs of one application without deploying an MCP service. Still define schemas, authorization, error behavior, and tests. In this case: Evaluate the existing integration's security, maintenance, and fit before deciding to duplicate it.
- **C:** Correct. A suitable standard integration may reduce work. Assess security, permissions, maintenance, and requirements before adoption; custom tools remain appropriate for unique workflows. In this case: Evaluate the existing integration's security, maintenance, and fit before deciding to duplicate it.
- **D:** Incorrect for this question. An MCP server exposes tools, resources, or prompts over supported transports and owns clear contracts. Reuse and security require deliberate deployment and permission design. In this case: Evaluate the existing integration's security, maintenance, and fit before deciding to duplicate it.

### Question 86 — D

Answer: Use an existing built-in tool when its scope fits. A fitting built-in tool avoids unnecessary deployment and maintenance work. Built-in tools can avoid unnecessary custom integration for supported local operations. They do not automatically reach arbitrary private services or bypass permissions. Local study-map skill 8.3 (Agentic Customization), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. An MCP server exposes tools, resources, or prompts over supported transports and owns clear contracts. Reuse and security require deliberate deployment and permission design. In this case: A fitting built-in tool avoids unnecessary deployment and maintenance work.
- **B:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: A fitting built-in tool avoids unnecessary deployment and maintenance work.
- **C:** Incorrect for this question. A local function tool can fit the needs of one application without deploying an MCP service. Still define schemas, authorization, error behavior, and tests. In this case: A fitting built-in tool avoids unnecessary deployment and maintenance work.
- **D:** Correct. Built-in tools can avoid unnecessary custom integration for supported local operations. They do not automatically reach arbitrary private services or bypass permissions. In this case: A fitting built-in tool avoids unnecessary deployment and maintenance work.

### Question 87 — B

Answer: Put an on-demand workflow in a project skill. An on-demand skill can package task guidance without inventing an external API. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. Local study-map skill 8.3 (Agentic Customization), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. An MCP server exposes tools, resources, or prompts over supported transports and owns clear contracts. Reuse and security require deliberate deployment and permission design. In this case: An on-demand skill can package task guidance without inventing an external API.
- **B:** Correct. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: An on-demand skill can package task guidance without inventing an external API.
- **C:** Incorrect for this question. A local function tool can fit the needs of one application without deploying an MCP service. Still define schemas, authorization, error behavior, and tests. In this case: An on-demand skill can package task guidance without inventing an external API.
- **D:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: An on-demand skill can package task guidance without inventing an external API.

### Question 88 — A

Answer: Implement an application-local tool for a specific integration. An application-local custom tool can implement a focused operation with proper checks. A local function tool can fit the needs of one application without deploying an MCP service. Still define schemas, authorization, error behavior, and tests. Local study-map skill 8.3 (Agentic Customization), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. A local function tool can fit the needs of one application without deploying an MCP service. Still define schemas, authorization, error behavior, and tests. In this case: An application-local custom tool can implement a focused operation with proper checks.
- **B:** Incorrect for this question. Built-in tools can avoid unnecessary custom integration for supported local operations. They do not automatically reach arbitrary private services or bypass permissions. In this case: An application-local custom tool can implement a focused operation with proper checks.
- **C:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: An application-local custom tool can implement a focused operation with proper checks.
- **D:** Incorrect for this question. MCP prompts package reusable interaction templates. They differ from resources providing content and tools executing operations. In this case: An application-local custom tool can implement a focused operation with proper checks.

### Question 89 — D

Answer: Implement a protocol-compatible server for approved capabilities. An MCP server can serve approved capabilities through a separately maintained protocol boundary. An MCP server exposes tools, resources, or prompts over supported transports and owns clear contracts. Reuse and security require deliberate deployment and permission design. Local study-map skill 8.3 (Agentic Customization), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: An MCP server can serve approved capabilities through a separately maintained protocol boundary.
- **B:** Incorrect for this question. Built-in tools can avoid unnecessary custom integration for supported local operations. They do not automatically reach arbitrary private services or bypass permissions. In this case: An MCP server can serve approved capabilities through a separately maintained protocol boundary.
- **C:** Incorrect for this question. MCP prompts package reusable interaction templates. They differ from resources providing content and tools executing operations. In this case: An MCP server can serve approved capabilities through a separately maintained protocol boundary.
- **D:** Correct. An MCP server exposes tools, resources, or prompts over supported transports and owns clear contracts. Reuse and security require deliberate deployment and permission design. In this case: An MCP server can serve approved capabilities through a separately maintained protocol boundary.

### Question 90 — C

Answer: Expose a supported MCP resource catalog. Use a resource for inspectable content rather than model it as an unrelated action. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. Local study-map skill 8.3 (Agentic Customization), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. A local function tool can fit the needs of one application without deploying an MCP service. Still define schemas, authorization, error behavior, and tests. In this case: Use a resource for inspectable content rather than model it as an unrelated action.
- **B:** Incorrect for this question. MCP prompts package reusable interaction templates. They differ from resources providing content and tools executing operations. In this case: Use a resource for inspectable content rather than model it as an unrelated action.
- **C:** Correct. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Use a resource for inspectable content rather than model it as an unrelated action.
- **D:** Incorrect for this question. Built-in tools can avoid unnecessary custom integration for supported local operations. They do not automatically reach arbitrary private services or bypass permissions. In this case: Use a resource for inspectable content rather than model it as an unrelated action.

### Question 91 — C

Answer: Expose a reusable prompt template through MCP. MCP prompts represent templates, distinct from resources and executing tools. MCP prompts package reusable interaction templates. They differ from resources providing content and tools executing operations. Local study-map skill 8.3 (Agentic Customization), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: MCP prompts represent templates, distinct from resources and executing tools.
- **B:** Incorrect for this question. A local function tool can fit the needs of one application without deploying an MCP service. Still define schemas, authorization, error behavior, and tests. In this case: MCP prompts represent templates, distinct from resources and executing tools.
- **C:** Correct. MCP prompts package reusable interaction templates. They differ from resources providing content and tools executing operations. In this case: MCP prompts represent templates, distinct from resources and executing tools.
- **D:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: MCP prompts represent templates, distinct from resources and executing tools.

### Question 92 — C

Answer: Use Grep for content-pattern searches. Grep searches text patterns rather than merely matching file paths. Content search finds symbols, strings, and imports inside files. It is distinct from matching filenames and paths. Local study-map skill 8.3 (Agentic Customization), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Glob discovers files by path patterns rather than searching their contents. It can identify candidates for later reading. In this case: Grep searches text patterns rather than merely matching file paths.
- **B:** Incorrect for this question. Command execution fits tests, builds, and similar tasks when authorized. It is more powerful than file search and needs explicit safety and runtime controls. In this case: Grep searches text patterns rather than merely matching file paths.
- **C:** Correct. Content search finds symbols, strings, and imports inside files. It is distinct from matching filenames and paths. In this case: Grep searches text patterns rather than merely matching file paths.
- **D:** Incorrect for this question. Inspecting current contents supplies evidence and reliable anchors before modification. A filename search alone does not reveal implementation behavior. In this case: Grep searches text patterns rather than merely matching file paths.

### Question 93 — D

Answer: Use Glob for filename or path-pattern discovery. Glob discovers paths before any content-specific inspection is possible. Glob discovers files by path patterns rather than searching their contents. It can identify candidates for later reading. Local study-map skill 8.3 (Agentic Customization), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Content search finds symbols, strings, and imports inside files. It is distinct from matching filenames and paths. In this case: Glob discovers paths before any content-specific inspection is possible.
- **B:** Incorrect for this question. Targeted replacement is suitable when current text can be identified uniquely. Ambiguous anchors can change the wrong location or fail. In this case: Glob discovers paths before any content-specific inspection is possible.
- **C:** Incorrect for this question. Inspecting current contents supplies evidence and reliable anchors before modification. A filename search alone does not reveal implementation behavior. In this case: Glob discovers paths before any content-specific inspection is possible.
- **D:** Correct. Glob discovers files by path patterns rather than searching their contents. It can identify candidates for later reading. In this case: Glob discovers paths before any content-specific inspection is possible.

### Question 94 — A

Answer: Use Read to inspect current file contents. Read current contents instead of edit from an obsolete or guessed snapshot. Inspecting current contents supplies evidence and reliable anchors before modification. A filename search alone does not reveal implementation behavior. Local study-map skill 8.3 (Agentic Customization), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Inspecting current contents supplies evidence and reliable anchors before modification. A filename search alone does not reveal implementation behavior. In this case: Read current contents instead of edit from an obsolete or guessed snapshot.
- **B:** Incorrect for this question. A full-file replacement can resolve ambiguous targeted edits, but must preserve unrelated content and account for concurrent changes. In this case: Read current contents instead of edit from an obsolete or guessed snapshot.
- **C:** Incorrect for this question. Command execution fits tests, builds, and similar tasks when authorized. It is more powerful than file search and needs explicit safety and runtime controls. In this case: Read current contents instead of edit from an obsolete or guessed snapshot.
- **D:** Incorrect for this question. Targeted replacement is suitable when current text can be identified uniquely. Ambiguous anchors can change the wrong location or fail. In this case: Read current contents instead of edit from an obsolete or guessed snapshot.

### Question 95 — B

Answer: Use Edit with a verified unique anchor. An anchored edit avoids unnecessary full-file replacement when the location is unambiguous. Targeted replacement is suitable when current text can be identified uniquely. Ambiguous anchors can change the wrong location or fail. Local study-map skill 8.3 (Agentic Customization), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Command execution fits tests, builds, and similar tasks when authorized. It is more powerful than file search and needs explicit safety and runtime controls. In this case: An anchored edit avoids unnecessary full-file replacement when the location is unambiguous.
- **B:** Correct. Targeted replacement is suitable when current text can be identified uniquely. Ambiguous anchors can change the wrong location or fail. In this case: An anchored edit avoids unnecessary full-file replacement when the location is unambiguous.
- **C:** Incorrect for this question. A full-file replacement can resolve ambiguous targeted edits, but must preserve unrelated content and account for concurrent changes. In this case: An anchored edit avoids unnecessary full-file replacement when the location is unambiguous.
- **D:** Incorrect for this question. Inspecting current contents supplies evidence and reliable anchors before modification. A filename search alone does not reveal implementation behavior. In this case: An anchored edit avoids unnecessary full-file replacement when the location is unambiguous.

### Question 96 — A

Answer: Read the current file and write a checked replacement. Read and construct a validated full replacement when a unique anchor is unavailable. A full-file replacement can resolve ambiguous targeted edits, but must preserve unrelated content and account for concurrent changes. Local study-map skill 8.3 (Agentic Customization), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. A full-file replacement can resolve ambiguous targeted edits, but must preserve unrelated content and account for concurrent changes. In this case: Read and construct a validated full replacement when a unique anchor is unavailable.
- **B:** Incorrect for this question. Content search finds symbols, strings, and imports inside files. It is distinct from matching filenames and paths. In this case: Read and construct a validated full replacement when a unique anchor is unavailable.
- **C:** Incorrect for this question. Targeted replacement is suitable when current text can be identified uniquely. Ambiguous anchors can change the wrong location or fail. In this case: Read and construct a validated full replacement when a unique anchor is unavailable.
- **D:** Incorrect for this question. Glob discovers files by path patterns rather than searching their contents. It can identify candidates for later reading. In this case: Read and construct a validated full replacement when a unique anchor is unavailable.

### Question 97 — B

Answer: Use Bash for an authorized command with bounded execution. Command execution differs from searching names or reading source content. Command execution fits tests, builds, and similar tasks when authorized. It is more powerful than file search and needs explicit safety and runtime controls. Local study-map skill 8.3 (Agentic Customization), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Inspecting current contents supplies evidence and reliable anchors before modification. A filename search alone does not reveal implementation behavior. In this case: Command execution differs from searching names or reading source content.
- **B:** Correct. Command execution fits tests, builds, and similar tasks when authorized. It is more powerful than file search and needs explicit safety and runtime controls. In this case: Command execution differs from searching names or reading source content.
- **C:** Incorrect for this question. Glob discovers files by path patterns rather than searching their contents. It can identify candidates for later reading. In this case: Command execution differs from searching names or reading source content.
- **D:** Incorrect for this question. Content search finds symbols, strings, and imports inside files. It is distinct from matching filenames and paths. In this case: Command execution differs from searching names or reading source content.

### Question 98 — C

Answer: Give each specialist only task-relevant tools. Keep available capabilities aligned with actual responsibilities and permissions. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. Local study-map skill 8.3 (Agentic Customization), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. A generic interface can be split when its unrelated responsibilities cause ambiguity. Do not multiply near-identical tools without a meaningful boundary. In this case: Keep available capabilities aligned with actual responsibilities and permissions.
- **B:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Keep available capabilities aligned with actual responsibilities and permissions.
- **C:** Correct. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Keep available capabilities aligned with actual responsibilities and permissions.
- **D:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Keep available capabilities aligned with actual responsibilities and permissions.

### Question 99 — D

Answer: Version and review plugin dependencies and permissions. Version, review, and constrain executable dependencies and their permissions. Plugins can change tools and workflow behavior. Track provenance, versions, compatibility, and permissions rather than install unreviewed code merely because a model suggests it. Local study-map skill 8.3 (Agentic Customization), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: Version, review, and constrain executable dependencies and their permissions.
- **B:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Version, review, and constrain executable dependencies and their permissions.
- **C:** Incorrect for this question. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: Version, review, and constrain executable dependencies and their permissions.
- **D:** Correct. Plugins can change tools and workflow behavior. Track provenance, versions, compatibility, and permissions rather than install unreviewed code merely because a model suggests it. In this case: Version, review, and constrain executable dependencies and their permissions.

### Question 100 — D

Answer: Translate business goals into measurable functional and operational requirements. Actual capability, reuse, deployment, and security requirements matter more than novelty. Specify behavior, latency, throughput, data constraints, failure policy, and acceptance criteria. A model or framework choice is not a substitute for requirements. Local study-map skill 8.3 (Agentic Customization), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. In this case: Actual capability, reuse, deployment, and security requirements matter more than novelty.
- **B:** Incorrect for this question. Self-hosting and managed deployment place different responsibilities on operations, networking, identity, and lifecycle. Availability and supported features must be verified. In this case: Actual capability, reuse, deployment, and security requirements matter more than novelty.
- **C:** Incorrect for this question. Evaluate state graphs, typed validation, tracing, ecosystem, and deployment fit across frameworks such as LangGraph, Strands, or PydanticAI. A framework does not guarantee safety or correctness. In this case: Actual capability, reuse, deployment, and security requirements matter more than novelty.
- **D:** Correct. Specify behavior, latency, throughput, data constraints, failure policy, and acceptance criteria. A model or framework choice is not a substitute for requirements. In this case: Actual capability, reuse, deployment, and security requirements matter more than novelty.
