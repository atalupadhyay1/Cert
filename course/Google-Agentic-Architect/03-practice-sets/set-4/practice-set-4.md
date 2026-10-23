# Google Cloud Professional Agentic Architect (PAA) — Practice Set 4

Evaluating and Deploying Agentic Workflows

100 questions · Suggested practice duration: 180 minutes · Practice target: 80%

Tests 1–5 are focused learning tests. Test 6 is an expanded five-domain review, not an official exam replica. Related concepts recur.

Select ONE best answer for every question. Answer key follows all questions.

Original educational content, not actual, recalled, or copied Anthropic exam items.

## Questions

### 1. A team is starting evaluation for a customer-support agent. What should anchor the test set?

Domain: Evaluating and Deploying Agentic Workflows

- A. Set explicit pass thresholds before evaluating
- B. Build a representative golden dataset from real tasks
- C. Include edge cases and adversarial inputs in test sets
- D. Author an ADK evalset with expected tool use and responses

### 2. A happy-path test set passes, but the agent fails on missing fields and hostile input. What is missing?

Domain: Evaluating and Deploying Agentic Workflows

- A. Use human review for unresolved or high-impact judgment
- B. Build a representative golden dataset from real tasks
- C. Use a calibrated model-based autorater for scalable judgment
- D. Include edge cases and adversarial inputs in test sets

### 3. A golden set contains only easy questions with one tool call. What risk does it create?

Domain: Evaluating and Deploying Agentic Workflows

- A. Author an ADK evalset with expected tool use and responses
- B. Build a representative golden dataset from real tasks
- C. Set explicit pass thresholds before evaluating
- D. Evaluate tool-call trajectories, not only final text

### 4. A safety-critical agent must be tested for prompt injection attempts. What should the test set include?

Domain: Evaluating and Deploying Agentic Workflows

- A. Build a representative golden dataset from real tasks
- B. Compare variants with controlled traffic and shared metrics
- C. Set explicit pass thresholds before evaluating
- D. Include edge cases and adversarial inputs in test sets

### 5. Subject-matter experts disagree on the expected answer for some cases. What should the team do?

Domain: Evaluating and Deploying Agentic Workflows

- A. Build a representative golden dataset from real tasks
- B. Use human review for unresolved or high-impact judgment
- C. Use a calibrated model-based autorater for scalable judgment
- D. Run evaluation on every meaningful change

### 6. A team sets a target of "90% good" without defining good. What should be defined first?

Domain: Evaluating and Deploying Agentic Workflows

- A. Evaluate tool-call trajectories, not only final text
- B. Set explicit pass thresholds before evaluating
- C. Build a representative golden dataset from real tasks
- D. Use Cloud Logging, Cloud Trace, and Cloud Monitoring

### 7. A new market introduces unfamiliar document formats. What should be added to evaluation?

Domain: Evaluating and Deploying Agentic Workflows

- A. Compare variants with controlled traffic and shared metrics
- B. Include edge cases and adversarial inputs in test sets
- C. Build a representative golden dataset from real tasks
- D. Run evaluation on every meaningful change

### 8. A test set is copied from vendor demos and does not resemble the organization's traffic. What is the flaw?

Domain: Evaluating and Deploying Agentic Workflows

- A. Author an ADK evalset with expected tool use and responses
- B. Set explicit pass thresholds before evaluating
- C. Use a calibrated model-based autorater for scalable judgment
- D. Build a representative golden dataset from real tasks

### 9. A low-volume but high-impact case appears rarely in production. How should it be handled?

Domain: Evaluating and Deploying Agentic Workflows

- A. Build a representative golden dataset from real tasks
- B. Use human review for unresolved or high-impact judgment
- C. Include edge cases and adversarial inputs in test sets
- D. Set explicit pass thresholds before evaluating

### 10. An evaluation set contains duplicate paraphrases of the same case. What is the effect?

Domain: Evaluating and Deploying Agentic Workflows

- A. Author an ADK evalset with expected tool use and responses
- B. Build a representative golden dataset from real tasks
- C. Run evaluation on every meaningful change
- D. Monitor production behavior with online evaluation

### 11. A test case requires a policy interpretation that the team cannot resolve. What should happen?

Domain: Evaluating and Deploying Agentic Workflows

- A. Include edge cases and adversarial inputs in test sets
- B. Build a representative golden dataset from real tasks
- C. Set explicit pass thresholds before evaluating
- D. Use human review for unresolved or high-impact judgment

### 12. A golden set has expected final answers but no expected tool calls. What can it not assess?

Domain: Evaluating and Deploying Agentic Workflows

- A. Author an ADK evalset with expected tool use and responses
- B. Evaluate tool-call trajectories, not only final text
- C. Set explicit pass thresholds before evaluating
- D. Build a representative golden dataset from real tasks

### 13. Two business units have different acceptable outcomes for the same request type. What should evaluation do?

Domain: Evaluating and Deploying Agentic Workflows

- A. Build a representative golden dataset from real tasks
- B. Include edge cases and adversarial inputs in test sets
- C. Compare variants with controlled traffic and shared metrics
- D. Run evaluation on every meaningful change

### 14. A production incident involved a request type absent from the test suite. What should follow?

Domain: Evaluating and Deploying Agentic Workflows

- A. Monitor production behavior with online evaluation
- B. Author an ADK evalset with expected tool use and responses
- C. Run evaluation on every meaningful change
- D. Use Cloud Logging, Cloud Trace, and Cloud Monitoring

### 15. A model-based judge disagrees with experts on sensitive cases. What should be done?

Domain: Evaluating and Deploying Agentic Workflows

- A. Use a calibrated model-based autorater for scalable judgment
- B. Build a representative golden dataset from real tasks
- C. Set explicit pass thresholds before evaluating
- D. Use human review for unresolved or high-impact judgment

### 16. A test set grows without version control or ownership. What problem arises?

Domain: Evaluating and Deploying Agentic Workflows

- A. Build a representative golden dataset from real tasks
- B. Set explicit pass thresholds before evaluating
- C. Include edge cases and adversarial inputs in test sets
- D. Provision capacity for peak concurrency and quotas

### 17. An agent gives a correct final answer after deleting a production record it should not have touched. What evaluation would catch this?

Domain: Evaluating and Deploying Agentic Workflows

- A. Measure retrieval relevance and recall separately
- B. Use a calibrated model-based autorater for scalable judgment
- C. Score response correctness, completeness, and helpfulness
- D. Evaluate tool-call trajectories, not only final text

### 18. A final answer is fluent but omits a required exception. What metric dimension applies?

Domain: Evaluating and Deploying Agentic Workflows

- A. Ground the response in cited retrieved evidence
- B. Score response correctness, completeness, and helpfulness
- C. Measure retrieval relevance and recall separately
- D. Evaluate tool-call trajectories, not only final text

### 19. The correct policy exists, but the agent answers from an unrelated older document. What should be measured?

Domain: Evaluating and Deploying Agentic Workflows

- A. Measure retrieval relevance and recall separately
- B. Evaluate tool-call trajectories, not only final text
- C. Ground the response in cited retrieved evidence
- D. Score response correctness, completeness, and helpfulness

### 20. A team wants repeatable checks of expected tool use and final responses. What artifact should it build?

Domain: Evaluating and Deploying Agentic Workflows

- A. Set explicit pass thresholds before evaluating
- B. Evaluate tool-call trajectories, not only final text
- C. Author an ADK evalset with expected tool use and responses
- D. Use a calibrated model-based autorater for scalable judgment

### 21. A model-based scorer rates tone and helpfulness at scale. What is required before trusting it?

Domain: Evaluating and Deploying Agentic Workflows

- A. Set explicit pass thresholds before evaluating
- B. Score response correctness, completeness, and helpfulness
- C. Use a calibrated model-based autorater for scalable judgment
- D. Use human review for unresolved or high-impact judgment

### 22. A decision requires judgment about a novel ethical trade-off. What evaluation method fits?

Domain: Evaluating and Deploying Agentic Workflows

- A. Use human review for unresolved or high-impact judgment
- B. Evaluate tool-call trajectories, not only final text
- C. Set explicit pass thresholds before evaluating
- D. Use a calibrated model-based autorater for scalable judgment

### 23. A team wants to block a release if tool safety checks fail. What must exist?

Domain: Evaluating and Deploying Agentic Workflows

- A. Score response correctness, completeness, and helpfulness
- B. Evaluate tool-call trajectories, not only final text
- C. Measure retrieval relevance and recall separately
- D. Set explicit pass thresholds before evaluating

### 24. A correct answer cites a source that does not support it. Which metrics disagree?

Domain: Evaluating and Deploying Agentic Workflows

- A. Ground the response in cited retrieved evidence
- B. Evaluate tool-call trajectories, not only final text
- C. Measure retrieval relevance and recall separately
- D. Score response correctness, completeness, and helpfulness

### 25. An agent wastes six tool calls but eventually succeeds. What should be measured?

Domain: Evaluating and Deploying Agentic Workflows

- A. Use a calibrated model-based autorater for scalable judgment
- B. Evaluate tool-call trajectories, not only final text
- C. Score response correctness, completeness, and helpfulness
- D. Use human review for unresolved or high-impact judgment

### 26. A retrieval change improves recall but adds conflicting passages. What should be evaluated?

Domain: Evaluating and Deploying Agentic Workflows

- A. Score response correctness, completeness, and helpfulness
- B. Set explicit pass thresholds before evaluating
- C. Ground the response in cited retrieved evidence
- D. Measure retrieval relevance and recall separately

### 27. An autorater is used to judge its own model family's outputs. What risk exists?

Domain: Evaluating and Deploying Agentic Workflows

- A. Set explicit pass thresholds before evaluating
- B. Use human review for unresolved or high-impact judgment
- C. Author an ADK evalset with expected tool use and responses
- D. Use a calibrated model-based autorater for scalable judgment

### 28. An evaluation checks only the final text for a refund workflow. What important failure is missed?

Domain: Evaluating and Deploying Agentic Workflows

- A. Evaluate tool-call trajectories, not only final text
- B. Use Cloud Logging, Cloud Trace, and Cloud Monitoring
- C. Author an ADK evalset with expected tool use and responses
- D. Score response correctness, completeness, and helpfulness

### 29. A high-risk action passes automated metrics but lacks approval evidence. What should happen?

Domain: Evaluating and Deploying Agentic Workflows

- A. Evaluate tool-call trajectories, not only final text
- B. Use human review for unresolved or high-impact judgment
- C. Use a calibrated model-based autorater for scalable judgment
- D. Set explicit pass thresholds before evaluating

### 30. An answer contains a correct conclusion but no usable citation. What should evaluation report?

Domain: Evaluating and Deploying Agentic Workflows

- A. Ground the response in cited retrieved evidence
- B. Score response correctness, completeness, and helpfulness
- C. Evaluate tool-call trajectories, not only final text
- D. Measure retrieval relevance and recall separately

### 31. A team wants to compare quality and efficiency across two agent designs. What should it report?

Domain: Evaluating and Deploying Agentic Workflows

- A. Evaluate tool-call trajectories, not only final text
- B. Score response correctness, completeness, and helpfulness
- C. Set explicit pass thresholds before evaluating
- D. Track token and tool cost per completed task

### 32. An evalset is updated whenever a test fails so that the suite stays green. What is the risk?

Domain: Evaluating and Deploying Agentic Workflows

- A. Set explicit pass thresholds before evaluating
- B. Run evaluation on every meaningful change
- C. Author an ADK evalset with expected tool use and responses
- D. Use Cloud Logging, Cloud Trace, and Cloud Monitoring

### 33. A judge model rewards long answers regardless of correctness. What should be done?

Domain: Evaluating and Deploying Agentic Workflows

- A. Ground the response in cited retrieved evidence
- B. Use human review for unresolved or high-impact judgment
- C. Use a calibrated model-based autorater for scalable judgment
- D. Score response correctness, completeness, and helpfulness

### 34. A prompt change is proposed for a production agent. What should run before release?

Domain: Evaluating and Deploying Agentic Workflows

- A. Compare variants with controlled traffic and shared metrics
- B. Monitor production behavior with online evaluation
- C. Set explicit pass thresholds before evaluating
- D. Run evaluation on every meaningful change

### 35. Offline tests pass, but production users phrase requests differently. What should be monitored?

Domain: Evaluating and Deploying Agentic Workflows

- A. Set explicit pass thresholds before evaluating
- B. Use human review for unresolved or high-impact judgment
- C. Monitor production behavior with online evaluation
- D. Use Cloud Logging, Cloud Trace, and Cloud Monitoring

### 36. A team changes the model, prompt, and retrieval configuration at once. What is the evaluation problem?

Domain: Evaluating and Deploying Agentic Workflows

- A. Compare variants with controlled traffic and shared metrics
- B. Track token and tool cost per completed task
- C. Set explicit pass thresholds before evaluating
- D. Run evaluation on every meaningful change

### 37. An agent release improves average quality but worsens a critical segment. What should the gate do?

Domain: Evaluating and Deploying Agentic Workflows

- A. Use staged rollout with measurable rollback criteria
- B. Set explicit pass thresholds before evaluating
- C. Run evaluation on every meaningful change
- D. Use Cloud Logging, Cloud Trace, and Cloud Monitoring

### 38. Online evaluation samples include sensitive customer text. What must be designed?

Domain: Evaluating and Deploying Agentic Workflows

- A. Use Cloud Logging, Cloud Trace, and Cloud Monitoring
- B. Use human review for unresolved or high-impact judgment
- C. Record agent actions and tool calls in audit logs
- D. Monitor production behavior with online evaluation

### 39. A model version is updated by the provider with no API change. What should happen?

Domain: Evaluating and Deploying Agentic Workflows

- A. Detect changes in inputs, data, or performance over time
- B. Set explicit pass thresholds before evaluating
- C. Run evaluation on every meaningful change
- D. Author an ADK evalset with expected tool use and responses

### 40. A canary receives 5% of traffic and shows a higher error rate. What should follow?

Domain: Evaluating and Deploying Agentic Workflows

- A. Use staged rollout with measurable rollback criteria
- B. Set explicit pass thresholds before evaluating
- C. Compare variants with controlled traffic and shared metrics
- D. Provision capacity for peak concurrency and quotas

### 41. A production agent starts calling an unexpected tool. What should detect it?

Domain: Evaluating and Deploying Agentic Workflows

- A. Use Cloud Logging, Cloud Trace, and Cloud Monitoring
- B. Run evaluation on every meaningful change
- C. Record agent actions and tool calls in audit logs
- D. Monitor production behavior with online evaluation

### 42. Automated online scoring flags many answers as low quality, but reviewers disagree. What should be reviewed?

Domain: Evaluating and Deploying Agentic Workflows

- A. Monitor production behavior with online evaluation
- B. Use human review for unresolved or high-impact judgment
- C. Use a calibrated model-based autorater for scalable judgment
- D. Set explicit pass thresholds before evaluating

### 43. Input distributions shift after a new customer segment is onboarded. What should be updated?

Domain: Evaluating and Deploying Agentic Workflows

