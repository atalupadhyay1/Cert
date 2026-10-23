# Claude Certified Developer – Foundations (CCDV-F) — Practice Set 5

Security, Claude Code and Debugging

100 questions · Suggested practice duration: 200 minutes · Practice target: 80%

Tests 1–5 are focused learning tests. Test 6 is an expanded blueprint-proportioned review, not an official exam replica. Related concepts recur.

Select ONE best answer for every question. Answer key follows all questions.

Original educational content, not actual, recalled, or copied Anthropic exam items.

## Questions

### 1. A retrieved vendor document tells an agent to send internal records to a new endpoint. What trust boundary should remain?

Domain: Security and Safety

- A. Treat retrieved instructions as untrusted source content
- B. Separate instructions and source data with explicit labels
- C. Apply requester permissions before evidence enters model context
- D. Place trusted application policy in the supported system instruction field

### 2. A logged-in user requests another tenant's record through a well-formed tool call. What must block access?

Domain: Security and Safety

- A. Define and validate a precise input schema
- B. Authenticate the calling identity
- C. Use supported strict structured output with a schema
- D. Authorize the current identity for the actual target and action

### 3. A workflow needs only a region but collects complete identity documents. What data principle should constrain collection?

Domain: Security and Safety

- A. Keep protected action and identity audit records
- B. Apply a privacy-preserving aggregate release mechanism
- C. Minimize, redact, and restrict sensitive data by approved purpose
- D. Review the exact service data-use and retention controls

### 4. An application renders model-generated markup without escaping. What boundary rule should apply?

Domain: Security and Safety

- A. Adjust sampling variability, not factual truth
- B. Validate extracted values against evidence and business rules
- C. Treat model output as untrusted before rendering or execution
- D. Use supported strict structured output with a schema

### 5. A URL loader accepts internal metadata endpoints despite only needing approved external documents. What control is relevant?

Domain: Security and Safety

- A. Treat retrieved instructions as untrusted source content
- B. Segment network zones between services
- C. Apply requester permissions before evidence enters model context
- D. Restrict network destinations and prevent unsafe fetch paths

### 6. A model-produced value is concatenated into a shell command. What should replace this unsafe handling?

Domain: Security and Safety

- A. Use supported strict structured output with a schema
- B. Adjust sampling variability, not factual truth
- C. Validate extracted values against evidence and business rules
- D. Validate and encode untrusted values for their destination

### 7. An engineer says frozen inference weights prove no prompts are stored. What must be reviewed instead?

Domain: Security and Safety

- A. Apply a privacy-preserving aggregate release mechanism
- B. Review the exact service data-use and retention controls
- C. Minimize, redact, and restrict sensitive data by approved purpose
- D. Keep protected action and identity audit records

### 8. A search connector can read more documents than the current user should see. What filter is required?

Domain: Security and Safety

- A. Apply requester permissions before evidence enters model context
- B. Compact context while preserving checked facts and open issues
- C. Reduce tool output to relevant fields with provenance
- D. Treat retrieved instructions as untrusted source content

### 9. A tool call has valid fields but proposes an action outside the user's current authority. What trusted check is necessary?

Domain: Security and Safety

- A. Define and validate a precise input schema
- B. Use supported strict structured output with a schema
- C. Authorize the current identity for the actual target and action
- D. Authenticate the calling identity

### 10. Debug traces include unnecessary personal data from every source record. What should collection minimize?

Domain: Security and Safety

- A. Keep protected action and identity audit records
- B. Minimize, redact, and restrict sensitive data by approved purpose
- C. Review the exact service data-use and retention controls
- D. Apply a privacy-preserving aggregate release mechanism

### 11. A tool response contains hostile instructions mixed with useful data. How should its role be represented?

Domain: Security and Safety

- A. Treat retrieved instructions as untrusted source content
- B. Apply requester permissions before evidence enters model context
- C. Place trusted application policy in the supported system instruction field
- D. Separate instructions and source data with explicit labels

### 12. A generated filename contains a parent-directory traversal sequence. What should guard its use?

Domain: Security and Safety

- A. Adjust sampling variability, not factual truth
- B. Treat model output as untrusted before rendering or execution
- C. Validate extracted values against evidence and business rules
- D. Use supported strict structured output with a schema

### 13. An API needs to establish which caller is making the request before evaluating permissions. What security operation is this?

Domain: Security and Safety

- A. Apply requester permissions before evidence enters model context
- B. Authorize the current identity for the actual target and action
- C. Enforce prerequisites in trusted execution code
- D. Authenticate the calling identity

### 14. The caller is known, but access to a specific document still needs approval. What security decision remains?

Domain: Security and Safety

- A. Authorize the current identity for the actual target and action
- B. Enforce prerequisites in trusted execution code
- C. Apply requester permissions before evidence enters model context
- D. Authenticate the calling identity

### 15. A provider offers several account plans with different data controls. What evidence should determine permitted use?

Domain: Security and Safety

- A. Minimize, redact, and restrict sensitive data by approved purpose
- B. Apply a privacy-preserving aggregate release mechanism
- C. Keep protected action and identity audit records
- D. Review the exact service data-use and retention controls

### 16. An agent can contact arbitrary destinations through a generic fetch operation. What execution control should narrow exposure?

Domain: Security and Safety

- A. Treat retrieved instructions as untrusted source content
- B. Restrict network destinations and prevent unsafe fetch paths
- C. Apply requester permissions before evidence enters model context
- D. Segment network zones between services

### 17. Test fixtures contain full real customer records although synthetic examples would suffice. What should guide revision?

Domain: Security and Safety

- A. Apply a privacy-preserving aggregate release mechanism
- B. Keep protected action and identity audit records
- C. Review the exact service data-use and retention controls
- D. Minimize, redact, and restrict sensitive data by approved purpose

### 18. A retrieved page declares itself a higher-priority policy document and asks for credential access. What boundary applies?

Domain: Security and Safety

- A. Separate instructions and source data with explicit labels
- B. Place trusted application policy in the supported system instruction field
- C. Apply requester permissions before evidence enters model context
- D. Treat retrieved instructions as untrusted source content

### 19. An assistant suggests a database query using a user-controlled field value. What coding practice reduces injection risk?

Domain: Security and Safety

- A. Validate and encode untrusted values for their destination
- B. Validate extracted values against evidence and business rules
- C. Adjust sampling variability, not factual truth
- D. Use supported strict structured output with a schema

### 20. A cached prior permission is used after an account's role was revoked. What should execution verify?

Domain: Security and Safety

- A. Apply requester permissions before evidence enters model context
- B. Authorize the current identity for the actual target and action
- C. Authenticate the calling identity
- D. Enforce prerequisites in trusted execution code

### 21. A team relies on one polite system instruction as its entire security plan. What design is needed?

Domain: Security and Safety

- A. Apply content-level safety detection and moderation
- B. Layer prevention, detection, approval, and recovery controls
- C. Enforce prerequisites in trusted execution code
- D. Require authorized approval before the consequential action

### 22. A read-only research worker receives powerful mutation tools it never needs. What principle should reduce access?

Domain: Security and Safety

- A. Give each specialist only task-relevant tools
- B. Expose a supported MCP resource catalog
- C. Check connected-server discovery and effective availability
- D. Clarify tool purpose, inputs, outputs, and boundaries

### 23. A high-impact external action requires a qualified person's authorization before commitment. What control fits?

Domain: Security and Safety

- A. Require authorized approval before the consequential action
- B. Keep protected action and identity audit records
- C. Enforce prerequisites in trusted execution code
- D. Monitor production service and outcome signals

### 24. A new guardrail passes development tests but production edge cases are uncertain. What rollout helps?

Domain: Security and Safety

- A. Separate environment configuration from application logic
- B. Pin compatible model, SDK, prompt, and dependency versions
- C. Canary a version change with regression gates and rollback
- D. Use a versioned representative held-out evaluation set

### 25. Ordinary tests cover only friendly users and expected content. What testing should probe misuse paths?

Domain: Security and Safety

- A. Test adversarial and misuse scenarios
- B. Use controlled stubs for repeatable failure-path tests
- C. Use tests and specific failure feedback to drive iteration
- D. Use a versioned representative held-out evaluation set

### 26. Monitoring confirms private data was sent outside approved boundaries. What coordinated process should activate?

Domain: Security and Safety

- A. Monitor production service and outcome signals
- B. Activate coordinated incident response and recovery
- C. Inspect a redacted end-to-end request and tool trace
- D. Keep protected action and identity audit records

### 27. A content filter blocks prohibited wording but cannot enforce account permissions. What broader strategy is required?

Domain: Security and Safety

- A. Layer prevention, detection, approval, and recovery controls
- B. Apply content-level safety detection and moderation
- C. Enforce prerequisites in trusted execution code
- D. Require authorized approval before the consequential action

### 28. A previously advisory assistant is about to gain write capabilities. What operating boundary must be revisited?

Domain: Security and Safety

- A. Enforce task, iteration, and spending safeguards
- B. Require authorized approval before the consequential action
- C. Enforce prerequisites in trusted execution code
- D. Give each specialist only task-relevant tools

### 29. Investigators need to reconstruct actions without granting everyone unrestricted access to raw prompts. What traceability design fits?

Domain: Security and Safety

- A. Inspect a redacted end-to-end request and tool trace
- B. Monitor production service and outcome signals
- C. Propagate correlation identifiers across requests and tools
- D. Keep protected action and identity audit records

### 30. Passing a finite security test suite is treated as proof all future attacks are impossible. What design principle corrects this?

Domain: Security and Safety

- A. Layer prevention, detection, approval, and recovery controls
- B. Test adversarial and misuse scenarios
- C. Apply content-level safety detection and moderation
- D. Enforce prerequisites in trusted execution code

### 31. A prohibited delete operation must be stopped before the tool executes. Which interception stage fits?

Domain: Security and Safety

- A. Normalize tool observations before model consumption
- B. State explicit reportable and non-reportable criteria
- C. Use pre-execution tool interception for blocking policy checks
- D. Record detected_pattern and dismissal reasons

### 32. A post-tool processor standardizes harmless status formats for model consumption. What hook-oriented responsibility is this?

Domain: Security and Safety

- A. Enforce prerequisites in trusted execution code
- B. Normalize tool observations before model consumption
- C. Use pre-execution tool interception for blocking policy checks
- D. Require authorized approval before the consequential action

### 33. A post-execution handler detects forbidden exports only after data leaves. What stage should prevent future exports?

Domain: Security and Safety

- A. Normalize tool observations before model consumption
- B. Monitor production service and outcome signals
- C. Use pre-execution tool interception for blocking policy checks
- D. Keep protected action and identity audit records

### 34. A hook trusts the model's statement that approval exists without checking stored state. What should enforce policy?

Domain: Security and Safety

- A. Use representative few-shot examples with boundaries
- B. Configure the subagent description, prompt, and tool scope
- C. Enforce prerequisites in trusted execution code
- D. State explicit reportable and non-reportable criteria

### 35. A tool proposes writing outside the approved workspace. Where should the destination restriction be checked?

Domain: Security and Safety

- A. Enforce task, iteration, and spending safeguards
- B. Normalize tool observations before model consumption
- C. Use pre-execution tool interception for blocking policy checks
- D. Require authorized approval before the consequential action

### 36. A tool returns an unknown status, and a handler converts it into success for readability. What should be corrected?

Domain: Security and Safety

- A. Enforce prerequisites in trusted execution code
- B. Normalize tool observations before model consumption
- C. Require authorized approval before the consequential action
- D. Use pre-execution tool interception for blocking policy checks

### 37. A strict business rule is only present in CLAUDE.md and occasionally ignored. What should implement enforcement?

Domain: Security and Safety

- A. Configure the subagent description, prompt, and tool scope
- B. Use representative few-shot examples with boundaries
- C. State explicit reportable and non-reportable criteria
- D. Enforce prerequisites in trusted execution code

### 38. A dangerous argument is discovered in the outgoing tool call. What control can reject it before execution?

Domain: Security and Safety

- A. Record detected_pattern and dismissal reasons
- B. State explicit reportable and non-reportable criteria
- C. Use pre-execution tool interception for blocking policy checks
- D. Normalize tool observations before model consumption

### 39. A team wants to verify that a blocking hook rejects prohibited calls without live destructive actions. What setup helps?

Domain: Security and Safety

- A. Test the integration contract at the provider boundary
- B. Use controlled stubs for repeatable failure-path tests
- C. Use a versioned representative held-out evaluation set
- D. Use tests and specific failure feedback to drive iteration

### 40. A hook is useful but cannot cover identity, all external state, and every data path alone. What deployment approach applies?

Domain: Security and Safety

- A. Normalize tool observations before model consumption
- B. Require authorized approval before the consequential action
- C. Layer prevention, detection, approval, and recovery controls
- D. Use pre-execution tool interception for blocking policy checks

### 41. An agent needs a backend credential, but the developer plans to put it in the prompt. Where should it be managed?

Domain: Security and Safety

- A. Reference runtime environment variables instead of committing tokens
- B. Authorize the current identity for the actual target and action
- C. Manage credentials in protected execution infrastructure
- D. Authenticate the calling identity

### 42. A shared configuration must reference a token without committing its value. What runtime pattern fits?

Domain: Security and Safety

- A. Version and review plugin dependencies and permissions
- B. Use the appropriate settings.json scope for behavioral configuration
- C. Reference runtime environment variables instead of committing tokens
- D. Separate environment configuration from application logic

### 43. A production key appears in a public diagnostic artifact. What should happen beyond deleting the visible copy?

Domain: Security and Safety

- A. Activate coordinated incident response and recovery
- B. Revoke exposed credentials and investigate their use
- C. Keep protected action and identity audit records
- D. Manage credentials in protected execution infrastructure

### 44. Several agents use one administrator credential despite distinct responsibilities. What design reduces shared authority?

Domain: Security and Safety

- A. Give each specialist only task-relevant tools
- B. Authorize the current identity for the actual target and action
- C. Authenticate the calling identity
- D. Use distinct least-privilege workload identities

### 45. A request presents a credential whose validity must be checked. What decision is being made?

Domain: Security and Safety

- A. Authorize the current identity for the actual target and action
- B. Authenticate the calling identity
- C. Apply requester permissions before evidence enters model context
- D. Enforce prerequisites in trusted execution code

### 46. An authenticated worker requests access outside its approved resource scope. What should deny the action?

Domain: Security and Safety

- A. Authenticate the calling identity
- B. Enforce prerequisites in trusted execution code
- C. Authorize the current identity for the actual target and action
- D. Apply requester permissions before evidence enters model context

### 47. An API key is absent from source code but appears in exception messages. What protection still needs improvement?

Domain: Security and Safety

- A. Separate environment configuration from application logic
- B. Reference runtime environment variables instead of committing tokens
- C. Manage credentials in protected execution infrastructure
- D. Keep protected action and identity audit records

### 48. Security needs to identify which workload identity performed a sensitive action. What evidence capability helps?

Domain: Security and Safety

- A. Propagate correlation identifiers across requests and tools
- B. Keep protected action and identity audit records
- C. Inspect a redacted end-to-end request and tool trace
- D. Monitor production service and outcome signals

### 49. A read-only assistant should not share a service account with a deployment agent. What principle applies?

Domain: Security and Safety

- A. Authenticate the calling identity
- B. Use distinct least-privilege workload identities
- C. Give each specialist only task-relevant tools
- D. Authorize the current identity for the actual target and action

### 50. An exposed credential is revoked, but investigators still need to assess possible misuse. What response should continue?

Domain: Security and Safety

- A. Activate coordinated incident response and recovery
- B. Keep protected action and identity audit records
- C. Manage credentials in protected execution infrastructure
- D. Revoke exposed credentials and investigate their use

### 51. A new teammate lacks repository standards stored only in another user's home instructions. Where should shared guidance go?

Domain: Claude Code

