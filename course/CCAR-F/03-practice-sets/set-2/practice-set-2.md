# Claude Certified Architect – Foundations (CCAR-F) — Practice Set 2

Tool Design & MCP Integration

100 questions · Suggested practice duration: 200 minutes · Practice target: 80%

Tests 1–5 are domain-focused. Test 6 is an expanded blueprint-proportioned review, not an official exam replica. Related concepts recur.

Select ONE best answer for every question. Answer key follows all questions.

Original educational content, not actual, recalled, or copied Anthropic exam items.

## Questions

### 1. Claude confuses two tools whose descriptions both say 'analyze information.' What should be improved first?

Domain: Tool Design & MCP Integration

- A. Expose a supported MCP resource catalog
- B. Give each specialist only task-relevant tools
- C. Define and validate a precise input schema
- D. Clarify tool purpose, inputs, outputs, and boundaries

### 2. A tool expects an order ID string but receives an object with an unrelated customer name. What interface control is needed?

Domain: Tool Design & MCP Integration

- A. Expose a supported MCP resource catalog
- B. Define and validate a precise input schema
- C. Inspect conflicting routing instructions as well as tool descriptions
- D. Clarify tool purpose, inputs, outputs, and boundaries

### 3. One generic analysis tool alternately extracts fields, summarizes prose, and verifies claims with inconsistent output shapes. What redesign may help?

Domain: Tool Design & MCP Integration

- A. Give each specialist only task-relevant tools
- B. Separate genuinely different tasks into clearly bounded tools
- C. Clarify tool purpose, inputs, outputs, and boundaries
- D. Expose a supported MCP resource catalog

### 4. Two tools differ only by source type, but their names and text never mention that difference. What change most directly improves routing?

Domain: Tool Design & MCP Integration

- A. Give each specialist only task-relevant tools
- B. Clarify tool purpose, inputs, outputs, and boundaries
- C. Separate genuinely different tasks into clearly bounded tools
- D. Expose a supported MCP resource catalog

### 5. Tool descriptions are clear, yet the system prompt maps every mention of 'report' to an unrelated tool. What should be investigated?

Domain: Tool Design & MCP Integration

- A. Give each specialist only task-relevant tools
- B. Inspect conflicting routing instructions as well as tool descriptions
- C. Define and validate a precise input schema
- D. Clarify tool purpose, inputs, outputs, and boundaries

### 6. An assistant should load only approved documentation URLs, not arbitrary internet locations. Which interface is safest as a starting point?

Domain: Tool Design & MCP Integration

- A. Give each specialist only task-relevant tools
- B. Define and validate a precise input schema
- C. Expose a constrained domain-specific operation
- D. Clarify tool purpose, inputs, outputs, and boundaries

### 7. A tool's name is recognizable, but Claude does not know whether it changes records. What description detail matters?

Domain: Tool Design & MCP Integration

- A. Expose a supported MCP resource catalog
- B. Define and validate a precise input schema
- C. Check connected-server discovery and effective availability
- D. Clarify tool purpose, inputs, outputs, and boundaries

### 8. An amount parameter is sometimes interpreted as dollars and sometimes cents. What should the interface define?

Domain: Tool Design & MCP Integration

- A. Define and validate a precise input schema
- B. Inspect conflicting routing instructions as well as tool descriptions
- C. Clarify tool purpose, inputs, outputs, and boundaries
- D. Give each specialist only task-relevant tools

### 9. A new MCP search tool is richer than Grep, but Claude rarely selects it because its description says only 'search.' What should improve?

Domain: Tool Design & MCP Integration

- A. Evaluate a maintained existing integration before writing a custom server
- B. Separate genuinely different tasks into clearly bounded tools
- C. Clarify tool purpose, inputs, outputs, and boundaries
- D. Expose a supported MCP resource catalog

### 10. A tool accepts an arbitrary shell command although the agent only needs approved invoice lookup. What alternative reduces unnecessary power?

Domain: Tool Design & MCP Integration

- A. Clarify tool purpose, inputs, outputs, and boundaries
- B. Expose a constrained domain-specific operation
- C. Give each specialist only task-relevant tools
- D. Define and validate a precise input schema

### 11. A destructive tool has an optional account identifier and silently defaults to the first account. What interface issue needs correction?

Domain: Tool Design & MCP Integration

- A. Clarify tool purpose, inputs, outputs, and boundaries
- B. Inspect conflicting routing instructions as well as tool descriptions
- C. Define and validate a precise input schema
- D. Expose a supported MCP resource catalog

### 12. A search tool may return partial pages, but its documentation implies complete coverage. What contract improvement is needed?

Domain: Tool Design & MCP Integration

- A. Define and validate a precise input schema
- B. Give each specialist only task-relevant tools
- C. Clarify tool purpose, inputs, outputs, and boundaries
- D. Separate genuinely different tasks into clearly bounded tools

### 13. Renaming a tool did not fix selection because an old routing instruction still refers to its previous role. What needs review?

Domain: Tool Design & MCP Integration

- A. Check connected-server discovery and effective availability
- B. Inspect conflicting routing instructions as well as tool descriptions
- C. Expose a supported MCP resource catalog
- D. Clarify tool purpose, inputs, outputs, and boundaries

### 14. A tool called manage_data performs unrelated deletion and summarization with indistinguishable responses. What decomposition may improve clarity?

Domain: Tool Design & MCP Integration

- A. Separate genuinely different tasks into clearly bounded tools
- B. Expose a supported MCP resource catalog
- C. Check connected-server discovery and effective availability
- D. Clarify tool purpose, inputs, outputs, and boundaries

### 15. A region field accepts only an approved set of values. Which interface component can express that constraint?

Domain: Tool Design & MCP Integration

- A. Define and validate a precise input schema
- B. Clarify tool purpose, inputs, outputs, and boundaries
- C. Expose a supported MCP resource catalog
- D. Give each specialist only task-relevant tools

### 16. A tool is safe for current records but misleading for historical questions. What should its documentation explain?

Domain: Tool Design & MCP Integration

- A. Expose a supported MCP resource catalog
- B. Inspect conflicting routing instructions as well as tool descriptions
- C. Define and validate a precise input schema
- D. Clarify tool purpose, inputs, outputs, and boundaries

### 17. A network loader should reject private service endpoints and unauthorized destinations. Which design addresses the actual execution path?

Domain: Tool Design & MCP Integration

- A. Clarify tool purpose, inputs, outputs, and boundaries
- B. Expose a constrained domain-specific operation
- C. Separate genuinely different tasks into clearly bounded tools
- D. Give each specialist only task-relevant tools

### 18. A tool receives a syntactically valid account ID for a user who lacks access. What should the architect remember about schemas?

Domain: Tool Design & MCP Integration

- A. Expose a supported MCP resource catalog
- B. Clarify tool purpose, inputs, outputs, and boundaries
- C. Schema validity does not grant authorization
- D. Give each specialist only task-relevant tools

### 19. A tool returns only an estimate, but users treat it as a committed booking. What must its boundary description clarify?

Domain: Tool Design & MCP Integration

- A. Check connected-server discovery and effective availability
- B. Evaluate a maintained existing integration before writing a custom server
- C. Expose a supported MCP resource catalog
- D. Clarify tool purpose, inputs, outputs, and boundaries

### 20. Selection traces show a repeated phrase in system instructions routing unrelated tasks to the same tool. What should be revised?

Domain: Tool Design & MCP Integration

- A. Give each specialist only task-relevant tools
- B. Inspect conflicting routing instructions as well as tool descriptions
- C. Define and validate a precise input schema
- D. Expose a supported MCP resource catalog

### 21. An MCP execution fails but returns an ordinary empty array with no failure metadata. What should replace that response?

Domain: Tool Design & MCP Integration

- A. Clarify tool purpose, inputs, outputs, and boundaries
- B. Append the assistant tool-use blocks and matching tool results
- C. Represent a successful query with no matches explicitly
- D. Return a structured tool error with category and retryability

### 22. A service is temporarily unavailable and explicitly permits retry. Which recovery class fits?

Domain: Tool Design & MCP Integration

- A. Correct invalid arguments before retrying
- B. Retry a transient failure with bounded backoff
- C. Stop the unauthorized operation and use an approved access path
- D. Explain the non-retryable business-rule outcome

### 23. A tool rejects a date string because its required format is ISO. What should the caller do first?

Domain: Tool Design & MCP Integration

- A. Stop the unauthorized operation and use an approved access path
- B. Explain the non-retryable business-rule outcome
- C. Correct invalid arguments before retrying
- D. Retry a transient failure with bounded backoff

### 24. A protected lookup denies the agent's identity. What recovery policy is appropriate?

Domain: Tool Design & MCP Integration

- A. Represent a successful query with no matches explicitly
- B. Correct invalid arguments before retrying
- C. Stop the unauthorized operation and use an approved access path
- D. Retry a transient failure with bounded backoff

### 25. A cancellation request is rejected because the contract's deadline passed. Which handling fits?

Domain: Tool Design & MCP Integration

- A. Explain the non-retryable business-rule outcome
- B. Stop the unauthorized operation and use an approved access path
- C. Retry a transient failure with bounded backoff
- D. Correct invalid arguments before retrying

### 26. A valid authorized search completes successfully but finds zero matching documents. How should this be represented?

Domain: Tool Design & MCP Integration

- A. Retry a transient failure with bounded backoff
- B. Return a structured tool error with category and retryability
- C. Stop the unauthorized operation and use an approved access path
- D. Represent a successful query with no matches explicitly

### 27. Every tool failure says only 'operation failed.' What response improvement enables intelligent recovery?

Domain: Tool Design & MCP Integration

- A. Return a structured tool error with category and retryability
- B. Expose a supported MCP resource catalog
- C. Clarify tool purpose, inputs, outputs, and boundaries
- D. Check connected-server discovery and effective availability

### 28. A worker can resolve a brief transient failure before involving the coordinator. Which strategy reduces unnecessary central recovery traffic?

Domain: Tool Design & MCP Integration

- A. Retry a transient failure with bounded backoff
- B. Return structured failure context and partial results
- C. Represent a successful query with no matches explicitly
- D. Recover transiently within the worker, then report unresolved failure

### 29. A tool says the account exists but the current identity may not view it. Which failure must not be converted into no matches?

Domain: Tool Design & MCP Integration

- A. Stop the unauthorized operation and use an approved access path
- B. Retry a transient failure with bounded backoff
- C. Correct invalid arguments before retrying
- D. Explain the non-retryable business-rule outcome

### 30. What response pattern should communicate an MCP tool execution failure back to the agent?

Domain: Tool Design & MCP Integration

- A. Return a structured tool error with category and retryability
- B. Append the assistant tool-use blocks and matching tool results
- C. Represent a successful query with no matches explicitly
- D. Clarify tool purpose, inputs, outputs, and boundaries

### 31. A request uses an unsupported enum value while all services are healthy. Which corrective step is most targeted?

Domain: Tool Design & MCP Integration

- A. Retry a transient failure with bounded backoff
- B. Stop the unauthorized operation and use an approved access path
- C. Explain the non-retryable business-rule outcome
- D. Correct invalid arguments before retrying

### 32. A rate-limit response includes a retry-after interval. What handling should respect it?

Domain: Tool Design & MCP Integration

- A. Explain the non-retryable business-rule outcome
- B. Correct invalid arguments before retrying
- C. Retry a transient failure with bounded backoff
- D. Stop the unauthorized operation and use an approved access path

### 33. A tool rejects a validly formed purchase because it exceeds the user's policy limit. What outcome should be explained?

Domain: Tool Design & MCP Integration

- A. Explain the non-retryable business-rule outcome
- B. Retry a transient failure with bounded backoff
- C. Correct invalid arguments before retrying
- D. Stop the unauthorized operation and use an approved access path

### 34. A tool returns partial records before a timeout. What should accompany those records?

Domain: Tool Design & MCP Integration

- A. Represent a successful query with no matches explicitly
- B. Return a structured tool error with category and retryability
- C. Clarify tool purpose, inputs, outputs, and boundaries
- D. Expose a supported MCP resource catalog

### 35. A specialist exhausts its permitted local retries. What should it do next?

Domain: Tool Design & MCP Integration

- A. Stop the unauthorized operation and use an approved access path
- B. Represent a successful query with no matches explicitly
- C. Recover transiently within the worker, then report unresolved failure
- D. Explain the non-retryable business-rule outcome

### 36. A successful database query reports count zero with no execution error. What should the coordinator infer?

Domain: Tool Design & MCP Integration

- A. Represent a successful query with no matches explicitly
- B. Retry a transient failure with bounded backoff
- C. Stop the unauthorized operation and use an approved access path
- D. Return a structured tool error with category and retryability

### 37. An agent proposes trying another employee's token after access is denied. What policy should block that recovery?

Domain: Tool Design & MCP Integration

- A. Stop the unauthorized operation and use an approved access path
- B. Represent a successful query with no matches explicitly
- C. Correct invalid arguments before retrying
- D. Retry a transient failure with bounded backoff

### 38. A worker hides the failed query text and only reports 'search unavailable.' What information should be restored?

Domain: Tool Design & MCP Integration

- A. Return a structured tool error with category and retryability
- B. Check connected-server discovery and effective availability
- C. Expose a supported MCP resource catalog
- D. Clarify tool purpose, inputs, outputs, and boundaries

### 39. A refund is correctly rejected under a known final-sale rule. Should retryability normally be true? Which handling fits?

Domain: Tool Design & MCP Integration

- A. Correct invalid arguments before retrying
- B. Represent a successful query with no matches explicitly
- C. Retry a transient failure with bounded backoff
- D. Explain the non-retryable business-rule outcome

### 40. Several workers forward every brief network hiccup to the coordinator before trying any permitted recovery. What design may help?

Domain: Tool Design & MCP Integration

- A. Stop the unauthorized operation and use an approved access path
- B. Clarify tool purpose, inputs, outputs, and boundaries
- C. Recover transiently within the worker, then report unresolved failure
- D. Represent a successful query with no matches explicitly

### 41. A report synthesizer has tools for unrelated payments and account deletion. What should be changed first?

Domain: Tool Design & MCP Integration

- A. Clarify tool purpose, inputs, outputs, and boundaries
- B. Separate genuinely different tasks into clearly bounded tools
- C. Give each specialist only task-relevant tools
- D. Expose a supported MCP resource catalog

### 42. A request may be answered directly or by a tool depending on need. Which tool-choice mode fits?

Domain: Tool Design & MCP Integration

- A. Give each specialist only task-relevant tools
- B. Use tool_choice with type any
- C. Use tool_choice with type auto
- D. Force the required named tool for that turn