- A. Detect changes in inputs, data, or performance over time
- B. Run evaluation on every meaningful change
- C. Use Cloud Logging, Cloud Trace, and Cloud Monitoring
- D. Author an ADK evalset with expected tool use and responses

### 44. A team wants evidence before expanding an agent to a new region. What approach fits?

Domain: Evaluating and Deploying Agentic Workflows

- A. Use staged rollout with measurable rollback criteria
- B. Set explicit pass thresholds before evaluating
- C. Run evaluation on every meaningful change
- D. Compare variants with controlled traffic and shared metrics

### 45. Online evaluation itself adds latency and model cost. How should it be designed?

Domain: Evaluating and Deploying Agentic Workflows

- A. Track token and tool cost per completed task
- B. Monitor production behavior with online evaluation
- C. Provision capacity for peak concurrency and quotas
- D. Use Cloud Logging, Cloud Trace, and Cloud Monitoring

### 46. A regression suite takes longer than the release cadence allows. What is a sound approach?

Domain: Evaluating and Deploying Agentic Workflows

- A. Run evaluation on every meaningful change
- B. Use human review for unresolved or high-impact judgment
- C. Set explicit pass thresholds before evaluating
- D. Author an ADK evalset with expected tool use and responses

### 47. A gradual quality decline is invisible week to week. What should be tracked?

Domain: Evaluating and Deploying Agentic Workflows

- A. Record agent actions and tool calls in audit logs
- B. Compare variants with controlled traffic and shared metrics
- C. Detect changes in inputs, data, or performance over time
- D. Set explicit pass thresholds before evaluating

### 48. A production sample contains a potential policy violation. What should happen?

Domain: Evaluating and Deploying Agentic Workflows

- A. Monitor production behavior with online evaluation
- B. Use human review for unresolved or high-impact judgment
- C. Encode organizational policy in enforceable controls
- D. Use Cloud Logging, Cloud Trace, and Cloud Monitoring

### 49. A change passes all tests but adds substantial latency. What should the release gate include?

Domain: Evaluating and Deploying Agentic Workflows

- A. Set explicit pass thresholds before evaluating
- B. Compare variants with controlled traffic and shared metrics
- C. Use staged rollout with measurable rollback criteria
- D. Run evaluation on every meaningful change

### 50. A team wants a managed runtime for agents with sessions and memory integration. What should it evaluate?

Domain: Evaluating and Deploying Agentic Workflows

- A. Deploy to Agent Runtime for managed agent hosting
- B. Keep the service stateless and externalize session data
- C. Use GKE when you need cluster-level control and custom orchestration
- D. Deploy to Cloud Run for containerized request-driven services

### 51. A stateless API agent should scale to zero and handle short requests. What fits?

Domain: Evaluating and Deploying Agentic Workflows

- A. Use GKE when you need cluster-level control and custom orchestration
- B. Deploy to Agent Runtime for managed agent hosting
- C. Deploy to Cloud Run for containerized request-driven services
- D. Use Cloud Workstations for managed developer environments

### 52. A workload requires custom node pools, networking, and scheduling. What fits?

Domain: Evaluating and Deploying Agentic Workflows

- A. Deploy to Agent Runtime for managed agent hosting
- B. Deploy to Cloud Run for containerized request-driven services
- C. Use GKE when you need cluster-level control and custom orchestration
- D. Use Firestore for low-latency document-oriented state

### 53. A service loses conversations during deployments because sessions live in memory. What should change?

Domain: Evaluating and Deploying Agentic Workflows

- A. Use Cloud SQL for relational state and transactions
- B. Keep the service stateless and externalize session data
- C. Persist sessions in a durable managed store
- D. Use Memorystore for Redis for fast shared ephemeral state

### 54. A stateless agent design needs shared conversation continuity. What must be added?

Domain: Evaluating and Deploying Agentic Workflows

- A. Keep the service stateless and externalize session data
- B. Deploy to Cloud Run for containerized request-driven services
- C. Deploy to Agent Runtime for managed agent hosting
- D. Provision capacity for peak concurrency and quotas

### 55. An agent performs long-running document analysis beyond typical request limits. What should be designed?

Domain: Evaluating and Deploying Agentic Workflows

- A. Provision capacity for peak concurrency and quotas
- B. Track token and tool cost per completed task
- C. Set an end-to-end latency budget
- D. Set timeouts and bounded retries for tool calls

### 56. A team wants managed scaling but needs a custom sidecar and network policy. What trade-off should it evaluate?

Domain: Evaluating and Deploying Agentic Workflows

- A. Deploy to Cloud Run for containerized request-driven services
- B. Deploy to Agent Runtime for managed agent hosting
- C. Use GKE when you need cluster-level control and custom orchestration
- D. Use Memorystore for Redis for fast shared ephemeral state

### 57. A service has bursty traffic with long idle periods. What runtime characteristic matters?

Domain: Evaluating and Deploying Agentic Workflows

- A. Deploy to Agent Runtime for managed agent hosting
- B. Deploy to Cloud Run for containerized request-driven services
- C. Use BigQuery for governed analytical access to enterprise data
- D. Use GKE when you need cluster-level control and custom orchestration

### 58. A conversational agent needs per-session documents with low-latency reads. What storage fits?

Domain: Evaluating and Deploying Agentic Workflows

- A. Use Cloud SQL for relational state and transactions
- B. Use Firestore for low-latency document-oriented state
- C. Use Cloud Storage for large artifacts and source documents
- D. Persist sessions in a durable managed store

### 59. An agent must query governed analytical data with cost controls. What service fits?

Domain: Evaluating and Deploying Agentic Workflows

- A. Use Memorystore for Redis for fast shared ephemeral state
- B. Use Cloud Storage for large artifacts and source documents
- C. Use BigQuery for governed analytical access to enterprise data
- D. Use Cloud SQL for relational state and transactions

### 60. Large generated reports must persist beyond a conversation. What should be used?

Domain: Evaluating and Deploying Agentic Workflows

- A. Use Firestore for low-latency document-oriented state
- B. Use Cloud SQL for relational state and transactions
- C. Pass files and large outputs as artifacts
- D. Use Cloud Storage for large artifacts and source documents

### 61. A team wants minimal infrastructure management for a simple agent API. What fits?

Domain: Evaluating and Deploying Agentic Workflows

- A. Deploy to Agent Runtime for managed agent hosting
- B. Keep the service stateless and externalize session data
- C. Use GKE when you need cluster-level control and custom orchestration
- D. Deploy to Cloud Run for containerized request-driven services

### 62. A deployment plan ignores model and tool quotas. What is the likely outcome?

Domain: Evaluating and Deploying Agentic Workflows

- A. Use staged rollout with measurable rollback criteria
- B. Track token and tool cost per completed task
- C. Set an end-to-end latency budget
- D. Provision capacity for peak concurrency and quotas

### 63. Multiple agent workers need fast shared coordination with ephemeral data. What fits?

Domain: Evaluating and Deploying Agentic Workflows

- A. Persist sessions in a durable managed store
- B. Use Memorystore for Redis for fast shared ephemeral state
- C. Use Firestore for low-latency document-oriented state
- D. Use Cloud SQL for relational state and transactions

### 64. A team needs a managed environment for both agent deployment and evaluation workflows. What should it assess?

Domain: Evaluating and Deploying Agentic Workflows

- A. Deploy to Cloud Run for containerized request-driven services
- B. Use Cloud Workstations for managed developer environments
- C. Use GKE when you need cluster-level control and custom orchestration
- D. Deploy to Agent Runtime for managed agent hosting

### 65. An agent needs transactional records for order changes. What storage fits?

Domain: Evaluating and Deploying Agentic Workflows

- A. Use BigQuery for governed analytical access to enterprise data
- B. Use Cloud Storage for large artifacts and source documents
- C. Use Cloud SQL for relational state and transactions
- D. Use Memorystore for Redis for fast shared ephemeral state

### 66. A new runtime is adopted without load testing. What risk should be addressed?

Domain: Evaluating and Deploying Agentic Workflows

- A. Use staged rollout with measurable rollback criteria
- B. Use Cloud Logging, Cloud Trace, and Cloud Monitoring
- C. Keep the service stateless and externalize session data
- D. Provision capacity for peak concurrency and quotas

### 67. An agent's answers degrade gradually after a source schema change. What should be investigated first?

Domain: Evaluating and Deploying Agentic Workflows

- A. Inspect spans across agent, model, and tool calls
- B. Set timeouts and bounded retries for tool calls
- C. Detect changes in inputs, data, or performance over time
- D. Bound iterations and detect reasoning loops

### 68. An agent repeatedly calls the same search tool without progress. What should be implemented?

Domain: Evaluating and Deploying Agentic Workflows

- A. Bound iterations and detect reasoning loops
- B. Set timeouts and bounded retries for tool calls
- C. Detect changes in inputs, data, or performance over time
- D. Inspect spans across agent, model, and tool calls

### 69. A tool call occasionally hangs and blocks the workflow. What should be added?

Domain: Evaluating and Deploying Agentic Workflows

- A. Return structured tool errors that guide recovery
- B. Bound iterations and detect reasoning loops
- C. Set timeouts and bounded retries for tool calls
- D. Inspect spans across agent, model, and tool calls

### 70. A request is slow, but it is unclear which step dominates. What should be inspected?

Domain: Evaluating and Deploying Agentic Workflows

- A. Use Cloud Logging, Cloud Trace, and Cloud Monitoring
- B. Inspect spans across agent, model, and tool calls
- C. Bound iterations and detect reasoning loops
- D. Detect changes in inputs, data, or performance over time

### 71. A tool returns a permission error that the agent retries indefinitely. What should change?

Domain: Evaluating and Deploying Agentic Workflows

- A. Set timeouts and bounded retries for tool calls
- B. Use human review for unresolved or high-impact judgment
- C. Inspect spans across agent, model, and tool calls
- D. Return structured tool errors that guide recovery

### 72. A provider updates a model and tool-call behavior changes. What should detect the effect?

Domain: Evaluating and Deploying Agentic Workflows

- A. Run evaluation on every meaningful change
- B. Set explicit pass thresholds before evaluating
- C. Use Cloud Logging, Cloud Trace, and Cloud Monitoring
- D. Detect changes in inputs, data, or performance over time

### 73. A planner keeps decomposing a task into smaller subtasks without executing them. What control addresses this?

Domain: Evaluating and Deploying Agentic Workflows

- A. Run agents in a fixed sequence
- B. Bound iterations and detect reasoning loops
- C. Use a graph workflow for branching dependencies
- D. Run independent agents concurrently

### 74. A workflow succeeds but costs far more than expected. What should be analyzed?

Domain: Evaluating and Deploying Agentic Workflows

- A. Inspect spans across agent, model, and tool calls
- B. Provision capacity for peak concurrency and quotas
- C. Record agent actions and tool calls in audit logs
- D. Track token and tool cost per completed task

### 75. A retry duplicates a payment because the first call succeeded but timed out. What is missing?

Domain: Evaluating and Deploying Agentic Workflows

- A. Set timeouts and bounded retries for tool calls
- B. Return structured tool errors that guide recovery
- C. Inspect spans across agent, model, and tool calls
- D. Detect changes in inputs, data, or performance over time

### 76. A new user cohort asks shorter, more ambiguous questions. What should be monitored?

Domain: Evaluating and Deploying Agentic Workflows

- A. Detect changes in inputs, data, or performance over time
- B. Set explicit pass thresholds before evaluating
- C. Monitor production behavior with online evaluation
- D. Use human review for unresolved or high-impact judgment

### 77. An agent cannot resolve a conflict after several attempts. What should happen?

Domain: Evaluating and Deploying Agentic Workflows

- A. Enforce a policy check before a consequential action
- B. Require human approval before a consequential action
- C. Bound iterations and detect reasoning loops
- D. Gate the action on explicit, attributable approval

### 78. Logs show tool errors but not which agent initiated them. What should be improved?

Domain: Evaluating and Deploying Agentic Workflows

- A. Govern agent traffic through Agent Gateway
- B. Record agent actions and tool calls in audit logs
- C. Use Cloud Logging, Cloud Trace, and Cloud Monitoring
- D. Inspect spans across agent, model, and tool calls

### 79. A retrieval service exceeds its latency budget during peak load. What should be evaluated?

Domain: Evaluating and Deploying Agentic Workflows

- A. Provision capacity for peak concurrency and quotas
- B. Use staged rollout with measurable rollback criteria
- C. Set timeouts and bounded retries for tool calls
- D. Set an end-to-end latency budget

### 80. A drift alert fires but no evaluation case covers the changed behavior. What should follow?

Domain: Evaluating and Deploying Agentic Workflows

- A. Run evaluation on every meaningful change
- B. Author an ADK evalset with expected tool use and responses
- C. Detect changes in inputs, data, or performance over time
- D. Set explicit pass thresholds before evaluating

### 81. A tool returns a validation error with a clear field-level message. What should the agent do?

Domain: Evaluating and Deploying Agentic Workflows

- A. Inspect spans across agent, model, and tool calls
- B. Return structured tool errors that guide recovery
- C. Set timeouts and bounded retries for tool calls
- D. Bound iterations and detect reasoning loops

### 82. An agent's error rate rises only for long conversations. What should be examined?

Domain: Evaluating and Deploying Agentic Workflows

- A. Track token and tool cost per completed task
- B. Use Cloud Logging, Cloud Trace, and Cloud Monitoring
- C. Use staged rollout with measurable rollback criteria
- D. Provision capacity for peak concurrency and quotas

### 83. A correct answer was produced, but the tool arguments were wrong. What reveals this?

Domain: Evaluating and Deploying Agentic Workflows

- A. Use human review for unresolved or high-impact judgment
- B. Detect changes in inputs, data, or performance over time
- C. Inspect spans across agent, model, and tool calls
- D. Record agent actions and tool calls in audit logs

### 84. A platform team needs end-to-end visibility into agent behavior and failures. What should it implement?

Domain: Evaluating and Deploying Agentic Workflows

- A. Govern agent traffic through Agent Gateway
- B. Inspect spans across agent, model, and tool calls
- C. Use Cloud Logging, Cloud Trace, and Cloud Monitoring
- D. Record agent actions and tool calls in audit logs

### 85. A team wants to control spend per completed task. What should it measure?

Domain: Evaluating and Deploying Agentic Workflows

- A. Set explicit pass thresholds before evaluating
- B. Track token and tool cost per completed task
- C. Provision capacity for peak concurrency and quotas
- D. Use staged rollout with measurable rollback criteria

### 86. An agent meets quality targets but violates peak latency goals. What should be optimized?

Domain: Evaluating and Deploying Agentic Workflows

- A. Use staged rollout with measurable rollback criteria
- B. Set an end-to-end latency budget
- C. Provision capacity for peak concurrency and quotas
- D. Use Cloud Logging, Cloud Trace, and Cloud Monitoring

### 87. A new version reduces cost but increases escalations. What decision framework fits?

Domain: Evaluating and Deploying Agentic Workflows

- A. Use staged rollout with measurable rollback criteria
- B. Run evaluation on every meaningful change
- C. Set explicit pass thresholds before evaluating
- D. Compare variants with controlled traffic and shared metrics

