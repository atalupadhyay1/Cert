# Claude Certified Architect – Foundations (CCAR-F) — Practice Set 1

Agentic Architecture & Orchestration

100 questions · Suggested practice duration: 200 minutes · Practice target: 80%

Tests 1–5 are domain-focused. Test 6 is an expanded blueprint-proportioned review, not an official exam replica. Related concepts recur.

Select ONE best answer for every question. Answer key follows all questions.

Original educational content, not actual, recalled, or copied Anthropic exam items.

## Questions

### 1. A client-tool response contains commentary followed by a tool_use block. What should control the application's next branch?

Domain: Agentic Architecture & Orchestration

- A. Inspect stop_reason and dispatch the appropriate branch
- B. Treat end_turn as the end of the current assistant turn
- C. Use a predictable sequence of specialized stages
- D. Enforce task, iteration, and spending safeguards

### 2. After a lookup finishes, Claude repeats its original question because it never sees the observation. What is missing?

Domain: Agentic Architecture & Orchestration

- A. Start a fresh session with a checked structured summary
- B. Persist structured task state and pending actions
- C. Create a structured handoff with facts, status, and next actions
- D. Append the assistant tool-use blocks and matching tool results

### 3. A response stops with end_turn and contains no pending client-tool requests. What does that signal?

Domain: Agentic Architecture & Orchestration

- A. Inspect stop_reason and dispatch the appropriate branch
- B. Handle the output limit as an incomplete response
- C. Treat end_turn as the end of the current assistant turn
- D. Enforce task, iteration, and spending safeguards

### 4. A generated action proposal stops at the output-token ceiling halfway through its payload. What should the caller do?

Domain: Agentic Architecture & Orchestration

- A. Resume the identified session when its context remains valid
- B. Treat end_turn as the end of the current assistant turn
- C. Handle the output limit as an incomplete response
- D. Compact context while preserving checked facts and open issues

### 5. An agent follows valid tool-use turns but spends indefinitely on an unsolvable task. What additional safeguard is needed?

Domain: Agentic Architecture & Orchestration

- A. Inspect stop_reason and dispatch the appropriate branch
- B. Wait for validated prerequisite outputs
- C. Treat end_turn as the end of the current assistant turn
- D. Enforce task, iteration, and spending safeguards

### 6. Three tools were requested together. How should the caller return their observations without confusing which result belongs to which call?

Domain: Agentic Architecture & Orchestration

- A. Pass relevant evidence and constraints explicitly
- B. Append the assistant tool-use blocks and matching tool results
- C. Normalize tool observations before model consumption
- D. Configure the subagent description, prompt, and tool scope

### 7. Why is checking whether Claude wrote 'finished' a weak loop-termination strategy? Which approach should replace it?

Domain: Agentic Architecture & Orchestration

- A. Inspect stop_reason and dispatch the appropriate branch
- B. Resume the identified session when its context remains valid
- C. Use a predictable sequence of specialized stages
- D. Treat end_turn as the end of the current assistant turn

### 8. An external action requires the verified output of a prior lookup. How should the loop schedule those operations?

Domain: Agentic Architecture & Orchestration

- A. Run independent branches concurrently and join checked results
- B. Evaluate coverage and delegate targeted follow-up work
- C. Wait for validated prerequisite outputs
- D. Select specialists according to the actual task

### 9. A caller may retry the same shipment creation after an uncertain network response. What protects against duplicate creation where supported?

Domain: Agentic Architecture & Orchestration

- A. Resume the identified session when its context remains valid
- B. Normalize tool observations before model consumption
- C. Use a durable idempotency key for the same logical action
- D. Enforce task, iteration, and spending safeguards

### 10. Claude returns end_turn after proposing a disallowed account change. What should determine whether any change is executed?

Domain: Agentic Architecture & Orchestration

- A. Pass relevant evidence and constraints explicitly
- B. Configure the subagent description, prompt, and tool scope
- C. Treat end_turn as the end of the current assistant turn
- D. Enforce prerequisites in trusted execution code

### 11. A research system needs one place to aggregate evidence and handle specialist failures. Which orchestration pattern fits?

Domain: Agentic Architecture & Orchestration

- A. Run independent branches concurrently and join checked results
- B. Fork an independent branch from a valid shared baseline
- C. Route coordination through an orchestrator
- D. Use a predictable sequence of specialized stages

### 12. A simple question needs only document lookup, yet the workflow always invokes five specialists. What change reduces unnecessary work?

Domain: Agentic Architecture & Orchestration

- A. Assign distinct scopes and explicit coverage responsibilities
- B. Wait for validated prerequisite outputs
- C. Select specialists according to the actual task
- D. Use a predictable sequence of specialized stages

### 13. Two research agents repeatedly inspect identical sources while another required topic is ignored. What assignment change is needed?

Domain: Agentic Architecture & Orchestration

- A. Evaluate coverage and delegate targeted follow-up work
- B. Assign distinct scopes and explicit coverage responsibilities
- C. Run independent branches concurrently and join checked results
- D. Route coordination through an orchestrator

### 14. A synthesis draft lacks evidence for one required comparison. What should the coordinator do next?

Domain: Agentic Architecture & Orchestration

- A. Evaluate coverage and delegate targeted follow-up work
- B. Run independent branches concurrently and join checked results
- C. Start a fresh session with a checked structured summary
- D. Use a predictable sequence of specialized stages

### 15. Specialists secretly route failures directly to one another, bypassing central tracking. What architecture change improves controlled information flow?

Domain: Agentic Architecture & Orchestration

- A. Pass relevant evidence and constraints explicitly
- B. Select specialists according to the actual task
- C. Configure the subagent description, prompt, and tool scope
- D. Route coordination through an orchestrator

### 16. Two independent literature searches have no shared mutable resources. Which scheduling option can reduce elapsed research time?

Domain: Agentic Architecture & Orchestration

- A. Use a predictable sequence of specialized stages
- B. Wait for validated prerequisite outputs
- C. Run independent branches concurrently and join checked results
- D. Resume the identified session when its context remains valid

### 17. A synthesis agent needs the completed document-analysis output. Which scheduling choice avoids unsupported synthesis?

Domain: Agentic Architecture & Orchestration

- A. Wait for validated prerequisite outputs
- B. Run independent branches concurrently and join checked results
- C. Fork an independent branch from a valid shared baseline
- D. Select specialists according to the actual task

### 18. A broad investigation is split into many tiny snippets and never addresses the original question. What should be redesigned?

Domain: Agentic Architecture & Orchestration

- A. Assign distinct scopes and explicit coverage responsibilities
- B. Evaluate coverage and delegate targeted follow-up work
- C. Configure the subagent description, prompt, and tool scope
- D. Select specialists according to the actual task

### 19. A coordinator declares success after every worker returns, although the research requirements remain unmet. What evaluation is missing?

Domain: Agentic Architecture & Orchestration

- A. Evaluate coverage and delegate targeted follow-up work
- B. Resume the identified session when its context remains valid
- C. Treat end_turn as the end of the current assistant turn
- D. Enforce task, iteration, and spending safeguards

### 20. A coordinator is instructed to call the summarizer even when a request only asks for a raw source list. What principle should change?

Domain: Agentic Architecture & Orchestration

- A. Route coordination through an orchestrator
- B. Select specialists according to the actual task
- C. Use a predictable sequence of specialized stages
- D. Run independent branches concurrently and join checked results

### 21. A fresh analysis worker knows its task but not the constraints discussed with the coordinator. What should be supplied?

Domain: Agentic Architecture & Orchestration

- A. Resume the identified session when its context remains valid
- B. Configure the subagent description, prompt, and tool scope
- C. Pass relevant evidence and constraints explicitly
- D. Persist structured task state and pending actions

### 22. Claude frequently selects the wrong specialist despite adequate task evidence. Which configuration should clarify when each worker is useful?

Domain: Agentic Architecture & Orchestration

- A. Configure the subagent description, prompt, and tool scope
- B. Enable the version-appropriate subagent invocation tool
- C. Assign distinct scopes and explicit coverage responsibilities
- D. Pass relevant evidence and constraints explicitly

### 23. Delegation never occurs because the coordinator lacks its SDK's invocation tool. What should be checked?

Domain: Agentic Architecture & Orchestration

- A. Give each specialist only task-relevant tools
- B. Enable the version-appropriate subagent invocation tool
- C. Route coordination through an orchestrator
- D. Configure the subagent description, prompt, and tool scope

### 24. The synthesis worker receives only 'use the earlier findings' in a fresh context. What is the best correction?

Domain: Agentic Architecture & Orchestration

- A. Run independent branches concurrently and join checked results
- B. Configure the subagent description, prompt, and tool scope
- C. Persist structured task state and pending actions
- D. Pass relevant evidence and constraints explicitly

### 25. The coordinator can issue several independent subagent calls in one response. What execution strategy does this enable?

Domain: Agentic Architecture & Orchestration

- A. Run independent branches concurrently and join checked results
- B. Use a predictable sequence of specialized stages
- C. Wait for validated prerequisite outputs
- D. Fork an independent branch from a valid shared baseline

### 26. A document specialist should read and analyze sources but never modify them. What agent configuration is relevant?

Domain: Agentic Architecture & Orchestration

- A. Evaluate coverage and delegate targeted follow-up work
- B. Route coordination through an orchestrator
- C. Configure the subagent description, prompt, and tool scope
- D. Pass relevant evidence and constraints explicitly

### 27. A worker receives excerpts without page numbers and cannot substantiate its output. What should the coordinator include?

Domain: Agentic Architecture & Orchestration

- A. Persist structured task state and pending actions
- B. Create a structured handoff with facts, status, and next actions
- C. Pass relevant evidence and constraints explicitly
- D. Resume the identified session when its context remains valid

### 28. A coordinator chooses the correct specialist, but the specialist misunderstands its own objective. Which definition component needs attention?

Domain: Agentic Architecture & Orchestration

- A. Use a predictable sequence of specialized stages
- B. Wait for validated prerequisite outputs
- C. Enforce task, iteration, and spending safeguards
- D. Configure the subagent description, prompt, and tool scope

### 29. Two designers should explore competing designs from the same valid analysis without sharing later conversation changes. What session pattern fits?

Domain: Agentic Architecture & Orchestration

- A. Fork an independent branch from a valid shared baseline
- B. Start a fresh session with a checked structured summary
- C. Resume the identified session when its context remains valid
- D. Persist structured task state and pending actions

### 30. The guide calls the spawning tool Task, but installed SDK examples use Agent. What implementation concern should be addressed?

Domain: Agentic Architecture & Orchestration

- A. Give each specialist only task-relevant tools
- B. Pass relevant evidence and constraints explicitly
- C. Configure the subagent description, prompt, and tool scope
- D. Enable the version-appropriate subagent invocation tool

### 31. A compliance rule must block account export until authorization has been checked. Which mechanism should enforce that ordering?

Domain: Agentic Architecture & Orchestration

- A. Use representative few-shot examples with boundaries
- B. State explicit reportable and non-reportable criteria
- C. Configure the subagent description, prompt, and tool scope
- D. Enforce prerequisites in trusted execution code

### 32. An agent can prepare a contract amendment, but only an authorized manager may approve sending it. What control is required?

Domain: Agentic Architecture & Orchestration

- A. Enforce prerequisites in trusted execution code
- B. Persist structured task state and pending actions
- C. Require authorized approval before the consequential action
- D. Create a structured handoff with facts, status, and next actions

### 33. A specialist receiving an escalation cannot access the original conversation. What should accompany the transfer?

Domain: Agentic Architecture & Orchestration

- A. Persist concise codebase findings with file and symbol pointers
- B. Create a structured handoff with facts, status, and next actions
- C. Resume the identified session when its context remains valid
- D. Pass relevant evidence and constraints explicitly

### 34. A customer reports three unrelated account issues in one message. What task-design step should precede investigation?

Domain: Agentic Architecture & Orchestration

- A. Assign distinct scopes and explicit coverage responsibilities
- B. Wait for validated prerequisite outputs
- C. Use a predictable sequence of specialized stages
- D. Evaluate coverage and delegate targeted follow-up work

### 35. Once a customer's authorized context is established, two unrelated issues can be checked independently. What scheduling approach may help?

Domain: Agentic Architecture & Orchestration

- A. Run independent branches concurrently and join checked results
- B. Use a predictable sequence of specialized stages
- C. Wait for validated prerequisite outputs
- D. Fork an independent branch from a valid shared baseline

### 36. An account closure depends on confirming outstanding charges first. Which scheduling pattern is appropriate?

Domain: Agentic Architecture & Orchestration

- A. Wait for validated prerequisite outputs
- B. Run independent branches concurrently and join checked results
- C. Select specialists according to the actual task
- D. Fork an independent branch from a valid shared baseline

### 37. A required verification rule is sometimes ignored despite clear examples in the prompt. What architectural response addresses enforcement most directly?

Domain: Agentic Architecture & Orchestration

- A. Use representative few-shot examples with boundaries
- B. Enforce prerequisites in trusted execution code
- C. State explicit reportable and non-reportable criteria
- D. Use pre-execution tool interception for blocking policy checks

### 38. A transferred case contains a customer ID but omits what has already been attempted. What handoff improvement is needed?

Domain: Agentic Architecture & Orchestration

- A. Create a structured handoff with facts, status, and next actions
- B. Persist concise codebase findings with file and symbol pointers
- C. Persist structured task state and pending actions
- D. Pass relevant evidence and constraints explicitly

### 39. An audit occurs only after a high-impact action has executed. Which control would enforce the required prior human decision?

Domain: Agentic Architecture & Orchestration

- A. Enforce prerequisites in trusted execution code
- B. Normalize tool observations before model consumption
- C. Enforce task, iteration, and spending safeguards
- D. Require authorized approval before the consequential action

### 40. An interrupted workflow cannot tell which pending external requests have completed. What should its architecture persist?

Domain: Agentic Architecture & Orchestration

- A. Pass relevant evidence and constraints explicitly
- B. Resume the identified session when its context remains valid
- C. Start a fresh session with a checked structured summary
- D. Persist structured task state and pending actions

### 41. A prohibited destructive tool command must be stopped before execution. Which interception stage is relevant?

