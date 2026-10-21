# CCAR-F — Sources, coverage, and editorial boundaries

## Primary research

Retrieved October 21, 2026:

1. **Official Anthropic Academy certification portal:** https://anthropic-partners.skilljar.com/claude-certified-architect-foundations-certification. Retrieved the page identifying CCAR-F domains, format, scaled scoring, and the linked exam guide. Do not infer eligibility, discounts, or universal registration availability from this package.
2. **Official linked exam guide:** https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542750/Claude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf. Version 1.0, effective July 2026. Retrieved chunks 0–6, covering format, blueprint, all detailed task statements, and preparation exercises. The tail of chunk 6 begins the public samples; those samples were not used as source questions or rewritten into this bank. Remaining sample chunks were not retrieved.
3. **Current SDK subagent documentation:** https://code.claude.com/docs/en/agent-sdk/subagents. Retrieved the initial section describing programmatic definitions, the current Agent launcher, isolated contexts, parallelism, and role-specific tools. Not every SDK reference or fork behavior was implementation-tested.
4. **Claude API tool definitions:** https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools. Retrieved the initial section on tool fields, input schemas, descriptive boundaries, examples, and high-signal observations. Not every linked schema, batch, or error API reference was retrieved.
5. **Claude Code memory:** https://code.claude.com/docs/en/memory. Retrieved the initial section on instruction scope, shared versus personal files, on-demand subdirectory context, and the fact that instructions are guidance rather than enforced security configuration.

An attempted generic anthropic.com certification URL returned 404; the working official Academy portal above replaces it. Third-party search results helped locate primary sources, but competitor question banks were not used for authoring.

## Organization and descriptive counts

| Test | Focus | Questions |
|---|---|---:|
| 1 | Agentic Architecture & Orchestration | 100 |
| 2 | Tool Design & MCP Integration | 100 |
| 3 | Claude Code Configuration & Workflows | 100 |
| 4 | Prompt Engineering & Structured Output | 100 |
| 5 | Context Management & Reliability | 100 |
| 6 | Integrated Architecture Scenarios & Final Review | 100 |

| Official domain | Approximate exam weight | Tests 1–5 | Test 6 | Package total |
|---|---:|---:|---:|---:|
| Agentic Architecture & Orchestration | 27% | 100 | 27 | 127 |
| Tool Design & MCP Integration | 18% | 100 | 18 | 118 |
| Claude Code Configuration & Workflows | 20% | 100 | 20 | 120 |
| Prompt Engineering & Structured Output | 20% | 100 | 20 | 120 |
| Context Management & Reliability | 15% | 100 | 15 | 115 |

These are independent learning tests, not actual or recalled exam questions. Tests 1–5 are domain deep dives; Test 6 is an expanded mixed-domain review with 27/18/20/20/15 questions. The overall 600-question package is deliberately not weighted like one exam.


## Objective coverage

- **1.1–1.7:** loops; coordination; invocation/context; prerequisites and handoff; hooks; decomposition; sessions.
- **2.1–2.5:** contracts; structured errors; distribution/tool choice; MCP integration; built-in tools.
- **3.1–3.6:** instruction hierarchy; commands/skills; path rules; planning; refinement; CI.
- **4.1–4.6:** explicit criteria; demonstrations; schemas; validation; batches; independent/multi-pass review.
- **5.1–5.6:** conversation context; escalation; error propagation; codebase context; review/calibration; provenance.

Every delivered item carries one closest guide task anchor and broad technical-reference link. These are further-study references, not a claim that a single linked paragraph proves every supplementary reliability detail. Durable idempotency, least privilege, race-safe action checks, and operational recovery extend the task statements using ordinary production-engineering reasoning.

## Version differences and careful interpretations

- The July guide calls the launcher **Task**. Current SDK documentation uses **Agent**. Questions either address the conceptual launcher or explicitly name the version difference; do not combine identifiers without checking your installed SDK.
- Fresh subagent contexts should receive relevant evidence explicitly. Newer fork or persistent-memory features may have different inheritance semantics; this bank does not claim every invocation starts with literally no inherited information.
- The guide discusses **/memory**; current memory documentation also describes **/context** for inspecting loaded files. Questions ask for effective instruction inspection rather than assert a command exists in every release.
- CLAUDE.md and skill instructions guide behavior; they are not a hard authorization boundary. Allowed tools, hooks, runtime permissions, server-side checks, and sandboxes have distinct roles. A forked conversation is not automatically an isolated filesystem.
- Tool choice controls selection, not permission. Ordinary tool_use plus a schema should not be treated as universal guaranteed structural compliance. Use supported strict schema mechanisms and handle compatibility, refusals, truncation, and execution status.
- Schema validity does not establish source correctness, authorized identity, correct totals, or factual truth. A required nullable key and an optional key mean different things.
- Post-tool normalization cannot block an already executed side effect. Local cancellation or network timeout does not prove remote rollback. Idempotency requires durable logical-action handling in a supporting system.
- Prefix caching is not answer verification, permanent learning, or a larger context window. Context overflow and token accounting are service-specific.
- The guide describes a **50% batch discount and processing window up to 24 hours**, explicitly without a guaranteed latency SLA. Arithmetic items label prices and planning bounds as illustrative assumptions, not current provider prices or guaranteed delivery.
- Self-reported confidence needs representative labeled calibration. Aggregate accuracy and independent reviewers are not complete correctness or safety guarantees.

## Originality and repetition

The source has **600 individually authored rows**, not six rewordings generated from a shared 100-stem template. Four option keys are authored with the best answer first, then deterministically shuffled at export. Shared conceptual definitions and some case distinctions intentionally recur. Exact normalized stem uniqueness is checked; semantic independence is not claimed.

No copied commercial questions, actual/recalled exam items, or rewritten public sample questions are included. The test themes follow the published domains, not confidential exam disclosures.

## Official format versus package

The retrieved July 2026 v1.0 guide lists **60 items, 120 minutes, multiple-choice and multiple-response**, with four scenarios drawn from six published scenario themes. The passing score is **720 on a 100–1,000 scaled scale**, not a published raw 72% threshold. This package instead has 100 questions per test, all **single-answer with four options**. Its mini-scenarios do not reproduce the official four-of-six scenario structure. Optional **200 minutes and an 80% study target** are custom guidance, not official timing, scaled-score equivalents, or a passing guarantee.


## Review still required

Automated checks verify source/key parity, formats, counts, normalized wording uniqueness, blueprint counts for Test 6, arithmetic expectations, Markdown/manifest parity, and archive reproducibility. They do not independently certify factual accuracy, eliminate every ambiguous distractor, calibrate difficulty, continuously verify live links, execute SDK examples, or import into a Udemy account.

Before publication, review every question and distractor, current program details, version-sensitive product claims, source URLs, and all six imports. No platform publication or certification guarantee is claimed.
