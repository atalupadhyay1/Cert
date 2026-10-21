# Claude Certified Developer – Foundations (CCDV-F) — Practice Set 6

Integrated Developer Scenarios and Final Review

100 questions · Suggested practice duration: 200 minutes · Practice target: 80%

Tests 1–5 are focused learning tests. Test 6 is an expanded blueprint-proportioned review, not an official exam replica. Related concepts recur.

Select ONE best answer for every question. Answer key follows all questions.

Original educational content, not actual, recalled, or copied Anthropic exam items.

## Questions

### 1. A stateless model answers using current context without updating its training parameters. What remains fixed during ordinary inference?

Domain: Model Selection and Optimization

- A. Persist structured task state and pending actions
- B. Supply the relevant conversation state on subsequent requests
- C. Retrieve application-managed memory into later context
- D. Distinguish fixed inference parameters from supplied context

### 2. A developer assumes using an SDK means the vendor hosts the team's worker infrastructure. What must be decided separately?

Domain: Agents and Workflows

- A. Choose execution hosting and operational ownership explicitly
- B. Separate environment configuration from application logic
- C. Use distinct least-privilege workload identities
- D. Pin compatible model, SDK, prompt, and dependency versions

### 3. A separate custom application channel requires bidirectional persistent messaging. What transport may fit?

Domain: Model Selection and Optimization

- A. Use WebSockets for an explicitly bidirectional persistent channel
- B. Apply HTTP method, status, authentication, and payload contracts
- C. Consume the Messages stream as server-sent events
- D. Use asynchronous I/O with bounded concurrency

### 4. An object passes schema validation but assigns evidence to the wrong entity. What check remains necessary?

Domain: Prompt and Context Engineering

- A. Validate extracted values against evidence and business rules
- B. Use supported strict structured output with a schema
- C. Allow explicit unknown or absent values in the schema
- D. Specify deterministic normalization rules and preserve originals when needed

### 5. A supported model offers a control for how much reasoning work it invests. What control should be evaluated?

Domain: Model Selection and Optimization

- A. Set a supported maximum generated-output length
- B. Adjust sampling variability, not factual truth
- C. Evaluate supported reasoning effort controls
- D. Evaluate supported fast inference mode

### 6. User-provided attachment text is presented as if it were trusted application policy. What boundary should be corrected?

Domain: Applications and Integration

- A. Separate instructions and source data with explicit labels
- B. Treat retrieved instructions as untrusted source content
- C. Place trusted application policy in the supported system instruction field
- D. Apply requester permissions before evidence enters model context

### 7. A mock always returns ideal JSON and misses a provider adapter defect. What test should be added?

Domain: Eval, Testing, and Debugging

- A. Use controlled stubs for repeatable failure-path tests
- B. Use a versioned representative held-out evaluation set
- C. Use tests and specific failure feedback to drive iteration
- D. Test the integration contract at the provider boundary

### 8. An engineering team wants supported agent orchestration features rather than write every loop primitive itself. What should it evaluate?

Domain: Agents and Workflows

- A. Evaluate the supported Claude Agent SDK
- B. Apply HTTP method, status, authentication, and payload contracts
- C. Implement a custom Messages-based agent harness
- D. Choose a framework for needed orchestration semantics

### 9. Two similarly named tools are misselected because their descriptions omit boundaries. What should improve first?

Domain: Tools and MCPs

- A. Give each specialist only task-relevant tools
- B. Separate genuinely different tasks into clearly bounded tools
- C. Inspect conflicting routing instructions as well as tool descriptions
- D. Clarify tool purpose, inputs, outputs, and boundaries

### 10. A framework must recover a graph execution at an explicit completed stage. What state facility should be assessed?

Domain: Agents and Workflows

- A. Supply the relevant conversation state on subsequent requests
- B. Persist structured task state and pending actions
- C. Resume the identified session when its context remains valid
- D. Checkpoint durable state at safe workflow boundaries

### 11. An attached file asks the assistant to change its approved operational authority. What trust treatment applies?

Domain: Security and Safety

- A. Treat retrieved instructions as untrusted source content
- B. Place trusted application policy in the supported system instruction field
- C. Apply requester permissions before evidence enters model context
- D. Separate instructions and source data with explicit labels

### 12. A supported host needs an on-demand procedural workflow using existing capabilities. What extension may fit?

Domain: Tools and MCPs

- A. Put an on-demand workflow in a project skill
- B. Expose a supported MCP resource catalog
- C. Use a project-scoped custom slash command
- D. Use project-scoped .mcp.json for shared server configuration

### 13. A tool may mutate production state, but the policy requires checking the current environment first. Where should enforcement occur?

Domain: Agents and Workflows

- A. Require authorized approval before the consequential action
- B. Normalize tool observations before model consumption
- C. Use pre-execution tool interception for blocking policy checks
- D. Enforce task, iteration, and spending safeguards

### 14. A team considers only initial coding and ignores maintenance and retirement. What broader practice is required?

Domain: Applications and Integration

- A. Plan deployment, operation, maintenance, and retirement
- B. Use a versioned representative held-out evaluation set
- C. Manage release approval and rollback boundaries
- D. Canary a version change with regression gates and rollback

### 15. A source-supported amount was assigned to the wrong field. What repair input helps?

Domain: Prompt and Context Engineering

- A. Specify deterministic normalization rules and preserve originals when needed
- B. Retry with the document, failed result, and specific validation errors
- C. Use supported strict structured output with a schema
- D. Mark missing evidence and route for retrieval or review

### 16. An authenticated employee requests an action beyond the current account's permissions. What trusted check is required?

Domain: Security and Safety

- A. Authenticate the calling identity
- B. Authorize the current identity for the actual target and action
- C. Define and validate a precise input schema
- D. Use supported strict structured output with a schema

### 17. A narrow reading specialist is given unrelated mutation tools. What principle should narrow its capabilities?

Domain: Security and Safety

- A. Expose a supported MCP resource catalog
- B. Clarify tool purpose, inputs, outputs, and boundaries
- C. Give each specialist only task-relevant tools
- D. Check connected-server discovery and effective availability

### 18. A team needs ongoing evidence of latency, failures, and task outcomes after launch. What capability is needed?

Domain: Applications and Integration

- A. Use a versioned representative held-out evaluation set
- B. Inspect a redacted end-to-end request and tool trace
- C. Propagate correlation identifiers across requests and tools
- D. Monitor production service and outcome signals

### 19. Nobody owns escalation when model evidence is inadequate. What operating requirement is missing?

Domain: Applications and Integration

- A. Identify affected users and accountable stakeholders
- B. Assign operational owners and escalation responsibilities
- C. Translate business goals into measurable functional and operational requirements
- D. Plan deployment, operation, maintenance, and retirement

### 20. A stateless service must keep different users' conversations separate. What application concern must be designed?

Domain: Applications and Integration

- A. Design explicit user and conversation session boundaries
- B. Pass relevant evidence and constraints explicitly
- C. Persist structured task state and pending actions
- D. Supply the relevant conversation state on subsequent requests

### 21. Tool arguments need types, required fields, and allowed values. What contract should define these?

Domain: Tools and MCPs

- A. Use supported strict structured output with a schema
- B. Define and validate a precise input schema
- C. Clarify tool purpose, inputs, outputs, and boundaries
- D. Expose a constrained domain-specific operation

### 22. A third-party cloud exposes a Claude model with a different authentication and deployment contract. What must integration verify?

Domain: Applications and Integration

- A. Pin compatible model, SDK, prompt, and dependency versions
- B. Verify the actual hosting provider contract
- C. Separate environment configuration from application logic
- D. Apply HTTP method, status, authentication, and payload contracts

### 23. A backend credential is placed in model-readable instructions for convenience. Where should it be managed?

Domain: Security and Safety

- A. Manage credentials in protected execution infrastructure
- B. Reference runtime environment variables instead of committing tokens
- C. Separate environment configuration from application logic
- D. Keep protected action and identity audit records

### 24. A failure investigation discovers new hypotheses after each observation. What architecture fits that uncertainty?

Domain: Agents and Workflows

- A. Wait for validated prerequisite outputs
- B. Run independent branches concurrently and join checked results
- C. Map the problem and revise subtasks as evidence emerges
- D. Use a predictable sequence of specialized stages

### 25. A task needs a model to inspect an image through a supported input mechanism. What capability should be assessed?

Domain: Applications and Integration

- A. Use supported token counting before oversized submission
- B. Send supported image content in the documented multimodal format
- C. Build a valid Messages API request with explicit content blocks
- D. Dispatch response content according to each block type

### 26. A proposed workflow shifts an approval responsibility, but the accountable operator was never consulted. What discovery is missing?

Domain: Applications and Integration

- A. Assign operational owners and escalation responsibilities
- B. Identify affected users and accountable stakeholders
- C. Define observable acceptance criteria for required outcomes
- D. Translate business goals into measurable functional and operational requirements

### 27. A local MCP process communicates through standard input and output. What transport style is this?

Domain: Tools and MCPs

- A. Use stdio for a suitable local subprocess MCP connection
- B. Use a supported network MCP transport with explicit authentication
- C. Consume the Messages stream as server-sent events
- D. Use WebSockets for an explicitly bidirectional persistent channel

### 28. A deployed assistant begins causing confirmed harmful side effects. What coordinated process should start?

Domain: Applications and Integration

- A. Keep protected action and identity audit records
- B. Inspect a redacted end-to-end request and tool trace
- C. Activate coordinated incident response and recovery
- D. Monitor production service and outcome signals

### 29. A final recommendation must use the result of an eligibility check performed first. What ordering is required?

Domain: Agents and Workflows

- A. Run independent branches concurrently and join checked results
- B. Wait for validated prerequisite outputs
- C. Map the problem and revise subtasks as evidence emerges
- D. Route coordination through an orchestrator

### 30. Incoming tasks outpace downstream capacity and memory grows without bound. What flow control is needed?

Domain: Applications and Integration

- A. Use asynchronous I/O with bounded concurrency
- B. Run independent branches concurrently and join checked results
- C. Bound work queues and apply backpressure
- D. Enforce task, iteration, and spending safeguards

### 31. A summary weakens an exact regulatory deadline into a vague date phrase. What persistence should protect it?

Domain: Prompt and Context Engineering

- A. Present key findings early and organize supporting details
- B. Preserve exact transactional facts outside lossy summaries
- C. Supply the relevant conversation state on subsequent requests
- D. Compact context while preserving checked facts and open issues

### 32. An extraction task lacks the requested fact in all approved evidence. What schema design avoids compelled guessing?

Domain: Prompt and Context Engineering

- A. Specify deterministic normalization rules and preserve originals when needed
- B. Use an extensible category plus a detail field
- C. Allow explicit unknown or absent values in the schema
- D. Use supported strict structured output with a schema

### 33. A pinned model has a scheduled retirement date. What lifecycle work is needed?

Domain: Model Selection and Optimization

- A. Plan a tested migration before model or API retirement
- B. Pin compatible model, SDK, prompt, and dependency versions
- C. Verify the actual hosting provider contract
- D. Select the least costly configuration that meets required outcomes

### 34. A team needs complete control over Messages calls, tool dispatch, and custom stopping logic. Which implementation fits?

Domain: Agents and Workflows

- A. Choose a framework for needed orchestration semantics
- B. Evaluate the supported Claude Agent SDK
- C. Use a predefined deterministic orchestration workflow
- D. Implement a custom Messages-based agent harness

### 35. A post-tool adapter standardizes units before model consumption. What responsibility should remain truthful?

Domain: Security and Safety

- A. Use pre-execution tool interception for blocking policy checks
- B. Require authorized approval before the consequential action
- C. Enforce prerequisites in trusted execution code
- D. Normalize tool observations before model consumption

### 36. A production credential is exposed in a diagnostic record. What response must go beyond redaction?

Domain: Security and Safety

- A. Manage credentials in protected execution infrastructure
- B. Keep protected action and identity audit records
- C. Revoke exposed credentials and investigate their use
- D. Activate coordinated incident response and recovery

### 37. A valid response object is sent directly to an interpreter. What final consumer boundary remains?

Domain: Applications and Integration

- A. Adjust sampling variability, not factual truth
- B. Treat model output as untrusted before rendering or execution
- C. Use supported strict structured output with a schema
- D. Validate extracted values against evidence and business rules

### 38. An automated worker escalates a partially completed task to a person. What packet should be prepared?

Domain: Agents and Workflows

- A. Persist structured task state and pending actions
- B. Supply the relevant conversation state on subsequent requests
- C. Pass relevant evidence and constraints explicitly
- D. Create a structured handoff with facts, status, and next actions

### 39. A tool input arrives in fragments with invalid JSON until the block completes. What should the client do?

Domain: Applications and Integration

- A. Treat end_turn as the end of the current assistant turn
- B. Accumulate deltas by block index before final validation
- C. Handle errors after streaming has already begun
- D. Handle the output limit as an incomplete response

### 40. A budget estimator assumes each word equals exactly one model input unit. What underlying concept should correct it?

Domain: Model Selection and Optimization

- A. Use supported token counting before oversized submission
- B. Count tokens with model-compatible accounting
- C. Track actual usage by token and billing category
- D. Budget instructions, evidence, history, and generation together

### 41. A custom API caller needs trusted behavioral instructions separate from user turns. Where should they be placed?

Domain: Applications and Integration

- A. Build a valid Messages API request with explicit content blocks
- B. Place trusted application policy in the supported system instruction field
- C. Put shared project standards in versioned CLAUDE.md
- D. Put personal cross-project preferences in ~/.claude/CLAUDE.md

### 42. An integration is ready for limited exposure before broad rollout. What release technique fits?

Domain: Applications and Integration

- A. Canary a version change with regression gates and rollback
- B. Use a versioned representative held-out evaluation set
- C. Pin compatible model, SDK, prompt, and dependency versions
- D. Manage release approval and rollback boundaries

### 43. A public ranking favors one family, but the application has strict domain-specific acceptance criteria. What should choose the model?

Domain: Model Selection and Optimization

- A. Evaluate Sonnet for a measured balance of capability and efficiency
- B. Select the least costly configuration that meets required outcomes
- C. Evaluate Haiku for suitable speed- and efficiency-oriented tasks
- D. Evaluate Opus for demanding capability-oriented work

### 44. A review instruction asks for 'important' findings without defining reportable categories. What should be added?

Domain: Prompt and Context Engineering

- A. Include valid examples that should not be flagged
- B. Define severity using impact and concrete examples
- C. State explicit reportable and non-reportable criteria
- D. Use representative few-shot examples with boundaries

### 45. A team reports cache savings without checking actual cache-read and write behavior. What evidence is missing?

Domain: Model Selection and Optimization

- A. Track actual usage by token and billing category
- B. Put eligible stable common content before variable input for cache reuse
- C. Use supported prompt-prefix caching for eligible repeated input
- D. Verify cache reads, writes, and economics in actual usage

### 46. A fresh specialist does not know a restriction stated only in the coordinator's context. What must be supplied?

Domain: Prompt and Context Engineering

- A. Pass relevant evidence and constraints explicitly
- B. Configure the subagent description, prompt, and tool scope
- C. Enable the version-appropriate subagent invocation tool
- D. Supply the relevant conversation state on subsequent requests

### 47. A correct answer is unusable because it targets experts rather than new operators. What should be clarified?

Domain: Prompt and Context Engineering

- A. Specify task, audience, constraints, and output expectations
- B. Assign a relevant role or perspective in the prompt
- C. Set a supported maximum generated-output length
- D. Use representative few-shot examples with boundaries

### 48. An agent explores indefinitely despite no new useful evidence. What operating limit is needed?

Domain: Agents and Workflows

- A. Require authorized approval before the consequential action
- B. Persist structured task state and pending actions
- C. Enforce prerequisites in trusted execution code
- D. Enforce task, iteration, and spending safeguards

### 49. An API app must transmit user and assistant conversation content through the documented request contract. What structure fits?

Domain: Applications and Integration

- A. Apply HTTP method, status, authentication, and payload contracts
- B. Build a valid Messages API request with explicit content blocks
- C. Place trusted application policy in the supported system instruction field
- D. Dispatch response content according to each block type

### 50. An integration drops a valid response field before storage. What error boundary should be isolated?