### 88. An auditor asks who approved a high-impact action taken by an agent. What evidence is needed?

Domain: Evaluating and Deploying Agentic Workflows

- A. Record agent actions and tool calls in audit logs
- B. Govern agent traffic through Agent Gateway
- C. Use Cloud Logging, Cloud Trace, and Cloud Monitoring
- D. Encode organizational policy in enforceable controls

### 89. Traffic doubles unexpectedly, and the runtime throttles. What should be reviewed?

Domain: Evaluating and Deploying Agentic Workflows

- A. Use GKE when you need cluster-level control and custom orchestration
- B. Deploy to Cloud Run for containerized request-driven services
- C. Deploy to Agent Runtime for managed agent hosting
- D. Provision capacity for peak concurrency and quotas

### 90. A team wants to find which tool causes most failures. What should it analyze?

Domain: Evaluating and Deploying Agentic Workflows

- A. Detect changes in inputs, data, or performance over time
- B. Inspect spans across agent, model, and tool calls
- C. Track token and tool cost per completed task
- D. Use Cloud Logging, Cloud Trace, and Cloud Monitoring

### 91. A canary shows a small quality drop within an acceptable range. What should happen?

Domain: Evaluating and Deploying Agentic Workflows

- A. Use Cloud Logging, Cloud Trace, and Cloud Monitoring
- B. Set explicit pass thresholds before evaluating
- C. Use human review for unresolved or high-impact judgment
- D. Use staged rollout with measurable rollback criteria

### 92. A prompt change increases tokens but slightly improves quality. What should be evaluated?

Domain: Evaluating and Deploying Agentic Workflows

- A. Provision capacity for peak concurrency and quotas
- B. Use Cloud Logging, Cloud Trace, and Cloud Monitoring
- C. Set an end-to-end latency budget
- D. Track token and tool cost per completed task

### 93. An agent's traffic is not visible at the network or policy layer. What should be added?

Domain: Evaluating and Deploying Agentic Workflows

- A. Record agent actions and tool calls in audit logs
- B. Govern agent traffic through Agent Gateway
- C. Use Cloud Logging, Cloud Trace, and Cloud Monitoring
- D. Encode organizational policy in enforceable controls

### 94. A team wants early warning of changing user behavior. What should it monitor?

Domain: Evaluating and Deploying Agentic Workflows

- A. Monitor production behavior with online evaluation
- B. Detect changes in inputs, data, or performance over time
- C. Run evaluation on every meaningful change
- D. Use Cloud Logging, Cloud Trace, and Cloud Monitoring

### 95. Leaders ask whether an agent is ready for wider release. What evidence should be presented?

Domain: Evaluating and Deploying Agentic Workflows

- A. Use human review for unresolved or high-impact judgment
- B. Use staged rollout with measurable rollback criteria
- C. Set explicit pass thresholds before evaluating
- D. Use a calibrated model-based autorater for scalable judgment

### 96. Autoscaling creates many cold starts and higher tail latency. What should be evaluated?

Domain: Evaluating and Deploying Agentic Workflows

- A. Track token and tool cost per completed task
- B. Deploy to Cloud Run for containerized request-driven services
- C. Provision capacity for peak concurrency and quotas
- D. Keep the service stateless and externalize session data

### 97. An agent calls a tool that is not in the approved registry. What should happen?

Domain: Evaluating and Deploying Agentic Workflows

- A. Register agents and capabilities in Agent Registry
- B. Govern agent traffic through Agent Gateway
- C. Encode organizational policy in enforceable controls
- D. Record agent actions and tool calls in audit logs

### 98. A recurring hallucination appears only in one document type. What should be done?

Domain: Evaluating and Deploying Agentic Workflows

- A. Detect changes in inputs, data, or performance over time
- B. Use Cloud Logging, Cloud Trace, and Cloud Monitoring
- C. Use human review for unresolved or high-impact judgment
- D. Inspect spans across agent, model, and tool calls

### 99. A team plans a full launch based on one week of favorable metrics. What is missing?

Domain: Evaluating and Deploying Agentic Workflows

- A. Use staged rollout with measurable rollback criteria
- B. Compare variants with controlled traffic and shared metrics
- C. Set explicit pass thresholds before evaluating
- D. Run evaluation on every meaningful change

### 100. A cost optimization removes a validation step. What must be verified before adoption?

Domain: Evaluating and Deploying Agentic Workflows

- A. Use staged rollout with measurable rollback criteria
- B. Provision capacity for peak concurrency and quotas
- C. Set an end-to-end latency budget
- D. Track token and tool cost per completed task

---

## Answer key and explanations

### Question 1 — B

Answer: Build a representative golden dataset from real tasks. A representative golden dataset drawn from real task patterns and expected outcomes. A golden set anchors evaluation in expected behavior and evidence. It should cover normal, rare, and risky cases. Local study-map skill 4.1 (Evaluation Test Sets), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: A representative golden dataset drawn from real task patterns and expected outcomes.
- **B:** Correct. A golden set anchors evaluation in expected behavior and evidence. It should cover normal, rare, and risky cases. In this case: A representative golden dataset drawn from real task patterns and expected outcomes.
- **C:** Incorrect for this question. Boundary and hostile inputs reveal failures that happy-path tests miss. Include prompt injection and missing-data cases. In this case: A representative golden dataset drawn from real task patterns and expected outcomes.
- **D:** Incorrect for this question. An evalset gives repeatable evidence for agent behavior. It must be maintained as the workflow changes. In this case: A representative golden dataset drawn from real task patterns and expected outcomes.

### Question 2 — D

Answer: Include edge cases and adversarial inputs in test sets. Explicit edge cases, including adversarial and incomplete inputs. Boundary and hostile inputs reveal failures that happy-path tests miss. Include prompt injection and missing-data cases. Local study-map skill 4.1 (Evaluation Test Sets), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. In this case: Explicit edge cases, including adversarial and incomplete inputs.
- **B:** Incorrect for this question. A golden set anchors evaluation in expected behavior and evidence. It should cover normal, rare, and risky cases. In this case: Explicit edge cases, including adversarial and incomplete inputs.
- **C:** Incorrect for this question. Autoraters can score nuanced qualities at scale. They require calibration against human judgments and periodic review. In this case: Explicit edge cases, including adversarial and incomplete inputs.
- **D:** Correct. Boundary and hostile inputs reveal failures that happy-path tests miss. Include prompt injection and missing-data cases. In this case: Explicit edge cases, including adversarial and incomplete inputs.

### Question 3 — B

Answer: Build a representative golden dataset from real tasks. It will overstate readiness for multi-step and ambiguous production work. A golden set anchors evaluation in expected behavior and evidence. It should cover normal, rare, and risky cases. Local study-map skill 4.1 (Evaluation Test Sets), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. An evalset gives repeatable evidence for agent behavior. It must be maintained as the workflow changes. In this case: It will overstate readiness for multi-step and ambiguous production work.
- **B:** Correct. A golden set anchors evaluation in expected behavior and evidence. It should cover normal, rare, and risky cases. In this case: It will overstate readiness for multi-step and ambiguous production work.
- **C:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: It will overstate readiness for multi-step and ambiguous production work.
- **D:** Incorrect for this question. A correct answer can hide an unsafe or wasteful action sequence. Trajectory checks verify which tools were called and with what arguments. In this case: It will overstate readiness for multi-step and ambiguous production work.

### Question 4 — D

Answer: Include edge cases and adversarial inputs in test sets. Adversarial cases that attempt to override instructions or exfiltrate data. Boundary and hostile inputs reveal failures that happy-path tests miss. Include prompt injection and missing-data cases. Local study-map skill 4.1 (Evaluation Test Sets), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. A golden set anchors evaluation in expected behavior and evidence. It should cover normal, rare, and risky cases. In this case: Adversarial cases that attempt to override instructions or exfiltrate data.
- **B:** Incorrect for this question. Controlled comparison supports evidence-based rollout. Changing several variables at once confuses attribution. In this case: Adversarial cases that attempt to override instructions or exfiltrate data.
- **C:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Adversarial cases that attempt to override instructions or exfiltrate data.
- **D:** Correct. Boundary and hostile inputs reveal failures that happy-path tests miss. Include prompt injection and missing-data cases. In this case: Adversarial cases that attempt to override instructions or exfiltrate data.

### Question 5 — A

Answer: Build a representative golden dataset from real tasks. Record adjudicated expected behavior and keep the disagreement visible for review. A golden set anchors evaluation in expected behavior and evidence. It should cover normal, rare, and risky cases. Local study-map skill 4.1 (Evaluation Test Sets), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Correct. A golden set anchors evaluation in expected behavior and evidence. It should cover normal, rare, and risky cases. In this case: Record adjudicated expected behavior and keep the disagreement visible for review.
- **B:** Incorrect for this question. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. In this case: Record adjudicated expected behavior and keep the disagreement visible for review.
- **C:** Incorrect for this question. Autoraters can score nuanced qualities at scale. They require calibration against human judgments and periodic review. In this case: Record adjudicated expected behavior and keep the disagreement visible for review.
- **D:** Incorrect for this question. Prompts, models, tools, and data can all change behavior. Regression testing catches unintended effects. In this case: Record adjudicated expected behavior and keep the disagreement visible for review.

### Question 6 — B

Answer: Set explicit pass thresholds before evaluating. Task-specific criteria and measurement method for each quality dimension. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. Local study-map skill 4.1 (Evaluation Test Sets), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. A correct answer can hide an unsafe or wasteful action sequence. Trajectory checks verify which tools were called and with what arguments. In this case: Task-specific criteria and measurement method for each quality dimension.
- **B:** Correct. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Task-specific criteria and measurement method for each quality dimension.
- **C:** Incorrect for this question. A golden set anchors evaluation in expected behavior and evidence. It should cover normal, rare, and risky cases. In this case: Task-specific criteria and measurement method for each quality dimension.
- **D:** Incorrect for this question. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. In this case: Task-specific criteria and measurement method for each quality dimension.

### Question 7 — B

Answer: Include edge cases and adversarial inputs in test sets. Representative samples of the new formats and their boundary cases. Boundary and hostile inputs reveal failures that happy-path tests miss. Include prompt injection and missing-data cases. Local study-map skill 4.1 (Evaluation Test Sets), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Controlled comparison supports evidence-based rollout. Changing several variables at once confuses attribution. In this case: Representative samples of the new formats and their boundary cases.
- **B:** Correct. Boundary and hostile inputs reveal failures that happy-path tests miss. Include prompt injection and missing-data cases. In this case: Representative samples of the new formats and their boundary cases.
- **C:** Incorrect for this question. A golden set anchors evaluation in expected behavior and evidence. It should cover normal, rare, and risky cases. In this case: Representative samples of the new formats and their boundary cases.
- **D:** Incorrect for this question. Prompts, models, tools, and data can all change behavior. Regression testing catches unintended effects. In this case: Representative samples of the new formats and their boundary cases.

### Question 8 — D

Answer: Build a representative golden dataset from real tasks. It is not representative, so results will not predict local performance. A golden set anchors evaluation in expected behavior and evidence. It should cover normal, rare, and risky cases. Local study-map skill 4.1 (Evaluation Test Sets), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. An evalset gives repeatable evidence for agent behavior. It must be maintained as the workflow changes. In this case: It is not representative, so results will not predict local performance.
- **B:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: It is not representative, so results will not predict local performance.
- **C:** Incorrect for this question. Autoraters can score nuanced qualities at scale. They require calibration against human judgments and periodic review. In this case: It is not representative, so results will not predict local performance.
- **D:** Correct. A golden set anchors evaluation in expected behavior and evidence. It should cover normal, rare, and risky cases. In this case: It is not representative, so results will not predict local performance.

### Question 9 — B

Answer: Use human review for unresolved or high-impact judgment. Include it deliberately in the test set and route real occurrences to review. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. Local study-map skill 4.1 (Evaluation Test Sets), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. A golden set anchors evaluation in expected behavior and evidence. It should cover normal, rare, and risky cases. In this case: Include it deliberately in the test set and route real occurrences to review.
- **B:** Correct. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. In this case: Include it deliberately in the test set and route real occurrences to review.
- **C:** Incorrect for this question. Boundary and hostile inputs reveal failures that happy-path tests miss. Include prompt injection and missing-data cases. In this case: Include it deliberately in the test set and route real occurrences to review.
- **D:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Include it deliberately in the test set and route real occurrences to review.

### Question 10 — A

Answer: Author an ADK evalset with expected tool use and responses. It overweights one behavior and distorts aggregate scores. An evalset gives repeatable evidence for agent behavior. It must be maintained as the workflow changes. Local study-map skill 4.1 (Evaluation Test Sets), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Correct. An evalset gives repeatable evidence for agent behavior. It must be maintained as the workflow changes. In this case: It overweights one behavior and distorts aggregate scores.
- **B:** Incorrect for this question. A golden set anchors evaluation in expected behavior and evidence. It should cover normal, rare, and risky cases. In this case: It overweights one behavior and distorts aggregate scores.
- **C:** Incorrect for this question. Prompts, models, tools, and data can all change behavior. Regression testing catches unintended effects. In this case: It overweights one behavior and distorts aggregate scores.
- **D:** Incorrect for this question. Production traffic reveals distribution and failure patterns that offline sets miss. Sampling and privacy must be designed. In this case: It overweights one behavior and distorts aggregate scores.

### Question 11 — A

Answer: Include edge cases and adversarial inputs in test sets. Escalate to the accountable owner and encode the decision in expected behavior. Boundary and hostile inputs reveal failures that happy-path tests miss. Include prompt injection and missing-data cases. Local study-map skill 4.1 (Evaluation Test Sets), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Correct. Boundary and hostile inputs reveal failures that happy-path tests miss. Include prompt injection and missing-data cases. In this case: Escalate to the accountable owner and encode the decision in expected behavior.
- **B:** Incorrect for this question. A golden set anchors evaluation in expected behavior and evidence. It should cover normal, rare, and risky cases. In this case: Escalate to the accountable owner and encode the decision in expected behavior.
- **C:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Escalate to the accountable owner and encode the decision in expected behavior.
- **D:** Incorrect for this question. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. In this case: Escalate to the accountable owner and encode the decision in expected behavior.

### Question 12 — D

Answer: Build a representative golden dataset from real tasks. Whether the agent used the right tools and arguments. A golden set anchors evaluation in expected behavior and evidence. It should cover normal, rare, and risky cases. Local study-map skill 4.1 (Evaluation Test Sets), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. An evalset gives repeatable evidence for agent behavior. It must be maintained as the workflow changes. In this case: Whether the agent used the right tools and arguments.
- **B:** Incorrect for this question. A correct answer can hide an unsafe or wasteful action sequence. Trajectory checks verify which tools were called and with what arguments. In this case: Whether the agent used the right tools and arguments.
- **C:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Whether the agent used the right tools and arguments.
- **D:** Correct. A golden set anchors evaluation in expected behavior and evidence. It should cover normal, rare, and risky cases. In this case: Whether the agent used the right tools and arguments.

### Question 13 — C

