# Claude Certified Architect – Foundations (CCAR-F) — Practice Set 3

Claude Code Configuration & Workflows

100 questions · Suggested practice duration: 200 minutes · Practice target: 80%

Tests 1–5 are domain-focused. Test 6 is an expanded blueprint-proportioned review, not an official exam replica. Related concepts recur.

Select ONE best answer for every question. Answer key follows all questions.

Original educational content, not actual, recalled, or copied Anthropic exam items.

## Questions

### 1. A new teammate misses mandatory repository conventions stored only in another developer's home directory. Where should shared instructions go?

Domain: Claude Code Configuration & Workflows

- A. Put personal cross-project preferences in ~/.claude/CLAUDE.md
- B. Put shared project standards in versioned CLAUDE.md
- C. Put an on-demand workflow in a project skill
- D. Use directory-scoped CLAUDE.md for a local package

### 2. A developer wants a preferred response style across their own repositories without changing teammates' behavior. Which scope fits?

Domain: Claude Code Configuration & Workflows

- A. Use directory-scoped CLAUDE.md for a local package
- B. Put shared project standards in versioned CLAUDE.md
- C. Organize focused conventions in .claude/rules/
- D. Put personal cross-project preferences in ~/.claude/CLAUDE.md

### 3. One package has conventions that do not apply to its siblings. Which instruction placement can fit that subtree?

Domain: Claude Code Configuration & Workflows

- A. Scope a rule with YAML paths glob patterns
- B. Put personal cross-project preferences in ~/.claude/CLAUDE.md
- C. Put shared project standards in versioned CLAUDE.md
- D. Use directory-scoped CLAUDE.md for a local package

### 4. A root instruction file should reference approved standards documents instead of copying their entire contents. Which mechanism is relevant?

Domain: Claude Code Configuration & Workflows

- A. Organize focused conventions in .claude/rules/
- B. Scope a rule with YAML paths glob patterns
- C. Put an on-demand workflow in a project skill
- D. Use @imports to keep instruction content modular

### 5. A single instruction file has become an unreadable mixture of testing, API, and deployment guidance. What organization helps?

Domain: Claude Code Configuration & Workflows

- A. Organize focused conventions in .claude/rules/
- B. Put shared project standards in versioned CLAUDE.md
- C. Put personal cross-project preferences in ~/.claude/CLAUDE.md
- D. Put an on-demand workflow in a project skill

### 6. Claude behaves as though a rule is missing even though its file exists. What diagnostic step should come first?

Domain: Claude Code Configuration & Workflows

- A. Inspect which instruction files are actually loaded
- B. Put shared project standards in versioned CLAUDE.md
- C. Use @imports to keep instruction content modular
- D. Put personal cross-project preferences in ~/.claude/CLAUDE.md

### 7. A project's universal build and test commands should be available to every teammate's sessions. Where should they be documented?

Domain: Claude Code Configuration & Workflows

- A. Put an on-demand workflow in a project skill
- B. Put personal cross-project preferences in ~/.claude/CLAUDE.md
- C. Put shared project standards in versioned CLAUDE.md
- D. Use a project-scoped custom slash command

### 8. A developer's home-level instruction causes behavior their teammates cannot reproduce. Which scope explains the difference?

Domain: Claude Code Configuration & Workflows

- A. Put shared project standards in versioned CLAUDE.md
- B. Use @imports to keep instruction content modular
- C. Put personal cross-project preferences in ~/.claude/CLAUDE.md
- D. Organize focused conventions in .claude/rules/

### 9. Two packages share an approved standards document but need different local additions. What modular mechanism can avoid duplicated shared text?

Domain: Claude Code Configuration & Workflows

- A. Use directory-scoped CLAUDE.md for a local package
- B. Use @imports to keep instruction content modular
- C. Put an on-demand workflow in a project skill
- D. Scope a rule with YAML paths glob patterns

### 10. A CLAUDE.md instruction forbids deployment, but trusted tooling still permits it. What should enforce an absolute prohibition?

Domain: Claude Code Configuration & Workflows

- A. Enforce prerequisites in trusted execution code
- B. Organize focused conventions in .claude/rules/
- C. Put personal cross-project preferences in ~/.claude/CLAUDE.md
- D. Put shared project standards in versioned CLAUDE.md

### 11. A team needs an invocable release-note workflow that is irrelevant to most coding turns. Which extension fits?

Domain: Claude Code Configuration & Workflows

- A. Put an on-demand workflow in a project skill
- B. Put shared project standards in versioned CLAUDE.md
- C. Use directory-scoped CLAUDE.md for a local package
- D. Scope a rule with YAML paths glob patterns

### 12. A reusable project slash command should be available to every developer through version control. What scope fits?

Domain: Claude Code Configuration & Workflows

- A. Put personal cross-project preferences in ~/.claude/CLAUDE.md
- B. Use a project-scoped custom slash command
- C. Put shared project standards in versioned CLAUDE.md
- D. Expose a supported MCP resource catalog

### 13. A repository-analysis skill produces extensive intermediate output that should not fill the main conversation. Which option is relevant?

Domain: Claude Code Configuration & Workflows

- A. Create a differently named personal skill variant
- B. Restrict skill tool access with supported frontmatter
- C. Use context: fork for isolated skill execution
- D. Provide argument-hint for invocation guidance

### 14. A documentation skill should not run destructive shell operations. Which frontmatter capability helps limit its tools?

Domain: Claude Code Configuration & Workflows

- A. Create a differently named personal skill variant
- B. Provide argument-hint for invocation guidance
- C. Use context: fork for isolated skill execution
- D. Restrict skill tool access with supported frontmatter

### 15. Users invoke a skill without knowing its expected package argument. Which metadata improves invocation guidance?

Domain: Claude Code Configuration & Workflows

- A. Create a differently named personal skill variant
- B. Restrict skill tool access with supported frontmatter
- C. Provide argument-hint for invocation guidance
- D. Use context: fork for isolated skill execution

### 16. One engineer wants a personal twist on a shared skill without changing the team's version. What approach fits?

Domain: Claude Code Configuration & Workflows

- A. Create a differently named personal skill variant
- B. Use a project-scoped custom slash command
- C. Put an on-demand workflow in a project skill
- D. Put shared project standards in versioned CLAUDE.md

### 17. A standard must guide every repository session, not only users who remember to invoke a workflow. Where should it live?

Domain: Claude Code Configuration & Workflows

- A. Put an on-demand workflow in a project skill
- B. Use a project-scoped custom slash command
- C. Scope a rule with YAML paths glob patterns
- D. Put shared project standards in versioned CLAUDE.md

### 18. A skill explores many alternatives, but only its concise conclusion should enter the main conversation. Which skill behavior fits?

Domain: Claude Code Configuration & Workflows

- A. Fork an independent branch from a valid shared baseline
- B. Delegate focused exploration to a read-oriented subagent
- C. Use context: fork for isolated skill execution
- D. Use plan mode to investigate and compare approaches

### 19. A skill prompt says 'never use Bash' but its effective configuration still grants command execution. What should be checked?

Domain: Claude Code Configuration & Workflows

- A. State explicit reportable and non-reportable criteria
- B. Restrict skill tool access with supported frontmatter
- C. Provide argument-hint for invocation guidance
- D. Use context: fork for isolated skill execution

### 20. A skill shows an argument hint, but a user passes an invalid target. What limitation should the architect recognize?

Domain: Claude Code Configuration & Workflows

- A. Use context: fork for isolated skill execution
- B. Define and validate a precise input schema
- C. Restrict skill tool access with supported frontmatter
- D. An argument hint is guidance, not validation

### 21. Test conventions must apply to matching test files scattered across several packages. Which scoping mechanism fits?

Domain: Claude Code Configuration & Workflows

- A. Put personal cross-project preferences in ~/.claude/CLAUDE.md
- B. Use directory-scoped CLAUDE.md for a local package
- C. Scope a rule with YAML paths glob patterns
- D. Put shared project standards in versioned CLAUDE.md

### 22. A team wants separate maintained files for API, test, and deployment conventions. Which organization is appropriate?

Domain: Claude Code Configuration & Workflows

- A. Use a project-scoped custom slash command
- B. Use @imports to keep instruction content modular
- C. Organize focused conventions in .claude/rules/
- D. Put an on-demand workflow in a project skill

### 23. Terraform instructions should load only for matching infrastructure files rather than ordinary UI work. What should be configured?

Domain: Claude Code Configuration & Workflows

- A. Use a project-scoped custom slash command
- B. Put shared project standards in versioned CLAUDE.md
- C. Put personal cross-project preferences in ~/.claude/CLAUDE.md
- D. Scope a rule with YAML paths glob patterns

### 24. Every file within one package follows its own convention, with no cross-directory pattern needed. Which approach can be simplest?

Domain: Claude Code Configuration & Workflows

- A. Put personal cross-project preferences in ~/.claude/CLAUDE.md
- B. Scope a rule with YAML paths glob patterns
- C. Use directory-scoped CLAUDE.md for a local package
- D. Put an on-demand workflow in a project skill

### 25. A glob-scoped rule never activates for the intended files. What diagnostic should verify the actual behavior?

Domain: Claude Code Configuration & Workflows

- A. Scope a rule with YAML paths glob patterns
- B. Use @imports to keep instruction content modular
- C. Put shared project standards in versioned CLAUDE.md
- D. Inspect which instruction files are actually loaded

### 26. A convention targets every *.test.ts file, regardless of package location. Which rule property is relevant?

Domain: Claude Code Configuration & Workflows

- A. Use @imports to keep instruction content modular
- B. Scope a rule with YAML paths glob patterns
- C. Use directory-scoped CLAUDE.md for a local package
- D. Put an on-demand workflow in a project skill

### 27. A universal secret-handling guideline should not disappear when no special file pattern matches. Where should it be available?

Domain: Claude Code Configuration & Workflows

- A. Put shared project standards in versioned CLAUDE.md
- B. Scope a rule with YAML paths glob patterns
- C. Put an on-demand workflow in a project skill
- D. Use directory-scoped CLAUDE.md for a local package

### 28. A monorepo has generated client files in unrelated subtrees that share one convention. What avoids duplicating local instruction files everywhere?

Domain: Claude Code Configuration & Workflows

- A. Put personal cross-project preferences in ~/.claude/CLAUDE.md
- B. Scope a rule with YAML paths glob patterns
- C. Use @imports to keep instruction content modular
- D. Use directory-scoped CLAUDE.md for a local package

### 29. Several instruction files copy the same long style standard and drift apart over time. What mechanism can reference one maintained version?

Domain: Claude Code Configuration & Workflows

- A. Use @imports to keep instruction content modular
- B. Organize focused conventions in .claude/rules/
- C. Put an on-demand workflow in a project skill
- D. Use a project-scoped custom slash command

### 30. A path rule says production files must not be changed, but that restriction must hold regardless of model behavior. What else is required?

Domain: Claude Code Configuration & Workflows

- A. Scope a rule with YAML paths glob patterns
- B. Put shared project standards in versioned CLAUDE.md
- C. Organize focused conventions in .claude/rules/
- D. Enforce prerequisites in trusted execution code

### 31. A migration affects many modules and has several valid architectural approaches. What mode should precede implementation?

Domain: Claude Code Configuration & Workflows

- A. Provide concrete input–output examples
- B. Use plan mode to investigate and compare approaches
- C. Use tests and specific failure feedback to drive iteration
- D. Implement a small well-understood change directly

### 32. A single known function needs one clearly specified validation check with existing tests. Which approach is proportionate?

Domain: Claude Code Configuration & Workflows

- A. Implement a small well-understood change directly
- B. Ask targeted design questions before implementation
- C. Use plan mode to investigate and compare approaches
- D. Delegate focused exploration to a read-oriented subagent

### 33. An unfamiliar package requires verbose discovery before a small design decision. What can keep exploration out of the main context?

Domain: Claude Code Configuration & Workflows

- A. Ask targeted design questions before implementation
- B. Delegate focused exploration to a read-oriented subagent
- C. Implement a small well-understood change directly
- D. Use plan mode to investigate and compare approaches

### 34. Two integration approaches require different infrastructure and failure handling. What should be compared before editing code?

Domain: Claude Code Configuration & Workflows

- A. Use tests and specific failure feedback to drive iteration
- B. Use plan mode to investigate and compare approaches
- C. Provide concrete input–output examples
- D. Implement a small well-understood change directly

### 35. A bug has a precise stack trace and an agreed one-line correction in one file. Which execution strategy fits?

Domain: Claude Code Configuration & Workflows

- A. Ask targeted design questions before implementation
- B. Implement a small well-understood change directly
- C. Delegate focused exploration to a read-oriented subagent
- D. Use plan mode to investigate and compare approaches

### 36. A developer cannot specify data-retention or retry requirements for a new service. What conversation pattern can surface missing constraints?

Domain: Claude Code Configuration & Workflows

- A. Use plan mode to investigate and compare approaches
- B. Use tests and specific failure feedback to drive iteration
- C. Implement a small well-understood change directly
- D. Ask targeted design questions before implementation

### 37. An engineer requests a library replacement across dozens of dependent files. What should the assistant do before broad changes?

Domain: Claude Code Configuration & Workflows

- A. Use plan mode to investigate and compare approaches
- B. Implement a small well-understood change directly
- C. Provide concrete input–output examples
- D. Use tests and specific failure feedback to drive iteration

### 38. Detailed code discovery is exhausting the main session while the coordinator only needs an architecture map. What delegation fits?

Domain: Claude Code Configuration & Workflows

- A. Compact context while preserving checked facts and open issues
- B. Delegate focused exploration to a read-oriented subagent
- C. Use plan mode to investigate and compare approaches
- D. Implement a small well-understood change directly

### 39. A team approves an investigation plan and now wants tested implementation. What relationship should connect those phases?

Domain: Claude Code Configuration & Workflows

- A. Use plan mode to investigate and compare approaches
- B. Implement a small well-understood change directly
- C. Wait for validated prerequisite outputs
- D. Run independent branches concurrently and join checked results

### 40. A request has clear goals but several competing cross-service designs. Which mode best supports choosing among them?

Domain: Claude Code Configuration & Workflows