- A. Put an on-demand workflow in a project skill
- B. Put personal cross-project preferences in ~/.claude/CLAUDE.md
- C. Put shared project standards in versioned CLAUDE.md
- D. Use directory-scoped CLAUDE.md for a local package

### 52. A user wants preferences across personal projects without modifying team repositories. Which instruction scope fits?

Domain: Claude Code

- A. Put personal cross-project preferences in ~/.claude/CLAUDE.md
- B. Use directory-scoped CLAUDE.md for a local package
- C. Put shared project standards in versioned CLAUDE.md
- D. Organize focused conventions in .claude/rules/

### 53. A test convention applies to matching files scattered across packages. Which scoping mechanism fits?

Domain: Claude Code

- A. Scope a rule with YAML paths glob patterns
- B. Put shared project standards in versioned CLAUDE.md
- C. Use directory-scoped CLAUDE.md for a local package
- D. Put personal cross-project preferences in ~/.claude/CLAUDE.md

### 54. A long task-specific procedure should load only when invoked. What extension type fits?

Domain: Claude Code

- A. Put shared project standards in versioned CLAUDE.md
- B. Put an on-demand workflow in a project skill
- C. Put personal cross-project preferences in ~/.claude/CLAUDE.md
- D. Organize focused conventions in .claude/rules/

### 55. A reusable project slash command should be shared through version control. Which scope fits?

Domain: Claude Code

- A. Put shared project standards in versioned CLAUDE.md
- B. Expose a supported MCP resource catalog
- C. Put personal cross-project preferences in ~/.claude/CLAUDE.md
- D. Use a project-scoped custom slash command

### 56. A team needs supported hook and permission configuration, not just written conventions. What mechanism matters?

Domain: Claude Code

- A. Put personal cross-project preferences in ~/.claude/CLAUDE.md
- B. Put shared project standards in versioned CLAUDE.md
- C. Organize focused conventions in .claude/rules/
- D. Use the appropriate settings.json scope for behavioral configuration

### 57. A headless review job waits for interactive input. Which invocation mode should be used?

Domain: Claude Code

- A. Use plan mode to investigate and compare approaches
- B. Run Claude Code in non-interactive print mode
- C. Use a project-scoped custom slash command
- D. Use supported JSON output and schema CLI options

### 58. A CI consumer needs machine-readable schema-shaped findings. What output mode should be assessed?

Domain: Claude Code

- A. Pass prior findings and request only new or unresolved issues
- B. Run Claude Code in non-interactive print mode
- C. Use supported JSON output and schema CLI options
- D. State explicit reportable and non-reportable criteria

### 59. A named investigation remains valid and should continue from its prior context. What session facility is relevant?

Domain: Claude Code

- A. Fork an independent branch from a valid shared baseline
- B. Compact context while preserving checked facts and open issues
- C. Start a fresh session with a checked structured summary
- D. Resume the identified session when its context remains valid

### 60. A rule file exists but behavior suggests it is not in effective context. What should be inspected?

Domain: Claude Code

- A. Scope a rule with YAML paths glob patterns
- B. Put personal cross-project preferences in ~/.claude/CLAUDE.md
- C. Inspect which instruction files are actually loaded
- D. Put shared project standards in versioned CLAUDE.md

### 61. A skill produces verbose intermediate exploration that should not fill the main conversation. What supported setting helps?

Domain: Claude Code

- A. Configure a least-privilege skill workflow and verify effective permissions
- B. Create a differently named personal skill variant
- C. Use context: fork for isolated skill execution
- D. Provide argument-hint for invocation guidance

### 62. A documentation skill should not have unrelated command execution capabilities. What should be configured?

Domain: Claude Code

- A. Create a differently named personal skill variant
- B. Configure a least-privilege skill workflow and verify effective permissions
- C. Use context: fork for isolated skill execution
- D. Provide argument-hint for invocation guidance

### 63. Users need to know a skill expects a package argument. What frontmatter improves invocation guidance?

Domain: Claude Code

- A. Configure a least-privilege skill workflow and verify effective permissions
- B. Provide argument-hint for invocation guidance
- C. Use context: fork for isolated skill execution
- D. Create a differently named personal skill variant

### 64. One developer wants an experimental personal skill without altering the shared workflow. What approach fits?

Domain: Claude Code

- A. Use a project-scoped custom slash command
- B. Create a differently named personal skill variant
- C. Put an on-demand workflow in a project skill
- D. Put shared project standards in versioned CLAUDE.md

### 65. A broad migration has several valid approaches and uncertain cross-file effects. What mode should precede edits?

Domain: Claude Code

- A. Use tests and specific failure feedback to drive iteration
- B. Provide concrete input–output examples
- C. Implement a small well-understood change directly
- D. Use plan mode to investigate and compare approaches

### 66. A single known function needs a clearly specified narrow correction. What mode is proportionate?

Domain: Claude Code

- A. Implement a small well-understood change directly
- B. Ask targeted design questions before implementation
- C. Delegate focused exploration to a read-oriented subagent
- D. Use plan mode to investigate and compare approaches

### 67. Detailed repository discovery would exhaust the coordinator's context. What delegation can help?

Domain: Claude Code

- A. Delegate focused exploration to a read-oriented subagent
- B. Use plan mode to investigate and compare approaches
- C. Implement a small well-understood change directly
- D. Ask targeted design questions before implementation

### 68. Packages duplicate the same changing instruction standard. What modular mechanism can reduce drift?

Domain: Claude Code

- A. Use @imports to keep instruction content modular
- B. Scope a rule with YAML paths glob patterns
- C. Organize focused conventions in .claude/rules/
- D. Put an on-demand workflow in a project skill

### 69. Generated tests invent unavailable helpers and duplicate existing cases. What repository evidence should be supplied?

Domain: Claude Code

- A. Put shared project standards in versioned CLAUDE.md
- B. Provide concrete input–output examples
- C. Provide existing tests and approved fixtures
- D. Use tests and specific failure feedback to drive iteration

### 70. A review rerun repeats resolved findings after every push. What context supports better comparison?

Domain: Claude Code

- A. Record detected_pattern and dismissal reasons
- B. State explicit reportable and non-reportable criteria
- C. Use an independent reviewer without the generator rationale
- D. Pass prior findings and request only new or unresolved issues

### 71. A plugin changes effective tools and defaults across machines. What management practice is needed?

Domain: Claude Code

- A. Pin compatible model, SDK, prompt, and dependency versions
- B. Use the appropriate settings.json scope for behavioral configuration
- C. Separate environment configuration from application logic
- D. Version and review plugin dependencies and permissions

### 72. A local override differs from shared configuration and causes inconsistent behavior. What diagnostic matters?

Domain: Claude Code

- A. Use the appropriate settings.json scope for behavioral configuration
- B. Put shared project standards in versioned CLAUDE.md
- C. Inspect which instruction files are actually loaded
- D. Put personal cross-project preferences in ~/.claude/CLAUDE.md

### 73. The repository needs shared contextual build commands, not only machine behavior settings. Where should instructions live?

Domain: Claude Code

- A. Organize focused conventions in .claude/rules/
- B. Use the appropriate settings.json scope for behavioral configuration
- C. Put personal cross-project preferences in ~/.claude/CLAUDE.md
- D. Put shared project standards in versioned CLAUDE.md

### 74. A developer connects to documented API streaming while integrating a code workflow. Which transport contract should not be confused with WebSockets?

Domain: Claude Code

- A. Use supported JSON output and schema CLI options
- B. Use WebSockets for an explicitly bidirectional persistent channel
- C. Run Claude Code in non-interactive print mode
- D. Consume the Messages stream as server-sent events

### 75. A contextual instruction forbids destructive writes but hard prevention is required. What must enforce it?

Domain: Claude Code

- A. Enforce prerequisites in trusted execution code
- B. Put shared project standards in versioned CLAUDE.md
- C. Put personal cross-project preferences in ~/.claude/CLAUDE.md
- D. Organize focused conventions in .claude/rules/

### 76. A user-visible answer is wrong, but the first failing boundary is unknown. What evidence should debugging inspect?

Domain: Eval, Testing, and Debugging

- A. Inspect a redacted end-to-end request and tool trace
- B. Use controlled stubs for repeatable failure-path tests
- C. State explicit reportable and non-reportable criteria
- D. Use a versioned representative held-out evaluation set

### 77. The model returns correct JSON, but persistence stores fields in reversed columns. What origin should be isolated?

Domain: Eval, Testing, and Debugging

- A. State explicit reportable and non-reportable criteria
- B. Use a versioned representative held-out evaluation set
- C. Isolate model-output defects from integration defects
- D. Inspect a redacted end-to-end request and tool trace

### 78. An operation rejects malformed arguments. Which recovery fits?

Domain: Eval, Testing, and Debugging

- A. Explain the non-retryable business-rule outcome
- B. Stop the unauthorized operation and use an approved access path
- C. Retry a transient failure with bounded backoff
- D. Correct invalid arguments before retrying

### 79. A provider reports temporary unavailability with permitted recovery guidance. What should the caller consider?

Domain: Eval, Testing, and Debugging

- A. Explain the non-retryable business-rule outcome
- B. Stop the unauthorized operation and use an approved access path
- C. Correct invalid arguments before retrying
- D. Retry a transient failure with bounded backoff

### 80. A request is denied for lack of authority. Which recovery should prevent credential evasion?

Domain: Eval, Testing, and Debugging

- A. Represent a successful query with no matches explicitly
- B. Retry a transient failure with bounded backoff
- C. Stop the unauthorized operation and use an approved access path
- D. Correct invalid arguments before retrying

### 81. A well-formed request violates a known eligibility rule. What classification should guide handling?

Domain: Eval, Testing, and Debugging

- A. Represent a successful query with no matches explicitly
- B. Explain the non-retryable business-rule outcome
- C. Correct invalid arguments before retrying
- D. Retry a transient failure with bounded backoff

### 82. An authorized query completes with no matches. What result must remain distinct from failure?

Domain: Eval, Testing, and Debugging

- A. Represent a successful query with no matches explicitly
- B. Retry a transient failure with bounded backoff
- C. Return a structured tool error with category and retryability
- D. Stop the unauthorized operation and use an approved access path

### 83. A response begins streaming normally but later fails. What error path must be handled?

Domain: Eval, Testing, and Debugging

- A. Handle errors after streaming has already begun
- B. Treat end_turn as the end of the current assistant turn
- C. Handle the output limit as an incomplete response
- D. Use the final assembled message and completion status

### 84. Parsing fails because the client treats each partial tool delta as complete JSON. What should be corrected?

Domain: Eval, Testing, and Debugging

- A. Consume the Messages stream as server-sent events
- B. Accumulate deltas by block index before final validation
- C. Use the final assembled message and completion status
- D. Dispatch response content according to each block type

### 85. A regression test needs repeatable timeouts without affecting production services. What testing tool fits?

Domain: Eval, Testing, and Debugging

- A. Use controlled stubs for repeatable failure-path tests
- B. Test the integration contract at the provider boundary
- C. Use a versioned representative held-out evaluation set
- D. Use tests and specific failure feedback to drive iteration

### 86. A failure spans several model and tool calls with no common trace identity. What should propagate?

Domain: Eval, Testing, and Debugging

- A. Record detected_pattern and dismissal reasons
- B. Propagate correlation identifiers across requests and tools
- C. Keep protected action and identity audit records
- D. Inspect a redacted end-to-end request and tool trace

### 87. A mocked success hides a real request serialization error. What testing boundary should be added?

Domain: Eval, Testing, and Debugging

- A. Use tests and specific failure feedback to drive iteration
- B. Use a versioned representative held-out evaluation set
- C. Use controlled stubs for repeatable failure-path tests
- D. Test the integration contract at the provider boundary

### 88. A retry storm appears because multiple layers each retry automatically. What should be inspected?

Domain: Eval, Testing, and Debugging

- A. Bound work queues and apply backpressure
- B. Coordinate retries across SDK and application layers
- C. Retry a transient failure with bounded backoff
- D. Set explicit deadlines and classify timeout outcomes

### 89. A request times out after a mutation might have completed. What should debugging avoid assuming?

Domain: Eval, Testing, and Debugging

- A. Set explicit deadlines and classify timeout outcomes
- B. Use a durable idempotency key for the same logical action
- C. Validate and commit business changes through a controlled boundary
- D. Cancel local work and reconcile any external operation separately

### 90. A typed output is valid but refers to the wrong source record. What validation failure is present?

Domain: Eval, Testing, and Debugging

- A. Allow explicit unknown or absent values in the schema
- B. Specify deterministic normalization rules and preserve originals when needed
- C. Use supported strict structured output with a schema
- D. Validate extracted values against evidence and business rules

### 91. A model appears to ignore instructions, but tracing reveals the system field was never sent. What should be inspected first?

Domain: Eval, Testing, and Debugging

- A. Inspect a redacted end-to-end request and tool trace
- B. Use a versioned representative held-out evaluation set
- C. State explicit reportable and non-reportable criteria
- D. Isolate model-output defects from integration defects

### 92. A prompt fix solves one example but breaks required languages. What regression coverage is needed?

Domain: Eval, Testing, and Debugging

- A. Use tests and specific failure feedback to drive iteration
- B. Provide concrete input–output examples
- C. State explicit reportable and non-reportable criteria
- D. Use a versioned representative held-out evaluation set

### 93. A bug cannot be reproduced because no one knows the deployed prompt or dependency revisions. What record is needed?

Domain: Eval, Testing, and Debugging

- A. Version exact prompt content and its dependencies
- B. Version and review plugin dependencies and permissions
- C. Pin compatible model, SDK, prompt, and dependency versions
- D. Separate environment configuration from application logic

### 94. A browser shows a partial response as complete after an event-stream disconnect. What path should be corrected?

Domain: Eval, Testing, and Debugging

- A. Treat end_turn as the end of the current assistant turn
- B. Handle the output limit as an incomplete response
- C. Handle errors after streaming has already begun
- D. Use the final assembled message and completion status

### 95. The raw response contains the required field, but a mapping function drops it. Where should the fix be targeted?

Domain: Eval, Testing, and Debugging

- A. Inspect a redacted end-to-end request and tool trace
- B. Isolate model-output defects from integration defects
- C. State explicit reportable and non-reportable criteria
- D. Use a versioned representative held-out evaluation set

### 96. An error handler was never exercised because tests cover only successful responses. What should be injected?

Domain: Eval, Testing, and Debugging

- A. Use controlled stubs for repeatable failure-path tests
- B. Use a versioned representative held-out evaluation set
- C. Use tests and specific failure feedback to drive iteration
- D. Test the integration contract at the provider boundary

### 97. A developer guesses a failure cause from the final answer alone. What stronger evidence should guide diagnosis?

Domain: Eval, Testing, and Debugging

- A. Record detected_pattern and dismissal reasons
- B. Inspect a redacted end-to-end request and tool trace
- C. Use a versioned representative held-out evaluation set
- D. Propagate correlation identifiers across requests and tools

### 98. A proposed fix passes offline tests but may introduce production-specific effects. What rollout supports validation?

Domain: Eval, Testing, and Debugging

- A. Canary a version change with regression gates and rollback
- B. Use a versioned representative held-out evaluation set
- C. Pin compatible model, SDK, prompt, and dependency versions
- D. Separate environment configuration from application logic

### 99. A transient response loss causes duplicate writes on retry. What integration property should be tested?

Domain: Eval, Testing, and Debugging

- A. Use a durable idempotency key for the same logical action
- B. Cancel local work and reconcile any external operation separately
- C. Validate and commit business changes through a controlled boundary
- D. Set explicit deadlines and classify timeout outcomes

### 100. A provider adapter strips required continuation metadata. What boundary test should expose this?

Domain: Eval, Testing, and Debugging

