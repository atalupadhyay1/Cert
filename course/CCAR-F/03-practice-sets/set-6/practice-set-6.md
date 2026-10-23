# Claude Certified Architect – Foundations (CCAR-F) — Practice Set 6

Integrated Architecture Scenarios & Final Review

100 questions · Suggested practice duration: 200 minutes · Practice target: 80%

Tests 1–5 are domain-focused. Test 6 is an expanded blueprint-proportioned review, not an official exam replica. Related concepts recur.

Select ONE best answer for every question. Answer key follows all questions.

Original educational content, not actual, recalled, or copied Anthropic exam items.

## Questions

### 1. A transformation must treat null, absent, and blank values differently, but prose instructions yield inconsistent changes. What can clarify intent?

Domain: Claude Code Configuration & Workflows

- A. Ask targeted design questions before implementation
- B. State explicit reportable and non-reportable criteria
- C. Use tests and specific failure feedback to drive iteration
- D. Provide concrete input–output examples

### 2. A research platform cannot reconstruct which specialist changed a finding because workers pass messages through uncontrolled peer channels. Which coordination pattern better supports traceability?

Domain: Agentic Architecture & Orchestration

- A. Route coordination through an orchestrator
- B. Run independent branches concurrently and join checked results
- C. Assign distinct scopes and explicit coverage responsibilities
- D. Wait for validated prerequisite outputs

### 3. Two failures share the same state transition, so each isolated fix breaks the other. How should revision feedback be supplied?

Domain: Claude Code Configuration & Workflows

- A. Explain interacting issues together before revising
- B. Run independent branches concurrently and join checked results
- C. Wait for validated prerequisite outputs
- D. Use tests and specific failure feedback to drive iteration

### 4. A team wants to reduce one recurring dismissed warning pattern but stores only overall acceptance rates. What structured metadata is missing?

Domain: Prompt Engineering & Structured Output

- A. Record detected_pattern and dismissal reasons
- B. State explicit reportable and non-reportable criteria
- C. Define severity using impact and concrete examples
- D. Temporarily disable a noisy category while repairing and evaluating it

### 5. The coordinator needs a dependency map, but detailed discovery would exhaust its main context. What should be delegated?

Domain: Claude Code Configuration & Workflows

- A. Ask targeted design questions before implementation
- B. Implement a small well-understood change directly
- C. Delegate focused exploration to a read-oriented subagent
- D. Use plan mode to investigate and compare approaches

### 6. An engineer knows an error string but not which module emits it. Which built-in tool should start the investigation?

Domain: Tool Design & MCP Integration

- A. Use Read to inspect current file contents
- B. Use Grep for content-pattern searches
- C. Use Glob for filename or path-pattern discovery
- D. Use Edit with a verified unique anchor

### 7. A single package uses a distinct local architecture convention for its whole subtree. What scope can express that cleanly?

Domain: Claude Code Configuration & Workflows

- A. Scope a rule with YAML paths glob patterns
- B. Put an on-demand workflow in a project skill
- C. Put personal cross-project preferences in ~/.claude/CLAUDE.md
- D. Use directory-scoped CLAUDE.md for a local package

### 8. A strategy report returns polished prose but never compares implementation risks, which the user explicitly requested. What should the coordinator do before release?

Domain: Agentic Architecture & Orchestration

- A. Evaluate coverage and delegate targeted follow-up work
- B. Run independent branches concurrently and join checked results
- C. Use a predictable sequence of specialized stages
- D. Enforce task, iteration, and spending safeguards

### 9. A worker encounters a timeout after retrieving some useful evidence. What should the coordinator receive?

Domain: Context Management & Reliability

- A. Annotate evidence coverage and unavailable sources
- B. Represent a successful query with no matches explicitly
- C. Return a structured tool error with category and retryability
- D. Return structured failure context and partial results

### 10. Programmatically configured workers never run after an SDK upgrade, and tracing shows the coordinator's allowed tool name no longer matches the installed launcher. What should be checked?

Domain: Agentic Architecture & Orchestration

- A. Pass relevant evidence and constraints explicitly
- B. Configure the subagent description, prompt, and tool scope
- C. Give each specialist only task-relevant tools
- D. Enable the version-appropriate subagent invocation tool

### 11. Results arrive out of order, and indexing by position attaches extractions to the wrong documents. What should correlate outcomes?

Domain: Prompt Engineering & Structured Output

- A. Correlate batch outcomes by custom_id
- B. Resubmit only failed items after diagnosing their errors
- C. Record detected_pattern and dismissal reasons
- D. Tune and validate on a representative sample before large submission

### 12. Reviewers see only low-confidence records, so accepted confident errors remain invisible. What monitoring should be added?

Domain: Context Management & Reliability

- A. Sample high-confidence outputs within relevant strata
- B. Calibrate field-confidence thresholds against labeled examples
- C. Route ambiguous, conflicting, or high-risk cases to qualified review
- D. Evaluate accuracy by document type and field segment

### 13. An isolated energy-analysis worker receives the topic but not the client's restriction to a specific region and period. Its results are irrelevant. What delegation input is missing?

Domain: Agentic Architecture & Orchestration

- A. Enable the version-appropriate subagent invocation tool
- B. Configure the subagent description, prompt, and tool scope
- C. Pass relevant evidence and constraints explicitly
- D. Persist structured task state and pending actions

### 14. Local reviewers approve two modules independently, but their changed parameter conventions are incompatible. What analysis pass should be added?

Domain: Agentic Architecture & Orchestration

- A. Add a cross-file or cross-component integration pass
- B. Run independent branches concurrently and join checked results
- C. Configure the subagent description, prompt, and tool scope
- D. Assign distinct scopes and explicit coverage responsibilities

### 15. A merge gate must return within the active developer workflow. Why is a batch turnaround window inappropriate? Which approach fits better?

Domain: Prompt Engineering & Structured Output

- A. Orchestrate client-tool follow-up outside a single batch request
- B. Use synchronous requests for blocking latency-sensitive work
- C. Tune and validate on a representative sample before large submission
- D. Use Message Batches for latency-tolerant independent requests

### 16. A patch reviewer inherits the generator's persuasive rationale and overlooks its central assumption. What separation may improve scrutiny?

Domain: Prompt Engineering & Structured Output

- A. Separate local analysis from cross-file integration review
- B. Use an independent reviewer without the generator rationale
- C. Calibrate field-confidence thresholds against labeled examples
- D. State explicit reportable and non-reportable criteria

### 17. A long support conversation summarizes a verified exact fee as 'a modest charge,' and a later decision needs the amount. What should be retained separately?

Domain: Context Management & Reliability

- A. Present key findings early and organize supporting details
- B. Compact context while preserving checked facts and open issues
- C. Preserve exact transactional facts outside lossy summaries
- D. Reduce tool output to relevant fields with provenance

### 18. Only a small authorization module changed after an otherwise useful exploration. What should be supplied on resumption?

Domain: Agentic Architecture & Orchestration

- A. Start a fresh session with a checked structured summary
- B. Resume the identified session when its context remains valid
- C. Fork an independent branch from a valid shared baseline
- D. Tell the resumed agent what changed and recheck affected evidence

### 19. A legacy audit begins without a dependency map, and each discovered service suggests new investigation paths. What decomposition strategy fits?

Domain: Agentic Architecture & Orchestration

- A. Use a predictable sequence of specialized stages
- B. Map the problem and revise subtasks as evidence emerges
- C. Wait for validated prerequisite outputs
- D. Run independent branches concurrently and join checked results

### 20. An agent wastes exploratory calls merely discovering which document collections exist. What MCP interface can expose this metadata?

Domain: Tool Design & MCP Integration

- A. Expose a supported MCP resource catalog
- B. Evaluate a maintained existing integration before writing a custom server
- C. Check connected-server discovery and effective availability
- D. Clarify tool purpose, inputs, outputs, and boundaries

### 21. Two records satisfy a customer's broad description, and the assistant proposes choosing the newest. What should happen first?

Domain: Context Management & Reliability

- A. Acknowledge frustration and offer a permitted resolution
- B. Ask for a discriminating identifier before selecting a record
- C. Honor an explicit request for a human agent
- D. Escalate a policy gap rather than invent a rule

### 22. A restricted repository denies the current identity. A worker proposes another employee's credential. Which handling should apply?

Domain: Tool Design & MCP Integration

- A. Correct invalid arguments before retrying
- B. Stop the unauthorized operation and use an approved access path
- C. Represent a successful query with no matches explicitly
- D. Retry a transient failure with bounded backoff

### 23. A customer explicitly asks for a representative, but an automation target encourages the bot to keep investigating. What should the workflow honor?

Domain: Context Management & Reliability

- A. Honor an explicit request for a human agent
- B. Acknowledge frustration and offer a permitted resolution
- C. Ask for a discriminating identifier before selecting a record
- D. Escalate when bounded attempts make no meaningful progress

### 24. A museum catalog lookup succeeds, but the next request includes only the user's original question. Claude cannot use the accession record. What should the client return?

Domain: Agentic Architecture & Orchestration

- A. Normalize tool observations before model consumption
- B. Resume the identified session when its context remains valid
- C. Append the assistant tool-use blocks and matching tool results
- D. Persist structured task state and pending actions

### 25. A valid purchase request is rejected under a fixed spending policy. Repeating it will not change eligibility. What outcome should the tool communicate?

Domain: Tool Design & MCP Integration

- A. Represent a successful query with no matches explicitly
- B. Explain the non-retryable business-rule outcome
- C. Correct invalid arguments before retrying
- D. Retry a transient failure with bounded backoff

### 26. A scheduling agent proposes a field visit before checking the technician's required certification. Which dependency must execution respect?

Domain: Agentic Architecture & Orchestration

- A. Fork an independent branch from a valid shared baseline
- B. Wait for validated prerequisite outputs
- C. Select specialists according to the actual task
- D. Run independent branches concurrently and join checked results

### 27. A model assigns a high confidence value to an extraction. What evidence is required before that value drives automation?

Domain: Context Management & Reliability

- A. Calibrate field-confidence thresholds against labeled examples
- B. Evaluate accuracy by document type and field segment
- C. Route ambiguous, conflicting, or high-risk cases to qualified review
- D. Sample high-confidence outputs within relevant strata

### 28. An engineer pauses a named investigation and later confirms that all relevant files and assumptions remain valid. Which session strategy can reuse that work?

Domain: Agentic Architecture & Orchestration

- A. Compact context while preserving checked facts and open issues
- B. Fork an independent branch from a valid shared baseline
- C. Resume the identified session when its context remains valid
- D. Start a fresh session with a checked structured summary

### 29. An institutional research system invokes legal, statistical, and editorial workers even when asked only for a report's publication date. What orchestration change is proportionate?

Domain: Agentic Architecture & Orchestration

- A. Use a predictable sequence of specialized stages
- B. Select specialists according to the actual task
- C. Assign distinct scopes and explicit coverage responsibilities
- D. Route coordination through an orchestrator

### 30. The first response must select one specific named metadata schema, although several tools exist. Which selection control fits?

Domain: Tool Design & MCP Integration

- A. Use tool_choice with type auto
- B. Use tool_choice with type any
- C. Force the required named tool for that turn
- D. Use supported strict structured output with a schema

### 31. A parser requires a supported schema, but the prompt merely says 'return JSON.' What mechanism most directly addresses structural compliance?

Domain: Prompt Engineering & Structured Output

- A. Specify deterministic normalization rules and preserve originals when needed
- B. Use supported strict structured output with a schema
- C. Use representative few-shot examples with boundaries
- D. State explicit reportable and non-reportable criteria

### 32. A weekly archive audit contains independent documents and is not user-blocking. Which processing approach should be considered?

Domain: Prompt Engineering & Structured Output

- A. Resubmit only failed items after diagnosing their errors
- B. Use synchronous requests for blocking latency-sensitive work
- C. Use Message Batches for latency-tolerant independent requests
- D. Tune and validate on a representative sample before large submission

### 33. One false-positive category damages developer trust, while other findings remain valuable. What temporary rollout adjustment is reasonable?

Domain: Prompt Engineering & Structured Output

- A. Temporarily disable a noisy category while repairing and evaluating it
- B. State explicit reportable and non-reportable criteria
- C. Record detected_pattern and dismissal reasons
- D. Include valid examples that should not be flagged

### 34. Three market researchers inspect the same news sites while no worker checks the required regulatory sources. What should change in task assignment?

Domain: Agentic Architecture & Orchestration

- A. Evaluate coverage and delegate targeted follow-up work
- B. Run independent branches concurrently and join checked results
- C. Select specialists according to the actual task
- D. Assign distinct scopes and explicit coverage responsibilities

### 35. An engineer assumes prefix caching permits inputs larger than the model's context capacity. What design principle should correct that?

Domain: Context Management & Reliability

- A. Use supported prompt-prefix caching for eligible repeated input
- B. Reduce tool output to relevant fields with provenance
- C. Compact context while preserving checked facts and open issues
- D. Budget instructions, evidence, history, and generation together

### 36. A policy describes one standard case but not the customer's materially different exception. What should the agent do?

Domain: Context Management & Reliability

- A. Ask for a discriminating identifier before selecting a record
- B. Acknowledge frustration and offer a permitted resolution
- C. Escalate a policy gap rather than invent a rule
- D. Honor an explicit request for a human agent

### 37. A library function is imported through renamed wrappers, and one literal search misses important callers. What investigation is needed?

Domain: Tool Design & MCP Integration

- A. Use Read to inspect current file contents
- B. Search exported aliases and wrappers as well as the original symbol
- C. Use Grep for content-pattern searches
- D. Use Glob for filename or path-pattern discovery

### 38. A contract agent may draft an amendment but only a designated officer may authorize submission. Which control belongs immediately before sending?

Domain: Agentic Architecture & Orchestration

- A. State explicit reportable and non-reportable criteria
- B. Enforce prerequisites in trusted execution code
- C. Create a structured handoff with facts, status, and next actions
- D. Require authorized approval before the consequential action

### 39. A compliance assistant only needs registered document IDs, yet its fetch tool accepts arbitrary network destinations. What interface is more appropriate?

Domain: Tool Design & MCP Integration

- A. Give each specialist only task-relevant tools
- B. Expose a constrained domain-specific operation
- C. Clarify tool purpose, inputs, outputs, and boundaries
- D. Separate genuinely different tasks into clearly bounded tools

### 40. A newly edited glob activates instructions for unintended files. What should be verified before adding workaround prompts?

Domain: Claude Code Configuration & Workflows

- A. Scope a rule with YAML paths glob patterns
- B. Inspect which instruction files are actually loaded
- C. Use @imports to keep instruction content modular
- D. Organize focused conventions in .claude/rules/

### 41. An agent has two necessary lookup tools for different source repositories, but both descriptions say 'find records.' Misrouting remains frequent. What should be improved first?

Domain: Tool Design & MCP Integration

- A. Define and validate a precise input schema
- B. Clarify tool purpose, inputs, outputs, and boundaries
- C. Give each specialist only task-relevant tools
- D. Expose a supported MCP resource catalog