- A. Use plan mode to investigate and compare approaches
- B. Provide concrete input–output examples
- C. Ask targeted design questions before implementation
- D. Implement a small well-understood change directly

### 41. A prose transformation requirement is interpreted differently in every run. What input can make expectations more concrete?

Domain: Claude Code Configuration & Workflows

- A. Ask targeted design questions before implementation
- B. Use tests and specific failure feedback to drive iteration
- C. State explicit reportable and non-reportable criteria
- D. Provide concrete input–output examples

### 42. A fix must handle null values and malformed dates correctly. What should guide iterative implementation?

Domain: Claude Code Configuration & Workflows

- A. Ask targeted design questions before implementation
- B. Provide concrete input–output examples
- C. Use tests and specific failure feedback to drive iteration
- D. State explicit reportable and non-reportable criteria

### 43. A caching feature has unspecified invalidation and failure behavior. What should happen before coding?

Domain: Claude Code Configuration & Workflows

- A. State explicit reportable and non-reportable criteria
- B. Ask targeted design questions before implementation
- C. Use tests and specific failure feedback to drive iteration
- D. Provide concrete input–output examples

### 44. Three reported bugs share a state transition, and fixing one changes the others. How should feedback be supplied?

Domain: Claude Code Configuration & Workflows

- A. Wait for validated prerequisite outputs
- B. Use tests and specific failure feedback to drive iteration
- C. Run independent branches concurrently and join checked results
- D. Explain interacting issues together before revising

### 45. Two fixes affect unrelated modules and can be validated independently. What iteration pattern can be appropriate?

Domain: Claude Code Configuration & Workflows

- A. Run independent branches concurrently and join checked results
- B. Explain interacting issues together before revising
- C. Provide concrete input–output examples
- D. Wait for validated prerequisite outputs

### 46. Claude says a fix works, but the team has a reproducible failing test. What feedback should drive the next revision?

Domain: Claude Code Configuration & Workflows

- A. Ask targeted design questions before implementation
- B. State explicit reportable and non-reportable criteria
- C. Use tests and specific failure feedback to drive iteration
- D. Provide concrete input–output examples

### 47. A migration must map blank strings, nulls, and missing fields differently. What can clarify the transformation contract?

Domain: Claude Code Configuration & Workflows

- A. Ask targeted design questions before implementation
- B. Use tests and specific failure feedback to drive iteration
- C. Provide concrete input–output examples
- D. State explicit reportable and non-reportable criteria

### 48. A change passes its happy path but breaks an important edge case. What should be added to the refinement loop?

Domain: Claude Code Configuration & Workflows

- A. Ask targeted design questions before implementation
- B. Provide concrete input–output examples
- C. Use tests and specific failure feedback to drive iteration
- D. Explain interacting issues together before revising

### 49. A request says 'make retries robust' but gives no acceptable duplicate-effect behavior. What should be clarified first?

Domain: Claude Code Configuration & Workflows

- A. Ask targeted design questions before implementation
- B. Implement a small well-understood change directly
- C. Provide concrete input–output examples
- D. Use plan mode to investigate and compare approaches

### 50. Concurrency and cache invalidation bugs appear only together. What issue-reporting pattern is most useful?

Domain: Claude Code Configuration & Workflows

- A. State explicit reportable and non-reportable criteria
- B. Use tests and specific failure feedback to drive iteration
- C. Explain interacting issues together before revising
- D. Provide concrete input–output examples

### 51. A CI job hangs because Claude Code waits for interactive conversation input. Which invocation mode is relevant?

Domain: Claude Code Configuration & Workflows

- A. Run Claude Code in non-interactive print mode
- B. Use plan mode to investigate and compare approaches
- C. Use supported JSON output and schema CLI options
- D. Use a project-scoped custom slash command

### 52. A review bot must produce fields that can be parsed into inline comments. Which CLI configuration helps?

Domain: Claude Code Configuration & Workflows

- A. Use supported JSON output and schema CLI options
- B. State explicit reportable and non-reportable criteria
- C. Provide concrete input–output examples
- D. Run Claude Code in non-interactive print mode

### 53. CI-generated tests ignore the team's fixture conventions. Where should shared universal test guidance be documented?

Domain: Claude Code Configuration & Workflows

- A. Put an on-demand workflow in a project skill
- B. Use a project-scoped custom slash command
- C. Put personal cross-project preferences in ~/.claude/CLAUDE.md
- D. Put shared project standards in versioned CLAUDE.md

### 54. Every push causes the review bot to repost the same unchanged finding. What context should the next review include?

Domain: Claude Code Configuration & Workflows

- A. Use an independent reviewer without the generator rationale
- B. State explicit reportable and non-reportable criteria
- C. Record detected_pattern and dismissal reasons
- D. Pass prior findings and request only new or unresolved issues

### 55. Test generation proposes helpers that do not exist and duplicates scenarios already covered. What context should be supplied?

Domain: Claude Code Configuration & Workflows

- A. Provide concrete input–output examples
- B. Put shared project standards in versioned CLAUDE.md
- C. Provide existing tests and approved fixtures
- D. Use tests and specific failure feedback to drive iteration

### 56. The same session generates and reviews its own patch, repeatedly missing its original assumption. What review architecture may help?

Domain: Claude Code Configuration & Workflows

- A. Use an independent reviewer without the generator rationale
- B. State explicit reportable and non-reportable criteria
- C. Pass prior findings and request only new or unresolved issues
- D. Use tests and specific failure feedback to drive iteration

### 57. A headless pipeline needs to invoke Claude Code without an interactive session. Which flag family fits?

Domain: Claude Code Configuration & Workflows

- A. Use supported JSON output and schema CLI options
- B. Run Claude Code in non-interactive print mode
- C. Use plan mode to investigate and compare approaches
- D. Put an on-demand workflow in a project skill

### 58. A CI parser fails because free-form review text changes between runs. What structured-output mechanism should be assessed?

Domain: Claude Code Configuration & Workflows

- A. Run Claude Code in non-interactive print mode
- B. Use supported JSON output and schema CLI options
- C. Pass prior findings and request only new or unresolved issues
- D. State explicit reportable and non-reportable criteria

### 59. Generated test cases use a different assertion library from the project. What evidence should the assistant see?

Domain: Claude Code Configuration & Workflows

- A. Use tests and specific failure feedback to drive iteration
- B. Provide existing tests and approved fixtures
- C. Pass prior findings and request only new or unresolved issues
- D. Provide concrete input–output examples

### 60. A review rerun must preserve still-unaddressed defects while suppressing resolved duplicates. What should be passed in?

Domain: Claude Code Configuration & Workflows

- A. Record detected_pattern and dismissal reasons
- B. Pass prior findings and request only new or unresolved issues
- C. State explicit reportable and non-reportable criteria
- D. Use an independent reviewer without the generator rationale

### 61. Two teammates on the same commit receive different instructions because their personal files differ. What should diagnose the discrepancy?

Domain: Claude Code Configuration & Workflows

- A. Put shared project standards in versioned CLAUDE.md
- B. Scope a rule with YAML paths glob patterns
- C. Inspect which instruction files are actually loaded
- D. Put personal cross-project preferences in ~/.claude/CLAUDE.md

### 62. A developer wants a personal experimental review workflow without altering the shared one. What naming and scope choice fits?

Domain: Claude Code Configuration & Workflows

- A. Put an on-demand workflow in a project skill
- B. Put shared project standards in versioned CLAUDE.md
- C. Create a differently named personal skill variant
- D. Use a project-scoped custom slash command

### 63. API-handler rules should apply to matching files in multiple services, not every file in each service. Which scope fits?

Domain: Claude Code Configuration & Workflows

- A. Use @imports to keep instruction content modular
- B. Scope a rule with YAML paths glob patterns
- C. Organize focused conventions in .claude/rules/
- D. Use directory-scoped CLAUDE.md for a local package

### 64. A refactor changes public interfaces and has uncertain compatibility requirements. What should precede broad implementation?

Domain: Claude Code Configuration & Workflows

- A. Implement a small well-understood change directly
- B. Use plan mode to investigate and compare approaches
- C. Provide concrete input–output examples
- D. Use tests and specific failure feedback to drive iteration

### 65. A developer reports only 'still broken' after a revision. What feedback would be more useful?

Domain: Claude Code Configuration & Workflows

- A. Provide concrete input–output examples
- B. Explain interacting issues together before revising
- C. Ask targeted design questions before implementation
- D. Use tests and specific failure feedback to drive iteration

### 66. A generated implementation must be reviewed against requirements, not defended using its original rationale. What reviewer setup helps?

Domain: Claude Code Configuration & Workflows

- A. Pass prior findings and request only new or unresolved issues
- B. Use tests and specific failure feedback to drive iteration
- C. Use an independent reviewer without the generator rationale
- D. State explicit reportable and non-reportable criteria

### 67. A package needs only selected shared standards, not an entire organization handbook. What modular instruction approach fits?

Domain: Claude Code Configuration & Workflows

- A. Put an on-demand workflow in a project skill
- B. Use a project-scoped custom slash command
- C. Use @imports to keep instruction content modular
- D. Scope a rule with YAML paths glob patterns

### 68. A skill runs separately but still uses the same external repository. What isolation limit should be understood?

Domain: Claude Code Configuration & Workflows

- A. Create a differently named personal skill variant
- B. Use context: fork for isolated skill execution
- C. Restrict skill tool access with supported frontmatter
- D. Provide argument-hint for invocation guidance

### 69. Two seemingly separate bug fixes modify the same state machine transition. How should their requirements be communicated?

Domain: Claude Code Configuration & Workflows

- A. Explain interacting issues together before revising
- B. Provide concrete input–output examples
- C. Wait for validated prerequisite outputs
- D. Use tests and specific failure feedback to drive iteration

### 70. A review bot overwhelms developers with harmless style comments despite a requirement to report actionable defects. What prompting improvement fits?

Domain: Claude Code Configuration & Workflows

- A. Use an independent reviewer without the generator rationale
- B. Provide existing tests and approved fixtures
- C. Pass prior findings and request only new or unresolved issues
- D. State explicit reportable and non-reportable criteria

### 71. A package's database conventions should appear when work reaches that subtree, not as personal guidance for every repository. What scope fits?

Domain: Claude Code Configuration & Workflows

- A. Put shared project standards in versioned CLAUDE.md
- B. Put personal cross-project preferences in ~/.claude/CLAUDE.md
- C. Use directory-scoped CLAUDE.md for a local package
- D. Put an on-demand workflow in a project skill

### 72. Team standards need separate review ownership for API and testing guidance. What instruction organization supports this?

Domain: Claude Code Configuration & Workflows

- A. Use a project-scoped custom slash command
- B. Use @imports to keep instruction content modular
- C. Put an on-demand workflow in a project skill
- D. Organize focused conventions in .claude/rules/

### 73. A test command lives only in a personal home file and therefore CI does not receive the guidance. What scope should change?

Domain: Claude Code Configuration & Workflows

- A. Put personal cross-project preferences in ~/.claude/CLAUDE.md
- B. Put an on-demand workflow in a project skill
- C. Use a project-scoped custom slash command
- D. Put shared project standards in versioned CLAUDE.md

### 74. A file contains the desired convention, but the running session never references that instruction source. What verification matters?

Domain: Claude Code Configuration & Workflows

- A. Inspect which instruction files are actually loaded
- B. Use @imports to keep instruction content modular
- C. Put personal cross-project preferences in ~/.claude/CLAUDE.md
- D. Scope a rule with YAML paths glob patterns

### 75. A standards document changes frequently and duplicated copies become inconsistent across packages. What approach reduces that drift?

Domain: Claude Code Configuration & Workflows

- A. Put shared project standards in versioned CLAUDE.md
- B. Use directory-scoped CLAUDE.md for a local package
- C. Use @imports to keep instruction content modular
- D. Scope a rule with YAML paths glob patterns

### 76. A team workflow needs specialized instructions only when users request a dependency audit. Which packaging fits?

Domain: Claude Code Configuration & Workflows

- A. Put an on-demand workflow in a project skill
- B. Put shared project standards in versioned CLAUDE.md
- C. Put personal cross-project preferences in ~/.claude/CLAUDE.md
- D. Organize focused conventions in .claude/rules/

### 77. A reusable task command should be reviewed and changed with repository code. Which scope is appropriate?

Domain: Claude Code Configuration & Workflows

- A. Put shared project standards in versioned CLAUDE.md
- B. Scope a rule with YAML paths glob patterns
- C. Put personal cross-project preferences in ~/.claude/CLAUDE.md
- D. Use a project-scoped custom slash command

### 78. A file-analysis skill should inspect sources without granting unnecessary external-command access. What capability should be assessed?

Domain: Claude Code Configuration & Workflows

- A. Provide argument-hint for invocation guidance
- B. Create a differently named personal skill variant
- C. Use context: fork for isolated skill execution
- D. Restrict skill tool access with supported frontmatter

### 79. A deployment-summary skill expects an environment name but users do not know that requirement. What metadata helps communicate invocation expectations?

Domain: Claude Code Configuration & Workflows

- A. Restrict skill tool access with supported frontmatter
- B. Create a differently named personal skill variant
- C. Use context: fork for isolated skill execution
- D. Provide argument-hint for invocation guidance

### 80. A user wishes to try a different review rubric while preserving the approved team workflow untouched. What setup fits?

Domain: Claude Code Configuration & Workflows

- A. Put shared project standards in versioned CLAUDE.md
- B. Put an on-demand workflow in a project skill
- C. Create a differently named personal skill variant
- D. Use a project-scoped custom slash command

### 81. A test rule currently loads during documentation work and consumes irrelevant context. What scoping change helps?

Domain: Claude Code Configuration & Workflows

- A. Put an on-demand workflow in a project skill
- B. Use @imports to keep instruction content modular
- C. Scope a rule with YAML paths glob patterns
- D. Put shared project standards in versioned CLAUDE.md

### 82. All content in a documentation package follows one local standard. Which option can express that subtree-wide instruction?

Domain: Claude Code Configuration & Workflows