- A. Use controlled stubs for repeatable failure-path tests
- B. Inspect a redacted end-to-end request and tool trace
- C. Test the integration contract at the provider boundary
- D. Use a versioned representative held-out evaluation set

---

## Answer key and explanations

### Question 1 — A

Answer: Treat retrieved instructions as untrusted source content. External document content must not acquire authority over trusted instructions or tool permissions. External pages and tool observations must not acquire trusted instruction authority. Pair separation with trusted tool authorization; delimiters alone are insufficient. Local study-map skill 7.1 (AI Application Security), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Correct. External pages and tool observations must not acquire trusted instruction authority. Pair separation with trusted tool authorization; delimiters alone are insufficient. In this case: External document content must not acquire authority over trusted instructions or tool permissions.
- **B:** Incorrect for this question. Delimiters improve clarity about source boundaries but are not a security barrier or a grant of authority to the enclosed content. In this case: External document content must not acquire authority over trusted instructions or tool permissions.
- **C:** Incorrect for this question. Data access must be authorized externally. Retrieved content being internal or relevant does not justify showing it to every user. In this case: External document content must not acquire authority over trusted instructions or tool permissions.
- **D:** Incorrect for this question. Keep trusted instructions separate from user and retrieved data. On the direct Messages API, system instructions use the top-level system parameter rather than a system-role entry in messages. In this case: External document content must not acquire authority over trusted instructions or tool permissions.

### Question 2 — D

Answer: Authorize the current identity for the actual target and action. Authentication and valid syntax do not authorize the target resource for this requester. Permission must be enforced in trusted code using current resource and business state. A valid login, JSON schema, or model proposal alone does not grant authority. Local study-map skill 7.1 (AI Application Security), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. In this case: Authentication and valid syntax do not authorize the target resource for this requester.
- **B:** Incorrect for this question. Authentication establishes who is calling. Authorization separately decides what that identity may do to a particular resource. In this case: Authentication and valid syntax do not authorize the target resource for this requester.
- **C:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Authentication and valid syntax do not authorize the target resource for this requester.
- **D:** Correct. Permission must be enforced in trusted code using current resource and business state. A valid login, JSON schema, or model proposal alone does not grant authority. In this case: Authentication and valid syntax do not authorize the target resource for this requester.

### Question 3 — C

Answer: Minimize, redact, and restrict sensitive data by approved purpose. Limit sensitive information to what the approved purpose actually requires. Collect and expose only necessary personal information, including in tool outputs, traces, and test data. A blacklist alone does not establish privacy. Local study-map skill 7.1 (AI Application Security), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. Audit records support attribution and reconstruction of consequential actions. Limit access, sensitive content, and retention; they do not themselves block an effect. In this case: Limit sensitive information to what the approved purpose actually requires.
- **B:** Incorrect for this question. Statistical privacy mechanisms may protect aggregate publication under their assumptions. They do not replace purpose-limited collection, requester authorization, or operational secret management. In this case: Limit sensitive information to what the approved purpose actually requires.
- **C:** Correct. Collect and expose only necessary personal information, including in tool outputs, traces, and test data. A blacklist alone does not establish privacy. In this case: Limit sensitive information to what the approved purpose actually requires.
- **D:** Incorrect for this question. Parameter freezing does not imply no logs, abuse monitoring, stored history, or caches. Review provider, plan, region, settings, and contractual obligations. In this case: Limit sensitive information to what the approved purpose actually requires.

### Question 4 — C

Answer: Treat model output as untrusted before rendering or execution. Generated content remains untrusted for rendering even when its container is valid JSON. Use destination-appropriate escaping, validation, and permission checks. Valid JSON can still contain executable or malicious values. Local study-map skill 7.1 (AI Application Security), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. Temperature changes next-token sampling behavior where supported. Lowering it does not independently guarantee correct extraction, grounding, or identical execution. In this case: Generated content remains untrusted for rendering even when its container is valid JSON.
- **B:** Incorrect for this question. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Generated content remains untrusted for rendering even when its container is valid JSON.
- **C:** Correct. Use destination-appropriate escaping, validation, and permission checks. Valid JSON can still contain executable or malicious values. In this case: Generated content remains untrusted for rendering even when its container is valid JSON.
- **D:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Generated content remains untrusted for rendering even when its container is valid JSON.

### Question 5 — D

Answer: Restrict network destinations and prevent unsafe fetch paths. Trusted destination and address restrictions reduce unsafe network fetch and exfiltration paths. Enforce approved destinations and address handling to reduce exfiltration and SSRF risk. A friendly tool name or URL string check alone is not enough. Local study-map skill 7.1 (AI Application Security), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. External pages and tool observations must not acquire trusted instruction authority. Pair separation with trusted tool authorization; delimiters alone are insufficient. In this case: Trusted destination and address restrictions reduce unsafe network fetch and exfiltration paths.
- **B:** Incorrect for this question. Network segmentation limits movement between execution environments. It does not by itself validate every URL, authorize business actions, or replace specific egress controls. In this case: Trusted destination and address restrictions reduce unsafe network fetch and exfiltration paths.
- **C:** Incorrect for this question. Data access must be authorized externally. Retrieved content being internal or relevant does not justify showing it to every user. In this case: Trusted destination and address restrictions reduce unsafe network fetch and exfiltration paths.
- **D:** Correct. Enforce approved destinations and address handling to reduce exfiltration and SSRF risk. A friendly tool name or URL string check alone is not enough. In this case: Trusted destination and address restrictions reduce unsafe network fetch and exfiltration paths.

### Question 6 — D

Answer: Validate and encode untrusted values for their destination. Constrain execution and validate or encode values for their actual destination. Model-generated strings are not safe SQL, shell, HTML, or filenames by default. Prefer parameterized operations, output encoding, and constrained execution paths. Local study-map skill 7.1 (AI Application Security), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Constrain execution and validate or encode values for their actual destination.
- **B:** Incorrect for this question. Temperature changes next-token sampling behavior where supported. Lowering it does not independently guarantee correct extraction, grounding, or identical execution. In this case: Constrain execution and validate or encode values for their actual destination.
- **C:** Incorrect for this question. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Constrain execution and validate or encode values for their actual destination.
- **D:** Correct. Model-generated strings are not safe SQL, shell, HTML, or filenames by default. Prefer parameterized operations, output encoding, and constrained execution paths. In this case: Constrain execution and validate or encode values for their actual destination.

### Question 7 — B

Answer: Review the exact service data-use and retention controls. Data storage and use depend on actual service terms and configuration, not weight updates. Parameter freezing does not imply no logs, abuse monitoring, stored history, or caches. Review provider, plan, region, settings, and contractual obligations. Local study-map skill 7.1 (AI Application Security), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. Statistical privacy mechanisms may protect aggregate publication under their assumptions. They do not replace purpose-limited collection, requester authorization, or operational secret management. In this case: Data storage and use depend on actual service terms and configuration, not weight updates.
- **B:** Correct. Parameter freezing does not imply no logs, abuse monitoring, stored history, or caches. Review provider, plan, region, settings, and contractual obligations. In this case: Data storage and use depend on actual service terms and configuration, not weight updates.
- **C:** Incorrect for this question. Collect and expose only necessary personal information, including in tool outputs, traces, and test data. A blacklist alone does not establish privacy. In this case: Data storage and use depend on actual service terms and configuration, not weight updates.
- **D:** Incorrect for this question. Audit records support attribution and reconstruction of consequential actions. Limit access, sensitive content, and retention; they do not themselves block an effect. In this case: Data storage and use depend on actual service terms and configuration, not weight updates.

### Question 8 — A

Answer: Apply requester permissions before evidence enters model context. Evidence must follow requester permissions before restricted content reaches model context. Data access must be authorized externally. Retrieved content being internal or relevant does not justify showing it to every user. Local study-map skill 7.1 (AI Application Security), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Correct. Data access must be authorized externally. Retrieved content being internal or relevant does not justify showing it to every user. In this case: Evidence must follow requester permissions before restricted content reaches model context.
- **B:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Evidence must follow requester permissions before restricted content reaches model context.
- **C:** Incorrect for this question. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: Evidence must follow requester permissions before restricted content reaches model context.
- **D:** Incorrect for this question. External pages and tool observations must not acquire trusted instruction authority. Pair separation with trusted tool authorization; delimiters alone are insufficient. In this case: Evidence must follow requester permissions before restricted content reaches model context.

### Question 9 — C

Answer: Authorize the current identity for the actual target and action. Authorize the actual target and action rather than trust model-generated arguments. Permission must be enforced in trusted code using current resource and business state. A valid login, JSON schema, or model proposal alone does not grant authority. Local study-map skill 7.1 (AI Application Security), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. In this case: Authorize the actual target and action rather than trust model-generated arguments.
- **B:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Authorize the actual target and action rather than trust model-generated arguments.
- **C:** Correct. Permission must be enforced in trusted code using current resource and business state. A valid login, JSON schema, or model proposal alone does not grant authority. In this case: Authorize the actual target and action rather than trust model-generated arguments.
- **D:** Incorrect for this question. Authentication establishes who is calling. Authorization separately decides what that identity may do to a particular resource. In this case: Authorize the actual target and action rather than trust model-generated arguments.

### Question 10 — B

Answer: Minimize, redact, and restrict sensitive data by approved purpose. Telemetry also needs purpose-limited sensitive-data handling rather than indiscriminate logging. Collect and expose only necessary personal information, including in tool outputs, traces, and test data. A blacklist alone does not establish privacy. Local study-map skill 7.1 (AI Application Security), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. Audit records support attribution and reconstruction of consequential actions. Limit access, sensitive content, and retention; they do not themselves block an effect. In this case: Telemetry also needs purpose-limited sensitive-data handling rather than indiscriminate logging.
- **B:** Correct. Collect and expose only necessary personal information, including in tool outputs, traces, and test data. A blacklist alone does not establish privacy. In this case: Telemetry also needs purpose-limited sensitive-data handling rather than indiscriminate logging.
- **C:** Incorrect for this question. Parameter freezing does not imply no logs, abuse monitoring, stored history, or caches. Review provider, plan, region, settings, and contractual obligations. In this case: Telemetry also needs purpose-limited sensitive-data handling rather than indiscriminate logging.
- **D:** Incorrect for this question. Statistical privacy mechanisms may protect aggregate publication under their assumptions. They do not replace purpose-limited collection, requester authorization, or operational secret management. In this case: Telemetry also needs purpose-limited sensitive-data handling rather than indiscriminate logging.

### Question 11 — A

Answer: Treat retrieved instructions as untrusted source content. Treat the response as untrusted observation data and retain external authorization controls. External pages and tool observations must not acquire trusted instruction authority. Pair separation with trusted tool authorization; delimiters alone are insufficient. Local study-map skill 7.1 (AI Application Security), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Correct. External pages and tool observations must not acquire trusted instruction authority. Pair separation with trusted tool authorization; delimiters alone are insufficient. In this case: Treat the response as untrusted observation data and retain external authorization controls.
- **B:** Incorrect for this question. Data access must be authorized externally. Retrieved content being internal or relevant does not justify showing it to every user. In this case: Treat the response as untrusted observation data and retain external authorization controls.
- **C:** Incorrect for this question. Keep trusted instructions separate from user and retrieved data. On the direct Messages API, system instructions use the top-level system parameter rather than a system-role entry in messages. In this case: Treat the response as untrusted observation data and retain external authorization controls.
- **D:** Incorrect for this question. Delimiters improve clarity about source boundaries but are not a security barrier or a grant of authority to the enclosed content. In this case: Treat the response as untrusted observation data and retain external authorization controls.

### Question 12 — B

Answer: Treat model output as untrusted before rendering or execution. Destination-specific path constraints must apply before file access or modification. Use destination-appropriate escaping, validation, and permission checks. Valid JSON can still contain executable or malicious values. Local study-map skill 7.1 (AI Application Security), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. Temperature changes next-token sampling behavior where supported. Lowering it does not independently guarantee correct extraction, grounding, or identical execution. In this case: Destination-specific path constraints must apply before file access or modification.
- **B:** Correct. Use destination-appropriate escaping, validation, and permission checks. Valid JSON can still contain executable or malicious values. In this case: Destination-specific path constraints must apply before file access or modification.
- **C:** Incorrect for this question. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Destination-specific path constraints must apply before file access or modification.
- **D:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Destination-specific path constraints must apply before file access or modification.

### Question 13 — D

Answer: Authenticate the calling identity. Authentication establishes identity, while later authorization checks allowed actions. Authentication establishes who is calling. Authorization separately decides what that identity may do to a particular resource. Local study-map skill 7.1 (AI Application Security), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. Data access must be authorized externally. Retrieved content being internal or relevant does not justify showing it to every user. In this case: Authentication establishes identity, while later authorization checks allowed actions.
- **B:** Incorrect for this question. Permission must be enforced in trusted code using current resource and business state. A valid login, JSON schema, or model proposal alone does not grant authority. In this case: Authentication establishes identity, while later authorization checks allowed actions.
- **C:** Incorrect for this question. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Authentication establishes identity, while later authorization checks allowed actions.
- **D:** Correct. Authentication establishes who is calling. Authorization separately decides what that identity may do to a particular resource. In this case: Authentication establishes identity, while later authorization checks allowed actions.

### Question 14 — A

Answer: Authorize the current identity for the actual target and action. Authorization is resource- and action-specific rather than automatically granted by login. Permission must be enforced in trusted code using current resource and business state. A valid login, JSON schema, or model proposal alone does not grant authority. Local study-map skill 7.1 (AI Application Security), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Correct. Permission must be enforced in trusted code using current resource and business state. A valid login, JSON schema, or model proposal alone does not grant authority. In this case: Authorization is resource- and action-specific rather than automatically granted by login.
- **B:** Incorrect for this question. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Authorization is resource- and action-specific rather than automatically granted by login.
- **C:** Incorrect for this question. Data access must be authorized externally. Retrieved content being internal or relevant does not justify showing it to every user. In this case: Authorization is resource- and action-specific rather than automatically granted by login.
- **D:** Incorrect for this question. Authentication establishes who is calling. Authorization separately decides what that identity may do to a particular resource. In this case: Authorization is resource- and action-specific rather than automatically granted by login.

### Question 15 — D

Answer: Review the exact service data-use and retention controls. Review exact service, plan, settings, and contracts rather than infer universal guarantees from branding. Parameter freezing does not imply no logs, abuse monitoring, stored history, or caches. Review provider, plan, region, settings, and contractual obligations. Local study-map skill 7.1 (AI Application Security), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. Collect and expose only necessary personal information, including in tool outputs, traces, and test data. A blacklist alone does not establish privacy. In this case: Review exact service, plan, settings, and contracts rather than infer universal guarantees from branding.
- **B:** Incorrect for this question. Statistical privacy mechanisms may protect aggregate publication under their assumptions. They do not replace purpose-limited collection, requester authorization, or operational secret management. In this case: Review exact service, plan, settings, and contracts rather than infer universal guarantees from branding.
- **C:** Incorrect for this question. Audit records support attribution and reconstruction of consequential actions. Limit access, sensitive content, and retention; they do not themselves block an effect. In this case: Review exact service, plan, settings, and contracts rather than infer universal guarantees from branding.
- **D:** Correct. Parameter freezing does not imply no logs, abuse monitoring, stored history, or caches. Review provider, plan, region, settings, and contractual obligations. In this case: Review exact service, plan, settings, and contracts rather than infer universal guarantees from branding.

### Question 16 — B

