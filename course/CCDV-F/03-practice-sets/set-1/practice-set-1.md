# Claude Certified Developer – Foundations (CCDV-F) — Practice Set 1

Applications and Integration

100 questions · Suggested practice duration: 200 minutes · Practice target: 80%

Tests 1–5 are focused learning tests. Test 6 is an expanded blueprint-proportioned review, not an official exam replica. Related concepts recur.

Select ONE best answer for every question. Answer key follows all questions.

Original educational content, not actual, recalled, or copied Anthropic exam items.

## Questions

### 1. A feature request says 'add AI' without describing outputs or acceptable failures. What should the developer establish first?

Domain: Applications and Integration

- A. Translate business goals into measurable functional and operational requirements
- B. Define observable service-level objectives and failure behavior
- C. Choose a framework for needed orchestration semantics
- D. Select the least costly configuration that meets required outcomes

### 2. An interactive assistant needs explicit response-time and availability targets for production. What operational contract should be defined?

Domain: Applications and Integration

- A. Track actual usage by token and billing category
- B. Translate business goals into measurable functional and operational requirements
- C. Measure tail latency as well as average latency
- D. Define observable service-level objectives and failure behavior

### 3. A team selects a model before learning that source data cannot leave its approved environment. What process should come first?

Domain: Applications and Integration

- A. Select the least costly configuration that meets required outcomes
- B. Route requests using evaluated task classes and safe fallbacks
- C. Translate business goals into measurable functional and operational requirements
- D. Choose a framework for needed orchestration semantics

### 4. An application depends on several external services but measures only model response speed. What should requirements include?

Domain: Applications and Integration

- A. Measure time to first token separately from full completion
- B. Measure tail latency as well as average latency
- C. Define observable service-level objectives and failure behavior
- D. Track actual usage by token and billing category

### 5. Users disagree about whether an assistant should advise or actually commit changes. What must be clarified?

Domain: Applications and Integration

- A. State explicit reportable and non-reportable criteria
- B. Select the least costly configuration that meets required outcomes
- C. Provide concrete input–output examples
- D. Translate business goals into measurable functional and operational requirements

### 6. A prototype works for one user but the intended traffic and data constraints are unknown. What is missing?

Domain: Applications and Integration

- A. Compare hosting responsibility, control, and service constraints
- B. Translate business goals into measurable functional and operational requirements
- C. Route requests using evaluated task classes and safe fallbacks
- D. Choose a framework for needed orchestration semantics

### 7. The application has no documented behavior when a dependency exceeds the user's deadline. What should be specified?

Domain: Applications and Integration

- A. Define observable service-level objectives and failure behavior
- B. Measure tail latency as well as average latency
- C. Track actual usage by token and billing category
- D. Compare total cost per verified successful outcome

### 8. A buyer needs both supported image inputs and private transactional data access. What should drive design?

Domain: Applications and Integration

- A. Select the least costly configuration that meets required outcomes
- B. Use a provider-specific adapter behind a stable application interface
- C. Translate business goals into measurable functional and operational requirements
- D. Choose a framework for needed orchestration semantics

### 9. The product team wants summaries but cannot state what makes one acceptable. What should development agree first?

Domain: Applications and Integration

- A. State explicit reportable and non-reportable criteria
- B. Provide concrete input–output examples
- C. Translate business goals into measurable functional and operational requirements
- D. Use a versioned representative held-out evaluation set

### 10. A system promises rapid answers without any measured service objective or timeout policy. What should be defined?

Domain: Applications and Integration

- A. Measure tail latency as well as average latency
- B. Set explicit deadlines and classify timeout outcomes
- C. Measure time to first token separately from full completion
- D. Define observable service-level objectives and failure behavior

### 11. A successful API demo has no owner for updates, monitoring, or retirement. What engineering view is missing?

Domain: Applications and Integration

- A. Canary a version change with regression gates and rollback
- B. Pin compatible model, SDK, prompt, and dependency versions
- C. Plan deployment, operation, maintenance, and retirement
- D. Separate environment configuration from application logic

### 12. A revised application passes offline tests and is ready for controlled production exposure. What deployment method limits surprises?

Domain: Applications and Integration

- A. Separate environment configuration from application logic
- B. Use a versioned representative held-out evaluation set
- C. Canary a version change with regression gates and rollback
- D. Pin compatible model, SDK, prompt, and dependency versions

### 13. An integration is being retired but its credentials and retained artifacts remain active. What process must cover this?

Domain: Applications and Integration

- A. Separate environment configuration from application logic
- B. Plan deployment, operation, maintenance, and retirement
- C. Pin compatible model, SDK, prompt, and dependency versions
- D. Version and review plugin dependencies and permissions

### 14. Quality changes as real user traffic evolves after release. What activity should continue?

Domain: Applications and Integration

- A. Monitor production service and outcome signals
- B. Inspect a redacted end-to-end request and tool trace
- C. Keep protected action and identity audit records
- D. Use a versioned representative held-out evaluation set

### 15. An interrupted workflow must recover pending work after a process restart. What design supports this?

Domain: Applications and Integration

- A. Resume the identified session when its context remains valid
- B. Persist structured task state and pending actions
- C. Resume from a checked manifest of worker states and artifacts
- D. Checkpoint durable state at safe workflow boundaries

### 16. A new prompt behaves differently under production traffic despite strong development results. What release control helps contain harm?

Domain: Applications and Integration

- A. Pin compatible model, SDK, prompt, and dependency versions
- B. Use a versioned representative held-out evaluation set
- C. Canary a version change with regression gates and rollback
- D. Separate environment configuration from application logic

### 17. A team plans only implementation tasks and ignores maintenance after API versions change. What should its plan include?

Domain: Applications and Integration

- A. Plan deployment, operation, maintenance, and retirement
- B. Choose a framework for needed orchestration semantics
- C. Compare hosting responsibility, control, and service constraints
- D. Select the least costly configuration that meets required outcomes

### 18. An assistant begins exposing private records after a configuration change. What coordinated process should activate?

Domain: Applications and Integration

- A. Activate coordinated incident response and recovery
- B. Monitor production service and outcome signals
- C. Keep protected action and identity audit records
- D. Inspect a redacted end-to-end request and tool trace

### 19. An engineer cannot reproduce last week's behavior because model and prompt versions were never recorded. What practice helps?

Domain: Applications and Integration

- A. Pin compatible model, SDK, prompt, and dependency versions
- B. Version and review plugin dependencies and permissions
- C. Separate environment configuration from application logic
- D. Canary a version change with regression gates and rollback

### 20. A service will be replaced, but retained data and downstream dependencies have no transition plan. What discipline addresses this?

Domain: Applications and Integration

- A. Canary a version change with regression gates and rollback
- B. Plan deployment, operation, maintenance, and retirement
- C. Compare hosting responsibility, control, and service constraints
- D. Choose a framework for needed orchestration semantics

### 21. A developer sends a consumer-chat transcript directly to an API expecting typed message content. What should be built?

Domain: Applications and Integration

- A. Place trusted application policy in the supported system instruction field
- B. Use a provider-specific adapter behind a stable application interface
- C. Build a valid Messages API request with explicit content blocks
- D. Supply the relevant conversation state on subsequent requests

### 22. On the direct Messages API, where should trusted application instructions go rather than an invented system-role message?

Domain: Applications and Integration

- A. Place trusted application policy in the supported system instruction field
- B. Build a valid Messages API request with explicit content blocks
- C. Put personal cross-project preferences in ~/.claude/CLAUDE.md
- D. Put shared project standards in versioned CLAUDE.md

### 23. A parser assumes response.content is one string and crashes on a tool block. What response strategy is needed?

Domain: Applications and Integration

- A. Use the final assembled message and completion status
- B. Dispatch response content according to each block type
- C. Accumulate deltas by block index before final validation
- D. Build a valid Messages API request with explicit content blocks

### 24. A follow-up request omits the earlier conversation and loses a user preference. What should the caller supply?

Domain: Applications and Integration

- A. Resume the identified session when its context remains valid
- B. Build a valid Messages API request with explicit content blocks
- C. Persist structured task state and pending actions
- D. Supply the relevant conversation state on subsequent requests

### 25. A client tool executes, but Claude never receives its observation. What should the application append?

Domain: Applications and Integration

- A. Append the assistant tool-use blocks and matching tool results
- B. Build a valid Messages API request with explicit content blocks
- C. Dispatch response content according to each block type
- D. Use the final assembled message and completion status

### 26. A hosted-provider endpoint rejects direct-API authentication and model identifiers. What integration layer should handle the difference?

Domain: Applications and Integration

- A. Pin compatible model, SDK, prompt, and dependency versions
- B. Separate environment configuration from application logic
- C. Use a provider-specific adapter behind a stable application interface
- D. Build a valid Messages API request with explicit content blocks

### 27. The SDK offers a final assembled message after streaming. What should downstream processing inspect before acceptance?

Domain: Applications and Integration

- A. Handle the output limit as an incomplete response
- B. Treat end_turn as the end of the current assistant turn
- C. Use the final assembled message and completion status
- D. Dispatch response content according to each block type

### 28. A response stops at max_tokens before its generated object is complete. What should the caller recognize?

Domain: Applications and Integration

- A. Treat end_turn as the end of the current assistant turn
- B. Inspect stop_reason and dispatch the appropriate branch
- C. Use the final assembled message and completion status
- D. Handle the output limit as an incomplete response

### 29. Claude emits commentary and requests a tool in one response. What should determine the next protocol branch?

Domain: Applications and Integration

- A. Inspect stop_reason and dispatch the appropriate branch
- B. Dispatch response content according to each block type
- C. Treat end_turn as the end of the current assistant turn
- D. Enforce task, iteration, and spending safeguards

### 30. A continuation uses a feature requiring unchanged signed blocks. What should the integration preserve?

Domain: Applications and Integration

- A. Dispatch response content according to each block type
- B. Append the assistant tool-use blocks and matching tool results
- C. Supply the relevant conversation state on subsequent requests
- D. Preserve protocol-required blocks through tool continuations

### 31. A developer implements standard Messages streaming as a WebSocket client and receives HTTP event text. Which transport should be consumed?

Domain: Applications and Integration

- A. Apply HTTP method, status, authentication, and payload contracts
- B. Use WebSockets for an explicitly bidirectional persistent channel
- C. Use asynchronous I/O with bounded concurrency
- D. Consume the Messages stream as server-sent events

### 32. Tool arguments arrive as several partial JSON string deltas. When should the application consume a complete validated object?

Domain: Applications and Integration

- A. Dispatch response content according to each block type
- B. Consume the Messages stream as server-sent events
- C. Accumulate deltas by block index before final validation
- D. Use the final assembled message and completion status

### 33. The HTTP stream starts successfully but later emits an error event. What must the application handle?

Domain: Applications and Integration

- A. Handle the output limit as an incomplete response
- B. Handle errors after streaming has already begun
- C. Treat end_turn as the end of the current assistant turn
- D. Use the final assembled message and completion status

### 34. Two streamed content blocks interleave their deltas. What should keep their accumulated values separate?

Domain: Applications and Integration

- A. Accumulate deltas by block index before final validation
- B. Dispatch response content according to each block type
- C. Consume the Messages stream as server-sent events
- D. Use the final assembled message and completion status

### 35. A caller needs a complete response object but does not need to display tokens incrementally. What SDK facility may simplify handling?

Domain: Applications and Integration

- A. Use the final assembled message and completion status
- B. Treat end_turn as the end of the current assistant turn
- C. Accumulate deltas by block index before final validation
- D. Dispatch response content according to each block type

### 36. A network disconnect occurs after half a displayed answer. What should prevent a false success indication?

Domain: Applications and Integration

- A. Handle errors after streaming has already begun
- B. Handle the output limit as an incomplete response
- C. Use the final assembled message and completion status
- D. Treat end_turn as the end of the current assistant turn

### 37. A streaming parser assumes each network packet contains one complete JSON event. Which protocol framing should it follow instead?

Domain: Applications and Integration

- A. Apply HTTP method, status, authentication, and payload contracts
- B. Consume the Messages stream as server-sent events
- C. Use asynchronous I/O with bounded concurrency
- D. Use WebSockets for an explicitly bidirectional persistent channel

### 38. A stream includes text and other supported content types. What should the renderer distinguish?

Domain: Applications and Integration

- A. Dispatch response content according to each block type
- B. Use the final assembled message and completion status
- C. Preserve protocol-required blocks through tool continuations
- D. Accumulate deltas by block index before final validation

### 39. A provider returns an overload event after stream establishment. Which failure handling is required?

Domain: Applications and Integration

- A. Use the final assembled message and completion status
- B. Inspect stop_reason and dispatch the appropriate branch
- C. Treat end_turn as the end of the current assistant turn
- D. Handle errors after streaming has already begun

### 40. A developer tries to parse each partial_json delta independently and sees invalid JSON errors. What should change?

Domain: Applications and Integration

- A. Consume the Messages stream as server-sent events
- B. Use the final assembled message and completion status
- C. Dispatch response content according to each block type
- D. Accumulate deltas by block index before final validation

### 41. An application sends only an image filename as text and expects visual analysis. What is required?

Domain: Applications and Integration

- A. Build a valid Messages API request with explicit content blocks
- B. Dispatch response content according to each block type
- C. Use a provider-specific adapter behind a stable application interface
- D. Send supported image content in the documented multimodal format

### 42. A model rejects an image because its declared media type does not match the data. What contract should be corrected?

Domain: Applications and Integration

- A. Build a valid Messages API request with explicit content blocks
- B. Use a provider-specific adapter behind a stable application interface
- C. Dispatch response content according to each block type
- D. Send supported image content in the documented multimodal format

### 43. A developer enables reasoning-related controls unsupported by the selected model release. What should be checked?

Domain: Applications and Integration

- A. Pin compatible model, SDK, prompt, and dependency versions
- B. Select the least costly configuration that meets required outcomes
- C. Adjust sampling variability, not factual truth
- D. Use supported thinking or effort controls after measuring task benefit

### 44. Requests repeatedly send the same eligible long prefix before user-specific input. What supported optimization may help?

Domain: Applications and Integration

- A. Use supported token counting before oversized submission
- B. Put eligible stable common content before variable input for cache reuse
- C. Verify cache reads, writes, and economics in actual usage
- D. Track actual usage by token and billing category

### 45. A non-blocking recurring audit accepts asynchronous completion. Which API path may fit its latency tolerance?

Domain: Applications and Integration

- A. Use synchronous requests for blocking latency-sensitive work
- B. Bound work queues and apply backpressure
- C. Use Message Batches for latency-tolerant independent requests
- D. Use asynchronous I/O with bounded concurrency

### 46. A user-facing approval request must complete within an active interaction deadline. Which API path should lead the design?

Domain: Applications and Integration

- A. Use synchronous requests for blocking latency-sensitive work
- B. Use Message Batches for latency-tolerant independent requests
- C. Use asynchronous I/O with bounded concurrency
- D. Consume the Messages stream as server-sent events

### 47. Batch results arrive in a different order from submitted source records. What should correlate them?

Domain: Applications and Integration

- A. Propagate correlation identifiers across requests and tools
- B. Resubmit only failed items after diagnosing their errors
- C. Correlate batch outcomes by custom_id
- D. Record detected_pattern and dismissal reasons

### 48. Only some asynchronous items fail due to oversized inputs. What resubmission strategy is appropriate?

Domain: Applications and Integration

- A. Correlate batch outcomes by custom_id
- B. Tune and validate on a representative sample before large submission
- C. Use Message Batches for latency-tolerant independent requests
- D. Resubmit only failed items after diagnosing their errors

### 49. A feature works through one provider but is unavailable through another. What should application integration account for?

Domain: Applications and Integration

- A. Send supported image content in the documented multimodal format
- B. Pin compatible model, SDK, prompt, and dependency versions
- C. Use a provider-specific adapter behind a stable application interface
- D. Use supported thinking or effort controls after measuring task benefit

### 50. A client edits signed continuation content to make it shorter and later requests fail. What contract practice matters?