- A. Use directory-scoped CLAUDE.md for a local package
- B. Scope a rule with YAML paths glob patterns
- C. Put personal cross-project preferences in ~/.claude/CLAUDE.md
- D. Put an on-demand workflow in a project skill

### 83. A formatting convention applies only to generated *.client.ts files across many packages. Which rule mechanism fits?

Domain: Claude Code Configuration & Workflows

- A. Use @imports to keep instruction content modular
- B. Scope a rule with YAML paths glob patterns
- C. Use a project-scoped custom slash command
- D. Use directory-scoped CLAUDE.md for a local package

### 84. A path rule seems to activate too broadly after a pattern edit. What should be inspected before adding more instructions?

Domain: Claude Code Configuration & Workflows

- A. Scope a rule with YAML paths glob patterns
- B. Put shared project standards in versioned CLAUDE.md
- C. Put personal cross-project preferences in ~/.claude/CLAUDE.md
- D. Inspect which instruction files are actually loaded

### 85. A team wants an understandable maintained set of conventions with separate topic files. What mechanism is appropriate?

Domain: Claude Code Configuration & Workflows

- A. Put an on-demand workflow in a project skill
- B. Organize focused conventions in .claude/rules/
- C. Use @imports to keep instruction content modular
- D. Use a project-scoped custom slash command

### 86. A verbose search for entry points would fill the main session, but the coordinator only needs a concise dependency map. What should be delegated?

Domain: Claude Code Configuration & Workflows

- A. Implement a small well-understood change directly
- B. Delegate focused exploration to a read-oriented subagent
- C. Use plan mode to investigate and compare approaches
- D. Ask targeted design questions before implementation

### 87. A feature changes authentication flow across several services with uncertain rollback behavior. Which mode should come first?

Domain: Claude Code Configuration & Workflows

- A. Use plan mode to investigate and compare approaches
- B. Implement a small well-understood change directly
- C. Use tests and specific failure feedback to drive iteration
- D. Provide concrete input–output examples

### 88. An agreed typo correction affects a single user-facing string and has no architectural impact. What mode is proportionate?

Domain: Claude Code Configuration & Workflows

- A. Implement a small well-understood change directly
- B. Ask targeted design questions before implementation
- C. Delegate focused exploration to a read-oriented subagent
- D. Use plan mode to investigate and compare approaches

### 89. A proposed feature depends on whether audit retention is mandatory, but nobody has specified it. What should the assistant do first?

Domain: Claude Code Configuration & Workflows

- A. Use plan mode to investigate and compare approaches
- B. Provide concrete input–output examples
- C. Use tests and specific failure feedback to drive iteration
- D. Ask targeted design questions before implementation

### 90. A team expects a design comparison, but Claude has already edited the code. What workflow choice would better match the request?

Domain: Claude Code Configuration & Workflows

- A. Provide concrete input–output examples
- B. Use tests and specific failure feedback to drive iteration
- C. Use plan mode to investigate and compare approaches
- D. Implement a small well-understood change directly

### 91. A parser must preserve leading zeros but normalize whitespace, and prose guidance yields inconsistent results. What evidence would clarify intent?

Domain: Claude Code Configuration & Workflows

- A. Provide concrete input–output examples
- B. State explicit reportable and non-reportable criteria
- C. Use tests and specific failure feedback to drive iteration
- D. Ask targeted design questions before implementation

### 92. An implementation fixes one failing case but breaks a previously supported input. What iteration mechanism should expose this?

Domain: Claude Code Configuration & Workflows

- A. Provide concrete input–output examples
- B. Use tests and specific failure feedback to drive iteration
- C. State explicit reportable and non-reportable criteria
- D. Ask targeted design questions before implementation

### 93. Two proposed changes alter the same validation order and cannot be reasoned about separately. How should feedback be organized?

Domain: Claude Code Configuration & Workflows

- A. Wait for validated prerequisite outputs
- B. Run independent branches concurrently and join checked results
- C. Provide concrete input–output examples
- D. Explain interacting issues together before revising

### 94. A developer requests 'secure file uploads' without specifying accepted types or size limits. What pattern helps discover requirements?

Domain: Claude Code Configuration & Workflows

- A. Use tests and specific failure feedback to drive iteration
- B. Provide concrete input–output examples
- C. Ask targeted design questions before implementation
- D. State explicit reportable and non-reportable criteria

### 95. A performance requirement is repeatedly ignored because it exists only as a vague sentence. What can make refinement measurable?

Domain: Claude Code Configuration & Workflows

- A. State explicit reportable and non-reportable criteria
- B. Use tests and specific failure feedback to drive iteration
- C. Provide concrete input–output examples
- D. Ask targeted design questions before implementation

### 96. A nightly job must finish without waiting for a human response in the terminal. Which invocation choice is necessary?

Domain: Claude Code Configuration & Workflows

- A. Run Claude Code in non-interactive print mode
- B. Use plan mode to investigate and compare approaches
- C. Use supported JSON output and schema CLI options
- D. Use a project-scoped custom slash command

### 97. A pipeline needs both execution status and validated structured findings before posting comments. What output approach is appropriate?

Domain: Claude Code Configuration & Workflows

- A. Use supported JSON output and schema CLI options
- B. Pass prior findings and request only new or unresolved issues
- C. Run Claude Code in non-interactive print mode
- D. State explicit reportable and non-reportable criteria

### 98. A new commit shifts line numbers but leaves a real finding unresolved. What context helps avoid either duplication or accidental suppression?

Domain: Claude Code Configuration & Workflows

- A. Use an independent reviewer without the generator rationale
- B. Pass prior findings and request only new or unresolved issues
- C. Provide existing tests and approved fixtures
- D. Record detected_pattern and dismissal reasons

### 99. Test generation invents a database fixture instead of using the repository's approved in-memory helper. What should be supplied?

Domain: Claude Code Configuration & Workflows

- A. Provide existing tests and approved fixtures
- B. Put shared project standards in versioned CLAUDE.md
- C. Use tests and specific failure feedback to drive iteration
- D. Provide concrete input–output examples

### 100. A CI review praises a generated patch because it repeats the original session's assumptions. What separation may improve scrutiny?

Domain: Claude Code Configuration & Workflows

- A. Use an independent reviewer without the generator rationale
- B. State explicit reportable and non-reportable criteria
- C. Use tests and specific failure feedback to drive iteration
- D. Pass prior findings and request only new or unresolved issues

---

## Answer key and explanations

### Question 1 — B

Answer: Put shared project standards in versioned CLAUDE.md. Versioned project instructions distribute team standards instead of relying on personal files. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. Closest official exam-guide objective 3.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: Versioned project instructions distribute team standards instead of relying on personal files.
- **B:** Correct. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Versioned project instructions distribute team standards instead of relying on personal files.
- **C:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: Versioned project instructions distribute team standards instead of relying on personal files.
- **D:** Incorrect for this question. Local instructions fit conventions tied to a particular subtree. Cross-directory filename patterns may be better served by path-scoped rules. In this case: Versioned project instructions distribute team standards instead of relying on personal files.

### Question 2 — D

Answer: Put personal cross-project preferences in ~/.claude/CLAUDE.md. User-level instructions express personal cross-project preferences without distributing them to teammates. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. Closest official exam-guide objective 3.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Local instructions fit conventions tied to a particular subtree. Cross-directory filename patterns may be better served by path-scoped rules. In this case: User-level instructions express personal cross-project preferences without distributing them to teammates.
- **B:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: User-level instructions express personal cross-project preferences without distributing them to teammates.
- **C:** Incorrect for this question. Topic-specific rule files reduce one oversized instruction document. Add path scoping when a rule is only relevant to selected files. In this case: User-level instructions express personal cross-project preferences without distributing them to teammates.
- **D:** Correct. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: User-level instructions express personal cross-project preferences without distributing them to teammates.

### Question 3 — D

Answer: Use directory-scoped CLAUDE.md for a local package. Directory-scoped instructions localize package-specific guidance instead of applying it to unrelated siblings. Local instructions fit conventions tied to a particular subtree. Cross-directory filename patterns may be better served by path-scoped rules. Closest official exam-guide objective 3.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. In this case: Directory-scoped instructions localize package-specific guidance instead of applying it to unrelated siblings.
- **B:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: Directory-scoped instructions localize package-specific guidance instead of applying it to unrelated siblings.
- **C:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Directory-scoped instructions localize package-specific guidance instead of applying it to unrelated siblings.
- **D:** Correct. Local instructions fit conventions tied to a particular subtree. Cross-directory filename patterns may be better served by path-scoped rules. In this case: Directory-scoped instructions localize package-specific guidance instead of applying it to unrelated siblings.

### Question 4 — D

Answer: Use @imports to keep instruction content modular. Imports can keep instruction content modular while retaining explicit references. Imports reference relevant supporting instruction files. Their actual loading and accessibility should be verified rather than assumed. Closest official exam-guide objective 3.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Topic-specific rule files reduce one oversized instruction document. Add path scoping when a rule is only relevant to selected files. In this case: Imports can keep instruction content modular while retaining explicit references.
- **B:** Incorrect for this question. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. In this case: Imports can keep instruction content modular while retaining explicit references.
- **C:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: Imports can keep instruction content modular while retaining explicit references.
- **D:** Correct. Imports reference relevant supporting instruction files. Their actual loading and accessibility should be verified rather than assumed. In this case: Imports can keep instruction content modular while retaining explicit references.

### Question 5 — A

Answer: Organize focused conventions in .claude/rules/. Focused topic files make conventions easier to maintain than one monolith. Topic-specific rule files reduce one oversized instruction document. Add path scoping when a rule is only relevant to selected files. Closest official exam-guide objective 3.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. Topic-specific rule files reduce one oversized instruction document. Add path scoping when a rule is only relevant to selected files. In this case: Focused topic files make conventions easier to maintain than one monolith.
- **B:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Focused topic files make conventions easier to maintain than one monolith.
- **C:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: Focused topic files make conventions easier to maintain than one monolith.
- **D:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: Focused topic files make conventions easier to maintain than one monolith.

### Question 6 — A

Answer: Inspect which instruction files are actually loaded. Inspect the effective loaded instruction set rather than infer loading from existence alone. The guide mentions /memory; current documentation also describes /context. Use the available inspection mechanism to diagnose scope and loading, not just the presence of a file. Closest official exam-guide objective 3.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. The guide mentions /memory; current documentation also describes /context. Use the available inspection mechanism to diagnose scope and loading, not just the presence of a file. In this case: Inspect the effective loaded instruction set rather than infer loading from existence alone.
- **B:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Inspect the effective loaded instruction set rather than infer loading from existence alone.
- **C:** Incorrect for this question. Imports reference relevant supporting instruction files. Their actual loading and accessibility should be verified rather than assumed. In this case: Inspect the effective loaded instruction set rather than infer loading from existence alone.
- **D:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: Inspect the effective loaded instruction set rather than infer loading from existence alone.

### Question 7 — C

Answer: Put shared project standards in versioned CLAUDE.md. Project instructions fit shared always-relevant repository guidance rather than a personal-only setting. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. Closest official exam-guide objective 3.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: Project instructions fit shared always-relevant repository guidance rather than a personal-only setting.
- **B:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: Project instructions fit shared always-relevant repository guidance rather than a personal-only setting.
- **C:** Correct. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Project instructions fit shared always-relevant repository guidance rather than a personal-only setting.
- **D:** Incorrect for this question. The guide describes .claude/commands/ for shared invocable commands. User-scoped commands are personal; feature details depend on Claude Code version. In this case: Project instructions fit shared always-relevant repository guidance rather than a personal-only setting.

### Question 8 — C

Answer: Put personal cross-project preferences in ~/.claude/CLAUDE.md. Personal configuration affects one user and is not automatically distributed through Git. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. Closest official exam-guide objective 3.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Personal configuration affects one user and is not automatically distributed through Git.
- **B:** Incorrect for this question. Imports reference relevant supporting instruction files. Their actual loading and accessibility should be verified rather than assumed. In this case: Personal configuration affects one user and is not automatically distributed through Git.
- **C:** Correct. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: Personal configuration affects one user and is not automatically distributed through Git.
- **D:** Incorrect for this question. Topic-specific rule files reduce one oversized instruction document. Add path scoping when a rule is only relevant to selected files. In this case: Personal configuration affects one user and is not automatically distributed through Git.

### Question 9 — B

Answer: Use @imports to keep instruction content modular. Each package can import relevant shared guidance while keeping its own additions. Imports reference relevant supporting instruction files. Their actual loading and accessibility should be verified rather than assumed. Closest official exam-guide objective 3.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Local instructions fit conventions tied to a particular subtree. Cross-directory filename patterns may be better served by path-scoped rules. In this case: Each package can import relevant shared guidance while keeping its own additions.
- **B:** Correct. Imports reference relevant supporting instruction files. Their actual loading and accessibility should be verified rather than assumed. In this case: Each package can import relevant shared guidance while keeping its own additions.
- **C:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: Each package can import relevant shared guidance while keeping its own additions.
- **D:** Incorrect for this question. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. In this case: Each package can import relevant shared guidance while keeping its own additions.

### Question 10 — A

Answer: Enforce prerequisites in trusted execution code. Contextual instructions are not hard policy; execution permissions and gates must enforce it. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. Closest official exam-guide objective 3.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Contextual instructions are not hard policy; execution permissions and gates must enforce it.
- **B:** Incorrect for this question. Topic-specific rule files reduce one oversized instruction document. Add path scoping when a rule is only relevant to selected files. In this case: Contextual instructions are not hard policy; execution permissions and gates must enforce it.
- **C:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: Contextual instructions are not hard policy; execution permissions and gates must enforce it.
- **D:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Contextual instructions are not hard policy; execution permissions and gates must enforce it.

### Question 11 — A

Answer: Put an on-demand workflow in a project skill. An on-demand skill packages task-specific procedure without filling universal instructions. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. Closest official exam-guide objective 3.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: An on-demand skill packages task-specific procedure without filling universal instructions.
- **B:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: An on-demand skill packages task-specific procedure without filling universal instructions.
- **C:** Incorrect for this question. Local instructions fit conventions tied to a particular subtree. Cross-directory filename patterns may be better served by path-scoped rules. In this case: An on-demand skill packages task-specific procedure without filling universal instructions.
- **D:** Incorrect for this question. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. In this case: An on-demand skill packages task-specific procedure without filling universal instructions.