### 43. A request must produce a tool call but may choose among several extraction tools. Which mode fits?

Domain: Tool Design & MCP Integration

- A. Give each specialist only task-relevant tools
- B. Use tool_choice with type any
- C. Use tool_choice with type auto
- D. Force the required named tool for that turn

### 44. A workflow must select its named metadata-extraction tool for this turn. Which configuration is relevant?

Domain: Tool Design & MCP Integration

- A. Use tool_choice with type any
- B. Force the required named tool for that turn
- C. Use tool_choice with type auto
- D. Give each specialist only task-relevant tools

### 45. An agent's tool list grows from a focused handful to dozens of unrelated operations and selection quality falls. What should be reconsidered?

Domain: Tool Design & MCP Integration

- A. Clarify tool purpose, inputs, outputs, and boundaries
- B. Separate genuinely different tasks into clearly bounded tools
- C. Check connected-server discovery and effective availability
- D. Give each specialist only task-relevant tools

### 46. A synthesis worker occasionally needs a narrow fact check but should not browse arbitrarily. What tool design balances those needs?

Domain: Tool Design & MCP Integration

- A. Clarify tool purpose, inputs, outputs, and boundaries
- B. Define and validate a precise input schema
- C. Give each specialist only task-relevant tools
- D. Expose a constrained domain-specific operation

### 47. Using any sometimes calls the wrong extraction tool when a specific schema is required. What should replace it for that turn?

Domain: Tool Design & MCP Integration

- A. Force the required named tool for that turn
- B. Use tool_choice with type any
- C. Use tool_choice with type auto
- D. Wait for validated prerequisite outputs

### 48. Why can tool_choice auto fail a requirement that every request use an extraction tool? Which mode permits that behavior?

Domain: Tool Design & MCP Integration

- A. Expose a supported MCP resource catalog
- B. Use tool_choice with type auto
- C. Use tool_choice with type any
- D. Force the required named tool for that turn

### 49. A specialist misuses a tool outside its expertise even though the tool description is accurate. What configuration most directly removes that possibility?

Domain: Tool Design & MCP Integration

- A. Give each specialist only task-relevant tools
- B. Evaluate a maintained existing integration before writing a custom server
- C. Clarify tool purpose, inputs, outputs, and boundaries
- D. Check connected-server discovery and effective availability

### 50. A named tool must run before enrichment, but enrichment is allowed only afterward. What should ensure the first selection?

Domain: Tool Design & MCP Integration

- A. Give each specialist only task-relevant tools
- B. Use tool_choice with type auto
- C. Force the required named tool for that turn
- D. Use tool_choice with type any

### 51. A team needs the same approved MCP server setup available from its repository. Where should shared configuration live?

Domain: Tool Design & MCP Integration

- A. Use user-scoped MCP configuration for personal servers
- B. Check connected-server discovery and effective availability
- C. Expose a supported MCP resource catalog
- D. Use project-scoped .mcp.json for shared server configuration

### 52. One developer wants an experimental MCP server without changing teammates' setup. Which scope fits?

Domain: Tool Design & MCP Integration

- A. Evaluate a maintained existing integration before writing a custom server
- B. Use user-scoped MCP configuration for personal servers
- C. Use project-scoped .mcp.json for shared server configuration
- D. Expose a supported MCP resource catalog

### 53. A shared MCP configuration needs authentication but must not contain a literal production token. What pattern fits?

Domain: Tool Design & MCP Integration

- A. Clarify tool purpose, inputs, outputs, and boundaries
- B. Reference runtime environment variables instead of committing tokens
- C. Use project-scoped .mcp.json for shared server configuration
- D. Use user-scoped MCP configuration for personal servers

### 54. An agent repeatedly calls exploratory tools merely to learn available document categories. What MCP interface may expose that catalog?

Domain: Tool Design & MCP Integration

- A. Check connected-server discovery and effective availability
- B. Clarify tool purpose, inputs, outputs, and boundaries
- C. Expose a supported MCP resource catalog
- D. Separate genuinely different tasks into clearly bounded tools

### 55. A server is listed in configuration but its tools never appear. What should be investigated?

Domain: Tool Design & MCP Integration

- A. Expose a supported MCP resource catalog
- B. Use project-scoped .mcp.json for shared server configuration
- C. Check connected-server discovery and effective availability
- D. Use user-scoped MCP configuration for personal servers

### 56. A standard issue-tracker integration already has a maintained suitable server. What should precede writing a custom equivalent?

Domain: Tool Design & MCP Integration

- A. Clarify tool purpose, inputs, outputs, and boundaries
- B. Separate genuinely different tasks into clearly bounded tools
- C. Expose a supported MCP resource catalog
- D. Evaluate a maintained existing integration before writing a custom server

### 57. Claude prefers a basic built-in search over a richer MCP search because the latter's capabilities are undocumented. What needs improvement?

Domain: Tool Design & MCP Integration

- A. Clarify tool purpose, inputs, outputs, and boundaries
- B. Expose a supported MCP resource catalog
- C. Check connected-server discovery and effective availability
- D. Give each specialist only task-relevant tools

### 58. A database integration should expose its read-only schema catalog before queries are constructed. Which MCP primitive is relevant?

Domain: Tool Design & MCP Integration

- A. Expose a supported MCP resource catalog
- B. Define and validate a precise input schema
- C. Check connected-server discovery and effective availability
- D. Clarify tool purpose, inputs, outputs, and boundaries

### 59. A token was removed from .mcp.json but remains printed in startup logs. What credential practice is still necessary?

Domain: Tool Design & MCP Integration

- A. Give each specialist only task-relevant tools
- B. Reference runtime environment variables instead of committing tokens
- C. Check connected-server discovery and effective availability
- D. Clarify tool purpose, inputs, outputs, and boundaries

### 60. A new teammate lacks an approved server because it exists only in another developer's home configuration. What scope correction is needed?

Domain: Tool Design & MCP Integration

- A. Give each specialist only task-relevant tools
- B. Use project-scoped .mcp.json for shared server configuration
- C. Use user-scoped MCP configuration for personal servers
- D. Expose a supported MCP resource catalog

### 61. An engineer needs to find every occurrence of an error message inside repository files. Which built-in tool fits?

Domain: Tool Design & MCP Integration

- A. Use Read to inspect current file contents
- B. Use Bash for an authorized command with bounded execution
- C. Use Glob for filename or path-pattern discovery
- D. Use Grep for content-pattern searches

### 62. An engineer needs paths matching **/*.spec.ts before opening their contents. Which tool fits?

Domain: Tool Design & MCP Integration

- A. Use Grep for content-pattern searches
- B. Use Glob for filename or path-pattern discovery
- C. Use Edit with a verified unique anchor
- D. Use Read to inspect current file contents

### 63. A file was identified, and the agent must inspect its current function body before changing it. Which tool fits?

Domain: Tool Design & MCP Integration

- A. Use Glob for filename or path-pattern discovery
- B. Use Edit with a verified unique anchor
- C. Use Read to inspect current file contents
- D. Read the current file and write a checked replacement

### 64. A small change has one verified unique text anchor in the current file. Which operation is most targeted?

Domain: Tool Design & MCP Integration

- A. Use Bash for an authorized command with bounded execution
- B. Use Read to inspect current file contents
- C. Read the current file and write a checked replacement
- D. Use Edit with a verified unique anchor

### 65. Repeated identical anchors make a targeted replacement ambiguous. What fallback can be used with care?

Domain: Tool Design & MCP Integration

- A. Use Edit with a verified unique anchor
- B. Use Glob for filename or path-pattern discovery
- C. Read the current file and write a checked replacement
- D. Use Grep for content-pattern searches

### 66. The next authorized step is running the project's unit-test command. Which tool category fits?

Domain: Tool Design & MCP Integration

- A. Use Bash for an authorized command with bounded execution
- B. Use Grep for content-pattern searches
- C. Use Glob for filename or path-pattern discovery
- D. Use Read to inspect current file contents

### 67. A literal search finds no callers because a function is re-exported under several names. What exploration strategy is needed?

Domain: Tool Design & MCP Integration

- A. Search exported aliases and wrappers as well as the original symbol
- B. Use Read to inspect current file contents
- C. Use Glob for filename or path-pattern discovery
- D. Use Grep for content-pattern searches

### 68. A legacy investigation should first locate imports mentioning a specific client library. Which tool is most direct?

Domain: Tool Design & MCP Integration

- A. Use Grep for content-pattern searches
- B. Read the current file and write a checked replacement
- C. Use Edit with a verified unique anchor
- D. Use Glob for filename or path-pattern discovery

### 69. The task is finding configuration filenames ending in .yaml, regardless of their contents. Which tool fits?

Domain: Tool Design & MCP Integration

- A. Read the current file and write a checked replacement
- B. Use Grep for content-pattern searches
- C. Use Bash for an authorized command with bounded execution
- D. Use Glob for filename or path-pattern discovery

### 70. A proposed edit relies on a file snapshot from before another change. What should occur first?

Domain: Tool Design & MCP Integration

- A. Use Edit with a verified unique anchor
- B. Use Glob for filename or path-pattern discovery
- C. Use Read to inspect current file contents
- D. Read the current file and write a checked replacement

### 71. A research agent can select a deletion operation it will never need. What change reduces both confusion and excess capability?

Domain: Tool Design & MCP Integration

- A. Give each specialist only task-relevant tools
- B. Expose a supported MCP resource catalog
- C. Define and validate a precise input schema
- D. Clarify tool purpose, inputs, outputs, and boundaries

### 72. Two configured MCP servers expose similar tools, but one failed authentication. What should the agent's application verify?

Domain: Tool Design & MCP Integration

- A. Evaluate a maintained existing integration before writing a custom server
- B. Clarify tool purpose, inputs, outputs, and boundaries
- C. Expose a supported MCP resource catalog
- D. Check connected-server discovery and effective availability

### 73. A search returns no records from an approved source without error. What should not be misreported as a failure?

Domain: Tool Design & MCP Integration

- A. Stop the unauthorized operation and use an approved access path
- B. Return a structured tool error with category and retryability
- C. Retry a transient failure with bounded backoff
- D. Represent a successful query with no matches explicitly

### 74. A document-fetch tool is being repurposed to contact arbitrary internal hosts. What boundary should be enforced?

Domain: Tool Design & MCP Integration

- A. Expose a constrained domain-specific operation
- B. Clarify tool purpose, inputs, outputs, and boundaries
- C. Separate genuinely different tasks into clearly bounded tools
- D. Define and validate a precise input schema

### 75. A change to a public function must account for wrappers and renamed imports. Which investigation is relevant?

Domain: Tool Design & MCP Integration

- A. Use Glob for filename or path-pattern discovery
- B. Search exported aliases and wrappers as well as the original symbol
- C. Read the current file and write a checked replacement
- D. Use Bash for an authorized command with bounded execution

### 76. A server returns a precise missing-argument error. Which recovery should be attempted before resubmission?

Domain: Tool Design & MCP Integration

- A. Retry a transient failure with bounded backoff
- B. Correct invalid arguments before retrying
- C. Explain the non-retryable business-rule outcome
- D. Stop the unauthorized operation and use an approved access path

### 77. A team wants reproducible server setup while keeping each user's credential private. What authentication pattern fits?

Domain: Tool Design & MCP Integration

- A. Use user-scoped MCP configuration for personal servers
- B. Reference runtime environment variables instead of committing tokens
- C. Expose a supported MCP resource catalog
- D. Use project-scoped .mcp.json for shared server configuration

### 78. There are several allowed schema tools, and the model should choose the document-appropriate one while always using a tool. Which mode fits?

Domain: Tool Design & MCP Integration

- A. Force the required named tool for that turn
- B. Give each specialist only task-relevant tools
- C. Use tool_choice with type any
- D. Use tool_choice with type auto

### 79. An engineer wants to update one current unique configuration value without regenerating the whole file. Which operation fits?

Domain: Tool Design & MCP Integration

- A. Use Edit with a verified unique anchor
- B. Use Bash for an authorized command with bounded execution
- C. Read the current file and write a checked replacement
- D. Use Read to inspect current file contents

### 80. A tool execution is unauthorized, but the response looks like a valid empty list. What contract repair is essential?

Domain: Tool Design & MCP Integration

- A. Expose a supported MCP resource catalog
- B. Represent a successful query with no matches explicitly
- C. Clarify tool purpose, inputs, outputs, and boundaries
- D. Return a structured tool error with category and retryability

### 81. A document specialist receives payment tools 'just in case' and begins using them during extraction. What should be removed?

Domain: Tool Design & MCP Integration

- A. Clarify tool purpose, inputs, outputs, and boundaries
- B. Give each specialist only task-relevant tools
- C. Separate genuinely different tasks into clearly bounded tools
- D. Expose a supported MCP resource catalog

### 82. A researcher needs to load registered report IDs, but its tool accepts arbitrary local file paths. What safer interface should be considered?

Domain: Tool Design & MCP Integration

- A. Define and validate a precise input schema
- B. Give each specialist only task-relevant tools
- C. Clarify tool purpose, inputs, outputs, and boundaries
- D. Expose a constrained domain-specific operation

### 83. A downstream parser expects arguments from exactly one named schema tool. What mode best matches that tool-selection requirement?

Domain: Tool Design & MCP Integration

- A. Use tool_choice with type any
- B. Check connected-server discovery and effective availability
- C. Force the required named tool for that turn
- D. Use tool_choice with type auto

### 84. An informational chat request should not be compelled to invoke an external service every time. Which mode allows discretion?

Domain: Tool Design & MCP Integration

- A. Use tool_choice with type auto
- B. Use tool_choice with type any
- C. Force the required named tool for that turn
- D. Give each specialist only task-relevant tools

### 85. A model was forced to call a refund tool. What still decides whether its proposed refund is actually permitted?

Domain: Tool Design & MCP Integration

- A. Clarify tool purpose, inputs, outputs, and boundaries
- B. Use tool_choice with type any
- C. Enforce prerequisites in trusted execution code
- D. Force the required named tool for that turn

### 86. An agent needs two similar lookup tools, but their differences are invisible in documentation. What should be attempted before removing a necessary tool?

Domain: Tool Design & MCP Integration

- A. Separate genuinely different tasks into clearly bounded tools
- B. Expose a supported MCP resource catalog
- C. Give each specialist only task-relevant tools
- D. Clarify tool purpose, inputs, outputs, and boundaries

### 87. A metadata tool must finish before enrichment can use its result. What must accompany correct tool selection?

Domain: Tool Design & MCP Integration

- A. Use tool_choice with type any
- B. Wait for validated prerequisite outputs
- C. Force the required named tool for that turn
- D. Use tool_choice with type auto