Answer: Compare variants with controlled traffic and shared metrics. Stratify cases by policy context rather than average incompatible expectations. Controlled comparison supports evidence-based rollout. Changing several variables at once confuses attribution. Local study-map skill 4.1 (Evaluation Test Sets), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. A golden set anchors evaluation in expected behavior and evidence. It should cover normal, rare, and risky cases. In this case: Stratify cases by policy context rather than average incompatible expectations.
- **B:** Incorrect for this question. Boundary and hostile inputs reveal failures that happy-path tests miss. Include prompt injection and missing-data cases. In this case: Stratify cases by policy context rather than average incompatible expectations.
- **C:** Correct. Controlled comparison supports evidence-based rollout. Changing several variables at once confuses attribution. In this case: Stratify cases by policy context rather than average incompatible expectations.
- **D:** Incorrect for this question. Prompts, models, tools, and data can all change behavior. Regression testing catches unintended effects. In this case: Stratify cases by policy context rather than average incompatible expectations.

### Question 14 — B

Answer: Author an ADK evalset with expected tool use and responses. Add a regression case reproducing the failure before the fix is accepted. An evalset gives repeatable evidence for agent behavior. It must be maintained as the workflow changes. Local study-map skill 4.1 (Evaluation Test Sets), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Production traffic reveals distribution and failure patterns that offline sets miss. Sampling and privacy must be designed. In this case: Add a regression case reproducing the failure before the fix is accepted.
- **B:** Correct. An evalset gives repeatable evidence for agent behavior. It must be maintained as the workflow changes. In this case: Add a regression case reproducing the failure before the fix is accepted.
- **C:** Incorrect for this question. Prompts, models, tools, and data can all change behavior. Regression testing catches unintended effects. In this case: Add a regression case reproducing the failure before the fix is accepted.
- **D:** Incorrect for this question. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. In this case: Add a regression case reproducing the failure before the fix is accepted.

### Question 15 — D

Answer: Use human review for unresolved or high-impact judgment. Calibrate or restrict the judge and add human review for that category. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. Local study-map skill 4.1 (Evaluation Test Sets), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Autoraters can score nuanced qualities at scale. They require calibration against human judgments and periodic review. In this case: Calibrate or restrict the judge and add human review for that category.
- **B:** Incorrect for this question. A golden set anchors evaluation in expected behavior and evidence. It should cover normal, rare, and risky cases. In this case: Calibrate or restrict the judge and add human review for that category.
- **C:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Calibrate or restrict the judge and add human review for that category.
- **D:** Correct. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. In this case: Calibrate or restrict the judge and add human review for that category.

### Question 16 — A

Answer: Build a representative golden dataset from real tasks. Results become irreproducible and stale expectations go unnoticed. A golden set anchors evaluation in expected behavior and evidence. It should cover normal, rare, and risky cases. Local study-map skill 4.1 (Evaluation Test Sets), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Correct. A golden set anchors evaluation in expected behavior and evidence. It should cover normal, rare, and risky cases. In this case: Results become irreproducible and stale expectations go unnoticed.
- **B:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Results become irreproducible and stale expectations go unnoticed.
- **C:** Incorrect for this question. Boundary and hostile inputs reveal failures that happy-path tests miss. Include prompt injection and missing-data cases. In this case: Results become irreproducible and stale expectations go unnoticed.
- **D:** Incorrect for this question. Quotas and scaling limits can become the real bottleneck. Plan for bursts and graceful degradation. In this case: Results become irreproducible and stale expectations go unnoticed.

### Question 17 — D

Answer: Evaluate tool-call trajectories, not only final text. Trajectory evaluation of tool calls, arguments, and side effects. A correct answer can hide an unsafe or wasteful action sequence. Trajectory checks verify which tools were called and with what arguments. Local study-map skill 4.2 (Evaluation Metrics and Tooling), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Generation cannot compensate for missing evidence. Retrieval metrics localize pipeline failures. In this case: Trajectory evaluation of tool calls, arguments, and side effects.
- **B:** Incorrect for this question. Autoraters can score nuanced qualities at scale. They require calibration against human judgments and periodic review. In this case: Trajectory evaluation of tool calls, arguments, and side effects.
- **C:** Incorrect for this question. Response metrics assess what the user receives. They should be tied to explicit task criteria. In this case: Trajectory evaluation of tool calls, arguments, and side effects.
- **D:** Correct. A correct answer can hide an unsafe or wasteful action sequence. Trajectory checks verify which tools were called and with what arguments. In this case: Trajectory evaluation of tool calls, arguments, and side effects.

### Question 18 — B

Answer: Score response correctness, completeness, and helpfulness. Response completeness against explicit task criteria. Response metrics assess what the user receives. They should be tied to explicit task criteria. Local study-map skill 4.2 (Evaluation Metrics and Tooling), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Citations let users check claims against sources. Grounding reduces but does not eliminate hallucination. In this case: Response completeness against explicit task criteria.
- **B:** Correct. Response metrics assess what the user receives. They should be tied to explicit task criteria. In this case: Response completeness against explicit task criteria.
- **C:** Incorrect for this question. Generation cannot compensate for missing evidence. Retrieval metrics localize pipeline failures. In this case: Response completeness against explicit task criteria.
- **D:** Incorrect for this question. A correct answer can hide an unsafe or wasteful action sequence. Trajectory checks verify which tools were called and with what arguments. In this case: Response completeness against explicit task criteria.

### Question 19 — A

Answer: Measure retrieval relevance and recall separately. Retrieval relevance and groundedness of the cited evidence. Generation cannot compensate for missing evidence. Retrieval metrics localize pipeline failures. Local study-map skill 4.2 (Evaluation Metrics and Tooling), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Correct. Generation cannot compensate for missing evidence. Retrieval metrics localize pipeline failures. In this case: Retrieval relevance and groundedness of the cited evidence.
- **B:** Incorrect for this question. A correct answer can hide an unsafe or wasteful action sequence. Trajectory checks verify which tools were called and with what arguments. In this case: Retrieval relevance and groundedness of the cited evidence.
- **C:** Incorrect for this question. Citations let users check claims against sources. Grounding reduces but does not eliminate hallucination. In this case: Retrieval relevance and groundedness of the cited evidence.
- **D:** Incorrect for this question. Response metrics assess what the user receives. They should be tied to explicit task criteria. In this case: Retrieval relevance and groundedness of the cited evidence.

### Question 20 — C

Answer: Author an ADK evalset with expected tool use and responses. An evalset with expected trajectory and response criteria. An evalset gives repeatable evidence for agent behavior. It must be maintained as the workflow changes. Local study-map skill 4.2 (Evaluation Metrics and Tooling), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: An evalset with expected trajectory and response criteria.
- **B:** Incorrect for this question. A correct answer can hide an unsafe or wasteful action sequence. Trajectory checks verify which tools were called and with what arguments. In this case: An evalset with expected trajectory and response criteria.
- **C:** Correct. An evalset gives repeatable evidence for agent behavior. It must be maintained as the workflow changes. In this case: An evalset with expected trajectory and response criteria.
- **D:** Incorrect for this question. Autoraters can score nuanced qualities at scale. They require calibration against human judgments and periodic review. In this case: An evalset with expected trajectory and response criteria.

### Question 21 — C

Answer: Use a calibrated model-based autorater for scalable judgment. Calibration against human judgments and periodic review. Autoraters can score nuanced qualities at scale. They require calibration against human judgments and periodic review. Local study-map skill 4.2 (Evaluation Metrics and Tooling), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Calibration against human judgments and periodic review.
- **B:** Incorrect for this question. Response metrics assess what the user receives. They should be tied to explicit task criteria. In this case: Calibration against human judgments and periodic review.
- **C:** Correct. Autoraters can score nuanced qualities at scale. They require calibration against human judgments and periodic review. In this case: Calibration against human judgments and periodic review.
- **D:** Incorrect for this question. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. In this case: Calibration against human judgments and periodic review.

### Question 22 — A

Answer: Use human review for unresolved or high-impact judgment. Accountable human review using explicit criteria. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. Local study-map skill 4.2 (Evaluation Metrics and Tooling), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Correct. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. In this case: Accountable human review using explicit criteria.
- **B:** Incorrect for this question. A correct answer can hide an unsafe or wasteful action sequence. Trajectory checks verify which tools were called and with what arguments. In this case: Accountable human review using explicit criteria.
- **C:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Accountable human review using explicit criteria.
- **D:** Incorrect for this question. Autoraters can score nuanced qualities at scale. They require calibration against human judgments and periodic review. In this case: Accountable human review using explicit criteria.

### Question 23 — D

Answer: Set explicit pass thresholds before evaluating. A pre-agreed pass threshold and a blocking gate for that metric. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. Local study-map skill 4.2 (Evaluation Metrics and Tooling), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Response metrics assess what the user receives. They should be tied to explicit task criteria. In this case: A pre-agreed pass threshold and a blocking gate for that metric.
- **B:** Incorrect for this question. A correct answer can hide an unsafe or wasteful action sequence. Trajectory checks verify which tools were called and with what arguments. In this case: A pre-agreed pass threshold and a blocking gate for that metric.
- **C:** Incorrect for this question. Generation cannot compensate for missing evidence. Retrieval metrics localize pipeline failures. In this case: A pre-agreed pass threshold and a blocking gate for that metric.
- **D:** Correct. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: A pre-agreed pass threshold and a blocking gate for that metric.

### Question 24 — B

Answer: Evaluate tool-call trajectories, not only final text. Response quality may look acceptable while groundedness fails. A correct answer can hide an unsafe or wasteful action sequence. Trajectory checks verify which tools were called and with what arguments. Local study-map skill 4.2 (Evaluation Metrics and Tooling), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Citations let users check claims against sources. Grounding reduces but does not eliminate hallucination. In this case: Response quality may look acceptable while groundedness fails.
- **B:** Correct. A correct answer can hide an unsafe or wasteful action sequence. Trajectory checks verify which tools were called and with what arguments. In this case: Response quality may look acceptable while groundedness fails.
- **C:** Incorrect for this question. Generation cannot compensate for missing evidence. Retrieval metrics localize pipeline failures. In this case: Response quality may look acceptable while groundedness fails.
- **D:** Incorrect for this question. Response metrics assess what the user receives. They should be tied to explicit task criteria. In this case: Response quality may look acceptable while groundedness fails.

### Question 25 — C

Answer: Score response correctness, completeness, and helpfulness. Trajectory efficiency and unnecessary calls alongside success. Response metrics assess what the user receives. They should be tied to explicit task criteria. Local study-map skill 4.2 (Evaluation Metrics and Tooling), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Autoraters can score nuanced qualities at scale. They require calibration against human judgments and periodic review. In this case: Trajectory efficiency and unnecessary calls alongside success.
- **B:** Incorrect for this question. A correct answer can hide an unsafe or wasteful action sequence. Trajectory checks verify which tools were called and with what arguments. In this case: Trajectory efficiency and unnecessary calls alongside success.
- **C:** Correct. Response metrics assess what the user receives. They should be tied to explicit task criteria. In this case: Trajectory efficiency and unnecessary calls alongside success.
- **D:** Incorrect for this question. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. In this case: Trajectory efficiency and unnecessary calls alongside success.

### Question 26 — D

Answer: Measure retrieval relevance and recall separately. Whether answer accuracy and groundedness improve or degrade. Generation cannot compensate for missing evidence. Retrieval metrics localize pipeline failures. Local study-map skill 4.2 (Evaluation Metrics and Tooling), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Response metrics assess what the user receives. They should be tied to explicit task criteria. In this case: Whether answer accuracy and groundedness improve or degrade.
- **B:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Whether answer accuracy and groundedness improve or degrade.
- **C:** Incorrect for this question. Citations let users check claims against sources. Grounding reduces but does not eliminate hallucination. In this case: Whether answer accuracy and groundedness improve or degrade.
- **D:** Correct. Generation cannot compensate for missing evidence. Retrieval metrics localize pipeline failures. In this case: Whether answer accuracy and groundedness improve or degrade.

### Question 27 — D

Answer: Use a calibrated model-based autorater for scalable judgment. Self-preference bias; use independent judges and human calibration. Autoraters can score nuanced qualities at scale. They require calibration against human judgments and periodic review. Local study-map skill 4.2 (Evaluation Metrics and Tooling), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Self-preference bias; use independent judges and human calibration.
- **B:** Incorrect for this question. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. In this case: Self-preference bias; use independent judges and human calibration.
- **C:** Incorrect for this question. An evalset gives repeatable evidence for agent behavior. It must be maintained as the workflow changes. In this case: Self-preference bias; use independent judges and human calibration.
- **D:** Correct. Autoraters can score nuanced qualities at scale. They require calibration against human judgments and periodic review. In this case: Self-preference bias; use independent judges and human calibration.

### Question 28 — A

Answer: Evaluate tool-call trajectories, not only final text. An unauthorized refund executed and then described in a correct-sounding answer. A correct answer can hide an unsafe or wasteful action sequence. Trajectory checks verify which tools were called and with what arguments. Local study-map skill 4.2 (Evaluation Metrics and Tooling), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Correct. A correct answer can hide an unsafe or wasteful action sequence. Trajectory checks verify which tools were called and with what arguments. In this case: An unauthorized refund executed and then described in a correct-sounding answer.
- **B:** Incorrect for this question. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. In this case: An unauthorized refund executed and then described in a correct-sounding answer.
- **C:** Incorrect for this question. An evalset gives repeatable evidence for agent behavior. It must be maintained as the workflow changes. In this case: An unauthorized refund executed and then described in a correct-sounding answer.
- **D:** Incorrect for this question. Response metrics assess what the user receives. They should be tied to explicit task criteria. In this case: An unauthorized refund executed and then described in a correct-sounding answer.

### Question 29 — B

Answer: Use human review for unresolved or high-impact judgment. Block the action and require attributable approval. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. Local study-map skill 4.2 (Evaluation Metrics and Tooling), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. A correct answer can hide an unsafe or wasteful action sequence. Trajectory checks verify which tools were called and with what arguments. In this case: Block the action and require attributable approval.
- **B:** Correct. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. In this case: Block the action and require attributable approval.
- **C:** Incorrect for this question. Autoraters can score nuanced qualities at scale. They require calibration against human judgments and periodic review. In this case: Block the action and require attributable approval.
- **D:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Block the action and require attributable approval.

### Question 30 — A

Answer: Ground the response in cited retrieved evidence. A groundedness deficiency even if the conclusion is right. Citations let users check claims against sources. Grounding reduces but does not eliminate hallucination. Local study-map skill 4.2 (Evaluation Metrics and Tooling), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Correct. Citations let users check claims against sources. Grounding reduces but does not eliminate hallucination. In this case: A groundedness deficiency even if the conclusion is right.
- **B:** Incorrect for this question. Response metrics assess what the user receives. They should be tied to explicit task criteria. In this case: A groundedness deficiency even if the conclusion is right.
- **C:** Incorrect for this question. A correct answer can hide an unsafe or wasteful action sequence. Trajectory checks verify which tools were called and with what arguments. In this case: A groundedness deficiency even if the conclusion is right.
- **D:** Incorrect for this question. Generation cannot compensate for missing evidence. Retrieval metrics localize pipeline failures. In this case: A groundedness deficiency even if the conclusion is right.