Domain: Applications and Integration

- A. Supply the relevant conversation state on subsequent requests
- B. Dispatch response content according to each block type
- C. Preserve protocol-required blocks through tool continuations
- D. Use supported thinking or effort controls after measuring task benefit

### 51. A synchronous network call blocks every request in an async web handler. What I/O approach fits?

Domain: Applications and Integration

- A. Bound work queues and apply backpressure
- B. Run independent branches concurrently and join checked results
- C. Use asynchronous I/O with bounded concurrency
- D. Wait for validated prerequisite outputs

### 52. A bulk endpoint launches unbounded model requests and exhausts connections. What concurrency mechanism is needed?

Domain: Applications and Integration

- A. Enforce task, iteration, and spending safeguards
- B. Bound work queues and apply backpressure
- C. Run independent branches concurrently and join checked results
- D. Use asynchronous I/O with bounded concurrency

### 53. An external request may wait forever because no deadline exists. What should be configured?

Domain: Applications and Integration

- A. Cancel local work and reconcile any external operation separately
- B. Retry a transient failure with bounded backoff
- C. Set explicit deadlines and classify timeout outcomes
- D. Coordinate retries across SDK and application layers

### 54. A mutation may commit before its network response is lost. What makes retries safer where supported?

Domain: Applications and Integration

- A. Set explicit deadlines and classify timeout outcomes
- B. Cancel local work and reconcile any external operation separately
- C. Use a durable idempotency key for the same logical action
- D. Validate and commit business changes through a controlled boundary

### 55. A backend returns HTTP success but business status rejected. What integration contract should the caller respect?

Domain: Applications and Integration

- A. Use a provider-specific adapter behind a stable application interface
- B. Test the integration contract at the provider boundary
- C. Build a valid Messages API request with explicit content blocks
- D. Apply HTTP method, status, authentication, and payload contracts

### 56. Mocks always return valid data, while real provider calls fail due to serialization. What testing boundary is missing?

Domain: Applications and Integration

- A. Inspect a redacted end-to-end request and tool trace
- B. Use controlled stubs for repeatable failure-path tests
- C. Use a versioned representative held-out evaluation set
- D. Test the integration contract at the provider boundary

### 57. The SDK retries automatically and the application adds another retry loop. What should control their combined behavior?

Domain: Applications and Integration

- A. Retry a transient failure with bounded backoff
- B. Bound work queues and apply backpressure
- C. Coordinate retries across SDK and application layers
- D. Set explicit deadlines and classify timeout outcomes

### 58. A user cancels locally after an external action may already have run. What should the application do?

Domain: Applications and Integration

- A. Set explicit deadlines and classify timeout outcomes
- B. Validate and commit business changes through a controlled boundary
- C. Use a durable idempotency key for the same logical action
- D. Cancel local work and reconcile any external operation separately

### 59. Support cannot link a customer failure to the corresponding model and tool calls. What should propagate across boundaries?

Domain: Applications and Integration

- A. Inspect a redacted end-to-end request and tool trace
- B. Record detected_pattern and dismissal reasons
- C. Propagate correlation identifiers across requests and tools
- D. Keep protected action and identity audit records

### 60. An AI proposal must update several related records without leaving inconsistent state. What application boundary matters?

Domain: Applications and Integration

- A. Use a durable idempotency key for the same logical action
- B. Validate and commit business changes through a controlled boundary
- C. Enforce prerequisites in trusted execution code
- D. Require authorized approval before the consequential action

### 61. A refactor changes parsing code and accidentally drops tool-use identifiers. What check should catch this regression?

Domain: Applications and Integration

- A. Test the integration contract at the provider boundary
- B. Use tests and specific failure feedback to drive iteration
- C. Use controlled stubs for repeatable failure-path tests
- D. Use a versioned representative held-out evaluation set

### 62. A deployment changes SDK, prompt, and model simultaneously without a recorded manifest. What reproducibility practice helps?

Domain: Applications and Integration

- A. Canary a version change with regression gates and rollback
- B. Separate environment configuration from application logic
- C. Version and review plugin dependencies and permissions
- D. Pin compatible model, SDK, prompt, and dependency versions

### 63. A parser rewrite works on examples but has not faced representative production responses. What rollout strategy is safer?

Domain: Applications and Integration

- A. Separate environment configuration from application logic
- B. Canary a version change with regression gates and rollback
- C. Pin compatible model, SDK, prompt, and dependency versions
- D. Use a versioned representative held-out evaluation set

### 64. An application interpolates a model-produced string directly into SQL. What software security practice should replace this?

Domain: Applications and Integration

- A. Validate extracted values against evidence and business rules
- B. Use supported strict structured output with a schema
- C. Adjust sampling variability, not factual truth
- D. Validate and encode untrusted values for their destination

### 65. Developers need repeatable overload and timeout tests without contacting live services. What test setup fits?

Domain: Applications and Integration

- A. Use tests and specific failure feedback to drive iteration
- B. Test the integration contract at the provider boundary
- C. Use a versioned representative held-out evaluation set
- D. Use controlled stubs for repeatable failure-path tests

### 66. The model emits a correct amount, but an application conversion divides it twice. What kind of defect should be isolated?

Domain: Applications and Integration

- A. Inspect a redacted end-to-end request and tool trace
- B. Isolate model-output defects from integration defects
- C. Use a versioned representative held-out evaluation set
- D. State explicit reportable and non-reportable criteria

### 67. A developer creates a coroutine but never awaits or schedules it. Which programming concept needs correction?

Domain: Applications and Integration

- A. Wait for validated prerequisite outputs
- B. Use asynchronous I/O with bounded concurrency
- C. Run independent branches concurrently and join checked results
- D. Bound work queues and apply backpressure

### 68. A provider upgrade changes an expected response field. Which boundary tests should reveal incompatibility?

Domain: Applications and Integration

- A. Use tests and specific failure feedback to drive iteration
- B. Use a versioned representative held-out evaluation set
- C. Use controlled stubs for repeatable failure-path tests
- D. Test the integration contract at the provider boundary

### 69. Two concurrent requests modify the same business record from stale snapshots. What should manage conflicts?

Domain: Applications and Integration

- A. Use a durable idempotency key for the same logical action
- B. Validate and commit business changes through a controlled boundary
- C. Enforce prerequisites in trusted execution code
- D. Require authorized approval before the consequential action

### 70. A refactor has no rollback or maintenance owner once deployed. What engineering discipline is incomplete?

Domain: Applications and Integration

- A. Canary a version change with regression gates and rollback
- B. Separate environment configuration from application logic
- C. Pin compatible model, SDK, prompt, and dependency versions
- D. Plan deployment, operation, maintenance, and retirement

### 71. An application places retrieved text beside trusted rules without distinguishing their roles. Where should trusted policy be represented?

Domain: Applications and Integration

- A. Put shared project standards in versioned CLAUDE.md
- B. Place trusted application policy in the supported system instruction field
- C. Put personal cross-project preferences in ~/.claude/CLAUDE.md
- D. Build a valid Messages API request with explicit content blocks

### 72. A developer expects a browser chat conversation to appear automatically in a separate API request. What should the application manage?

Domain: Applications and Integration

- A. Persist structured task state and pending actions
- B. Supply the relevant conversation state on subsequent requests
- C. Resume the identified session when its context remains valid
- D. Build a valid Messages API request with explicit content blocks

### 73. A downstream parser needs a supported schema instead of variable narrative text. What output mechanism should be assessed?

Domain: Applications and Integration

- A. Use supported strict structured output with a schema
- B. Specify deterministic normalization rules and preserve originals when needed
- C. Validate extracted values against evidence and business rules
- D. Build a valid Messages API request with explicit content blocks

### 74. An API result fits the schema but maps one person's data to another record. What must application validation check?

Domain: Applications and Integration

- A. Specify deterministic normalization rules and preserve originals when needed
- B. Validate extracted values against evidence and business rules
- C. Allow explicit unknown or absent values in the schema
- D. Use supported strict structured output with a schema

### 75. A source lacks an optional business detail, but the output demands a concrete value. What schema design avoids fabrication?

Domain: Applications and Integration

- A. Use supported strict structured output with a schema
- B. Allow explicit unknown or absent values in the schema
- C. Use an extensible category plus a detail field
- D. Specify deterministic normalization rules and preserve originals when needed

### 76. An extension adds new tools and changes output behavior without review. What dependency practice is needed?

Domain: Applications and Integration

- A. Separate environment configuration from application logic
- B. Use the appropriate settings.json scope for behavioral configuration
- C. Pin compatible model, SDK, prompt, and dependency versions
- D. Version and review plugin dependencies and permissions

### 77. A team assumes identical instruction behavior across Desktop, Claude Code, and a custom API app. What design principle helps?

Domain: Applications and Integration

- A. Supply the relevant conversation state on subsequent requests
- B. Place trusted application policy in the supported system instruction field
- C. Use a provider-specific adapter behind a stable application interface
- D. Build a valid Messages API request with explicit content blocks

### 78. A syntactically valid response includes HTML that the UI renders without escaping. What boundary should protect the user?

Domain: Applications and Integration

- A. Validate extracted values against evidence and business rules
- B. Specify deterministic normalization rules and preserve originals when needed
- C. Treat model output as untrusted before rendering or execution
- D. Use supported strict structured output with a schema

### 79. A model-generated recommendation must not become a database change until validated and authorized. What boundary should separate them?

Domain: Applications and Integration

- A. Validate and commit business changes through a controlled boundary
- B. Require authorized approval before the consequential action
- C. Validate extracted values against evidence and business rules
- D. Enforce prerequisites in trusted execution code

### 80. An application design copies a playground demo despite needing multi-user authorization and persistent state. What should drive redesign?

Domain: Applications and Integration

- A. Compare hosting responsibility, control, and service constraints
- B. Translate business goals into measurable functional and operational requirements
- C. Select the least costly configuration that meets required outcomes
- D. Choose a framework for needed orchestration semantics

### 81. Production accidentally uses a development endpoint hard-coded in application logic. What should be separated?

Domain: Applications and Integration

- A. Separate environment configuration from application logic
- B. Version and review plugin dependencies and permissions
- C. Use the appropriate settings.json scope for behavioral configuration
- D. Pin compatible model, SDK, prompt, and dependency versions

### 82. A moving model alias changes behavior while source code remains unchanged. What versioning choice improves reproducibility?

Domain: Applications and Integration

- A. Canary a version change with regression gates and rollback
- B. Pin compatible model, SDK, prompt, and dependency versions
- C. Route requests using evaluated task classes and safe fallbacks
- D. Select the least costly configuration that meets required outcomes

### 83. No one can identify which prompt revision produced a customer-visible regression. What should be maintained?

Domain: Applications and Integration

- A. Separate environment configuration from application logic
- B. Version exact prompt content and its dependencies
- C. Pin compatible model, SDK, prompt, and dependency versions
- D. Use a versioned representative held-out evaluation set

### 84. A team wants shared Claude Code hook and permission configuration, not only prose guidance. What configuration mechanism is relevant?

Domain: Applications and Integration

- A. Put personal cross-project preferences in ~/.claude/CLAUDE.md
- B. Organize focused conventions in .claude/rules/
- C. Put shared project standards in versioned CLAUDE.md
- D. Use the appropriate settings.json scope for behavioral configuration

### 85. A plugin dependency auto-updates and exposes unexpected capabilities. What management should have been in place?

Domain: Applications and Integration

- A. Version and review plugin dependencies and permissions
- B. Canary a version change with regression gates and rollback
- C. Separate environment configuration from application logic
- D. Pin compatible model, SDK, prompt, and dependency versions

### 86. Universal repository build guidance should be shared with every contributor. Where should contextual instructions live?

Domain: Applications and Integration

- A. Put shared project standards in versioned CLAUDE.md
- B. Put personal cross-project preferences in ~/.claude/CLAUDE.md
- C. Put an on-demand workflow in a project skill
- D. Use the appropriate settings.json scope for behavioral configuration

### 87. A new model version is available but task-specific behavior may break. What deployment practice should follow evaluation?

Domain: Applications and Integration

- A. Canary a version change with regression gates and rollback
- B. Use a versioned representative held-out evaluation set
- C. Pin compatible model, SDK, prompt, and dependency versions
- D. Separate environment configuration from application logic

### 88. An application starts with a missing required model identifier and fails on its first user request. What should happen earlier?

Domain: Applications and Integration

- A. Separate environment configuration from application logic
- B. Use the appropriate settings.json scope for behavioral configuration
- C. Version and review plugin dependencies and permissions
- D. Pin compatible model, SDK, prompt, and dependency versions

### 89. A release record includes model and prompt versions but omits the SDK and extension versions. What practice should expand?

Domain: Applications and Integration

- A. Separate environment configuration from application logic
- B. Version and review plugin dependencies and permissions
- C. Version exact prompt content and its dependencies
- D. Pin compatible model, SDK, prompt, and dependency versions

### 90. One developer's local override differs from the team's shared settings. What should troubleshooting distinguish?

Domain: Applications and Integration

- A. Organize focused conventions in .claude/rules/
- B. Put shared project standards in versioned CLAUDE.md
- C. Use the appropriate settings.json scope for behavioral configuration
- D. Put personal cross-project preferences in ~/.claude/CLAUDE.md

### 91. A request is rejected because content uses a format copied from another provider's API. What should be rebuilt?

Domain: Applications and Integration

- A. Supply the relevant conversation state on subsequent requests
- B. Dispatch response content according to each block type
- C. Build a valid Messages API request with explicit content blocks
- D. Use a provider-specific adapter behind a stable application interface

### 92. A supported visual model is called with an inaccessible local path string. What input correction is needed?

Domain: Applications and Integration

- A. Send supported image content in the documented multimodal format
- B. Use a provider-specific adapter behind a stable application interface
- C. Dispatch response content according to each block type
- D. Build a valid Messages API request with explicit content blocks

### 93. A response begins with a non-text block, and the UI displays an empty answer despite later text. What should change?

Domain: Applications and Integration

- A. Dispatch response content according to each block type
- B. Use the final assembled message and completion status
- C. Build a valid Messages API request with explicit content blocks
- D. Accumulate deltas by block index before final validation

### 94. A proxy forwards event-stream bytes but the client tries WebSocket upgrade negotiation. Which streaming contract should the client use?

Domain: Applications and Integration

- A. Consume the Messages stream as server-sent events
- B. Use asynchronous I/O with bounded concurrency
- C. Use WebSockets for an explicitly bidirectional persistent channel
- D. Apply HTTP method, status, authentication, and payload contracts

### 95. A batch manifest contains duplicate request identifiers, making results ambiguous. What correlation requirement needs repair?

Domain: Applications and Integration

- A. Resubmit only failed items after diagnosing their errors
- B. Correlate batch outcomes by custom_id
- C. Propagate correlation identifiers across requests and tools
- D. Record detected_pattern and dismissal reasons

### 96. An application has a user deadline shorter than its combined retry waits. What should govern execution?

Domain: Applications and Integration

- A. Set explicit deadlines and classify timeout outcomes
- B. Cancel local work and reconcile any external operation separately
- C. Bound work queues and apply backpressure
- D. Coordinate retries across SDK and application layers

### 97. A supposedly three-attempt operation invokes its provider many more times because the SDK also retries. What must be coordinated?

Domain: Applications and Integration

- A. Retry a transient failure with bounded backoff
- B. Coordinate retries across SDK and application layers
- C. Bound work queues and apply backpressure
- D. Set explicit deadlines and classify timeout outcomes

### 98. The UI assumes a valid structured object cannot contain a malicious display string. What boundary rule should apply?

Domain: Applications and Integration

- A. Adjust sampling variability, not factual truth
- B. Validate extracted values against evidence and business rules
- C. Treat model output as untrusted before rendering or execution
- D. Use supported strict structured output with a schema

### 99. Staging and production use different provider credentials but share the same checked application code. What separation supports this?

Domain: Applications and Integration