Domain: Agentic Architecture & Orchestration

- A. Normalize tool observations before model consumption
- B. State explicit reportable and non-reportable criteria
- C. Record detected_pattern and dismissal reasons
- D. Use pre-execution tool interception for blocking policy checks

### 42. Two tools return the same status using numeric codes and descriptive strings. Which processing step should standardize them for Claude?

Domain: Agentic Architecture & Orchestration

- A. State explicit reportable and non-reportable criteria
- B. Use pre-execution tool interception for blocking policy checks
- C. Enforce prerequisites in trusted execution code
- D. Normalize tool observations before model consumption

### 43. A PostToolUse handler detects that a transaction exceeded policy. What interception should instead prevent future violations?

Domain: Agentic Architecture & Orchestration

- A. Persist structured task state and pending actions
- B. Create a structured handoff with facts, status, and next actions
- C. Normalize tool observations before model consumption
- D. Use pre-execution tool interception for blocking policy checks

### 44. A tool returns epoch timestamps while another returns ISO-formatted dates. What hook-oriented approach improves model interpretation?

Domain: Agentic Architecture & Orchestration

- A. Enforce task, iteration, and spending safeguards
- B. Normalize tool observations before model consumption
- C. Use pre-execution tool interception for blocking policy checks
- D. Require authorized approval before the consequential action

### 45. Business policy must hold even when a model is misled by external content. What should remain authoritative?

Domain: Agentic Architecture & Orchestration

- A. State explicit reportable and non-reportable criteria
- B. Configure the subagent description, prompt, and tool scope
- C. Enforce prerequisites in trusted execution code
- D. Use representative few-shot examples with boundaries

### 46. An organization requires prohibited tool arguments to be rejected before the tool runs. Which hook category is appropriate?

Domain: Agentic Architecture & Orchestration

- A. Use pre-execution tool interception for blocking policy checks
- B. Normalize tool observations before model consumption
- C. Pass relevant evidence and constraints explicitly
- D. Use a predictable sequence of specialized stages

### 47. An observation handler converts currency units but silently discards the original unit. What processing responsibility should be improved?

Domain: Agentic Architecture & Orchestration

- A. Handle the output limit as an incomplete response
- B. Compact context while preserving checked facts and open issues
- C. Normalize tool observations before model consumption
- D. Reduce tool output to relevant fields with provenance

### 48. An agent's prompt says approvals are mandatory, but the application accepts any generated action. What enforcement layer is missing?

Domain: Agentic Architecture & Orchestration

- A. Enforce task, iteration, and spending safeguards
- B. Use representative few-shot examples with boundaries
- C. State explicit reportable and non-reportable criteria
- D. Enforce prerequisites in trusted execution code

### 49. The agent proposes an unauthorized operation and the pre-tool interceptor denies it. What prevented the external effect?

Domain: Agentic Architecture & Orchestration

- A. Normalize tool observations before model consumption
- B. Append the assistant tool-use blocks and matching tool results
- C. Use pre-execution tool interception for blocking policy checks
- D. Treat end_turn as the end of the current assistant turn

### 50. A data-cleaning hook replaces unknown statuses with 'success.' What hook design principle should be restored?

Domain: Agentic Architecture & Orchestration

- A. Configure the subagent description, prompt, and tool scope
- B. Resume the identified session when its context remains valid
- C. Normalize tool observations before model consumption
- D. Pass relevant evidence and constraints explicitly

### 51. A report always requires extraction, validation, then formatting with known dependencies. Which decomposition pattern is a natural fit?

Domain: Agentic Architecture & Orchestration

- A. Map the problem and revise subtasks as evidence emerges
- B. Route coordination through an orchestrator
- C. Use a predictable sequence of specialized stages
- D. Fork an independent branch from a valid shared baseline

### 52. An unfamiliar legacy application's failure cause is unknown. Which task strategy should guide investigation?

Domain: Agentic Architecture & Orchestration

- A. Resume the identified session when its context remains valid
- B. Map the problem and revise subtasks as evidence emerges
- C. Wait for validated prerequisite outputs
- D. Use a predictable sequence of specialized stages

### 53. Every file passes local review, but cross-module data handling is broken. What review pass is missing?

Domain: Agentic Architecture & Orchestration

- A. Run independent branches concurrently and join checked results
- B. Configure the subagent description, prompt, and tool scope
- C. Add a cross-file or cross-component integration pass
- D. Assign distinct scopes and explicit coverage responsibilities

### 54. Each reviewer reads the whole repository and produces overlapping comments. What decomposition improvement is most direct?

Domain: Agentic Architecture & Orchestration

- A. Use a predictable sequence of specialized stages
- B. Fork an independent branch from a valid shared baseline
- C. Assign distinct scopes and explicit coverage responsibilities
- D. Route coordination through an orchestrator

### 55. A testing project discovers previously unknown dependencies midway through exploration. How should the plan respond?

Domain: Agentic Architecture & Orchestration

- A. Use a predictable sequence of specialized stages
- B. Wait for validated prerequisite outputs
- C. Select specialists according to the actual task
- D. Map the problem and revise subtasks as evidence emerges

### 56. A well-understood compliance review uses the same ordered checklist for every artifact. Which approach avoids unnecessary replanning?

Domain: Agentic Architecture & Orchestration

- A. Select specialists according to the actual task
- B. Map the problem and revise subtasks as evidence emerges
- C. Evaluate coverage and delegate targeted follow-up work
- D. Use a predictable sequence of specialized stages

### 57. Local schema changes look valid individually but break the producer-consumer contract. What review scope should be added?

Domain: Agentic Architecture & Orchestration

- A. Assign distinct scopes and explicit coverage responsibilities
- B. Configure the subagent description, prompt, and tool scope
- C. Add a cross-file or cross-component integration pass
- D. Run independent branches concurrently and join checked results

### 58. A coordinator receives a complete-looking report that omits the requested risk analysis. What should happen before acceptance?

Domain: Agentic Architecture & Orchestration

- A. Enforce task, iteration, and spending safeguards
- B. Persist structured task state and pending actions
- C. Treat end_turn as the end of the current assistant turn
- D. Evaluate coverage and delegate targeted follow-up work

### 59. A migration must analyze current data before choosing the transformation. Which dependency should be respected?

Domain: Agentic Architecture & Orchestration

- A. Run independent branches concurrently and join checked results
- B. Select specialists according to the actual task
- C. Wait for validated prerequisite outputs
- D. Fork an independent branch from a valid shared baseline

### 60. A user asks for comprehensive tests in a codebase whose important paths are undocumented. What is the best first decomposition strategy?

Domain: Agentic Architecture & Orchestration

- A. Normalize tool observations before model consumption
- B. Map the problem and revise subtasks as evidence emerges
- C. Use a predictable sequence of specialized stages
- D. Resume the identified session when its context remains valid

### 61. An investigation pauses overnight, and relevant files and assumptions remain unchanged. What session option can reuse valid analysis?

Domain: Agentic Architecture & Orchestration

- A. Fork an independent branch from a valid shared baseline
- B. Resume the identified session when its context remains valid
- C. Compact context while preserving checked facts and open issues
- D. Start a fresh session with a checked structured summary

### 62. Most previously inspected modules were replaced after a redesign. What context strategy is safer than blindly resuming stale observations?

Domain: Agentic Architecture & Orchestration

- A. Compact context while preserving checked facts and open issues
- B. Resume the identified session when its context remains valid
- C. Fork an independent branch from a valid shared baseline
- D. Start a fresh session with a checked structured summary

### 63. Only two analyzed files changed before a session resumed. What should the engineer tell the agent?

Domain: Agentic Architecture & Orchestration

- A. Compact context while preserving checked facts and open issues
- B. Tell the resumed agent what changed and recheck affected evidence
- C. Fork an independent branch from a valid shared baseline
- D. Start a fresh session with a checked structured summary

### 64. A team wants separate exploratory conversations for two refactoring approaches from one baseline. Which option fits?

Domain: Agentic Architecture & Orchestration

- A. Resume the identified session when its context remains valid
- B. Start a fresh session with a checked structured summary
- C. Persist structured task state and pending actions
- D. Fork an independent branch from a valid shared baseline

### 65. A long-running task must survive process failure, not merely conversational interruption. What must be durable?

Domain: Agentic Architecture & Orchestration

- A. Compact context while preserving checked facts and open issues
- B. Resume the identified session when its context remains valid
- C. Pass relevant evidence and constraints explicitly
- D. Persist structured task state and pending actions

### 66. An engineer must continue one specific prior investigation, not whichever session happened most recently. What session strategy is relevant?

Domain: Agentic Architecture & Orchestration

- A. Fork an independent branch from a valid shared baseline
- B. Resume the identified session when its context remains valid
- C. Start a fresh session with a checked structured summary
- D. Tell the resumed agent what changed and recheck affected evidence

### 67. A resumed agent references deleted helper functions after a small code update. What targeted correction should be supplied?

Domain: Agentic Architecture & Orchestration

- A. Resume the identified session when its context remains valid
- B. Tell the resumed agent what changed and recheck affected evidence
- C. Compact context while preserving checked facts and open issues
- D. Normalize tool observations before model consumption

### 68. A forked agent edits a real file also used by another branch. What should the architect understand about fork semantics?

Domain: Agentic Architecture & Orchestration

- A. Persist structured task state and pending actions
- B. Run independent branches concurrently and join checked results
- C. Resume the identified session when its context remains valid
- D. Conversation forks do not isolate external filesystem effects

### 69. A prior investigation relies mostly on now-invalid test outputs. What should be preferred when little trustworthy context remains?

Domain: Agentic Architecture & Orchestration

- A. Resume the identified session when its context remains valid
- B. Start a fresh session with a checked structured summary
- C. Tell the resumed agent what changed and recheck affected evidence
- D. Compact context while preserving checked facts and open issues

### 70. An agent resumes after a crash and cannot determine whether an external action was committed. What persistent information was missing?

Domain: Agentic Architecture & Orchestration

- A. Pass relevant evidence and constraints explicitly
- B. Treat end_turn as the end of the current assistant turn
- C. Configure the subagent description, prompt, and tool scope
- D. Persist structured task state and pending actions

### 71. A research team assigns workers by random page ranges but never covers methodology differences. What assignment principle should change?

Domain: Agentic Architecture & Orchestration

- A. Evaluate coverage and delegate targeted follow-up work
- B. Assign distinct scopes and explicit coverage responsibilities
- C. Run independent branches concurrently and join checked results
- D. Enforce task, iteration, and spending safeguards

### 72. A worker understands its role but gives results for the wrong customer because the assigned prompt omitted the verified ID. What is missing?

Domain: Agentic Architecture & Orchestration

- A. Enable the version-appropriate subagent invocation tool
- B. Pass relevant evidence and constraints explicitly
- C. Configure the subagent description, prompt, and tool scope
- D. Route coordination through an orchestrator

### 73. The same action's authorization is checked against yesterday's cached status. What should control execution instead?

Domain: Agentic Architecture & Orchestration

- A. Enforce prerequisites in trusted execution code
- B. Normalize tool observations before model consumption
- C. Require authorized approval before the consequential action
- D. Enforce task, iteration, and spending safeguards

### 74. The model requests a client tool, but the application invents a successful observation without executing it. What should replace that behavior?

Domain: Agentic Architecture & Orchestration

- A. Pass relevant evidence and constraints explicitly
- B. Append the assistant tool-use blocks and matching tool results
- C. Treat end_turn as the end of the current assistant turn
- D. Normalize tool observations before model consumption

### 75. All assigned specialists finish, yet their combined work contains two contradictory recommendations. What should the coordinator assess?

Domain: Agentic Architecture & Orchestration

- A. Route coordination through an orchestrator
- B. Evaluate coverage and delegate targeted follow-up work
- C. Assign distinct scopes and explicit coverage responsibilities
- D. Use a predictable sequence of specialized stages

### 76. Reviewers check function bodies separately and miss a changed caller assumption. What additional analysis is required?

Domain: Agentic Architecture & Orchestration

- A. Run independent branches concurrently and join checked results
- B. Map the problem and revise subtasks as evidence emerges
- C. Use a predictable sequence of specialized stages
- D. Add a cross-file or cross-component integration pass

### 77. A session remains mostly useful after a dependency version changes. What should the resumed agent be asked to re-evaluate?

Domain: Agentic Architecture & Orchestration

- A. Fork an independent branch from a valid shared baseline
- B. Start a fresh session with a checked structured summary
- C. Tell the resumed agent what changed and recheck affected evidence
- D. Resume the identified session when its context remains valid

### 78. A post-tool transformation changes a returned failure into a friendlier but misleading success message. What should be corrected?

Domain: Agentic Architecture & Orchestration

- A. Enforce prerequisites in trusted execution code
- B. Require authorized approval before the consequential action
- C. Normalize tool observations before model consumption
- D. Use pre-execution tool interception for blocking policy checks

### 79. Two specialist types have identical descriptions but different expertise. What configuration improvement supports better delegation?

Domain: Agentic Architecture & Orchestration

- A. Configure the subagent description, prompt, and tool scope
- B. Assign distinct scopes and explicit coverage responsibilities
- C. Pass relevant evidence and constraints explicitly
- D. Enable the version-appropriate subagent invocation tool

### 80. A safety limit ends execution before the requested research is complete. What should the workflow report?

Domain: Agentic Architecture & Orchestration

- A. Handle the output limit as an incomplete response
- B. Report an explicit incomplete or escalated outcome
- C. Inspect stop_reason and dispatch the appropriate branch
- D. Treat end_turn as the end of the current assistant turn

### 81. A query asks for one authoritative document title. Must the coordinator always invoke search, analysis, synthesis, and report agents? Which principle applies?

Domain: Agentic Architecture & Orchestration

- A. Select specialists according to the actual task
- B. Assign distinct scopes and explicit coverage responsibilities
- C. Route coordination through an orchestrator
- D. Use a predictable sequence of specialized stages

### 82. A subagent generates unattributed claims because only prose conclusions were passed to it. What delegation input should improve?

Domain: Agentic Architecture & Orchestration

- A. Persist structured task state and pending actions
- B. Pass relevant evidence and constraints explicitly
- C. Fork an independent branch from a valid shared baseline
- D. Configure the subagent description, prompt, and tool scope