### Question 12 — B

Answer: Use a project-scoped custom slash command. A project-scoped command is shared; a user command is personal. The guide describes .claude/commands/ for shared invocable commands. User-scoped commands are personal; feature details depend on Claude Code version. Closest official exam-guide objective 3.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: A project-scoped command is shared; a user command is personal.
- **B:** Correct. The guide describes .claude/commands/ for shared invocable commands. User-scoped commands are personal; feature details depend on Claude Code version. In this case: A project-scoped command is shared; a user command is personal.
- **C:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: A project-scoped command is shared; a user command is personal.
- **D:** Incorrect for this question. Resources can expose content or metadata such as document hierarchies and database schemas. They are not interchangeable with actions executed as tools. In this case: A project-scoped command is shared; a user command is personal.

### Question 13 — C

Answer: Use context: fork for isolated skill execution. Forked skill execution isolates exploratory conversational context where supported. Where supported, an isolated skill context contains intermediate exploration. It does not automatically provide filesystem isolation or remove tool-permission obligations. Closest official exam-guide objective 3.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. A personal variant can customize workflow without changing the shared skill for teammates. Distinct naming avoids accidental shadowing or confusion. In this case: Forked skill execution isolates exploratory conversational context where supported.
- **B:** Incorrect for this question. The guide covers allowed-tools to limit a skill workflow. Validate effective permissions; contextual instructions alone are not a sandbox. In this case: Forked skill execution isolates exploratory conversational context where supported.
- **C:** Correct. Where supported, an isolated skill context contains intermediate exploration. It does not automatically provide filesystem isolation or remove tool-permission obligations. In this case: Forked skill execution isolates exploratory conversational context where supported.
- **D:** Incorrect for this question. Argument hints help users supply needed parameters. They do not replace actual argument validation or supply missing business facts. In this case: Forked skill execution isolates exploratory conversational context where supported.

### Question 14 — D

Answer: Restrict skill tool access with supported frontmatter. Restrict supported tool access and verify effective permissions rather than rely only on prose. The guide covers allowed-tools to limit a skill workflow. Validate effective permissions; contextual instructions alone are not a sandbox. Closest official exam-guide objective 3.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. A personal variant can customize workflow without changing the shared skill for teammates. Distinct naming avoids accidental shadowing or confusion. In this case: Restrict supported tool access and verify effective permissions rather than rely only on prose.
- **B:** Incorrect for this question. Argument hints help users supply needed parameters. They do not replace actual argument validation or supply missing business facts. In this case: Restrict supported tool access and verify effective permissions rather than rely only on prose.
- **C:** Incorrect for this question. Where supported, an isolated skill context contains intermediate exploration. It does not automatically provide filesystem isolation or remove tool-permission obligations. In this case: Restrict supported tool access and verify effective permissions rather than rely only on prose.
- **D:** Correct. The guide covers allowed-tools to limit a skill workflow. Validate effective permissions; contextual instructions alone are not a sandbox. In this case: Restrict supported tool access and verify effective permissions rather than rely only on prose.

### Question 15 — C

Answer: Provide argument-hint for invocation guidance. An argument hint can show expected parameters but does not validate them by itself. Argument hints help users supply needed parameters. They do not replace actual argument validation or supply missing business facts. Closest official exam-guide objective 3.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. A personal variant can customize workflow without changing the shared skill for teammates. Distinct naming avoids accidental shadowing or confusion. In this case: An argument hint can show expected parameters but does not validate them by itself.
- **B:** Incorrect for this question. The guide covers allowed-tools to limit a skill workflow. Validate effective permissions; contextual instructions alone are not a sandbox. In this case: An argument hint can show expected parameters but does not validate them by itself.
- **C:** Correct. Argument hints help users supply needed parameters. They do not replace actual argument validation or supply missing business facts. In this case: An argument hint can show expected parameters but does not validate them by itself.
- **D:** Incorrect for this question. Where supported, an isolated skill context contains intermediate exploration. It does not automatically provide filesystem isolation or remove tool-permission obligations. In this case: An argument hint can show expected parameters but does not validate them by itself.

### Question 16 — A

Answer: Create a differently named personal skill variant. A differently named personal variant avoids modifying or ambiguously shadowing shared behavior. A personal variant can customize workflow without changing the shared skill for teammates. Distinct naming avoids accidental shadowing or confusion. Closest official exam-guide objective 3.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. A personal variant can customize workflow without changing the shared skill for teammates. Distinct naming avoids accidental shadowing or confusion. In this case: A differently named personal variant avoids modifying or ambiguously shadowing shared behavior.
- **B:** Incorrect for this question. The guide describes .claude/commands/ for shared invocable commands. User-scoped commands are personal; feature details depend on Claude Code version. In this case: A differently named personal variant avoids modifying or ambiguously shadowing shared behavior.
- **C:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: A differently named personal variant avoids modifying or ambiguously shadowing shared behavior.
- **D:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: A differently named personal variant avoids modifying or ambiguously shadowing shared behavior.

### Question 17 — D

Answer: Put shared project standards in versioned CLAUDE.md. Universal project guidance should not depend solely on optional skill invocation. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. Closest official exam-guide objective 3.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: Universal project guidance should not depend solely on optional skill invocation.
- **B:** Incorrect for this question. The guide describes .claude/commands/ for shared invocable commands. User-scoped commands are personal; feature details depend on Claude Code version. In this case: Universal project guidance should not depend solely on optional skill invocation.
- **C:** Incorrect for this question. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. In this case: Universal project guidance should not depend solely on optional skill invocation.
- **D:** Correct. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Universal project guidance should not depend solely on optional skill invocation.

### Question 18 — C

Answer: Use context: fork for isolated skill execution. Isolated skill context can contain intermediate exploration while returning useful results. Where supported, an isolated skill context contains intermediate exploration. It does not automatically provide filesystem isolation or remove tool-permission obligations. Closest official exam-guide objective 3.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Forking supports divergent explorations without overwriting the original conversation. It does not itself isolate external files or undo side effects. In this case: Isolated skill context can contain intermediate exploration while returning useful results.
- **B:** Incorrect for this question. Discovery can be isolated so verbose file output does not overwhelm the main conversation. Return useful findings and source pointers. In this case: Isolated skill context can contain intermediate exploration while returning useful results.
- **C:** Correct. Where supported, an isolated skill context contains intermediate exploration. It does not automatically provide filesystem isolation or remove tool-permission obligations. In this case: Isolated skill context can contain intermediate exploration while returning useful results.
- **D:** Incorrect for this question. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. In this case: Isolated skill context can contain intermediate exploration while returning useful results.

### Question 19 — B

Answer: Restrict skill tool access with supported frontmatter. Supported tool restrictions and actual permissions must match the intended boundary. The guide covers allowed-tools to limit a skill workflow. Validate effective permissions; contextual instructions alone are not a sandbox. Closest official exam-guide objective 3.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Supported tool restrictions and actual permissions must match the intended boundary.
- **B:** Correct. The guide covers allowed-tools to limit a skill workflow. Validate effective permissions; contextual instructions alone are not a sandbox. In this case: Supported tool restrictions and actual permissions must match the intended boundary.
- **C:** Incorrect for this question. Argument hints help users supply needed parameters. They do not replace actual argument validation or supply missing business facts. In this case: Supported tool restrictions and actual permissions must match the intended boundary.
- **D:** Incorrect for this question. Where supported, an isolated skill context contains intermediate exploration. It does not automatically provide filesystem isolation or remove tool-permission obligations. In this case: Supported tool restrictions and actual permissions must match the intended boundary.

### Question 20 — D

Answer: An argument hint is guidance, not validation. Invocation guidance does not replace real target or argument validation. A skill invocation hint communicates expected inputs but does not establish that supplied values are valid, authorized, or complete. Closest official exam-guide objective 3.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Where supported, an isolated skill context contains intermediate exploration. It does not automatically provide filesystem isolation or remove tool-permission obligations. In this case: Invocation guidance does not replace real target or argument validation.
- **B:** Incorrect for this question. Schemas specify types, required fields, enums, and constraints. Trusted code still checks authorization and semantic business rules. In this case: Invocation guidance does not replace real target or argument validation.
- **C:** Incorrect for this question. The guide covers allowed-tools to limit a skill workflow. Validate effective permissions; contextual instructions alone are not a sandbox. In this case: Invocation guidance does not replace real target or argument validation.
- **D:** Correct. A skill invocation hint communicates expected inputs but does not establish that supplied values are valid, authorized, or complete. In this case: Invocation guidance does not replace real target or argument validation.

### Question 21 — C

Answer: Scope a rule with YAML paths glob patterns. Path globs can match file roles across directory boundaries. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. Closest official exam-guide objective 3.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: Path globs can match file roles across directory boundaries.
- **B:** Incorrect for this question. Local instructions fit conventions tied to a particular subtree. Cross-directory filename patterns may be better served by path-scoped rules. In this case: Path globs can match file roles across directory boundaries.
- **C:** Correct. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. In this case: Path globs can match file roles across directory boundaries.
- **D:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Path globs can match file roles across directory boundaries.

### Question 22 — C

Answer: Organize focused conventions in .claude/rules/. Focused rule files separate topics and can later add path conditions where useful. Topic-specific rule files reduce one oversized instruction document. Add path scoping when a rule is only relevant to selected files. Closest official exam-guide objective 3.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. The guide describes .claude/commands/ for shared invocable commands. User-scoped commands are personal; feature details depend on Claude Code version. In this case: Focused rule files separate topics and can later add path conditions where useful.
- **B:** Incorrect for this question. Imports reference relevant supporting instruction files. Their actual loading and accessibility should be verified rather than assumed. In this case: Focused rule files separate topics and can later add path conditions where useful.
- **C:** Correct. Topic-specific rule files reduce one oversized instruction document. Add path scoping when a rule is only relevant to selected files. In this case: Focused rule files separate topics and can later add path conditions where useful.
- **D:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: Focused rule files separate topics and can later add path conditions where useful.

### Question 23 — D

Answer: Scope a rule with YAML paths glob patterns. YAML path patterns limit relevance to the intended files. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. Closest official exam-guide objective 3.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. The guide describes .claude/commands/ for shared invocable commands. User-scoped commands are personal; feature details depend on Claude Code version. In this case: YAML path patterns limit relevance to the intended files.
- **B:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: YAML path patterns limit relevance to the intended files.
- **C:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: YAML path patterns limit relevance to the intended files.
- **D:** Correct. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. In this case: YAML path patterns limit relevance to the intended files.

### Question 24 — C

Answer: Use directory-scoped CLAUDE.md for a local package. A subtree instruction file can express a genuinely local package convention. Local instructions fit conventions tied to a particular subtree. Cross-directory filename patterns may be better served by path-scoped rules. Closest official exam-guide objective 3.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: A subtree instruction file can express a genuinely local package convention.
- **B:** Incorrect for this question. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. In this case: A subtree instruction file can express a genuinely local package convention.
- **C:** Correct. Local instructions fit conventions tied to a particular subtree. Cross-directory filename patterns may be better served by path-scoped rules. In this case: A subtree instruction file can express a genuinely local package convention.
- **D:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: A subtree instruction file can express a genuinely local package convention.

### Question 25 — D

Answer: Inspect which instruction files are actually loaded. Inspect effective loading and the pattern rather than assume a saved rule is active. The guide mentions /memory; current documentation also describes /context. Use the available inspection mechanism to diagnose scope and loading, not just the presence of a file. Closest official exam-guide objective 3.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. In this case: Inspect effective loading and the pattern rather than assume a saved rule is active.
- **B:** Incorrect for this question. Imports reference relevant supporting instruction files. Their actual loading and accessibility should be verified rather than assumed. In this case: Inspect effective loading and the pattern rather than assume a saved rule is active.
- **C:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Inspect effective loading and the pattern rather than assume a saved rule is active.
- **D:** Correct. The guide mentions /memory; current documentation also describes /context. Use the available inspection mechanism to diagnose scope and loading, not just the presence of a file. In this case: Inspect effective loading and the pattern rather than assume a saved rule is active.

### Question 26 — B

Answer: Scope a rule with YAML paths glob patterns. Filename-based glob scoping follows the file role across the repository. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. Closest official exam-guide objective 3.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Imports reference relevant supporting instruction files. Their actual loading and accessibility should be verified rather than assumed. In this case: Filename-based glob scoping follows the file role across the repository.
- **B:** Correct. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. In this case: Filename-based glob scoping follows the file role across the repository.
- **C:** Incorrect for this question. Local instructions fit conventions tied to a particular subtree. Cross-directory filename patterns may be better served by path-scoped rules. In this case: Filename-based glob scoping follows the file role across the repository.
- **D:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: Filename-based glob scoping follows the file role across the repository.

### Question 27 — A

Answer: Put shared project standards in versioned CLAUDE.md. Always-relevant project guidance should not be confined to a conditional narrow rule. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. Closest official exam-guide objective 3.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Always-relevant project guidance should not be confined to a conditional narrow rule.
- **B:** Incorrect for this question. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. In this case: Always-relevant project guidance should not be confined to a conditional narrow rule.
- **C:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: Always-relevant project guidance should not be confined to a conditional narrow rule.
- **D:** Incorrect for this question. Local instructions fit conventions tied to a particular subtree. Cross-directory filename patterns may be better served by path-scoped rules. In this case: Always-relevant project guidance should not be confined to a conditional narrow rule.

### Question 28 — B

Answer: Scope a rule with YAML paths glob patterns. A cross-directory path rule can capture the shared filename or directory pattern. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. Closest official exam-guide objective 3.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: A cross-directory path rule can capture the shared filename or directory pattern.
- **B:** Correct. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. In this case: A cross-directory path rule can capture the shared filename or directory pattern.
- **C:** Incorrect for this question. Imports reference relevant supporting instruction files. Their actual loading and accessibility should be verified rather than assumed. In this case: A cross-directory path rule can capture the shared filename or directory pattern.
- **D:** Incorrect for this question. Local instructions fit conventions tied to a particular subtree. Cross-directory filename patterns may be better served by path-scoped rules. In this case: A cross-directory path rule can capture the shared filename or directory pattern.