- A. Use the appropriate settings.json scope for behavioral configuration
- B. Separate environment configuration from application logic
- C. Pin compatible model, SDK, prompt, and dependency versions
- D. Version and review plugin dependencies and permissions

### 100. A service stops accepting traffic, but retained request logs still need governed handling. What process must include that work?

Domain: Applications and Integration

- A. Monitor production service and outcome signals
- B. Plan deployment, operation, maintenance, and retirement
- C. Canary a version change with regression gates and rollback
- D. Pin compatible model, SDK, prompt, and dependency versions

---

## Answer key and explanations

### Question 1 — A

Answer: Translate business goals into measurable functional and operational requirements. Translate the goal into checkable behavior and operational constraints before selecting technology. Specify behavior, latency, throughput, data constraints, failure policy, and acceptance criteria. A model or framework choice is not a substitute for requirements. Local study-map skill 2.1 (Understanding Requirements), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Correct. Specify behavior, latency, throughput, data constraints, failure policy, and acceptance criteria. A model or framework choice is not a substitute for requirements. In this case: Translate the goal into checkable behavior and operational constraints before selecting technology.
- **B:** Incorrect for this question. Set measurable latency, availability, and quality targets for the complete workflow. Account for dependencies and tail behavior rather than only average model speed. In this case: Translate the goal into checkable behavior and operational constraints before selecting technology.
- **C:** Incorrect for this question. Evaluate state graphs, typed validation, tracing, ecosystem, and deployment fit across frameworks such as LangGraph, Strands, or PydanticAI. A framework does not guarantee safety or correctness. In this case: Translate the goal into checkable behavior and operational constraints before selecting technology.
- **D:** Incorrect for this question. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. In this case: Translate the goal into checkable behavior and operational constraints before selecting technology.

### Question 2 — D

Answer: Define observable service-level objectives and failure behavior. Service objectives make the complete workflow's acceptable operation observable and testable. Set measurable latency, availability, and quality targets for the complete workflow. Account for dependencies and tail behavior rather than only average model speed. Local study-map skill 2.1 (Understanding Requirements), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. In this case: Service objectives make the complete workflow's acceptable operation observable and testable.
- **B:** Incorrect for this question. Specify behavior, latency, throughput, data constraints, failure policy, and acceptance criteria. A model or framework choice is not a substitute for requirements. In this case: Service objectives make the complete workflow's acceptable operation observable and testable.
- **C:** Incorrect for this question. An acceptable mean can hide slow requests that violate user requirements. Define percentile measurements and end-to-end boundaries consistently. In this case: Service objectives make the complete workflow's acceptable operation observable and testable.
- **D:** Correct. Set measurable latency, availability, and quality targets for the complete workflow. Account for dependencies and tail behavior rather than only average model speed. In this case: Service objectives make the complete workflow's acceptable operation observable and testable.

### Question 3 — C

Answer: Translate business goals into measurable functional and operational requirements. Infrastructure and data restrictions belong in requirements before implementation choices are fixed. Specify behavior, latency, throughput, data constraints, failure policy, and acceptance criteria. A model or framework choice is not a substitute for requirements. Local study-map skill 2.1 (Understanding Requirements), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. In this case: Infrastructure and data restrictions belong in requirements before implementation choices are fixed.
- **B:** Incorrect for this question. Use evidence-based routing to suitable configurations, monitor misclassification, and define fallback. Routing complexity must justify its own operating cost. In this case: Infrastructure and data restrictions belong in requirements before implementation choices are fixed.
- **C:** Correct. Specify behavior, latency, throughput, data constraints, failure policy, and acceptance criteria. A model or framework choice is not a substitute for requirements. In this case: Infrastructure and data restrictions belong in requirements before implementation choices are fixed.
- **D:** Incorrect for this question. Evaluate state graphs, typed validation, tracing, ecosystem, and deployment fit across frameworks such as LangGraph, Strands, or PydanticAI. A framework does not guarantee safety or correctness. In this case: Infrastructure and data restrictions belong in requirements before implementation choices are fixed.

### Question 4 — C

Answer: Define observable service-level objectives and failure behavior. Define end-to-end objectives and failure behavior across all required dependencies. Set measurable latency, availability, and quality targets for the complete workflow. Account for dependencies and tail behavior rather than only average model speed. Local study-map skill 2.1 (Understanding Requirements), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Streaming can improve perceived responsiveness without reducing total generation or external-tool time. First-token delay and total duration measure different things. In this case: Define end-to-end objectives and failure behavior across all required dependencies.
- **B:** Incorrect for this question. An acceptable mean can hide slow requests that violate user requirements. Define percentile measurements and end-to-end boundaries consistently. In this case: Define end-to-end objectives and failure behavior across all required dependencies.
- **C:** Correct. Set measurable latency, availability, and quality targets for the complete workflow. Account for dependencies and tail behavior rather than only average model speed. In this case: Define end-to-end objectives and failure behavior across all required dependencies.
- **D:** Incorrect for this question. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. In this case: Define end-to-end objectives and failure behavior across all required dependencies.

### Question 5 — D

Answer: Translate business goals into measurable functional and operational requirements. Functional requirements must distinguish proposed content from authorized external effects. Specify behavior, latency, throughput, data constraints, failure policy, and acceptance criteria. A model or framework choice is not a substitute for requirements. Local study-map skill 2.1 (Understanding Requirements), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Functional requirements must distinguish proposed content from authorized external effects.
- **B:** Incorrect for this question. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. In this case: Functional requirements must distinguish proposed content from authorized external effects.
- **C:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Functional requirements must distinguish proposed content from authorized external effects.
- **D:** Correct. Specify behavior, latency, throughput, data constraints, failure policy, and acceptance criteria. A model or framework choice is not a substitute for requirements. In this case: Functional requirements must distinguish proposed content from authorized external effects.

### Question 6 — B

Answer: Translate business goals into measurable functional and operational requirements. Production design needs explicit capacity and data requirements rather than demo assumptions. Specify behavior, latency, throughput, data constraints, failure policy, and acceptance criteria. A model or framework choice is not a substitute for requirements. Local study-map skill 2.1 (Understanding Requirements), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Self-hosting and managed deployment place different responsibilities on operations, networking, identity, and lifecycle. Availability and supported features must be verified. In this case: Production design needs explicit capacity and data requirements rather than demo assumptions.
- **B:** Correct. Specify behavior, latency, throughput, data constraints, failure policy, and acceptance criteria. A model or framework choice is not a substitute for requirements. In this case: Production design needs explicit capacity and data requirements rather than demo assumptions.
- **C:** Incorrect for this question. Use evidence-based routing to suitable configurations, monitor misclassification, and define fallback. Routing complexity must justify its own operating cost. In this case: Production design needs explicit capacity and data requirements rather than demo assumptions.
- **D:** Incorrect for this question. Evaluate state graphs, typed validation, tracing, ecosystem, and deployment fit across frameworks such as LangGraph, Strands, or PydanticAI. A framework does not guarantee safety or correctness. In this case: Production design needs explicit capacity and data requirements rather than demo assumptions.

### Question 7 — A

Answer: Define observable service-level objectives and failure behavior. Define observable service targets and a safe response when dependencies cannot meet them. Set measurable latency, availability, and quality targets for the complete workflow. Account for dependencies and tail behavior rather than only average model speed. Local study-map skill 2.1 (Understanding Requirements), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Correct. Set measurable latency, availability, and quality targets for the complete workflow. Account for dependencies and tail behavior rather than only average model speed. In this case: Define observable service targets and a safe response when dependencies cannot meet them.
- **B:** Incorrect for this question. An acceptable mean can hide slow requests that violate user requirements. Define percentile measurements and end-to-end boundaries consistently. In this case: Define observable service targets and a safe response when dependencies cannot meet them.
- **C:** Incorrect for this question. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. In this case: Define observable service targets and a safe response when dependencies cannot meet them.
- **D:** Incorrect for this question. Include failed attempts, retries, review, tool work, and operating overhead rather than compare only listed unit token rates. In this case: Define observable service targets and a safe response when dependencies cannot meet them.

### Question 8 — C

Answer: Translate business goals into measurable functional and operational requirements. Capture modality, integration, and privacy requirements before choosing components. Specify behavior, latency, throughput, data constraints, failure policy, and acceptance criteria. A model or framework choice is not a substitute for requirements. Local study-map skill 2.1 (Understanding Requirements), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. In this case: Capture modality, integration, and privacy requirements before choosing components.
- **B:** Incorrect for this question. Different hosting providers can use distinct authentication, endpoints, identifiers, and supported features. Normalize the application contract without assuming identical wire protocols. In this case: Capture modality, integration, and privacy requirements before choosing components.
- **C:** Correct. Specify behavior, latency, throughput, data constraints, failure policy, and acceptance criteria. A model or framework choice is not a substitute for requirements. In this case: Capture modality, integration, and privacy requirements before choosing components.
- **D:** Incorrect for this question. Evaluate state graphs, typed validation, tracing, ecosystem, and deployment fit across frameworks such as LangGraph, Strands, or PydanticAI. A framework does not guarantee safety or correctness. In this case: Capture modality, integration, and privacy requirements before choosing components.

### Question 9 — C

Answer: Translate business goals into measurable functional and operational requirements. Acceptance requirements make later implementation and evaluation judgments meaningful. Specify behavior, latency, throughput, data constraints, failure policy, and acceptance criteria. A model or framework choice is not a substitute for requirements. Local study-map skill 2.1 (Understanding Requirements), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Acceptance requirements make later implementation and evaluation judgments meaningful.
- **B:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Acceptance requirements make later implementation and evaluation judgments meaningful.
- **C:** Correct. Specify behavior, latency, throughput, data constraints, failure policy, and acceptance criteria. A model or framework choice is not a substitute for requirements. In this case: Acceptance requirements make later implementation and evaluation judgments meaningful.
- **D:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Acceptance requirements make later implementation and evaluation judgments meaningful.

### Question 10 — D

Answer: Define observable service-level objectives and failure behavior. The complete user-facing operation needs measurable objectives and explicit failure handling. Set measurable latency, availability, and quality targets for the complete workflow. Account for dependencies and tail behavior rather than only average model speed. Local study-map skill 2.1 (Understanding Requirements), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. An acceptable mean can hide slow requests that violate user requirements. Define percentile measurements and end-to-end boundaries consistently. In this case: The complete user-facing operation needs measurable objectives and explicit failure handling.
- **B:** Incorrect for this question. Bound user and dependency waits. A timeout is an uncertain execution outcome for mutations and may require status reconciliation rather than blind retry. In this case: The complete user-facing operation needs measurable objectives and explicit failure handling.
- **C:** Incorrect for this question. Streaming can improve perceived responsiveness without reducing total generation or external-tool time. First-token delay and total duration measure different things. In this case: The complete user-facing operation needs measurable objectives and explicit failure handling.
- **D:** Correct. Set measurable latency, availability, and quality targets for the complete workflow. Account for dependencies and tail behavior rather than only average model speed. In this case: The complete user-facing operation needs measurable objectives and explicit failure handling.

### Question 11 — C

Answer: Plan deployment, operation, maintenance, and retirement. A system lifecycle includes operation and maintenance beyond initial construction. Development does not end at a successful API call. Include monitoring, updates, recovery, ownership, and decommissioning in the system lifecycle. Local study-map skill 2.2 (Systems Life Cycle), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Stage exposure to the new configuration, compare required outcomes, and retain a known-good path. A vendor release note is not workload validation. In this case: A system lifecycle includes operation and maintenance beyond initial construction.
- **B:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: A system lifecycle includes operation and maintenance beyond initial construction.
- **C:** Correct. Development does not end at a successful API call. Include monitoring, updates, recovery, ownership, and decommissioning in the system lifecycle. In this case: A system lifecycle includes operation and maintenance beyond initial construction.
- **D:** Incorrect for this question. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: A system lifecycle includes operation and maintenance beyond initial construction.

### Question 12 — C

Answer: Canary a version change with regression gates and rollback. Stage exposure with regression gates and a known-good rollback path. Stage exposure to the new configuration, compare required outcomes, and retain a known-good path. A vendor release note is not workload validation. Local study-map skill 2.2 (Systems Life Cycle), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: Stage exposure with regression gates and a known-good rollback path.
- **B:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Stage exposure with regression gates and a known-good rollback path.
- **C:** Correct. Stage exposure to the new configuration, compare required outcomes, and retain a known-good path. A vendor release note is not workload validation. In this case: Stage exposure with regression gates and a known-good rollback path.
- **D:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Stage exposure with regression gates and a known-good rollback path.

### Question 13 — B

Answer: Plan deployment, operation, maintenance, and retirement. Decommissioning is part of lifecycle management rather than simply disabling the UI. Development does not end at a successful API call. Include monitoring, updates, recovery, ownership, and decommissioning in the system lifecycle. Local study-map skill 2.2 (Systems Life Cycle), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: Decommissioning is part of lifecycle management rather than simply disabling the UI.
- **B:** Correct. Development does not end at a successful API call. Include monitoring, updates, recovery, ownership, and decommissioning in the system lifecycle. In this case: Decommissioning is part of lifecycle management rather than simply disabling the UI.
- **C:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Decommissioning is part of lifecycle management rather than simply disabling the UI.
- **D:** Incorrect for this question. Plugins can change tools and workflow behavior. Track provenance, versions, compatibility, and permissions rather than install unreviewed code merely because a model suggests it. In this case: Decommissioning is part of lifecycle management rather than simply disabling the UI.

### Question 14 — A

Answer: Monitor production service and outcome signals. Monitor production outcomes instead of assuming launch-time quality remains permanent. Observe deployed latency, failures, drift, and task outcomes with accountable response thresholds. Monitoring differs from an offline evaluation or a single diagnostic trace. Local study-map skill 2.2 (Systems Life Cycle), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Correct. Observe deployed latency, failures, drift, and task outcomes with accountable response thresholds. Monitoring differs from an offline evaluation or a single diagnostic trace. In this case: Monitor production outcomes instead of assuming launch-time quality remains permanent.
- **B:** Incorrect for this question. Correlate the actual request, model response, tool execution, retries, and validation results. Diagnose the first failing boundary rather than infer cause from the final prose. In this case: Monitor production outcomes instead of assuming launch-time quality remains permanent.
- **C:** Incorrect for this question. Audit records support attribution and reconstruction of consequential actions. Limit access, sensitive content, and retention; they do not themselves block an effect. In this case: Monitor production outcomes instead of assuming launch-time quality remains permanent.
- **D:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Monitor production outcomes instead of assuming launch-time quality remains permanent.

### Question 15 — D

Answer: Checkpoint durable state at safe workflow boundaries. Persist consistent progress and pending effects at safe recovery boundaries. Recovery needs committed progress, pending actions, evidence versions, and consistent artifacts. Checkpointing conversation text alone does not establish transaction completion. Local study-map skill 2.2 (Systems Life Cycle), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Persist consistent progress and pending effects at safe recovery boundaries.
- **B:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Persist consistent progress and pending effects at safe recovery boundaries.
- **C:** Incorrect for this question. Recovery needs known state locations, completion status, source versions, and pending work. Do not infer completion merely because an output file exists. In this case: Persist consistent progress and pending effects at safe recovery boundaries.
- **D:** Correct. Recovery needs committed progress, pending actions, evidence versions, and consistent artifacts. Checkpointing conversation text alone does not establish transaction completion. In this case: Persist consistent progress and pending effects at safe recovery boundaries.

### Question 16 — C

Answer: Canary a version change with regression gates and rollback. A controlled rollout can detect regression before all users receive the change. Stage exposure to the new configuration, compare required outcomes, and retain a known-good path. A vendor release note is not workload validation. Local study-map skill 2.2 (Systems Life Cycle), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: A controlled rollout can detect regression before all users receive the change.
- **B:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: A controlled rollout can detect regression before all users receive the change.
- **C:** Correct. Stage exposure to the new configuration, compare required outcomes, and retain a known-good path. A vendor release note is not workload validation. In this case: A controlled rollout can detect regression before all users receive the change.
- **D:** Incorrect for this question. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: A controlled rollout can detect regression before all users receive the change.