### 42. A recurring reporting workflow has the same known stages: extract approved data, validate, then format. Which decomposition avoids unnecessary adaptive complexity?

Domain: Agentic Architecture & Orchestration

- A. Use a predictable sequence of specialized stages
- B. Select specialists according to the actual task
- C. Evaluate coverage and delegate targeted follow-up work
- D. Map the problem and revise subtasks as evidence emerges

### 43. A test generator invents unavailable fixtures and duplicates existing coverage. What repository context should it receive?

Domain: Claude Code Configuration & Workflows

- A. Use tests and specific failure feedback to drive iteration
- B. Provide existing tests and approved fixtures
- C. Provide concrete input–output examples
- D. Put shared project standards in versioned CLAUDE.md

### 44. A validation check identifies a recoverable field-placement error, but retries repeat the original prompt unchanged. What feedback should be supplied?

Domain: Prompt Engineering & Structured Output

- A. Use representative few-shot examples with boundaries
- B. Mark missing evidence and route for retrieval or review
- C. Retry with the document, failed result, and specific validation errors
- D. Use supported strict structured output with a schema

### 45. Examples teach only dangerous uses of an API, so the reviewer also flags its safe supported configuration. What example type should be added?

Domain: Prompt Engineering & Structured Output

- A. Record detected_pattern and dismissal reasons
- B. Use representative few-shot examples with boundaries
- C. State explicit reportable and non-reportable criteria
- D. Include valid examples that should not be flagged

### 46. A required output key may have no known source value. What schema distinction allows truthful representation?

Domain: Prompt Engineering & Structured Output

- A. Allow explicit unknown or absent values in the schema
- B. Use an extensible category plus a detail field
- C. Specify deterministic normalization rules and preserve originals when needed
- D. Use supported strict structured output with a schema

### 47. Sources mix currency units, and the downstream system expects one normalized unit. What should guide transformation?

Domain: Prompt Engineering & Structured Output

- A. Specify deterministic normalization rules and preserve originals when needed
- B. Validate extracted values against evidence and business rules
- C. Allow explicit unknown or absent values in the schema
- D. Use supported strict structured output with a schema

### 48. A coordinator sends accounting questions to a legal worker because their selection descriptions are identical. What should be revised?

Domain: Agentic Architecture & Orchestration

- A. Enable the version-appropriate subagent invocation tool
- B. Pass relevant evidence and constraints explicitly
- C. Assign distinct scopes and explicit coverage responsibilities
- D. Configure the subagent description, prompt, and tool scope

### 49. A restart occurs after an external request may have committed but before its response was stored. What recovery capability is essential?

Domain: Agentic Architecture & Orchestration

- A. Treat end_turn as the end of the current assistant turn
- B. Persist structured task state and pending actions
- C. Resume the identified session when its context remains valid
- D. Pass relevant evidence and constraints explicitly

### 50. One engineer wants a different review rubric without changing the approved team skill or accidentally shadowing it. What approach fits?

Domain: Claude Code Configuration & Workflows

- A. Put an on-demand workflow in a project skill
- B. Put shared project standards in versioned CLAUDE.md
- C. Use a project-scoped custom slash command
- D. Create a differently named personal skill variant

### 51. An approved MCP integration must be reviewed in pull requests and available to every project contributor. Which configuration scope fits?

Domain: Tool Design & MCP Integration

- A. Expose a supported MCP resource catalog
- B. Use user-scoped MCP configuration for personal servers
- C. Check connected-server discovery and effective availability
- D. Use project-scoped .mcp.json for shared server configuration

### 52. Two credible statistics use incompatible methods, and the report averages them into a new number. What synthesis behavior is preferable?

Domain: Context Management & Reliability

- A. Represent credible disagreement with attributed values
- B. Preserve collection and publication dates with claims
- C. Use representations suited to the content type
- D. Preserve claim-to-source mappings through every handoff

### 53. A convention applies to test files in many unrelated package directories but not other files alongside them. Which rule scope fits?

Domain: Claude Code Configuration & Workflows

- A. Put shared project standards in versioned CLAUDE.md
- B. Use directory-scoped CLAUDE.md for a local package
- C. Scope a rule with YAML paths glob patterns
- D. Use @imports to keep instruction content modular

### 54. Every new commit makes a bot repost already resolved findings and duplicate unresolved ones. What context supports better reruns?

Domain: Claude Code Configuration & Workflows

- A. Pass prior findings and request only new or unresolved issues
- B. Use an independent reviewer without the generator rationale
- C. State explicit reportable and non-reportable criteria
- D. Record detected_pattern and dismissal reasons

### 55. Extraction succeeds for tables but misses equivalent facts embedded in prose. What demonstration change should be evaluated?

Domain: Prompt Engineering & Structured Output

- A. Use representative few-shot examples with boundaries
- B. Provide concrete input–output examples
- C. Specify deterministic normalization rules and preserve originals when needed
- D. Allow explicit unknown or absent values in the schema

### 56. An obviously true but cosmetic observation is labeled critical solely because confidence is high. What rubric should distinguish these concepts?

Domain: Prompt Engineering & Structured Output

- A. Calibrate field-confidence thresholds against labeled examples
- B. Define severity using impact and concrete examples
- C. Record detected_pattern and dismissal reasons
- D. State explicit reportable and non-reportable criteria

### 57. A saved session contains mostly obsolete observations after a platform redesign. What starting context is safer for the next investigation?

Domain: Agentic Architecture & Orchestration

- A. Compact context while preserving checked facts and open issues
- B. Tell the resumed agent what changed and recheck affected evidence
- C. Resume the identified session when its context remains valid
- D. Start a fresh session with a checked structured summary

### 58. A saved instruction file seems to have no effect, and the team cannot tell whether it is in scope. What should be inspected?

Domain: Claude Code Configuration & Workflows

- A. Inspect which instruction files are actually loaded
- B. Put personal cross-project preferences in ~/.claude/CLAUDE.md
- C. Scope a rule with YAML paths glob patterns
- D. Put shared project standards in versioned CLAUDE.md

### 59. A feature request leaves retry side effects and retention requirements unspecified. What should the assistant do before implementation?

Domain: Claude Code Configuration & Workflows

- A. Ask targeted design questions before implementation
- B. State explicit reportable and non-reportable criteria
- C. Provide concrete input–output examples
- D. Use tests and specific failure feedback to drive iteration

### 60. A platform migration changes public interfaces across many modules and requires a rollback strategy. Which mode should precede broad edits?

Domain: Claude Code Configuration & Workflows

- A. Use tests and specific failure feedback to drive iteration
- B. Provide concrete input–output examples
- C. Implement a small well-understood change directly
- D. Use plan mode to investigate and compare approaches

### 61. An agent repeatedly searches for a publication that does not appear in any permitted catalog. Every individual call is valid. What prevents unlimited cost without confusing the stopping protocol?

Domain: Agentic Architecture & Orchestration

- A. Use a predictable sequence of specialized stages
- B. Inspect stop_reason and dispatch the appropriate branch
- C. Enforce task, iteration, and spending safeguards
- D. Treat end_turn as the end of the current assistant turn

### 62. An archive assistant writes 'I can check that' and emits a catalog tool request in the same response. The client stops because text is present. What should control continuation instead?

Domain: Agentic Architecture & Orchestration

- A. Inspect stop_reason and dispatch the appropriate branch
- B. Handle the output limit as an incomplete response
- C. Treat end_turn as the end of the current assistant turn
- D. Enforce task, iteration, and spending safeguards

### 63. An extracted object passes the schema but swaps the supplier and customer identifiers. What validation is still needed?

Domain: Prompt Engineering & Structured Output

- A. Allow explicit unknown or absent values in the schema
- B. Validate extracted values against evidence and business rules
- C. Specify deterministic normalization rules and preserve originals when needed
- D. Use supported strict structured output with a schema

### 64. A broad review misses both small local defects and interactions across files. What analysis architecture should be evaluated?

Domain: Prompt Engineering & Structured Output

- A. Use an independent reviewer without the generator rationale
- B. Separate local analysis from cross-file integration review
- C. Assign distinct scopes and explicit coverage responsibilities
- D. State explicit reportable and non-reportable criteria

### 65. A documentation skill should have only task-appropriate file operations rather than broad shell access. Which configuration feature helps?

Domain: Claude Code Configuration & Workflows

- A. Provide argument-hint for invocation guidance
- B. Use context: fork for isolated skill execution
- C. Restrict skill tool access with supported frontmatter
- D. Create a differently named personal skill variant

### 66. A tool contract is clear, but a system instruction maps all mentions of 'history' to an unrelated analytics operation. What should be examined?

Domain: Tool Design & MCP Integration

- A. Check connected-server discovery and effective availability
- B. Clarify tool purpose, inputs, outputs, and boundaries
- C. Inspect conflicting routing instructions as well as tool descriptions
- D. Define and validate a precise input schema

### 67. A status-normalization hook maps an unrecognized code to 'completed' so output sounds clearer. What principle should replace that transformation?

Domain: Agentic Architecture & Orchestration

- A. Use pre-execution tool interception for blocking policy checks
- B. Handle the output limit as an incomplete response
- C. Normalize tool observations before model consumption
- D. Compact context while preserving checked facts and open issues

### 68. A team wants to compare two migration strategies from one verified repository analysis without merging later conversational assumptions. What session approach fits?

Domain: Agentic Architecture & Orchestration

- A. Resume the identified session when its context remains valid
- B. Persist structured task state and pending actions
- C. Fork an independent branch from a valid shared baseline
- D. Start a fresh session with a checked structured summary

### 69. A document may belong to several known extraction types, and every response must call one available schema tool. What mode fits?

Domain: Tool Design & MCP Integration

- A. Use tool_choice with type auto
- B. Give each specialist only task-relevant tools
- C. Force the required named tool for that turn
- D. Use tool_choice with type any

### 70. An authorized archive query completes and reports no accession records for the supplied filters. What result class is this?

Domain: Tool Design & MCP Integration

- A. Stop the unauthorized operation and use an approved access path
- B. Represent a successful query with no matches explicitly
- C. Retry a transient failure with bounded backoff
- D. Return a structured tool error with category and retryability

### 71. Several packages duplicate one long approved standard and diverge after updates. What modular instruction mechanism helps?

Domain: Claude Code Configuration & Workflows

- A. Put an on-demand workflow in a project skill
- B. Scope a rule with YAML paths glob patterns
- C. Organize focused conventions in .claude/rules/
- D. Use @imports to keep instruction content modular

### 72. A document clearly belongs to a valid category absent from the enum. Which pattern retains the actual information?

Domain: Prompt Engineering & Structured Output

- A. Allow explicit unknown or absent values in the schema
- B. Use supported strict structured output with a schema
- C. Use an extensible category plus a detail field
- D. Specify deterministic normalization rules and preserve originals when needed

### 73. A targeted edit cannot distinguish repeated anchors. The agent can inspect the current full file and preserve unrelated content. What fallback may be appropriate?

Domain: Tool Design & MCP Integration

- A. Use Bash for an authorized command with bounded execution
- B. Use Read to inspect current file contents
- C. Read the current file and write a checked replacement
- D. Use Edit with a verified unique anchor

### 74. A confirmed defect needs one known conditional added to one function with existing tests. Which implementation approach is proportionate?

Domain: Claude Code Configuration & Workflows

- A. Delegate focused exploration to a read-oriented subagent
- B. Implement a small well-understood change directly
- C. Use plan mode to investigate and compare approaches
- D. Ask targeted design questions before implementation

### 75. An engineer needs files matching an integration-test naming pattern without knowing their contents. Which tool fits?

Domain: Tool Design & MCP Integration

- A. Use Glob for filename or path-pattern discovery
- B. Use Read to inspect current file contents
- C. Use Grep for content-pattern searches
- D. Read the current file and write a checked replacement

### 76. A receipt's stated total conflicts with the sum of extracted items. What design preserves evidence for investigation?

Domain: Prompt Engineering & Structured Output

- A. Compare independently calculated and source-stated totals
- B. Specify deterministic normalization rules and preserve originals when needed
- C. Use supported strict structured output with a schema
- D. Validate extracted values against evidence and business rules

### 77. A reviewer flags harmless formatting because its prompt says only 'find anything suspicious.' What prompting change targets precision?

Domain: Prompt Engineering & Structured Output

- A. Temporarily disable a noisy category while repairing and evaluating it
- B. State explicit reportable and non-reportable criteria
- C. Define severity using impact and concrete examples
- D. Use representative few-shot examples with boundaries

### 78. A pipeline needs schema-shaped machine-readable findings for inline comments, not variable prose. Which CLI output mechanism should be assessed?

Domain: Claude Code Configuration & Workflows

- A. State explicit reportable and non-reportable criteria
- B. Pass prior findings and request only new or unresolved issues
- C. Run Claude Code in non-interactive print mode
- D. Use supported JSON output and schema CLI options

### 79. An order lookup contributes fifty fields every turn even though only status, dates, and identifiers matter. What upstream change reduces context waste?

Domain: Context Management & Reliability

- A. Compact context while preserving checked facts and open issues
- B. Present key findings early and organize supporting details
- C. Supply the relevant conversation state on subsequent requests
- D. Reduce tool output to relevant fields with provenance

### 80. A crash leaves several worker artifacts, some partial and some validated. What should recovery consult before continuing?

Domain: Context Management & Reliability

- A. Resume from a checked manifest of worker states and artifacts
- B. Persist structured task state and pending actions
- C. Resume the identified session when its context remains valid
- D. Persist concise codebase findings with file and symbol pointers

### 81. A CI review job waits indefinitely for interactive input. Which invocation mode is relevant to automation?

Domain: Claude Code Configuration & Workflows

- A. Use plan mode to investigate and compare approaches
- B. Use supported JSON output and schema CLI options
- C. Run Claude Code in non-interactive print mode
- D. Use a project-scoped custom slash command

### 82. One required source remains unavailable, but a report can still answer other questions. What should the final artifact distinguish?

Domain: Context Management & Reliability

- A. Preserve claim-to-source mappings through every handoff
- B. Return structured failure context and partial results
- C. Annotate evidence coverage and unavailable sources
- D. Represent credible disagreement with attributed values

### 83. A final report keeps its bibliography but loses the link between each claim and its evidence. What must survive every handoff?

Domain: Context Management & Reliability

- A. Preserve collection and publication dates with claims
- B. Represent credible disagreement with attributed values
- C. Preserve claim-to-source mappings through every handoff
- D. Use representations suited to the content type

### 84. A prompt requires location, issue, severity, and suggested fix, but responses vary widely. What instructional addition can reinforce the expected format?

Domain: Prompt Engineering & Structured Output

- A. Include valid examples that should not be flagged
- B. Use representative few-shot examples with boundaries
- C. State explicit reportable and non-reportable criteria
- D. Provide concrete input–output examples

### 85. An equipment-disposal agent must never release a device before current asset ownership is verified. Prompt reminders are sometimes ignored. What should enforce the prerequisite?

Domain: Agentic Architecture & Orchestration