### Question 29 — A

Answer: Use @imports to keep instruction content modular. Imports can reduce duplicated instruction text when common guidance is shared appropriately. Imports reference relevant supporting instruction files. Their actual loading and accessibility should be verified rather than assumed. Closest official exam-guide objective 3.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. Imports reference relevant supporting instruction files. Their actual loading and accessibility should be verified rather than assumed. In this case: Imports can reduce duplicated instruction text when common guidance is shared appropriately.
- **B:** Incorrect for this question. Topic-specific rule files reduce one oversized instruction document. Add path scoping when a rule is only relevant to selected files. In this case: Imports can reduce duplicated instruction text when common guidance is shared appropriately.
- **C:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: Imports can reduce duplicated instruction text when common guidance is shared appropriately.
- **D:** Incorrect for this question. The guide describes .claude/commands/ for shared invocable commands. User-scoped commands are personal; feature details depend on Claude Code version. In this case: Imports can reduce duplicated instruction text when common guidance is shared appropriately.

### Question 30 — D

Answer: Enforce prerequisites in trusted execution code. Trusted permissions or execution checks enforce the actual modification boundary. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. Closest official exam-guide objective 3.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. In this case: Trusted permissions or execution checks enforce the actual modification boundary.
- **B:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Trusted permissions or execution checks enforce the actual modification boundary.
- **C:** Incorrect for this question. Topic-specific rule files reduce one oversized instruction document. Add path scoping when a rule is only relevant to selected files. In this case: Trusted permissions or execution checks enforce the actual modification boundary.
- **D:** Correct. A programmatic gate checks current identity, state, and business rules before an external action. Prompt instructions alone are not an authorization boundary. In this case: Trusted permissions or execution checks enforce the actual modification boundary.

### Question 31 — B

Answer: Use plan mode to investigate and compare approaches. Plan first when scope and trade-offs require investigation and comparison. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. Closest official exam-guide objective 3.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Plan first when scope and trade-offs require investigation and comparison.
- **B:** Correct. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. In this case: Plan first when scope and trade-offs require investigation and comparison.
- **C:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Plan first when scope and trade-offs require investigation and comparison.
- **D:** Incorrect for this question. A narrow fix with known requirements may not need a long planning phase. Tests and review still apply. In this case: Plan first when scope and trade-offs require investigation and comparison.

### Question 32 — A

Answer: Implement a small well-understood change directly. A small well-understood fix may be implemented directly while retaining tests and review. A narrow fix with known requirements may not need a long planning phase. Tests and review still apply. Closest official exam-guide objective 3.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. A narrow fix with known requirements may not need a long planning phase. Tests and review still apply. In this case: A small well-understood fix may be implemented directly while retaining tests and review.
- **B:** Incorrect for this question. An interview-style clarification step surfaces unknown assumptions and constraints. Use it when uncertainty materially affects design. In this case: A small well-understood fix may be implemented directly while retaining tests and review.
- **C:** Incorrect for this question. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. In this case: A small well-understood fix may be implemented directly while retaining tests and review.
- **D:** Incorrect for this question. Discovery can be isolated so verbose file output does not overwhelm the main conversation. Return useful findings and source pointers. In this case: A small well-understood fix may be implemented directly while retaining tests and review.

### Question 33 — B

Answer: Delegate focused exploration to a read-oriented subagent. A focused read-oriented exploration worker can return concise useful findings. Discovery can be isolated so verbose file output does not overwhelm the main conversation. Return useful findings and source pointers. Closest official exam-guide objective 3.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. An interview-style clarification step surfaces unknown assumptions and constraints. Use it when uncertainty materially affects design. In this case: A focused read-oriented exploration worker can return concise useful findings.
- **B:** Correct. Discovery can be isolated so verbose file output does not overwhelm the main conversation. Return useful findings and source pointers. In this case: A focused read-oriented exploration worker can return concise useful findings.
- **C:** Incorrect for this question. A narrow fix with known requirements may not need a long planning phase. Tests and review still apply. In this case: A focused read-oriented exploration worker can return concise useful findings.
- **D:** Incorrect for this question. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. In this case: A focused read-oriented exploration worker can return concise useful findings.

### Question 34 — B

Answer: Use plan mode to investigate and compare approaches. Planning clarifies meaningful architectural trade-offs before committing to implementation. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. Closest official exam-guide objective 3.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Planning clarifies meaningful architectural trade-offs before committing to implementation.
- **B:** Correct. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. In this case: Planning clarifies meaningful architectural trade-offs before committing to implementation.
- **C:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Planning clarifies meaningful architectural trade-offs before committing to implementation.
- **D:** Incorrect for this question. A narrow fix with known requirements may not need a long planning phase. Tests and review still apply. In this case: Planning clarifies meaningful architectural trade-offs before committing to implementation.

### Question 35 — B

Answer: Implement a small well-understood change directly. The scope is already understood, so a large planning phase may add little value. A narrow fix with known requirements may not need a long planning phase. Tests and review still apply. Closest official exam-guide objective 3.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. An interview-style clarification step surfaces unknown assumptions and constraints. Use it when uncertainty materially affects design. In this case: The scope is already understood, so a large planning phase may add little value.
- **B:** Correct. A narrow fix with known requirements may not need a long planning phase. Tests and review still apply. In this case: The scope is already understood, so a large planning phase may add little value.
- **C:** Incorrect for this question. Discovery can be isolated so verbose file output does not overwhelm the main conversation. Return useful findings and source pointers. In this case: The scope is already understood, so a large planning phase may add little value.
- **D:** Incorrect for this question. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. In this case: The scope is already understood, so a large planning phase may add little value.

### Question 36 — D

Answer: Ask targeted design questions before implementation. Targeted questions should resolve design-critical uncertainty before implementation. An interview-style clarification step surfaces unknown assumptions and constraints. Use it when uncertainty materially affects design. Closest official exam-guide objective 3.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. In this case: Targeted questions should resolve design-critical uncertainty before implementation.
- **B:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Targeted questions should resolve design-critical uncertainty before implementation.
- **C:** Incorrect for this question. A narrow fix with known requirements may not need a long planning phase. Tests and review still apply. In this case: Targeted questions should resolve design-critical uncertainty before implementation.
- **D:** Correct. An interview-style clarification step surfaces unknown assumptions and constraints. Use it when uncertainty materially affects design. In this case: Targeted questions should resolve design-critical uncertainty before implementation.

### Question 37 — A

Answer: Use plan mode to investigate and compare approaches. Investigate dependencies and agree an approach rather than improvise a large migration. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. Closest official exam-guide objective 3.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. In this case: Investigate dependencies and agree an approach rather than improvise a large migration.
- **B:** Incorrect for this question. A narrow fix with known requirements may not need a long planning phase. Tests and review still apply. In this case: Investigate dependencies and agree an approach rather than improvise a large migration.
- **C:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Investigate dependencies and agree an approach rather than improvise a large migration.
- **D:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Investigate dependencies and agree an approach rather than improvise a large migration.

### Question 38 — B

Answer: Delegate focused exploration to a read-oriented subagent. Isolate discovery in a focused worker and return structured findings. Discovery can be isolated so verbose file output does not overwhelm the main conversation. Return useful findings and source pointers. Closest official exam-guide objective 3.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Isolate discovery in a focused worker and return structured findings.
- **B:** Correct. Discovery can be isolated so verbose file output does not overwhelm the main conversation. Return useful findings and source pointers. In this case: Isolate discovery in a focused worker and return structured findings.
- **C:** Incorrect for this question. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. In this case: Isolate discovery in a focused worker and return structured findings.
- **D:** Incorrect for this question. A narrow fix with known requirements may not need a long planning phase. Tests and review still apply. In this case: Isolate discovery in a focused worker and return structured findings.

### Question 39 — C

Answer: Wait for validated prerequisite outputs. Execution should follow the accepted plan and verified prerequisites rather than be confused with planning completion. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. Closest official exam-guide objective 3.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. In this case: Execution should follow the accepted plan and verified prerequisites rather than be confused with planning completion.
- **B:** Incorrect for this question. A narrow fix with known requirements may not need a long planning phase. Tests and review still apply. In this case: Execution should follow the accepted plan and verified prerequisites rather than be confused with planning completion.
- **C:** Correct. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: Execution should follow the accepted plan and verified prerequisites rather than be confused with planning completion.
- **D:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Execution should follow the accepted plan and verified prerequisites rather than be confused with planning completion.

### Question 40 — A

Answer: Use plan mode to investigate and compare approaches. Architectural alternatives benefit from explicit analysis before edits begin. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. Closest official exam-guide objective 3.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. In this case: Architectural alternatives benefit from explicit analysis before edits begin.
- **B:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Architectural alternatives benefit from explicit analysis before edits begin.
- **C:** Incorrect for this question. An interview-style clarification step surfaces unknown assumptions and constraints. Use it when uncertainty materially affects design. In this case: Architectural alternatives benefit from explicit analysis before edits begin.
- **D:** Incorrect for this question. A narrow fix with known requirements may not need a long planning phase. Tests and review still apply. In this case: Architectural alternatives benefit from explicit analysis before edits begin.

### Question 41 — D

Answer: Provide concrete input–output examples. Representative input-output examples clarify the exact intended transformation. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. Closest official exam-guide objective 3.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. An interview-style clarification step surfaces unknown assumptions and constraints. Use it when uncertainty materially affects design. In this case: Representative input-output examples clarify the exact intended transformation.
- **B:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Representative input-output examples clarify the exact intended transformation.
- **C:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Representative input-output examples clarify the exact intended transformation.
- **D:** Correct. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Representative input-output examples clarify the exact intended transformation.

### Question 42 — C

Answer: Use tests and specific failure feedback to drive iteration. Specific tests make boundary behavior and regressions observable. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. Closest official exam-guide objective 3.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. An interview-style clarification step surfaces unknown assumptions and constraints. Use it when uncertainty materially affects design. In this case: Specific tests make boundary behavior and regressions observable.
- **B:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Specific tests make boundary behavior and regressions observable.
- **C:** Correct. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Specific tests make boundary behavior and regressions observable.
- **D:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Specific tests make boundary behavior and regressions observable.

### Question 43 — B

Answer: Ask targeted design questions before implementation. Targeted design questions can uncover overlooked requirements that affect architecture. An interview-style clarification step surfaces unknown assumptions and constraints. Use it when uncertainty materially affects design. Closest official exam-guide objective 3.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Targeted design questions can uncover overlooked requirements that affect architecture.
- **B:** Correct. An interview-style clarification step surfaces unknown assumptions and constraints. Use it when uncertainty materially affects design. In this case: Targeted design questions can uncover overlooked requirements that affect architecture.
- **C:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Targeted design questions can uncover overlooked requirements that affect architecture.
- **D:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Targeted design questions can uncover overlooked requirements that affect architecture.

### Question 44 — D

Answer: Explain interacting issues together before revising. Explain the interacting failures and constraints together so the revision can reconcile them. When fixes influence one another, provide the combined constraints and failure evidence. Independent issues can be addressed separately. Closest official exam-guide objective 3.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: Explain the interacting failures and constraints together so the revision can reconcile them.
- **B:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Explain the interacting failures and constraints together so the revision can reconcile them.
- **C:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Explain the interacting failures and constraints together so the revision can reconcile them.
- **D:** Correct. When fixes influence one another, provide the combined constraints and failure evidence. Independent issues can be addressed separately. In this case: Explain the interacting failures and constraints together so the revision can reconcile them.

### Question 45 — D

Answer: Wait for validated prerequisite outputs. Independent issues may be addressed sequentially without forcing one tangled revision. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. Closest official exam-guide objective 3.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Independent issues may be addressed sequentially without forcing one tangled revision.
- **B:** Incorrect for this question. When fixes influence one another, provide the combined constraints and failure evidence. Independent issues can be addressed separately. In this case: Independent issues may be addressed sequentially without forcing one tangled revision.
- **C:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Independent issues may be addressed sequentially without forcing one tangled revision.
- **D:** Correct. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: Independent issues may be addressed sequentially without forcing one tangled revision.

### Question 46 — C

Answer: Use tests and specific failure feedback to drive iteration. Share the specific failure and expected behavior instead of accepting an unsupported success claim. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. Closest official exam-guide objective 3.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. An interview-style clarification step surfaces unknown assumptions and constraints. Use it when uncertainty materially affects design. In this case: Share the specific failure and expected behavior instead of accepting an unsupported success claim.
- **B:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Share the specific failure and expected behavior instead of accepting an unsupported success claim.
- **C:** Correct. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Share the specific failure and expected behavior instead of accepting an unsupported success claim.
- **D:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Share the specific failure and expected behavior instead of accepting an unsupported success claim.

### Question 47 — C

Answer: Provide concrete input–output examples. Concrete examples reveal distinctions that broad prose may leave ambiguous. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. Closest official exam-guide objective 3.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. An interview-style clarification step surfaces unknown assumptions and constraints. Use it when uncertainty materially affects design. In this case: Concrete examples reveal distinctions that broad prose may leave ambiguous.
- **B:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Concrete examples reveal distinctions that broad prose may leave ambiguous.
- **C:** Correct. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Concrete examples reveal distinctions that broad prose may leave ambiguous.
- **D:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Concrete examples reveal distinctions that broad prose may leave ambiguous.

### Question 48 — C

Answer: Use tests and specific failure feedback to drive iteration. Include the edge case in checkable tests and use its failure as feedback. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. Closest official exam-guide objective 3.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. An interview-style clarification step surfaces unknown assumptions and constraints. Use it when uncertainty materially affects design. In this case: Include the edge case in checkable tests and use its failure as feedback.
- **B:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Include the edge case in checkable tests and use its failure as feedback.
- **C:** Correct. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Include the edge case in checkable tests and use its failure as feedback.
- **D:** Incorrect for this question. When fixes influence one another, provide the combined constraints and failure evidence. Independent issues can be addressed separately. In this case: Include the edge case in checkable tests and use its failure as feedback.

### Question 49 — A