### Question 31 — C

Answer: Set explicit pass thresholds before evaluating. Task success, trajectory quality, and cost per successful task. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. Local study-map skill 4.2 (Evaluation Metrics and Tooling), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. A correct answer can hide an unsafe or wasteful action sequence. Trajectory checks verify which tools were called and with what arguments. In this case: Task success, trajectory quality, and cost per successful task.
- **B:** Incorrect for this question. Response metrics assess what the user receives. They should be tied to explicit task criteria. In this case: Task success, trajectory quality, and cost per successful task.
- **C:** Correct. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Task success, trajectory quality, and cost per successful task.
- **D:** Incorrect for this question. Cost attribution supports optimization and budgeting. Per-task cost reveals expensive failure paths. In this case: Task success, trajectory quality, and cost per successful task.

### Question 32 — C

Answer: Author an ADK evalset with expected tool use and responses. The evaluation no longer detects real regressions. An evalset gives repeatable evidence for agent behavior. It must be maintained as the workflow changes. Local study-map skill 4.2 (Evaluation Metrics and Tooling), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: The evaluation no longer detects real regressions.
- **B:** Incorrect for this question. Prompts, models, tools, and data can all change behavior. Regression testing catches unintended effects. In this case: The evaluation no longer detects real regressions.
- **C:** Correct. An evalset gives repeatable evidence for agent behavior. It must be maintained as the workflow changes. In this case: The evaluation no longer detects real regressions.
- **D:** Incorrect for this question. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. In this case: The evaluation no longer detects real regressions.

### Question 33 — C

Answer: Use a calibrated model-based autorater for scalable judgment. Use explicit rubric criteria and validate scores against human ratings. Autoraters can score nuanced qualities at scale. They require calibration against human judgments and periodic review. Local study-map skill 4.2 (Evaluation Metrics and Tooling), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Citations let users check claims against sources. Grounding reduces but does not eliminate hallucination. In this case: Use explicit rubric criteria and validate scores against human ratings.
- **B:** Incorrect for this question. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. In this case: Use explicit rubric criteria and validate scores against human ratings.
- **C:** Correct. Autoraters can score nuanced qualities at scale. They require calibration against human judgments and periodic review. In this case: Use explicit rubric criteria and validate scores against human ratings.
- **D:** Incorrect for this question. Response metrics assess what the user receives. They should be tied to explicit task criteria. In this case: Use explicit rubric criteria and validate scores against human ratings.

### Question 34 — D

Answer: Run evaluation on every meaningful change. Regression evaluation on representative sets plus staged online monitoring. Prompts, models, tools, and data can all change behavior. Regression testing catches unintended effects. Local study-map skill 4.3 (Continuous Evaluation and Regression), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Controlled comparison supports evidence-based rollout. Changing several variables at once confuses attribution. In this case: Regression evaluation on representative sets plus staged online monitoring.
- **B:** Incorrect for this question. Production traffic reveals distribution and failure patterns that offline sets miss. Sampling and privacy must be designed. In this case: Regression evaluation on representative sets plus staged online monitoring.
- **C:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Regression evaluation on representative sets plus staged online monitoring.
- **D:** Correct. Prompts, models, tools, and data can all change behavior. Regression testing catches unintended effects. In this case: Regression evaluation on representative sets plus staged online monitoring.

### Question 35 — C

Answer: Monitor production behavior with online evaluation. Online quality and failure patterns on sampled real traffic. Production traffic reveals distribution and failure patterns that offline sets miss. Sampling and privacy must be designed. Local study-map skill 4.3 (Continuous Evaluation and Regression), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Online quality and failure patterns on sampled real traffic.
- **B:** Incorrect for this question. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. In this case: Online quality and failure patterns on sampled real traffic.
- **C:** Correct. Production traffic reveals distribution and failure patterns that offline sets miss. Sampling and privacy must be designed. In this case: Online quality and failure patterns on sampled real traffic.
- **D:** Incorrect for this question. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. In this case: Online quality and failure patterns on sampled real traffic.

### Question 36 — A

Answer: Compare variants with controlled traffic and shared metrics. Effects cannot be attributed; change one variable where feasible. Controlled comparison supports evidence-based rollout. Changing several variables at once confuses attribution. Local study-map skill 4.3 (Continuous Evaluation and Regression), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Correct. Controlled comparison supports evidence-based rollout. Changing several variables at once confuses attribution. In this case: Effects cannot be attributed; change one variable where feasible.
- **B:** Incorrect for this question. Cost attribution supports optimization and budgeting. Per-task cost reveals expensive failure paths. In this case: Effects cannot be attributed; change one variable where feasible.
- **C:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Effects cannot be attributed; change one variable where feasible.
- **D:** Incorrect for this question. Prompts, models, tools, and data can all change behavior. Regression testing catches unintended effects. In this case: Effects cannot be attributed; change one variable where feasible.

### Question 37 — B

Answer: Set explicit pass thresholds before evaluating. Evaluate segment-level thresholds, not only the aggregate. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. Local study-map skill 4.3 (Continuous Evaluation and Regression), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. A canary or phased rollout limits exposure while evidence accumulates. Rollback must be practical, not theoretical. In this case: Evaluate segment-level thresholds, not only the aggregate.
- **B:** Correct. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Evaluate segment-level thresholds, not only the aggregate.
- **C:** Incorrect for this question. Prompts, models, tools, and data can all change behavior. Regression testing catches unintended effects. In this case: Evaluate segment-level thresholds, not only the aggregate.
- **D:** Incorrect for this question. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. In this case: Evaluate segment-level thresholds, not only the aggregate.

### Question 38 — D

Answer: Monitor production behavior with online evaluation. Minimization, access control, and retention rules for evaluation data. Production traffic reveals distribution and failure patterns that offline sets miss. Sampling and privacy must be designed. Local study-map skill 4.3 (Continuous Evaluation and Regression), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. In this case: Minimization, access control, and retention rules for evaluation data.
- **B:** Incorrect for this question. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. In this case: Minimization, access control, and retention rules for evaluation data.
- **C:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Minimization, access control, and retention rules for evaluation data.
- **D:** Correct. Production traffic reveals distribution and failure patterns that offline sets miss. Sampling and privacy must be designed. In this case: Minimization, access control, and retention rules for evaluation data.

### Question 39 — C

Answer: Run evaluation on every meaningful change. Re-run the evaluation suite and compare against thresholds before rollout. Prompts, models, tools, and data can all change behavior. Regression testing catches unintended effects. Local study-map skill 4.3 (Continuous Evaluation and Regression), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Models, sources, and user behavior change. Monitoring detects when evaluation assumptions no longer hold. In this case: Re-run the evaluation suite and compare against thresholds before rollout.
- **B:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Re-run the evaluation suite and compare against thresholds before rollout.
- **C:** Correct. Prompts, models, tools, and data can all change behavior. Regression testing catches unintended effects. In this case: Re-run the evaluation suite and compare against thresholds before rollout.
- **D:** Incorrect for this question. An evalset gives repeatable evidence for agent behavior. It must be maintained as the workflow changes. In this case: Re-run the evaluation suite and compare against thresholds before rollout.

### Question 40 — C

Answer: Compare variants with controlled traffic and shared metrics. Pause or roll back using the pre-agreed criteria and investigate. Controlled comparison supports evidence-based rollout. Changing several variables at once confuses attribution. Local study-map skill 4.3 (Continuous Evaluation and Regression), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. A canary or phased rollout limits exposure while evidence accumulates. Rollback must be practical, not theoretical. In this case: Pause or roll back using the pre-agreed criteria and investigate.
- **B:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Pause or roll back using the pre-agreed criteria and investigate.
- **C:** Correct. Controlled comparison supports evidence-based rollout. Changing several variables at once confuses attribution. In this case: Pause or roll back using the pre-agreed criteria and investigate.
- **D:** Incorrect for this question. Quotas and scaling limits can become the real bottleneck. Plan for bursts and graceful degradation. In this case: Pause or roll back using the pre-agreed criteria and investigate.

### Question 41 — A

Answer: Use Cloud Logging, Cloud Trace, and Cloud Monitoring. Trajectory monitoring and alerting on tool-use patterns. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. Local study-map skill 4.3 (Continuous Evaluation and Regression), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Correct. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. In this case: Trajectory monitoring and alerting on tool-use patterns.
- **B:** Incorrect for this question. Prompts, models, tools, and data can all change behavior. Regression testing catches unintended effects. In this case: Trajectory monitoring and alerting on tool-use patterns.
- **C:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Trajectory monitoring and alerting on tool-use patterns.
- **D:** Incorrect for this question. Production traffic reveals distribution and failure patterns that offline sets miss. Sampling and privacy must be designed. In this case: Trajectory monitoring and alerting on tool-use patterns.

### Question 42 — D

Answer: Set explicit pass thresholds before evaluating. The scorer calibration and the sampling method. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. Local study-map skill 4.3 (Continuous Evaluation and Regression), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Production traffic reveals distribution and failure patterns that offline sets miss. Sampling and privacy must be designed. In this case: The scorer calibration and the sampling method.
- **B:** Incorrect for this question. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. In this case: The scorer calibration and the sampling method.
- **C:** Incorrect for this question. Autoraters can score nuanced qualities at scale. They require calibration against human judgments and periodic review. In this case: The scorer calibration and the sampling method.
- **D:** Correct. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: The scorer calibration and the sampling method.

### Question 43 — B

Answer: Run evaluation on every meaningful change. Representative evaluation data and drift monitoring for the new segment. Prompts, models, tools, and data can all change behavior. Regression testing catches unintended effects. Local study-map skill 4.3 (Continuous Evaluation and Regression), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Models, sources, and user behavior change. Monitoring detects when evaluation assumptions no longer hold. In this case: Representative evaluation data and drift monitoring for the new segment.
- **B:** Correct. Prompts, models, tools, and data can all change behavior. Regression testing catches unintended effects. In this case: Representative evaluation data and drift monitoring for the new segment.
- **C:** Incorrect for this question. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. In this case: Representative evaluation data and drift monitoring for the new segment.
- **D:** Incorrect for this question. An evalset gives repeatable evidence for agent behavior. It must be maintained as the workflow changes. In this case: Representative evaluation data and drift monitoring for the new segment.

### Question 44 — A

Answer: Use staged rollout with measurable rollback criteria. A limited rollout with region-specific evaluation and monitoring. A canary or phased rollout limits exposure while evidence accumulates. Rollback must be practical, not theoretical. Local study-map skill 4.3 (Continuous Evaluation and Regression), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Correct. A canary or phased rollout limits exposure while evidence accumulates. Rollback must be practical, not theoretical. In this case: A limited rollout with region-specific evaluation and monitoring.
- **B:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: A limited rollout with region-specific evaluation and monitoring.
- **C:** Incorrect for this question. Prompts, models, tools, and data can all change behavior. Regression testing catches unintended effects. In this case: A limited rollout with region-specific evaluation and monitoring.
- **D:** Incorrect for this question. Controlled comparison supports evidence-based rollout. Changing several variables at once confuses attribution. In this case: A limited rollout with region-specific evaluation and monitoring.

### Question 45 — B

Answer: Monitor production behavior with online evaluation. Sample traffic and evaluate asynchronously outside the response path. Production traffic reveals distribution and failure patterns that offline sets miss. Sampling and privacy must be designed. Local study-map skill 4.3 (Continuous Evaluation and Regression), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Cost attribution supports optimization and budgeting. Per-task cost reveals expensive failure paths. In this case: Sample traffic and evaluate asynchronously outside the response path.
- **B:** Correct. Production traffic reveals distribution and failure patterns that offline sets miss. Sampling and privacy must be designed. In this case: Sample traffic and evaluate asynchronously outside the response path.
- **C:** Incorrect for this question. Quotas and scaling limits can become the real bottleneck. Plan for bursts and graceful degradation. In this case: Sample traffic and evaluate asynchronously outside the response path.
- **D:** Incorrect for this question. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. In this case: Sample traffic and evaluate asynchronously outside the response path.

### Question 46 — A

Answer: Run evaluation on every meaningful change. Tier the suite into fast blocking checks and broader scheduled evaluation. Prompts, models, tools, and data can all change behavior. Regression testing catches unintended effects. Local study-map skill 4.3 (Continuous Evaluation and Regression), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Correct. Prompts, models, tools, and data can all change behavior. Regression testing catches unintended effects. In this case: Tier the suite into fast blocking checks and broader scheduled evaluation.
- **B:** Incorrect for this question. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. In this case: Tier the suite into fast blocking checks and broader scheduled evaluation.
- **C:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Tier the suite into fast blocking checks and broader scheduled evaluation.
- **D:** Incorrect for this question. An evalset gives repeatable evidence for agent behavior. It must be maintained as the workflow changes. In this case: Tier the suite into fast blocking checks and broader scheduled evaluation.

### Question 47 — C

Answer: Detect changes in inputs, data, or performance over time. Rolling metrics with baselines and alerts over time. Models, sources, and user behavior change. Monitoring detects when evaluation assumptions no longer hold. Local study-map skill 4.3 (Continuous Evaluation and Regression), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Rolling metrics with baselines and alerts over time.
- **B:** Incorrect for this question. Controlled comparison supports evidence-based rollout. Changing several variables at once confuses attribution. In this case: Rolling metrics with baselines and alerts over time.
- **C:** Correct. Models, sources, and user behavior change. Monitoring detects when evaluation assumptions no longer hold. In this case: Rolling metrics with baselines and alerts over time.
- **D:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Rolling metrics with baselines and alerts over time.

### Question 48 — A

Answer: Monitor production behavior with online evaluation. Route to the responsible team and preserve evidence under policy. Production traffic reveals distribution and failure patterns that offline sets miss. Sampling and privacy must be designed. Local study-map skill 4.3 (Continuous Evaluation and Regression), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Correct. Production traffic reveals distribution and failure patterns that offline sets miss. Sampling and privacy must be designed. In this case: Route to the responsible team and preserve evidence under policy.
- **B:** Incorrect for this question. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. In this case: Route to the responsible team and preserve evidence under policy.
- **C:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Route to the responsible team and preserve evidence under policy.
- **D:** Incorrect for this question. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. In this case: Route to the responsible team and preserve evidence under policy.

### Question 49 — D

Answer: Run evaluation on every meaningful change. Latency budgets and cost thresholds in addition to quality. Prompts, models, tools, and data can all change behavior. Regression testing catches unintended effects. Local study-map skill 4.3 (Continuous Evaluation and Regression), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Latency budgets and cost thresholds in addition to quality.
- **B:** Incorrect for this question. Controlled comparison supports evidence-based rollout. Changing several variables at once confuses attribution. In this case: Latency budgets and cost thresholds in addition to quality.
- **C:** Incorrect for this question. A canary or phased rollout limits exposure while evidence accumulates. Rollback must be practical, not theoretical. In this case: Latency budgets and cost thresholds in addition to quality.
- **D:** Correct. Prompts, models, tools, and data can all change behavior. Regression testing catches unintended effects. In this case: Latency budgets and cost thresholds in addition to quality.

### Question 50 — A