Answer: Restrict network destinations and prevent unsafe fetch paths. Enforce approved network destinations and address handling inside the trusted boundary. Enforce approved destinations and address handling to reduce exfiltration and SSRF risk. A friendly tool name or URL string check alone is not enough. Local study-map skill 7.1 (AI Application Security), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. External pages and tool observations must not acquire trusted instruction authority. Pair separation with trusted tool authorization; delimiters alone are insufficient. In this case: Enforce approved network destinations and address handling inside the trusted boundary.
- **B:** Correct. Enforce approved destinations and address handling to reduce exfiltration and SSRF risk. A friendly tool name or URL string check alone is not enough. In this case: Enforce approved network destinations and address handling inside the trusted boundary.
- **C:** Incorrect for this question. Data access must be authorized externally. Retrieved content being internal or relevant does not justify showing it to every user. In this case: Enforce approved network destinations and address handling inside the trusted boundary.
- **D:** Incorrect for this question. Network segmentation limits movement between execution environments. It does not by itself validate every URL, authorize business actions, or replace specific egress controls. In this case: Enforce approved network destinations and address handling inside the trusted boundary.

### Question 17 — D

Answer: Minimize, redact, and restrict sensitive data by approved purpose. Use only necessary approved sensitive data and protect test information like other copies. Collect and expose only necessary personal information, including in tool outputs, traces, and test data. A blacklist alone does not establish privacy. Local study-map skill 7.1 (AI Application Security), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. Statistical privacy mechanisms may protect aggregate publication under their assumptions. They do not replace purpose-limited collection, requester authorization, or operational secret management. In this case: Use only necessary approved sensitive data and protect test information like other copies.
- **B:** Incorrect for this question. Audit records support attribution and reconstruction of consequential actions. Limit access, sensitive content, and retention; they do not themselves block an effect. In this case: Use only necessary approved sensitive data and protect test information like other copies.
- **C:** Incorrect for this question. Parameter freezing does not imply no logs, abuse monitoring, stored history, or caches. Review provider, plan, region, settings, and contractual obligations. In this case: Use only necessary approved sensitive data and protect test information like other copies.
- **D:** Correct. Collect and expose only necessary personal information, including in tool outputs, traces, and test data. A blacklist alone does not establish privacy. In this case: Use only necessary approved sensitive data and protect test information like other copies.

### Question 18 — D

Answer: Treat retrieved instructions as untrusted source content. Untrusted source text cannot grant new instruction or execution authority. External pages and tool observations must not acquire trusted instruction authority. Pair separation with trusted tool authorization; delimiters alone are insufficient. Local study-map skill 7.1 (AI Application Security), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. Delimiters improve clarity about source boundaries but are not a security barrier or a grant of authority to the enclosed content. In this case: Untrusted source text cannot grant new instruction or execution authority.
- **B:** Incorrect for this question. Keep trusted instructions separate from user and retrieved data. On the direct Messages API, system instructions use the top-level system parameter rather than a system-role entry in messages. In this case: Untrusted source text cannot grant new instruction or execution authority.
- **C:** Incorrect for this question. Data access must be authorized externally. Retrieved content being internal or relevant does not justify showing it to every user. In this case: Untrusted source text cannot grant new instruction or execution authority.
- **D:** Correct. External pages and tool observations must not acquire trusted instruction authority. Pair separation with trusted tool authorization; delimiters alone are insufficient. In this case: Untrusted source text cannot grant new instruction or execution authority.

### Question 19 — A

Answer: Validate and encode untrusted values for their destination. Use parameterized operations and trusted validation instead of interpolate generated strings. Model-generated strings are not safe SQL, shell, HTML, or filenames by default. Prefer parameterized operations, output encoding, and constrained execution paths. Local study-map skill 7.1 (AI Application Security), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Correct. Model-generated strings are not safe SQL, shell, HTML, or filenames by default. Prefer parameterized operations, output encoding, and constrained execution paths. In this case: Use parameterized operations and trusted validation instead of interpolate generated strings.
- **B:** Incorrect for this question. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Use parameterized operations and trusted validation instead of interpolate generated strings.
- **C:** Incorrect for this question. Temperature changes next-token sampling behavior where supported. Lowering it does not independently guarantee correct extraction, grounding, or identical execution. In this case: Use parameterized operations and trusted validation instead of interpolate generated strings.
- **D:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Use parameterized operations and trusted validation instead of interpolate generated strings.

### Question 20 — B

Answer: Authorize the current identity for the actual target and action. Current authority for the actual action must be checked, not stale eligibility. Permission must be enforced in trusted code using current resource and business state. A valid login, JSON schema, or model proposal alone does not grant authority. Local study-map skill 7.1 (AI Application Security), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. Data access must be authorized externally. Retrieved content being internal or relevant does not justify showing it to every user. In this case: Current authority for the actual action must be checked, not stale eligibility.
- **B:** Correct. Permission must be enforced in trusted code using current resource and business state. A valid login, JSON schema, or model proposal alone does not grant authority. In this case: Current authority for the actual action must be checked, not stale eligibility.
- **C:** Incorrect for this question. Authentication establishes who is calling. Authorization separately decides what that identity may do to a particular resource. In this case: Current authority for the actual action must be checked, not stale eligibility.
- **D:** Incorrect for this question. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Current authority for the actual action must be checked, not stale eligibility.

### Question 21 — B

Answer: Layer prevention, detection, approval, and recovery controls. Combine trusted permissions, constrained execution, detection, review, and recovery instead of one prompt. No one prompt or content filter covers all attack paths. Combine least privilege, trusted checks, telemetry, tests, and incident response. Local study-map skill 7.2 (Guardrails and Safe Deployment), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. Content controls address applicable unsafe-content categories. They are not a replacement for identity checks, resource authorization, constrained tools, or secure execution. In this case: Combine trusted permissions, constrained execution, detection, review, and recovery instead of one prompt.
- **B:** Correct. No one prompt or content filter covers all attack paths. Combine least privilege, trusted checks, telemetry, tests, and incident response. In this case: Combine trusted permissions, constrained execution, detection, review, and recovery instead of one prompt.
- **C:** Incorrect for this question. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Combine trusted permissions, constrained execution, detection, review, and recovery instead of one prompt.
- **D:** Incorrect for this question. Review must gate the external effect, be tied to the intended action, and use current authority. A later audit cannot reliably reverse a completed effect. In this case: Combine trusted permissions, constrained execution, detection, review, and recovery instead of one prompt.

### Question 22 — A

Answer: Give each specialist only task-relevant tools. Limit effective capabilities to the specialist's intended responsibilities. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. Local study-map skill 7.2 (Guardrails and Safe Deployment), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Correct. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Limit effective capabilities to the specialist's intended responsibilities.
- **B:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Limit effective capabilities to the specialist's intended responsibilities.
- **C:** Incorrect for this question. Configured servers can expose tools together when connected, but server failure, approval, filtering, and permissions can affect what is actually usable. In this case: Limit effective capabilities to the specialist's intended responsibilities.
- **D:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Limit effective capabilities to the specialist's intended responsibilities.

### Question 23 — A

Answer: Require authorized approval before the consequential action. Human approval must gate the current action before its effect occurs. Review must gate the external effect, be tied to the intended action, and use current authority. A later audit cannot reliably reverse a completed effect. Local study-map skill 7.2 (Guardrails and Safe Deployment), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Correct. Review must gate the external effect, be tied to the intended action, and use current authority. A later audit cannot reliably reverse a completed effect. In this case: Human approval must gate the current action before its effect occurs.
- **B:** Incorrect for this question. Audit records support attribution and reconstruction of consequential actions. Limit access, sensitive content, and retention; they do not themselves block an effect. In this case: Human approval must gate the current action before its effect occurs.
- **C:** Incorrect for this question. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Human approval must gate the current action before its effect occurs.
- **D:** Incorrect for this question. Observe deployed latency, failures, drift, and task outcomes with accountable response thresholds. Monitoring differs from an offline evaluation or a single diagnostic trace. In this case: Human approval must gate the current action before its effect occurs.

### Question 24 — C

Answer: Canary a version change with regression gates and rollback. Stage exposure with acceptance gates, monitoring, and a rollback route. Stage exposure to the new configuration, compare required outcomes, and retain a known-good path. A vendor release note is not workload validation. Local study-map skill 7.2 (Guardrails and Safe Deployment), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: Stage exposure with acceptance gates, monitoring, and a rollback route.
- **B:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Stage exposure with acceptance gates, monitoring, and a rollback route.
- **C:** Correct. Stage exposure to the new configuration, compare required outcomes, and retain a known-good path. A vendor release note is not workload validation. In this case: Stage exposure with acceptance gates, monitoring, and a rollback route.
- **D:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Stage exposure with acceptance gates, monitoring, and a rollback route.

### Question 25 — A

Answer: Test adversarial and misuse scenarios. Adversarial tests investigate bypasses and harmful interactions beyond happy-path behavior. Probe injection, bypasses, harmful tool combinations, and failures beyond friendly expected inputs. Finite adversarial testing does not prove that every future attack is prevented. Local study-map skill 7.2 (Guardrails and Safe Deployment), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Correct. Probe injection, bypasses, harmful tool combinations, and failures beyond friendly expected inputs. Finite adversarial testing does not prove that every future attack is prevented. In this case: Adversarial tests investigate bypasses and harmful interactions beyond happy-path behavior.
- **B:** Incorrect for this question. Inject timeouts, malformed responses, and provider failures without live side effects. Combine with contract and representative integration tests rather than infer complete correctness from mocks. In this case: Adversarial tests investigate bypasses and harmful interactions beyond happy-path behavior.
- **C:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Adversarial tests investigate bypasses and harmful interactions beyond happy-path behavior.
- **D:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Adversarial tests investigate bypasses and harmful interactions beyond happy-path behavior.

### Question 26 — B

Answer: Activate coordinated incident response and recovery. Containment, investigation, recovery, and communication require incident-response ownership. Contain verified harm, investigate affected systems and data, recover safely, and communicate through accountable owners. Observation alone is not containment. Local study-map skill 7.2 (Guardrails and Safe Deployment), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. Observe deployed latency, failures, drift, and task outcomes with accountable response thresholds. Monitoring differs from an offline evaluation or a single diagnostic trace. In this case: Containment, investigation, recovery, and communication require incident-response ownership.
- **B:** Correct. Contain verified harm, investigate affected systems and data, recover safely, and communicate through accountable owners. Observation alone is not containment. In this case: Containment, investigation, recovery, and communication require incident-response ownership.
- **C:** Incorrect for this question. Correlate the actual request, model response, tool execution, retries, and validation results. Diagnose the first failing boundary rather than infer cause from the final prose. In this case: Containment, investigation, recovery, and communication require incident-response ownership.
- **D:** Incorrect for this question. Audit records support attribution and reconstruction of consequential actions. Limit access, sensitive content, and retention; they do not themselves block an effect. In this case: Containment, investigation, recovery, and communication require incident-response ownership.

### Question 27 — A

Answer: Layer prevention, detection, approval, and recovery controls. Security needs complementary controls for distinct risks rather than treat moderation as universal authorization. No one prompt or content filter covers all attack paths. Combine least privilege, trusted checks, telemetry, tests, and incident response. Local study-map skill 7.2 (Guardrails and Safe Deployment), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Correct. No one prompt or content filter covers all attack paths. Combine least privilege, trusted checks, telemetry, tests, and incident response. In this case: Security needs complementary controls for distinct risks rather than treat moderation as universal authorization.
- **B:** Incorrect for this question. Content controls address applicable unsafe-content categories. They are not a replacement for identity checks, resource authorization, constrained tools, or secure execution. In this case: Security needs complementary controls for distinct risks rather than treat moderation as universal authorization.
- **C:** Incorrect for this question. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Security needs complementary controls for distinct risks rather than treat moderation as universal authorization.
- **D:** Incorrect for this question. Review must gate the external effect, be tied to the intended action, and use current authority. A later audit cannot reliably reverse a completed effect. In this case: Security needs complementary controls for distinct risks rather than treat moderation as universal authorization.

### Question 28 — D

Answer: Give each specialist only task-relevant tools. Expanded authority changes permitted tasks, consequences, and required enforcement. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. Local study-map skill 7.2 (Guardrails and Safe Deployment), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. In this case: Expanded authority changes permitted tasks, consequences, and required enforcement.
- **B:** Incorrect for this question. Review must gate the external effect, be tied to the intended action, and use current authority. A later audit cannot reliably reverse a completed effect. In this case: Expanded authority changes permitted tasks, consequences, and required enforcement.
- **C:** Incorrect for this question. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Expanded authority changes permitted tasks, consequences, and required enforcement.
- **D:** Correct. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Expanded authority changes permitted tasks, consequences, and required enforcement.

### Question 29 — D

Answer: Keep protected action and identity audit records. Protected purpose-limited audit records balance accountability with sensitive-data controls. Audit records support attribution and reconstruction of consequential actions. Limit access, sensitive content, and retention; they do not themselves block an effect. Local study-map skill 7.2 (Guardrails and Safe Deployment), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. Correlate the actual request, model response, tool execution, retries, and validation results. Diagnose the first failing boundary rather than infer cause from the final prose. In this case: Protected purpose-limited audit records balance accountability with sensitive-data controls.
- **B:** Incorrect for this question. Observe deployed latency, failures, drift, and task outcomes with accountable response thresholds. Monitoring differs from an offline evaluation or a single diagnostic trace. In this case: Protected purpose-limited audit records balance accountability with sensitive-data controls.
- **C:** Incorrect for this question. Link a user task to provider requests, worker runs, and actions without using sensitive content as an identifier. Protect telemetry access and retention. In this case: Protected purpose-limited audit records balance accountability with sensitive-data controls.
- **D:** Correct. Audit records support attribution and reconstruction of consequential actions. Limit access, sensitive content, and retention; they do not themselves block an effect. In this case: Protected purpose-limited audit records balance accountability with sensitive-data controls.

### Question 30 — A

Answer: Layer prevention, detection, approval, and recovery controls. Layered ongoing controls and recovery remain necessary because finite tests do not prove complete security. No one prompt or content filter covers all attack paths. Combine least privilege, trusted checks, telemetry, tests, and incident response. Local study-map skill 7.2 (Guardrails and Safe Deployment), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Correct. No one prompt or content filter covers all attack paths. Combine least privilege, trusted checks, telemetry, tests, and incident response. In this case: Layered ongoing controls and recovery remain necessary because finite tests do not prove complete security.
- **B:** Incorrect for this question. Probe injection, bypasses, harmful tool combinations, and failures beyond friendly expected inputs. Finite adversarial testing does not prove that every future attack is prevented. In this case: Layered ongoing controls and recovery remain necessary because finite tests do not prove complete security.
- **C:** Incorrect for this question. Content controls address applicable unsafe-content categories. They are not a replacement for identity checks, resource authorization, constrained tools, or secure execution. In this case: Layered ongoing controls and recovery remain necessary because finite tests do not prove complete security.
- **D:** Incorrect for this question. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Layered ongoing controls and recovery remain necessary because finite tests do not prove complete security.

### Question 31 — C

Answer: Use pre-execution tool interception for blocking policy checks. A pre-execution gate can deny the effect before it occurs. An appropriate pre-tool hook or equivalent trusted gate can deny a disallowed action before it runs. Hook implementation and failure handling must be tested. Local study-map skill 7.3 (Claude Hooks), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. In this case: A pre-execution gate can deny the effect before it occurs.
- **B:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: A pre-execution gate can deny the effect before it occurs.
- **C:** Correct. An appropriate pre-tool hook or equivalent trusted gate can deny a disallowed action before it runs. Hook implementation and failure handling must be tested. In this case: A pre-execution gate can deny the effect before it occurs.
- **D:** Incorrect for this question. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: A pre-execution gate can deny the effect before it occurs.

### Question 32 — B

Answer: Normalize tool observations before model consumption. Normalize observations while preserving their meaning and truthful outcome. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. Local study-map skill 7.3 (Claude Hooks), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Normalize observations while preserving their meaning and truthful outcome.
- **B:** Correct. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. In this case: Normalize observations while preserving their meaning and truthful outcome.
- **C:** Incorrect for this question. An appropriate pre-tool hook or equivalent trusted gate can deny a disallowed action before it runs. Hook implementation and failure handling must be tested. In this case: Normalize observations while preserving their meaning and truthful outcome.
- **D:** Incorrect for this question. Review must gate the external effect, be tied to the intended action, and use current authority. A later audit cannot reliably reverse a completed effect. In this case: Normalize observations while preserving their meaning and truthful outcome.