### 83. A case transfer includes a long transcript but no unresolved issue list or proposed next step. What structured artifact is more useful?

Domain: Agentic Architecture & Orchestration

- A. Pass relevant evidence and constraints explicitly
- B. Create a structured handoff with facts, status, and next actions
- C. Persist concise codebase findings with file and symbol pointers
- D. Persist structured task state and pending actions

### 84. An automatic policy check must reject disallowed destinations before network transmission. Where should it act?

Domain: Agentic Architecture & Orchestration

- A. Require authorized approval before the consequential action
- B. Enforce task, iteration, and spending safeguards
- C. Normalize tool observations before model consumption
- D. Use pre-execution tool interception for blocking policy checks

### 85. An incident investigation's next useful test depends on each prior result. Which decomposition strategy fits?

Domain: Agentic Architecture & Orchestration

- A. Map the problem and revise subtasks as evidence emerges
- B. Run independent branches concurrently and join checked results
- C. Wait for validated prerequisite outputs
- D. Use a predictable sequence of specialized stages

### 86. Two alternatives should share original analysis but not each other's later conversational assumptions. What session pattern fits?

Domain: Agentic Architecture & Orchestration

- A. Fork an independent branch from a valid shared baseline
- B. Start a fresh session with a checked structured summary
- C. Compact context while preserving checked facts and open issues
- D. Resume the identified session when its context remains valid

### 87. A loop stops whenever assistant text is nonempty, skipping requested tools in mixed-content responses. What should replace that condition?

Domain: Agentic Architecture & Orchestration

- A. Inspect stop_reason and dispatch the appropriate branch
- B. Handle the output limit as an incomplete response
- C. Treat end_turn as the end of the current assistant turn
- D. Enforce task, iteration, and spending safeguards

### 88. An architect needs consistent failure reporting across workers that currently use incompatible peer-to-peer protocols. Which coordination pattern helps?

Domain: Agentic Architecture & Orchestration

- A. Route coordination through an orchestrator
- B. Assign distinct scopes and explicit coverage responsibilities
- C. Select specialists according to the actual task
- D. Run independent branches concurrently and join checked results

### 89. An agent proposes a refund while identity verification is still pending. What dependency must be honored?

Domain: Agentic Architecture & Orchestration

- A. Fork an independent branch from a valid shared baseline
- B. Select specialists according to the actual task
- C. Run independent branches concurrently and join checked results
- D. Wait for validated prerequisite outputs

### 90. A restarted task finds an old output artifact but no record that validation finished. What should govern recovery?

Domain: Agentic Architecture & Orchestration

- A. Treat end_turn as the end of the current assistant turn
- B. Resume the identified session when its context remains valid
- C. Persist structured task state and pending actions
- D. Pass relevant evidence and constraints explicitly

### 91. The caller receives an unfamiliar stop reason after an API upgrade. Which overall control approach should handle it?

Domain: Agentic Architecture & Orchestration

- A. Treat end_turn as the end of the current assistant turn
- B. Handle the output limit as an incomplete response
- C. Inspect stop_reason and dispatch the appropriate branch
- D. Append the assistant tool-use blocks and matching tool results

### 92. A research summary covers every topic but provides no evidence for a required numerical claim. What should the coordinator request?

Domain: Agentic Architecture & Orchestration

- A. Evaluate coverage and delegate targeted follow-up work
- B. Select specialists according to the actual task
- C. Assign distinct scopes and explicit coverage responsibilities
- D. Run independent branches concurrently and join checked results

### 93. A worker is invoked correctly but receives write tools even though its responsibility is verification only. What configuration should change?

Domain: Agentic Architecture & Orchestration

- A. Configure the subagent description, prompt, and tool scope
- B. Enable the version-appropriate subagent invocation tool
- C. Route coordination through an orchestrator
- D. Pass relevant evidence and constraints explicitly

### 94. A user alters an action payload after it passed a prerequisite check. What must execution enforce?

Domain: Agentic Architecture & Orchestration

- A. Enforce prerequisites in trusted execution code
- B. Create a structured handoff with facts, status, and next actions
- C. Require authorized approval before the consequential action
- D. Normalize tool observations before model consumption

### 95. Different MCP servers report weights in grams and kilograms. Which observation processing should occur before comparison?

Domain: Agentic Architecture & Orchestration

- A. Enforce prerequisites in trusted execution code
- B. Normalize tool observations before model consumption
- C. Use pre-execution tool interception for blocking policy checks
- D. State explicit reportable and non-reportable criteria

### 96. A broad review splits responsibilities into security, behavior, and integration ownership. What principle makes that division useful?

Domain: Agentic Architecture & Orchestration

- A. Assign distinct scopes and explicit coverage responsibilities
- B. Use a predictable sequence of specialized stages
- C. Evaluate coverage and delegate targeted follow-up work
- D. Map the problem and revise subtasks as evidence emerges

### 97. A resumed workflow needs to know which of several external operations still require reconciliation. What record should it consult?

Domain: Agentic Architecture & Orchestration

- A. Resume the identified session when its context remains valid
- B. Persist structured task state and pending actions
- C. Start a fresh session with a checked structured summary
- D. Tell the resumed agent what changed and recheck affected evidence

### 98. A report generator formats the accepted synthesis rather than independently deciding its claims. How should the dependency be scheduled?

Domain: Agentic Architecture & Orchestration

- A. Fork an independent branch from a valid shared baseline
- B. Select specialists according to the actual task
- C. Wait for validated prerequisite outputs
- D. Run independent branches concurrently and join checked results

### 99. An isolated worker needs a prior experiment's measurements but has no access to its artifact store. What should delegation include?

Domain: Agentic Architecture & Orchestration

- A. Resume the identified session when its context remains valid
- B. Pass relevant evidence and constraints explicitly
- C. Configure the subagent description, prompt, and tool scope
- D. Enable the version-appropriate subagent invocation tool

### 100. An escalation contains a recommendation but omits which customer statements remain unverified. What should the handoff distinguish?

Domain: Agentic Architecture & Orchestration

- A. Persist structured task state and pending actions
- B. Create a structured handoff with facts, status, and next actions
- C. Pass relevant evidence and constraints explicitly
- D. Persist concise codebase findings with file and symbol pointers

---

## Answer key and explanations

### Question 1 — A

Answer: Inspect stop_reason and dispatch the appropriate branch. Follow the protocol stop reason, not the presence of ordinary text. The loop follows protocol stop reasons, executes permitted requested tools, and returns observations before continuing. Text appearing in a response does not establish completion. Closest official exam-guide objective 1.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Correct. The loop follows protocol stop reasons, executes permitted requested tools, and returns observations before continuing. Text appearing in a response does not establish completion. In this case: Follow the protocol stop reason, not the presence of ordinary text.
- **B:** Incorrect for this question. This indicates ordinary turn completion, not that every business objective or external action succeeded. Application acceptance checks still apply. In this case: Follow the protocol stop reason, not the presence of ordinary text.
- **C:** Incorrect for this question. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: Follow the protocol stop reason, not the presence of ordinary text.
- **D:** Incorrect for this question. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. In this case: Follow the protocol stop reason, not the presence of ordinary text.

### Question 2 — D

Answer: Append the assistant tool-use blocks and matching tool results. The next request must include the matching result in valid conversation history. Client-tool observations must be returned with the correct tool-use identifiers in a valid message sequence so Claude can use actual results. Closest official exam-guide objective 1.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. A new context can avoid stale tool results when assumptions changed widely. Preserve verified facts, relevant constraints, and pointers rather than import all obsolete history. In this case: The next request must include the matching result in valid conversation history.
- **B:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: The next request must include the matching result in valid conversation history.
- **C:** Incorrect for this question. The recipient needs verified identifiers, completed work, unresolved issues, supporting evidence, and recommended actions, especially when the full transcript is unavailable. In this case: The next request must include the matching result in valid conversation history.
- **D:** Correct. Client-tool observations must be returned with the correct tool-use identifiers in a valid message sequence so Claude can use actual results. In this case: The next request must include the matching result in valid conversation history.

### Question 3 — C

Answer: Treat end_turn as the end of the current assistant turn. The assistant turn ended; business acceptance still needs separate validation. This indicates ordinary turn completion, not that every business objective or external action succeeded. Application acceptance checks still apply. Closest official exam-guide objective 1.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. The loop follows protocol stop reasons, executes permitted requested tools, and returns observations before continuing. Text appearing in a response does not establish completion. In this case: The assistant turn ended; business acceptance still needs separate validation.
- **B:** Incorrect for this question. A max_tokens stop can leave content incomplete. Inspect the response and recover appropriately instead of treating it as normal completion. In this case: The assistant turn ended; business acceptance still needs separate validation.
- **C:** Correct. This indicates ordinary turn completion, not that every business objective or external action succeeded. Application acceptance checks still apply. In this case: The assistant turn ended; business acceptance still needs separate validation.
- **D:** Incorrect for this question. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. In this case: The assistant turn ended; business acceptance still needs separate validation.

### Question 4 — C

Answer: Handle the output limit as an incomplete response. An output-limit stop is incomplete, not evidence of a valid completed action. A max_tokens stop can leave content incomplete. Inspect the response and recover appropriately instead of treating it as normal completion. Closest official exam-guide objective 1.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: An output-limit stop is incomplete, not evidence of a valid completed action.
- **B:** Incorrect for this question. This indicates ordinary turn completion, not that every business objective or external action succeeded. Application acceptance checks still apply. In this case: An output-limit stop is incomplete, not evidence of a valid completed action.
- **C:** Correct. A max_tokens stop can leave content incomplete. Inspect the response and recover appropriately instead of treating it as normal completion. In this case: An output-limit stop is incomplete, not evidence of a valid completed action.
- **D:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: An output-limit stop is incomplete, not evidence of a valid completed action.

### Question 5 — D

Answer: Enforce task, iteration, and spending safeguards. Protocol correctness does not bound total task cost or iteration count. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. Closest official exam-guide objective 1.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. The loop follows protocol stop reasons, executes permitted requested tools, and returns observations before continuing. Text appearing in a response does not establish completion. In this case: Protocol correctness does not bound total task cost or iteration count.
- **B:** Incorrect for this question. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: Protocol correctness does not bound total task cost or iteration count.
- **C:** Incorrect for this question. This indicates ordinary turn completion, not that every business objective or external action succeeded. Application acceptance checks still apply. In this case: Protocol correctness does not bound total task cost or iteration count.
- **D:** Correct. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. In this case: Protocol correctness does not bound total task cost or iteration count.

### Question 6 — B

Answer: Append the assistant tool-use blocks and matching tool results. Match each observation to the original tool-use identifier in the message sequence. Client-tool observations must be returned with the correct tool-use identifiers in a valid message sequence so Claude can use actual results. Closest official exam-guide objective 1.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Match each observation to the original tool-use identifier in the message sequence.
- **B:** Correct. Client-tool observations must be returned with the correct tool-use identifiers in a valid message sequence so Claude can use actual results. In this case: Match each observation to the original tool-use identifier in the message sequence.
- **C:** Incorrect for this question. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. In this case: Match each observation to the original tool-use identifier in the message sequence.
- **D:** Incorrect for this question. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: Match each observation to the original tool-use identifier in the message sequence.

### Question 7 — A

Answer: Inspect stop_reason and dispatch the appropriate branch. Natural-language wording is not the protocol signal for tool execution or turn completion. The loop follows protocol stop reasons, executes permitted requested tools, and returns observations before continuing. Text appearing in a response does not establish completion. Closest official exam-guide objective 1.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Correct. The loop follows protocol stop reasons, executes permitted requested tools, and returns observations before continuing. Text appearing in a response does not establish completion. In this case: Natural-language wording is not the protocol signal for tool execution or turn completion.
- **B:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Natural-language wording is not the protocol signal for tool execution or turn completion.
- **C:** Incorrect for this question. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: Natural-language wording is not the protocol signal for tool execution or turn completion.
- **D:** Incorrect for this question. This indicates ordinary turn completion, not that every business objective or external action succeeded. Application acceptance checks still apply. In this case: Natural-language wording is not the protocol signal for tool execution or turn completion.

### Question 8 — C

Answer: Wait for validated prerequisite outputs. The dependent action cannot safely use a result that does not yet exist. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. Closest official exam-guide objective 1.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: The dependent action cannot safely use a result that does not yet exist.
- **B:** Incorrect for this question. The coordinator compares results with requirements, identifies missing evidence, and commissions focused work rather than blindly repeating the whole pipeline. In this case: The dependent action cannot safely use a result that does not yet exist.
- **C:** Correct. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: The dependent action cannot safely use a result that does not yet exist.
- **D:** Incorrect for this question. Dynamic routing avoids invoking every specialist for a simple request. Selection should follow coverage needs, not a fixed ritual. In this case: The dependent action cannot safely use a result that does not yet exist.

### Question 9 — C

Answer: Use a durable idempotency key for the same logical action. The same logical action should reuse a durable key across retries. Where supported, repeated requests for one operation should resolve to one intended external effect. Generating a new key for each retry defeats duplicate protection. Closest official exam-guide objective 1.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: The same logical action should reuse a durable key across retries.
- **B:** Incorrect for this question. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. In this case: The same logical action should reuse a durable key across retries.
- **C:** Correct. Where supported, repeated requests for one operation should resolve to one intended external effect. Generating a new key for each retry defeats duplicate protection. In this case: The same logical action should reuse a durable key across retries.
- **D:** Incorrect for this question. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. In this case: The same logical action should reuse a durable key across retries.

### Question 10 — D

Answer: Enforce prerequisites in trusted execution code. Turn completion is not permission to perform an external business action. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. Closest official exam-guide objective 1.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Turn completion is not permission to perform an external business action.
- **B:** Incorrect for this question. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: Turn completion is not permission to perform an external business action.
- **C:** Incorrect for this question. This indicates ordinary turn completion, not that every business objective or external action succeeded. Application acceptance checks still apply. In this case: Turn completion is not permission to perform an external business action.
- **D:** Correct. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Turn completion is not permission to perform an external business action.

### Question 11 — C