Answer: Deploy to Agent Runtime for managed agent hosting. Agent Runtime for supported managed hosting. Agent Runtime provides managed hosting and agent platform integration. It is not automatically the best fit for every workload. Local study-map skill 4.4 (Runtime Selection), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Correct. Agent Runtime provides managed hosting and agent platform integration. It is not automatically the best fit for every workload. In this case: Agent Runtime for supported managed hosting.
- **B:** Incorrect for this question. Stateless services scale and recover more predictably. External state introduces its own availability and security requirements. In this case: Agent Runtime for supported managed hosting.
- **C:** Incorrect for this question. GKE offers flexibility for complex workloads at higher operational cost. Use it when requirements justify that control. In this case: Agent Runtime for supported managed hosting.
- **D:** Incorrect for this question. Cloud Run suits stateless or externally-stateful container services with managed scaling. Design sessions and long tasks accordingly. In this case: Agent Runtime for supported managed hosting.

### Question 51 — C

Answer: Deploy to Cloud Run for containerized request-driven services. Cloud Run fits a stateless service when session data is externalized to a managed store. Cloud Run suits stateless or externally-stateful container services with managed scaling. Design sessions and long tasks accordingly. Local study-map skill 4.4 (Runtime Selection), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. GKE offers flexibility for complex workloads at higher operational cost. Use it when requirements justify that control. In this case: Cloud Run fits a stateless service when session data is externalized to a managed store.
- **B:** Incorrect for this question. Agent Runtime provides managed hosting and agent platform integration. It is not automatically the best fit for every workload. In this case: Cloud Run fits a stateless service when session data is externalized to a managed store.
- **C:** Correct. Cloud Run suits stateless or externally-stateful container services with managed scaling. Design sessions and long tasks accordingly. In this case: Cloud Run fits a stateless service when session data is externalized to a managed store.
- **D:** Incorrect for this question. Managed workstations provide controlled, reproducible development sessions. They should still use least privilege and approved network paths. In this case: Cloud Run fits a stateless service when session data is externalized to a managed store.

### Question 52 — C

Answer: Use GKE when you need cluster-level control and custom orchestration. GKE with dedicated infrastructure and policy. GKE offers flexibility for complex workloads at higher operational cost. Use it when requirements justify that control. Local study-map skill 4.4 (Runtime Selection), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Agent Runtime provides managed hosting and agent platform integration. It is not automatically the best fit for every workload. In this case: GKE with dedicated infrastructure and policy.
- **B:** Incorrect for this question. Cloud Run suits stateless or externally-stateful container services with managed scaling. Design sessions and long tasks accordingly. In this case: GKE with dedicated infrastructure and policy.
- **C:** Correct. GKE offers flexibility for complex workloads at higher operational cost. Use it when requirements justify that control. In this case: GKE with dedicated infrastructure and policy.
- **D:** Incorrect for this question. Firestore can serve per-session documents and real-time access patterns. Model access and consistency deliberately. In this case: GKE with dedicated infrastructure and policy.

### Question 53 — C

Answer: Persist sessions in a durable managed store. Persist sessions in an external durable store. Durable session storage supports continuity and recovery. Retention and isolation rules still apply. Local study-map skill 4.4 (Runtime Selection), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Relational storage fits structured, transactional data. It is usually not the first choice for high-frequency session blobs. In this case: Persist sessions in an external durable store.
- **B:** Incorrect for this question. Stateless services scale and recover more predictably. External state introduces its own availability and security requirements. In this case: Persist sessions in an external durable store.
- **C:** Correct. Durable session storage supports continuity and recovery. Retention and isolation rules still apply. In this case: Persist sessions in an external durable store.
- **D:** Incorrect for this question. An in-memory store can reduce latency for coordination and caching. It is not durable evidence storage by default. In this case: Persist sessions in an external durable store.

### Question 54 — A

Answer: Keep the service stateless and externalize session data. An external session store keyed by conversation and identity. Stateless services scale and recover more predictably. External state introduces its own availability and security requirements. Local study-map skill 4.4 (Runtime Selection), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Correct. Stateless services scale and recover more predictably. External state introduces its own availability and security requirements. In this case: An external session store keyed by conversation and identity.
- **B:** Incorrect for this question. Cloud Run suits stateless or externally-stateful container services with managed scaling. Design sessions and long tasks accordingly. In this case: An external session store keyed by conversation and identity.
- **C:** Incorrect for this question. Agent Runtime provides managed hosting and agent platform integration. It is not automatically the best fit for every workload. In this case: An external session store keyed by conversation and identity.
- **D:** Incorrect for this question. Quotas and scaling limits can become the real bottleneck. Plan for bursts and graceful degradation. In this case: An external session store keyed by conversation and identity.

### Question 55 — A

Answer: Provision capacity for peak concurrency and quotas. Asynchronous execution with status tracking and appropriate timeouts. Quotas and scaling limits can become the real bottleneck. Plan for bursts and graceful degradation. Local study-map skill 4.4 (Runtime Selection), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Correct. Quotas and scaling limits can become the real bottleneck. Plan for bursts and graceful degradation. In this case: Asynchronous execution with status tracking and appropriate timeouts.
- **B:** Incorrect for this question. Cost attribution supports optimization and budgeting. Per-task cost reveals expensive failure paths. In this case: Asynchronous execution with status tracking and appropriate timeouts.
- **C:** Incorrect for this question. User experience depends on retrieval, tool calls, model turns, and approval. Optimize the whole path, not only generation time. In this case: Asynchronous execution with status tracking and appropriate timeouts.
- **D:** Incorrect for this question. Timeouts protect the workflow from stalled dependencies. Retries must avoid duplicating consequential actions. In this case: Asynchronous execution with status tracking and appropriate timeouts.

### Question 56 — B

Answer: Deploy to Agent Runtime for managed agent hosting. The control of GKE versus the operational simplicity of managed runtimes. Agent Runtime provides managed hosting and agent platform integration. It is not automatically the best fit for every workload. Local study-map skill 4.4 (Runtime Selection), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Cloud Run suits stateless or externally-stateful container services with managed scaling. Design sessions and long tasks accordingly. In this case: The control of GKE versus the operational simplicity of managed runtimes.
- **B:** Correct. Agent Runtime provides managed hosting and agent platform integration. It is not automatically the best fit for every workload. In this case: The control of GKE versus the operational simplicity of managed runtimes.
- **C:** Incorrect for this question. GKE offers flexibility for complex workloads at higher operational cost. Use it when requirements justify that control. In this case: The control of GKE versus the operational simplicity of managed runtimes.
- **D:** Incorrect for this question. An in-memory store can reduce latency for coordination and caching. It is not durable evidence storage by default. In this case: The control of GKE versus the operational simplicity of managed runtimes.

### Question 57 — B

Answer: Deploy to Cloud Run for containerized request-driven services. Scale-to-zero or rapid scaling with acceptable cold-start behavior. Cloud Run suits stateless or externally-stateful container services with managed scaling. Design sessions and long tasks accordingly. Local study-map skill 4.4 (Runtime Selection), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Agent Runtime provides managed hosting and agent platform integration. It is not automatically the best fit for every workload. In this case: Scale-to-zero or rapid scaling with acceptable cold-start behavior.
- **B:** Correct. Cloud Run suits stateless or externally-stateful container services with managed scaling. Design sessions and long tasks accordingly. In this case: Scale-to-zero or rapid scaling with acceptable cold-start behavior.
- **C:** Incorrect for this question. BigQuery can support analytics and controlled data sharing. Agent queries still need authorization and cost limits. In this case: Scale-to-zero or rapid scaling with acceptable cold-start behavior.
- **D:** Incorrect for this question. GKE offers flexibility for complex workloads at higher operational cost. Use it when requirements justify that control. In this case: Scale-to-zero or rapid scaling with acceptable cold-start behavior.

### Question 58 — B

Answer: Use Firestore for low-latency document-oriented state. A document store designed for session access. Firestore can serve per-session documents and real-time access patterns. Model access and consistency deliberately. Local study-map skill 4.4 (Runtime Selection), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Relational storage fits structured, transactional data. It is usually not the first choice for high-frequency session blobs. In this case: A document store designed for session access.
- **B:** Correct. Firestore can serve per-session documents and real-time access patterns. Model access and consistency deliberately. In this case: A document store designed for session access.
- **C:** Incorrect for this question. Object storage is appropriate for files, models, and large outputs. Apply lifecycle and access controls. In this case: A document store designed for session access.
- **D:** Incorrect for this question. Durable session storage supports continuity and recovery. Retention and isolation rules still apply. In this case: A document store designed for session access.

### Question 59 — C

Answer: Use BigQuery for governed analytical access to enterprise data. BigQuery with appropriate authorization and query limits. BigQuery can support analytics and controlled data sharing. Agent queries still need authorization and cost limits. Local study-map skill 4.4 (Runtime Selection), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. An in-memory store can reduce latency for coordination and caching. It is not durable evidence storage by default. In this case: BigQuery with appropriate authorization and query limits.
- **B:** Incorrect for this question. Object storage is appropriate for files, models, and large outputs. Apply lifecycle and access controls. In this case: BigQuery with appropriate authorization and query limits.
- **C:** Correct. BigQuery can support analytics and controlled data sharing. Agent queries still need authorization and cost limits. In this case: BigQuery with appropriate authorization and query limits.
- **D:** Incorrect for this question. Relational storage fits structured, transactional data. It is usually not the first choice for high-frequency session blobs. In this case: BigQuery with appropriate authorization and query limits.

### Question 60 — D

Answer: Use Cloud Storage for large artifacts and source documents. Cloud Storage or an artifact store with lifecycle and access controls. Object storage is appropriate for files, models, and large outputs. Apply lifecycle and access controls. Local study-map skill 4.4 (Runtime Selection), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Firestore can serve per-session documents and real-time access patterns. Model access and consistency deliberately. In this case: Cloud Storage or an artifact store with lifecycle and access controls.
- **B:** Incorrect for this question. Relational storage fits structured, transactional data. It is usually not the first choice for high-frequency session blobs. In this case: Cloud Storage or an artifact store with lifecycle and access controls.
- **C:** Incorrect for this question. Artifacts keep large content out of the prompt and provide a durable reference. They still require access control and validation. In this case: Cloud Storage or an artifact store with lifecycle and access controls.
- **D:** Correct. Object storage is appropriate for files, models, and large outputs. Apply lifecycle and access controls. In this case: Cloud Storage or an artifact store with lifecycle and access controls.

### Question 61 — B

Answer: Keep the service stateless and externalize session data. A managed serverless or agent runtime rather than a custom cluster. Stateless services scale and recover more predictably. External state introduces its own availability and security requirements. Local study-map skill 4.4 (Runtime Selection), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Agent Runtime provides managed hosting and agent platform integration. It is not automatically the best fit for every workload. In this case: A managed serverless or agent runtime rather than a custom cluster.
- **B:** Correct. Stateless services scale and recover more predictably. External state introduces its own availability and security requirements. In this case: A managed serverless or agent runtime rather than a custom cluster.
- **C:** Incorrect for this question. GKE offers flexibility for complex workloads at higher operational cost. Use it when requirements justify that control. In this case: A managed serverless or agent runtime rather than a custom cluster.
- **D:** Incorrect for this question. Cloud Run suits stateless or externally-stateful container services with managed scaling. Design sessions and long tasks accordingly. In this case: A managed serverless or agent runtime rather than a custom cluster.

### Question 62 — D

Answer: Provision capacity for peak concurrency and quotas. Throttling and failures under peak load. Quotas and scaling limits can become the real bottleneck. Plan for bursts and graceful degradation. Local study-map skill 4.4 (Runtime Selection), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. A canary or phased rollout limits exposure while evidence accumulates. Rollback must be practical, not theoretical. In this case: Throttling and failures under peak load.
- **B:** Incorrect for this question. Cost attribution supports optimization and budgeting. Per-task cost reveals expensive failure paths. In this case: Throttling and failures under peak load.
- **C:** Incorrect for this question. User experience depends on retrieval, tool calls, model turns, and approval. Optimize the whole path, not only generation time. In this case: Throttling and failures under peak load.
- **D:** Correct. Quotas and scaling limits can become the real bottleneck. Plan for bursts and graceful degradation. In this case: Throttling and failures under peak load.

### Question 63 — B

Answer: Use Memorystore for Redis for fast shared ephemeral state. An in-memory data store with appropriate durability expectations. An in-memory store can reduce latency for coordination and caching. It is not durable evidence storage by default. Local study-map skill 4.4 (Runtime Selection), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Durable session storage supports continuity and recovery. Retention and isolation rules still apply. In this case: An in-memory data store with appropriate durability expectations.
- **B:** Correct. An in-memory store can reduce latency for coordination and caching. It is not durable evidence storage by default. In this case: An in-memory data store with appropriate durability expectations.
- **C:** Incorrect for this question. Firestore can serve per-session documents and real-time access patterns. Model access and consistency deliberately. In this case: An in-memory data store with appropriate durability expectations.
- **D:** Incorrect for this question. Relational storage fits structured, transactional data. It is usually not the first choice for high-frequency session blobs. In this case: An in-memory data store with appropriate durability expectations.

### Question 64 — D

Answer: Deploy to Agent Runtime for managed agent hosting. Whether the managed agent platform supports the required evaluation and session features. Agent Runtime provides managed hosting and agent platform integration. It is not automatically the best fit for every workload. Local study-map skill 4.4 (Runtime Selection), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Cloud Run suits stateless or externally-stateful container services with managed scaling. Design sessions and long tasks accordingly. In this case: Whether the managed agent platform supports the required evaluation and session features.
- **B:** Incorrect for this question. Managed workstations provide controlled, reproducible development sessions. They should still use least privilege and approved network paths. In this case: Whether the managed agent platform supports the required evaluation and session features.
- **C:** Incorrect for this question. GKE offers flexibility for complex workloads at higher operational cost. Use it when requirements justify that control. In this case: Whether the managed agent platform supports the required evaluation and session features.
- **D:** Correct. Agent Runtime provides managed hosting and agent platform integration. It is not automatically the best fit for every workload. In this case: Whether the managed agent platform supports the required evaluation and session features.

### Question 65 — C

Answer: Use Cloud SQL for relational state and transactions. A relational database with transactional guarantees. Relational storage fits structured, transactional data. It is usually not the first choice for high-frequency session blobs. Local study-map skill 4.4 (Runtime Selection), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. BigQuery can support analytics and controlled data sharing. Agent queries still need authorization and cost limits. In this case: A relational database with transactional guarantees.
- **B:** Incorrect for this question. Object storage is appropriate for files, models, and large outputs. Apply lifecycle and access controls. In this case: A relational database with transactional guarantees.
- **C:** Correct. Relational storage fits structured, transactional data. It is usually not the first choice for high-frequency session blobs. In this case: A relational database with transactional guarantees.
- **D:** Incorrect for this question. An in-memory store can reduce latency for coordination and caching. It is not durable evidence storage by default. In this case: A relational database with transactional guarantees.

### Question 66 — A