### 88. A general coordinator has broad access, but its narrow specialist should not inherit every available operation. What should be configured?

Domain: Tool Design & MCP Integration

- A. Give each specialist only task-relevant tools
- B. Check connected-server discovery and effective availability
- C. Clarify tool purpose, inputs, outputs, and boundaries
- D. Expose a supported MCP resource catalog

### 89. A source-checking tool can return yes/no evidence but cannot initiate arbitrary navigation. What design principle does this illustrate?

Domain: Tool Design & MCP Integration

- A. Give each specialist only task-relevant tools
- B. Clarify tool purpose, inputs, outputs, and boundaries
- C. Separate genuinely different tasks into clearly bounded tools
- D. Expose a constrained domain-specific operation

### 90. A forced tool call contains an unknown enum value. What must still validate the proposed arguments?

Domain: Tool Design & MCP Integration

- A. Use tool_choice with type any
- B. Force the required named tool for that turn
- C. Define and validate a precise input schema
- D. Use tool_choice with type auto

### 91. An agent needs a table of available source collections before deciding which query to run. What can expose that metadata?

Domain: Tool Design & MCP Integration

- A. Use project-scoped .mcp.json for shared server configuration
- B. Clarify tool purpose, inputs, outputs, and boundaries
- C. Expose a supported MCP resource catalog
- D. Check connected-server discovery and effective availability

### 92. An available community server is unmaintained and requests excessive permissions. What adoption principle should guide the decision?

Domain: Tool Design & MCP Integration

- A. Use project-scoped .mcp.json for shared server configuration
- B. Separate genuinely different tasks into clearly bounded tools
- C. Evaluate a maintained existing integration before writing a custom server
- D. Use user-scoped MCP configuration for personal servers

### 93. Approved team MCP setup should survive developer laptop replacement and be reviewed in pull requests. Which configuration scope fits?

Domain: Tool Design & MCP Integration

- A. Use user-scoped MCP configuration for personal servers
- B. Expose a supported MCP resource catalog
- C. Reference runtime environment variables instead of committing tokens
- D. Use project-scoped .mcp.json for shared server configuration

### 94. An engineer's experimental server should apply across personal projects without editing each team's repository. Which scope is relevant?

Domain: Tool Design & MCP Integration

- A. Use user-scoped MCP configuration for personal servers
- B. Expose a supported MCP resource catalog
- C. Check connected-server discovery and effective availability
- D. Use project-scoped .mcp.json for shared server configuration

### 95. A server starts successfully but a required capability is unavailable after an approval policy changes. What should be checked?

Domain: Tool Design & MCP Integration

- A. Give each specialist only task-relevant tools
- B. Check connected-server discovery and effective availability
- C. Clarify tool purpose, inputs, outputs, and boundaries
- D. Expose a supported MCP resource catalog

### 96. A developer knows an imported package name but not which files use it. What search should start the investigation?

Domain: Tool Design & MCP Integration

- A. Use Grep for content-pattern searches
- B. Read the current file and write a checked replacement
- C. Use Glob for filename or path-pattern discovery
- D. Use Read to inspect current file contents

### 97. A developer knows only the expected test filename pattern, not any test contents. What discovery tool fits?

Domain: Tool Design & MCP Integration

- A. Use Grep for content-pattern searches
- B. Use Glob for filename or path-pattern discovery
- C. Use Edit with a verified unique anchor
- D. Read the current file and write a checked replacement

### 98. A mutating tool times out after its server may have committed the change. What integration feature makes a retry safer where supported?

Domain: Tool Design & MCP Integration

- A. Correct invalid arguments before retrying
- B. Represent a successful query with no matches explicitly
- C. Use a durable idempotency key for the same logical action
- D. Retry a transient failure with bounded backoff

### 99. A server reports three retrieved records and then an access failure on another partition. How should the overall outcome be communicated?

Domain: Tool Design & MCP Integration

- A. Expose a supported MCP resource catalog
- B. Represent a successful query with no matches explicitly
- C. Clarify tool purpose, inputs, outputs, and boundaries
- D. Return a structured tool error with category and retryability

### 100. An agent must replace a full generated configuration after verifying current content and preserving user sections. Which operation may fit?

Domain: Tool Design & MCP Integration

- A. Use Bash for an authorized command with bounded execution
- B. Use Glob for filename or path-pattern discovery
- C. Use Edit with a verified unique anchor
- D. Read the current file and write a checked replacement

---

## Answer key and explanations

### Question 1 — D

Answer: Clarify tool purpose, inputs, outputs, and boundaries. Differentiate purpose, accepted inputs, outputs, and boundary cases in the contracts. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. Closest official exam-guide objective 2.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Differentiate purpose, accepted inputs, outputs, and boundary cases in the contracts.
- **B:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Differentiate purpose, accepted inputs, outputs, and boundary cases in the contracts.
- **C:** Incorrect for this question. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. In this case: Differentiate purpose, accepted inputs, outputs, and boundary cases in the contracts.
- **D:** Correct. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Differentiate purpose, accepted inputs, outputs, and boundary cases in the contracts.

### Question 2 — B

Answer: Define and validate a precise input schema. A precise schema plus validation makes the required argument shape explicit. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. Closest official exam-guide objective 2.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: A precise schema plus validation makes the required argument shape explicit.
- **B:** Correct. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. In this case: A precise schema plus validation makes the required argument shape explicit.
- **C:** Incorrect for this question. System-prompt keywords can misroute requests even when tool contracts are reasonable. Diagnose both instruction and interface effects. In this case: A precise schema plus validation makes the required argument shape explicit.
- **D:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: A precise schema plus validation makes the required argument shape explicit.

### Question 3 — B

Answer: Separate genuinely different tasks into clearly bounded tools. Genuinely distinct tasks can have explicit separate contracts rather than one ambiguous interface. A generic interface can be split when its unrelated responsibilities cause ambiguity. Do not multiply near-identical tools without a meaningful boundary. Closest official exam-guide objective 2.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Genuinely distinct tasks can have explicit separate contracts rather than one ambiguous interface.
- **B:** Correct. A generic interface can be split when its unrelated responsibilities cause ambiguity. Do not multiply near-identical tools without a meaningful boundary. In this case: Genuinely distinct tasks can have explicit separate contracts rather than one ambiguous interface.
- **C:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Genuinely distinct tasks can have explicit separate contracts rather than one ambiguous interface.
- **D:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Genuinely distinct tasks can have explicit separate contracts rather than one ambiguous interface.

### Question 4 — B

Answer: Clarify tool purpose, inputs, outputs, and boundaries. Make source boundaries explicit so the model can select the right operation. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. Closest official exam-guide objective 2.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Make source boundaries explicit so the model can select the right operation.
- **B:** Correct. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Make source boundaries explicit so the model can select the right operation.
- **C:** Incorrect for this question. A generic interface can be split when its unrelated responsibilities cause ambiguity. Do not multiply near-identical tools without a meaningful boundary. In this case: Make source boundaries explicit so the model can select the right operation.
- **D:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Make source boundaries explicit so the model can select the right operation.

### Question 5 — B

Answer: Inspect conflicting routing instructions as well as tool descriptions. Conflicting keyword-based routing instructions can override otherwise useful descriptions. System-prompt keywords can misroute requests even when tool contracts are reasonable. Diagnose both instruction and interface effects. Closest official exam-guide objective 2.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Conflicting keyword-based routing instructions can override otherwise useful descriptions.
- **B:** Correct. System-prompt keywords can misroute requests even when tool contracts are reasonable. Diagnose both instruction and interface effects. In this case: Conflicting keyword-based routing instructions can override otherwise useful descriptions.
- **C:** Incorrect for this question. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. In this case: Conflicting keyword-based routing instructions can override otherwise useful descriptions.
- **D:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Conflicting keyword-based routing instructions can override otherwise useful descriptions.

### Question 6 — C

Answer: Expose a constrained domain-specific operation. A constrained document loader can validate allowed sources before fetching content. A narrow operation can enforce permitted sources, destinations, or actions more reliably than a general arbitrary-command or unrestricted-fetch interface. Closest official exam-guide objective 2.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: A constrained document loader can validate allowed sources before fetching content.
- **B:** Incorrect for this question. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. In this case: A constrained document loader can validate allowed sources before fetching content.
- **C:** Correct. A narrow operation can enforce permitted sources, destinations, or actions more reliably than a general arbitrary-command or unrestricted-fetch interface. In this case: A constrained document loader can validate allowed sources before fetching content.
- **D:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: A constrained document loader can validate allowed sources before fetching content.

### Question 7 — D

Answer: Clarify tool purpose, inputs, outputs, and boundaries. The contract should identify side effects and distinguish lookup from mutation. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. Closest official exam-guide objective 2.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: The contract should identify side effects and distinguish lookup from mutation.
- **B:** Incorrect for this question. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. In this case: The contract should identify side effects and distinguish lookup from mutation.
- **C:** Incorrect for this question. Configured servers can expose tools together when connected, but server failure, approval, filtering, and permissions can affect what is actually usable. In this case: The contract should identify side effects and distinguish lookup from mutation.
- **D:** Correct. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: The contract should identify side effects and distinguish lookup from mutation.

### Question 8 — A

Answer: Define and validate a precise input schema. Specify units and accepted values explicitly and validate them in trusted code. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. Closest official exam-guide objective 2.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. In this case: Specify units and accepted values explicitly and validate them in trusted code.
- **B:** Incorrect for this question. System-prompt keywords can misroute requests even when tool contracts are reasonable. Diagnose both instruction and interface effects. In this case: Specify units and accepted values explicitly and validate them in trusted code.
- **C:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Specify units and accepted values explicitly and validate them in trusted code.
- **D:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Specify units and accepted values explicitly and validate them in trusted code.

### Question 9 — C

Answer: Clarify tool purpose, inputs, outputs, and boundaries. Describe distinctive capabilities, output structure, and when that search is preferable. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. Closest official exam-guide objective 2.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. A suitable standard integration may reduce work. Assess security, permissions, maintenance, and requirements before adoption; custom tools remain appropriate for unique workflows. In this case: Describe distinctive capabilities, output structure, and when that search is preferable.
- **B:** Incorrect for this question. A generic interface can be split when its unrelated responsibilities cause ambiguity. Do not multiply near-identical tools without a meaningful boundary. In this case: Describe distinctive capabilities, output structure, and when that search is preferable.
- **C:** Correct. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Describe distinctive capabilities, output structure, and when that search is preferable.
- **D:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Describe distinctive capabilities, output structure, and when that search is preferable.

### Question 10 — B

Answer: Expose a constrained domain-specific operation. Expose the narrow business operation rather than a general command executor. A narrow operation can enforce permitted sources, destinations, or actions more reliably than a general arbitrary-command or unrestricted-fetch interface. Closest official exam-guide objective 2.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Expose the narrow business operation rather than a general command executor.
- **B:** Correct. A narrow operation can enforce permitted sources, destinations, or actions more reliably than a general arbitrary-command or unrestricted-fetch interface. In this case: Expose the narrow business operation rather than a general command executor.
- **C:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Expose the narrow business operation rather than a general command executor.
- **D:** Incorrect for this question. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. In this case: Expose the narrow business operation rather than a general command executor.

### Question 11 — C

Answer: Define and validate a precise input schema. Require an explicit validated target instead of silently selecting a dangerous default. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. Closest official exam-guide objective 2.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Require an explicit validated target instead of silently selecting a dangerous default.
- **B:** Incorrect for this question. System-prompt keywords can misroute requests even when tool contracts are reasonable. Diagnose both instruction and interface effects. In this case: Require an explicit validated target instead of silently selecting a dangerous default.
- **C:** Correct. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. In this case: Require an explicit validated target instead of silently selecting a dangerous default.
- **D:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Require an explicit validated target instead of silently selecting a dangerous default.

### Question 12 — C

Answer: Clarify tool purpose, inputs, outputs, and boundaries. Explain pagination and completeness so absence from one page is not mistaken for absence everywhere. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. Closest official exam-guide objective 2.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. In this case: Explain pagination and completeness so absence from one page is not mistaken for absence everywhere.
- **B:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Explain pagination and completeness so absence from one page is not mistaken for absence everywhere.
- **C:** Correct. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Explain pagination and completeness so absence from one page is not mistaken for absence everywhere.
- **D:** Incorrect for this question. A generic interface can be split when its unrelated responsibilities cause ambiguity. Do not multiply near-identical tools without a meaningful boundary. In this case: Explain pagination and completeness so absence from one page is not mistaken for absence everywhere.

### Question 13 — B

Answer: Inspect conflicting routing instructions as well as tool descriptions. Inspect instruction-level associations alongside the current tool interface. System-prompt keywords can misroute requests even when tool contracts are reasonable. Diagnose both instruction and interface effects. Closest official exam-guide objective 2.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Configured servers can expose tools together when connected, but server failure, approval, filtering, and permissions can affect what is actually usable. In this case: Inspect instruction-level associations alongside the current tool interface.
- **B:** Correct. System-prompt keywords can misroute requests even when tool contracts are reasonable. Diagnose both instruction and interface effects. In this case: Inspect instruction-level associations alongside the current tool interface.
- **C:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Inspect instruction-level associations alongside the current tool interface.
- **D:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Inspect instruction-level associations alongside the current tool interface.

### Question 14 — A

Answer: Separate genuinely different tasks into clearly bounded tools. Separate materially different responsibilities and effect types into bounded operations. A generic interface can be split when its unrelated responsibilities cause ambiguity. Do not multiply near-identical tools without a meaningful boundary. Closest official exam-guide objective 2.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. A generic interface can be split when its unrelated responsibilities cause ambiguity. Do not multiply near-identical tools without a meaningful boundary. In this case: Separate materially different responsibilities and effect types into bounded operations.
- **B:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Separate materially different responsibilities and effect types into bounded operations.
- **C:** Incorrect for this question. Configured servers can expose tools together when connected, but server failure, approval, filtering, and permissions can affect what is actually usable. In this case: Separate materially different responsibilities and effect types into bounded operations.
- **D:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Separate materially different responsibilities and effect types into bounded operations.

### Question 15 — A

Answer: Define and validate a precise input schema. An enum in the input schema represents allowed categories for validation. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. Closest official exam-guide objective 2.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. In this case: An enum in the input schema represents allowed categories for validation.
- **B:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: An enum in the input schema represents allowed categories for validation.
- **C:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: An enum in the input schema represents allowed categories for validation.
- **D:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: An enum in the input schema represents allowed categories for validation.

### Question 16 — D