### Question 33 — C

Answer: Use pre-execution tool interception for blocking policy checks. Blocking must happen before the sensitive external effect rather than only after detection. An appropriate pre-tool hook or equivalent trusted gate can deny a disallowed action before it runs. Hook implementation and failure handling must be tested. Local study-map skill 7.3 (Claude Hooks), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. In this case: Blocking must happen before the sensitive external effect rather than only after detection.
- **B:** Incorrect for this question. Observe deployed latency, failures, drift, and task outcomes with accountable response thresholds. Monitoring differs from an offline evaluation or a single diagnostic trace. In this case: Blocking must happen before the sensitive external effect rather than only after detection.
- **C:** Correct. An appropriate pre-tool hook or equivalent trusted gate can deny a disallowed action before it runs. Hook implementation and failure handling must be tested. In this case: Blocking must happen before the sensitive external effect rather than only after detection.
- **D:** Incorrect for this question. Audit records support attribution and reconstruction of consequential actions. Limit access, sensitive content, and retention; they do not themselves block an effect. In this case: Blocking must happen before the sensitive external effect rather than only after detection.

### Question 34 — C

Answer: Enforce prerequisites in trusted execution code. Trusted code must inspect authoritative current approval and business state. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. Local study-map skill 7.3 (Claude Hooks), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Trusted code must inspect authoritative current approval and business state.
- **B:** Incorrect for this question. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: Trusted code must inspect authoritative current approval and business state.
- **C:** Correct. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Trusted code must inspect authoritative current approval and business state.
- **D:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Trusted code must inspect authoritative current approval and business state.

### Question 35 — C

Answer: Use pre-execution tool interception for blocking policy checks. Intercept and validate the actual write before execution. An appropriate pre-tool hook or equivalent trusted gate can deny a disallowed action before it runs. Hook implementation and failure handling must be tested. Local study-map skill 7.3 (Claude Hooks), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. In this case: Intercept and validate the actual write before execution.
- **B:** Incorrect for this question. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. In this case: Intercept and validate the actual write before execution.
- **C:** Correct. An appropriate pre-tool hook or equivalent trusted gate can deny a disallowed action before it runs. Hook implementation and failure handling must be tested. In this case: Intercept and validate the actual write before execution.
- **D:** Incorrect for this question. Review must gate the external effect, be tied to the intended action, and use current authority. A later audit cannot reliably reverse a completed effect. In this case: Intercept and validate the actual write before execution.

### Question 36 — B

Answer: Normalize tool observations before model consumption. Normalization must preserve uncertainty instead of fabricate successful outcomes. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. Local study-map skill 7.3 (Claude Hooks), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Normalization must preserve uncertainty instead of fabricate successful outcomes.
- **B:** Correct. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. In this case: Normalization must preserve uncertainty instead of fabricate successful outcomes.
- **C:** Incorrect for this question. Review must gate the external effect, be tied to the intended action, and use current authority. A later audit cannot reliably reverse a completed effect. In this case: Normalization must preserve uncertainty instead of fabricate successful outcomes.
- **D:** Incorrect for this question. An appropriate pre-tool hook or equivalent trusted gate can deny a disallowed action before it runs. Hook implementation and failure handling must be tested. In this case: Normalization must preserve uncertainty instead of fabricate successful outcomes.

### Question 37 — D

Answer: Enforce prerequisites in trusted execution code. Trusted execution checks must enforce mandatory rules independently of contextual guidance. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. Local study-map skill 7.3 (Claude Hooks), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: Trusted execution checks must enforce mandatory rules independently of contextual guidance.
- **B:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Trusted execution checks must enforce mandatory rules independently of contextual guidance.
- **C:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Trusted execution checks must enforce mandatory rules independently of contextual guidance.
- **D:** Correct. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Trusted execution checks must enforce mandatory rules independently of contextual guidance.

### Question 38 — C

Answer: Use pre-execution tool interception for blocking policy checks. Appropriate pre-tool interception can inspect and deny disallowed arguments. An appropriate pre-tool hook or equivalent trusted gate can deny a disallowed action before it runs. Hook implementation and failure handling must be tested. Local study-map skill 7.3 (Claude Hooks), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: Appropriate pre-tool interception can inspect and deny disallowed arguments.
- **B:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Appropriate pre-tool interception can inspect and deny disallowed arguments.
- **C:** Correct. An appropriate pre-tool hook or equivalent trusted gate can deny a disallowed action before it runs. Hook implementation and failure handling must be tested. In this case: Appropriate pre-tool interception can inspect and deny disallowed arguments.
- **D:** Incorrect for this question. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. In this case: Appropriate pre-tool interception can inspect and deny disallowed arguments.

### Question 39 — B

Answer: Use controlled stubs for repeatable failure-path tests. Controlled stubs can exercise enforcement and failure paths safely and repeatably. Inject timeouts, malformed responses, and provider failures without live side effects. Combine with contract and representative integration tests rather than infer complete correctness from mocks. Local study-map skill 7.3 (Claude Hooks), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. Check serialized requests, content blocks, status handling, and representative responses. Mock success alone may not reveal a malformed real request or unsupported provider feature. In this case: Controlled stubs can exercise enforcement and failure paths safely and repeatably.
- **B:** Correct. Inject timeouts, malformed responses, and provider failures without live side effects. Combine with contract and representative integration tests rather than infer complete correctness from mocks. In this case: Controlled stubs can exercise enforcement and failure paths safely and repeatably.
- **C:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Controlled stubs can exercise enforcement and failure paths safely and repeatably.
- **D:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Controlled stubs can exercise enforcement and failure paths safely and repeatably.

### Question 40 — C

Answer: Layer prevention, detection, approval, and recovery controls. Combine complementary enforcement and recovery controls rather than rely on one interception point. No one prompt or content filter covers all attack paths. Combine least privilege, trusted checks, telemetry, tests, and incident response. Local study-map skill 7.3 (Claude Hooks), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. In this case: Combine complementary enforcement and recovery controls rather than rely on one interception point.
- **B:** Incorrect for this question. Review must gate the external effect, be tied to the intended action, and use current authority. A later audit cannot reliably reverse a completed effect. In this case: Combine complementary enforcement and recovery controls rather than rely on one interception point.
- **C:** Correct. No one prompt or content filter covers all attack paths. Combine least privilege, trusted checks, telemetry, tests, and incident response. In this case: Combine complementary enforcement and recovery controls rather than rely on one interception point.
- **D:** Incorrect for this question. An appropriate pre-tool hook or equivalent trusted gate can deny a disallowed action before it runs. Hook implementation and failure handling must be tested. In this case: Combine complementary enforcement and recovery controls rather than rely on one interception point.

### Question 41 — C

