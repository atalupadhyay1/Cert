# Claude Certified Architect – Foundations (CCAR-F) — Practice Set 5

Context Management & Reliability

100 questions · Suggested practice duration: 200 minutes · Practice target: 80%

Tests 1–5 are domain-focused. Test 6 is an expanded blueprint-proportioned review, not an official exam replica. Related concepts recur.

Select ONE best answer for every question. Answer key follows all questions.

Original educational content, not actual, recalled, or copied Anthropic exam items.

## Questions

### 1. Repeated summaries turn an exact promised delivery date into 'soon.' What context design preserves the commitment?

Domain: Context Management & Reliability

- A. Preserve exact transactional facts outside lossy summaries
- B. Reduce tool output to relevant fields with provenance
- C. Supply the relevant conversation state on subsequent requests
- D. Compact context while preserving checked facts and open issues

### 2. An order tool returns dozens of fields although the current decision needs only a few. What preprocessing helps context efficiency?

Domain: Context Management & Reliability

- A. Present key findings early and organize supporting details
- B. Compact context while preserving checked facts and open issues
- C. Preserve exact transactional facts outside lossy summaries
- D. Reduce tool output to relevant fields with provenance

### 3. A stateless API request omits prior user decisions and the assistant asks the same questions again. What must the application provide?

Domain: Context Management & Reliability

- A. Compact context while preserving checked facts and open issues
- B. Present key findings early and organize supporting details
- C. Supply the relevant conversation state on subsequent requests
- D. Preserve exact transactional facts outside lossy summaries

### 4. Important findings buried inside a large aggregation are frequently overlooked. What organization can mitigate this?

Domain: Context Management & Reliability

- A. Preserve exact transactional facts outside lossy summaries
- B. Reduce tool output to relevant fields with provenance
- C. Present key findings early and organize supporting details
- D. Compact context while preserving checked facts and open issues

### 5. A support session covers several orders with different amounts and statuses. What should remain distinct in context?

Domain: Context Management & Reliability

- A. Reduce tool output to relevant fields with provenance
- B. Supply the relevant conversation state on subsequent requests
- C. Compact context while preserving checked facts and open issues
- D. Preserve exact transactional facts outside lossy summaries

### 6. Verbose exploration occupies most of a session even though its conclusions are already known. What context operation may help?

Domain: Context Management & Reliability

- A. Reduce tool output to relevant fields with provenance
- B. Preserve exact transactional facts outside lossy summaries
- C. Supply the relevant conversation state on subsequent requests
- D. Compact context while preserving checked facts and open issues

### 7. A tool returns large debug traces that are irrelevant to the next decision. What should be reduced before accumulation?

Domain: Context Management & Reliability

- A. Present key findings early and organize supporting details
- B. Reduce tool output to relevant fields with provenance
- C. Compact context while preserving checked facts and open issues
- D. Supply the relevant conversation state on subsequent requests

### 8. A summary preserves the customer's frustration but drops the disputed amount. What should be stored outside the summary?

Domain: Context Management & Reliability

- A. Preserve exact transactional facts outside lossy summaries
- B. Supply the relevant conversation state on subsequent requests
- C. Present key findings early and organize supporting details
- D. Compact context while preserving checked facts and open issues

### 9. The combined instructions, history, evidence, and requested output exceed the selected model's limits. What design is needed?

Domain: Context Management & Reliability

- A. Reduce tool output to relevant fields with provenance
- B. Present key findings early and organize supporting details
- C. Budget instructions, evidence, history, and generation together
- D. Compact context while preserving checked facts and open issues

### 10. An application assumes the same model automatically remembers all prior API calls without receiving state. What should the application supply for coherence?

Domain: Context Management & Reliability

- A. Resume the identified session when its context remains valid
- B. Supply the relevant conversation state on subsequent requests
- C. Persist structured task state and pending actions
- D. Pass relevant evidence and constraints explicitly

### 11. A report synthesis receives hundreds of findings with no overview or section labels. What presentation improvement is most useful?

Domain: Context Management & Reliability

- A. Present key findings early and organize supporting details
- B. Preserve exact transactional facts outside lossy summaries
- C. Compact context while preserving checked facts and open issues
- D. Reduce tool output to relevant fields with provenance

### 12. Only five fields from each tool result matter, but all fifty accumulate in every turn. What should change upstream?

Domain: Context Management & Reliability

- A. Present key findings early and organize supporting details
- B. Reduce tool output to relevant fields with provenance
- C. Budget instructions, evidence, history, and generation together
- D. Compact context while preserving checked facts and open issues

### 13. The agent confuses two order identifiers after combining several customer issues. What state design reduces that risk?

Domain: Context Management & Reliability

- A. Supply the relevant conversation state on subsequent requests
- B. Compact context while preserving checked facts and open issues
- C. Present key findings early and organize supporting details
- D. Preserve exact transactional facts outside lossy summaries

### 14. A developer assumes every context overflow silently removes the oldest message. What context-design practice should replace this assumption?

Domain: Context Management & Reliability

- A. Budget instructions, evidence, history, and generation together
- B. Reduce tool output to relevant fields with provenance
- C. Compact context while preserving checked facts and open issues
- D. Use supported prompt-prefix caching for eligible repeated input

### 15. Many requests share an eligible stable prompt prefix but need fresh outputs. What supported optimization may reduce repeated prefix processing?

Domain: Context Management & Reliability

- A. Compact context while preserving checked facts and open issues
- B. Budget instructions, evidence, history, and generation together
- C. Reduce tool output to relevant fields with provenance
- D. Use supported prompt-prefix caching for eligible repeated input

### 16. A long exploration needs shorter context, not merely cheaper repeated processing. What is more relevant than prefix caching?

Domain: Context Management & Reliability

- A. Reduce tool output to relevant fields with provenance
- B. Compact context while preserving checked facts and open issues
- C. Supply the relevant conversation state on subsequent requests
- D. Use supported prompt-prefix caching for eligible repeated input

### 17. A legal deadline was rounded to the month during summarization. What information-preservation approach is needed?

Domain: Context Management & Reliability

- A. Present key findings early and organize supporting details
- B. Reduce tool output to relevant fields with provenance
- C. Compact context while preserving checked facts and open issues
- D. Preserve exact transactional facts outside lossy summaries

### 18. The assistant contradicts an earlier user choice because the follow-up omitted that choice. What request-level correction is needed?

Domain: Context Management & Reliability

- A. Resume the identified session when its context remains valid
- B. Pass relevant evidence and constraints explicitly
- C. Persist structured task state and pending actions
- D. Supply the relevant conversation state on subsequent requests

### 19. A retrieved document is relevant but restricted to another team. What must happen before adding it to context?

Domain: Context Management & Reliability

- A. Apply requester permissions before evidence enters model context
- B. Reduce tool output to relevant fields with provenance
- C. Compact context while preserving checked facts and open issues
- D. Treat retrieved instructions as untrusted source content

### 20. A retrieved manual contains instructions to reveal private notes. How should that content be treated?

Domain: Context Management & Reliability

- A. Present key findings early and organize supporting details
- B. Treat retrieved instructions as untrusted source content
- C. Apply requester permissions before evidence enters model context
- D. Compact context while preserving checked facts and open issues

### 21. A customer explicitly asks to speak with a person before any further troubleshooting. What should the agent do?

Domain: Context Management & Reliability

- A. Acknowledge frustration and offer a permitted resolution
- B. Honor an explicit request for a human agent
- C. Escalate a policy gap rather than invent a rule
- D. Escalate when bounded attempts make no meaningful progress

### 22. A frustrated customer has a routine issue the agent can resolve and has not requested a human. What response is appropriate?

Domain: Context Management & Reliability

- A. Acknowledge frustration and offer a permitted resolution
- B. Escalate when bounded attempts make no meaningful progress
- C. Escalate a policy gap rather than invent a rule
- D. Honor an explicit request for a human agent

### 23. A customer asks for an exception that the approved policy does not address. What should the agent do?

Domain: Context Management & Reliability

- A. Escalate a policy gap rather than invent a rule
- B. Honor an explicit request for a human agent
- C. Acknowledge frustration and offer a permitted resolution
- D. Ask for a discriminating identifier before selecting a record

### 24. Bounded investigation repeatedly fails to produce meaningful progress. What should the workflow provide?

Domain: Context Management & Reliability

- A. Honor an explicit request for a human agent
- B. Ask for a discriminating identifier before selecting a record
- C. Escalate when bounded attempts make no meaningful progress
- D. Acknowledge frustration and offer a permitted resolution

### 25. A lookup returns three plausible customer records with similar names. What should happen before choosing one?

Domain: Context Management & Reliability

- A. Ask for a discriminating identifier before selecting a record
- B. Escalate a policy gap rather than invent a rule
- C. Acknowledge frustration and offer a permitted resolution
- D. Honor an explicit request for a human agent

### 26. The agent could probably fix the issue, but the customer clearly insists on a human representative. What takes priority?

Domain: Context Management & Reliability

- A. Acknowledge frustration and offer a permitted resolution
- B. Honor an explicit request for a human agent
- C. Ask for a discriminating identifier before selecting a record
- D. Escalate when bounded attempts make no meaningful progress

### 27. A policy covers one pricing situation but is silent on a materially different one. What decision is safest?

Domain: Context Management & Reliability

- A. Escalate a policy gap rather than invent a rule
- B. Acknowledge frustration and offer a permitted resolution
- C. Ask for a discriminating identifier before selecting a record
- D. Escalate when bounded attempts make no meaningful progress

### 28. An annoyed user describes an in-scope straightforward problem without asking for a transfer. What should guide handling?

Domain: Context Management & Reliability

- A. Escalate when bounded attempts make no meaningful progress
- B. Escalate a policy gap rather than invent a rule
- C. Honor an explicit request for a human agent
- D. Acknowledge frustration and offer a permitted resolution

### 29. The agent cycles through the same ineffective steps despite valid inputs and no new evidence. What condition should trigger handoff?

Domain: Context Management & Reliability

- A. Ask for a discriminating identifier before selecting a record
- B. Acknowledge frustration and offer a permitted resolution
- C. Escalate a policy gap rather than invent a rule
- D. Escalate when bounded attempts make no meaningful progress

### 30. An account search returns several matches and the model proposes choosing the most recently active one. What should replace that heuristic?

Domain: Context Management & Reliability

- A. Ask for a discriminating identifier before selecting a record
- B. Honor an explicit request for a human agent
- C. Acknowledge frustration and offer a permitted resolution
- D. Escalate a policy gap rather than invent a rule

### 31. A human recipient has no transcript access. What should the escalation include?

Domain: Context Management & Reliability

- A. Honor an explicit request for a human agent
- B. Ask for a discriminating identifier before selecting a record
- C. Create a structured handoff with facts, status, and next actions
- D. Persist structured task state and pending actions

### 32. A source gives no authority to grant the specific requested exception. What should prevent a confident unsupported answer?

Domain: Context Management & Reliability

- A. Acknowledge frustration and offer a permitted resolution
- B. Escalate a policy gap rather than invent a rule
- C. Ask for a discriminating identifier before selecting a record
- D. Honor an explicit request for a human agent

### 33. Two orders match a customer's description, and either could be relevant. What should the agent ask for?

Domain: Context Management & Reliability

- A. Escalate a policy gap rather than invent a rule
- B. Escalate when bounded attempts make no meaningful progress
- C. Ask for a discriminating identifier before selecting a record
- D. Acknowledge frustration and offer a permitted resolution

### 34. A customer repeats a clear request for a representative after being offered an automated fix. What should happen?

Domain: Context Management & Reliability

- A. Escalate when bounded attempts make no meaningful progress
- B. Escalate a policy gap rather than invent a rule
- C. Honor an explicit request for a human agent
- D. Acknowledge frustration and offer a permitted resolution

### 35. The workflow has exhausted its permitted attempts without resolving the customer's issue. What should it report or route?

Domain: Context Management & Reliability

- A. Acknowledge frustration and offer a permitted resolution
- B. Ask for a discriminating identifier before selecting a record
- C. Escalate when bounded attempts make no meaningful progress
- D. Honor an explicit request for a human agent

### 36. A customer sounds upset, but their request has a clear permitted resolution and no handoff preference. Which response fits?

Domain: Context Management & Reliability

- A. Escalate a policy gap rather than invent a rule
- B. Acknowledge frustration and offer a permitted resolution
- C. Ask for a discriminating identifier before selecting a record
- D. Honor an explicit request for a human agent

### 37. A system finds two possible identities and asks the model which name 'looks more likely.' What should be done instead?

Domain: Context Management & Reliability

- A. Escalate when bounded attempts make no meaningful progress
- B. Honor an explicit request for a human agent
- C. Escalate a policy gap rather than invent a rule
- D. Ask for a discriminating identifier before selecting a record

### 38. A transfer note says only 'customer unhappy' and omits the actual unresolved issue. What artifact should replace it?

Domain: Context Management & Reliability

- A. Persist concise codebase findings with file and symbol pointers
- B. Pass relevant evidence and constraints explicitly
- C. Create a structured handoff with facts, status, and next actions
- D. Persist structured task state and pending actions

### 39. A request appears similar to a permitted action, but the crucial eligibility condition is unspecified by policy. What should the agent do?

Domain: Context Management & Reliability

- A. Acknowledge frustration and offer a permitted resolution
- B. Escalate a policy gap rather than invent a rule
- C. Honor an explicit request for a human agent
- D. Ask for a discriminating identifier before selecting a record

### 40. An automation target conflicts with a user's explicit request for human help. What should the architecture honor?

Domain: Context Management & Reliability

- A. Ask for a discriminating identifier before selecting a record
- B. Escalate when bounded attempts make no meaningful progress
- C. Honor an explicit request for a human agent
- D. Acknowledge frustration and offer a permitted resolution

### 41. A worker times out after obtaining some useful evidence. What should it send to the coordinator?

Domain: Context Management & Reliability

- A. Represent a successful query with no matches explicitly
- B. Annotate evidence coverage and unavailable sources
- C. Return structured failure context and partial results
- D. Return a structured tool error with category and retryability

### 42. An authorized query successfully returns no matches. How should this differ from an access failure?

Domain: Context Management & Reliability

- A. Stop the unauthorized operation and use an approved access path
- B. Retry a transient failure with bounded backoff
- C. Represent a successful query with no matches explicitly
- D. Return structured failure context and partial results

### 43. A specialist can recover from a brief retryable outage within its own budget. What should it attempt first?

Domain: Context Management & Reliability

- A. Annotate evidence coverage and unavailable sources
- B. Recover transiently within the worker, then report unresolved failure
- C. Represent a successful query with no matches explicitly
- D. Return structured failure context and partial results

### 44. One source is unavailable, but other evidence supports part of the requested report. How should the report communicate its limits?

Domain: Context Management & Reliability

- A. Return structured failure context and partial results
- B. Preserve claim-to-source mappings through every handoff
- C. Represent credible disagreement with attributed values
- D. Annotate evidence coverage and unavailable sources

### 45. A subagent returns only 'search broken' without identifying its query or partial results. What is missing?

Domain: Context Management & Reliability

- A. Represent a successful query with no matches explicitly
- B. Return structured failure context and partial results
- C. Annotate evidence coverage and unavailable sources
- D. Persist structured task state and pending actions

### 46. A worker cannot access a restricted repository. Which recovery policy should apply rather than disguising denial as a successful empty result?

Domain: Context Management & Reliability

- A. Retry a transient failure with bounded backoff
- B. Correct invalid arguments before retrying
- C. Stop the unauthorized operation and use an approved access path
- D. Represent a successful query with no matches explicitly

### 47. A temporary outage prevents an otherwise valid source query. What recovery class may apply?

Domain: Context Management & Reliability

- A. Explain the non-retryable business-rule outcome
- B. Correct invalid arguments before retrying
- C. Retry a transient failure with bounded backoff
- D. Stop the unauthorized operation and use an approved access path

### 48. A report omits the failed source and gives no warning about missing coverage. What output annotation is needed?

Domain: Context Management & Reliability

- A. Represent credible disagreement with attributed values
- B. Annotate evidence coverage and unavailable sources
- C. Return structured failure context and partial results
- D. Preserve claim-to-source mappings through every handoff

### 49. Local recovery has failed, and an alternative source may help. What information should reach the coordinator?