Answer: Route coordination through an orchestrator. Central coordination gives consistent routing, observation, and recovery decisions. A coordinator manages decomposition, routing, error handling, and aggregation in a hub-and-spoke design. Specialists need not communicate through uncontrolled peer channels. Closest official exam-guide objective 1.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Central coordination gives consistent routing, observation, and recovery decisions.
- **B:** Incorrect for this question. Forking supports divergent explorations without overwriting the original conversation. It does not itself isolate external files or undo side effects. In this case: Central coordination gives consistent routing, observation, and recovery decisions.
- **C:** Correct. A coordinator manages decomposition, routing, error handling, and aggregation in a hub-and-spoke design. Specialists need not communicate through uncontrolled peer channels. In this case: Central coordination gives consistent routing, observation, and recovery decisions.
- **D:** Incorrect for this question. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: Central coordination gives consistent routing, observation, and recovery decisions.

### Question 12 — C

Answer: Select specialists according to the actual task. Choose workers from the actual query needs instead of always executing every role. Dynamic routing avoids invoking every specialist for a simple request. Selection should follow coverage needs, not a fixed ritual. Closest official exam-guide objective 1.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. In this case: Choose workers from the actual query needs instead of always executing every role.
- **B:** Incorrect for this question. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: Choose workers from the actual query needs instead of always executing every role.
- **C:** Correct. Dynamic routing avoids invoking every specialist for a simple request. Selection should follow coverage needs, not a fixed ritual. In this case: Choose workers from the actual query needs instead of always executing every role.
- **D:** Incorrect for this question. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: Choose workers from the actual query needs instead of always executing every role.

### Question 13 — B

Answer: Assign distinct scopes and explicit coverage responsibilities. Distinct scopes and explicit coverage reduce duplication without leaving gaps. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. Closest official exam-guide objective 1.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. The coordinator compares results with requirements, identifies missing evidence, and commissions focused work rather than blindly repeating the whole pipeline. In this case: Distinct scopes and explicit coverage reduce duplication without leaving gaps.
- **B:** Correct. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. In this case: Distinct scopes and explicit coverage reduce duplication without leaving gaps.
- **C:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Distinct scopes and explicit coverage reduce duplication without leaving gaps.
- **D:** Incorrect for this question. A coordinator manages decomposition, routing, error handling, and aggregation in a hub-and-spoke design. Specialists need not communicate through uncontrolled peer channels. In this case: Distinct scopes and explicit coverage reduce duplication without leaving gaps.

### Question 14 — A

Answer: Evaluate coverage and delegate targeted follow-up work. Delegate a targeted evidence gap rather than repeat all completed research. The coordinator compares results with requirements, identifies missing evidence, and commissions focused work rather than blindly repeating the whole pipeline. Closest official exam-guide objective 1.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Correct. The coordinator compares results with requirements, identifies missing evidence, and commissions focused work rather than blindly repeating the whole pipeline. In this case: Delegate a targeted evidence gap rather than repeat all completed research.
- **B:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Delegate a targeted evidence gap rather than repeat all completed research.
- **C:** Incorrect for this question. A new context can avoid stale tool results when assumptions changed widely. Preserve verified facts, relevant constraints, and pointers rather than import all obsolete history. In this case: Delegate a targeted evidence gap rather than repeat all completed research.
- **D:** Incorrect for this question. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: Delegate a targeted evidence gap rather than repeat all completed research.

### Question 15 — D

Answer: Route coordination through an orchestrator. The coordinator should observe and route cross-worker communication and recovery. A coordinator manages decomposition, routing, error handling, and aggregation in a hub-and-spoke design. Specialists need not communicate through uncontrolled peer channels. Closest official exam-guide objective 1.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: The coordinator should observe and route cross-worker communication and recovery.
- **B:** Incorrect for this question. Dynamic routing avoids invoking every specialist for a simple request. Selection should follow coverage needs, not a fixed ritual. In this case: The coordinator should observe and route cross-worker communication and recovery.
- **C:** Incorrect for this question. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: The coordinator should observe and route cross-worker communication and recovery.
- **D:** Correct. A coordinator manages decomposition, routing, error handling, and aggregation in a hub-and-spoke design. Specialists need not communicate through uncontrolled peer channels. In this case: The coordinator should observe and route cross-worker communication and recovery.

### Question 16 — C

Answer: Run independent branches concurrently and join checked results. Independent branches may run together if capacity and access permit. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. Closest official exam-guide objective 1.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: Independent branches may run together if capacity and access permit.
- **B:** Incorrect for this question. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: Independent branches may run together if capacity and access permit.
- **C:** Correct. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Independent branches may run together if capacity and access permit.
- **D:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Independent branches may run together if capacity and access permit.

### Question 17 — A

Answer: Wait for validated prerequisite outputs. The synthesis stage must wait for its actual evidence dependency. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. Closest official exam-guide objective 1.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Correct. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: The synthesis stage must wait for its actual evidence dependency.
- **B:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: The synthesis stage must wait for its actual evidence dependency.
- **C:** Incorrect for this question. Forking supports divergent explorations without overwriting the original conversation. It does not itself isolate external files or undo side effects. In this case: The synthesis stage must wait for its actual evidence dependency.
- **D:** Incorrect for this question. Dynamic routing avoids invoking every specialist for a simple request. Selection should follow coverage needs, not a fixed ritual. In this case: The synthesis stage must wait for its actual evidence dependency.

### Question 18 — A

Answer: Assign distinct scopes and explicit coverage responsibilities. Assignments need meaningful scopes connected to an explicit overall coverage goal. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. Closest official exam-guide objective 1.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Correct. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. In this case: Assignments need meaningful scopes connected to an explicit overall coverage goal.
- **B:** Incorrect for this question. The coordinator compares results with requirements, identifies missing evidence, and commissions focused work rather than blindly repeating the whole pipeline. In this case: Assignments need meaningful scopes connected to an explicit overall coverage goal.
- **C:** Incorrect for this question. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: Assignments need meaningful scopes connected to an explicit overall coverage goal.
- **D:** Incorrect for this question. Dynamic routing avoids invoking every specialist for a simple request. Selection should follow coverage needs, not a fixed ritual. In this case: Assignments need meaningful scopes connected to an explicit overall coverage goal.

### Question 19 — A

Answer: Evaluate coverage and delegate targeted follow-up work. Worker completion does not establish sufficient coverage of the user's goal. The coordinator compares results with requirements, identifies missing evidence, and commissions focused work rather than blindly repeating the whole pipeline. Closest official exam-guide objective 1.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Correct. The coordinator compares results with requirements, identifies missing evidence, and commissions focused work rather than blindly repeating the whole pipeline. In this case: Worker completion does not establish sufficient coverage of the user's goal.
- **B:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Worker completion does not establish sufficient coverage of the user's goal.
- **C:** Incorrect for this question. This indicates ordinary turn completion, not that every business objective or external action succeeded. Application acceptance checks still apply. In this case: Worker completion does not establish sufficient coverage of the user's goal.
- **D:** Incorrect for this question. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. In this case: Worker completion does not establish sufficient coverage of the user's goal.

### Question 20 — B

Answer: Select specialists according to the actual task. Specialist invocation should depend on required output, not an unconditional pipeline. Dynamic routing avoids invoking every specialist for a simple request. Selection should follow coverage needs, not a fixed ritual. Closest official exam-guide objective 1.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. A coordinator manages decomposition, routing, error handling, and aggregation in a hub-and-spoke design. Specialists need not communicate through uncontrolled peer channels. In this case: Specialist invocation should depend on required output, not an unconditional pipeline.
- **B:** Correct. Dynamic routing avoids invoking every specialist for a simple request. Selection should follow coverage needs, not a fixed ritual. In this case: Specialist invocation should depend on required output, not an unconditional pipeline.
- **C:** Incorrect for this question. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: Specialist invocation should depend on required output, not an unconditional pipeline.
- **D:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Specialist invocation should depend on required output, not an unconditional pipeline.

### Question 21 — C

Answer: Pass relevant evidence and constraints explicitly. Relevant constraints must be explicitly present in the worker's task context. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. Closest official exam-guide objective 1.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Relevant constraints must be explicitly present in the worker's task context.
- **B:** Incorrect for this question. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: Relevant constraints must be explicitly present in the worker's task context.
- **C:** Correct. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Relevant constraints must be explicitly present in the worker's task context.
- **D:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Relevant constraints must be explicitly present in the worker's task context.

### Question 22 — A

Answer: Configure the subagent description, prompt, and tool scope. The agent description guides selection separately from its internal task instructions. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. Closest official exam-guide objective 1.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Correct. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: The agent description guides selection separately from its internal task instructions.
- **B:** Incorrect for this question. Delegation needs a permitted launcher. The July 2026 guide calls it Task; newer SDK documentation uses Agent. Check the installed SDK rather than mix names blindly. In this case: The agent description guides selection separately from its internal task instructions.
- **C:** Incorrect for this question. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. In this case: The agent description guides selection separately from its internal task instructions.
- **D:** Incorrect for this question. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: The agent description guides selection separately from its internal task instructions.

### Question 23 — B

Answer: Enable the version-appropriate subagent invocation tool. A configured specialist cannot be invoked without the permitted version-appropriate launcher. Delegation needs a permitted launcher. The July 2026 guide calls it Task; newer SDK documentation uses Agent. Check the installed SDK rather than mix names blindly. Closest official exam-guide objective 1.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: A configured specialist cannot be invoked without the permitted version-appropriate launcher.
- **B:** Correct. Delegation needs a permitted launcher. The July 2026 guide calls it Task; newer SDK documentation uses Agent. Check the installed SDK rather than mix names blindly. In this case: A configured specialist cannot be invoked without the permitted version-appropriate launcher.
- **C:** Incorrect for this question. A coordinator manages decomposition, routing, error handling, and aggregation in a hub-and-spoke design. Specialists need not communicate through uncontrolled peer channels. In this case: A configured specialist cannot be invoked without the permitted version-appropriate launcher.
- **D:** Incorrect for this question. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: A configured specialist cannot be invoked without the permitted version-appropriate launcher.

### Question 24 — D

Answer: Pass relevant evidence and constraints explicitly. Pass the actual findings and source metadata instead of relying on hidden shared memory. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. Closest official exam-guide objective 1.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Pass the actual findings and source metadata instead of relying on hidden shared memory.
- **B:** Incorrect for this question. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: Pass the actual findings and source metadata instead of relying on hidden shared memory.
- **C:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Pass the actual findings and source metadata instead of relying on hidden shared memory.
- **D:** Correct. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Pass the actual findings and source metadata instead of relying on hidden shared memory.

### Question 25 — A

Answer: Run independent branches concurrently and join checked results. Independent invocations can be scheduled concurrently rather than unnecessarily across sequential turns. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. Closest official exam-guide objective 1.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Correct. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Independent invocations can be scheduled concurrently rather than unnecessarily across sequential turns.
- **B:** Incorrect for this question. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: Independent invocations can be scheduled concurrently rather than unnecessarily across sequential turns.
- **C:** Incorrect for this question. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: Independent invocations can be scheduled concurrently rather than unnecessarily across sequential turns.
- **D:** Incorrect for this question. Forking supports divergent explorations without overwriting the original conversation. It does not itself isolate external files or undo side effects. In this case: Independent invocations can be scheduled concurrently rather than unnecessarily across sequential turns.

### Question 26 — C

Answer: Configure the subagent description, prompt, and tool scope. Specialist instructions and scoped tools should match its read-oriented role. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. Closest official exam-guide objective 1.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. The coordinator compares results with requirements, identifies missing evidence, and commissions focused work rather than blindly repeating the whole pipeline. In this case: Specialist instructions and scoped tools should match its read-oriented role.
- **B:** Incorrect for this question. A coordinator manages decomposition, routing, error handling, and aggregation in a hub-and-spoke design. Specialists need not communicate through uncontrolled peer channels. In this case: Specialist instructions and scoped tools should match its read-oriented role.
- **C:** Correct. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: Specialist instructions and scoped tools should match its read-oriented role.
- **D:** Incorrect for this question. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Specialist instructions and scoped tools should match its read-oriented role.

### Question 27 — C

Answer: Pass relevant evidence and constraints explicitly. Task context should keep evidence attached to source locations and identifiers. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. Closest official exam-guide objective 1.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Task context should keep evidence attached to source locations and identifiers.
- **B:** Incorrect for this question. The recipient needs verified identifiers, completed work, unresolved issues, supporting evidence, and recommended actions, especially when the full transcript is unavailable. In this case: Task context should keep evidence attached to source locations and identifiers.
- **C:** Correct. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Task context should keep evidence attached to source locations and identifiers.
- **D:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Task context should keep evidence attached to source locations and identifiers.

### Question 28 — D

Answer: Configure the subagent description, prompt, and tool scope. The worker's prompt defines its behavior; the selection description serves a different purpose. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. Closest official exam-guide objective 1.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: The worker's prompt defines its behavior; the selection description serves a different purpose.
- **B:** Incorrect for this question. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: The worker's prompt defines its behavior; the selection description serves a different purpose.
- **C:** Incorrect for this question. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. In this case: The worker's prompt defines its behavior; the selection description serves a different purpose.
- **D:** Correct. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: The worker's prompt defines its behavior; the selection description serves a different purpose.

### Question 29 — A

Answer: Fork an independent branch from a valid shared baseline. A fork creates independent conversational branches from a common baseline. Forking supports divergent explorations without overwriting the original conversation. It does not itself isolate external files or undo side effects. Closest official exam-guide objective 1.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Correct. Forking supports divergent explorations without overwriting the original conversation. It does not itself isolate external files or undo side effects. In this case: A fork creates independent conversational branches from a common baseline.
- **B:** Incorrect for this question. A new context can avoid stale tool results when assumptions changed widely. Preserve verified facts, relevant constraints, and pointers rather than import all obsolete history. In this case: A fork creates independent conversational branches from a common baseline.
- **C:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: A fork creates independent conversational branches from a common baseline.
- **D:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: A fork creates independent conversational branches from a common baseline.

### Question 30 — D