### Question 17 — A

Answer: Plan deployment, operation, maintenance, and retirement. Lifecycle ownership includes updates, support, monitoring, and eventual retirement. Development does not end at a successful API call. Include monitoring, updates, recovery, ownership, and decommissioning in the system lifecycle. Local study-map skill 2.2 (Systems Life Cycle), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Correct. Development does not end at a successful API call. Include monitoring, updates, recovery, ownership, and decommissioning in the system lifecycle. In this case: Lifecycle ownership includes updates, support, monitoring, and eventual retirement.
- **B:** Incorrect for this question. Evaluate state graphs, typed validation, tracing, ecosystem, and deployment fit across frameworks such as LangGraph, Strands, or PydanticAI. A framework does not guarantee safety or correctness. In this case: Lifecycle ownership includes updates, support, monitoring, and eventual retirement.
- **C:** Incorrect for this question. Self-hosting and managed deployment place different responsibilities on operations, networking, identity, and lifecycle. Availability and supported features must be verified. In this case: Lifecycle ownership includes updates, support, monitoring, and eventual retirement.
- **D:** Incorrect for this question. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. In this case: Lifecycle ownership includes updates, support, monitoring, and eventual retirement.

### Question 18 — A

Answer: Activate coordinated incident response and recovery. Containment, investigation, recovery, and communication require a defined incident response. Contain verified harm, investigate affected systems and data, recover safely, and communicate through accountable owners. Observation alone is not containment. Local study-map skill 2.2 (Systems Life Cycle), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Correct. Contain verified harm, investigate affected systems and data, recover safely, and communicate through accountable owners. Observation alone is not containment. In this case: Containment, investigation, recovery, and communication require a defined incident response.
- **B:** Incorrect for this question. Observe deployed latency, failures, drift, and task outcomes with accountable response thresholds. Monitoring differs from an offline evaluation or a single diagnostic trace. In this case: Containment, investigation, recovery, and communication require a defined incident response.
- **C:** Incorrect for this question. Audit records support attribution and reconstruction of consequential actions. Limit access, sensitive content, and retention; they do not themselves block an effect. In this case: Containment, investigation, recovery, and communication require a defined incident response.
- **D:** Incorrect for this question. Correlate the actual request, model response, tool execution, retries, and validation results. Diagnose the first failing boundary rather than infer cause from the final prose. In this case: Containment, investigation, recovery, and communication require a defined incident response.

### Question 19 — A

Answer: Pin compatible model, SDK, prompt, and dependency versions. Track behavior-relevant versions so a deployed configuration can be identified. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. Local study-map skill 2.2 (Systems Life Cycle), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Correct. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Track behavior-relevant versions so a deployed configuration can be identified.
- **B:** Incorrect for this question. Plugins can change tools and workflow behavior. Track provenance, versions, compatibility, and permissions rather than install unreviewed code merely because a model suggests it. In this case: Track behavior-relevant versions so a deployed configuration can be identified.
- **C:** Incorrect for this question. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: Track behavior-relevant versions so a deployed configuration can be identified.
- **D:** Incorrect for this question. Stage exposure to the new configuration, compare required outcomes, and retain a known-good path. A vendor release note is not workload validation. In this case: Track behavior-relevant versions so a deployed configuration can be identified.

### Question 20 — B

Answer: Plan deployment, operation, maintenance, and retirement. Controlled retirement and migration belong in the system lifecycle from planning onward. Development does not end at a successful API call. Include monitoring, updates, recovery, ownership, and decommissioning in the system lifecycle. Local study-map skill 2.2 (Systems Life Cycle), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Stage exposure to the new configuration, compare required outcomes, and retain a known-good path. A vendor release note is not workload validation. In this case: Controlled retirement and migration belong in the system lifecycle from planning onward.
- **B:** Correct. Development does not end at a successful API call. Include monitoring, updates, recovery, ownership, and decommissioning in the system lifecycle. In this case: Controlled retirement and migration belong in the system lifecycle from planning onward.
- **C:** Incorrect for this question. Self-hosting and managed deployment place different responsibilities on operations, networking, identity, and lifecycle. Availability and supported features must be verified. In this case: Controlled retirement and migration belong in the system lifecycle from planning onward.
- **D:** Incorrect for this question. Evaluate state graphs, typed validation, tracing, ecosystem, and deployment fit across frameworks such as LangGraph, Strands, or PydanticAI. A framework does not guarantee safety or correctness. In this case: Controlled retirement and migration belong in the system lifecycle from planning onward.

### Question 21 — C

Answer: Build a valid Messages API request with explicit content blocks. Construct a request that follows the chosen Messages API contract. Use the selected API contract for model, instructions, messages, and typed content. Do not assume a consumer chat interface and a developer API share implicit state. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Keep trusted instructions separate from user and retrieved data. On the direct Messages API, system instructions use the top-level system parameter rather than a system-role entry in messages. In this case: Construct a request that follows the chosen Messages API contract.
- **B:** Incorrect for this question. Different hosting providers can use distinct authentication, endpoints, identifiers, and supported features. Normalize the application contract without assuming identical wire protocols. In this case: Construct a request that follows the chosen Messages API contract.
- **C:** Correct. Use the selected API contract for model, instructions, messages, and typed content. Do not assume a consumer chat interface and a developer API share implicit state. In this case: Construct a request that follows the chosen Messages API contract.
- **D:** Incorrect for this question. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. In this case: Construct a request that follows the chosen Messages API contract.

### Question 22 — A

Answer: Place trusted application policy in the supported system instruction field. Use the supported top-level system field for trusted application policy. Keep trusted instructions separate from user and retrieved data. On the direct Messages API, system instructions use the top-level system parameter rather than a system-role entry in messages. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Correct. Keep trusted instructions separate from user and retrieved data. On the direct Messages API, system instructions use the top-level system parameter rather than a system-role entry in messages. In this case: Use the supported top-level system field for trusted application policy.
- **B:** Incorrect for this question. Use the selected API contract for model, instructions, messages, and typed content. Do not assume a consumer chat interface and a developer API share implicit state. In this case: Use the supported top-level system field for trusted application policy.
- **C:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: Use the supported top-level system field for trusted application policy.
- **D:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Use the supported top-level system field for trusted application policy.

### Question 23 — B

Answer: Dispatch response content according to each block type. Dispatch typed content blocks instead of assuming every block is display text. A response can contain text, tool use, thinking, or other supported blocks. Do not assume content is one string or that the first block is always displayable text. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. SDK accumulation helpers can provide the complete message. Inspect termination and errors before treating the resulting object as accepted application output. In this case: Dispatch typed content blocks instead of assuming every block is display text.
- **B:** Correct. A response can contain text, tool use, thinking, or other supported blocks. Do not assume content is one string or that the first block is always displayable text. In this case: Dispatch typed content blocks instead of assuming every block is display text.
- **C:** Incorrect for this question. Network chunks and content deltas can contain partial strings or JSON. Track event and block boundaries or use SDK helpers before consuming a complete structured value. In this case: Dispatch typed content blocks instead of assuming every block is display text.
- **D:** Incorrect for this question. Use the selected API contract for model, instructions, messages, and typed content. Do not assume a consumer chat interface and a developer API share implicit state. In this case: Dispatch typed content blocks instead of assuming every block is display text.

### Question 24 — D

Answer: Supply the relevant conversation state on subsequent requests. Stateless request flows need relevant explicit history or accurate state. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Stateless request flows need relevant explicit history or accurate state.
- **B:** Incorrect for this question. Use the selected API contract for model, instructions, messages, and typed content. Do not assume a consumer chat interface and a developer API share implicit state. In this case: Stateless request flows need relevant explicit history or accurate state.
- **C:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Stateless request flows need relevant explicit history or accurate state.
- **D:** Correct. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. In this case: Stateless request flows need relevant explicit history or accurate state.

### Question 25 — A

Answer: Append the assistant tool-use blocks and matching tool results. Preserve the tool-use request and matching result in valid message history. Client-tool observations must be returned with the correct tool-use identifiers in a valid message sequence so Claude can use actual results. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Correct. Client-tool observations must be returned with the correct tool-use identifiers in a valid message sequence so Claude can use actual results. In this case: Preserve the tool-use request and matching result in valid message history.
- **B:** Incorrect for this question. Use the selected API contract for model, instructions, messages, and typed content. Do not assume a consumer chat interface and a developer API share implicit state. In this case: Preserve the tool-use request and matching result in valid message history.
- **C:** Incorrect for this question. A response can contain text, tool use, thinking, or other supported blocks. Do not assume content is one string or that the first block is always displayable text. In this case: Preserve the tool-use request and matching result in valid message history.
- **D:** Incorrect for this question. SDK accumulation helpers can provide the complete message. Inspect termination and errors before treating the resulting object as accepted application output. In this case: Preserve the tool-use request and matching result in valid message history.

### Question 26 — C

Answer: Use a provider-specific adapter behind a stable application interface. Provider contracts can differ even when the underlying model family is similar. Different hosting providers can use distinct authentication, endpoints, identifiers, and supported features. Normalize the application contract without assuming identical wire protocols. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Provider contracts can differ even when the underlying model family is similar.
- **B:** Incorrect for this question. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: Provider contracts can differ even when the underlying model family is similar.
- **C:** Correct. Different hosting providers can use distinct authentication, endpoints, identifiers, and supported features. Normalize the application contract without assuming identical wire protocols. In this case: Provider contracts can differ even when the underlying model family is similar.
- **D:** Incorrect for this question. Use the selected API contract for model, instructions, messages, and typed content. Do not assume a consumer chat interface and a developer API share implicit state. In this case: Provider contracts can differ even when the underlying model family is similar.

### Question 27 — C

Answer: Use the final assembled message and completion status. Use the assembled object and its completion status, not a partial fragment. SDK accumulation helpers can provide the complete message. Inspect termination and errors before treating the resulting object as accepted application output. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. A max_tokens stop can leave content incomplete. Inspect the response and recover appropriately instead of treating it as normal completion. In this case: Use the assembled object and its completion status, not a partial fragment.
- **B:** Incorrect for this question. This indicates ordinary turn completion, not that every business objective or external action succeeded. Application acceptance checks still apply. In this case: Use the assembled object and its completion status, not a partial fragment.
- **C:** Correct. SDK accumulation helpers can provide the complete message. Inspect termination and errors before treating the resulting object as accepted application output. In this case: Use the assembled object and its completion status, not a partial fragment.
- **D:** Incorrect for this question. A response can contain text, tool use, thinking, or other supported blocks. Do not assume content is one string or that the first block is always displayable text. In this case: Use the assembled object and its completion status, not a partial fragment.

### Question 28 — D

Answer: Handle the output limit as an incomplete response. An output-limit stop is incomplete rather than successful ordinary completion. A max_tokens stop can leave content incomplete. Inspect the response and recover appropriately instead of treating it as normal completion. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. This indicates ordinary turn completion, not that every business objective or external action succeeded. Application acceptance checks still apply. In this case: An output-limit stop is incomplete rather than successful ordinary completion.
- **B:** Incorrect for this question. The loop follows protocol stop reasons, executes permitted requested tools, and returns observations before continuing. Text appearing in a response does not establish completion. In this case: An output-limit stop is incomplete rather than successful ordinary completion.
- **C:** Incorrect for this question. SDK accumulation helpers can provide the complete message. Inspect termination and errors before treating the resulting object as accepted application output. In this case: An output-limit stop is incomplete rather than successful ordinary completion.
- **D:** Correct. A max_tokens stop can leave content incomplete. Inspect the response and recover appropriately instead of treating it as normal completion. In this case: An output-limit stop is incomplete rather than successful ordinary completion.

### Question 29 — A

Answer: Inspect stop_reason and dispatch the appropriate branch. Use the documented stop state instead of equating nonempty text with completion. The loop follows protocol stop reasons, executes permitted requested tools, and returns observations before continuing. Text appearing in a response does not establish completion. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Correct. The loop follows protocol stop reasons, executes permitted requested tools, and returns observations before continuing. Text appearing in a response does not establish completion. In this case: Use the documented stop state instead of equating nonempty text with completion.
- **B:** Incorrect for this question. A response can contain text, tool use, thinking, or other supported blocks. Do not assume content is one string or that the first block is always displayable text. In this case: Use the documented stop state instead of equating nonempty text with completion.
- **C:** Incorrect for this question. This indicates ordinary turn completion, not that every business objective or external action succeeded. Application acceptance checks still apply. In this case: Use the documented stop state instead of equating nonempty text with completion.
- **D:** Incorrect for this question. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. In this case: Use the documented stop state instead of equating nonempty text with completion.

### Question 30 — D

Answer: Preserve protocol-required blocks through tool continuations. Follow the model-specific continuation contract rather than edit protocol-protected content. When a model or feature requires returned context or signed thinking blocks, follow that version-specific contract. Do not edit signed blocks or manufacture hidden reasoning. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. A response can contain text, tool use, thinking, or other supported blocks. Do not assume content is one string or that the first block is always displayable text. In this case: Follow the model-specific continuation contract rather than edit protocol-protected content.
- **B:** Incorrect for this question. Client-tool observations must be returned with the correct tool-use identifiers in a valid message sequence so Claude can use actual results. In this case: Follow the model-specific continuation contract rather than edit protocol-protected content.
- **C:** Incorrect for this question. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. In this case: Follow the model-specific continuation contract rather than edit protocol-protected content.
- **D:** Correct. When a model or feature requires returned context or signed thinking blocks, follow that version-specific contract. Do not edit signed blocks or manufacture hidden reasoning. In this case: Follow the model-specific continuation contract rather than edit protocol-protected content.

### Question 31 — D

Answer: Consume the Messages stream as server-sent events. The documented Messages streaming interface emits server-sent events over HTTP. The documented streaming interface emits SSE events over HTTP. It is not inherently a WebSocket connection or one valid JSON object per arbitrary network chunk. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. A REST integration must respect its actual endpoint contract. HTTP 200 does not establish that the requested business operation succeeded semantically. In this case: The documented Messages streaming interface emits server-sent events over HTTP.
- **B:** Incorrect for this question. WebSockets can fit bidirectional application communication, but the documented standard Messages streaming interface is SSE. Do not confuse a transport choice with model capability. In this case: The documented Messages streaming interface emits server-sent events over HTTP.
- **C:** Incorrect for this question. Await network operations without blocking an event loop, while limiting in-flight work and respecting service capacity. Creating a coroutine does not mean it has run. In this case: The documented Messages streaming interface emits server-sent events over HTTP.
- **D:** Correct. The documented streaming interface emits SSE events over HTTP. It is not inherently a WebSocket connection or one valid JSON object per arbitrary network chunk. In this case: The documented Messages streaming interface emits server-sent events over HTTP.

### Question 32 — C

Answer: Accumulate deltas by block index before final validation. Accumulate by block boundaries or use SDK helpers before final parsing and validation. Network chunks and content deltas can contain partial strings or JSON. Track event and block boundaries or use SDK helpers before consuming a complete structured value. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. A response can contain text, tool use, thinking, or other supported blocks. Do not assume content is one string or that the first block is always displayable text. In this case: Accumulate by block boundaries or use SDK helpers before final parsing and validation.
- **B:** Incorrect for this question. The documented streaming interface emits SSE events over HTTP. It is not inherently a WebSocket connection or one valid JSON object per arbitrary network chunk. In this case: Accumulate by block boundaries or use SDK helpers before final parsing and validation.
- **C:** Correct. Network chunks and content deltas can contain partial strings or JSON. Track event and block boundaries or use SDK helpers before consuming a complete structured value. In this case: Accumulate by block boundaries or use SDK helpers before final parsing and validation.
- **D:** Incorrect for this question. SDK accumulation helpers can provide the complete message. Inspect termination and errors before treating the resulting object as accepted application output. In this case: Accumulate by block boundaries or use SDK helpers before final parsing and validation.

### Question 33 — B