- A. Configure the subagent description, prompt, and tool scope
- B. State explicit reportable and non-reportable criteria
- C. Use representative few-shot examples with boundaries
- D. Enforce prerequisites in trusted execution code

### 86. A shared configuration needs a token, but source control must contain no literal credential. What authentication pattern fits?

Domain: Tool Design & MCP Integration

- A. Clarify tool purpose, inputs, outputs, and boundaries
- B. Use user-scoped MCP configuration for personal servers
- C. Reference runtime environment variables instead of committing tokens
- D. Use project-scoped .mcp.json for shared server configuration

### 87. A team convention is visible only to the engineer who stored it in ~/.claude/CLAUDE.md. How should shared guidance be distributed?

Domain: Claude Code Configuration & Workflows

- A. Put personal cross-project preferences in ~/.claude/CLAUDE.md
- B. Put an on-demand workflow in a project skill
- C. Use directory-scoped CLAUDE.md for a local package
- D. Put shared project standards in versioned CLAUDE.md

### 88. An assistant may answer a conceptual question directly and only call a lookup when needed. Which mode permits this discretion?

Domain: Tool Design & MCP Integration

- A. Give each specialist only task-relevant tools
- B. Use tool_choice with type any
- C. Force the required named tool for that turn
- D. Use tool_choice with type auto

### 89. A facilities case is transferred to an on-call specialist who cannot read the agent transcript. What transfer artifact should carry continuity?

Domain: Agentic Architecture & Orchestration

- A. Pass relevant evidence and constraints explicitly
- B. Persist structured task state and pending actions
- C. Persist concise codebase findings with file and symbol pointers
- D. Create a structured handoff with facts, status, and next actions

### 90. A read-oriented compliance worker receives finance mutation tools and starts selecting them during research. What should be changed?

Domain: Tool Design & MCP Integration

- A. Give each specialist only task-relevant tools
- B. Clarify tool purpose, inputs, outputs, and boundaries
- C. Separate genuinely different tasks into clearly bounded tools
- D. Check connected-server discovery and effective availability

### 91. Two source checks are independent, read-only, and within available capacity. The coordinator currently waits for the first before starting the second. What execution change may reduce elapsed time?

Domain: Agentic Architecture & Orchestration

- A. Wait for validated prerequisite outputs
- B. Run independent branches concurrently and join checked results
- C. Resume the identified session when its context remains valid
- D. Use a predictable sequence of specialized stages

### 92. An otherwise valid source query encounters a temporary outage, and the provider specifies when retry is permitted. Which recovery is appropriate?

Domain: Tool Design & MCP Integration

- A. Retry a transient failure with bounded backoff
- B. Stop the unauthorized operation and use an approved access path
- C. Explain the non-retryable business-rule outcome
- D. Correct invalid arguments before retrying

### 93. A pipeline repeatedly invents an attachment reference that never appears in the provided document. What should replace blind retry?

Domain: Prompt Engineering & Structured Output

- A. Allow explicit unknown or absent values in the schema
- B. Use supported strict structured output with a schema
- C. Mark missing evidence and route for retrieval or review
- D. Retry with the document, failed result, and specific validation errors

### 94. One inventory server returns timestamps in seconds and another uses ISO strings with time zones. Claude miscompares records. What observation processing helps?

Domain: Agentic Architecture & Orchestration

- A. Enforce prerequisites in trusted execution code
- B. Use pre-execution tool interception for blocking policy checks
- C. Require authorized approval before the consequential action
- D. Normalize tool observations before model consumption

### 95. A long codebase investigation starts referencing generic patterns instead of concrete discovered classes. What durable context aid helps?

Domain: Context Management & Reliability

- A. Resume from a checked manifest of worker states and artifacts
- B. Compact context while preserving checked facts and open issues
- C. Persist structured task state and pending actions
- D. Persist concise codebase findings with file and symbol pointers

### 96. A project skill produces long intermediate discovery logs, but the main session only needs its conclusion. Which behavior should be assessed?

Domain: Claude Code Configuration & Workflows

- A. Restrict skill tool access with supported frontmatter
- B. Create a differently named personal skill variant
- C. Provide argument-hint for invocation guidance
- D. Use context: fork for isolated skill execution

### 97. An outbound-message tool must reject unapproved destinations before sending any data. A post-tool audit detects violations too late. Which stage should block them?

Domain: Agentic Architecture & Orchestration

- A. Record detected_pattern and dismissal reasons
- B. Use pre-execution tool interception for blocking policy checks
- C. Normalize tool observations before model consumption
- D. State explicit reportable and non-reportable criteria

### 98. A maintenance assistant emits an unfinished structured proposal before reaching its generated-token limit. The pipeline marks the task complete. What response handling should replace this?

Domain: Agentic Architecture & Orchestration

- A. Resume the identified session when its context remains valid
- B. Treat end_turn as the end of the current assistant turn
- C. Handle the output limit as an incomplete response
- D. Enforce task, iteration, and spending safeguards

### 99. A dependency-audit procedure is relevant only when explicitly requested and should not fill every coding conversation. How should it be packaged?

Domain: Claude Code Configuration & Workflows

- A. Organize focused conventions in .claude/rules/
- B. Put shared project standards in versioned CLAUDE.md
- C. Put an on-demand workflow in a project skill
- D. Put personal cross-project preferences in ~/.claude/CLAUDE.md

### 100. An excellent overall score hides errors in a rare but consequential document field. What evaluation is needed before automation?

Domain: Context Management & Reliability

- A. Route ambiguous, conflicting, or high-risk cases to qualified review
- B. Sample high-confidence outputs within relevant strata
- C. Evaluate accuracy by document type and field segment
- D. Calibrate field-confidence thresholds against labeled examples

---

## Answer key and explanations

### Question 1 — D

Answer: Provide concrete input–output examples. Concrete input-output examples make those distinct behaviors visible. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. Closest official exam-guide objective 3.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. An interview-style clarification step surfaces unknown assumptions and constraints. Use it when uncertainty materially affects design. In this case: Concrete input-output examples make those distinct behaviors visible.
- **B:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Concrete input-output examples make those distinct behaviors visible.
- **C:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Concrete input-output examples make those distinct behaviors visible.
- **D:** Correct. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Concrete input-output examples make those distinct behaviors visible.

### Question 2 — A

Answer: Route coordination through an orchestrator. Route task communication and aggregation through a coordinator with consistent recovery and observation. A coordinator manages decomposition, routing, error handling, and aggregation in a hub-and-spoke design. Specialists need not communicate through uncontrolled peer channels. Closest official exam-guide objective 1.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Correct. A coordinator manages decomposition, routing, error handling, and aggregation in a hub-and-spoke design. Specialists need not communicate through uncontrolled peer channels. In this case: Route task communication and aggregation through a coordinator with consistent recovery and observation.
- **B:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Route task communication and aggregation through a coordinator with consistent recovery and observation.
- **C:** Incorrect for this question. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. In this case: Route task communication and aggregation through a coordinator with consistent recovery and observation.
- **D:** Incorrect for this question. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: Route task communication and aggregation through a coordinator with consistent recovery and observation.

### Question 3 — A

Answer: Explain interacting issues together before revising. Explain interacting constraints together so the implementation can reconcile them coherently. When fixes influence one another, provide the combined constraints and failure evidence. Independent issues can be addressed separately. Closest official exam-guide objective 3.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. When fixes influence one another, provide the combined constraints and failure evidence. Independent issues can be addressed separately. In this case: Explain interacting constraints together so the implementation can reconcile them coherently.
- **B:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Explain interacting constraints together so the implementation can reconcile them coherently.
- **C:** Incorrect for this question. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: Explain interacting constraints together so the implementation can reconcile them coherently.
- **D:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Explain interacting constraints together so the implementation can reconcile them coherently.

### Question 4 — A

Answer: Record detected_pattern and dismissal reasons. Detected patterns and dismissal reasons connect false positives to specific triggering constructs. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. Closest official exam-guide objective 4.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: Detected patterns and dismissal reasons connect false positives to specific triggering constructs.
- **B:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Detected patterns and dismissal reasons connect false positives to specific triggering constructs.
- **C:** Incorrect for this question. A consistent rubric distinguishes materially different harms. Self-reported confidence is not a substitute for severity or business impact. In this case: Detected patterns and dismissal reasons connect false positives to specific triggering constructs.
- **D:** Incorrect for this question. A narrowly controlled pause can restore trust while the category is improved. Preserve valuable other categories and monitor the consequences. In this case: Detected patterns and dismissal reasons connect false positives to specific triggering constructs.

### Question 5 — C

Answer: Delegate focused exploration to a read-oriented subagent. A focused exploration worker can isolate verbose investigation and return a concise map. Discovery can be isolated so verbose file output does not overwhelm the main conversation. Return useful findings and source pointers. Closest official exam-guide objective 3.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. An interview-style clarification step surfaces unknown assumptions and constraints. Use it when uncertainty materially affects design. In this case: A focused exploration worker can isolate verbose investigation and return a concise map.
- **B:** Incorrect for this question. A narrow fix with known requirements may not need a long planning phase. Tests and review still apply. In this case: A focused exploration worker can isolate verbose investigation and return a concise map.
- **C:** Correct. Discovery can be isolated so verbose file output does not overwhelm the main conversation. Return useful findings and source pointers. In this case: A focused exploration worker can isolate verbose investigation and return a concise map.
- **D:** Incorrect for this question. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. In this case: A focused exploration worker can isolate verbose investigation and return a concise map.

### Question 6 — B

Answer: Use Grep for content-pattern searches. Content-pattern search locates the string inside files before selective reading. Content search finds symbols, strings, and imports inside files. It is distinct from matching filenames and paths. Closest official exam-guide objective 2.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Inspecting current contents supplies evidence and reliable anchors before modification. A filename search alone does not reveal implementation behavior. In this case: Content-pattern search locates the string inside files before selective reading.
- **B:** Correct. Content search finds symbols, strings, and imports inside files. It is distinct from matching filenames and paths. In this case: Content-pattern search locates the string inside files before selective reading.
- **C:** Incorrect for this question. Glob discovers files by path patterns rather than searching their contents. It can identify candidates for later reading. In this case: Content-pattern search locates the string inside files before selective reading.
- **D:** Incorrect for this question. Targeted replacement is suitable when current text can be identified uniquely. Ambiguous anchors can change the wrong location or fail. In this case: Content-pattern search locates the string inside files before selective reading.

### Question 7 — D

Answer: Use directory-scoped CLAUDE.md for a local package. Directory instructions fit conventions whose relevance follows that package boundary. Local instructions fit conventions tied to a particular subtree. Cross-directory filename patterns may be better served by path-scoped rules. Closest official exam-guide objective 3.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. In this case: Directory instructions fit conventions whose relevance follows that package boundary.
- **B:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: Directory instructions fit conventions whose relevance follows that package boundary.
- **C:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: Directory instructions fit conventions whose relevance follows that package boundary.
- **D:** Correct. Local instructions fit conventions tied to a particular subtree. Cross-directory filename patterns may be better served by path-scoped rules. In this case: Directory instructions fit conventions whose relevance follows that package boundary.

### Question 8 — A

Answer: Evaluate coverage and delegate targeted follow-up work. Commission focused missing-risk work and reevaluate coverage rather than accept polished incompleteness. The coordinator compares results with requirements, identifies missing evidence, and commissions focused work rather than blindly repeating the whole pipeline. Closest official exam-guide objective 1.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Correct. The coordinator compares results with requirements, identifies missing evidence, and commissions focused work rather than blindly repeating the whole pipeline. In this case: Commission focused missing-risk work and reevaluate coverage rather than accept polished incompleteness.
- **B:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Commission focused missing-risk work and reevaluate coverage rather than accept polished incompleteness.
- **C:** Incorrect for this question. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: Commission focused missing-risk work and reevaluate coverage rather than accept polished incompleteness.
- **D:** Incorrect for this question. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. In this case: Commission focused missing-risk work and reevaluate coverage rather than accept polished incompleteness.

### Question 9 — D

Answer: Return structured failure context and partial results. Structured failure type, attempts, partial results, and alternatives enable targeted recovery. The coordinator needs failure type, attempted operation, useful outputs, and alternatives. A failure must not be disguised as a successful empty search. Closest official exam-guide objective 5.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. A report can proceed with supported partial results if it clearly distinguishes established conclusions from gaps. Silence falsely implies complete coverage. In this case: Structured failure type, attempts, partial results, and alternatives enable targeted recovery.
- **B:** Incorrect for this question. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. In this case: Structured failure type, attempts, partial results, and alternatives enable targeted recovery.
- **C:** Incorrect for this question. An error contract should identify failure class, recoverability, and useful context. MCP isError marks an execution failure; it should not disguise a valid empty result. In this case: Structured failure type, attempts, partial results, and alternatives enable targeted recovery.
- **D:** Correct. The coordinator needs failure type, attempted operation, useful outputs, and alternatives. A failure must not be disguised as a successful empty search. In this case: Structured failure type, attempts, partial results, and alternatives enable targeted recovery.

### Question 10 — D

Answer: Enable the version-appropriate subagent invocation tool. Use the version-appropriate supported invocation tool rather than blindly reuse the guide-era name. Delegation needs a permitted launcher. The July 2026 guide calls it Task; newer SDK documentation uses Agent. Check the installed SDK rather than mix names blindly. Closest official exam-guide objective 1.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Use the version-appropriate supported invocation tool rather than blindly reuse the guide-era name.
- **B:** Incorrect for this question. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: Use the version-appropriate supported invocation tool rather than blindly reuse the guide-era name.
- **C:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Use the version-appropriate supported invocation tool rather than blindly reuse the guide-era name.
- **D:** Correct. Delegation needs a permitted launcher. The July 2026 guide calls it Task; newer SDK documentation uses Agent. Check the installed SDK rather than mix names blindly. In this case: Use the version-appropriate supported invocation tool rather than blindly reuse the guide-era name.

### Question 11 — A

Answer: Correlate batch outcomes by custom_id. Match stable unique custom IDs to the submission manifest rather than assume ordering. Stable unique request identifiers connect results to inputs without assuming arrival order. Validate uniqueness and retain a manifest. Closest official exam-guide objective 4.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Stable unique request identifiers connect results to inputs without assuming arrival order. Validate uniqueness and retain a manifest. In this case: Match stable unique custom IDs to the submission manifest rather than assume ordering.
- **B:** Incorrect for this question. Targeted resubmission avoids repeating successes and allows input fixes. Track identities and protect downstream effects against duplicate processing. In this case: Match stable unique custom IDs to the submission manifest rather than assume ordering.
- **C:** Incorrect for this question. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: Match stable unique custom IDs to the submission manifest rather than assume ordering.
- **D:** Incorrect for this question. A small development sample reveals systematic extraction problems before multiplying them across the full dataset. Independent evaluation is still needed. In this case: Match stable unique custom IDs to the submission manifest rather than assume ordering.

### Question 12 — A