Domain: Eval, Testing, and Debugging

- A. Inspect a redacted end-to-end request and tool trace
- B. State explicit reportable and non-reportable criteria
- C. Use a versioned representative held-out evaluation set
- D. Isolate model-output defects from integration defects

### 51. A user needs an interactive assistant, while another product needs programmatic backend calls. What application choice should be explicit?

Domain: Applications and Integration

- A. Apply HTTP method, status, authentication, and payload contracts
- B. Verify the actual hosting provider contract
- C. Evaluate the supported Claude Agent SDK
- D. Select the Claude interface appropriate to the workflow

### 52. A team wants reviewed shared MCP server configuration without committing credentials. What scope is relevant?

Domain: Tools and MCPs

- A. Use project-scoped .mcp.json for shared server configuration
- B. Use user-scoped MCP configuration for personal servers
- C. Check connected-server discovery and effective availability
- D. Reference runtime environment variables instead of committing tokens

### 53. A provider event stream reports failure after an initially successful HTTP response. What path must the client handle?

Domain: Eval, Testing, and Debugging

- A. Use the final assembled message and completion status
- B. Treat end_turn as the end of the current assistant turn
- C. Handle errors after streaming has already begun
- D. Handle the output limit as an incomplete response

### 54. A high-throughput producer overwhelms a bounded downstream dependency. What control should coordinate rates?

Domain: Model Selection and Optimization

- A. Bound work queues and apply backpressure
- B. Enforce task, iteration, and spending safeguards
- C. Use asynchronous I/O with bounded concurrency
- D. Run independent branches concurrently and join checked results

### 55. After completion, the service reports actual billed token categories. What should cost reconciliation inspect?

Domain: Model Selection and Optimization

- A. Track actual usage by token and billing category
- B. Use supported token counting before oversized submission
- C. Compare total cost per verified successful outcome
- D. Measure end-to-end response latency

### 56. A challenging reasoning workload misses quality targets on evaluated cheaper candidates. Which family may merit an evidence-based trial?

Domain: Model Selection and Optimization

- A. Evaluate Sonnet for a measured balance of capability and efficiency
- B. Evaluate Opus for demanding capability-oriented work
- C. Use supported thinking or effort controls after measuring task benefit
- D. Evaluate Haiku for suitable speed- and efficiency-oriented tasks

### 57. A deployment needs approval gates and a defined way back to the prior stable version. What plan fits?

Domain: Applications and Integration

- A. Pin compatible model, SDK, prompt, and dependency versions
- B. Version exact prompt content and its dependencies
- C. Separate environment configuration from application logic
- D. Manage release approval and rollback boundaries

### 58. The team needs reviewed executable permission configuration rather than only natural-language standards. What artifact type is relevant?

Domain: Applications and Integration

- A. Use the appropriate settings.json scope for behavioral configuration
- B. Put personal cross-project preferences in ~/.claude/CLAUDE.md
- C. Organize focused conventions in .claude/rules/
- D. Put shared project standards in versioned CLAUDE.md

### 59. A backend sends an HTTP request with JSON to a documented resource endpoint. What integration style is being used?

Domain: Model Selection and Optimization

- A. Apply HTTP method, status, authentication, and payload contracts
- B. Consume the Messages stream as server-sent events
- C. Use asynchronous I/O with bounded concurrency
- D. Use WebSockets for an explicitly bidirectional persistent channel

### 60. Identical inputs produce different plausible completions. What model behavior explains this?

Domain: Model Selection and Optimization

- A. Use supported thinking or effort controls after measuring task benefit
- B. Evaluate supported reasoning effort controls
- C. Adjust sampling variability, not factual truth
- D. Account for probabilistic generation and output variability

### 61. Independent market checks have no shared mutable state and all are needed before synthesis. How can work be arranged?

Domain: Agents and Workflows

- A. Map the problem and revise subtasks as evidence emerges
- B. Wait for validated prerequisite outputs
- C. Run independent branches concurrently and join checked results
- D. Use a shared multi-agent working context

### 62. A compliance preparation job always checks documents, extracts fields, validates them, and drafts a summary in that order. What architecture best fits?

Domain: Agents and Workflows

- A. Use a predictable sequence of specialized stages
- B. Route coordination through an orchestrator
- C. Map the problem and revise subtasks as evidence emerges
- D. Run independent branches concurrently and join checked results

### 63. A worker repeatedly returns irrelevant diagnostic payloads that crowd useful evidence. What upstream change helps?

Domain: Prompt and Context Engineering

- A. Preserve exact transactional facts outside lossy summaries
- B. Reduce tool output to relevant fields with provenance
- C. Present key findings early and organize supporting details
- D. Compact context while preserving checked facts and open issues

### 64. A deployment uses only a language-based refusal instruction as a control. What security approach is needed?

Domain: Security and Safety

- A. Apply content-level safety detection and moderation
- B. Layer prevention, detection, approval, and recovery controls
- C. Require authorized approval before the consequential action
- D. Enforce prerequisites in trusted execution code

### 65. A test convention applies to matching filenames throughout a monorepo. What scope follows that file role?

Domain: Claude Code

- A. Use directory-scoped CLAUDE.md for a local package
- B. Put shared project standards in versioned CLAUDE.md
- C. Scope a rule with YAML paths glob patterns
- D. Put personal cross-project preferences in ~/.claude/CLAUDE.md

### 66. A standard streaming Messages consumer needs the provider's documented event transport. What should it use?

Domain: Applications and Integration

- A. Apply HTTP method, status, authentication, and payload contracts
- B. Use WebSockets for an explicitly bidirectional persistent channel
- C. Consume the Messages stream as server-sent events
- D. Use asynchronous I/O with bounded concurrency

### 67. A new action could have material regulatory consequences. What requirements activity should identify needed controls?

Domain: Applications and Integration

- A. Translate business goals into measurable functional and operational requirements
- B. Identify affected users and accountable stakeholders
- C. Assess impact, data, authority, and misuse risks before deployment
- D. Assign operational owners and escalation responsibilities

### 68. An application retrieves stored preferences into a later session. What is supplying continuity?

Domain: Agents and Workflows

- A. Supply the relevant conversation state on subsequent requests
- B. Use supported prompt-prefix caching for eligible repeated input
- C. Retrieve application-managed memory into later context
- D. Persist structured task state and pending actions

### 69. A generated change is about to enter a shared codebase. What engineering review should remain?

Domain: Applications and Integration

- A. Use tests and specific failure feedback to drive iteration
- B. Track source changes with version control
- C. Refactor internal structure while preserving required behavior
- D. Review generated changes as ordinary production code

### 70. A write may finish remotely before the response disappears. What can prevent repeated logical effects where supported?

Domain: Applications and Integration

- A. Cancel local work and reconcile any external operation separately
- B. Use a durable idempotency key for the same logical action
- C. Validate and commit business changes through a controlled boundary
- D. Set explicit deadlines and classify timeout outcomes

### 71. A broad moving model reference changes behavior unexpectedly. What selection practice improves reproducibility?

Domain: Applications and Integration

- A. Version and review plugin dependencies and permissions
- B. Version exact prompt content and its dependencies
- C. Separate environment configuration from application logic
- D. Pin compatible model, SDK, prompt, and dependency versions

### 72. A summary preserves conclusions but loses the passages supporting them. What linkage must survive?

Domain: Prompt and Context Engineering

- A. Preserve collection and publication dates with claims
- B. Represent credible disagreement with attributed values
- C. Preserve claim-to-source mappings through every handoff
- D. Use representations suited to the content type

### 73. Two deployments behave differently because their effective settings and dependencies differ. What should be governed?

Domain: Applications and Integration

- A. Version and review plugin dependencies and permissions
- B. Pin compatible model, SDK, prompt, and dependency versions
- C. Separate environment configuration from application logic
- D. Version exact prompt content and its dependencies

### 74. A prompt includes several representative labeled demonstrations. What instructional pattern is this?

Domain: Model Selection and Optimization

- A. Assign a relevant role or perspective in the prompt
- B. Use representative few-shot examples with boundaries
- C. Provide one representative demonstration
- D. Provide a task instruction without demonstrations

### 75. A team adopts an extension that adds behavior and tools to a supported host. What dependency needs review?

Domain: Applications and Integration

- A. Version and review plugin dependencies and permissions
- B. Expose a supported MCP resource catalog
- C. Put an on-demand workflow in a project skill
- D. Choose a framework for needed orchestration semantics

### 76. A prompt revision causes a regression, but its prior text was not saved. What management practice is needed?

Domain: Prompt and Context Engineering

- A. Version exact prompt content and its dependencies
- B. Use a versioned representative held-out evaluation set
- C. Separate environment configuration from application logic
- D. Pin compatible model, SDK, prompt, and dependency versions

### 77. An efficiency-oriented model passes every required test on a simple routing task. Which family is a suitable candidate to keep evaluating?

Domain: Model Selection and Optimization

- A. Use supported thinking or effort controls after measuring task benefit
- B. Evaluate Haiku for suitable speed- and efficiency-oriented tasks
- C. Evaluate Opus for demanding capability-oriented work
- D. Evaluate Sonnet for a measured balance of capability and efficiency

### 78. A developer obtains a coroutine but never awaits or schedules it. What programming contract was missed?

Domain: Model Selection and Optimization

- A. Wait for validated prerequisite outputs
- B. Apply HTTP method, status, authentication, and payload contracts
- C. Run independent branches concurrently and join checked results
- D. Use asynchronous I/O with bounded concurrency

### 79. A handler notices forbidden file writes only after they complete. What enforcement stage is needed?

Domain: Security and Safety

- A. Normalize tool observations before model consumption
- B. Keep protected action and identity audit records
- C. Monitor production service and outcome signals
- D. Use pre-execution tool interception for blocking policy checks

### 80. An MCP server exposes a supported document catalog for clients to inspect. What primitive fits content access?

Domain: Tools and MCPs

- A. Expose a supported MCP resource catalog
- B. Expose a reusable prompt template through MCP
- C. Define and validate a precise input schema
- D. Clarify tool purpose, inputs, outputs, and boundaries

### 81. A library wraps low-level requests but does not eliminate provider constraints. What integration abstraction is this?

Domain: Model Selection and Optimization

- A. Evaluate the supported Claude Agent SDK
- B. Apply HTTP method, status, authentication, and payload contracts
- C. Use an SDK wrapper over the provider request contract
- D. Verify the actual hosting provider contract

### 82. A custom tool needs the application to execute its implementation and return observations. What execution category fits?

Domain: Tools and MCPs

- A. Expose a supported MCP resource catalog
- B. Use a supported provider-executed server tool
- C. Execute a client-defined tool through the application harness
- D. Expose a reusable prompt template through MCP

### 83. A maintained integration may meet a required external-service connection without bespoke implementation. What should be assessed first?

Domain: Tools and MCPs

- A. Implement a custom Messages-based agent harness
- B. Expose a supported MCP resource catalog
- C. Evaluate a maintained existing integration before writing a custom server
- D. Choose a framework for needed orchestration semantics

### 84. A cheaper request produces many more unusable results. What cost measure better represents business efficiency?

Domain: Model Selection and Optimization

- A. Use supported token counting before oversized submission
- B. Compare total cost per verified successful outcome
- C. Track actual usage by token and billing category
- D. Verify cache reads, writes, and economics in actual usage

### 85. A client tool completes, but the agent cannot continue because its result is not correlated to the request. What should be returned?

Domain: Agents and Workflows

- A. Use the final assembled message and completion status
- B. Inspect stop_reason and dispatch the appropriate branch
- C. Treat end_turn as the end of the current assistant turn
- D. Append the assistant tool-use blocks and matching tool results

### 86. A backend consumer needs consistent machine-readable result shape. What design capability should be evaluated?

Domain: Applications and Integration

- A. Allow explicit unknown or absent values in the schema
- B. Specify deterministic normalization rules and preserve originals when needed
- C. Use supported strict structured output with a schema
- D. Validate extracted values against evidence and business rules

### 87. Prompt edits ship independently of code, making regressions hard to trace. What artifact needs a version?

Domain: Applications and Integration

- A. Separate environment configuration from application logic
- B. Version and review plugin dependencies and permissions
- C. Pin compatible model, SDK, prompt, and dependency versions
- D. Version exact prompt content and its dependencies

### 88. A developer reorganizes internal code while intending to preserve behavior. What engineering activity is this?

Domain: Applications and Integration

- A. Plan deployment, operation, maintenance, and retirement
- B. Review generated changes as ordinary production code
- C. Track source changes with version control
- D. Refactor internal structure while preserving required behavior

### 89. A team chooses an interface before clarifying what users need accomplished. What should be established first?

Domain: Applications and Integration

- A. Define observable acceptance criteria for required outcomes
- B. Identify affected users and accountable stakeholders
- C. Define observable service-level objectives and failure behavior
- D. Translate business goals into measurable functional and operational requirements

### 90. A server must handle concurrent I/O without blocking its event loop on every call. What implementation pattern fits?

Domain: Applications and Integration

- A. Use asynchronous I/O with bounded concurrency
- B. Run independent branches concurrently and join checked results
- C. Wait for validated prerequisite outputs
- D. Apply HTTP method, status, authentication, and payload contracts

### 91. A team is comparing Strands, LangGraph, and PydanticAI for orchestration. What kind of decision is this?

Domain: Agents and Workflows

- A. Evaluate the supported Claude Agent SDK
- B. Choose a framework for needed orchestration semantics
- C. Apply HTTP method, status, authentication, and payload contracts
- D. Implement a custom Messages-based agent harness

### 92. A large overnight analysis is flexible in completion time and should use an eligible asynchronous processing service. What mode fits?

Domain: Applications and Integration

- A. Use Message Batches for latency-tolerant independent requests
- B. Use a synchronous interactive request path
- C. Use asynchronous I/O with bounded concurrency
- D. Run independent branches concurrently and join checked results

### 93. A reviewer flags legitimate exceptions because demonstrations include only faults. What examples should be added?

Domain: Prompt and Context Engineering

- A. State explicit reportable and non-reportable criteria
- B. Provide concrete input–output examples
- C. Include valid examples that should not be flagged
- D. Use representative few-shot examples with boundaries

### 94. The product needs a measurable availability and response-time objective. What requirement captures this?

Domain: Applications and Integration

- A. Compare total cost per verified successful outcome
- B. Define observable acceptance criteria for required outcomes
- C. Measure end-to-end response latency
- D. Define observable service-level objectives and failure behavior

### 95. A provider's supported built-in tool executes within the provider service rather than the custom client harness. What category fits?

Domain: Tools and MCPs

- A. Expose a reusable prompt template through MCP
- B. Execute a client-defined tool through the application harness
- C. Expose a supported MCP resource catalog
- D. Use a supported provider-executed server tool

### 96. An automated job should finish without interactive questioning. Which invocation mode fits?

Domain: Claude Code

- A. Use supported JSON output and schema CLI options
- B. Use a project-scoped custom slash command
- C. Use plan mode to investigate and compare approaches
- D. Run Claude Code in non-interactive print mode

### 97. Users say the assistant should be 'good enough,' with no checkable outcomes. What should be defined?

Domain: Applications and Integration

- A. Use a versioned representative held-out evaluation set
- B. Define observable acceptance criteria for required outcomes
- C. Translate business goals into measurable functional and operational requirements
- D. Define observable service-level objectives and failure behavior

### 98. Several specialists need one owner to reconcile conflicts and decide next steps. What topology fits?

Domain: Agents and Workflows

- A. Run independent branches concurrently and join checked results
- B. Use a shared multi-agent working context
- C. Route coordination through an orchestrator
- D. Run specialists with separately scoped working contexts

### 99. A project relies on a build command described only in one contributor's private instructions. What sharing scope should be used?

Domain: Claude Code

- A. Use directory-scoped CLAUDE.md for a local package
- B. Put personal cross-project preferences in ~/.claude/CLAUDE.md
- C. Put shared project standards in versioned CLAUDE.md
- D. Put an on-demand workflow in a project skill

### 100. An MCP integration provides a reusable interaction template distinct from data and callable operations. What primitive fits?

Domain: Tools and MCPs

- A. Clarify tool purpose, inputs, outputs, and boundaries
- B. Define and validate a precise input schema
- C. Expose a reusable prompt template through MCP
- D. Expose a supported MCP resource catalog