Answer: Enable the version-appropriate subagent invocation tool. Use the tool name supported by the actual SDK version rather than combining incompatible names. Delegation needs a permitted launcher. The July 2026 guide calls it Task; newer SDK documentation uses Agent. Check the installed SDK rather than mix names blindly. Closest official exam-guide objective 1.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Use the tool name supported by the actual SDK version rather than combining incompatible names.
- **B:** Incorrect for this question. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Use the tool name supported by the actual SDK version rather than combining incompatible names.
- **C:** Incorrect for this question. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: Use the tool name supported by the actual SDK version rather than combining incompatible names.
- **D:** Correct. Delegation needs a permitted launcher. The July 2026 guide calls it Task; newer SDK documentation uses Agent. Check the installed SDK rather than mix names blindly. In this case: Use the tool name supported by the actual SDK version rather than combining incompatible names.

### Question 31 — D

Answer: Enforce prerequisites in trusted execution code. Trusted execution checks provide a real prerequisite boundary beyond prompt guidance. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. Closest official exam-guide objective 1.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Trusted execution checks provide a real prerequisite boundary beyond prompt guidance.
- **B:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Trusted execution checks provide a real prerequisite boundary beyond prompt guidance.
- **C:** Incorrect for this question. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: Trusted execution checks provide a real prerequisite boundary beyond prompt guidance.
- **D:** Correct. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Trusted execution checks provide a real prerequisite boundary beyond prompt guidance.

### Question 32 — C

Answer: Require authorized approval before the consequential action. The specific human authorization must occur before the external communication. Review must gate the external effect, be tied to the intended action, and use current authority. A later audit cannot reliably reverse a completed effect. Closest official exam-guide objective 1.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: The specific human authorization must occur before the external communication.
- **B:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: The specific human authorization must occur before the external communication.
- **C:** Correct. Review must gate the external effect, be tied to the intended action, and use current authority. A later audit cannot reliably reverse a completed effect. In this case: The specific human authorization must occur before the external communication.
- **D:** Incorrect for this question. The recipient needs verified identifiers, completed work, unresolved issues, supporting evidence, and recommended actions, especially when the full transcript is unavailable. In this case: The specific human authorization must occur before the external communication.

### Question 33 — B

Answer: Create a structured handoff with facts, status, and next actions. Provide verified facts, work completed, unresolved issues, and recommended next actions. The recipient needs verified identifiers, completed work, unresolved issues, supporting evidence, and recommended actions, especially when the full transcript is unavailable. Closest official exam-guide objective 1.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Durable notes counter context degradation and support later verification. Record source versions or change cues so notes are not mistaken for permanently current truth. In this case: Provide verified facts, work completed, unresolved issues, and recommended next actions.
- **B:** Correct. The recipient needs verified identifiers, completed work, unresolved issues, supporting evidence, and recommended actions, especially when the full transcript is unavailable. In this case: Provide verified facts, work completed, unresolved issues, and recommended next actions.
- **C:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Provide verified facts, work completed, unresolved issues, and recommended next actions.
- **D:** Incorrect for this question. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Provide verified facts, work completed, unresolved issues, and recommended next actions.

### Question 34 — A

Answer: Assign distinct scopes and explicit coverage responsibilities. Separate concerns explicitly so each can be investigated and later reconciled. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. Closest official exam-guide objective 1.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Correct. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. In this case: Separate concerns explicitly so each can be investigated and later reconciled.
- **B:** Incorrect for this question. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: Separate concerns explicitly so each can be investigated and later reconciled.
- **C:** Incorrect for this question. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: Separate concerns explicitly so each can be investigated and later reconciled.
- **D:** Incorrect for this question. The coordinator compares results with requirements, identifies missing evidence, and commissions focused work rather than blindly repeating the whole pipeline. In this case: Separate concerns explicitly so each can be investigated and later reconciled.

### Question 35 — A

Answer: Run independent branches concurrently and join checked results. Independent issue investigations can run concurrently before a unified response is built. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. Closest official exam-guide objective 1.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Correct. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Independent issue investigations can run concurrently before a unified response is built.
- **B:** Incorrect for this question. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: Independent issue investigations can run concurrently before a unified response is built.
- **C:** Incorrect for this question. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: Independent issue investigations can run concurrently before a unified response is built.
- **D:** Incorrect for this question. Forking supports divergent explorations without overwriting the original conversation. It does not itself isolate external files or undo side effects. In this case: Independent issue investigations can run concurrently before a unified response is built.

### Question 36 — A

Answer: Wait for validated prerequisite outputs. The closure action requires validated prerequisite information before it can proceed. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. Closest official exam-guide objective 1.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Correct. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: The closure action requires validated prerequisite information before it can proceed.
- **B:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: The closure action requires validated prerequisite information before it can proceed.
- **C:** Incorrect for this question. Dynamic routing avoids invoking every specialist for a simple request. Selection should follow coverage needs, not a fixed ritual. In this case: The closure action requires validated prerequisite information before it can proceed.
- **D:** Incorrect for this question. Forking supports divergent explorations without overwriting the original conversation. It does not itself isolate external files or undo side effects. In this case: The closure action requires validated prerequisite information before it can proceed.

### Question 37 — B

Answer: Enforce prerequisites in trusted execution code. Move the prerequisite into trusted execution checks rather than add more demonstrations. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. Closest official exam-guide objective 1.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Move the prerequisite into trusted execution checks rather than add more demonstrations.
- **B:** Correct. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Move the prerequisite into trusted execution checks rather than add more demonstrations.
- **C:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Move the prerequisite into trusted execution checks rather than add more demonstrations.
- **D:** Incorrect for this question. An appropriate pre-tool hook or equivalent trusted gate can deny a disallowed action before it runs. Hook implementation and failure handling must be tested. In this case: Move the prerequisite into trusted execution checks rather than add more demonstrations.

### Question 38 — A

Answer: Create a structured handoff with facts, status, and next actions. The recipient needs status and attempted actions to avoid repeating work or missing unresolved concerns. The recipient needs verified identifiers, completed work, unresolved issues, supporting evidence, and recommended actions, especially when the full transcript is unavailable. Closest official exam-guide objective 1.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Correct. The recipient needs verified identifiers, completed work, unresolved issues, supporting evidence, and recommended actions, especially when the full transcript is unavailable. In this case: The recipient needs status and attempted actions to avoid repeating work or missing unresolved concerns.
- **B:** Incorrect for this question. Durable notes counter context degradation and support later verification. Record source versions or change cues so notes are not mistaken for permanently current truth. In this case: The recipient needs status and attempted actions to avoid repeating work or missing unresolved concerns.
- **C:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: The recipient needs status and attempted actions to avoid repeating work or missing unresolved concerns.
- **D:** Incorrect for this question. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: The recipient needs status and attempted actions to avoid repeating work or missing unresolved concerns.

### Question 39 — D

Answer: Require authorized approval before the consequential action. A pre-action authorized approval gate controls timing; later review cannot reliably undo effects. Review must gate the external effect, be tied to the intended action, and use current authority. A later audit cannot reliably reverse a completed effect. Closest official exam-guide objective 1.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: A pre-action authorized approval gate controls timing; later review cannot reliably undo effects.
- **B:** Incorrect for this question. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. In this case: A pre-action authorized approval gate controls timing; later review cannot reliably undo effects.
- **C:** Incorrect for this question. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. In this case: A pre-action authorized approval gate controls timing; later review cannot reliably undo effects.
- **D:** Correct. Review must gate the external effect, be tied to the intended action, and use current authority. A later audit cannot reliably reverse a completed effect. In this case: A pre-action authorized approval gate controls timing; later review cannot reliably undo effects.

### Question 40 — D

Answer: Persist structured task state and pending actions. Durable action state supports reconciliation instead of guessing from conversational wording. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. Closest official exam-guide objective 1.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Durable action state supports reconciliation instead of guessing from conversational wording.
- **B:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Durable action state supports reconciliation instead of guessing from conversational wording.
- **C:** Incorrect for this question. A new context can avoid stale tool results when assumptions changed widely. Preserve verified facts, relevant constraints, and pointers rather than import all obsolete history. In this case: Durable action state supports reconciliation instead of guessing from conversational wording.
- **D:** Correct. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Durable action state supports reconciliation instead of guessing from conversational wording.

### Question 41 — D

Answer: Use pre-execution tool interception for blocking policy checks. Blocking must occur before the effect, not in observation processing afterward. An appropriate pre-tool hook or equivalent trusted gate can deny a disallowed action before it runs. Hook implementation and failure handling must be tested. Closest official exam-guide objective 1.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. In this case: Blocking must occur before the effect, not in observation processing afterward.
- **B:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Blocking must occur before the effect, not in observation processing afterward.
- **C:** Incorrect for this question. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: Blocking must occur before the effect, not in observation processing afterward.
- **D:** Correct. An appropriate pre-tool hook or equivalent trusted gate can deny a disallowed action before it runs. Hook implementation and failure handling must be tested. In this case: Blocking must occur before the effect, not in observation processing afterward.

### Question 42 — D

Answer: Normalize tool observations before model consumption. Observation normalization makes heterogeneous outputs comparable without changing their meaning. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. Closest official exam-guide objective 1.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Observation normalization makes heterogeneous outputs comparable without changing their meaning.
- **B:** Incorrect for this question. An appropriate pre-tool hook or equivalent trusted gate can deny a disallowed action before it runs. Hook implementation and failure handling must be tested. In this case: Observation normalization makes heterogeneous outputs comparable without changing their meaning.
- **C:** Incorrect for this question. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Observation normalization makes heterogeneous outputs comparable without changing their meaning.
- **D:** Correct. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. In this case: Observation normalization makes heterogeneous outputs comparable without changing their meaning.

### Question 43 — D

Answer: Use pre-execution tool interception for blocking policy checks. Post-execution detection cannot retroactively block an action that already happened. An appropriate pre-tool hook or equivalent trusted gate can deny a disallowed action before it runs. Hook implementation and failure handling must be tested. Closest official exam-guide objective 1.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Post-execution detection cannot retroactively block an action that already happened.
- **B:** Incorrect for this question. The recipient needs verified identifiers, completed work, unresolved issues, supporting evidence, and recommended actions, especially when the full transcript is unavailable. In this case: Post-execution detection cannot retroactively block an action that already happened.
- **C:** Incorrect for this question. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. In this case: Post-execution detection cannot retroactively block an action that already happened.
- **D:** Correct. An appropriate pre-tool hook or equivalent trusted gate can deny a disallowed action before it runs. Hook implementation and failure handling must be tested. In this case: Post-execution detection cannot retroactively block an action that already happened.

### Question 44 — B

Answer: Normalize tool observations before model consumption. Normalize observations before consumption and preserve time-zone and source information. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. Closest official exam-guide objective 1.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. In this case: Normalize observations before consumption and preserve time-zone and source information.
- **B:** Correct. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. In this case: Normalize observations before consumption and preserve time-zone and source information.
- **C:** Incorrect for this question. An appropriate pre-tool hook or equivalent trusted gate can deny a disallowed action before it runs. Hook implementation and failure handling must be tested. In this case: Normalize observations before consumption and preserve time-zone and source information.
- **D:** Incorrect for this question. Review must gate the external effect, be tied to the intended action, and use current authority. A later audit cannot reliably reverse a completed effect. In this case: Normalize observations before consumption and preserve time-zone and source information.

### Question 45 — C

Answer: Enforce prerequisites in trusted execution code. Trusted authorization and prerequisite checks must decide whether execution is allowed. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. Closest official exam-guide objective 1.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Trusted authorization and prerequisite checks must decide whether execution is allowed.
- **B:** Incorrect for this question. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: Trusted authorization and prerequisite checks must decide whether execution is allowed.
- **C:** Correct. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Trusted authorization and prerequisite checks must decide whether execution is allowed.
- **D:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Trusted authorization and prerequisite checks must decide whether execution is allowed.

### Question 46 — A

Answer: Use pre-execution tool interception for blocking policy checks. Pre-execution interception can inspect and deny the requested action. An appropriate pre-tool hook or equivalent trusted gate can deny a disallowed action before it runs. Hook implementation and failure handling must be tested. Closest official exam-guide objective 1.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Correct. An appropriate pre-tool hook or equivalent trusted gate can deny a disallowed action before it runs. Hook implementation and failure handling must be tested. In this case: Pre-execution interception can inspect and deny the requested action.
- **B:** Incorrect for this question. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. In this case: Pre-execution interception can inspect and deny the requested action.
- **C:** Incorrect for this question. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Pre-execution interception can inspect and deny the requested action.
- **D:** Incorrect for this question. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: Pre-execution interception can inspect and deny the requested action.

### Question 47 — C

Answer: Normalize tool observations before model consumption. Normalization should preserve semantics and provenance rather than conceal ambiguous units. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. Closest official exam-guide objective 1.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. A max_tokens stop can leave content incomplete. Inspect the response and recover appropriately instead of treating it as normal completion. In this case: Normalization should preserve semantics and provenance rather than conceal ambiguous units.
- **B:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Normalization should preserve semantics and provenance rather than conceal ambiguous units.
- **C:** Correct. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. In this case: Normalization should preserve semantics and provenance rather than conceal ambiguous units.
- **D:** Incorrect for this question. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: Normalization should preserve semantics and provenance rather than conceal ambiguous units.

### Question 48 — D

Answer: Enforce prerequisites in trusted execution code. Application checks must validate actual approval state independently of model compliance. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. Closest official exam-guide objective 1.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. In this case: Application checks must validate actual approval state independently of model compliance.
- **B:** Incorrect for this question. A small varied demonstration set can teach format and judgment. Include near-miss cases and valid negatives so the model can generalize distinctions. In this case: Application checks must validate actual approval state independently of model compliance.
- **C:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Application checks must validate actual approval state independently of model compliance.
- **D:** Correct. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Application checks must validate actual approval state independently of model compliance.

### Question 49 — C

Answer: Use pre-execution tool interception for blocking policy checks. The trusted pre-execution check stopped execution despite the model's proposal. An appropriate pre-tool hook or equivalent trusted gate can deny a disallowed action before it runs. Hook implementation and failure handling must be tested. Closest official exam-guide objective 1.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. In this case: The trusted pre-execution check stopped execution despite the model's proposal.
- **B:** Incorrect for this question. Client-tool observations must be returned with the correct tool-use identifiers in a valid message sequence so Claude can use actual results. In this case: The trusted pre-execution check stopped execution despite the model's proposal.
- **C:** Correct. An appropriate pre-tool hook or equivalent trusted gate can deny a disallowed action before it runs. Hook implementation and failure handling must be tested. In this case: The trusted pre-execution check stopped execution despite the model's proposal.
- **D:** Incorrect for this question. This indicates ordinary turn completion, not that every business objective or external action succeeded. Application acceptance checks still apply. In this case: The trusted pre-execution check stopped execution despite the model's proposal.