Answer: Ask targeted design questions before implementation. Ask about side effects and retry semantics before choosing an implementation. An interview-style clarification step surfaces unknown assumptions and constraints. Use it when uncertainty materially affects design. Closest official exam-guide objective 3.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. An interview-style clarification step surfaces unknown assumptions and constraints. Use it when uncertainty materially affects design. In this case: Ask about side effects and retry semantics before choosing an implementation.
- **B:** Incorrect for this question. A narrow fix with known requirements may not need a long planning phase. Tests and review still apply. In this case: Ask about side effects and retry semantics before choosing an implementation.
- **C:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Ask about side effects and retry semantics before choosing an implementation.
- **D:** Incorrect for this question. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. In this case: Ask about side effects and retry semantics before choosing an implementation.

### Question 50 — C

Answer: Explain interacting issues together before revising. Combined evidence helps prevent a local fix from violating another interacting requirement. When fixes influence one another, provide the combined constraints and failure evidence. Independent issues can be addressed separately. Closest official exam-guide objective 3.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Combined evidence helps prevent a local fix from violating another interacting requirement.
- **B:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Combined evidence helps prevent a local fix from violating another interacting requirement.
- **C:** Correct. When fixes influence one another, provide the combined constraints and failure evidence. Independent issues can be addressed separately. In this case: Combined evidence helps prevent a local fix from violating another interacting requirement.
- **D:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Combined evidence helps prevent a local fix from violating another interacting requirement.

### Question 51 — A

Answer: Run Claude Code in non-interactive print mode. Non-interactive print mode is intended for automated runs rather than conversational input. The -p or --print mode is intended for non-interactive runs. Authentication, permissions, termination, and artifact capture still require CI configuration. Closest official exam-guide objective 3.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. The -p or --print mode is intended for non-interactive runs. Authentication, permissions, termination, and artifact capture still require CI configuration. In this case: Non-interactive print mode is intended for automated runs rather than conversational input.
- **B:** Incorrect for this question. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. In this case: Non-interactive print mode is intended for automated runs rather than conversational input.
- **C:** Incorrect for this question. The guide describes --output-format json and --json-schema for machine-parseable CI results. Verify the installed version and check execution status as well as payload. In this case: Non-interactive print mode is intended for automated runs rather than conversational input.
- **D:** Incorrect for this question. The guide describes .claude/commands/ for shared invocable commands. User-scoped commands are personal; feature details depend on Claude Code version. In this case: Non-interactive print mode is intended for automated runs rather than conversational input.

### Question 52 — A

Answer: Use supported JSON output and schema CLI options. Use supported JSON output and schema options, then validate execution status and payload. The guide describes --output-format json and --json-schema for machine-parseable CI results. Verify the installed version and check execution status as well as payload. Closest official exam-guide objective 3.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. The guide describes --output-format json and --json-schema for machine-parseable CI results. Verify the installed version and check execution status as well as payload. In this case: Use supported JSON output and schema options, then validate execution status and payload.
- **B:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Use supported JSON output and schema options, then validate execution status and payload.
- **C:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Use supported JSON output and schema options, then validate execution status and payload.
- **D:** Incorrect for this question. The -p or --print mode is intended for non-interactive runs. Authentication, permissions, termination, and artifact capture still require CI configuration. In this case: Use supported JSON output and schema options, then validate execution status and payload.

### Question 53 — D

Answer: Put shared project standards in versioned CLAUDE.md. Project instructions make repository standards available beyond one developer's personal session. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. Closest official exam-guide objective 3.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: Project instructions make repository standards available beyond one developer's personal session.
- **B:** Incorrect for this question. The guide describes .claude/commands/ for shared invocable commands. User-scoped commands are personal; feature details depend on Claude Code version. In this case: Project instructions make repository standards available beyond one developer's personal session.
- **C:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: Project instructions make repository standards available beyond one developer's personal session.
- **D:** Correct. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Project instructions make repository standards available beyond one developer's personal session.

### Question 54 — D

Answer: Pass prior findings and request only new or unresolved issues. Prior findings help distinguish new or still-unresolved issues and avoid duplicate comments. Comparing the current diff with prior findings can reduce duplicate review comments. Preserve still-valid findings rather than simply suppressing all repeats. Closest official exam-guide objective 3.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Independent review reduces anchoring on the original solution. It still needs the specification, relevant code, and evidence; independence does not guarantee correctness. In this case: Prior findings help distinguish new or still-unresolved issues and avoid duplicate comments.
- **B:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Prior findings help distinguish new or still-unresolved issues and avoid duplicate comments.
- **C:** Incorrect for this question. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: Prior findings help distinguish new or still-unresolved issues and avoid duplicate comments.
- **D:** Correct. Comparing the current diff with prior findings can reduce duplicate review comments. Preserve still-valid findings rather than simply suppressing all repeats. In this case: Prior findings help distinguish new or still-unresolved issues and avoid duplicate comments.

### Question 55 — C

Answer: Provide existing tests and approved fixtures. Existing tests and approved fixtures constrain generation to the real repository. Relevant test context helps generation avoid duplicates and use valid repository conventions. Do not invent unavailable helper functions or external test data. Closest official exam-guide objective 3.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Existing tests and approved fixtures constrain generation to the real repository.
- **B:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Existing tests and approved fixtures constrain generation to the real repository.
- **C:** Correct. Relevant test context helps generation avoid duplicates and use valid repository conventions. Do not invent unavailable helper functions or external test data. In this case: Existing tests and approved fixtures constrain generation to the real repository.
- **D:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Existing tests and approved fixtures constrain generation to the real repository.

### Question 56 — A

Answer: Use an independent reviewer without the generator rationale. A separate reviewer without the generator rationale can reduce anchoring. Independent review reduces anchoring on the original solution. It still needs the specification, relevant code, and evidence; independence does not guarantee correctness. Closest official exam-guide objective 3.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. Independent review reduces anchoring on the original solution. It still needs the specification, relevant code, and evidence; independence does not guarantee correctness. In this case: A separate reviewer without the generator rationale can reduce anchoring.
- **B:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: A separate reviewer without the generator rationale can reduce anchoring.
- **C:** Incorrect for this question. Comparing the current diff with prior findings can reduce duplicate review comments. Preserve still-valid findings rather than simply suppressing all repeats. In this case: A separate reviewer without the generator rationale can reduce anchoring.
- **D:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: A separate reviewer without the generator rationale can reduce anchoring.

### Question 57 — B

Answer: Run Claude Code in non-interactive print mode. The -p or --print option supports non-interactive invocation. The -p or --print mode is intended for non-interactive runs. Authentication, permissions, termination, and artifact capture still require CI configuration. Closest official exam-guide objective 3.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. The guide describes --output-format json and --json-schema for machine-parseable CI results. Verify the installed version and check execution status as well as payload. In this case: The -p or --print option supports non-interactive invocation.
- **B:** Correct. The -p or --print mode is intended for non-interactive runs. Authentication, permissions, termination, and artifact capture still require CI configuration. In this case: The -p or --print option supports non-interactive invocation.
- **C:** Incorrect for this question. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. In this case: The -p or --print option supports non-interactive invocation.
- **D:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: The -p or --print option supports non-interactive invocation.

### Question 58 — B

Answer: Use supported JSON output and schema CLI options. Supported machine-readable CLI output and schema validation address parseability. The guide describes --output-format json and --json-schema for machine-parseable CI results. Verify the installed version and check execution status as well as payload. Closest official exam-guide objective 3.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. The -p or --print mode is intended for non-interactive runs. Authentication, permissions, termination, and artifact capture still require CI configuration. In this case: Supported machine-readable CLI output and schema validation address parseability.
- **B:** Correct. The guide describes --output-format json and --json-schema for machine-parseable CI results. Verify the installed version and check execution status as well as payload. In this case: Supported machine-readable CLI output and schema validation address parseability.
- **C:** Incorrect for this question. Comparing the current diff with prior findings can reduce duplicate review comments. Preserve still-valid findings rather than simply suppressing all repeats. In this case: Supported machine-readable CLI output and schema validation address parseability.
- **D:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Supported machine-readable CLI output and schema validation address parseability.

### Question 59 — B

Answer: Provide existing tests and approved fixtures. Actual test files and conventions demonstrate the supported local testing environment. Relevant test context helps generation avoid duplicates and use valid repository conventions. Do not invent unavailable helper functions or external test data. Closest official exam-guide objective 3.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Actual test files and conventions demonstrate the supported local testing environment.
- **B:** Correct. Relevant test context helps generation avoid duplicates and use valid repository conventions. Do not invent unavailable helper functions or external test data. In this case: Actual test files and conventions demonstrate the supported local testing environment.
- **C:** Incorrect for this question. Comparing the current diff with prior findings can reduce duplicate review comments. Preserve still-valid findings rather than simply suppressing all repeats. In this case: Actual test files and conventions demonstrate the supported local testing environment.
- **D:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Actual test files and conventions demonstrate the supported local testing environment.

### Question 60 — B

Answer: Pass prior findings and request only new or unresolved issues. Current code and prior findings enable a meaningful new-versus-unresolved comparison. Comparing the current diff with prior findings can reduce duplicate review comments. Preserve still-valid findings rather than simply suppressing all repeats. Closest official exam-guide objective 3.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: Current code and prior findings enable a meaningful new-versus-unresolved comparison.
- **B:** Correct. Comparing the current diff with prior findings can reduce duplicate review comments. Preserve still-valid findings rather than simply suppressing all repeats. In this case: Current code and prior findings enable a meaningful new-versus-unresolved comparison.
- **C:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Current code and prior findings enable a meaningful new-versus-unresolved comparison.
- **D:** Incorrect for this question. Independent review reduces anchoring on the original solution. It still needs the specification, relevant code, and evidence; independence does not guarantee correctness. In this case: Current code and prior findings enable a meaningful new-versus-unresolved comparison.

### Question 61 — C

Answer: Inspect which instruction files are actually loaded. Inspect effective instruction loading and distinguish personal from shared project scope. The guide mentions /memory; current documentation also describes /context. Use the available inspection mechanism to diagnose scope and loading, not just the presence of a file. Closest official exam-guide objective 3.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Inspect effective instruction loading and distinguish personal from shared project scope.
- **B:** Incorrect for this question. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. In this case: Inspect effective instruction loading and distinguish personal from shared project scope.
- **C:** Correct. The guide mentions /memory; current documentation also describes /context. Use the available inspection mechanism to diagnose scope and loading, not just the presence of a file. In this case: Inspect effective instruction loading and distinguish personal from shared project scope.
- **D:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: Inspect effective instruction loading and distinguish personal from shared project scope.

### Question 62 — C

Answer: Create a differently named personal skill variant. A differently named personal variant avoids unintentionally changing team behavior. A personal variant can customize workflow without changing the shared skill for teammates. Distinct naming avoids accidental shadowing or confusion. Closest official exam-guide objective 3.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: A differently named personal variant avoids unintentionally changing team behavior.
- **B:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: A differently named personal variant avoids unintentionally changing team behavior.
- **C:** Correct. A personal variant can customize workflow without changing the shared skill for teammates. Distinct naming avoids accidental shadowing or confusion. In this case: A differently named personal variant avoids unintentionally changing team behavior.
- **D:** Incorrect for this question. The guide describes .claude/commands/ for shared invocable commands. User-scoped commands are personal; feature details depend on Claude Code version. In this case: A differently named personal variant avoids unintentionally changing team behavior.

### Question 63 — B

Answer: Scope a rule with YAML paths glob patterns. Path patterns match the intended handler files across subtrees. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. Closest official exam-guide objective 3.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Imports reference relevant supporting instruction files. Their actual loading and accessibility should be verified rather than assumed. In this case: Path patterns match the intended handler files across subtrees.
- **B:** Correct. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. In this case: Path patterns match the intended handler files across subtrees.
- **C:** Incorrect for this question. Topic-specific rule files reduce one oversized instruction document. Add path scoping when a rule is only relevant to selected files. In this case: Path patterns match the intended handler files across subtrees.
- **D:** Incorrect for this question. Local instructions fit conventions tied to a particular subtree. Cross-directory filename patterns may be better served by path-scoped rules. In this case: Path patterns match the intended handler files across subtrees.

### Question 64 — B

Answer: Use plan mode to investigate and compare approaches. Planning should establish constraints and alternatives before modifying dependent code. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. Closest official exam-guide objective 3.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. A narrow fix with known requirements may not need a long planning phase. Tests and review still apply. In this case: Planning should establish constraints and alternatives before modifying dependent code.
- **B:** Correct. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. In this case: Planning should establish constraints and alternatives before modifying dependent code.
- **C:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Planning should establish constraints and alternatives before modifying dependent code.
- **D:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Planning should establish constraints and alternatives before modifying dependent code.

### Question 65 — D

Answer: Use tests and specific failure feedback to drive iteration. Specific failing inputs, outputs, and tests guide a checkable correction. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. Closest official exam-guide objective 3.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Specific failing inputs, outputs, and tests guide a checkable correction.
- **B:** Incorrect for this question. When fixes influence one another, provide the combined constraints and failure evidence. Independent issues can be addressed separately. In this case: Specific failing inputs, outputs, and tests guide a checkable correction.
- **C:** Incorrect for this question. An interview-style clarification step surfaces unknown assumptions and constraints. Use it when uncertainty materially affects design. In this case: Specific failing inputs, outputs, and tests guide a checkable correction.
- **D:** Correct. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Specific failing inputs, outputs, and tests guide a checkable correction.

### Question 66 — C

Answer: Use an independent reviewer without the generator rationale. A fresh independent review should receive the specification and artifacts without the generator's anchoring rationale. Independent review reduces anchoring on the original solution. It still needs the specification, relevant code, and evidence; independence does not guarantee correctness. Closest official exam-guide objective 3.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Comparing the current diff with prior findings can reduce duplicate review comments. Preserve still-valid findings rather than simply suppressing all repeats. In this case: A fresh independent review should receive the specification and artifacts without the generator's anchoring rationale.
- **B:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: A fresh independent review should receive the specification and artifacts without the generator's anchoring rationale.
- **C:** Correct. Independent review reduces anchoring on the original solution. It still needs the specification, relevant code, and evidence; independence does not guarantee correctness. In this case: A fresh independent review should receive the specification and artifacts without the generator's anchoring rationale.
- **D:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: A fresh independent review should receive the specification and artifacts without the generator's anchoring rationale.