Answer: Handle errors after streaming has already begun. A successful initial response does not prove the stream completed normally. A successful HTTP setup does not prove stream completion. Detect error events or interrupted streams, preserve status, and avoid publishing partial results as final success. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. A max_tokens stop can leave content incomplete. Inspect the response and recover appropriately instead of treating it as normal completion. In this case: A successful initial response does not prove the stream completed normally.
- **B:** Correct. A successful HTTP setup does not prove stream completion. Detect error events or interrupted streams, preserve status, and avoid publishing partial results as final success. In this case: A successful initial response does not prove the stream completed normally.
- **C:** Incorrect for this question. This indicates ordinary turn completion, not that every business objective or external action succeeded. Application acceptance checks still apply. In this case: A successful initial response does not prove the stream completed normally.
- **D:** Incorrect for this question. SDK accumulation helpers can provide the complete message. Inspect termination and errors before treating the resulting object as accepted application output. In this case: A successful initial response does not prove the stream completed normally.

### Question 34 — A

Answer: Accumulate deltas by block index before final validation. Track block indexes and event types rather than concatenate all bytes indiscriminately. Network chunks and content deltas can contain partial strings or JSON. Track event and block boundaries or use SDK helpers before consuming a complete structured value. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Correct. Network chunks and content deltas can contain partial strings or JSON. Track event and block boundaries or use SDK helpers before consuming a complete structured value. In this case: Track block indexes and event types rather than concatenate all bytes indiscriminately.
- **B:** Incorrect for this question. A response can contain text, tool use, thinking, or other supported blocks. Do not assume content is one string or that the first block is always displayable text. In this case: Track block indexes and event types rather than concatenate all bytes indiscriminately.
- **C:** Incorrect for this question. The documented streaming interface emits SSE events over HTTP. It is not inherently a WebSocket connection or one valid JSON object per arbitrary network chunk. In this case: Track block indexes and event types rather than concatenate all bytes indiscriminately.
- **D:** Incorrect for this question. SDK accumulation helpers can provide the complete message. Inspect termination and errors before treating the resulting object as accepted application output. In this case: Track block indexes and event types rather than concatenate all bytes indiscriminately.

### Question 35 — A

Answer: Use the final assembled message and completion status. A final-message accumulation helper can assemble the streamed response for inspection. SDK accumulation helpers can provide the complete message. Inspect termination and errors before treating the resulting object as accepted application output. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Correct. SDK accumulation helpers can provide the complete message. Inspect termination and errors before treating the resulting object as accepted application output. In this case: A final-message accumulation helper can assemble the streamed response for inspection.
- **B:** Incorrect for this question. This indicates ordinary turn completion, not that every business objective or external action succeeded. Application acceptance checks still apply. In this case: A final-message accumulation helper can assemble the streamed response for inspection.
- **C:** Incorrect for this question. Network chunks and content deltas can contain partial strings or JSON. Track event and block boundaries or use SDK helpers before consuming a complete structured value. In this case: A final-message accumulation helper can assemble the streamed response for inspection.
- **D:** Incorrect for this question. A response can contain text, tool use, thinking, or other supported blocks. Do not assume content is one string or that the first block is always displayable text. In this case: A final-message accumulation helper can assemble the streamed response for inspection.

### Question 36 — A

Answer: Handle errors after streaming has already begun. Treat interrupted streaming as incomplete and handle recovery explicitly. A successful HTTP setup does not prove stream completion. Detect error events or interrupted streams, preserve status, and avoid publishing partial results as final success. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Correct. A successful HTTP setup does not prove stream completion. Detect error events or interrupted streams, preserve status, and avoid publishing partial results as final success. In this case: Treat interrupted streaming as incomplete and handle recovery explicitly.
- **B:** Incorrect for this question. A max_tokens stop can leave content incomplete. Inspect the response and recover appropriately instead of treating it as normal completion. In this case: Treat interrupted streaming as incomplete and handle recovery explicitly.
- **C:** Incorrect for this question. SDK accumulation helpers can provide the complete message. Inspect termination and errors before treating the resulting object as accepted application output. In this case: Treat interrupted streaming as incomplete and handle recovery explicitly.
- **D:** Incorrect for this question. This indicates ordinary turn completion, not that every business objective or external action succeeded. Application acceptance checks still apply. In this case: Treat interrupted streaming as incomplete and handle recovery explicitly.

### Question 37 — B

Answer: Consume the Messages stream as server-sent events. Parse SSE event boundaries because arbitrary network chunks need not align with messages. The documented streaming interface emits SSE events over HTTP. It is not inherently a WebSocket connection or one valid JSON object per arbitrary network chunk. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. A REST integration must respect its actual endpoint contract. HTTP 200 does not establish that the requested business operation succeeded semantically. In this case: Parse SSE event boundaries because arbitrary network chunks need not align with messages.
- **B:** Correct. The documented streaming interface emits SSE events over HTTP. It is not inherently a WebSocket connection or one valid JSON object per arbitrary network chunk. In this case: Parse SSE event boundaries because arbitrary network chunks need not align with messages.
- **C:** Incorrect for this question. Await network operations without blocking an event loop, while limiting in-flight work and respecting service capacity. Creating a coroutine does not mean it has run. In this case: Parse SSE event boundaries because arbitrary network chunks need not align with messages.
- **D:** Incorrect for this question. WebSockets can fit bidirectional application communication, but the documented standard Messages streaming interface is SSE. Do not confuse a transport choice with model capability. In this case: Parse SSE event boundaries because arbitrary network chunks need not align with messages.

### Question 38 — A

Answer: Dispatch response content according to each block type. Display and processing must depend on block type rather than treat every payload as ordinary text. A response can contain text, tool use, thinking, or other supported blocks. Do not assume content is one string or that the first block is always displayable text. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Correct. A response can contain text, tool use, thinking, or other supported blocks. Do not assume content is one string or that the first block is always displayable text. In this case: Display and processing must depend on block type rather than treat every payload as ordinary text.
- **B:** Incorrect for this question. SDK accumulation helpers can provide the complete message. Inspect termination and errors before treating the resulting object as accepted application output. In this case: Display and processing must depend on block type rather than treat every payload as ordinary text.
- **C:** Incorrect for this question. When a model or feature requires returned context or signed thinking blocks, follow that version-specific contract. Do not edit signed blocks or manufacture hidden reasoning. In this case: Display and processing must depend on block type rather than treat every payload as ordinary text.
- **D:** Incorrect for this question. Network chunks and content deltas can contain partial strings or JSON. Track event and block boundaries or use SDK helpers before consuming a complete structured value. In this case: Display and processing must depend on block type rather than treat every payload as ordinary text.

### Question 39 — D

Answer: Handle errors after streaming has already begun. Detect in-stream errors instead of relying solely on the initial HTTP status. A successful HTTP setup does not prove stream completion. Detect error events or interrupted streams, preserve status, and avoid publishing partial results as final success. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. SDK accumulation helpers can provide the complete message. Inspect termination and errors before treating the resulting object as accepted application output. In this case: Detect in-stream errors instead of relying solely on the initial HTTP status.
- **B:** Incorrect for this question. The loop follows protocol stop reasons, executes permitted requested tools, and returns observations before continuing. Text appearing in a response does not establish completion. In this case: Detect in-stream errors instead of relying solely on the initial HTTP status.
- **C:** Incorrect for this question. This indicates ordinary turn completion, not that every business objective or external action succeeded. Application acceptance checks still apply. In this case: Detect in-stream errors instead of relying solely on the initial HTTP status.
- **D:** Correct. A successful HTTP setup does not prove stream completion. Detect error events or interrupted streams, preserve status, and avoid publishing partial results as final success. In this case: Detect in-stream errors instead of relying solely on the initial HTTP status.

### Question 40 — D

Answer: Accumulate deltas by block index before final validation. Fragments must be assembled at the correct block boundary before complete validation. Network chunks and content deltas can contain partial strings or JSON. Track event and block boundaries or use SDK helpers before consuming a complete structured value. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. The documented streaming interface emits SSE events over HTTP. It is not inherently a WebSocket connection or one valid JSON object per arbitrary network chunk. In this case: Fragments must be assembled at the correct block boundary before complete validation.
- **B:** Incorrect for this question. SDK accumulation helpers can provide the complete message. Inspect termination and errors before treating the resulting object as accepted application output. In this case: Fragments must be assembled at the correct block boundary before complete validation.
- **C:** Incorrect for this question. A response can contain text, tool use, thinking, or other supported blocks. Do not assume content is one string or that the first block is always displayable text. In this case: Fragments must be assembled at the correct block boundary before complete validation.
- **D:** Correct. Network chunks and content deltas can contain partial strings or JSON. Track event and block boundaries or use SDK helpers before consuming a complete structured value. In this case: Fragments must be assembled at the correct block boundary before complete validation.

### Question 41 — D

Answer: Send supported image content in the documented multimodal format. Supply actual supported image content or a documented source to a compatible model. Image understanding requires an actual supported image block or source, a compatible model, and valid media limits. A text filename alone does not provide image pixels. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Use the selected API contract for model, instructions, messages, and typed content. Do not assume a consumer chat interface and a developer API share implicit state. In this case: Supply actual supported image content or a documented source to a compatible model.
- **B:** Incorrect for this question. A response can contain text, tool use, thinking, or other supported blocks. Do not assume content is one string or that the first block is always displayable text. In this case: Supply actual supported image content or a documented source to a compatible model.
- **C:** Incorrect for this question. Different hosting providers can use distinct authentication, endpoints, identifiers, and supported features. Normalize the application contract without assuming identical wire protocols. In this case: Supply actual supported image content or a documented source to a compatible model.
- **D:** Correct. Image understanding requires an actual supported image block or source, a compatible model, and valid media limits. A text filename alone does not provide image pixels. In this case: Supply actual supported image content or a documented source to a compatible model.

### Question 42 — D

Answer: Send supported image content in the documented multimodal format. The multimodal input must follow supported media and encoding requirements. Image understanding requires an actual supported image block or source, a compatible model, and valid media limits. A text filename alone does not provide image pixels. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Use the selected API contract for model, instructions, messages, and typed content. Do not assume a consumer chat interface and a developer API share implicit state. In this case: The multimodal input must follow supported media and encoding requirements.
- **B:** Incorrect for this question. Different hosting providers can use distinct authentication, endpoints, identifiers, and supported features. Normalize the application contract without assuming identical wire protocols. In this case: The multimodal input must follow supported media and encoding requirements.
- **C:** Incorrect for this question. A response can contain text, tool use, thinking, or other supported blocks. Do not assume content is one string or that the first block is always displayable text. In this case: The multimodal input must follow supported media and encoding requirements.
- **D:** Correct. Image understanding requires an actual supported image block or source, a compatible model, and valid media limits. A text filename alone does not provide image pixels. In this case: The multimodal input must follow supported media and encoding requirements.

### Question 43 — D

Answer: Use supported thinking or effort controls after measuring task benefit. Thinking and effort features must match the specific model and hosting provider. Reasoning-related features and parameters vary by model and provider. Evaluate quality, latency, and cost rather than assume every release accepts the same switches. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Thinking and effort features must match the specific model and hosting provider.
- **B:** Incorrect for this question. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. In this case: Thinking and effort features must match the specific model and hosting provider.
- **C:** Incorrect for this question. Temperature changes next-token sampling behavior where supported. Lowering it does not independently guarantee correct extraction, grounding, or identical execution. In this case: Thinking and effort features must match the specific model and hosting provider.
- **D:** Correct. Reasoning-related features and parameters vary by model and provider. Evaluate quality, latency, and cost rather than assume every release accepts the same switches. In this case: Thinking and effort features must match the specific model and hosting provider.

### Question 44 — B

Answer: Put eligible stable common content before variable input for cache reuse. Eligible prefix reuse can reduce repeated processing without sharing final user answers. Supported prefix caching depends on exact eligible content, placement, checkpoints, model, and service rules. It is not a cross-user final-answer cache. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. A token-count endpoint or compatible estimator can help plan requests. Include hidden overhead allowed by the documented interface and verify actual usage afterward. In this case: Eligible prefix reuse can reduce repeated processing without sharing final user answers.
- **B:** Correct. Supported prefix caching depends on exact eligible content, placement, checkpoints, model, and service rules. It is not a cross-user final-answer cache. In this case: Eligible prefix reuse can reduce repeated processing without sharing final user answers.
- **C:** Incorrect for this question. Repeated text does not prove cache reuse. Check eligible matching, expiration, thresholds, and current prices before claiming savings. In this case: Eligible prefix reuse can reduce repeated processing without sharing final user answers.
- **D:** Incorrect for this question. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. In this case: Eligible prefix reuse can reduce repeated processing without sharing final user answers.

### Question 45 — C

Answer: Use Message Batches for latency-tolerant independent requests. Batch processing can suit independent latency-tolerant work under current service terms. Asynchronous batches fit non-blocking workloads. The retrieved guide describes discounted processing and a window up to 24 hours, not a guaranteed latency SLA. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Blocking user or pre-merge flows need an appropriate timely request path. Synchronous execution still needs timeouts and failure policy. In this case: Batch processing can suit independent latency-tolerant work under current service terms.
- **B:** Incorrect for this question. Limit queued and active work so slow consumers or provider limits do not exhaust memory or connections. Unbounded parallelism is not a capacity plan. In this case: Batch processing can suit independent latency-tolerant work under current service terms.
- **C:** Correct. Asynchronous batches fit non-blocking workloads. The retrieved guide describes discounted processing and a window up to 24 hours, not a guaranteed latency SLA. In this case: Batch processing can suit independent latency-tolerant work under current service terms.
- **D:** Incorrect for this question. Await network operations without blocking an event loop, while limiting in-flight work and respecting service capacity. Creating a coroutine does not mean it has run. In this case: Batch processing can suit independent latency-tolerant work under current service terms.

### Question 46 — A

Answer: Use synchronous requests for blocking latency-sensitive work. Use a latency-appropriate synchronous flow rather than rely on asynchronous batch timing. Blocking user or pre-merge flows need an appropriate timely request path. Synchronous execution still needs timeouts and failure policy. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Correct. Blocking user or pre-merge flows need an appropriate timely request path. Synchronous execution still needs timeouts and failure policy. In this case: Use a latency-appropriate synchronous flow rather than rely on asynchronous batch timing.
- **B:** Incorrect for this question. Asynchronous batches fit non-blocking workloads. The retrieved guide describes discounted processing and a window up to 24 hours, not a guaranteed latency SLA. In this case: Use a latency-appropriate synchronous flow rather than rely on asynchronous batch timing.
- **C:** Incorrect for this question. Await network operations without blocking an event loop, while limiting in-flight work and respecting service capacity. Creating a coroutine does not mean it has run. In this case: Use a latency-appropriate synchronous flow rather than rely on asynchronous batch timing.
- **D:** Incorrect for this question. The documented streaming interface emits SSE events over HTTP. It is not inherently a WebSocket connection or one valid JSON object per arbitrary network chunk. In this case: Use a latency-appropriate synchronous flow rather than rely on asynchronous batch timing.

### Question 47 — C

Answer: Correlate batch outcomes by custom_id. Stable custom IDs connect outcomes to inputs without assuming result order. Stable unique request identifiers connect results to inputs without assuming arrival order. Validate uniqueness and retain a manifest. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Link a user task to provider requests, worker runs, and actions without using sensitive content as an identifier. Protect telemetry access and retention. In this case: Stable custom IDs connect outcomes to inputs without assuming result order.
- **B:** Incorrect for this question. Targeted resubmission avoids repeating successes and allows input fixes. Track identities and protect downstream effects against duplicate processing. In this case: Stable custom IDs connect outcomes to inputs without assuming result order.
- **C:** Correct. Stable unique request identifiers connect results to inputs without assuming arrival order. Validate uniqueness and retain a manifest. In this case: Stable custom IDs connect outcomes to inputs without assuming result order.
- **D:** Incorrect for this question. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: Stable custom IDs connect outcomes to inputs without assuming result order.

### Question 48 — D

