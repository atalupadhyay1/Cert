# AI-500 — Curriculum and study strategy

## Six mixed-domain practice tests

| Test | Display title | Questions | Suggested custom duration |
|---|---|---:|---:|
| 1 | AI-500 Multi-Agent AI Solutions — Practice Test 1 | 100 | 180 minutes |
| 2 | AI-500 Multi-Agent AI Solutions — Practice Test 2 | 100 | 180 minutes |
| 3 | AI-500 Multi-Agent AI Solutions — Practice Test 3 | 100 | 180 minutes |
| 4 | AI-500 Multi-Agent AI Solutions — Practice Test 4 | 100 | 180 minutes |
| 5 | AI-500 Multi-Agent AI Solutions — Practice Test 5 | 100 | 180 minutes |
| 6 | AI-500 Multi-Agent AI Solutions — Practice Test 6 | 100 | 180 minutes |

Each set uses 18 architecture, 33 development, 24 evaluation/monitoring, and 25 security/deployment questions. This is one valid allocation within the official ranges, not an assertion about exact real-exam question counts. The sets are balanced learning exercises, not domain-specific deep dives or calibrated difficulty levels.

## Learner prerequisites

Experience with Python, Azure services, AI applications, Microsoft Foundry, agent orchestration, MCP, RAG, and related frameworks is recommended. The official AI-500 audience is expert-level. This package does not replace practical implementation work.

## Scoring and pacing

- Single-answer questions require one correct selection.
- Select-two questions require both correct selections and no other selection for credit.
- Suggested practice target: **80%**, not a Microsoft scaled-score conversion or passing guarantee.
- Suggested **180 minutes** is a course setting for 100 practice questions, not the official exam duration.
- Core concepts recur across the sets. Repeated scores are not statistically independent readiness estimates.

## Three-week study plan

### Week 1 — Architecture and implementation

1. Read the official study guide and take Set 1 without notes.
2. Review agent roles, autonomy, orchestration, state tiers, identities, and communication boundaries.
3. Implement or sketch a bounded tool wrapper with validation, idempotency, and timeouts.
4. Review prompt/context strategies, retrieval, and memory governance, then take Set 2.

### Week 2 — Evaluation and operations

1. Review human evaluation, retrieval precision, groundedness, and tool-outcome checks.
2. Study context-loss modes, quotas, traces, latency, and cost attribution.
3. Take Set 3 and explain missed distinctions using fresh examples.
4. Review identity, OAuth, secrets, layered guardrails, and failure recovery, then take Set 4.

### Week 3 — Production readiness

1. Practice deployment and rollback decisions: DTAP, canary, blue/green, compatibility, and CI/CD gates.
2. Take Set 5 and investigate low-confidence answers.
3. Revisit the four official learning paths and selected practical exercises.
4. Take Set 6, then review the complete official objectives for gaps not exhaustively covered by the question bank.

## Error log

| Test / Q | Skill area | Why my choice failed | Requirement I missed | Correct distinguishing rule | Reference / practical check |
|---|---|---|---|---|---|
| | | | | | |

Categories: dependency mistake, protocol confusion, trust-boundary error, state inconsistency, missing validation, quota assumption, quality/availability confusion, or release incompatibility.

## Official references

- https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-500
- https://learn.microsoft.com/en-us/credentials/certifications/exams/ai-500/