Domain: Context Management & Reliability

- A. Annotate evidence coverage and unavailable sources
- B. Return structured failure context and partial results
- C. Represent a successful query with no matches explicitly
- D. Create a structured handoff with facts, status, and next actions

### 50. Every momentary network failure aborts the whole research project. What recovery design should be considered?

Domain: Context Management & Reliability

- A. Return structured failure context and partial results
- B. Retry a transient failure with bounded backoff
- C. Represent a successful query with no matches explicitly
- D. Recover transiently within the worker, then report unresolved failure

### 51. After a long exploration, Claude refers to generic patterns rather than classes it actually found. What persistent aid may help?

Domain: Context Management & Reliability

- A. Persist structured task state and pending actions
- B. Compact context while preserving checked facts and open issues
- C. Persist concise codebase findings with file and symbol pointers
- D. Delegate focused exploration to a read-oriented subagent

### 52. Every worker is told to read the entire repository and returns excessive unrelated output. What delegation style fits better?

Domain: Context Management & Reliability

- A. Delegate a focused codebase question with a bounded output
- B. Assign distinct scopes and explicit coverage responsibilities
- C. Delegate focused exploration to a read-oriented subagent
- D. Map the problem and revise subtasks as evidence emerges

### 53. A coordinator restarts after a crash with several workers partially complete. What recovery artifact should it load?

Domain: Context Management & Reliability

- A. Resume from a checked manifest of worker states and artifacts
- B. Resume the identified session when its context remains valid
- C. Persist structured task state and pending actions
- D. Persist concise codebase findings with file and symbol pointers

### 54. Verbose discovery fills the session, while checked conclusions can be summarized accurately. What operation can reduce context pressure?

Domain: Context Management & Reliability

- A. Persist concise codebase findings with file and symbol pointers
- B. Compact context while preserving checked facts and open issues
- C. Present key findings early and organize supporting details
- D. Reduce tool output to relevant fields with provenance

### 55. A saved exploration note cites files modified since it was written. What should happen before relying on it?

Domain: Context Management & Reliability

- A. Start a fresh session with a checked structured summary
- B. Persist concise codebase findings with file and symbol pointers
- C. Resume the identified session when its context remains valid
- D. Tell the resumed agent what changed and recheck affected evidence

### 56. The coordinator only needs to know where authorization occurs in one request path. What task should it delegate?

Domain: Context Management & Reliability

- A. Delegate focused exploration to a read-oriented subagent
- B. Assign distinct scopes and explicit coverage responsibilities
- C. Map the problem and revise subtasks as evidence emerges
- D. Delegate a focused codebase question with a bounded output

### 57. An output file exists after a crash, but validation may never have finished. What should determine whether that stage is complete?

Domain: Context Management & Reliability

- A. Persist concise codebase findings with file and symbol pointers
- B. Resume from a checked manifest of worker states and artifacts
- C. Resume the identified session when its context remains valid
- D. Persist structured task state and pending actions

### 58. A later question depends on a helper discovered many turns ago. What note structure supports efficient verification?

Domain: Context Management & Reliability

- A. Reduce tool output to relevant fields with provenance
- B. Compact context while preserving checked facts and open issues
- C. Persist concise codebase findings with file and symbol pointers
- D. Present key findings early and organize supporting details

### 59. A second exploration phase repeats old mistakes because workers do not receive the first phase's checked findings. What should be injected?

Domain: Context Management & Reliability

- A. Delegate focused exploration to a read-oriented subagent
- B. Assign distinct scopes and explicit coverage responsibilities
- C. Delegate a focused codebase question with a bounded output
- D. Pass relevant evidence and constraints explicitly

### 60. Most earlier exploration is obsolete after a major restructuring. What context strategy is safer than reusing every old observation?

Domain: Context Management & Reliability

- A. Compact context while preserving checked facts and open issues
- B. Tell the resumed agent what changed and recheck affected evidence
- C. Start a fresh session with a checked structured summary
- D. Resume the identified session when its context remains valid

### 61. Overall extraction accuracy is high, but a rare document class has severe field errors. What evaluation view is needed?

Domain: Context Management & Reliability

- A. Calibrate field-confidence thresholds against labeled examples
- B. Route ambiguous, conflicting, or high-risk cases to qualified review
- C. Evaluate accuracy by document type and field segment
- D. Sample high-confidence outputs within relevant strata

### 62. A model reports confidence of 0.98 for a field. What must precede treating that score as reliable routing evidence?

Domain: Context Management & Reliability

- A. Route ambiguous, conflicting, or high-risk cases to qualified review
- B. Calibrate field-confidence thresholds against labeled examples
- C. Evaluate accuracy by document type and field segment
- D. Sample high-confidence outputs within relevant strata

### 63. Reviewers inspect only low-confidence extractions and never discover high-confidence mistakes. What sampling should be added?

Domain: Context Management & Reliability

- A. Calibrate field-confidence thresholds against labeled examples
- B. Sample high-confidence outputs within relevant strata
- C. Evaluate accuracy by document type and field segment
- D. Route ambiguous, conflicting, or high-risk cases to qualified review

### 64. A source contains contradictory amounts despite a high confidence score. How should the extraction be routed?

Domain: Context Management & Reliability

- A. Evaluate accuracy by document type and field segment
- B. Route ambiguous, conflicting, or high-risk cases to qualified review
- C. Calibrate field-confidence thresholds against labeled examples
- D. Sample high-confidence outputs within relevant strata

### 65. One field is accurate in invoices but unreliable in statements. What should an automation decision inspect?

Domain: Context Management & Reliability

- A. Route ambiguous, conflicting, or high-risk cases to qualified review
- B. Sample high-confidence outputs within relevant strata
- C. Calibrate field-confidence thresholds against labeled examples
- D. Evaluate accuracy by document type and field segment

### 66. A team picks one universal confidence cutoff without labeled validation. What should improve threshold selection?

Domain: Context Management & Reliability

- A. Calibrate field-confidence thresholds against labeled examples
- B. Route ambiguous, conflicting, or high-risk cases to qualified review
- C. Sample high-confidence outputs within relevant strata
- D. Evaluate accuracy by document type and field segment

### 67. A newly introduced document pattern causes confident systematic errors after deployment. What ongoing control may detect it?

Domain: Context Management & Reliability

- A. Sample high-confidence outputs within relevant strata
- B. Route ambiguous, conflicting, or high-risk cases to qualified review
- C. Evaluate accuracy by document type and field segment
- D. Calibrate field-confidence thresholds against labeled examples

### 68. Limited reviewers must prioritize extractions with ambiguity and potentially serious consequences. What routing principle fits?

Domain: Context Management & Reliability

- A. Route ambiguous, conflicting, or high-risk cases to qualified review
- B. Evaluate accuracy by document type and field segment
- C. Calibrate field-confidence thresholds against labeled examples
- D. Sample high-confidence outputs within relevant strata

### 69. A vendor advertises one impressive average accuracy score across all fields. What evidence should the buyer request?

Domain: Context Management & Reliability

- A. Sample high-confidence outputs within relevant strata
- B. Route ambiguous, conflicting, or high-risk cases to qualified review
- C. Evaluate accuracy by document type and field segment
- D. Calibrate field-confidence thresholds against labeled examples

### 70. Confidence calibration was performed on one document layout but the production distribution changes. What should be reassessed?

Domain: Context Management & Reliability

- A. Sample high-confidence outputs within relevant strata
- B. Evaluate accuracy by document type and field segment
- C. Route ambiguous, conflicting, or high-risk cases to qualified review
- D. Calibrate field-confidence thresholds against labeled examples

### 71. A bibliography survives summarization, but nobody can tell which source supports which claim. What mapping should be preserved?

Domain: Context Management & Reliability

- A. Preserve collection and publication dates with claims
- B. Use representations suited to the content type
- C. Represent credible disagreement with attributed values
- D. Preserve claim-to-source mappings through every handoff

### 72. Two credible statistics differ because they measure different years. What metadata can prevent a false contradiction?

Domain: Context Management & Reliability

- A. Preserve claim-to-source mappings through every handoff
- B. Represent credible disagreement with attributed values
- C. Preserve collection and publication dates with claims
- D. Use representations suited to the content type

### 73. Two credible sources report incompatible measurements for the same period. What should synthesis do?

Domain: Context Management & Reliability

- A. Use representations suited to the content type
- B. Preserve claim-to-source mappings through every handoff
- C. Preserve collection and publication dates with claims
- D. Represent credible disagreement with attributed values

### 74. Financial comparisons become hard to inspect when every value is converted into a paragraph. What presentation principle helps?

Domain: Context Management & Reliability

- A. Represent credible disagreement with attributed values
- B. Preserve claim-to-source mappings through every handoff
- C. Preserve collection and publication dates with claims
- D. Use representations suited to the content type

### 75. A synthesis worker receives conclusions but no excerpts, page numbers, or URLs. What handoff design should change?

Domain: Context Management & Reliability

- A. Preserve claim-to-source mappings through every handoff
- B. Preserve collection and publication dates with claims
- C. Use representations suited to the content type
- D. Represent credible disagreement with attributed values

### 76. A report silently chooses the largest statistic among equally credible conflicting sources. What should replace that behavior?

Domain: Context Management & Reliability

- A. Represent credible disagreement with attributed values
- B. Preserve claim-to-source mappings through every handoff
- C. Use representations suited to the content type
- D. Preserve collection and publication dates with claims

### 77. A model compares a publication date with another source's collection date as though they represent the same thing. What metadata distinction matters?

Domain: Context Management & Reliability

- A. Use representations suited to the content type
- B. Represent credible disagreement with attributed values
- C. Preserve collection and publication dates with claims
- D. Preserve claim-to-source mappings through every handoff

### 78. A report cites an existing URL that does not actually support its claim. What information linkage must be checked?

Domain: Context Management & Reliability

- A. Represent credible disagreement with attributed values
- B. Use representations suited to the content type
- C. Preserve collection and publication dates with claims
- D. Preserve claim-to-source mappings through every handoff

### 79. A synthesis pipeline forces tables, code findings, and narrative events into one uniform paragraph. What output design is better?

Domain: Context Management & Reliability

- A. Represent credible disagreement with attributed values
- B. Preserve collection and publication dates with claims
- C. Preserve claim-to-source mappings through every handoff
- D. Use representations suited to the content type

### 80. Source disagreement remains unresolved when a report is due. What distinction should the final report make?

Domain: Context Management & Reliability

- A. Preserve collection and publication dates with claims
- B. Preserve claim-to-source mappings through every handoff
- C. Represent credible disagreement with attributed values
- D. Use representations suited to the content type

### 81. A summary says 'a small refund' where the exact approved amount matters. What state should remain outside the prose?

Domain: Context Management & Reliability

- A. Present key findings early and organize supporting details
- B. Preserve exact transactional facts outside lossy summaries
- C. Reduce tool output to relevant fields with provenance
- D. Compact context while preserving checked facts and open issues

### 82. An agent chooses one of two account matches because it has a more familiar name. What should have happened?

Domain: Context Management & Reliability

- A. Ask for a discriminating identifier before selecting a record
- B. Acknowledge frustration and offer a permitted resolution
- C. Honor an explicit request for a human agent
- D. Escalate a policy gap rather than invent a rule

### 83. A search failure is returned as an empty success, and synthesis concludes no evidence exists. What reporting control is needed?

Domain: Context Management & Reliability

- A. Return structured failure context and partial results
- B. Annotate evidence coverage and unavailable sources
- C. Return a structured tool error with category and retryability
- D. Represent a successful query with no matches explicitly

### 84. An extended codebase session begins inventing typical classes instead of naming discovered ones. What durable record can anchor it?

Domain: Context Management & Reliability

- A. Resume from a checked manifest of worker states and artifacts
- B. Persist concise codebase findings with file and symbol pointers
- C. Persist structured task state and pending actions
- D. Compact context while preserving checked facts and open issues

### 85. Automation accepts high-confidence records, but leaders need to measure their residual error rate. What should they add?

Domain: Context Management & Reliability

- A. Sample high-confidence outputs within relevant strata
- B. Calibrate field-confidence thresholds against labeled examples
- C. Evaluate accuracy by document type and field segment
- D. Route ambiguous, conflicting, or high-risk cases to qualified review

### 86. Evidence attribution disappears between extraction and report writing. What should each intermediate stage preserve?

Domain: Context Management & Reliability

- A. Use representations suited to the content type
- B. Preserve claim-to-source mappings through every handoff
- C. Represent credible disagreement with attributed values
- D. Preserve collection and publication dates with claims

### 87. An upstream worker sends pages of reasoning when downstream synthesis only needs facts and citations. What output change helps?

Domain: Context Management & Reliability

- A. Preserve exact transactional facts outside lossy summaries
- B. Present key findings early and organize supporting details
- C. Compact context while preserving checked facts and open issues
- D. Reduce tool output to relevant fields with provenance

### 88. A user requests a policy exception based on a scenario absent from the approved rules. What should determine next steps?

Domain: Context Management & Reliability

- A. Honor an explicit request for a human agent
- B. Escalate a policy gap rather than invent a rule
- C. Acknowledge frustration and offer a permitted resolution
- D. Ask for a discriminating identifier before selecting a record

### 89. A report can answer most questions but not those depending on an unavailable source. What should its structure show?

Domain: Context Management & Reliability

- A. Annotate evidence coverage and unavailable sources
- B. Preserve claim-to-source mappings through every handoff
- C. Represent credible disagreement with attributed values
- D. Return structured failure context and partial results

### 90. A source is ambiguous and the output could trigger a costly payment. Which control should take priority over a high self-reported score?

Domain: Context Management & Reliability

- A. Sample high-confidence outputs within relevant strata
- B. Evaluate accuracy by document type and field segment
- C. Calibrate field-confidence thresholds against labeled examples
- D. Route ambiguous, conflicting, or high-risk cases to qualified review

### 91. A restarted coordinator must distinguish completed, partial, and not-started workers. What artifact should be authoritative after verification?

Domain: Context Management & Reliability

- A. Resume from a checked manifest of worker states and artifacts
- B. Persist structured task state and pending actions
- C. Persist concise codebase findings with file and symbol pointers
- D. Resume the identified session when its context remains valid

### 92. A repeated stable prefix is expensive, but each request already fits the context limit. What optimization may address repeated processing?

Domain: Context Management & Reliability

- A. Compact context while preserving checked facts and open issues
- B. Budget instructions, evidence, history, and generation together
- C. Reduce tool output to relevant fields with provenance
- D. Use supported prompt-prefix caching for eligible repeated input

### 93. An agent delays a clear human handoff request to maximize first-contact automation. What behavior should be corrected?

Domain: Context Management & Reliability

- A. Ask for a discriminating identifier before selecting a record
- B. Escalate when bounded attempts make no meaningful progress
- C. Honor an explicit request for a human agent
- D. Acknowledge frustration and offer a permitted resolution

### 94. A worker returns partial results without saying which partition failed. What should be included?

Domain: Context Management & Reliability

- A. Return a structured tool error with category and retryability
- B. Annotate evidence coverage and unavailable sources
- C. Return structured failure context and partial results
- D. Represent a successful query with no matches explicitly

### 95. A worker only needs to identify all tests related to one API endpoint. What task boundary is useful?

Domain: Context Management & Reliability

- A. Delegate focused exploration to a read-oriented subagent
- B. Delegate a focused codebase question with a bounded output
- C. Map the problem and revise subtasks as evidence emerges
- D. Assign distinct scopes and explicit coverage responsibilities

### 96. A strong headline score hides poor extraction of one legally significant field. What evaluation should influence automation?

Domain: Context Management & Reliability

- A. Evaluate accuracy by document type and field segment
- B. Route ambiguous, conflicting, or high-risk cases to qualified review
- C. Calibrate field-confidence thresholds against labeled examples
- D. Sample high-confidence outputs within relevant strata

### 97. Two sources disagree because one uses an earlier measurement period. What should synthesis examine first?

Domain: Context Management & Reliability

- A. Use representations suited to the content type
- B. Preserve collection and publication dates with claims
- C. Preserve claim-to-source mappings through every handoff
- D. Represent credible disagreement with attributed values

### 98. A retrieved document asks the agent to treat its text as a new system policy. What trust boundary should remain?