Answer: Resubmit only failed items after diagnosing their errors. Diagnose and repair failed items rather than repeat all successful work. Targeted resubmission avoids repeating successes and allows input fixes. Track identities and protect downstream effects against duplicate processing. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Stable unique request identifiers connect results to inputs without assuming arrival order. Validate uniqueness and retain a manifest. In this case: Diagnose and repair failed items rather than repeat all successful work.
- **B:** Incorrect for this question. A small development sample reveals systematic extraction problems before multiplying them across the full dataset. Independent evaluation is still needed. In this case: Diagnose and repair failed items rather than repeat all successful work.
- **C:** Incorrect for this question. Asynchronous batches fit non-blocking workloads. The retrieved guide describes discounted processing and a window up to 24 hours, not a guaranteed latency SLA. In this case: Diagnose and repair failed items rather than repeat all successful work.
- **D:** Correct. Targeted resubmission avoids repeating successes and allows input fixes. Track identities and protect downstream effects against duplicate processing. In this case: Diagnose and repair failed items rather than repeat all successful work.

### Question 49 — C

Answer: Use a provider-specific adapter behind a stable application interface. Provider support and request contracts must be verified rather than inferred from model branding. Different hosting providers can use distinct authentication, endpoints, identifiers, and supported features. Normalize the application contract without assuming identical wire protocols. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Image understanding requires an actual supported image block or source, a compatible model, and valid media limits. A text filename alone does not provide image pixels. In this case: Provider support and request contracts must be verified rather than inferred from model branding.
- **B:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Provider support and request contracts must be verified rather than inferred from model branding.
- **C:** Correct. Different hosting providers can use distinct authentication, endpoints, identifiers, and supported features. Normalize the application contract without assuming identical wire protocols. In this case: Provider support and request contracts must be verified rather than inferred from model branding.
- **D:** Incorrect for this question. Reasoning-related features and parameters vary by model and provider. Evaluate quality, latency, and cost rather than assume every release accepts the same switches. In this case: Provider support and request contracts must be verified rather than inferred from model branding.

### Question 50 — C

Answer: Preserve protocol-required blocks through tool continuations. Preserve protocol-required blocks exactly as documented for that feature and release. When a model or feature requires returned context or signed thinking blocks, follow that version-specific contract. Do not edit signed blocks or manufacture hidden reasoning. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. In this case: Preserve protocol-required blocks exactly as documented for that feature and release.
- **B:** Incorrect for this question. A response can contain text, tool use, thinking, or other supported blocks. Do not assume content is one string or that the first block is always displayable text. In this case: Preserve protocol-required blocks exactly as documented for that feature and release.
- **C:** Correct. When a model or feature requires returned context or signed thinking blocks, follow that version-specific contract. Do not edit signed blocks or manufacture hidden reasoning. In this case: Preserve protocol-required blocks exactly as documented for that feature and release.
- **D:** Incorrect for this question. Reasoning-related features and parameters vary by model and provider. Evaluate quality, latency, and cost rather than assume every release accepts the same switches. In this case: Preserve protocol-required blocks exactly as documented for that feature and release.

### Question 51 — C

Answer: Use asynchronous I/O with bounded concurrency. Await asynchronous I/O instead of blocking the event loop during network waits. Await network operations without blocking an event loop, while limiting in-flight work and respecting service capacity. Creating a coroutine does not mean it has run. Local study-map skill 2.4 (Software Engineering Foundations), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Limit queued and active work so slow consumers or provider limits do not exhaust memory or connections. Unbounded parallelism is not a capacity plan. In this case: Await asynchronous I/O instead of blocking the event loop during network waits.
- **B:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Await asynchronous I/O instead of blocking the event loop during network waits.
- **C:** Correct. Await network operations without blocking an event loop, while limiting in-flight work and respecting service capacity. Creating a coroutine does not mean it has run. In this case: Await asynchronous I/O instead of blocking the event loop during network waits.
- **D:** Incorrect for this question. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: Await asynchronous I/O instead of blocking the event loop during network waits.

### Question 52 — B

Answer: Bound work queues and apply backpressure. Bound active work and queued demand rather than assume unlimited parallelism is efficient. Limit queued and active work so slow consumers or provider limits do not exhaust memory or connections. Unbounded parallelism is not a capacity plan. Local study-map skill 2.4 (Software Engineering Foundations), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. In this case: Bound active work and queued demand rather than assume unlimited parallelism is efficient.
- **B:** Correct. Limit queued and active work so slow consumers or provider limits do not exhaust memory or connections. Unbounded parallelism is not a capacity plan. In this case: Bound active work and queued demand rather than assume unlimited parallelism is efficient.
- **C:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Bound active work and queued demand rather than assume unlimited parallelism is efficient.
- **D:** Incorrect for this question. Await network operations without blocking an event loop, while limiting in-flight work and respecting service capacity. Creating a coroutine does not mean it has run. In this case: Bound active work and queued demand rather than assume unlimited parallelism is efficient.

### Question 53 — C

Answer: Set explicit deadlines and classify timeout outcomes. Explicit deadlines bound dependency waits and make timeout behavior actionable. Bound user and dependency waits. A timeout is an uncertain execution outcome for mutations and may require status reconciliation rather than blind retry. Local study-map skill 2.4 (Software Engineering Foundations), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Local cancellation limits waiting or computation but does not guarantee the server stopped or a remote side effect was rolled back. In this case: Explicit deadlines bound dependency waits and make timeout behavior actionable.
- **B:** Incorrect for this question. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: Explicit deadlines bound dependency waits and make timeout behavior actionable.
- **C:** Correct. Bound user and dependency waits. A timeout is an uncertain execution outcome for mutations and may require status reconciliation rather than blind retry. In this case: Explicit deadlines bound dependency waits and make timeout behavior actionable.
- **D:** Incorrect for this question. Nested automatic retries can multiply attempts and latency. Set a shared attempt or elapsed-time budget and inspect SDK defaults. In this case: Explicit deadlines bound dependency waits and make timeout behavior actionable.

### Question 54 — C

Answer: Use a durable idempotency key for the same logical action. Reuse a durable logical-action key to avoid duplicated external effects. Where supported, repeated requests for one operation should resolve to one intended external effect. Generating a new key for each retry defeats duplicate protection. Local study-map skill 2.4 (Software Engineering Foundations), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Bound user and dependency waits. A timeout is an uncertain execution outcome for mutations and may require status reconciliation rather than blind retry. In this case: Reuse a durable logical-action key to avoid duplicated external effects.
- **B:** Incorrect for this question. Local cancellation limits waiting or computation but does not guarantee the server stopped or a remote side effect was rolled back. In this case: Reuse a durable logical-action key to avoid duplicated external effects.
- **C:** Correct. Where supported, repeated requests for one operation should resolve to one intended external effect. Generating a new key for each retry defeats duplicate protection. In this case: Reuse a durable logical-action key to avoid duplicated external effects.
- **D:** Incorrect for this question. Separate a generated proposal from an authorized atomic or otherwise well-coordinated business effect. Define conflict handling and rollback or compensation behavior. In this case: Reuse a durable logical-action key to avoid duplicated external effects.

### Question 55 — D

Answer: Apply HTTP method, status, authentication, and payload contracts. HTTP transport success and semantic business success are different outcomes. A REST integration must respect its actual endpoint contract. HTTP 200 does not establish that the requested business operation succeeded semantically. Local study-map skill 2.4 (Software Engineering Foundations), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Different hosting providers can use distinct authentication, endpoints, identifiers, and supported features. Normalize the application contract without assuming identical wire protocols. In this case: HTTP transport success and semantic business success are different outcomes.
- **B:** Incorrect for this question. Check serialized requests, content blocks, status handling, and representative responses. Mock success alone may not reveal a malformed real request or unsupported provider feature. In this case: HTTP transport success and semantic business success are different outcomes.
- **C:** Incorrect for this question. Use the selected API contract for model, instructions, messages, and typed content. Do not assume a consumer chat interface and a developer API share implicit state. In this case: HTTP transport success and semantic business success are different outcomes.
- **D:** Correct. A REST integration must respect its actual endpoint contract. HTTP 200 does not establish that the requested business operation succeeded semantically. In this case: HTTP transport success and semantic business success are different outcomes.

### Question 56 — D

Answer: Test the integration contract at the provider boundary. Test the actual serialized provider contract instead of only a mocked happy path. Check serialized requests, content blocks, status handling, and representative responses. Mock success alone may not reveal a malformed real request or unsupported provider feature. Local study-map skill 2.4 (Software Engineering Foundations), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Correlate the actual request, model response, tool execution, retries, and validation results. Diagnose the first failing boundary rather than infer cause from the final prose. In this case: Test the actual serialized provider contract instead of only a mocked happy path.
- **B:** Incorrect for this question. Inject timeouts, malformed responses, and provider failures without live side effects. Combine with contract and representative integration tests rather than infer complete correctness from mocks. In this case: Test the actual serialized provider contract instead of only a mocked happy path.
- **C:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Test the actual serialized provider contract instead of only a mocked happy path.
- **D:** Correct. Check serialized requests, content blocks, status handling, and representative responses. Mock success alone may not reveal a malformed real request or unsupported provider feature. In this case: Test the actual serialized provider contract instead of only a mocked happy path.

### Question 57 — C

Answer: Coordinate retries across SDK and application layers. Nested retries need a shared attempt or elapsed-time budget. Nested automatic retries can multiply attempts and latency. Set a shared attempt or elapsed-time budget and inspect SDK defaults. Local study-map skill 2.4 (Software Engineering Foundations), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: Nested retries need a shared attempt or elapsed-time budget.
- **B:** Incorrect for this question. Limit queued and active work so slow consumers or provider limits do not exhaust memory or connections. Unbounded parallelism is not a capacity plan. In this case: Nested retries need a shared attempt or elapsed-time budget.
- **C:** Correct. Nested automatic retries can multiply attempts and latency. Set a shared attempt or elapsed-time budget and inspect SDK defaults. In this case: Nested retries need a shared attempt or elapsed-time budget.
- **D:** Incorrect for this question. Bound user and dependency waits. A timeout is an uncertain execution outcome for mutations and may require status reconciliation rather than blind retry. In this case: Nested retries need a shared attempt or elapsed-time budget.

### Question 58 — D

Answer: Cancel local work and reconcile any external operation separately. Stop local waiting as appropriate and reconcile the remote operation separately. Local cancellation limits waiting or computation but does not guarantee the server stopped or a remote side effect was rolled back. Local study-map skill 2.4 (Software Engineering Foundations), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Bound user and dependency waits. A timeout is an uncertain execution outcome for mutations and may require status reconciliation rather than blind retry. In this case: Stop local waiting as appropriate and reconcile the remote operation separately.
- **B:** Incorrect for this question. Separate a generated proposal from an authorized atomic or otherwise well-coordinated business effect. Define conflict handling and rollback or compensation behavior. In this case: Stop local waiting as appropriate and reconcile the remote operation separately.
- **C:** Incorrect for this question. Where supported, repeated requests for one operation should resolve to one intended external effect. Generating a new key for each retry defeats duplicate protection. In this case: Stop local waiting as appropriate and reconcile the remote operation separately.
- **D:** Correct. Local cancellation limits waiting or computation but does not guarantee the server stopped or a remote side effect was rolled back. In this case: Stop local waiting as appropriate and reconcile the remote operation separately.

### Question 59 — C

Answer: Propagate correlation identifiers across requests and tools. Correlation identifiers join the task trace without exposing private content. Link a user task to provider requests, worker runs, and actions without using sensitive content as an identifier. Protect telemetry access and retention. Local study-map skill 2.4 (Software Engineering Foundations), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Correlate the actual request, model response, tool execution, retries, and validation results. Diagnose the first failing boundary rather than infer cause from the final prose. In this case: Correlation identifiers join the task trace without exposing private content.
- **B:** Incorrect for this question. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: Correlation identifiers join the task trace without exposing private content.
- **C:** Correct. Link a user task to provider requests, worker runs, and actions without using sensitive content as an identifier. Protect telemetry access and retention. In this case: Correlation identifiers join the task trace without exposing private content.
- **D:** Incorrect for this question. Audit records support attribution and reconstruction of consequential actions. Limit access, sensitive content, and retention; they do not themselves block an effect. In this case: Correlation identifiers join the task trace without exposing private content.

### Question 60 — B

Answer: Validate and commit business changes through a controlled boundary. Validated business changes need coordinated commit and conflict-handling semantics. Separate a generated proposal from an authorized atomic or otherwise well-coordinated business effect. Define conflict handling and rollback or compensation behavior. Local study-map skill 2.4 (Software Engineering Foundations), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Where supported, repeated requests for one operation should resolve to one intended external effect. Generating a new key for each retry defeats duplicate protection. In this case: Validated business changes need coordinated commit and conflict-handling semantics.
- **B:** Correct. Separate a generated proposal from an authorized atomic or otherwise well-coordinated business effect. Define conflict handling and rollback or compensation behavior. In this case: Validated business changes need coordinated commit and conflict-handling semantics.
- **C:** Incorrect for this question. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Validated business changes need coordinated commit and conflict-handling semantics.
- **D:** Incorrect for this question. Review must gate the external effect, be tied to the intended action, and use current authority. A later audit cannot reliably reverse a completed effect. In this case: Validated business changes need coordinated commit and conflict-handling semantics.

### Question 61 — B

Answer: Use tests and specific failure feedback to drive iteration. Regression tests should cover preservation of required protocol fields across changes. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. Local study-map skill 2.4 (Software Engineering Foundations), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Check serialized requests, content blocks, status handling, and representative responses. Mock success alone may not reveal a malformed real request or unsupported provider feature. In this case: Regression tests should cover preservation of required protocol fields across changes.
- **B:** Correct. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Regression tests should cover preservation of required protocol fields across changes.
- **C:** Incorrect for this question. Inject timeouts, malformed responses, and provider failures without live side effects. Combine with contract and representative integration tests rather than infer complete correctness from mocks. In this case: Regression tests should cover preservation of required protocol fields across changes.
- **D:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Regression tests should cover preservation of required protocol fields across changes.

### Question 62 — D

Answer: Pin compatible model, SDK, prompt, and dependency versions. Identify all behavior-relevant versions instead of tracking only application source. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. Local study-map skill 2.4 (Software Engineering Foundations), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Stage exposure to the new configuration, compare required outcomes, and retain a known-good path. A vendor release note is not workload validation. In this case: Identify all behavior-relevant versions instead of tracking only application source.
- **B:** Incorrect for this question. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: Identify all behavior-relevant versions instead of tracking only application source.
- **C:** Incorrect for this question. Plugins can change tools and workflow behavior. Track provenance, versions, compatibility, and permissions rather than install unreviewed code merely because a model suggests it. In this case: Identify all behavior-relevant versions instead of tracking only application source.
- **D:** Correct. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Identify all behavior-relevant versions instead of tracking only application source.

### Question 63 — B

Answer: Canary a version change with regression gates and rollback. Use staged exposure with validation gates and a rollback path. Stage exposure to the new configuration, compare required outcomes, and retain a known-good path. A vendor release note is not workload validation. Local study-map skill 2.4 (Software Engineering Foundations), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: Use staged exposure with validation gates and a rollback path.
- **B:** Correct. Stage exposure to the new configuration, compare required outcomes, and retain a known-good path. A vendor release note is not workload validation. In this case: Use staged exposure with validation gates and a rollback path.
- **C:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Use staged exposure with validation gates and a rollback path.
- **D:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Use staged exposure with validation gates and a rollback path.

### Question 64 — D

Answer: Validate and encode untrusted values for their destination. Use parameterized operations and destination validation rather than trust generated strings. Model-generated strings are not safe SQL, shell, HTML, or filenames by default. Prefer parameterized operations, output encoding, and constrained execution paths. Local study-map skill 2.4 (Software Engineering Foundations), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Use parameterized operations and destination validation rather than trust generated strings.
- **B:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Use parameterized operations and destination validation rather than trust generated strings.
- **C:** Incorrect for this question. Temperature changes next-token sampling behavior where supported. Lowering it does not independently guarantee correct extraction, grounding, or identical execution. In this case: Use parameterized operations and destination validation rather than trust generated strings.
- **D:** Correct. Model-generated strings are not safe SQL, shell, HTML, or filenames by default. Prefer parameterized operations, output encoding, and constrained execution paths. In this case: Use parameterized operations and destination validation rather than trust generated strings.