### Question 50 — C

Answer: Normalize tool observations before model consumption. Observation transformation must not turn unknown or failed operations into successful results. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. Closest official exam-guide objective 1.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: Observation transformation must not turn unknown or failed operations into successful results.
- **B:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Observation transformation must not turn unknown or failed operations into successful results.
- **C:** Correct. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. In this case: Observation transformation must not turn unknown or failed operations into successful results.
- **D:** Incorrect for this question. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Observation transformation must not turn unknown or failed operations into successful results.

### Question 51 — C

Answer: Use a predictable sequence of specialized stages. A predictable sequence fits a stable set of dependent transformations. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. Closest official exam-guide objective 1.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Open-ended investigation benefits from exploration, prioritized hypotheses, and revised decomposition rather than an exhaustive fixed script chosen before evidence. In this case: A predictable sequence fits a stable set of dependent transformations.
- **B:** Incorrect for this question. A coordinator manages decomposition, routing, error handling, and aggregation in a hub-and-spoke design. Specialists need not communicate through uncontrolled peer channels. In this case: A predictable sequence fits a stable set of dependent transformations.
- **C:** Correct. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: A predictable sequence fits a stable set of dependent transformations.
- **D:** Incorrect for this question. Forking supports divergent explorations without overwriting the original conversation. It does not itself isolate external files or undo side effects. In this case: A predictable sequence fits a stable set of dependent transformations.

### Question 52 — B

Answer: Map the problem and revise subtasks as evidence emerges. Map structure and revise hypotheses as evidence emerges rather than lock in a complete script. Open-ended investigation benefits from exploration, prioritized hypotheses, and revised decomposition rather than an exhaustive fixed script chosen before evidence. Closest official exam-guide objective 1.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Map structure and revise hypotheses as evidence emerges rather than lock in a complete script.
- **B:** Correct. Open-ended investigation benefits from exploration, prioritized hypotheses, and revised decomposition rather than an exhaustive fixed script chosen before evidence. In this case: Map structure and revise hypotheses as evidence emerges rather than lock in a complete script.
- **C:** Incorrect for this question. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: Map structure and revise hypotheses as evidence emerges rather than lock in a complete script.
- **D:** Incorrect for this question. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: Map structure and revise hypotheses as evidence emerges rather than lock in a complete script.

### Question 53 — C

Answer: Add a cross-file or cross-component integration pass. Interactions require a separate cross-file check beyond isolated local analysis. Local review finds local defects; a separate integration pass checks interactions, interfaces, and data flow across boundaries. Closest official exam-guide objective 1.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Interactions require a separate cross-file check beyond isolated local analysis.
- **B:** Incorrect for this question. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: Interactions require a separate cross-file check beyond isolated local analysis.
- **C:** Correct. Local review finds local defects; a separate integration pass checks interactions, interfaces, and data flow across boundaries. In this case: Interactions require a separate cross-file check beyond isolated local analysis.
- **D:** Incorrect for this question. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. In this case: Interactions require a separate cross-file check beyond isolated local analysis.

### Question 54 — C

Answer: Assign distinct scopes and explicit coverage responsibilities. Give focused responsibilities and define how combined coverage will be checked. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. Closest official exam-guide objective 1.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: Give focused responsibilities and define how combined coverage will be checked.
- **B:** Incorrect for this question. Forking supports divergent explorations without overwriting the original conversation. It does not itself isolate external files or undo side effects. In this case: Give focused responsibilities and define how combined coverage will be checked.
- **C:** Correct. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. In this case: Give focused responsibilities and define how combined coverage will be checked.
- **D:** Incorrect for this question. A coordinator manages decomposition, routing, error handling, and aggregation in a hub-and-spoke design. Specialists need not communicate through uncontrolled peer channels. In this case: Give focused responsibilities and define how combined coverage will be checked.

### Question 55 — D

Answer: Map the problem and revise subtasks as evidence emerges. New evidence should inform priorities and subtasks instead of being ignored to preserve the initial checklist. Open-ended investigation benefits from exploration, prioritized hypotheses, and revised decomposition rather than an exhaustive fixed script chosen before evidence. Closest official exam-guide objective 1.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: New evidence should inform priorities and subtasks instead of being ignored to preserve the initial checklist.
- **B:** Incorrect for this question. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: New evidence should inform priorities and subtasks instead of being ignored to preserve the initial checklist.
- **C:** Incorrect for this question. Dynamic routing avoids invoking every specialist for a simple request. Selection should follow coverage needs, not a fixed ritual. In this case: New evidence should inform priorities and subtasks instead of being ignored to preserve the initial checklist.
- **D:** Correct. Open-ended investigation benefits from exploration, prioritized hypotheses, and revised decomposition rather than an exhaustive fixed script chosen before evidence. In this case: New evidence should inform priorities and subtasks instead of being ignored to preserve the initial checklist.

### Question 56 — D

Answer: Use a predictable sequence of specialized stages. A fixed chain is appropriate when steps and dependencies are already stable. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. Closest official exam-guide objective 1.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Dynamic routing avoids invoking every specialist for a simple request. Selection should follow coverage needs, not a fixed ritual. In this case: A fixed chain is appropriate when steps and dependencies are already stable.
- **B:** Incorrect for this question. Open-ended investigation benefits from exploration, prioritized hypotheses, and revised decomposition rather than an exhaustive fixed script chosen before evidence. In this case: A fixed chain is appropriate when steps and dependencies are already stable.
- **C:** Incorrect for this question. The coordinator compares results with requirements, identifies missing evidence, and commissions focused work rather than blindly repeating the whole pipeline. In this case: A fixed chain is appropriate when steps and dependencies are already stable.
- **D:** Correct. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: A fixed chain is appropriate when steps and dependencies are already stable.

### Question 57 — C

Answer: Add a cross-file or cross-component integration pass. Cross-component validation catches interface failures invisible within one file. Local review finds local defects; a separate integration pass checks interactions, interfaces, and data flow across boundaries. Closest official exam-guide objective 1.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. In this case: Cross-component validation catches interface failures invisible within one file.
- **B:** Incorrect for this question. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: Cross-component validation catches interface failures invisible within one file.
- **C:** Correct. Local review finds local defects; a separate integration pass checks interactions, interfaces, and data flow across boundaries. In this case: Cross-component validation catches interface failures invisible within one file.
- **D:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Cross-component validation catches interface failures invisible within one file.

### Question 58 — D

Answer: Evaluate coverage and delegate targeted follow-up work. Compare the artifact with requirements and commission the missing analysis. The coordinator compares results with requirements, identifies missing evidence, and commissions focused work rather than blindly repeating the whole pipeline. Closest official exam-guide objective 1.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. In this case: Compare the artifact with requirements and commission the missing analysis.
- **B:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Compare the artifact with requirements and commission the missing analysis.
- **C:** Incorrect for this question. This indicates ordinary turn completion, not that every business objective or external action succeeded. Application acceptance checks still apply. In this case: Compare the artifact with requirements and commission the missing analysis.
- **D:** Correct. The coordinator compares results with requirements, identifies missing evidence, and commissions focused work rather than blindly repeating the whole pipeline. In this case: Compare the artifact with requirements and commission the missing analysis.

### Question 59 — C

Answer: Wait for validated prerequisite outputs. Transformation design should depend on actual analyzed data rather than precede it. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. Closest official exam-guide objective 1.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Transformation design should depend on actual analyzed data rather than precede it.
- **B:** Incorrect for this question. Dynamic routing avoids invoking every specialist for a simple request. Selection should follow coverage needs, not a fixed ritual. In this case: Transformation design should depend on actual analyzed data rather than precede it.
- **C:** Correct. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: Transformation design should depend on actual analyzed data rather than precede it.
- **D:** Incorrect for this question. Forking supports divergent explorations without overwriting the original conversation. It does not itself isolate external files or undo side effects. In this case: Transformation design should depend on actual analyzed data rather than precede it.

### Question 60 — B

Answer: Map the problem and revise subtasks as evidence emerges. Explore structure and high-impact paths before committing to a detailed test plan. Open-ended investigation benefits from exploration, prioritized hypotheses, and revised decomposition rather than an exhaustive fixed script chosen before evidence. Closest official exam-guide objective 1.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. In this case: Explore structure and high-impact paths before committing to a detailed test plan.
- **B:** Correct. Open-ended investigation benefits from exploration, prioritized hypotheses, and revised decomposition rather than an exhaustive fixed script chosen before evidence. In this case: Explore structure and high-impact paths before committing to a detailed test plan.
- **C:** Incorrect for this question. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: Explore structure and high-impact paths before committing to a detailed test plan.
- **D:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Explore structure and high-impact paths before committing to a detailed test plan.

### Question 61 — B

Answer: Resume the identified session when its context remains valid. Resume the identified conversation after verifying its context is still applicable. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. Closest official exam-guide objective 1.7: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Forking supports divergent explorations without overwriting the original conversation. It does not itself isolate external files or undo side effects. In this case: Resume the identified conversation after verifying its context is still applicable.
- **B:** Correct. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Resume the identified conversation after verifying its context is still applicable.
- **C:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Resume the identified conversation after verifying its context is still applicable.
- **D:** Incorrect for this question. A new context can avoid stale tool results when assumptions changed widely. Preserve verified facts, relevant constraints, and pointers rather than import all obsolete history. In this case: Resume the identified conversation after verifying its context is still applicable.

### Question 62 — D

Answer: Start a fresh session with a checked structured summary. A fresh checked summary avoids carrying large quantities of obsolete tool evidence. A new context can avoid stale tool results when assumptions changed widely. Preserve verified facts, relevant constraints, and pointers rather than import all obsolete history. Closest official exam-guide objective 1.7: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: A fresh checked summary avoids carrying large quantities of obsolete tool evidence.
- **B:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: A fresh checked summary avoids carrying large quantities of obsolete tool evidence.
- **C:** Incorrect for this question. Forking supports divergent explorations without overwriting the original conversation. It does not itself isolate external files or undo side effects. In this case: A fresh checked summary avoids carrying large quantities of obsolete tool evidence.
- **D:** Correct. A new context can avoid stale tool results when assumptions changed widely. Preserve verified facts, relevant constraints, and pointers rather than import all obsolete history. In this case: A fresh checked summary avoids carrying large quantities of obsolete tool evidence.

### Question 63 — B

Answer: Tell the resumed agent what changed and recheck affected evidence. Identify those changes so affected evidence can be rechecked without needless full re-exploration. Targeted re-analysis works when most prior context remains useful. Explicit change information prevents reliance on stale file or tool observations. Closest official exam-guide objective 1.7: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Identify those changes so affected evidence can be rechecked without needless full re-exploration.
- **B:** Correct. Targeted re-analysis works when most prior context remains useful. Explicit change information prevents reliance on stale file or tool observations. In this case: Identify those changes so affected evidence can be rechecked without needless full re-exploration.
- **C:** Incorrect for this question. Forking supports divergent explorations without overwriting the original conversation. It does not itself isolate external files or undo side effects. In this case: Identify those changes so affected evidence can be rechecked without needless full re-exploration.
- **D:** Incorrect for this question. A new context can avoid stale tool results when assumptions changed widely. Preserve verified facts, relevant constraints, and pointers rather than import all obsolete history. In this case: Identify those changes so affected evidence can be rechecked without needless full re-exploration.

### Question 64 — D

Answer: Fork an independent branch from a valid shared baseline. Independent forks preserve the shared starting analysis while allowing divergence. Forking supports divergent explorations without overwriting the original conversation. It does not itself isolate external files or undo side effects. Closest official exam-guide objective 1.7: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Independent forks preserve the shared starting analysis while allowing divergence.
- **B:** Incorrect for this question. A new context can avoid stale tool results when assumptions changed widely. Preserve verified facts, relevant constraints, and pointers rather than import all obsolete history. In this case: Independent forks preserve the shared starting analysis while allowing divergence.
- **C:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Independent forks preserve the shared starting analysis while allowing divergence.
- **D:** Correct. Forking supports divergent explorations without overwriting the original conversation. It does not itself isolate external files or undo side effects. In this case: Independent forks preserve the shared starting analysis while allowing divergence.

### Question 65 — D

Answer: Persist structured task state and pending actions. Persist task and pending-action state outside transient conversation memory. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. Closest official exam-guide objective 1.7: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Persist task and pending-action state outside transient conversation memory.
- **B:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Persist task and pending-action state outside transient conversation memory.
- **C:** Incorrect for this question. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Persist task and pending-action state outside transient conversation memory.
- **D:** Correct. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Persist task and pending-action state outside transient conversation memory.

### Question 66 — B

Answer: Resume the identified session when its context remains valid. Select the intended named or identified session using supported resumption facilities. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. Closest official exam-guide objective 1.7: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Forking supports divergent explorations without overwriting the original conversation. It does not itself isolate external files or undo side effects. In this case: Select the intended named or identified session using supported resumption facilities.
- **B:** Correct. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Select the intended named or identified session using supported resumption facilities.
- **C:** Incorrect for this question. A new context can avoid stale tool results when assumptions changed widely. Preserve verified facts, relevant constraints, and pointers rather than import all obsolete history. In this case: Select the intended named or identified session using supported resumption facilities.
- **D:** Incorrect for this question. Targeted re-analysis works when most prior context remains useful. Explicit change information prevents reliance on stale file or tool observations. In this case: Select the intended named or identified session using supported resumption facilities.

### Question 67 — B

Answer: Tell the resumed agent what changed and recheck affected evidence. Explicitly describe changed files and require verification of the affected symbols. Targeted re-analysis works when most prior context remains useful. Explicit change information prevents reliance on stale file or tool observations. Closest official exam-guide objective 1.7: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Explicitly describe changed files and require verification of the affected symbols.
- **B:** Correct. Targeted re-analysis works when most prior context remains useful. Explicit change information prevents reliance on stale file or tool observations. In this case: Explicitly describe changed files and require verification of the affected symbols.
- **C:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Explicitly describe changed files and require verification of the affected symbols.
- **D:** Incorrect for this question. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. In this case: Explicitly describe changed files and require verification of the affected symbols.