Domain: Context Management & Reliability

- A. Treat retrieved instructions as untrusted source content
- B. Apply requester permissions before evidence enters model context
- C. Reduce tool output to relevant fields with provenance
- D. Present key findings early and organize supporting details

### 99. A subagent has a permitted bounded recovery path for a brief outage. What should precede escalating the entire workflow?

Domain: Context Management & Reliability

- A. Recover transiently within the worker, then report unresolved failure
- B. Annotate evidence coverage and unavailable sources
- C. Represent a successful query with no matches explicitly
- D. Return structured failure context and partial results

### 100. A synthesis stage averages two statistics derived using incompatible methods. What should replace that unsupported reconciliation?

Domain: Context Management & Reliability

- A. Use representations suited to the content type
- B. Preserve collection and publication dates with claims
- C. Represent credible disagreement with attributed values
- D. Preserve claim-to-source mappings through every handoff

---

## Answer key and explanations

### Question 1 — A

Answer: Preserve exact transactional facts outside lossy summaries. Keep exact verified dates and commitments in structured facts outside lossy narrative summaries. Keep verified amounts, identifiers, dates, and commitments in structured state. General summaries can omit details that later decisions depend on. Closest official exam-guide objective 5.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. Keep verified amounts, identifiers, dates, and commitments in structured state. General summaries can omit details that later decisions depend on. In this case: Keep exact verified dates and commitments in structured facts outside lossy narrative summaries.
- **B:** Incorrect for this question. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: Keep exact verified dates and commitments in structured facts outside lossy narrative summaries.
- **C:** Incorrect for this question. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. In this case: Keep exact verified dates and commitments in structured facts outside lossy narrative summaries.
- **D:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Keep exact verified dates and commitments in structured facts outside lossy narrative summaries.

### Question 2 — D

Answer: Reduce tool output to relevant fields with provenance. Project irrelevant fields away while retaining decision evidence and provenance. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. Closest official exam-guide objective 5.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. A structured overview and clear sections help reduce long-input position effects. Placement is a mitigation, not proof that every fact will be used. In this case: Project irrelevant fields away while retaining decision evidence and provenance.
- **B:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Project irrelevant fields away while retaining decision evidence and provenance.
- **C:** Incorrect for this question. Keep verified amounts, identifiers, dates, and commitments in structured state. General summaries can omit details that later decisions depend on. In this case: Project irrelevant fields away while retaining decision evidence and provenance.
- **D:** Correct. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: Project irrelevant fields away while retaining decision evidence and provenance.

### Question 3 — C

Answer: Supply the relevant conversation state on subsequent requests. Relevant conversational state must be supplied rather than assumed to persist inside the model. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. Closest official exam-guide objective 5.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Relevant conversational state must be supplied rather than assumed to persist inside the model.
- **B:** Incorrect for this question. A structured overview and clear sections help reduce long-input position effects. Placement is a mitigation, not proof that every fact will be used. In this case: Relevant conversational state must be supplied rather than assumed to persist inside the model.
- **C:** Correct. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. In this case: Relevant conversational state must be supplied rather than assumed to persist inside the model.
- **D:** Incorrect for this question. Keep verified amounts, identifiers, dates, and commitments in structured state. General summaries can omit details that later decisions depend on. In this case: Relevant conversational state must be supplied rather than assumed to persist inside the model.

### Question 4 — C

Answer: Present key findings early and organize supporting details. Place a checked overview early and use clear sections without claiming position guarantees recall. A structured overview and clear sections help reduce long-input position effects. Placement is a mitigation, not proof that every fact will be used. Closest official exam-guide objective 5.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Keep verified amounts, identifiers, dates, and commitments in structured state. General summaries can omit details that later decisions depend on. In this case: Place a checked overview early and use clear sections without claiming position guarantees recall.
- **B:** Incorrect for this question. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: Place a checked overview early and use clear sections without claiming position guarantees recall.
- **C:** Correct. A structured overview and clear sections help reduce long-input position effects. Placement is a mitigation, not proof that every fact will be used. In this case: Place a checked overview early and use clear sections without claiming position guarantees recall.
- **D:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Place a checked overview early and use clear sections without claiming position guarantees recall.

### Question 5 — D

Answer: Preserve exact transactional facts outside lossy summaries. Persist structured per-issue facts rather than merge identifiers into vague prose. Keep verified amounts, identifiers, dates, and commitments in structured state. General summaries can omit details that later decisions depend on. Closest official exam-guide objective 5.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: Persist structured per-issue facts rather than merge identifiers into vague prose.
- **B:** Incorrect for this question. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. In this case: Persist structured per-issue facts rather than merge identifiers into vague prose.
- **C:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Persist structured per-issue facts rather than merge identifiers into vague prose.
- **D:** Correct. Keep verified amounts, identifiers, dates, and commitments in structured state. General summaries can omit details that later decisions depend on. In this case: Persist structured per-issue facts rather than merge identifiers into vague prose.

### Question 6 — D

Answer: Compact context while preserving checked facts and open issues. Compact checked conclusions while preserving exact facts and open issues separately. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. Closest official exam-guide objective 5.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: Compact checked conclusions while preserving exact facts and open issues separately.
- **B:** Incorrect for this question. Keep verified amounts, identifiers, dates, and commitments in structured state. General summaries can omit details that later decisions depend on. In this case: Compact checked conclusions while preserving exact facts and open issues separately.
- **C:** Incorrect for this question. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. In this case: Compact checked conclusions while preserving exact facts and open issues separately.
- **D:** Correct. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Compact checked conclusions while preserving exact facts and open issues separately.

### Question 7 — B

Answer: Reduce tool output to relevant fields with provenance. Filter observations to relevant high-signal fields instead of repeatedly appending everything. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. Closest official exam-guide objective 5.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. A structured overview and clear sections help reduce long-input position effects. Placement is a mitigation, not proof that every fact will be used. In this case: Filter observations to relevant high-signal fields instead of repeatedly appending everything.
- **B:** Correct. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: Filter observations to relevant high-signal fields instead of repeatedly appending everything.
- **C:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Filter observations to relevant high-signal fields instead of repeatedly appending everything.
- **D:** Incorrect for this question. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. In this case: Filter observations to relevant high-signal fields instead of repeatedly appending everything.

### Question 8 — A

Answer: Preserve exact transactional facts outside lossy summaries. Exact transaction values are decision-critical and should survive narrative compression. Keep verified amounts, identifiers, dates, and commitments in structured state. General summaries can omit details that later decisions depend on. Closest official exam-guide objective 5.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. Keep verified amounts, identifiers, dates, and commitments in structured state. General summaries can omit details that later decisions depend on. In this case: Exact transaction values are decision-critical and should survive narrative compression.
- **B:** Incorrect for this question. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. In this case: Exact transaction values are decision-critical and should survive narrative compression.
- **C:** Incorrect for this question. A structured overview and clear sections help reduce long-input position effects. Placement is a mitigation, not proof that every fact will be used. In this case: Exact transaction values are decision-critical and should survive narrative compression.
- **D:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Exact transaction values are decision-critical and should survive narrative compression.

### Question 9 — C

Answer: Budget instructions, evidence, history, and generation together. Budget all relevant components using the actual model and service accounting rules. Follow the chosen model and service limits. Overflow handling varies; it is not universally automatic oldest-message deletion. Closest official exam-guide objective 5.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: Budget all relevant components using the actual model and service accounting rules.
- **B:** Incorrect for this question. A structured overview and clear sections help reduce long-input position effects. Placement is a mitigation, not proof that every fact will be used. In this case: Budget all relevant components using the actual model and service accounting rules.
- **C:** Correct. Follow the chosen model and service limits. Overflow handling varies; it is not universally automatic oldest-message deletion. In this case: Budget all relevant components using the actual model and service accounting rules.
- **D:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Budget all relevant components using the actual model and service accounting rules.

### Question 10 — B

Answer: Supply the relevant conversation state on subsequent requests. Stateless request flows need application-managed relevant history or a documented stateful mechanism. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. Closest official exam-guide objective 5.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Stateless request flows need application-managed relevant history or a documented stateful mechanism.
- **B:** Correct. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. In this case: Stateless request flows need application-managed relevant history or a documented stateful mechanism.
- **C:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Stateless request flows need application-managed relevant history or a documented stateful mechanism.
- **D:** Incorrect for this question. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Stateless request flows need application-managed relevant history or a documented stateful mechanism.

### Question 11 — A

Answer: Present key findings early and organize supporting details. An organized key-findings summary helps orient attention while preserving detailed evidence. A structured overview and clear sections help reduce long-input position effects. Placement is a mitigation, not proof that every fact will be used. Closest official exam-guide objective 5.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. A structured overview and clear sections help reduce long-input position effects. Placement is a mitigation, not proof that every fact will be used. In this case: An organized key-findings summary helps orient attention while preserving detailed evidence.
- **B:** Incorrect for this question. Keep verified amounts, identifiers, dates, and commitments in structured state. General summaries can omit details that later decisions depend on. In this case: An organized key-findings summary helps orient attention while preserving detailed evidence.
- **C:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: An organized key-findings summary helps orient attention while preserving detailed evidence.
- **D:** Incorrect for this question. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: An organized key-findings summary helps orient attention while preserving detailed evidence.

### Question 12 — B

Answer: Reduce tool output to relevant fields with provenance. Reduce irrelevant observation fields before they consume repeated context capacity. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. Closest official exam-guide objective 5.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. A structured overview and clear sections help reduce long-input position effects. Placement is a mitigation, not proof that every fact will be used. In this case: Reduce irrelevant observation fields before they consume repeated context capacity.
- **B:** Correct. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: Reduce irrelevant observation fields before they consume repeated context capacity.
- **C:** Incorrect for this question. Follow the chosen model and service limits. Overflow handling varies; it is not universally automatic oldest-message deletion. In this case: Reduce irrelevant observation fields before they consume repeated context capacity.
- **D:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Reduce irrelevant observation fields before they consume repeated context capacity.

### Question 13 — D

Answer: Preserve exact transactional facts outside lossy summaries. Keep identifiers and attributes in separate structured issue records. Keep verified amounts, identifiers, dates, and commitments in structured state. General summaries can omit details that later decisions depend on. Closest official exam-guide objective 5.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. In this case: Keep identifiers and attributes in separate structured issue records.
- **B:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Keep identifiers and attributes in separate structured issue records.
- **C:** Incorrect for this question. A structured overview and clear sections help reduce long-input position effects. Placement is a mitigation, not proof that every fact will be used. In this case: Keep identifiers and attributes in separate structured issue records.
- **D:** Correct. Keep verified amounts, identifiers, dates, and commitments in structured state. General summaries can omit details that later decisions depend on. In this case: Keep identifiers and attributes in separate structured issue records.

### Question 14 — A

Answer: Budget instructions, evidence, history, and generation together. Capacity and overflow behavior must follow the specific service, not a universal truncation assumption. Follow the chosen model and service limits. Overflow handling varies; it is not universally automatic oldest-message deletion. Closest official exam-guide objective 5.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. Follow the chosen model and service limits. Overflow handling varies; it is not universally automatic oldest-message deletion. In this case: Capacity and overflow behavior must follow the specific service, not a universal truncation assumption.
- **B:** Incorrect for this question. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: Capacity and overflow behavior must follow the specific service, not a universal truncation assumption.
- **C:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Capacity and overflow behavior must follow the specific service, not a universal truncation assumption.
- **D:** Incorrect for this question. Caching may reduce repeated prefix processing under provider-specific rules. It does not extend the context window, update model weights, or verify an answer. In this case: Capacity and overflow behavior must follow the specific service, not a universal truncation assumption.

### Question 15 — D

Answer: Use supported prompt-prefix caching for eligible repeated input. Prompt-prefix caching can reuse eligible input processing without changing the context limit. Caching may reduce repeated prefix processing under provider-specific rules. It does not extend the context window, update model weights, or verify an answer. Closest official exam-guide objective 5.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Prompt-prefix caching can reuse eligible input processing without changing the context limit.
- **B:** Incorrect for this question. Follow the chosen model and service limits. Overflow handling varies; it is not universally automatic oldest-message deletion. In this case: Prompt-prefix caching can reuse eligible input processing without changing the context limit.
- **C:** Incorrect for this question. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: Prompt-prefix caching can reuse eligible input processing without changing the context limit.
- **D:** Correct. Caching may reduce repeated prefix processing under provider-specific rules. It does not extend the context window, update model weights, or verify an answer. In this case: Prompt-prefix caching can reuse eligible input processing without changing the context limit.

### Question 16 — B

Answer: Compact context while preserving checked facts and open issues. Compaction reduces accumulated content; caching does not increase available context capacity. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. Closest official exam-guide objective 5.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: Compaction reduces accumulated content; caching does not increase available context capacity.
- **B:** Correct. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Compaction reduces accumulated content; caching does not increase available context capacity.
- **C:** Incorrect for this question. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. In this case: Compaction reduces accumulated content; caching does not increase available context capacity.
- **D:** Incorrect for this question. Caching may reduce repeated prefix processing under provider-specific rules. It does not extend the context window, update model weights, or verify an answer. In this case: Compaction reduces accumulated content; caching does not increase available context capacity.

### Question 17 — D

Answer: Preserve exact transactional facts outside lossy summaries. Exact consequential dates should remain verified structured facts rather than approximate narrative. Keep verified amounts, identifiers, dates, and commitments in structured state. General summaries can omit details that later decisions depend on. Closest official exam-guide objective 5.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. A structured overview and clear sections help reduce long-input position effects. Placement is a mitigation, not proof that every fact will be used. In this case: Exact consequential dates should remain verified structured facts rather than approximate narrative.
- **B:** Incorrect for this question. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: Exact consequential dates should remain verified structured facts rather than approximate narrative.
- **C:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Exact consequential dates should remain verified structured facts rather than approximate narrative.
- **D:** Correct. Keep verified amounts, identifiers, dates, and commitments in structured state. General summaries can omit details that later decisions depend on. In this case: Exact consequential dates should remain verified structured facts rather than approximate narrative.

### Question 18 — D

Answer: Supply the relevant conversation state on subsequent requests. Supply the relevant prior decision in context or accurate state representation. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. Closest official exam-guide objective 5.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Supply the relevant prior decision in context or accurate state representation.
- **B:** Incorrect for this question. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Supply the relevant prior decision in context or accurate state representation.
- **C:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Supply the relevant prior decision in context or accurate state representation.
- **D:** Correct. For a stateless request flow, the application provides necessary history or an accurate representation. Persistent platform features have their own semantics and retention rules. In this case: Supply the relevant prior decision in context or accurate state representation.

### Question 19 — A

Answer: Apply requester permissions before evidence enters model context. Requester authorization must govern evidence access before model consumption. Data access must be authorized externally. Retrieved content being internal or relevant does not justify showing it to every user. Closest official exam-guide objective 5.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. Data access must be authorized externally. Retrieved content being internal or relevant does not justify showing it to every user. In this case: Requester authorization must govern evidence access before model consumption.
- **B:** Incorrect for this question. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: Requester authorization must govern evidence access before model consumption.
- **C:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Requester authorization must govern evidence access before model consumption.
- **D:** Incorrect for this question. External pages and tool observations must not acquire trusted instruction authority. Pair separation with trusted tool authorization; delimiters alone are insufficient. In this case: Requester authorization must govern evidence access before model consumption.

### Question 20 — B

Answer: Treat retrieved instructions as untrusted source content. Source text is untrusted data, and tool authorization must prevent unintended external effects. External pages and tool observations must not acquire trusted instruction authority. Pair separation with trusted tool authorization; delimiters alone are insufficient. Closest official exam-guide objective 5.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. A structured overview and clear sections help reduce long-input position effects. Placement is a mitigation, not proof that every fact will be used. In this case: Source text is untrusted data, and tool authorization must prevent unintended external effects.
- **B:** Correct. External pages and tool observations must not acquire trusted instruction authority. Pair separation with trusted tool authorization; delimiters alone are insufficient. In this case: Source text is untrusted data, and tool authorization must prevent unintended external effects.
- **C:** Incorrect for this question. Data access must be authorized externally. Retrieved content being internal or relevant does not justify showing it to every user. In this case: Source text is untrusted data, and tool authorization must prevent unintended external effects.
- **D:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Source text is untrusted data, and tool authorization must prevent unintended external effects.