Answer: Clarify tool purpose, inputs, outputs, and boundaries. State temporal coverage and exclusions so the model does not infer unsupported historical capability. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. Closest official exam-guide objective 2.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: State temporal coverage and exclusions so the model does not infer unsupported historical capability.
- **B:** Incorrect for this question. System-prompt keywords can misroute requests even when tool contracts are reasonable. Diagnose both instruction and interface effects. In this case: State temporal coverage and exclusions so the model does not infer unsupported historical capability.
- **C:** Incorrect for this question. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. In this case: State temporal coverage and exclusions so the model does not infer unsupported historical capability.
- **D:** Correct. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: State temporal coverage and exclusions so the model does not infer unsupported historical capability.

### Question 17 — B

Answer: Expose a constrained domain-specific operation. Enforce destination restrictions inside a constrained operation rather than rely on wording alone. A narrow operation can enforce permitted sources, destinations, or actions more reliably than a general arbitrary-command or unrestricted-fetch interface. Closest official exam-guide objective 2.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Enforce destination restrictions inside a constrained operation rather than rely on wording alone.
- **B:** Correct. A narrow operation can enforce permitted sources, destinations, or actions more reliably than a general arbitrary-command or unrestricted-fetch interface. In this case: Enforce destination restrictions inside a constrained operation rather than rely on wording alone.
- **C:** Incorrect for this question. A generic interface can be split when its unrelated responsibilities cause ambiguity. Do not multiply near-identical tools without a meaningful boundary. In this case: Enforce destination restrictions inside a constrained operation rather than rely on wording alone.
- **D:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Enforce destination restrictions inside a constrained operation rather than rely on wording alone.

### Question 18 — C

Answer: Schema validity does not grant authorization. Argument shape validation does not replace requester authorization or business policy checks. A well-formed identifier or tool argument can still target data or actions the requester may not access. Trusted authorization must check the current requester and target. Closest official exam-guide objective 2.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Argument shape validation does not replace requester authorization or business policy checks.
- **B:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Argument shape validation does not replace requester authorization or business policy checks.
- **C:** Correct. A well-formed identifier or tool argument can still target data or actions the requester may not access. Trusted authorization must check the current requester and target. In this case: Argument shape validation does not replace requester authorization or business policy checks.
- **D:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Argument shape validation does not replace requester authorization or business policy checks.

### Question 19 — D

Answer: Clarify tool purpose, inputs, outputs, and boundaries. The contract should distinguish advisory output from an externally confirmed action. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. Closest official exam-guide objective 2.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Configured servers can expose tools together when connected, but server failure, approval, filtering, and permissions can affect what is actually usable. In this case: The contract should distinguish advisory output from an externally confirmed action.
- **B:** Incorrect for this question. A suitable standard integration may reduce work. Assess security, permissions, maintenance, and requirements before adoption; custom tools remain appropriate for unique workflows. In this case: The contract should distinguish advisory output from an externally confirmed action.
- **C:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: The contract should distinguish advisory output from an externally confirmed action.
- **D:** Correct. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: The contract should distinguish advisory output from an externally confirmed action.

### Question 20 — B

Answer: Inspect conflicting routing instructions as well as tool descriptions. Remove unintended keyword associations rather than only adding more tools. System-prompt keywords can misroute requests even when tool contracts are reasonable. Diagnose both instruction and interface effects. Closest official exam-guide objective 2.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Remove unintended keyword associations rather than only adding more tools.
- **B:** Correct. System-prompt keywords can misroute requests even when tool contracts are reasonable. Diagnose both instruction and interface effects. In this case: Remove unintended keyword associations rather than only adding more tools.
- **C:** Incorrect for this question. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. In this case: Remove unintended keyword associations rather than only adding more tools.
- **D:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Remove unintended keyword associations rather than only adding more tools.

### Question 21 — D

Answer: Return a structured tool error with category and retryability. A structured error distinguishes failure from a successful query that found nothing. An error contract should identify failure class, recoverability, and useful context. MCP isError marks an execution failure; it should not disguise a valid empty result. Closest official exam-guide objective 2.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: A structured error distinguishes failure from a successful query that found nothing.
- **B:** Incorrect for this question. Client-tool observations must be returned with the correct tool-use identifiers in a valid message sequence so Claude can use actual results. In this case: A structured error distinguishes failure from a successful query that found nothing.
- **C:** Incorrect for this question. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. In this case: A structured error distinguishes failure from a successful query that found nothing.
- **D:** Correct. An error contract should identify failure class, recoverability, and useful context. MCP isError marks an execution failure; it should not disguise a valid empty result. In this case: A structured error distinguishes failure from a successful query that found nothing.

### Question 22 — B

Answer: Retry a transient failure with bounded backoff. Temporary availability failures may justify bounded delayed retry under service guidance. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. Closest official exam-guide objective 2.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. A validation failure points to an input defect. Repeating identical invalid arguments is not recovery. In this case: Temporary availability failures may justify bounded delayed retry under service guidance.
- **B:** Correct. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: Temporary availability failures may justify bounded delayed retry under service guidance.
- **C:** Incorrect for this question. Permission denial does not justify trying alternate credentials or leaking restricted content. Recover only through explicitly authorized mechanisms. In this case: Temporary availability failures may justify bounded delayed retry under service guidance.
- **D:** Incorrect for this question. A policy rejection is not normally fixed by repeating the same operation. Communicate the reason and legitimate next steps without evasion. In this case: Temporary availability failures may justify bounded delayed retry under service guidance.

### Question 23 — C

Answer: Correct invalid arguments before retrying. Correct the invalid argument rather than repeat the identical malformed request. A validation failure points to an input defect. Repeating identical invalid arguments is not recovery. Closest official exam-guide objective 2.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Permission denial does not justify trying alternate credentials or leaking restricted content. Recover only through explicitly authorized mechanisms. In this case: Correct the invalid argument rather than repeat the identical malformed request.
- **B:** Incorrect for this question. A policy rejection is not normally fixed by repeating the same operation. Communicate the reason and legitimate next steps without evasion. In this case: Correct the invalid argument rather than repeat the identical malformed request.
- **C:** Correct. A validation failure points to an input defect. Repeating identical invalid arguments is not recovery. In this case: Correct the invalid argument rather than repeat the identical malformed request.
- **D:** Incorrect for this question. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: Correct the invalid argument rather than repeat the identical malformed request.

### Question 24 — C

Answer: Stop the unauthorized operation and use an approved access path. Authorization denial requires an approved access route, not blind retries or credential evasion. Permission denial does not justify trying alternate credentials or leaking restricted content. Recover only through explicitly authorized mechanisms. Closest official exam-guide objective 2.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. In this case: Authorization denial requires an approved access route, not blind retries or credential evasion.
- **B:** Incorrect for this question. A validation failure points to an input defect. Repeating identical invalid arguments is not recovery. In this case: Authorization denial requires an approved access route, not blind retries or credential evasion.
- **C:** Correct. Permission denial does not justify trying alternate credentials or leaking restricted content. Recover only through explicitly authorized mechanisms. In this case: Authorization denial requires an approved access route, not blind retries or credential evasion.
- **D:** Incorrect for this question. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: Authorization denial requires an approved access route, not blind retries or credential evasion.

### Question 25 — A

Answer: Explain the non-retryable business-rule outcome. A business-policy rejection should be explained and routed through legitimate next steps. A policy rejection is not normally fixed by repeating the same operation. Communicate the reason and legitimate next steps without evasion. Closest official exam-guide objective 2.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. A policy rejection is not normally fixed by repeating the same operation. Communicate the reason and legitimate next steps without evasion. In this case: A business-policy rejection should be explained and routed through legitimate next steps.
- **B:** Incorrect for this question. Permission denial does not justify trying alternate credentials or leaking restricted content. Recover only through explicitly authorized mechanisms. In this case: A business-policy rejection should be explained and routed through legitimate next steps.
- **C:** Incorrect for this question. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: A business-policy rejection should be explained and routed through legitimate next steps.
- **D:** Incorrect for this question. A validation failure points to an input defect. Repeating identical invalid arguments is not recovery. In this case: A business-policy rejection should be explained and routed through legitimate next steps.

### Question 26 — D

Answer: Represent a successful query with no matches explicitly. No matches is a real successful query outcome, not a service failure. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. Closest official exam-guide objective 2.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: No matches is a real successful query outcome, not a service failure.
- **B:** Incorrect for this question. An error contract should identify failure class, recoverability, and useful context. MCP isError marks an execution failure; it should not disguise a valid empty result. In this case: No matches is a real successful query outcome, not a service failure.
- **C:** Incorrect for this question. Permission denial does not justify trying alternate credentials or leaking restricted content. Recover only through explicitly authorized mechanisms. In this case: No matches is a real successful query outcome, not a service failure.
- **D:** Correct. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. In this case: No matches is a real successful query outcome, not a service failure.

### Question 27 — A

Answer: Return a structured tool error with category and retryability. Provide category, retryability, and useful failure context instead of one undifferentiated message. An error contract should identify failure class, recoverability, and useful context. MCP isError marks an execution failure; it should not disguise a valid empty result. Closest official exam-guide objective 2.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. An error contract should identify failure class, recoverability, and useful context. MCP isError marks an execution failure; it should not disguise a valid empty result. In this case: Provide category, retryability, and useful failure context instead of one undifferentiated message.
- **B:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Provide category, retryability, and useful failure context instead of one undifferentiated message.
- **C:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Provide category, retryability, and useful failure context instead of one undifferentiated message.
- **D:** Incorrect for this question. Configured servers can expose tools together when connected, but server failure, approval, filtering, and permissions can affect what is actually usable. In this case: Provide category, retryability, and useful failure context instead of one undifferentiated message.

### Question 28 — D

Answer: Recover transiently within the worker, then report unresolved failure. Use bounded local recovery, then propagate unresolved failure with context. Bounded local recovery reduces coordinator noise. Exhausted recovery should preserve attempts, partial results, and alternatives rather than silently disappear. Closest official exam-guide objective 2.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: Use bounded local recovery, then propagate unresolved failure with context.
- **B:** Incorrect for this question. The coordinator needs failure type, attempted operation, useful outputs, and alternatives. A failure must not be disguised as a successful empty search. In this case: Use bounded local recovery, then propagate unresolved failure with context.
- **C:** Incorrect for this question. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. In this case: Use bounded local recovery, then propagate unresolved failure with context.
- **D:** Correct. Bounded local recovery reduces coordinator noise. Exhausted recovery should preserve attempts, partial results, and alternatives rather than silently disappear. In this case: Use bounded local recovery, then propagate unresolved failure with context.

### Question 29 — A

Answer: Stop the unauthorized operation and use an approved access path. An access denial is distinct from evidence that no record exists. Permission denial does not justify trying alternate credentials or leaking restricted content. Recover only through explicitly authorized mechanisms. Closest official exam-guide objective 2.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Permission denial does not justify trying alternate credentials or leaking restricted content. Recover only through explicitly authorized mechanisms. In this case: An access denial is distinct from evidence that no record exists.
- **B:** Incorrect for this question. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: An access denial is distinct from evidence that no record exists.
- **C:** Incorrect for this question. A validation failure points to an input defect. Repeating identical invalid arguments is not recovery. In this case: An access denial is distinct from evidence that no record exists.
- **D:** Incorrect for this question. A policy rejection is not normally fixed by repeating the same operation. Communicate the reason and legitimate next steps without evasion. In this case: An access denial is distinct from evidence that no record exists.

### Question 30 — A

Answer: Return a structured tool error with category and retryability. Use the appropriate isError signal with meaningful structured failure details. An error contract should identify failure class, recoverability, and useful context. MCP isError marks an execution failure; it should not disguise a valid empty result. Closest official exam-guide objective 2.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. An error contract should identify failure class, recoverability, and useful context. MCP isError marks an execution failure; it should not disguise a valid empty result. In this case: Use the appropriate isError signal with meaningful structured failure details.
- **B:** Incorrect for this question. Client-tool observations must be returned with the correct tool-use identifiers in a valid message sequence so Claude can use actual results. In this case: Use the appropriate isError signal with meaningful structured failure details.
- **C:** Incorrect for this question. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. In this case: Use the appropriate isError signal with meaningful structured failure details.
- **D:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Use the appropriate isError signal with meaningful structured failure details.

### Question 31 — D

Answer: Correct invalid arguments before retrying. Repair the input using the documented allowed values before another attempt. A validation failure points to an input defect. Repeating identical invalid arguments is not recovery. Closest official exam-guide objective 2.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: Repair the input using the documented allowed values before another attempt.
- **B:** Incorrect for this question. Permission denial does not justify trying alternate credentials or leaking restricted content. Recover only through explicitly authorized mechanisms. In this case: Repair the input using the documented allowed values before another attempt.
- **C:** Incorrect for this question. A policy rejection is not normally fixed by repeating the same operation. Communicate the reason and legitimate next steps without evasion. In this case: Repair the input using the documented allowed values before another attempt.
- **D:** Correct. A validation failure points to an input defect. Repeating identical invalid arguments is not recovery. In this case: Repair the input using the documented allowed values before another attempt.

### Question 32 — C

Answer: Retry a transient failure with bounded backoff. A bounded delayed retry can follow the provider's guidance instead of immediate repetition. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. Closest official exam-guide objective 2.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. A policy rejection is not normally fixed by repeating the same operation. Communicate the reason and legitimate next steps without evasion. In this case: A bounded delayed retry can follow the provider's guidance instead of immediate repetition.
- **B:** Incorrect for this question. A validation failure points to an input defect. Repeating identical invalid arguments is not recovery. In this case: A bounded delayed retry can follow the provider's guidance instead of immediate repetition.
- **C:** Correct. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: A bounded delayed retry can follow the provider's guidance instead of immediate repetition.
- **D:** Incorrect for this question. Permission denial does not justify trying alternate credentials or leaking restricted content. Recover only through explicitly authorized mechanisms. In this case: A bounded delayed retry can follow the provider's guidance instead of immediate repetition.

### Question 33 — A

Answer: Explain the non-retryable business-rule outcome. The policy restriction is a business result, not a temporary availability problem. A policy rejection is not normally fixed by repeating the same operation. Communicate the reason and legitimate next steps without evasion. Closest official exam-guide objective 2.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. A policy rejection is not normally fixed by repeating the same operation. Communicate the reason and legitimate next steps without evasion. In this case: The policy restriction is a business result, not a temporary availability problem.
- **B:** Incorrect for this question. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: The policy restriction is a business result, not a temporary availability problem.
- **C:** Incorrect for this question. A validation failure points to an input defect. Repeating identical invalid arguments is not recovery. In this case: The policy restriction is a business result, not a temporary availability problem.
- **D:** Incorrect for this question. Permission denial does not justify trying alternate credentials or leaking restricted content. Recover only through explicitly authorized mechanisms. In this case: The policy restriction is a business result, not a temporary availability problem.

