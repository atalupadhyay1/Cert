# CCAR-F — Curriculum and study plan

| Test | Focus | Questions |
|---|---|---:|
| 1 | Agentic Architecture & Orchestration | 100 |
| 2 | Tool Design & MCP Integration | 100 |
| 3 | Claude Code Configuration & Workflows | 100 |
| 4 | Prompt Engineering & Structured Output | 100 |
| 5 | Context Management & Reliability | 100 |
| 6 | Integrated Architecture Scenarios & Final Review | 100 |

## What each test develops

1. **Architecture:** protocol-based agent loops, client-tool observations, coordinator decisions, isolated subagent context, prerequisite gates, action approval, hooks, decomposition, resumption, and forking.
2. **Tools and MCP:** distinct contracts, input schemas, error classes, role-appropriate tools, tool choice, shared versus personal server configuration, secret references, resources, discovery, and Read/Edit/Write/Bash/Grep/Glob choices.
3. **Claude Code:** shared versus personal instruction scope, modular instructions, path rules, commands and skills, forked execution, planning versus direct edits, test-driven refinement, and non-interactive CI review.
4. **Prompts and output:** explicit review criteria, representative examples and valid negatives, strict supported output schemas, semantic validation, missing values, bounded correction, batch processing, and independent multi-pass review.
5. **Reliability:** exact facts, relevant history, tool-output trimming, context budgeting, escalation, ambiguity, structured errors, durable exploration notes, crash recovery, confidence calibration, segmented accuracy, and provenance.
6. **Integrated review:** mixed-domain architecture trade-offs and failure diagnosis. Counts are 27/18/20/20/15; the test is longer and simpler in response format than the official exam.

## Suggested three-week progression

- **Week 1:** Read the current official guide. Complete Tests 1 and 2; explain the difference between protocol completion, business success, tool selection, and authorization. Practice identifying retryable versus non-retryable outcomes.
- **Week 2:** Complete Tests 3 and 4. Map configuration scope and check your understanding of schemas versus meaning. Explain how review criteria, validation feedback, and independent context improve results.
- **Week 3:** Complete Test 5, repair gaps, then attempt Test 6 without notes if useful. Review low-confidence correct guesses as carefully as errors. Compare your remaining gaps with the entire official outline.

Optional timing: **200 minutes per 100-question test**. Optional practice target: **80%**. These are learning settings, not official passing-score conversions.

## Error log

| Test / item | Domain / objective | Decisive requirement | Why my choice fails | Source / fresh example |
|---|---|---|---|---|
| | | | | |

Useful error categories: confused stop reason, missing observation, stale context, wrong instruction scope, unbounded retry, absent evidence, schema-versus-meaning confusion, misplaced trust, or unsupported confidence.

## Optional practical reinforcement

These are suggestions, not included provisioned labs: trace a tool-use conversation; inspect a small project's instructions and rules; design one MCP error contract; validate a structured extraction; outline recovery from a worker interruption. Never use real secrets or sensitive data in exercises. Check version-appropriate documentation before running commands or SDK examples.

## Format limitations

These are independent learning tests, not actual or recalled exam questions. Tests 1–5 are domain deep dives; Test 6 is an expanded mixed-domain review with 27/18/20/20/15 questions. The overall 600-question package is deliberately not weighted like one exam.

The retrieved July 2026 v1.0 guide lists **60 items, 120 minutes, multiple-choice and multiple-response**, with four scenarios drawn from six published scenario themes. The passing score is **720 on a 100–1,000 scaled scale**, not a published raw 72% threshold. This package instead has 100 questions per test, all **single-answer with four options**. Its mini-scenarios do not reproduce the official four-of-six scenario structure. Optional **200 minutes and an 80% study target** are custom guidance, not official timing, scaled-score equivalents, or a passing guarantee.

Repeated concepts can improve learning but can also inflate repeated-attempt scores. No identical difficulty or predictive readiness guarantee is made.

## References

- [Official certification portal](https://anthropic-partners.skilljar.com/claude-certified-architect-foundations-certification)
- [Official CCAR-F exam guide, v1.0 effective July 2026](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf)
- [Agent SDK subagents](https://code.claude.com/docs/en/agent-sdk/subagents)
- [Claude API tool definitions](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)
- [Claude Code project memory and rules](https://code.claude.com/docs/en/memory)