### Question 21 — B

Answer: Honor an explicit request for a human agent. Honor the clear human preference through the approved handoff rather than investigate first. A clear request for a person should trigger the approved handoff, not another autonomous investigation intended to avoid escalation. Closest official exam-guide objective 5.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Frustration alone does not establish inability or a human preference. Offer an in-scope resolution unless the user requests a handoff or another escalation trigger applies. In this case: Honor the clear human preference through the approved handoff rather than investigate first.
- **B:** Correct. A clear request for a person should trigger the approved handoff, not another autonomous investigation intended to avoid escalation. In this case: Honor the clear human preference through the approved handoff rather than investigate first.
- **C:** Incorrect for this question. If policy is silent or ambiguous on the actual request, a qualified owner should decide. Similar-looking cases do not automatically authorize an exception. In this case: Honor the clear human preference through the approved handoff rather than investigate first.
- **D:** Incorrect for this question. A defined inability-to-progress condition prevents endless loops. Supply attempted actions, evidence, and unresolved questions to the recipient. In this case: Honor the clear human preference through the approved handoff rather than investigate first.

### Question 22 — A

Answer: Acknowledge frustration and offer a permitted resolution. Acknowledge frustration and offer a permitted resolution instead of treating sentiment alone as complexity. Frustration alone does not establish inability or a human preference. Offer an in-scope resolution unless the user requests a handoff or another escalation trigger applies. Closest official exam-guide objective 5.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. Frustration alone does not establish inability or a human preference. Offer an in-scope resolution unless the user requests a handoff or another escalation trigger applies. In this case: Acknowledge frustration and offer a permitted resolution instead of treating sentiment alone as complexity.
- **B:** Incorrect for this question. A defined inability-to-progress condition prevents endless loops. Supply attempted actions, evidence, and unresolved questions to the recipient. In this case: Acknowledge frustration and offer a permitted resolution instead of treating sentiment alone as complexity.
- **C:** Incorrect for this question. If policy is silent or ambiguous on the actual request, a qualified owner should decide. Similar-looking cases do not automatically authorize an exception. In this case: Acknowledge frustration and offer a permitted resolution instead of treating sentiment alone as complexity.
- **D:** Incorrect for this question. A clear request for a person should trigger the approved handoff, not another autonomous investigation intended to avoid escalation. In this case: Acknowledge frustration and offer a permitted resolution instead of treating sentiment alone as complexity.

### Question 23 — A

Answer: Escalate a policy gap rather than invent a rule. Escalate the policy gap rather than invent an exception from analogy. If policy is silent or ambiguous on the actual request, a qualified owner should decide. Similar-looking cases do not automatically authorize an exception. Closest official exam-guide objective 5.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. If policy is silent or ambiguous on the actual request, a qualified owner should decide. Similar-looking cases do not automatically authorize an exception. In this case: Escalate the policy gap rather than invent an exception from analogy.
- **B:** Incorrect for this question. A clear request for a person should trigger the approved handoff, not another autonomous investigation intended to avoid escalation. In this case: Escalate the policy gap rather than invent an exception from analogy.
- **C:** Incorrect for this question. Frustration alone does not establish inability or a human preference. Offer an in-scope resolution unless the user requests a handoff or another escalation trigger applies. In this case: Escalate the policy gap rather than invent an exception from analogy.
- **D:** Incorrect for this question. Multiple plausible matches require clarification or an approved verification process. Recency, sentiment, or a guessed identity is not sufficient. In this case: Escalate the policy gap rather than invent an exception from analogy.

### Question 24 — C

Answer: Escalate when bounded attempts make no meaningful progress. A defined escalation path should carry attempts, evidence, and unresolved questions. A defined inability-to-progress condition prevents endless loops. Supply attempted actions, evidence, and unresolved questions to the recipient. Closest official exam-guide objective 5.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. A clear request for a person should trigger the approved handoff, not another autonomous investigation intended to avoid escalation. In this case: A defined escalation path should carry attempts, evidence, and unresolved questions.
- **B:** Incorrect for this question. Multiple plausible matches require clarification or an approved verification process. Recency, sentiment, or a guessed identity is not sufficient. In this case: A defined escalation path should carry attempts, evidence, and unresolved questions.
- **C:** Correct. A defined inability-to-progress condition prevents endless loops. Supply attempted actions, evidence, and unresolved questions to the recipient. In this case: A defined escalation path should carry attempts, evidence, and unresolved questions.
- **D:** Incorrect for this question. Frustration alone does not establish inability or a human preference. Offer an in-scope resolution unless the user requests a handoff or another escalation trigger applies. In this case: A defined escalation path should carry attempts, evidence, and unresolved questions.

### Question 25 — A

Answer: Ask for a discriminating identifier before selecting a record. Request a discriminating identifier or use an approved verification process. Multiple plausible matches require clarification or an approved verification process. Recency, sentiment, or a guessed identity is not sufficient. Closest official exam-guide objective 5.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. Multiple plausible matches require clarification or an approved verification process. Recency, sentiment, or a guessed identity is not sufficient. In this case: Request a discriminating identifier or use an approved verification process.
- **B:** Incorrect for this question. If policy is silent or ambiguous on the actual request, a qualified owner should decide. Similar-looking cases do not automatically authorize an exception. In this case: Request a discriminating identifier or use an approved verification process.
- **C:** Incorrect for this question. Frustration alone does not establish inability or a human preference. Offer an in-scope resolution unless the user requests a handoff or another escalation trigger applies. In this case: Request a discriminating identifier or use an approved verification process.
- **D:** Incorrect for this question. A clear request for a person should trigger the approved handoff, not another autonomous investigation intended to avoid escalation. In this case: Request a discriminating identifier or use an approved verification process.

### Question 26 — B

Answer: Honor an explicit request for a human agent. A clear handoff preference should not be overridden merely to improve automation metrics. A clear request for a person should trigger the approved handoff, not another autonomous investigation intended to avoid escalation. Closest official exam-guide objective 5.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Frustration alone does not establish inability or a human preference. Offer an in-scope resolution unless the user requests a handoff or another escalation trigger applies. In this case: A clear handoff preference should not be overridden merely to improve automation metrics.
- **B:** Correct. A clear request for a person should trigger the approved handoff, not another autonomous investigation intended to avoid escalation. In this case: A clear handoff preference should not be overridden merely to improve automation metrics.
- **C:** Incorrect for this question. Multiple plausible matches require clarification or an approved verification process. Recency, sentiment, or a guessed identity is not sufficient. In this case: A clear handoff preference should not be overridden merely to improve automation metrics.
- **D:** Incorrect for this question. A defined inability-to-progress condition prevents endless loops. Supply attempted actions, evidence, and unresolved questions to the recipient. In this case: A clear handoff preference should not be overridden merely to improve automation metrics.

### Question 27 — A

Answer: Escalate a policy gap rather than invent a rule. Do not extend the written rule without authorized policy judgment. If policy is silent or ambiguous on the actual request, a qualified owner should decide. Similar-looking cases do not automatically authorize an exception. Closest official exam-guide objective 5.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. If policy is silent or ambiguous on the actual request, a qualified owner should decide. Similar-looking cases do not automatically authorize an exception. In this case: Do not extend the written rule without authorized policy judgment.
- **B:** Incorrect for this question. Frustration alone does not establish inability or a human preference. Offer an in-scope resolution unless the user requests a handoff or another escalation trigger applies. In this case: Do not extend the written rule without authorized policy judgment.
- **C:** Incorrect for this question. Multiple plausible matches require clarification or an approved verification process. Recency, sentiment, or a guessed identity is not sufficient. In this case: Do not extend the written rule without authorized policy judgment.
- **D:** Incorrect for this question. A defined inability-to-progress condition prevents endless loops. Supply attempted actions, evidence, and unresolved questions to the recipient. In this case: Do not extend the written rule without authorized policy judgment.

### Question 28 — D

Answer: Acknowledge frustration and offer a permitted resolution. Frustration alone is not a reliable reason to abandon an available permitted resolution. Frustration alone does not establish inability or a human preference. Offer an in-scope resolution unless the user requests a handoff or another escalation trigger applies. Closest official exam-guide objective 5.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. A defined inability-to-progress condition prevents endless loops. Supply attempted actions, evidence, and unresolved questions to the recipient. In this case: Frustration alone is not a reliable reason to abandon an available permitted resolution.
- **B:** Incorrect for this question. If policy is silent or ambiguous on the actual request, a qualified owner should decide. Similar-looking cases do not automatically authorize an exception. In this case: Frustration alone is not a reliable reason to abandon an available permitted resolution.
- **C:** Incorrect for this question. A clear request for a person should trigger the approved handoff, not another autonomous investigation intended to avoid escalation. In this case: Frustration alone is not a reliable reason to abandon an available permitted resolution.
- **D:** Correct. Frustration alone does not establish inability or a human preference. Offer an in-scope resolution unless the user requests a handoff or another escalation trigger applies. In this case: Frustration alone is not a reliable reason to abandon an available permitted resolution.

### Question 29 — D

Answer: Escalate when bounded attempts make no meaningful progress. Lack of meaningful progress after bounded attempts is a legitimate escalation trigger. A defined inability-to-progress condition prevents endless loops. Supply attempted actions, evidence, and unresolved questions to the recipient. Closest official exam-guide objective 5.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Multiple plausible matches require clarification or an approved verification process. Recency, sentiment, or a guessed identity is not sufficient. In this case: Lack of meaningful progress after bounded attempts is a legitimate escalation trigger.
- **B:** Incorrect for this question. Frustration alone does not establish inability or a human preference. Offer an in-scope resolution unless the user requests a handoff or another escalation trigger applies. In this case: Lack of meaningful progress after bounded attempts is a legitimate escalation trigger.
- **C:** Incorrect for this question. If policy is silent or ambiguous on the actual request, a qualified owner should decide. Similar-looking cases do not automatically authorize an exception. In this case: Lack of meaningful progress after bounded attempts is a legitimate escalation trigger.
- **D:** Correct. A defined inability-to-progress condition prevents endless loops. Supply attempted actions, evidence, and unresolved questions to the recipient. In this case: Lack of meaningful progress after bounded attempts is a legitimate escalation trigger.

### Question 30 — A

Answer: Ask for a discriminating identifier before selecting a record. Identity ambiguity must be resolved with verification, not a plausible popularity or recency guess. Multiple plausible matches require clarification or an approved verification process. Recency, sentiment, or a guessed identity is not sufficient. Closest official exam-guide objective 5.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. Multiple plausible matches require clarification or an approved verification process. Recency, sentiment, or a guessed identity is not sufficient. In this case: Identity ambiguity must be resolved with verification, not a plausible popularity or recency guess.
- **B:** Incorrect for this question. A clear request for a person should trigger the approved handoff, not another autonomous investigation intended to avoid escalation. In this case: Identity ambiguity must be resolved with verification, not a plausible popularity or recency guess.
- **C:** Incorrect for this question. Frustration alone does not establish inability or a human preference. Offer an in-scope resolution unless the user requests a handoff or another escalation trigger applies. In this case: Identity ambiguity must be resolved with verification, not a plausible popularity or recency guess.
- **D:** Incorrect for this question. If policy is silent or ambiguous on the actual request, a qualified owner should decide. Similar-looking cases do not automatically authorize an exception. In this case: Identity ambiguity must be resolved with verification, not a plausible popularity or recency guess.

### Question 31 — C

Answer: Create a structured handoff with facts, status, and next actions. Verified identifiers, attempted work, unresolved issues, evidence, and recommended actions support continuity. The recipient needs verified identifiers, completed work, unresolved issues, supporting evidence, and recommended actions, especially when the full transcript is unavailable. Closest official exam-guide objective 5.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. A clear request for a person should trigger the approved handoff, not another autonomous investigation intended to avoid escalation. In this case: Verified identifiers, attempted work, unresolved issues, evidence, and recommended actions support continuity.
- **B:** Incorrect for this question. Multiple plausible matches require clarification or an approved verification process. Recency, sentiment, or a guessed identity is not sufficient. In this case: Verified identifiers, attempted work, unresolved issues, evidence, and recommended actions support continuity.
- **C:** Correct. The recipient needs verified identifiers, completed work, unresolved issues, supporting evidence, and recommended actions, especially when the full transcript is unavailable. In this case: Verified identifiers, attempted work, unresolved issues, evidence, and recommended actions support continuity.
- **D:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Verified identifiers, attempted work, unresolved issues, evidence, and recommended actions support continuity.

### Question 32 — B

Answer: Escalate a policy gap rather than invent a rule. Treat silence or ambiguity as a policy gap requiring an authorized decision. If policy is silent or ambiguous on the actual request, a qualified owner should decide. Similar-looking cases do not automatically authorize an exception. Closest official exam-guide objective 5.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Frustration alone does not establish inability or a human preference. Offer an in-scope resolution unless the user requests a handoff or another escalation trigger applies. In this case: Treat silence or ambiguity as a policy gap requiring an authorized decision.
- **B:** Correct. If policy is silent or ambiguous on the actual request, a qualified owner should decide. Similar-looking cases do not automatically authorize an exception. In this case: Treat silence or ambiguity as a policy gap requiring an authorized decision.
- **C:** Incorrect for this question. Multiple plausible matches require clarification or an approved verification process. Recency, sentiment, or a guessed identity is not sufficient. In this case: Treat silence or ambiguity as a policy gap requiring an authorized decision.
- **D:** Incorrect for this question. A clear request for a person should trigger the approved handoff, not another autonomous investigation intended to avoid escalation. In this case: Treat silence or ambiguity as a policy gap requiring an authorized decision.

### Question 33 — C

Answer: Ask for a discriminating identifier before selecting a record. A distinguishing order identifier avoids applying actions to the wrong transaction. Multiple plausible matches require clarification or an approved verification process. Recency, sentiment, or a guessed identity is not sufficient. Closest official exam-guide objective 5.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. If policy is silent or ambiguous on the actual request, a qualified owner should decide. Similar-looking cases do not automatically authorize an exception. In this case: A distinguishing order identifier avoids applying actions to the wrong transaction.
- **B:** Incorrect for this question. A defined inability-to-progress condition prevents endless loops. Supply attempted actions, evidence, and unresolved questions to the recipient. In this case: A distinguishing order identifier avoids applying actions to the wrong transaction.
- **C:** Correct. Multiple plausible matches require clarification or an approved verification process. Recency, sentiment, or a guessed identity is not sufficient. In this case: A distinguishing order identifier avoids applying actions to the wrong transaction.
- **D:** Incorrect for this question. Frustration alone does not establish inability or a human preference. Offer an in-scope resolution unless the user requests a handoff or another escalation trigger applies. In this case: A distinguishing order identifier avoids applying actions to the wrong transaction.

### Question 34 — C

Answer: Honor an explicit request for a human agent. Proceed with the approved human handoff rather than continue trying to persuade them. A clear request for a person should trigger the approved handoff, not another autonomous investigation intended to avoid escalation. Closest official exam-guide objective 5.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. A defined inability-to-progress condition prevents endless loops. Supply attempted actions, evidence, and unresolved questions to the recipient. In this case: Proceed with the approved human handoff rather than continue trying to persuade them.
- **B:** Incorrect for this question. If policy is silent or ambiguous on the actual request, a qualified owner should decide. Similar-looking cases do not automatically authorize an exception. In this case: Proceed with the approved human handoff rather than continue trying to persuade them.
- **C:** Correct. A clear request for a person should trigger the approved handoff, not another autonomous investigation intended to avoid escalation. In this case: Proceed with the approved human handoff rather than continue trying to persuade them.
- **D:** Incorrect for this question. Frustration alone does not establish inability or a human preference. Offer an in-scope resolution unless the user requests a handoff or another escalation trigger applies. In this case: Proceed with the approved human handoff rather than continue trying to persuade them.

### Question 35 — C

