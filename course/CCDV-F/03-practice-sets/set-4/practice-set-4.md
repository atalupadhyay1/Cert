# Claude Certified Developer – Foundations (CCDV-F) — Practice Set 4

Prompt and Context Engineering

100 questions · Suggested practice duration: 200 minutes · Practice target: 80%

Tests 1–5 are focused learning tests. Test 6 is an expanded blueprint-proportioned review, not an official exam replica. Related concepts recur.

Select ONE best answer for every question. Answer key follows all questions.

Original educational content, not actual, recalled, or copied Anthropic exam items.

## Questions

### 1. A conversation summary rounds a verified invoice amount into 'about a hundred.' What state should preserve the exact value?

Domain: Prompt and Context Engineering

- A. Supply the relevant conversation state on subsequent requests
- B. Preserve exact transactional facts outside lossy summaries
- C. Compact context while preserving checked facts and open issues
- D. Present key findings early and organize supporting details

### 2. A stateless follow-up loses the user's earlier correction because it is absent from the request. What should the application supply?

Domain: Prompt and Context Engineering

- A. Pass relevant evidence and constraints explicitly
- B. Resume the identified session when its context remains valid
- C. Persist structured task state and pending actions
- D. Supply the relevant conversation state on subsequent requests

### 3. A tool returns a verbose object whose irrelevant fields repeatedly fill context. What should change upstream?

Domain: Prompt and Context Engineering

- A. Compact context while preserving checked facts and open issues
- B. Reduce tool output to relevant fields with provenance
- C. Present key findings early and organize supporting details
- D. Preserve exact transactional facts outside lossy summaries

### 4. A fresh worker lacks a key restriction only discussed in the parent conversation. What should delegation provide?

Domain: Prompt and Context Engineering

- A. Enable the version-appropriate subagent invocation tool
- B. Supply the relevant conversation state on subsequent requests
- C. Configure the subagent description, prompt, and tool scope
- D. Pass relevant evidence and constraints explicitly

### 5. Exploratory history is long, but its conclusions can be preserved accurately in less space. What operation may help?

Domain: Prompt and Context Engineering

- A. Compact context while preserving checked facts and open issues
- B. Reduce tool output to relevant fields with provenance
- C. Use supported prompt-prefix caching for eligible repeated input
- D. Present key findings early and organize supporting details

### 6. Instructions, tools, source text, and output compete for limited capacity. What design is needed?

Domain: Prompt and Context Engineering

- A. Reduce tool output to relevant fields with provenance
- B. Budget instructions, evidence, history, and generation together
- C. Use supported prompt-prefix caching for eligible repeated input
- D. Compact context while preserving checked facts and open issues

### 7. A support session involves several orders with different statuses. What state should keep them distinct?

Domain: Prompt and Context Engineering

- A. Supply the relevant conversation state on subsequent requests
- B. Preserve exact transactional facts outside lossy summaries
- C. Compact context while preserving checked facts and open issues
- D. Present key findings early and organize supporting details

### 8. Important findings are lost within a long unstructured aggregation. What presentation can mitigate this?

Domain: Prompt and Context Engineering

- A. Compact context while preserving checked facts and open issues
- B. Preserve exact transactional facts outside lossy summaries
- C. Reduce tool output to relevant fields with provenance
- D. Present key findings early and organize supporting details

### 9. A long coding conversation starts citing typical patterns instead of real discovered files. What persistence may anchor it?

Domain: Prompt and Context Engineering

- A. Compact context while preserving checked facts and open issues
- B. Persist concise codebase findings with file and symbol pointers
- C. Persist structured task state and pending actions
- D. Supply the relevant conversation state on subsequent requests

### 10. Only a few source files changed after an otherwise useful analysis. What should the resumed agent receive?

Domain: Prompt and Context Engineering

- A. Tell the resumed agent what changed and recheck affected evidence
- B. Resume the identified session when its context remains valid
- C. Start a fresh session with a checked structured summary
- D. Compact context while preserving checked facts and open issues

### 11. A worker receives the entire repository but only needs to trace one route. What delegation boundary helps?

Domain: Prompt and Context Engineering

- A. Delegate a focused codebase question with a bounded output
- B. Map the problem and revise subtasks as evidence emerges
- C. Assign distinct scopes and explicit coverage responsibilities
- D. Delegate focused exploration to a read-oriented subagent

### 12. Most earlier tool observations are obsolete after a major redesign. What context strategy fits?

Domain: Prompt and Context Engineering

- A. Tell the resumed agent what changed and recheck affected evidence
- B. Compact context while preserving checked facts and open issues
- C. Resume the identified session when its context remains valid
- D. Start a fresh session with a checked structured summary

### 13. A crash leaves several worker artifacts whose validation status differs. What should recovery consult?

Domain: Prompt and Context Engineering

- A. Persist structured task state and pending actions
- B. Resume the identified session when its context remains valid
- C. Resume from a checked manifest of worker states and artifacts
- D. Persist concise codebase findings with file and symbol pointers

### 14. A synthesis summary keeps conclusions but loses which source supports each claim. What should be preserved?

Domain: Prompt and Context Engineering

- A. Represent credible disagreement with attributed values
- B. Preserve claim-to-source mappings through every handoff
- C. Use representations suited to the content type
- D. Preserve collection and publication dates with claims

### 15. Two statistics appear contradictory because their measurement periods were removed during summarization. What metadata is needed?

Domain: Prompt and Context Engineering

- A. Preserve claim-to-source mappings through every handoff
- B. Represent credible disagreement with attributed values
- C. Use representations suited to the content type
- D. Preserve collection and publication dates with claims

### 16. Credible sources disagree, and the summary chooses one value without explanation. What output should preserve uncertainty?

Domain: Prompt and Context Engineering

- A. Represent credible disagreement with attributed values
- B. Preserve claim-to-source mappings through every handoff
- C. Preserve collection and publication dates with claims
- D. Use representations suited to the content type

### 17. A developer wants a larger context window by enabling prefix caching. What optimization is actually being configured?

Domain: Prompt and Context Engineering

- A. Reduce tool output to relevant fields with provenance
- B. Budget instructions, evidence, history, and generation together
- C. Compact context while preserving checked facts and open issues
- D. Use supported prompt-prefix caching for eligible repeated input

### 18. A downstream agent needs facts and citations, but upstream sends pages of exploratory reasoning. What output should be reduced?

Domain: Prompt and Context Engineering

- A. Preserve exact transactional facts outside lossy summaries
- B. Reduce tool output to relevant fields with provenance
- C. Present key findings early and organize supporting details
- D. Compact context while preserving checked facts and open issues

### 19. A specialist starts fresh and is told only to 'continue what we discussed.' What should be supplied?

Domain: Prompt and Context Engineering

- A. Pass relevant evidence and constraints explicitly
- B. Persist structured task state and pending actions
- C. Supply the relevant conversation state on subsequent requests
- D. Configure the subagent description, prompt, and tool scope

### 20. A deadline becomes 'later this month' in progressive summaries. What should remain exact?

Domain: Prompt and Context Engineering

- A. Supply the relevant conversation state on subsequent requests
- B. Compact context while preserving checked facts and open issues
- C. Preserve exact transactional facts outside lossy summaries
- D. Present key findings early and organize supporting details

### 21. A source packet exceeds the documented request limit. What should govern selection and reservation?

Domain: Prompt and Context Engineering

- A. Reduce tool output to relevant fields with provenance
- B. Compact context while preserving checked facts and open issues
- C. Budget instructions, evidence, history, and generation together
- D. Use supported token counting before oversized submission

### 22. A relevant source belongs to another user's restricted workspace. What must happen before insertion into context?

Domain: Prompt and Context Engineering

- A. Apply requester permissions before evidence enters model context
- B. Reduce tool output to relevant fields with provenance
- C. Compact context while preserving checked facts and open issues
- D. Treat retrieved instructions as untrusted source content

### 23. A source passage claims it is a new trusted developer instruction. How should context represent it?

Domain: Prompt and Context Engineering

- A. Present key findings early and organize supporting details
- B. Apply requester permissions before evidence enters model context
- C. Compact context while preserving checked facts and open issues
- D. Treat retrieved instructions as untrusted source content

### 24. An application persists memory by reloading stored verified preferences into new requests. What capability is supplying continuity?

Domain: Prompt and Context Engineering

- A. Resume the identified session when its context remains valid
- B. Supply the relevant conversation state on subsequent requests
- C. Pass relevant evidence and constraints explicitly
- D. Persist structured task state and pending actions

### 25. Compaction removes an unresolved question that later work depends on. What should its design preserve?

Domain: Prompt and Context Engineering

- A. Present key findings early and organize supporting details
- B. Reduce tool output to relevant fields with provenance
- C. Compact context while preserving checked facts and open issues
- D. Preserve exact transactional facts outside lossy summaries

### 26. A later query needs the exact helper discovered much earlier. What saved note should make verification efficient?

Domain: Prompt and Context Engineering

- A. Resume from a checked manifest of worker states and artifacts
- B. Resume the identified session when its context remains valid
- C. Persist structured task state and pending actions
- D. Persist concise codebase findings with file and symbol pointers

### 27. A multi-stage pipeline passes findings without restrictions and later violates the user's scope. What handoff content is missing?

Domain: Prompt and Context Engineering

- A. Configure the subagent description, prompt, and tool scope
- B. Route coordination through an orchestrator
- C. Enable the version-appropriate subagent invocation tool
- D. Pass relevant evidence and constraints explicitly

### 28. A long report contains all evidence but no clear required-outcome overview. What arrangement can help?

Domain: Prompt and Context Engineering

- A. Present key findings early and organize supporting details
- B. Preserve exact transactional facts outside lossy summaries
- C. Compact context while preserving checked facts and open issues
- D. Reduce tool output to relevant fields with provenance

### 29. A report has a bibliography but no link from claims to specific passages. What evidence structure is needed?

Domain: Prompt and Context Engineering

- A. Use representations suited to the content type
- B. Preserve claim-to-source mappings through every handoff
- C. Represent credible disagreement with attributed values
- D. Preserve collection and publication dates with claims

### 30. A stored summary is mostly based on invalidated assumptions. What should replace blind reuse?

Domain: Prompt and Context Engineering

- A. Start a fresh session with a checked structured summary
- B. Tell the resumed agent what changed and recheck affected evidence
- C. Compact context while preserving checked facts and open issues
- D. Resume the identified session when its context remains valid

### 31. A review prompt says only 'be careful' and produces inconsistent findings. What should be stated?

Domain: Prompt and Context Engineering

- A. Define severity using impact and concrete examples
- B. Use representative few-shot examples with boundaries
- C. State explicit reportable and non-reportable criteria
- D. Temporarily disable a noisy category while repairing and evaluating it

### 32. Answers are accurate but far too advanced for the intended audience. What prompt requirement should change?

Domain: Prompt and Context Engineering

- A. Use representative few-shot examples with boundaries
- B. Assign a relevant role or perspective in the prompt
- C. Specify task, audience, constraints, and output expectations
- D. Set a supported maximum generated-output length

### 33. A custom API app needs trusted behavioral policy separate from user data. What instruction placement fits?

Domain: Prompt and Context Engineering

- A. Put shared project standards in versioned CLAUDE.md
- B. Build a valid Messages API request with explicit content blocks
- C. Place trusted application policy in the supported system instruction field
- D. Put personal cross-project preferences in ~/.claude/CLAUDE.md

### 34. Source prose and task instructions are mixed together without role boundaries. What prompt organization helps?

Domain: Prompt and Context Engineering

- A. Treat retrieved instructions as untrusted source content
- B. Pass relevant evidence and constraints explicitly
- C. Place trusted application policy in the supported system instruction field
- D. Separate instructions and source data with explicit labels

### 35. Detailed instructions alone do not yield consistent complete finding records. What can demonstrate the desired pattern?

Domain: Prompt and Context Engineering

- A. Include valid examples that should not be flagged
- B. Provide a task instruction without demonstrations
- C. Use representative few-shot examples with boundaries
- D. State explicit reportable and non-reportable criteria

### 36. A reviewer flags safe local patterns because examples only show defects. What should the examples include?

Domain: Prompt and Context Engineering

- A. Include valid examples that should not be flagged
- B. Define severity using impact and concrete examples
- C. State explicit reportable and non-reportable criteria
- D. Use representative few-shot examples with boundaries

### 37. A conversion must treat absent, null, and blank values differently. What can clarify intent?

Domain: Prompt and Context Engineering

- A. Specify deterministic normalization rules and preserve originals when needed
- B. Provide concrete input–output examples
- C. State explicit reportable and non-reportable criteria
- D. Validate extracted values against evidence and business rules

### 38. A confidently true cosmetic observation is labeled critical. What should the rubric distinguish?

Domain: Prompt and Context Engineering

- A. Calibrate field-confidence thresholds against labeled examples
- B. Record detected_pattern and dismissal reasons
- C. State explicit reportable and non-reportable criteria
- D. Define severity using impact and concrete examples

### 39. Several prompt edits occur without records and a regression cannot be attributed. What practice helps?

Domain: Prompt and Context Engineering

- A. Separate environment configuration from application logic
- B. Pin compatible model, SDK, prompt, and dependency versions
- C. Version exact prompt content and its dependencies
- D. Use a versioned representative held-out evaluation set

### 40. A new prompt works only on examples its author used while tuning. What evidence is needed?

Domain: Prompt and Context Engineering

- A. Use representative few-shot examples with boundaries
- B. State explicit reportable and non-reportable criteria
- C. Use a versioned representative held-out evaluation set
- D. Include valid examples that should not be flagged

### 41. Extraction examples show tables only, but production often uses narrative descriptions. What should be broadened?

Domain: Prompt and Context Engineering

- A. Use representative few-shot examples with boundaries
- B. State explicit reportable and non-reportable criteria
- C. Specify deterministic normalization rules and preserve originals when needed
- D. Provide a task instruction without demonstrations