Answer: Sample high-confidence outputs within relevant strata. Randomly inspect high-confidence outputs within relevant strata to measure residual errors. Ongoing random checks among high-confidence results can discover hidden errors and changing patterns that low-confidence-only review misses. Closest official exam-guide objective 5.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. Ongoing random checks among high-confidence results can discover hidden errors and changing patterns that low-confidence-only review misses. In this case: Randomly inspect high-confidence outputs within relevant strata to measure residual errors.
- **B:** Incorrect for this question. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. In this case: Randomly inspect high-confidence outputs within relevant strata to measure residual errors.
- **C:** Incorrect for this question. Review priority should reflect uncertainty and consequences. A high uncalibrated confidence number should not override contradictory evidence. In this case: Randomly inspect high-confidence outputs within relevant strata to measure residual errors.
- **D:** Incorrect for this question. Averages can hide systematic failures in rare forms or important fields. Segment-level evaluation informs safe automation and review allocation. In this case: Randomly inspect high-confidence outputs within relevant strata to measure residual errors.

### Question 13 — C

Answer: Pass relevant evidence and constraints explicitly. Pass task-specific constraints explicitly instead of assume the worker inherits parent conversation details. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. Closest official exam-guide objective 1.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Delegation needs a permitted launcher. The July 2026 guide calls it Task; newer SDK documentation uses Agent. Check the installed SDK rather than mix names blindly. In this case: Pass task-specific constraints explicitly instead of assume the worker inherits parent conversation details.
- **B:** Incorrect for this question. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: Pass task-specific constraints explicitly instead of assume the worker inherits parent conversation details.
- **C:** Correct. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Pass task-specific constraints explicitly instead of assume the worker inherits parent conversation details.
- **D:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Pass task-specific constraints explicitly instead of assume the worker inherits parent conversation details.

### Question 14 — A

Answer: Add a cross-file or cross-component integration pass. Cross-component integration review checks interface assumptions invisible within isolated local passes. Local review finds local defects; a separate integration pass checks interactions, interfaces, and data flow across boundaries. Closest official exam-guide objective 1.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Correct. Local review finds local defects; a separate integration pass checks interactions, interfaces, and data flow across boundaries. In this case: Cross-component integration review checks interface assumptions invisible within isolated local passes.
- **B:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Cross-component integration review checks interface assumptions invisible within isolated local passes.
- **C:** Incorrect for this question. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: Cross-component integration review checks interface assumptions invisible within isolated local passes.
- **D:** Incorrect for this question. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. In this case: Cross-component integration review checks interface assumptions invisible within isolated local passes.

### Question 15 — B

Answer: Use synchronous requests for blocking latency-sensitive work. Use a latency-appropriate synchronous path with explicit timeout and failure policy. Blocking user or pre-merge flows need an appropriate timely request path. Synchronous execution still needs timeouts and failure policy. Closest official exam-guide objective 4.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. A batch item does not synchronously run an interactive client-tool conversation inside itself. The application executes permitted tools and constructs any follow-up requests. In this case: Use a latency-appropriate synchronous path with explicit timeout and failure policy.
- **B:** Correct. Blocking user or pre-merge flows need an appropriate timely request path. Synchronous execution still needs timeouts and failure policy. In this case: Use a latency-appropriate synchronous path with explicit timeout and failure policy.
- **C:** Incorrect for this question. A small development sample reveals systematic extraction problems before multiplying them across the full dataset. Independent evaluation is still needed. In this case: Use a latency-appropriate synchronous path with explicit timeout and failure policy.
- **D:** Incorrect for this question. Asynchronous batches fit non-blocking workloads. The retrieved guide describes discounted processing and a window up to 24 hours, not a guaranteed latency SLA. In this case: Use a latency-appropriate synchronous path with explicit timeout and failure policy.

### Question 16 — B

Answer: Use an independent reviewer without the generator rationale. An independent reviewer should receive requirements and artifacts without the original defense. Independent review reduces anchoring on the original solution. It still needs the specification, relevant code, and evidence; independence does not guarantee correctness. Closest official exam-guide objective 4.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Focused passes reduce attention dilution while integration review checks interactions. Manage deduplication and reconcile findings before release. In this case: An independent reviewer should receive requirements and artifacts without the original defense.
- **B:** Correct. Independent review reduces anchoring on the original solution. It still needs the specification, relevant code, and evidence; independence does not guarantee correctness. In this case: An independent reviewer should receive requirements and artifacts without the original defense.
- **C:** Incorrect for this question. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. In this case: An independent reviewer should receive requirements and artifacts without the original defense.
- **D:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: An independent reviewer should receive requirements and artifacts without the original defense.

### Question 17 — C

Answer: Preserve exact transactional facts outside lossy summaries. Keep exact transactional facts outside lossy narrative compression. Keep verified amounts, identifiers, dates, and commitments in structured state. General summaries can omit details that later decisions depend on. Closest official exam-guide objective 5.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. A structured overview and clear sections help reduce long-input position effects. Placement is a mitigation, not proof that every fact will be used. In this case: Keep exact transactional facts outside lossy narrative compression.
- **B:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Keep exact transactional facts outside lossy narrative compression.
- **C:** Correct. Keep verified amounts, identifiers, dates, and commitments in structured state. General summaries can omit details that later decisions depend on. In this case: Keep exact transactional facts outside lossy narrative compression.
- **D:** Incorrect for this question. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: Keep exact transactional facts outside lossy narrative compression.

### Question 18 — D

Answer: Tell the resumed agent what changed and recheck affected evidence. Identify the exact changed evidence and request targeted re-analysis rather than silently trust stale observations. Targeted re-analysis works when most prior context remains useful. Explicit change information prevents reliance on stale file or tool observations. Closest official exam-guide objective 1.7: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. A new context can avoid stale tool results when assumptions changed widely. Preserve verified facts, relevant constraints, and pointers rather than import all obsolete history. In this case: Identify the exact changed evidence and request targeted re-analysis rather than silently trust stale observations.
- **B:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Identify the exact changed evidence and request targeted re-analysis rather than silently trust stale observations.
- **C:** Incorrect for this question. Forking supports divergent explorations without overwriting the original conversation. It does not itself isolate external files or undo side effects. In this case: Identify the exact changed evidence and request targeted re-analysis rather than silently trust stale observations.
- **D:** Correct. Targeted re-analysis works when most prior context remains useful. Explicit change information prevents reliance on stale file or tool observations. In this case: Identify the exact changed evidence and request targeted re-analysis rather than silently trust stale observations.

### Question 19 — B

Answer: Map the problem and revise subtasks as evidence emerges. Explore and revise prioritized subtasks as evidence emerges rather than impose a premature exhaustive script. Open-ended investigation benefits from exploration, prioritized hypotheses, and revised decomposition rather than an exhaustive fixed script chosen before evidence. Closest official exam-guide objective 1.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: Explore and revise prioritized subtasks as evidence emerges rather than impose a premature exhaustive script.
- **B:** Correct. Open-ended investigation benefits from exploration, prioritized hypotheses, and revised decomposition rather than an exhaustive fixed script chosen before evidence. In this case: Explore and revise prioritized subtasks as evidence emerges rather than impose a premature exhaustive script.
- **C:** Incorrect for this question. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: Explore and revise prioritized subtasks as evidence emerges rather than impose a premature exhaustive script.
- **D:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Explore and revise prioritized subtasks as evidence emerges rather than impose a premature exhaustive script.

### Question 20 — A

Answer: Expose a supported MCP resource catalog. A resource catalog can describe available content without repeated action-like tool exploration. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. Closest official exam-guide objective 2.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: A resource catalog can describe available content without repeated action-like tool exploration.
- **B:** Incorrect for this question. A suitable standard integration may reduce work. Assess security, permissions, maintenance, and requirements before adoption; custom tools remain appropriate for unique workflows. In this case: A resource catalog can describe available content without repeated action-like tool exploration.
- **C:** Incorrect for this question. Configured servers can expose tools together when connected, but server failure, approval, filtering, and permissions can affect what is actually usable. In this case: A resource catalog can describe available content without repeated action-like tool exploration.
- **D:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: A resource catalog can describe available content without repeated action-like tool exploration.

### Question 21 — B

Answer: Ask for a discriminating identifier before selecting a record. Ask for a discriminating identifier or approved verification before selecting a target. Multiple plausible matches require clarification or an approved verification process. Recency, sentiment, or a guessed identity is not sufficient. Closest official exam-guide objective 5.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Frustration alone does not establish inability or a human preference. Offer an in-scope resolution unless the user requests a handoff or another escalation trigger applies. In this case: Ask for a discriminating identifier or approved verification before selecting a target.
- **B:** Correct. Multiple plausible matches require clarification or an approved verification process. Recency, sentiment, or a guessed identity is not sufficient. In this case: Ask for a discriminating identifier or approved verification before selecting a target.
- **C:** Incorrect for this question. A clear request for a person should trigger the approved handoff, not another autonomous investigation intended to avoid escalation. In this case: Ask for a discriminating identifier or approved verification before selecting a target.
- **D:** Incorrect for this question. If policy is silent or ambiguous on the actual request, a qualified owner should decide. Similar-looking cases do not automatically authorize an exception. In this case: Ask for a discriminating identifier or approved verification before selecting a target.

### Question 22 — B

Answer: Stop the unauthorized operation and use an approved access path. Use only an approved access path; denial does not authorize credential evasion. Permission denial does not justify trying alternate credentials or leaking restricted content. Recover only through explicitly authorized mechanisms. Closest official exam-guide objective 2.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. A validation failure points to an input defect. Repeating identical invalid arguments is not recovery. In this case: Use only an approved access path; denial does not authorize credential evasion.
- **B:** Correct. Permission denial does not justify trying alternate credentials or leaking restricted content. Recover only through explicitly authorized mechanisms. In this case: Use only an approved access path; denial does not authorize credential evasion.
- **C:** Incorrect for this question. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. In this case: Use only an approved access path; denial does not authorize credential evasion.
- **D:** Incorrect for this question. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: Use only an approved access path; denial does not authorize credential evasion.

### Question 23 — A

Answer: Honor an explicit request for a human agent. A clear human preference should trigger the approved handoff instead of being overridden for metrics. A clear request for a person should trigger the approved handoff, not another autonomous investigation intended to avoid escalation. Closest official exam-guide objective 5.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. A clear request for a person should trigger the approved handoff, not another autonomous investigation intended to avoid escalation. In this case: A clear human preference should trigger the approved handoff instead of being overridden for metrics.
- **B:** Incorrect for this question. Frustration alone does not establish inability or a human preference. Offer an in-scope resolution unless the user requests a handoff or another escalation trigger applies. In this case: A clear human preference should trigger the approved handoff instead of being overridden for metrics.
- **C:** Incorrect for this question. Multiple plausible matches require clarification or an approved verification process. Recency, sentiment, or a guessed identity is not sufficient. In this case: A clear human preference should trigger the approved handoff instead of being overridden for metrics.
- **D:** Incorrect for this question. A defined inability-to-progress condition prevents endless loops. Supply attempted actions, evidence, and unresolved questions to the recipient. In this case: A clear human preference should trigger the approved handoff instead of being overridden for metrics.

### Question 24 — C

Answer: Append the assistant tool-use blocks and matching tool results. Preserve the assistant request and matching tool-result observations in the valid message history. Client-tool observations must be returned with the correct tool-use identifiers in a valid message sequence so Claude can use actual results. Closest official exam-guide objective 1.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. In this case: Preserve the assistant request and matching tool-result observations in the valid message history.
- **B:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Preserve the assistant request and matching tool-result observations in the valid message history.
- **C:** Correct. Client-tool observations must be returned with the correct tool-use identifiers in a valid message sequence so Claude can use actual results. In this case: Preserve the assistant request and matching tool-result observations in the valid message history.
- **D:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Preserve the assistant request and matching tool-result observations in the valid message history.

### Question 25 — B

Answer: Explain the non-retryable business-rule outcome. Return a non-retryable business-policy rejection with legitimate next steps. A policy rejection is not normally fixed by repeating the same operation. Communicate the reason and legitimate next steps without evasion. Closest official exam-guide objective 2.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. In this case: Return a non-retryable business-policy rejection with legitimate next steps.
- **B:** Correct. A policy rejection is not normally fixed by repeating the same operation. Communicate the reason and legitimate next steps without evasion. In this case: Return a non-retryable business-policy rejection with legitimate next steps.
- **C:** Incorrect for this question. A validation failure points to an input defect. Repeating identical invalid arguments is not recovery. In this case: Return a non-retryable business-policy rejection with legitimate next steps.
- **D:** Incorrect for this question. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: Return a non-retryable business-policy rejection with legitimate next steps.

### Question 26 — B

Answer: Wait for validated prerequisite outputs. The proposed commitment must wait for the validated prerequisite certification and authorization checks. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. Closest official exam-guide objective 1.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Forking supports divergent explorations without overwriting the original conversation. It does not itself isolate external files or undo side effects. In this case: The proposed commitment must wait for the validated prerequisite certification and authorization checks.
- **B:** Correct. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: The proposed commitment must wait for the validated prerequisite certification and authorization checks.
- **C:** Incorrect for this question. Dynamic routing avoids invoking every specialist for a simple request. Selection should follow coverage needs, not a fixed ritual. In this case: The proposed commitment must wait for the validated prerequisite certification and authorization checks.
- **D:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: The proposed commitment must wait for the validated prerequisite certification and authorization checks.

### Question 27 — A

Answer: Calibrate field-confidence thresholds against labeled examples. Calibrate field-level scores against representative labeled correctness outcomes. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. Closest official exam-guide objective 5.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. In this case: Calibrate field-level scores against representative labeled correctness outcomes.
- **B:** Incorrect for this question. Averages can hide systematic failures in rare forms or important fields. Segment-level evaluation informs safe automation and review allocation. In this case: Calibrate field-level scores against representative labeled correctness outcomes.
- **C:** Incorrect for this question. Review priority should reflect uncertainty and consequences. A high uncalibrated confidence number should not override contradictory evidence. In this case: Calibrate field-level scores against representative labeled correctness outcomes.
- **D:** Incorrect for this question. Ongoing random checks among high-confidence results can discover hidden errors and changing patterns that low-confidence-only review misses. In this case: Calibrate field-level scores against representative labeled correctness outcomes.

### Question 28 — C

Answer: Resume the identified session when its context remains valid. Resume the identified valid session after checking current context applicability. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. Closest official exam-guide objective 1.7: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Resume the identified valid session after checking current context applicability.
- **B:** Incorrect for this question. Forking supports divergent explorations without overwriting the original conversation. It does not itself isolate external files or undo side effects. In this case: Resume the identified valid session after checking current context applicability.
- **C:** Correct. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Resume the identified valid session after checking current context applicability.
- **D:** Incorrect for this question. A new context can avoid stale tool results when assumptions changed widely. Preserve verified facts, relevant constraints, and pointers rather than import all obsolete history. In this case: Resume the identified valid session after checking current context applicability.

### Question 29 — B