Answer: Use staged rollout with measurable rollback criteria. Unknown scaling limits and latency under realistic concurrency. A canary or phased rollout limits exposure while evidence accumulates. Rollback must be practical, not theoretical. Local study-map skill 4.4 (Runtime Selection), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Correct. A canary or phased rollout limits exposure while evidence accumulates. Rollback must be practical, not theoretical. In this case: Unknown scaling limits and latency under realistic concurrency.
- **B:** Incorrect for this question. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. In this case: Unknown scaling limits and latency under realistic concurrency.
- **C:** Incorrect for this question. Stateless services scale and recover more predictably. External state introduces its own availability and security requirements. In this case: Unknown scaling limits and latency under realistic concurrency.
- **D:** Incorrect for this question. Quotas and scaling limits can become the real bottleneck. Plan for bursts and graceful degradation. In this case: Unknown scaling limits and latency under realistic concurrency.

### Question 67 — C

Answer: Detect changes in inputs, data, or performance over time. Input and retrieval drift caused by the schema change. Models, sources, and user behavior change. Monitoring detects when evaluation assumptions no longer hold. Local study-map skill 4.5 (Troubleshooting Agent Failures), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Traces localize latency and failures in multi-step workflows. They are essential for debugging non-deterministic behavior. In this case: Input and retrieval drift caused by the schema change.
- **B:** Incorrect for this question. Timeouts protect the workflow from stalled dependencies. Retries must avoid duplicating consequential actions. In this case: Input and retrieval drift caused by the schema change.
- **C:** Correct. Models, sources, and user behavior change. Monitoring detects when evaluation assumptions no longer hold. In this case: Input and retrieval drift caused by the schema change.
- **D:** Incorrect for this question. A maximum step or time budget prevents runaway cost and repeated actions. Progress checks should trigger escalation. In this case: Input and retrieval drift caused by the schema change.

### Question 68 — A

Answer: Bound iterations and detect reasoning loops. A step or time limit with loop detection and escalation. A maximum step or time budget prevents runaway cost and repeated actions. Progress checks should trigger escalation. Local study-map skill 4.5 (Troubleshooting Agent Failures), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Correct. A maximum step or time budget prevents runaway cost and repeated actions. Progress checks should trigger escalation. In this case: A step or time limit with loop detection and escalation.
- **B:** Incorrect for this question. Timeouts protect the workflow from stalled dependencies. Retries must avoid duplicating consequential actions. In this case: A step or time limit with loop detection and escalation.
- **C:** Incorrect for this question. Models, sources, and user behavior change. Monitoring detects when evaluation assumptions no longer hold. In this case: A step or time limit with loop detection and escalation.
- **D:** Incorrect for this question. Traces localize latency and failures in multi-step workflows. They are essential for debugging non-deterministic behavior. In this case: A step or time limit with loop detection and escalation.

### Question 69 — C

Answer: Set timeouts and bounded retries for tool calls. Timeouts, bounded retries, and a clear failure path. Timeouts protect the workflow from stalled dependencies. Retries must avoid duplicating consequential actions. Local study-map skill 4.5 (Troubleshooting Agent Failures), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Actionable errors let the agent correct arguments or escalate. Silent failure or fabricated success is unsafe. In this case: Timeouts, bounded retries, and a clear failure path.
- **B:** Incorrect for this question. A maximum step or time budget prevents runaway cost and repeated actions. Progress checks should trigger escalation. In this case: Timeouts, bounded retries, and a clear failure path.
- **C:** Correct. Timeouts protect the workflow from stalled dependencies. Retries must avoid duplicating consequential actions. In this case: Timeouts, bounded retries, and a clear failure path.
- **D:** Incorrect for this question. Traces localize latency and failures in multi-step workflows. They are essential for debugging non-deterministic behavior. In this case: Timeouts, bounded retries, and a clear failure path.

### Question 70 — B

Answer: Inspect spans across agent, model, and tool calls. Distributed traces spanning model calls, retrieval, and tools. Traces localize latency and failures in multi-step workflows. They are essential for debugging non-deterministic behavior. Local study-map skill 4.5 (Troubleshooting Agent Failures), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. In this case: Distributed traces spanning model calls, retrieval, and tools.
- **B:** Correct. Traces localize latency and failures in multi-step workflows. They are essential for debugging non-deterministic behavior. In this case: Distributed traces spanning model calls, retrieval, and tools.
- **C:** Incorrect for this question. A maximum step or time budget prevents runaway cost and repeated actions. Progress checks should trigger escalation. In this case: Distributed traces spanning model calls, retrieval, and tools.
- **D:** Incorrect for this question. Models, sources, and user behavior change. Monitoring detects when evaluation assumptions no longer hold. In this case: Distributed traces spanning model calls, retrieval, and tools.

### Question 71 — D

Answer: Return structured tool errors that guide recovery. Classify the error as non-retryable and escalate instead of looping. Actionable errors let the agent correct arguments or escalate. Silent failure or fabricated success is unsafe. Local study-map skill 4.5 (Troubleshooting Agent Failures), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Timeouts protect the workflow from stalled dependencies. Retries must avoid duplicating consequential actions. In this case: Classify the error as non-retryable and escalate instead of looping.
- **B:** Incorrect for this question. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. In this case: Classify the error as non-retryable and escalate instead of looping.
- **C:** Incorrect for this question. Traces localize latency and failures in multi-step workflows. They are essential for debugging non-deterministic behavior. In this case: Classify the error as non-retryable and escalate instead of looping.
- **D:** Correct. Actionable errors let the agent correct arguments or escalate. Silent failure or fabricated success is unsafe. In this case: Classify the error as non-retryable and escalate instead of looping.

### Question 72 — D

Answer: Detect changes in inputs, data, or performance over time. Regression evaluation and production comparison against baselines. Models, sources, and user behavior change. Monitoring detects when evaluation assumptions no longer hold. Local study-map skill 4.5 (Troubleshooting Agent Failures), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Prompts, models, tools, and data can all change behavior. Regression testing catches unintended effects. In this case: Regression evaluation and production comparison against baselines.
- **B:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Regression evaluation and production comparison against baselines.
- **C:** Incorrect for this question. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. In this case: Regression evaluation and production comparison against baselines.
- **D:** Correct. Models, sources, and user behavior change. Monitoring detects when evaluation assumptions no longer hold. In this case: Regression evaluation and production comparison against baselines.

### Question 73 — B

Answer: Bound iterations and detect reasoning loops. A maximum planning depth with a requirement to act or escalate. A maximum step or time budget prevents runaway cost and repeated actions. Progress checks should trigger escalation. Local study-map skill 4.5 (Troubleshooting Agent Failures), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Sequential workflows make dependencies explicit and are easier to reason about. They may add latency when steps could run independently. In this case: A maximum planning depth with a requirement to act or escalate.
- **B:** Correct. A maximum step or time budget prevents runaway cost and repeated actions. Progress checks should trigger escalation. In this case: A maximum planning depth with a requirement to act or escalate.
- **C:** Incorrect for this question. Graphs express conditional paths and joins more clearly than a fixed chain. Complexity should be justified by real control flow. In this case: A maximum planning depth with a requirement to act or escalate.
- **D:** Incorrect for this question. Parallel branches reduce wall-clock time when work is truly independent. Shared state and reconciliation still require design. In this case: A maximum planning depth with a requirement to act or escalate.

### Question 74 — A

Answer: Inspect spans across agent, model, and tool calls. Per-step token and tool usage from traces and cost records. Traces localize latency and failures in multi-step workflows. They are essential for debugging non-deterministic behavior. Local study-map skill 4.5 (Troubleshooting Agent Failures), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Correct. Traces localize latency and failures in multi-step workflows. They are essential for debugging non-deterministic behavior. In this case: Per-step token and tool usage from traces and cost records.
- **B:** Incorrect for this question. Quotas and scaling limits can become the real bottleneck. Plan for bursts and graceful degradation. In this case: Per-step token and tool usage from traces and cost records.
- **C:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Per-step token and tool usage from traces and cost records.
- **D:** Incorrect for this question. Cost attribution supports optimization and budgeting. Per-task cost reveals expensive failure paths. In this case: Per-step token and tool usage from traces and cost records.

### Question 75 — A

Answer: Set timeouts and bounded retries for tool calls. Idempotency and a check for prior success before retry. Timeouts protect the workflow from stalled dependencies. Retries must avoid duplicating consequential actions. Local study-map skill 4.5 (Troubleshooting Agent Failures), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Correct. Timeouts protect the workflow from stalled dependencies. Retries must avoid duplicating consequential actions. In this case: Idempotency and a check for prior success before retry.
- **B:** Incorrect for this question. Actionable errors let the agent correct arguments or escalate. Silent failure or fabricated success is unsafe. In this case: Idempotency and a check for prior success before retry.
- **C:** Incorrect for this question. Traces localize latency and failures in multi-step workflows. They are essential for debugging non-deterministic behavior. In this case: Idempotency and a check for prior success before retry.
- **D:** Incorrect for this question. Models, sources, and user behavior change. Monitoring detects when evaluation assumptions no longer hold. In this case: Idempotency and a check for prior success before retry.

### Question 76 — A

Answer: Detect changes in inputs, data, or performance over time. Drift in input patterns and quality by segment. Models, sources, and user behavior change. Monitoring detects when evaluation assumptions no longer hold. Local study-map skill 4.5 (Troubleshooting Agent Failures), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Correct. Models, sources, and user behavior change. Monitoring detects when evaluation assumptions no longer hold. In this case: Drift in input patterns and quality by segment.
- **B:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Drift in input patterns and quality by segment.
- **C:** Incorrect for this question. Production traffic reveals distribution and failure patterns that offline sets miss. Sampling and privacy must be designed. In this case: Drift in input patterns and quality by segment.
- **D:** Incorrect for this question. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. In this case: Drift in input patterns and quality by segment.

### Question 77 — C

Answer: Bound iterations and detect reasoning loops. Escalate to a human rather than continue autonomously. A maximum step or time budget prevents runaway cost and repeated actions. Progress checks should trigger escalation. Local study-map skill 4.5 (Troubleshooting Agent Failures), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Guardrails constrain behavior in code or infrastructure, not only in prompts. The check must cover the actual action and identity. In this case: Escalate to a human rather than continue autonomously.
- **B:** Incorrect for this question. Human-in-the-loop review is appropriate when impact or uncertainty is high. Approval must occur before the effect and with enough context to decide. In this case: Escalate to a human rather than continue autonomously.
- **C:** Correct. A maximum step or time budget prevents runaway cost and repeated actions. Progress checks should trigger escalation. In this case: Escalate to a human rather than continue autonomously.
- **D:** Incorrect for this question. Approval should identify who approved what and under which evidence. A vague acknowledgment is not authorization. In this case: Escalate to a human rather than continue autonomously.

### Question 78 — D

Answer: Inspect spans across agent, model, and tool calls. Trace and log context that identifies the agent, session, and tool call. Traces localize latency and failures in multi-step workflows. They are essential for debugging non-deterministic behavior. Local study-map skill 4.5 (Troubleshooting Agent Failures), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Trace and log context that identifies the agent, session, and tool call.
- **B:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Trace and log context that identifies the agent, session, and tool call.
- **C:** Incorrect for this question. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. In this case: Trace and log context that identifies the agent, session, and tool call.
- **D:** Correct. Traces localize latency and failures in multi-step workflows. They are essential for debugging non-deterministic behavior. In this case: Trace and log context that identifies the agent, session, and tool call.

### Question 79 — C

Answer: Set timeouts and bounded retries for tool calls. Capacity, caching, and graceful degradation for the dependency. Timeouts protect the workflow from stalled dependencies. Retries must avoid duplicating consequential actions. Local study-map skill 4.5 (Troubleshooting Agent Failures), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Quotas and scaling limits can become the real bottleneck. Plan for bursts and graceful degradation. In this case: Capacity, caching, and graceful degradation for the dependency.
- **B:** Incorrect for this question. A canary or phased rollout limits exposure while evidence accumulates. Rollback must be practical, not theoretical. In this case: Capacity, caching, and graceful degradation for the dependency.
- **C:** Correct. Timeouts protect the workflow from stalled dependencies. Retries must avoid duplicating consequential actions. In this case: Capacity, caching, and graceful degradation for the dependency.
- **D:** Incorrect for this question. User experience depends on retrieval, tool calls, model turns, and approval. Optimize the whole path, not only generation time. In this case: Capacity, caching, and graceful degradation for the dependency.

### Question 80 — C

Answer: Detect changes in inputs, data, or performance over time. Add representative cases and decide whether behavior is acceptable. Models, sources, and user behavior change. Monitoring detects when evaluation assumptions no longer hold. Local study-map skill 4.5 (Troubleshooting Agent Failures), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Prompts, models, tools, and data can all change behavior. Regression testing catches unintended effects. In this case: Add representative cases and decide whether behavior is acceptable.
- **B:** Incorrect for this question. An evalset gives repeatable evidence for agent behavior. It must be maintained as the workflow changes. In this case: Add representative cases and decide whether behavior is acceptable.
- **C:** Correct. Models, sources, and user behavior change. Monitoring detects when evaluation assumptions no longer hold. In this case: Add representative cases and decide whether behavior is acceptable.
- **D:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Add representative cases and decide whether behavior is acceptable.

### Question 81 — B

Answer: Return structured tool errors that guide recovery. Correct the arguments within a bounded attempt and then escalate if needed. Actionable errors let the agent correct arguments or escalate. Silent failure or fabricated success is unsafe. Local study-map skill 4.5 (Troubleshooting Agent Failures), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Traces localize latency and failures in multi-step workflows. They are essential for debugging non-deterministic behavior. In this case: Correct the arguments within a bounded attempt and then escalate if needed.
- **B:** Correct. Actionable errors let the agent correct arguments or escalate. Silent failure or fabricated success is unsafe. In this case: Correct the arguments within a bounded attempt and then escalate if needed.
- **C:** Incorrect for this question. Timeouts protect the workflow from stalled dependencies. Retries must avoid duplicating consequential actions. In this case: Correct the arguments within a bounded attempt and then escalate if needed.
- **D:** Incorrect for this question. A maximum step or time budget prevents runaway cost and repeated actions. Progress checks should trigger escalation. In this case: Correct the arguments within a bounded attempt and then escalate if needed.

### Question 82 — B

Answer: Use Cloud Logging, Cloud Trace, and Cloud Monitoring. Context growth, truncation, and session-state behavior over time. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. Local study-map skill 4.5 (Troubleshooting Agent Failures), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Cost attribution supports optimization and budgeting. Per-task cost reveals expensive failure paths. In this case: Context growth, truncation, and session-state behavior over time.
- **B:** Correct. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. In this case: Context growth, truncation, and session-state behavior over time.
- **C:** Incorrect for this question. A canary or phased rollout limits exposure while evidence accumulates. Rollback must be practical, not theoretical. In this case: Context growth, truncation, and session-state behavior over time.
- **D:** Incorrect for this question. Quotas and scaling limits can become the real bottleneck. Plan for bursts and graceful degradation. In this case: Context growth, truncation, and session-state behavior over time.

### Question 83 — C