---

## Answer key and explanations

### Question 1 — D

Answer: Distinguish fixed inference parameters from supplied context. In-context adaptation differs from automatically changing the model's learned weights. Ordinary in-context examples and current messages do not automatically update the learned model parameters. Application memory is separate from training. Local study-map skill 5.1 (LLM Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: In-context adaptation differs from automatically changing the model's learned weights.
- **B:** Incorrect for this question. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. In this case: In-context adaptation differs from automatically changing the model's learned weights.
- **C:** Incorrect for this question. Persisted preferences or facts can be selected and supplied to later requests. That continuity is external state management rather than automatic updates to model training weights. In this case: In-context adaptation differs from automatically changing the model's learned weights.
- **D:** Correct. Ordinary in-context examples and current messages do not automatically update the learned model parameters. Application memory is separate from training. In this case: In-context adaptation differs from automatically changing the model's learned weights.

### Question 2 — A

Answer: Choose execution hosting and operational ownership explicitly. Execution hosting and operational ownership are deployment choices, not consequences of importing a library. An imported SDK does not determine who hosts workers, manages infrastructure, or handles operations. Assess actual hosted and self-hosted deployment contracts separately. Local study-map skill 1.2 (Agent Construction with Claude), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Correct. An imported SDK does not determine who hosts workers, manages infrastructure, or handles operations. Assess actual hosted and self-hosted deployment contracts separately. In this case: Execution hosting and operational ownership are deployment choices, not consequences of importing a library.
- **B:** Incorrect for this question. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: Execution hosting and operational ownership are deployment choices, not consequences of importing a library.
- **C:** Incorrect for this question. Separate workload identities constrain unnecessary shared authority and improve attribution. Verify granted permissions and credential handling for each operational role. In this case: Execution hosting and operational ownership are deployment choices, not consequences of importing a library.
- **D:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Execution hosting and operational ownership are deployment choices, not consequences of importing a library.

### Question 3 — A