Answer: Select specialists according to the actual task. Select only the specialist path needed by the actual request instead of always executing all roles. Dynamic routing avoids invoking every specialist for a simple request. Selection should follow coverage needs, not a fixed ritual. Closest official exam-guide objective 1.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: Select only the specialist path needed by the actual request instead of always executing all roles.
- **B:** Correct. Dynamic routing avoids invoking every specialist for a simple request. Selection should follow coverage needs, not a fixed ritual. In this case: Select only the specialist path needed by the actual request instead of always executing all roles.
- **C:** Incorrect for this question. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. In this case: Select only the specialist path needed by the actual request instead of always executing all roles.
- **D:** Incorrect for this question. A coordinator manages decomposition, routing, error handling, and aggregation in a hub-and-spoke design. Specialists need not communicate through uncontrolled peer channels. In this case: Select only the specialist path needed by the actual request instead of always executing all roles.

### Question 30 — C

Answer: Force the required named tool for that turn. Force the required named tool where supported rather than allow arbitrary tool choice. Where supported, named tool selection requires the specified tool. Additional workflow ordering and authorization still belong in application code. Closest official exam-guide objective 2.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Auto permits either a tool call or an ordinary response. It cannot guarantee extraction through a tool on every request. In this case: Force the required named tool where supported rather than allow arbitrary tool choice.
- **B:** Incorrect for this question. Where supported, any requires a tool selection but leaves the specific tool to the model. It does not guarantee that a particular named tool runs. In this case: Force the required named tool where supported rather than allow arbitrary tool choice.
- **C:** Correct. Where supported, named tool selection requires the specified tool. Additional workflow ordering and authorization still belong in application code. In this case: Force the required named tool where supported rather than allow arbitrary tool choice.
- **D:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Force the required named tool where supported rather than allow arbitrary tool choice.

### Question 31 — B

Answer: Use supported strict structured output with a schema. Use supported strict structured output and handle compatibility, refusal, and truncation states. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. Closest official exam-guide objective 4.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Use supported strict structured output and handle compatibility, refusal, and truncation states.
- **B:** Correct. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Use supported strict structured output and handle compatibility, refusal, and truncation states.
- **C:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Use supported strict structured output and handle compatibility, refusal, and truncation states.
- **D:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Use supported strict structured output and handle compatibility, refusal, and truncation states.

### Question 32 — C

Answer: Use Message Batches for latency-tolerant independent requests. Latency-tolerant work can use asynchronous batches under current service terms. Asynchronous batches fit non-blocking workloads. The retrieved guide describes discounted processing and a window up to 24 hours, not a guaranteed latency SLA. Closest official exam-guide objective 4.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Targeted resubmission avoids repeating successes and allows input fixes. Track identities and protect downstream effects against duplicate processing. In this case: Latency-tolerant work can use asynchronous batches under current service terms.
- **B:** Incorrect for this question. Blocking user or pre-merge flows need an appropriate timely request path. Synchronous execution still needs timeouts and failure policy. In this case: Latency-tolerant work can use asynchronous batches under current service terms.
- **C:** Correct. Asynchronous batches fit non-blocking workloads. The retrieved guide describes discounted processing and a window up to 24 hours, not a guaranteed latency SLA. In this case: Latency-tolerant work can use asynchronous batches under current service terms.
- **D:** Incorrect for this question. A small development sample reveals systematic extraction problems before multiplying them across the full dataset. Independent evaluation is still needed. In this case: Latency-tolerant work can use asynchronous batches under current service terms.

### Question 33 — A

Answer: Temporarily disable a noisy category while repairing and evaluating it. Pause the noisy category during repair and evaluation without discarding useful unrelated categories. A narrowly controlled pause can restore trust while the category is improved. Preserve valuable other categories and monitor the consequences. Closest official exam-guide objective 4.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. A narrowly controlled pause can restore trust while the category is improved. Preserve valuable other categories and monitor the consequences. In this case: Pause the noisy category during repair and evaluation without discarding useful unrelated categories.
- **B:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Pause the noisy category during repair and evaluation without discarding useful unrelated categories.
- **C:** Incorrect for this question. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: Pause the noisy category during repair and evaluation without discarding useful unrelated categories.
- **D:** Incorrect for this question. Negative examples teach a boundary and can reduce repeated false positives. They should not teach blanket suppression of an entire genuine-risk category. In this case: Pause the noisy category during repair and evaluation without discarding useful unrelated categories.

### Question 34 — D

Answer: Assign distinct scopes and explicit coverage responsibilities. Assign distinct source or subtopic responsibilities and verify combined required coverage. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. Closest official exam-guide objective 1.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. The coordinator compares results with requirements, identifies missing evidence, and commissions focused work rather than blindly repeating the whole pipeline. In this case: Assign distinct source or subtopic responsibilities and verify combined required coverage.
- **B:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Assign distinct source or subtopic responsibilities and verify combined required coverage.
- **C:** Incorrect for this question. Dynamic routing avoids invoking every specialist for a simple request. Selection should follow coverage needs, not a fixed ritual. In this case: Assign distinct source or subtopic responsibilities and verify combined required coverage.
- **D:** Correct. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. In this case: Assign distinct source or subtopic responsibilities and verify combined required coverage.

### Question 35 — D

Answer: Budget instructions, evidence, history, and generation together. Budget all request and generation components under actual limits; caching does not expand capacity. Follow the chosen model and service limits. Overflow handling varies; it is not universally automatic oldest-message deletion. Closest official exam-guide objective 5.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Caching may reduce repeated prefix processing under provider-specific rules. It does not extend the context window, update model weights, or verify an answer. In this case: Budget all request and generation components under actual limits; caching does not expand capacity.
- **B:** Incorrect for this question. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: Budget all request and generation components under actual limits; caching does not expand capacity.
- **C:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Budget all request and generation components under actual limits; caching does not expand capacity.
- **D:** Correct. Follow the chosen model and service limits. Overflow handling varies; it is not universally automatic oldest-message deletion. In this case: Budget all request and generation components under actual limits; caching does not expand capacity.

### Question 36 — C

Answer: Escalate a policy gap rather than invent a rule. An authorized owner must decide the policy gap rather than a model invent new authority. If policy is silent or ambiguous on the actual request, a qualified owner should decide. Similar-looking cases do not automatically authorize an exception. Closest official exam-guide objective 5.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Multiple plausible matches require clarification or an approved verification process. Recency, sentiment, or a guessed identity is not sufficient. In this case: An authorized owner must decide the policy gap rather than a model invent new authority.
- **B:** Incorrect for this question. Frustration alone does not establish inability or a human preference. Offer an in-scope resolution unless the user requests a handoff or another escalation trigger applies. In this case: An authorized owner must decide the policy gap rather than a model invent new authority.
- **C:** Correct. If policy is silent or ambiguous on the actual request, a qualified owner should decide. Similar-looking cases do not automatically authorize an exception. In this case: An authorized owner must decide the policy gap rather than a model invent new authority.
- **D:** Incorrect for this question. A clear request for a person should trigger the approved handoff, not another autonomous investigation intended to avoid escalation. In this case: An authorized owner must decide the policy gap rather than a model invent new authority.

### Question 37 — B

Answer: Search exported aliases and wrappers as well as the original symbol. Trace re-exports and aliases rather than assume the original spelling covers all usage. Usage can flow through re-exports and renamed wrappers. A single literal search may not reveal every relevant caller. Closest official exam-guide objective 2.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Inspecting current contents supplies evidence and reliable anchors before modification. A filename search alone does not reveal implementation behavior. In this case: Trace re-exports and aliases rather than assume the original spelling covers all usage.
- **B:** Correct. Usage can flow through re-exports and renamed wrappers. A single literal search may not reveal every relevant caller. In this case: Trace re-exports and aliases rather than assume the original spelling covers all usage.
- **C:** Incorrect for this question. Content search finds symbols, strings, and imports inside files. It is distinct from matching filenames and paths. In this case: Trace re-exports and aliases rather than assume the original spelling covers all usage.
- **D:** Incorrect for this question. Glob discovers files by path patterns rather than searching their contents. It can identify candidates for later reading. In this case: Trace re-exports and aliases rather than assume the original spelling covers all usage.

### Question 38 — D

Answer: Require authorized approval before the consequential action. Bind an authorized approval to the intended current action before the external effect occurs. Review must gate the external effect, be tied to the intended action, and use current authority. A later audit cannot reliably reverse a completed effect. Closest official exam-guide objective 1.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Bind an authorized approval to the intended current action before the external effect occurs.
- **B:** Incorrect for this question. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Bind an authorized approval to the intended current action before the external effect occurs.
- **C:** Incorrect for this question. The recipient needs verified identifiers, completed work, unresolved issues, supporting evidence, and recommended actions, especially when the full transcript is unavailable. In this case: Bind an authorized approval to the intended current action before the external effect occurs.
- **D:** Correct. Review must gate the external effect, be tied to the intended action, and use current authority. A later audit cannot reliably reverse a completed effect. In this case: Bind an authorized approval to the intended current action before the external effect occurs.

### Question 39 — B

Answer: Expose a constrained domain-specific operation. Expose a constrained approved-document operation with trusted destination checks. A narrow operation can enforce permitted sources, destinations, or actions more reliably than a general arbitrary-command or unrestricted-fetch interface. Closest official exam-guide objective 2.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Expose a constrained approved-document operation with trusted destination checks.
- **B:** Correct. A narrow operation can enforce permitted sources, destinations, or actions more reliably than a general arbitrary-command or unrestricted-fetch interface. In this case: Expose a constrained approved-document operation with trusted destination checks.
- **C:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Expose a constrained approved-document operation with trusted destination checks.
- **D:** Incorrect for this question. A generic interface can be split when its unrelated responsibilities cause ambiguity. Do not multiply near-identical tools without a meaningful boundary. In this case: Expose a constrained approved-document operation with trusted destination checks.

### Question 40 — B

Answer: Inspect which instruction files are actually loaded. Inspect actual path matching and effective loading instead of accumulating conflicting guidance. The guide mentions /memory; current documentation also describes /context. Use the available inspection mechanism to diagnose scope and loading, not just the presence of a file. Closest official exam-guide objective 3.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. In this case: Inspect actual path matching and effective loading instead of accumulating conflicting guidance.
- **B:** Correct. The guide mentions /memory; current documentation also describes /context. Use the available inspection mechanism to diagnose scope and loading, not just the presence of a file. In this case: Inspect actual path matching and effective loading instead of accumulating conflicting guidance.
- **C:** Incorrect for this question. Imports reference relevant supporting instruction files. Their actual loading and accessibility should be verified rather than assumed. In this case: Inspect actual path matching and effective loading instead of accumulating conflicting guidance.
- **D:** Incorrect for this question. Topic-specific rule files reduce one oversized instruction document. Add path scoping when a rule is only relevant to selected files. In this case: Inspect actual path matching and effective loading instead of accumulating conflicting guidance.

### Question 41 — B

Answer: Clarify tool purpose, inputs, outputs, and boundaries. Explain each source boundary, accepted input, returned evidence, and appropriate use case. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. Closest official exam-guide objective 2.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. In this case: Explain each source boundary, accepted input, returned evidence, and appropriate use case.
- **B:** Correct. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Explain each source boundary, accepted input, returned evidence, and appropriate use case.
- **C:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Explain each source boundary, accepted input, returned evidence, and appropriate use case.
- **D:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Explain each source boundary, accepted input, returned evidence, and appropriate use case.

### Question 42 — A

Answer: Use a predictable sequence of specialized stages. A predictable ordered chain fits stable dependent transformations. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. Closest official exam-guide objective 1.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Correct. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: A predictable ordered chain fits stable dependent transformations.
- **B:** Incorrect for this question. Dynamic routing avoids invoking every specialist for a simple request. Selection should follow coverage needs, not a fixed ritual. In this case: A predictable ordered chain fits stable dependent transformations.
- **C:** Incorrect for this question. The coordinator compares results with requirements, identifies missing evidence, and commissions focused work rather than blindly repeating the whole pipeline. In this case: A predictable ordered chain fits stable dependent transformations.
- **D:** Incorrect for this question. Open-ended investigation benefits from exploration, prioritized hypotheses, and revised decomposition rather than an exhaustive fixed script chosen before evidence. In this case: A predictable ordered chain fits stable dependent transformations.

### Question 43 — B

Answer: Provide existing tests and approved fixtures. Existing tests and approved fixture conventions anchor generation in the actual test environment. Relevant test context helps generation avoid duplicates and use valid repository conventions. Do not invent unavailable helper functions or external test data. Closest official exam-guide objective 3.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Existing tests and approved fixture conventions anchor generation in the actual test environment.
- **B:** Correct. Relevant test context helps generation avoid duplicates and use valid repository conventions. Do not invent unavailable helper functions or external test data. In this case: Existing tests and approved fixture conventions anchor generation in the actual test environment.
- **C:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Existing tests and approved fixture conventions anchor generation in the actual test environment.
- **D:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Existing tests and approved fixture conventions anchor generation in the actual test environment.

### Question 44 — C

Answer: Retry with the document, failed result, and specific validation errors. Include the document, failed extraction, and precise error in a bounded correction request. Actionable feedback supports correction when evidence exists. Bound attempts and validate the revised result rather than resubmit the same vague request indefinitely. Closest official exam-guide objective 4.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Include the document, failed extraction, and precise error in a bounded correction request.
- **B:** Incorrect for this question. Retries cannot recover a fact that the available document never contained. Use unknown status, authorized retrieval, clarification, or review instead of fabrication. In this case: Include the document, failed extraction, and precise error in a bounded correction request.
- **C:** Correct. Actionable feedback supports correction when evidence exists. Bound attempts and validate the revised result rather than resubmit the same vague request indefinitely. In this case: Include the document, failed extraction, and precise error in a bounded correction request.
- **D:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Include the document, failed extraction, and precise error in a bounded correction request.

### Question 45 — D

Answer: Include valid examples that should not be flagged. A valid near-miss demonstrates the boundary and should be explicitly shown as non-reportable. Negative examples teach a boundary and can reduce repeated false positives. They should not teach blanket suppression of an entire genuine-risk category. Closest official exam-guide objective 4.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: A valid near-miss demonstrates the boundary and should be explicitly shown as non-reportable.
- **B:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: A valid near-miss demonstrates the boundary and should be explicitly shown as non-reportable.
- **C:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: A valid near-miss demonstrates the boundary and should be explicitly shown as non-reportable.
- **D:** Correct. Negative examples teach a boundary and can reduce repeated false positives. They should not teach blanket suppression of an entire genuine-risk category. In this case: A valid near-miss demonstrates the boundary and should be explicitly shown as non-reportable.

### Question 46 — A

Answer: Allow explicit unknown or absent values in the schema. A nullable required key may contain null, whereas an optional key may be omitted. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. Closest official exam-guide objective 4.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: A nullable required key may contain null, whereas an optional key may be omitted.
- **B:** Incorrect for this question. An other category with details can represent valid cases outside an enum. Unclear represents uncertainty and should not be confused with known-but-uncatalogued categories. In this case: A nullable required key may contain null, whereas an optional key may be omitted.
- **C:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: A nullable required key may contain null, whereas an optional key may be omitted.
- **D:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: A nullable required key may contain null, whereas an optional key may be omitted.