### 42. A task request leaves material design constraints unspecified. What interaction should precede implementation?

Domain: Prompt and Context Engineering

- A. State explicit reportable and non-reportable criteria
- B. Provide concrete input–output examples
- C. Use tests and specific failure feedback to drive iteration
- D. Ask targeted design questions before implementation

### 43. Two revisions affect the same state transition and cannot be fixed independently. How should feedback be supplied?

Domain: Prompt and Context Engineering

- A. Wait for validated prerequisite outputs
- B. Explain interacting issues together before revising
- C. Provide concrete input–output examples
- D. Run independent branches concurrently and join checked results

### 44. A task benefits from extracting facts first and drafting only from checked extraction. What prompt pattern fits?

Domain: Prompt and Context Engineering

- A. Break the task into linked checked prompt stages
- B. Provide a task instruction without demonstrations
- C. Provide one representative demonstration
- D. Assign a relevant role or perspective in the prompt

### 45. A team wants bugs reported but harmless formatting ignored. What should the prompt define?

Domain: Prompt and Context Engineering

- A. Temporarily disable a noisy category while repairing and evaluating it
- B. State explicit reportable and non-reportable criteria
- C. Use representative few-shot examples with boundaries
- D. Include valid examples that should not be flagged

### 46. A requested answer should be a short comparison table, but output is a long essay. What should be specified?

Domain: Prompt and Context Engineering

- A. Specify task, audience, constraints, and output expectations
- B. Set a supported maximum generated-output length
- C. Use representative few-shot examples with boundaries
- D. Assign a relevant role or perspective in the prompt

### 47. An external report contains sentences resembling application instructions. What prompt structure reduces confusion?

Domain: Prompt and Context Engineering

- A. Pass relevant evidence and constraints explicitly
- B. Treat retrieved instructions as untrusted source content
- C. Separate instructions and source data with explicit labels
- D. Place trusted application policy in the supported system instruction field

### 48. A demonstration set teaches that every unfamiliar API use is defective. What addition improves the boundary?

Domain: Prompt and Context Engineering

- A. Include valid examples that should not be flagged
- B. Use representative few-shot examples with boundaries
- C. State explicit reportable and non-reportable criteria
- D. Provide concrete input–output examples

### 49. A release includes the same model but changed prompt instructions. What should identify the behavioral change?

Domain: Prompt and Context Engineering

- A. Pin compatible model, SDK, prompt, and dependency versions
- B. Use a versioned representative held-out evaluation set
- C. Separate environment configuration from application logic
- D. Version exact prompt content and its dependencies

### 50. A prompt asks for only 'high-confidence' warnings without defining a defect. What should replace that ambiguity?

Domain: Prompt and Context Engineering

- A. State explicit reportable and non-reportable criteria
- B. Record detected_pattern and dismissal reasons
- C. Define severity using impact and concrete examples
- D. Calibrate field-confidence thresholds against labeled examples

### 51. A label convention remains inconsistent despite prose guidance. What can demonstrate exact desired labeling?

Domain: Prompt and Context Engineering

- A. State explicit reportable and non-reportable criteria
- B. Provide a task instruction without demonstrations
- C. Use representative few-shot examples with boundaries
- D. Include valid examples that should not be flagged

### 52. A revision fails a reproducible edge case. What feedback should drive correction?

Domain: Prompt and Context Engineering

- A. Ask targeted design questions before implementation
- B. Provide concrete input–output examples
- C. Use tests and specific failure feedback to drive iteration
- D. State explicit reportable and non-reportable criteria

### 53. A developer asks for 'safe retry' but has not specified whether side effects can repeat. What should be clarified?

Domain: Prompt and Context Engineering

- A. Provide concrete input–output examples
- B. Use tests and specific failure feedback to drive iteration
- C. Ask targeted design questions before implementation
- D. Use plan mode to investigate and compare approaches

### 54. Review outputs include speculative complaints unrelated to requested behavior. What should narrow them?

Domain: Prompt and Context Engineering

- A. State explicit reportable and non-reportable criteria
- B. Use representative few-shot examples with boundaries
- C. Define severity using impact and concrete examples
- D. Include valid examples that should not be flagged

### 55. An extractor misreads informal measurements that differ from formal table notation. What demonstration helps?

Domain: Prompt and Context Engineering

- A. Provide concrete input–output examples
- B. Validate extracted values against evidence and business rules
- C. Specify deterministic normalization rules and preserve originals when needed
- D. Provide a task instruction without demonstrations

### 56. A valid exception resembles a risky pattern and is repeatedly flagged. What instructional evidence is useful?

Domain: Prompt and Context Engineering

- A. Use representative few-shot examples with boundaries
- B. Include valid examples that should not be flagged
- C. State explicit reportable and non-reportable criteria
- D. Record detected_pattern and dismissal reasons

### 57. A team wants to compare two prompt revisions fairly. What should be recorded?

Domain: Prompt and Context Engineering

- A. Separate environment configuration from application logic
- B. Version exact prompt content and its dependencies
- C. Pin compatible model, SDK, prompt, and dependency versions
- D. Use a versioned representative held-out evaluation set

### 58. A model must mention uncertainty when approved evidence is insufficient. What prompt design should include that behavior?

Domain: Prompt and Context Engineering

- A. Use representative few-shot examples with boundaries
- B. Specify task, audience, constraints, and output expectations
- C. Assign a relevant role or perspective in the prompt
- D. State explicit reportable and non-reportable criteria

### 59. An API developer copies a CLI instruction-file convention and expects the API to load it automatically. What placement is required?

Domain: Prompt and Context Engineering

- A. Build a valid Messages API request with explicit content blocks
- B. Put personal cross-project preferences in ~/.claude/CLAUDE.md
- C. Place trusted application policy in the supported system instruction field
- D. Put shared project standards in versioned CLAUDE.md

### 60. A prompt change reduces one failure but creates new errors on required cases. What should evaluate it?

Domain: Prompt and Context Engineering

- A. Include valid examples that should not be flagged
- B. Use representative few-shot examples with boundaries
- C. State explicit reportable and non-reportable criteria
- D. Use a versioned representative held-out evaluation set

### 61. A downstream consumer needs a supported schema-constrained object. What output mechanism addresses structural validity?

Domain: Prompt and Context Engineering

- A. Validate extracted values against evidence and business rules
- B. Use supported strict structured output with a schema
- C. Allow explicit unknown or absent values in the schema
- D. Specify deterministic normalization rules and preserve originals when needed

### 62. A valid structured object puts the customer's amount in the supplier's field. What validation is still needed?

Domain: Prompt and Context Engineering

- A. Specify deterministic normalization rules and preserve originals when needed
- B. Allow explicit unknown or absent values in the schema
- C. Use supported strict structured output with a schema
- D. Validate extracted values against evidence and business rules

### 63. A document never states a required business fact. What schema design avoids forcing fabrication?

Domain: Prompt and Context Engineering

- A. Specify deterministic normalization rules and preserve originals when needed
- B. Allow explicit unknown or absent values in the schema
- C. Use supported strict structured output with a schema
- D. Use an extensible category plus a detail field

### 64. A known valid category falls outside the enumerated list. What extensible representation fits?

Domain: Prompt and Context Engineering

- A. Allow explicit unknown or absent values in the schema
- B. Specify deterministic normalization rules and preserve originals when needed
- C. Use supported strict structured output with a schema
- D. Use an extensible category plus a detail field

### 65. Sources mix units while the output contract expects one normalized representation. What should guide conversion?

Domain: Prompt and Context Engineering

- A. Use supported strict structured output with a schema
- B. Validate extracted values against evidence and business rules
- C. Specify deterministic normalization rules and preserve originals when needed
- D. Allow explicit unknown or absent values in the schema

### 66. An object has valid numbers, but extracted quantities contradict the source. What must acceptance verify?

Domain: Prompt and Context Engineering

- A. Validate extracted values against evidence and business rules
- B. Specify deterministic normalization rules and preserve originals when needed
- C. Compare independently calculated and source-stated totals
- D. Use supported strict structured output with a schema

### 67. A key must exist, but its value may genuinely be unknown. What schema distinction matters?

Domain: Prompt and Context Engineering

- A. Specify deterministic normalization rules and preserve originals when needed
- B. Use an extensible category plus a detail field
- C. Allow explicit unknown or absent values in the schema
- D. Use supported strict structured output with a schema

### 68. A schema-valid object contains a dangerous shell fragment in a string. What boundary should protect execution?

Domain: Prompt and Context Engineering

- A. Treat model output as untrusted before rendering or execution
- B. Use supported strict structured output with a schema
- C. Validate extracted values against evidence and business rules
- D. Adjust sampling variability, not factual truth

### 69. A parser consumes streaming fragments as final records before completion. What should it inspect first?

Domain: Prompt and Context Engineering

- A. Accumulate deltas by block index before final validation
- B. Dispatch response content according to each block type
- C. Use the final assembled message and completion status
- D. Use supported strict structured output with a schema

### 70. Output ends mid-object due to the generation limit. What state must handling recognize?

Domain: Prompt and Context Engineering

- A. Treat end_turn as the end of the current assistant turn
- B. Handle the output limit as an incomplete response
- C. Inspect stop_reason and dispatch the appropriate branch
- D. Use the final assembled message and completion status

### 71. The source contains the fact, but extraction placed it in the wrong field. What correction input is useful?

Domain: Prompt and Context Engineering

- A. Use supported strict structured output with a schema
- B. Allow explicit unknown or absent values in the schema
- C. Mark missing evidence and route for retrieval or review
- D. Retry with the document, failed result, and specific validation errors

### 72. Repeated retries invent a value that is absent from the provided evidence. What should replace them?

Domain: Prompt and Context Engineering

- A. Use supported strict structured output with a schema
- B. Allow explicit unknown or absent values in the schema
- C. Retry with the document, failed result, and specific validation errors
- D. Mark missing evidence and route for retrieval or review

### 73. Line items and a source-stated total disagree. What extraction design preserves the discrepancy?

Domain: Prompt and Context Engineering

- A. Validate extracted values against evidence and business rules
- B. Compare independently calculated and source-stated totals
- C. Specify deterministic normalization rules and preserve originals when needed
- D. Use supported strict structured output with a schema

### 74. Two source sections provide incompatible values and neither is clearly authoritative. What should the output retain?

Domain: Prompt and Context Engineering

- A. Preserve conflicting source values with an explicit flag
- B. Use an extensible category plus a detail field
- C. Compare independently calculated and source-stated totals
- D. Allow explicit unknown or absent values in the schema

### 75. A self-correction loop makes endless calls on one unfixable record. What safeguard is needed?

Domain: Prompt and Context Engineering

- A. Enforce task, iteration, and spending safeguards
- B. Retry with the document, failed result, and specific validation errors
- C. Use supported strict structured output with a schema
- D. Mark missing evidence and route for retrieval or review

### 76. A corrected response now parses but silently changes a previously verified identifier. What should the loop do?

Domain: Prompt and Context Engineering

- A. Validate extracted values against evidence and business rules
- B. Use supported strict structured output with a schema
- C. Specify deterministic normalization rules and preserve originals when needed
- D. Allow explicit unknown or absent values in the schema

### 77. A repair request omits the original document and gives only 'wrong answer.' What evidence should be restored?

Domain: Prompt and Context Engineering

- A. Specify deterministic normalization rules and preserve originals when needed
- B. Mark missing evidence and route for retrieval or review
- C. Retry with the document, failed result, and specific validation errors
- D. Use supported strict structured output with a schema

### 78. A requested detail exists only in a missing attachment. What handling should replace repeated correction attempts?

Domain: Prompt and Context Engineering

- A. Use supported strict structured output with a schema
- B. Allow explicit unknown or absent values in the schema
- C. Retry with the document, failed result, and specific validation errors
- D. Mark missing evidence and route for retrieval or review

### 79. An extractor silently picks one of two incompatible dates. What should its output make explicit?

Domain: Prompt and Context Engineering

- A. Compare independently calculated and source-stated totals
- B. Use an extensible category plus a detail field
- C. Preserve conflicting source values with an explicit flag
- D. Allow explicit unknown or absent values in the schema

### 80. A structured date string is valid but belongs to a different event. What should be checked?

Domain: Prompt and Context Engineering

- A. Use supported strict structured output with a schema
- B. Specify deterministic normalization rules and preserve originals when needed
- C. Validate extracted values against evidence and business rules
- D. Allow explicit unknown or absent values in the schema

### 81. A generated filename includes a path traversal sequence. What should protect the destination?

Domain: Prompt and Context Engineering

- A. Adjust sampling variability, not factual truth
- B. Treat model output as untrusted before rendering or execution
- C. Validate extracted values against evidence and business rules
- D. Use supported strict structured output with a schema

### 82. A model assigns 99% confidence without any labeled validation. What must precede automated trust?

Domain: Prompt and Context Engineering

- A. Evaluate accuracy by document type and field segment
- B. Calibrate field-confidence thresholds against labeled examples
- C. Sample high-confidence outputs within relevant strata
- D. Route ambiguous, conflicting, or high-risk cases to qualified review

### 83. Evidence is contradictory and the result could cause serious harm. What handling should override an impressive confidence score?

Domain: Prompt and Context Engineering

- A. Sample high-confidence outputs within relevant strata
- B. Evaluate accuracy by document type and field segment
- C. Route ambiguous, conflicting, or high-risk cases to qualified review
- D. Calibrate field-confidence thresholds against labeled examples

### 84. Aggregate extraction accuracy is high but one required field is poor on rare layouts. What analysis is needed?

Domain: Prompt and Context Engineering

- A. Sample high-confidence outputs within relevant strata
- B. Route ambiguous, conflicting, or high-risk cases to qualified review
- C. Evaluate accuracy by document type and field segment
- D. Calibrate field-confidence thresholds against labeled examples