### Question 34 — B

Answer: Return a structured tool error with category and retryability. Preserve failure category, partial-result status, attempts, and possible alternatives. An error contract should identify failure class, recoverability, and useful context. MCP isError marks an execution failure; it should not disguise a valid empty result. Closest official exam-guide objective 2.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. In this case: Preserve failure category, partial-result status, attempts, and possible alternatives.
- **B:** Correct. An error contract should identify failure class, recoverability, and useful context. MCP isError marks an execution failure; it should not disguise a valid empty result. In this case: Preserve failure category, partial-result status, attempts, and possible alternatives.
- **C:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Preserve failure category, partial-result status, attempts, and possible alternatives.
- **D:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Preserve failure category, partial-result status, attempts, and possible alternatives.

### Question 35 — C

Answer: Recover transiently within the worker, then report unresolved failure. Report unresolved failure and partial findings rather than silently return success. Bounded local recovery reduces coordinator noise. Exhausted recovery should preserve attempts, partial results, and alternatives rather than silently disappear. Closest official exam-guide objective 2.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Permission denial does not justify trying alternate credentials or leaking restricted content. Recover only through explicitly authorized mechanisms. In this case: Report unresolved failure and partial findings rather than silently return success.
- **B:** Incorrect for this question. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. In this case: Report unresolved failure and partial findings rather than silently return success.
- **C:** Correct. Bounded local recovery reduces coordinator noise. Exhausted recovery should preserve attempts, partial results, and alternatives rather than silently disappear. In this case: Report unresolved failure and partial findings rather than silently return success.
- **D:** Incorrect for this question. A policy rejection is not normally fixed by repeating the same operation. Communicate the reason and legitimate next steps without evasion. In this case: Report unresolved failure and partial findings rather than silently return success.

### Question 36 — A

Answer: Represent a successful query with no matches explicitly. The specific query found no matching records; broader absence still depends on query coverage. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. Closest official exam-guide objective 2.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. In this case: The specific query found no matching records; broader absence still depends on query coverage.
- **B:** Incorrect for this question. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: The specific query found no matching records; broader absence still depends on query coverage.
- **C:** Incorrect for this question. Permission denial does not justify trying alternate credentials or leaking restricted content. Recover only through explicitly authorized mechanisms. In this case: The specific query found no matching records; broader absence still depends on query coverage.
- **D:** Incorrect for this question. An error contract should identify failure class, recoverability, and useful context. MCP isError marks an execution failure; it should not disguise a valid empty result. In this case: The specific query found no matching records; broader absence still depends on query coverage.

### Question 37 — A

Answer: Stop the unauthorized operation and use an approved access path. Permission failure never authorizes credential substitution or access evasion. Permission denial does not justify trying alternate credentials or leaking restricted content. Recover only through explicitly authorized mechanisms. Closest official exam-guide objective 2.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Permission denial does not justify trying alternate credentials or leaking restricted content. Recover only through explicitly authorized mechanisms. In this case: Permission failure never authorizes credential substitution or access evasion.
- **B:** Incorrect for this question. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. In this case: Permission failure never authorizes credential substitution or access evasion.
- **C:** Incorrect for this question. A validation failure points to an input defect. Repeating identical invalid arguments is not recovery. In this case: Permission failure never authorizes credential substitution or access evasion.
- **D:** Incorrect for this question. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: Permission failure never authorizes credential substitution or access evasion.

### Question 38 — A

Answer: Return a structured tool error with category and retryability. Structured failure context enables targeted recovery and avoids repeating the same unsuccessful attempt. An error contract should identify failure class, recoverability, and useful context. MCP isError marks an execution failure; it should not disguise a valid empty result. Closest official exam-guide objective 2.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. An error contract should identify failure class, recoverability, and useful context. MCP isError marks an execution failure; it should not disguise a valid empty result. In this case: Structured failure context enables targeted recovery and avoids repeating the same unsuccessful attempt.
- **B:** Incorrect for this question. Configured servers can expose tools together when connected, but server failure, approval, filtering, and permissions can affect what is actually usable. In this case: Structured failure context enables targeted recovery and avoids repeating the same unsuccessful attempt.
- **C:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Structured failure context enables targeted recovery and avoids repeating the same unsuccessful attempt.
- **D:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Structured failure context enables targeted recovery and avoids repeating the same unsuccessful attempt.

### Question 39 — D

Answer: Explain the non-retryable business-rule outcome. Repeating the same valid request will not change the policy rejection. A policy rejection is not normally fixed by repeating the same operation. Communicate the reason and legitimate next steps without evasion. Closest official exam-guide objective 2.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. A validation failure points to an input defect. Repeating identical invalid arguments is not recovery. In this case: Repeating the same valid request will not change the policy rejection.
- **B:** Incorrect for this question. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. In this case: Repeating the same valid request will not change the policy rejection.
- **C:** Incorrect for this question. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: Repeating the same valid request will not change the policy rejection.
- **D:** Correct. A policy rejection is not normally fixed by repeating the same operation. Communicate the reason and legitimate next steps without evasion. In this case: Repeating the same valid request will not change the policy rejection.

### Question 40 — C

Answer: Recover transiently within the worker, then report unresolved failure. Local bounded recovery can reduce orchestration noise while preserving unresolved failure details. Bounded local recovery reduces coordinator noise. Exhausted recovery should preserve attempts, partial results, and alternatives rather than silently disappear. Closest official exam-guide objective 2.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Permission denial does not justify trying alternate credentials or leaking restricted content. Recover only through explicitly authorized mechanisms. In this case: Local bounded recovery can reduce orchestration noise while preserving unresolved failure details.
- **B:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Local bounded recovery can reduce orchestration noise while preserving unresolved failure details.
- **C:** Correct. Bounded local recovery reduces coordinator noise. Exhausted recovery should preserve attempts, partial results, and alternatives rather than silently disappear. In this case: Local bounded recovery can reduce orchestration noise while preserving unresolved failure details.
- **D:** Incorrect for this question. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. In this case: Local bounded recovery can reduce orchestration noise while preserving unresolved failure details.

### Question 41 — C

Answer: Give each specialist only task-relevant tools. Keep tools aligned to the specialist's actual role to reduce misuse and unnecessary authority. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. Closest official exam-guide objective 2.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Keep tools aligned to the specialist's actual role to reduce misuse and unnecessary authority.
- **B:** Incorrect for this question. A generic interface can be split when its unrelated responsibilities cause ambiguity. Do not multiply near-identical tools without a meaningful boundary. In this case: Keep tools aligned to the specialist's actual role to reduce misuse and unnecessary authority.
- **C:** Correct. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Keep tools aligned to the specialist's actual role to reduce misuse and unnecessary authority.
- **D:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Keep tools aligned to the specialist's actual role to reduce misuse and unnecessary authority.

### Question 42 — C

Answer: Use tool_choice with type auto. Auto allows conversational output when no tool call is needed. Auto permits either a tool call or an ordinary response. It cannot guarantee extraction through a tool on every request. Closest official exam-guide objective 2.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Auto allows conversational output when no tool call is needed.
- **B:** Incorrect for this question. Where supported, any requires a tool selection but leaves the specific tool to the model. It does not guarantee that a particular named tool runs. In this case: Auto allows conversational output when no tool call is needed.
- **C:** Correct. Auto permits either a tool call or an ordinary response. It cannot guarantee extraction through a tool on every request. In this case: Auto allows conversational output when no tool call is needed.
- **D:** Incorrect for this question. Where supported, named tool selection requires the specified tool. Additional workflow ordering and authorization still belong in application code. In this case: Auto allows conversational output when no tool call is needed.

### Question 43 — B

Answer: Use tool_choice with type any. Any requires tool use without choosing one named tool in advance. Where supported, any requires a tool selection but leaves the specific tool to the model. It does not guarantee that a particular named tool runs. Closest official exam-guide objective 2.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Any requires tool use without choosing one named tool in advance.
- **B:** Correct. Where supported, any requires a tool selection but leaves the specific tool to the model. It does not guarantee that a particular named tool runs. In this case: Any requires tool use without choosing one named tool in advance.
- **C:** Incorrect for this question. Auto permits either a tool call or an ordinary response. It cannot guarantee extraction through a tool on every request. In this case: Any requires tool use without choosing one named tool in advance.
- **D:** Incorrect for this question. Where supported, named tool selection requires the specified tool. Additional workflow ordering and authorization still belong in application code. In this case: Any requires tool use without choosing one named tool in advance.

### Question 44 — B

Answer: Force the required named tool for that turn. Named forced selection targets the required operation where supported. Where supported, named tool selection requires the specified tool. Additional workflow ordering and authorization still belong in application code. Closest official exam-guide objective 2.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Where supported, any requires a tool selection but leaves the specific tool to the model. It does not guarantee that a particular named tool runs. In this case: Named forced selection targets the required operation where supported.
- **B:** Correct. Where supported, named tool selection requires the specified tool. Additional workflow ordering and authorization still belong in application code. In this case: Named forced selection targets the required operation where supported.
- **C:** Incorrect for this question. Auto permits either a tool call or an ordinary response. It cannot guarantee extraction through a tool on every request. In this case: Named forced selection targets the required operation where supported.
- **D:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Named forced selection targets the required operation where supported.

### Question 45 — D

Answer: Give each specialist only task-relevant tools. Scope tools to required responsibilities instead of exposing the full organization catalog indiscriminately. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. Closest official exam-guide objective 2.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Scope tools to required responsibilities instead of exposing the full organization catalog indiscriminately.
- **B:** Incorrect for this question. A generic interface can be split when its unrelated responsibilities cause ambiguity. Do not multiply near-identical tools without a meaningful boundary. In this case: Scope tools to required responsibilities instead of exposing the full organization catalog indiscriminately.
- **C:** Incorrect for this question. Configured servers can expose tools together when connected, but server failure, approval, filtering, and permissions can affect what is actually usable. In this case: Scope tools to required responsibilities instead of exposing the full organization catalog indiscriminately.
- **D:** Correct. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Scope tools to required responsibilities instead of exposing the full organization catalog indiscriminately.

### Question 46 — D

Answer: Expose a constrained domain-specific operation. Expose a constrained verification operation and route broader research through coordination. A narrow operation can enforce permitted sources, destinations, or actions more reliably than a general arbitrary-command or unrestricted-fetch interface. Closest official exam-guide objective 2.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Expose a constrained verification operation and route broader research through coordination.
- **B:** Incorrect for this question. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. In this case: Expose a constrained verification operation and route broader research through coordination.
- **C:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Expose a constrained verification operation and route broader research through coordination.
- **D:** Correct. A narrow operation can enforce permitted sources, destinations, or actions more reliably than a general arbitrary-command or unrestricted-fetch interface. In this case: Expose a constrained verification operation and route broader research through coordination.

### Question 47 — A

Answer: Force the required named tool for that turn. Force the required named tool rather than leave selection among tools open. Where supported, named tool selection requires the specified tool. Additional workflow ordering and authorization still belong in application code. Closest official exam-guide objective 2.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Where supported, named tool selection requires the specified tool. Additional workflow ordering and authorization still belong in application code. In this case: Force the required named tool rather than leave selection among tools open.
- **B:** Incorrect for this question. Where supported, any requires a tool selection but leaves the specific tool to the model. It does not guarantee that a particular named tool runs. In this case: Force the required named tool rather than leave selection among tools open.
- **C:** Incorrect for this question. Auto permits either a tool call or an ordinary response. It cannot guarantee extraction through a tool on every request. In this case: Force the required named tool rather than leave selection among tools open.
- **D:** Incorrect for this question. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: Force the required named tool rather than leave selection among tools open.

### Question 48 — B

Answer: Use tool_choice with type auto. Auto can legitimately return ordinary text, so it does not enforce a tool call. Auto permits either a tool call or an ordinary response. It cannot guarantee extraction through a tool on every request. Closest official exam-guide objective 2.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Auto can legitimately return ordinary text, so it does not enforce a tool call.
- **B:** Correct. Auto permits either a tool call or an ordinary response. It cannot guarantee extraction through a tool on every request. In this case: Auto can legitimately return ordinary text, so it does not enforce a tool call.
- **C:** Incorrect for this question. Where supported, any requires a tool selection but leaves the specific tool to the model. It does not guarantee that a particular named tool runs. In this case: Auto can legitimately return ordinary text, so it does not enforce a tool call.
- **D:** Incorrect for this question. Where supported, named tool selection requires the specified tool. Additional workflow ordering and authorization still belong in application code. In this case: Auto can legitimately return ordinary text, so it does not enforce a tool call.

### Question 49 — A

Answer: Give each specialist only task-relevant tools. Do not expose the irrelevant tool to that specialist's effective tool set. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. Closest official exam-guide objective 2.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Do not expose the irrelevant tool to that specialist's effective tool set.
- **B:** Incorrect for this question. A suitable standard integration may reduce work. Assess security, permissions, maintenance, and requirements before adoption; custom tools remain appropriate for unique workflows. In this case: Do not expose the irrelevant tool to that specialist's effective tool set.
- **C:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Do not expose the irrelevant tool to that specialist's effective tool set.
- **D:** Incorrect for this question. Configured servers can expose tools together when connected, but server failure, approval, filtering, and permissions can affect what is actually usable. In this case: Do not expose the irrelevant tool to that specialist's effective tool set.

### Question 50 — C

Answer: Force the required named tool for that turn. Force the initial named operation, then enforce later dependencies in follow-up orchestration. Where supported, named tool selection requires the specified tool. Additional workflow ordering and authorization still belong in application code. Closest official exam-guide objective 2.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Force the initial named operation, then enforce later dependencies in follow-up orchestration.
- **B:** Incorrect for this question. Auto permits either a tool call or an ordinary response. It cannot guarantee extraction through a tool on every request. In this case: Force the initial named operation, then enforce later dependencies in follow-up orchestration.
- **C:** Correct. Where supported, named tool selection requires the specified tool. Additional workflow ordering and authorization still belong in application code. In this case: Force the initial named operation, then enforce later dependencies in follow-up orchestration.
- **D:** Incorrect for this question. Where supported, any requires a tool selection but leaves the specific tool to the model. It does not guarantee that a particular named tool runs. In this case: Force the initial named operation, then enforce later dependencies in follow-up orchestration.

### Question 51 — D