Answer: Escalate when bounded attempts make no meaningful progress. Use an explicit unresolved or escalation outcome instead of silently claiming completion. A defined inability-to-progress condition prevents endless loops. Supply attempted actions, evidence, and unresolved questions to the recipient. Closest official exam-guide objective 5.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Frustration alone does not establish inability or a human preference. Offer an in-scope resolution unless the user requests a handoff or another escalation trigger applies. In this case: Use an explicit unresolved or escalation outcome instead of silently claiming completion.
- **B:** Incorrect for this question. Multiple plausible matches require clarification or an approved verification process. Recency, sentiment, or a guessed identity is not sufficient. In this case: Use an explicit unresolved or escalation outcome instead of silently claiming completion.
- **C:** Correct. A defined inability-to-progress condition prevents endless loops. Supply attempted actions, evidence, and unresolved questions to the recipient. In this case: Use an explicit unresolved or escalation outcome instead of silently claiming completion.
- **D:** Incorrect for this question. A clear request for a person should trigger the approved handoff, not another autonomous investigation intended to avoid escalation. In this case: Use an explicit unresolved or escalation outcome instead of silently claiming completion.

### Question 36 — B

Answer: Acknowledge frustration and offer a permitted resolution. Acknowledge emotion while addressing the in-scope task rather than infer incapacity from sentiment. Frustration alone does not establish inability or a human preference. Offer an in-scope resolution unless the user requests a handoff or another escalation trigger applies. Closest official exam-guide objective 5.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. If policy is silent or ambiguous on the actual request, a qualified owner should decide. Similar-looking cases do not automatically authorize an exception. In this case: Acknowledge emotion while addressing the in-scope task rather than infer incapacity from sentiment.
- **B:** Correct. Frustration alone does not establish inability or a human preference. Offer an in-scope resolution unless the user requests a handoff or another escalation trigger applies. In this case: Acknowledge emotion while addressing the in-scope task rather than infer incapacity from sentiment.
- **C:** Incorrect for this question. Multiple plausible matches require clarification or an approved verification process. Recency, sentiment, or a guessed identity is not sufficient. In this case: Acknowledge emotion while addressing the in-scope task rather than infer incapacity from sentiment.
- **D:** Incorrect for this question. A clear request for a person should trigger the approved handoff, not another autonomous investigation intended to avoid escalation. In this case: Acknowledge emotion while addressing the in-scope task rather than infer incapacity from sentiment.

### Question 37 — D

Answer: Ask for a discriminating identifier before selecting a record. Clarification or approved verification is needed before choosing a record. Multiple plausible matches require clarification or an approved verification process. Recency, sentiment, or a guessed identity is not sufficient. Closest official exam-guide objective 5.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. A defined inability-to-progress condition prevents endless loops. Supply attempted actions, evidence, and unresolved questions to the recipient. In this case: Clarification or approved verification is needed before choosing a record.
- **B:** Incorrect for this question. A clear request for a person should trigger the approved handoff, not another autonomous investigation intended to avoid escalation. In this case: Clarification or approved verification is needed before choosing a record.
- **C:** Incorrect for this question. If policy is silent or ambiguous on the actual request, a qualified owner should decide. Similar-looking cases do not automatically authorize an exception. In this case: Clarification or approved verification is needed before choosing a record.
- **D:** Correct. Multiple plausible matches require clarification or an approved verification process. Recency, sentiment, or a guessed identity is not sufficient. In this case: Clarification or approved verification is needed before choosing a record.

### Question 38 — C

Answer: Create a structured handoff with facts, status, and next actions. A structured handoff should preserve facts, status, attempted steps, and next-action needs. The recipient needs verified identifiers, completed work, unresolved issues, supporting evidence, and recommended actions, especially when the full transcript is unavailable. Closest official exam-guide objective 5.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Durable notes counter context degradation and support later verification. Record source versions or change cues so notes are not mistaken for permanently current truth. In this case: A structured handoff should preserve facts, status, attempted steps, and next-action needs.
- **B:** Incorrect for this question. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: A structured handoff should preserve facts, status, attempted steps, and next-action needs.
- **C:** Correct. The recipient needs verified identifiers, completed work, unresolved issues, supporting evidence, and recommended actions, especially when the full transcript is unavailable. In this case: A structured handoff should preserve facts, status, attempted steps, and next-action needs.
- **D:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: A structured handoff should preserve facts, status, attempted steps, and next-action needs.

### Question 39 — B

Answer: Escalate a policy gap rather than invent a rule. Escalate the unsupported policy interpretation rather than assume similarity grants permission. If policy is silent or ambiguous on the actual request, a qualified owner should decide. Similar-looking cases do not automatically authorize an exception. Closest official exam-guide objective 5.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Frustration alone does not establish inability or a human preference. Offer an in-scope resolution unless the user requests a handoff or another escalation trigger applies. In this case: Escalate the unsupported policy interpretation rather than assume similarity grants permission.
- **B:** Correct. If policy is silent or ambiguous on the actual request, a qualified owner should decide. Similar-looking cases do not automatically authorize an exception. In this case: Escalate the unsupported policy interpretation rather than assume similarity grants permission.
- **C:** Incorrect for this question. A clear request for a person should trigger the approved handoff, not another autonomous investigation intended to avoid escalation. In this case: Escalate the unsupported policy interpretation rather than assume similarity grants permission.
- **D:** Incorrect for this question. Multiple plausible matches require clarification or an approved verification process. Recency, sentiment, or a guessed identity is not sufficient. In this case: Escalate the unsupported policy interpretation rather than assume similarity grants permission.

### Question 40 — C

Answer: Honor an explicit request for a human agent. The approved human escalation pathway should not be suppressed to inflate automation statistics. A clear request for a person should trigger the approved handoff, not another autonomous investigation intended to avoid escalation. Closest official exam-guide objective 5.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Multiple plausible matches require clarification or an approved verification process. Recency, sentiment, or a guessed identity is not sufficient. In this case: The approved human escalation pathway should not be suppressed to inflate automation statistics.
- **B:** Incorrect for this question. A defined inability-to-progress condition prevents endless loops. Supply attempted actions, evidence, and unresolved questions to the recipient. In this case: The approved human escalation pathway should not be suppressed to inflate automation statistics.
- **C:** Correct. A clear request for a person should trigger the approved handoff, not another autonomous investigation intended to avoid escalation. In this case: The approved human escalation pathway should not be suppressed to inflate automation statistics.
- **D:** Incorrect for this question. Frustration alone does not establish inability or a human preference. Offer an in-scope resolution unless the user requests a handoff or another escalation trigger applies. In this case: The approved human escalation pathway should not be suppressed to inflate automation statistics.

### Question 41 — C

Answer: Return structured failure context and partial results. Report failure type, attempts, partial findings, and alternatives so recovery can be targeted. The coordinator needs failure type, attempted operation, useful outputs, and alternatives. A failure must not be disguised as a successful empty search. Closest official exam-guide objective 5.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. In this case: Report failure type, attempts, partial findings, and alternatives so recovery can be targeted.
- **B:** Incorrect for this question. A report can proceed with supported partial results if it clearly distinguishes established conclusions from gaps. Silence falsely implies complete coverage. In this case: Report failure type, attempts, partial findings, and alternatives so recovery can be targeted.
- **C:** Correct. The coordinator needs failure type, attempted operation, useful outputs, and alternatives. A failure must not be disguised as a successful empty search. In this case: Report failure type, attempts, partial findings, and alternatives so recovery can be targeted.
- **D:** Incorrect for this question. An error contract should identify failure class, recoverability, and useful context. MCP isError marks an execution failure; it should not disguise a valid empty result. In this case: Report failure type, attempts, partial findings, and alternatives so recovery can be targeted.

### Question 42 — C

Answer: Represent a successful query with no matches explicitly. Represent valid emptiness as a successful query outcome, not a failed search. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. Closest official exam-guide objective 5.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Permission denial does not justify trying alternate credentials or leaking restricted content. Recover only through explicitly authorized mechanisms. In this case: Represent valid emptiness as a successful query outcome, not a failed search.
- **B:** Incorrect for this question. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: Represent valid emptiness as a successful query outcome, not a failed search.
- **C:** Correct. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. In this case: Represent valid emptiness as a successful query outcome, not a failed search.
- **D:** Incorrect for this question. The coordinator needs failure type, attempted operation, useful outputs, and alternatives. A failure must not be disguised as a successful empty search. In this case: Represent valid emptiness as a successful query outcome, not a failed search.

### Question 43 — B

Answer: Recover transiently within the worker, then report unresolved failure. Bounded local recovery can avoid unnecessary central coordination while preserving unresolved failures. Bounded local recovery reduces coordinator noise. Exhausted recovery should preserve attempts, partial results, and alternatives rather than silently disappear. Closest official exam-guide objective 5.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. A report can proceed with supported partial results if it clearly distinguishes established conclusions from gaps. Silence falsely implies complete coverage. In this case: Bounded local recovery can avoid unnecessary central coordination while preserving unresolved failures.
- **B:** Correct. Bounded local recovery reduces coordinator noise. Exhausted recovery should preserve attempts, partial results, and alternatives rather than silently disappear. In this case: Bounded local recovery can avoid unnecessary central coordination while preserving unresolved failures.
- **C:** Incorrect for this question. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. In this case: Bounded local recovery can avoid unnecessary central coordination while preserving unresolved failures.
- **D:** Incorrect for this question. The coordinator needs failure type, attempted operation, useful outputs, and alternatives. A failure must not be disguised as a successful empty search. In this case: Bounded local recovery can avoid unnecessary central coordination while preserving unresolved failures.

### Question 44 — D

Answer: Annotate evidence coverage and unavailable sources. Distinguish supported conclusions from topic gaps caused by the unavailable source. A report can proceed with supported partial results if it clearly distinguishes established conclusions from gaps. Silence falsely implies complete coverage. Closest official exam-guide objective 5.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. The coordinator needs failure type, attempted operation, useful outputs, and alternatives. A failure must not be disguised as a successful empty search. In this case: Distinguish supported conclusions from topic gaps caused by the unavailable source.
- **B:** Incorrect for this question. Claims need traceable source identities, relevant excerpts, locations, and dates as applicable. A bibliography without claim mappings can lose attribution. In this case: Distinguish supported conclusions from topic gaps caused by the unavailable source.
- **C:** Incorrect for this question. Do not average incompatible measurements or choose one arbitrarily. Preserve context and distinguish contested findings from established ones. In this case: Distinguish supported conclusions from topic gaps caused by the unavailable source.
- **D:** Correct. A report can proceed with supported partial results if it clearly distinguishes established conclusions from gaps. Silence falsely implies complete coverage. In this case: Distinguish supported conclusions from topic gaps caused by the unavailable source.

### Question 45 — B

Answer: Return structured failure context and partial results. Structured failure context is needed for informed recovery rather than blind repetition. The coordinator needs failure type, attempted operation, useful outputs, and alternatives. A failure must not be disguised as a successful empty search. Closest official exam-guide objective 5.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. In this case: Structured failure context is needed for informed recovery rather than blind repetition.
- **B:** Correct. The coordinator needs failure type, attempted operation, useful outputs, and alternatives. A failure must not be disguised as a successful empty search. In this case: Structured failure context is needed for informed recovery rather than blind repetition.
- **C:** Incorrect for this question. A report can proceed with supported partial results if it clearly distinguishes established conclusions from gaps. Silence falsely implies complete coverage. In this case: Structured failure context is needed for informed recovery rather than blind repetition.
- **D:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Structured failure context is needed for informed recovery rather than blind repetition.

### Question 46 — C

Answer: Stop the unauthorized operation and use an approved access path. A permission failure says nothing about whether matching evidence exists behind the restriction. Permission denial does not justify trying alternate credentials or leaking restricted content. Recover only through explicitly authorized mechanisms. Closest official exam-guide objective 5.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: A permission failure says nothing about whether matching evidence exists behind the restriction.
- **B:** Incorrect for this question. A validation failure points to an input defect. Repeating identical invalid arguments is not recovery. In this case: A permission failure says nothing about whether matching evidence exists behind the restriction.
- **C:** Correct. Permission denial does not justify trying alternate credentials or leaking restricted content. Recover only through explicitly authorized mechanisms. In this case: A permission failure says nothing about whether matching evidence exists behind the restriction.
- **D:** Incorrect for this question. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. In this case: A permission failure says nothing about whether matching evidence exists behind the restriction.

### Question 47 — C

Answer: Retry a transient failure with bounded backoff. Use permitted bounded retry rather than treat temporary inaccessibility as absent evidence. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. Closest official exam-guide objective 5.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. A policy rejection is not normally fixed by repeating the same operation. Communicate the reason and legitimate next steps without evasion. In this case: Use permitted bounded retry rather than treat temporary inaccessibility as absent evidence.
- **B:** Incorrect for this question. A validation failure points to an input defect. Repeating identical invalid arguments is not recovery. In this case: Use permitted bounded retry rather than treat temporary inaccessibility as absent evidence.
- **C:** Correct. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: Use permitted bounded retry rather than treat temporary inaccessibility as absent evidence.
- **D:** Incorrect for this question. Permission denial does not justify trying alternate credentials or leaking restricted content. Recover only through explicitly authorized mechanisms. In this case: Use permitted bounded retry rather than treat temporary inaccessibility as absent evidence.

### Question 48 — B

Answer: Annotate evidence coverage and unavailable sources. Unavailable evidence must be reflected in the report's coverage and uncertainty statements. A report can proceed with supported partial results if it clearly distinguishes established conclusions from gaps. Silence falsely implies complete coverage. Closest official exam-guide objective 5.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Do not average incompatible measurements or choose one arbitrarily. Preserve context and distinguish contested findings from established ones. In this case: Unavailable evidence must be reflected in the report's coverage and uncertainty statements.
- **B:** Correct. A report can proceed with supported partial results if it clearly distinguishes established conclusions from gaps. Silence falsely implies complete coverage. In this case: Unavailable evidence must be reflected in the report's coverage and uncertainty statements.
- **C:** Incorrect for this question. The coordinator needs failure type, attempted operation, useful outputs, and alternatives. A failure must not be disguised as a successful empty search. In this case: Unavailable evidence must be reflected in the report's coverage and uncertainty statements.
- **D:** Incorrect for this question. Claims need traceable source identities, relevant excerpts, locations, and dates as applicable. A bibliography without claim mappings can lose attribution. In this case: Unavailable evidence must be reflected in the report's coverage and uncertainty statements.

### Question 49 — B

Answer: Return structured failure context and partial results. Preserve attempts, partial results, and the alternative so it can choose the next action. The coordinator needs failure type, attempted operation, useful outputs, and alternatives. A failure must not be disguised as a successful empty search. Closest official exam-guide objective 5.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. A report can proceed with supported partial results if it clearly distinguishes established conclusions from gaps. Silence falsely implies complete coverage. In this case: Preserve attempts, partial results, and the alternative so it can choose the next action.
- **B:** Correct. The coordinator needs failure type, attempted operation, useful outputs, and alternatives. A failure must not be disguised as a successful empty search. In this case: Preserve attempts, partial results, and the alternative so it can choose the next action.
- **C:** Incorrect for this question. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. In this case: Preserve attempts, partial results, and the alternative so it can choose the next action.
- **D:** Incorrect for this question. The recipient needs verified identifiers, completed work, unresolved issues, supporting evidence, and recommended actions, especially when the full transcript is unavailable. In this case: Preserve attempts, partial results, and the alternative so it can choose the next action.

### Question 50 — D

Answer: Recover transiently within the worker, then report unresolved failure. Recover locally when permitted and propagate only unresolved failures with useful context. Bounded local recovery reduces coordinator noise. Exhausted recovery should preserve attempts, partial results, and alternatives rather than silently disappear. Closest official exam-guide objective 5.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. The coordinator needs failure type, attempted operation, useful outputs, and alternatives. A failure must not be disguised as a successful empty search. In this case: Recover locally when permitted and propagate only unresolved failures with useful context.
- **B:** Incorrect for this question. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: Recover locally when permitted and propagate only unresolved failures with useful context.
- **C:** Incorrect for this question. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. In this case: Recover locally when permitted and propagate only unresolved failures with useful context.
- **D:** Correct. Bounded local recovery reduces coordinator noise. Exhausted recovery should preserve attempts, partial results, and alternatives rather than silently disappear. In this case: Recover locally when permitted and propagate only unresolved failures with useful context.

### Question 51 — C