### 85. A generated claim cites an existing page that does not support it. What linkage must be verified?

Domain: Prompt and Context Engineering

- A. Preserve collection and publication dates with claims
- B. Preserve claim-to-source mappings through every handoff
- C. Represent credible disagreement with attributed values
- D. Use representations suited to the content type

### 86. Approved context does not support a consequential answer. What output policy is preferable to guessing?

Domain: Prompt and Context Engineering

- A. Validate extracted values against evidence and business rules
- B. Route ambiguous, conflicting, or high-risk cases to qualified review
- C. State insufficient evidence or use an approved escalation path
- D. Allow explicit unknown or absent values in the schema

### 87. The raw model object is correct but the application parser swaps fields. What source of error should be isolated?

Domain: Prompt and Context Engineering

- A. Isolate model-output defects from integration defects
- B. Use supported strict structured output with a schema
- C. Validate extracted values against evidence and business rules
- D. Inspect a redacted end-to-end request and tool trace

### 88. The team needs to identify recurring false-positive output constructs. What diagnostic metadata helps?

Domain: Prompt and Context Engineering

- A. Record detected_pattern and dismissal reasons
- B. Temporarily disable a noisy category while repairing and evaluating it
- C. State explicit reportable and non-reportable criteria
- D. Define severity using impact and concrete examples

### 89. A generator repeatedly approves its own flawed assumption in the same context. What review setup may help?

Domain: Prompt and Context Engineering

- A. Calibrate field-confidence thresholds against labeled examples
- B. Separate local analysis from cross-file integration review
- C. State explicit reportable and non-reportable criteria
- D. Use an independent reviewer without the generator rationale

### 90. High-confidence results bypass review, so confident mistakes remain invisible. What ongoing check should be added?

Domain: Prompt and Context Engineering

- A. Route ambiguous, conflicting, or high-risk cases to qualified review
- B. Sample high-confidence outputs within relevant strata
- C. Evaluate accuracy by document type and field segment
- D. Calibrate field-confidence thresholds against labeled examples

### 91. A developer assumes saying 'JSON only' enforces an exact supported field schema. What mechanism addresses that requirement?

Domain: Prompt and Context Engineering

- A. Specify deterministic normalization rules and preserve originals when needed
- B. Validate extracted values against evidence and business rules
- C. Allow explicit unknown or absent values in the schema
- D. Use supported strict structured output with a schema

### 92. A response includes the correct quantity but the wrong measurement unit. What must acceptance verify?

Domain: Prompt and Context Engineering

- A. Specify deterministic normalization rules and preserve originals when needed
- B. Allow explicit unknown or absent values in the schema
- C. Use supported strict structured output with a schema
- D. Validate extracted values against evidence and business rules

### 93. A downstream record must distinguish genuinely unknown information from a known uncatalogued category. What missing-value design is relevant?

Domain: Prompt and Context Engineering

- A. Use an extensible category plus a detail field
- B. Allow explicit unknown or absent values in the schema
- C. Use supported strict structured output with a schema
- D. Specify deterministic normalization rules and preserve originals when needed

### 94. A valid new category has a clear source description but is absent from a fixed list. What extensible pattern preserves it?

Domain: Prompt and Context Engineering

- A. Specify deterministic normalization rules and preserve originals when needed
- B. Use an extensible category plus a detail field
- C. Use supported strict structured output with a schema
- D. Allow explicit unknown or absent values in the schema

### 95. A model-generated string is inserted into an HTML attribute without encoding. What boundary principle should apply?

Domain: Prompt and Context Engineering

- A. Treat model output as untrusted before rendering or execution
- B. Adjust sampling variability, not factual truth
- C. Use supported strict structured output with a schema
- D. Validate extracted values against evidence and business rules

### 96. A value exists in the source but was assigned to the wrong account field. What repair context is useful?

Domain: Prompt and Context Engineering

- A. Mark missing evidence and route for retrieval or review
- B. Allow explicit unknown or absent values in the schema
- C. Retry with the document, failed result, and specific validation errors
- D. Use supported strict structured output with a schema

### 97. A user asks for a source fact that the available evidence never contained. What response handling is appropriate?

Domain: Prompt and Context Engineering

- A. Use representative few-shot examples with boundaries
- B. Retry with the document, failed result, and specific validation errors
- C. Use supported strict structured output with a schema
- D. Mark missing evidence and route for retrieval or review

### 98. The source states incompatible amounts in two authoritative-looking sections. What should extraction preserve?

Domain: Prompt and Context Engineering

- A. Use supported strict structured output with a schema
- B. Compare independently calculated and source-stated totals
- C. Validate extracted values against evidence and business rules
- D. Preserve conflicting source values with an explicit flag

### 99. A parser receives an incomplete streamed object before its block closes. What should govern final consumption?

Domain: Prompt and Context Engineering

- A. Use the final assembled message and completion status
- B. Dispatch response content according to each block type
- C. Accumulate deltas by block index before final validation
- D. Use supported strict structured output with a schema

### 100. A schema-compliant output is fluent and confident but contradicts approved evidence. What validation must remain skeptical?

Domain: Prompt and Context Engineering

- A. Allow explicit unknown or absent values in the schema
- B. Use supported strict structured output with a schema
- C. Specify deterministic normalization rules and preserve originals when needed
- D. Validate extracted values against evidence and business rules

---

## Answer key and explanations

### Question 1 — B