Answer: Use project-scoped .mcp.json for shared server configuration. Project-scoped configuration is versioned with the project rather than confined to one developer. Versioned project configuration can distribute team tooling. Keep real credentials outside Git and check approvals and environment requirements. Closest official exam-guide objective 2.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. The guide describes user-scoped configuration in ~/.claude.json for personal tooling. Personal configuration is not automatically shared through the repository. In this case: Project-scoped configuration is versioned with the project rather than confined to one developer.
- **B:** Incorrect for this question. Configured servers can expose tools together when connected, but server failure, approval, filtering, and permissions can affect what is actually usable. In this case: Project-scoped configuration is versioned with the project rather than confined to one developer.
- **C:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Project-scoped configuration is versioned with the project rather than confined to one developer.
- **D:** Correct. Versioned project configuration can distribute team tooling. Keep real credentials outside Git and check approvals and environment requirements. In this case: Project-scoped configuration is versioned with the project rather than confined to one developer.

### Question 52 — B

Answer: Use user-scoped MCP configuration for personal servers. Personal server configuration should remain user-scoped instead of modifying the shared project file. The guide describes user-scoped configuration in ~/.claude.json for personal tooling. Personal configuration is not automatically shared through the repository. Closest official exam-guide objective 2.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. A suitable standard integration may reduce work. Assess security, permissions, maintenance, and requirements before adoption; custom tools remain appropriate for unique workflows. In this case: Personal server configuration should remain user-scoped instead of modifying the shared project file.
- **B:** Correct. The guide describes user-scoped configuration in ~/.claude.json for personal tooling. Personal configuration is not automatically shared through the repository. In this case: Personal server configuration should remain user-scoped instead of modifying the shared project file.
- **C:** Incorrect for this question. Versioned project configuration can distribute team tooling. Keep real credentials outside Git and check approvals and environment requirements. In this case: Personal server configuration should remain user-scoped instead of modifying the shared project file.
- **D:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Personal server configuration should remain user-scoped instead of modifying the shared project file.

### Question 53 — B

Answer: Reference runtime environment variables instead of committing tokens. Reference runtime-supplied credentials and keep secret values out of source control. Environment expansion can keep literal secrets out of project files. Supply credentials through an approved secret path and protect logs as well. Closest official exam-guide objective 2.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Reference runtime-supplied credentials and keep secret values out of source control.
- **B:** Correct. Environment expansion can keep literal secrets out of project files. Supply credentials through an approved secret path and protect logs as well. In this case: Reference runtime-supplied credentials and keep secret values out of source control.
- **C:** Incorrect for this question. Versioned project configuration can distribute team tooling. Keep real credentials outside Git and check approvals and environment requirements. In this case: Reference runtime-supplied credentials and keep secret values out of source control.
- **D:** Incorrect for this question. The guide describes user-scoped configuration in ~/.claude.json for personal tooling. Personal configuration is not automatically shared through the repository. In this case: Reference runtime-supplied credentials and keep secret values out of source control.

### Question 54 — C

Answer: Expose a supported MCP resource catalog. A resource catalog can provide browsable metadata without repeated action-like exploration. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. Closest official exam-guide objective 2.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Configured servers can expose tools together when connected, but server failure, approval, filtering, and permissions can affect what is actually usable. In this case: A resource catalog can provide browsable metadata without repeated action-like exploration.
- **B:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: A resource catalog can provide browsable metadata without repeated action-like exploration.
- **C:** Correct. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: A resource catalog can provide browsable metadata without repeated action-like exploration.
- **D:** Incorrect for this question. A generic interface can be split when its unrelated responsibilities cause ambiguity. Do not multiply near-identical tools without a meaningful boundary. In this case: A resource catalog can provide browsable metadata without repeated action-like exploration.

### Question 55 — C

Answer: Check connected-server discovery and effective availability. Check connection, discovery, approvals, effective filters, and permissions rather than assume configuration implies availability. Configured servers can expose tools together when connected, but server failure, approval, filtering, and permissions can affect what is actually usable. Closest official exam-guide objective 2.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Check connection, discovery, approvals, effective filters, and permissions rather than assume configuration implies availability.
- **B:** Incorrect for this question. Versioned project configuration can distribute team tooling. Keep real credentials outside Git and check approvals and environment requirements. In this case: Check connection, discovery, approvals, effective filters, and permissions rather than assume configuration implies availability.
- **C:** Correct. Configured servers can expose tools together when connected, but server failure, approval, filtering, and permissions can affect what is actually usable. In this case: Check connection, discovery, approvals, effective filters, and permissions rather than assume configuration implies availability.
- **D:** Incorrect for this question. The guide describes user-scoped configuration in ~/.claude.json for personal tooling. Personal configuration is not automatically shared through the repository. In this case: Check connection, discovery, approvals, effective filters, and permissions rather than assume configuration implies availability.

### Question 56 — D

Answer: Evaluate a maintained existing integration before writing a custom server. Evaluate the existing integration against requirements, security, and maintenance needs. A suitable standard integration may reduce work. Assess security, permissions, maintenance, and requirements before adoption; custom tools remain appropriate for unique workflows. Closest official exam-guide objective 2.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Evaluate the existing integration against requirements, security, and maintenance needs.
- **B:** Incorrect for this question. A generic interface can be split when its unrelated responsibilities cause ambiguity. Do not multiply near-identical tools without a meaningful boundary. In this case: Evaluate the existing integration against requirements, security, and maintenance needs.
- **C:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Evaluate the existing integration against requirements, security, and maintenance needs.
- **D:** Correct. A suitable standard integration may reduce work. Assess security, permissions, maintenance, and requirements before adoption; custom tools remain appropriate for unique workflows. In this case: Evaluate the existing integration against requirements, security, and maintenance needs.

### Question 57 — A

Answer: Clarify tool purpose, inputs, outputs, and boundaries. Explain the MCP tool's distinct search coverage and useful output so selection can be informed. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. Closest official exam-guide objective 2.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Explain the MCP tool's distinct search coverage and useful output so selection can be informed.
- **B:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Explain the MCP tool's distinct search coverage and useful output so selection can be informed.
- **C:** Incorrect for this question. Configured servers can expose tools together when connected, but server failure, approval, filtering, and permissions can affect what is actually usable. In this case: Explain the MCP tool's distinct search coverage and useful output so selection can be informed.
- **D:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Explain the MCP tool's distinct search coverage and useful output so selection can be informed.

### Question 58 — A

Answer: Expose a supported MCP resource catalog. Resources can present schema metadata, distinct from executing a database action. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. Closest official exam-guide objective 2.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Resources can present schema metadata, distinct from executing a database action.
- **B:** Incorrect for this question. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. In this case: Resources can present schema metadata, distinct from executing a database action.
- **C:** Incorrect for this question. Configured servers can expose tools together when connected, but server failure, approval, filtering, and permissions can affect what is actually usable. In this case: Resources can present schema metadata, distinct from executing a database action.
- **D:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Resources can present schema metadata, distinct from executing a database action.

### Question 59 — B

Answer: Reference runtime environment variables instead of committing tokens. Runtime secret references do not protect secrets if execution and logging expose them. Environment expansion can keep literal secrets out of project files. Supply credentials through an approved secret path and protect logs as well. Closest official exam-guide objective 2.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Runtime secret references do not protect secrets if execution and logging expose them.
- **B:** Correct. Environment expansion can keep literal secrets out of project files. Supply credentials through an approved secret path and protect logs as well. In this case: Runtime secret references do not protect secrets if execution and logging expose them.
- **C:** Incorrect for this question. Configured servers can expose tools together when connected, but server failure, approval, filtering, and permissions can affect what is actually usable. In this case: Runtime secret references do not protect secrets if execution and logging expose them.
- **D:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Runtime secret references do not protect secrets if execution and logging expose them.

### Question 60 — B

Answer: Use project-scoped .mcp.json for shared server configuration. Move shareable non-secret setup into project configuration with appropriate approvals. Versioned project configuration can distribute team tooling. Keep real credentials outside Git and check approvals and environment requirements. Closest official exam-guide objective 2.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Move shareable non-secret setup into project configuration with appropriate approvals.
- **B:** Correct. Versioned project configuration can distribute team tooling. Keep real credentials outside Git and check approvals and environment requirements. In this case: Move shareable non-secret setup into project configuration with appropriate approvals.
- **C:** Incorrect for this question. The guide describes user-scoped configuration in ~/.claude.json for personal tooling. Personal configuration is not automatically shared through the repository. In this case: Move shareable non-secret setup into project configuration with appropriate approvals.
- **D:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Move shareable non-secret setup into project configuration with appropriate approvals.

### Question 61 — D

Answer: Use Grep for content-pattern searches. This is a content-pattern search rather than filename discovery. Content search finds symbols, strings, and imports inside files. It is distinct from matching filenames and paths. Closest official exam-guide objective 2.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Inspecting current contents supplies evidence and reliable anchors before modification. A filename search alone does not reveal implementation behavior. In this case: This is a content-pattern search rather than filename discovery.
- **B:** Incorrect for this question. Command execution fits tests, builds, and similar tasks when authorized. It is more powerful than file search and needs explicit safety and runtime controls. In this case: This is a content-pattern search rather than filename discovery.
- **C:** Incorrect for this question. Glob discovers files by path patterns rather than searching their contents. It can identify candidates for later reading. In this case: This is a content-pattern search rather than filename discovery.
- **D:** Correct. Content search finds symbols, strings, and imports inside files. It is distinct from matching filenames and paths. In this case: This is a content-pattern search rather than filename discovery.

### Question 62 — B

Answer: Use Glob for filename or path-pattern discovery. Path-pattern discovery is distinct from searching text within files. Glob discovers files by path patterns rather than searching their contents. It can identify candidates for later reading. Closest official exam-guide objective 2.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Content search finds symbols, strings, and imports inside files. It is distinct from matching filenames and paths. In this case: Path-pattern discovery is distinct from searching text within files.
- **B:** Correct. Glob discovers files by path patterns rather than searching their contents. It can identify candidates for later reading. In this case: Path-pattern discovery is distinct from searching text within files.
- **C:** Incorrect for this question. Targeted replacement is suitable when current text can be identified uniquely. Ambiguous anchors can change the wrong location or fail. In this case: Path-pattern discovery is distinct from searching text within files.
- **D:** Incorrect for this question. Inspecting current contents supplies evidence and reliable anchors before modification. A filename search alone does not reveal implementation behavior. In this case: Path-pattern discovery is distinct from searching text within files.

### Question 63 — C

Answer: Use Read to inspect current file contents. Current contents provide the evidence and anchors needed for a safe edit. Inspecting current contents supplies evidence and reliable anchors before modification. A filename search alone does not reveal implementation behavior. Closest official exam-guide objective 2.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Glob discovers files by path patterns rather than searching their contents. It can identify candidates for later reading. In this case: Current contents provide the evidence and anchors needed for a safe edit.
- **B:** Incorrect for this question. Targeted replacement is suitable when current text can be identified uniquely. Ambiguous anchors can change the wrong location or fail. In this case: Current contents provide the evidence and anchors needed for a safe edit.
- **C:** Correct. Inspecting current contents supplies evidence and reliable anchors before modification. A filename search alone does not reveal implementation behavior. In this case: Current contents provide the evidence and anchors needed for a safe edit.
- **D:** Incorrect for this question. A full-file replacement can resolve ambiguous targeted edits, but must preserve unrelated content and account for concurrent changes. In this case: Current contents provide the evidence and anchors needed for a safe edit.

### Question 64 — D

Answer: Use Edit with a verified unique anchor. A unique anchored replacement avoids unnecessary full-file rewriting. Targeted replacement is suitable when current text can be identified uniquely. Ambiguous anchors can change the wrong location or fail. Closest official exam-guide objective 2.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Command execution fits tests, builds, and similar tasks when authorized. It is more powerful than file search and needs explicit safety and runtime controls. In this case: A unique anchored replacement avoids unnecessary full-file rewriting.
- **B:** Incorrect for this question. Inspecting current contents supplies evidence and reliable anchors before modification. A filename search alone does not reveal implementation behavior. In this case: A unique anchored replacement avoids unnecessary full-file rewriting.
- **C:** Incorrect for this question. A full-file replacement can resolve ambiguous targeted edits, but must preserve unrelated content and account for concurrent changes. In this case: A unique anchored replacement avoids unnecessary full-file rewriting.
- **D:** Correct. Targeted replacement is suitable when current text can be identified uniquely. Ambiguous anchors can change the wrong location or fail. In this case: A unique anchored replacement avoids unnecessary full-file rewriting.

### Question 65 — C

Answer: Read the current file and write a checked replacement. Inspect the full current file, construct a checked replacement, and preserve unrelated content. A full-file replacement can resolve ambiguous targeted edits, but must preserve unrelated content and account for concurrent changes. Closest official exam-guide objective 2.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Targeted replacement is suitable when current text can be identified uniquely. Ambiguous anchors can change the wrong location or fail. In this case: Inspect the full current file, construct a checked replacement, and preserve unrelated content.
- **B:** Incorrect for this question. Glob discovers files by path patterns rather than searching their contents. It can identify candidates for later reading. In this case: Inspect the full current file, construct a checked replacement, and preserve unrelated content.
- **C:** Correct. A full-file replacement can resolve ambiguous targeted edits, but must preserve unrelated content and account for concurrent changes. In this case: Inspect the full current file, construct a checked replacement, and preserve unrelated content.
- **D:** Incorrect for this question. Content search finds symbols, strings, and imports inside files. It is distinct from matching filenames and paths. In this case: Inspect the full current file, construct a checked replacement, and preserve unrelated content.

### Question 66 — A

Answer: Use Bash for an authorized command with bounded execution. Executing a command differs from discovering files or reading their text. Command execution fits tests, builds, and similar tasks when authorized. It is more powerful than file search and needs explicit safety and runtime controls. Closest official exam-guide objective 2.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Command execution fits tests, builds, and similar tasks when authorized. It is more powerful than file search and needs explicit safety and runtime controls. In this case: Executing a command differs from discovering files or reading their text.
- **B:** Incorrect for this question. Content search finds symbols, strings, and imports inside files. It is distinct from matching filenames and paths. In this case: Executing a command differs from discovering files or reading their text.
- **C:** Incorrect for this question. Glob discovers files by path patterns rather than searching their contents. It can identify candidates for later reading. In this case: Executing a command differs from discovering files or reading their text.
- **D:** Incorrect for this question. Inspecting current contents supplies evidence and reliable anchors before modification. A filename search alone does not reveal implementation behavior. In this case: Executing a command differs from discovering files or reading their text.

### Question 67 — A