### Question 68 — D

Answer: Conversation forks do not isolate external filesystem effects. Conversational separation does not by itself isolate external files or side effects. A session fork separates later conversational branches. Shared files, credentials, processes, and remote effects still need independent isolation and coordination controls. Closest official exam-guide objective 1.7: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Conversational separation does not by itself isolate external files or side effects.
- **B:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Conversational separation does not by itself isolate external files or side effects.
- **C:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Conversational separation does not by itself isolate external files or side effects.
- **D:** Correct. A session fork separates later conversational branches. Shared files, credentials, processes, and remote effects still need independent isolation and coordination controls. In this case: Conversational separation does not by itself isolate external files or side effects.

### Question 69 — B

Answer: Start a fresh session with a checked structured summary. Start with a checked current summary rather than reuse obsolete observations wholesale. A new context can avoid stale tool results when assumptions changed widely. Preserve verified facts, relevant constraints, and pointers rather than import all obsolete history. Closest official exam-guide objective 1.7: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Start with a checked current summary rather than reuse obsolete observations wholesale.
- **B:** Correct. A new context can avoid stale tool results when assumptions changed widely. Preserve verified facts, relevant constraints, and pointers rather than import all obsolete history. In this case: Start with a checked current summary rather than reuse obsolete observations wholesale.
- **C:** Incorrect for this question. Targeted re-analysis works when most prior context remains useful. Explicit change information prevents reliance on stale file or tool observations. In this case: Start with a checked current summary rather than reuse obsolete observations wholesale.
- **D:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Start with a checked current summary rather than reuse obsolete observations wholesale.

### Question 70 — D

Answer: Persist structured task state and pending actions. Pending-action records and reconciled completion status are needed for safe recovery. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. Closest official exam-guide objective 1.7: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Pending-action records and reconciled completion status are needed for safe recovery.
- **B:** Incorrect for this question. This indicates ordinary turn completion, not that every business objective or external action succeeded. Application acceptance checks still apply. In this case: Pending-action records and reconciled completion status are needed for safe recovery.
- **C:** Incorrect for this question. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: Pending-action records and reconciled completion status are needed for safe recovery.
- **D:** Correct. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Pending-action records and reconciled completion status are needed for safe recovery.

### Question 71 — B

Answer: Assign distinct scopes and explicit coverage responsibilities. Scopes should follow required questions and coverage responsibilities rather than arbitrary fragments alone. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. Closest official exam-guide objective 1.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. The coordinator compares results with requirements, identifies missing evidence, and commissions focused work rather than blindly repeating the whole pipeline. In this case: Scopes should follow required questions and coverage responsibilities rather than arbitrary fragments alone.
- **B:** Correct. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. In this case: Scopes should follow required questions and coverage responsibilities rather than arbitrary fragments alone.
- **C:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Scopes should follow required questions and coverage responsibilities rather than arbitrary fragments alone.
- **D:** Incorrect for this question. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. In this case: Scopes should follow required questions and coverage responsibilities rather than arbitrary fragments alone.

### Question 72 — B

Answer: Pass relevant evidence and constraints explicitly. Task-specific authorized identity context must accompany the delegation. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. Closest official exam-guide objective 1.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Delegation needs a permitted launcher. The July 2026 guide calls it Task; newer SDK documentation uses Agent. Check the installed SDK rather than mix names blindly. In this case: Task-specific authorized identity context must accompany the delegation.
- **B:** Correct. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Task-specific authorized identity context must accompany the delegation.
- **C:** Incorrect for this question. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: Task-specific authorized identity context must accompany the delegation.
- **D:** Incorrect for this question. A coordinator manages decomposition, routing, error handling, and aggregation in a hub-and-spoke design. Specialists need not communicate through uncontrolled peer channels. In this case: Task-specific authorized identity context must accompany the delegation.

### Question 73 — A

Answer: Enforce prerequisites in trusted execution code. Prerequisites must be validated against current authoritative state before the effect. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. Closest official exam-guide objective 1.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Correct. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Prerequisites must be validated against current authoritative state before the effect.
- **B:** Incorrect for this question. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. In this case: Prerequisites must be validated against current authoritative state before the effect.
- **C:** Incorrect for this question. Review must gate the external effect, be tied to the intended action, and use current authority. A later audit cannot reliably reverse a completed effect. In this case: Prerequisites must be validated against current authoritative state before the effect.
- **D:** Incorrect for this question. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. In this case: Prerequisites must be validated against current authoritative state before the effect.

### Question 74 — B

Answer: Append the assistant tool-use blocks and matching tool results. Return the real authorized execution result or an explicit failure, never fabricated success. Client-tool observations must be returned with the correct tool-use identifiers in a valid message sequence so Claude can use actual results. Closest official exam-guide objective 1.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Return the real authorized execution result or an explicit failure, never fabricated success.
- **B:** Correct. Client-tool observations must be returned with the correct tool-use identifiers in a valid message sequence so Claude can use actual results. In this case: Return the real authorized execution result or an explicit failure, never fabricated success.
- **C:** Incorrect for this question. This indicates ordinary turn completion, not that every business objective or external action succeeded. Application acceptance checks still apply. In this case: Return the real authorized execution result or an explicit failure, never fabricated success.
- **D:** Incorrect for this question. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. In this case: Return the real authorized execution result or an explicit failure, never fabricated success.

### Question 75 — B

Answer: Evaluate coverage and delegate targeted follow-up work. Aggregation must resolve or expose conflicts instead of treating worker completion as acceptance. The coordinator compares results with requirements, identifies missing evidence, and commissions focused work rather than blindly repeating the whole pipeline. Closest official exam-guide objective 1.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. A coordinator manages decomposition, routing, error handling, and aggregation in a hub-and-spoke design. Specialists need not communicate through uncontrolled peer channels. In this case: Aggregation must resolve or expose conflicts instead of treating worker completion as acceptance.
- **B:** Correct. The coordinator compares results with requirements, identifies missing evidence, and commissions focused work rather than blindly repeating the whole pipeline. In this case: Aggregation must resolve or expose conflicts instead of treating worker completion as acceptance.
- **C:** Incorrect for this question. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. In this case: Aggregation must resolve or expose conflicts instead of treating worker completion as acceptance.
- **D:** Incorrect for this question. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: Aggregation must resolve or expose conflicts instead of treating worker completion as acceptance.

### Question 76 — D

Answer: Add a cross-file or cross-component integration pass. A cross-boundary pass must inspect how changed components interact. Local review finds local defects; a separate integration pass checks interactions, interfaces, and data flow across boundaries. Closest official exam-guide objective 1.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: A cross-boundary pass must inspect how changed components interact.
- **B:** Incorrect for this question. Open-ended investigation benefits from exploration, prioritized hypotheses, and revised decomposition rather than an exhaustive fixed script chosen before evidence. In this case: A cross-boundary pass must inspect how changed components interact.
- **C:** Incorrect for this question. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: A cross-boundary pass must inspect how changed components interact.
- **D:** Correct. Local review finds local defects; a separate integration pass checks interactions, interfaces, and data flow across boundaries. In this case: A cross-boundary pass must inspect how changed components interact.

### Question 77 — C

Answer: Tell the resumed agent what changed and recheck affected evidence. Recheck assumptions and evidence affected by the explicit dependency change. Targeted re-analysis works when most prior context remains useful. Explicit change information prevents reliance on stale file or tool observations. Closest official exam-guide objective 1.7: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Forking supports divergent explorations without overwriting the original conversation. It does not itself isolate external files or undo side effects. In this case: Recheck assumptions and evidence affected by the explicit dependency change.
- **B:** Incorrect for this question. A new context can avoid stale tool results when assumptions changed widely. Preserve verified facts, relevant constraints, and pointers rather than import all obsolete history. In this case: Recheck assumptions and evidence affected by the explicit dependency change.
- **C:** Correct. Targeted re-analysis works when most prior context remains useful. Explicit change information prevents reliance on stale file or tool observations. In this case: Recheck assumptions and evidence affected by the explicit dependency change.
- **D:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Recheck assumptions and evidence affected by the explicit dependency change.

### Question 78 — C

Answer: Normalize tool observations before model consumption. Normalization must preserve outcome truth even when presentation becomes more readable. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. Closest official exam-guide objective 1.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Normalization must preserve outcome truth even when presentation becomes more readable.
- **B:** Incorrect for this question. Review must gate the external effect, be tied to the intended action, and use current authority. A later audit cannot reliably reverse a completed effect. In this case: Normalization must preserve outcome truth even when presentation becomes more readable.
- **C:** Correct. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. In this case: Normalization must preserve outcome truth even when presentation becomes more readable.
- **D:** Incorrect for this question. An appropriate pre-tool hook or equivalent trusted gate can deny a disallowed action before it runs. Hook implementation and failure handling must be tested. In this case: Normalization must preserve outcome truth even when presentation becomes more readable.

### Question 79 — A

Answer: Configure the subagent description, prompt, and tool scope. Differentiate when each specialist should be selected, not only their internal prompts. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. Closest official exam-guide objective 1.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Correct. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: Differentiate when each specialist should be selected, not only their internal prompts.
- **B:** Incorrect for this question. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. In this case: Differentiate when each specialist should be selected, not only their internal prompts.
- **C:** Incorrect for this question. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Differentiate when each specialist should be selected, not only their internal prompts.
- **D:** Incorrect for this question. Delegation needs a permitted launcher. The July 2026 guide calls it Task; newer SDK documentation uses Agent. Check the installed SDK rather than mix names blindly. In this case: Differentiate when each specialist should be selected, not only their internal prompts.

### Question 80 — B

Answer: Report an explicit incomplete or escalated outcome. A budget stop must be represented as incomplete or escalated, not as normal goal completion. A safety budget ending the run is not evidence that the user goal was met. Preserve progress and unresolved work for safe continuation or handoff. Closest official exam-guide objective 1.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. A max_tokens stop can leave content incomplete. Inspect the response and recover appropriately instead of treating it as normal completion. In this case: A budget stop must be represented as incomplete or escalated, not as normal goal completion.
- **B:** Correct. A safety budget ending the run is not evidence that the user goal was met. Preserve progress and unresolved work for safe continuation or handoff. In this case: A budget stop must be represented as incomplete or escalated, not as normal goal completion.
- **C:** Incorrect for this question. The loop follows protocol stop reasons, executes permitted requested tools, and returns observations before continuing. Text appearing in a response does not establish completion. In this case: A budget stop must be represented as incomplete or escalated, not as normal goal completion.
- **D:** Incorrect for this question. This indicates ordinary turn completion, not that every business objective or external action succeeded. Application acceptance checks still apply. In this case: A budget stop must be represented as incomplete or escalated, not as normal goal completion.

### Question 81 — A

Answer: Select specialists according to the actual task. Choose the minimal adequate specialist path from the actual task requirements. Dynamic routing avoids invoking every specialist for a simple request. Selection should follow coverage needs, not a fixed ritual. Closest official exam-guide objective 1.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Correct. Dynamic routing avoids invoking every specialist for a simple request. Selection should follow coverage needs, not a fixed ritual. In this case: Choose the minimal adequate specialist path from the actual task requirements.
- **B:** Incorrect for this question. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. In this case: Choose the minimal adequate specialist path from the actual task requirements.
- **C:** Incorrect for this question. A coordinator manages decomposition, routing, error handling, and aggregation in a hub-and-spoke design. Specialists need not communicate through uncontrolled peer channels. In this case: Choose the minimal adequate specialist path from the actual task requirements.
- **D:** Incorrect for this question. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: Choose the minimal adequate specialist path from the actual task requirements.

### Question 82 — B

Answer: Pass relevant evidence and constraints explicitly. Supply source-linked findings and metadata rather than unsupported summaries alone. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. Closest official exam-guide objective 1.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Supply source-linked findings and metadata rather than unsupported summaries alone.
- **B:** Correct. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Supply source-linked findings and metadata rather than unsupported summaries alone.
- **C:** Incorrect for this question. Forking supports divergent explorations without overwriting the original conversation. It does not itself isolate external files or undo side effects. In this case: Supply source-linked findings and metadata rather than unsupported summaries alone.
- **D:** Incorrect for this question. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: Supply source-linked findings and metadata rather than unsupported summaries alone.

### Question 83 — B

Answer: Create a structured handoff with facts, status, and next actions. A focused handoff makes status and action needs explicit for the recipient. The recipient needs verified identifiers, completed work, unresolved issues, supporting evidence, and recommended actions, especially when the full transcript is unavailable. Closest official exam-guide objective 1.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: A focused handoff makes status and action needs explicit for the recipient.
- **B:** Correct. The recipient needs verified identifiers, completed work, unresolved issues, supporting evidence, and recommended actions, especially when the full transcript is unavailable. In this case: A focused handoff makes status and action needs explicit for the recipient.
- **C:** Incorrect for this question. Durable notes counter context degradation and support later verification. Record source versions or change cues so notes are not mistaken for permanently current truth. In this case: A focused handoff makes status and action needs explicit for the recipient.
- **D:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: A focused handoff makes status and action needs explicit for the recipient.

### Question 84 — D

Answer: Use pre-execution tool interception for blocking policy checks. Pre-execution interception is needed before sensitive information leaves the system. An appropriate pre-tool hook or equivalent trusted gate can deny a disallowed action before it runs. Hook implementation and failure handling must be tested. Closest official exam-guide objective 1.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Review must gate the external effect, be tied to the intended action, and use current authority. A later audit cannot reliably reverse a completed effect. In this case: Pre-execution interception is needed before sensitive information leaves the system.
- **B:** Incorrect for this question. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. In this case: Pre-execution interception is needed before sensitive information leaves the system.
- **C:** Incorrect for this question. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. In this case: Pre-execution interception is needed before sensitive information leaves the system.
- **D:** Correct. An appropriate pre-tool hook or equivalent trusted gate can deny a disallowed action before it runs. Hook implementation and failure handling must be tested. In this case: Pre-execution interception is needed before sensitive information leaves the system.