Answer: Inspect spans across agent, model, and tool calls. Trajectory traces showing the actual calls and arguments. Traces localize latency and failures in multi-step workflows. They are essential for debugging non-deterministic behavior. Local study-map skill 4.5 (Troubleshooting Agent Failures), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. In this case: Trajectory traces showing the actual calls and arguments.
- **B:** Incorrect for this question. Models, sources, and user behavior change. Monitoring detects when evaluation assumptions no longer hold. In this case: Trajectory traces showing the actual calls and arguments.
- **C:** Correct. Traces localize latency and failures in multi-step workflows. They are essential for debugging non-deterministic behavior. In this case: Trajectory traces showing the actual calls and arguments.
- **D:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Trajectory traces showing the actual calls and arguments.

### Question 84 — C

Answer: Use Cloud Logging, Cloud Trace, and Cloud Monitoring. Logging, tracing, and monitoring across agent, model, and tool components. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. Local study-map skill 4.6 (Monitoring and Optimization), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Logging, tracing, and monitoring across agent, model, and tool components.
- **B:** Incorrect for this question. Traces localize latency and failures in multi-step workflows. They are essential for debugging non-deterministic behavior. In this case: Logging, tracing, and monitoring across agent, model, and tool components.
- **C:** Correct. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. In this case: Logging, tracing, and monitoring across agent, model, and tool components.
- **D:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Logging, tracing, and monitoring across agent, model, and tool components.

### Question 85 — B

Answer: Track token and tool cost per completed task. Token, tool, retry, and review cost attributed to accepted outcomes. Cost attribution supports optimization and budgeting. Per-task cost reveals expensive failure paths. Local study-map skill 4.6 (Monitoring and Optimization), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Token, tool, retry, and review cost attributed to accepted outcomes.
- **B:** Correct. Cost attribution supports optimization and budgeting. Per-task cost reveals expensive failure paths. In this case: Token, tool, retry, and review cost attributed to accepted outcomes.
- **C:** Incorrect for this question. Quotas and scaling limits can become the real bottleneck. Plan for bursts and graceful degradation. In this case: Token, tool, retry, and review cost attributed to accepted outcomes.
- **D:** Incorrect for this question. A canary or phased rollout limits exposure while evidence accumulates. Rollback must be practical, not theoretical. In this case: Token, tool, retry, and review cost attributed to accepted outcomes.

### Question 86 — C

Answer: Provision capacity for peak concurrency and quotas. The dominant latency contributors identified through traces. Quotas and scaling limits can become the real bottleneck. Plan for bursts and graceful degradation. Local study-map skill 4.6 (Monitoring and Optimization), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. A canary or phased rollout limits exposure while evidence accumulates. Rollback must be practical, not theoretical. In this case: The dominant latency contributors identified through traces.
- **B:** Incorrect for this question. User experience depends on retrieval, tool calls, model turns, and approval. Optimize the whole path, not only generation time. In this case: The dominant latency contributors identified through traces.
- **C:** Correct. Quotas and scaling limits can become the real bottleneck. Plan for bursts and graceful degradation. In this case: The dominant latency contributors identified through traces.
- **D:** Incorrect for this question. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. In this case: The dominant latency contributors identified through traces.

### Question 87 — A

Answer: Use staged rollout with measurable rollback criteria. Compare against pre-agreed quality and cost thresholds before expanding. A canary or phased rollout limits exposure while evidence accumulates. Rollback must be practical, not theoretical. Local study-map skill 4.6 (Monitoring and Optimization), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Correct. A canary or phased rollout limits exposure while evidence accumulates. Rollback must be practical, not theoretical. In this case: Compare against pre-agreed quality and cost thresholds before expanding.
- **B:** Incorrect for this question. Prompts, models, tools, and data can all change behavior. Regression testing catches unintended effects. In this case: Compare against pre-agreed quality and cost thresholds before expanding.
- **C:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Compare against pre-agreed quality and cost thresholds before expanding.
- **D:** Incorrect for this question. Controlled comparison supports evidence-based rollout. Changing several variables at once confuses attribution. In this case: Compare against pre-agreed quality and cost thresholds before expanding.

### Question 88 — A

Answer: Record agent actions and tool calls in audit logs. Attributable logs linking the action, identity, and approval record. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. Local study-map skill 4.6 (Monitoring and Optimization), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Correct. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Attributable logs linking the action, identity, and approval record.
- **B:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Attributable logs linking the action, identity, and approval record.
- **C:** Incorrect for this question. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. In this case: Attributable logs linking the action, identity, and approval record.
- **D:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Attributable logs linking the action, identity, and approval record.

### Question 89 — D

Answer: Provision capacity for peak concurrency and quotas. Quota, scaling configuration, and degradation behavior. Quotas and scaling limits can become the real bottleneck. Plan for bursts and graceful degradation. Local study-map skill 4.6 (Monitoring and Optimization), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. GKE offers flexibility for complex workloads at higher operational cost. Use it when requirements justify that control. In this case: Quota, scaling configuration, and degradation behavior.
- **B:** Incorrect for this question. Cloud Run suits stateless or externally-stateful container services with managed scaling. Design sessions and long tasks accordingly. In this case: Quota, scaling configuration, and degradation behavior.
- **C:** Incorrect for this question. Agent Runtime provides managed hosting and agent platform integration. It is not automatically the best fit for every workload. In this case: Quota, scaling configuration, and degradation behavior.
- **D:** Correct. Quotas and scaling limits can become the real bottleneck. Plan for bursts and graceful degradation. In this case: Quota, scaling configuration, and degradation behavior.

### Question 90 — B

Answer: Inspect spans across agent, model, and tool calls. Error rates grouped by tool from traces and logs. Traces localize latency and failures in multi-step workflows. They are essential for debugging non-deterministic behavior. Local study-map skill 4.6 (Monitoring and Optimization), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Models, sources, and user behavior change. Monitoring detects when evaluation assumptions no longer hold. In this case: Error rates grouped by tool from traces and logs.
- **B:** Correct. Traces localize latency and failures in multi-step workflows. They are essential for debugging non-deterministic behavior. In this case: Error rates grouped by tool from traces and logs.
- **C:** Incorrect for this question. Cost attribution supports optimization and budgeting. Per-task cost reveals expensive failure paths. In this case: Error rates grouped by tool from traces and logs.
- **D:** Incorrect for this question. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. In this case: Error rates grouped by tool from traces and logs.

### Question 91 — D

Answer: Use staged rollout with measurable rollback criteria. Continue monitoring against thresholds and decide using pre-agreed criteria. A canary or phased rollout limits exposure while evidence accumulates. Rollback must be practical, not theoretical. Local study-map skill 4.6 (Monitoring and Optimization), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. In this case: Continue monitoring against thresholds and decide using pre-agreed criteria.
- **B:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Continue monitoring against thresholds and decide using pre-agreed criteria.
- **C:** Incorrect for this question. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. In this case: Continue monitoring against thresholds and decide using pre-agreed criteria.
- **D:** Correct. A canary or phased rollout limits exposure while evidence accumulates. Rollback must be practical, not theoretical. In this case: Continue monitoring against thresholds and decide using pre-agreed criteria.

### Question 92 — D

Answer: Track token and tool cost per completed task. Whether the quality gain justifies cost and latency under the use case. Cost attribution supports optimization and budgeting. Per-task cost reveals expensive failure paths. Local study-map skill 4.6 (Monitoring and Optimization), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Quotas and scaling limits can become the real bottleneck. Plan for bursts and graceful degradation. In this case: Whether the quality gain justifies cost and latency under the use case.
- **B:** Incorrect for this question. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. In this case: Whether the quality gain justifies cost and latency under the use case.
- **C:** Incorrect for this question. User experience depends on retrieval, tool calls, model turns, and approval. Optimize the whole path, not only generation time. In this case: Whether the quality gain justifies cost and latency under the use case.
- **D:** Correct. Cost attribution supports optimization and budgeting. Per-task cost reveals expensive failure paths. In this case: Whether the quality gain justifies cost and latency under the use case.

### Question 93 — B

Answer: Govern agent traffic through Agent Gateway. Gateway-level observation and policy enforcement make agent traffic visible and controllable centrally. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. Local study-map skill 4.6 (Monitoring and Optimization), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Gateway-level observation and policy enforcement make agent traffic visible and controllable centrally.
- **B:** Correct. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Gateway-level observation and policy enforcement make agent traffic visible and controllable centrally.
- **C:** Incorrect for this question. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. In this case: Gateway-level observation and policy enforcement make agent traffic visible and controllable centrally.
- **D:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Gateway-level observation and policy enforcement make agent traffic visible and controllable centrally.

### Question 94 — B

Answer: Detect changes in inputs, data, or performance over time. Input distribution and quality metrics with rolling baselines. Models, sources, and user behavior change. Monitoring detects when evaluation assumptions no longer hold. Local study-map skill 4.6 (Monitoring and Optimization), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Production traffic reveals distribution and failure patterns that offline sets miss. Sampling and privacy must be designed. In this case: Input distribution and quality metrics with rolling baselines.
- **B:** Correct. Models, sources, and user behavior change. Monitoring detects when evaluation assumptions no longer hold. In this case: Input distribution and quality metrics with rolling baselines.
- **C:** Incorrect for this question. Prompts, models, tools, and data can all change behavior. Regression testing catches unintended effects. In this case: Input distribution and quality metrics with rolling baselines.
- **D:** Incorrect for this question. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. In this case: Input distribution and quality metrics with rolling baselines.

### Question 95 — A

Answer: Use human review for unresolved or high-impact judgment. Offline and online metrics, segment results, risks, and rollback readiness. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. Local study-map skill 4.6 (Monitoring and Optimization), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Correct. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. In this case: Offline and online metrics, segment results, risks, and rollback readiness.
- **B:** Incorrect for this question. A canary or phased rollout limits exposure while evidence accumulates. Rollback must be practical, not theoretical. In this case: Offline and online metrics, segment results, risks, and rollback readiness.
- **C:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Offline and online metrics, segment results, risks, and rollback readiness.
- **D:** Incorrect for this question. Autoraters can score nuanced qualities at scale. They require calibration against human judgments and periodic review. In this case: Offline and online metrics, segment results, risks, and rollback readiness.

### Question 96 — C

Answer: Provision capacity for peak concurrency and quotas. Minimum instances and warm capacity against cost. Quotas and scaling limits can become the real bottleneck. Plan for bursts and graceful degradation. Local study-map skill 4.6 (Monitoring and Optimization), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Cost attribution supports optimization and budgeting. Per-task cost reveals expensive failure paths. In this case: Minimum instances and warm capacity against cost.
- **B:** Incorrect for this question. Cloud Run suits stateless or externally-stateful container services with managed scaling. Design sessions and long tasks accordingly. In this case: Minimum instances and warm capacity against cost.
- **C:** Correct. Quotas and scaling limits can become the real bottleneck. Plan for bursts and graceful degradation. In this case: Minimum instances and warm capacity against cost.
- **D:** Incorrect for this question. Stateless services scale and recover more predictably. External state introduces its own availability and security requirements. In this case: Minimum instances and warm capacity against cost.

### Question 97 — D

Answer: Record agent actions and tool calls in audit logs. Block or alert on unapproved tool use and investigate the configuration. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. Local study-map skill 4.6 (Monitoring and Optimization), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. A registry supports discovery and governance of agents and tools. Registration should reflect approved ownership and metadata. In this case: Block or alert on unapproved tool use and investigate the configuration.
- **B:** Incorrect for this question. A gateway can apply policy, observe traffic, and track agent interactions. It does not make an authorized but malicious action benign. In this case: Block or alert on unapproved tool use and investigate the configuration.
- **C:** Incorrect for this question. Policies should translate into IAM, gateway, guardrail, and approval mechanisms. Prompt text alone is not enforcement. In this case: Block or alert on unapproved tool use and investigate the configuration.
- **D:** Correct. Audit evidence supports investigation and accountability. Logging must protect sensitive content and be retained appropriately. In this case: Block or alert on unapproved tool use and investigate the configuration.

### Question 98 — D

Answer: Inspect spans across agent, model, and tool calls. Localize the pattern through traces and retrieval evidence, then add targeted tests. Traces localize latency and failures in multi-step workflows. They are essential for debugging non-deterministic behavior. Local study-map skill 4.6 (Monitoring and Optimization), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. Models, sources, and user behavior change. Monitoring detects when evaluation assumptions no longer hold. In this case: Localize the pattern through traces and retrieval evidence, then add targeted tests.
- **B:** Incorrect for this question. Observability reveals latency, errors, and behavior across components. Logs must avoid unnecessary sensitive content. In this case: Localize the pattern through traces and retrieval evidence, then add targeted tests.
- **C:** Incorrect for this question. Some quality and safety questions cannot be fully automated. Review should be targeted and accountable. In this case: Localize the pattern through traces and retrieval evidence, then add targeted tests.
- **D:** Correct. Traces localize latency and failures in multi-step workflows. They are essential for debugging non-deterministic behavior. In this case: Localize the pattern through traces and retrieval evidence, then add targeted tests.

### Question 99 — A

Answer: Use staged rollout with measurable rollback criteria. Broader representative evidence and continued monitoring for delayed failures. A canary or phased rollout limits exposure while evidence accumulates. Rollback must be practical, not theoretical. Local study-map skill 4.6 (Monitoring and Optimization), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Correct. A canary or phased rollout limits exposure while evidence accumulates. Rollback must be practical, not theoretical. In this case: Broader representative evidence and continued monitoring for delayed failures.
- **B:** Incorrect for this question. Controlled comparison supports evidence-based rollout. Changing several variables at once confuses attribution. In this case: Broader representative evidence and continued monitoring for delayed failures.
- **C:** Incorrect for this question. Thresholds turn metrics into decisions and prevent post-hoc rationalization. They should reflect business risk. In this case: Broader representative evidence and continued monitoring for delayed failures.
- **D:** Incorrect for this question. Prompts, models, tools, and data can all change behavior. Regression testing catches unintended effects. In this case: Broader representative evidence and continued monitoring for delayed failures.

### Question 100 — D

Answer: Track token and tool cost per completed task. That safety and quality thresholds still hold under representative evaluation. Cost attribution supports optimization and budgeting. Per-task cost reveals expensive failure paths. Local study-map skill 4.6 (Monitoring and Optimization), mapped to the official guide: Google Cloud Professional Agentic Architect Certification Exam Guide (English) Primary technical reference: Official Vertex AI agent platform documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview

- **A:** Incorrect for this question. A canary or phased rollout limits exposure while evidence accumulates. Rollback must be practical, not theoretical. In this case: That safety and quality thresholds still hold under representative evaluation.
- **B:** Incorrect for this question. Quotas and scaling limits can become the real bottleneck. Plan for bursts and graceful degradation. In this case: That safety and quality thresholds still hold under representative evaluation.
- **C:** Incorrect for this question. User experience depends on retrieval, tool calls, model turns, and approval. Optimize the whole path, not only generation time. In this case: That safety and quality thresholds still hold under representative evaluation.
- **D:** Correct. Cost attribution supports optimization and budgeting. Per-task cost reveals expensive failure paths. In this case: That safety and quality thresholds still hold under representative evaluation.