### Question 67 — C

Answer: Use @imports to keep instruction content modular. Import relevant maintained guidance rather than copy all potentially irrelevant material. Imports reference relevant supporting instruction files. Their actual loading and accessibility should be verified rather than assumed. Closest official exam-guide objective 3.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: Import relevant maintained guidance rather than copy all potentially irrelevant material.
- **B:** Incorrect for this question. The guide describes .claude/commands/ for shared invocable commands. User-scoped commands are personal; feature details depend on Claude Code version. In this case: Import relevant maintained guidance rather than copy all potentially irrelevant material.
- **C:** Correct. Imports reference relevant supporting instruction files. Their actual loading and accessibility should be verified rather than assumed. In this case: Import relevant maintained guidance rather than copy all potentially irrelevant material.
- **D:** Incorrect for this question. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. In this case: Import relevant maintained guidance rather than copy all potentially irrelevant material.

### Question 68 — B

Answer: Use context: fork for isolated skill execution. Forked conversational context does not itself create independent filesystem state. Where supported, an isolated skill context contains intermediate exploration. It does not automatically provide filesystem isolation or remove tool-permission obligations. Closest official exam-guide objective 3.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. A personal variant can customize workflow without changing the shared skill for teammates. Distinct naming avoids accidental shadowing or confusion. In this case: Forked conversational context does not itself create independent filesystem state.
- **B:** Correct. Where supported, an isolated skill context contains intermediate exploration. It does not automatically provide filesystem isolation or remove tool-permission obligations. In this case: Forked conversational context does not itself create independent filesystem state.
- **C:** Incorrect for this question. The guide covers allowed-tools to limit a skill workflow. Validate effective permissions; contextual instructions alone are not a sandbox. In this case: Forked conversational context does not itself create independent filesystem state.
- **D:** Incorrect for this question. Argument hints help users supply needed parameters. They do not replace actual argument validation or supply missing business facts. In this case: Forked conversational context does not itself create independent filesystem state.

### Question 69 — A

Answer: Explain interacting issues together before revising. Combined constraints are needed because the corrections influence one another. When fixes influence one another, provide the combined constraints and failure evidence. Independent issues can be addressed separately. Closest official exam-guide objective 3.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. When fixes influence one another, provide the combined constraints and failure evidence. Independent issues can be addressed separately. In this case: Combined constraints are needed because the corrections influence one another.
- **B:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Combined constraints are needed because the corrections influence one another.
- **C:** Incorrect for this question. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: Combined constraints are needed because the corrections influence one another.
- **D:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Combined constraints are needed because the corrections influence one another.

### Question 70 — D

Answer: State explicit reportable and non-reportable criteria. Explicit reportable and excluded categories address precision more directly than generic caution. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. Closest official exam-guide objective 3.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Independent review reduces anchoring on the original solution. It still needs the specification, relevant code, and evidence; independence does not guarantee correctness. In this case: Explicit reportable and excluded categories address precision more directly than generic caution.
- **B:** Incorrect for this question. Relevant test context helps generation avoid duplicates and use valid repository conventions. Do not invent unavailable helper functions or external test data. In this case: Explicit reportable and excluded categories address precision more directly than generic caution.
- **C:** Incorrect for this question. Comparing the current diff with prior findings can reduce duplicate review comments. Preserve still-valid findings rather than simply suppressing all repeats. In this case: Explicit reportable and excluded categories address precision more directly than generic caution.
- **D:** Correct. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Explicit reportable and excluded categories address precision more directly than generic caution.

### Question 71 — C

Answer: Use directory-scoped CLAUDE.md for a local package. Subdirectory instructions tie conventions to the relevant package rather than the user's identity. Local instructions fit conventions tied to a particular subtree. Cross-directory filename patterns may be better served by path-scoped rules. Closest official exam-guide objective 3.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Subdirectory instructions tie conventions to the relevant package rather than the user's identity.
- **B:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: Subdirectory instructions tie conventions to the relevant package rather than the user's identity.
- **C:** Correct. Local instructions fit conventions tied to a particular subtree. Cross-directory filename patterns may be better served by path-scoped rules. In this case: Subdirectory instructions tie conventions to the relevant package rather than the user's identity.
- **D:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: Subdirectory instructions tie conventions to the relevant package rather than the user's identity.

### Question 72 — D

Answer: Organize focused conventions in .claude/rules/. Focused rule files can be maintained by topic rather than one unstructured document. Topic-specific rule files reduce one oversized instruction document. Add path scoping when a rule is only relevant to selected files. Closest official exam-guide objective 3.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. The guide describes .claude/commands/ for shared invocable commands. User-scoped commands are personal; feature details depend on Claude Code version. In this case: Focused rule files can be maintained by topic rather than one unstructured document.
- **B:** Incorrect for this question. Imports reference relevant supporting instruction files. Their actual loading and accessibility should be verified rather than assumed. In this case: Focused rule files can be maintained by topic rather than one unstructured document.
- **C:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: Focused rule files can be maintained by topic rather than one unstructured document.
- **D:** Correct. Topic-specific rule files reduce one oversized instruction document. Add path scoping when a rule is only relevant to selected files. In this case: Focused rule files can be maintained by topic rather than one unstructured document.

### Question 73 — D

Answer: Put shared project standards in versioned CLAUDE.md. Shared repository standards belong in versioned project instructions. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. Closest official exam-guide objective 3.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: Shared repository standards belong in versioned project instructions.
- **B:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: Shared repository standards belong in versioned project instructions.
- **C:** Incorrect for this question. The guide describes .claude/commands/ for shared invocable commands. User-scoped commands are personal; feature details depend on Claude Code version. In this case: Shared repository standards belong in versioned project instructions.
- **D:** Correct. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Shared repository standards belong in versioned project instructions.

### Question 74 — A

Answer: Inspect which instruction files are actually loaded. Inspect actual loaded context instead of assuming a file anywhere on disk is active. The guide mentions /memory; current documentation also describes /context. Use the available inspection mechanism to diagnose scope and loading, not just the presence of a file. Closest official exam-guide objective 3.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. The guide mentions /memory; current documentation also describes /context. Use the available inspection mechanism to diagnose scope and loading, not just the presence of a file. In this case: Inspect actual loaded context instead of assuming a file anywhere on disk is active.
- **B:** Incorrect for this question. Imports reference relevant supporting instruction files. Their actual loading and accessibility should be verified rather than assumed. In this case: Inspect actual loaded context instead of assuming a file anywhere on disk is active.
- **C:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: Inspect actual loaded context instead of assuming a file anywhere on disk is active.
- **D:** Incorrect for this question. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. In this case: Inspect actual loaded context instead of assuming a file anywhere on disk is active.

### Question 75 — C

Answer: Use @imports to keep instruction content modular. Refer to a maintained shared source through appropriate imports instead of copying its text. Imports reference relevant supporting instruction files. Their actual loading and accessibility should be verified rather than assumed. Closest official exam-guide objective 3.1: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Refer to a maintained shared source through appropriate imports instead of copying its text.
- **B:** Incorrect for this question. Local instructions fit conventions tied to a particular subtree. Cross-directory filename patterns may be better served by path-scoped rules. In this case: Refer to a maintained shared source through appropriate imports instead of copying its text.
- **C:** Correct. Imports reference relevant supporting instruction files. Their actual loading and accessibility should be verified rather than assumed. In this case: Refer to a maintained shared source through appropriate imports instead of copying its text.
- **D:** Incorrect for this question. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. In this case: Refer to a maintained shared source through appropriate imports instead of copying its text.

### Question 76 — A

Answer: Put an on-demand workflow in a project skill. An on-demand skill avoids loading a long specialized procedure into every task. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. Closest official exam-guide objective 3.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: An on-demand skill avoids loading a long specialized procedure into every task.
- **B:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: An on-demand skill avoids loading a long specialized procedure into every task.
- **C:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: An on-demand skill avoids loading a long specialized procedure into every task.
- **D:** Incorrect for this question. Topic-specific rule files reduce one oversized instruction document. Add path scoping when a rule is only relevant to selected files. In this case: An on-demand skill avoids loading a long specialized procedure into every task.

### Question 77 — D

Answer: Use a project-scoped custom slash command. Project-scoped invocation files can be version-controlled with the team workflow. The guide describes .claude/commands/ for shared invocable commands. User-scoped commands are personal; feature details depend on Claude Code version. Closest official exam-guide objective 3.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Project-scoped invocation files can be version-controlled with the team workflow.
- **B:** Incorrect for this question. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. In this case: Project-scoped invocation files can be version-controlled with the team workflow.
- **C:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: Project-scoped invocation files can be version-controlled with the team workflow.
- **D:** Correct. The guide describes .claude/commands/ for shared invocable commands. User-scoped commands are personal; feature details depend on Claude Code version. In this case: Project-scoped invocation files can be version-controlled with the team workflow.

### Question 78 — D

Answer: Restrict skill tool access with supported frontmatter. Configure and verify supported tool restrictions appropriate to the skill's role. The guide covers allowed-tools to limit a skill workflow. Validate effective permissions; contextual instructions alone are not a sandbox. Closest official exam-guide objective 3.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Argument hints help users supply needed parameters. They do not replace actual argument validation or supply missing business facts. In this case: Configure and verify supported tool restrictions appropriate to the skill's role.
- **B:** Incorrect for this question. A personal variant can customize workflow without changing the shared skill for teammates. Distinct naming avoids accidental shadowing or confusion. In this case: Configure and verify supported tool restrictions appropriate to the skill's role.
- **C:** Incorrect for this question. Where supported, an isolated skill context contains intermediate exploration. It does not automatically provide filesystem isolation or remove tool-permission obligations. In this case: Configure and verify supported tool restrictions appropriate to the skill's role.
- **D:** Correct. The guide covers allowed-tools to limit a skill workflow. Validate effective permissions; contextual instructions alone are not a sandbox. In this case: Configure and verify supported tool restrictions appropriate to the skill's role.

### Question 79 — D

Answer: Provide argument-hint for invocation guidance. An argument hint improves discoverability, while validation still checks the actual supplied environment. Argument hints help users supply needed parameters. They do not replace actual argument validation or supply missing business facts. Closest official exam-guide objective 3.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. The guide covers allowed-tools to limit a skill workflow. Validate effective permissions; contextual instructions alone are not a sandbox. In this case: An argument hint improves discoverability, while validation still checks the actual supplied environment.
- **B:** Incorrect for this question. A personal variant can customize workflow without changing the shared skill for teammates. Distinct naming avoids accidental shadowing or confusion. In this case: An argument hint improves discoverability, while validation still checks the actual supplied environment.
- **C:** Incorrect for this question. Where supported, an isolated skill context contains intermediate exploration. It does not automatically provide filesystem isolation or remove tool-permission obligations. In this case: An argument hint improves discoverability, while validation still checks the actual supplied environment.
- **D:** Correct. Argument hints help users supply needed parameters. They do not replace actual argument validation or supply missing business facts. In this case: An argument hint improves discoverability, while validation still checks the actual supplied environment.

### Question 80 — C

Answer: Create a differently named personal skill variant. A distinct personal skill variant limits the experiment to that user. A personal variant can customize workflow without changing the shared skill for teammates. Distinct naming avoids accidental shadowing or confusion. Closest official exam-guide objective 3.2: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: A distinct personal skill variant limits the experiment to that user.
- **B:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: A distinct personal skill variant limits the experiment to that user.
- **C:** Correct. A personal variant can customize workflow without changing the shared skill for teammates. Distinct naming avoids accidental shadowing or confusion. In this case: A distinct personal skill variant limits the experiment to that user.
- **D:** Incorrect for this question. The guide describes .claude/commands/ for shared invocable commands. User-scoped commands are personal; feature details depend on Claude Code version. In this case: A distinct personal skill variant limits the experiment to that user.

### Question 81 — C

Answer: Scope a rule with YAML paths glob patterns. Add matching path conditions so test-specific guidance appears for relevant files. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. Closest official exam-guide objective 3.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: Add matching path conditions so test-specific guidance appears for relevant files.
- **B:** Incorrect for this question. Imports reference relevant supporting instruction files. Their actual loading and accessibility should be verified rather than assumed. In this case: Add matching path conditions so test-specific guidance appears for relevant files.
- **C:** Correct. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. In this case: Add matching path conditions so test-specific guidance appears for relevant files.
- **D:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Add matching path conditions so test-specific guidance appears for relevant files.

### Question 82 — A

Answer: Use directory-scoped CLAUDE.md for a local package. A local package instruction file is suitable when scope genuinely follows the directory. Local instructions fit conventions tied to a particular subtree. Cross-directory filename patterns may be better served by path-scoped rules. Closest official exam-guide objective 3.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. Local instructions fit conventions tied to a particular subtree. Cross-directory filename patterns may be better served by path-scoped rules. In this case: A local package instruction file is suitable when scope genuinely follows the directory.
- **B:** Incorrect for this question. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. In this case: A local package instruction file is suitable when scope genuinely follows the directory.
- **C:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: A local package instruction file is suitable when scope genuinely follows the directory.
- **D:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: A local package instruction file is suitable when scope genuinely follows the directory.

### Question 83 — B

Answer: Scope a rule with YAML paths glob patterns. A glob-based path condition can express the cross-directory filename role. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. Closest official exam-guide objective 3.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Imports reference relevant supporting instruction files. Their actual loading and accessibility should be verified rather than assumed. In this case: A glob-based path condition can express the cross-directory filename role.
- **B:** Correct. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. In this case: A glob-based path condition can express the cross-directory filename role.
- **C:** Incorrect for this question. The guide describes .claude/commands/ for shared invocable commands. User-scoped commands are personal; feature details depend on Claude Code version. In this case: A glob-based path condition can express the cross-directory filename role.
- **D:** Incorrect for this question. Local instructions fit conventions tied to a particular subtree. Cross-directory filename patterns may be better served by path-scoped rules. In this case: A glob-based path condition can express the cross-directory filename role.

### Question 84 — D