Answer: Persist concise codebase findings with file and symbol pointers. Concise notes with file and symbol pointers preserve concrete discovered evidence. Durable notes counter context degradation and support later verification. Record source versions or change cues so notes are not mistaken for permanently current truth. Closest official exam-guide objective 5.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Concise notes with file and symbol pointers preserve concrete discovered evidence.
- **B:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Concise notes with file and symbol pointers preserve concrete discovered evidence.
- **C:** Correct. Durable notes counter context degradation and support later verification. Record source versions or change cues so notes are not mistaken for permanently current truth. In this case: Concise notes with file and symbol pointers preserve concrete discovered evidence.
- **D:** Incorrect for this question. Discovery can be isolated so verbose file output does not overwhelm the main conversation. Return useful findings and source pointers. In this case: Concise notes with file and symbol pointers preserve concrete discovered evidence.

### Question 52 — A

Answer: Delegate a focused codebase question with a bounded output. Ask focused bounded questions tied to the information the coordinator needs. A concrete question such as tracing one authorization path gives useful coverage with less irrelevant exploration than asking every worker to read everything. Closest official exam-guide objective 5.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. A concrete question such as tracing one authorization path gives useful coverage with less irrelevant exploration than asking every worker to read everything. In this case: Ask focused bounded questions tied to the information the coordinator needs.
- **B:** Incorrect for this question. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. In this case: Ask focused bounded questions tied to the information the coordinator needs.
- **C:** Incorrect for this question. Discovery can be isolated so verbose file output does not overwhelm the main conversation. Return useful findings and source pointers. In this case: Ask focused bounded questions tied to the information the coordinator needs.
- **D:** Incorrect for this question. Open-ended investigation benefits from exploration, prioritized hypotheses, and revised decomposition rather than an exhaustive fixed script chosen before evidence. In this case: Ask focused bounded questions tied to the information the coordinator needs.

### Question 53 — A

Answer: Resume from a checked manifest of worker states and artifacts. A checked manifest identifies worker status, artifacts, source versions, and remaining work. Recovery needs known state locations, completion status, source versions, and pending work. Do not infer completion merely because an output file exists. Closest official exam-guide objective 5.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. Recovery needs known state locations, completion status, source versions, and pending work. Do not infer completion merely because an output file exists. In this case: A checked manifest identifies worker status, artifacts, source versions, and remaining work.
- **B:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: A checked manifest identifies worker status, artifacts, source versions, and remaining work.
- **C:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: A checked manifest identifies worker status, artifacts, source versions, and remaining work.
- **D:** Incorrect for this question. Durable notes counter context degradation and support later verification. Record source versions or change cues so notes are not mistaken for permanently current truth. In this case: A checked manifest identifies worker status, artifacts, source versions, and remaining work.

### Question 54 — B

Answer: Compact context while preserving checked facts and open issues. Compaction can help if exact critical facts and durable evidence pointers remain available. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. Closest official exam-guide objective 5.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Durable notes counter context degradation and support later verification. Record source versions or change cues so notes are not mistaken for permanently current truth. In this case: Compaction can help if exact critical facts and durable evidence pointers remain available.
- **B:** Correct. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Compaction can help if exact critical facts and durable evidence pointers remain available.
- **C:** Incorrect for this question. A structured overview and clear sections help reduce long-input position effects. Placement is a mitigation, not proof that every fact will be used. In this case: Compaction can help if exact critical facts and durable evidence pointers remain available.
- **D:** Incorrect for this question. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: Compaction can help if exact critical facts and durable evidence pointers remain available.

### Question 55 — D

Answer: Tell the resumed agent what changed and recheck affected evidence. Recheck evidence affected by the explicit source changes instead of treating notes as timeless truth. Targeted re-analysis works when most prior context remains useful. Explicit change information prevents reliance on stale file or tool observations. Closest official exam-guide objective 5.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. A new context can avoid stale tool results when assumptions changed widely. Preserve verified facts, relevant constraints, and pointers rather than import all obsolete history. In this case: Recheck evidence affected by the explicit source changes instead of treating notes as timeless truth.
- **B:** Incorrect for this question. Durable notes counter context degradation and support later verification. Record source versions or change cues so notes are not mistaken for permanently current truth. In this case: Recheck evidence affected by the explicit source changes instead of treating notes as timeless truth.
- **C:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Recheck evidence affected by the explicit source changes instead of treating notes as timeless truth.
- **D:** Correct. Targeted re-analysis works when most prior context remains useful. Explicit change information prevents reliance on stale file or tool observations. In this case: Recheck evidence affected by the explicit source changes instead of treating notes as timeless truth.

### Question 56 — D

Answer: Delegate a focused codebase question with a bounded output. A focused trace question yields useful bounded evidence rather than repository-wide noise. A concrete question such as tracing one authorization path gives useful coverage with less irrelevant exploration than asking every worker to read everything. Closest official exam-guide objective 5.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Discovery can be isolated so verbose file output does not overwhelm the main conversation. Return useful findings and source pointers. In this case: A focused trace question yields useful bounded evidence rather than repository-wide noise.
- **B:** Incorrect for this question. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. In this case: A focused trace question yields useful bounded evidence rather than repository-wide noise.
- **C:** Incorrect for this question. Open-ended investigation benefits from exploration, prioritized hypotheses, and revised decomposition rather than an exhaustive fixed script chosen before evidence. In this case: A focused trace question yields useful bounded evidence rather than repository-wide noise.
- **D:** Correct. A concrete question such as tracing one authorization path gives useful coverage with less irrelevant exploration than asking every worker to read everything. In this case: A focused trace question yields useful bounded evidence rather than repository-wide noise.

### Question 57 — B

Answer: Resume from a checked manifest of worker states and artifacts. Recovery status and artifact validation must be checked rather than inferred from existence. Recovery needs known state locations, completion status, source versions, and pending work. Do not infer completion merely because an output file exists. Closest official exam-guide objective 5.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Durable notes counter context degradation and support later verification. Record source versions or change cues so notes are not mistaken for permanently current truth. In this case: Recovery status and artifact validation must be checked rather than inferred from existence.
- **B:** Correct. Recovery needs known state locations, completion status, source versions, and pending work. Do not infer completion merely because an output file exists. In this case: Recovery status and artifact validation must be checked rather than inferred from existence.
- **C:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Recovery status and artifact validation must be checked rather than inferred from existence.
- **D:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Recovery status and artifact validation must be checked rather than inferred from existence.

### Question 58 — C

Answer: Persist concise codebase findings with file and symbol pointers. Preserve the relevant symbol and file pointer with a concise finding. Durable notes counter context degradation and support later verification. Record source versions or change cues so notes are not mistaken for permanently current truth. Closest official exam-guide objective 5.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: Preserve the relevant symbol and file pointer with a concise finding.
- **B:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Preserve the relevant symbol and file pointer with a concise finding.
- **C:** Correct. Durable notes counter context degradation and support later verification. Record source versions or change cues so notes are not mistaken for permanently current truth. In this case: Preserve the relevant symbol and file pointer with a concise finding.
- **D:** Incorrect for this question. A structured overview and clear sections help reduce long-input position effects. Placement is a mitigation, not proof that every fact will be used. In this case: Preserve the relevant symbol and file pointer with a concise finding.

### Question 59 — D

Answer: Pass relevant evidence and constraints explicitly. Relevant prior conclusions and constraints should accompany the next focused delegation. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. Closest official exam-guide objective 5.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Discovery can be isolated so verbose file output does not overwhelm the main conversation. Return useful findings and source pointers. In this case: Relevant prior conclusions and constraints should accompany the next focused delegation.
- **B:** Incorrect for this question. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. In this case: Relevant prior conclusions and constraints should accompany the next focused delegation.
- **C:** Incorrect for this question. A concrete question such as tracing one authorization path gives useful coverage with less irrelevant exploration than asking every worker to read everything. In this case: Relevant prior conclusions and constraints should accompany the next focused delegation.
- **D:** Correct. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Relevant prior conclusions and constraints should accompany the next focused delegation.

### Question 60 — C

Answer: Start a fresh session with a checked structured summary. Start from a current checked summary and re-explore changed evidence selectively. A new context can avoid stale tool results when assumptions changed widely. Preserve verified facts, relevant constraints, and pointers rather than import all obsolete history. Closest official exam-guide objective 5.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Start from a current checked summary and re-explore changed evidence selectively.
- **B:** Incorrect for this question. Targeted re-analysis works when most prior context remains useful. Explicit change information prevents reliance on stale file or tool observations. In this case: Start from a current checked summary and re-explore changed evidence selectively.
- **C:** Correct. A new context can avoid stale tool results when assumptions changed widely. Preserve verified facts, relevant constraints, and pointers rather than import all obsolete history. In this case: Start from a current checked summary and re-explore changed evidence selectively.
- **D:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Start from a current checked summary and re-explore changed evidence selectively.

### Question 61 — C

Answer: Evaluate accuracy by document type and field segment. Segment results by document type and field instead of hiding failures in an average. Averages can hide systematic failures in rare forms or important fields. Segment-level evaluation informs safe automation and review allocation. Closest official exam-guide objective 5.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. In this case: Segment results by document type and field instead of hiding failures in an average.
- **B:** Incorrect for this question. Review priority should reflect uncertainty and consequences. A high uncalibrated confidence number should not override contradictory evidence. In this case: Segment results by document type and field instead of hiding failures in an average.
- **C:** Correct. Averages can hide systematic failures in rare forms or important fields. Segment-level evaluation informs safe automation and review allocation. In this case: Segment results by document type and field instead of hiding failures in an average.
- **D:** Incorrect for this question. Ongoing random checks among high-confidence results can discover hidden errors and changing patterns that low-confidence-only review misses. In this case: Segment results by document type and field instead of hiding failures in an average.

### Question 62 — B

Answer: Calibrate field-confidence thresholds against labeled examples. Compare confidence with labeled outcomes for representative fields and document types. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. Closest official exam-guide objective 5.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Review priority should reflect uncertainty and consequences. A high uncalibrated confidence number should not override contradictory evidence. In this case: Compare confidence with labeled outcomes for representative fields and document types.
- **B:** Correct. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. In this case: Compare confidence with labeled outcomes for representative fields and document types.
- **C:** Incorrect for this question. Averages can hide systematic failures in rare forms or important fields. Segment-level evaluation informs safe automation and review allocation. In this case: Compare confidence with labeled outcomes for representative fields and document types.
- **D:** Incorrect for this question. Ongoing random checks among high-confidence results can discover hidden errors and changing patterns that low-confidence-only review misses. In this case: Compare confidence with labeled outcomes for representative fields and document types.

### Question 63 — B

Answer: Sample high-confidence outputs within relevant strata. Random checks within high-confidence strata can reveal hidden and emerging errors. Ongoing random checks among high-confidence results can discover hidden errors and changing patterns that low-confidence-only review misses. Closest official exam-guide objective 5.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. In this case: Random checks within high-confidence strata can reveal hidden and emerging errors.
- **B:** Correct. Ongoing random checks among high-confidence results can discover hidden errors and changing patterns that low-confidence-only review misses. In this case: Random checks within high-confidence strata can reveal hidden and emerging errors.
- **C:** Incorrect for this question. Averages can hide systematic failures in rare forms or important fields. Segment-level evaluation informs safe automation and review allocation. In this case: Random checks within high-confidence strata can reveal hidden and emerging errors.
- **D:** Incorrect for this question. Review priority should reflect uncertainty and consequences. A high uncalibrated confidence number should not override contradictory evidence. In this case: Random checks within high-confidence strata can reveal hidden and emerging errors.

### Question 64 — B

Answer: Route ambiguous, conflicting, or high-risk cases to qualified review. Contradictory evidence warrants qualified review rather than automatic acceptance based on confidence alone. Review priority should reflect uncertainty and consequences. A high uncalibrated confidence number should not override contradictory evidence. Closest official exam-guide objective 5.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Averages can hide systematic failures in rare forms or important fields. Segment-level evaluation informs safe automation and review allocation. In this case: Contradictory evidence warrants qualified review rather than automatic acceptance based on confidence alone.
- **B:** Correct. Review priority should reflect uncertainty and consequences. A high uncalibrated confidence number should not override contradictory evidence. In this case: Contradictory evidence warrants qualified review rather than automatic acceptance based on confidence alone.
- **C:** Incorrect for this question. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. In this case: Contradictory evidence warrants qualified review rather than automatic acceptance based on confidence alone.
- **D:** Incorrect for this question. Ongoing random checks among high-confidence results can discover hidden errors and changing patterns that low-confidence-only review misses. In this case: Contradictory evidence warrants qualified review rather than automatic acceptance based on confidence alone.

### Question 65 — D

Answer: Evaluate accuracy by document type and field segment. Document-type and field segments need separate evaluation before review is reduced. Averages can hide systematic failures in rare forms or important fields. Segment-level evaluation informs safe automation and review allocation. Closest official exam-guide objective 5.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Review priority should reflect uncertainty and consequences. A high uncalibrated confidence number should not override contradictory evidence. In this case: Document-type and field segments need separate evaluation before review is reduced.
- **B:** Incorrect for this question. Ongoing random checks among high-confidence results can discover hidden errors and changing patterns that low-confidence-only review misses. In this case: Document-type and field segments need separate evaluation before review is reduced.
- **C:** Incorrect for this question. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. In this case: Document-type and field segments need separate evaluation before review is reduced.
- **D:** Correct. Averages can hide systematic failures in rare forms or important fields. Segment-level evaluation informs safe automation and review allocation. In this case: Document-type and field segments need separate evaluation before review is reduced.

### Question 66 — A

Answer: Calibrate field-confidence thresholds against labeled examples. Calibrate routing with observed field-level correctness instead of assuming numerical confidence means accuracy. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. Closest official exam-guide objective 5.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. In this case: Calibrate routing with observed field-level correctness instead of assuming numerical confidence means accuracy.
- **B:** Incorrect for this question. Review priority should reflect uncertainty and consequences. A high uncalibrated confidence number should not override contradictory evidence. In this case: Calibrate routing with observed field-level correctness instead of assuming numerical confidence means accuracy.
- **C:** Incorrect for this question. Ongoing random checks among high-confidence results can discover hidden errors and changing patterns that low-confidence-only review misses. In this case: Calibrate routing with observed field-level correctness instead of assuming numerical confidence means accuracy.
- **D:** Incorrect for this question. Averages can hide systematic failures in rare forms or important fields. Segment-level evaluation informs safe automation and review allocation. In this case: Calibrate routing with observed field-level correctness instead of assuming numerical confidence means accuracy.

### Question 67 — A

Answer: Sample high-confidence outputs within relevant strata. Stratified sampling of accepted high-confidence outputs can expose novel failure patterns. Ongoing random checks among high-confidence results can discover hidden errors and changing patterns that low-confidence-only review misses. Closest official exam-guide objective 5.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. Ongoing random checks among high-confidence results can discover hidden errors and changing patterns that low-confidence-only review misses. In this case: Stratified sampling of accepted high-confidence outputs can expose novel failure patterns.
- **B:** Incorrect for this question. Review priority should reflect uncertainty and consequences. A high uncalibrated confidence number should not override contradictory evidence. In this case: Stratified sampling of accepted high-confidence outputs can expose novel failure patterns.
- **C:** Incorrect for this question. Averages can hide systematic failures in rare forms or important fields. Segment-level evaluation informs safe automation and review allocation. In this case: Stratified sampling of accepted high-confidence outputs can expose novel failure patterns.
- **D:** Incorrect for this question. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. In this case: Stratified sampling of accepted high-confidence outputs can expose novel failure patterns.

### Question 68 — A

Answer: Route ambiguous, conflicting, or high-risk cases to qualified review. Use uncertainty, conflict, and impact to allocate qualified human attention. Review priority should reflect uncertainty and consequences. A high uncalibrated confidence number should not override contradictory evidence. Closest official exam-guide objective 5.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. Review priority should reflect uncertainty and consequences. A high uncalibrated confidence number should not override contradictory evidence. In this case: Use uncertainty, conflict, and impact to allocate qualified human attention.
- **B:** Incorrect for this question. Averages can hide systematic failures in rare forms or important fields. Segment-level evaluation informs safe automation and review allocation. In this case: Use uncertainty, conflict, and impact to allocate qualified human attention.
- **C:** Incorrect for this question. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. In this case: Use uncertainty, conflict, and impact to allocate qualified human attention.
- **D:** Incorrect for this question. Ongoing random checks among high-confidence results can discover hidden errors and changing patterns that low-confidence-only review misses. In this case: Use uncertainty, conflict, and impact to allocate qualified human attention.