Answer: Use WebSockets for an explicitly bidirectional persistent channel. WebSockets support bidirectional application communication unlike one-way server-sent event delivery. WebSockets can fit bidirectional application communication, but the documented standard Messages streaming interface is SSE. Do not confuse a transport choice with model capability. Local study-map skill 5.2 (Technical Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Correct. WebSockets can fit bidirectional application communication, but the documented standard Messages streaming interface is SSE. Do not confuse a transport choice with model capability. In this case: WebSockets support bidirectional application communication unlike one-way server-sent event delivery.
- **B:** Incorrect for this question. A REST integration must respect its actual endpoint contract. HTTP 200 does not establish that the requested business operation succeeded semantically. In this case: WebSockets support bidirectional application communication unlike one-way server-sent event delivery.
- **C:** Incorrect for this question. The documented streaming interface emits SSE events over HTTP. It is not inherently a WebSocket connection or one valid JSON object per arbitrary network chunk. In this case: WebSockets support bidirectional application communication unlike one-way server-sent event delivery.
- **D:** Incorrect for this question. Await network operations without blocking an event loop, while limiting in-flight work and respecting service capacity. Creating a coroutine does not mean it has run. In this case: WebSockets support bidirectional application communication unlike one-way server-sent event delivery.

### Question 4 — A

Answer: Validate extracted values against evidence and business rules. Semantic validation must verify values, relationships, and source support. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Correct. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Semantic validation must verify values, relationships, and source support.
- **B:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Semantic validation must verify values, relationships, and source support.
- **C:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Semantic validation must verify values, relationships, and source support.
- **D:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Semantic validation must verify values, relationships, and source support.

### Question 5 — C

Answer: Evaluate supported reasoning effort controls. Use documented effort behavior and compare quality, latency, and cost rather than treat it as a temperature synonym. Effort settings influence supported reasoning behavior under a particular model contract. They are not synonyms for sampling temperature or guarantees of correctness. Local study-map skill 5.1 (LLM Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. An output ceiling bounds generation subject to model accounting. It does not itself expand input context or guarantee that a complete response fits. In this case: Use documented effort behavior and compare quality, latency, and cost rather than treat it as a temperature synonym.
- **B:** Incorrect for this question. Temperature changes next-token sampling behavior where supported. Lowering it does not independently guarantee correct extraction, grounding, or identical execution. In this case: Use documented effort behavior and compare quality, latency, and cost rather than treat it as a temperature synonym.
- **C:** Correct. Effort settings influence supported reasoning behavior under a particular model contract. They are not synonyms for sampling temperature or guarantees of correctness. In this case: Use documented effort behavior and compare quality, latency, and cost rather than treat it as a temperature synonym.
- **D:** Incorrect for this question. Fast-mode availability, pricing, and behavior depend on the selected service and model. Measure its latency and cost impact instead of assume it changes model capability, output length, or reasoning effort in a universal way. In this case: Use documented effort behavior and compare quality, latency, and cost rather than treat it as a temperature synonym.

### Question 6 — B

Answer: Treat retrieved instructions as untrusted source content. External content must remain data rather than become authoritative instruction. External pages and tool observations must not acquire trusted instruction authority. Pair separation with trusted tool authorization; delimiters alone are insufficient. Local study-map skill 2.5 (Claude Application Design), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Delimiters improve clarity about source boundaries but are not a security barrier or a grant of authority to the enclosed content. In this case: External content must remain data rather than become authoritative instruction.
- **B:** Correct. External pages and tool observations must not acquire trusted instruction authority. Pair separation with trusted tool authorization; delimiters alone are insufficient. In this case: External content must remain data rather than become authoritative instruction.
- **C:** Incorrect for this question. Keep trusted instructions separate from user and retrieved data. On the direct Messages API, system instructions use the top-level system parameter rather than a system-role entry in messages. In this case: External content must remain data rather than become authoritative instruction.
- **D:** Incorrect for this question. Data access must be authorized externally. Retrieved content being internal or relevant does not justify showing it to every user. In this case: External content must remain data rather than become authoritative instruction.

### Question 7 — D

Answer: Test the integration contract at the provider boundary. Check real request and response contract preservation at the integration boundary. Check serialized requests, content blocks, status handling, and representative responses. Mock success alone may not reveal a malformed real request or unsupported provider feature. Local study-map skill 4.1 (Debugging and Error Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/streaming

- **A:** Incorrect for this question. Inject timeouts, malformed responses, and provider failures without live side effects. Combine with contract and representative integration tests rather than infer complete correctness from mocks. In this case: Check real request and response contract preservation at the integration boundary.
- **B:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Check real request and response contract preservation at the integration boundary.
- **C:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Check real request and response contract preservation at the integration boundary.
- **D:** Correct. Check serialized requests, content blocks, status handling, and representative responses. Mock success alone may not reveal a malformed real request or unsupported provider feature. In this case: Check real request and response contract preservation at the integration boundary.

### Question 8 — A

Answer: Evaluate the supported Claude Agent SDK. A supported Agent SDK can supply capabilities subject to version and deployment constraints. An agent SDK can provide supported orchestration capabilities while still requiring version-aware deployment, permissions, monitoring, and application controls. Local study-map skill 1.2 (Agent Construction with Claude), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Correct. An agent SDK can provide supported orchestration capabilities while still requiring version-aware deployment, permissions, monitoring, and application controls. In this case: A supported Agent SDK can supply capabilities subject to version and deployment constraints.
- **B:** Incorrect for this question. A REST integration must respect its actual endpoint contract. HTTP 200 does not establish that the requested business operation succeeded semantically. In this case: A supported Agent SDK can supply capabilities subject to version and deployment constraints.
- **C:** Incorrect for this question. A custom harness gives the application direct control over requests, tool dispatch, stopping, state, and recovery. The application owns the resulting protocol and operational responsibilities. In this case: A supported Agent SDK can supply capabilities subject to version and deployment constraints.
- **D:** Incorrect for this question. Evaluate state graphs, typed validation, tracing, ecosystem, and deployment fit across frameworks such as LangGraph, Strands, or PydanticAI. A framework does not guarantee safety or correctness. In this case: A supported Agent SDK can supply capabilities subject to version and deployment constraints.

### Question 9 — D

Answer: Clarify tool purpose, inputs, outputs, and boundaries. Explain when each tool applies, including purpose, inputs, outputs, and distinctions. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. Local study-map skill 8.1 (Tool Implementation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Explain when each tool applies, including purpose, inputs, outputs, and distinctions.
- **B:** Incorrect for this question. A generic interface can be split when its unrelated responsibilities cause ambiguity. Do not multiply near-identical tools without a meaningful boundary. In this case: Explain when each tool applies, including purpose, inputs, outputs, and distinctions.
- **C:** Incorrect for this question. System-prompt keywords can misroute requests even when tool contracts are reasonable. Diagnose both instruction and interface effects. In this case: Explain when each tool applies, including purpose, inputs, outputs, and distinctions.
- **D:** Correct. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Explain when each tool applies, including purpose, inputs, outputs, and distinctions.

### Question 10 — D

Answer: Checkpoint durable state at safe workflow boundaries. Supported checkpointing records execution progress but does not automatically roll back external effects. Recovery needs committed progress, pending actions, evidence versions, and consistent artifacts. Checkpointing conversation text alone does not establish transaction completion. Local study-map skill 1.3 (Agent Patterns and Frameworks), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. In this case: Supported checkpointing records execution progress but does not automatically roll back external effects.
- **B:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Supported checkpointing records execution progress but does not automatically roll back external effects.
- **C:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Supported checkpointing records execution progress but does not automatically roll back external effects.
- **D:** Correct. Recovery needs committed progress, pending actions, evidence versions, and consistent artifacts. Checkpointing conversation text alone does not establish transaction completion. In this case: Supported checkpointing records execution progress but does not automatically roll back external effects.

### Question 11 — A

Answer: Treat retrieved instructions as untrusted source content. External content is data and cannot grant new instruction or execution privileges. External pages and tool observations must not acquire trusted instruction authority. Pair separation with trusted tool authorization; delimiters alone are insufficient. Local study-map skill 7.1 (AI Application Security), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Correct. External pages and tool observations must not acquire trusted instruction authority. Pair separation with trusted tool authorization; delimiters alone are insufficient. In this case: External content is data and cannot grant new instruction or execution privileges.
- **B:** Incorrect for this question. Keep trusted instructions separate from user and retrieved data. On the direct Messages API, system instructions use the top-level system parameter rather than a system-role entry in messages. In this case: External content is data and cannot grant new instruction or execution privileges.
- **C:** Incorrect for this question. Data access must be authorized externally. Retrieved content being internal or relevant does not justify showing it to every user. In this case: External content is data and cannot grant new instruction or execution privileges.
- **D:** Incorrect for this question. Delimiters improve clarity about source boundaries but are not a security barrier or a grant of authority to the enclosed content. In this case: External content is data and cannot grant new instruction or execution privileges.

### Question 12 — A

Answer: Put an on-demand workflow in a project skill. Skills package task instructions and context rather than necessarily add a new external service. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. Local study-map skill 8.3 (Agentic Customization), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: Skills package task instructions and context rather than necessarily add a new external service.
- **B:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Skills package task instructions and context rather than necessarily add a new external service.
- **C:** Incorrect for this question. The guide describes .claude/commands/ for shared invocable commands. User-scoped commands are personal; feature details depend on Claude Code version. In this case: Skills package task instructions and context rather than necessarily add a new external service.
- **D:** Incorrect for this question. Versioned project configuration can distribute team tooling. Keep real credentials outside Git and check approvals and environment requirements. In this case: Skills package task instructions and context rather than necessarily add a new external service.

### Question 13 — C

Answer: Use pre-execution tool interception for blocking policy checks. A pre-execution control must validate the real action before an external effect. An appropriate pre-tool hook or equivalent trusted gate can deny a disallowed action before it runs. Hook implementation and failure handling must be tested. Local study-map skill 1.2 (Agent Construction with Claude), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. Review must gate the external effect, be tied to the intended action, and use current authority. A later audit cannot reliably reverse a completed effect. In this case: A pre-execution control must validate the real action before an external effect.
- **B:** Incorrect for this question. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. In this case: A pre-execution control must validate the real action before an external effect.
- **C:** Correct. An appropriate pre-tool hook or equivalent trusted gate can deny a disallowed action before it runs. Hook implementation and failure handling must be tested. In this case: A pre-execution control must validate the real action before an external effect.
- **D:** Incorrect for this question. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. In this case: A pre-execution control must validate the real action before an external effect.

### Question 14 — A

Answer: Plan deployment, operation, maintenance, and retirement. Manage requirements through deployment, monitoring, change, and decommissioning. Development does not end at a successful API call. Include monitoring, updates, recovery, ownership, and decommissioning in the system lifecycle. Local study-map skill 2.2 (Systems Life Cycle), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Correct. Development does not end at a successful API call. Include monitoring, updates, recovery, ownership, and decommissioning in the system lifecycle. In this case: Manage requirements through deployment, monitoring, change, and decommissioning.
- **B:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Manage requirements through deployment, monitoring, change, and decommissioning.
- **C:** Incorrect for this question. Record the deployable configuration, approval gates, and a practical known-good recovery path. Deployment is an operational change rather than just a successful local build. In this case: Manage requirements through deployment, monitoring, change, and decommissioning.
- **D:** Incorrect for this question. Stage exposure to the new configuration, compare required outcomes, and retain a known-good path. A vendor release note is not workload validation. In this case: Manage requirements through deployment, monitoring, change, and decommissioning.

### Question 15 — B

Answer: Retry with the document, failed result, and specific validation errors. Send source evidence, the failed result, and exact validation feedback within a bounded retry policy. Actionable feedback supports correction when evidence exists. Bound attempts and validate the revised result rather than resubmit the same vague request indefinitely. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Send source evidence, the failed result, and exact validation feedback within a bounded retry policy.
- **B:** Correct. Actionable feedback supports correction when evidence exists. Bound attempts and validate the revised result rather than resubmit the same vague request indefinitely. In this case: Send source evidence, the failed result, and exact validation feedback within a bounded retry policy.
- **C:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Send source evidence, the failed result, and exact validation feedback within a bounded retry policy.
- **D:** Incorrect for this question. Retries cannot recover a fact that the available document never contained. Use unknown status, authorized retrieval, clarification, or review instead of fabrication. In this case: Send source evidence, the failed result, and exact validation feedback within a bounded retry policy.

### Question 16 — B

Answer: Authorize the current identity for the actual target and action. Authorize the specific action and resource independently of login and schema validity. Permission must be enforced in trusted code using current resource and business state. A valid login, JSON schema, or model proposal alone does not grant authority. Local study-map skill 7.1 (AI Application Security), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. Authentication establishes who is calling. Authorization separately decides what that identity may do to a particular resource. In this case: Authorize the specific action and resource independently of login and schema validity.
- **B:** Correct. Permission must be enforced in trusted code using current resource and business state. A valid login, JSON schema, or model proposal alone does not grant authority. In this case: Authorize the specific action and resource independently of login and schema validity.
- **C:** Incorrect for this question. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. In this case: Authorize the specific action and resource independently of login and schema validity.
- **D:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Authorize the specific action and resource independently of login and schema validity.

### Question 17 — C

Answer: Give each specialist only task-relevant tools. Task-relevant tools reduce unnecessary authority and selection ambiguity. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. Local study-map skill 7.2 (Guardrails and Safe Deployment), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Task-relevant tools reduce unnecessary authority and selection ambiguity.
- **B:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Task-relevant tools reduce unnecessary authority and selection ambiguity.
- **C:** Correct. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Task-relevant tools reduce unnecessary authority and selection ambiguity.
- **D:** Incorrect for this question. Configured servers can expose tools together when connected, but server failure, approval, filtering, and permissions can affect what is actually usable. In this case: Task-relevant tools reduce unnecessary authority and selection ambiguity.

### Question 18 — D

Answer: Monitor production service and outcome signals. Production monitoring tracks operation beyond one-time offline evaluation. Observe deployed latency, failures, drift, and task outcomes with accountable response thresholds. Monitoring differs from an offline evaluation or a single diagnostic trace. Local study-map skill 2.2 (Systems Life Cycle), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Production monitoring tracks operation beyond one-time offline evaluation.
- **B:** Incorrect for this question. Correlate the actual request, model response, tool execution, retries, and validation results. Diagnose the first failing boundary rather than infer cause from the final prose. In this case: Production monitoring tracks operation beyond one-time offline evaluation.
- **C:** Incorrect for this question. Link a user task to provider requests, worker runs, and actions without using sensitive content as an identifier. Protect telemetry access and retention. In this case: Production monitoring tracks operation beyond one-time offline evaluation.
- **D:** Correct. Observe deployed latency, failures, drift, and task outcomes with accountable response thresholds. Monitoring differs from an offline evaluation or a single diagnostic trace. In this case: Production monitoring tracks operation beyond one-time offline evaluation.

### Question 19 — B

Answer: Assign operational owners and escalation responsibilities. Assign accountable owners and recovery paths instead of leave unresolved cases unhandled. Define who handles uncertain results, incidents, updates, and recovery. A model cannot substitute for accountable organizational responsibility. Local study-map skill 2.1 (Understanding Requirements), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Consult people who use, operate, approve, or are materially affected by a workflow. Requirements should reflect real responsibilities rather than assumptions made by implementers alone. In this case: Assign accountable owners and recovery paths instead of leave unresolved cases unhandled.
- **B:** Correct. Define who handles uncertain results, incidents, updates, and recovery. A model cannot substitute for accountable organizational responsibility. In this case: Assign accountable owners and recovery paths instead of leave unresolved cases unhandled.
- **C:** Incorrect for this question. Specify behavior, latency, throughput, data constraints, failure policy, and acceptance criteria. A model or framework choice is not a substitute for requirements. In this case: Assign accountable owners and recovery paths instead of leave unresolved cases unhandled.
- **D:** Incorrect for this question. Development does not end at a successful API call. Include monitoring, updates, recovery, ownership, and decommissioning in the system lifecycle. In this case: Assign accountable owners and recovery paths instead of leave unresolved cases unhandled.

### Question 20 — A

Answer: Design explicit user and conversation session boundaries. Session boundaries and explicit state prevent accidental cross-user contamination. Keep relevant history and state associated with the correct user and task. Stateless model calls do not automatically maintain safe cross-user conversation persistence. Local study-map skill 2.5 (Claude Application Design), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Correct. Keep relevant history and state associated with the correct user and task. Stateless model calls do not automatically maintain safe cross-user conversation persistence. In this case: Session boundaries and explicit state prevent accidental cross-user contamination.
- **B:** Incorrect for this question. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Session boundaries and explicit state prevent accidental cross-user contamination.
- **C:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Session boundaries and explicit state prevent accidental cross-user contamination.
- **D:** Incorrect for this question. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. In this case: Session boundaries and explicit state prevent accidental cross-user contamination.

### Question 21 — B

Answer: Define and validate a precise input schema. A precise input schema supports validation while authorization and semantics remain separate. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. Local study-map skill 8.1 (Tool Implementation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: A precise input schema supports validation while authorization and semantics remain separate.
- **B:** Correct. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. In this case: A precise input schema supports validation while authorization and semantics remain separate.
- **C:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: A precise input schema supports validation while authorization and semantics remain separate.
- **D:** Incorrect for this question. A narrow operation can enforce permitted sources, destinations, or actions more reliably than a general arbitrary-command or unrestricted-fetch interface. In this case: A precise input schema supports validation while authorization and semantics remain separate.

### Question 22 — B

Answer: Verify the actual hosting provider contract. Use the actual provider's capabilities and policies instead of assume every direct-API feature is identical. Check endpoints, authentication, model identifiers, capabilities, data terms, and feature support for the selected provider. Shared model branding does not guarantee identical APIs or policies. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Use the actual provider's capabilities and policies instead of assume every direct-API feature is identical.
- **B:** Correct. Check endpoints, authentication, model identifiers, capabilities, data terms, and feature support for the selected provider. Shared model branding does not guarantee identical APIs or policies. In this case: Use the actual provider's capabilities and policies instead of assume every direct-API feature is identical.
- **C:** Incorrect for this question. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: Use the actual provider's capabilities and policies instead of assume every direct-API feature is identical.
- **D:** Incorrect for this question. A REST integration must respect its actual endpoint contract. HTTP 200 does not establish that the requested business operation succeeded semantically. In this case: Use the actual provider's capabilities and policies instead of assume every direct-API feature is identical.

### Question 23 — A

Answer: Manage credentials in protected execution infrastructure. Use protected execution infrastructure and avoid model-visible secrets and sensitive telemetry. Keep credentials out of prompts, repositories, generated output, and unprotected logs. Supply narrowly scoped credentials through approved runtime secret mechanisms. Local study-map skill 7.4 (Identity, Secrets, and Key Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Correct. Keep credentials out of prompts, repositories, generated output, and unprotected logs. Supply narrowly scoped credentials through approved runtime secret mechanisms. In this case: Use protected execution infrastructure and avoid model-visible secrets and sensitive telemetry.
- **B:** Incorrect for this question. Environment expansion can keep literal secrets out of project files. Supply credentials through an approved secret path and protect logs as well. In this case: Use protected execution infrastructure and avoid model-visible secrets and sensitive telemetry.
- **C:** Incorrect for this question. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: Use protected execution infrastructure and avoid model-visible secrets and sensitive telemetry.
- **D:** Incorrect for this question. Audit records support attribution and reconstruction of consequential actions. Limit access, sensitive content, and retention; they do not themselves block an effect. In this case: Use protected execution infrastructure and avoid model-visible secrets and sensitive telemetry.

### Question 24 — C

Answer: Map the problem and revise subtasks as evidence emerges. Adaptive planning can revise subtasks as evidence changes instead of force every path upfront. Open-ended investigation benefits from exploration, prioritized hypotheses, and revised decomposition rather than an exhaustive fixed script chosen before evidence. Local study-map skill 1.1 (Agent Architecture), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: Adaptive planning can revise subtasks as evidence changes instead of force every path upfront.
- **B:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Adaptive planning can revise subtasks as evidence changes instead of force every path upfront.
- **C:** Correct. Open-ended investigation benefits from exploration, prioritized hypotheses, and revised decomposition rather than an exhaustive fixed script chosen before evidence. In this case: Adaptive planning can revise subtasks as evidence changes instead of force every path upfront.
- **D:** Incorrect for this question. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: Adaptive planning can revise subtasks as evidence changes instead of force every path upfront.

### Question 25 — B

Answer: Send supported image content in the documented multimodal format. Verify image support, media format, sizing, and provider constraints for the selected configuration. Image understanding requires an actual supported image block or source, a compatible model, and valid media limits. A text filename alone does not provide image pixels. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. A token-count endpoint or compatible estimator can help plan requests. Include hidden overhead allowed by the documented interface and verify actual usage afterward. In this case: Verify image support, media format, sizing, and provider constraints for the selected configuration.
- **B:** Correct. Image understanding requires an actual supported image block or source, a compatible model, and valid media limits. A text filename alone does not provide image pixels. In this case: Verify image support, media format, sizing, and provider constraints for the selected configuration.
- **C:** Incorrect for this question. Use the selected API contract for model, instructions, messages, and typed content. Do not assume a consumer chat interface and a developer API share implicit state. In this case: Verify image support, media format, sizing, and provider constraints for the selected configuration.
- **D:** Incorrect for this question. A response can contain text, tool use, thinking, or other supported blocks. Do not assume content is one string or that the first block is always displayable text. In this case: Verify image support, media format, sizing, and provider constraints for the selected configuration.

### Question 26 — B

Answer: Identify affected users and accountable stakeholders. Identify affected owners and users so the design reflects real responsibilities. Consult people who use, operate, approve, or are materially affected by a workflow. Requirements should reflect real responsibilities rather than assumptions made by implementers alone. Local study-map skill 2.1 (Understanding Requirements), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Define who handles uncertain results, incidents, updates, and recovery. A model cannot substitute for accountable organizational responsibility. In this case: Identify affected owners and users so the design reflects real responsibilities.
- **B:** Correct. Consult people who use, operate, approve, or are materially affected by a workflow. Requirements should reflect real responsibilities rather than assumptions made by implementers alone. In this case: Identify affected owners and users so the design reflects real responsibilities.
- **C:** Incorrect for this question. Checkable success and failure conditions make a proposed behavior evaluable. Generic quality adjectives and technology choices do not establish acceptable results. In this case: Identify affected owners and users so the design reflects real responsibilities.
- **D:** Incorrect for this question. Specify behavior, latency, throughput, data constraints, failure policy, and acceptance criteria. A model or framework choice is not a substitute for requirements. In this case: Identify affected owners and users so the design reflects real responsibilities.

### Question 27 — A

Answer: Use stdio for a suitable local subprocess MCP connection. Use the supported local standard-I/O contract and keep diagnostics from corrupting protocol output. Protocol messages use the standard streams defined by the transport. Keep diagnostic logging off protocol stdout so clients can parse messages reliably. Local study-map skill 8.2 (MCP Server Development), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Protocol messages use the standard streams defined by the transport. Keep diagnostic logging off protocol stdout so clients can parse messages reliably. In this case: Use the supported local standard-I/O contract and keep diagnostics from corrupting protocol output.
- **B:** Incorrect for this question. Network deployment requires the protocol version, transport, authentication, TLS, and session handling to match. Do not assume arbitrary raw sockets are interchangeable with MCP. In this case: Use the supported local standard-I/O contract and keep diagnostics from corrupting protocol output.
- **C:** Incorrect for this question. The documented streaming interface emits SSE events over HTTP. It is not inherently a WebSocket connection or one valid JSON object per arbitrary network chunk. In this case: Use the supported local standard-I/O contract and keep diagnostics from corrupting protocol output.
- **D:** Incorrect for this question. WebSockets can fit bidirectional application communication, but the documented standard Messages streaming interface is SSE. Do not confuse a transport choice with model capability. In this case: Use the supported local standard-I/O contract and keep diagnostics from corrupting protocol output.

### Question 28 — C

Answer: Activate coordinated incident response and recovery. Containment, investigation, and recovery require explicit incident management. Contain verified harm, investigate affected systems and data, recover safely, and communicate through accountable owners. Observation alone is not containment. Local study-map skill 2.2 (Systems Life Cycle), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Audit records support attribution and reconstruction of consequential actions. Limit access, sensitive content, and retention; they do not themselves block an effect. In this case: Containment, investigation, and recovery require explicit incident management.
- **B:** Incorrect for this question. Correlate the actual request, model response, tool execution, retries, and validation results. Diagnose the first failing boundary rather than infer cause from the final prose. In this case: Containment, investigation, and recovery require explicit incident management.
- **C:** Correct. Contain verified harm, investigate affected systems and data, recover safely, and communicate through accountable owners. Observation alone is not containment. In this case: Containment, investigation, and recovery require explicit incident management.
- **D:** Incorrect for this question. Observe deployed latency, failures, drift, and task outcomes with accountable response thresholds. Monitoring differs from an offline evaluation or a single diagnostic trace. In this case: Containment, investigation, and recovery require explicit incident management.

### Question 29 — B

Answer: Wait for validated prerequisite outputs. Dependent stages must be sequenced rather than run against unavailable prerequisite evidence. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. Local study-map skill 1.1 (Agent Architecture), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Dependent stages must be sequenced rather than run against unavailable prerequisite evidence.
- **B:** Correct. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: Dependent stages must be sequenced rather than run against unavailable prerequisite evidence.
- **C:** Incorrect for this question. Open-ended investigation benefits from exploration, prioritized hypotheses, and revised decomposition rather than an exhaustive fixed script chosen before evidence. In this case: Dependent stages must be sequenced rather than run against unavailable prerequisite evidence.
- **D:** Incorrect for this question. A coordinator manages decomposition, routing, error handling, and aggregation in a hub-and-spoke design. Specialists need not communicate through uncontrolled peer channels. In this case: Dependent stages must be sequenced rather than run against unavailable prerequisite evidence.

### Question 30 — C

Answer: Bound work queues and apply backpressure. Limit in-flight work and handle queues or overload instead of simply increase parallel calls. Limit queued and active work so slow consumers or provider limits do not exhaust memory or connections. Unbounded parallelism is not a capacity plan. Local study-map skill 2.4 (Software Engineering Foundations), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Await network operations without blocking an event loop, while limiting in-flight work and respecting service capacity. Creating a coroutine does not mean it has run. In this case: Limit in-flight work and handle queues or overload instead of simply increase parallel calls.
- **B:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Limit in-flight work and handle queues or overload instead of simply increase parallel calls.
- **C:** Correct. Limit queued and active work so slow consumers or provider limits do not exhaust memory or connections. Unbounded parallelism is not a capacity plan. In this case: Limit in-flight work and handle queues or overload instead of simply increase parallel calls.
- **D:** Incorrect for this question. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. In this case: Limit in-flight work and handle queues or overload instead of simply increase parallel calls.

### Question 31 — B

Answer: Preserve exact transactional facts outside lossy summaries. Verified critical facts should be retained exactly outside lossy narrative compression. Keep verified amounts, identifiers, dates, and commitments in structured state. General summaries can omit details that later decisions depend on. Local study-map skill 6.1 (Context Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. A structured overview and clear sections help reduce long-input position effects. Placement is a mitigation, not proof that every fact will be used. In this case: Verified critical facts should be retained exactly outside lossy narrative compression.
- **B:** Correct. Keep verified amounts, identifiers, dates, and commitments in structured state. General summaries can omit details that later decisions depend on. In this case: Verified critical facts should be retained exactly outside lossy narrative compression.
- **C:** Incorrect for this question. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. In this case: Verified critical facts should be retained exactly outside lossy narrative compression.
- **D:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Verified critical facts should be retained exactly outside lossy narrative compression.

### Question 32 — C

Answer: Allow explicit unknown or absent values in the schema. Explicit missing or unknown values distinguish evidence gaps from known values. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Explicit missing or unknown values distinguish evidence gaps from known values.
- **B:** Incorrect for this question. An other category with details can represent valid cases outside an enum. Unclear represents uncertainty and should not be confused with known-but-uncatalogued categories. In this case: Explicit missing or unknown values distinguish evidence gaps from known values.
- **C:** Correct. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Explicit missing or unknown values distinguish evidence gaps from known values.
- **D:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Explicit missing or unknown values distinguish evidence gaps from known values.

### Question 33 — A

Answer: Plan a tested migration before model or API retirement. Plan and validate migration before support ends instead of assume pinning guarantees perpetual availability. Pinning helps reproducibility only while that version remains supported. Track retirement notices and validate a supported replacement before the deadline. Local study-map skill 5.3 (Model Selection and Tradeoffs), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Correct. Pinning helps reproducibility only while that version remains supported. Track retirement notices and validate a supported replacement before the deadline. In this case: Plan and validate migration before support ends instead of assume pinning guarantees perpetual availability.
- **B:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Plan and validate migration before support ends instead of assume pinning guarantees perpetual availability.
- **C:** Incorrect for this question. Check endpoints, authentication, model identifiers, capabilities, data terms, and feature support for the selected provider. Shared model branding does not guarantee identical APIs or policies. In this case: Plan and validate migration before support ends instead of assume pinning guarantees perpetual availability.
- **D:** Incorrect for this question. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. In this case: Plan and validate migration before support ends instead of assume pinning guarantees perpetual availability.

### Question 34 — D

Answer: Implement a custom Messages-based agent harness. A custom harness owns orchestration and must implement protocol and safety responsibilities correctly. A custom harness gives the application direct control over requests, tool dispatch, stopping, state, and recovery. The application owns the resulting protocol and operational responsibilities. Local study-map skill 1.2 (Agent Construction with Claude), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. Evaluate state graphs, typed validation, tracing, ecosystem, and deployment fit across frameworks such as LangGraph, Strands, or PydanticAI. A framework does not guarantee safety or correctness. In this case: A custom harness owns orchestration and must implement protocol and safety responsibilities correctly.
- **B:** Incorrect for this question. An agent SDK can provide supported orchestration capabilities while still requiring version-aware deployment, permissions, monitoring, and application controls. In this case: A custom harness owns orchestration and must implement protocol and safety responsibilities correctly.
- **C:** Incorrect for this question. A known control path can suit predictable dependent transformations. It is not the same as a general SDK, custom agent harness, or adaptive decision loop. In this case: A custom harness owns orchestration and must implement protocol and safety responsibilities correctly.
- **D:** Correct. A custom harness gives the application direct control over requests, tool dispatch, stopping, state, and recovery. The application owns the resulting protocol and operational responsibilities. In this case: A custom harness owns orchestration and must implement protocol and safety responsibilities correctly.

### Question 35 — D

Answer: Normalize tool observations before model consumption. Observation normalization must preserve the actual result and uncertainty. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. Local study-map skill 7.3 (Claude Hooks), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. An appropriate pre-tool hook or equivalent trusted gate can deny a disallowed action before it runs. Hook implementation and failure handling must be tested. In this case: Observation normalization must preserve the actual result and uncertainty.
- **B:** Incorrect for this question. Review must gate the external effect, be tied to the intended action, and use current authority. A later audit cannot reliably reverse a completed effect. In this case: Observation normalization must preserve the actual result and uncertainty.
- **C:** Incorrect for this question. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Observation normalization must preserve the actual result and uncertainty.
- **D:** Correct. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. In this case: Observation normalization must preserve the actual result and uncertainty.

### Question 36 — C

Answer: Revoke exposed credentials and investigate their use. Revoke or rotate it and assess possible misuse and retained copies. Secret exposure requires containment and appropriate incident investigation, rotation, affected-copy handling, and monitoring. Removing one visible copy is not sufficient. Local study-map skill 7.4 (Identity, Secrets, and Key Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. Keep credentials out of prompts, repositories, generated output, and unprotected logs. Supply narrowly scoped credentials through approved runtime secret mechanisms. In this case: Revoke or rotate it and assess possible misuse and retained copies.
- **B:** Incorrect for this question. Audit records support attribution and reconstruction of consequential actions. Limit access, sensitive content, and retention; they do not themselves block an effect. In this case: Revoke or rotate it and assess possible misuse and retained copies.
- **C:** Correct. Secret exposure requires containment and appropriate incident investigation, rotation, affected-copy handling, and monitoring. Removing one visible copy is not sufficient. In this case: Revoke or rotate it and assess possible misuse and retained copies.
- **D:** Incorrect for this question. Contain verified harm, investigate affected systems and data, recover safely, and communicate through accountable owners. Observation alone is not containment. In this case: Revoke or rotate it and assess possible misuse and retained copies.

### Question 37 — B

Answer: Treat model output as untrusted before rendering or execution. Treat generated values as untrusted and enforce destination-specific constraints before use. Use destination-appropriate escaping, validation, and permission checks. Valid JSON can still contain executable or malicious values. Local study-map skill 2.5 (Claude Application Design), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Temperature changes next-token sampling behavior where supported. Lowering it does not independently guarantee correct extraction, grounding, or identical execution. In this case: Treat generated values as untrusted and enforce destination-specific constraints before use.
- **B:** Correct. Use destination-appropriate escaping, validation, and permission checks. Valid JSON can still contain executable or malicious values. In this case: Treat generated values as untrusted and enforce destination-specific constraints before use.
- **C:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Treat generated values as untrusted and enforce destination-specific constraints before use.
- **D:** Incorrect for this question. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Treat generated values as untrusted and enforce destination-specific constraints before use.

### Question 38 — D

Answer: Create a structured handoff with facts, status, and next actions. Verified facts, status, unresolved issues, and supporting evidence make continuation actionable. The recipient needs verified identifiers, completed work, unresolved issues, supporting evidence, and recommended actions, especially when the full transcript is unavailable. Local study-map skill 1.3 (Agent Patterns and Frameworks), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Verified facts, status, unresolved issues, and supporting evidence make continuation actionable.
- **B:** Incorrect for this question. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. In this case: Verified facts, status, unresolved issues, and supporting evidence make continuation actionable.
- **C:** Incorrect for this question. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Verified facts, status, unresolved issues, and supporting evidence make continuation actionable.
- **D:** Correct. The recipient needs verified identifiers, completed work, unresolved issues, supporting evidence, and recommended actions, especially when the full transcript is unavailable. In this case: Verified facts, status, unresolved issues, and supporting evidence make continuation actionable.

### Question 39 — B

Answer: Accumulate deltas by block index before final validation. Accumulate the documented deltas before parsing and considering any authorized action. Network chunks and content deltas can contain partial strings or JSON. Track event and block boundaries or use SDK helpers before consuming a complete structured value. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. This indicates ordinary turn completion, not that every business objective or external action succeeded. Application acceptance checks still apply. In this case: Accumulate the documented deltas before parsing and considering any authorized action.
- **B:** Correct. Network chunks and content deltas can contain partial strings or JSON. Track event and block boundaries or use SDK helpers before consuming a complete structured value. In this case: Accumulate the documented deltas before parsing and considering any authorized action.
- **C:** Incorrect for this question. A successful HTTP setup does not prove stream completion. Detect error events or interrupted streams, preserve status, and avoid publishing partial results as final success. In this case: Accumulate the documented deltas before parsing and considering any authorized action.
- **D:** Incorrect for this question. A max_tokens stop can leave content incomplete. Inspect the response and recover appropriately instead of treating it as normal completion. In this case: Accumulate the documented deltas before parsing and considering any authorized action.

### Question 40 — B

Answer: Count tokens with model-compatible accounting. Tokenization varies across text and languages rather than obey a universal word ratio. Tokens are model-dependent units, not always words or characters. Include actual system, tool, content, and output usage according to the service contract. Local study-map skill 5.1 (LLM Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. A token-count endpoint or compatible estimator can help plan requests. Include hidden overhead allowed by the documented interface and verify actual usage afterward. In this case: Tokenization varies across text and languages rather than obey a universal word ratio.
- **B:** Correct. Tokens are model-dependent units, not always words or characters. Include actual system, tool, content, and output usage according to the service contract. In this case: Tokenization varies across text and languages rather than obey a universal word ratio.
- **C:** Incorrect for this question. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. In this case: Tokenization varies across text and languages rather than obey a universal word ratio.
- **D:** Incorrect for this question. Follow the chosen model and service limits. Overflow handling varies; it is not universally automatic oldest-message deletion. In this case: Tokenization varies across text and languages rather than obey a universal word ratio.

### Question 41 — B

Answer: Place trusted application policy in the supported system instruction field. Use the supported top-level system instruction mechanism rather than invent an unsupported role. Keep trusted instructions separate from user and retrieved data. On the direct Messages API, system instructions use the top-level system parameter rather than a system-role entry in messages. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Use the selected API contract for model, instructions, messages, and typed content. Do not assume a consumer chat interface and a developer API share implicit state. In this case: Use the supported top-level system instruction mechanism rather than invent an unsupported role.
- **B:** Correct. Keep trusted instructions separate from user and retrieved data. On the direct Messages API, system instructions use the top-level system parameter rather than a system-role entry in messages. In this case: Use the supported top-level system instruction mechanism rather than invent an unsupported role.
- **C:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Use the supported top-level system instruction mechanism rather than invent an unsupported role.
- **D:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: Use the supported top-level system instruction mechanism rather than invent an unsupported role.

### Question 42 — A

Answer: Canary a version change with regression gates and rollback. Staged production exposure supports observation and rollback without claiming offline tests prove all behavior. Stage exposure to the new configuration, compare required outcomes, and retain a known-good path. A vendor release note is not workload validation. Local study-map skill 2.2 (Systems Life Cycle), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Correct. Stage exposure to the new configuration, compare required outcomes, and retain a known-good path. A vendor release note is not workload validation. In this case: Staged production exposure supports observation and rollback without claiming offline tests prove all behavior.
- **B:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Staged production exposure supports observation and rollback without claiming offline tests prove all behavior.
- **C:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Staged production exposure supports observation and rollback without claiming offline tests prove all behavior.
- **D:** Incorrect for this question. Record the deployable configuration, approval gates, and a practical known-good recovery path. Deployment is an operational change rather than just a successful local build. In this case: Staged production exposure supports observation and rollback without claiming offline tests prove all behavior.

### Question 43 — B

Answer: Select the least costly configuration that meets required outcomes. Evaluate representative application cases instead of infer task fitness from a generic leaderboard. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. Local study-map skill 5.3 (Model Selection and Tradeoffs), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. A balanced model may suit many development workflows, but the actual selected release and workload requirements determine fitness. In this case: Evaluate representative application cases instead of infer task fitness from a generic leaderboard.
- **B:** Correct. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. In this case: Evaluate representative application cases instead of infer task fitness from a generic leaderboard.
- **C:** Incorrect for this question. Model-family positioning is a starting hypothesis, not proof of fit. Use a specific supported version and measure the required quality, cost, and latency. In this case: Evaluate representative application cases instead of infer task fitness from a generic leaderboard.
- **D:** Incorrect for this question. A high-capability model may help difficult tasks, but size or family alone does not guarantee accuracy, acceptable latency, or economical deployment. In this case: Evaluate representative application cases instead of infer task fitness from a generic leaderboard.

### Question 44 — C

Answer: State explicit reportable and non-reportable criteria. Concrete inclusion and exclusion criteria make judgment more consistent and testable. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. Local study-map skill 6.2 (Prompt Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Negative examples teach a boundary and can reduce repeated false positives. They should not teach blanket suppression of an entire genuine-risk category. In this case: Concrete inclusion and exclusion criteria make judgment more consistent and testable.
- **B:** Incorrect for this question. A consistent rubric distinguishes materially different harms. Self-reported confidence is not a substitute for severity or business impact. In this case: Concrete inclusion and exclusion criteria make judgment more consistent and testable.
- **C:** Correct. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Concrete inclusion and exclusion criteria make judgment more consistent and testable.
- **D:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Concrete inclusion and exclusion criteria make judgment more consistent and testable.

### Question 45 — D

Answer: Verify cache reads, writes, and economics in actual usage. Measure observed eligible reuse and pricing rather than assume a checkpoint guarantees savings. Repeated text does not prove cache reuse. Check eligible matching, expiration, thresholds, and current prices before claiming savings. Local study-map skill 5.4 (Cost and Token Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. In this case: Measure observed eligible reuse and pricing rather than assume a checkpoint guarantees savings.
- **B:** Incorrect for this question. Supported prefix caching depends on exact eligible content, placement, checkpoints, model, and service rules. It is not a cross-user final-answer cache. In this case: Measure observed eligible reuse and pricing rather than assume a checkpoint guarantees savings.
- **C:** Incorrect for this question. Caching may reduce repeated prefix processing under provider-specific rules. It does not extend the context window, update model weights, or verify an answer. In this case: Measure observed eligible reuse and pricing rather than assume a checkpoint guarantees savings.
- **D:** Correct. Repeated text does not prove cache reuse. Check eligible matching, expiration, thresholds, and current prices before claiming savings. In this case: Measure observed eligible reuse and pricing rather than assume a checkpoint guarantees savings.

### Question 46 — A

Answer: Pass relevant evidence and constraints explicitly. Explicit relevant constraints and evidence prevent incorrect assumptions about inherited context. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. Local study-map skill 6.1 (Context Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Correct. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Explicit relevant constraints and evidence prevent incorrect assumptions about inherited context.
- **B:** Incorrect for this question. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: Explicit relevant constraints and evidence prevent incorrect assumptions about inherited context.
- **C:** Incorrect for this question. Delegation requires a permitted launcher under the installed SDK contract. Check Agent versus legacy Task identifiers rather than assume all versions accept the same names. In this case: Explicit relevant constraints and evidence prevent incorrect assumptions about inherited context.
- **D:** Incorrect for this question. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. In this case: Explicit relevant constraints and evidence prevent incorrect assumptions about inherited context.

### Question 47 — A

Answer: Specify task, audience, constraints, and output expectations. Specify intended audience, task, constraints, and output expectations. Concrete requirements clarify what useful output means. A role, sampling setting, or longer answer limit does not replace a precise task contract. Local study-map skill 6.2 (Prompt Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Correct. Concrete requirements clarify what useful output means. A role, sampling setting, or longer answer limit does not replace a precise task contract. In this case: Specify intended audience, task, constraints, and output expectations.
- **B:** Incorrect for this question. A role can guide style and viewpoint, but it does not grant expertise, authorization, or verified knowledge. In this case: Specify intended audience, task, constraints, and output expectations.
- **C:** Incorrect for this question. An output ceiling bounds generation subject to model accounting. It does not itself expand input context or guarantee that a complete response fits. In this case: Specify intended audience, task, constraints, and output expectations.
- **D:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Specify intended audience, task, constraints, and output expectations.

### Question 48 — D

Answer: Enforce task, iteration, and spending safeguards. Bound attempts, time, or spend and define a useful stopping and escalation policy. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. Local study-map skill 1.2 (Agent Construction with Claude), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. Review must gate the external effect, be tied to the intended action, and use current authority. A later audit cannot reliably reverse a completed effect. In this case: Bound attempts, time, or spend and define a useful stopping and escalation policy.
- **B:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Bound attempts, time, or spend and define a useful stopping and escalation policy.
- **C:** Incorrect for this question. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Bound attempts, time, or spend and define a useful stopping and escalation policy.
- **D:** Correct. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. In this case: Bound attempts, time, or spend and define a useful stopping and escalation policy.

### Question 49 — B

Answer: Build a valid Messages API request with explicit content blocks. Use supported role-structured Messages content rather than assume a server-side transcript is implicit. Use the selected API contract for model, instructions, messages, and typed content. Do not assume a consumer chat interface and a developer API share implicit state. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. A REST integration must respect its actual endpoint contract. HTTP 200 does not establish that the requested business operation succeeded semantically. In this case: Use supported role-structured Messages content rather than assume a server-side transcript is implicit.
- **B:** Correct. Use the selected API contract for model, instructions, messages, and typed content. Do not assume a consumer chat interface and a developer API share implicit state. In this case: Use supported role-structured Messages content rather than assume a server-side transcript is implicit.
- **C:** Incorrect for this question. Keep trusted instructions separate from user and retrieved data. On the direct Messages API, system instructions use the top-level system parameter rather than a system-role entry in messages. In this case: Use supported role-structured Messages content rather than assume a server-side transcript is implicit.
- **D:** Incorrect for this question. A response can contain text, tool use, thinking, or other supported blocks. Do not assume content is one string or that the first block is always displayable text. In this case: Use supported role-structured Messages content rather than assume a server-side transcript is implicit.

### Question 50 — D

Answer: Isolate model-output defects from integration defects. The faulty application transformation should be fixed rather than repeatedly change model instructions. Check whether correct raw output was lost or changed by serialization, parsing, routing, or persistence. Not every visible error is fixed by changing the prompt. Local study-map skill 4.1 (Debugging and Error Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/streaming

- **A:** Incorrect for this question. Correlate the actual request, model response, tool execution, retries, and validation results. Diagnose the first failing boundary rather than infer cause from the final prose. In this case: The faulty application transformation should be fixed rather than repeatedly change model instructions.
- **B:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: The faulty application transformation should be fixed rather than repeatedly change model instructions.
- **C:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: The faulty application transformation should be fixed rather than repeatedly change model instructions.
- **D:** Correct. Check whether correct raw output was lost or changed by serialization, parsing, routing, or persistence. Not every visible error is fixed by changing the prompt. In this case: The faulty application transformation should be fixed rather than repeatedly change model instructions.

### Question 51 — D

Answer: Select the Claude interface appropriate to the workflow. Select an interface appropriate to the workflow instead of assume every Claude surface has identical contracts. Claude Code, Desktop, consumer chat, APIs, and SDKs serve different interaction needs. Verify each interface contract instead of assume identical state, configuration, and capabilities. Local study-map skill 2.5 (Claude Application Design), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. A REST integration must respect its actual endpoint contract. HTTP 200 does not establish that the requested business operation succeeded semantically. In this case: Select an interface appropriate to the workflow instead of assume every Claude surface has identical contracts.
- **B:** Incorrect for this question. Check endpoints, authentication, model identifiers, capabilities, data terms, and feature support for the selected provider. Shared model branding does not guarantee identical APIs or policies. In this case: Select an interface appropriate to the workflow instead of assume every Claude surface has identical contracts.
- **C:** Incorrect for this question. An agent SDK can provide supported orchestration capabilities while still requiring version-aware deployment, permissions, monitoring, and application controls. In this case: Select an interface appropriate to the workflow instead of assume every Claude surface has identical contracts.
- **D:** Correct. Claude Code, Desktop, consumer chat, APIs, and SDKs serve different interaction needs. Verify each interface contract instead of assume identical state, configuration, and capabilities. In this case: Select an interface appropriate to the workflow instead of assume every Claude surface has identical contracts.

### Question 52 — A

Answer: Use project-scoped .mcp.json for shared server configuration. Project configuration can be versioned with runtime secret references and appropriate approvals. Versioned project configuration can distribute team tooling. Keep real credentials outside Git and check approvals and environment requirements. Local study-map skill 8.3 (Agentic Customization), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Versioned project configuration can distribute team tooling. Keep real credentials outside Git and check approvals and environment requirements. In this case: Project configuration can be versioned with runtime secret references and appropriate approvals.
- **B:** Incorrect for this question. The guide describes user-scoped configuration in ~/.claude.json for personal tooling. Personal configuration is not automatically shared through the repository. In this case: Project configuration can be versioned with runtime secret references and appropriate approvals.
- **C:** Incorrect for this question. Configured servers can expose tools together when connected, but server failure, approval, filtering, and permissions can affect what is actually usable. In this case: Project configuration can be versioned with runtime secret references and appropriate approvals.
- **D:** Incorrect for this question. Environment expansion can keep literal secrets out of project files. Supply credentials through an approved secret path and protect logs as well. In this case: Project configuration can be versioned with runtime secret references and appropriate approvals.

### Question 53 — C

Answer: Handle errors after streaming has already begun. Streaming completion needs explicit inspection beyond the initial status code. A successful HTTP setup does not prove stream completion. Detect error events or interrupted streams, preserve status, and avoid publishing partial results as final success. Local study-map skill 4.1 (Debugging and Error Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/streaming

- **A:** Incorrect for this question. SDK accumulation helpers can provide the complete message. Inspect termination and errors before treating the resulting object as accepted application output. In this case: Streaming completion needs explicit inspection beyond the initial status code.
- **B:** Incorrect for this question. This indicates ordinary turn completion, not that every business objective or external action succeeded. Application acceptance checks still apply. In this case: Streaming completion needs explicit inspection beyond the initial status code.
- **C:** Correct. A successful HTTP setup does not prove stream completion. Detect error events or interrupted streams, preserve status, and avoid publishing partial results as final success. In this case: Streaming completion needs explicit inspection beyond the initial status code.
- **D:** Incorrect for this question. A max_tokens stop can leave content incomplete. Inspect the response and recover appropriately instead of treating it as normal completion. In this case: Streaming completion needs explicit inspection beyond the initial status code.

### Question 54 — A

Answer: Bound work queues and apply backpressure. Limit in-flight and queued work instead of assume unlimited concurrent tasks improve throughput. Limit queued and active work so slow consumers or provider limits do not exhaust memory or connections. Unbounded parallelism is not a capacity plan. Local study-map skill 5.2 (Technical Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Correct. Limit queued and active work so slow consumers or provider limits do not exhaust memory or connections. Unbounded parallelism is not a capacity plan. In this case: Limit in-flight and queued work instead of assume unlimited concurrent tasks improve throughput.
- **B:** Incorrect for this question. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. In this case: Limit in-flight and queued work instead of assume unlimited concurrent tasks improve throughput.
- **C:** Incorrect for this question. Await network operations without blocking an event loop, while limiting in-flight work and respecting service capacity. Creating a coroutine does not mean it has run. In this case: Limit in-flight and queued work instead of assume unlimited concurrent tasks improve throughput.
- **D:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Limit in-flight and queued work instead of assume unlimited concurrent tasks improve throughput.

### Question 55 — A

Answer: Track actual usage by token and billing category. Use provider-reported usage and applicable rates rather than only pre-request estimates. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. Local study-map skill 5.4 (Cost and Token Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Correct. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. In this case: Use provider-reported usage and applicable rates rather than only pre-request estimates.
- **B:** Incorrect for this question. A token-count endpoint or compatible estimator can help plan requests. Include hidden overhead allowed by the documented interface and verify actual usage afterward. In this case: Use provider-reported usage and applicable rates rather than only pre-request estimates.
- **C:** Incorrect for this question. Include failed attempts, retries, review, tool work, and operating overhead rather than compare only listed unit token rates. In this case: Use provider-reported usage and applicable rates rather than only pre-request estimates.
- **D:** Incorrect for this question. Measure the complete user-facing interval consistently, including relevant tool and queue time. Lower per-request price does not establish lower cost per successful outcome. In this case: Use provider-reported usage and applicable rates rather than only pre-request estimates.

### Question 56 — B

Answer: Evaluate Opus for demanding capability-oriented work. A higher-capability family can be tested while checking cost and latency rather than assume guaranteed success. A high-capability model may help difficult tasks, but size or family alone does not guarantee accuracy, acceptable latency, or economical deployment. Local study-map skill 5.3 (Model Selection and Tradeoffs), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. A balanced model may suit many development workflows, but the actual selected release and workload requirements determine fitness. In this case: A higher-capability family can be tested while checking cost and latency rather than assume guaranteed success.
- **B:** Correct. A high-capability model may help difficult tasks, but size or family alone does not guarantee accuracy, acceptable latency, or economical deployment. In this case: A higher-capability family can be tested while checking cost and latency rather than assume guaranteed success.
- **C:** Incorrect for this question. Reasoning-related features and parameters vary by model and provider. Evaluate quality, latency, and cost rather than assume every release accepts the same switches. In this case: A higher-capability family can be tested while checking cost and latency rather than assume guaranteed success.
- **D:** Incorrect for this question. Model-family positioning is a starting hypothesis, not proof of fit. Use a specific supported version and measure the required quality, cost, and latency. In this case: A higher-capability family can be tested while checking cost and latency rather than assume guaranteed success.

### Question 57 — D

Answer: Manage release approval and rollback boundaries. Manage the release and rollback boundary rather than treat deployment as an irreversible file copy. Record the deployable configuration, approval gates, and a practical known-good recovery path. Deployment is an operational change rather than just a successful local build. Local study-map skill 2.2 (Systems Life Cycle), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Manage the release and rollback boundary rather than treat deployment as an irreversible file copy.
- **B:** Incorrect for this question. Record revisions of behavioral instructions with evaluation and release history. A model pin does not freeze changing application prompts. In this case: Manage the release and rollback boundary rather than treat deployment as an irreversible file copy.
- **C:** Incorrect for this question. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: Manage the release and rollback boundary rather than treat deployment as an irreversible file copy.
- **D:** Correct. Record the deployable configuration, approval gates, and a practical known-good recovery path. Deployment is an operational change rather than just a successful local build. In this case: Manage the release and rollback boundary rather than treat deployment as an irreversible file copy.

### Question 58 — A

Answer: Use the appropriate settings.json scope for behavioral configuration. Supported settings govern runtime behavior under their documented scopes. Claude Code settings configure supported behavior, permissions, hooks, and plugins. Shared .claude/settings.json, user, local, and managed scopes have distinct reach. Local study-map skill 2.6 (Configuration Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Correct. Claude Code settings configure supported behavior, permissions, hooks, and plugins. Shared .claude/settings.json, user, local, and managed scopes have distinct reach. In this case: Supported settings govern runtime behavior under their documented scopes.
- **B:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: Supported settings govern runtime behavior under their documented scopes.
- **C:** Incorrect for this question. Topic-specific rule files reduce one oversized instruction document. Add path scoping when a rule is only relevant to selected files. In this case: Supported settings govern runtime behavior under their documented scopes.
- **D:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Supported settings govern runtime behavior under their documented scopes.

### Question 59 — A

Answer: Apply HTTP method, status, authentication, and payload contracts. REST-style request and response mechanics still require authentication and robust error handling. A REST integration must respect its actual endpoint contract. HTTP 200 does not establish that the requested business operation succeeded semantically. Local study-map skill 5.2 (Technical Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Correct. A REST integration must respect its actual endpoint contract. HTTP 200 does not establish that the requested business operation succeeded semantically. In this case: REST-style request and response mechanics still require authentication and robust error handling.
- **B:** Incorrect for this question. The documented streaming interface emits SSE events over HTTP. It is not inherently a WebSocket connection or one valid JSON object per arbitrary network chunk. In this case: REST-style request and response mechanics still require authentication and robust error handling.
- **C:** Incorrect for this question. Await network operations without blocking an event loop, while limiting in-flight work and respecting service capacity. Creating a coroutine does not mean it has run. In this case: REST-style request and response mechanics still require authentication and robust error handling.
- **D:** Incorrect for this question. WebSockets can fit bidirectional application communication, but the documented standard Messages streaming interface is SSE. Do not confuse a transport choice with model capability. In this case: REST-style request and response mechanics still require authentication and robust error handling.

### Question 60 — D

Answer: Account for probabilistic generation and output variability. Probabilistic generation can yield variation and should not be mistaken for persistent memory changes. Next-token generation may yield different plausible results across calls. Validate required outcomes rather than assume ordinary inference changes persistent model memory. Local study-map skill 5.1 (LLM Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Reasoning-related features and parameters vary by model and provider. Evaluate quality, latency, and cost rather than assume every release accepts the same switches. In this case: Probabilistic generation can yield variation and should not be mistaken for persistent memory changes.
- **B:** Incorrect for this question. Effort settings influence supported reasoning behavior under a particular model contract. They are not synonyms for sampling temperature or guarantees of correctness. In this case: Probabilistic generation can yield variation and should not be mistaken for persistent memory changes.
- **C:** Incorrect for this question. Temperature changes next-token sampling behavior where supported. Lowering it does not independently guarantee correct extraction, grounding, or identical execution. In this case: Probabilistic generation can yield variation and should not be mistaken for persistent memory changes.
- **D:** Correct. Next-token generation may yield different plausible results across calls. Validate required outcomes rather than assume ordinary inference changes persistent model memory. In this case: Probabilistic generation can yield variation and should not be mistaken for persistent memory changes.

### Question 61 — C

Answer: Run independent branches concurrently and join checked results. Bounded parallel work can reduce latency when independence and aggregation rules are clear. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. Local study-map skill 1.1 (Agent Architecture), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. Open-ended investigation benefits from exploration, prioritized hypotheses, and revised decomposition rather than an exhaustive fixed script chosen before evidence. In this case: Bounded parallel work can reduce latency when independence and aggregation rules are clear.
- **B:** Incorrect for this question. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: Bounded parallel work can reduce latency when independence and aggregation rules are clear.
- **C:** Correct. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Bounded parallel work can reduce latency when independence and aggregation rules are clear.
- **D:** Incorrect for this question. Shared context can support collaboration but needs coordination, scope, and concurrency controls. It differs from a supervisor owning delegation and reconciling final outputs. In this case: Bounded parallel work can reduce latency when independence and aggregation rules are clear.

### Question 62 — A

Answer: Use a predictable sequence of specialized stages. A known dependency sequence favors a predictable workflow over open-ended autonomous planning. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. Local study-map skill 1.1 (Agent Architecture), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Correct. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: A known dependency sequence favors a predictable workflow over open-ended autonomous planning.
- **B:** Incorrect for this question. A coordinator manages decomposition, routing, error handling, and aggregation in a hub-and-spoke design. Specialists need not communicate through uncontrolled peer channels. In this case: A known dependency sequence favors a predictable workflow over open-ended autonomous planning.
- **C:** Incorrect for this question. Open-ended investigation benefits from exploration, prioritized hypotheses, and revised decomposition rather than an exhaustive fixed script chosen before evidence. In this case: A known dependency sequence favors a predictable workflow over open-ended autonomous planning.
- **D:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: A known dependency sequence favors a predictable workflow over open-ended autonomous planning.

### Question 63 — B

Answer: Reduce tool output to relevant fields with provenance. Return only high-signal fields while preserving meaning and provenance. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. Local study-map skill 6.1 (Context Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Keep verified amounts, identifiers, dates, and commitments in structured state. General summaries can omit details that later decisions depend on. In this case: Return only high-signal fields while preserving meaning and provenance.
- **B:** Correct. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: Return only high-signal fields while preserving meaning and provenance.
- **C:** Incorrect for this question. A structured overview and clear sections help reduce long-input position effects. Placement is a mitigation, not proof that every fact will be used. In this case: Return only high-signal fields while preserving meaning and provenance.
- **D:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Return only high-signal fields while preserving meaning and provenance.

### Question 64 — B

Answer: Layer prevention, detection, approval, and recovery controls. Combine complementary trusted controls, monitoring, review, and recovery for distinct risks. No one prompt or content filter covers all attack paths. Combine least privilege, trusted checks, telemetry, tests, and incident response. Local study-map skill 7.2 (Guardrails and Safe Deployment), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. Content controls address applicable unsafe-content categories. They are not a replacement for identity checks, resource authorization, constrained tools, or secure execution. In this case: Combine complementary trusted controls, monitoring, review, and recovery for distinct risks.
- **B:** Correct. No one prompt or content filter covers all attack paths. Combine least privilege, trusted checks, telemetry, tests, and incident response. In this case: Combine complementary trusted controls, monitoring, review, and recovery for distinct risks.
- **C:** Incorrect for this question. Review must gate the external effect, be tied to the intended action, and use current authority. A later audit cannot reliably reverse a completed effect. In this case: Combine complementary trusted controls, monitoring, review, and recovery for distinct risks.
- **D:** Incorrect for this question. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Combine complementary trusted controls, monitoring, review, and recovery for distinct risks.

### Question 65 — C

Answer: Scope a rule with YAML paths glob patterns. Path-specific rules can match the role across directories instead of apply indiscriminately. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. Local study-map skill 3.1 (Claude Code Operation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/settings

- **A:** Incorrect for this question. Local instructions fit conventions tied to a particular subtree. Cross-directory filename patterns may be better served by path-scoped rules. In this case: Path-specific rules can match the role across directories instead of apply indiscriminately.
- **B:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Path-specific rules can match the role across directories instead of apply indiscriminately.
- **C:** Correct. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. In this case: Path-specific rules can match the role across directories instead of apply indiscriminately.
- **D:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: Path-specific rules can match the role across directories instead of apply indiscriminately.

### Question 66 — C

Answer: Consume the Messages stream as server-sent events. Server-sent events carry incremental responses; they are not a bidirectional WebSocket contract. The documented streaming interface emits SSE events over HTTP. It is not inherently a WebSocket connection or one valid JSON object per arbitrary network chunk. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. A REST integration must respect its actual endpoint contract. HTTP 200 does not establish that the requested business operation succeeded semantically. In this case: Server-sent events carry incremental responses; they are not a bidirectional WebSocket contract.
- **B:** Incorrect for this question. WebSockets can fit bidirectional application communication, but the documented standard Messages streaming interface is SSE. Do not confuse a transport choice with model capability. In this case: Server-sent events carry incremental responses; they are not a bidirectional WebSocket contract.
- **C:** Correct. The documented streaming interface emits SSE events over HTTP. It is not inherently a WebSocket connection or one valid JSON object per arbitrary network chunk. In this case: Server-sent events carry incremental responses; they are not a bidirectional WebSocket contract.
- **D:** Incorrect for this question. Await network operations without blocking an event loop, while limiting in-flight work and respecting service capacity. Creating a coroutine does not mean it has run. In this case: Server-sent events carry incremental responses; they are not a bidirectional WebSocket contract.

### Question 67 — C

Answer: Assess impact, data, authority, and misuse risks before deployment. Assess impact, data, authority, and misuse risks before granting operational capability. Risk review identifies consequences and necessary controls before capability is granted. Ordinary quality evaluation alone may omit regulatory, privacy, and misuse concerns. Local study-map skill 2.1 (Understanding Requirements), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Specify behavior, latency, throughput, data constraints, failure policy, and acceptance criteria. A model or framework choice is not a substitute for requirements. In this case: Assess impact, data, authority, and misuse risks before granting operational capability.
- **B:** Incorrect for this question. Consult people who use, operate, approve, or are materially affected by a workflow. Requirements should reflect real responsibilities rather than assumptions made by implementers alone. In this case: Assess impact, data, authority, and misuse risks before granting operational capability.
- **C:** Correct. Risk review identifies consequences and necessary controls before capability is granted. Ordinary quality evaluation alone may omit regulatory, privacy, and misuse concerns. In this case: Assess impact, data, authority, and misuse risks before granting operational capability.
- **D:** Incorrect for this question. Define who handles uncertain results, incidents, updates, and recovery. A model cannot substitute for accountable organizational responsibility. In this case: Assess impact, data, authority, and misuse risks before granting operational capability.

### Question 68 — C

Answer: Retrieve application-managed memory into later context. External application memory differs from changing the model's inference-time weights. Persisted preferences or facts can be selected and supplied to later requests. That continuity is external state management rather than automatic updates to model training weights. Local study-map skill 1.3 (Agent Patterns and Frameworks), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. In this case: External application memory differs from changing the model's inference-time weights.
- **B:** Incorrect for this question. Caching may reduce repeated prefix processing under provider-specific rules. It does not extend the context window, update model weights, or verify an answer. In this case: External application memory differs from changing the model's inference-time weights.
- **C:** Correct. Persisted preferences or facts can be selected and supplied to later requests. That continuity is external state management rather than automatic updates to model training weights. In this case: External application memory differs from changing the model's inference-time weights.
- **D:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: External application memory differs from changing the model's inference-time weights.

### Question 69 — D

Answer: Review generated changes as ordinary production code. Inspect correctness, maintainability, and safety alongside tests rather than trust generated code automatically. Inspect correctness, maintainability, dependencies, tests, and security. Generated code is not exempt from normal engineering review or accountable approval. Local study-map skill 2.4 (Software Engineering Foundations), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Inspect correctness, maintainability, and safety alongside tests rather than trust generated code automatically.
- **B:** Incorrect for this question. Version control records reviewable history and enables collaboration and rollback of code artifacts. It does not automatically record every runtime setting or external side effect. In this case: Inspect correctness, maintainability, and safety alongside tests rather than trust generated code automatically.
- **C:** Incorrect for this question. Refactoring changes implementation organization without intended external behavior changes. Tests and review help detect accidental regressions. In this case: Inspect correctness, maintainability, and safety alongside tests rather than trust generated code automatically.
- **D:** Correct. Inspect correctness, maintainability, dependencies, tests, and security. Generated code is not exempt from normal engineering review or accountable approval. In this case: Inspect correctness, maintainability, and safety alongside tests rather than trust generated code automatically.

### Question 70 — B

Answer: Use a durable idempotency key for the same logical action. Reuse a durable key for the same intended action rather than create a new retry identity. Where supported, repeated requests for one operation should resolve to one intended external effect. Generating a new key for each retry defeats duplicate protection. Local study-map skill 2.4 (Software Engineering Foundations), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Local cancellation limits waiting or computation but does not guarantee the server stopped or a remote side effect was rolled back. In this case: Reuse a durable key for the same intended action rather than create a new retry identity.
- **B:** Correct. Where supported, repeated requests for one operation should resolve to one intended external effect. Generating a new key for each retry defeats duplicate protection. In this case: Reuse a durable key for the same intended action rather than create a new retry identity.
- **C:** Incorrect for this question. Separate a generated proposal from an authorized atomic or otherwise well-coordinated business effect. Define conflict handling and rollback or compensation behavior. In this case: Reuse a durable key for the same intended action rather than create a new retry identity.
- **D:** Incorrect for this question. Bound user and dependency waits. A timeout is an uncertain execution outcome for mutations and may require status reconciliation rather than blind retry. In this case: Reuse a durable key for the same intended action rather than create a new retry identity.

### Question 71 — D

Answer: Pin compatible model, SDK, prompt, and dependency versions. Pin a supported model version where available and plan tested migrations before retirement. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. Local study-map skill 2.6 (Configuration Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Plugins can change tools and workflow behavior. Track provenance, versions, compatibility, and permissions rather than install unreviewed code merely because a model suggests it. In this case: Pin a supported model version where available and plan tested migrations before retirement.
- **B:** Incorrect for this question. Record revisions of behavioral instructions with evaluation and release history. A model pin does not freeze changing application prompts. In this case: Pin a supported model version where available and plan tested migrations before retirement.
- **C:** Incorrect for this question. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: Pin a supported model version where available and plan tested migrations before retirement.
- **D:** Correct. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Pin a supported model version where available and plan tested migrations before retirement.

### Question 72 — C

Answer: Preserve claim-to-source mappings through every handoff. Claim-to-source support is needed for verification, not just an unaffiliated bibliography. Claims need traceable source identities, relevant excerpts, locations, and dates as applicable. A bibliography without claim mappings can lose attribution. Local study-map skill 6.1 (Context Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Different measurement periods can explain apparent disagreements. Dates and methodology should remain attached rather than being stripped in summaries. In this case: Claim-to-source support is needed for verification, not just an unaffiliated bibliography.
- **B:** Incorrect for this question. Do not average incompatible measurements or choose one arbitrarily. Preserve context and distinguish contested findings from established ones. In this case: Claim-to-source support is needed for verification, not just an unaffiliated bibliography.
- **C:** Correct. Claims need traceable source identities, relevant excerpts, locations, and dates as applicable. A bibliography without claim mappings can lose attribution. In this case: Claim-to-source support is needed for verification, not just an unaffiliated bibliography.
- **D:** Incorrect for this question. Tables can preserve financial comparisons, while prose and structured lists suit other needs. A single forced format can hide important structure. In this case: Claim-to-source support is needed for verification, not just an unaffiliated bibliography.

### Question 73 — C

Answer: Separate environment configuration from application logic. Track actual runtime configuration and its scope rather than only application source. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. Local study-map skill 2.6 (Configuration Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Plugins can change tools and workflow behavior. Track provenance, versions, compatibility, and permissions rather than install unreviewed code merely because a model suggests it. In this case: Track actual runtime configuration and its scope rather than only application source.
- **B:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Track actual runtime configuration and its scope rather than only application source.
- **C:** Correct. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: Track actual runtime configuration and its scope rather than only application source.
- **D:** Incorrect for this question. Record revisions of behavioral instructions with evaluation and release history. A model pin does not freeze changing application prompts. In this case: Track actual runtime configuration and its scope rather than only application source.

### Question 74 — B

Answer: Use representative few-shot examples with boundaries. Multiple examples demonstrate expected behavior rather than leave the task entirely example-free. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. Local study-map skill 5.1 (LLM Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. A role can guide style and viewpoint, but it does not grant expertise, authorization, or verified knowledge. In this case: Multiple examples demonstrate expected behavior rather than leave the task entirely example-free.
- **B:** Correct. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Multiple examples demonstrate expected behavior rather than leave the task entirely example-free.
- **C:** Incorrect for this question. One-shot prompting includes one example. It is different from a training update and may not cover important task variation. In this case: Multiple examples demonstrate expected behavior rather than leave the task entirely example-free.
- **D:** Incorrect for this question. Zero-shot prompting supplies no example input-output pairs. The model may still use its pretrained capabilities and the request context. In this case: Multiple examples demonstrate expected behavior rather than leave the task entirely example-free.

### Question 75 — A

Answer: Version and review plugin dependencies and permissions. Plugins may alter permissions and execution behavior, so version and compatibility matter. Plugins can change tools and workflow behavior. Track provenance, versions, compatibility, and permissions rather than install unreviewed code merely because a model suggests it. Local study-map skill 2.5 (Claude Application Design), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Correct. Plugins can change tools and workflow behavior. Track provenance, versions, compatibility, and permissions rather than install unreviewed code merely because a model suggests it. In this case: Plugins may alter permissions and execution behavior, so version and compatibility matter.
- **B:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Plugins may alter permissions and execution behavior, so version and compatibility matter.
- **C:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: Plugins may alter permissions and execution behavior, so version and compatibility matter.
- **D:** Incorrect for this question. Evaluate state graphs, typed validation, tracing, ecosystem, and deployment fit across frameworks such as LangGraph, Strands, or PydanticAI. A framework does not guarantee safety or correctness. In this case: Plugins may alter permissions and execution behavior, so version and compatibility matter.

### Question 76 — A

Answer: Version exact prompt content and its dependencies. Version exact instructions and dependencies so evaluations and rollback can be reproduced. Record revisions of behavioral instructions with evaluation and release history. A model pin does not freeze changing application prompts. Local study-map skill 6.2 (Prompt Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Correct. Record revisions of behavioral instructions with evaluation and release history. A model pin does not freeze changing application prompts. In this case: Version exact instructions and dependencies so evaluations and rollback can be reproduced.
- **B:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Version exact instructions and dependencies so evaluations and rollback can be reproduced.
- **C:** Incorrect for this question. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: Version exact instructions and dependencies so evaluations and rollback can be reproduced.
- **D:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Version exact instructions and dependencies so evaluations and rollback can be reproduced.

### Question 77 — B

Answer: Evaluate Haiku for suitable speed- and efficiency-oriented tasks. Haiku's positioning may suit efficient tasks when actual measured requirements are satisfied. Model-family positioning is a starting hypothesis, not proof of fit. Use a specific supported version and measure the required quality, cost, and latency. Local study-map skill 5.3 (Model Selection and Tradeoffs), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Reasoning-related features and parameters vary by model and provider. Evaluate quality, latency, and cost rather than assume every release accepts the same switches. In this case: Haiku's positioning may suit efficient tasks when actual measured requirements are satisfied.
- **B:** Correct. Model-family positioning is a starting hypothesis, not proof of fit. Use a specific supported version and measure the required quality, cost, and latency. In this case: Haiku's positioning may suit efficient tasks when actual measured requirements are satisfied.
- **C:** Incorrect for this question. A high-capability model may help difficult tasks, but size or family alone does not guarantee accuracy, acceptable latency, or economical deployment. In this case: Haiku's positioning may suit efficient tasks when actual measured requirements are satisfied.
- **D:** Incorrect for this question. A balanced model may suit many development workflows, but the actual selected release and workload requirements determine fitness. In this case: Haiku's positioning may suit efficient tasks when actual measured requirements are satisfied.

### Question 78 — D

Answer: Use asynchronous I/O with bounded concurrency. Async operations need appropriate execution in the event loop rather than mere function construction. Await network operations without blocking an event loop, while limiting in-flight work and respecting service capacity. Creating a coroutine does not mean it has run. Local study-map skill 5.2 (Technical Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: Async operations need appropriate execution in the event loop rather than mere function construction.
- **B:** Incorrect for this question. A REST integration must respect its actual endpoint contract. HTTP 200 does not establish that the requested business operation succeeded semantically. In this case: Async operations need appropriate execution in the event loop rather than mere function construction.
- **C:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Async operations need appropriate execution in the event loop rather than mere function construction.
- **D:** Correct. Await network operations without blocking an event loop, while limiting in-flight work and respecting service capacity. Creating a coroutine does not mean it has run. In this case: Async operations need appropriate execution in the event loop rather than mere function construction.

### Question 79 — D

Answer: Use pre-execution tool interception for blocking policy checks. Check and block the actual action before execution rather than rely on post-action detection. An appropriate pre-tool hook or equivalent trusted gate can deny a disallowed action before it runs. Hook implementation and failure handling must be tested. Local study-map skill 7.3 (Claude Hooks), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. In this case: Check and block the actual action before execution rather than rely on post-action detection.
- **B:** Incorrect for this question. Audit records support attribution and reconstruction of consequential actions. Limit access, sensitive content, and retention; they do not themselves block an effect. In this case: Check and block the actual action before execution rather than rely on post-action detection.
- **C:** Incorrect for this question. Observe deployed latency, failures, drift, and task outcomes with accountable response thresholds. Monitoring differs from an offline evaluation or a single diagnostic trace. In this case: Check and block the actual action before execution rather than rely on post-action detection.
- **D:** Correct. An appropriate pre-tool hook or equivalent trusted gate can deny a disallowed action before it runs. Hook implementation and failure handling must be tested. In this case: Check and block the actual action before execution rather than rely on post-action detection.

### Question 80 — A

Answer: Expose a supported MCP resource catalog. Resources represent content or metadata rather than automatically execute domain actions. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. Local study-map skill 8.2 (MCP Server Development), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Resources represent content or metadata rather than automatically execute domain actions.
- **B:** Incorrect for this question. MCP prompts package reusable interaction templates. They differ from resources providing content and tools executing operations. In this case: Resources represent content or metadata rather than automatically execute domain actions.
- **C:** Incorrect for this question. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. In this case: Resources represent content or metadata rather than automatically execute domain actions.
- **D:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Resources represent content or metadata rather than automatically execute domain actions.

### Question 81 — C

Answer: Use an SDK wrapper over the provider request contract. An SDK wrapper simplifies supported mechanics without removing schema, policy, or retry responsibilities. An SDK can simplify serialization, accumulation, and error handling. The actual provider schema, policies, supported features, and operational limits still apply. Local study-map skill 5.2 (Technical Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. An agent SDK can provide supported orchestration capabilities while still requiring version-aware deployment, permissions, monitoring, and application controls. In this case: An SDK wrapper simplifies supported mechanics without removing schema, policy, or retry responsibilities.
- **B:** Incorrect for this question. A REST integration must respect its actual endpoint contract. HTTP 200 does not establish that the requested business operation succeeded semantically. In this case: An SDK wrapper simplifies supported mechanics without removing schema, policy, or retry responsibilities.
- **C:** Correct. An SDK can simplify serialization, accumulation, and error handling. The actual provider schema, policies, supported features, and operational limits still apply. In this case: An SDK wrapper simplifies supported mechanics without removing schema, policy, or retry responsibilities.
- **D:** Incorrect for this question. Check endpoints, authentication, model identifiers, capabilities, data terms, and feature support for the selected provider. Shared model branding does not guarantee identical APIs or policies. In this case: An SDK wrapper simplifies supported mechanics without removing schema, policy, or retry responsibilities.

### Question 82 — C

Answer: Execute a client-defined tool through the application harness. Client-executed tools place dispatch and result responsibilities in the application harness. The model proposes supported client tool calls; the application validates, authorizes, executes, and returns correlated results. A proposal alone does not execute application code. Local study-map skill 8.1 (Tool Implementation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Client-executed tools place dispatch and result responsibilities in the application harness.
- **B:** Incorrect for this question. Supported built-in server tools execute within the provider service under that feature contract. They differ from application functions the client must dispatch itself. In this case: Client-executed tools place dispatch and result responsibilities in the application harness.
- **C:** Correct. The model proposes supported client tool calls; the application validates, authorizes, executes, and returns correlated results. A proposal alone does not execute application code. In this case: Client-executed tools place dispatch and result responsibilities in the application harness.
- **D:** Incorrect for this question. MCP prompts package reusable interaction templates. They differ from resources providing content and tools executing operations. In this case: Client-executed tools place dispatch and result responsibilities in the application harness.

### Question 83 — C

Answer: Evaluate a maintained existing integration before writing a custom server. Evaluate fit, security, maintenance, and permissions before deciding to build a custom server. A suitable standard integration may reduce work. Assess security, permissions, maintenance, and requirements before adoption; custom tools remain appropriate for unique workflows. Local study-map skill 8.3 (Agentic Customization), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. A custom harness gives the application direct control over requests, tool dispatch, stopping, state, and recovery. The application owns the resulting protocol and operational responsibilities. In this case: Evaluate fit, security, maintenance, and permissions before deciding to build a custom server.
- **B:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Evaluate fit, security, maintenance, and permissions before deciding to build a custom server.
- **C:** Correct. A suitable standard integration may reduce work. Assess security, permissions, maintenance, and requirements before adoption; custom tools remain appropriate for unique workflows. In this case: Evaluate fit, security, maintenance, and permissions before deciding to build a custom server.
- **D:** Incorrect for this question. Evaluate state graphs, typed validation, tracing, ecosystem, and deployment fit across frameworks such as LangGraph, Strands, or PydanticAI. A framework does not guarantee safety or correctness. In this case: Evaluate fit, security, maintenance, and permissions before deciding to build a custom server.

### Question 84 — B

Answer: Compare total cost per verified successful outcome. Compare cost per accepted outcome including retries and review rather than unit request price alone. Include failed attempts, retries, review, tool work, and operating overhead rather than compare only listed unit token rates. Local study-map skill 5.4 (Cost and Token Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. A token-count endpoint or compatible estimator can help plan requests. Include hidden overhead allowed by the documented interface and verify actual usage afterward. In this case: Compare cost per accepted outcome including retries and review rather than unit request price alone.
- **B:** Correct. Include failed attempts, retries, review, tool work, and operating overhead rather than compare only listed unit token rates. In this case: Compare cost per accepted outcome including retries and review rather than unit request price alone.
- **C:** Incorrect for this question. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. In this case: Compare cost per accepted outcome including retries and review rather than unit request price alone.
- **D:** Incorrect for this question. Repeated text does not prove cache reuse. Check eligible matching, expiration, thresholds, and current prices before claiming savings. In this case: Compare cost per accepted outcome including retries and review rather than unit request price alone.

### Question 85 — D

Answer: Append the assistant tool-use blocks and matching tool results. Preserve matching tool-use and result blocks so the next model call has correct observations. Client-tool observations must be returned with the correct tool-use identifiers in a valid message sequence so Claude can use actual results. Local study-map skill 1.3 (Agent Patterns and Frameworks), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. SDK accumulation helpers can provide the complete message. Inspect termination and errors before treating the resulting object as accepted application output. In this case: Preserve matching tool-use and result blocks so the next model call has correct observations.
- **B:** Incorrect for this question. The loop follows protocol stop reasons, executes permitted requested tools, and returns observations before continuing. Text appearing in a response does not establish completion. In this case: Preserve matching tool-use and result blocks so the next model call has correct observations.
- **C:** Incorrect for this question. This indicates ordinary turn completion, not that every business objective or external action succeeded. Application acceptance checks still apply. In this case: Preserve matching tool-use and result blocks so the next model call has correct observations.
- **D:** Correct. Client-tool observations must be returned with the correct tool-use identifiers in a valid message sequence so Claude can use actual results. In this case: Preserve matching tool-use and result blocks so the next model call has correct observations.

### Question 86 — C

Answer: Use supported strict structured output with a schema. Structured output mechanisms address shape while semantic and authorization checks remain separate. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. Local study-map skill 2.5 (Claude Application Design), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Structured output mechanisms address shape while semantic and authorization checks remain separate.
- **B:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Structured output mechanisms address shape while semantic and authorization checks remain separate.
- **C:** Correct. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Structured output mechanisms address shape while semantic and authorization checks remain separate.
- **D:** Incorrect for this question. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Structured output mechanisms address shape while semantic and authorization checks remain separate.

### Question 87 — D

Answer: Version exact prompt content and its dependencies. Record exact prompt revisions with evaluation and rollout history. Record revisions of behavioral instructions with evaluation and release history. A model pin does not freeze changing application prompts. Local study-map skill 2.6 (Configuration Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: Record exact prompt revisions with evaluation and rollout history.
- **B:** Incorrect for this question. Plugins can change tools and workflow behavior. Track provenance, versions, compatibility, and permissions rather than install unreviewed code merely because a model suggests it. In this case: Record exact prompt revisions with evaluation and rollout history.
- **C:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Record exact prompt revisions with evaluation and rollout history.
- **D:** Correct. Record revisions of behavioral instructions with evaluation and release history. A model pin does not freeze changing application prompts. In this case: Record exact prompt revisions with evaluation and rollout history.

### Question 88 — D

Answer: Refactor internal structure while preserving required behavior. Refactoring improves structure with tests that guard the expected external behavior. Refactoring changes implementation organization without intended external behavior changes. Tests and review help detect accidental regressions. Local study-map skill 2.4 (Software Engineering Foundations), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Development does not end at a successful API call. Include monitoring, updates, recovery, ownership, and decommissioning in the system lifecycle. In this case: Refactoring improves structure with tests that guard the expected external behavior.
- **B:** Incorrect for this question. Inspect correctness, maintainability, dependencies, tests, and security. Generated code is not exempt from normal engineering review or accountable approval. In this case: Refactoring improves structure with tests that guard the expected external behavior.
- **C:** Incorrect for this question. Version control records reviewable history and enables collaboration and rollback of code artifacts. It does not automatically record every runtime setting or external side effect. In this case: Refactoring improves structure with tests that guard the expected external behavior.
- **D:** Correct. Refactoring changes implementation organization without intended external behavior changes. Tests and review help detect accidental regressions. In this case: Refactoring improves structure with tests that guard the expected external behavior.

### Question 89 — D

Answer: Translate business goals into measurable functional and operational requirements. Define actual tasks, users, constraints, and success requirements before committing to implementation. Specify behavior, latency, throughput, data constraints, failure policy, and acceptance criteria. A model or framework choice is not a substitute for requirements. Local study-map skill 2.1 (Understanding Requirements), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Checkable success and failure conditions make a proposed behavior evaluable. Generic quality adjectives and technology choices do not establish acceptable results. In this case: Define actual tasks, users, constraints, and success requirements before committing to implementation.
- **B:** Incorrect for this question. Consult people who use, operate, approve, or are materially affected by a workflow. Requirements should reflect real responsibilities rather than assumptions made by implementers alone. In this case: Define actual tasks, users, constraints, and success requirements before committing to implementation.
- **C:** Incorrect for this question. Set measurable latency, availability, and quality targets for the complete workflow. Account for dependencies and tail behavior rather than only average model speed. In this case: Define actual tasks, users, constraints, and success requirements before committing to implementation.
- **D:** Correct. Specify behavior, latency, throughput, data constraints, failure policy, and acceptance criteria. A model or framework choice is not a substitute for requirements. In this case: Define actual tasks, users, constraints, and success requirements before committing to implementation.

### Question 90 — A

Answer: Use asynchronous I/O with bounded concurrency. Use correctly awaited asynchronous operations and compatible libraries with bounded concurrency. Await network operations without blocking an event loop, while limiting in-flight work and respecting service capacity. Creating a coroutine does not mean it has run. Local study-map skill 2.4 (Software Engineering Foundations), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Correct. Await network operations without blocking an event loop, while limiting in-flight work and respecting service capacity. Creating a coroutine does not mean it has run. In this case: Use correctly awaited asynchronous operations and compatible libraries with bounded concurrency.
- **B:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Use correctly awaited asynchronous operations and compatible libraries with bounded concurrency.
- **C:** Incorrect for this question. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: Use correctly awaited asynchronous operations and compatible libraries with bounded concurrency.
- **D:** Incorrect for this question. A REST integration must respect its actual endpoint contract. HTTP 200 does not establish that the requested business operation succeeded semantically. In this case: Use correctly awaited asynchronous operations and compatible libraries with bounded concurrency.

### Question 91 — B

Answer: Choose a framework for needed orchestration semantics. Framework choice should follow needed semantics and maintenance rather than imply identical capabilities. Evaluate state graphs, typed validation, tracing, ecosystem, and deployment fit across frameworks such as LangGraph, Strands, or PydanticAI. A framework does not guarantee safety or correctness. Local study-map skill 1.3 (Agent Patterns and Frameworks), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. An agent SDK can provide supported orchestration capabilities while still requiring version-aware deployment, permissions, monitoring, and application controls. In this case: Framework choice should follow needed semantics and maintenance rather than imply identical capabilities.
- **B:** Correct. Evaluate state graphs, typed validation, tracing, ecosystem, and deployment fit across frameworks such as LangGraph, Strands, or PydanticAI. A framework does not guarantee safety or correctness. In this case: Framework choice should follow needed semantics and maintenance rather than imply identical capabilities.
- **C:** Incorrect for this question. A REST integration must respect its actual endpoint contract. HTTP 200 does not establish that the requested business operation succeeded semantically. In this case: Framework choice should follow needed semantics and maintenance rather than imply identical capabilities.
- **D:** Incorrect for this question. A custom harness gives the application direct control over requests, tool dispatch, stopping, state, and recovery. The application owns the resulting protocol and operational responsibilities. In this case: Framework choice should follow needed semantics and maintenance rather than imply identical capabilities.

### Question 92 — A

Answer: Use Message Batches for latency-tolerant independent requests. Batch processing can suit deferred workloads but is not a guaranteed interactive response path. Asynchronous batches fit non-blocking workloads. The retrieved guide describes discounted processing and a window up to 24 hours, not a guaranteed latency SLA. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Correct. Asynchronous batches fit non-blocking workloads. The retrieved guide describes discounted processing and a window up to 24 hours, not a guaranteed latency SLA. In this case: Batch processing can suit deferred workloads but is not a guaranteed interactive response path.
- **B:** Incorrect for this question. An interactive path suits work needing a prompt response within its service targets. It is distinct from deferred batch submission and does not guarantee arbitrary latency. In this case: Batch processing can suit deferred workloads but is not a guaranteed interactive response path.
- **C:** Incorrect for this question. Await network operations without blocking an event loop, while limiting in-flight work and respecting service capacity. Creating a coroutine does not mean it has run. In this case: Batch processing can suit deferred workloads but is not a guaranteed interactive response path.
- **D:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Batch processing can suit deferred workloads but is not a guaranteed interactive response path.

### Question 93 — C

Answer: Include valid examples that should not be flagged. Valid near-misses demonstrate the intended boundary between acceptable behavior and defects. Negative examples teach a boundary and can reduce repeated false positives. They should not teach blanket suppression of an entire genuine-risk category. Local study-map skill 6.2 (Prompt Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Valid near-misses demonstrate the intended boundary between acceptable behavior and defects.
- **B:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Valid near-misses demonstrate the intended boundary between acceptable behavior and defects.
- **C:** Correct. Negative examples teach a boundary and can reduce repeated false positives. They should not teach blanket suppression of an entire genuine-risk category. In this case: Valid near-misses demonstrate the intended boundary between acceptable behavior and defects.
- **D:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Valid near-misses demonstrate the intended boundary between acceptable behavior and defects.

### Question 94 — D

Answer: Define observable service-level objectives and failure behavior. Operational service targets clarify measurable expectations rather than rely on model quality alone. Set measurable latency, availability, and quality targets for the complete workflow. Account for dependencies and tail behavior rather than only average model speed. Local study-map skill 2.1 (Understanding Requirements), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Include failed attempts, retries, review, tool work, and operating overhead rather than compare only listed unit token rates. In this case: Operational service targets clarify measurable expectations rather than rely on model quality alone.
- **B:** Incorrect for this question. Checkable success and failure conditions make a proposed behavior evaluable. Generic quality adjectives and technology choices do not establish acceptable results. In this case: Operational service targets clarify measurable expectations rather than rely on model quality alone.
- **C:** Incorrect for this question. Measure the complete user-facing interval consistently, including relevant tool and queue time. Lower per-request price does not establish lower cost per successful outcome. In this case: Operational service targets clarify measurable expectations rather than rely on model quality alone.
- **D:** Correct. Set measurable latency, availability, and quality targets for the complete workflow. Account for dependencies and tail behavior rather than only average model speed. In this case: Operational service targets clarify measurable expectations rather than rely on model quality alone.

### Question 95 — D

Answer: Use a supported provider-executed server tool. Server-executed tools differ from client tools whose implementations the application runs. Supported built-in server tools execute within the provider service under that feature contract. They differ from application functions the client must dispatch itself. Local study-map skill 8.1 (Tool Implementation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. MCP prompts package reusable interaction templates. They differ from resources providing content and tools executing operations. In this case: Server-executed tools differ from client tools whose implementations the application runs.
- **B:** Incorrect for this question. The model proposes supported client tool calls; the application validates, authorizes, executes, and returns correlated results. A proposal alone does not execute application code. In this case: Server-executed tools differ from client tools whose implementations the application runs.
- **C:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Server-executed tools differ from client tools whose implementations the application runs.
- **D:** Correct. Supported built-in server tools execute within the provider service under that feature contract. They differ from application functions the client must dispatch itself. In this case: Server-executed tools differ from client tools whose implementations the application runs.

### Question 96 — D

Answer: Run Claude Code in non-interactive print mode. Non-interactive print operation suits CI when required permissions and inputs are prepared. The -p or --print mode is intended for non-interactive runs. Authentication, permissions, termination, and artifact capture still require CI configuration. Local study-map skill 3.1 (Claude Code Operation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/settings

- **A:** Incorrect for this question. The guide describes --output-format json and --json-schema for machine-parseable CI results. Verify the installed version and check execution status as well as payload. In this case: Non-interactive print operation suits CI when required permissions and inputs are prepared.
- **B:** Incorrect for this question. The guide describes .claude/commands/ for shared invocable commands. User-scoped commands are personal; feature details depend on Claude Code version. In this case: Non-interactive print operation suits CI when required permissions and inputs are prepared.
- **C:** Incorrect for this question. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. In this case: Non-interactive print operation suits CI when required permissions and inputs are prepared.
- **D:** Correct. The -p or --print mode is intended for non-interactive runs. Authentication, permissions, termination, and artifact capture still require CI configuration. In this case: Non-interactive print operation suits CI when required permissions and inputs are prepared.

### Question 97 — B

Answer: Define observable acceptance criteria for required outcomes. Observable acceptance criteria make implementation and evaluation decisions accountable. Checkable success and failure conditions make a proposed behavior evaluable. Generic quality adjectives and technology choices do not establish acceptable results. Local study-map skill 2.1 (Understanding Requirements), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Observable acceptance criteria make implementation and evaluation decisions accountable.
- **B:** Correct. Checkable success and failure conditions make a proposed behavior evaluable. Generic quality adjectives and technology choices do not establish acceptable results. In this case: Observable acceptance criteria make implementation and evaluation decisions accountable.
- **C:** Incorrect for this question. Specify behavior, latency, throughput, data constraints, failure policy, and acceptance criteria. A model or framework choice is not a substitute for requirements. In this case: Observable acceptance criteria make implementation and evaluation decisions accountable.
- **D:** Incorrect for this question. Set measurable latency, availability, and quality targets for the complete workflow. Account for dependencies and tail behavior rather than only average model speed. In this case: Observable acceptance criteria make implementation and evaluation decisions accountable.

### Question 98 — C

Answer: Route coordination through an orchestrator. A coordinator can integrate evidence and control delegation without uncontrolled peer messaging. A coordinator manages decomposition, routing, error handling, and aggregation in a hub-and-spoke design. Specialists need not communicate through uncontrolled peer channels. Local study-map skill 1.1 (Agent Architecture), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/overview

- **A:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: A coordinator can integrate evidence and control delegation without uncontrolled peer messaging.
- **B:** Incorrect for this question. Shared context can support collaboration but needs coordination, scope, and concurrency controls. It differs from a supervisor owning delegation and reconciling final outputs. In this case: A coordinator can integrate evidence and control delegation without uncontrolled peer messaging.
- **C:** Correct. A coordinator manages decomposition, routing, error handling, and aggregation in a hub-and-spoke design. Specialists need not communicate through uncontrolled peer channels. In this case: A coordinator can integrate evidence and control delegation without uncontrolled peer messaging.
- **D:** Incorrect for this question. Context isolation reduces unrelated material and can limit conversational access. It does not automatically isolate external files, credentials, or remote side effects. In this case: A coordinator can integrate evidence and control delegation without uncontrolled peer messaging.

### Question 99 — C

Answer: Put shared project standards in versioned CLAUDE.md. Versioned repository instructions give teammates the same contextual conventions. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. Local study-map skill 3.1 (Claude Code Operation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/settings

- **A:** Incorrect for this question. Local instructions fit conventions tied to a particular subtree. Cross-directory filename patterns may be better served by path-scoped rules. In this case: Versioned repository instructions give teammates the same contextual conventions.
- **B:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: Versioned repository instructions give teammates the same contextual conventions.
- **C:** Correct. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Versioned repository instructions give teammates the same contextual conventions.
- **D:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: Versioned repository instructions give teammates the same contextual conventions.

### Question 100 — C

Answer: Expose a reusable prompt template through MCP. MCP prompts represent templates; tools and resources have different protocol roles. MCP prompts package reusable interaction templates. They differ from resources providing content and tools executing operations. Local study-map skill 8.2 (MCP Server Development), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: MCP prompts represent templates; tools and resources have different protocol roles.
- **B:** Incorrect for this question. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. In this case: MCP prompts represent templates; tools and resources have different protocol roles.
- **C:** Correct. MCP prompts package reusable interaction templates. They differ from resources providing content and tools executing operations. In this case: MCP prompts represent templates; tools and resources have different protocol roles.
- **D:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: MCP prompts represent templates; tools and resources have different protocol roles.