### Question 47 — A

Answer: Specify deterministic normalization rules and preserve originals when needed. Define normalization rules and validate them against original values rather than guess or silently overwrite. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. Closest official exam-guide objective 4.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Define normalization rules and validate them against original values rather than guess or silently overwrite.
- **B:** Incorrect for this question. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Define normalization rules and validate them against original values rather than guess or silently overwrite.
- **C:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Define normalization rules and validate them against original values rather than guess or silently overwrite.
- **D:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Define normalization rules and validate them against original values rather than guess or silently overwrite.

### Question 48 — D

Answer: Configure the subagent description, prompt, and tool scope. Differentiate the descriptions that tell the coordinator when each specialist is appropriate. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. Closest official exam-guide objective 1.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Delegation needs a permitted launcher. The July 2026 guide calls it Task; newer SDK documentation uses Agent. Check the installed SDK rather than mix names blindly. In this case: Differentiate the descriptions that tell the coordinator when each specialist is appropriate.
- **B:** Incorrect for this question. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Differentiate the descriptions that tell the coordinator when each specialist is appropriate.
- **C:** Incorrect for this question. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. In this case: Differentiate the descriptions that tell the coordinator when each specialist is appropriate.
- **D:** Correct. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: Differentiate the descriptions that tell the coordinator when each specialist is appropriate.

### Question 49 — B

Answer: Persist structured task state and pending actions. Durable pending-action state enables reconciliation instead of repeating an uncertain side effect blindly. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. Closest official exam-guide objective 1.7: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. This indicates ordinary turn completion, not that every business objective or external action succeeded. Application acceptance checks still apply. In this case: Durable pending-action state enables reconciliation instead of repeating an uncertain side effect blindly.
- **B:** Correct. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Durable pending-action state enables reconciliation instead of repeating an uncertain side effect blindly.
- **C:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Durable pending-action state enables reconciliation instead of repeating an uncertain side effect blindly.
- **D:** Incorrect for this question. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Durable pending-action state enables reconciliation instead of repeating an uncertain side effect blindly.

### Question 50 — D

Answer: Create a differently named personal skill variant. Use a differently named personal variant rather than alter shared configuration. A personal variant can customize workflow without changing the shared skill for teammates. Distinct naming avoids accidental shadowing or confusion. Closest official exam-guide objective 3.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: Use a differently named personal variant rather than alter shared configuration.
- **B:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Use a differently named personal variant rather than alter shared configuration.
- **C:** Incorrect for this question. The guide describes .claude/commands/ for shared invocable commands. User-scoped commands are personal; feature details depend on Claude Code version. In this case: Use a differently named personal variant rather than alter shared configuration.
- **D:** Correct. A personal variant can customize workflow without changing the shared skill for teammates. Distinct naming avoids accidental shadowing or confusion. In this case: Use a differently named personal variant rather than alter shared configuration.

### Question 51 — D

Answer: Use project-scoped .mcp.json for shared server configuration. Versioned project server setup distributes shared tooling without relying on one user's home configuration. Versioned project configuration can distribute team tooling. Keep real credentials outside Git and check approvals and environment requirements. Closest official exam-guide objective 2.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Versioned project server setup distributes shared tooling without relying on one user's home configuration.
- **B:** Incorrect for this question. The guide describes user-scoped configuration in ~/.claude.json for personal tooling. Personal configuration is not automatically shared through the repository. In this case: Versioned project server setup distributes shared tooling without relying on one user's home configuration.
- **C:** Incorrect for this question. Configured servers can expose tools together when connected, but server failure, approval, filtering, and permissions can affect what is actually usable. In this case: Versioned project server setup distributes shared tooling without relying on one user's home configuration.
- **D:** Correct. Versioned project configuration can distribute team tooling. Keep real credentials outside Git and check approvals and environment requirements. In this case: Versioned project server setup distributes shared tooling without relying on one user's home configuration.

### Question 52 — A

Answer: Represent credible disagreement with attributed values. Preserve attributed disagreement and methodology rather than manufacture an unsupported reconciliation. Do not average incompatible measurements or choose one arbitrarily. Preserve context and distinguish contested findings from established ones. Closest official exam-guide objective 5.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. Do not average incompatible measurements or choose one arbitrarily. Preserve context and distinguish contested findings from established ones. In this case: Preserve attributed disagreement and methodology rather than manufacture an unsupported reconciliation.
- **B:** Incorrect for this question. Different measurement periods can explain apparent disagreements. Dates and methodology should remain attached rather than being stripped in summaries. In this case: Preserve attributed disagreement and methodology rather than manufacture an unsupported reconciliation.
- **C:** Incorrect for this question. Tables can preserve financial comparisons, while prose and structured lists suit other needs. A single forced format can hide important structure. In this case: Preserve attributed disagreement and methodology rather than manufacture an unsupported reconciliation.
- **D:** Incorrect for this question. Claims need traceable source identities, relevant excerpts, locations, and dates as applicable. A bibliography without claim mappings can lose attribution. In this case: Preserve attributed disagreement and methodology rather than manufacture an unsupported reconciliation.

### Question 53 — C

Answer: Scope a rule with YAML paths glob patterns. A YAML paths glob can follow the cross-directory file role. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. Closest official exam-guide objective 3.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: A YAML paths glob can follow the cross-directory file role.
- **B:** Incorrect for this question. Local instructions fit conventions tied to a particular subtree. Cross-directory filename patterns may be better served by path-scoped rules. In this case: A YAML paths glob can follow the cross-directory file role.
- **C:** Correct. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. In this case: A YAML paths glob can follow the cross-directory file role.
- **D:** Incorrect for this question. Imports reference relevant supporting instruction files. Their actual loading and accessibility should be verified rather than assumed. In this case: A YAML paths glob can follow the cross-directory file role.

### Question 54 — A

Answer: Pass prior findings and request only new or unresolved issues. Compare current code with prior findings and request only new or still-unaddressed issues. Comparing the current diff with prior findings can reduce duplicate review comments. Preserve still-valid findings rather than simply suppressing all repeats. Closest official exam-guide objective 3.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. Comparing the current diff with prior findings can reduce duplicate review comments. Preserve still-valid findings rather than simply suppressing all repeats. In this case: Compare current code with prior findings and request only new or still-unaddressed issues.
- **B:** Incorrect for this question. Independent review reduces anchoring on the original solution. It still needs the specification, relevant code, and evidence; independence does not guarantee correctness. In this case: Compare current code with prior findings and request only new or still-unaddressed issues.
- **C:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Compare current code with prior findings and request only new or still-unaddressed issues.
- **D:** Incorrect for this question. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: Compare current code with prior findings and request only new or still-unaddressed issues.

### Question 55 — A

Answer: Use representative few-shot examples with boundaries. Cover relevant document-structure variation rather than provide only one ideal layout. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. Closest official exam-guide objective 4.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Cover relevant document-structure variation rather than provide only one ideal layout.
- **B:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Cover relevant document-structure variation rather than provide only one ideal layout.
- **C:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Cover relevant document-structure variation rather than provide only one ideal layout.
- **D:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Cover relevant document-structure variation rather than provide only one ideal layout.

### Question 56 — B

Answer: Define severity using impact and concrete examples. Severity reflects business or technical impact, not certainty that an observation is true. A consistent rubric distinguishes materially different harms. Self-reported confidence is not a substitute for severity or business impact. Closest official exam-guide objective 4.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. In this case: Severity reflects business or technical impact, not certainty that an observation is true.
- **B:** Correct. A consistent rubric distinguishes materially different harms. Self-reported confidence is not a substitute for severity or business impact. In this case: Severity reflects business or technical impact, not certainty that an observation is true.
- **C:** Incorrect for this question. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: Severity reflects business or technical impact, not certainty that an observation is true.
- **D:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Severity reflects business or technical impact, not certainty that an observation is true.

### Question 57 — D

Answer: Start a fresh session with a checked structured summary. A fresh checked summary avoids treating superseded tool results as current facts. A new context can avoid stale tool results when assumptions changed widely. Preserve verified facts, relevant constraints, and pointers rather than import all obsolete history. Closest official exam-guide objective 1.7: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: A fresh checked summary avoids treating superseded tool results as current facts.
- **B:** Incorrect for this question. Targeted re-analysis works when most prior context remains useful. Explicit change information prevents reliance on stale file or tool observations. In this case: A fresh checked summary avoids treating superseded tool results as current facts.
- **C:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: A fresh checked summary avoids treating superseded tool results as current facts.
- **D:** Correct. A new context can avoid stale tool results when assumptions changed widely. Preserve verified facts, relevant constraints, and pointers rather than import all obsolete history. In this case: A fresh checked summary avoids treating superseded tool results as current facts.

### Question 58 — A

Answer: Inspect which instruction files are actually loaded. Verify the actual loaded instruction sources using supported inspection commands for the installed version. The guide mentions /memory; current documentation also describes /context. Use the available inspection mechanism to diagnose scope and loading, not just the presence of a file. Closest official exam-guide objective 3.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. The guide mentions /memory; current documentation also describes /context. Use the available inspection mechanism to diagnose scope and loading, not just the presence of a file. In this case: Verify the actual loaded instruction sources using supported inspection commands for the installed version.
- **B:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: Verify the actual loaded instruction sources using supported inspection commands for the installed version.
- **C:** Incorrect for this question. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. In this case: Verify the actual loaded instruction sources using supported inspection commands for the installed version.
- **D:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Verify the actual loaded instruction sources using supported inspection commands for the installed version.

### Question 59 — A

Answer: Ask targeted design questions before implementation. Ask targeted questions about design-critical assumptions rather than silently invent defaults. An interview-style clarification step surfaces unknown assumptions and constraints. Use it when uncertainty materially affects design. Closest official exam-guide objective 3.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. An interview-style clarification step surfaces unknown assumptions and constraints. Use it when uncertainty materially affects design. In this case: Ask targeted questions about design-critical assumptions rather than silently invent defaults.
- **B:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Ask targeted questions about design-critical assumptions rather than silently invent defaults.
- **C:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Ask targeted questions about design-critical assumptions rather than silently invent defaults.
- **D:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Ask targeted questions about design-critical assumptions rather than silently invent defaults.

### Question 60 — D

Answer: Use plan mode to investigate and compare approaches. Architectural alternatives and cross-file impact need investigation and an agreed plan. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. Closest official exam-guide objective 3.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Architectural alternatives and cross-file impact need investigation and an agreed plan.
- **B:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Architectural alternatives and cross-file impact need investigation and an agreed plan.
- **C:** Incorrect for this question. A narrow fix with known requirements may not need a long planning phase. Tests and review still apply. In this case: Architectural alternatives and cross-file impact need investigation and an agreed plan.
- **D:** Correct. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. In this case: Architectural alternatives and cross-file impact need investigation and an agreed plan.

### Question 61 — C

Answer: Enforce task, iteration, and spending safeguards. Task-level spending and iteration limits should yield an explicit unresolved outcome when exhausted. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. Closest official exam-guide objective 1.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: Task-level spending and iteration limits should yield an explicit unresolved outcome when exhausted.
- **B:** Incorrect for this question. The loop follows protocol stop reasons, executes permitted requested tools, and returns observations before continuing. Text appearing in a response does not establish completion. In this case: Task-level spending and iteration limits should yield an explicit unresolved outcome when exhausted.
- **C:** Correct. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. In this case: Task-level spending and iteration limits should yield an explicit unresolved outcome when exhausted.
- **D:** Incorrect for this question. This indicates ordinary turn completion, not that every business objective or external action succeeded. Application acceptance checks still apply. In this case: Task-level spending and iteration limits should yield an explicit unresolved outcome when exhausted.

### Question 62 — A

Answer: Inspect stop_reason and dispatch the appropriate branch. Inspect protocol stop_reason and dispatch the tool request rather than infer completion from commentary. The loop follows protocol stop reasons, executes permitted requested tools, and returns observations before continuing. Text appearing in a response does not establish completion. Closest official exam-guide objective 1.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Correct. The loop follows protocol stop reasons, executes permitted requested tools, and returns observations before continuing. Text appearing in a response does not establish completion. In this case: Inspect protocol stop_reason and dispatch the tool request rather than infer completion from commentary.
- **B:** Incorrect for this question. A max_tokens stop can leave content incomplete. Inspect the response and recover appropriately instead of treating it as normal completion. In this case: Inspect protocol stop_reason and dispatch the tool request rather than infer completion from commentary.
- **C:** Incorrect for this question. This indicates ordinary turn completion, not that every business objective or external action succeeded. Application acceptance checks still apply. In this case: Inspect protocol stop_reason and dispatch the tool request rather than infer completion from commentary.
- **D:** Incorrect for this question. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. In this case: Inspect protocol stop_reason and dispatch the tool request rather than infer completion from commentary.

### Question 63 — B

Answer: Validate extracted values against evidence and business rules. Source-backed semantic checks must verify field meaning beyond type and shape. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. Closest official exam-guide objective 4.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Source-backed semantic checks must verify field meaning beyond type and shape.
- **B:** Correct. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Source-backed semantic checks must verify field meaning beyond type and shape.
- **C:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Source-backed semantic checks must verify field meaning beyond type and shape.
- **D:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Source-backed semantic checks must verify field meaning beyond type and shape.

### Question 64 — B

Answer: Separate local analysis from cross-file integration review. Use focused local passes plus a reconciled integration pass for cross-file behavior. Focused passes reduce attention dilution while integration review checks interactions. Manage deduplication and reconcile findings before release. Closest official exam-guide objective 4.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Independent review reduces anchoring on the original solution. It still needs the specification, relevant code, and evidence; independence does not guarantee correctness. In this case: Use focused local passes plus a reconciled integration pass for cross-file behavior.
- **B:** Correct. Focused passes reduce attention dilution while integration review checks interactions. Manage deduplication and reconcile findings before release. In this case: Use focused local passes plus a reconciled integration pass for cross-file behavior.
- **C:** Incorrect for this question. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. In this case: Use focused local passes plus a reconciled integration pass for cross-file behavior.
- **D:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Use focused local passes plus a reconciled integration pass for cross-file behavior.

### Question 65 — C

Answer: Restrict skill tool access with supported frontmatter. Supported tool frontmatter can restrict exposure, with effective permissions verified separately. The guide covers allowed-tools to limit a skill workflow. Validate effective permissions; contextual instructions alone are not a sandbox. Closest official exam-guide objective 3.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Argument hints help users supply needed parameters. They do not replace actual argument validation or supply missing business facts. In this case: Supported tool frontmatter can restrict exposure, with effective permissions verified separately.
- **B:** Incorrect for this question. Where supported, an isolated skill context contains intermediate exploration. It does not automatically provide filesystem isolation or remove tool-permission obligations. In this case: Supported tool frontmatter can restrict exposure, with effective permissions verified separately.
- **C:** Correct. The guide covers allowed-tools to limit a skill workflow. Validate effective permissions; contextual instructions alone are not a sandbox. In this case: Supported tool frontmatter can restrict exposure, with effective permissions verified separately.
- **D:** Incorrect for this question. A personal variant can customize workflow without changing the shared skill for teammates. Distinct naming avoids accidental shadowing or confusion. In this case: Supported tool frontmatter can restrict exposure, with effective permissions verified separately.