### Question 69 — C

Answer: Evaluate accuracy by document type and field segment. Examine segment-level field and document performance rather than rely on aggregate accuracy. Averages can hide systematic failures in rare forms or important fields. Segment-level evaluation informs safe automation and review allocation. Closest official exam-guide objective 5.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Ongoing random checks among high-confidence results can discover hidden errors and changing patterns that low-confidence-only review misses. In this case: Examine segment-level field and document performance rather than rely on aggregate accuracy.
- **B:** Incorrect for this question. Review priority should reflect uncertainty and consequences. A high uncalibrated confidence number should not override contradictory evidence. In this case: Examine segment-level field and document performance rather than rely on aggregate accuracy.
- **C:** Correct. Averages can hide systematic failures in rare forms or important fields. Segment-level evaluation informs safe automation and review allocation. In this case: Examine segment-level field and document performance rather than rely on aggregate accuracy.
- **D:** Incorrect for this question. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. In this case: Examine segment-level field and document performance rather than rely on aggregate accuracy.

### Question 70 — D

Answer: Calibrate field-confidence thresholds against labeled examples. Calibration must reflect current representative data rather than remain an assumed permanent property. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. Closest official exam-guide objective 5.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Ongoing random checks among high-confidence results can discover hidden errors and changing patterns that low-confidence-only review misses. In this case: Calibration must reflect current representative data rather than remain an assumed permanent property.
- **B:** Incorrect for this question. Averages can hide systematic failures in rare forms or important fields. Segment-level evaluation informs safe automation and review allocation. In this case: Calibration must reflect current representative data rather than remain an assumed permanent property.
- **C:** Incorrect for this question. Review priority should reflect uncertainty and consequences. A high uncalibrated confidence number should not override contradictory evidence. In this case: Calibration must reflect current representative data rather than remain an assumed permanent property.
- **D:** Correct. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. In this case: Calibration must reflect current representative data rather than remain an assumed permanent property.

### Question 71 — D

Answer: Preserve claim-to-source mappings through every handoff. Claims must remain linked to their supporting sources and relevant excerpts. Claims need traceable source identities, relevant excerpts, locations, and dates as applicable. A bibliography without claim mappings can lose attribution. Closest official exam-guide objective 5.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Different measurement periods can explain apparent disagreements. Dates and methodology should remain attached rather than being stripped in summaries. In this case: Claims must remain linked to their supporting sources and relevant excerpts.
- **B:** Incorrect for this question. Tables can preserve financial comparisons, while prose and structured lists suit other needs. A single forced format can hide important structure. In this case: Claims must remain linked to their supporting sources and relevant excerpts.
- **C:** Incorrect for this question. Do not average incompatible measurements or choose one arbitrarily. Preserve context and distinguish contested findings from established ones. In this case: Claims must remain linked to their supporting sources and relevant excerpts.
- **D:** Correct. Claims need traceable source identities, relevant excerpts, locations, and dates as applicable. A bibliography without claim mappings can lose attribution. In this case: Claims must remain linked to their supporting sources and relevant excerpts.

### Question 72 — C

Answer: Preserve collection and publication dates with claims. Attach collection and publication dates along with methodological context. Different measurement periods can explain apparent disagreements. Dates and methodology should remain attached rather than being stripped in summaries. Closest official exam-guide objective 5.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Claims need traceable source identities, relevant excerpts, locations, and dates as applicable. A bibliography without claim mappings can lose attribution. In this case: Attach collection and publication dates along with methodological context.
- **B:** Incorrect for this question. Do not average incompatible measurements or choose one arbitrarily. Preserve context and distinguish contested findings from established ones. In this case: Attach collection and publication dates along with methodological context.
- **C:** Correct. Different measurement periods can explain apparent disagreements. Dates and methodology should remain attached rather than being stripped in summaries. In this case: Attach collection and publication dates along with methodological context.
- **D:** Incorrect for this question. Tables can preserve financial comparisons, while prose and structured lists suit other needs. A single forced format can hide important structure. In this case: Attach collection and publication dates along with methodological context.

### Question 73 — D

Answer: Represent credible disagreement with attributed values. Preserve attributed disagreement instead of selecting or averaging values arbitrarily. Do not average incompatible measurements or choose one arbitrarily. Preserve context and distinguish contested findings from established ones. Closest official exam-guide objective 5.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Tables can preserve financial comparisons, while prose and structured lists suit other needs. A single forced format can hide important structure. In this case: Preserve attributed disagreement instead of selecting or averaging values arbitrarily.
- **B:** Incorrect for this question. Claims need traceable source identities, relevant excerpts, locations, and dates as applicable. A bibliography without claim mappings can lose attribution. In this case: Preserve attributed disagreement instead of selecting or averaging values arbitrarily.
- **C:** Incorrect for this question. Different measurement periods can explain apparent disagreements. Dates and methodology should remain attached rather than being stripped in summaries. In this case: Preserve attributed disagreement instead of selecting or averaging values arbitrarily.
- **D:** Correct. Do not average incompatible measurements or choose one arbitrarily. Preserve context and distinguish contested findings from established ones. In this case: Preserve attributed disagreement instead of selecting or averaging values arbitrarily.

### Question 74 — D

Answer: Use representations suited to the content type. Use a format suited to the content, such as tables for comparable financial values. Tables can preserve financial comparisons, while prose and structured lists suit other needs. A single forced format can hide important structure. Closest official exam-guide objective 5.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Do not average incompatible measurements or choose one arbitrarily. Preserve context and distinguish contested findings from established ones. In this case: Use a format suited to the content, such as tables for comparable financial values.
- **B:** Incorrect for this question. Claims need traceable source identities, relevant excerpts, locations, and dates as applicable. A bibliography without claim mappings can lose attribution. In this case: Use a format suited to the content, such as tables for comparable financial values.
- **C:** Incorrect for this question. Different measurement periods can explain apparent disagreements. Dates and methodology should remain attached rather than being stripped in summaries. In this case: Use a format suited to the content, such as tables for comparable financial values.
- **D:** Correct. Tables can preserve financial comparisons, while prose and structured lists suit other needs. A single forced format can hide important structure. In this case: Use a format suited to the content, such as tables for comparable financial values.

### Question 75 — A

Answer: Preserve claim-to-source mappings through every handoff. Source-linked structured claims enable traceability through later summarization. Claims need traceable source identities, relevant excerpts, locations, and dates as applicable. A bibliography without claim mappings can lose attribution. Closest official exam-guide objective 5.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. Claims need traceable source identities, relevant excerpts, locations, and dates as applicable. A bibliography without claim mappings can lose attribution. In this case: Source-linked structured claims enable traceability through later summarization.
- **B:** Incorrect for this question. Different measurement periods can explain apparent disagreements. Dates and methodology should remain attached rather than being stripped in summaries. In this case: Source-linked structured claims enable traceability through later summarization.
- **C:** Incorrect for this question. Tables can preserve financial comparisons, while prose and structured lists suit other needs. A single forced format can hide important structure. In this case: Source-linked structured claims enable traceability through later summarization.
- **D:** Incorrect for this question. Do not average incompatible measurements or choose one arbitrarily. Preserve context and distinguish contested findings from established ones. In this case: Source-linked structured claims enable traceability through later summarization.

### Question 76 — A

Answer: Represent credible disagreement with attributed values. Expose the disagreement with attribution and context rather than hide selection uncertainty. Do not average incompatible measurements or choose one arbitrarily. Preserve context and distinguish contested findings from established ones. Closest official exam-guide objective 5.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. Do not average incompatible measurements or choose one arbitrarily. Preserve context and distinguish contested findings from established ones. In this case: Expose the disagreement with attribution and context rather than hide selection uncertainty.
- **B:** Incorrect for this question. Claims need traceable source identities, relevant excerpts, locations, and dates as applicable. A bibliography without claim mappings can lose attribution. In this case: Expose the disagreement with attribution and context rather than hide selection uncertainty.
- **C:** Incorrect for this question. Tables can preserve financial comparisons, while prose and structured lists suit other needs. A single forced format can hide important structure. In this case: Expose the disagreement with attribution and context rather than hide selection uncertainty.
- **D:** Incorrect for this question. Different measurement periods can explain apparent disagreements. Dates and methodology should remain attached rather than being stripped in summaries. In this case: Expose the disagreement with attribution and context rather than hide selection uncertainty.

### Question 77 — C

Answer: Preserve collection and publication dates with claims. Preserve and label both time concepts instead of collapsing them into one date. Different measurement periods can explain apparent disagreements. Dates and methodology should remain attached rather than being stripped in summaries. Closest official exam-guide objective 5.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Tables can preserve financial comparisons, while prose and structured lists suit other needs. A single forced format can hide important structure. In this case: Preserve and label both time concepts instead of collapsing them into one date.
- **B:** Incorrect for this question. Do not average incompatible measurements or choose one arbitrarily. Preserve context and distinguish contested findings from established ones. In this case: Preserve and label both time concepts instead of collapsing them into one date.
- **C:** Correct. Different measurement periods can explain apparent disagreements. Dates and methodology should remain attached rather than being stripped in summaries. In this case: Preserve and label both time concepts instead of collapsing them into one date.
- **D:** Incorrect for this question. Claims need traceable source identities, relevant excerpts, locations, and dates as applicable. A bibliography without claim mappings can lose attribution. In this case: Preserve and label both time concepts instead of collapsing them into one date.

### Question 78 — D

Answer: Preserve claim-to-source mappings through every handoff. Claim-source support must be verified, not inferred from the presence of a link. Claims need traceable source identities, relevant excerpts, locations, and dates as applicable. A bibliography without claim mappings can lose attribution. Closest official exam-guide objective 5.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Do not average incompatible measurements or choose one arbitrarily. Preserve context and distinguish contested findings from established ones. In this case: Claim-source support must be verified, not inferred from the presence of a link.
- **B:** Incorrect for this question. Tables can preserve financial comparisons, while prose and structured lists suit other needs. A single forced format can hide important structure. In this case: Claim-source support must be verified, not inferred from the presence of a link.
- **C:** Incorrect for this question. Different measurement periods can explain apparent disagreements. Dates and methodology should remain attached rather than being stripped in summaries. In this case: Claim-source support must be verified, not inferred from the presence of a link.
- **D:** Correct. Claims need traceable source identities, relevant excerpts, locations, and dates as applicable. A bibliography without claim mappings can lose attribution. In this case: Claim-source support must be verified, not inferred from the presence of a link.

### Question 79 — D

Answer: Use representations suited to the content type. Choose representations appropriate to each content type without losing evidence structure. Tables can preserve financial comparisons, while prose and structured lists suit other needs. A single forced format can hide important structure. Closest official exam-guide objective 5.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Do not average incompatible measurements or choose one arbitrarily. Preserve context and distinguish contested findings from established ones. In this case: Choose representations appropriate to each content type without losing evidence structure.
- **B:** Incorrect for this question. Different measurement periods can explain apparent disagreements. Dates and methodology should remain attached rather than being stripped in summaries. In this case: Choose representations appropriate to each content type without losing evidence structure.
- **C:** Incorrect for this question. Claims need traceable source identities, relevant excerpts, locations, and dates as applicable. A bibliography without claim mappings can lose attribution. In this case: Choose representations appropriate to each content type without losing evidence structure.
- **D:** Correct. Tables can preserve financial comparisons, while prose and structured lists suit other needs. A single forced format can hide important structure. In this case: Choose representations appropriate to each content type without losing evidence structure.

### Question 80 — C

Answer: Represent credible disagreement with attributed values. Separate well-supported findings from contested ones while retaining source characterizations. Do not average incompatible measurements or choose one arbitrarily. Preserve context and distinguish contested findings from established ones. Closest official exam-guide objective 5.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Different measurement periods can explain apparent disagreements. Dates and methodology should remain attached rather than being stripped in summaries. In this case: Separate well-supported findings from contested ones while retaining source characterizations.
- **B:** Incorrect for this question. Claims need traceable source identities, relevant excerpts, locations, and dates as applicable. A bibliography without claim mappings can lose attribution. In this case: Separate well-supported findings from contested ones while retaining source characterizations.
- **C:** Correct. Do not average incompatible measurements or choose one arbitrarily. Preserve context and distinguish contested findings from established ones. In this case: Separate well-supported findings from contested ones while retaining source characterizations.
- **D:** Incorrect for this question. Tables can preserve financial comparisons, while prose and structured lists suit other needs. A single forced format can hide important structure. In this case: Separate well-supported findings from contested ones while retaining source characterizations.

### Question 81 — B

Answer: Preserve exact transactional facts outside lossy summaries. Preserve the verified amount explicitly so later actions do not depend on vague compression. Keep verified amounts, identifiers, dates, and commitments in structured state. General summaries can omit details that later decisions depend on. Closest official exam-guide objective 5.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. A structured overview and clear sections help reduce long-input position effects. Placement is a mitigation, not proof that every fact will be used. In this case: Preserve the verified amount explicitly so later actions do not depend on vague compression.
- **B:** Correct. Keep verified amounts, identifiers, dates, and commitments in structured state. General summaries can omit details that later decisions depend on. In this case: Preserve the verified amount explicitly so later actions do not depend on vague compression.
- **C:** Incorrect for this question. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: Preserve the verified amount explicitly so later actions do not depend on vague compression.
- **D:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Preserve the verified amount explicitly so later actions do not depend on vague compression.

### Question 82 — A

Answer: Ask for a discriminating identifier before selecting a record. Request discriminating verification rather than rely on a subjective match heuristic. Multiple plausible matches require clarification or an approved verification process. Recency, sentiment, or a guessed identity is not sufficient. Closest official exam-guide objective 5.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. Multiple plausible matches require clarification or an approved verification process. Recency, sentiment, or a guessed identity is not sufficient. In this case: Request discriminating verification rather than rely on a subjective match heuristic.
- **B:** Incorrect for this question. Frustration alone does not establish inability or a human preference. Offer an in-scope resolution unless the user requests a handoff or another escalation trigger applies. In this case: Request discriminating verification rather than rely on a subjective match heuristic.
- **C:** Incorrect for this question. A clear request for a person should trigger the approved handoff, not another autonomous investigation intended to avoid escalation. In this case: Request discriminating verification rather than rely on a subjective match heuristic.
- **D:** Incorrect for this question. If policy is silent or ambiguous on the actual request, a qualified owner should decide. Similar-looking cases do not automatically authorize an exception. In this case: Request discriminating verification rather than rely on a subjective match heuristic.

### Question 83 — A

Answer: Return structured failure context and partial results. Distinguish inability to search from a successful search with no matches. The coordinator needs failure type, attempted operation, useful outputs, and alternatives. A failure must not be disguised as a successful empty search. Closest official exam-guide objective 5.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. The coordinator needs failure type, attempted operation, useful outputs, and alternatives. A failure must not be disguised as a successful empty search. In this case: Distinguish inability to search from a successful search with no matches.
- **B:** Incorrect for this question. A report can proceed with supported partial results if it clearly distinguishes established conclusions from gaps. Silence falsely implies complete coverage. In this case: Distinguish inability to search from a successful search with no matches.
- **C:** Incorrect for this question. An error contract should identify failure class, recoverability, and useful context. MCP isError marks an execution failure; it should not disguise a valid empty result. In this case: Distinguish inability to search from a successful search with no matches.
- **D:** Incorrect for this question. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. In this case: Distinguish inability to search from a successful search with no matches.

### Question 84 — B

Answer: Persist concise codebase findings with file and symbol pointers. Persist checked findings with concrete source pointers that can be revisited. Durable notes counter context degradation and support later verification. Record source versions or change cues so notes are not mistaken for permanently current truth. Closest official exam-guide objective 5.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Recovery needs known state locations, completion status, source versions, and pending work. Do not infer completion merely because an output file exists. In this case: Persist checked findings with concrete source pointers that can be revisited.
- **B:** Correct. Durable notes counter context degradation and support later verification. Record source versions or change cues so notes are not mistaken for permanently current truth. In this case: Persist checked findings with concrete source pointers that can be revisited.
- **C:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Persist checked findings with concrete source pointers that can be revisited.
- **D:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Persist checked findings with concrete source pointers that can be revisited.

