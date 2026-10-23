# CCDV-F official sources, version boundary, and coverage

## Baseline and change notice

Baseline: official Exam Guide v1.0, effective July 2026; reviewed October 21, 2026. The portal announces an exam update on December 7, 2026, with an updated guide due November 17, 2026. This package does not claim coverage of the unpublished update. Recheck and revise before using it for that exam version.

- Primary program source: [official certification portal](https://anthropic-partners.skilljar.com/claude-certified-developer-foundations-certification).
- Primary scope source: [Claude Certified Developer – Foundations Exam Guide](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf), **v1.0, effective July 2026**.
- Portal and guide reviewed October 21, 2026. No future guide or future-domain content is asserted.
- The July 2026 guide lists 53 items in 120 minutes, including multiple-choice and multiple-response items; each multiple-response item specifies how many selections are required. The passing score is 720 on a 100–1000 scaled range, not a raw percentage conversion. The listed exam fee is $125, validity is 12 months, and there are no mandatory prerequisites. Confirm current program terms before registration.
- Recommended background in the guide includes roughly 1–5 years of software engineering, six months with Claude or comparable LLMs, and Python/TypeScript, REST, and CLI familiarity. Recommendations are not mandatory prerequisites.

## Official domains and actual package allocation

| Official domain | Guide weight | Tests 1–5 | Test 6 | Package total |
|---|---:|---:|---:|---:|
| 1. Agents and Workflows | 14.7% | 50 | 15 | 65 |
| 2. Applications and Integration | 33.1% | 100 | 33 | 133 |
| 3. Claude Code | 3.1% | 25 | 3 | 28 |
| 4. Eval, Testing, and Debugging | 2.6% | 25 | 3 | 28 |
| 5. Model Selection and Optimization | 16.8% | 100 | 17 | 117 |
| 6. Prompt and Context Engineering | 11.0% | 100 | 11 | 111 |
| 7. Security and Safety | 8.1% | 50 | 8 | 58 |
| 8. Tools and MCPs | 10.6% | 50 | 10 | 60 |

Only Test 6 approximates official weights. It expands to 100 items and uses largest-remainder-style integer allocation, resolving the equal remainder between debugging and tools/MCP in favor of debugging. The focused tests and aggregate intentionally differ.

## All 25 named skills

The guide names skills; **1.1, 2.1, and other numeric skill identifiers are local study-map IDs**, not official numbering. Counts are generated from authored records. Mapping establishes closest subject coverage, not equal depth across every bullet or expert certification of each item's difficulty.

| Local ID (not official) | Named guide skill | Items | Appears in tests |
|---|---|---:|---|
| 1.1 | Agent Architecture | 25 | 2, 6 |
| 1.2 | Agent Construction with Claude | 20 | 2, 6 |
| 1.3 | Agent Patterns and Frameworks | 20 | 2, 6 |
| 2.1 | Understanding Requirements | 16 | 1, 6 |
| 2.2 | Systems Life Cycle | 16 | 1, 6 |
| 2.3 | Claude API Mechanics | 42 | 1, 6 |
| 2.4 | Software Engineering Foundations | 27 | 1, 6 |
| 2.5 | Claude Application Design | 17 | 1, 6 |
| 2.6 | Configuration Management | 15 | 1, 6 |
| 3.1 | Claude Code Operation | 28 | 5, 6 |
| 4.1 | Debugging and Error Handling | 28 | 5, 6 |
| 5.1 | LLM Fundamentals | 28 | 3, 6 |
| 5.2 | Technical Fundamentals | 28 | 3, 6 |
| 5.3 | Model Selection and Tradeoffs | 33 | 3, 6 |
| 5.4 | Cost and Token Management | 28 | 3, 6 |
| 6.1 | Context Engineering | 34 | 4, 6 |
| 6.2 | Prompt Engineering | 34 | 4, 6 |
| 6.3 | Output Handling | 43 | 4, 6 |
| 7.1 | AI Application Security | 22 | 5, 6 |
| 7.2 | Guardrails and Safe Deployment | 12 | 5, 6 |
| 7.3 | Claude Hooks | 12 | 5, 6 |
| 7.4 | Identity, Secrets, and Key Management | 12 | 5, 6 |
| 8.1 | Tool Implementation | 24 | 2, 6 |
| 8.2 | MCP Server Development | 18 | 2, 6 |
| 8.3 | Agentic Customization | 18 | 2, 6 |

## Technical references and evidence limits

The July guide establishes exam scope. Additional implementation patterns are educational enrichment and ordinary software-engineering practice; a guide link in an explanation does not claim that every detail appears verbatim there.

Directly reviewed during this package's research:

- [Messages API](https://platform.claude.com/docs/en/api/messages): typed content and Messages/token-count mechanics; retrieved introductory/type sections, not every endpoint detail.
- [Streaming](https://platform.claude.com/docs/en/build-with-claude/streaming): SSE event lifecycle, partial deltas, post-start errors, and SDK accumulation.
- [Claude Code settings](https://code.claude.com/docs/en/settings): user, shared project, local, and managed configuration scopes and permissions.

Further-study reference anchors (not a claim of comprehensive retrieval or continuous URL verification):

- Agents and Workflows: https://code.claude.com/docs/en/agent-sdk/overview
- Applications and Integration: https://platform.claude.com/docs/en/api/messages
- Claude Code: https://code.claude.com/docs/en/settings
- Eval, Testing, and Debugging: https://platform.claude.com/docs/en/build-with-claude/streaming
- Model Selection and Optimization: https://platform.claude.com/docs/en/about-claude/models/overview
- Prompt and Context Engineering: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview
- Security and Safety: https://code.claude.com/docs/en/security
- Tools and MCPs: https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools
- Claude Code memory and rules: https://code.claude.com/docs/en/memory
- Agent SDK subagents: https://code.claude.com/docs/en/agent-sdk/subagents

Some supplementary anchors were previously reviewed for the Architect course; that is not an exhaustive Developer-specific live documentation audit. Verify the installed SDK, provider, model, and account contract before implementation.

## Version-sensitive and safety distinctions

- **Agent** versus legacy **Task** launcher identifiers depend on installed SDK versions. This note does not assign legacy names to the Developer guide without a direct guide quotation.
- Claude Code shared project settings use `.claude/settings.json`; personal project settings use `.claude/settings.local.json`. Ensure manually created local files are ignored. User settings and managed policies have different scope; cloud sessions do not necessarily read every local preference.
- `CLAUDE.md` gives contextual guidance, not hard authorization. Settings, supported permission controls, and trusted code must enforce mandatory constraints. Inspect effective configuration and instruction loading rather than rely on file existence.
- Skill `allowed-tools` declarations can influence pre-approval. Do not infer a complete deny-all-other-tools sandbox from that field alone; verify actual execution permissions and isolation.
- Standard Messages streaming is **SSE**, not WebSocket. Track block indexes and accumulate partial tool JSON; do not execute fragments. Initial HTTP 200 is not final stream success.
- Schema validity does not establish semantic truth, evidence support, authorization, or safe rendering/execution. Refusal, truncation, and transport failures still need handling.
- Pre-tool enforcement can block an effect; **Post-tool normalization** only changes subsequent observations and cannot prevent an already executed side effect.
- Model-family positioning is an evaluation starting point, not a universal benchmark. Supported identifiers, context limits, fast mode, thinking, effort, cache rules, feature combinations, and retirement dates vary.
- Checkpointing, conversation forks, local timeouts, and cancellation do not automatically isolate or roll back remote effects.
- No fixed-weights claim proves prompts are never stored. Data terms depend on the actual service, provider, plan, and settings.
- Numerical cost and capacity exercises use hypothetical or explicitly case-stated assumptions, not current provider prices or guaranteed delivery. Test 3 exercises calculate $1.80, 11,000 evidence tokens, A at $0.025 versus B at $0.03 per accepted result, and 60% cache-read share. That share is not automatically 60% monetary savings.

## Authorship, explanation design, and QA limits

All 600 source stems and case rationales are original educational content. Official sample questions and commercial banks were not copied or lightly rewritten into this bank. Short concept checks and scenario variations intentionally revisit concepts. The option registry supplies explanatory definitions; every option explanation also includes the case rationale. This is feedback for the decision, not a claim that each question tests an unrelated concept.

Source validation checks counts, skill and domain allocations, option keys, rationale presence, and normalized duplicate wording. Export validation verifies the 17-column contract, four unique options, one key, explanations, references, exact source parity, and balanced answer positions. Artifact checks verify readable copies, the answer manifest, and report freshness.

These checks do not constitute independent factual certification, exhaustive semantic duplicate detection, psychometric calibration, live provider execution, accessibility certification, continuous source-link verification, or Udemy account import/publication. An instructor should perform final expert editorial review and platform preview. No passing guarantee or affiliation is implied.
