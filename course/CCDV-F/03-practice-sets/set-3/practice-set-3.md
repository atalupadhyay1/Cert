# Claude Certified Developer – Foundations (CCDV-F) — Practice Set 3

Model Selection and Optimization

100 questions · Suggested practice duration: 200 minutes · Practice target: 80%

Tests 1–5 are focused learning tests. Test 6 is an expanded blueprint-proportioned review, not an official exam replica. Related concepts recur.

Select ONE best answer for every question. Answer key follows all questions.

Original educational content, not actual, recalled, or copied Anthropic exam items.

## Questions

### 1. A developer estimates prompt size by counting English words and is surprised by a code-heavy request. What accounting unit should be used?

Domain: Model Selection and Optimization

- A. Use supported token counting before oversized submission
- B. Count tokens with model-compatible accounting
- C. Budget instructions, evidence, history, and generation together
- D. Track actual usage by token and billing category

### 2. A request includes system instructions, tools, history, documents, and expected output. What needs a capacity plan?

Domain: Model Selection and Optimization

- A. Reduce tool output to relevant fields with provenance
- B. Use supported token counting before oversized submission
- C. Compact context while preserving checked facts and open issues
- D. Budget instructions, evidence, history, and generation together

### 3. Repeated low-temperature requests produce slightly different answers. What property must the application accommodate?

Domain: Model Selection and Optimization

- A. Pin compatible model, SDK, prompt, and dependency versions
- B. Use a versioned representative held-out evaluation set
- C. Adjust sampling variability, not factual truth
- D. Allow for output variability and validate outcomes

### 4. A creative task needs a supported control over sampling variability rather than a truth guarantee. Which setting fits?

Domain: Model Selection and Optimization

- A. Use supported thinking or effort controls after measuring task benefit
- B. Select the least costly configuration that meets required outcomes
- C. Route requests using evaluated task classes and safe fallbacks
- D. Adjust sampling variability, not factual truth

### 5. A request provides an instruction without any example input-output pair. What prompting setup is this?

Domain: Model Selection and Optimization

- A. Provide a task instruction without demonstrations
- B. Provide one representative demonstration
- C. Provide several representative demonstrations
- D. Provide concrete input–output examples

### 6. A request contains exactly one worked demonstration before the new task. What setup is illustrated?

Domain: Model Selection and Optimization

- A. Provide one representative demonstration
- B. Provide a task instruction without demonstrations
- C. Provide concrete input–output examples
- D. Provide several representative demonstrations

### 7. A request includes several representative worked examples to show a transformation. What setup is this?

Domain: Model Selection and Optimization

- A. Provide a task instruction without demonstrations
- B. Provide one representative demonstration
- C. Provide several representative demonstrations
- D. Provide concrete input–output examples

### 8. A reasoning-related option works on one model but is rejected by another. What should be evaluated?

Domain: Model Selection and Optimization

- A. Adjust sampling variability, not factual truth
- B. Pin compatible model, SDK, prompt, and dependency versions
- C. Use supported thinking or effort controls after measuring task benefit
- D. Select the least costly configuration that meets required outcomes

### 9. A supported model offers a faster inference mode, and the team wants to assess its latency and cost impact. Which feature should it evaluate under the actual service contract?

Domain: Model Selection and Optimization

- A. Use supported thinking or effort controls after measuring task benefit
- B. Evaluate supported fast inference mode
- C. Evaluate supported reasoning effort controls
- D. Adjust sampling variability, not factual truth

### 10. The same text has different token counts under different model-compatible tokenizers. What should developers recognize?

Domain: Model Selection and Optimization

- A. Count tokens with model-compatible accounting
- B. Use supported token counting before oversized submission
- C. Track actual usage by token and billing category
- D. Budget instructions, evidence, history, and generation together

### 11. An integration requires correct extraction and assumes temperature zero guarantees it. What fundamental limitation matters?

Domain: Model Selection and Optimization

- A. Allow for output variability and validate outcomes
- B. Adjust sampling variability, not factual truth
- C. Pin compatible model, SDK, prompt, and dependency versions
- D. Use supported thinking or effort controls after measuring task benefit

### 12. A supported adaptive-reasoning setting may improve difficult cases but add latency. What should guide enabling it?

Domain: Model Selection and Optimization

- A. Adjust sampling variability, not factual truth
- B. Use supported thinking or effort controls after measuring task benefit
- C. Route requests using evaluated task classes and safe fallbacks
- D. Select the least costly configuration that meets required outcomes

### 13. A request exceeds capacity and the developer assumes the oldest sentence always disappears automatically. What design is needed?

Domain: Model Selection and Optimization

- A. Reduce tool output to relevant fields with provenance
- B. Use supported prompt-prefix caching for eligible repeated input
- C. Budget instructions, evidence, history, and generation together
- D. Compact context while preserving checked facts and open issues

### 14. A billing dashboard treats every punctuation character as one token. What representation should replace that assumption?

Domain: Model Selection and Optimization

- A. Budget instructions, evidence, history, and generation together
- B. Track actual usage by token and billing category
- C. Use supported token counting before oversized submission
- D. Count tokens with model-compatible accounting

### 15. A response convention is demonstrated by three complete input-output pairs. Which prompting category fits?

Domain: Model Selection and Optimization

- A. Provide concrete input–output examples
- B. Provide one representative demonstration
- C. Provide several representative demonstrations
- D. Provide a task instruction without demonstrations

### 16. A model performs a new task using only explicit instructions and available context. Which setup applies without demonstrations?

Domain: Model Selection and Optimization

- A. Provide a task instruction without demonstrations
- B. Provide concrete input–output examples
- C. Provide one representative demonstration
- D. Provide several representative demonstrations

### 17. A developer supplies one example and wrongly calls the method model fine-tuning. What is actually being used?

Domain: Model Selection and Optimization

- A. Provide a task instruction without demonstrations
- B. Provide several representative demonstrations
- C. Provide concrete input–output examples
- D. Provide one representative demonstration

### 18. A developer copies an effort setting from a different model release. What needs verification?

Domain: Model Selection and Optimization

- A. Preserve protocol-required blocks through tool continuations
- B. Select the least costly configuration that meets required outcomes
- C. Use supported thinking or effort controls after measuring task benefit
- D. Adjust sampling variability, not factual truth

### 19. A product compares complete answer strings as though every acceptable response must be identical. What model property should testing allow?

Domain: Model Selection and Optimization

- A. Use a versioned representative held-out evaluation set
- B. Allow for output variability and validate outcomes
- C. Pin compatible model, SDK, prompt, and dependency versions
- D. Adjust sampling variability, not factual truth

### 20. A huge document leaves no room for required output under a shared budget assumption. What must be planned?

Domain: Model Selection and Optimization

- A. Compact context while preserving checked facts and open issues
- B. Use supported token counting before oversized submission
- C. Reduce tool output to relevant fields with provenance
- D. Budget instructions, evidence, history, and generation together

### 21. A TypeScript SDK wraps HTTP calls but exposes different convenience methods from a Python SDK. What integration design handles these differences?

Domain: Model Selection and Optimization

- A. Separate environment configuration from application logic
- B. Apply HTTP method, status, authentication, and payload contracts
- C. Use a provider-specific adapter behind a stable application interface
- D. Build a valid Messages API request with explicit content blocks

### 22. An endpoint requires specific authentication headers and a JSON payload. What foundational contract should be followed?

Domain: Model Selection and Optimization

- A. Test the integration contract at the provider boundary
- B. Use a provider-specific adapter behind a stable application interface
- C. Apply HTTP method, status, authentication, and payload contracts
- D. Build a valid Messages API request with explicit content blocks

### 23. An application explicitly needs persistent bidirectional communication between client and its own backend. Which transport may fit?

Domain: Model Selection and Optimization

- A. Use asynchronous I/O with bounded concurrency
- B. Consume the Messages stream as server-sent events
- C. Apply HTTP method, status, authentication, and payload contracts
- D. Use WebSockets for an explicitly bidirectional persistent channel

### 24. The standard Messages streaming endpoint emits incremental HTTP events. Which protocol should its client understand?

Domain: Model Selection and Optimization

- A. Use asynchronous I/O with bounded concurrency
- B. Use WebSockets for an explicitly bidirectional persistent channel
- C. Consume the Messages stream as server-sent events
- D. Apply HTTP method, status, authentication, and payload contracts

### 25. A service must wait on model I/O without blocking its event loop. Which programming technique fits?

Domain: Model Selection and Optimization

- A. Run independent branches concurrently and join checked results
- B. Bound work queues and apply backpressure
- C. Wait for validated prerequisite outputs
- D. Use asynchronous I/O with bounded concurrency

### 26. A fast producer overwhelms a slow consumer of generated results. What should the pipeline enforce?

Domain: Model Selection and Optimization

- A. Use asynchronous I/O with bounded concurrency
- B. Bound work queues and apply backpressure
- C. Run independent branches concurrently and join checked results
- D. Enforce task, iteration, and spending safeguards

### 27. A supported SDK upgrade changes serialization behavior at the provider boundary. What testing helps catch compatibility issues?

Domain: Model Selection and Optimization

- A. Test the integration contract at the provider boundary
- B. Use controlled stubs for repeatable failure-path tests
- C. Use tests and specific failure feedback to drive iteration
- D. Use a versioned representative held-out evaluation set

### 28. Different deployments silently use different SDK versions and cannot reproduce failures. What practice improves diagnosis?

Domain: Model Selection and Optimization

- A. Separate environment configuration from application logic
- B. Pin compatible model, SDK, prompt, and dependency versions
- C. Version and review plugin dependencies and permissions
- D. Use a provider-specific adapter behind a stable application interface

### 29. A long request consumes resources after the application's useful response deadline. What should bound the wait?

Domain: Model Selection and Optimization

- A. Set explicit deadlines and classify timeout outcomes
- B. Cancel local work and reconcile any external operation separately
- C. Coordinate retries across SDK and application layers
- D. Retry a transient failure with bounded backoff

### 30. SDK retries and custom retries multiply provider traffic unexpectedly. What should be coordinated?

Domain: Model Selection and Optimization

- A. Retry a transient failure with bounded backoff
- B. Bound work queues and apply backpressure
- C. Set explicit deadlines and classify timeout outcomes
- D. Coordinate retries across SDK and application layers

### 31. A streamed JSON value is split across multiple network chunks. What should happen before final parsing?

Domain: Model Selection and Optimization

- A. Consume the Messages stream as server-sent events
- B. Accumulate deltas by block index before final validation
- C. Use the final assembled message and completion status
- D. Dispatch response content according to each block type

### 32. A response contains several content types, but the parser assumes one display string. What design should replace this?

Domain: Model Selection and Optimization

- A. Dispatch response content according to each block type
- B. Use the final assembled message and completion status
- C. Accumulate deltas by block index before final validation
- D. Build a valid Messages API request with explicit content blocks

### 33. A cost increase appears after a refactor but its cause is unclear. What diagnostic evidence should be inspected?

Domain: Model Selection and Optimization

- A. Use controlled stubs for repeatable failure-path tests
- B. Inspect a redacted end-to-end request and tool trace
- C. Use a versioned representative held-out evaluation set
- D. Propagate correlation identifiers across requests and tools

### 34. A retry could repeat a committed backend operation after response loss. What feature improves safety where supported?

Domain: Model Selection and Optimization

- A. Set explicit deadlines and classify timeout outcomes
- B. Use a durable idempotency key for the same logical action
- C. Cancel local work and reconcile any external operation separately
- D. Validate and commit business changes through a controlled boundary

### 35. A client stops waiting for a provider call and claims a remote action was undone. What handling is required?

Domain: Model Selection and Optimization

- A. Validate and commit business changes through a controlled boundary
- B. Cancel local work and reconcile any external operation separately
- C. Use a durable idempotency key for the same logical action
- D. Set explicit deadlines and classify timeout outcomes

### 36. The same named feature has different request parameters on different hosts. What should shield application code?

Domain: Model Selection and Optimization

- A. Separate environment configuration from application logic
- B. Select the least costly configuration that meets required outcomes
- C. Pin compatible model, SDK, prompt, and dependency versions
- D. Use a provider-specific adapter behind a stable application interface

### 37. Developers need to connect billing usage to one user task across several model calls. What should propagate?

Domain: Model Selection and Optimization

- A. Propagate correlation identifiers across requests and tools
- B. Inspect a redacted end-to-end request and tool trace
- C. Record detected_pattern and dismissal reasons
- D. Keep protected action and identity audit records

### 38. A developer's machine and production use different endpoints and credentials. What separation is appropriate?

Domain: Model Selection and Optimization

- A. Version and review plugin dependencies and permissions
- B. Separate environment configuration from application logic
- C. Pin compatible model, SDK, prompt, and dependency versions
- D. Use a provider-specific adapter behind a stable application interface

### 39. A recovery test must simulate a repeatable malformed response without live provider costs. What technique fits?

Domain: Model Selection and Optimization

- A. Use a versioned representative held-out evaluation set
- B. Use tests and specific failure feedback to drive iteration
- C. Use controlled stubs for repeatable failure-path tests
- D. Test the integration contract at the provider boundary

### 40. A token-count display is wrong because application code applies the rate twice. Where should debugging isolate the issue?

Domain: Model Selection and Optimization

- A. Isolate model-output defects from integration defects
- B. State explicit reportable and non-reportable criteria
- C. Use a versioned representative held-out evaluation set
- D. Inspect a redacted end-to-end request and tool trace

### 41. A task prioritizes speed and efficiency, and its quality target is modest but verified. Which family is a starting candidate?

Domain: Model Selection and Optimization

- A. Use supported thinking or effort controls after measuring task benefit
- B. Evaluate Opus for demanding capability-oriented work
- C. Evaluate Sonnet for a measured balance of capability and efficiency
- D. Evaluate Haiku for suitable speed- and efficiency-oriented tasks

### 42. A team seeks a measured balance of coding capability and operating efficiency. Which family is a reasonable starting candidate?

Domain: Model Selection and Optimization

- A. Evaluate Opus for demanding capability-oriented work
- B. Evaluate Haiku for suitable speed- and efficiency-oriented tasks
- C. Evaluate Sonnet for a measured balance of capability and efficiency
- D. Use supported thinking or effort controls after measuring task benefit

### 43. A difficult analytical task justifies evaluating a capability-oriented family despite tighter cost and latency review. Which candidate fits that starting hypothesis?

Domain: Model Selection and Optimization

- A. Use supported thinking or effort controls after measuring task benefit
- B. Evaluate Opus for demanding capability-oriented work
- C. Evaluate Haiku for suitable speed- and efficiency-oriented tasks
- D. Evaluate Sonnet for a measured balance of capability and efficiency

### 44. All three model families are available. What should determine the final production choice?

Domain: Model Selection and Optimization

- A. Evaluate Haiku for suitable speed- and efficiency-oriented tasks
- B. Evaluate Opus for demanding capability-oriented work
- C. Evaluate Sonnet for a measured balance of capability and efficiency
- D. Select the least costly configuration that meets required outcomes

### 45. Routine and difficult requests have distinct evaluated requirements. What may reduce unnecessary expensive processing?

Domain: Model Selection and Optimization

- A. Evaluate Haiku for suitable speed- and efficiency-oriented tasks
- B. Select the least costly configuration that meets required outcomes
- C. Evaluate Opus for demanding capability-oriented work
- D. Route requests using evaluated task classes and safe fallbacks

### 46. A replacement model improves a generic benchmark but may change tool behavior. What release practice should follow task evaluation?

Domain: Model Selection and Optimization

- A. Select the least costly configuration that meets required outcomes
- B. Use a versioned representative held-out evaluation set
- C. Canary a version change with regression gates and rollback
- D. Pin compatible model, SDK, prompt, and dependency versions

### 47. A team considers replacing a model based on a vendor demo. What evidence should it gather?

Domain: Model Selection and Optimization

- A. Route requests using evaluated task classes and safe fallbacks
- B. Select the least costly configuration that meets required outcomes
- C. Use a versioned representative held-out evaluation set
- D. Pin compatible model, SDK, prompt, and dependency versions

### 48. More reasoning effort improves some outputs but makes routine requests too slow. What configuration decision is appropriate?

Domain: Model Selection and Optimization

- A. Select the least costly configuration that meets required outcomes
- B. Adjust sampling variability, not factual truth
- C. Use supported thinking or effort controls after measuring task benefit
- D. Route requests using evaluated task classes and safe fallbacks

### 49. A moving model alias changes response behavior after a deployment. What improves reproducible version identification?

Domain: Model Selection and Optimization

- A. Pin compatible model, SDK, prompt, and dependency versions
- B. Select the least costly configuration that meets required outcomes
- C. Separate environment configuration from application logic
- D. Canary a version change with regression gates and rollback