Answer: Inspect which instruction files are actually loaded. Verify the effective matching and loaded rules rather than stack contradictory workarounds. The guide mentions /memory; current documentation also describes /context. Use the available inspection mechanism to diagnose scope and loading, not just the presence of a file. Closest official exam-guide objective 3.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Path-scoped rules apply to matching work rather than every task. Globs can cover files with the same role across different directories. In this case: Verify the effective matching and loaded rules rather than stack contradictory workarounds.
- **B:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Verify the effective matching and loaded rules rather than stack contradictory workarounds.
- **C:** Incorrect for this question. User-level instructions apply to that user rather than automatically to everyone cloning the repository. Do not place shared team standards only here. In this case: Verify the effective matching and loaded rules rather than stack contradictory workarounds.
- **D:** Correct. The guide mentions /memory; current documentation also describes /context. Use the available inspection mechanism to diagnose scope and loading, not just the presence of a file. In this case: Verify the effective matching and loaded rules rather than stack contradictory workarounds.

### Question 85 — B

Answer: Organize focused conventions in .claude/rules/. Rule files provide topic organization without requiring every convention to become an invocable workflow. Topic-specific rule files reduce one oversized instruction document. Add path scoping when a rule is only relevant to selected files. Closest official exam-guide objective 3.3: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. A versioned .claude/skills/<name>/SKILL.md can package task-specific guidance. Keep universally relevant standards in project instructions rather than only in an optional skill. In this case: Rule files provide topic organization without requiring every convention to become an invocable workflow.
- **B:** Correct. Topic-specific rule files reduce one oversized instruction document. Add path scoping when a rule is only relevant to selected files. In this case: Rule files provide topic organization without requiring every convention to become an invocable workflow.
- **C:** Incorrect for this question. Imports reference relevant supporting instruction files. Their actual loading and accessibility should be verified rather than assumed. In this case: Rule files provide topic organization without requiring every convention to become an invocable workflow.
- **D:** Incorrect for this question. The guide describes .claude/commands/ for shared invocable commands. User-scoped commands are personal; feature details depend on Claude Code version. In this case: Rule files provide topic organization without requiring every convention to become an invocable workflow.

### Question 86 — B

Answer: Delegate focused exploration to a read-oriented subagent. A focused exploration worker can isolate discovery and return high-signal findings. Discovery can be isolated so verbose file output does not overwhelm the main conversation. Return useful findings and source pointers. Closest official exam-guide objective 3.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. A narrow fix with known requirements may not need a long planning phase. Tests and review still apply. In this case: A focused exploration worker can isolate discovery and return high-signal findings.
- **B:** Correct. Discovery can be isolated so verbose file output does not overwhelm the main conversation. Return useful findings and source pointers. In this case: A focused exploration worker can isolate discovery and return high-signal findings.
- **C:** Incorrect for this question. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. In this case: A focused exploration worker can isolate discovery and return high-signal findings.
- **D:** Incorrect for this question. An interview-style clarification step surfaces unknown assumptions and constraints. Use it when uncertainty materially affects design. In this case: A focused exploration worker can isolate discovery and return high-signal findings.

### Question 87 — A

Answer: Use plan mode to investigate and compare approaches. Architectural risk and unknowns justify investigation and planning before broad edits. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. Closest official exam-guide objective 3.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. In this case: Architectural risk and unknowns justify investigation and planning before broad edits.
- **B:** Incorrect for this question. A narrow fix with known requirements may not need a long planning phase. Tests and review still apply. In this case: Architectural risk and unknowns justify investigation and planning before broad edits.
- **C:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Architectural risk and unknowns justify investigation and planning before broad edits.
- **D:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Architectural risk and unknowns justify investigation and planning before broad edits.

### Question 88 — A

Answer: Implement a small well-understood change directly. A simple understood change can proceed directly with appropriate verification. A narrow fix with known requirements may not need a long planning phase. Tests and review still apply. Closest official exam-guide objective 3.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. A narrow fix with known requirements may not need a long planning phase. Tests and review still apply. In this case: A simple understood change can proceed directly with appropriate verification.
- **B:** Incorrect for this question. An interview-style clarification step surfaces unknown assumptions and constraints. Use it when uncertainty materially affects design. In this case: A simple understood change can proceed directly with appropriate verification.
- **C:** Incorrect for this question. Discovery can be isolated so verbose file output does not overwhelm the main conversation. Return useful findings and source pointers. In this case: A simple understood change can proceed directly with appropriate verification.
- **D:** Incorrect for this question. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. In this case: A simple understood change can proceed directly with appropriate verification.

### Question 89 — D

Answer: Ask targeted design questions before implementation. Ask the design-critical question instead of silently inventing a policy assumption. An interview-style clarification step surfaces unknown assumptions and constraints. Use it when uncertainty materially affects design. Closest official exam-guide objective 3.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. In this case: Ask the design-critical question instead of silently inventing a policy assumption.
- **B:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Ask the design-critical question instead of silently inventing a policy assumption.
- **C:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Ask the design-critical question instead of silently inventing a policy assumption.
- **D:** Correct. An interview-style clarification step surfaces unknown assumptions and constraints. Use it when uncertainty materially affects design. In this case: Ask the design-critical question instead of silently inventing a policy assumption.

### Question 90 — C

Answer: Use plan mode to investigate and compare approaches. Planning is appropriate when the deliverable is analysis before committing to one implementation. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. Closest official exam-guide objective 3.4: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Planning is appropriate when the deliverable is analysis before committing to one implementation.
- **B:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Planning is appropriate when the deliverable is analysis before committing to one implementation.
- **C:** Correct. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. In this case: Planning is appropriate when the deliverable is analysis before committing to one implementation.
- **D:** Incorrect for this question. A narrow fix with known requirements may not need a long planning phase. Tests and review still apply. In this case: Planning is appropriate when the deliverable is analysis before committing to one implementation.

### Question 91 — A

Answer: Provide concrete input–output examples. Concrete input-output examples distinguish normalization from information loss. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. Closest official exam-guide objective 3.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Concrete input-output examples distinguish normalization from information loss.
- **B:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Concrete input-output examples distinguish normalization from information loss.
- **C:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Concrete input-output examples distinguish normalization from information loss.
- **D:** Incorrect for this question. An interview-style clarification step surfaces unknown assumptions and constraints. Use it when uncertainty materially affects design. In this case: Concrete input-output examples distinguish normalization from information loss.

### Question 92 — B

Answer: Use tests and specific failure feedback to drive iteration. Regression tests must accompany specific failure feedback rather than replace old checks. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. Closest official exam-guide objective 3.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Regression tests must accompany specific failure feedback rather than replace old checks.
- **B:** Correct. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Regression tests must accompany specific failure feedback rather than replace old checks.
- **C:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Regression tests must accompany specific failure feedback rather than replace old checks.
- **D:** Incorrect for this question. An interview-style clarification step surfaces unknown assumptions and constraints. Use it when uncertainty materially affects design. In this case: Regression tests must accompany specific failure feedback rather than replace old checks.

### Question 93 — D

Answer: Explain interacting issues together before revising. Provide their combined expectations and interactions to guide one coherent correction. When fixes influence one another, provide the combined constraints and failure evidence. Independent issues can be addressed separately. Closest official exam-guide objective 3.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: Provide their combined expectations and interactions to guide one coherent correction.
- **B:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Provide their combined expectations and interactions to guide one coherent correction.
- **C:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Provide their combined expectations and interactions to guide one coherent correction.
- **D:** Correct. When fixes influence one another, provide the combined constraints and failure evidence. Independent issues can be addressed separately. In this case: Provide their combined expectations and interactions to guide one coherent correction.

### Question 94 — C

Answer: Ask targeted design questions before implementation. Targeted questions surface assumptions before an implementation commits to unsafe defaults. An interview-style clarification step surfaces unknown assumptions and constraints. Use it when uncertainty materially affects design. Closest official exam-guide objective 3.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Targeted questions surface assumptions before an implementation commits to unsafe defaults.
- **B:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Targeted questions surface assumptions before an implementation commits to unsafe defaults.
- **C:** Correct. An interview-style clarification step surfaces unknown assumptions and constraints. Use it when uncertainty materially affects design. In this case: Targeted questions surface assumptions before an implementation commits to unsafe defaults.
- **D:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Targeted questions surface assumptions before an implementation commits to unsafe defaults.

### Question 95 — B

Answer: Use tests and specific failure feedback to drive iteration. A checkable performance test or explicit acceptance check turns the requirement into actionable feedback. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. Closest official exam-guide objective 3.5: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: A checkable performance test or explicit acceptance check turns the requirement into actionable feedback.
- **B:** Correct. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: A checkable performance test or explicit acceptance check turns the requirement into actionable feedback.
- **C:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: A checkable performance test or explicit acceptance check turns the requirement into actionable feedback.
- **D:** Incorrect for this question. An interview-style clarification step surfaces unknown assumptions and constraints. Use it when uncertainty materially affects design. In this case: A checkable performance test or explicit acceptance check turns the requirement into actionable feedback.

### Question 96 — A

Answer: Run Claude Code in non-interactive print mode. Use a non-interactive mode while separately configuring credentials, permissions, and failure handling. The -p or --print mode is intended for non-interactive runs. Authentication, permissions, termination, and artifact capture still require CI configuration. Closest official exam-guide objective 3.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. The -p or --print mode is intended for non-interactive runs. Authentication, permissions, termination, and artifact capture still require CI configuration. In this case: Use a non-interactive mode while separately configuring credentials, permissions, and failure handling.
- **B:** Incorrect for this question. Planning fits uncertain architectural or multi-file changes before implementation. It is not evidence that a change has been executed or tested. In this case: Use a non-interactive mode while separately configuring credentials, permissions, and failure handling.
- **C:** Incorrect for this question. The guide describes --output-format json and --json-schema for machine-parseable CI results. Verify the installed version and check execution status as well as payload. In this case: Use a non-interactive mode while separately configuring credentials, permissions, and failure handling.
- **D:** Incorrect for this question. The guide describes .claude/commands/ for shared invocable commands. User-scoped commands are personal; feature details depend on Claude Code version. In this case: Use a non-interactive mode while separately configuring credentials, permissions, and failure handling.

### Question 97 — A

Answer: Use supported JSON output and schema CLI options. Machine-readable CLI output helps, but the caller must also inspect status and validate the payload. The guide describes --output-format json and --json-schema for machine-parseable CI results. Verify the installed version and check execution status as well as payload. Closest official exam-guide objective 3.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. The guide describes --output-format json and --json-schema for machine-parseable CI results. Verify the installed version and check execution status as well as payload. In this case: Machine-readable CLI output helps, but the caller must also inspect status and validate the payload.
- **B:** Incorrect for this question. Comparing the current diff with prior findings can reduce duplicate review comments. Preserve still-valid findings rather than simply suppressing all repeats. In this case: Machine-readable CLI output helps, but the caller must also inspect status and validate the payload.
- **C:** Incorrect for this question. The -p or --print mode is intended for non-interactive runs. Authentication, permissions, termination, and artifact capture still require CI configuration. In this case: Machine-readable CLI output helps, but the caller must also inspect status and validate the payload.
- **D:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: Machine-readable CLI output helps, but the caller must also inspect status and validate the payload.

### Question 98 — B

Answer: Pass prior findings and request only new or unresolved issues. Compare prior finding identity and current code rather than blindly deduplicate by old line number. Comparing the current diff with prior findings can reduce duplicate review comments. Preserve still-valid findings rather than simply suppressing all repeats. Closest official exam-guide objective 3.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Incorrect for this question. Independent review reduces anchoring on the original solution. It still needs the specification, relevant code, and evidence; independence does not guarantee correctness. In this case: Compare prior finding identity and current code rather than blindly deduplicate by old line number.
- **B:** Correct. Comparing the current diff with prior findings can reduce duplicate review comments. Preserve still-valid findings rather than simply suppressing all repeats. In this case: Compare prior finding identity and current code rather than blindly deduplicate by old line number.
- **C:** Incorrect for this question. Relevant test context helps generation avoid duplicates and use valid repository conventions. Do not invent unavailable helper functions or external test data. In this case: Compare prior finding identity and current code rather than blindly deduplicate by old line number.
- **D:** Incorrect for this question. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: Compare prior finding identity and current code rather than blindly deduplicate by old line number.

### Question 99 — A

Answer: Provide existing tests and approved fixtures. Existing tests and fixture conventions anchor generation in actual available infrastructure. Relevant test context helps generation avoid duplicates and use valid repository conventions. Do not invent unavailable helper functions or external test data. Closest official exam-guide objective 3.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. Relevant test context helps generation avoid duplicates and use valid repository conventions. Do not invent unavailable helper functions or external test data. In this case: Existing tests and fixture conventions anchor generation in actual available infrastructure.
- **B:** Incorrect for this question. Root CLAUDE.md or .claude/CLAUDE.md can distribute project instructions to teammates. These are contextual guidance, not a hard security policy. In this case: Existing tests and fixture conventions anchor generation in actual available infrastructure.
- **C:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Existing tests and fixture conventions anchor generation in actual available infrastructure.
- **D:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Existing tests and fixture conventions anchor generation in actual available infrastructure.

### Question 100 — A

Answer: Use an independent reviewer without the generator rationale. A separate reviewer can assess the artifact against requirements without inheriting the generator rationale. Independent review reduces anchoring on the original solution. It still needs the specification, relevant code, and evidence; independence does not guarantee correctness. Closest official exam-guide objective 3.6: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://code.claude.com/docs/en/memory

- **A:** Correct. Independent review reduces anchoring on the original solution. It still needs the specification, relevant code, and evidence; independence does not guarantee correctness. In this case: A separate reviewer can assess the artifact against requirements without inheriting the generator rationale.
- **B:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: A separate reviewer can assess the artifact against requirements without inheriting the generator rationale.
- **C:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: A separate reviewer can assess the artifact against requirements without inheriting the generator rationale.
- **D:** Incorrect for this question. Comparing the current diff with prior findings can reduce duplicate review comments. Preserve still-valid findings rather than simply suppressing all repeats. In this case: A separate reviewer can assess the artifact against requirements without inheriting the generator rationale.