### Question 66 — C

Answer: Inspect conflicting routing instructions as well as tool descriptions. Conflicting keyword-based routing instructions can misdirect selection despite adequate descriptions. System-prompt keywords can misroute requests even when tool contracts are reasonable. Diagnose both instruction and interface effects. Closest official exam-guide objective 2.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Configured servers can expose tools together when connected, but server failure, approval, filtering, and permissions can affect what is actually usable. In this case: Conflicting keyword-based routing instructions can misdirect selection despite adequate descriptions.
- **B:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Conflicting keyword-based routing instructions can misdirect selection despite adequate descriptions.
- **C:** Correct. System-prompt keywords can misroute requests even when tool contracts are reasonable. Diagnose both instruction and interface effects. In this case: Conflicting keyword-based routing instructions can misdirect selection despite adequate descriptions.
- **D:** Incorrect for this question. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. In this case: Conflicting keyword-based routing instructions can misdirect selection despite adequate descriptions.

### Question 67 — C

Answer: Normalize tool observations before model consumption. Normalization must preserve uncertainty and outcome truth rather than fabricate success. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. Closest official exam-guide objective 1.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. An appropriate pre-tool hook or equivalent trusted gate can deny a disallowed action before it runs. Hook implementation and failure handling must be tested. In this case: Normalization must preserve uncertainty and outcome truth rather than fabricate success.
- **B:** Incorrect for this question. A max_tokens stop can leave content incomplete. Inspect the response and recover appropriately instead of treating it as normal completion. In this case: Normalization must preserve uncertainty and outcome truth rather than fabricate success.
- **C:** Correct. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. In this case: Normalization must preserve uncertainty and outcome truth rather than fabricate success.
- **D:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Normalization must preserve uncertainty and outcome truth rather than fabricate success.

### Question 68 — C

Answer: Fork an independent branch from a valid shared baseline. Fork independent conversations from the valid baseline while controlling shared external side effects separately. Forking supports divergent explorations without overwriting the original conversation. It does not itself isolate external files or undo side effects. Closest official exam-guide objective 1.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Fork independent conversations from the valid baseline while controlling shared external side effects separately.
- **B:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Fork independent conversations from the valid baseline while controlling shared external side effects separately.
- **C:** Correct. Forking supports divergent explorations without overwriting the original conversation. It does not itself isolate external files or undo side effects. In this case: Fork independent conversations from the valid baseline while controlling shared external side effects separately.
- **D:** Incorrect for this question. A new context can avoid stale tool results when assumptions changed widely. Preserve verified facts, relevant constraints, and pointers rather than import all obsolete history. In this case: Fork independent conversations from the valid baseline while controlling shared external side effects separately.

### Question 69 — D

Answer: Use tool_choice with type any. Any requires a tool call while letting the model select an appropriate named schema. Where supported, any requires a tool selection but leaves the specific tool to the model. It does not guarantee that a particular named tool runs. Closest official exam-guide objective 2.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Auto permits either a tool call or an ordinary response. It cannot guarantee extraction through a tool on every request. In this case: Any requires a tool call while letting the model select an appropriate named schema.
- **B:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Any requires a tool call while letting the model select an appropriate named schema.
- **C:** Incorrect for this question. Where supported, named tool selection requires the specified tool. Additional workflow ordering and authorization still belong in application code. In this case: Any requires a tool call while letting the model select an appropriate named schema.
- **D:** Correct. Where supported, any requires a tool selection but leaves the specific tool to the model. It does not guarantee that a particular named tool runs. In this case: Any requires a tool call while letting the model select an appropriate named schema.

### Question 70 — B

Answer: Represent a successful query with no matches explicitly. Successful emptiness is distinct from a tool execution or access failure. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. Closest official exam-guide objective 2.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Permission denial does not justify trying alternate credentials or leaking restricted content. Recover only through explicitly authorized mechanisms. In this case: Successful emptiness is distinct from a tool execution or access failure.
- **B:** Correct. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. In this case: Successful emptiness is distinct from a tool execution or access failure.
- **C:** Incorrect for this question. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: Successful emptiness is distinct from a tool execution or access failure.
- **D:** Incorrect for this question. An error contract should identify failure class, recoverability, and useful context. MCP isError marks an execution failure; it should not disguise a valid empty result. In this case: Successful emptiness is distinct from a tool execution or access failure.

### Question 71 — D

Answer: Use @imports to keep instruction content modular. Reference relevant maintained guidance rather than keep inconsistent copied text. Imports reference relevant supporting instruction files. Their actual loading and accessibility should be verified rather than assumed. Closest official exam-guide objective 3.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: Reference relevant maintained guidance rather than keep inconsistent copied text.
- **B:** Incorrect for this question. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. In this case: Reference relevant maintained guidance rather than keep inconsistent copied text.
- **C:** Incorrect for this question. Topic-specific rule files reduce one oversized instruction document. Add path scoping when a rule is only relevant to selected files. In this case: Reference relevant maintained guidance rather than keep inconsistent copied text.
- **D:** Correct. Imports reference relevant supporting instruction files. Their actual loading and accessibility should be verified rather than assumed. In this case: Reference relevant maintained guidance rather than keep inconsistent copied text.

### Question 72 — C

Answer: Use an extensible category plus a detail field. Use an extensible other category with details instead of mislabeling the case as unknown. An other category with details can represent valid cases outside an enum. Unclear represents uncertainty and should not be confused with known-but-uncatalogued categories. Closest official exam-guide objective 4.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Use an extensible other category with details instead of mislabeling the case as unknown.
- **B:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Use an extensible other category with details instead of mislabeling the case as unknown.
- **C:** Correct. An other category with details can represent valid cases outside an enum. Unclear represents uncertainty and should not be confused with known-but-uncatalogued categories. In this case: Use an extensible other category with details instead of mislabeling the case as unknown.
- **D:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Use an extensible other category with details instead of mislabeling the case as unknown.

### Question 73 — C

Answer: Read the current file and write a checked replacement. Construct and verify a full-file replacement when a safe unique anchored change is unavailable. A full-file replacement can resolve ambiguous targeted edits, but must preserve unrelated content and account for concurrent changes. Closest official exam-guide objective 2.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Command execution fits tests, builds, and similar tasks when authorized. It is more powerful than file search and needs explicit safety and runtime controls. In this case: Construct and verify a full-file replacement when a safe unique anchored change is unavailable.
- **B:** Incorrect for this question. Inspecting current contents supplies evidence and reliable anchors before modification. A filename search alone does not reveal implementation behavior. In this case: Construct and verify a full-file replacement when a safe unique anchored change is unavailable.
- **C:** Correct. A full-file replacement can resolve ambiguous targeted edits, but must preserve unrelated content and account for concurrent changes. In this case: Construct and verify a full-file replacement when a safe unique anchored change is unavailable.
- **D:** Incorrect for this question. Targeted replacement is suitable when current text can be identified uniquely. Ambiguous anchors can change the wrong location or fail. In this case: Construct and verify a full-file replacement when a safe unique anchored change is unavailable.

### Question 74 — B

Answer: Implement a small well-understood change directly. The narrow understood scope can proceed directly with verification rather than a large planning phase. A narrow fix with known requirements may not need a long planning phase. Tests and review still apply. Closest official exam-guide objective 3.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Discovery can be isolated so verbose file output does not overwhelm the main conversation. Return useful findings and source pointers. In this case: The narrow understood scope can proceed directly with verification rather than a large planning phase.
- **B:** Correct. A narrow fix with known requirements may not need a long planning phase. Tests and review still apply. In this case: The narrow understood scope can proceed directly with verification rather than a large planning phase.
- **C:** Incorrect for this question. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. In this case: The narrow understood scope can proceed directly with verification rather than a large planning phase.
- **D:** Incorrect for this question. An interview-style clarification step surfaces unknown assumptions and constraints. Use it when uncertainty materially affects design. In this case: The narrow understood scope can proceed directly with verification rather than a large planning phase.

### Question 75 — A

Answer: Use Glob for filename or path-pattern discovery. Path-pattern discovery finds candidate filenames rather than scanning internal text. Glob discovers files by path patterns rather than searching their contents. It can identify candidates for later reading. Closest official exam-guide objective 2.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Glob discovers files by path patterns rather than searching their contents. It can identify candidates for later reading. In this case: Path-pattern discovery finds candidate filenames rather than scanning internal text.
- **B:** Incorrect for this question. Inspecting current contents supplies evidence and reliable anchors before modification. A filename search alone does not reveal implementation behavior. In this case: Path-pattern discovery finds candidate filenames rather than scanning internal text.
- **C:** Incorrect for this question. Content search finds symbols, strings, and imports inside files. It is distinct from matching filenames and paths. In this case: Path-pattern discovery finds candidate filenames rather than scanning internal text.
- **D:** Incorrect for this question. A full-file replacement can resolve ambiguous targeted edits, but must preserve unrelated content and account for concurrent changes. In this case: Path-pattern discovery finds candidate filenames rather than scanning internal text.

### Question 76 — A

Answer: Compare independently calculated and source-stated totals. Store both independently calculated and stated totals instead of silently replacing one. Separate calculated_total and stated_total can expose arithmetic or source inconsistencies. Preserve disagreement rather than silently overwrite evidence. Closest official exam-guide objective 4.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Separate calculated_total and stated_total can expose arithmetic or source inconsistencies. Preserve disagreement rather than silently overwrite evidence. In this case: Store both independently calculated and stated totals instead of silently replacing one.
- **B:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Store both independently calculated and stated totals instead of silently replacing one.
- **C:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Store both independently calculated and stated totals instead of silently replacing one.
- **D:** Incorrect for this question. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Store both independently calculated and stated totals instead of silently replacing one.

### Question 77 — B

Answer: State explicit reportable and non-reportable criteria. Define reportable defects and excluded patterns explicitly instead of asking for generic caution. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. Closest official exam-guide objective 4.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. A narrowly controlled pause can restore trust while the category is improved. Preserve valuable other categories and monitor the consequences. In this case: Define reportable defects and excluded patterns explicitly instead of asking for generic caution.
- **B:** Correct. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Define reportable defects and excluded patterns explicitly instead of asking for generic caution.
- **C:** Incorrect for this question. A consistent rubric distinguishes materially different harms. Self-reported confidence is not a substitute for severity or business impact. In this case: Define reportable defects and excluded patterns explicitly instead of asking for generic caution.
- **D:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Define reportable defects and excluded patterns explicitly instead of asking for generic caution.

### Question 78 — D

Answer: Use supported JSON output and schema CLI options. Use supported JSON output and schema options, then inspect status and validate the payload. The guide describes --output-format json and --json-schema for machine-parseable CI results. Verify the installed version and check execution status as well as payload. Closest official exam-guide objective 3.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Use supported JSON output and schema options, then inspect status and validate the payload.
- **B:** Incorrect for this question. Comparing the current diff with prior findings can reduce duplicate review comments. Preserve still-valid findings rather than simply suppressing all repeats. In this case: Use supported JSON output and schema options, then inspect status and validate the payload.
- **C:** Incorrect for this question. The -p or --print mode is intended for non-interactive runs. Authentication, permissions, termination, and artifact capture still require CI configuration. In this case: Use supported JSON output and schema options, then inspect status and validate the payload.
- **D:** Correct. The guide describes --output-format json and --json-schema for machine-parseable CI results. Verify the installed version and check execution status as well as payload. In this case: Use supported JSON output and schema options, then inspect status and validate the payload.

### Question 79 — D

Answer: Reduce tool output to relevant fields with provenance. Return relevant fields with evidence metadata before verbose observations accumulate. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. Closest official exam-guide objective 5.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Return relevant fields with evidence metadata before verbose observations accumulate.
- **B:** Incorrect for this question. A structured overview and clear sections help reduce long-input position effects. Placement is a mitigation, not proof that every fact will be used. In this case: Return relevant fields with evidence metadata before verbose observations accumulate.
- **C:** Incorrect for this question. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. In this case: Return relevant fields with evidence metadata before verbose observations accumulate.
- **D:** Correct. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: Return relevant fields with evidence metadata before verbose observations accumulate.

### Question 80 — A

Answer: Resume from a checked manifest of worker states and artifacts. A checked manifest should identify actual stage status and remaining work rather than infer completion from files. Recovery needs known state locations, completion status, source versions, and pending work. Do not infer completion merely because an output file exists. Closest official exam-guide objective 5.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. Recovery needs known state locations, completion status, source versions, and pending work. Do not infer completion merely because an output file exists. In this case: A checked manifest should identify actual stage status and remaining work rather than infer completion from files.
- **B:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: A checked manifest should identify actual stage status and remaining work rather than infer completion from files.
- **C:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: A checked manifest should identify actual stage status and remaining work rather than infer completion from files.
- **D:** Incorrect for this question. Durable notes counter context degradation and support later verification. Record source versions or change cues so notes are not mistaken for permanently current truth. In this case: A checked manifest should identify actual stage status and remaining work rather than infer completion from files.

### Question 81 — C

Answer: Run Claude Code in non-interactive print mode. Use non-interactive print mode with separately configured credentials, permissions, and failure handling. The -p or --print mode is intended for non-interactive runs. Authentication, permissions, termination, and artifact capture still require CI configuration. Closest official exam-guide objective 3.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. In this case: Use non-interactive print mode with separately configured credentials, permissions, and failure handling.
- **B:** Incorrect for this question. The guide describes --output-format json and --json-schema for machine-parseable CI results. Verify the installed version and check execution status as well as payload. In this case: Use non-interactive print mode with separately configured credentials, permissions, and failure handling.
- **C:** Correct. The -p or --print mode is intended for non-interactive runs. Authentication, permissions, termination, and artifact capture still require CI configuration. In this case: Use non-interactive print mode with separately configured credentials, permissions, and failure handling.
- **D:** Incorrect for this question. The guide describes .claude/commands/ for shared invocable commands. User-scoped commands are personal; feature details depend on Claude Code version. In this case: Use non-interactive print mode with separately configured credentials, permissions, and failure handling.

### Question 82 — C

Answer: Annotate evidence coverage and unavailable sources. Annotate supported findings and explicit coverage gaps instead of implying complete evidence. A report can proceed with supported partial results if it clearly distinguishes established conclusions from gaps. Silence falsely implies complete coverage. Closest official exam-guide objective 5.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Claims need traceable source identities, relevant excerpts, locations, and dates as applicable. A bibliography without claim mappings can lose attribution. In this case: Annotate supported findings and explicit coverage gaps instead of implying complete evidence.
- **B:** Incorrect for this question. The coordinator needs failure type, attempted operation, useful outputs, and alternatives. A failure must not be disguised as a successful empty search. In this case: Annotate supported findings and explicit coverage gaps instead of implying complete evidence.
- **C:** Correct. A report can proceed with supported partial results if it clearly distinguishes established conclusions from gaps. Silence falsely implies complete coverage. In this case: Annotate supported findings and explicit coverage gaps instead of implying complete evidence.
- **D:** Incorrect for this question. Do not average incompatible measurements or choose one arbitrarily. Preserve context and distinguish contested findings from established ones. In this case: Annotate supported findings and explicit coverage gaps instead of implying complete evidence.