Answer: Preserve exact transactional facts outside lossy summaries. Keep verified transactional facts outside lossy prose summaries for later decisions. Keep verified amounts, identifiers, dates, and commitments in structured state. General summaries can omit details that later decisions depend on. Local study-map skill 6.1 (Context Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. In this case: Keep verified transactional facts outside lossy prose summaries for later decisions.
- **B:** Correct. Keep verified amounts, identifiers, dates, and commitments in structured state. General summaries can omit details that later decisions depend on. In this case: Keep verified transactional facts outside lossy prose summaries for later decisions.
- **C:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Keep verified transactional facts outside lossy prose summaries for later decisions.
- **D:** Incorrect for this question. A structured overview and clear sections help reduce long-input position effects. Placement is a mitigation, not proof that every fact will be used. In this case: Keep verified transactional facts outside lossy prose summaries for later decisions.

### Question 2 — D

Answer: Supply the relevant conversation state on subsequent requests. Include relevant conversation state or an accurate checked representation explicitly. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. Local study-map skill 6.1 (Context Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Include relevant conversation state or an accurate checked representation explicitly.
- **B:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Include relevant conversation state or an accurate checked representation explicitly.
- **C:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Include relevant conversation state or an accurate checked representation explicitly.
- **D:** Correct. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. In this case: Include relevant conversation state or an accurate checked representation explicitly.

### Question 3 — B

Answer: Reduce tool output to relevant fields with provenance. Reduce observations to high-signal fields while preserving decision evidence and provenance. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. Local study-map skill 6.1 (Context Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Reduce observations to high-signal fields while preserving decision evidence and provenance.
- **B:** Correct. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: Reduce observations to high-signal fields while preserving decision evidence and provenance.
- **C:** Incorrect for this question. A structured overview and clear sections help reduce long-input position effects. Placement is a mitigation, not proof that every fact will be used. In this case: Reduce observations to high-signal fields while preserving decision evidence and provenance.
- **D:** Incorrect for this question. Keep verified amounts, identifiers, dates, and commitments in structured state. General summaries can omit details that later decisions depend on. In this case: Reduce observations to high-signal fields while preserving decision evidence and provenance.

### Question 4 — D

Answer: Pass relevant evidence and constraints explicitly. Relevant restrictions and evidence should be passed explicitly rather than assumed inherited. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. Local study-map skill 6.1 (Context Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Delegation requires a permitted launcher under the installed SDK contract. Check Agent versus legacy Task identifiers rather than assume all versions accept the same names. In this case: Relevant restrictions and evidence should be passed explicitly rather than assumed inherited.
- **B:** Incorrect for this question. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. In this case: Relevant restrictions and evidence should be passed explicitly rather than assumed inherited.
- **C:** Incorrect for this question. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: Relevant restrictions and evidence should be passed explicitly rather than assumed inherited.
- **D:** Correct. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Relevant restrictions and evidence should be passed explicitly rather than assumed inherited.

### Question 5 — A

Answer: Compact context while preserving checked facts and open issues. Compact checked findings while retaining exact critical facts and unresolved issues separately. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. Local study-map skill 6.1 (Context Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Correct. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Compact checked findings while retaining exact critical facts and unresolved issues separately.
- **B:** Incorrect for this question. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: Compact checked findings while retaining exact critical facts and unresolved issues separately.
- **C:** Incorrect for this question. Caching may reduce repeated prefix processing under provider-specific rules. It does not extend the context window, update model weights, or verify an answer. In this case: Compact checked findings while retaining exact critical facts and unresolved issues separately.
- **D:** Incorrect for this question. A structured overview and clear sections help reduce long-input position effects. Placement is a mitigation, not proof that every fact will be used. In this case: Compact checked findings while retaining exact critical facts and unresolved issues separately.

### Question 6 — B

Answer: Budget instructions, evidence, history, and generation together. Budget all relevant content under the selected model and service rules. Follow the chosen model and service limits. Overflow handling varies; it is not universally automatic oldest-message deletion. Local study-map skill 6.1 (Context Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: Budget all relevant content under the selected model and service rules.
- **B:** Correct. Follow the chosen model and service limits. Overflow handling varies; it is not universally automatic oldest-message deletion. In this case: Budget all relevant content under the selected model and service rules.
- **C:** Incorrect for this question. Caching may reduce repeated prefix processing under provider-specific rules. It does not extend the context window, update model weights, or verify an answer. In this case: Budget all relevant content under the selected model and service rules.
- **D:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Budget all relevant content under the selected model and service rules.

### Question 7 — B

Answer: Preserve exact transactional facts outside lossy summaries. Structured per-issue facts prevent identifiers and attributes from merging into vague narration. Keep verified amounts, identifiers, dates, and commitments in structured state. General summaries can omit details that later decisions depend on. Local study-map skill 6.1 (Context Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. In this case: Structured per-issue facts prevent identifiers and attributes from merging into vague narration.
- **B:** Correct. Keep verified amounts, identifiers, dates, and commitments in structured state. General summaries can omit details that later decisions depend on. In this case: Structured per-issue facts prevent identifiers and attributes from merging into vague narration.
- **C:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Structured per-issue facts prevent identifiers and attributes from merging into vague narration.
- **D:** Incorrect for this question. A structured overview and clear sections help reduce long-input position effects. Placement is a mitigation, not proof that every fact will be used. In this case: Structured per-issue facts prevent identifiers and attributes from merging into vague narration.

### Question 8 — D

Answer: Present key findings early and organize supporting details. Provide a checked overview and explicit sections without claiming perfect position-based recall. A structured overview and clear sections help reduce long-input position effects. Placement is a mitigation, not proof that every fact will be used. Local study-map skill 6.1 (Context Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Provide a checked overview and explicit sections without claiming perfect position-based recall.
- **B:** Incorrect for this question. Keep verified amounts, identifiers, dates, and commitments in structured state. General summaries can omit details that later decisions depend on. In this case: Provide a checked overview and explicit sections without claiming perfect position-based recall.
- **C:** Incorrect for this question. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: Provide a checked overview and explicit sections without claiming perfect position-based recall.
- **D:** Correct. A structured overview and clear sections help reduce long-input position effects. Placement is a mitigation, not proof that every fact will be used. In this case: Provide a checked overview and explicit sections without claiming perfect position-based recall.

### Question 9 — B

Answer: Persist concise codebase findings with file and symbol pointers. Save concise verified findings with concrete file and symbol pointers. Durable notes counter context degradation and support later verification. Record source versions or change cues so notes are not mistaken for permanently current truth. Local study-map skill 6.1 (Context Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Save concise verified findings with concrete file and symbol pointers.
- **B:** Correct. Durable notes counter context degradation and support later verification. Record source versions or change cues so notes are not mistaken for permanently current truth. In this case: Save concise verified findings with concrete file and symbol pointers.
- **C:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Save concise verified findings with concrete file and symbol pointers.
- **D:** Incorrect for this question. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. In this case: Save concise verified findings with concrete file and symbol pointers.

### Question 10 — A

Answer: Tell the resumed agent what changed and recheck affected evidence. Explicitly identify changed evidence and request targeted revalidation of affected findings. Targeted re-analysis works when most prior context remains useful. Explicit change information prevents reliance on stale file or tool observations. Local study-map skill 6.1 (Context Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Correct. Targeted re-analysis works when most prior context remains useful. Explicit change information prevents reliance on stale file or tool observations. In this case: Explicitly identify changed evidence and request targeted revalidation of affected findings.
- **B:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Explicitly identify changed evidence and request targeted revalidation of affected findings.
- **C:** Incorrect for this question. A new context can avoid stale tool results when assumptions changed widely. Preserve verified facts, relevant constraints, and pointers rather than import all obsolete history. In this case: Explicitly identify changed evidence and request targeted revalidation of affected findings.
- **D:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Explicitly identify changed evidence and request targeted revalidation of affected findings.

### Question 11 — A

Answer: Delegate a focused codebase question with a bounded output. Ask a focused bounded question that returns useful evidence instead of exhaustive noise. A concrete question such as tracing one authorization path gives useful coverage with less irrelevant exploration than asking every worker to read everything. Local study-map skill 6.1 (Context Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Correct. A concrete question such as tracing one authorization path gives useful coverage with less irrelevant exploration than asking every worker to read everything. In this case: Ask a focused bounded question that returns useful evidence instead of exhaustive noise.
- **B:** Incorrect for this question. Open-ended investigation benefits from exploration, prioritized hypotheses, and revised decomposition rather than an exhaustive fixed script chosen before evidence. In this case: Ask a focused bounded question that returns useful evidence instead of exhaustive noise.
- **C:** Incorrect for this question. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. In this case: Ask a focused bounded question that returns useful evidence instead of exhaustive noise.
- **D:** Incorrect for this question. Discovery can be isolated so verbose file output does not overwhelm the main conversation. Return useful findings and source pointers. In this case: Ask a focused bounded question that returns useful evidence instead of exhaustive noise.

### Question 12 — D

Answer: Start a fresh session with a checked structured summary. Start from a checked current summary rather than import stale evidence wholesale. A new context can avoid stale tool results when assumptions changed widely. Preserve verified facts, relevant constraints, and pointers rather than import all obsolete history. Local study-map skill 6.1 (Context Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Targeted re-analysis works when most prior context remains useful. Explicit change information prevents reliance on stale file or tool observations. In this case: Start from a checked current summary rather than import stale evidence wholesale.
- **B:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Start from a checked current summary rather than import stale evidence wholesale.
- **C:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Start from a checked current summary rather than import stale evidence wholesale.
- **D:** Correct. A new context can avoid stale tool results when assumptions changed widely. Preserve verified facts, relevant constraints, and pointers rather than import all obsolete history. In this case: Start from a checked current summary rather than import stale evidence wholesale.

### Question 13 — C

Answer: Resume from a checked manifest of worker states and artifacts. A checked manifest distinguishes completed, partial, and pending work instead of guessing from filenames. Recovery needs known state locations, completion status, source versions, and pending work. Do not infer completion merely because an output file exists. Local study-map skill 6.1 (Context Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: A checked manifest distinguishes completed, partial, and pending work instead of guessing from filenames.
- **B:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: A checked manifest distinguishes completed, partial, and pending work instead of guessing from filenames.
- **C:** Correct. Recovery needs known state locations, completion status, source versions, and pending work. Do not infer completion merely because an output file exists. In this case: A checked manifest distinguishes completed, partial, and pending work instead of guessing from filenames.
- **D:** Incorrect for this question. Durable notes counter context degradation and support later verification. Record source versions or change cues so notes are not mistaken for permanently current truth. In this case: A checked manifest distinguishes completed, partial, and pending work instead of guessing from filenames.

### Question 14 — B

Answer: Preserve claim-to-source mappings through every handoff. Claim-to-source mappings must remain attached through every context transformation. Claims need traceable source identities, relevant excerpts, locations, and dates as applicable. A bibliography without claim mappings can lose attribution. Local study-map skill 6.1 (Context Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Do not average incompatible measurements or choose one arbitrarily. Preserve context and distinguish contested findings from established ones. In this case: Claim-to-source mappings must remain attached through every context transformation.
- **B:** Correct. Claims need traceable source identities, relevant excerpts, locations, and dates as applicable. A bibliography without claim mappings can lose attribution. In this case: Claim-to-source mappings must remain attached through every context transformation.
- **C:** Incorrect for this question. Tables can preserve financial comparisons, while prose and structured lists suit other needs. A single forced format can hide important structure. In this case: Claim-to-source mappings must remain attached through every context transformation.
- **D:** Incorrect for this question. Different measurement periods can explain apparent disagreements. Dates and methodology should remain attached rather than being stripped in summaries. In this case: Claim-to-source mappings must remain attached through every context transformation.

### Question 15 — D

Answer: Preserve collection and publication dates with claims. Preserve collection and publication dates with their claims and methodology. Different measurement periods can explain apparent disagreements. Dates and methodology should remain attached rather than being stripped in summaries. Local study-map skill 6.1 (Context Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Claims need traceable source identities, relevant excerpts, locations, and dates as applicable. A bibliography without claim mappings can lose attribution. In this case: Preserve collection and publication dates with their claims and methodology.
- **B:** Incorrect for this question. Do not average incompatible measurements or choose one arbitrarily. Preserve context and distinguish contested findings from established ones. In this case: Preserve collection and publication dates with their claims and methodology.
- **C:** Incorrect for this question. Tables can preserve financial comparisons, while prose and structured lists suit other needs. A single forced format can hide important structure. In this case: Preserve collection and publication dates with their claims and methodology.
- **D:** Correct. Different measurement periods can explain apparent disagreements. Dates and methodology should remain attached rather than being stripped in summaries. In this case: Preserve collection and publication dates with their claims and methodology.

### Question 16 — A

Answer: Represent credible disagreement with attributed values. Represent attributed disagreement instead of silently select a convenient figure. Do not average incompatible measurements or choose one arbitrarily. Preserve context and distinguish contested findings from established ones. Local study-map skill 6.1 (Context Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Correct. Do not average incompatible measurements or choose one arbitrarily. Preserve context and distinguish contested findings from established ones. In this case: Represent attributed disagreement instead of silently select a convenient figure.
- **B:** Incorrect for this question. Claims need traceable source identities, relevant excerpts, locations, and dates as applicable. A bibliography without claim mappings can lose attribution. In this case: Represent attributed disagreement instead of silently select a convenient figure.
- **C:** Incorrect for this question. Different measurement periods can explain apparent disagreements. Dates and methodology should remain attached rather than being stripped in summaries. In this case: Represent attributed disagreement instead of silently select a convenient figure.
- **D:** Incorrect for this question. Tables can preserve financial comparisons, while prose and structured lists suit other needs. A single forced format can hide important structure. In this case: Represent attributed disagreement instead of silently select a convenient figure.

### Question 17 — D

Answer: Use supported prompt-prefix caching for eligible repeated input. Caching reuses eligible processing; it does not expand model capacity. Caching may reduce repeated prefix processing under provider-specific rules. It does not extend the context window, update model weights, or verify an answer. Local study-map skill 6.1 (Context Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: Caching reuses eligible processing; it does not expand model capacity.
- **B:** Incorrect for this question. Follow the chosen model and service limits. Overflow handling varies; it is not universally automatic oldest-message deletion. In this case: Caching reuses eligible processing; it does not expand model capacity.
- **C:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Caching reuses eligible processing; it does not expand model capacity.
- **D:** Correct. Caching may reduce repeated prefix processing under provider-specific rules. It does not extend the context window, update model weights, or verify an answer. In this case: Caching reuses eligible processing; it does not expand model capacity.

### Question 18 — B

Answer: Reduce tool output to relevant fields with provenance. Return relevant structured evidence rather than unnecessary intermediate narrative. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. Local study-map skill 6.1 (Context Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Keep verified amounts, identifiers, dates, and commitments in structured state. General summaries can omit details that later decisions depend on. In this case: Return relevant structured evidence rather than unnecessary intermediate narrative.
- **B:** Correct. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: Return relevant structured evidence rather than unnecessary intermediate narrative.
- **C:** Incorrect for this question. A structured overview and clear sections help reduce long-input position effects. Placement is a mitigation, not proof that every fact will be used. In this case: Return relevant structured evidence rather than unnecessary intermediate narrative.
- **D:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Return relevant structured evidence rather than unnecessary intermediate narrative.

### Question 19 — A

Answer: Pass relevant evidence and constraints explicitly. Provide the relevant actual task context rather than rely on inaccessible prior conversation. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. Local study-map skill 6.1 (Context Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Correct. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Provide the relevant actual task context rather than rely on inaccessible prior conversation.
- **B:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Provide the relevant actual task context rather than rely on inaccessible prior conversation.
- **C:** Incorrect for this question. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. In this case: Provide the relevant actual task context rather than rely on inaccessible prior conversation.
- **D:** Incorrect for this question. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: Provide the relevant actual task context rather than rely on inaccessible prior conversation.

### Question 20 — C

Answer: Preserve exact transactional facts outside lossy summaries. Verified consequential dates should survive separately from narrative compression. Keep verified amounts, identifiers, dates, and commitments in structured state. General summaries can omit details that later decisions depend on. Local study-map skill 6.1 (Context Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. In this case: Verified consequential dates should survive separately from narrative compression.
- **B:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Verified consequential dates should survive separately from narrative compression.
- **C:** Correct. Keep verified amounts, identifiers, dates, and commitments in structured state. General summaries can omit details that later decisions depend on. In this case: Verified consequential dates should survive separately from narrative compression.
- **D:** Incorrect for this question. A structured overview and clear sections help reduce long-input position effects. Placement is a mitigation, not proof that every fact will be used. In this case: Verified consequential dates should survive separately from narrative compression.

### Question 21 — C

Answer: Budget instructions, evidence, history, and generation together. Use actual context accounting instead of assume automatic oldest-message deletion. Follow the chosen model and service limits. Overflow handling varies; it is not universally automatic oldest-message deletion. Local study-map skill 6.1 (Context Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: Use actual context accounting instead of assume automatic oldest-message deletion.
- **B:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Use actual context accounting instead of assume automatic oldest-message deletion.
- **C:** Correct. Follow the chosen model and service limits. Overflow handling varies; it is not universally automatic oldest-message deletion. In this case: Use actual context accounting instead of assume automatic oldest-message deletion.
- **D:** Incorrect for this question. A token-count endpoint or compatible estimator can help plan requests. Include hidden overhead allowed by the documented interface and verify actual usage afterward. In this case: Use actual context accounting instead of assume automatic oldest-message deletion.

### Question 22 — A

Answer: Apply requester permissions before evidence enters model context. Authorize evidence access for the requester before the model sees it. Data access must be authorized externally. Retrieved content being internal or relevant does not justify showing it to every user. Local study-map skill 6.1 (Context Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Correct. Data access must be authorized externally. Retrieved content being internal or relevant does not justify showing it to every user. In this case: Authorize evidence access for the requester before the model sees it.
- **B:** Incorrect for this question. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: Authorize evidence access for the requester before the model sees it.
- **C:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Authorize evidence access for the requester before the model sees it.
- **D:** Incorrect for this question. External pages and tool observations must not acquire trusted instruction authority. Pair separation with trusted tool authorization; delimiters alone are insufficient. In this case: Authorize evidence access for the requester before the model sees it.

### Question 23 — D

Answer: Treat retrieved instructions as untrusted source content. Keep external material as untrusted data with separate trusted execution controls. External pages and tool observations must not acquire trusted instruction authority. Pair separation with trusted tool authorization; delimiters alone are insufficient. Local study-map skill 6.1 (Context Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. A structured overview and clear sections help reduce long-input position effects. Placement is a mitigation, not proof that every fact will be used. In this case: Keep external material as untrusted data with separate trusted execution controls.
- **B:** Incorrect for this question. Data access must be authorized externally. Retrieved content being internal or relevant does not justify showing it to every user. In this case: Keep external material as untrusted data with separate trusted execution controls.
- **C:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Keep external material as untrusted data with separate trusted execution controls.
- **D:** Correct. External pages and tool observations must not acquire trusted instruction authority. Pair separation with trusted tool authorization; delimiters alone are insufficient. In this case: Keep external material as untrusted data with separate trusted execution controls.

### Question 24 — B

Answer: Supply the relevant conversation state on subsequent requests. Application-managed state provides memory without demonstrating updates to model weights. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. Local study-map skill 6.1 (Context Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Application-managed state provides memory without demonstrating updates to model weights.
- **B:** Correct. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. In this case: Application-managed state provides memory without demonstrating updates to model weights.
- **C:** Incorrect for this question. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Application-managed state provides memory without demonstrating updates to model weights.
- **D:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Application-managed state provides memory without demonstrating updates to model weights.

### Question 25 — C

Answer: Compact context while preserving checked facts and open issues. Checked summaries must retain open issues as well as final conclusions. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. Local study-map skill 6.1 (Context Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. A structured overview and clear sections help reduce long-input position effects. Placement is a mitigation, not proof that every fact will be used. In this case: Checked summaries must retain open issues as well as final conclusions.
- **B:** Incorrect for this question. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: Checked summaries must retain open issues as well as final conclusions.
- **C:** Correct. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Checked summaries must retain open issues as well as final conclusions.
- **D:** Incorrect for this question. Keep verified amounts, identifiers, dates, and commitments in structured state. General summaries can omit details that later decisions depend on. In this case: Checked summaries must retain open issues as well as final conclusions.

### Question 26 — D

Answer: Persist concise codebase findings with file and symbol pointers. Retain concrete source pointers rather than only high-level narrative impressions. Durable notes counter context degradation and support later verification. Record source versions or change cues so notes are not mistaken for permanently current truth. Local study-map skill 6.1 (Context Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Recovery needs known state locations, completion status, source versions, and pending work. Do not infer completion merely because an output file exists. In this case: Retain concrete source pointers rather than only high-level narrative impressions.
- **B:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Retain concrete source pointers rather than only high-level narrative impressions.
- **C:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Retain concrete source pointers rather than only high-level narrative impressions.
- **D:** Correct. Durable notes counter context degradation and support later verification. Record source versions or change cues so notes are not mistaken for permanently current truth. In this case: Retain concrete source pointers rather than only high-level narrative impressions.

### Question 27 — D

Answer: Pass relevant evidence and constraints explicitly. Relevant constraints should travel with evidence across isolated stages. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. Local study-map skill 6.1 (Context Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: Relevant constraints should travel with evidence across isolated stages.
- **B:** Incorrect for this question. A coordinator manages decomposition, routing, error handling, and aggregation in a hub-and-spoke design. Specialists need not communicate through uncontrolled peer channels. In this case: Relevant constraints should travel with evidence across isolated stages.
- **C:** Incorrect for this question. Delegation requires a permitted launcher under the installed SDK contract. Check Agent versus legacy Task identifiers rather than assume all versions accept the same names. In this case: Relevant constraints should travel with evidence across isolated stages.
- **D:** Correct. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Relevant constraints should travel with evidence across isolated stages.

### Question 28 — A

Answer: Present key findings early and organize supporting details. An early checked summary and labeled sections improve orientation within long context. A structured overview and clear sections help reduce long-input position effects. Placement is a mitigation, not proof that every fact will be used. Local study-map skill 6.1 (Context Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Correct. A structured overview and clear sections help reduce long-input position effects. Placement is a mitigation, not proof that every fact will be used. In this case: An early checked summary and labeled sections improve orientation within long context.
- **B:** Incorrect for this question. Keep verified amounts, identifiers, dates, and commitments in structured state. General summaries can omit details that later decisions depend on. In this case: An early checked summary and labeled sections improve orientation within long context.
- **C:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: An early checked summary and labeled sections improve orientation within long context.
- **D:** Incorrect for this question. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: An early checked summary and labeled sections improve orientation within long context.

### Question 29 — B

Answer: Preserve claim-to-source mappings through every handoff. Preserve claim-source support rather than merely list source titles globally. Claims need traceable source identities, relevant excerpts, locations, and dates as applicable. A bibliography without claim mappings can lose attribution. Local study-map skill 6.1 (Context Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Tables can preserve financial comparisons, while prose and structured lists suit other needs. A single forced format can hide important structure. In this case: Preserve claim-source support rather than merely list source titles globally.
- **B:** Correct. Claims need traceable source identities, relevant excerpts, locations, and dates as applicable. A bibliography without claim mappings can lose attribution. In this case: Preserve claim-source support rather than merely list source titles globally.
- **C:** Incorrect for this question. Do not average incompatible measurements or choose one arbitrarily. Preserve context and distinguish contested findings from established ones. In this case: Preserve claim-source support rather than merely list source titles globally.
- **D:** Incorrect for this question. Different measurement periods can explain apparent disagreements. Dates and methodology should remain attached rather than being stripped in summaries. In this case: Preserve claim-source support rather than merely list source titles globally.

### Question 30 — A

Answer: Start a fresh session with a checked structured summary. Build a current checked starting context and revisit changed evidence explicitly. A new context can avoid stale tool results when assumptions changed widely. Preserve verified facts, relevant constraints, and pointers rather than import all obsolete history. Local study-map skill 6.1 (Context Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Correct. A new context can avoid stale tool results when assumptions changed widely. Preserve verified facts, relevant constraints, and pointers rather than import all obsolete history. In this case: Build a current checked starting context and revisit changed evidence explicitly.
- **B:** Incorrect for this question. Targeted re-analysis works when most prior context remains useful. Explicit change information prevents reliance on stale file or tool observations. In this case: Build a current checked starting context and revisit changed evidence explicitly.
- **C:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Build a current checked starting context and revisit changed evidence explicitly.
- **D:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Build a current checked starting context and revisit changed evidence explicitly.

### Question 31 — C

Answer: State explicit reportable and non-reportable criteria. Explicit inclusion criteria and exclusions make the intended judgment checkable. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. Local study-map skill 6.2 (Prompt Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. A consistent rubric distinguishes materially different harms. Self-reported confidence is not a substitute for severity or business impact. In this case: Explicit inclusion criteria and exclusions make the intended judgment checkable.
- **B:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Explicit inclusion criteria and exclusions make the intended judgment checkable.
- **C:** Correct. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Explicit inclusion criteria and exclusions make the intended judgment checkable.
- **D:** Incorrect for this question. A narrowly controlled pause can restore trust while the category is improved. Preserve valuable other categories and monitor the consequences. In this case: Explicit inclusion criteria and exclusions make the intended judgment checkable.

### Question 32 — C

Answer: Specify task, audience, constraints, and output expectations. Specify audience, task, constraints, and output expectations instead of vague improvement requests. Concrete requirements clarify what useful output means. A role, sampling setting, or longer answer limit does not replace a precise task contract. Local study-map skill 6.2 (Prompt Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Specify audience, task, constraints, and output expectations instead of vague improvement requests.
- **B:** Incorrect for this question. A role can guide style and viewpoint, but it does not grant expertise, authorization, or verified knowledge. In this case: Specify audience, task, constraints, and output expectations instead of vague improvement requests.
- **C:** Correct. Concrete requirements clarify what useful output means. A role, sampling setting, or longer answer limit does not replace a precise task contract. In this case: Specify audience, task, constraints, and output expectations instead of vague improvement requests.
- **D:** Incorrect for this question. An output ceiling bounds generation subject to model accounting. It does not itself expand input context or guarantee that a complete response fits. In this case: Specify audience, task, constraints, and output expectations instead of vague improvement requests.

### Question 33 — C

Answer: Place trusted application policy in the supported system instruction field. Use supported system instructions rather than bury trusted rules inside retrieved content. Keep trusted instructions separate from user and retrieved data. On the direct Messages API, system instructions use the top-level system parameter rather than a system-role entry in messages. Local study-map skill 6.2 (Prompt Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Use supported system instructions rather than bury trusted rules inside retrieved content.
- **B:** Incorrect for this question. Use the selected API contract for model, instructions, messages, and typed content. Do not assume a consumer chat interface and a developer API share implicit state. In this case: Use supported system instructions rather than bury trusted rules inside retrieved content.
- **C:** Correct. Keep trusted instructions separate from user and retrieved data. On the direct Messages API, system instructions use the top-level system parameter rather than a system-role entry in messages. In this case: Use supported system instructions rather than bury trusted rules inside retrieved content.
- **D:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: Use supported system instructions rather than bury trusted rules inside retrieved content.

### Question 34 — D

Answer: Separate instructions and source data with explicit labels. Clearly separate trusted instructions from untrusted material while retaining external controls. Delimiters improve clarity about source boundaries but are not a security barrier or a grant of authority to the enclosed content. Local study-map skill 6.2 (Prompt Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. External pages and tool observations must not acquire trusted instruction authority. Pair separation with trusted tool authorization; delimiters alone are insufficient. In this case: Clearly separate trusted instructions from untrusted material while retaining external controls.
- **B:** Incorrect for this question. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Clearly separate trusted instructions from untrusted material while retaining external controls.
- **C:** Incorrect for this question. Keep trusted instructions separate from user and retrieved data. On the direct Messages API, system instructions use the top-level system parameter rather than a system-role entry in messages. In this case: Clearly separate trusted instructions from untrusted material while retaining external controls.
- **D:** Correct. Delimiters improve clarity about source boundaries but are not a security barrier or a grant of authority to the enclosed content. In this case: Clearly separate trusted instructions from untrusted material while retaining external controls.

### Question 35 — C

Answer: Use representative few-shot examples with boundaries. Representative few-shot examples show both output structure and judgment boundaries. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. Local study-map skill 6.2 (Prompt Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Negative examples teach a boundary and can reduce repeated false positives. They should not teach blanket suppression of an entire genuine-risk category. In this case: Representative few-shot examples show both output structure and judgment boundaries.
- **B:** Incorrect for this question. Zero-shot prompting supplies no example input-output pairs. The model may still use its pretrained capabilities and the request context. In this case: Representative few-shot examples show both output structure and judgment boundaries.
- **C:** Correct. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Representative few-shot examples show both output structure and judgment boundaries.
- **D:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Representative few-shot examples show both output structure and judgment boundaries.

### Question 36 — A

Answer: Include valid examples that should not be flagged. Valid negatives teach acceptable near-misses and reduce overgeneralization to false positives. Negative examples teach a boundary and can reduce repeated false positives. They should not teach blanket suppression of an entire genuine-risk category. Local study-map skill 6.2 (Prompt Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Correct. Negative examples teach a boundary and can reduce repeated false positives. They should not teach blanket suppression of an entire genuine-risk category. In this case: Valid negatives teach acceptable near-misses and reduce overgeneralization to false positives.
- **B:** Incorrect for this question. A consistent rubric distinguishes materially different harms. Self-reported confidence is not a substitute for severity or business impact. In this case: Valid negatives teach acceptable near-misses and reduce overgeneralization to false positives.
- **C:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Valid negatives teach acceptable near-misses and reduce overgeneralization to false positives.
- **D:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Valid negatives teach acceptable near-misses and reduce overgeneralization to false positives.

### Question 37 — B

Answer: Provide concrete input–output examples. Concrete before-and-after examples make these transformation boundaries explicit. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. Local study-map skill 6.2 (Prompt Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Concrete before-and-after examples make these transformation boundaries explicit.
- **B:** Correct. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Concrete before-and-after examples make these transformation boundaries explicit.
- **C:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Concrete before-and-after examples make these transformation boundaries explicit.
- **D:** Incorrect for this question. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Concrete before-and-after examples make these transformation boundaries explicit.

### Question 38 — D

Answer: Define severity using impact and concrete examples. Severity reflects impact rather than the model's confidence in an observation. A consistent rubric distinguishes materially different harms. Self-reported confidence is not a substitute for severity or business impact. Local study-map skill 6.2 (Prompt Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. In this case: Severity reflects impact rather than the model's confidence in an observation.
- **B:** Incorrect for this question. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: Severity reflects impact rather than the model's confidence in an observation.
- **C:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Severity reflects impact rather than the model's confidence in an observation.
- **D:** Correct. A consistent rubric distinguishes materially different harms. Self-reported confidence is not a substitute for severity or business impact. In this case: Severity reflects impact rather than the model's confidence in an observation.

### Question 39 — C

Answer: Version exact prompt content and its dependencies. Version actual prompt content and dependencies for comparison and rollback. Record revisions of behavioral instructions with evaluation and release history. A model pin does not freeze changing application prompts. Local study-map skill 6.2 (Prompt Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: Version actual prompt content and dependencies for comparison and rollback.
- **B:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Version actual prompt content and dependencies for comparison and rollback.
- **C:** Correct. Record revisions of behavioral instructions with evaluation and release history. A model pin does not freeze changing application prompts. In this case: Version actual prompt content and dependencies for comparison and rollback.
- **D:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Version actual prompt content and dependencies for comparison and rollback.

### Question 40 — C

Answer: Use a versioned representative held-out evaluation set. Representative held-out evaluation checks behavior beyond familiar development cases. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. Local study-map skill 6.2 (Prompt Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Representative held-out evaluation checks behavior beyond familiar development cases.
- **B:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Representative held-out evaluation checks behavior beyond familiar development cases.
- **C:** Correct. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Representative held-out evaluation checks behavior beyond familiar development cases.
- **D:** Incorrect for this question. Negative examples teach a boundary and can reduce repeated false positives. They should not teach blanket suppression of an entire genuine-risk category. In this case: Representative held-out evaluation checks behavior beyond familiar development cases.

### Question 41 — A

Answer: Use representative few-shot examples with boundaries. Demonstrations should cover relevant document variation rather than one ideal structure. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. Local study-map skill 6.2 (Prompt Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Correct. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Demonstrations should cover relevant document variation rather than one ideal structure.
- **B:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Demonstrations should cover relevant document variation rather than one ideal structure.
- **C:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Demonstrations should cover relevant document variation rather than one ideal structure.
- **D:** Incorrect for this question. Zero-shot prompting supplies no example input-output pairs. The model may still use its pretrained capabilities and the request context. In this case: Demonstrations should cover relevant document variation rather than one ideal structure.

### Question 42 — D

Answer: Ask targeted design questions before implementation. Targeted questions can resolve assumptions that would otherwise be guessed. An interview-style clarification step surfaces unknown assumptions and constraints. Use it when uncertainty materially affects design. Local study-map skill 6.2 (Prompt Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Targeted questions can resolve assumptions that would otherwise be guessed.
- **B:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Targeted questions can resolve assumptions that would otherwise be guessed.
- **C:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Targeted questions can resolve assumptions that would otherwise be guessed.
- **D:** Correct. An interview-style clarification step surfaces unknown assumptions and constraints. Use it when uncertainty materially affects design. In this case: Targeted questions can resolve assumptions that would otherwise be guessed.

### Question 43 — B

Answer: Explain interacting issues together before revising. Explain interacting constraints together so one correction does not undermine another. When fixes influence one another, provide the combined constraints and failure evidence. Independent issues can be addressed separately. Local study-map skill 6.2 (Prompt Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: Explain interacting constraints together so one correction does not undermine another.
- **B:** Correct. When fixes influence one another, provide the combined constraints and failure evidence. Independent issues can be addressed separately. In this case: Explain interacting constraints together so one correction does not undermine another.
- **C:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Explain interacting constraints together so one correction does not undermine another.
- **D:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Explain interacting constraints together so one correction does not undermine another.

### Question 44 — A

Answer: Break the task into linked checked prompt stages. Separate linked stages can isolate errors and feed validated outputs forward. Prompt chaining can isolate extraction, validation, and drafting when stages have known dependencies. Validate intermediate results rather than propagate errors blindly. Local study-map skill 6.2 (Prompt Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Correct. Prompt chaining can isolate extraction, validation, and drafting when stages have known dependencies. Validate intermediate results rather than propagate errors blindly. In this case: Separate linked stages can isolate errors and feed validated outputs forward.
- **B:** Incorrect for this question. Zero-shot prompting supplies no example input-output pairs. The model may still use its pretrained capabilities and the request context. In this case: Separate linked stages can isolate errors and feed validated outputs forward.
- **C:** Incorrect for this question. One-shot prompting includes one example. It is different from a training update and may not cover important task variation. In this case: Separate linked stages can isolate errors and feed validated outputs forward.
- **D:** Incorrect for this question. A role can guide style and viewpoint, but it does not grant expertise, authorization, or verified knowledge. In this case: Separate linked stages can isolate errors and feed validated outputs forward.

### Question 45 — B

Answer: State explicit reportable and non-reportable criteria. State reportable and non-reportable categories rather than ask for generic conservatism. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. Local study-map skill 6.2 (Prompt Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. A narrowly controlled pause can restore trust while the category is improved. Preserve valuable other categories and monitor the consequences. In this case: State reportable and non-reportable categories rather than ask for generic conservatism.
- **B:** Correct. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: State reportable and non-reportable categories rather than ask for generic conservatism.
- **C:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: State reportable and non-reportable categories rather than ask for generic conservatism.
- **D:** Incorrect for this question. Negative examples teach a boundary and can reduce repeated false positives. They should not teach blanket suppression of an entire genuine-risk category. In this case: State reportable and non-reportable categories rather than ask for generic conservatism.

### Question 46 — A

Answer: Specify task, audience, constraints, and output expectations. Make the desired format and scope explicit before changing unrelated model settings. Concrete requirements clarify what useful output means. A role, sampling setting, or longer answer limit does not replace a precise task contract. Local study-map skill 6.2 (Prompt Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Correct. Concrete requirements clarify what useful output means. A role, sampling setting, or longer answer limit does not replace a precise task contract. In this case: Make the desired format and scope explicit before changing unrelated model settings.
- **B:** Incorrect for this question. An output ceiling bounds generation subject to model accounting. It does not itself expand input context or guarantee that a complete response fits. In this case: Make the desired format and scope explicit before changing unrelated model settings.
- **C:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Make the desired format and scope explicit before changing unrelated model settings.
- **D:** Incorrect for this question. A role can guide style and viewpoint, but it does not grant expertise, authorization, or verified knowledge. In this case: Make the desired format and scope explicit before changing unrelated model settings.

### Question 47 — C

Answer: Separate instructions and source data with explicit labels. Separate and label source content as data without treating delimiters as a security guarantee. Delimiters improve clarity about source boundaries but are not a security barrier or a grant of authority to the enclosed content. Local study-map skill 6.2 (Prompt Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Separate and label source content as data without treating delimiters as a security guarantee.
- **B:** Incorrect for this question. External pages and tool observations must not acquire trusted instruction authority. Pair separation with trusted tool authorization; delimiters alone are insufficient. In this case: Separate and label source content as data without treating delimiters as a security guarantee.
- **C:** Correct. Delimiters improve clarity about source boundaries but are not a security barrier or a grant of authority to the enclosed content. In this case: Separate and label source content as data without treating delimiters as a security guarantee.
- **D:** Incorrect for this question. Keep trusted instructions separate from user and retrieved data. On the direct Messages API, system instructions use the top-level system parameter rather than a system-role entry in messages. In this case: Separate and label source content as data without treating delimiters as a security guarantee.

### Question 48 — A

Answer: Include valid examples that should not be flagged. Include legitimate supported uses that should not produce findings. Negative examples teach a boundary and can reduce repeated false positives. They should not teach blanket suppression of an entire genuine-risk category. Local study-map skill 6.2 (Prompt Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Correct. Negative examples teach a boundary and can reduce repeated false positives. They should not teach blanket suppression of an entire genuine-risk category. In this case: Include legitimate supported uses that should not produce findings.
- **B:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Include legitimate supported uses that should not produce findings.
- **C:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Include legitimate supported uses that should not produce findings.
- **D:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Include legitimate supported uses that should not produce findings.

### Question 49 — D

Answer: Version exact prompt content and its dependencies. Track the actual prompt revision instead of attribute all behavior solely to the model version. Record revisions of behavioral instructions with evaluation and release history. A model pin does not freeze changing application prompts. Local study-map skill 6.2 (Prompt Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Track the actual prompt revision instead of attribute all behavior solely to the model version.
- **B:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Track the actual prompt revision instead of attribute all behavior solely to the model version.
- **C:** Incorrect for this question. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: Track the actual prompt revision instead of attribute all behavior solely to the model version.
- **D:** Correct. Record revisions of behavioral instructions with evaluation and release history. A model pin does not freeze changing application prompts. In this case: Track the actual prompt revision instead of attribute all behavior solely to the model version.

### Question 50 — A

Answer: State explicit reportable and non-reportable criteria. Concrete categorical criteria establish what counts as a reportable issue. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. Local study-map skill 6.2 (Prompt Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Correct. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Concrete categorical criteria establish what counts as a reportable issue.
- **B:** Incorrect for this question. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: Concrete categorical criteria establish what counts as a reportable issue.
- **C:** Incorrect for this question. A consistent rubric distinguishes materially different harms. Self-reported confidence is not a substitute for severity or business impact. In this case: Concrete categorical criteria establish what counts as a reportable issue.
- **D:** Incorrect for this question. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. In this case: Concrete categorical criteria establish what counts as a reportable issue.

### Question 51 — C

Answer: Use representative few-shot examples with boundaries. Representative examples show the pattern more concretely than another vague instruction. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. Local study-map skill 6.2 (Prompt Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Representative examples show the pattern more concretely than another vague instruction.
- **B:** Incorrect for this question. Zero-shot prompting supplies no example input-output pairs. The model may still use its pretrained capabilities and the request context. In this case: Representative examples show the pattern more concretely than another vague instruction.
- **C:** Correct. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Representative examples show the pattern more concretely than another vague instruction.
- **D:** Incorrect for this question. Negative examples teach a boundary and can reduce repeated false positives. They should not teach blanket suppression of an entire genuine-risk category. In this case: Representative examples show the pattern more concretely than another vague instruction.

### Question 52 — C

Answer: Use tests and specific failure feedback to drive iteration. Provide the specific input, expected behavior, and actual failure rather than only dissatisfaction. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. Local study-map skill 6.2 (Prompt Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. An interview-style clarification step surfaces unknown assumptions and constraints. Use it when uncertainty materially affects design. In this case: Provide the specific input, expected behavior, and actual failure rather than only dissatisfaction.
- **B:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Provide the specific input, expected behavior, and actual failure rather than only dissatisfaction.
- **C:** Correct. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Provide the specific input, expected behavior, and actual failure rather than only dissatisfaction.
- **D:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Provide the specific input, expected behavior, and actual failure rather than only dissatisfaction.

### Question 53 — C

Answer: Ask targeted design questions before implementation. Retry side-effect requirements materially affect design and should not be silently assumed. An interview-style clarification step surfaces unknown assumptions and constraints. Use it when uncertainty materially affects design. Local study-map skill 6.2 (Prompt Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Retry side-effect requirements materially affect design and should not be silently assumed.
- **B:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Retry side-effect requirements materially affect design and should not be silently assumed.
- **C:** Correct. An interview-style clarification step surfaces unknown assumptions and constraints. Use it when uncertainty materially affects design. In this case: Retry side-effect requirements materially affect design and should not be silently assumed.
- **D:** Incorrect for this question. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. In this case: Retry side-effect requirements materially affect design and should not be silently assumed.

### Question 54 — A

Answer: State explicit reportable and non-reportable criteria. Define the actual reportable scope and require evidence for the specified categories. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. Local study-map skill 6.2 (Prompt Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Correct. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Define the actual reportable scope and require evidence for the specified categories.
- **B:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Define the actual reportable scope and require evidence for the specified categories.
- **C:** Incorrect for this question. A consistent rubric distinguishes materially different harms. Self-reported confidence is not a substitute for severity or business impact. In this case: Define the actual reportable scope and require evidence for the specified categories.
- **D:** Incorrect for this question. Negative examples teach a boundary and can reduce repeated false positives. They should not teach blanket suppression of an entire genuine-risk category. In this case: Define the actual reportable scope and require evidence for the specified categories.

### Question 55 — A

Answer: Provide concrete input–output examples. Show the intended normalization using varied source forms and checked outputs. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. Local study-map skill 6.2 (Prompt Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Correct. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Show the intended normalization using varied source forms and checked outputs.
- **B:** Incorrect for this question. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Show the intended normalization using varied source forms and checked outputs.
- **C:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Show the intended normalization using varied source forms and checked outputs.
- **D:** Incorrect for this question. Zero-shot prompting supplies no example input-output pairs. The model may still use its pretrained capabilities and the request context. In this case: Show the intended normalization using varied source forms and checked outputs.

### Question 56 — B

Answer: Include valid examples that should not be flagged. Demonstrate the acceptable exception and why it differs from a genuine defect. Negative examples teach a boundary and can reduce repeated false positives. They should not teach blanket suppression of an entire genuine-risk category. Local study-map skill 6.2 (Prompt Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Demonstrate the acceptable exception and why it differs from a genuine defect.
- **B:** Correct. Negative examples teach a boundary and can reduce repeated false positives. They should not teach blanket suppression of an entire genuine-risk category. In this case: Demonstrate the acceptable exception and why it differs from a genuine defect.
- **C:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Demonstrate the acceptable exception and why it differs from a genuine defect.
- **D:** Incorrect for this question. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: Demonstrate the acceptable exception and why it differs from a genuine defect.

### Question 57 — B

Answer: Version exact prompt content and its dependencies. Track exact prompt content and relevant dependencies while keeping evaluation conditions comparable. Record revisions of behavioral instructions with evaluation and release history. A model pin does not freeze changing application prompts. Local study-map skill 6.2 (Prompt Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: Track exact prompt content and relevant dependencies while keeping evaluation conditions comparable.
- **B:** Correct. Record revisions of behavioral instructions with evaluation and release history. A model pin does not freeze changing application prompts. In this case: Track exact prompt content and relevant dependencies while keeping evaluation conditions comparable.
- **C:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Track exact prompt content and relevant dependencies while keeping evaluation conditions comparable.
- **D:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Track exact prompt content and relevant dependencies while keeping evaluation conditions comparable.

### Question 58 — B

Answer: Specify task, audience, constraints, and output expectations. Specify evidence constraints and uncertainty handling rather than assume confidence means support. Concrete requirements clarify what useful output means. A role, sampling setting, or longer answer limit does not replace a precise task contract. Local study-map skill 6.2 (Prompt Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Specify evidence constraints and uncertainty handling rather than assume confidence means support.
- **B:** Correct. Concrete requirements clarify what useful output means. A role, sampling setting, or longer answer limit does not replace a precise task contract. In this case: Specify evidence constraints and uncertainty handling rather than assume confidence means support.
- **C:** Incorrect for this question. A role can guide style and viewpoint, but it does not grant expertise, authorization, or verified knowledge. In this case: Specify evidence constraints and uncertainty handling rather than assume confidence means support.
- **D:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Specify evidence constraints and uncertainty handling rather than assume confidence means support.

### Question 59 — C

Answer: Place trusted application policy in the supported system instruction field. Supply trusted instructions through the API's supported contract instead of assume shared interface behavior. Keep trusted instructions separate from user and retrieved data. On the direct Messages API, system instructions use the top-level system parameter rather than a system-role entry in messages. Local study-map skill 6.2 (Prompt Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Use the selected API contract for model, instructions, messages, and typed content. Do not assume a consumer chat interface and a developer API share implicit state. In this case: Supply trusted instructions through the API's supported contract instead of assume shared interface behavior.
- **B:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: Supply trusted instructions through the API's supported contract instead of assume shared interface behavior.
- **C:** Correct. Keep trusted instructions separate from user and retrieved data. On the direct Messages API, system instructions use the top-level system parameter rather than a system-role entry in messages. In this case: Supply trusted instructions through the API's supported contract instead of assume shared interface behavior.
- **D:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Supply trusted instructions through the API's supported contract instead of assume shared interface behavior.

### Question 60 — D

Answer: Use a versioned representative held-out evaluation set. Use a representative regression set instead of judge only the targeted example. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. Local study-map skill 6.2 (Prompt Engineering), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Negative examples teach a boundary and can reduce repeated false positives. They should not teach blanket suppression of an entire genuine-risk category. In this case: Use a representative regression set instead of judge only the targeted example.
- **B:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Use a representative regression set instead of judge only the targeted example.
- **C:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Use a representative regression set instead of judge only the targeted example.
- **D:** Correct. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Use a representative regression set instead of judge only the targeted example.

### Question 61 — B

Answer: Use supported strict structured output with a schema. Use supported strict output constraints and handle incompatible or incomplete response states. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Use supported strict output constraints and handle incompatible or incomplete response states.
- **B:** Correct. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Use supported strict output constraints and handle incompatible or incomplete response states.
- **C:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Use supported strict output constraints and handle incompatible or incomplete response states.
- **D:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Use supported strict output constraints and handle incompatible or incomplete response states.

### Question 62 — D

Answer: Validate extracted values against evidence and business rules. Verify field meaning against source evidence instead of trust shape alone. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Verify field meaning against source evidence instead of trust shape alone.
- **B:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Verify field meaning against source evidence instead of trust shape alone.
- **C:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Verify field meaning against source evidence instead of trust shape alone.
- **D:** Correct. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Verify field meaning against source evidence instead of trust shape alone.

### Question 63 — B

Answer: Allow explicit unknown or absent values in the schema. Allow explicit unknown or missing values when the source cannot support a concrete answer. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Allow explicit unknown or missing values when the source cannot support a concrete answer.
- **B:** Correct. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Allow explicit unknown or missing values when the source cannot support a concrete answer.
- **C:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Allow explicit unknown or missing values when the source cannot support a concrete answer.
- **D:** Incorrect for this question. An other category with details can represent valid cases outside an enum. Unclear represents uncertainty and should not be confused with known-but-uncatalogued categories. In this case: Allow explicit unknown or missing values when the source cannot support a concrete answer.

### Question 64 — D

Answer: Use an extensible category plus a detail field. Use an other category plus details rather than label a known value as uncertain. An other category with details can represent valid cases outside an enum. Unclear represents uncertainty and should not be confused with known-but-uncatalogued categories. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Use an other category plus details rather than label a known value as uncertain.
- **B:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Use an other category plus details rather than label a known value as uncertain.
- **C:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Use an other category plus details rather than label a known value as uncertain.
- **D:** Correct. An other category with details can represent valid cases outside an enum. Unclear represents uncertainty and should not be confused with known-but-uncatalogued categories. In this case: Use an other category plus details rather than label a known value as uncertain.

### Question 65 — C

Answer: Specify deterministic normalization rules and preserve originals when needed. State normalization rules explicitly and validate them against original evidence. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: State normalization rules explicitly and validate them against original evidence.
- **B:** Incorrect for this question. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: State normalization rules explicitly and validate them against original evidence.
- **C:** Correct. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: State normalization rules explicitly and validate them against original evidence.
- **D:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: State normalization rules explicitly and validate them against original evidence.

### Question 66 — A

Answer: Validate extracted values against evidence and business rules. Semantic validation compares values and relationships with authoritative source content. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Correct. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Semantic validation compares values and relationships with authoritative source content.
- **B:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Semantic validation compares values and relationships with authoritative source content.
- **C:** Incorrect for this question. Separate calculated_total and stated_total can expose arithmetic or source inconsistencies. Preserve disagreement rather than silently overwrite evidence. In this case: Semantic validation compares values and relationships with authoritative source content.
- **D:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Semantic validation compares values and relationships with authoritative source content.

### Question 67 — C

Answer: Allow explicit unknown or absent values in the schema. A required nullable field can contain null; optionality instead concerns key omission. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: A required nullable field can contain null; optionality instead concerns key omission.
- **B:** Incorrect for this question. An other category with details can represent valid cases outside an enum. Unclear represents uncertainty and should not be confused with known-but-uncatalogued categories. In this case: A required nullable field can contain null; optionality instead concerns key omission.
- **C:** Correct. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: A required nullable field can contain null; optionality instead concerns key omission.
- **D:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: A required nullable field can contain null; optionality instead concerns key omission.

### Question 68 — A

Answer: Treat model output as untrusted before rendering or execution. Generated values remain untrusted and require destination-specific handling and authorization. Use destination-appropriate escaping, validation, and permission checks. Valid JSON can still contain executable or malicious values. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Correct. Use destination-appropriate escaping, validation, and permission checks. Valid JSON can still contain executable or malicious values. In this case: Generated values remain untrusted and require destination-specific handling and authorization.
- **B:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Generated values remain untrusted and require destination-specific handling and authorization.
- **C:** Incorrect for this question. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Generated values remain untrusted and require destination-specific handling and authorization.
- **D:** Incorrect for this question. Temperature changes next-token sampling behavior where supported. Lowering it does not independently guarantee correct extraction, grounding, or identical execution. In this case: Generated values remain untrusted and require destination-specific handling and authorization.

### Question 69 — C

Answer: Use the final assembled message and completion status. Use the assembled response and completion status before final validation and acceptance. SDK accumulation helpers can provide the complete message. Inspect termination and errors before treating the resulting object as accepted application output. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Network chunks and content deltas can contain partial strings or JSON. Track event and block boundaries or use SDK helpers before consuming a complete structured value. In this case: Use the assembled response and completion status before final validation and acceptance.
- **B:** Incorrect for this question. A response can contain text, tool use, thinking, or other supported blocks. Do not assume content is one string or that the first block is always displayable text. In this case: Use the assembled response and completion status before final validation and acceptance.
- **C:** Correct. SDK accumulation helpers can provide the complete message. Inspect termination and errors before treating the resulting object as accepted application output. In this case: Use the assembled response and completion status before final validation and acceptance.
- **D:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Use the assembled response and completion status before final validation and acceptance.

### Question 70 — B

Answer: Handle the output limit as an incomplete response. A limit-truncated response is incomplete even when structured output was requested. A max_tokens stop can leave content incomplete. Inspect the response and recover appropriately instead of treating it as normal completion. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. This indicates ordinary turn completion, not that every business objective or external action succeeded. Application acceptance checks still apply. In this case: A limit-truncated response is incomplete even when structured output was requested.
- **B:** Correct. A max_tokens stop can leave content incomplete. Inspect the response and recover appropriately instead of treating it as normal completion. In this case: A limit-truncated response is incomplete even when structured output was requested.
- **C:** Incorrect for this question. The loop follows protocol stop reasons, executes permitted requested tools, and returns observations before continuing. Text appearing in a response does not establish completion. In this case: A limit-truncated response is incomplete even when structured output was requested.
- **D:** Incorrect for this question. SDK accumulation helpers can provide the complete message. Inspect termination and errors before treating the resulting object as accepted application output. In this case: A limit-truncated response is incomplete even when structured output was requested.

### Question 71 — D

Answer: Retry with the document, failed result, and specific validation errors. Send the document, failed result, and precise validation error for bounded repair. Actionable feedback supports correction when evidence exists. Bound attempts and validate the revised result rather than resubmit the same vague request indefinitely. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Send the document, failed result, and precise validation error for bounded repair.
- **B:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Send the document, failed result, and precise validation error for bounded repair.
- **C:** Incorrect for this question. Retries cannot recover a fact that the available document never contained. Use unknown status, authorized retrieval, clarification, or review instead of fabrication. In this case: Send the document, failed result, and precise validation error for bounded repair.
- **D:** Correct. Actionable feedback supports correction when evidence exists. Bound attempts and validate the revised result rather than resubmit the same vague request indefinitely. In this case: Send the document, failed result, and precise validation error for bounded repair.

### Question 72 — D

Answer: Mark missing evidence and route for retrieval or review. Mark the evidence gap and retrieve, clarify, or review rather than hallucinate missing facts. Retries cannot recover a fact that the available document never contained. Use unknown status, authorized retrieval, clarification, or review instead of fabrication. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Mark the evidence gap and retrieve, clarify, or review rather than hallucinate missing facts.
- **B:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Mark the evidence gap and retrieve, clarify, or review rather than hallucinate missing facts.
- **C:** Incorrect for this question. Actionable feedback supports correction when evidence exists. Bound attempts and validate the revised result rather than resubmit the same vague request indefinitely. In this case: Mark the evidence gap and retrieve, clarify, or review rather than hallucinate missing facts.
- **D:** Correct. Retries cannot recover a fact that the available document never contained. Use unknown status, authorized retrieval, clarification, or review instead of fabrication. In this case: Mark the evidence gap and retrieve, clarify, or review rather than hallucinate missing facts.

### Question 73 — B

Answer: Compare independently calculated and source-stated totals. Keep independently calculated and stated totals separate instead of overwrite the source. Separate calculated_total and stated_total can expose arithmetic or source inconsistencies. Preserve disagreement rather than silently overwrite evidence. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Keep independently calculated and stated totals separate instead of overwrite the source.
- **B:** Correct. Separate calculated_total and stated_total can expose arithmetic or source inconsistencies. Preserve disagreement rather than silently overwrite evidence. In this case: Keep independently calculated and stated totals separate instead of overwrite the source.
- **C:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Keep independently calculated and stated totals separate instead of overwrite the source.
- **D:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Keep independently calculated and stated totals separate instead of overwrite the source.

### Question 74 — A

Answer: Preserve conflicting source values with an explicit flag. Flag and preserve attributed disagreement so it can be resolved knowingly. A conflict record enables review and prevents a synthetic answer from hiding disagreement. A valid schema alone does not resolve the underlying facts. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Correct. A conflict record enables review and prevents a synthetic answer from hiding disagreement. A valid schema alone does not resolve the underlying facts. In this case: Flag and preserve attributed disagreement so it can be resolved knowingly.
- **B:** Incorrect for this question. An other category with details can represent valid cases outside an enum. Unclear represents uncertainty and should not be confused with known-but-uncatalogued categories. In this case: Flag and preserve attributed disagreement so it can be resolved knowingly.
- **C:** Incorrect for this question. Separate calculated_total and stated_total can expose arithmetic or source inconsistencies. Preserve disagreement rather than silently overwrite evidence. In this case: Flag and preserve attributed disagreement so it can be resolved knowingly.
- **D:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Flag and preserve attributed disagreement so it can be resolved knowingly.

### Question 75 — A

Answer: Enforce task, iteration, and spending safeguards. Bound repair attempts and route unresolved cases instead of repeat indefinitely. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Correct. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. In this case: Bound repair attempts and route unresolved cases instead of repeat indefinitely.
- **B:** Incorrect for this question. Actionable feedback supports correction when evidence exists. Bound attempts and validate the revised result rather than resubmit the same vague request indefinitely. In this case: Bound repair attempts and route unresolved cases instead of repeat indefinitely.
- **C:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Bound repair attempts and route unresolved cases instead of repeat indefinitely.
- **D:** Incorrect for this question. Retries cannot recover a fact that the available document never contained. Use unknown status, authorized retrieval, clarification, or review instead of fabrication. In this case: Bound repair attempts and route unresolved cases instead of repeat indefinitely.

### Question 76 — A

Answer: Validate extracted values against evidence and business rules. Revalidate source correctness and field relationships after every revision. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Correct. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Revalidate source correctness and field relationships after every revision.
- **B:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Revalidate source correctness and field relationships after every revision.
- **C:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Revalidate source correctness and field relationships after every revision.
- **D:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Revalidate source correctness and field relationships after every revision.

### Question 77 — C

Answer: Retry with the document, failed result, and specific validation errors. Specific errors and source evidence make a corrective attempt actionable. Actionable feedback supports correction when evidence exists. Bound attempts and validate the revised result rather than resubmit the same vague request indefinitely. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Specific errors and source evidence make a corrective attempt actionable.
- **B:** Incorrect for this question. Retries cannot recover a fact that the available document never contained. Use unknown status, authorized retrieval, clarification, or review instead of fabrication. In this case: Specific errors and source evidence make a corrective attempt actionable.
- **C:** Correct. Actionable feedback supports correction when evidence exists. Bound attempts and validate the revised result rather than resubmit the same vague request indefinitely. In this case: Specific errors and source evidence make a corrective attempt actionable.
- **D:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Specific errors and source evidence make a corrective attempt actionable.

### Question 78 — D

Answer: Mark missing evidence and route for retrieval or review. No rewording supplies unavailable evidence without an authorized additional source or reviewer. Retries cannot recover a fact that the available document never contained. Use unknown status, authorized retrieval, clarification, or review instead of fabrication. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: No rewording supplies unavailable evidence without an authorized additional source or reviewer.
- **B:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: No rewording supplies unavailable evidence without an authorized additional source or reviewer.
- **C:** Incorrect for this question. Actionable feedback supports correction when evidence exists. Bound attempts and validate the revised result rather than resubmit the same vague request indefinitely. In this case: No rewording supplies unavailable evidence without an authorized additional source or reviewer.
- **D:** Correct. Retries cannot recover a fact that the available document never contained. Use unknown status, authorized retrieval, clarification, or review instead of fabrication. In this case: No rewording supplies unavailable evidence without an authorized additional source or reviewer.

### Question 79 — C

Answer: Preserve conflicting source values with an explicit flag. Preserve the disagreement rather than present a guessed resolution as a verified fact. A conflict record enables review and prevents a synthetic answer from hiding disagreement. A valid schema alone does not resolve the underlying facts. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Separate calculated_total and stated_total can expose arithmetic or source inconsistencies. Preserve disagreement rather than silently overwrite evidence. In this case: Preserve the disagreement rather than present a guessed resolution as a verified fact.
- **B:** Incorrect for this question. An other category with details can represent valid cases outside an enum. Unclear represents uncertainty and should not be confused with known-but-uncatalogued categories. In this case: Preserve the disagreement rather than present a guessed resolution as a verified fact.
- **C:** Correct. A conflict record enables review and prevents a synthetic answer from hiding disagreement. A valid schema alone does not resolve the underlying facts. In this case: Preserve the disagreement rather than present a guessed resolution as a verified fact.
- **D:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Preserve the disagreement rather than present a guessed resolution as a verified fact.

### Question 80 — C

Answer: Validate extracted values against evidence and business rules. Validate semantic placement and evidence support, not only the field's string format. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Validate semantic placement and evidence support, not only the field's string format.
- **B:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Validate semantic placement and evidence support, not only the field's string format.
- **C:** Correct. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Validate semantic placement and evidence support, not only the field's string format.
- **D:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Validate semantic placement and evidence support, not only the field's string format.

### Question 81 — B

Answer: Treat model output as untrusted before rendering or execution. Constrain and validate output for its actual filesystem use instead of trust generated text. Use destination-appropriate escaping, validation, and permission checks. Valid JSON can still contain executable or malicious values. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Temperature changes next-token sampling behavior where supported. Lowering it does not independently guarantee correct extraction, grounding, or identical execution. In this case: Constrain and validate output for its actual filesystem use instead of trust generated text.
- **B:** Correct. Use destination-appropriate escaping, validation, and permission checks. Valid JSON can still contain executable or malicious values. In this case: Constrain and validate output for its actual filesystem use instead of trust generated text.
- **C:** Incorrect for this question. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Constrain and validate output for its actual filesystem use instead of trust generated text.
- **D:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Constrain and validate output for its actual filesystem use instead of trust generated text.

### Question 82 — B

Answer: Calibrate field-confidence thresholds against labeled examples. Calibrate the field-level signal against representative observed correctness. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Averages can hide systematic failures in rare forms or important fields. Segment-level evaluation informs safe automation and review allocation. In this case: Calibrate the field-level signal against representative observed correctness.
- **B:** Correct. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. In this case: Calibrate the field-level signal against representative observed correctness.
- **C:** Incorrect for this question. Ongoing random checks among high-confidence results can discover hidden errors and changing patterns that low-confidence-only review misses. In this case: Calibrate the field-level signal against representative observed correctness.
- **D:** Incorrect for this question. Review priority should reflect uncertainty and consequences. A high uncalibrated confidence number should not override contradictory evidence. In this case: Calibrate the field-level signal against representative observed correctness.

### Question 83 — C

Answer: Route ambiguous, conflicting, or high-risk cases to qualified review. Qualified review should consider source ambiguity and consequences beyond self-reported confidence. Review priority should reflect uncertainty and consequences. A high uncalibrated confidence number should not override contradictory evidence. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Ongoing random checks among high-confidence results can discover hidden errors and changing patterns that low-confidence-only review misses. In this case: Qualified review should consider source ambiguity and consequences beyond self-reported confidence.
- **B:** Incorrect for this question. Averages can hide systematic failures in rare forms or important fields. Segment-level evaluation informs safe automation and review allocation. In this case: Qualified review should consider source ambiguity and consequences beyond self-reported confidence.
- **C:** Correct. Review priority should reflect uncertainty and consequences. A high uncalibrated confidence number should not override contradictory evidence. In this case: Qualified review should consider source ambiguity and consequences beyond self-reported confidence.
- **D:** Incorrect for this question. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. In this case: Qualified review should consider source ambiguity and consequences beyond self-reported confidence.

### Question 84 — C

Answer: Evaluate accuracy by document type and field segment. Evaluate by field and document segment rather than rely on an average. Averages can hide systematic failures in rare forms or important fields. Segment-level evaluation informs safe automation and review allocation. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Ongoing random checks among high-confidence results can discover hidden errors and changing patterns that low-confidence-only review misses. In this case: Evaluate by field and document segment rather than rely on an average.
- **B:** Incorrect for this question. Review priority should reflect uncertainty and consequences. A high uncalibrated confidence number should not override contradictory evidence. In this case: Evaluate by field and document segment rather than rely on an average.
- **C:** Correct. Averages can hide systematic failures in rare forms or important fields. Segment-level evaluation informs safe automation and review allocation. In this case: Evaluate by field and document segment rather than rely on an average.
- **D:** Incorrect for this question. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. In this case: Evaluate by field and document segment rather than rely on an average.

### Question 85 — B

Answer: Preserve claim-to-source mappings through every handoff. Check claim-to-passage support instead of assume a citation marker proves grounding. Claims need traceable source identities, relevant excerpts, locations, and dates as applicable. A bibliography without claim mappings can lose attribution. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Different measurement periods can explain apparent disagreements. Dates and methodology should remain attached rather than being stripped in summaries. In this case: Check claim-to-passage support instead of assume a citation marker proves grounding.
- **B:** Correct. Claims need traceable source identities, relevant excerpts, locations, and dates as applicable. A bibliography without claim mappings can lose attribution. In this case: Check claim-to-passage support instead of assume a citation marker proves grounding.
- **C:** Incorrect for this question. Do not average incompatible measurements or choose one arbitrarily. Preserve context and distinguish contested findings from established ones. In this case: Check claim-to-passage support instead of assume a citation marker proves grounding.
- **D:** Incorrect for this question. Tables can preserve financial comparisons, while prose and structured lists suit other needs. A single forced format can hide important structure. In this case: Check claim-to-passage support instead of assume a citation marker proves grounding.

### Question 86 — C

Answer: State insufficient evidence or use an approved escalation path. Acknowledge insufficient evidence or escalate through a defined approved pathway. Avoid fabricate unsupported consequential answers. Clarify, obtain authorized evidence, or escalate under the defined policy when approved context is inadequate. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Acknowledge insufficient evidence or escalate through a defined approved pathway.
- **B:** Incorrect for this question. Review priority should reflect uncertainty and consequences. A high uncalibrated confidence number should not override contradictory evidence. In this case: Acknowledge insufficient evidence or escalate through a defined approved pathway.
- **C:** Correct. Avoid fabricate unsupported consequential answers. Clarify, obtain authorized evidence, or escalate under the defined policy when approved context is inadequate. In this case: Acknowledge insufficient evidence or escalate through a defined approved pathway.
- **D:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Acknowledge insufficient evidence or escalate through a defined approved pathway.

### Question 87 — A

Answer: Isolate model-output defects from integration defects. The integration transformation, not the prompt alone, caused the visible defect. Check whether correct raw output was lost or changed by serialization, parsing, routing, or persistence. Not every visible error is fixed by changing the prompt. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Correct. Check whether correct raw output was lost or changed by serialization, parsing, routing, or persistence. Not every visible error is fixed by changing the prompt. In this case: The integration transformation, not the prompt alone, caused the visible defect.
- **B:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: The integration transformation, not the prompt alone, caused the visible defect.
- **C:** Incorrect for this question. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: The integration transformation, not the prompt alone, caused the visible defect.
- **D:** Incorrect for this question. Correlate the actual request, model response, tool execution, retries, and validation results. Diagnose the first failing boundary rather than infer cause from the final prose. In this case: The integration transformation, not the prompt alone, caused the visible defect.

### Question 88 — A

Answer: Record detected_pattern and dismissal reasons. Structured detected-pattern and dismissal records support targeted correction rather than speculation. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Correct. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: Structured detected-pattern and dismissal records support targeted correction rather than speculation.
- **B:** Incorrect for this question. A narrowly controlled pause can restore trust while the category is improved. Preserve valuable other categories and monitor the consequences. In this case: Structured detected-pattern and dismissal records support targeted correction rather than speculation.
- **C:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Structured detected-pattern and dismissal records support targeted correction rather than speculation.
- **D:** Incorrect for this question. A consistent rubric distinguishes materially different harms. Self-reported confidence is not a substitute for severity or business impact. In this case: Structured detected-pattern and dismissal records support targeted correction rather than speculation.

### Question 89 — D

Answer: Use an independent reviewer without the generator rationale. An independent reviewer can reduce anchoring without guaranteeing correctness or inventing missing evidence. Independent review reduces anchoring on the original solution. It still needs the specification, relevant code, and evidence; independence does not guarantee correctness. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. In this case: An independent reviewer can reduce anchoring without guaranteeing correctness or inventing missing evidence.
- **B:** Incorrect for this question. Focused passes reduce attention dilution while integration review checks interactions. Manage deduplication and reconcile findings before release. In this case: An independent reviewer can reduce anchoring without guaranteeing correctness or inventing missing evidence.
- **C:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: An independent reviewer can reduce anchoring without guaranteeing correctness or inventing missing evidence.
- **D:** Correct. Independent review reduces anchoring on the original solution. It still needs the specification, relevant code, and evidence; independence does not guarantee correctness. In this case: An independent reviewer can reduce anchoring without guaranteeing correctness or inventing missing evidence.

### Question 90 — B

Answer: Sample high-confidence outputs within relevant strata. Sample accepted outputs within relevant strata to measure hidden residual error. Ongoing random checks among high-confidence results can discover hidden errors and changing patterns that low-confidence-only review misses. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Review priority should reflect uncertainty and consequences. A high uncalibrated confidence number should not override contradictory evidence. In this case: Sample accepted outputs within relevant strata to measure hidden residual error.
- **B:** Correct. Ongoing random checks among high-confidence results can discover hidden errors and changing patterns that low-confidence-only review misses. In this case: Sample accepted outputs within relevant strata to measure hidden residual error.
- **C:** Incorrect for this question. Averages can hide systematic failures in rare forms or important fields. Segment-level evaluation informs safe automation and review allocation. In this case: Sample accepted outputs within relevant strata to measure hidden residual error.
- **D:** Incorrect for this question. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. In this case: Sample accepted outputs within relevant strata to measure hidden residual error.

### Question 91 — D

Answer: Use supported strict structured output with a schema. Use supported schema-constrained output rather than rely solely on natural-language formatting requests. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Use supported schema-constrained output rather than rely solely on natural-language formatting requests.
- **B:** Incorrect for this question. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Use supported schema-constrained output rather than rely solely on natural-language formatting requests.
- **C:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Use supported schema-constrained output rather than rely solely on natural-language formatting requests.
- **D:** Correct. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Use supported schema-constrained output rather than rely solely on natural-language formatting requests.

### Question 92 — D

Answer: Validate extracted values against evidence and business rules. Validate meaning and units against the source rather than trust typed numeric fields. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Validate meaning and units against the source rather than trust typed numeric fields.
- **B:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Validate meaning and units against the source rather than trust typed numeric fields.
- **C:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Validate meaning and units against the source rather than trust typed numeric fields.
- **D:** Correct. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Validate meaning and units against the source rather than trust typed numeric fields.

### Question 93 — B

Answer: Allow explicit unknown or absent values in the schema. Explicit null or unknown representation differs from a known value labeled other. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. An other category with details can represent valid cases outside an enum. Unclear represents uncertainty and should not be confused with known-but-uncatalogued categories. In this case: Explicit null or unknown representation differs from a known value labeled other.
- **B:** Correct. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Explicit null or unknown representation differs from a known value labeled other.
- **C:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Explicit null or unknown representation differs from a known value labeled other.
- **D:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Explicit null or unknown representation differs from a known value labeled other.

### Question 94 — B

Answer: Use an extensible category plus a detail field. Use other with details instead of fabricate an existing enum value. An other category with details can represent valid cases outside an enum. Unclear represents uncertainty and should not be confused with known-but-uncatalogued categories. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Use other with details instead of fabricate an existing enum value.
- **B:** Correct. An other category with details can represent valid cases outside an enum. Unclear represents uncertainty and should not be confused with known-but-uncatalogued categories. In this case: Use other with details instead of fabricate an existing enum value.
- **C:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Use other with details instead of fabricate an existing enum value.
- **D:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Use other with details instead of fabricate an existing enum value.

### Question 95 — A

Answer: Treat model output as untrusted before rendering or execution. Output must be treated as untrusted for its rendering destination even if JSON is valid. Use destination-appropriate escaping, validation, and permission checks. Valid JSON can still contain executable or malicious values. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Correct. Use destination-appropriate escaping, validation, and permission checks. Valid JSON can still contain executable or malicious values. In this case: Output must be treated as untrusted for its rendering destination even if JSON is valid.
- **B:** Incorrect for this question. Temperature changes next-token sampling behavior where supported. Lowering it does not independently guarantee correct extraction, grounding, or identical execution. In this case: Output must be treated as untrusted for its rendering destination even if JSON is valid.
- **C:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Output must be treated as untrusted for its rendering destination even if JSON is valid.
- **D:** Incorrect for this question. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Output must be treated as untrusted for its rendering destination even if JSON is valid.

### Question 96 — C

Answer: Retry with the document, failed result, and specific validation errors. Provide source, failed result, and exact validation feedback for a bounded correction. Actionable feedback supports correction when evidence exists. Bound attempts and validate the revised result rather than resubmit the same vague request indefinitely. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Retries cannot recover a fact that the available document never contained. Use unknown status, authorized retrieval, clarification, or review instead of fabrication. In this case: Provide source, failed result, and exact validation feedback for a bounded correction.
- **B:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Provide source, failed result, and exact validation feedback for a bounded correction.
- **C:** Correct. Actionable feedback supports correction when evidence exists. Bound attempts and validate the revised result rather than resubmit the same vague request indefinitely. In this case: Provide source, failed result, and exact validation feedback for a bounded correction.
- **D:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Provide source, failed result, and exact validation feedback for a bounded correction.

### Question 97 — D

Answer: Mark missing evidence and route for retrieval or review. Mark the gap and seek authorized evidence or review rather than keep guessing. Retries cannot recover a fact that the available document never contained. Use unknown status, authorized retrieval, clarification, or review instead of fabrication. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Mark the gap and seek authorized evidence or review rather than keep guessing.
- **B:** Incorrect for this question. Actionable feedback supports correction when evidence exists. Bound attempts and validate the revised result rather than resubmit the same vague request indefinitely. In this case: Mark the gap and seek authorized evidence or review rather than keep guessing.
- **C:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Mark the gap and seek authorized evidence or review rather than keep guessing.
- **D:** Correct. Retries cannot recover a fact that the available document never contained. Use unknown status, authorized retrieval, clarification, or review instead of fabrication. In this case: Mark the gap and seek authorized evidence or review rather than keep guessing.

### Question 98 — D

Answer: Preserve conflicting source values with an explicit flag. Retain both attributed values with an explicit conflict rather than silently resolve them. A conflict record enables review and prevents a synthetic answer from hiding disagreement. A valid schema alone does not resolve the underlying facts. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Retain both attributed values with an explicit conflict rather than silently resolve them.
- **B:** Incorrect for this question. Separate calculated_total and stated_total can expose arithmetic or source inconsistencies. Preserve disagreement rather than silently overwrite evidence. In this case: Retain both attributed values with an explicit conflict rather than silently resolve them.
- **C:** Incorrect for this question. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Retain both attributed values with an explicit conflict rather than silently resolve them.
- **D:** Correct. A conflict record enables review and prevents a synthetic answer from hiding disagreement. A valid schema alone does not resolve the underlying facts. In this case: Retain both attributed values with an explicit conflict rather than silently resolve them.

### Question 99 — A

Answer: Use the final assembled message and completion status. Use the assembled completed message and status before validating a final business record. SDK accumulation helpers can provide the complete message. Inspect termination and errors before treating the resulting object as accepted application output. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Correct. SDK accumulation helpers can provide the complete message. Inspect termination and errors before treating the resulting object as accepted application output. In this case: Use the assembled completed message and status before validating a final business record.
- **B:** Incorrect for this question. A response can contain text, tool use, thinking, or other supported blocks. Do not assume content is one string or that the first block is always displayable text. In this case: Use the assembled completed message and status before validating a final business record.
- **C:** Incorrect for this question. Network chunks and content deltas can contain partial strings or JSON. Track event and block boundaries or use SDK helpers before consuming a complete structured value. In this case: Use the assembled completed message and status before validating a final business record.
- **D:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Use the assembled completed message and status before validating a final business record.

### Question 100 — D

Answer: Validate extracted values against evidence and business rules. Source-backed semantic checks remain necessary regardless of tone or structural validity. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. Local study-map skill 6.3 (Output Handling), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

- **A:** Incorrect for this question. An optional field may be omitted; a nullable field may contain null. Design missing-data behavior deliberately instead of forcing invented values. In this case: Source-backed semantic checks remain necessary regardless of tone or structural validity.
- **B:** Incorrect for this question. Constrained schema support targets structural compliance for supported schemas and response modes. Handle refusals, truncation, and compatibility; factual correctness is separate. In this case: Source-backed semantic checks remain necessary regardless of tone or structural validity.
- **C:** Incorrect for this question. Date, unit, and string normalization should be explicit and should not conceal source uncertainty. Validate transformations instead of guessing locale. In this case: Source-backed semantic checks remain necessary regardless of tone or structural validity.
- **D:** Correct. Valid syntax does not prove correct fields, sums, units, identities, or permitted actions. Semantic checks are needed before downstream use. In this case: Source-backed semantic checks remain necessary regardless of tone or structural validity.