### Question 65 — D

Answer: Use controlled stubs for repeatable failure-path tests. Controlled stubs can exercise failure paths without unpredictable external effects. Inject timeouts, malformed responses, and provider failures without live side effects. Combine with contract and representative integration tests rather than infer complete correctness from mocks. Local study-map skill 2.4 (Software Engineering Foundations), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Controlled stubs can exercise failure paths without unpredictable external effects.
- **B:** Incorrect for this question. Check serialized requests, content blocks, status handling, and representative responses. Mock success alone may not reveal a malformed real request or unsupported provider feature. In this case: Controlled stubs can exercise failure paths without unpredictable external effects.
- **C:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Controlled stubs can exercise failure paths without unpredictable external effects.
- **D:** Correct. Inject timeouts, malformed responses, and provider failures without live side effects. Combine with contract and representative integration tests rather than infer complete correctness from mocks. In this case: Controlled stubs can exercise failure paths without unpredictable external effects.

### Question 66 — B

Answer: Isolate model-output defects from integration defects. The error originates in integration transformation rather than model reasoning. Check whether correct raw output was lost or changed by serialization, parsing, routing, or persistence. Not every visible error is fixed by changing the prompt. Local study-map skill 2.4 (Software Engineering Foundations), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Correlate the actual request, model response, tool execution, retries, and validation results. Diagnose the first failing boundary rather than infer cause from the final prose. In this case: The error originates in integration transformation rather than model reasoning.
- **B:** Correct. Check whether correct raw output was lost or changed by serialization, parsing, routing, or persistence. Not every visible error is fixed by changing the prompt. In this case: The error originates in integration transformation rather than model reasoning.
- **C:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: The error originates in integration transformation rather than model reasoning.
- **D:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: The error originates in integration transformation rather than model reasoning.

### Question 67 — B

Answer: Use asynchronous I/O with bounded concurrency. Async work must actually execute through the runtime rather than merely exist as a coroutine object. Await network operations without blocking an event loop, while limiting in-flight work and respecting service capacity. Creating a coroutine does not mean it has run. Local study-map skill 2.4 (Software Engineering Foundations), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: Async work must actually execute through the runtime rather than merely exist as a coroutine object.
- **B:** Correct. Await network operations without blocking an event loop, while limiting in-flight work and respecting service capacity. Creating a coroutine does not mean it has run. In this case: Async work must actually execute through the runtime rather than merely exist as a coroutine object.
- **C:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Async work must actually execute through the runtime rather than merely exist as a coroutine object.
- **D:** Incorrect for this question. Limit queued and active work so slow consumers or provider limits do not exhaust memory or connections. Unbounded parallelism is not a capacity plan. In this case: Async work must actually execute through the runtime rather than merely exist as a coroutine object.

### Question 68 — D

Answer: Test the integration contract at the provider boundary. Validate the serialized request and parsed response contract against supported versions. Check serialized requests, content blocks, status handling, and representative responses. Mock success alone may not reveal a malformed real request or unsupported provider feature. Local study-map skill 2.4 (Software Engineering Foundations), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Validate the serialized request and parsed response contract against supported versions.
- **B:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Validate the serialized request and parsed response contract against supported versions.
- **C:** Incorrect for this question. Inject timeouts, malformed responses, and provider failures without live side effects. Combine with contract and representative integration tests rather than infer complete correctness from mocks. In this case: Validate the serialized request and parsed response contract against supported versions.
- **D:** Correct. Check serialized requests, content blocks, status handling, and representative responses. Mock success alone may not reveal a malformed real request or unsupported provider feature. In this case: Validate the serialized request and parsed response contract against supported versions.

### Question 69 — B

Answer: Validate and commit business changes through a controlled boundary. The business commit boundary needs current-state validation and concurrency handling. Separate a generated proposal from an authorized atomic or otherwise well-coordinated business effect. Define conflict handling and rollback or compensation behavior. Local study-map skill 2.4 (Software Engineering Foundations), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Where supported, repeated requests for one operation should resolve to one intended external effect. Generating a new key for each retry defeats duplicate protection. In this case: The business commit boundary needs current-state validation and concurrency handling.
- **B:** Correct. Separate a generated proposal from an authorized atomic or otherwise well-coordinated business effect. Define conflict handling and rollback or compensation behavior. In this case: The business commit boundary needs current-state validation and concurrency handling.
- **C:** Incorrect for this question. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: The business commit boundary needs current-state validation and concurrency handling.
- **D:** Incorrect for this question. Review must gate the external effect, be tied to the intended action, and use current authority. A later audit cannot reliably reverse a completed effect. In this case: The business commit boundary needs current-state validation and concurrency handling.

### Question 70 — D

Answer: Plan deployment, operation, maintenance, and retirement. Change delivery must include operational ownership and lifecycle management after release. Development does not end at a successful API call. Include monitoring, updates, recovery, ownership, and decommissioning in the system lifecycle. Local study-map skill 2.4 (Software Engineering Foundations), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Stage exposure to the new configuration, compare required outcomes, and retain a known-good path. A vendor release note is not workload validation. In this case: Change delivery must include operational ownership and lifecycle management after release.
- **B:** Incorrect for this question. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: Change delivery must include operational ownership and lifecycle management after release.
- **C:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Change delivery must include operational ownership and lifecycle management after release.
- **D:** Correct. Development does not end at a successful API call. Include monitoring, updates, recovery, ownership, and decommissioning in the system lifecycle. In this case: Change delivery must include operational ownership and lifecycle management after release.

### Question 71 — B

Answer: Place trusted application policy in the supported system instruction field. Use supported trusted instruction placement and keep source data clearly separate. Keep trusted instructions separate from user and retrieved data. On the direct Messages API, system instructions use the top-level system parameter rather than a system-role entry in messages. Local study-map skill 2.5 (Claude Application Design), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Use supported trusted instruction placement and keep source data clearly separate.
- **B:** Correct. Keep trusted instructions separate from user and retrieved data. On the direct Messages API, system instructions use the top-level system parameter rather than a system-role entry in messages. In this case: Use supported trusted instruction placement and keep source data clearly separate.
- **C:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: Use supported trusted instruction placement and keep source data clearly separate.
- **D:** Incorrect for this question. Use the selected API contract for model, instructions, messages, and typed content. Do not assume a consumer chat interface and a developer API share implicit state. In this case: Use supported trusted instruction placement and keep source data clearly separate.

### Question 72 — B

Answer: Supply the relevant conversation state on subsequent requests. State transfer between interfaces must be explicit rather than assumed universal memory. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. Local study-map skill 2.5 (Claude Application Design), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: State transfer between interfaces must be explicit rather than assumed universal memory.
- **B:** Correct. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. In this case: State transfer between interfaces must be explicit rather than assumed universal memory.
- **C:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: State transfer between interfaces must be explicit rather than assumed universal memory.
- **D:** Incorrect for this question. Use the selected API contract for model, instructions, messages, and typed content. Do not assume a consumer chat interface and a developer API share implicit state. In this case: State transfer between interfaces must be explicit rather than assumed universal memory.

### Question 73 — A

Answer: Use supported strict structured output with a schema. Supported structured output targets shape while later checks still verify meaning. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. Local study-map skill 2.5 (Claude Application Design), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Correct. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Supported structured output targets shape while later checks still verify meaning.
- **B:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Supported structured output targets shape while later checks still verify meaning.
- **C:** Incorrect for this question. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Supported structured output targets shape while later checks still verify meaning.
- **D:** Incorrect for this question. Use the selected API contract for model, instructions, messages, and typed content. Do not assume a consumer chat interface and a developer API share implicit state. In this case: Supported structured output targets shape while later checks still verify meaning.

### Question 74 — B

Answer: Validate extracted values against evidence and business rules. Verify identity and source-backed field meaning beyond syntactic compliance. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. Local study-map skill 2.5 (Claude Application Design), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Verify identity and source-backed field meaning beyond syntactic compliance.
- **B:** Correct. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Verify identity and source-backed field meaning beyond syntactic compliance.
- **C:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Verify identity and source-backed field meaning beyond syntactic compliance.
- **D:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Verify identity and source-backed field meaning beyond syntactic compliance.

### Question 75 — B

Answer: Allow explicit unknown or absent values in the schema. Allow truthful unknown or missing representation instead of force an invented value. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. Local study-map skill 2.5 (Claude Application Design), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Allow truthful unknown or missing representation instead of force an invented value.
- **B:** Correct. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Allow truthful unknown or missing representation instead of force an invented value.
- **C:** Incorrect for this question. An other category with details can represent valid cases outside an enum. Unclear represents uncertainty and should not be confused with known-but-uncatalogued categories. In this case: Allow truthful unknown or missing representation instead of force an invented value.
- **D:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Allow truthful unknown or missing representation instead of force an invented value.

### Question 76 — D

Answer: Version and review plugin dependencies and permissions. Plugins require version, compatibility, provenance, and permission management like other executable dependencies. Plugins can change tools and workflow behavior. Track provenance, versions, compatibility, and permissions rather than install unreviewed code merely because a model suggests it. Local study-map skill 2.5 (Claude Application Design), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: Plugins require version, compatibility, provenance, and permission management like other executable dependencies.
- **B:** Incorrect for this question. Claude Code settings configure supported behavior, permissions, hooks, and plugins. Shared .claude/settings.json, user, local, and managed scopes have distinct reach. In this case: Plugins require version, compatibility, provenance, and permission management like other executable dependencies.
- **C:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Plugins require version, compatibility, provenance, and permission management like other executable dependencies.
- **D:** Correct. Plugins can change tools and workflow behavior. Track provenance, versions, compatibility, and permissions rather than install unreviewed code merely because a model suggests it. In this case: Plugins require version, compatibility, provenance, and permission management like other executable dependencies.

### Question 77 — C

Answer: Use a provider-specific adapter behind a stable application interface. Treat each interface's supported contract and state semantics explicitly through integration boundaries. Different hosting providers can use distinct authentication, endpoints, identifiers, and supported features. Normalize the application contract without assuming identical wire protocols. Local study-map skill 2.5 (Claude Application Design), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. In this case: Treat each interface's supported contract and state semantics explicitly through integration boundaries.
- **B:** Incorrect for this question. Keep trusted instructions separate from user and retrieved data. On the direct Messages API, system instructions use the top-level system parameter rather than a system-role entry in messages. In this case: Treat each interface's supported contract and state semantics explicitly through integration boundaries.
- **C:** Correct. Different hosting providers can use distinct authentication, endpoints, identifiers, and supported features. Normalize the application contract without assuming identical wire protocols. In this case: Treat each interface's supported contract and state semantics explicitly through integration boundaries.
- **D:** Incorrect for this question. Use the selected API contract for model, instructions, messages, and typed content. Do not assume a consumer chat interface and a developer API share implicit state. In this case: Treat each interface's supported contract and state semantics explicitly through integration boundaries.

### Question 78 — C

Answer: Treat model output as untrusted before rendering or execution. Treat generated content as untrusted at rendering and execution destinations. Use destination-appropriate escaping, validation, and permission checks. Valid JSON can still contain executable or malicious values. Local study-map skill 2.5 (Claude Application Design), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Treat generated content as untrusted at rendering and execution destinations.
- **B:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Treat generated content as untrusted at rendering and execution destinations.
- **C:** Correct. Use destination-appropriate escaping, validation, and permission checks. Valid JSON can still contain executable or malicious values. In this case: Treat generated content as untrusted at rendering and execution destinations.
- **D:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Treat generated content as untrusted at rendering and execution destinations.

### Question 79 — A

Answer: Validate and commit business changes through a controlled boundary. Keep proposals distinct from the controlled business commit operation. Separate a generated proposal from an authorized atomic or otherwise well-coordinated business effect. Define conflict handling and rollback or compensation behavior. Local study-map skill 2.5 (Claude Application Design), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Correct. Separate a generated proposal from an authorized atomic or otherwise well-coordinated business effect. Define conflict handling and rollback or compensation behavior. In this case: Keep proposals distinct from the controlled business commit operation.
- **B:** Incorrect for this question. Review must gate the external effect, be tied to the intended action, and use current authority. A later audit cannot reliably reverse a completed effect. In this case: Keep proposals distinct from the controlled business commit operation.
- **C:** Incorrect for this question. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Keep proposals distinct from the controlled business commit operation.
- **D:** Incorrect for this question. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Keep proposals distinct from the controlled business commit operation.

### Question 80 — B

Answer: Translate business goals into measurable functional and operational requirements. Real functional and operational requirements determine the application architecture. Specify behavior, latency, throughput, data constraints, failure policy, and acceptance criteria. A model or framework choice is not a substitute for requirements. Local study-map skill 2.5 (Claude Application Design), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Self-hosting and managed deployment place different responsibilities on operations, networking, identity, and lifecycle. Availability and supported features must be verified. In this case: Real functional and operational requirements determine the application architecture.
- **B:** Correct. Specify behavior, latency, throughput, data constraints, failure policy, and acceptance criteria. A model or framework choice is not a substitute for requirements. In this case: Real functional and operational requirements determine the application architecture.
- **C:** Incorrect for this question. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. In this case: Real functional and operational requirements determine the application architecture.
- **D:** Incorrect for this question. Evaluate state graphs, typed validation, tracing, ecosystem, and deployment fit across frameworks such as LangGraph, Strands, or PydanticAI. A framework does not guarantee safety or correctness. In this case: Real functional and operational requirements determine the application architecture.

### Question 81 — A