### 50. The lowest-price model misses a mandatory accuracy threshold. What should selection prioritize?

Domain: Model Selection and Optimization

- A. Measure tail latency as well as average latency
- B. Compare total cost per verified successful outcome
- C. Select the least costly configuration that meets required outcomes
- D. Track actual usage by token and billing category

### 51. Average latency looks acceptable, but many users experience extreme delays. What measurement is needed?

Domain: Model Selection and Optimization

- A. Measure tail latency as well as average latency
- B. Track actual usage by token and billing category
- C. Measure time to first token separately from full completion
- D. Compare total cost per verified successful outcome

### 52. Streaming starts slowly but finishes quickly once tokens appear. What isolates the initial wait?

Domain: Model Selection and Optimization

- A. Measure time to first token separately from full completion
- B. Track actual usage by token and billing category
- C. Compare total cost per verified successful outcome
- D. Measure tail latency as well as average latency

### 53. A smaller model passes every required quality and safety check at lower total cost. What selection principle supports using it?

Domain: Model Selection and Optimization

- A. Evaluate Haiku for suitable speed- and efficiency-oriented tasks
- B. Evaluate Opus for demanding capability-oriented work
- C. Evaluate Sonnet for a measured balance of capability and efficiency
- D. Select the least costly configuration that meets required outcomes

### 54. Most requests are easy, but occasional complex cases need a stronger path. What application pattern may fit?

Domain: Model Selection and Optimization

- A. Select the least costly configuration that meets required outcomes
- B. Use supported thinking or effort controls after measuring task benefit
- C. Canary a version change with regression gates and rollback
- D. Route requests using evaluated task classes and safe fallbacks

### 55. A new release changes defaults affecting structured outputs. How should adoption be staged?

Domain: Model Selection and Optimization

- A. Use a versioned representative held-out evaluation set
- B. Route requests using evaluated task classes and safe fallbacks
- C. Canary a version change with regression gates and rollback
- D. Pin compatible model, SDK, prompt, and dependency versions

### 56. A high-capability model is accurate but violates the interaction deadline. What should guide the decision?

Domain: Model Selection and Optimization

- A. Select the least costly configuration that meets required outcomes
- B. Track actual usage by token and billing category
- C. Measure tail latency as well as average latency
- D. Compare total cost per verified successful outcome

### 57. A provider supports adaptive reasoning only for selected versions. What should developers verify before enabling it?

Domain: Model Selection and Optimization

- A. Adjust sampling variability, not factual truth
- B. Use supported thinking or effort controls after measuring task benefit
- C. Allow for output variability and validate outcomes
- D. Pin compatible model, SDK, prompt, and dependency versions

### 58. A cheap model needs many retries and substantial reviewer correction. What economic comparison is useful?

Domain: Model Selection and Optimization

- A. Track actual usage by token and billing category
- B. Compare total cost per verified successful outcome
- C. Measure tail latency as well as average latency
- D. Select the least costly configuration that meets required outcomes

### 59. The chosen model performs well on English examples but poorly on required multilingual tasks. What selection evidence is missing?

Domain: Model Selection and Optimization

- A. Pin compatible model, SDK, prompt, and dependency versions
- B. Use a versioned representative held-out evaluation set
- C. Canary a version change with regression gates and rollback
- D. Select the least costly configuration that meets required outcomes

### 60. A team always picks one family regardless of task constraints. What should replace that policy?

Domain: Model Selection and Optimization

- A. Route requests using evaluated task classes and safe fallbacks
- B. Select the least costly configuration that meets required outcomes
- C. Evaluate Haiku for suitable speed- and efficiency-oriented tasks
- D. Evaluate Opus for demanding capability-oriented work

### 61. A bill combines ordinary input, output, and applicable cache categories. What monitoring should distinguish them?

Domain: Model Selection and Optimization

- A. Count tokens with model-compatible accounting
- B. Compare total cost per verified successful outcome
- C. Track actual usage by token and billing category
- D. Use supported token counting before oversized submission

### 62. A large request may exceed supported limits before it is sent. What preflight technique can help?

Domain: Model Selection and Optimization

- A. Count tokens with model-compatible accounting
- B. Track actual usage by token and billing category
- C. Use supported token counting before oversized submission
- D. Budget instructions, evidence, history, and generation together

### 63. Stable instructions appear after a changing user-specific prefix and expected cache reuse is poor. What layout should be evaluated?

Domain: Model Selection and Optimization

- A. Use supported prompt-prefix caching for eligible repeated input
- B. Put eligible stable common content before variable input for cache reuse
- C. Track actual usage by token and billing category
- D. Verify cache reads, writes, and economics in actual usage

### 64. Identical text is repeated, but no measured cache reads appear. What should be investigated?

Domain: Model Selection and Optimization

- A. Put eligible stable common content before variable input for cache reuse
- B. Verify cache reads, writes, and economics in actual usage
- C. Use supported token counting before oversized submission
- D. Track actual usage by token and billing category

### 65. A monthly report excludes retries, review, and tool expenses from AI cost. What metric should be added?

Domain: Model Selection and Optimization

- A. Track actual usage by token and billing category
- B. Measure tail latency as well as average latency
- C. Select the least costly configuration that meets required outcomes
- D. Compare total cost per verified successful outcome

### 66. Evidence consumes the whole context budget, leaving no generation allowance under the stated shared-limit model. What should change?

Domain: Model Selection and Optimization

- A. Use supported token counting before oversized submission
- B. Compact context while preserving checked facts and open issues
- C. Budget instructions, evidence, history, and generation together
- D. Reduce tool output to relevant fields with provenance

### 67. A provider uses different cache-write and cache-read charges. What accounting is required?

Domain: Model Selection and Optimization

- A. Put eligible stable common content before variable input for cache reuse
- B. Use supported token counting before oversized submission
- C. Track actual usage by token and billing category
- D. Verify cache reads, writes, and economics in actual usage

### 68. Many requests share one eligible standards document but require new personalized answers. What reuse is appropriate?

Domain: Model Selection and Optimization

- A. Track actual usage by token and billing category
- B. Put eligible stable common content before variable input for cache reuse
- C. Verify cache reads, writes, and economics in actual usage
- D. Use supported prompt-prefix caching for eligible repeated input

### 69. A developer estimates input capacity using an unrelated model tokenizer. What should be corrected?

Domain: Model Selection and Optimization

- A. Use supported token counting before oversized submission
- B. Count tokens with model-compatible accounting
- C. Track actual usage by token and billing category
- D. Budget instructions, evidence, history, and generation together

### 70. A caching experiment adds write overhead but serves few repeated requests. What should be measured?

Domain: Model Selection and Optimization

- A. Put eligible stable common content before variable input for cache reuse
- B. Compare total cost per verified successful outcome
- C. Track actual usage by token and billing category
- D. Verify cache reads, writes, and economics in actual usage

### 71. At hypothetical rates of $2 per million input tokens and $6 per million output tokens, what do 300,000 input and 200,000 output tokens cost?

Domain: Model Selection and Optimization

- A. $0.18
- B. $18.00
- C. $1.80
- D. $2.40

### 72. Assume a shared 16,000-token budget, 3,000 tokens of instructions/history, and 2,000 reserved for generation. How much remains for evidence?

Domain: Model Selection and Optimization

- A. 13,000 tokens
- B. 14,000 tokens
- C. 16,000 tokens
- D. 11,000 tokens

### 73. A costs $0.02 per attempt with 80% acceptance; B costs $0.015 with 50%. Ignoring other costs, which has lower accepted-result cost?

Domain: Model Selection and Optimization

- A. B: $0.015 per accepted result
- B. Both have identical accepted-result cost
- C. Acceptance does not affect cost per accepted result
- D. A: $0.025 per accepted result

### 74. Usage records show 60,000 cache-read tokens out of 100,000 categorized input tokens. What share was cache reads?

Domain: Model Selection and Optimization

- A. 60% of input tokens were cache reads
- B. 40% of input tokens were cache reads
- C. 100% of input tokens were cache reads
- D. 0.06% of input tokens were cache reads

### 75. Model calls become cheaper but rework rises enough to increase total workflow expense. What metric captures this?

Domain: Model Selection and Optimization

- A. Track actual usage by token and billing category
- B. Verify cache reads, writes, and economics in actual usage
- C. Compare total cost per verified successful outcome
- D. Measure tail latency as well as average latency

### 76. A cost forecast assumes all input tokens receive the cache-read rate even on cold requests. What should be corrected?

Domain: Model Selection and Optimization

- A. Track actual usage by token and billing category
- B. Verify cache reads, writes, and economics in actual usage
- C. Use supported token counting before oversized submission
- D. Put eligible stable common content before variable input for cache reuse

### 77. A developer reserves output but ignores system and tool-definition tokens. What budgeting principle should apply?

Domain: Model Selection and Optimization

- A. Use supported token counting before oversized submission
- B. Compact context while preserving checked facts and open issues
- C. Reduce tool output to relevant fields with provenance
- D. Budget instructions, evidence, history, and generation together

### 78. A dashboard claims 60% monetary savings merely because 60% of input tokens were cache reads. What should be evaluated?

Domain: Model Selection and Optimization

- A. Put eligible stable common content before variable input for cache reuse
- B. Compare total cost per verified successful outcome
- C. Track actual usage by token and billing category
- D. Verify cache reads, writes, and economics in actual usage

### 79. A multi-step task makes several model calls, but accounting records only the final answer. What should be tracked?

Domain: Model Selection and Optimization

- A. Use supported token counting before oversized submission
- B. Compare total cost per verified successful outcome
- C. Count tokens with model-compatible accounting
- D. Track actual usage by token and billing category

### 80. Two configurations have equal token charges but different review and failure costs. Which comparison should guide the choice?

Domain: Model Selection and Optimization

- A. Measure tail latency as well as average latency
- B. Track actual usage by token and billing category
- C. Compare total cost per verified successful outcome
- D. Select the least costly configuration that meets required outcomes

### 81. A service-level objective applies to 95th-percentile completion time, but tests report only means. What should be measured?

Domain: Model Selection and Optimization

- A. Track actual usage by token and billing category
- B. Measure time to first token separately from full completion
- C. Measure tail latency as well as average latency
- D. Compare total cost per verified successful outcome

### 82. A streaming optimization shows text earlier but leaves total completion time unchanged. What metric did it most directly improve?

Domain: Model Selection and Optimization

- A. Measure time to first token separately from full completion
- B. Measure tail latency as well as average latency
- C. Track actual usage by token and billing category
- D. Compare total cost per verified successful outcome

### 83. A routing rule sends hard cases to an undersized model because complexity detection is weak. What pattern needs evaluation?

Domain: Model Selection and Optimization

- A. Use supported thinking or effort controls after measuring task benefit
- B. Route requests using evaluated task classes and safe fallbacks
- C. Canary a version change with regression gates and rollback
- D. Select the least costly configuration that meets required outcomes

### 84. A leaderboard winner lacks required modality support in the intended provider environment. What should selection follow?

Domain: Model Selection and Optimization

- A. Evaluate Haiku for suitable speed- and efficiency-oriented tasks
- B. Evaluate Sonnet for a measured balance of capability and efficiency
- C. Evaluate Opus for demanding capability-oriented work
- D. Select the least costly configuration that meets required outcomes

### 85. Caching stops working after a small prefix change. What should be verified?

Domain: Model Selection and Optimization

- A. Track actual usage by token and billing category
- B. Verify cache reads, writes, and economics in actual usage
- C. Put eligible stable common content before variable input for cache reuse
- D. Use supported token counting before oversized submission

### 86. A model option changes the usage categories billed by the provider. What should the cost model update?

Domain: Model Selection and Optimization

- A. Use supported token counting before oversized submission
- B. Track actual usage by token and billing category
- C. Verify cache reads, writes, and economics in actual usage
- D. Count tokens with model-compatible accounting

### 87. A model swap works directly but fails through an SDK wrapper. What test boundary should isolate the incompatibility?

Domain: Model Selection and Optimization

- A. Test the integration contract at the provider boundary
- B. Use controlled stubs for repeatable failure-path tests
- C. Use a versioned representative held-out evaluation set
- D. Inspect a redacted end-to-end request and tool trace

### 88. A pinned model with low temperature still produces occasional different valid wording. What should acceptance allow?

Domain: Model Selection and Optimization

- A. Allow for output variability and validate outcomes
- B. Pin compatible model, SDK, prompt, and dependency versions
- C. Use a versioned representative held-out evaluation set
- D. Adjust sampling variability, not factual truth

### 89. A new model passes offline evaluation but production dependency behavior is uncertain. What rollout discipline fits?

Domain: Model Selection and Optimization

- A. Pin compatible model, SDK, prompt, and dependency versions
- B. Use a versioned representative held-out evaluation set
- C. Select the least costly configuration that meets required outcomes
- D. Canary a version change with regression gates and rollback

### 90. A proposed optimization reduces token volume but increases incorrect outputs. What economic boundary matters?

Domain: Model Selection and Optimization

- A. Measure tail latency as well as average latency
- B. Verify cache reads, writes, and economics in actual usage
- C. Compare total cost per verified successful outcome
- D. Track actual usage by token and billing category

### 91. A text unit may be a subword or byte-derived segment rather than a whole word. What is being counted?

Domain: Model Selection and Optimization

- A. Count tokens with model-compatible accounting
- B. Track actual usage by token and billing category
- C. Use supported token counting before oversized submission
- D. Budget instructions, evidence, history, and generation together

### 92. A task needs deeper reasoning only on difficult cases, and the selected model supports adaptive controls. What should be tested?

Domain: Model Selection and Optimization

- A. Adjust sampling variability, not factual truth
- B. Use supported thinking or effort controls after measuring task benefit
- C. Select the least costly configuration that meets required outcomes
- D. Pin compatible model, SDK, prompt, and dependency versions

### 93. A custom collaboration feature requires both client and server to send messages independently over a persistent channel. What transport may fit?

Domain: Model Selection and Optimization

- A. Consume the Messages stream as server-sent events
- B. Use asynchronous I/O with bounded concurrency
- C. Apply HTTP method, status, authentication, and payload contracts
- D. Use WebSockets for an explicitly bidirectional persistent channel

### 94. A developer calls an async SDK from an event loop but forgets to await its response. What concept should be corrected?

Domain: Model Selection and Optimization

- A. Run independent branches concurrently and join checked results
- B. Bound work queues and apply backpressure
- C. Use asynchronous I/O with bounded concurrency
- D. Wait for validated prerequisite outputs

### 95. An evaluated simple-label task meets every quality constraint with an efficiency-oriented supported family. Which starting candidate matches that positioning?

Domain: Model Selection and Optimization

- A. Evaluate Opus for demanding capability-oriented work
- B. Evaluate Haiku for suitable speed- and efficiency-oriented tasks
- C. Evaluate Sonnet for a measured balance of capability and efficiency
- D. Use supported thinking or effort controls after measuring task benefit

### 96. A team compares balanced capability and operating efficiency for routine development work. Which family is a reasonable candidate to evaluate?

Domain: Model Selection and Optimization

- A. Evaluate Sonnet for a measured balance of capability and efficiency
- B. Evaluate Opus for demanding capability-oriented work
- C. Evaluate Haiku for suitable speed- and efficiency-oriented tasks
- D. Use supported thinking or effort controls after measuring task benefit

### 97. A capability-demanding case remains difficult for evaluated lower-cost options. Which family may merit a measured trial?

Domain: Model Selection and Optimization

- A. Evaluate Opus for demanding capability-oriented work
- B. Use supported thinking or effort controls after measuring task benefit
- C. Evaluate Sonnet for a measured balance of capability and efficiency
- D. Evaluate Haiku for suitable speed- and efficiency-oriented tasks

### 98. User-specific data changes first and pushes a stable common document out of an eligible matching prefix. What layout should be tested?

Domain: Model Selection and Optimization

- A. Use supported token counting before oversized submission
- B. Put eligible stable common content before variable input for cache reuse
- C. Track actual usage by token and billing category
- D. Verify cache reads, writes, and economics in actual usage

### 99. A cache checkpoint is configured, but requests rarely reuse it before expiry. What evidence should determine economic value?

Domain: Model Selection and Optimization

- A. Verify cache reads, writes, and economics in actual usage
- B. Compare total cost per verified successful outcome
- C. Put eligible stable common content before variable input for cache reuse
- D. Track actual usage by token and billing category

### 100. A model is chosen from a tiny tuning set, then fails on independent production patterns. What evaluation should be added?

Domain: Model Selection and Optimization