### Question 85 — A

Answer: Sample high-confidence outputs within relevant strata. Sample accepted records within relevant strata instead of reviewing only rejected ones. Ongoing random checks among high-confidence results can discover hidden errors and changing patterns that low-confidence-only review misses. Closest official exam-guide objective 5.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. Ongoing random checks among high-confidence results can discover hidden errors and changing patterns that low-confidence-only review misses. In this case: Sample accepted records within relevant strata instead of reviewing only rejected ones.
- **B:** Incorrect for this question. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. In this case: Sample accepted records within relevant strata instead of reviewing only rejected ones.
- **C:** Incorrect for this question. Averages can hide systematic failures in rare forms or important fields. Segment-level evaluation informs safe automation and review allocation. In this case: Sample accepted records within relevant strata instead of reviewing only rejected ones.
- **D:** Incorrect for this question. Review priority should reflect uncertainty and consequences. A high uncalibrated confidence number should not override contradictory evidence. In this case: Sample accepted records within relevant strata instead of reviewing only rejected ones.

### Question 86 — B

Answer: Preserve claim-to-source mappings through every handoff. Claim-to-source mappings must survive every handoff, not just the initial extraction. Claims need traceable source identities, relevant excerpts, locations, and dates as applicable. A bibliography without claim mappings can lose attribution. Closest official exam-guide objective 5.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Tables can preserve financial comparisons, while prose and structured lists suit other needs. A single forced format can hide important structure. In this case: Claim-to-source mappings must survive every handoff, not just the initial extraction.
- **B:** Correct. Claims need traceable source identities, relevant excerpts, locations, and dates as applicable. A bibliography without claim mappings can lose attribution. In this case: Claim-to-source mappings must survive every handoff, not just the initial extraction.
- **C:** Incorrect for this question. Do not average incompatible measurements or choose one arbitrarily. Preserve context and distinguish contested findings from established ones. In this case: Claim-to-source mappings must survive every handoff, not just the initial extraction.
- **D:** Incorrect for this question. Different measurement periods can explain apparent disagreements. Dates and methodology should remain attached rather than being stripped in summaries. In this case: Claim-to-source mappings must survive every handoff, not just the initial extraction.

### Question 87 — D

Answer: Reduce tool output to relevant fields with provenance. Return relevant structured findings and provenance rather than verbose intermediate narrative. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. Closest official exam-guide objective 5.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Keep verified amounts, identifiers, dates, and commitments in structured state. General summaries can omit details that later decisions depend on. In this case: Return relevant structured findings and provenance rather than verbose intermediate narrative.
- **B:** Incorrect for this question. A structured overview and clear sections help reduce long-input position effects. Placement is a mitigation, not proof that every fact will be used. In this case: Return relevant structured findings and provenance rather than verbose intermediate narrative.
- **C:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Return relevant structured findings and provenance rather than verbose intermediate narrative.
- **D:** Correct. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: Return relevant structured findings and provenance rather than verbose intermediate narrative.

### Question 88 — B

Answer: Escalate a policy gap rather than invent a rule. An authorized owner should resolve the policy gap rather than a model infer new authority. If policy is silent or ambiguous on the actual request, a qualified owner should decide. Similar-looking cases do not automatically authorize an exception. Closest official exam-guide objective 5.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. A clear request for a person should trigger the approved handoff, not another autonomous investigation intended to avoid escalation. In this case: An authorized owner should resolve the policy gap rather than a model infer new authority.
- **B:** Correct. If policy is silent or ambiguous on the actual request, a qualified owner should decide. Similar-looking cases do not automatically authorize an exception. In this case: An authorized owner should resolve the policy gap rather than a model infer new authority.
- **C:** Incorrect for this question. Frustration alone does not establish inability or a human preference. Offer an in-scope resolution unless the user requests a handoff or another escalation trigger applies. In this case: An authorized owner should resolve the policy gap rather than a model infer new authority.
- **D:** Incorrect for this question. Multiple plausible matches require clarification or an approved verification process. Recency, sentiment, or a guessed identity is not sufficient. In this case: An authorized owner should resolve the policy gap rather than a model infer new authority.

### Question 89 — A

Answer: Annotate evidence coverage and unavailable sources. Explicit coverage annotations prevent partial evidence from masquerading as complete research. A report can proceed with supported partial results if it clearly distinguishes established conclusions from gaps. Silence falsely implies complete coverage. Closest official exam-guide objective 5.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. A report can proceed with supported partial results if it clearly distinguishes established conclusions from gaps. Silence falsely implies complete coverage. In this case: Explicit coverage annotations prevent partial evidence from masquerading as complete research.
- **B:** Incorrect for this question. Claims need traceable source identities, relevant excerpts, locations, and dates as applicable. A bibliography without claim mappings can lose attribution. In this case: Explicit coverage annotations prevent partial evidence from masquerading as complete research.
- **C:** Incorrect for this question. Do not average incompatible measurements or choose one arbitrarily. Preserve context and distinguish contested findings from established ones. In this case: Explicit coverage annotations prevent partial evidence from masquerading as complete research.
- **D:** Incorrect for this question. The coordinator needs failure type, attempted operation, useful outputs, and alternatives. A failure must not be disguised as a successful empty search. In this case: Explicit coverage annotations prevent partial evidence from masquerading as complete research.

### Question 90 — D

Answer: Route ambiguous, conflicting, or high-risk cases to qualified review. Qualified review should consider ambiguity and consequences rather than confidence alone. Review priority should reflect uncertainty and consequences. A high uncalibrated confidence number should not override contradictory evidence. Closest official exam-guide objective 5.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Ongoing random checks among high-confidence results can discover hidden errors and changing patterns that low-confidence-only review misses. In this case: Qualified review should consider ambiguity and consequences rather than confidence alone.
- **B:** Incorrect for this question. Averages can hide systematic failures in rare forms or important fields. Segment-level evaluation informs safe automation and review allocation. In this case: Qualified review should consider ambiguity and consequences rather than confidence alone.
- **C:** Incorrect for this question. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. In this case: Qualified review should consider ambiguity and consequences rather than confidence alone.
- **D:** Correct. Review priority should reflect uncertainty and consequences. A high uncalibrated confidence number should not override contradictory evidence. In this case: Qualified review should consider ambiguity and consequences rather than confidence alone.

### Question 91 — A

Answer: Resume from a checked manifest of worker states and artifacts. A checked structured manifest supports safe restart and targeted continuation. Recovery needs known state locations, completion status, source versions, and pending work. Do not infer completion merely because an output file exists. Closest official exam-guide objective 5.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. Recovery needs known state locations, completion status, source versions, and pending work. Do not infer completion merely because an output file exists. In this case: A checked structured manifest supports safe restart and targeted continuation.
- **B:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: A checked structured manifest supports safe restart and targeted continuation.
- **C:** Incorrect for this question. Durable notes counter context degradation and support later verification. Record source versions or change cues so notes are not mistaken for permanently current truth. In this case: A checked structured manifest supports safe restart and targeted continuation.
- **D:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: A checked structured manifest supports safe restart and targeted continuation.

### Question 92 — D

Answer: Use supported prompt-prefix caching for eligible repeated input. Supported prefix caching targets eligible reuse without changing semantic evidence or capacity. Caching may reduce repeated prefix processing under provider-specific rules. It does not extend the context window, update model weights, or verify an answer. Closest official exam-guide objective 5.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Supported prefix caching targets eligible reuse without changing semantic evidence or capacity.
- **B:** Incorrect for this question. Follow the chosen model and service limits. Overflow handling varies; it is not universally automatic oldest-message deletion. In this case: Supported prefix caching targets eligible reuse without changing semantic evidence or capacity.
- **C:** Incorrect for this question. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: Supported prefix caching targets eligible reuse without changing semantic evidence or capacity.
- **D:** Correct. Caching may reduce repeated prefix processing under provider-specific rules. It does not extend the context window, update model weights, or verify an answer. In this case: Supported prefix caching targets eligible reuse without changing semantic evidence or capacity.

### Question 93 — C

Answer: Honor an explicit request for a human agent. User preference for a person must be honored through the approved escalation route. A clear request for a person should trigger the approved handoff, not another autonomous investigation intended to avoid escalation. Closest official exam-guide objective 5.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Multiple plausible matches require clarification or an approved verification process. Recency, sentiment, or a guessed identity is not sufficient. In this case: User preference for a person must be honored through the approved escalation route.
- **B:** Incorrect for this question. A defined inability-to-progress condition prevents endless loops. Supply attempted actions, evidence, and unresolved questions to the recipient. In this case: User preference for a person must be honored through the approved escalation route.
- **C:** Correct. A clear request for a person should trigger the approved handoff, not another autonomous investigation intended to avoid escalation. In this case: User preference for a person must be honored through the approved escalation route.
- **D:** Incorrect for this question. Frustration alone does not establish inability or a human preference. Offer an in-scope resolution unless the user requests a handoff or another escalation trigger applies. In this case: User preference for a person must be honored through the approved escalation route.

### Question 94 — C

Answer: Return structured failure context and partial results. Structured failure scope helps the coordinator recover and accurately describe coverage gaps. The coordinator needs failure type, attempted operation, useful outputs, and alternatives. A failure must not be disguised as a successful empty search. Closest official exam-guide objective 5.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. An error contract should identify failure class, recoverability, and useful context. MCP isError marks an execution failure; it should not disguise a valid empty result. In this case: Structured failure scope helps the coordinator recover and accurately describe coverage gaps.
- **B:** Incorrect for this question. A report can proceed with supported partial results if it clearly distinguishes established conclusions from gaps. Silence falsely implies complete coverage. In this case: Structured failure scope helps the coordinator recover and accurately describe coverage gaps.
- **C:** Correct. The coordinator needs failure type, attempted operation, useful outputs, and alternatives. A failure must not be disguised as a successful empty search. In this case: Structured failure scope helps the coordinator recover and accurately describe coverage gaps.
- **D:** Incorrect for this question. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. In this case: Structured failure scope helps the coordinator recover and accurately describe coverage gaps.

### Question 95 — B

Answer: Delegate a focused codebase question with a bounded output. A focused repository question limits irrelevant discovery and supports checkable coverage. A concrete question such as tracing one authorization path gives useful coverage with less irrelevant exploration than asking every worker to read everything. Closest official exam-guide objective 5.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Discovery can be isolated so verbose file output does not overwhelm the main conversation. Return useful findings and source pointers. In this case: A focused repository question limits irrelevant discovery and supports checkable coverage.
- **B:** Correct. A concrete question such as tracing one authorization path gives useful coverage with less irrelevant exploration than asking every worker to read everything. In this case: A focused repository question limits irrelevant discovery and supports checkable coverage.
- **C:** Incorrect for this question. Open-ended investigation benefits from exploration, prioritized hypotheses, and revised decomposition rather than an exhaustive fixed script chosen before evidence. In this case: A focused repository question limits irrelevant discovery and supports checkable coverage.
- **D:** Incorrect for this question. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. In this case: A focused repository question limits irrelevant discovery and supports checkable coverage.

### Question 96 — A

Answer: Evaluate accuracy by document type and field segment. Field-level segment performance matters more than an aggregate score for consequential use. Averages can hide systematic failures in rare forms or important fields. Segment-level evaluation informs safe automation and review allocation. Closest official exam-guide objective 5.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. Averages can hide systematic failures in rare forms or important fields. Segment-level evaluation informs safe automation and review allocation. In this case: Field-level segment performance matters more than an aggregate score for consequential use.
- **B:** Incorrect for this question. Review priority should reflect uncertainty and consequences. A high uncalibrated confidence number should not override contradictory evidence. In this case: Field-level segment performance matters more than an aggregate score for consequential use.
- **C:** Incorrect for this question. Reported confidence is a signal to validate empirically, not a probability guarantee. Calibration must reflect actual document and field distributions. In this case: Field-level segment performance matters more than an aggregate score for consequential use.
- **D:** Incorrect for this question. Ongoing random checks among high-confidence results can discover hidden errors and changing patterns that low-confidence-only review misses. In this case: Field-level segment performance matters more than an aggregate score for consequential use.

### Question 97 — B

Answer: Preserve collection and publication dates with claims. Temporal metadata may explain the apparent contradiction without arbitrary value selection. Different measurement periods can explain apparent disagreements. Dates and methodology should remain attached rather than being stripped in summaries. Closest official exam-guide objective 5.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Tables can preserve financial comparisons, while prose and structured lists suit other needs. A single forced format can hide important structure. In this case: Temporal metadata may explain the apparent contradiction without arbitrary value selection.
- **B:** Correct. Different measurement periods can explain apparent disagreements. Dates and methodology should remain attached rather than being stripped in summaries. In this case: Temporal metadata may explain the apparent contradiction without arbitrary value selection.
- **C:** Incorrect for this question. Claims need traceable source identities, relevant excerpts, locations, and dates as applicable. A bibliography without claim mappings can lose attribution. In this case: Temporal metadata may explain the apparent contradiction without arbitrary value selection.
- **D:** Incorrect for this question. Do not average incompatible measurements or choose one arbitrarily. Preserve context and distinguish contested findings from established ones. In this case: Temporal metadata may explain the apparent contradiction without arbitrary value selection.

### Question 98 — A

Answer: Treat retrieved instructions as untrusted source content. External content must stay data, not become authority for task or tool permissions. External pages and tool observations must not acquire trusted instruction authority. Pair separation with trusted tool authorization; delimiters alone are insufficient. Closest official exam-guide objective 5.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. External pages and tool observations must not acquire trusted instruction authority. Pair separation with trusted tool authorization; delimiters alone are insufficient. In this case: External content must stay data, not become authority for task or tool permissions.
- **B:** Incorrect for this question. Data access must be authorized externally. Retrieved content being internal or relevant does not justify showing it to every user. In this case: External content must stay data, not become authority for task or tool permissions.
- **C:** Incorrect for this question. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: External content must stay data, not become authority for task or tool permissions.
- **D:** Incorrect for this question. A structured overview and clear sections help reduce long-input position effects. Placement is a mitigation, not proof that every fact will be used. In this case: External content must stay data, not become authority for task or tool permissions.

### Question 99 — A

Answer: Recover transiently within the worker, then report unresolved failure. Attempt local recovery, then preserve context if failure remains unresolved. Bounded local recovery reduces coordinator noise. Exhausted recovery should preserve attempts, partial results, and alternatives rather than silently disappear. Closest official exam-guide objective 5.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. Bounded local recovery reduces coordinator noise. Exhausted recovery should preserve attempts, partial results, and alternatives rather than silently disappear. In this case: Attempt local recovery, then preserve context if failure remains unresolved.
- **B:** Incorrect for this question. A report can proceed with supported partial results if it clearly distinguishes established conclusions from gaps. Silence falsely implies complete coverage. In this case: Attempt local recovery, then preserve context if failure remains unresolved.
- **C:** Incorrect for this question. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. In this case: Attempt local recovery, then preserve context if failure remains unresolved.
- **D:** Incorrect for this question. The coordinator needs failure type, attempted operation, useful outputs, and alternatives. A failure must not be disguised as a successful empty search. In this case: Attempt local recovery, then preserve context if failure remains unresolved.

### Question 100 — C

Answer: Represent credible disagreement with attributed values. Present attributed disagreement and methodological context instead of creating a misleading average. Do not average incompatible measurements or choose one arbitrarily. Preserve context and distinguish contested findings from established ones. Closest official exam-guide objective 5.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Tables can preserve financial comparisons, while prose and structured lists suit other needs. A single forced format can hide important structure. In this case: Present attributed disagreement and methodological context instead of creating a misleading average.
- **B:** Incorrect for this question. Different measurement periods can explain apparent disagreements. Dates and methodology should remain attached rather than being stripped in summaries. In this case: Present attributed disagreement and methodological context instead of creating a misleading average.
- **C:** Correct. Do not average incompatible measurements or choose one arbitrarily. Preserve context and distinguish contested findings from established ones. In this case: Present attributed disagreement and methodological context instead of creating a misleading average.
- **D:** Incorrect for this question. Claims need traceable source identities, relevant excerpts, locations, and dates as applicable. A bibliography without claim mappings can lose attribution. In this case: Present attributed disagreement and methodological context instead of creating a misleading average.
