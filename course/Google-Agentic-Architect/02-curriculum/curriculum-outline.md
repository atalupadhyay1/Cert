# PAA curriculum and study strategy

Baseline: the current official English Professional Agentic Architect exam guide (five sections; 13/17/33/22/15). The beta multiple-choice window ran September 8–30, 2026 and is closed. Google says general availability opens in mid-November 2026, with a 2-hour proctored session and the same two-part structure. The GA exam guide and format may change; this package makes no claim about an unpublished future blueprint.

## Course settings

- Six practice tests, 100 single-answer questions each; four alternatives per question.
- Optional custom duration: 180 minutes per test; optional study target: 80%.
- Read explanations after a first attempt; keep a mistake log by local study area.
- The real exam is a proctored multiple-choice test plus separate hands-on labs. This package does not simulate the labs, Pearson delivery, or the official item count.

## Sequence and learning goals

### Test 1: Low-Code Agents and Coding Agents

Configure state-based low-code workflows, instructions, enterprise data connections, and safe fallbacks. Then configure coding agents with MCP servers, skills, hooks, rules, subagents, secure sandboxes, and controlled code changes.

Allocation: Building Agents Using Low-Code Tools: 50; Using Coding Agents for Application Development: 50.

[Instructor CSV](../03-practice-sets/set-1/practice-set-1.csv) · [Offline questions and explanations](../03-practice-sets/set-1/practice-set-1.md)

Review task: draw one low-code flow and one coding-agent flow, marking where authorization, sandboxing, and human approval are enforced outside the prompt.

### Test 2: Custom Agents — Models, ADK, Memory, RAG, and Retrieval

Choose models using cost, latency, control, and security requirements. Build with ADK, manage sessions, state, memory, and artifacts, design RAG pipelines, and operate managed retrieval with authorization-aware evidence.

Allocation: Developing Custom Agents: 100.

[Instructor CSV](../03-practice-sets/set-2/practice-set-2.csv) · [Offline questions and explanations](../03-practice-sets/set-2/practice-set-2.md)

Review task: design a retrieval path for one real corpus and document chunking, embeddings, filters, grounding, and freshness checks.

### Test 3: Custom Agents — Identity, Orchestration, and Registry

Apply agent identity, principal access boundaries, registry and MCP capability integration, A2A interoperability, multi-agent patterns, and runtime coordination.

Allocation: Developing Custom Agents: 100.

[Instructor CSV](../03-practice-sets/set-3/practice-set-3.csv) · [Offline questions and explanations](../03-practice-sets/set-3/practice-set-3.md)

Review task: take one multi-agent workflow and write the identity, delegation, failure, and escalation contract for every hop.

### Test 4: Evaluating and Deploying Agentic Workflows

Build golden and edge-case test sets, evaluate responses and trajectories, run continuous evaluation, select Agent Runtime, Cloud Run, or GKE, and troubleshoot drift, loops, latency, and cost.

Allocation: Evaluating and Deploying Agentic Workflows: 100.

[Instructor CSV](../03-practice-sets/set-4/practice-set-4.csv) · [Offline questions and explanations](../03-practice-sets/set-4/practice-set-4.md)

Review task: define release gates for quality, safety, latency, and cost, then explain the rollback path.

### Test 5: Securing and Governing Agentic Workflows

Apply OAuth-based tool access, principal access boundaries, Agent Gateway traffic control, registry and Model Armor policy, human-in-the-loop guardrails, and secure data handling.

Allocation: Securing and Governing Agentic Workflows: 100.

[Instructor CSV](../03-practice-sets/set-5/practice-set-5.csv) · [Offline questions and explanations](../03-practice-sets/set-5/practice-set-5.md)

Review task: write a threat model for one agent, covering prompt injection, identity, egress, data minimization, and approval.

### Test 6: Integrated Architect Scenarios and Final Review

Apply all five published sections in an expanded mixed review: 13 low-code, 17 coding agents, 33 custom agents, 22 evaluation/deployment, and 15 security/governance questions.

Allocation: Section 1: 13; Section 2: 17; Section 3: 33; Section 4: 22; Section 5: 15.

[Instructor CSV](../03-practice-sets/set-6/practice-set-6.csv) · [Offline questions and explanations](../03-practice-sets/set-6/practice-set-6.md)

Review task: attempt the set closed-book, then classify each miss as design, evidence, security, or operations error and schedule a focused retry.

## Study cadence

1. **Diagnose:** take one focused test and log uncertain correct answers as well as misses.
2. **Repair:** revisit the mapped guide objective and the current official documentation.
3. **Build:** implement a small agent path in an approved sandbox or project.
4. **Evaluate:** create representative cases and measure response and trajectory quality.
5. **Secure:** threat-model the tool paths and verify enforcement in code and platform policy.
6. **Refresh:** check the current exam guide and GA details before scheduling.

## Coverage boundary

The package maps every local study area to a published guide section, but does not claim equal depth in every consideration, calibrated difficulty, psychometric equivalence, or that a practice score predicts the official result. Numeric IDs are local study aids; the official guide does not use this numbering.