- A. Use a versioned representative held-out evaluation set
- B. Pin compatible model, SDK, prompt, and dependency versions
- C. Canary a version change with regression gates and rollback
- D. Select the least costly configuration that meets required outcomes

---

## Answer key and explanations

### Question 1 — B

Answer: Count tokens with model-compatible accounting. Tokenization depends on the selected model and content rather than a fixed word ratio. Tokens are model-dependent units, not always words or characters. Include actual system, tool, content, and output usage according to the service contract. Local study-map skill 5.1 (LLM Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. A token-count endpoint or compatible estimator can help plan requests. Include hidden overhead allowed by the documented interface and verify actual usage afterward. In this case: Tokenization depends on the selected model and content rather than a fixed word ratio.
- **B:** Correct. Tokens are model-dependent units, not always words or characters. Include actual system, tool, content, and output usage according to the service contract. In this case: Tokenization depends on the selected model and content rather than a fixed word ratio.
- **C:** Incorrect for this question. Follow the chosen model and service limits. Overflow handling varies; it is not universally automatic oldest-message deletion. In this case: Tokenization depends on the selected model and content rather than a fixed word ratio.
- **D:** Incorrect for this question. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. In this case: Tokenization depends on the selected model and content rather than a fixed word ratio.

### Question 2 — D

Answer: Budget instructions, evidence, history, and generation together. All relevant components must fit the selected model and service accounting rules. Follow the chosen model and service limits. Overflow handling varies; it is not universally automatic oldest-message deletion. Local study-map skill 5.1 (LLM Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: All relevant components must fit the selected model and service accounting rules.
- **B:** Incorrect for this question. A token-count endpoint or compatible estimator can help plan requests. Include hidden overhead allowed by the documented interface and verify actual usage afterward. In this case: All relevant components must fit the selected model and service accounting rules.
- **C:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: All relevant components must fit the selected model and service accounting rules.
- **D:** Correct. Follow the chosen model and service limits. Overflow handling varies; it is not universally automatic oldest-message deletion. In this case: All relevant components must fit the selected model and service accounting rules.

### Question 3 — D

Answer: Allow for output variability and validate outcomes. Low variability settings do not establish universal deterministic execution or factual truth. Repeated calls can differ, even with low sampling settings. Seeds or low temperature do not establish universal cross-version determinism or factual accuracy. Local study-map skill 5.1 (LLM Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Low variability settings do not establish universal deterministic execution or factual truth.
- **B:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Low variability settings do not establish universal deterministic execution or factual truth.
- **C:** Incorrect for this question. Temperature changes next-token sampling behavior where supported. Lowering it does not independently guarantee correct extraction, grounding, or identical execution. In this case: Low variability settings do not establish universal deterministic execution or factual truth.
- **D:** Correct. Repeated calls can differ, even with low sampling settings. Seeds or low temperature do not establish universal cross-version determinism or factual accuracy. In this case: Low variability settings do not establish universal deterministic execution or factual truth.

### Question 4 — D

Answer: Adjust sampling variability, not factual truth. Temperature influences next-token sampling distribution where the chosen model supports it. Temperature changes next-token sampling behavior where supported. Lowering it does not independently guarantee correct extraction, grounding, or identical execution. Local study-map skill 5.1 (LLM Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Reasoning-related features and parameters vary by model and provider. Evaluate quality, latency, and cost rather than assume every release accepts the same switches. In this case: Temperature influences next-token sampling distribution where the chosen model supports it.
- **B:** Incorrect for this question. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. In this case: Temperature influences next-token sampling distribution where the chosen model supports it.
- **C:** Incorrect for this question. Use evidence-based routing to suitable configurations, monitor misclassification, and define fallback. Routing complexity must justify its own operating cost. In this case: Temperature influences next-token sampling distribution where the chosen model supports it.
- **D:** Correct. Temperature changes next-token sampling behavior where supported. Lowering it does not independently guarantee correct extraction, grounding, or identical execution. In this case: Temperature influences next-token sampling distribution where the chosen model supports it.

### Question 5 — A

Answer: Provide a task instruction without demonstrations. No demonstration is supplied, so the setup is zero-shot. Zero-shot prompting supplies no example input-output pairs. The model may still use its pretrained capabilities and the request context. Local study-map skill 5.1 (LLM Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Correct. Zero-shot prompting supplies no example input-output pairs. The model may still use its pretrained capabilities and the request context. In this case: No demonstration is supplied, so the setup is zero-shot.
- **B:** Incorrect for this question. One-shot prompting includes one example. It is different from a training update and may not cover important task variation. In this case: No demonstration is supplied, so the setup is zero-shot.
- **C:** Incorrect for this question. Few-shot examples illustrate task patterns in context. They should cover meaningful boundaries rather than merely repeat one ideal answer. In this case: No demonstration is supplied, so the setup is zero-shot.
- **D:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: No demonstration is supplied, so the setup is zero-shot.

### Question 6 — A

Answer: Provide one representative demonstration. One example distinguishes one-shot prompting from zero or several demonstrations. One-shot prompting includes one example. It is different from a training update and may not cover important task variation. Local study-map skill 5.1 (LLM Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Correct. One-shot prompting includes one example. It is different from a training update and may not cover important task variation. In this case: One example distinguishes one-shot prompting from zero or several demonstrations.
- **B:** Incorrect for this question. Zero-shot prompting supplies no example input-output pairs. The model may still use its pretrained capabilities and the request context. In this case: One example distinguishes one-shot prompting from zero or several demonstrations.
- **C:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: One example distinguishes one-shot prompting from zero or several demonstrations.
- **D:** Incorrect for this question. Few-shot examples illustrate task patterns in context. They should cover meaningful boundaries rather than merely repeat one ideal answer. In this case: One example distinguishes one-shot prompting from zero or several demonstrations.

### Question 7 — C

Answer: Provide several representative demonstrations. Several demonstrations guide behavior in context without necessarily updating model weights. Few-shot examples illustrate task patterns in context. They should cover meaningful boundaries rather than merely repeat one ideal answer. Local study-map skill 5.1 (LLM Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Zero-shot prompting supplies no example input-output pairs. The model may still use its pretrained capabilities and the request context. In this case: Several demonstrations guide behavior in context without necessarily updating model weights.
- **B:** Incorrect for this question. One-shot prompting includes one example. It is different from a training update and may not cover important task variation. In this case: Several demonstrations guide behavior in context without necessarily updating model weights.
- **C:** Correct. Few-shot examples illustrate task patterns in context. They should cover meaningful boundaries rather than merely repeat one ideal answer. In this case: Several demonstrations guide behavior in context without necessarily updating model weights.
- **D:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Several demonstrations guide behavior in context without necessarily updating model weights.

### Question 8 — C

Answer: Use supported thinking or effort controls after measuring task benefit. Thinking and effort controls must match the selected model and provider capabilities. Reasoning-related features and parameters vary by model and provider. Evaluate quality, latency, and cost rather than assume every release accepts the same switches. Local study-map skill 5.1 (LLM Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Temperature changes next-token sampling behavior where supported. Lowering it does not independently guarantee correct extraction, grounding, or identical execution. In this case: Thinking and effort controls must match the selected model and provider capabilities.
- **B:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Thinking and effort controls must match the selected model and provider capabilities.
- **C:** Correct. Reasoning-related features and parameters vary by model and provider. Evaluate quality, latency, and cost rather than assume every release accepts the same switches. In this case: Thinking and effort controls must match the selected model and provider capabilities.
- **D:** Incorrect for this question. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. In this case: Thinking and effort controls must match the selected model and provider capabilities.

### Question 9 — B

Answer: Evaluate supported fast inference mode. Evaluate supported fast-mode behavior rather than confuse inference speed with sampling variability or reasoning effort. Fast-mode availability, pricing, and behavior depend on the selected service and model. Measure its latency and cost impact instead of assume it changes model capability, output length, or reasoning effort in a universal way. Local study-map skill 5.1 (LLM Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Reasoning-related features and parameters vary by model and provider. Evaluate quality, latency, and cost rather than assume every release accepts the same switches. In this case: Evaluate supported fast-mode behavior rather than confuse inference speed with sampling variability or reasoning effort.
- **B:** Correct. Fast-mode availability, pricing, and behavior depend on the selected service and model. Measure its latency and cost impact instead of assume it changes model capability, output length, or reasoning effort in a universal way. In this case: Evaluate supported fast-mode behavior rather than confuse inference speed with sampling variability or reasoning effort.
- **C:** Incorrect for this question. Effort settings influence supported reasoning behavior under a particular model contract. They are not synonyms for sampling temperature or guarantees of correctness. In this case: Evaluate supported fast-mode behavior rather than confuse inference speed with sampling variability or reasoning effort.
- **D:** Incorrect for this question. Temperature changes next-token sampling behavior where supported. Lowering it does not independently guarantee correct extraction, grounding, or identical execution. In this case: Evaluate supported fast-mode behavior rather than confuse inference speed with sampling variability or reasoning effort.

### Question 10 — A

Answer: Count tokens with model-compatible accounting. Token units and accounting are model-dependent rather than universally fixed character counts. Tokens are model-dependent units, not always words or characters. Include actual system, tool, content, and output usage according to the service contract. Local study-map skill 5.1 (LLM Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Correct. Tokens are model-dependent units, not always words or characters. Include actual system, tool, content, and output usage according to the service contract. In this case: Token units and accounting are model-dependent rather than universally fixed character counts.
- **B:** Incorrect for this question. A token-count endpoint or compatible estimator can help plan requests. Include hidden overhead allowed by the documented interface and verify actual usage afterward. In this case: Token units and accounting are model-dependent rather than universally fixed character counts.
- **C:** Incorrect for this question. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. In this case: Token units and accounting are model-dependent rather than universally fixed character counts.
- **D:** Incorrect for this question. Follow the chosen model and service limits. Overflow handling varies; it is not universally automatic oldest-message deletion. In this case: Token units and accounting are model-dependent rather than universally fixed character counts.

### Question 11 — A

Answer: Allow for output variability and validate outcomes. Consistent sampling behavior does not independently establish factual correctness. Repeated calls can differ, even with low sampling settings. Seeds or low temperature do not establish universal cross-version determinism or factual accuracy. Local study-map skill 5.1 (LLM Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Correct. Repeated calls can differ, even with low sampling settings. Seeds or low temperature do not establish universal cross-version determinism or factual accuracy. In this case: Consistent sampling behavior does not independently establish factual correctness.
- **B:** Incorrect for this question. Temperature changes next-token sampling behavior where supported. Lowering it does not independently guarantee correct extraction, grounding, or identical execution. In this case: Consistent sampling behavior does not independently establish factual correctness.
- **C:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Consistent sampling behavior does not independently establish factual correctness.
- **D:** Incorrect for this question. Reasoning-related features and parameters vary by model and provider. Evaluate quality, latency, and cost rather than assume every release accepts the same switches. In this case: Consistent sampling behavior does not independently establish factual correctness.

### Question 12 — B

Answer: Use supported thinking or effort controls after measuring task benefit. Measure actual task benefit against speed and cost rather than enable reasoning indiscriminately. Reasoning-related features and parameters vary by model and provider. Evaluate quality, latency, and cost rather than assume every release accepts the same switches. Local study-map skill 5.1 (LLM Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Temperature changes next-token sampling behavior where supported. Lowering it does not independently guarantee correct extraction, grounding, or identical execution. In this case: Measure actual task benefit against speed and cost rather than enable reasoning indiscriminately.
- **B:** Correct. Reasoning-related features and parameters vary by model and provider. Evaluate quality, latency, and cost rather than assume every release accepts the same switches. In this case: Measure actual task benefit against speed and cost rather than enable reasoning indiscriminately.
- **C:** Incorrect for this question. Use evidence-based routing to suitable configurations, monitor misclassification, and define fallback. Routing complexity must justify its own operating cost. In this case: Measure actual task benefit against speed and cost rather than enable reasoning indiscriminately.
- **D:** Incorrect for this question. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. In this case: Measure actual task benefit against speed and cost rather than enable reasoning indiscriminately.

### Question 13 — C

Answer: Budget instructions, evidence, history, and generation together. Follow documented limits and overflow behavior instead of inventing universal truncation rules. Follow the chosen model and service limits. Overflow handling varies; it is not universally automatic oldest-message deletion. Local study-map skill 5.1 (LLM Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: Follow documented limits and overflow behavior instead of inventing universal truncation rules.
- **B:** Incorrect for this question. Caching may reduce repeated prefix processing under provider-specific rules. It does not extend the context window, update model weights, or verify an answer. In this case: Follow documented limits and overflow behavior instead of inventing universal truncation rules.
- **C:** Correct. Follow the chosen model and service limits. Overflow handling varies; it is not universally automatic oldest-message deletion. In this case: Follow documented limits and overflow behavior instead of inventing universal truncation rules.
- **D:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Follow documented limits and overflow behavior instead of inventing universal truncation rules.

### Question 14 — D

Answer: Count tokens with model-compatible accounting. Use model-compatible token accounting rather than an arbitrary character rule. Tokens are model-dependent units, not always words or characters. Include actual system, tool, content, and output usage according to the service contract. Local study-map skill 5.1 (LLM Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Follow the chosen model and service limits. Overflow handling varies; it is not universally automatic oldest-message deletion. In this case: Use model-compatible token accounting rather than an arbitrary character rule.
- **B:** Incorrect for this question. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. In this case: Use model-compatible token accounting rather than an arbitrary character rule.
- **C:** Incorrect for this question. A token-count endpoint or compatible estimator can help plan requests. Include hidden overhead allowed by the documented interface and verify actual usage afterward. In this case: Use model-compatible token accounting rather than an arbitrary character rule.
- **D:** Correct. Tokens are model-dependent units, not always words or characters. Include actual system, tool, content, and output usage according to the service contract. In this case: Use model-compatible token accounting rather than an arbitrary character rule.

### Question 15 — C

Answer: Provide several representative demonstrations. Multiple demonstrations constitute few-shot context rather than a training update. Few-shot examples illustrate task patterns in context. They should cover meaningful boundaries rather than merely repeat one ideal answer. Local study-map skill 5.1 (LLM Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: Multiple demonstrations constitute few-shot context rather than a training update.
- **B:** Incorrect for this question. One-shot prompting includes one example. It is different from a training update and may not cover important task variation. In this case: Multiple demonstrations constitute few-shot context rather than a training update.
- **C:** Correct. Few-shot examples illustrate task patterns in context. They should cover meaningful boundaries rather than merely repeat one ideal answer. In this case: Multiple demonstrations constitute few-shot context rather than a training update.
- **D:** Incorrect for this question. Zero-shot prompting supplies no example input-output pairs. The model may still use its pretrained capabilities and the request context. In this case: Multiple demonstrations constitute few-shot context rather than a training update.

### Question 16 — A

Answer: Provide a task instruction without demonstrations. The absence of worked examples makes this a zero-shot request. Zero-shot prompting supplies no example input-output pairs. The model may still use its pretrained capabilities and the request context. Local study-map skill 5.1 (LLM Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Correct. Zero-shot prompting supplies no example input-output pairs. The model may still use its pretrained capabilities and the request context. In this case: The absence of worked examples makes this a zero-shot request.
- **B:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: The absence of worked examples makes this a zero-shot request.
- **C:** Incorrect for this question. One-shot prompting includes one example. It is different from a training update and may not cover important task variation. In this case: The absence of worked examples makes this a zero-shot request.
- **D:** Incorrect for this question. Few-shot examples illustrate task patterns in context. They should cover meaningful boundaries rather than merely repeat one ideal answer. In this case: The absence of worked examples makes this a zero-shot request.

### Question 17 — D

Answer: Provide one representative demonstration. One in-context demonstration is one-shot prompting, not parameter adaptation. One-shot prompting includes one example. It is different from a training update and may not cover important task variation. Local study-map skill 5.1 (LLM Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Zero-shot prompting supplies no example input-output pairs. The model may still use its pretrained capabilities and the request context. In this case: One in-context demonstration is one-shot prompting, not parameter adaptation.
- **B:** Incorrect for this question. Few-shot examples illustrate task patterns in context. They should cover meaningful boundaries rather than merely repeat one ideal answer. In this case: One in-context demonstration is one-shot prompting, not parameter adaptation.
- **C:** Incorrect for this question. Examples clarify expected transformations when prose is interpreted inconsistently. Include boundaries and varied cases instead of only ideal examples. In this case: One in-context demonstration is one-shot prompting, not parameter adaptation.
- **D:** Correct. One-shot prompting includes one example. It is different from a training update and may not cover important task variation. In this case: One in-context demonstration is one-shot prompting, not parameter adaptation.

### Question 18 — C

Answer: Use supported thinking or effort controls after measuring task benefit. Reasoning configuration support and interaction rules vary across models and versions. Reasoning-related features and parameters vary by model and provider. Evaluate quality, latency, and cost rather than assume every release accepts the same switches. Local study-map skill 5.1 (LLM Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. When a model or feature requires returned context or signed thinking blocks, follow that version-specific contract. Do not edit signed blocks or manufacture hidden reasoning. In this case: Reasoning configuration support and interaction rules vary across models and versions.
- **B:** Incorrect for this question. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. In this case: Reasoning configuration support and interaction rules vary across models and versions.
- **C:** Correct. Reasoning-related features and parameters vary by model and provider. Evaluate quality, latency, and cost rather than assume every release accepts the same switches. In this case: Reasoning configuration support and interaction rules vary across models and versions.
- **D:** Incorrect for this question. Temperature changes next-token sampling behavior where supported. Lowering it does not independently guarantee correct extraction, grounding, or identical execution. In this case: Reasoning configuration support and interaction rules vary across models and versions.

### Question 19 — B

Answer: Allow for output variability and validate outcomes. Valid outputs can vary, so outcome-oriented validation may be more appropriate than exact-string equality. Repeated calls can differ, even with low sampling settings. Seeds or low temperature do not establish universal cross-version determinism or factual accuracy. Local study-map skill 5.1 (LLM Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Valid outputs can vary, so outcome-oriented validation may be more appropriate than exact-string equality.
- **B:** Correct. Repeated calls can differ, even with low sampling settings. Seeds or low temperature do not establish universal cross-version determinism or factual accuracy. In this case: Valid outputs can vary, so outcome-oriented validation may be more appropriate than exact-string equality.
- **C:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Valid outputs can vary, so outcome-oriented validation may be more appropriate than exact-string equality.
- **D:** Incorrect for this question. Temperature changes next-token sampling behavior where supported. Lowering it does not independently guarantee correct extraction, grounding, or identical execution. In this case: Valid outputs can vary, so outcome-oriented validation may be more appropriate than exact-string equality.

### Question 20 — D

Answer: Budget instructions, evidence, history, and generation together. Reserve instructions, evidence, history, and generation capacity according to the actual service contract. Follow the chosen model and service limits. Overflow handling varies; it is not universally automatic oldest-message deletion. Local study-map skill 5.1 (LLM Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Reserve instructions, evidence, history, and generation capacity according to the actual service contract.
- **B:** Incorrect for this question. A token-count endpoint or compatible estimator can help plan requests. Include hidden overhead allowed by the documented interface and verify actual usage afterward. In this case: Reserve instructions, evidence, history, and generation capacity according to the actual service contract.
- **C:** Incorrect for this question. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: Reserve instructions, evidence, history, and generation capacity according to the actual service contract.
- **D:** Correct. Follow the chosen model and service limits. Overflow handling varies; it is not universally automatic oldest-message deletion. In this case: Reserve instructions, evidence, history, and generation capacity according to the actual service contract.

### Question 21 — C

Answer: Use a provider-specific adapter behind a stable application interface. An adapter can isolate provider and SDK details behind a stable application contract. Different hosting providers can use distinct authentication, endpoints, identifiers, and supported features. Normalize the application contract without assuming identical wire protocols. Local study-map skill 5.2 (Technical Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: An adapter can isolate provider and SDK details behind a stable application contract.
- **B:** Incorrect for this question. A REST integration must respect its actual endpoint contract. HTTP 200 does not establish that the requested business operation succeeded semantically. In this case: An adapter can isolate provider and SDK details behind a stable application contract.
- **C:** Correct. Different hosting providers can use distinct authentication, endpoints, identifiers, and supported features. Normalize the application contract without assuming identical wire protocols. In this case: An adapter can isolate provider and SDK details behind a stable application contract.
- **D:** Incorrect for this question. Use the selected API contract for model, instructions, messages, and typed content. Do not assume a consumer chat interface and a developer API share implicit state. In this case: An adapter can isolate provider and SDK details behind a stable application contract.

### Question 22 — C

Answer: Apply HTTP method, status, authentication, and payload contracts. HTTP and payload semantics remain relevant even when an SDK abstracts transport. A REST integration must respect its actual endpoint contract. HTTP 200 does not establish that the requested business operation succeeded semantically. Local study-map skill 5.2 (Technical Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Check serialized requests, content blocks, status handling, and representative responses. Mock success alone may not reveal a malformed real request or unsupported provider feature. In this case: HTTP and payload semantics remain relevant even when an SDK abstracts transport.
- **B:** Incorrect for this question. Different hosting providers can use distinct authentication, endpoints, identifiers, and supported features. Normalize the application contract without assuming identical wire protocols. In this case: HTTP and payload semantics remain relevant even when an SDK abstracts transport.
- **C:** Correct. A REST integration must respect its actual endpoint contract. HTTP 200 does not establish that the requested business operation succeeded semantically. In this case: HTTP and payload semantics remain relevant even when an SDK abstracts transport.
- **D:** Incorrect for this question. Use the selected API contract for model, instructions, messages, and typed content. Do not assume a consumer chat interface and a developer API share implicit state. In this case: HTTP and payload semantics remain relevant even when an SDK abstracts transport.

### Question 23 — D

Answer: Use WebSockets for an explicitly bidirectional persistent channel. WebSockets can serve a bidirectional application channel, unlike one-way event delivery alone. WebSockets can fit bidirectional application communication, but the documented standard Messages streaming interface is SSE. Do not confuse a transport choice with model capability. Local study-map skill 5.2 (Technical Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Await network operations without blocking an event loop, while limiting in-flight work and respecting service capacity. Creating a coroutine does not mean it has run. In this case: WebSockets can serve a bidirectional application channel, unlike one-way event delivery alone.
- **B:** Incorrect for this question. The documented streaming interface emits SSE events over HTTP. It is not inherently a WebSocket connection or one valid JSON object per arbitrary network chunk. In this case: WebSockets can serve a bidirectional application channel, unlike one-way event delivery alone.
- **C:** Incorrect for this question. A REST integration must respect its actual endpoint contract. HTTP 200 does not establish that the requested business operation succeeded semantically. In this case: WebSockets can serve a bidirectional application channel, unlike one-way event delivery alone.
- **D:** Correct. WebSockets can fit bidirectional application communication, but the documented standard Messages streaming interface is SSE. Do not confuse a transport choice with model capability. In this case: WebSockets can serve a bidirectional application channel, unlike one-way event delivery alone.

### Question 24 — C

Answer: Consume the Messages stream as server-sent events. The documented Messages stream uses server-sent events rather than an implicit WebSocket connection. The documented streaming interface emits SSE events over HTTP. It is not inherently a WebSocket connection or one valid JSON object per arbitrary network chunk. Local study-map skill 5.2 (Technical Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Await network operations without blocking an event loop, while limiting in-flight work and respecting service capacity. Creating a coroutine does not mean it has run. In this case: The documented Messages stream uses server-sent events rather than an implicit WebSocket connection.
- **B:** Incorrect for this question. WebSockets can fit bidirectional application communication, but the documented standard Messages streaming interface is SSE. Do not confuse a transport choice with model capability. In this case: The documented Messages stream uses server-sent events rather than an implicit WebSocket connection.
- **C:** Correct. The documented streaming interface emits SSE events over HTTP. It is not inherently a WebSocket connection or one valid JSON object per arbitrary network chunk. In this case: The documented Messages stream uses server-sent events rather than an implicit WebSocket connection.
- **D:** Incorrect for this question. A REST integration must respect its actual endpoint contract. HTTP 200 does not establish that the requested business operation succeeded semantically. In this case: The documented Messages stream uses server-sent events rather than an implicit WebSocket connection.

### Question 25 — D

Answer: Use asynchronous I/O with bounded concurrency. Await asynchronous network operations while enforcing suitable concurrency limits. Await network operations without blocking an event loop, while limiting in-flight work and respecting service capacity. Creating a coroutine does not mean it has run. Local study-map skill 5.2 (Technical Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Await asynchronous network operations while enforcing suitable concurrency limits.
- **B:** Incorrect for this question. Limit queued and active work so slow consumers or provider limits do not exhaust memory or connections. Unbounded parallelism is not a capacity plan. In this case: Await asynchronous network operations while enforcing suitable concurrency limits.
- **C:** Incorrect for this question. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: Await asynchronous network operations while enforcing suitable concurrency limits.
- **D:** Correct. Await network operations without blocking an event loop, while limiting in-flight work and respecting service capacity. Creating a coroutine does not mean it has run. In this case: Await asynchronous network operations while enforcing suitable concurrency limits.

### Question 26 — B

Answer: Bound work queues and apply backpressure. Bound queues and signal backpressure rather than allow memory growth without limit. Limit queued and active work so slow consumers or provider limits do not exhaust memory or connections. Unbounded parallelism is not a capacity plan. Local study-map skill 5.2 (Technical Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Await network operations without blocking an event loop, while limiting in-flight work and respecting service capacity. Creating a coroutine does not mean it has run. In this case: Bound queues and signal backpressure rather than allow memory growth without limit.
- **B:** Correct. Limit queued and active work so slow consumers or provider limits do not exhaust memory or connections. Unbounded parallelism is not a capacity plan. In this case: Bound queues and signal backpressure rather than allow memory growth without limit.
- **C:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: Bound queues and signal backpressure rather than allow memory growth without limit.
- **D:** Incorrect for this question. Budgets bound runaway execution but are separate from protocol-based completion. Reaching a budget should yield an explicit incomplete or escalation state. In this case: Bound queues and signal backpressure rather than allow memory growth without limit.

### Question 27 — A

Answer: Test the integration contract at the provider boundary. Contract tests check actual request and response expectations beyond a mocked success path. Check serialized requests, content blocks, status handling, and representative responses. Mock success alone may not reveal a malformed real request or unsupported provider feature. Local study-map skill 5.2 (Technical Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Correct. Check serialized requests, content blocks, status handling, and representative responses. Mock success alone may not reveal a malformed real request or unsupported provider feature. In this case: Contract tests check actual request and response expectations beyond a mocked success path.
- **B:** Incorrect for this question. Inject timeouts, malformed responses, and provider failures without live side effects. Combine with contract and representative integration tests rather than infer complete correctness from mocks. In this case: Contract tests check actual request and response expectations beyond a mocked success path.
- **C:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Contract tests check actual request and response expectations beyond a mocked success path.
- **D:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Contract tests check actual request and response expectations beyond a mocked success path.

### Question 28 — B

Answer: Pin compatible model, SDK, prompt, and dependency versions. Record and pin compatible behavior-relevant dependencies rather than leave versions implicit. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. Local study-map skill 5.2 (Technical Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: Record and pin compatible behavior-relevant dependencies rather than leave versions implicit.
- **B:** Correct. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Record and pin compatible behavior-relevant dependencies rather than leave versions implicit.
- **C:** Incorrect for this question. Plugins can change tools and workflow behavior. Track provenance, versions, compatibility, and permissions rather than install unreviewed code merely because a model suggests it. In this case: Record and pin compatible behavior-relevant dependencies rather than leave versions implicit.
- **D:** Incorrect for this question. Different hosting providers can use distinct authentication, endpoints, identifiers, and supported features. Normalize the application contract without assuming identical wire protocols. In this case: Record and pin compatible behavior-relevant dependencies rather than leave versions implicit.

### Question 29 — A

Answer: Set explicit deadlines and classify timeout outcomes. Explicit deadlines define when waiting is no longer useful and trigger safe handling. Bound user and dependency waits. A timeout is an uncertain execution outcome for mutations and may require status reconciliation rather than blind retry. Local study-map skill 5.2 (Technical Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Correct. Bound user and dependency waits. A timeout is an uncertain execution outcome for mutations and may require status reconciliation rather than blind retry. In this case: Explicit deadlines define when waiting is no longer useful and trigger safe handling.
- **B:** Incorrect for this question. Local cancellation limits waiting or computation but does not guarantee the server stopped or a remote side effect was rolled back. In this case: Explicit deadlines define when waiting is no longer useful and trigger safe handling.
- **C:** Incorrect for this question. Nested automatic retries can multiply attempts and latency. Set a shared attempt or elapsed-time budget and inspect SDK defaults. In this case: Explicit deadlines define when waiting is no longer useful and trigger safe handling.
- **D:** Incorrect for this question. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: Explicit deadlines define when waiting is no longer useful and trigger safe handling.

### Question 30 — D

Answer: Coordinate retries across SDK and application layers. Treat retries as one aggregate budget rather than independent nested loops. Nested automatic retries can multiply attempts and latency. Set a shared attempt or elapsed-time budget and inspect SDK defaults. Local study-map skill 5.2 (Technical Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Temporary availability or rate-limit conditions may permit delayed retry. Follow provider guidance and distinguish retries from unsafe duplication of side effects. In this case: Treat retries as one aggregate budget rather than independent nested loops.
- **B:** Incorrect for this question. Limit queued and active work so slow consumers or provider limits do not exhaust memory or connections. Unbounded parallelism is not a capacity plan. In this case: Treat retries as one aggregate budget rather than independent nested loops.
- **C:** Incorrect for this question. Bound user and dependency waits. A timeout is an uncertain execution outcome for mutations and may require status reconciliation rather than blind retry. In this case: Treat retries as one aggregate budget rather than independent nested loops.
- **D:** Correct. Nested automatic retries can multiply attempts and latency. Set a shared attempt or elapsed-time budget and inspect SDK defaults. In this case: Treat retries as one aggregate budget rather than independent nested loops.

### Question 31 — B

Answer: Accumulate deltas by block index before final validation. Accumulate valid event and block deltas rather than assume chunks contain complete objects. Network chunks and content deltas can contain partial strings or JSON. Track event and block boundaries or use SDK helpers before consuming a complete structured value. Local study-map skill 5.2 (Technical Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. The documented streaming interface emits SSE events over HTTP. It is not inherently a WebSocket connection or one valid JSON object per arbitrary network chunk. In this case: Accumulate valid event and block deltas rather than assume chunks contain complete objects.
- **B:** Correct. Network chunks and content deltas can contain partial strings or JSON. Track event and block boundaries or use SDK helpers before consuming a complete structured value. In this case: Accumulate valid event and block deltas rather than assume chunks contain complete objects.
- **C:** Incorrect for this question. SDK accumulation helpers can provide the complete message. Inspect termination and errors before treating the resulting object as accepted application output. In this case: Accumulate valid event and block deltas rather than assume chunks contain complete objects.
- **D:** Incorrect for this question. A response can contain text, tool use, thinking, or other supported blocks. Do not assume content is one string or that the first block is always displayable text. In this case: Accumulate valid event and block deltas rather than assume chunks contain complete objects.

### Question 32 — A

Answer: Dispatch response content according to each block type. Process each supported block type under the actual API contract. A response can contain text, tool use, thinking, or other supported blocks. Do not assume content is one string or that the first block is always displayable text. Local study-map skill 5.2 (Technical Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Correct. A response can contain text, tool use, thinking, or other supported blocks. Do not assume content is one string or that the first block is always displayable text. In this case: Process each supported block type under the actual API contract.
- **B:** Incorrect for this question. SDK accumulation helpers can provide the complete message. Inspect termination and errors before treating the resulting object as accepted application output. In this case: Process each supported block type under the actual API contract.
- **C:** Incorrect for this question. Network chunks and content deltas can contain partial strings or JSON. Track event and block boundaries or use SDK helpers before consuming a complete structured value. In this case: Process each supported block type under the actual API contract.
- **D:** Incorrect for this question. Use the selected API contract for model, instructions, messages, and typed content. Do not assume a consumer chat interface and a developer API share implicit state. In this case: Process each supported block type under the actual API contract.

### Question 33 — B

Answer: Inspect a redacted end-to-end request and tool trace. Trace actual requests, retries, tool actions, and usage rather than infer from model names alone. Correlate the actual request, model response, tool execution, retries, and validation results. Diagnose the first failing boundary rather than infer cause from the final prose. Local study-map skill 5.2 (Technical Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Inject timeouts, malformed responses, and provider failures without live side effects. Combine with contract and representative integration tests rather than infer complete correctness from mocks. In this case: Trace actual requests, retries, tool actions, and usage rather than infer from model names alone.
- **B:** Correct. Correlate the actual request, model response, tool execution, retries, and validation results. Diagnose the first failing boundary rather than infer cause from the final prose. In this case: Trace actual requests, retries, tool actions, and usage rather than infer from model names alone.
- **C:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Trace actual requests, retries, tool actions, and usage rather than infer from model names alone.
- **D:** Incorrect for this question. Link a user task to provider requests, worker runs, and actions without using sensitive content as an identifier. Protect telemetry access and retention. In this case: Trace actual requests, retries, tool actions, and usage rather than infer from model names alone.

### Question 34 — B

Answer: Use a durable idempotency key for the same logical action. A stable logical-action key can prevent duplicated external effects across retries. Where supported, repeated requests for one operation should resolve to one intended external effect. Generating a new key for each retry defeats duplicate protection. Local study-map skill 5.2 (Technical Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Bound user and dependency waits. A timeout is an uncertain execution outcome for mutations and may require status reconciliation rather than blind retry. In this case: A stable logical-action key can prevent duplicated external effects across retries.
- **B:** Correct. Where supported, repeated requests for one operation should resolve to one intended external effect. Generating a new key for each retry defeats duplicate protection. In this case: A stable logical-action key can prevent duplicated external effects across retries.
- **C:** Incorrect for this question. Local cancellation limits waiting or computation but does not guarantee the server stopped or a remote side effect was rolled back. In this case: A stable logical-action key can prevent duplicated external effects across retries.
- **D:** Incorrect for this question. Separate a generated proposal from an authorized atomic or otherwise well-coordinated business effect. Define conflict handling and rollback or compensation behavior. In this case: A stable logical-action key can prevent duplicated external effects across retries.

### Question 35 — B

Answer: Cancel local work and reconcile any external operation separately. Local cancellation and remote effect reconciliation must be treated separately. Local cancellation limits waiting or computation but does not guarantee the server stopped or a remote side effect was rolled back. Local study-map skill 5.2 (Technical Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Separate a generated proposal from an authorized atomic or otherwise well-coordinated business effect. Define conflict handling and rollback or compensation behavior. In this case: Local cancellation and remote effect reconciliation must be treated separately.
- **B:** Correct. Local cancellation limits waiting or computation but does not guarantee the server stopped or a remote side effect was rolled back. In this case: Local cancellation and remote effect reconciliation must be treated separately.
- **C:** Incorrect for this question. Where supported, repeated requests for one operation should resolve to one intended external effect. Generating a new key for each retry defeats duplicate protection. In this case: Local cancellation and remote effect reconciliation must be treated separately.
- **D:** Incorrect for this question. Bound user and dependency waits. A timeout is an uncertain execution outcome for mutations and may require status reconciliation rather than blind retry. In this case: Local cancellation and remote effect reconciliation must be treated separately.

### Question 36 — D

Answer: Use a provider-specific adapter behind a stable application interface. A provider-specific adapter should normalize supported contracts without claiming identical interfaces. Different hosting providers can use distinct authentication, endpoints, identifiers, and supported features. Normalize the application contract without assuming identical wire protocols. Local study-map skill 5.2 (Technical Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: A provider-specific adapter should normalize supported contracts without claiming identical interfaces.
- **B:** Incorrect for this question. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. In this case: A provider-specific adapter should normalize supported contracts without claiming identical interfaces.
- **C:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: A provider-specific adapter should normalize supported contracts without claiming identical interfaces.
- **D:** Correct. Different hosting providers can use distinct authentication, endpoints, identifiers, and supported features. Normalize the application contract without assuming identical wire protocols. In this case: A provider-specific adapter should normalize supported contracts without claiming identical interfaces.

### Question 37 — A

Answer: Propagate correlation identifiers across requests and tools. Correlation identifiers enable traceable accounting without using private text as a key. Link a user task to provider requests, worker runs, and actions without using sensitive content as an identifier. Protect telemetry access and retention. Local study-map skill 5.2 (Technical Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Correct. Link a user task to provider requests, worker runs, and actions without using sensitive content as an identifier. Protect telemetry access and retention. In this case: Correlation identifiers enable traceable accounting without using private text as a key.
- **B:** Incorrect for this question. Correlate the actual request, model response, tool execution, retries, and validation results. Diagnose the first failing boundary rather than infer cause from the final prose. In this case: Correlation identifiers enable traceable accounting without using private text as a key.
- **C:** Incorrect for this question. Structured finding metadata enables analysis of recurring false positives and targeted prompt improvement. A generic accept/reject count loses diagnostic detail. In this case: Correlation identifiers enable traceable accounting without using private text as a key.
- **D:** Incorrect for this question. Audit records support attribution and reconstruction of consequential actions. Limit access, sensitive content, and retention; they do not themselves block an effect. In this case: Correlation identifiers enable traceable accounting without using private text as a key.

### Question 38 — B

Answer: Separate environment configuration from application logic. Keep environment settings explicit and validated rather than embed them in application logic. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. Local study-map skill 5.2 (Technical Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Plugins can change tools and workflow behavior. Track provenance, versions, compatibility, and permissions rather than install unreviewed code merely because a model suggests it. In this case: Keep environment settings explicit and validated rather than embed them in application logic.
- **B:** Correct. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: Keep environment settings explicit and validated rather than embed them in application logic.
- **C:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Keep environment settings explicit and validated rather than embed them in application logic.
- **D:** Incorrect for this question. Different hosting providers can use distinct authentication, endpoints, identifiers, and supported features. Normalize the application contract without assuming identical wire protocols. In this case: Keep environment settings explicit and validated rather than embed them in application logic.

### Question 39 — C

Answer: Use controlled stubs for repeatable failure-path tests. Use controlled stubs for deterministic failure injection alongside boundary tests. Inject timeouts, malformed responses, and provider failures without live side effects. Combine with contract and representative integration tests rather than infer complete correctness from mocks. Local study-map skill 5.2 (Technical Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Use controlled stubs for deterministic failure injection alongside boundary tests.
- **B:** Incorrect for this question. Expected behavior and edge cases make revisions checkable. A passing narrow suite is not proof of complete correctness or security. In this case: Use controlled stubs for deterministic failure injection alongside boundary tests.
- **C:** Correct. Inject timeouts, malformed responses, and provider failures without live side effects. Combine with contract and representative integration tests rather than infer complete correctness from mocks. In this case: Use controlled stubs for deterministic failure injection alongside boundary tests.
- **D:** Incorrect for this question. Check serialized requests, content blocks, status handling, and representative responses. Mock success alone may not reveal a malformed real request or unsupported provider feature. In this case: Use controlled stubs for deterministic failure injection alongside boundary tests.

### Question 40 — A

Answer: Isolate model-output defects from integration defects. The defect is an integration calculation, not necessarily the model output. Check whether correct raw output was lost or changed by serialization, parsing, routing, or persistence. Not every visible error is fixed by changing the prompt. Local study-map skill 5.2 (Technical Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Correct. Check whether correct raw output was lost or changed by serialization, parsing, routing, or persistence. Not every visible error is fixed by changing the prompt. In this case: The defect is an integration calculation, not necessarily the model output.
- **B:** Incorrect for this question. Concrete categories, severity thresholds, and exclusions are more actionable than vague requests to be careful. Evaluate precision and recall rather than assume compliance. In this case: The defect is an integration calculation, not necessarily the model output.
- **C:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: The defect is an integration calculation, not necessarily the model output.
- **D:** Incorrect for this question. Correlate the actual request, model response, tool execution, retries, and validation results. Diagnose the first failing boundary rather than infer cause from the final prose. In this case: The defect is an integration calculation, not necessarily the model output.

### Question 41 — D

Answer: Evaluate Haiku for suitable speed- and efficiency-oriented tasks. Haiku can be evaluated for efficiency-oriented tasks, with actual version-specific outcomes measured. Model-family positioning is a starting hypothesis, not proof of fit. Use a specific supported version and measure the required quality, cost, and latency. Local study-map skill 5.3 (Model Selection and Tradeoffs), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Reasoning-related features and parameters vary by model and provider. Evaluate quality, latency, and cost rather than assume every release accepts the same switches. In this case: Haiku can be evaluated for efficiency-oriented tasks, with actual version-specific outcomes measured.
- **B:** Incorrect for this question. A high-capability model may help difficult tasks, but size or family alone does not guarantee accuracy, acceptable latency, or economical deployment. In this case: Haiku can be evaluated for efficiency-oriented tasks, with actual version-specific outcomes measured.
- **C:** Incorrect for this question. A balanced model may suit many development workflows, but the actual selected release and workload requirements determine fitness. In this case: Haiku can be evaluated for efficiency-oriented tasks, with actual version-specific outcomes measured.
- **D:** Correct. Model-family positioning is a starting hypothesis, not proof of fit. Use a specific supported version and measure the required quality, cost, and latency. In this case: Haiku can be evaluated for efficiency-oriented tasks, with actual version-specific outcomes measured.

### Question 42 — C

Answer: Evaluate Sonnet for a measured balance of capability and efficiency. Sonnet may fit balanced workloads, but representative task evaluation must confirm suitability. A balanced model may suit many development workflows, but the actual selected release and workload requirements determine fitness. Local study-map skill 5.3 (Model Selection and Tradeoffs), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. A high-capability model may help difficult tasks, but size or family alone does not guarantee accuracy, acceptable latency, or economical deployment. In this case: Sonnet may fit balanced workloads, but representative task evaluation must confirm suitability.
- **B:** Incorrect for this question. Model-family positioning is a starting hypothesis, not proof of fit. Use a specific supported version and measure the required quality, cost, and latency. In this case: Sonnet may fit balanced workloads, but representative task evaluation must confirm suitability.
- **C:** Correct. A balanced model may suit many development workflows, but the actual selected release and workload requirements determine fitness. In this case: Sonnet may fit balanced workloads, but representative task evaluation must confirm suitability.
- **D:** Incorrect for this question. Reasoning-related features and parameters vary by model and provider. Evaluate quality, latency, and cost rather than assume every release accepts the same switches. In this case: Sonnet may fit balanced workloads, but representative task evaluation must confirm suitability.

### Question 43 — B

Answer: Evaluate Opus for demanding capability-oriented work. Opus can be tested for demanding capability needs rather than assumed universally superior. A high-capability model may help difficult tasks, but size or family alone does not guarantee accuracy, acceptable latency, or economical deployment. Local study-map skill 5.3 (Model Selection and Tradeoffs), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Reasoning-related features and parameters vary by model and provider. Evaluate quality, latency, and cost rather than assume every release accepts the same switches. In this case: Opus can be tested for demanding capability needs rather than assumed universally superior.
- **B:** Correct. A high-capability model may help difficult tasks, but size or family alone does not guarantee accuracy, acceptable latency, or economical deployment. In this case: Opus can be tested for demanding capability needs rather than assumed universally superior.
- **C:** Incorrect for this question. Model-family positioning is a starting hypothesis, not proof of fit. Use a specific supported version and measure the required quality, cost, and latency. In this case: Opus can be tested for demanding capability needs rather than assumed universally superior.
- **D:** Incorrect for this question. A balanced model may suit many development workflows, but the actual selected release and workload requirements determine fitness. In this case: Opus can be tested for demanding capability needs rather than assumed universally superior.

### Question 44 — D

Answer: Select the least costly configuration that meets required outcomes. Select a specific configuration using measured outcomes and required operational constraints. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. Local study-map skill 5.3 (Model Selection and Tradeoffs), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Model-family positioning is a starting hypothesis, not proof of fit. Use a specific supported version and measure the required quality, cost, and latency. In this case: Select a specific configuration using measured outcomes and required operational constraints.
- **B:** Incorrect for this question. A high-capability model may help difficult tasks, but size or family alone does not guarantee accuracy, acceptable latency, or economical deployment. In this case: Select a specific configuration using measured outcomes and required operational constraints.
- **C:** Incorrect for this question. A balanced model may suit many development workflows, but the actual selected release and workload requirements determine fitness. In this case: Select a specific configuration using measured outcomes and required operational constraints.
- **D:** Correct. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. In this case: Select a specific configuration using measured outcomes and required operational constraints.

### Question 45 — D

Answer: Route requests using evaluated task classes and safe fallbacks. Evidence-based task routing can send each class to a suitable model with safe fallback. Use evidence-based routing to suitable configurations, monitor misclassification, and define fallback. Routing complexity must justify its own operating cost. Local study-map skill 5.3 (Model Selection and Tradeoffs), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Model-family positioning is a starting hypothesis, not proof of fit. Use a specific supported version and measure the required quality, cost, and latency. In this case: Evidence-based task routing can send each class to a suitable model with safe fallback.
- **B:** Incorrect for this question. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. In this case: Evidence-based task routing can send each class to a suitable model with safe fallback.
- **C:** Incorrect for this question. A high-capability model may help difficult tasks, but size or family alone does not guarantee accuracy, acceptable latency, or economical deployment. In this case: Evidence-based task routing can send each class to a suitable model with safe fallback.
- **D:** Correct. Use evidence-based routing to suitable configurations, monitor misclassification, and define fallback. Routing complexity must justify its own operating cost. In this case: Evidence-based task routing can send each class to a suitable model with safe fallback.

### Question 46 — C

Answer: Canary a version change with regression gates and rollback. Canary the actual workload and preserve a rollback path before broad exposure. Stage exposure to the new configuration, compare required outcomes, and retain a known-good path. A vendor release note is not workload validation. Local study-map skill 5.3 (Model Selection and Tradeoffs), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. In this case: Canary the actual workload and preserve a rollback path before broad exposure.
- **B:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Canary the actual workload and preserve a rollback path before broad exposure.
- **C:** Correct. Stage exposure to the new configuration, compare required outcomes, and retain a known-good path. A vendor release note is not workload validation. In this case: Canary the actual workload and preserve a rollback path before broad exposure.
- **D:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Canary the actual workload and preserve a rollback path before broad exposure.

### Question 47 — C

Answer: Use a versioned representative held-out evaluation set. Use representative held-out cases rather than assume curated demonstrations establish production fitness. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. Local study-map skill 5.3 (Model Selection and Tradeoffs), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Use evidence-based routing to suitable configurations, monitor misclassification, and define fallback. Routing complexity must justify its own operating cost. In this case: Use representative held-out cases rather than assume curated demonstrations establish production fitness.
- **B:** Incorrect for this question. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. In this case: Use representative held-out cases rather than assume curated demonstrations establish production fitness.
- **C:** Correct. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Use representative held-out cases rather than assume curated demonstrations establish production fitness.
- **D:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Use representative held-out cases rather than assume curated demonstrations establish production fitness.

### Question 48 — C

Answer: Use supported thinking or effort controls after measuring task benefit. Measure where thinking benefit justifies its latency and cost instead of universal activation. Reasoning-related features and parameters vary by model and provider. Evaluate quality, latency, and cost rather than assume every release accepts the same switches. Local study-map skill 5.3 (Model Selection and Tradeoffs), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. In this case: Measure where thinking benefit justifies its latency and cost instead of universal activation.
- **B:** Incorrect for this question. Temperature changes next-token sampling behavior where supported. Lowering it does not independently guarantee correct extraction, grounding, or identical execution. In this case: Measure where thinking benefit justifies its latency and cost instead of universal activation.
- **C:** Correct. Reasoning-related features and parameters vary by model and provider. Evaluate quality, latency, and cost rather than assume every release accepts the same switches. In this case: Measure where thinking benefit justifies its latency and cost instead of universal activation.
- **D:** Incorrect for this question. Use evidence-based routing to suitable configurations, monitor misclassification, and define fallback. Routing complexity must justify its own operating cost. In this case: Measure where thinking benefit justifies its latency and cost instead of universal activation.

### Question 49 — A

Answer: Pin compatible model, SDK, prompt, and dependency versions. Track a compatible explicit model version along with related application configuration. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. Local study-map skill 5.3 (Model Selection and Tradeoffs), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Correct. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Track a compatible explicit model version along with related application configuration.
- **B:** Incorrect for this question. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. In this case: Track a compatible explicit model version along with related application configuration.
- **C:** Incorrect for this question. Validate configuration at startup and keep environments explicit. Do not hard-code secrets or assume development and production identifiers are interchangeable. In this case: Track a compatible explicit model version along with related application configuration.
- **D:** Incorrect for this question. Stage exposure to the new configuration, compare required outcomes, and retain a known-good path. A vendor release note is not workload validation. In this case: Track a compatible explicit model version along with related application configuration.

### Question 50 — C

Answer: Select the least costly configuration that meets required outcomes. A configuration must satisfy required outcomes before its price advantage matters. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. Local study-map skill 5.3 (Model Selection and Tradeoffs), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. An acceptable mean can hide slow requests that violate user requirements. Define percentile measurements and end-to-end boundaries consistently. In this case: A configuration must satisfy required outcomes before its price advantage matters.
- **B:** Incorrect for this question. Include failed attempts, retries, review, tool work, and operating overhead rather than compare only listed unit token rates. In this case: A configuration must satisfy required outcomes before its price advantage matters.
- **C:** Correct. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. In this case: A configuration must satisfy required outcomes before its price advantage matters.
- **D:** Incorrect for this question. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. In this case: A configuration must satisfy required outcomes before its price advantage matters.

### Question 51 — A

Answer: Measure tail latency as well as average latency. Tail latency can reveal failures hidden by an average. An acceptable mean can hide slow requests that violate user requirements. Define percentile measurements and end-to-end boundaries consistently. Local study-map skill 5.3 (Model Selection and Tradeoffs), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Correct. An acceptable mean can hide slow requests that violate user requirements. Define percentile measurements and end-to-end boundaries consistently. In this case: Tail latency can reveal failures hidden by an average.
- **B:** Incorrect for this question. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. In this case: Tail latency can reveal failures hidden by an average.
- **C:** Incorrect for this question. Streaming can improve perceived responsiveness without reducing total generation or external-tool time. First-token delay and total duration measure different things. In this case: Tail latency can reveal failures hidden by an average.
- **D:** Incorrect for this question. Include failed attempts, retries, review, tool work, and operating overhead rather than compare only listed unit token rates. In this case: Tail latency can reveal failures hidden by an average.

### Question 52 — A

Answer: Measure time to first token separately from full completion. Time to first token separates startup delay from full response duration. Streaming can improve perceived responsiveness without reducing total generation or external-tool time. First-token delay and total duration measure different things. Local study-map skill 5.3 (Model Selection and Tradeoffs), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Correct. Streaming can improve perceived responsiveness without reducing total generation or external-tool time. First-token delay and total duration measure different things. In this case: Time to first token separates startup delay from full response duration.
- **B:** Incorrect for this question. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. In this case: Time to first token separates startup delay from full response duration.
- **C:** Incorrect for this question. Include failed attempts, retries, review, tool work, and operating overhead rather than compare only listed unit token rates. In this case: Time to first token separates startup delay from full response duration.
- **D:** Incorrect for this question. An acceptable mean can hide slow requests that violate user requirements. Define percentile measurements and end-to-end boundaries consistently. In this case: Time to first token separates startup delay from full response duration.

### Question 53 — D

Answer: Select the least costly configuration that meets required outcomes. Choose the least costly verified suitable configuration rather than maximize size. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. Local study-map skill 5.3 (Model Selection and Tradeoffs), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Model-family positioning is a starting hypothesis, not proof of fit. Use a specific supported version and measure the required quality, cost, and latency. In this case: Choose the least costly verified suitable configuration rather than maximize size.
- **B:** Incorrect for this question. A high-capability model may help difficult tasks, but size or family alone does not guarantee accuracy, acceptable latency, or economical deployment. In this case: Choose the least costly verified suitable configuration rather than maximize size.
- **C:** Incorrect for this question. A balanced model may suit many development workflows, but the actual selected release and workload requirements determine fitness. In this case: Choose the least costly verified suitable configuration rather than maximize size.
- **D:** Correct. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. In this case: Choose the least costly verified suitable configuration rather than maximize size.

### Question 54 — D

Answer: Route requests using evaluated task classes and safe fallbacks. Evaluate routing and fallback against actual task classes and misclassification risk. Use evidence-based routing to suitable configurations, monitor misclassification, and define fallback. Routing complexity must justify its own operating cost. Local study-map skill 5.3 (Model Selection and Tradeoffs), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. In this case: Evaluate routing and fallback against actual task classes and misclassification risk.
- **B:** Incorrect for this question. Reasoning-related features and parameters vary by model and provider. Evaluate quality, latency, and cost rather than assume every release accepts the same switches. In this case: Evaluate routing and fallback against actual task classes and misclassification risk.
- **C:** Incorrect for this question. Stage exposure to the new configuration, compare required outcomes, and retain a known-good path. A vendor release note is not workload validation. In this case: Evaluate routing and fallback against actual task classes and misclassification risk.
- **D:** Correct. Use evidence-based routing to suitable configurations, monitor misclassification, and define fallback. Routing complexity must justify its own operating cost. In this case: Evaluate routing and fallback against actual task classes and misclassification risk.

### Question 55 — C

Answer: Canary a version change with regression gates and rollback. Regression gates and controlled exposure can catch breaking behavior before full rollout. Stage exposure to the new configuration, compare required outcomes, and retain a known-good path. A vendor release note is not workload validation. Local study-map skill 5.3 (Model Selection and Tradeoffs), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Regression gates and controlled exposure can catch breaking behavior before full rollout.
- **B:** Incorrect for this question. Use evidence-based routing to suitable configurations, monitor misclassification, and define fallback. Routing complexity must justify its own operating cost. In this case: Regression gates and controlled exposure can catch breaking behavior before full rollout.
- **C:** Correct. Stage exposure to the new configuration, compare required outcomes, and retain a known-good path. A vendor release note is not workload validation. In this case: Regression gates and controlled exposure can catch breaking behavior before full rollout.
- **D:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Regression gates and controlled exposure can catch breaking behavior before full rollout.

### Question 56 — A

Answer: Select the least costly configuration that meets required outcomes. Quality must be considered together with required latency and operational constraints. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. Local study-map skill 5.3 (Model Selection and Tradeoffs), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Correct. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. In this case: Quality must be considered together with required latency and operational constraints.
- **B:** Incorrect for this question. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. In this case: Quality must be considered together with required latency and operational constraints.
- **C:** Incorrect for this question. An acceptable mean can hide slow requests that violate user requirements. Define percentile measurements and end-to-end boundaries consistently. In this case: Quality must be considered together with required latency and operational constraints.
- **D:** Incorrect for this question. Include failed attempts, retries, review, tool work, and operating overhead rather than compare only listed unit token rates. In this case: Quality must be considered together with required latency and operational constraints.

### Question 57 — B

Answer: Use supported thinking or effort controls after measuring task benefit. Capability and parameter support are version- and provider-specific rather than family-wide guarantees. Reasoning-related features and parameters vary by model and provider. Evaluate quality, latency, and cost rather than assume every release accepts the same switches. Local study-map skill 5.3 (Model Selection and Tradeoffs), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Temperature changes next-token sampling behavior where supported. Lowering it does not independently guarantee correct extraction, grounding, or identical execution. In this case: Capability and parameter support are version- and provider-specific rather than family-wide guarantees.
- **B:** Correct. Reasoning-related features and parameters vary by model and provider. Evaluate quality, latency, and cost rather than assume every release accepts the same switches. In this case: Capability and parameter support are version- and provider-specific rather than family-wide guarantees.
- **C:** Incorrect for this question. Repeated calls can differ, even with low sampling settings. Seeds or low temperature do not establish universal cross-version determinism or factual accuracy. In this case: Capability and parameter support are version- and provider-specific rather than family-wide guarantees.
- **D:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Capability and parameter support are version- and provider-specific rather than family-wide guarantees.

### Question 58 — B

Answer: Compare total cost per verified successful outcome. Compare total verified-outcome cost rather than one call's sticker price. Include failed attempts, retries, review, tool work, and operating overhead rather than compare only listed unit token rates. Local study-map skill 5.3 (Model Selection and Tradeoffs), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. In this case: Compare total verified-outcome cost rather than one call's sticker price.
- **B:** Correct. Include failed attempts, retries, review, tool work, and operating overhead rather than compare only listed unit token rates. In this case: Compare total verified-outcome cost rather than one call's sticker price.
- **C:** Incorrect for this question. An acceptable mean can hide slow requests that violate user requirements. Define percentile measurements and end-to-end boundaries consistently. In this case: Compare total verified-outcome cost rather than one call's sticker price.
- **D:** Incorrect for this question. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. In this case: Compare total verified-outcome cost rather than one call's sticker price.

### Question 59 — B

Answer: Use a versioned representative held-out evaluation set. Representative evaluation must include the actual required language distribution and failure cases. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. Local study-map skill 5.3 (Model Selection and Tradeoffs), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Representative evaluation must include the actual required language distribution and failure cases.
- **B:** Correct. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Representative evaluation must include the actual required language distribution and failure cases.
- **C:** Incorrect for this question. Stage exposure to the new configuration, compare required outcomes, and retain a known-good path. A vendor release note is not workload validation. In this case: Representative evaluation must include the actual required language distribution and failure cases.
- **D:** Incorrect for this question. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. In this case: Representative evaluation must include the actual required language distribution and failure cases.

### Question 60 — B

Answer: Select the least costly configuration that meets required outcomes. Use measured workload fitness rather than assume a single family is always optimal. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. Local study-map skill 5.3 (Model Selection and Tradeoffs), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Use evidence-based routing to suitable configurations, monitor misclassification, and define fallback. Routing complexity must justify its own operating cost. In this case: Use measured workload fitness rather than assume a single family is always optimal.
- **B:** Correct. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. In this case: Use measured workload fitness rather than assume a single family is always optimal.
- **C:** Incorrect for this question. Model-family positioning is a starting hypothesis, not proof of fit. Use a specific supported version and measure the required quality, cost, and latency. In this case: Use measured workload fitness rather than assume a single family is always optimal.
- **D:** Incorrect for this question. A high-capability model may help difficult tasks, but size or family alone does not guarantee accuracy, acceptable latency, or economical deployment. In this case: Use measured workload fitness rather than assume a single family is always optimal.

### Question 61 — C

Answer: Track actual usage by token and billing category. Record actual usage by category rather than apply one assumed price to everything. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. Local study-map skill 5.4 (Cost and Token Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Tokens are model-dependent units, not always words or characters. Include actual system, tool, content, and output usage according to the service contract. In this case: Record actual usage by category rather than apply one assumed price to everything.
- **B:** Incorrect for this question. Include failed attempts, retries, review, tool work, and operating overhead rather than compare only listed unit token rates. In this case: Record actual usage by category rather than apply one assumed price to everything.
- **C:** Correct. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. In this case: Record actual usage by category rather than apply one assumed price to everything.
- **D:** Incorrect for this question. A token-count endpoint or compatible estimator can help plan requests. Include hidden overhead allowed by the documented interface and verify actual usage afterward. In this case: Record actual usage by category rather than apply one assumed price to everything.

### Question 62 — C

Answer: Use supported token counting before oversized submission. Use supported model-compatible token counting and verify actual usage afterward. A token-count endpoint or compatible estimator can help plan requests. Include hidden overhead allowed by the documented interface and verify actual usage afterward. Local study-map skill 5.4 (Cost and Token Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Tokens are model-dependent units, not always words or characters. Include actual system, tool, content, and output usage according to the service contract. In this case: Use supported model-compatible token counting and verify actual usage afterward.
- **B:** Incorrect for this question. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. In this case: Use supported model-compatible token counting and verify actual usage afterward.
- **C:** Correct. A token-count endpoint or compatible estimator can help plan requests. Include hidden overhead allowed by the documented interface and verify actual usage afterward. In this case: Use supported model-compatible token counting and verify actual usage afterward.
- **D:** Incorrect for this question. Follow the chosen model and service limits. Overflow handling varies; it is not universally automatic oldest-message deletion. In this case: Use supported model-compatible token counting and verify actual usage afterward.

### Question 63 — B

Answer: Put eligible stable common content before variable input for cache reuse. Eligible repeated common content generally needs stable prefix placement under service rules. Supported prefix caching depends on exact eligible content, placement, checkpoints, model, and service rules. It is not a cross-user final-answer cache. Local study-map skill 5.4 (Cost and Token Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Caching may reduce repeated prefix processing under provider-specific rules. It does not extend the context window, update model weights, or verify an answer. In this case: Eligible repeated common content generally needs stable prefix placement under service rules.
- **B:** Correct. Supported prefix caching depends on exact eligible content, placement, checkpoints, model, and service rules. It is not a cross-user final-answer cache. In this case: Eligible repeated common content generally needs stable prefix placement under service rules.
- **C:** Incorrect for this question. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. In this case: Eligible repeated common content generally needs stable prefix placement under service rules.
- **D:** Incorrect for this question. Repeated text does not prove cache reuse. Check eligible matching, expiration, thresholds, and current prices before claiming savings. In this case: Eligible repeated common content generally needs stable prefix placement under service rules.

### Question 64 — B

Answer: Verify cache reads, writes, and economics in actual usage. Check actual eligibility, checkpoint placement, matching, expiration, and usage rather than assume caching. Repeated text does not prove cache reuse. Check eligible matching, expiration, thresholds, and current prices before claiming savings. Local study-map skill 5.4 (Cost and Token Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Supported prefix caching depends on exact eligible content, placement, checkpoints, model, and service rules. It is not a cross-user final-answer cache. In this case: Check actual eligibility, checkpoint placement, matching, expiration, and usage rather than assume caching.
- **B:** Correct. Repeated text does not prove cache reuse. Check eligible matching, expiration, thresholds, and current prices before claiming savings. In this case: Check actual eligibility, checkpoint placement, matching, expiration, and usage rather than assume caching.
- **C:** Incorrect for this question. A token-count endpoint or compatible estimator can help plan requests. Include hidden overhead allowed by the documented interface and verify actual usage afterward. In this case: Check actual eligibility, checkpoint placement, matching, expiration, and usage rather than assume caching.
- **D:** Incorrect for this question. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. In this case: Check actual eligibility, checkpoint placement, matching, expiration, and usage rather than assume caching.

### Question 65 — D

Answer: Compare total cost per verified successful outcome. Include complete workflow resources when comparing cost per acceptable outcome. Include failed attempts, retries, review, tool work, and operating overhead rather than compare only listed unit token rates. Local study-map skill 5.4 (Cost and Token Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. In this case: Include complete workflow resources when comparing cost per acceptable outcome.
- **B:** Incorrect for this question. An acceptable mean can hide slow requests that violate user requirements. Define percentile measurements and end-to-end boundaries consistently. In this case: Include complete workflow resources when comparing cost per acceptable outcome.
- **C:** Incorrect for this question. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. In this case: Include complete workflow resources when comparing cost per acceptable outcome.
- **D:** Correct. Include failed attempts, retries, review, tool work, and operating overhead rather than compare only listed unit token rates. In this case: Include complete workflow resources when comparing cost per acceptable outcome.

### Question 66 — C

Answer: Budget instructions, evidence, history, and generation together. Allocate capacity across all request components and required output before submission. Follow the chosen model and service limits. Overflow handling varies; it is not universally automatic oldest-message deletion. Local study-map skill 5.4 (Cost and Token Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. A token-count endpoint or compatible estimator can help plan requests. Include hidden overhead allowed by the documented interface and verify actual usage afterward. In this case: Allocate capacity across all request components and required output before submission.
- **B:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Allocate capacity across all request components and required output before submission.
- **C:** Correct. Follow the chosen model and service limits. Overflow handling varies; it is not universally automatic oldest-message deletion. In this case: Allocate capacity across all request components and required output before submission.
- **D:** Incorrect for this question. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: Allocate capacity across all request components and required output before submission.

### Question 67 — C

Answer: Track actual usage by token and billing category. Track each applicable category under current provider terms instead of infer savings from text repetition. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. Local study-map skill 5.4 (Cost and Token Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Supported prefix caching depends on exact eligible content, placement, checkpoints, model, and service rules. It is not a cross-user final-answer cache. In this case: Track each applicable category under current provider terms instead of infer savings from text repetition.
- **B:** Incorrect for this question. A token-count endpoint or compatible estimator can help plan requests. Include hidden overhead allowed by the documented interface and verify actual usage afterward. In this case: Track each applicable category under current provider terms instead of infer savings from text repetition.
- **C:** Correct. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. In this case: Track each applicable category under current provider terms instead of infer savings from text repetition.
- **D:** Incorrect for this question. Repeated text does not prove cache reuse. Check eligible matching, expiration, thresholds, and current prices before claiming savings. In this case: Track each applicable category under current provider terms instead of infer savings from text repetition.

### Question 68 — B

Answer: Put eligible stable common content before variable input for cache reuse. Prefix processing reuse differs from sharing previously generated private final answers. Supported prefix caching depends on exact eligible content, placement, checkpoints, model, and service rules. It is not a cross-user final-answer cache. Local study-map skill 5.4 (Cost and Token Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. In this case: Prefix processing reuse differs from sharing previously generated private final answers.
- **B:** Correct. Supported prefix caching depends on exact eligible content, placement, checkpoints, model, and service rules. It is not a cross-user final-answer cache. In this case: Prefix processing reuse differs from sharing previously generated private final answers.
- **C:** Incorrect for this question. Repeated text does not prove cache reuse. Check eligible matching, expiration, thresholds, and current prices before claiming savings. In this case: Prefix processing reuse differs from sharing previously generated private final answers.
- **D:** Incorrect for this question. Caching may reduce repeated prefix processing under provider-specific rules. It does not extend the context window, update model weights, or verify an answer. In this case: Prefix processing reuse differs from sharing previously generated private final answers.

### Question 69 — A

Answer: Use supported token counting before oversized submission. Use the selected model's supported counting contract rather than an incompatible estimator. A token-count endpoint or compatible estimator can help plan requests. Include hidden overhead allowed by the documented interface and verify actual usage afterward. Local study-map skill 5.4 (Cost and Token Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Correct. A token-count endpoint or compatible estimator can help plan requests. Include hidden overhead allowed by the documented interface and verify actual usage afterward. In this case: Use the selected model's supported counting contract rather than an incompatible estimator.
- **B:** Incorrect for this question. Tokens are model-dependent units, not always words or characters. Include actual system, tool, content, and output usage according to the service contract. In this case: Use the selected model's supported counting contract rather than an incompatible estimator.
- **C:** Incorrect for this question. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. In this case: Use the selected model's supported counting contract rather than an incompatible estimator.
- **D:** Incorrect for this question. Follow the chosen model and service limits. Overflow handling varies; it is not universally automatic oldest-message deletion. In this case: Use the selected model's supported counting contract rather than an incompatible estimator.

### Question 70 — D

Answer: Verify cache reads, writes, and economics in actual usage. Actual read/write usage and economics determine whether caching saves money. Repeated text does not prove cache reuse. Check eligible matching, expiration, thresholds, and current prices before claiming savings. Local study-map skill 5.4 (Cost and Token Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Supported prefix caching depends on exact eligible content, placement, checkpoints, model, and service rules. It is not a cross-user final-answer cache. In this case: Actual read/write usage and economics determine whether caching saves money.
- **B:** Incorrect for this question. Include failed attempts, retries, review, tool work, and operating overhead rather than compare only listed unit token rates. In this case: Actual read/write usage and economics determine whether caching saves money.
- **C:** Incorrect for this question. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. In this case: Actual read/write usage and economics determine whether caching saves money.
- **D:** Correct. Repeated text does not prove cache reuse. Check eligible matching, expiration, thresholds, and current prices before claiming savings. In this case: Actual read/write usage and economics determine whether caching saves money.

### Question 71 — C

Answer: $1.80. Input costs $0.60 and output costs $1.20, totaling $1.80 under the stated rates. At hypothetical rates of $2 per million input tokens and $6 per million output tokens, 300,000 input and 200,000 output tokens cost $0.60 + $1.20 = $1.80. Local study-map skill 5.4 (Cost and Token Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. A hundred-thousand token count is not a ten-thousand count. Convert usage to the specified billing unit before multiplying. In this case: Input costs $0.60 and output costs $1.20, totaling $1.80 under the stated rates.
- **B:** Incorrect for this question. Check the million-token denominator and decimal placement; a tenfold scaling mistake can inflate an otherwise correct sum. In this case: Input costs $0.60 and output costs $1.20, totaling $1.80 under the stated rates.
- **C:** Correct. At hypothetical rates of $2 per million input tokens and $6 per million output tokens, 300,000 input and 200,000 output tokens cost $0.60 + $1.20 = $1.80. In this case: Input costs $0.60 and output costs $1.20, totaling $1.80 under the stated rates.
- **D:** Incorrect for this question. Input and output can have different rates. Apply each stated rate to its corresponding usage rather than use one rate for all tokens. In this case: Input costs $0.60 and output costs $1.20, totaling $1.80 under the stated rates.

### Question 72 — D

Answer: 11,000 tokens. Subtract both reservations from capacity: 16,000 minus 3,000 minus 2,000 leaves 11,000. A hypothetical shared 16,000-token budget minus 3,000 instructions/history and 2,000 reserved generation leaves 11,000 for evidence. Real service accounting must be verified. Local study-map skill 5.4 (Cost and Token Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Subtracting instructions alone omits the explicit generation reservation under a shared-budget assumption. In this case: Subtract both reservations from capacity: 16,000 minus 3,000 minus 2,000 leaves 11,000.
- **B:** Incorrect for this question. Subtract every specified budget component rather than reserve only output and ignore instructions or history. In this case: Subtract both reservations from capacity: 16,000 minus 3,000 minus 2,000 leaves 11,000.
- **C:** Incorrect for this question. Total context capacity is not all available for evidence when instructions, history, and generation share the stated budget. In this case: Subtract both reservations from capacity: 16,000 minus 3,000 minus 2,000 leaves 11,000.
- **D:** Correct. A hypothetical shared 16,000-token budget minus 3,000 instructions/history and 2,000 reserved generation leaves 11,000 for evidence. Real service accounting must be verified. In this case: Subtract both reservations from capacity: 16,000 minus 3,000 minus 2,000 leaves 11,000.

### Question 73 — D

Answer: A: $0.025 per accepted result. A costs $0.025 per accepted result compared with B at $0.03. Under the simplified assumptions, A costs $0.02 / 0.8 = $0.025 per accepted result; B costs $0.015 / 0.5 = $0.03. Other costs can change the comparison. Local study-map skill 5.4 (Cost and Token Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Call price is not accepted-result cost when only half of attempts are acceptable. Divide by the relevant acceptance rate. In this case: A costs $0.025 per accepted result compared with B at $0.03.
- **B:** Incorrect for this question. Equal outcome cost requires equal price-to-acceptance ratios under the simplified assumptions, not merely similar call prices. In this case: A costs $0.025 per accepted result compared with B at $0.03.
- **C:** Incorrect for this question. Failed attempts still consume resources, so acceptance matters when pricing verified outcomes. In this case: A costs $0.025 per accepted result compared with B at $0.03.
- **D:** Correct. Under the simplified assumptions, A costs $0.02 / 0.8 = $0.025 per accepted result; B costs $0.015 / 0.5 = $0.03. Other costs can change the comparison. In this case: A costs $0.025 per accepted result compared with B at $0.03.

### Question 74 — A

Answer: 60% of input tokens were cache reads. The ratio is 60,000 divided by 100,000, or 60%; this is not automatically savings. If 60,000 of 100,000 categorized input tokens were cache reads, the share is 60%. A read share is not automatically the same percentage in monetary savings. Local study-map skill 5.4 (Cost and Token Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Correct. If 60,000 of 100,000 categorized input tokens were cache reads, the share is 60%. A read share is not automatically the same percentage in monetary savings. In this case: The ratio is 60,000 divided by 100,000, or 60%; this is not automatically savings.
- **B:** Incorrect for this question. The non-read share differs from the read share when the categories are disjoint and exhaustive. In this case: The ratio is 60,000 divided by 100,000, or 60%; this is not automatically savings.
- **C:** Incorrect for this question. All categorized input would need to be read from cache for a 100% share. Some matching text alone is insufficient. In this case: The ratio is 60,000 divided by 100,000, or 60%; this is not automatically savings.
- **D:** Incorrect for this question. A proportion must be multiplied by 100 to express a percentage; unit conversion errors can distort monitoring. In this case: The ratio is 60,000 divided by 100,000, or 60%; this is not automatically savings.

### Question 75 — C

Answer: Compare total cost per verified successful outcome. Verified-outcome cost includes the downstream burden excluded from simple unit token price. Include failed attempts, retries, review, tool work, and operating overhead rather than compare only listed unit token rates. Local study-map skill 5.4 (Cost and Token Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. In this case: Verified-outcome cost includes the downstream burden excluded from simple unit token price.
- **B:** Incorrect for this question. Repeated text does not prove cache reuse. Check eligible matching, expiration, thresholds, and current prices before claiming savings. In this case: Verified-outcome cost includes the downstream burden excluded from simple unit token price.
- **C:** Correct. Include failed attempts, retries, review, tool work, and operating overhead rather than compare only listed unit token rates. In this case: Verified-outcome cost includes the downstream burden excluded from simple unit token price.
- **D:** Incorrect for this question. An acceptable mean can hide slow requests that violate user requirements. Define percentile measurements and end-to-end boundaries consistently. In this case: Verified-outcome cost includes the downstream burden excluded from simple unit token price.

### Question 76 — A

Answer: Track actual usage by token and billing category. Apply actual category-specific usage and current billing rules rather than a universal cache price. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. Local study-map skill 5.4 (Cost and Token Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Correct. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. In this case: Apply actual category-specific usage and current billing rules rather than a universal cache price.
- **B:** Incorrect for this question. Repeated text does not prove cache reuse. Check eligible matching, expiration, thresholds, and current prices before claiming savings. In this case: Apply actual category-specific usage and current billing rules rather than a universal cache price.
- **C:** Incorrect for this question. A token-count endpoint or compatible estimator can help plan requests. Include hidden overhead allowed by the documented interface and verify actual usage afterward. In this case: Apply actual category-specific usage and current billing rules rather than a universal cache price.
- **D:** Incorrect for this question. Supported prefix caching depends on exact eligible content, placement, checkpoints, model, and service rules. It is not a cross-user final-answer cache. In this case: Apply actual category-specific usage and current billing rules rather than a universal cache price.

### Question 77 — D

Answer: Budget instructions, evidence, history, and generation together. Include all relevant documented request components instead of count only user text. Follow the chosen model and service limits. Overflow handling varies; it is not universally automatic oldest-message deletion. Local study-map skill 5.4 (Cost and Token Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. A token-count endpoint or compatible estimator can help plan requests. Include hidden overhead allowed by the documented interface and verify actual usage afterward. In this case: Include all relevant documented request components instead of count only user text.
- **B:** Incorrect for this question. Compaction can reduce accumulated exploration, but summaries can be lossy. Validate critical state and preserve durable pointers to evidence. In this case: Include all relevant documented request components instead of count only user text.
- **C:** Incorrect for this question. Project unnecessary fields away before they accumulate in context, while preserving information needed for validation and decisions. Arbitrary truncation may destroy meaning. In this case: Include all relevant documented request components instead of count only user text.
- **D:** Correct. Follow the chosen model and service limits. Overflow handling varies; it is not universally automatic oldest-message deletion. In this case: Include all relevant documented request components instead of count only user text.

### Question 78 — D

Answer: Verify cache reads, writes, and economics in actual usage. Monetary savings depend on actual category rates and overhead, not read share alone. Repeated text does not prove cache reuse. Check eligible matching, expiration, thresholds, and current prices before claiming savings. Local study-map skill 5.4 (Cost and Token Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Supported prefix caching depends on exact eligible content, placement, checkpoints, model, and service rules. It is not a cross-user final-answer cache. In this case: Monetary savings depend on actual category rates and overhead, not read share alone.
- **B:** Incorrect for this question. Include failed attempts, retries, review, tool work, and operating overhead rather than compare only listed unit token rates. In this case: Monetary savings depend on actual category rates and overhead, not read share alone.
- **C:** Incorrect for this question. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. In this case: Monetary savings depend on actual category rates and overhead, not read share alone.
- **D:** Correct. Repeated text does not prove cache reuse. Check eligible matching, expiration, thresholds, and current prices before claiming savings. In this case: Monetary savings depend on actual category rates and overhead, not read share alone.

### Question 79 — D

Answer: Track actual usage by token and billing category. Include actual usage across the whole task and all applicable calls. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. Local study-map skill 5.4 (Cost and Token Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. A token-count endpoint or compatible estimator can help plan requests. Include hidden overhead allowed by the documented interface and verify actual usage afterward. In this case: Include actual usage across the whole task and all applicable calls.
- **B:** Incorrect for this question. Include failed attempts, retries, review, tool work, and operating overhead rather than compare only listed unit token rates. In this case: Include actual usage across the whole task and all applicable calls.
- **C:** Incorrect for this question. Tokens are model-dependent units, not always words or characters. Include actual system, tool, content, and output usage according to the service contract. In this case: Include actual usage across the whole task and all applicable calls.
- **D:** Correct. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. In this case: Include actual usage across the whole task and all applicable calls.

### Question 80 — C

Answer: Compare total cost per verified successful outcome. Compare complete cost per verified successful result rather than token fees alone. Include failed attempts, retries, review, tool work, and operating overhead rather than compare only listed unit token rates. Local study-map skill 5.4 (Cost and Token Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. An acceptable mean can hide slow requests that violate user requirements. Define percentile measurements and end-to-end boundaries consistently. In this case: Compare complete cost per verified successful result rather than token fees alone.
- **B:** Incorrect for this question. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. In this case: Compare complete cost per verified successful result rather than token fees alone.
- **C:** Correct. Include failed attempts, retries, review, tool work, and operating overhead rather than compare only listed unit token rates. In this case: Compare complete cost per verified successful result rather than token fees alone.
- **D:** Incorrect for this question. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. In this case: Compare complete cost per verified successful result rather than token fees alone.

### Question 81 — C

Answer: Measure tail latency as well as average latency. Evaluate the required latency percentile at the correct end-to-end boundary. An acceptable mean can hide slow requests that violate user requirements. Define percentile measurements and end-to-end boundaries consistently. Local study-map skill 5.3 (Model Selection and Tradeoffs), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. In this case: Evaluate the required latency percentile at the correct end-to-end boundary.
- **B:** Incorrect for this question. Streaming can improve perceived responsiveness without reducing total generation or external-tool time. First-token delay and total duration measure different things. In this case: Evaluate the required latency percentile at the correct end-to-end boundary.
- **C:** Correct. An acceptable mean can hide slow requests that violate user requirements. Define percentile measurements and end-to-end boundaries consistently. In this case: Evaluate the required latency percentile at the correct end-to-end boundary.
- **D:** Incorrect for this question. Include failed attempts, retries, review, tool work, and operating overhead rather than compare only listed unit token rates. In this case: Evaluate the required latency percentile at the correct end-to-end boundary.

### Question 82 — A

Answer: Measure time to first token separately from full completion. First-token responsiveness and total duration are distinct performance measures. Streaming can improve perceived responsiveness without reducing total generation or external-tool time. First-token delay and total duration measure different things. Local study-map skill 5.3 (Model Selection and Tradeoffs), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Correct. Streaming can improve perceived responsiveness without reducing total generation or external-tool time. First-token delay and total duration measure different things. In this case: First-token responsiveness and total duration are distinct performance measures.
- **B:** Incorrect for this question. An acceptable mean can hide slow requests that violate user requirements. Define percentile measurements and end-to-end boundaries consistently. In this case: First-token responsiveness and total duration are distinct performance measures.
- **C:** Incorrect for this question. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. In this case: First-token responsiveness and total duration are distinct performance measures.
- **D:** Incorrect for this question. Include failed attempts, retries, review, tool work, and operating overhead rather than compare only listed unit token rates. In this case: First-token responsiveness and total duration are distinct performance measures.

### Question 83 — B

Answer: Route requests using evaluated task classes and safe fallbacks. Task routing must include misclassification measurements and safe fallback behavior. Use evidence-based routing to suitable configurations, monitor misclassification, and define fallback. Routing complexity must justify its own operating cost. Local study-map skill 5.3 (Model Selection and Tradeoffs), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Reasoning-related features and parameters vary by model and provider. Evaluate quality, latency, and cost rather than assume every release accepts the same switches. In this case: Task routing must include misclassification measurements and safe fallback behavior.
- **B:** Correct. Use evidence-based routing to suitable configurations, monitor misclassification, and define fallback. Routing complexity must justify its own operating cost. In this case: Task routing must include misclassification measurements and safe fallback behavior.
- **C:** Incorrect for this question. Stage exposure to the new configuration, compare required outcomes, and retain a known-good path. A vendor release note is not workload validation. In this case: Task routing must include misclassification measurements and safe fallback behavior.
- **D:** Incorrect for this question. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. In this case: Task routing must include misclassification measurements and safe fallback behavior.

### Question 84 — D

Answer: Select the least costly configuration that meets required outcomes. Actual supported capabilities and operational requirements outweigh a generic leaderboard ranking. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. Local study-map skill 5.3 (Model Selection and Tradeoffs), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Model-family positioning is a starting hypothesis, not proof of fit. Use a specific supported version and measure the required quality, cost, and latency. In this case: Actual supported capabilities and operational requirements outweigh a generic leaderboard ranking.
- **B:** Incorrect for this question. A balanced model may suit many development workflows, but the actual selected release and workload requirements determine fitness. In this case: Actual supported capabilities and operational requirements outweigh a generic leaderboard ranking.
- **C:** Incorrect for this question. A high-capability model may help difficult tasks, but size or family alone does not guarantee accuracy, acceptable latency, or economical deployment. In this case: Actual supported capabilities and operational requirements outweigh a generic leaderboard ranking.
- **D:** Correct. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. In this case: Actual supported capabilities and operational requirements outweigh a generic leaderboard ranking.

### Question 85 — B

Answer: Verify cache reads, writes, and economics in actual usage. Eligible exact prefix matching and cache rules matter more than similar-looking instructions. Repeated text does not prove cache reuse. Check eligible matching, expiration, thresholds, and current prices before claiming savings. Local study-map skill 5.4 (Cost and Token Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. In this case: Eligible exact prefix matching and cache rules matter more than similar-looking instructions.
- **B:** Correct. Repeated text does not prove cache reuse. Check eligible matching, expiration, thresholds, and current prices before claiming savings. In this case: Eligible exact prefix matching and cache rules matter more than similar-looking instructions.
- **C:** Incorrect for this question. Supported prefix caching depends on exact eligible content, placement, checkpoints, model, and service rules. It is not a cross-user final-answer cache. In this case: Eligible exact prefix matching and cache rules matter more than similar-looking instructions.
- **D:** Incorrect for this question. A token-count endpoint or compatible estimator can help plan requests. Include hidden overhead allowed by the documented interface and verify actual usage afterward. In this case: Eligible exact prefix matching and cache rules matter more than similar-looking instructions.

### Question 86 — B

Answer: Track actual usage by token and billing category. Use current actual category accounting instead of assume unchanged token economics. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. Local study-map skill 5.4 (Cost and Token Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. A token-count endpoint or compatible estimator can help plan requests. Include hidden overhead allowed by the documented interface and verify actual usage afterward. In this case: Use current actual category accounting instead of assume unchanged token economics.
- **B:** Correct. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. In this case: Use current actual category accounting instead of assume unchanged token economics.
- **C:** Incorrect for this question. Repeated text does not prove cache reuse. Check eligible matching, expiration, thresholds, and current prices before claiming savings. In this case: Use current actual category accounting instead of assume unchanged token economics.
- **D:** Incorrect for this question. Tokens are model-dependent units, not always words or characters. Include actual system, tool, content, and output usage according to the service contract. In this case: Use current actual category accounting instead of assume unchanged token economics.

### Question 87 — A

Answer: Test the integration contract at the provider boundary. Inspect the wrapper's serialized request and parsed response contract. Check serialized requests, content blocks, status handling, and representative responses. Mock success alone may not reveal a malformed real request or unsupported provider feature. Local study-map skill 5.2 (Technical Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Correct. Check serialized requests, content blocks, status handling, and representative responses. Mock success alone may not reveal a malformed real request or unsupported provider feature. In this case: Inspect the wrapper's serialized request and parsed response contract.
- **B:** Incorrect for this question. Inject timeouts, malformed responses, and provider failures without live side effects. Combine with contract and representative integration tests rather than infer complete correctness from mocks. In this case: Inspect the wrapper's serialized request and parsed response contract.
- **C:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Inspect the wrapper's serialized request and parsed response contract.
- **D:** Incorrect for this question. Correlate the actual request, model response, tool execution, retries, and validation results. Diagnose the first failing boundary rather than infer cause from the final prose. In this case: Inspect the wrapper's serialized request and parsed response contract.

### Question 88 — A

Answer: Allow for output variability and validate outcomes. Outcome validation should distinguish harmless variation from failure rather than demand universal identical text. Repeated calls can differ, even with low sampling settings. Seeds or low temperature do not establish universal cross-version determinism or factual accuracy. Local study-map skill 5.1 (LLM Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Correct. Repeated calls can differ, even with low sampling settings. Seeds or low temperature do not establish universal cross-version determinism or factual accuracy. In this case: Outcome validation should distinguish harmless variation from failure rather than demand universal identical text.
- **B:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Outcome validation should distinguish harmless variation from failure rather than demand universal identical text.
- **C:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Outcome validation should distinguish harmless variation from failure rather than demand universal identical text.
- **D:** Incorrect for this question. Temperature changes next-token sampling behavior where supported. Lowering it does not independently guarantee correct extraction, grounding, or identical execution. In this case: Outcome validation should distinguish harmless variation from failure rather than demand universal identical text.

### Question 89 — D

Answer: Canary a version change with regression gates and rollback. Control exposure, observe required outcomes, and retain rollback capability. Stage exposure to the new configuration, compare required outcomes, and retain a known-good path. A vendor release note is not workload validation. Local study-map skill 5.3 (Model Selection and Tradeoffs), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Control exposure, observe required outcomes, and retain rollback capability.
- **B:** Incorrect for this question. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Control exposure, observe required outcomes, and retain rollback capability.
- **C:** Incorrect for this question. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. In this case: Control exposure, observe required outcomes, and retain rollback capability.
- **D:** Correct. Stage exposure to the new configuration, compare required outcomes, and retain a known-good path. A vendor release note is not workload validation. In this case: Control exposure, observe required outcomes, and retain rollback capability.

### Question 90 — C

Answer: Compare total cost per verified successful outcome. Savings are meaningful only when required verified outcomes remain acceptable. Include failed attempts, retries, review, tool work, and operating overhead rather than compare only listed unit token rates. Local study-map skill 5.4 (Cost and Token Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. An acceptable mean can hide slow requests that violate user requirements. Define percentile measurements and end-to-end boundaries consistently. In this case: Savings are meaningful only when required verified outcomes remain acceptable.
- **B:** Incorrect for this question. Repeated text does not prove cache reuse. Check eligible matching, expiration, thresholds, and current prices before claiming savings. In this case: Savings are meaningful only when required verified outcomes remain acceptable.
- **C:** Correct. Include failed attempts, retries, review, tool work, and operating overhead rather than compare only listed unit token rates. In this case: Savings are meaningful only when required verified outcomes remain acceptable.
- **D:** Incorrect for this question. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. In this case: Savings are meaningful only when required verified outcomes remain acceptable.

### Question 91 — A

Answer: Count tokens with model-compatible accounting. Model tokenization defines these units and may split code or unfamiliar words differently. Tokens are model-dependent units, not always words or characters. Include actual system, tool, content, and output usage according to the service contract. Local study-map skill 5.1 (LLM Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Correct. Tokens are model-dependent units, not always words or characters. Include actual system, tool, content, and output usage according to the service contract. In this case: Model tokenization defines these units and may split code or unfamiliar words differently.
- **B:** Incorrect for this question. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. In this case: Model tokenization defines these units and may split code or unfamiliar words differently.
- **C:** Incorrect for this question. A token-count endpoint or compatible estimator can help plan requests. Include hidden overhead allowed by the documented interface and verify actual usage afterward. In this case: Model tokenization defines these units and may split code or unfamiliar words differently.
- **D:** Incorrect for this question. Follow the chosen model and service limits. Overflow handling varies; it is not universally automatic oldest-message deletion. In this case: Model tokenization defines these units and may split code or unfamiliar words differently.

### Question 92 — B

Answer: Use supported thinking or effort controls after measuring task benefit. Measure supported reasoning configuration against representative benefit, latency, and cost. Reasoning-related features and parameters vary by model and provider. Evaluate quality, latency, and cost rather than assume every release accepts the same switches. Local study-map skill 5.1 (LLM Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Temperature changes next-token sampling behavior where supported. Lowering it does not independently guarantee correct extraction, grounding, or identical execution. In this case: Measure supported reasoning configuration against representative benefit, latency, and cost.
- **B:** Correct. Reasoning-related features and parameters vary by model and provider. Evaluate quality, latency, and cost rather than assume every release accepts the same switches. In this case: Measure supported reasoning configuration against representative benefit, latency, and cost.
- **C:** Incorrect for this question. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. In this case: Measure supported reasoning configuration against representative benefit, latency, and cost.
- **D:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Measure supported reasoning configuration against representative benefit, latency, and cost.

### Question 93 — D

Answer: Use WebSockets for an explicitly bidirectional persistent channel. Bidirectional application communication can suit WebSockets, unlike the standard one-way model event stream. WebSockets can fit bidirectional application communication, but the documented standard Messages streaming interface is SSE. Do not confuse a transport choice with model capability. Local study-map skill 5.2 (Technical Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. The documented streaming interface emits SSE events over HTTP. It is not inherently a WebSocket connection or one valid JSON object per arbitrary network chunk. In this case: Bidirectional application communication can suit WebSockets, unlike the standard one-way model event stream.
- **B:** Incorrect for this question. Await network operations without blocking an event loop, while limiting in-flight work and respecting service capacity. Creating a coroutine does not mean it has run. In this case: Bidirectional application communication can suit WebSockets, unlike the standard one-way model event stream.
- **C:** Incorrect for this question. A REST integration must respect its actual endpoint contract. HTTP 200 does not establish that the requested business operation succeeded semantically. In this case: Bidirectional application communication can suit WebSockets, unlike the standard one-way model event stream.
- **D:** Correct. WebSockets can fit bidirectional application communication, but the documented standard Messages streaming interface is SSE. Do not confuse a transport choice with model capability. In this case: Bidirectional application communication can suit WebSockets, unlike the standard one-way model event stream.

### Question 94 — C

Answer: Use asynchronous I/O with bounded concurrency. The coroutine must be awaited or appropriately scheduled to perform the operation. Await network operations without blocking an event loop, while limiting in-flight work and respecting service capacity. Creating a coroutine does not mean it has run. Local study-map skill 5.2 (Technical Fundamentals), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. Independent work can be parallelized within resource limits. A join must account for missing, failed, or conflicting outputs. In this case: The coroutine must be awaited or appropriately scheduled to perform the operation.
- **B:** Incorrect for this question. Limit queued and active work so slow consumers or provider limits do not exhaust memory or connections. Unbounded parallelism is not a capacity plan. In this case: The coroutine must be awaited or appropriately scheduled to perform the operation.
- **C:** Correct. Await network operations without blocking an event loop, while limiting in-flight work and respecting service capacity. Creating a coroutine does not mean it has run. In this case: The coroutine must be awaited or appropriately scheduled to perform the operation.
- **D:** Incorrect for this question. Dependent work must follow its prerequisites. Starting a dependent action early can use absent, stale, or unauthorized data. In this case: The coroutine must be awaited or appropriately scheduled to perform the operation.

### Question 95 — B

Answer: Evaluate Haiku for suitable speed- and efficiency-oriented tasks. Haiku is an efficiency-oriented candidate, but actual task fitness must be verified. Model-family positioning is a starting hypothesis, not proof of fit. Use a specific supported version and measure the required quality, cost, and latency. Local study-map skill 5.3 (Model Selection and Tradeoffs), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. A high-capability model may help difficult tasks, but size or family alone does not guarantee accuracy, acceptable latency, or economical deployment. In this case: Haiku is an efficiency-oriented candidate, but actual task fitness must be verified.
- **B:** Correct. Model-family positioning is a starting hypothesis, not proof of fit. Use a specific supported version and measure the required quality, cost, and latency. In this case: Haiku is an efficiency-oriented candidate, but actual task fitness must be verified.
- **C:** Incorrect for this question. A balanced model may suit many development workflows, but the actual selected release and workload requirements determine fitness. In this case: Haiku is an efficiency-oriented candidate, but actual task fitness must be verified.
- **D:** Incorrect for this question. Reasoning-related features and parameters vary by model and provider. Evaluate quality, latency, and cost rather than assume every release accepts the same switches. In this case: Haiku is an efficiency-oriented candidate, but actual task fitness must be verified.

### Question 96 — A

Answer: Evaluate Sonnet for a measured balance of capability and efficiency. Sonnet can be tested for balanced needs rather than assumed best without evidence. A balanced model may suit many development workflows, but the actual selected release and workload requirements determine fitness. Local study-map skill 5.3 (Model Selection and Tradeoffs), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Correct. A balanced model may suit many development workflows, but the actual selected release and workload requirements determine fitness. In this case: Sonnet can be tested for balanced needs rather than assumed best without evidence.
- **B:** Incorrect for this question. A high-capability model may help difficult tasks, but size or family alone does not guarantee accuracy, acceptable latency, or economical deployment. In this case: Sonnet can be tested for balanced needs rather than assumed best without evidence.
- **C:** Incorrect for this question. Model-family positioning is a starting hypothesis, not proof of fit. Use a specific supported version and measure the required quality, cost, and latency. In this case: Sonnet can be tested for balanced needs rather than assumed best without evidence.
- **D:** Incorrect for this question. Reasoning-related features and parameters vary by model and provider. Evaluate quality, latency, and cost rather than assume every release accepts the same switches. In this case: Sonnet can be tested for balanced needs rather than assumed best without evidence.

### Question 97 — A

Answer: Evaluate Opus for demanding capability-oriented work. Opus can be evaluated for demanding capability requirements with cost and latency checks. A high-capability model may help difficult tasks, but size or family alone does not guarantee accuracy, acceptable latency, or economical deployment. Local study-map skill 5.3 (Model Selection and Tradeoffs), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Correct. A high-capability model may help difficult tasks, but size or family alone does not guarantee accuracy, acceptable latency, or economical deployment. In this case: Opus can be evaluated for demanding capability requirements with cost and latency checks.
- **B:** Incorrect for this question. Reasoning-related features and parameters vary by model and provider. Evaluate quality, latency, and cost rather than assume every release accepts the same switches. In this case: Opus can be evaluated for demanding capability requirements with cost and latency checks.
- **C:** Incorrect for this question. A balanced model may suit many development workflows, but the actual selected release and workload requirements determine fitness. In this case: Opus can be evaluated for demanding capability requirements with cost and latency checks.
- **D:** Incorrect for this question. Model-family positioning is a starting hypothesis, not proof of fit. Use a specific supported version and measure the required quality, cost, and latency. In this case: Opus can be evaluated for demanding capability requirements with cost and latency checks.

### Question 98 — B

Answer: Put eligible stable common content before variable input for cache reuse. Place eligible common content before variable input while following provider cache rules. Supported prefix caching depends on exact eligible content, placement, checkpoints, model, and service rules. It is not a cross-user final-answer cache. Local study-map skill 5.4 (Cost and Token Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Incorrect for this question. A token-count endpoint or compatible estimator can help plan requests. Include hidden overhead allowed by the documented interface and verify actual usage afterward. In this case: Place eligible common content before variable input while following provider cache rules.
- **B:** Correct. Supported prefix caching depends on exact eligible content, placement, checkpoints, model, and service rules. It is not a cross-user final-answer cache. In this case: Place eligible common content before variable input while following provider cache rules.
- **C:** Incorrect for this question. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. In this case: Place eligible common content before variable input while following provider cache rules.
- **D:** Incorrect for this question. Repeated text does not prove cache reuse. Check eligible matching, expiration, thresholds, and current prices before claiming savings. In this case: Place eligible common content before variable input while following provider cache rules.

### Question 99 — A

Answer: Verify cache reads, writes, and economics in actual usage. Observe actual reads, writes, expiration, and costs rather than assume configured caching saves money. Repeated text does not prove cache reuse. Check eligible matching, expiration, thresholds, and current prices before claiming savings. Local study-map skill 5.4 (Cost and Token Management), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Correct. Repeated text does not prove cache reuse. Check eligible matching, expiration, thresholds, and current prices before claiming savings. In this case: Observe actual reads, writes, expiration, and costs rather than assume configured caching saves money.
- **B:** Incorrect for this question. Include failed attempts, retries, review, tool work, and operating overhead rather than compare only listed unit token rates. In this case: Observe actual reads, writes, expiration, and costs rather than assume configured caching saves money.
- **C:** Incorrect for this question. Supported prefix caching depends on exact eligible content, placement, checkpoints, model, and service rules. It is not a cross-user final-answer cache. In this case: Observe actual reads, writes, expiration, and costs rather than assume configured caching saves money.
- **D:** Incorrect for this question. Separate ordinary input, output, cache writes/reads, thinking or other applicable categories according to current provider terms. A single token price may not represent the complete bill. In this case: Observe actual reads, writes, expiration, and costs rather than assume configured caching saves money.

### Question 100 — A

Answer: Use a versioned representative held-out evaluation set. Use representative held-out cases covering meaningful task variation and failure modes. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. Local study-map skill 5.3 (Model Selection and Tradeoffs), mapped to the official guide: https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf Primary technical reference: https://platform.claude.com/docs/en/about-claude/models/overview

- **A:** Correct. Include actual task variation, important failures, and acceptance criteria. Keep tuning cases separate and track changes to avoid evaluating only familiar demonstrations. In this case: Use representative held-out cases covering meaningful task variation and failure modes.
- **B:** Incorrect for this question. Reproducible configuration requires identifying all behavior-relevant versions. A pinned model alone does not freeze application code, prompts, or provider behavior forever. In this case: Use representative held-out cases covering meaningful task variation and failure modes.
- **C:** Incorrect for this question. Stage exposure to the new configuration, compare required outcomes, and retain a known-good path. A vendor release note is not workload validation. In this case: Use representative held-out cases covering meaningful task variation and failure modes.
- **D:** Incorrect for this question. Compare supported models on representative quality, latency, safety, and operational constraints. Never optimize price while ignoring unacceptable failures. In this case: Use representative held-out cases covering meaningful task variation and failure modes.