Answer: Search exported aliases and wrappers as well as the original symbol. Trace exported aliases and wrappers instead of assuming one symbol spelling covers every call. Usage can flow through re-exports and renamed wrappers. A single literal search may not reveal every relevant caller. Closest official exam-guide objective 2.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Usage can flow through re-exports and renamed wrappers. A single literal search may not reveal every relevant caller. In this case: Trace exported aliases and wrappers instead of assuming one symbol spelling covers every call.
- **B:** Incorrect for this question. Inspecting current contents supplies evidence and reliable anchors before modification. A filename search alone does not reveal implementation behavior. In this case: Trace exported aliases and wrappers instead of assuming one symbol spelling covers every call.
- **C:** Incorrect for this question. Glob discovers files by path patterns rather than searching their contents. It can identify candidates for later reading. In this case: Trace exported aliases and wrappers instead of assuming one symbol spelling covers every call.
- **D:** Incorrect for this question. Content search finds symbols, strings, and imports inside files. It is distinct from matching filenames and paths. In this case: Trace exported aliases and wrappers instead of assuming one symbol spelling covers every call.

### Question 68 — A

Answer: Use Grep for content-pattern searches. Search file contents for the import pattern before selectively reading relevant files. Content search finds symbols, strings, and imports inside files. It is distinct from matching filenames and paths. Closest official exam-guide objective 2.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Content search finds symbols, strings, and imports inside files. It is distinct from matching filenames and paths. In this case: Search file contents for the import pattern before selectively reading relevant files.
- **B:** Incorrect for this question. A full-file replacement can resolve ambiguous targeted edits, but must preserve unrelated content and account for concurrent changes. In this case: Search file contents for the import pattern before selectively reading relevant files.
- **C:** Incorrect for this question. Targeted replacement is suitable when current text can be identified uniquely. Ambiguous anchors can change the wrong location or fail. In this case: Search file contents for the import pattern before selectively reading relevant files.
- **D:** Incorrect for this question. Glob discovers files by path patterns rather than searching their contents. It can identify candidates for later reading. In this case: Search file contents for the import pattern before selectively reading relevant files.

### Question 69 — D

Answer: Use Glob for filename or path-pattern discovery. Filename patterns identify candidates without scanning their internal text. Glob discovers files by path patterns rather than searching their contents. It can identify candidates for later reading. Closest official exam-guide objective 2.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. A full-file replacement can resolve ambiguous targeted edits, but must preserve unrelated content and account for concurrent changes. In this case: Filename patterns identify candidates without scanning their internal text.
- **B:** Incorrect for this question. Content search finds symbols, strings, and imports inside files. It is distinct from matching filenames and paths. In this case: Filename patterns identify candidates without scanning their internal text.
- **C:** Incorrect for this question. Command execution fits tests, builds, and similar tasks when authorized. It is more powerful than file search and needs explicit safety and runtime controls. In this case: Filename patterns identify candidates without scanning their internal text.
- **D:** Correct. Glob discovers files by path patterns rather than searching their contents. It can identify candidates for later reading. In this case: Filename patterns identify candidates without scanning their internal text.

### Question 70 — C

Answer: Use Read to inspect current file contents. Reinspect current content before deriving a safe replacement or anchor. Inspecting current contents supplies evidence and reliable anchors before modification. A filename search alone does not reveal implementation behavior. Closest official exam-guide objective 2.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Targeted replacement is suitable when current text can be identified uniquely. Ambiguous anchors can change the wrong location or fail. In this case: Reinspect current content before deriving a safe replacement or anchor.
- **B:** Incorrect for this question. Glob discovers files by path patterns rather than searching their contents. It can identify candidates for later reading. In this case: Reinspect current content before deriving a safe replacement or anchor.
- **C:** Correct. Inspecting current contents supplies evidence and reliable anchors before modification. A filename search alone does not reveal implementation behavior. In this case: Reinspect current content before deriving a safe replacement or anchor.
- **D:** Incorrect for this question. A full-file replacement can resolve ambiguous targeted edits, but must preserve unrelated content and account for concurrent changes. In this case: Reinspect current content before deriving a safe replacement or anchor.

### Question 71 — A

Answer: Give each specialist only task-relevant tools. Remove irrelevant operations from its effective tool set. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. Closest official exam-guide objective 2.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Remove irrelevant operations from its effective tool set.
- **B:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Remove irrelevant operations from its effective tool set.
- **C:** Incorrect for this question. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. In this case: Remove irrelevant operations from its effective tool set.
- **D:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Remove irrelevant operations from its effective tool set.

### Question 72 — D

Answer: Check connected-server discovery and effective availability. Effective connected capabilities matter more than the intended configuration list. Configured servers can expose tools together when connected, but server failure, approval, filtering, and permissions can affect what is actually usable. Closest official exam-guide objective 2.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. A suitable standard integration may reduce work. Assess security, permissions, maintenance, and requirements before adoption; custom tools remain appropriate for unique workflows. In this case: Effective connected capabilities matter more than the intended configuration list.
- **B:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Effective connected capabilities matter more than the intended configuration list.
- **C:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Effective connected capabilities matter more than the intended configuration list.
- **D:** Correct. Configured servers can expose tools together when connected, but server failure, approval, filtering, and permissions can affect what is actually usable. In this case: Effective connected capabilities matter more than the intended configuration list.

### Question 73 — D

Answer: Represent a successful query with no matches explicitly. A successful empty outcome differs from inability to access the source. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. Closest official exam-guide objective 2.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Permission denial does not justify trying alternate credentials or leaking restricted content. Recover only through explicitly authorized mechanisms. In this case: A successful empty outcome differs from inability to access the source.
- **B:** Incorrect for this question. An error contract should identify failure class, recoverability, and useful context. MCP isError marks an execution failure; it should not disguise a valid empty result. In this case: A successful empty outcome differs from inability to access the source.
- **C:** Incorrect for this question. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: A successful empty outcome differs from inability to access the source.
- **D:** Correct. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. In this case: A successful empty outcome differs from inability to access the source.

### Question 74 — A

Answer: Expose a constrained domain-specific operation. Validate destinations in a constrained operation rather than rely on its benign name. A narrow operation can enforce permitted sources, destinations, or actions more reliably than a general arbitrary-command or unrestricted-fetch interface. Closest official exam-guide objective 2.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. A narrow operation can enforce permitted sources, destinations, or actions more reliably than a general arbitrary-command or unrestricted-fetch interface. In this case: Validate destinations in a constrained operation rather than rely on its benign name.
- **B:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Validate destinations in a constrained operation rather than rely on its benign name.
- **C:** Incorrect for this question. A generic interface can be split when its unrelated responsibilities cause ambiguity. Do not multiply near-identical tools without a meaningful boundary. In this case: Validate destinations in a constrained operation rather than rely on its benign name.
- **D:** Incorrect for this question. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. In this case: Validate destinations in a constrained operation rather than rely on its benign name.

### Question 75 — B

Answer: Search exported aliases and wrappers as well as the original symbol. Search the exported names and their usage paths to avoid missing indirect callers. Usage can flow through re-exports and renamed wrappers. A single literal search may not reveal every relevant caller. Closest official exam-guide objective 2.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Glob discovers files by path patterns rather than searching their contents. It can identify candidates for later reading. In this case: Search the exported names and their usage paths to avoid missing indirect callers.
- **B:** Correct. Usage can flow through re-exports and renamed wrappers. A single literal search may not reveal every relevant caller. In this case: Search the exported names and their usage paths to avoid missing indirect callers.
- **C:** Incorrect for this question. A full-file replacement can resolve ambiguous targeted edits, but must preserve unrelated content and account for concurrent changes. In this case: Search the exported names and their usage paths to avoid missing indirect callers.
- **D:** Incorrect for this question. Command execution fits tests, builds, and similar tasks when authorized. It is more powerful than file search and needs explicit safety and runtime controls. In this case: Search the exported names and their usage paths to avoid missing indirect callers.

### Question 76 — B

Answer: Correct invalid arguments before retrying. Supply the documented required argument instead of retrying unchanged input. A validation failure points to an input defect. Repeating identical invalid arguments is not recovery. Closest official exam-guide objective 2.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: Supply the documented required argument instead of retrying unchanged input.
- **B:** Correct. A validation failure points to an input defect. Repeating identical invalid arguments is not recovery. In this case: Supply the documented required argument instead of retrying unchanged input.
- **C:** Incorrect for this question. A policy rejection is not normally fixed by repeating the same operation. Communicate the reason and legitimate next steps without evasion. In this case: Supply the documented required argument instead of retrying unchanged input.
- **D:** Incorrect for this question. Permission denial does not justify trying alternate credentials or leaking restricted content. Recover only through explicitly authorized mechanisms. In this case: Supply the documented required argument instead of retrying unchanged input.

### Question 77 — B

Answer: Reference runtime environment variables instead of committing tokens. Share configuration references, not literal secret values, and supply credentials at runtime. Environment expansion can keep literal secrets out of project files. Supply credentials through an approved secret path and protect logs as well. Closest official exam-guide objective 2.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. The guide describes user-scoped configuration in ~/.claude.json for personal tooling. Personal configuration is not automatically shared through the repository. In this case: Share configuration references, not literal secret values, and supply credentials at runtime.
- **B:** Correct. Environment expansion can keep literal secrets out of project files. Supply credentials through an approved secret path and protect logs as well. In this case: Share configuration references, not literal secret values, and supply credentials at runtime.
- **C:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Share configuration references, not literal secret values, and supply credentials at runtime.
- **D:** Incorrect for this question. Versioned project configuration can distribute team tooling. Keep real credentials outside Git and check approvals and environment requirements. In this case: Share configuration references, not literal secret values, and supply credentials at runtime.

### Question 78 — C

Answer: Use tool_choice with type any. Any enforces a tool call without forcing the same named schema for every document. Where supported, any requires a tool selection but leaves the specific tool to the model. It does not guarantee that a particular named tool runs. Closest official exam-guide objective 2.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Where supported, named tool selection requires the specified tool. Additional workflow ordering and authorization still belong in application code. In this case: Any enforces a tool call without forcing the same named schema for every document.
- **B:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Any enforces a tool call without forcing the same named schema for every document.
- **C:** Correct. Where supported, any requires a tool selection but leaves the specific tool to the model. It does not guarantee that a particular named tool runs. In this case: Any enforces a tool call without forcing the same named schema for every document.
- **D:** Incorrect for this question. Auto permits either a tool call or an ordinary response. It cannot guarantee extraction through a tool on every request. In this case: Any enforces a tool call without forcing the same named schema for every document.

### Question 79 — A

Answer: Use Edit with a verified unique anchor. A verified unique anchored edit is the least broad modification. Targeted replacement is suitable when current text can be identified uniquely. Ambiguous anchors can change the wrong location or fail. Closest official exam-guide objective 2.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Targeted replacement is suitable when current text can be identified uniquely. Ambiguous anchors can change the wrong location or fail. In this case: A verified unique anchored edit is the least broad modification.
- **B:** Incorrect for this question. Command execution fits tests, builds, and similar tasks when authorized. It is more powerful than file search and needs explicit safety and runtime controls. In this case: A verified unique anchored edit is the least broad modification.
- **C:** Incorrect for this question. A full-file replacement can resolve ambiguous targeted edits, but must preserve unrelated content and account for concurrent changes. In this case: A verified unique anchored edit is the least broad modification.
- **D:** Incorrect for this question. Inspecting current contents supplies evidence and reliable anchors before modification. A filename search alone does not reveal implementation behavior. In this case: A verified unique anchored edit is the least broad modification.

### Question 80 — D

Answer: Return a structured tool error with category and retryability. Report the permission failure explicitly so the coordinator does not conclude the records do not exist. An error contract should identify failure class, recoverability, and useful context. MCP isError marks an execution failure; it should not disguise a valid empty result. Closest official exam-guide objective 2.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Report the permission failure explicitly so the coordinator does not conclude the records do not exist.
- **B:** Incorrect for this question. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. In this case: Report the permission failure explicitly so the coordinator does not conclude the records do not exist.
- **C:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Report the permission failure explicitly so the coordinator does not conclude the records do not exist.
- **D:** Correct. An error contract should identify failure class, recoverability, and useful context. MCP isError marks an execution failure; it should not disguise a valid empty result. In this case: Report the permission failure explicitly so the coordinator does not conclude the records do not exist.

### Question 81 — B

Answer: Give each specialist only task-relevant tools. Unneeded cross-role operations should not be available to a document-only worker. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. Closest official exam-guide objective 2.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Unneeded cross-role operations should not be available to a document-only worker.
- **B:** Correct. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Unneeded cross-role operations should not be available to a document-only worker.
- **C:** Incorrect for this question. A generic interface can be split when its unrelated responsibilities cause ambiguity. Do not multiply near-identical tools without a meaningful boundary. In this case: Unneeded cross-role operations should not be available to a document-only worker.
- **D:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Unneeded cross-role operations should not be available to a document-only worker.

### Question 82 — D

Answer: Expose a constrained domain-specific operation. Constrain access to the approved document operation and validate permitted targets externally. A narrow operation can enforce permitted sources, destinations, or actions more reliably than a general arbitrary-command or unrestricted-fetch interface. Closest official exam-guide objective 2.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. In this case: Constrain access to the approved document operation and validate permitted targets externally.
- **B:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Constrain access to the approved document operation and validate permitted targets externally.
- **C:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Constrain access to the approved document operation and validate permitted targets externally.
- **D:** Correct. A narrow operation can enforce permitted sources, destinations, or actions more reliably than a general arbitrary-command or unrestricted-fetch interface. In this case: Constrain access to the approved document operation and validate permitted targets externally.

### Question 83 — C

Answer: Force the required named tool for that turn. Named selection is appropriate when choosing any available tool would be insufficient. Where supported, named tool selection requires the specified tool. Additional workflow ordering and authorization still belong in application code. Closest official exam-guide objective 2.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Where supported, any requires a tool selection but leaves the specific tool to the model. It does not guarantee that a particular named tool runs. In this case: Named selection is appropriate when choosing any available tool would be insufficient.
- **B:** Incorrect for this question. Configured servers can expose tools together when connected, but server failure, approval, filtering, and permissions can affect what is actually usable. In this case: Named selection is appropriate when choosing any available tool would be insufficient.
- **C:** Correct. Where supported, named tool selection requires the specified tool. Additional workflow ordering and authorization still belong in application code. In this case: Named selection is appropriate when choosing any available tool would be insufficient.
- **D:** Incorrect for this question. Auto permits either a tool call or an ordinary response. It cannot guarantee extraction through a tool on every request. In this case: Named selection is appropriate when choosing any available tool would be insufficient.

### Question 84 — A