### Question 83 — C

Answer: Preserve claim-to-source mappings through every handoff. Preserve structured claim-source mappings with relevant excerpts and locations. Claims need traceable source identities, relevant excerpts, locations, and dates as applicable. A bibliography without claim mappings can lose attribution. Closest official exam-guide objective 5.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Different measurement periods can explain apparent disagreements. Dates and methodology should remain attached rather than being stripped in summaries. In this case: Preserve structured claim-source mappings with relevant excerpts and locations.
- **B:** Incorrect for this question. Do not average incompatible measurements or choose one arbitrarily. Preserve context and distinguish contested findings from established ones. In this case: Preserve structured claim-source mappings with relevant excerpts and locations.
- **C:** Correct. Claims need traceable source identities, relevant excerpts, locations, and dates as applicable. A bibliography without claim mappings can lose attribution. In this case: Preserve structured claim-source mappings with relevant excerpts and locations.
- **D:** Incorrect for this question. Tables can preserve financial comparisons, while prose and structured lists suit other needs. A single forced format can hide important structure. In this case: Preserve structured claim-source mappings with relevant excerpts and locations.

### Question 84 — B

Answer: Use representative few-shot examples with boundaries. Representative complete demonstrations show the desired structure and judgment. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. Closest official exam-guide objective 4.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Negative examples teach a boundary and can reduce repeated false positives. They should not teach blanket suppression of an entire genuine-risk category. In this case: Representative complete demonstrations show the desired structure and judgment.
- **B:** Correct. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Representative complete demonstrations show the desired structure and judgment.
- **C:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Representative complete demonstrations show the desired structure and judgment.
- **D:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Representative complete demonstrations show the desired structure and judgment.

### Question 85 — D

Answer: Enforce prerequisites in trusted execution code. Trusted execution code must block the release until authoritative verification state satisfies the rule. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. Closest official exam-guide objective 1.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: Trusted execution code must block the release until authoritative verification state satisfies the rule.
- **B:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Trusted execution code must block the release until authoritative verification state satisfies the rule.
- **C:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Trusted execution code must block the release until authoritative verification state satisfies the rule.
- **D:** Correct. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Trusted execution code must block the release until authoritative verification state satisfies the rule.

### Question 86 — C

Answer: Reference runtime environment variables instead of committing tokens. Reference an approved runtime-provided secret and protect its use in execution and logs. Environment expansion can keep literal secrets out of project files. Supply credentials through an approved secret path and protect logs as well. Closest official exam-guide objective 2.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Reference an approved runtime-provided secret and protect its use in execution and logs.
- **B:** Incorrect for this question. The guide describes user-scoped configuration in ~/.claude.json for personal tooling. Personal configuration is not automatically shared through the repository. In this case: Reference an approved runtime-provided secret and protect its use in execution and logs.
- **C:** Correct. Environment expansion can keep literal secrets out of project files. Supply credentials through an approved secret path and protect logs as well. In this case: Reference an approved runtime-provided secret and protect its use in execution and logs.
- **D:** Incorrect for this question. Versioned project configuration can distribute team tooling. Keep real credentials outside Git and check approvals and environment requirements. In this case: Reference an approved runtime-provided secret and protect its use in execution and logs.

### Question 87 — D

Answer: Put shared project standards in versioned CLAUDE.md. Place shared standards in versioned project instructions instead of a personal home file. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. Closest official exam-guide objective 3.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: Place shared standards in versioned project instructions instead of a personal home file.
- **B:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: Place shared standards in versioned project instructions instead of a personal home file.
- **C:** Incorrect for this question. Local instructions fit conventions tied to a particular subtree. Cross-directory filename patterns may be better served by path-scoped rules. In this case: Place shared standards in versioned project instructions instead of a personal home file.
- **D:** Correct. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Place shared standards in versioned project instructions instead of a personal home file.

### Question 88 — D

Answer: Use tool_choice with type auto. Auto allows ordinary text instead of compelling a tool for every request. Auto permits either a tool call or an ordinary response. It cannot guarantee extraction through a tool on every request. Closest official exam-guide objective 2.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Auto allows ordinary text instead of compelling a tool for every request.
- **B:** Incorrect for this question. Where supported, any requires a tool selection but leaves the specific tool to the model. It does not guarantee that a particular named tool runs. In this case: Auto allows ordinary text instead of compelling a tool for every request.
- **C:** Incorrect for this question. Where supported, named tool selection requires the specified tool. Additional workflow ordering and authorization still belong in application code. In this case: Auto allows ordinary text instead of compelling a tool for every request.
- **D:** Correct. Auto permits either a tool call or an ordinary response. It cannot guarantee extraction through a tool on every request. In this case: Auto allows ordinary text instead of compelling a tool for every request.

### Question 89 — D

Answer: Create a structured handoff with facts, status, and next actions. Include verified identifiers, evidence, completed checks, unresolved issues, and proposed next actions. The recipient needs verified identifiers, completed work, unresolved issues, supporting evidence, and recommended actions, especially when the full transcript is unavailable. Closest official exam-guide objective 1.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Include verified identifiers, evidence, completed checks, unresolved issues, and proposed next actions.
- **B:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Include verified identifiers, evidence, completed checks, unresolved issues, and proposed next actions.
- **C:** Incorrect for this question. Durable notes counter context degradation and support later verification. Record source versions or change cues so notes are not mistaken for permanently current truth. In this case: Include verified identifiers, evidence, completed checks, unresolved issues, and proposed next actions.
- **D:** Correct. The recipient needs verified identifiers, completed work, unresolved issues, supporting evidence, and recommended actions, especially when the full transcript is unavailable. In this case: Include verified identifiers, evidence, completed checks, unresolved issues, and proposed next actions.

### Question 90 — A

Answer: Give each specialist only task-relevant tools. Remove operations unrelated to its role from the effective tool surface. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. Closest official exam-guide objective 2.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Remove operations unrelated to its role from the effective tool surface.
- **B:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Remove operations unrelated to its role from the effective tool surface.
- **C:** Incorrect for this question. A generic interface can be split when its unrelated responsibilities cause ambiguity. Do not multiply near-identical tools without a meaningful boundary. In this case: Remove operations unrelated to its role from the effective tool surface.
- **D:** Incorrect for this question. Configured servers can expose tools together when connected, but server failure, approval, filtering, and permissions can affect what is actually usable. In this case: Remove operations unrelated to its role from the effective tool surface.

### Question 91 — B

Answer: Run independent branches concurrently and join checked results. Independent worker calls can run concurrently before their checked outputs are combined. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. Closest official exam-guide objective 1.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: Independent worker calls can run concurrently before their checked outputs are combined.
- **B:** Correct. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Independent worker calls can run concurrently before their checked outputs are combined.
- **C:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Independent worker calls can run concurrently before their checked outputs are combined.
- **D:** Incorrect for this question. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: Independent worker calls can run concurrently before their checked outputs are combined.

### Question 92 — A

Answer: Retry a transient failure with bounded backoff. Use bounded delayed recovery that respects provider guidance instead of treating inaccessibility as no evidence. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. Closest official exam-guide objective 2.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: Use bounded delayed recovery that respects provider guidance instead of treating inaccessibility as no evidence.
- **B:** Incorrect for this question. Permission denial does not justify trying alternate credentials or leaking restricted content. Recover only through explicitly authorized mechanisms. In this case: Use bounded delayed recovery that respects provider guidance instead of treating inaccessibility as no evidence.
- **C:** Incorrect for this question. A policy rejection is not normally fixed by repeating the same operation. Communicate the reason and legitimate next steps without evasion. In this case: Use bounded delayed recovery that respects provider guidance instead of treating inaccessibility as no evidence.
- **D:** Incorrect for this question. A validation failure points to an input defect. Repeating identical invalid arguments is not recovery. In this case: Use bounded delayed recovery that respects provider guidance instead of treating inaccessibility as no evidence.

### Question 93 — C

Answer: Mark missing evidence and route for retrieval or review. Represent missing evidence and retrieve an authorized source or route for clarification and review. Retries cannot recover a fact that the available document never contained. Use unknown status, authorized retrieval, clarification, or review instead of fabrication. Closest official exam-guide objective 4.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Represent missing evidence and retrieve an authorized source or route for clarification and review.
- **B:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Represent missing evidence and retrieve an authorized source or route for clarification and review.
- **C:** Correct. Retries cannot recover a fact that the available document never contained. Use unknown status, authorized retrieval, clarification, or review instead of fabrication. In this case: Represent missing evidence and retrieve an authorized source or route for clarification and review.
- **D:** Incorrect for this question. Actionable feedback supports correction when evidence exists. Bound attempts and validate the revised result rather than resubmit the same vague request indefinitely. In this case: Represent missing evidence and retrieve an authorized source or route for clarification and review.

### Question 94 — D

Answer: Normalize tool observations before model consumption. Normalize representations while preserving source meaning, time-zone information, and provenance. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. Closest official exam-guide objective 1.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Normalize representations while preserving source meaning, time-zone information, and provenance.
- **B:** Incorrect for this question. An appropriate pre-tool hook or equivalent trusted gate can deny a disallowed action before it runs. Hook implementation and failure handling must be tested. In this case: Normalize representations while preserving source meaning, time-zone information, and provenance.
- **C:** Incorrect for this question. Review must gate the external effect, be tied to the intended action, and use current authority. A later audit cannot reliably reverse a completed effect. In this case: Normalize representations while preserving source meaning, time-zone information, and provenance.
- **D:** Correct. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. In this case: Normalize representations while preserving source meaning, time-zone information, and provenance.

### Question 95 — D

Answer: Persist concise codebase findings with file and symbol pointers. Record concise checked findings with file and symbol pointers that can be revalidated. Durable notes counter context degradation and support later verification. Record source versions or change cues so notes are not mistaken for permanently current truth. Closest official exam-guide objective 5.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Recovery needs known state locations, completion status, source versions, and pending work. Do not infer completion merely because an output file exists. In this case: Record concise checked findings with file and symbol pointers that can be revalidated.
- **B:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Record concise checked findings with file and symbol pointers that can be revalidated.
- **C:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Record concise checked findings with file and symbol pointers that can be revalidated.
- **D:** Correct. Durable notes counter context degradation and support later verification. Record source versions or change cues so notes are not mistaken for permanently current truth. In this case: Record concise checked findings with file and symbol pointers that can be revalidated.

### Question 96 — D

Answer: Use context: fork for isolated skill execution. Isolated skill context can contain intermediate exploration while returning concise results. Where supported, an isolated skill context contains intermediate exploration. It does not automatically provide filesystem isolation or remove tool-permission obligations. Closest official exam-guide objective 3.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. The guide covers allowed-tools to limit a skill workflow. Validate effective permissions; contextual instructions alone are not a sandbox. In this case: Isolated skill context can contain intermediate exploration while returning concise results.
- **B:** Incorrect for this question. A personal variant can customize workflow without changing the shared skill for teammates. Distinct naming avoids accidental shadowing or confusion. In this case: Isolated skill context can contain intermediate exploration while returning concise results.
- **C:** Incorrect for this question. Argument hints help users supply needed parameters. They do not replace actual argument validation or supply missing business facts. In this case: Isolated skill context can contain intermediate exploration while returning concise results.
- **D:** Correct. Where supported, an isolated skill context contains intermediate exploration. It does not automatically provide filesystem isolation or remove tool-permission obligations. In this case: Isolated skill context can contain intermediate exploration while returning concise results.

### Question 97 — B

Answer: Use pre-execution tool interception for blocking policy checks. Pre-execution interception must enforce the destination rule before information leaves the system. An appropriate pre-tool hook or equivalent trusted gate can deny a disallowed action before it runs. Hook implementation and failure handling must be tested. Closest official exam-guide objective 1.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: Pre-execution interception must enforce the destination rule before information leaves the system.
- **B:** Correct. An appropriate pre-tool hook or equivalent trusted gate can deny a disallowed action before it runs. Hook implementation and failure handling must be tested. In this case: Pre-execution interception must enforce the destination rule before information leaves the system.
- **C:** Incorrect for this question. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. In this case: Pre-execution interception must enforce the destination rule before information leaves the system.
- **D:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Pre-execution interception must enforce the destination rule before information leaves the system.

### Question 98 — C

Answer: Handle the output limit as an incomplete response. An output-limit stop must be handled as incomplete before any acceptance or execution decision. A max_tokens stop can leave content incomplete. Inspect the response and recover appropriately instead of treating it as normal completion. Closest official exam-guide objective 1.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: An output-limit stop must be handled as incomplete before any acceptance or execution decision.
- **B:** Incorrect for this question. This indicates ordinary turn completion, not that every business objective or external action succeeded. Application acceptance checks still apply. In this case: An output-limit stop must be handled as incomplete before any acceptance or execution decision.
- **C:** Correct. A max_tokens stop can leave content incomplete. Inspect the response and recover appropriately instead of treating it as normal completion. In this case: An output-limit stop must be handled as incomplete before any acceptance or execution decision.
- **D:** Incorrect for this question. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. In this case: An output-limit stop must be handled as incomplete before any acceptance or execution decision.

### Question 99 — C

Answer: Put an on-demand workflow in a project skill. An on-demand skill fits a specialized workflow better than universal instruction text. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. Closest official exam-guide objective 3.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Topic-specific rule files reduce one oversized instruction document. Add path scoping when a rule is only relevant to selected files. In this case: An on-demand skill fits a specialized workflow better than universal instruction text.
- **B:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: An on-demand skill fits a specialized workflow better than universal instruction text.
- **C:** Correct. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: An on-demand skill fits a specialized workflow better than universal instruction text.
- **D:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: An on-demand skill fits a specialized workflow better than universal instruction text.

### Question 100 — C

Answer: Evaluate accuracy by document type and field segment. Assess accuracy by document type and field segment rather than rely on an aggregate average. Averages can hide systematic failures in rare forms or important fields. Segment-level evaluation informs safe automation and review allocation. Closest official exam-guide objective 5.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Review priority should reflect uncertainty and consequences. A high uncalibrated confidence number should not override contradictory evidence. In this case: Assess accuracy by document type and field segment rather than rely on an aggregate average.
- **B:** Incorrect for this question. Ongoing random checks among high-confidence results can discover hidden errors and changing patterns that low-confidence-only review misses. In this case: Assess accuracy by document type and field segment rather than rely on an aggregate average.
- **C:** Correct. Averages can hide systematic failures in rare forms or important fields. Segment-level evaluation informs safe automation and review allocation. In this case: Assess accuracy by document type and field segment rather than rely on an aggregate average.
- **D:** Incorrect for this question. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. In this case: Assess accuracy by document type and field segment rather than rely on an aggregate average.