Answer: Manage credentials in protected execution infrastructure. Store secrets in controlled execution infrastructure rather than model-visible instructions. Keep credentials out of prompts, repositories, generated output, and unprotected logs. Supply narrowly scoped credentials through approved runtime secret mechanisms. Local study-map skill 7.4 (Identity, Secrets, and Key Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. Environment expansion can keep literal secrets out of project files. Supply credentials through an approved secret path and protect logs as well. In this case: Store secrets in controlled execution infrastructure rather than model-visible instructions.
- **B:** Incorrect for this question. Permission must be enforced in trusted code using current resource and business state. A valid login, JSON schema, or model proposal alone does not grant authority. In this case: Store secrets in controlled execution infrastructure rather than model-visible instructions.
- **C:** Correct. Keep credentials out of prompts, repositories, generated output, and unprotected logs. Supply narrowly scoped credentials through approved runtime secret mechanisms. In this case: Store secrets in controlled execution infrastructure rather than model-visible instructions.
- **D:** Incorrect for this question. Authentication establishes who is calling. Authorization separately decides what that identity may do to a particular resource. In this case: Store secrets in controlled execution infrastructure rather than model-visible instructions.

### Question 42 — C

Answer: Reference runtime environment variables instead of committing tokens. Use approved environment or secret references and keep literal credentials out of Git. Environment expansion can keep literal secrets out of project files. Supply credentials through an approved secret path and protect logs as well. Local study-map skill 7.4 (Identity, Secrets, and Key Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. Plugins can change tools and workflow behavior. Track provenance, versions, compatibility, and permissions rather than install unreviewed code merely because a model suggests it. In this case: Use approved environment or secret references and keep literal credentials out of Git.
- **B:** Incorrect for this question. Claude Code settings configure supported behavior, permissions, hooks, and plugins. Shared .claude/settings.json, user, local, and managed scopes have distinct reach. In this case: Use approved environment or secret references and keep literal credentials out of Git.
- **C:** Correct. Environment expansion can keep literal secrets out of project files. Supply credentials through an approved secret path and protect logs as well. In this case: Use approved environment or secret references and keep literal credentials out of Git.
- **D:** Incorrect for this question. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: Use approved environment or secret references and keep literal credentials out of Git.

### Question 43 — B

Answer: Revoke exposed credentials and investigate their use. Revoke or rotate exposed credentials and investigate their use and retained copies. Secret exposure requires containment and appropriate incident investigation, rotation, affected-copy handling, and monitoring. Removing one visible copy is not sufficient. Local study-map skill 7.4 (Identity, Secrets, and Key Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. Contain verified harm, investigate affected systems and data, recover safely, and communicate through accountable owners. Observation alone is not containment. In this case: Revoke or rotate exposed credentials and investigate their use and retained copies.
- **B:** Correct. Secret exposure requires containment and appropriate incident investigation, rotation, affected-copy handling, and monitoring. Removing one visible copy is not sufficient. In this case: Revoke or rotate exposed credentials and investigate their use and retained copies.
- **C:** Incorrect for this question. Audit records support attribution and reconstruction of consequential actions. Limit access, sensitive content, and retention; they do not themselves block an effect. In this case: Revoke or rotate exposed credentials and investigate their use and retained copies.
- **D:** Incorrect for this question. Keep credentials out of prompts, repositories, generated output, and unprotected logs. Supply narrowly scoped credentials through approved runtime secret mechanisms. In this case: Revoke or rotate exposed credentials and investigate their use and retained copies.

### Question 44 — D

Answer: Use distinct least-privilege workload identities. Separate least-privilege workload identities improve isolation and attribution. Separate workload identities constrain unnecessary shared authority and improve attribution. Verify granted permissions and credential handling for each operational role. Local study-map skill 7.4 (Identity, Secrets, and Key Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Separate least-privilege workload identities improve isolation and attribution.
- **B:** Incorrect for this question. Permission must be enforced in trusted code using current resource and business state. A valid login, JSON schema, or model proposal alone does not grant authority. In this case: Separate least-privilege workload identities improve isolation and attribution.
- **C:** Incorrect for this question. Authentication establishes who is calling. Authorization separately decides what that identity may do to a particular resource. In this case: Separate least-privilege workload identities improve isolation and attribution.
- **D:** Correct. Separate workload identities constrain unnecessary shared authority and improve attribution. Verify granted permissions and credential handling for each operational role. In this case: Separate least-privilege workload identities improve isolation and attribution.

### Question 45 — B

Answer: Authenticate the calling identity. Authentication verifies the caller's identity before specific permission decisions. Authentication establishes who is calling. Authorization separately decides what that identity may do to a particular resource. Local study-map skill 7.4 (Identity, Secrets, and Key Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. Permission must be enforced in trusted code using current resource and business state. A valid login, JSON schema, or model proposal alone does not grant authority. In this case: Authentication verifies the caller's identity before specific permission decisions.
- **B:** Correct. Authentication establishes who is calling. Authorization separately decides what that identity may do to a particular resource. In this case: Authentication verifies the caller's identity before specific permission decisions.
- **C:** Incorrect for this question. Data access must be authorized externally. Retrieved content being internal or relevant does not justify showing it to every user. In this case: Authentication verifies the caller's identity before specific permission decisions.
- **D:** Incorrect for this question. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Authentication verifies the caller's identity before specific permission decisions.

### Question 46 — C

Answer: Authorize the current identity for the actual target and action. Trusted authorization must enforce resource and action permissions even after login. Permission must be enforced in trusted code using current resource and business state. A valid login, JSON schema, or model proposal alone does not grant authority. Local study-map skill 7.4 (Identity, Secrets, and Key Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. Authentication establishes who is calling. Authorization separately decides what that identity may do to a particular resource. In this case: Trusted authorization must enforce resource and action permissions even after login.
- **B:** Incorrect for this question. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Trusted authorization must enforce resource and action permissions even after login.
- **C:** Correct. Permission must be enforced in trusted code using current resource and business state. A valid login, JSON schema, or model proposal alone does not grant authority. In this case: Trusted authorization must enforce resource and action permissions even after login.
- **D:** Incorrect for this question. Data access must be authorized externally. Retrieved content being internal or relevant does not justify showing it to every user. In this case: Trusted authorization must enforce resource and action permissions even after login.

### Question 47 — C

Answer: Manage credentials in protected execution infrastructure. Secrets must remain protected in telemetry and errors, not merely repositories. Keep credentials out of prompts, repositories, generated output, and unprotected logs. Supply narrowly scoped credentials through approved runtime secret mechanisms. Local study-map skill 7.4 (Identity, Secrets, and Key Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: Secrets must remain protected in telemetry and errors, not merely repositories.
- **B:** Incorrect for this question. Environment expansion can keep literal secrets out of project files. Supply credentials through an approved secret path and protect logs as well. In this case: Secrets must remain protected in telemetry and errors, not merely repositories.
- **C:** Correct. Keep credentials out of prompts, repositories, generated output, and unprotected logs. Supply narrowly scoped credentials through approved runtime secret mechanisms. In this case: Secrets must remain protected in telemetry and errors, not merely repositories.
- **D:** Incorrect for this question. Audit records support attribution and reconstruction of consequential actions. Limit access, sensitive content, and retention; they do not themselves block an effect. In this case: Secrets must remain protected in telemetry and errors, not merely repositories.

### Question 48 — B

Answer: Keep protected action and identity audit records. Protected action and identity records support attribution without unbounded sensitive logging. Audit records support attribution and reconstruction of consequential actions. Limit access, sensitive content, and retention; they do not themselves block an effect. Local study-map skill 7.4 (Identity, Secrets, and Key Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. Link a user task to provider requests, worker runs, and actions without using sensitive content as an identifier. Protect telemetry access and retention. In this case: Protected action and identity records support attribution without unbounded sensitive logging.
- **B:** Correct. Audit records support attribution and reconstruction of consequential actions. Limit access, sensitive content, and retention; they do not themselves block an effect. In this case: Protected action and identity records support attribution without unbounded sensitive logging.
- **C:** Incorrect for this question. Correlate the actual request, model response, tool execution, retries, and validation results. Diagnose the first failing boundary rather than infer cause from the final prose. In this case: Protected action and identity records support attribution without unbounded sensitive logging.
- **D:** Incorrect for this question. Observe deployed latency, failures, drift, and task outcomes with accountable response thresholds. Monitoring differs from an offline evaluation or a single diagnostic trace. In this case: Protected action and identity records support attribution without unbounded sensitive logging.

### Question 49 — B

Answer: Use distinct least-privilege workload identities. Distinct least-privilege identities avoid granting unnecessary inherited authority. Separate workload identities constrain unnecessary shared authority and improve attribution. Verify granted permissions and credential handling for each operational role. Local study-map skill 7.4 (Identity, Secrets, and Key Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. Authentication establishes who is calling. Authorization separately decides what that identity may do to a particular resource. In this case: Distinct least-privilege identities avoid granting unnecessary inherited authority.
- **B:** Correct. Separate workload identities constrain unnecessary shared authority and improve attribution. Verify granted permissions and credential handling for each operational role. In this case: Distinct least-privilege identities avoid granting unnecessary inherited authority.
- **C:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Distinct least-privilege identities avoid granting unnecessary inherited authority.
- **D:** Incorrect for this question. Permission must be enforced in trusted code using current resource and business state. A valid login, JSON schema, or model proposal alone does not grant authority. In this case: Distinct least-privilege identities avoid granting unnecessary inherited authority.

### Question 50 — D

Answer: Revoke exposed credentials and investigate their use. Credential containment should be accompanied by appropriate investigation and recovery handling. Secret exposure requires containment and appropriate incident investigation, rotation, affected-copy handling, and monitoring. Removing one visible copy is not sufficient. Local study-map skill 7.4 (Identity, Secrets, and Key Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/security

- **A:** Incorrect for this question. Contain verified harm, investigate affected systems and data, recover safely, and communicate through accountable owners. Observation alone is not containment. In this case: Credential containment should be accompanied by appropriate investigation and recovery handling.
- **B:** Incorrect for this question. Audit records support attribution and reconstruction of consequential actions. Limit access, sensitive content, and retention; they do not themselves block an effect. In this case: Credential containment should be accompanied by appropriate investigation and recovery handling.
- **C:** Incorrect for this question. Keep credentials out of prompts, repositories, generated output, and unprotected logs. Supply narrowly scoped credentials through approved runtime secret mechanisms. In this case: Credential containment should be accompanied by appropriate investigation and recovery handling.
- **D:** Correct. Secret exposure requires containment and appropriate incident investigation, rotation, affected-copy handling, and monitoring. Removing one visible copy is not sufficient. In this case: Credential containment should be accompanied by appropriate investigation and recovery handling.

### Question 51 — C

Answer: Put shared project standards in versioned CLAUDE.md. Versioned project instructions distribute standards rather than depend on personal files. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. Local study-map skill 3.1 (Claude Code Operation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/settings

- **A:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: Versioned project instructions distribute standards rather than depend on personal files.
- **B:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: Versioned project instructions distribute standards rather than depend on personal files.
- **C:** Correct. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Versioned project instructions distribute standards rather than depend on personal files.
- **D:** Incorrect for this question. Local instructions fit conventions tied to a particular subtree. Cross-directory filename patterns may be better served by path-scoped rules. In this case: Versioned project instructions distribute standards rather than depend on personal files.

### Question 52 — A

Answer: Put personal cross-project preferences in ~/.claude/CLAUDE.md. User-level instructions apply to that user's workflows rather than every teammate. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. Local study-map skill 3.1 (Claude Code Operation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/settings

- **A:** Correct. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: User-level instructions apply to that user's workflows rather than every teammate.
- **B:** Incorrect for this question. Local instructions fit conventions tied to a particular subtree. Cross-directory filename patterns may be better served by path-scoped rules. In this case: User-level instructions apply to that user's workflows rather than every teammate.
- **C:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: User-level instructions apply to that user's workflows rather than every teammate.
- **D:** Incorrect for this question. Topic-specific rule files reduce one oversized instruction document. Add path scoping when a rule is only relevant to selected files. In this case: User-level instructions apply to that user's workflows rather than every teammate.

### Question 53 — A

Answer: Scope a rule with YAML paths glob patterns. Path glob rules can follow file roles across different directory boundaries. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. Local study-map skill 3.1 (Claude Code Operation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/settings

- **A:** Correct. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. In this case: Path glob rules can follow file roles across different directory boundaries.
- **B:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Path glob rules can follow file roles across different directory boundaries.
- **C:** Incorrect for this question. Local instructions fit conventions tied to a particular subtree. Cross-directory filename patterns may be better served by path-scoped rules. In this case: Path glob rules can follow file roles across different directory boundaries.
- **D:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: Path glob rules can follow file roles across different directory boundaries.

### Question 54 — B

Answer: Put an on-demand workflow in a project skill. An on-demand skill is more suitable than universal instruction text for a specialized workflow. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. Local study-map skill 3.1 (Claude Code Operation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/settings

- **A:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: An on-demand skill is more suitable than universal instruction text for a specialized workflow.
- **B:** Correct. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: An on-demand skill is more suitable than universal instruction text for a specialized workflow.
- **C:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: An on-demand skill is more suitable than universal instruction text for a specialized workflow.
- **D:** Incorrect for this question. Topic-specific rule files reduce one oversized instruction document. Add path scoping when a rule is only relevant to selected files. In this case: An on-demand skill is more suitable than universal instruction text for a specialized workflow.

### Question 55 — D

Answer: Use a project-scoped custom slash command. Project-scoped command files distribute invocation workflows to contributors. The guide describes .claude/commands/ for shared invocable commands. User-scoped commands are personal; feature details depend on Claude Code version. Local study-map skill 3.1 (Claude Code Operation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/settings

- **A:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Project-scoped command files distribute invocation workflows to contributors.
- **B:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Project-scoped command files distribute invocation workflows to contributors.
- **C:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: Project-scoped command files distribute invocation workflows to contributors.
- **D:** Correct. The guide describes .claude/commands/ for shared invocable commands. User-scoped commands are personal; feature details depend on Claude Code version. In this case: Project-scoped command files distribute invocation workflows to contributors.

### Question 56 — D

Answer: Use the appropriate settings.json scope for behavioral configuration. Settings configure runtime behavior under appropriate scope, unlike prose guidance alone. Claude Code settings configure supported behavior, permissions, hooks, and plugins. Shared .claude/settings.json, user, local, and managed scopes have distinct reach. Local study-map skill 3.1 (Claude Code Operation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/settings

- **A:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: Settings configure runtime behavior under appropriate scope, unlike prose guidance alone.
- **B:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Settings configure runtime behavior under appropriate scope, unlike prose guidance alone.
- **C:** Incorrect for this question. Topic-specific rule files reduce one oversized instruction document. Add path scoping when a rule is only relevant to selected files. In this case: Settings configure runtime behavior under appropriate scope, unlike prose guidance alone.
- **D:** Correct. Claude Code settings configure supported behavior, permissions, hooks, and plugins. Shared .claude/settings.json, user, local, and managed scopes have distinct reach. In this case: Settings configure runtime behavior under appropriate scope, unlike prose guidance alone.

### Question 57 — B

Answer: Run Claude Code in non-interactive print mode. Non-interactive print mode fits automation when credentials and permissions are configured. The -p or --print mode is intended for non-interactive runs. Authentication, permissions, termination, and artifact capture still require CI configuration. Local study-map skill 3.1 (Claude Code Operation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/settings

- **A:** Incorrect for this question. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. In this case: Non-interactive print mode fits automation when credentials and permissions are configured.
- **B:** Correct. The -p or --print mode is intended for non-interactive runs. Authentication, permissions, termination, and artifact capture still require CI configuration. In this case: Non-interactive print mode fits automation when credentials and permissions are configured.
- **C:** Incorrect for this question. The guide describes .claude/commands/ for shared invocable commands. User-scoped commands are personal; feature details depend on Claude Code version. In this case: Non-interactive print mode fits automation when credentials and permissions are configured.
- **D:** Incorrect for this question. The guide describes --output-format json and --json-schema for machine-parseable CI results. Verify the installed version and check execution status as well as payload. In this case: Non-interactive print mode fits automation when credentials and permissions are configured.

### Question 58 — C

Answer: Use supported JSON output and schema CLI options. Use supported JSON and schema options and inspect execution status as well. The guide describes --output-format json and --json-schema for machine-parseable CI results. Verify the installed version and check execution status as well as payload. Local study-map skill 3.1 (Claude Code Operation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/settings

- **A:** Incorrect for this question. Comparing the current diff with prior findings can reduce duplicate review comments. Preserve still-valid findings rather than simply suppressing all repeats. In this case: Use supported JSON and schema options and inspect execution status as well.
- **B:** Incorrect for this question. The -p or --print mode is intended for non-interactive runs. Authentication, permissions, termination, and artifact capture still require CI configuration. In this case: Use supported JSON and schema options and inspect execution status as well.
- **C:** Correct. The guide describes --output-format json and --json-schema for machine-parseable CI results. Verify the installed version and check execution status as well as payload. In this case: Use supported JSON and schema options and inspect execution status as well.
- **D:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Use supported JSON and schema options and inspect execution status as well.

### Question 59 — D

Answer: Resume the identified session when its context remains valid. Resume the intended identified conversation rather than whichever session is most recent. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. Local study-map skill 3.1 (Claude Code Operation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/settings

- **A:** Incorrect for this question. Forking supports divergent explorations without overwriting the original conversation. It does not itself isolate external files or undo side effects. In this case: Resume the intended identified conversation rather than whichever session is most recent.
- **B:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Resume the intended identified conversation rather than whichever session is most recent.
- **C:** Incorrect for this question. A new context can avoid stale tool results when assumptions changed widely. Preserve verified facts, relevant constraints, and pointers rather than import all obsolete history. In this case: Resume the intended identified conversation rather than whichever session is most recent.
- **D:** Correct. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Resume the intended identified conversation rather than whichever session is most recent.

### Question 60 — C

Answer: Inspect which instruction files are actually loaded. Verify actual instruction loading and scope rather than file existence alone. The guide mentions /memory; current documentation also describes /context. Use the available inspection mechanism to diagnose scope and loading, not just the presence of a file. Local study-map skill 3.1 (Claude Code Operation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/settings

- **A:** Incorrect for this question. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. In this case: Verify actual instruction loading and scope rather than file existence alone.
- **B:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: Verify actual instruction loading and scope rather than file existence alone.
- **C:** Correct. The guide mentions /memory; current documentation also describes /context. Use the available inspection mechanism to diagnose scope and loading, not just the presence of a file. In this case: Verify actual instruction loading and scope rather than file existence alone.
- **D:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Verify actual instruction loading and scope rather than file existence alone.

### Question 61 — C

Answer: Use context: fork for isolated skill execution. Isolated skill execution can contain conversational clutter while returning useful conclusions. Where supported, an isolated skill context contains intermediate exploration. It does not automatically provide filesystem isolation or remove tool-permission obligations. Local study-map skill 3.1 (Claude Code Operation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/settings

- **A:** Incorrect for this question. Use supported workflow configuration and actual runtime permission controls. A skill allowed-tools declaration can affect pre-approval; it must not be assumed to create a hard sandbox or deny every other tool by itself. In this case: Isolated skill execution can contain conversational clutter while returning useful conclusions.
- **B:** Incorrect for this question. A personal variant can customize workflow without changing the shared skill for teammates. Distinct naming avoids accidental shadowing or confusion. In this case: Isolated skill execution can contain conversational clutter while returning useful conclusions.
- **C:** Correct. Where supported, an isolated skill context contains intermediate exploration. It does not automatically provide filesystem isolation or remove tool-permission obligations. In this case: Isolated skill execution can contain conversational clutter while returning useful conclusions.
- **D:** Incorrect for this question. Argument hints help users supply needed parameters. They do not replace actual argument validation or supply missing business facts. In this case: Isolated skill execution can contain conversational clutter while returning useful conclusions.

### Question 62 — B

Answer: Configure a least-privilege skill workflow and verify effective permissions. Restrict supported effective tools and verify actual permissions rather than rely on prose alone. Use supported workflow configuration and actual runtime permission controls. A skill allowed-tools declaration can affect pre-approval; it must not be assumed to create a hard sandbox or deny every other tool by itself. Local study-map skill 3.1 (Claude Code Operation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/settings

- **A:** Incorrect for this question. A personal variant can customize workflow without changing the shared skill for teammates. Distinct naming avoids accidental shadowing or confusion. In this case: Restrict supported effective tools and verify actual permissions rather than rely on prose alone.
- **B:** Correct. Use supported workflow configuration and actual runtime permission controls. A skill allowed-tools declaration can affect pre-approval; it must not be assumed to create a hard sandbox or deny every other tool by itself. In this case: Restrict supported effective tools and verify actual permissions rather than rely on prose alone.
- **C:** Incorrect for this question. Where supported, an isolated skill context contains intermediate exploration. It does not automatically provide filesystem isolation or remove tool-permission obligations. In this case: Restrict supported effective tools and verify actual permissions rather than rely on prose alone.
- **D:** Incorrect for this question. Argument hints help users supply needed parameters. They do not replace actual argument validation or supply missing business facts. In this case: Restrict supported effective tools and verify actual permissions rather than rely on prose alone.

### Question 63 — B

Answer: Provide argument-hint for invocation guidance. An argument hint communicates expected input but does not validate its correctness. Argument hints help users supply needed parameters. They do not replace actual argument validation or supply missing business facts. Local study-map skill 3.1 (Claude Code Operation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/settings

- **A:** Incorrect for this question. Use supported workflow configuration and actual runtime permission controls. A skill allowed-tools declaration can affect pre-approval; it must not be assumed to create a hard sandbox or deny every other tool by itself. In this case: An argument hint communicates expected input but does not validate its correctness.
- **B:** Correct. Argument hints help users supply needed parameters. They do not replace actual argument validation or supply missing business facts. In this case: An argument hint communicates expected input but does not validate its correctness.
- **C:** Incorrect for this question. Where supported, an isolated skill context contains intermediate exploration. It does not automatically provide filesystem isolation or remove tool-permission obligations. In this case: An argument hint communicates expected input but does not validate its correctness.
- **D:** Incorrect for this question. A personal variant can customize workflow without changing the shared skill for teammates. Distinct naming avoids accidental shadowing or confusion. In this case: An argument hint communicates expected input but does not validate its correctness.

### Question 64 — B

Answer: Create a differently named personal skill variant. Use a differently named personal variant rather than modify or ambiguously shadow shared behavior. A personal variant can customize workflow without changing the shared skill for teammates. Distinct naming avoids accidental shadowing or confusion. Local study-map skill 3.1 (Claude Code Operation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/settings

- **A:** Incorrect for this question. The guide describes .claude/commands/ for shared invocable commands. User-scoped commands are personal; feature details depend on Claude Code version. In this case: Use a differently named personal variant rather than modify or ambiguously shadow shared behavior.
- **B:** Correct. A personal variant can customize workflow without changing the shared skill for teammates. Distinct naming avoids accidental shadowing or confusion. In this case: Use a differently named personal variant rather than modify or ambiguously shadow shared behavior.
- **C:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: Use a differently named personal variant rather than modify or ambiguously shadow shared behavior.
- **D:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Use a differently named personal variant rather than modify or ambiguously shadow shared behavior.

### Question 65 — D

Answer: Use plan mode to investigate and compare approaches. Planning supports investigation and comparison before committing to a complex implementation. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. Local study-map skill 3.1 (Claude Code Operation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/settings

- **A:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Planning supports investigation and comparison before committing to a complex implementation.
- **B:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Planning supports investigation and comparison before committing to a complex implementation.
- **C:** Incorrect for this question. A narrow fix with known requirements may not need a long planning phase. Tests and review still apply. In this case: Planning supports investigation and comparison before committing to a complex implementation.
- **D:** Correct. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. In this case: Planning supports investigation and comparison before committing to a complex implementation.

### Question 66 — A

Answer: Implement a small well-understood change directly. A well-understood small change may proceed directly with tests and review. A narrow fix with known requirements may not need a long planning phase. Tests and review still apply. Local study-map skill 3.1 (Claude Code Operation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/settings

- **A:** Correct. A narrow fix with known requirements may not need a long planning phase. Tests and review still apply. In this case: A well-understood small change may proceed directly with tests and review.
- **B:** Incorrect for this question. An interview-style clarification step surfaces unknown assumptions and constraints. Use it when uncertainty materially affects design. In this case: A well-understood small change may proceed directly with tests and review.
- **C:** Incorrect for this question. Discovery can be isolated so verbose file output does not overwhelm the main conversation. Return useful findings and source pointers. In this case: A well-understood small change may proceed directly with tests and review.
- **D:** Incorrect for this question. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. In this case: A well-understood small change may proceed directly with tests and review.

### Question 67 — A

Answer: Delegate focused exploration to a read-oriented subagent. A focused exploration subagent can return concise findings without all intermediate output. Discovery can be isolated so verbose file output does not overwhelm the main conversation. Return useful findings and source pointers. Local study-map skill 3.1 (Claude Code Operation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/settings

- **A:** Correct. Discovery can be isolated so verbose file output does not overwhelm the main conversation. Return useful findings and source pointers. In this case: A focused exploration subagent can return concise findings without all intermediate output.
- **B:** Incorrect for this question. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. In this case: A focused exploration subagent can return concise findings without all intermediate output.
- **C:** Incorrect for this question. A narrow fix with known requirements may not need a long planning phase. Tests and review still apply. In this case: A focused exploration subagent can return concise findings without all intermediate output.
- **D:** Incorrect for this question. An interview-style clarification step surfaces unknown assumptions and constraints. Use it when uncertainty materially affects design. In this case: A focused exploration subagent can return concise findings without all intermediate output.

### Question 68 — A

Answer: Use @imports to keep instruction content modular. Reference relevant maintained guidance through imports instead of copying it repeatedly. Imports reference relevant supporting instruction files. Their actual loading and accessibility should be verified rather than assumed. Local study-map skill 3.1 (Claude Code Operation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/settings

- **A:** Correct. Imports reference relevant supporting instruction files. Their actual loading and accessibility should be verified rather than assumed. In this case: Reference relevant maintained guidance through imports instead of copying it repeatedly.
- **B:** Incorrect for this question. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. In this case: Reference relevant maintained guidance through imports instead of copying it repeatedly.
- **C:** Incorrect for this question. Topic-specific rule files reduce one oversized instruction document. Add path scoping when a rule is only relevant to selected files. In this case: Reference relevant maintained guidance through imports instead of copying it repeatedly.
- **D:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: Reference relevant maintained guidance through imports instead of copying it repeatedly.

### Question 69 — C

Answer: Provide existing tests and approved fixtures. Provide existing tests and approved fixtures to anchor generation in real conventions. Relevant test context helps generation avoid duplicates and use valid repository conventions. Do not invent unavailable helper functions or external test data. Local study-map skill 3.1 (Claude Code Operation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/settings

- **A:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Provide existing tests and approved fixtures to anchor generation in real conventions.
- **B:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Provide existing tests and approved fixtures to anchor generation in real conventions.
- **C:** Correct. Relevant test context helps generation avoid duplicates and use valid repository conventions. Do not invent unavailable helper functions or external test data. In this case: Provide existing tests and approved fixtures to anchor generation in real conventions.
- **D:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Provide existing tests and approved fixtures to anchor generation in real conventions.

### Question 70 — D

Answer: Pass prior findings and request only new or unresolved issues. Include prior findings and current code to distinguish new or still-unresolved issues. Comparing the current diff with prior findings can reduce duplicate review comments. Preserve still-valid findings rather than simply suppressing all repeats. Local study-map skill 3.1 (Claude Code Operation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/settings

- **A:** Incorrect for this question. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: Include prior findings and current code to distinguish new or still-unresolved issues.
- **B:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Include prior findings and current code to distinguish new or still-unresolved issues.
- **C:** Incorrect for this question. Independent review reduces anchoring on the original solution. It still needs the specification, relevant code, and evidence; independence does not guarantee correctness. In this case: Include prior findings and current code to distinguish new or still-unresolved issues.
- **D:** Correct. Comparing the current diff with prior findings can reduce duplicate review comments. Preserve still-valid findings rather than simply suppressing all repeats. In this case: Include prior findings and current code to distinguish new or still-unresolved issues.

### Question 71 — D

Answer: Version and review plugin dependencies and permissions. Review and record plugin versions, compatibility, and permissions alongside other dependencies. Plugins can change tools and workflow behavior. Track provenance, versions, compatibility, and permissions rather than install unreviewed code merely because a model suggests it. Local study-map skill 3.1 (Claude Code Operation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/settings

- **A:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Review and record plugin versions, compatibility, and permissions alongside other dependencies.
- **B:** Incorrect for this question. Claude Code settings configure supported behavior, permissions, hooks, and plugins. Shared .claude/settings.json, user, local, and managed scopes have distinct reach. In this case: Review and record plugin versions, compatibility, and permissions alongside other dependencies.
- **C:** Incorrect for this question. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: Review and record plugin versions, compatibility, and permissions alongside other dependencies.
- **D:** Correct. Plugins can change tools and workflow behavior. Track provenance, versions, compatibility, and permissions rather than install unreviewed code merely because a model suggests it. In this case: Review and record plugin versions, compatibility, and permissions alongside other dependencies.

### Question 72 — C

Answer: Inspect which instruction files are actually loaded. Inspect effective scoped configuration rather than assume one file governs all users and environments. The guide mentions /memory; current documentation also describes /context. Use the available inspection mechanism to diagnose scope and loading, not just the presence of a file. Local study-map skill 3.1 (Claude Code Operation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/settings

- **A:** Incorrect for this question. Claude Code settings configure supported behavior, permissions, hooks, and plugins. Shared .claude/settings.json, user, local, and managed scopes have distinct reach. In this case: Inspect effective scoped configuration rather than assume one file governs all users and environments.
- **B:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Inspect effective scoped configuration rather than assume one file governs all users and environments.
- **C:** Correct. The guide mentions /memory; current documentation also describes /context. Use the available inspection mechanism to diagnose scope and loading, not just the presence of a file. In this case: Inspect effective scoped configuration rather than assume one file governs all users and environments.
- **D:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: Inspect effective scoped configuration rather than assume one file governs all users and environments.

### Question 73 — D

Answer: Put shared project standards in versioned CLAUDE.md. Project instruction files provide shared guidance while settings serve a different configuration role. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. Local study-map skill 3.1 (Claude Code Operation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/settings

- **A:** Incorrect for this question. Topic-specific rule files reduce one oversized instruction document. Add path scoping when a rule is only relevant to selected files. In this case: Project instruction files provide shared guidance while settings serve a different configuration role.
- **B:** Incorrect for this question. Claude Code settings configure supported behavior, permissions, hooks, and plugins. Shared .claude/settings.json, user, local, and managed scopes have distinct reach. In this case: Project instruction files provide shared guidance while settings serve a different configuration role.
- **C:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: Project instruction files provide shared guidance while settings serve a different configuration role.
- **D:** Correct. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Project instruction files provide shared guidance while settings serve a different configuration role.

### Question 74 — D

Answer: Consume the Messages stream as server-sent events. Standard Messages streaming uses server-sent events under its documented API contract. The documented streaming interface emits SSE events over HTTP. It is not inherently a WebSocket connection or one valid JSON object per arbitrary network chunk. Local study-map skill 3.1 (Claude Code Operation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/settings

- **A:** Incorrect for this question. The guide describes --output-format json and --json-schema for machine-parseable CI results. Verify the installed version and check execution status as well as payload. In this case: Standard Messages streaming uses server-sent events under its documented API contract.
- **B:** Incorrect for this question. WebSockets can fit bidirectional application communication, but the documented standard Messages streaming interface is SSE. Do not confuse a transport choice with model capability. In this case: Standard Messages streaming uses server-sent events under its documented API contract.
- **C:** Incorrect for this question. The -p or --print mode is intended for non-interactive runs. Authentication, permissions, termination, and artifact capture still require CI configuration. In this case: Standard Messages streaming uses server-sent events under its documented API contract.
- **D:** Correct. The documented streaming interface emits SSE events over HTTP. It is not inherently a WebSocket connection or one valid JSON object per arbitrary network chunk. In this case: Standard Messages streaming uses server-sent events under its documented API contract.

### Question 75 — A

Answer: Enforce prerequisites in trusted execution code. Execution controls must enforce mandatory boundaries beyond model-readable instructions. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. Local study-map skill 3.1 (Claude Code Operation), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/settings

- **A:** Correct. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Execution controls must enforce mandatory boundaries beyond model-readable instructions.
- **B:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Execution controls must enforce mandatory boundaries beyond model-readable instructions.
- **C:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: Execution controls must enforce mandatory boundaries beyond model-readable instructions.
- **D:** Incorrect for this question. Topic-specific rule files reduce one oversized instruction document. Add path scoping when a rule is only relevant to selected files. In this case: Execution controls must enforce mandatory boundaries beyond model-readable instructions.

### Question 76 — A

Answer: Inspect a redacted end-to-end request and tool trace. A redacted end-to-end trace can show where requests, outputs, tools, or parsing first diverge. Correlate the actual request, model response, tool execution, retries, and validation results. Diagnose the first failing boundary rather than infer cause from the final prose. Local study-map skill 4.1 (Debugging and Error Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/streaming

- **A:** Correct. Correlate the actual request, model response, tool execution, retries, and validation results. Diagnose the first failing boundary rather than infer cause from the final prose. In this case: A redacted end-to-end trace can show where requests, outputs, tools, or parsing first diverge.
- **B:** Incorrect for this question. Inject timeouts, malformed responses, and provider failures without live side effects. Combine with contract and representative integration tests rather than infer complete correctness from mocks. In this case: A redacted end-to-end trace can show where requests, outputs, tools, or parsing first diverge.
- **C:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: A redacted end-to-end trace can show where requests, outputs, tools, or parsing first diverge.
- **D:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: A redacted end-to-end trace can show where requests, outputs, tools, or parsing first diverge.

### Question 77 — C

Answer: Isolate model-output defects from integration defects. The integration layer caused the defect rather than the model's response. Check whether correct raw output was lost or changed by serialization, parsing, routing, or persistence. Not every visible error is fixed by changing the prompt. Local study-map skill 4.1 (Debugging and Error Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/streaming

- **A:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: The integration layer caused the defect rather than the model's response.
- **B:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: The integration layer caused the defect rather than the model's response.
- **C:** Correct. Check whether correct raw output was lost or changed by serialization, parsing, routing, or persistence. Not every visible error is fixed by changing the prompt. In this case: The integration layer caused the defect rather than the model's response.
- **D:** Incorrect for this question. Correlate the actual request, model response, tool execution, retries, and validation results. Diagnose the first failing boundary rather than infer cause from the final prose. In this case: The integration layer caused the defect rather than the model's response.

### Question 78 — D

Answer: Correct invalid arguments before retrying. Correct invalid inputs instead of repeat the same request without modification. A validation failure points to an input defect. Repeating identical invalid arguments is not recovery. Local study-map skill 4.1 (Debugging and Error Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/streaming

- **A:** Incorrect for this question. A policy rejection is not normally fixed by repeating the same operation. Communicate the reason and legitimate next steps without evasion. In this case: Correct invalid inputs instead of repeat the same request without modification.
- **B:** Incorrect for this question. Permission denial does not justify trying alternate credentials or leaking restricted content. Recover only through explicitly authorized mechanisms. In this case: Correct invalid inputs instead of repeat the same request without modification.
- **C:** Incorrect for this question. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: Correct invalid inputs instead of repeat the same request without modification.
- **D:** Correct. A validation failure points to an input defect. Repeating identical invalid arguments is not recovery. In this case: Correct invalid inputs instead of repeat the same request without modification.

### Question 79 — D

Answer: Retry a transient failure with bounded backoff. Use bounded retry appropriate to the service and safety of the operation. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. Local study-map skill 4.1 (Debugging and Error Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/streaming

- **A:** Incorrect for this question. A policy rejection is not normally fixed by repeating the same operation. Communicate the reason and legitimate next steps without evasion. In this case: Use bounded retry appropriate to the service and safety of the operation.
- **B:** Incorrect for this question. Permission denial does not justify trying alternate credentials or leaking restricted content. Recover only through explicitly authorized mechanisms. In this case: Use bounded retry appropriate to the service and safety of the operation.
- **C:** Incorrect for this question. A validation failure points to an input defect. Repeating identical invalid arguments is not recovery. In this case: Use bounded retry appropriate to the service and safety of the operation.
- **D:** Correct. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: Use bounded retry appropriate to the service and safety of the operation.

### Question 80 — C

Answer: Stop the unauthorized operation and use an approved access path. Use only an approved access path rather than retry with another person's credential. Permission denial does not justify trying alternate credentials or leaking restricted content. Recover only through explicitly authorized mechanisms. Local study-map skill 4.1 (Debugging and Error Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/streaming

- **A:** Incorrect for this question. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. In this case: Use only an approved access path rather than retry with another person's credential.
- **B:** Incorrect for this question. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: Use only an approved access path rather than retry with another person's credential.
- **C:** Correct. Permission denial does not justify trying alternate credentials or leaking restricted content. Recover only through explicitly authorized mechanisms. In this case: Use only an approved access path rather than retry with another person's credential.
- **D:** Incorrect for this question. A validation failure points to an input defect. Repeating identical invalid arguments is not recovery. In this case: Use only an approved access path rather than retry with another person's credential.

### Question 81 — B

Answer: Explain the non-retryable business-rule outcome. Treat the policy outcome as a business rejection, not a transient service outage. A policy rejection is not normally fixed by repeating the same operation. Communicate the reason and legitimate next steps without evasion. Local study-map skill 4.1 (Debugging and Error Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/streaming

- **A:** Incorrect for this question. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. In this case: Treat the policy outcome as a business rejection, not a transient service outage.
- **B:** Correct. A policy rejection is not normally fixed by repeating the same operation. Communicate the reason and legitimate next steps without evasion. In this case: Treat the policy outcome as a business rejection, not a transient service outage.
- **C:** Incorrect for this question. A validation failure points to an input defect. Repeating identical invalid arguments is not recovery. In this case: Treat the policy outcome as a business rejection, not a transient service outage.
- **D:** Incorrect for this question. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: Treat the policy outcome as a business rejection, not a transient service outage.

### Question 82 — A

Answer: Represent a successful query with no matches explicitly. Successful emptiness does not mean the service was inaccessible. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. Local study-map skill 4.1 (Debugging and Error Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/streaming

- **A:** Correct. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. In this case: Successful emptiness does not mean the service was inaccessible.
- **B:** Incorrect for this question. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: Successful emptiness does not mean the service was inaccessible.
- **C:** Incorrect for this question. An error contract should identify failure class, recoverability, and useful context. MCP isError marks an execution failure; it should not disguise a valid empty result. In this case: Successful emptiness does not mean the service was inaccessible.
- **D:** Incorrect for this question. Permission denial does not justify trying alternate credentials or leaking restricted content. Recover only through explicitly authorized mechanisms. In this case: Successful emptiness does not mean the service was inaccessible.

### Question 83 — A

Answer: Handle errors after streaming has already begun. Initial HTTP success does not prove the streamed message completed. A successful HTTP setup does not prove stream completion. Detect error events or interrupted streams, preserve status, and avoid publishing partial results as final success. Local study-map skill 4.1 (Debugging and Error Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/streaming

- **A:** Correct. A successful HTTP setup does not prove stream completion. Detect error events or interrupted streams, preserve status, and avoid publishing partial results as final success. In this case: Initial HTTP success does not prove the streamed message completed.
- **B:** Incorrect for this question. This indicates ordinary turn completion, not that every business objective or external action succeeded. Application acceptance checks still apply. In this case: Initial HTTP success does not prove the streamed message completed.
- **C:** Incorrect for this question. A max_tokens stop can leave content incomplete. Inspect the response and recover appropriately instead of treating it as normal completion. In this case: Initial HTTP success does not prove the streamed message completed.
- **D:** Incorrect for this question. SDK accumulation helpers can provide the complete message. Inspect termination and errors before treating the resulting object as accepted application output. In this case: Initial HTTP success does not prove the streamed message completed.

### Question 84 — B

Answer: Accumulate deltas by block index before final validation. Assemble content according to protocol boundaries before final structured parsing. Network chunks and content deltas can contain partial strings or JSON. Track event and block boundaries or use SDK helpers before consuming a complete structured value. Local study-map skill 4.1 (Debugging and Error Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/streaming

- **A:** Incorrect for this question. The documented streaming interface emits SSE events over HTTP. It is not inherently a WebSocket connection or one valid JSON object per arbitrary network chunk. In this case: Assemble content according to protocol boundaries before final structured parsing.
- **B:** Correct. Network chunks and content deltas can contain partial strings or JSON. Track event and block boundaries or use SDK helpers before consuming a complete structured value. In this case: Assemble content according to protocol boundaries before final structured parsing.
- **C:** Incorrect for this question. SDK accumulation helpers can provide the complete message. Inspect termination and errors before treating the resulting object as accepted application output. In this case: Assemble content according to protocol boundaries before final structured parsing.
- **D:** Incorrect for this question. A response can contain text, tool use, thinking, or other supported blocks. Do not assume content is one string or that the first block is always displayable text. In this case: Assemble content according to protocol boundaries before final structured parsing.

### Question 85 — A

Answer: Use controlled stubs for repeatable failure-path tests. Controlled stubs can inject failure paths safely and deterministically. Inject timeouts, malformed responses, and provider failures without live side effects. Combine with contract and representative integration tests rather than infer complete correctness from mocks. Local study-map skill 4.1 (Debugging and Error Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/streaming

- **A:** Correct. Inject timeouts, malformed responses, and provider failures without live side effects. Combine with contract and representative integration tests rather than infer complete correctness from mocks. In this case: Controlled stubs can inject failure paths safely and deterministically.
- **B:** Incorrect for this question. Check serialized requests, content blocks, status handling, and representative responses. Mock success alone may not reveal a malformed real request or unsupported provider feature. In this case: Controlled stubs can inject failure paths safely and deterministically.
- **C:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Controlled stubs can inject failure paths safely and deterministically.
- **D:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Controlled stubs can inject failure paths safely and deterministically.

### Question 86 — B

Answer: Propagate correlation identifiers across requests and tools. Correlation identifiers let developers connect the actual operation chain. Link a user task to provider requests, worker runs, and actions without using sensitive content as an identifier. Protect telemetry access and retention. Local study-map skill 4.1 (Debugging and Error Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/streaming

- **A:** Incorrect for this question. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: Correlation identifiers let developers connect the actual operation chain.
- **B:** Correct. Link a user task to provider requests, worker runs, and actions without using sensitive content as an identifier. Protect telemetry access and retention. In this case: Correlation identifiers let developers connect the actual operation chain.
- **C:** Incorrect for this question. Audit records support attribution and reconstruction of consequential actions. Limit access, sensitive content, and retention; they do not themselves block an effect. In this case: Correlation identifiers let developers connect the actual operation chain.
- **D:** Incorrect for this question. Correlate the actual request, model response, tool execution, retries, and validation results. Diagnose the first failing boundary rather than infer cause from the final prose. In this case: Correlation identifiers let developers connect the actual operation chain.

### Question 87 — D

Answer: Test the integration contract at the provider boundary. Validate actual provider request and response contracts rather than only fake payloads. Check serialized requests, content blocks, status handling, and representative responses. Mock success alone may not reveal a malformed real request or unsupported provider feature. Local study-map skill 4.1 (Debugging and Error Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/streaming

- **A:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Validate actual provider request and response contracts rather than only fake payloads.
- **B:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Validate actual provider request and response contracts rather than only fake payloads.
- **C:** Incorrect for this question. Inject timeouts, malformed responses, and provider failures without live side effects. Combine with contract and representative integration tests rather than infer complete correctness from mocks. In this case: Validate actual provider request and response contracts rather than only fake payloads.
- **D:** Correct. Check serialized requests, content blocks, status handling, and representative responses. Mock success alone may not reveal a malformed real request or unsupported provider feature. In this case: Validate actual provider request and response contracts rather than only fake payloads.

### Question 88 — B

Answer: Coordinate retries across SDK and application layers. Coordinate total attempts and elapsed-time budgets across SDK and application behavior. Nested automatic retries can multiply attempts and latency. Set a shared attempt or elapsed-time budget and inspect SDK defaults. Local study-map skill 4.1 (Debugging and Error Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/streaming

- **A:** Incorrect for this question. Limit queued and active work so slow consumers or provider limits do not exhaust memory or connections. Unbounded parallelism is not a capacity plan. In this case: Coordinate total attempts and elapsed-time budgets across SDK and application behavior.
- **B:** Correct. Nested automatic retries can multiply attempts and latency. Set a shared attempt or elapsed-time budget and inspect SDK defaults. In this case: Coordinate total attempts and elapsed-time budgets across SDK and application behavior.
- **C:** Incorrect for this question. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: Coordinate total attempts and elapsed-time budgets across SDK and application behavior.
- **D:** Incorrect for this question. Bound user and dependency waits. A timeout is an uncertain execution outcome for mutations and may require status reconciliation rather than blind retry. In this case: Coordinate total attempts and elapsed-time budgets across SDK and application behavior.

### Question 89 — A

Answer: Set explicit deadlines and classify timeout outcomes. A local deadline does not prove remote failure or rollback. Bound user and dependency waits. A timeout is an uncertain execution outcome for mutations and may require status reconciliation rather than blind retry. Local study-map skill 4.1 (Debugging and Error Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/streaming

- **A:** Correct. Bound user and dependency waits. A timeout is an uncertain execution outcome for mutations and may require status reconciliation rather than blind retry. In this case: A local deadline does not prove remote failure or rollback.
- **B:** Incorrect for this question. Where supported, repeated requests for one operation should resolve to one intended external effect. Generating a new key for each retry defeats duplicate protection. In this case: A local deadline does not prove remote failure or rollback.
- **C:** Incorrect for this question. Separate a generated proposal from an authorized atomic or otherwise well-coordinated business effect. Define conflict handling and rollback or compensation behavior. In this case: A local deadline does not prove remote failure or rollback.
- **D:** Incorrect for this question. Local cancellation limits waiting or computation but does not guarantee the server stopped or a remote side effect was rolled back. In this case: A local deadline does not prove remote failure or rollback.

### Question 90 — D

Answer: Validate extracted values against evidence and business rules. Semantic evidence alignment differs from JSON structural validity. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. Local study-map skill 4.1 (Debugging and Error Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/streaming

- **A:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Semantic evidence alignment differs from JSON structural validity.
- **B:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Semantic evidence alignment differs from JSON structural validity.
- **C:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Semantic evidence alignment differs from JSON structural validity.
- **D:** Correct. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Semantic evidence alignment differs from JSON structural validity.

### Question 91 — A

Answer: Inspect a redacted end-to-end request and tool trace. The serialized integration request must contain the actual intended instructions. Correlate the actual request, model response, tool execution, retries, and validation results. Diagnose the first failing boundary rather than infer cause from the final prose. Local study-map skill 4.1 (Debugging and Error Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/streaming

- **A:** Correct. Correlate the actual request, model response, tool execution, retries, and validation results. Diagnose the first failing boundary rather than infer cause from the final prose. In this case: The serialized integration request must contain the actual intended instructions.
- **B:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: The serialized integration request must contain the actual intended instructions.
- **C:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: The serialized integration request must contain the actual intended instructions.
- **D:** Incorrect for this question. Check whether correct raw output was lost or changed by serialization, parsing, routing, or persistence. Not every visible error is fixed by changing the prompt. In this case: The serialized integration request must contain the actual intended instructions.

### Question 92 — D

Answer: Use a versioned representative held-out evaluation set. Representative held-out cases should reflect actual task variation and important failure modes. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. Local study-map skill 4.1 (Debugging and Error Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/streaming

- **A:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Representative held-out cases should reflect actual task variation and important failure modes.
- **B:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Representative held-out cases should reflect actual task variation and important failure modes.
- **C:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Representative held-out cases should reflect actual task variation and important failure modes.
- **D:** Correct. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Representative held-out cases should reflect actual task variation and important failure modes.

### Question 93 — C

Answer: Pin compatible model, SDK, prompt, and dependency versions. Track actual behavior-relevant versions and deployed artifacts for reproducible diagnosis. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. Local study-map skill 4.1 (Debugging and Error Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/streaming

- **A:** Incorrect for this question. Record revisions of behavioral instructions with evaluation and release history. A model pin does not freeze changing application prompts. In this case: Track actual behavior-relevant versions and deployed artifacts for reproducible diagnosis.
- **B:** Incorrect for this question. Plugins can change tools and workflow behavior. Track provenance, versions, compatibility, and permissions rather than install unreviewed code merely because a model suggests it. In this case: Track actual behavior-relevant versions and deployed artifacts for reproducible diagnosis.
- **C:** Correct. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Track actual behavior-relevant versions and deployed artifacts for reproducible diagnosis.
- **D:** Incorrect for this question. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: Track actual behavior-relevant versions and deployed artifacts for reproducible diagnosis.

### Question 94 — C

Answer: Handle errors after streaming has already begun. Incomplete streaming must not be reported as accepted final output. A successful HTTP setup does not prove stream completion. Detect error events or interrupted streams, preserve status, and avoid publishing partial results as final success. Local study-map skill 4.1 (Debugging and Error Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/streaming

- **A:** Incorrect for this question. This indicates ordinary turn completion, not that every business objective or external action succeeded. Application acceptance checks still apply. In this case: Incomplete streaming must not be reported as accepted final output.
- **B:** Incorrect for this question. A max_tokens stop can leave content incomplete. Inspect the response and recover appropriately instead of treating it as normal completion. In this case: Incomplete streaming must not be reported as accepted final output.
- **C:** Correct. A successful HTTP setup does not prove stream completion. Detect error events or interrupted streams, preserve status, and avoid publishing partial results as final success. In this case: Incomplete streaming must not be reported as accepted final output.
- **D:** Incorrect for this question. SDK accumulation helpers can provide the complete message. Inspect termination and errors before treating the resulting object as accepted application output. In this case: Incomplete streaming must not be reported as accepted final output.

### Question 95 — B

Answer: Isolate model-output defects from integration defects. Repair the integration transformation rather than repeatedly change the prompt. Check whether correct raw output was lost or changed by serialization, parsing, routing, or persistence. Not every visible error is fixed by changing the prompt. Local study-map skill 4.1 (Debugging and Error Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/streaming

- **A:** Incorrect for this question. Correlate the actual request, model response, tool execution, retries, and validation results. Diagnose the first failing boundary rather than infer cause from the final prose. In this case: Repair the integration transformation rather than repeatedly change the prompt.
- **B:** Correct. Check whether correct raw output was lost or changed by serialization, parsing, routing, or persistence. Not every visible error is fixed by changing the prompt. In this case: Repair the integration transformation rather than repeatedly change the prompt.
- **C:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Repair the integration transformation rather than repeatedly change the prompt.
- **D:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Repair the integration transformation rather than repeatedly change the prompt.

### Question 96 — A

Answer: Use controlled stubs for repeatable failure-path tests. Simulate relevant failures so recovery behavior is checkable before deployment. Inject timeouts, malformed responses, and provider failures without live side effects. Combine with contract and representative integration tests rather than infer complete correctness from mocks. Local study-map skill 4.1 (Debugging and Error Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/streaming

- **A:** Correct. Inject timeouts, malformed responses, and provider failures without live side effects. Combine with contract and representative integration tests rather than infer complete correctness from mocks. In this case: Simulate relevant failures so recovery behavior is checkable before deployment.
- **B:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Simulate relevant failures so recovery behavior is checkable before deployment.
- **C:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Simulate relevant failures so recovery behavior is checkable before deployment.
- **D:** Incorrect for this question. Check serialized requests, content blocks, status handling, and representative responses. Mock success alone may not reveal a malformed real request or unsupported provider feature. In this case: Simulate relevant failures so recovery behavior is checkable before deployment.

### Question 97 — B

Answer: Inspect a redacted end-to-end request and tool trace. Inspect actual request, response, tool, and validation traces to find the first failing boundary. Correlate the actual request, model response, tool execution, retries, and validation results. Diagnose the first failing boundary rather than infer cause from the final prose. Local study-map skill 4.1 (Debugging and Error Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/streaming

- **A:** Incorrect for this question. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: Inspect actual request, response, tool, and validation traces to find the first failing boundary.
- **B:** Correct. Correlate the actual request, model response, tool execution, retries, and validation results. Diagnose the first failing boundary rather than infer cause from the final prose. In this case: Inspect actual request, response, tool, and validation traces to find the first failing boundary.
- **C:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Inspect actual request, response, tool, and validation traces to find the first failing boundary.
- **D:** Incorrect for this question. Link a user task to provider requests, worker runs, and actions without using sensitive content as an identifier. Protect telemetry access and retention. In this case: Inspect actual request, response, tool, and validation traces to find the first failing boundary.

### Question 98 — A

Answer: Canary a version change with regression gates and rollback. Use controlled exposure, acceptance gates, observation, and rollback capability. Stage exposure to the new configuration, compare required outcomes, and retain a known-good path. A vendor release note is not workload validation. Local study-map skill 4.1 (Debugging and Error Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/streaming

- **A:** Correct. Stage exposure to the new configuration, compare required outcomes, and retain a known-good path. A vendor release note is not workload validation. In this case: Use controlled exposure, acceptance gates, observation, and rollback capability.
- **B:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Use controlled exposure, acceptance gates, observation, and rollback capability.
- **C:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Use controlled exposure, acceptance gates, observation, and rollback capability.
- **D:** Incorrect for this question. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: Use controlled exposure, acceptance gates, observation, and rollback capability.

### Question 99 — A

Answer: Use a durable idempotency key for the same logical action. Durable logical-action identity can prevent duplicate effects where the system supports it. Where supported, repeated requests for one operation should resolve to one intended external effect. Generating a new key for each retry defeats duplicate protection. Local study-map skill 4.1 (Debugging and Error Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/streaming

- **A:** Correct. Where supported, repeated requests for one operation should resolve to one intended external effect. Generating a new key for each retry defeats duplicate protection. In this case: Durable logical-action identity can prevent duplicate effects where the system supports it.
- **B:** Incorrect for this question. Local cancellation limits waiting or computation but does not guarantee the server stopped or a remote side effect was rolled back. In this case: Durable logical-action identity can prevent duplicate effects where the system supports it.
- **C:** Incorrect for this question. Separate a generated proposal from an authorized atomic or otherwise well-coordinated business effect. Define conflict handling and rollback or compensation behavior. In this case: Durable logical-action identity can prevent duplicate effects where the system supports it.
- **D:** Incorrect for this question. Bound user and dependency waits. A timeout is an uncertain execution outcome for mutations and may require status reconciliation rather than blind retry. In this case: Durable logical-action identity can prevent duplicate effects where the system supports it.

### Question 100 — C

Answer: Test the integration contract at the provider boundary. Test preservation of required fields through real serialization and parsing contracts. Check serialized requests, content blocks, status handling, and representative responses. Mock success alone may not reveal a malformed real request or unsupported provider feature. Local study-map skill 4.1 (Debugging and Error Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/streaming

- **A:** Incorrect for this question. Inject timeouts, malformed responses, and provider failures without live side effects. Combine with contract and representative integration tests rather than infer complete correctness from mocks. In this case: Test preservation of required fields through real serialization and parsing contracts.
- **B:** Incorrect for this question. Correlate the actual request, model response, tool execution, retries, and validation results. Diagnose the first failing boundary rather than infer cause from the final prose. In this case: Test preservation of required fields through real serialization and parsing contracts.
- **C:** Correct. Check serialized requests, content blocks, status handling, and representative responses. Mock success alone may not reveal a malformed real request or unsupported provider feature. In this case: Test preservation of required fields through real serialization and parsing contracts.
- **D:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Test preservation of required fields through real serialization and parsing contracts.