Answer: Use tool_choice with type auto. Auto permits ordinary responses as well as tool use when appropriate. Auto permits either a tool call or an ordinary response. It cannot guarantee extraction through a tool on every request. Closest official exam-guide objective 2.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Auto permits either a tool call or an ordinary response. It cannot guarantee extraction through a tool on every request. In this case: Auto permits ordinary responses as well as tool use when appropriate.
- **B:** Incorrect for this question. Where supported, any requires a tool selection but leaves the specific tool to the model. It does not guarantee that a particular named tool runs. In this case: Auto permits ordinary responses as well as tool use when appropriate.
- **C:** Incorrect for this question. Where supported, named tool selection requires the specified tool. Additional workflow ordering and authorization still belong in application code. In this case: Auto permits ordinary responses as well as tool use when appropriate.
- **D:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Auto permits ordinary responses as well as tool use when appropriate.

### Question 85 — C

Answer: Enforce prerequisites in trusted execution code. Tool selection does not replace trusted authorization and business checks. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. Closest official exam-guide objective 2.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Tool selection does not replace trusted authorization and business checks.
- **B:** Incorrect for this question. Where supported, any requires a tool selection but leaves the specific tool to the model. It does not guarantee that a particular named tool runs. In this case: Tool selection does not replace trusted authorization and business checks.
- **C:** Correct. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Tool selection does not replace trusted authorization and business checks.
- **D:** Incorrect for this question. Where supported, named tool selection requires the specified tool. Additional workflow ordering and authorization still belong in application code. In this case: Tool selection does not replace trusted authorization and business checks.

### Question 86 — D

Answer: Clarify tool purpose, inputs, outputs, and boundaries. Clarify the relevant boundaries so both required operations can be selected correctly. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. Closest official exam-guide objective 2.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. A generic interface can be split when its unrelated responsibilities cause ambiguity. Do not multiply near-identical tools without a meaningful boundary. In this case: Clarify the relevant boundaries so both required operations can be selected correctly.
- **B:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Clarify the relevant boundaries so both required operations can be selected correctly.
- **C:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Clarify the relevant boundaries so both required operations can be selected correctly.
- **D:** Correct. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Clarify the relevant boundaries so both required operations can be selected correctly.

### Question 87 — B

Answer: Wait for validated prerequisite outputs. The application must enforce the data dependency instead of assuming selection implies completion. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. Closest official exam-guide objective 2.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Where supported, any requires a tool selection but leaves the specific tool to the model. It does not guarantee that a particular named tool runs. In this case: The application must enforce the data dependency instead of assuming selection implies completion.
- **B:** Correct. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: The application must enforce the data dependency instead of assuming selection implies completion.
- **C:** Incorrect for this question. Where supported, named tool selection requires the specified tool. Additional workflow ordering and authorization still belong in application code. In this case: The application must enforce the data dependency instead of assuming selection implies completion.
- **D:** Incorrect for this question. Auto permits either a tool call or an ordinary response. It cannot guarantee extraction through a tool on every request. In this case: The application must enforce the data dependency instead of assuming selection implies completion.

### Question 88 — A

Answer: Give each specialist only task-relevant tools. Specify the specialist's effective role-appropriate tool set rather than leave exposure unnecessarily broad. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. Closest official exam-guide objective 2.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Specify the specialist's effective role-appropriate tool set rather than leave exposure unnecessarily broad.
- **B:** Incorrect for this question. Configured servers can expose tools together when connected, but server failure, approval, filtering, and permissions can affect what is actually usable. In this case: Specify the specialist's effective role-appropriate tool set rather than leave exposure unnecessarily broad.
- **C:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Specify the specialist's effective role-appropriate tool set rather than leave exposure unnecessarily broad.
- **D:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Specify the specialist's effective role-appropriate tool set rather than leave exposure unnecessarily broad.

### Question 89 — D

Answer: Expose a constrained domain-specific operation. A constrained operation serves a frequent need without opening unrelated external actions. A narrow operation can enforce permitted sources, destinations, or actions more reliably than a general arbitrary-command or unrestricted-fetch interface. Closest official exam-guide objective 2.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: A constrained operation serves a frequent need without opening unrelated external actions.
- **B:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: A constrained operation serves a frequent need without opening unrelated external actions.
- **C:** Incorrect for this question. A generic interface can be split when its unrelated responsibilities cause ambiguity. Do not multiply near-identical tools without a meaningful boundary. In this case: A constrained operation serves a frequent need without opening unrelated external actions.
- **D:** Correct. A narrow operation can enforce permitted sources, destinations, or actions more reliably than a general arbitrary-command or unrestricted-fetch interface. In this case: A constrained operation serves a frequent need without opening unrelated external actions.

### Question 90 — C

Answer: Define and validate a precise input schema. Selection controls do not substitute for schema and semantic validation at execution boundaries. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. Closest official exam-guide objective 2.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Where supported, any requires a tool selection but leaves the specific tool to the model. It does not guarantee that a particular named tool runs. In this case: Selection controls do not substitute for schema and semantic validation at execution boundaries.
- **B:** Incorrect for this question. Where supported, named tool selection requires the specified tool. Additional workflow ordering and authorization still belong in application code. In this case: Selection controls do not substitute for schema and semantic validation at execution boundaries.
- **C:** Correct. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. In this case: Selection controls do not substitute for schema and semantic validation at execution boundaries.
- **D:** Incorrect for this question. Auto permits either a tool call or an ordinary response. It cannot guarantee extraction through a tool on every request. In this case: Selection controls do not substitute for schema and semantic validation at execution boundaries.

### Question 91 — C

Answer: Expose a supported MCP resource catalog. A resource catalog can present available content without pretending to execute a business action. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. Closest official exam-guide objective 2.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Versioned project configuration can distribute team tooling. Keep real credentials outside Git and check approvals and environment requirements. In this case: A resource catalog can present available content without pretending to execute a business action.
- **B:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: A resource catalog can present available content without pretending to execute a business action.
- **C:** Correct. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: A resource catalog can present available content without pretending to execute a business action.
- **D:** Incorrect for this question. Configured servers can expose tools together when connected, but server failure, approval, filtering, and permissions can affect what is actually usable. In this case: A resource catalog can present available content without pretending to execute a business action.

### Question 92 — C

Answer: Evaluate a maintained existing integration before writing a custom server. An existing integration must be assessed, not adopted solely because it avoids custom code. A suitable standard integration may reduce work. Assess security, permissions, maintenance, and requirements before adoption; custom tools remain appropriate for unique workflows. Closest official exam-guide objective 2.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Versioned project configuration can distribute team tooling. Keep real credentials outside Git and check approvals and environment requirements. In this case: An existing integration must be assessed, not adopted solely because it avoids custom code.
- **B:** Incorrect for this question. A generic interface can be split when its unrelated responsibilities cause ambiguity. Do not multiply near-identical tools without a meaningful boundary. In this case: An existing integration must be assessed, not adopted solely because it avoids custom code.
- **C:** Correct. A suitable standard integration may reduce work. Assess security, permissions, maintenance, and requirements before adoption; custom tools remain appropriate for unique workflows. In this case: An existing integration must be assessed, not adopted solely because it avoids custom code.
- **D:** Incorrect for this question. The guide describes user-scoped configuration in ~/.claude.json for personal tooling. Personal configuration is not automatically shared through the repository. In this case: An existing integration must be assessed, not adopted solely because it avoids custom code.

### Question 93 — D

Answer: Use project-scoped .mcp.json for shared server configuration. Versioned project setup supports reproducibility and shared review without sharing secret values. Versioned project configuration can distribute team tooling. Keep real credentials outside Git and check approvals and environment requirements. Closest official exam-guide objective 2.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. The guide describes user-scoped configuration in ~/.claude.json for personal tooling. Personal configuration is not automatically shared through the repository. In this case: Versioned project setup supports reproducibility and shared review without sharing secret values.
- **B:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Versioned project setup supports reproducibility and shared review without sharing secret values.
- **C:** Incorrect for this question. Environment expansion can keep literal secrets out of project files. Supply credentials through an approved secret path and protect logs as well. In this case: Versioned project setup supports reproducibility and shared review without sharing secret values.
- **D:** Correct. Versioned project configuration can distribute team tooling. Keep real credentials outside Git and check approvals and environment requirements. In this case: Versioned project setup supports reproducibility and shared review without sharing secret values.

### Question 94 — A

Answer: Use user-scoped MCP configuration for personal servers. User-scoped configuration serves personal rather than shared project tooling. The guide describes user-scoped configuration in ~/.claude.json for personal tooling. Personal configuration is not automatically shared through the repository. Closest official exam-guide objective 2.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. The guide describes user-scoped configuration in ~/.claude.json for personal tooling. Personal configuration is not automatically shared through the repository. In this case: User-scoped configuration serves personal rather than shared project tooling.
- **B:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: User-scoped configuration serves personal rather than shared project tooling.
- **C:** Incorrect for this question. Configured servers can expose tools together when connected, but server failure, approval, filtering, and permissions can affect what is actually usable. In this case: User-scoped configuration serves personal rather than shared project tooling.
- **D:** Incorrect for this question. Versioned project configuration can distribute team tooling. Keep real credentials outside Git and check approvals and environment requirements. In this case: User-scoped configuration serves personal rather than shared project tooling.

### Question 95 — B

Answer: Check connected-server discovery and effective availability. Discovery and effective approval or permission state determine actual available operations. Configured servers can expose tools together when connected, but server failure, approval, filtering, and permissions can affect what is actually usable. Closest official exam-guide objective 2.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Role-appropriate tools reduce selection ambiguity and unnecessary authority. Tool scoping complements, not replaces, external permission checks. In this case: Discovery and effective approval or permission state determine actual available operations.
- **B:** Correct. Configured servers can expose tools together when connected, but server failure, approval, filtering, and permissions can affect what is actually usable. In this case: Discovery and effective approval or permission state determine actual available operations.
- **C:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Discovery and effective approval or permission state determine actual available operations.
- **D:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Discovery and effective approval or permission state determine actual available operations.

### Question 96 — A

Answer: Use Grep for content-pattern searches. Content search can locate import statements across files before deeper reading. Content search finds symbols, strings, and imports inside files. It is distinct from matching filenames and paths. Closest official exam-guide objective 2.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Correct. Content search finds symbols, strings, and imports inside files. It is distinct from matching filenames and paths. In this case: Content search can locate import statements across files before deeper reading.
- **B:** Incorrect for this question. A full-file replacement can resolve ambiguous targeted edits, but must preserve unrelated content and account for concurrent changes. In this case: Content search can locate import statements across files before deeper reading.
- **C:** Incorrect for this question. Glob discovers files by path patterns rather than searching their contents. It can identify candidates for later reading. In this case: Content search can locate import statements across files before deeper reading.
- **D:** Incorrect for this question. Inspecting current contents supplies evidence and reliable anchors before modification. A filename search alone does not reveal implementation behavior. In this case: Content search can locate import statements across files before deeper reading.

### Question 97 — B

Answer: Use Glob for filename or path-pattern discovery. Glob matches paths when content terms are not yet known. Glob discovers files by path patterns rather than searching their contents. It can identify candidates for later reading. Closest official exam-guide objective 2.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Content search finds symbols, strings, and imports inside files. It is distinct from matching filenames and paths. In this case: Glob matches paths when content terms are not yet known.
- **B:** Correct. Glob discovers files by path patterns rather than searching their contents. It can identify candidates for later reading. In this case: Glob matches paths when content terms are not yet known.
- **C:** Incorrect for this question. Targeted replacement is suitable when current text can be identified uniquely. Ambiguous anchors can change the wrong location or fail. In this case: Glob matches paths when content terms are not yet known.
- **D:** Incorrect for this question. A full-file replacement can resolve ambiguous targeted edits, but must preserve unrelated content and account for concurrent changes. In this case: Glob matches paths when content terms are not yet known.

### Question 98 — C

Answer: Use a durable idempotency key for the same logical action. Durable logical-action identity helps prevent repeated effects despite an uncertain response. Where supported, repeated requests for one operation should resolve to one intended external effect. Generating a new key for each retry defeats duplicate protection. Closest official exam-guide objective 2.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. A validation failure points to an input defect. Repeating identical invalid arguments is not recovery. In this case: Durable logical-action identity helps prevent repeated effects despite an uncertain response.
- **B:** Incorrect for this question. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. In this case: Durable logical-action identity helps prevent repeated effects despite an uncertain response.
- **C:** Correct. Where supported, repeated requests for one operation should resolve to one intended external effect. Generating a new key for each retry defeats duplicate protection. In this case: Durable logical-action identity helps prevent repeated effects despite an uncertain response.
- **D:** Incorrect for this question. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: Durable logical-action identity helps prevent repeated effects despite an uncertain response.

### Question 99 — D

Answer: Return a structured tool error with category and retryability. Preserve the partial success and explicit failure rather than claim complete coverage or total absence. An error contract should identify failure class, recoverability, and useful context. MCP isError marks an execution failure; it should not disguise a valid empty result. Closest official exam-guide objective 2.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: Preserve the partial success and explicit failure rather than claim complete coverage or total absence.
- **B:** Incorrect for this question. An empty successful result means no matching records were found under the query. It is distinct from a timeout or permission failure. In this case: Preserve the partial success and explicit failure rather than claim complete coverage or total absence.
- **C:** Incorrect for this question. Useful descriptions explain when to use a tool and how it differs from neighbors. Reliable selection needs more than names or generic one-line descriptions. In this case: Preserve the partial success and explicit failure rather than claim complete coverage or total absence.
- **D:** Correct. An error contract should identify failure class, recoverability, and useful context. MCP isError marks an execution failure; it should not disguise a valid empty result. In this case: Preserve the partial success and explicit failure rather than claim complete coverage or total absence.

### Question 100 — D

Answer: Read the current file and write a checked replacement. A checked full-file write is appropriate when targeted anchors are unsuitable and unrelated content is preserved. A full-file replacement can resolve ambiguous targeted edits, but must preserve unrelated content and account for concurrent changes. Closest official exam-guide objective 2.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools

- **A:** Incorrect for this question. Command execution fits tests, builds, and similar tasks when authorized. It is more powerful than file search and needs explicit safety and runtime controls. In this case: A checked full-file write is appropriate when targeted anchors are unsuitable and unrelated content is preserved.
- **B:** Incorrect for this question. Glob discovers files by path patterns rather than searching their contents. It can identify candidates for later reading. In this case: A checked full-file write is appropriate when targeted anchors are unsuitable and unrelated content is preserved.
- **C:** Incorrect for this question. Targeted replacement is suitable when current text can be identified uniquely. Ambiguous anchors can change the wrong location or fail. In this case: A checked full-file write is appropriate when targeted anchors are unsuitable and unrelated content is preserved.
- **D:** Correct. A full-file replacement can resolve ambiguous targeted edits, but must preserve unrelated content and account for concurrent changes. In this case: A checked full-file write is appropriate when targeted anchors are unsuitable and unrelated content is preserved.