### Question 85 — A

Answer: Map the problem and revise subtasks as evidence emerges. Adapt tasks to observations instead of pretending the whole path is known in advance. Open-ended investigation benefits from exploration, prioritized hypotheses, and revised decomposition rather than an exhaustive fixed script chosen before evidence. Closest official exam-guide objective 1.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Correct. Open-ended investigation benefits from exploration, prioritized hypotheses, and revised decomposition rather than an exhaustive fixed script chosen before evidence. In this case: Adapt tasks to observations instead of pretending the whole path is known in advance.
- **B:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Adapt tasks to observations instead of pretending the whole path is known in advance.
- **C:** Incorrect for this question. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: Adapt tasks to observations instead of pretending the whole path is known in advance.
- **D:** Incorrect for this question. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: Adapt tasks to observations instead of pretending the whole path is known in advance.

### Question 86 — A

Answer: Fork an independent branch from a valid shared baseline. Forked conversations allow independent reasoning from the same valid baseline. Forking supports divergent explorations without overwriting the original conversation. It does not itself isolate external files or undo side effects. Closest official exam-guide objective 1.7: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Correct. Forking supports divergent explorations without overwriting the original conversation. It does not itself isolate external files or undo side effects. In this case: Forked conversations allow independent reasoning from the same valid baseline.
- **B:** Incorrect for this question. A new context can avoid stale tool results when assumptions changed widely. Preserve verified facts, relevant constraints, and pointers rather than import all obsolete history. In this case: Forked conversations allow independent reasoning from the same valid baseline.
- **C:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Forked conversations allow independent reasoning from the same valid baseline.
- **D:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Forked conversations allow independent reasoning from the same valid baseline.

### Question 87 — A

Answer: Inspect stop_reason and dispatch the appropriate branch. Inspect the protocol stop reason and process tool-use content instead of equating text with completion. The loop follows protocol stop reasons, executes permitted requested tools, and returns observations before continuing. Text appearing in a response does not establish completion. Closest official exam-guide objective 1.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Correct. The loop follows protocol stop reasons, executes permitted requested tools, and returns observations before continuing. Text appearing in a response does not establish completion. In this case: Inspect the protocol stop reason and process tool-use content instead of equating text with completion.
- **B:** Incorrect for this question. A max_tokens stop can leave content incomplete. Inspect the response and recover appropriately instead of treating it as normal completion. In this case: Inspect the protocol stop reason and process tool-use content instead of equating text with completion.
- **C:** Incorrect for this question. This indicates ordinary turn completion, not that every business objective or external action succeeded. Application acceptance checks still apply. In this case: Inspect the protocol stop reason and process tool-use content instead of equating text with completion.
- **D:** Incorrect for this question. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. In this case: Inspect the protocol stop reason and process tool-use content instead of equating text with completion.

### Question 88 — A

Answer: Route coordination through an orchestrator. Central orchestration provides one controlled route for aggregation and recovery. A coordinator manages decomposition, routing, error handling, and aggregation in a hub-and-spoke design. Specialists need not communicate through uncontrolled peer channels. Closest official exam-guide objective 1.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Correct. A coordinator manages decomposition, routing, error handling, and aggregation in a hub-and-spoke design. Specialists need not communicate through uncontrolled peer channels. In this case: Central orchestration provides one controlled route for aggregation and recovery.
- **B:** Incorrect for this question. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. In this case: Central orchestration provides one controlled route for aggregation and recovery.
- **C:** Incorrect for this question. Dynamic routing avoids invoking every specialist for a simple request. Selection should follow coverage needs, not a fixed ritual. In this case: Central orchestration provides one controlled route for aggregation and recovery.
- **D:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Central orchestration provides one controlled route for aggregation and recovery.

### Question 89 — D

Answer: Wait for validated prerequisite outputs. The financial action must wait for verified authorized identity and other required checks. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. Closest official exam-guide objective 1.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Forking supports divergent explorations without overwriting the original conversation. It does not itself isolate external files or undo side effects. In this case: The financial action must wait for verified authorized identity and other required checks.
- **B:** Incorrect for this question. Dynamic routing avoids invoking every specialist for a simple request. Selection should follow coverage needs, not a fixed ritual. In this case: The financial action must wait for verified authorized identity and other required checks.
- **C:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: The financial action must wait for verified authorized identity and other required checks.
- **D:** Correct. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: The financial action must wait for verified authorized identity and other required checks.

### Question 90 — C

Answer: Persist structured task state and pending actions. Use durable task status and validate artifacts rather than infer completion from file existence. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. Closest official exam-guide objective 1.7: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. This indicates ordinary turn completion, not that every business objective or external action succeeded. Application acceptance checks still apply. In this case: Use durable task status and validate artifacts rather than infer completion from file existence.
- **B:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Use durable task status and validate artifacts rather than infer completion from file existence.
- **C:** Correct. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Use durable task status and validate artifacts rather than infer completion from file existence.
- **D:** Incorrect for this question. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Use durable task status and validate artifacts rather than infer completion from file existence.

### Question 91 — C

Answer: Inspect stop_reason and dispatch the appropriate branch. Dispatch explicitly by documented protocol state and fail safely rather than assume completion. The loop follows protocol stop reasons, executes permitted requested tools, and returns observations before continuing. Text appearing in a response does not establish completion. Closest official exam-guide objective 1.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. This indicates ordinary turn completion, not that every business objective or external action succeeded. Application acceptance checks still apply. In this case: Dispatch explicitly by documented protocol state and fail safely rather than assume completion.
- **B:** Incorrect for this question. A max_tokens stop can leave content incomplete. Inspect the response and recover appropriately instead of treating it as normal completion. In this case: Dispatch explicitly by documented protocol state and fail safely rather than assume completion.
- **C:** Correct. The loop follows protocol stop reasons, executes permitted requested tools, and returns observations before continuing. Text appearing in a response does not establish completion. In this case: Dispatch explicitly by documented protocol state and fail safely rather than assume completion.
- **D:** Incorrect for this question. Client-tool observations must be returned with the correct tool-use identifiers in a valid message sequence so Claude can use actual results. In this case: Dispatch explicitly by documented protocol state and fail safely rather than assume completion.

### Question 92 — A

Answer: Evaluate coverage and delegate targeted follow-up work. Coverage includes evidential sufficiency, so commission focused verification of the unsupported claim. The coordinator compares results with requirements, identifies missing evidence, and commissions focused work rather than blindly repeating the whole pipeline. Closest official exam-guide objective 1.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Correct. The coordinator compares results with requirements, identifies missing evidence, and commissions focused work rather than blindly repeating the whole pipeline. In this case: Coverage includes evidential sufficiency, so commission focused verification of the unsupported claim.
- **B:** Incorrect for this question. Dynamic routing avoids invoking every specialist for a simple request. Selection should follow coverage needs, not a fixed ritual. In this case: Coverage includes evidential sufficiency, so commission focused verification of the unsupported claim.
- **C:** Incorrect for this question. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. In this case: Coverage includes evidential sufficiency, so commission focused verification of the unsupported claim.
- **D:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Coverage includes evidential sufficiency, so commission focused verification of the unsupported claim.

### Question 93 — A

Answer: Configure the subagent description, prompt, and tool scope. Its tool restrictions should match the bounded verification role. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. Closest official exam-guide objective 1.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Correct. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: Its tool restrictions should match the bounded verification role.
- **B:** Incorrect for this question. Delegation needs a permitted launcher. The July 2026 guide calls it Task; newer SDK documentation uses Agent. Check the installed SDK rather than mix names blindly. In this case: Its tool restrictions should match the bounded verification role.
- **C:** Incorrect for this question. A coordinator manages decomposition, routing, error handling, and aggregation in a hub-and-spoke design. Specialists need not communicate through uncontrolled peer channels. In this case: Its tool restrictions should match the bounded verification role.
- **D:** Incorrect for this question. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Its tool restrictions should match the bounded verification role.

### Question 94 — A

Answer: Enforce prerequisites in trusted execution code. Validate the actual current action and state, not an earlier unrelated approval or check. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. Closest official exam-guide objective 1.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Correct. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Validate the actual current action and state, not an earlier unrelated approval or check.
- **B:** Incorrect for this question. The recipient needs verified identifiers, completed work, unresolved issues, supporting evidence, and recommended actions, especially when the full transcript is unavailable. In this case: Validate the actual current action and state, not an earlier unrelated approval or check.
- **C:** Incorrect for this question. Review must gate the external effect, be tied to the intended action, and use current authority. A later audit cannot reliably reverse a completed effect. In this case: Validate the actual current action and state, not an earlier unrelated approval or check.
- **D:** Incorrect for this question. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. In this case: Validate the actual current action and state, not an earlier unrelated approval or check.

### Question 95 — B

Answer: Normalize tool observations before model consumption. Standardize units without losing original values, units, or source attribution. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. Closest official exam-guide objective 1.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Standardize units without losing original values, units, or source attribution.
- **B:** Correct. A post-tool processing step can standardize timestamps, statuses, units, and field shapes while preserving meaning and provenance. It is too late to block an action already executed. In this case: Standardize units without losing original values, units, or source attribution.
- **C:** Incorrect for this question. An appropriate pre-tool hook or equivalent trusted gate can deny a disallowed action before it runs. Hook implementation and failure handling must be tested. In this case: Standardize units without losing original values, units, or source attribution.
- **D:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Standardize units without losing original values, units, or source attribution.

### Question 96 — A

Answer: Assign distinct scopes and explicit coverage responsibilities. Each scope owns meaningful coverage rather than repeating the whole task. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. Closest official exam-guide objective 1.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Correct. Non-overlapping assignments reduce duplicated research while a coverage checklist helps prevent missing important aspects. In this case: Each scope owns meaningful coverage rather than repeating the whole task.
- **B:** Incorrect for this question. A fixed pipeline fits a known set of dependent transformations. It is different from adaptive investigation whose next task depends on new discoveries. In this case: Each scope owns meaningful coverage rather than repeating the whole task.
- **C:** Incorrect for this question. The coordinator compares results with requirements, identifies missing evidence, and commissions focused work rather than blindly repeating the whole pipeline. In this case: Each scope owns meaningful coverage rather than repeating the whole task.
- **D:** Incorrect for this question. Open-ended investigation benefits from exploration, prioritized hypotheses, and revised decomposition rather than an exhaustive fixed script chosen before evidence. In this case: Each scope owns meaningful coverage rather than repeating the whole task.

### Question 97 — B

Answer: Persist structured task state and pending actions. Structured pending-action state is more dependable than a vague narrative summary. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. Closest official exam-guide objective 1.7: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Structured pending-action state is more dependable than a vague narrative summary.
- **B:** Correct. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Structured pending-action state is more dependable than a vague narrative summary.
- **C:** Incorrect for this question. A new context can avoid stale tool results when assumptions changed widely. Preserve verified facts, relevant constraints, and pointers rather than import all obsolete history. In this case: Structured pending-action state is more dependable than a vague narrative summary.
- **D:** Incorrect for this question. Targeted re-analysis works when most prior context remains useful. Explicit change information prevents reliance on stale file or tool observations. In this case: Structured pending-action state is more dependable than a vague narrative summary.

### Question 98 — C

Answer: Wait for validated prerequisite outputs. Formatting should consume the checked synthesis after it exists. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. Closest official exam-guide objective 1.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Forking supports divergent explorations without overwriting the original conversation. It does not itself isolate external files or undo side effects. In this case: Formatting should consume the checked synthesis after it exists.
- **B:** Incorrect for this question. Dynamic routing avoids invoking every specialist for a simple request. Selection should follow coverage needs, not a fixed ritual. In this case: Formatting should consume the checked synthesis after it exists.
- **C:** Correct. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: Formatting should consume the checked synthesis after it exists.
- **D:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Formatting should consume the checked synthesis after it exists.

### Question 99 — B

Answer: Pass relevant evidence and constraints explicitly. Provide the relevant measurements and provenance explicitly or an authorized accessible reference. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. Closest official exam-guide objective 1.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Resumption can reuse prior analysis when still accurate. The session identity and current external state must be verified; resumption is not automatic freshness. In this case: Provide the relevant measurements and provenance explicitly or an authorized accessible reference.
- **B:** Correct. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Provide the relevant measurements and provenance explicitly or an authorized accessible reference.
- **C:** Incorrect for this question. An agent definition separates when to delegate, what the specialist should do, and which tools it can use. SDK option names are version-specific. In this case: Provide the relevant measurements and provenance explicitly or an authorized accessible reference.
- **D:** Incorrect for this question. Delegation needs a permitted launcher. The July 2026 guide calls it Task; newer SDK documentation uses Agent. Check the installed SDK rather than mix names blindly. In this case: Provide the relevant measurements and provenance explicitly or an authorized accessible reference.

### Question 100 — B

Answer: Create a structured handoff with facts, status, and next actions. Separate verified facts from unresolved claims so the recipient does not mistake assumptions for evidence. The recipient needs verified identifiers, completed work, unresolved issues, supporting evidence, and recommended actions, especially when the full transcript is unavailable. Closest official exam-guide objective 1.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/agent-sdk/subagents

- **A:** Incorrect for this question. Durable state records facts, progress, outputs, and unresolved operations across interruptions. Conversation prose alone is not a reliable transaction log. In this case: Separate verified facts from unresolved claims so the recipient does not mistake assumptions for evidence.
- **B:** Correct. The recipient needs verified identifiers, completed work, unresolved issues, supporting evidence, and recommended actions, especially when the full transcript is unavailable. In this case: Separate verified facts from unresolved claims so the recipient does not mistake assumptions for evidence.
- **C:** Incorrect for this question. Fresh subagents should receive the task-relevant findings, restrictions, and source metadata they need. Do not assume automatic access to the full parent conversation; fork semantics differ. In this case: Separate verified facts from unresolved claims so the recipient does not mistake assumptions for evidence.
- **D:** Incorrect for this question. Durable notes counter context degradation and support later verification. Record source versions or change cues so notes are not mistaken for permanently current truth. In this case: Separate verified facts from unresolved claims so the recipient does not mistake assumptions for evidence.
