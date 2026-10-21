# CCDV-F curriculum and study strategy

Baseline: official Exam Guide v1.0, effective July 2026; reviewed October 21, 2026. The portal announces an exam update on December 7, 2026, with an updated guide due November 17, 2026. This package does not claim coverage of the unpublished update. Recheck and revise before using it for that exam version.

## Course settings

- Six practice tests, 100 single-answer questions each; four alternatives per question.
- Optional custom duration: 200 minutes per test; optional study target: 80%.
- Read explanations after a first attempt; keep a mistake and uncertainty log.
- The actual exam has 53 items in 120 minutes with multiple-choice and multiple-response items. These tests deliberately do not simulate that full format.

## Sequence and learning goals

### Test 1: Applications and Integration

Translate requirements into acceptance criteria; manage lifecycle, Messages requests, streaming, provider differences, async integration, safe retries, application boundaries, and configuration.

Allocation: Applications and Integration: 100.

[Instructor CSV](../03-practice-sets/set-1/practice-set-1.csv) · [Offline questions and explanations](../03-practice-sets/set-1/practice-set-1.md)

Review task: explain the deciding requirement for three missed or uncertain items, then create a new safe example that changes the best answer by changing one constraint.

### Test 2: Agents, Workflows, Tools and MCPs

Compare workflows and agents, coordinate specialists, manage hooks and durable state, design tool contracts, handle tool errors, distinguish MCP primitives and transports, and choose customization approaches.

Allocation: Agents and Workflows: 50, Tools and MCPs: 50.

[Instructor CSV](../03-practice-sets/set-2/practice-set-2.csv) · [Offline questions and explanations](../03-practice-sets/set-2/practice-set-2.md)

Review task: explain the deciding requirement for three missed or uncertain items, then create a new safe example that changes the best answer by changing one constraint.

### Test 3: Model Selection and Optimization

Study tokenization, probabilistic generation, prompting fundamentals, supported reasoning and fast-mode controls, API/SDK mechanics, model-family trade-offs, retirement, caching, usage, and cost per accepted outcome.

Allocation: Model Selection and Optimization: 100.

[Instructor CSV](../03-practice-sets/set-3/practice-set-3.csv) · [Offline questions and explanations](../03-practice-sets/set-3/practice-set-3.md)

Review task: explain the deciding requirement for three missed or uncertain items, then create a new safe example that changes the best answer by changing one constraint.

### Test 4: Prompt and Context Engineering

Preserve exact facts and provenance, budget and prune context, isolate workers, write precise instructions and examples, validate outputs, handle missing evidence and conflicts, and consume generated content defensively.

Allocation: Prompt and Context Engineering: 100.

[Instructor CSV](../03-practice-sets/set-4/practice-set-4.csv) · [Offline questions and explanations](../03-practice-sets/set-4/practice-set-4.md)

Review task: explain the deciding requirement for three missed or uncertain items, then create a new safe example that changes the best answer by changing one constraint.

### Test 5: Security, Claude Code and Debugging

Apply trust boundaries, identity, authorization, secrets, layered controls, and pre-action hooks. Review Claude Code instructions, settings, skills, sessions, headless operation, traces, error classes, and integration debugging.

Allocation: Security and Safety: 50, Claude Code: 25, Eval, Testing, and Debugging: 25.

[Instructor CSV](../03-practice-sets/set-5/practice-set-5.csv) · [Offline questions and explanations](../03-practice-sets/set-5/practice-set-5.md)

Review task: explain the deciding requirement for three missed or uncertain items, then create a new safe example that changes the best answer by changing one constraint.

### Test 6: Integrated Developer Scenarios and Final Review

Apply all eight guide domains in an expanded mixed review: 15 agents, 33 applications, 3 Claude Code, 3 debugging, 17 optimization, 11 prompt/context, 8 security, and 10 tools/MCP questions.

Allocation: Agents and Workflows: 15, Applications and Integration: 33, Claude Code: 3, Eval, Testing, and Debugging: 3, Model Selection and Optimization: 17, Prompt and Context Engineering: 11, Security and Safety: 8, Tools and MCPs: 10.

[Instructor CSV](../03-practice-sets/set-6/practice-set-6.csv) · [Offline questions and explanations](../03-practice-sets/set-6/practice-set-6.md)

Review task: explain the deciding requirement for three missed or uncertain items, then create a new safe example that changes the best answer by changing one constraint.

## Domain allocation

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

Only the integrated review approximates official percentages. Local skill identifiers are bookkeeping, not official numbered objectives. Consult the [full skill coverage](../04-resources/sources-and-coverage.md).

## Suggested routine

1. Read the current official guide and confirm the exam version you intend to take.
2. Establish familiarity with APIs, JSON, asynchronous programming, Git, and testing.
3. Complete a focused test; record mistakes as requirement, selected alternative, missing distinction, and next practice action.
4. Review all options, including correct guesses. Explain why each alternative fails the case's particular requirement.
5. Build a small safe example or test double for weak technical topics; never use live destructive operations as an unreviewed exercise.
6. Revisit weak named skills, then attempt Test 6 with unfamiliar variations and without relying on remembered answer positions.
7. Use current official resources and hands-on work for gaps. Practice scores alone are not certification readiness estimates.

## Instructor setup

Create six Udemy practice-test activities and import the corresponding CSV into each activity after verifying the current uploader template. Enter custom timing and target only if useful, clearly identifying them as study settings. Preview all explanations, domain labels, special characters, and single-answer keys. There are no included video lectures, graded labs, API credits, vouchers, or automatic publication steps.

## Version refresh boundary

Revisit the official portal and revised guide due November 17, 2026 before preparation for the December 7 update. Reconcile every domain, named skill, product contract, and affected question before claiming updated alignment. Do not infer future scope from the announcement alone.