Answer: Separate environment configuration from application logic. Environment-specific configuration belongs outside hard-coded behavior and needs startup validation. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. Local study-map skill 2.6 (Configuration Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Correct. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: Environment-specific configuration belongs outside hard-coded behavior and needs startup validation.
- **B:** Incorrect for this question. Plugins can change tools and workflow behavior. Track provenance, versions, compatibility, and permissions rather than install unreviewed code merely because a model suggests it. In this case: Environment-specific configuration belongs outside hard-coded behavior and needs startup validation.
- **C:** Incorrect for this question. Claude Code settings configure supported behavior, permissions, hooks, and plugins. Shared .claude/settings.json, user, local, and managed scopes have distinct reach. In this case: Environment-specific configuration belongs outside hard-coded behavior and needs startup validation.
- **D:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Environment-specific configuration belongs outside hard-coded behavior and needs startup validation.

### Question 82 — B

Answer: Pin compatible model, SDK, prompt, and dependency versions. Use compatible explicit version identification and record the deployed configuration. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. Local study-map skill 2.6 (Configuration Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Stage exposure to the new configuration, compare required outcomes, and retain a known-good path. A vendor release note is not workload validation. In this case: Use compatible explicit version identification and record the deployed configuration.
- **B:** Correct. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Use compatible explicit version identification and record the deployed configuration.
- **C:** Incorrect for this question. Use evidence-based routing to suitable configurations, monitor misclassification, and define fallback. Routing complexity must justify its own operating cost. In this case: Use compatible explicit version identification and record the deployed configuration.
- **D:** Incorrect for this question. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. In this case: Use compatible explicit version identification and record the deployed configuration.

### Question 83 — B

Answer: Version exact prompt content and its dependencies. Track actual prompt content and dependencies so changes are attributable and reversible. Record revisions of behavioral instructions with evaluation and release history. A model pin does not freeze changing application prompts. Local study-map skill 2.6 (Configuration Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: Track actual prompt content and dependencies so changes are attributable and reversible.
- **B:** Correct. Record revisions of behavioral instructions with evaluation and release history. A model pin does not freeze changing application prompts. In this case: Track actual prompt content and dependencies so changes are attributable and reversible.
- **C:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Track actual prompt content and dependencies so changes are attributable and reversible.
- **D:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Track actual prompt content and dependencies so changes are attributable and reversible.

### Question 84 — D

Answer: Use the appropriate settings.json scope for behavioral configuration. Use the correct settings scope rather than assume CLAUDE.md text enforces runtime configuration. Claude Code settings configure supported behavior, permissions, hooks, and plugins. Shared .claude/settings.json, user, local, and managed scopes have distinct reach. Local study-map skill 2.6 (Configuration Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: Use the correct settings scope rather than assume CLAUDE.md text enforces runtime configuration.
- **B:** Incorrect for this question. Topic-specific rule files reduce one oversized instruction document. Add path scoping when a rule is only relevant to selected files. In this case: Use the correct settings scope rather than assume CLAUDE.md text enforces runtime configuration.
- **C:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Use the correct settings scope rather than assume CLAUDE.md text enforces runtime configuration.
- **D:** Correct. Claude Code settings configure supported behavior, permissions, hooks, and plugins. Shared .claude/settings.json, user, local, and managed scopes have distinct reach. In this case: Use the correct settings scope rather than assume CLAUDE.md text enforces runtime configuration.

### Question 85 — A

Answer: Version and review plugin dependencies and permissions. Review and version dependency behavior and permissions instead of treating plugins as static text. Plugins can change tools and workflow behavior. Track provenance, versions, compatibility, and permissions rather than install unreviewed code merely because a model suggests it. Local study-map skill 2.6 (Configuration Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Correct. Plugins can change tools and workflow behavior. Track provenance, versions, compatibility, and permissions rather than install unreviewed code merely because a model suggests it. In this case: Review and version dependency behavior and permissions instead of treating plugins as static text.
- **B:** Incorrect for this question. Stage exposure to the new configuration, compare required outcomes, and retain a known-good path. A vendor release note is not workload validation. In this case: Review and version dependency behavior and permissions instead of treating plugins as static text.
- **C:** Incorrect for this question. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: Review and version dependency behavior and permissions instead of treating plugins as static text.
- **D:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Review and version dependency behavior and permissions instead of treating plugins as static text.

### Question 86 — A

Answer: Put shared project standards in versioned CLAUDE.md. Versioned project instructions distribute shared standards rather than personal-only guidance. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. Local study-map skill 2.6 (Configuration Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Correct. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Versioned project instructions distribute shared standards rather than personal-only guidance.
- **B:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: Versioned project instructions distribute shared standards rather than personal-only guidance.
- **C:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: Versioned project instructions distribute shared standards rather than personal-only guidance.
- **D:** Incorrect for this question. Claude Code settings configure supported behavior, permissions, hooks, and plugins. Shared .claude/settings.json, user, local, and managed scopes have distinct reach. In this case: Versioned project instructions distribute shared standards rather than personal-only guidance.

### Question 87 — A

Answer: Canary a version change with regression gates and rollback. Canary the actual configuration with regression gates and rollback readiness. Stage exposure to the new configuration, compare required outcomes, and retain a known-good path. A vendor release note is not workload validation. Local study-map skill 2.6 (Configuration Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Correct. Stage exposure to the new configuration, compare required outcomes, and retain a known-good path. A vendor release note is not workload validation. In this case: Canary the actual configuration with regression gates and rollback readiness.
- **B:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Canary the actual configuration with regression gates and rollback readiness.
- **C:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Canary the actual configuration with regression gates and rollback readiness.
- **D:** Incorrect for this question. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: Canary the actual configuration with regression gates and rollback readiness.

### Question 88 — A

Answer: Separate environment configuration from application logic. Validate required configuration at startup rather than defer predictable failure to users. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. Local study-map skill 2.6 (Configuration Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Correct. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: Validate required configuration at startup rather than defer predictable failure to users.
- **B:** Incorrect for this question. Claude Code settings configure supported behavior, permissions, hooks, and plugins. Shared .claude/settings.json, user, local, and managed scopes have distinct reach. In this case: Validate required configuration at startup rather than defer predictable failure to users.
- **C:** Incorrect for this question. Plugins can change tools and workflow behavior. Track provenance, versions, compatibility, and permissions rather than install unreviewed code merely because a model suggests it. In this case: Validate required configuration at startup rather than defer predictable failure to users.
- **D:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Validate required configuration at startup rather than defer predictable failure to users.

### Question 89 — D

Answer: Pin compatible model, SDK, prompt, and dependency versions. Track all behavior-relevant dependencies for reproducible diagnosis and maintenance. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. Local study-map skill 2.6 (Configuration Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: Track all behavior-relevant dependencies for reproducible diagnosis and maintenance.
- **B:** Incorrect for this question. Plugins can change tools and workflow behavior. Track provenance, versions, compatibility, and permissions rather than install unreviewed code merely because a model suggests it. In this case: Track all behavior-relevant dependencies for reproducible diagnosis and maintenance.
- **C:** Incorrect for this question. Record revisions of behavioral instructions with evaluation and release history. A model pin does not freeze changing application prompts. In this case: Track all behavior-relevant dependencies for reproducible diagnosis and maintenance.
- **D:** Correct. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Track all behavior-relevant dependencies for reproducible diagnosis and maintenance.

### Question 90 — C

Answer: Use the appropriate settings.json scope for behavioral configuration. Configuration scope determines who receives a setting and which environment it affects. Claude Code settings configure supported behavior, permissions, hooks, and plugins. Shared .claude/settings.json, user, local, and managed scopes have distinct reach. Local study-map skill 2.6 (Configuration Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Topic-specific rule files reduce one oversized instruction document. Add path scoping when a rule is only relevant to selected files. In this case: Configuration scope determines who receives a setting and which environment it affects.
- **B:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Configuration scope determines who receives a setting and which environment it affects.
- **C:** Correct. Claude Code settings configure supported behavior, permissions, hooks, and plugins. Shared .claude/settings.json, user, local, and managed scopes have distinct reach. In this case: Configuration scope determines who receives a setting and which environment it affects.
- **D:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: Configuration scope determines who receives a setting and which environment it affects.

### Question 91 — C

Answer: Build a valid Messages API request with explicit content blocks. Follow the selected provider's documented request contract rather than assume interchangeable payloads. Use the selected API contract for model, instructions, messages, and typed content. Do not assume a consumer chat interface and a developer API share implicit state. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. In this case: Follow the selected provider's documented request contract rather than assume interchangeable payloads.
- **B:** Incorrect for this question. A response can contain text, tool use, thinking, or other supported blocks. Do not assume content is one string or that the first block is always displayable text. In this case: Follow the selected provider's documented request contract rather than assume interchangeable payloads.
- **C:** Correct. Use the selected API contract for model, instructions, messages, and typed content. Do not assume a consumer chat interface and a developer API share implicit state. In this case: Follow the selected provider's documented request contract rather than assume interchangeable payloads.
- **D:** Incorrect for this question. Different hosting providers can use distinct authentication, endpoints, identifiers, and supported features. Normalize the application contract without assuming identical wire protocols. In this case: Follow the selected provider's documented request contract rather than assume interchangeable payloads.

### Question 92 — A

Answer: Send supported image content in the documented multimodal format. Provide actual supported image content instead of a filename the remote service cannot read. Image understanding requires an actual supported image block or source, a compatible model, and valid media limits. A text filename alone does not provide image pixels. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Correct. Image understanding requires an actual supported image block or source, a compatible model, and valid media limits. A text filename alone does not provide image pixels. In this case: Provide actual supported image content instead of a filename the remote service cannot read.
- **B:** Incorrect for this question. Different hosting providers can use distinct authentication, endpoints, identifiers, and supported features. Normalize the application contract without assuming identical wire protocols. In this case: Provide actual supported image content instead of a filename the remote service cannot read.
- **C:** Incorrect for this question. A response can contain text, tool use, thinking, or other supported blocks. Do not assume content is one string or that the first block is always displayable text. In this case: Provide actual supported image content instead of a filename the remote service cannot read.
- **D:** Incorrect for this question. Use the selected API contract for model, instructions, messages, and typed content. Do not assume a consumer chat interface and a developer API share implicit state. In this case: Provide actual supported image content instead of a filename the remote service cannot read.

### Question 93 — A

Answer: Dispatch response content according to each block type. Inspect each typed content block instead of assuming index zero contains the answer. A response can contain text, tool use, thinking, or other supported blocks. Do not assume content is one string or that the first block is always displayable text. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Correct. A response can contain text, tool use, thinking, or other supported blocks. Do not assume content is one string or that the first block is always displayable text. In this case: Inspect each typed content block instead of assuming index zero contains the answer.
- **B:** Incorrect for this question. SDK accumulation helpers can provide the complete message. Inspect termination and errors before treating the resulting object as accepted application output. In this case: Inspect each typed content block instead of assuming index zero contains the answer.
- **C:** Incorrect for this question. Use the selected API contract for model, instructions, messages, and typed content. Do not assume a consumer chat interface and a developer API share implicit state. In this case: Inspect each typed content block instead of assuming index zero contains the answer.
- **D:** Incorrect for this question. Network chunks and content deltas can contain partial strings or JSON. Track event and block boundaries or use SDK helpers before consuming a complete structured value. In this case: Inspect each typed content block instead of assuming index zero contains the answer.

### Question 94 — A

Answer: Consume the Messages stream as server-sent events. Consume the documented SSE channel rather than invent an incompatible handshake. The documented streaming interface emits SSE events over HTTP. It is not inherently a WebSocket connection or one valid JSON object per arbitrary network chunk. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Correct. The documented streaming interface emits SSE events over HTTP. It is not inherently a WebSocket connection or one valid JSON object per arbitrary network chunk. In this case: Consume the documented SSE channel rather than invent an incompatible handshake.
- **B:** Incorrect for this question. Await network operations without blocking an event loop, while limiting in-flight work and respecting service capacity. Creating a coroutine does not mean it has run. In this case: Consume the documented SSE channel rather than invent an incompatible handshake.
- **C:** Incorrect for this question. WebSockets can fit bidirectional application communication, but the documented standard Messages streaming interface is SSE. Do not confuse a transport choice with model capability. In this case: Consume the documented SSE channel rather than invent an incompatible handshake.
- **D:** Incorrect for this question. A REST integration must respect its actual endpoint contract. HTTP 200 does not establish that the requested business operation succeeded semantically. In this case: Consume the documented SSE channel rather than invent an incompatible handshake.

### Question 95 — B

Answer: Correlate batch outcomes by custom_id. Each submitted item needs a unique stable custom identifier for reliable matching. Stable unique request identifiers connect results to inputs without assuming arrival order. Validate uniqueness and retain a manifest. Local study-map skill 2.3 (Claude API Mechanics), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Targeted resubmission avoids repeating successes and allows input fixes. Track identities and protect downstream effects against duplicate processing. In this case: Each submitted item needs a unique stable custom identifier for reliable matching.
- **B:** Correct. Stable unique request identifiers connect results to inputs without assuming arrival order. Validate uniqueness and retain a manifest. In this case: Each submitted item needs a unique stable custom identifier for reliable matching.
- **C:** Incorrect for this question. Link a user task to provider requests, worker runs, and actions without using sensitive content as an identifier. Protect telemetry access and retention. In this case: Each submitted item needs a unique stable custom identifier for reliable matching.
- **D:** Incorrect for this question. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: Each submitted item needs a unique stable custom identifier for reliable matching.

### Question 96 — A

Answer: Set explicit deadlines and classify timeout outcomes. Enforce an end-to-end deadline as well as individual dependency timeouts. Bound user and dependency waits. A timeout is an uncertain execution outcome for mutations and may require status reconciliation rather than blind retry. Local study-map skill 2.4 (Software Engineering Foundations), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Correct. Bound user and dependency waits. A timeout is an uncertain execution outcome for mutations and may require status reconciliation rather than blind retry. In this case: Enforce an end-to-end deadline as well as individual dependency timeouts.
- **B:** Incorrect for this question. Local cancellation limits waiting or computation but does not guarantee the server stopped or a remote side effect was rolled back. In this case: Enforce an end-to-end deadline as well as individual dependency timeouts.
- **C:** Incorrect for this question. Limit queued and active work so slow consumers or provider limits do not exhaust memory or connections. Unbounded parallelism is not a capacity plan. In this case: Enforce an end-to-end deadline as well as individual dependency timeouts.
- **D:** Incorrect for this question. Nested automatic retries can multiply attempts and latency. Set a shared attempt or elapsed-time budget and inspect SDK defaults. In this case: Enforce an end-to-end deadline as well as individual dependency timeouts.

### Question 97 — B

Answer: Coordinate retries across SDK and application layers. SDK and application retries need one explicit aggregate attempt or time budget. Nested automatic retries can multiply attempts and latency. Set a shared attempt or elapsed-time budget and inspect SDK defaults. Local study-map skill 2.4 (Software Engineering Foundations), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: SDK and application retries need one explicit aggregate attempt or time budget.
- **B:** Correct. Nested automatic retries can multiply attempts and latency. Set a shared attempt or elapsed-time budget and inspect SDK defaults. In this case: SDK and application retries need one explicit aggregate attempt or time budget.
- **C:** Incorrect for this question. Limit queued and active work so slow consumers or provider limits do not exhaust memory or connections. Unbounded parallelism is not a capacity plan. In this case: SDK and application retries need one explicit aggregate attempt or time budget.
- **D:** Incorrect for this question. Bound user and dependency waits. A timeout is an uncertain execution outcome for mutations and may require status reconciliation rather than blind retry. In this case: SDK and application retries need one explicit aggregate attempt or time budget.

### Question 98 — C

Answer: Treat model output as untrusted before rendering or execution. Schema compliance does not make embedded text safe to render or execute. Use destination-appropriate escaping, validation, and permission checks. Valid JSON can still contain executable or malicious values. Local study-map skill 2.5 (Claude Application Design), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Temperature changes next-token sampling behavior where supported. Lowering it does not independently guarantee correct extraction, grounding, or identical execution. In this case: Schema compliance does not make embedded text safe to render or execute.
- **B:** Incorrect for this question. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Schema compliance does not make embedded text safe to render or execute.
- **C:** Correct. Use destination-appropriate escaping, validation, and permission checks. Valid JSON can still contain executable or malicious values. In this case: Schema compliance does not make embedded text safe to render or execute.
- **D:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Schema compliance does not make embedded text safe to render or execute.

### Question 99 — B

Answer: Separate environment configuration from application logic. Use explicit validated environment configuration without embedding real secrets in code. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. Local study-map skill 2.6 (Configuration Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Claude Code settings configure supported behavior, permissions, hooks, and plugins. Shared .claude/settings.json, user, local, and managed scopes have distinct reach. In this case: Use explicit validated environment configuration without embedding real secrets in code.
- **B:** Correct. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: Use explicit validated environment configuration without embedding real secrets in code.
- **C:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Use explicit validated environment configuration without embedding real secrets in code.
- **D:** Incorrect for this question. Plugins can change tools and workflow behavior. Track provenance, versions, compatibility, and permissions rather than install unreviewed code merely because a model suggests it. In this case: Use explicit validated environment configuration without embedding real secrets in code.

### Question 100 — B

Answer: Plan deployment, operation, maintenance, and retirement. Retirement includes data and operational obligations rather than only stopping requests. Development does not end at a successful API call. Include monitoring, updates, recovery, ownership, and decommissioning in the system lifecycle. Local study-map skill 2.2 (Systems Life Cycle), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/api/messages

- **A:** Incorrect for this question. Observe deployed latency, failures, drift, and task outcomes with accountable response thresholds. Monitoring differs from an offline evaluation or a single diagnostic trace. In this case: Retirement includes data and operational obligations rather than only stopping requests.
- **B:** Correct. Development does not end at a successful API call. Include monitoring, updates, recovery, ownership, and decommissioning in the system lifecycle. In this case: Retirement includes data and operational obligations rather than only stopping requests.
- **C:** Incorrect for this question. Stage exposure to the new configuration, compare required outcomes, and retain a known-good path. A vendor release note is not workload validation. In this case: Retirement includes data and operational obligations rather than only stopping requests.
- **D:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Retirement includes data and operational obligations rather than only stopping requests.
