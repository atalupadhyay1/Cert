# AWS Certified Generative AI Developer - Professional (AIP-C01) — Full-Length Mock Exam 6

Generative AI Developer · 75 questions · 180 minutes · scaled passing score 750 of 1000

Blueprint-weighted mock exam. Item mix: 60 multiple-choice and 15 multiple-response items (the selection count is stated in each multi-response stem). The published exam has 75 questions in 180 minutes, of which 65 are scored and 10 are unscored, and AWS does not identify the unscored items. AWS publishes no split between multiple-choice and multiple-response items, so the 15-item multi-response block is an authoring choice. At 75 items in 180 minutes this set matches the published pacing at about 144 seconds per item, including the same unscored proportion. The published format has no case-study component, so no case-study item appears here. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied AWS exam items.

## Questions

---

## Domain 1 — Foundation Model Integration, Data Management, and Compliance (31%) — Model integration, data pipelines, vector stores, retrieval, and prompts

### 1. Nine engineering teams will consume one internal assistant, and each team keeps trying to keep its own credentials and wording. Which two shared components remove that duplication? Select two.

- A. Hardcode one model identifier in the application source
- B. Version the prompt in Amazon Bedrock Prompt Management
- C. Keep the prompt as a string constant in the application code
- D. Let each application call the model API directly
- E. Put one internal GenAI gateway in front of every model call

### 2. A platform team must justify its model choice and its running cost to an engineering director before build. Which two artefacts make that case? Select two.

- A. Compare quality per thousand tokens across candidates
- B. Compare the candidates with an Amazon Bedrock model evaluation job
- C. Run a full fine-tune of every model weight
- D. Use one frontier model for every request
- E. Keep a GPU endpoint running for occasional requests

### 3. Before building a code-explanation assistant, the team must know whether engineers trust the output. What should the spike produce?

- A. Compare the candidates with an Amazon Bedrock model evaluation job
- B. Use one frontier model for every request
- C. Report ROUGE and BLEU against the reference answers
- D. Have reviewers score a sample against a written rubric

### 4. Two models are shortlisted for reviewing pull requests, and five hundred merged reviews carry maintainer verdicts. How should the choice be made?

- A. Use one frontier model for every request
- B. Run a full fine-tune of every model weight
- C. Compare the candidates with an Amazon Bedrock model evaluation job
- D. Fine-tune with low-rank adaptation adapters

### 5. An on-call helper answers short runbook lookups and must reply inside a chat timeout. Which model choice fits?

- A. Right-size the model to the task difficulty
- B. Route the call through Amazon Bedrock cross-Region inference
- C. Use one frontier model for every request
- D. Run a full fine-tune of every model weight

### 6. A platform team wants a different model for one internal tool next sprint without shipping a release. What allows that?

- A. Hardcode one model identifier in the application source
- B. Put the model identifier in AWS AppConfig and switch it without a deploy
- C. Let each application call the model API directly
- D. Keep the prompt as a string constant in the application code

### 7. A release-day traffic spike throttles the assistant in the home Region while another Region is idle. What absorbs it?

- A. Route the call through Amazon Bedrock cross-Region inference
- B. Retry the failed call until it succeeds
- C. Store the model API key in an environment variable
- D. Keep a GPU endpoint running for occasional requests

### 8. A provider outage lands during an incident, and engineers would rather have terse answers than none. What design meets that?

- A. Retry the failed call until it succeeds
- B. Fall back to a second model when the first is unavailable
- C. Use one frontier model for every request
- D. Raise the temperature for creative variants

### 9. A code assistant started suggesting a deprecated API after the provider silently moved its default model. What prevents a repeat?

- A. Pin the model version instead of tracking the latest alias
- B. Let each application call the model API directly
- C. Keep the prompt as a string constant in the application code
- D. Run a full fine-tune of every model weight

### 10. Documentation syncs from six repositories and sometimes loses a file path or an owner field. What should reject the bad sync?

- A. Validate response structure and log the failures
- B. Set an explicit CloudWatch Logs retention period
- C. Enforce freshness and completeness rules with AWS Glue Data Quality
- D. Scan the data store with Amazon Macie

### 11. Runbooks mix wiki markup, shell blocks, and free text, and retrieval quality suffers. What should run before embedding?

- A. Format the turns as an alternating conversation structure
- B. Concatenate all fields into one unlabelled text block
- C. Raise the temperature for creative variants
- D. Normalise the text with a model call before indexing

### 12. Support engineers attach screenshots of dashboards to tickets and want their text searchable. What extracts it?

- A. Embed text and images with one multimodal model
- B. Transcribe the call recordings with Amazon Transcribe
- C. Extract the text from scanned pages with Amazon Textract
- D. Extract entities with Amazon Comprehend before indexing

### 13. An incident assistant must keep the timeline, the reporter, and the assistant's own replies in order. How should the request be built?

- A. Cap the response length in the request
- B. Raise the temperature for creative variants
- C. Format the turns as an alternating conversation structure
- D. Concatenate all fields into one unlabelled text block

### 14. An SDK call keeps returning a schema error even though the prompt string looks valid. Which part of the payload is at fault?

- A. Keep the prompt as a string constant in the application code
- B. Concatenate all fields into one unlabelled text block
- C. Format the turns as an alternating conversation structure
- D. Send the request as the JSON body the model expects

### 15. The runbook corpus already lives in Amazon S3 under review, and the index must never become the only copy. Where should the source sit?

- A. Keep embeddings and metadata in Amazon DynamoDB
- B. Store the knowledge graph in Amazon Neptune
- C. Keep the source documents in Amazon DocumentDB
- D. Keep the source corpus in Amazon S3 and index references into it

### 16. One assistant serves eight engineering teams whose documents are confidential to each team. What keeps answers inside a team boundary?

- A. Filter the search by document metadata before the similarity ranking
- B. Raise the number of retrieved passages per query
- C. Drop passages below a relevance score threshold
- D. Partition the corpus into per-tenant namespaces

### 17. The platform is moving to a newer embedding model with a different dimension. What must happen to the existing index?

- A. Cache every answer with no expiry
- B. Re-embed the corpus when the embedding model changes
- C. Keep old vectors and embed new documents with the newer model
- D. Rebuild the index on a schedule and accept staleness between runs

### 18. A team must document a stable vector dimension for an index that will run for years. What supplies that?

- A. Generate embeddings with an Amazon Titan text embedding model
- B. Embed text and images with one multimodal model
- C. Fine-tune the embedding model on labelled query and passage pairs
- D. Keep old vectors and embed new documents with the newer model

### 19. Engineers search for exact error identifiers and for descriptions of behaviour, and the best match often ranks late. Which two changes fix both? Select two.

- A. Increase the chunk size so every answer fits in one chunk
- B. Rerank the retrieved passages with an Amazon Bedrock reranker
- C. Keep old vectors and embed new documents with the newer model
- D. Combine keyword and vector retrieval and merge the ranked lists
- E. Raise the number of retrieved passages per query

### 20. Answers keep citing loosely related pages that add noise to the prompt. What trims the shortlist?

- A. Expand the user query into related terms before retrieval
- B. Drop passages below a relevance score threshold
- C. Split where the embedding similarity between sentences drops
- D. Raise the number of retrieved passages per query

### 21. An engineer asks one question covering both a deploy failure and a rollback policy. What should happen before retrieval?

- A. Break a multi-part question into separate retrievals
- B. Expand the user query into related terms before retrieval
- C. Raise the number of retrieved passages per query
- D. Cache every answer with no expiry

### 22. A bot must return a severity, an owner, and a next action in fixed fields for the incident tool. What guarantees that shape?

- A. Cap the response length in the request
- B. Concatenate all fields into one unlabelled text block
- C. Raise the temperature for creative variants
- D. Constrain the response with a JSON schema

### 23. Two engineers ask the same configuration question and receive different commands. What setting reduces that variance?

- A. Add worked examples of the expected answer shape
- B. Lower the temperature for factual answers
- C. Cap the response length in the request
- D. Raise the temperature for creative variants

---

## Domain 2 — Implementation and Integration (26%) — Agents, deployment, enterprise integration, APIs, and developer tooling

### 24. An incident agent needs managed session memory and a runtime for its reasoning loop. What provides both?

- A. Keep memory only in the prompt of the current turn
- B. Let each application call the model API directly
- C. Run the agent on Amazon Bedrock AgentCore
- D. Implement the tool as an AWS Lambda function

### 25. An incident channel runs for hours and every turn is resent to the model. What keeps the prompt affordable?

- A. Increase the chunk size so every answer fits in one chunk
- B. Concatenate all fields into one unlabelled text block
- C. Summarise the conversation before adding more turns
- D. Keep memory only in the prompt of the current turn

### 26. Two models review the same pull request and a reviewer wants one combined verdict. What pattern fits?

- A. Keep the prompt as a string constant in the application code
- B. Aggregate answers from several models with custom logic
- C. Give one agent every tool in the platform
- D. Keep a GPU endpoint running for occasional requests

### 27. An agent can roll back a production deployment, and its reasoning loop must not run away. Which two controls are required? Select two.

- A. Give one agent every tool in the platform
- B. Retry the failed call until it succeeds
- C. Require human approval before the agent performs the action
- D. Set an explicit step and budget limit on the agent loop
- E. Raise the temperature for creative variants

### 28. An agent passes a commit hash in the wrong form and the build tool fails after a long round trip. Where should that be caught?

- A. Set an explicit CloudWatch Logs retention period
- B. Validate tool arguments against a schema before calling
- C. Cache every answer with no expiry
- D. Retry the failed call until it succeeds

### 29. The build-status tool hangs for minutes and freezes the agent turn. What contains that?

- A. Bound each tool call with a timeout and a fallback
- B. Retry the failed call until it succeeds
- C. Set an explicit CloudWatch Logs retention period
- D. Keep a GPU endpoint running for occasional requests

### 30. A code review assistant runs at a steady load all day and the team is tired of throttle retries. What should it buy?

- A. Keep a GPU endpoint running for occasional requests
- B. Call the model on demand through Amazon Bedrock
- C. Use one frontier model for every request
- D. Buy Amazon Bedrock provisioned throughput for the model

### 31. Review comments are needed instantly, while nightly documentation summaries can wait until morning. Which two capacity patterns fit both? Select two.

- A. Call the model on demand through Amazon Bedrock
- B. Buy Amazon Bedrock provisioned throughput for the model
- C. Run the work as an Amazon Bedrock batch inference job
- D. Return the whole answer from one synchronous call
- E. Retry the failed call until it succeeds

### 32. A merged pull request must trigger documentation, changelog, and review-summary jobs, with new consumers arriving each quarter. What connects them?

- A. Buffer the work in an Amazon SQS queue
- B. Fan the result out with Amazon SNS
- C. Move SaaS records in with Amazon AppFlow
- D. Route domain events through Amazon EventBridge

### 33. A backlog of two thousand repositories must be documented without losing work when a call fails. What should sit in front of the model?

- A. Buffer the work in an Amazon SQS queue
- B. Fan the result out with Amazon SNS
- C. Front the model with Amazon API Gateway
- D. Return the whole answer from one synchronous call

### 34. A platform service needs temporary credentials for one bucket prefix and one model, with no secret on disk. What should it assume?

- A. Store the model API key in an environment variable
- B. Give the task an IAM role scoped to the resources it uses
- C. Receive partner files over AWS Transfer Family
- D. Make the document bucket publicly readable

### 35. Every squad calls the model API with its own key and nobody can revoke access for a leaver quickly. What should the platform provide?

- A. Let each application call the model API directly
- B. Store the model API key in an environment variable
- C. Put one internal GenAI gateway in front of every model call
- D. Hardcode one model identifier in the application source

### 36. A prompt change must pass the evaluation suite before any internal user sees it. Which two services carry that path? Select two.

- A. Keep the prompt as a string constant in the application code
- B. Let each application call the model API directly
- C. Run the evaluation suite in AWS CodeBuild
- D. Release the assistant through AWS CodePipeline
- E. Store the model API key in an environment variable

### 37. A chat panel must show generated text as it arrives over ordinary HTTP. What fits?

- A. Return the whole answer from one synchronous call
- B. Queue the prompt and return a job identifier for polling
- C. Stream tokens as server-sent events
- D. Keep a GPU endpoint running for occasional requests

### 38. A CLI tool retries instantly when the service asks it to slow down, which multiplies the load. What retry strategy should it use?

- A. Keep a GPU endpoint running for occasional requests
- B. Open a circuit breaker after repeated dependency failures
- C. Retry the failed call until it succeeds
- D. Retry throttled calls with exponential backoff and jitter

### 39. The build service has failed every call for twenty minutes and requests keep queueing behind it. What should open?

- A. Open a circuit breaker after repeated dependency failures
- B. Retry the failed call until it succeeds
- C. Return the whole answer from one synchronous call
- D. Retry throttled calls with exponential backoff and jitter

### 40. A developer portal needs one query for services, incidents, and assistant answers with live updates. What API style fits?

- A. Run the request shaping logic at the edge with Lambda@Edge
- B. Expose the assistant through AWS AppSync
- C. Front the model with Amazon API Gateway
- D. Stream tokens as server-sent events

### 41. Requests from regions with strict data rules must be trimmed and redacted before they leave the edge. What runs that logic?

- A. Serve repeatable responses from Amazon CloudFront
- B. Front the model with Amazon API Gateway
- C. Let each application call the model API directly
- D. Run the request shaping logic at the edge with Lambda@Edge

### 42. Engineers copy the same SDK boilerplate into every internal tool. What reduces that effort?

- A. Release the assistant through AWS CodePipeline
- B. Keep the prompt as a string constant in the application code
- C. Run the evaluation suite in AWS CodeBuild
- D. Generate and explain the integration code with Amazon Q Developer

### 43. One squad reports that answers about its service became wrong yesterday, and the prompts are needed. What finds them?

- A. Query the prompt and response logs with CloudWatch Logs Insights
- B. Set an explicit CloudWatch Logs retention period
- C. Trace the request across services with AWS X-Ray
- D. Record control-plane activity in AWS CloudTrail

---

## Domain 3 — AI Safety, Security, and Governance (20%) — Safety controls, privacy, governance, and responsible AI

### 44. A code assistant reads pasted stack traces and answers them, and neither direction should carry abuse or credentials. What covers both?

- A. Cap the response length in the request
- B. Set an explicit CloudWatch Logs retention period
- C. Lower the temperature for factual answers
- D. Apply Amazon Bedrock Guardrails content filters

### 45. The assistant must refuse to discuss one unreleased product and must never echo a customer identifier from a log paste. Which two guardrail policies cover that? Select two.

- A. Cache every answer with no expiry
- B. Enable sensitive-information filters in Amazon Bedrock Guardrails
- C. Define denied topics in Amazon Bedrock Guardrails
- D. Retry the failed call until it succeeds
- E. Cap the response length in the request

### 46. Engineers will only trust a runbook answer they can check against the current page. What should each answer include?

- A. Cap the response length in the request
- B. Escalate low-confidence or high-impact answers to a person
- C. Require the answer to cite the retrieved passage
- D. Return a confidence score with each answer

### 47. An answer invents a command flag that appears nowhere in the retrieved runbook. Which control catches that?

- A. Enable the contextual grounding check in Guardrails
- B. Lower the temperature for factual answers
- C. Constrain the response with a JSON schema
- D. Score answers by embedding similarity to the reference

### 48. A vendor pastes text instructing the assistant to reveal the internal deployment token. What detects that attempt?

- A. Lower the temperature for factual answers
- B. Screen inputs for instruction override and jailbreak patterns
- C. Cap the response length in the request
- D. Retry the failed call until it succeeds

### 49. Security wants a standing hostile-prompt test on every build of the internal assistant. What should be added?

- A. Run the release against a curated golden question set
- B. Cache every answer with no expiry
- C. Have reviewers score a sample against a written rubric
- D. Run an adversarial prompt suite before each release

### 50. Ticket text is retained for years, and customer identifiers must not survive in the stored copy. What should be applied at write time?

- A. Scan the data store with Amazon Macie
- B. Mask direct identifiers before the record is stored
- C. Mask personal data before the prompt is built
- D. Enable sensitive-information filters in Amazon Bedrock Guardrails

### 51. Before old tickets are indexed, the team must find identifiers in storage and strip them from the text. Which two services do that work? Select two.

- A. Set an explicit CloudWatch Logs retention period
- B. Scan the data store with Amazon Macie
- C. Store the model API key in an environment variable
- D. Detect personal data with Amazon Comprehend
- E. Apply Amazon Bedrock Guardrails content filters

### 52. Platform policy forbids assistant traffic leaving the private network path. What provides that route?

- A. Serve repeatable responses from Amazon CloudFront
- B. Store the model API key in an environment variable
- C. Make the document bucket publicly readable
- D. Call the model through an interface VPC endpoint

### 53. The assistant's compute must have no public address while still calling regional AWS APIs. What placement satisfies that?

- A. Serve repeatable responses from Amazon CloudFront
- B. Let each application call the model API directly
- C. Deploy the workload in private subnets
- D. Make the document bucket publicly readable

### 54. An audit asks who widened a guardrail and when the model identifier changed. What answers both?

- A. Set an explicit CloudWatch Logs retention period
- B. Turn on Amazon Bedrock model invocation logging
- C. Record control-plane activity in AWS CloudTrail
- D. Build the operations view in Amazon Managed Grafana

### 55. A disputed answer must be rebuilt with the documentation version and the exact request behind it. Which two records allow that? Select two.

- A. Record data lineage in the AWS Glue Data Catalog
- B. Turn on Amazon Bedrock model invocation logging
- C. Cache every answer with no expiry
- D. Store the model API key in an environment variable
- E. Lower the temperature for factual answers

### 56. Reviewers want the intended use and known limits of the code assistant before it ships. What documents that?

- A. Publish a model card with the model version
- B. Constrain the response with a JSON schema
- C. Compare the candidates with an Amazon Bedrock model evaluation job
- D. Set an explicit CloudWatch Logs retention period

### 57. The interface should mark an uncertain answer instead of presenting a guess as fact. What supports that marking?

- A. Return a confidence score with each answer
- B. Raise the temperature for creative variants
- C. Cap the response length in the request
- D. Cache every answer with no expiry

### 58. Token counts per squad and per model must explain a sudden increase in the monthly bill. Which logging feature records the request, the response, and the usage figures?

- A. Alert when fairness metrics move beyond a band
- B. Detect spend spikes with AWS Cost Anomaly Detection
- C. Alarm on p95 latency and error rate
- D. Report fairness metrics per user segment

---

## Domain 4 — Operational Efficiency and Optimization for GenAI Applications (12%) — Token cost, latency, throughput, and observability

### 59. An incident channel keeps every message and the resend charge now dominates the bill. What should be removed from the prompt?

- A. Raise the number of retrieved passages per query
- B. Raise the temperature for creative variants
- C. Increase the chunk size so every answer fits in one chunk
- D. Prune older turns from the context window

### 60. Some answers run to several screens when a three-line summary would do. What bounds spend per call?

- A. Concatenate all fields into one unlabelled text block
- B. Cap the response length in the request
- C. Raise the number of retrieved passages per query
- D. Increase the chunk size so every answer fits in one chunk

### 61. Every request resends the same long coding standard before a short question. What reduces the charge for that prefix?

- A. Cache answers by embedding similarity to earlier questions
- B. Cache the response under a hash of the normalised request
- C. Cache the stable prompt prefix with prompt caching
- D. Cache every answer with no expiry

### 62. The assistant serves a million questions a month, most of them repeats of a small set. Which two levers cut spend most? Select two.

- A. Cache the response under a hash of the normalised request
- B. Send routine prompts to a small model and hard prompts to a large one
- C. Run a full fine-tune of every model weight
- D. Use one frontier model for every request
- E. Cache every answer with no expiry

### 63. A review summariser makes four independent model calls per pull request and the reviewer waits for all of them. What reduces the wait?

- A. Issue independent model calls in parallel
- B. Use one frontier model for every request
- C. Run the work as an Amazon Bedrock batch inference job
- D. Retry the failed call until it succeeds

### 64. A chat helper must feel instant, and its first token currently arrives after four seconds. Which two changes address both? Select two.

- A. Keep a GPU endpoint running for occasional requests
- B. Run the work as an Amazon Bedrock batch inference job
- C. Choose a lower-latency model for the interactive path
- D. Retry the failed call until it succeeds
- E. Stream tokens as they are generated

### 65. Answers shortened sharply after a model swap, and the team needs the exact prompts and responses from that window. Where are they?

- A. Set an explicit CloudWatch Logs retention period
- B. Record control-plane activity in AWS CloudTrail
- C. Turn on Amazon Bedrock model invocation logging
- D. Publish a model card with the model version

### 66. The platform wants spend attributed per squad and an alert when a squad suddenly uses far more tokens. Which two capabilities provide that? Select two.

- A. Publish a model card with the model version
- B. Detect spend spikes with AWS Cost Anomaly Detection
- C. Alarm on p95 latency and error rate
- D. Publish token usage as CloudWatch metrics
- E. Set an explicit CloudWatch Logs retention period

### 67. The platform runs a steady compute baseline all year for embeddings and batch jobs. What discounts that predictable capacity?

- A. Alert when a tenant crosses its monthly token budget
- B. Cover the steady compute with a Savings Plan
- C. Detect spend spikes with AWS Cost Anomaly Detection
- D. Keep a GPU endpoint running for occasional requests

---

## Domain 5 — Testing, Validation, and Troubleshooting (11%) — Evaluation, validation, regression testing, and diagnosis

### 68. A prompt revision should reach a small group of internal users before everyone else. Which pattern describes that?

- A. Report BERTScore for semantic similarity to the reference
- B. Measure whether the needed passage was retrieved at all
- C. Score how directly the answer addresses the question
- D. Report ROUGE and BLEU against the reference answers

### 69. Answers are compared with reference runbooks and must also be checked for claims the source never makes. Which two scores cover both? Select two.

- A. Measure whether the needed passage was retrieved at all
- B. Report ROUGE and BLEU against the reference answers
- C. Report BERTScore for semantic similarity to the reference
- D. Raise the temperature for creative variants
- E. Measure whether each claim is supported by the retrieved context

### 70. A revised prompt should reach a small share of internal users first so a regression is contained. What deployment pattern is that?

- A. Split traffic between two model versions and compare outcomes
- B. Send a small traffic share to the new prompt and watch the metrics
- C. Have reviewers score a sample against a written rubric
- D. Mirror production traffic to the new version and compare offline

### 71. A model refresh must not break the two hundred runbook questions the on-call team trusts. What should the release replay?

- A. Run the release against a curated golden question set
- B. Cache every answer with no expiry
- C. Have reviewers score a sample against a written rubric
- D. Set an explicit CloudWatch Logs retention period

### 72. A release must be blocked automatically when quality drops, and every prompt template needs its own tests. Which two practices deliver that? Select two.

- A. Cache every answer with no expiry
- B. Retry the failed call until it succeeds
- C. Block the release when evaluation drops below the threshold
- D. Raise the temperature for creative variants
- E. Run a prompt regression suite before promoting a version

### 73. The prompt fills with loosely related wiki pages that dilute the answer. Which retrieval score exposes that?

- A. Measure whether the agent called the right tool with the right arguments
- B. Measure whether the retrieved passages were relevant
- C. Measure whether the needed passage was retrieved at all
- D. Report ROUGE and BLEU against the reference answers

### 74. An incident agent calls the wrong service tool and sometimes leaves the investigation unfinished. Which two measurements separate those failures? Select two.

- A. Report BERTScore for semantic similarity to the reference
- B. Report ROUGE and BLEU against the reference answers
- C. Measure whether the agent called the right tool with the right arguments
- D. Measure the share of agent tasks completed end to end
- E. Measure whether the retrieved passages were relevant

### 75. Answers ignore the final instruction whenever a long log is pasted, and no error appears. What should be checked first?

- A. Query the prompt and response logs with CloudWatch Logs Insights
- B. Trim or chunk the request when it exceeds the context window
- C. Log the token count and check for truncated prompts
- D. Cache every answer with no expiry

---

## Answer key and explanations

### Question 1 — B, E

Answers: Put one internal GenAI gateway in front of every model call; Version the prompt in Amazon Bedrock Prompt Management. A gateway owns the credentials and quotas while versioned templates keep the wording consistent everywhere. A gateway centralises credentials, quotas, logging, and model routing for all teams. Prompt Management stores versions and variables so the same template serves every environment. Local study-map skill 1.1 (GenAI Solution Architecture), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. A hardcoded identifier forces a code change and a release to try another model. Why the correct answer wins: A gateway owns the credentials and quotas while versioned templates keep the wording consistent everywhere.
- **B:** Correct. Prompt Management stores versions and variables so the same template serves every environment. In this case: A gateway owns the credentials and quotas while versioned templates keep the wording consistent everywhere.
- **C:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: A gateway owns the credentials and quotas while versioned templates keep the wording consistent everywhere.
- **D:** Incorrect for this question. Direct calls from every app scatter keys, quotas, and logging across teams. Why the correct answer wins: A gateway owns the credentials and quotas while versioned templates keep the wording consistent everywhere.
- **E:** Correct. A gateway centralises credentials, quotas, logging, and model routing for all teams. In this case: A gateway owns the credentials and quotas while versioned templates keep the wording consistent everywhere.

### Question 2 — A, B

Answers: Compare the candidates with an Amazon Bedrock model evaluation job; Compare quality per thousand tokens across candidates. An evaluation job compares candidates on real prompts and quality per thousand tokens prices the recommendation. A Bedrock evaluation job scores candidate models on your prompts and metrics before you choose. Quality per unit of spend separates a cheaper model that is good enough from a false economy. Local study-map skill 1.1 (GenAI Solution Architecture), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Correct. Quality per unit of spend separates a cheaper model that is good enough from a false economy. In this case: An evaluation job compares candidates on real prompts and quality per thousand tokens prices the recommendation.
- **B:** Correct. A Bedrock evaluation job scores candidate models on your prompts and metrics before you choose. In this case: An evaluation job compares candidates on real prompts and quality per thousand tokens prices the recommendation.
- **C:** Incorrect for this question. A full fine-tune changes all weights, which is expensive and gives one model per task. Why the correct answer wins: An evaluation job compares candidates on real prompts and quality per thousand tokens prices the recommendation.
- **D:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: An evaluation job compares candidates on real prompts and quality per thousand tokens prices the recommendation.
- **E:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: An evaluation job compares candidates on real prompts and quality per thousand tokens prices the recommendation.

### Question 3 — D

Answer: Have reviewers score a sample against a written rubric. A rubric with human scores gives a reference the automatic metrics can be checked against. Local study-map skill 1.2 (Proof-of-Concept Validation), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. A Bedrock evaluation job scores candidate models on your prompts and metrics before you choose. Why the correct answer wins: A rubric with human scores gives a reference the automatic metrics can be checked against.
- **B:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: A rubric with human scores gives a reference the automatic metrics can be checked against.
- **C:** Incorrect for this question. Overlap metrics are cheap and reward wording that matches the references. Why the correct answer wins: A rubric with human scores gives a reference the automatic metrics can be checked against.
- **D:** Correct. In this case: A rubric with human scores gives a reference the automatic metrics can be checked against.

### Question 4 — C

Answer: Compare the candidates with an Amazon Bedrock model evaluation job. A Bedrock evaluation job scores every candidate on the same labelled prompts before a choice is made. A Bedrock evaluation job scores candidate models on your prompts and metrics before you choose. Local study-map skill 1.3 (Foundation Model Selection and Benchmarking), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: A Bedrock evaluation job scores every candidate on the same labelled prompts before a choice is made.
- **B:** Incorrect for this question. A full fine-tune changes all weights, which is expensive and gives one model per task. Why the correct answer wins: A Bedrock evaluation job scores every candidate on the same labelled prompts before a choice is made.
- **C:** Correct. A Bedrock evaluation job scores candidate models on your prompts and metrics before you choose. In this case: A Bedrock evaluation job scores every candidate on the same labelled prompts before a choice is made.
- **D:** Incorrect for this question. LoRA trains a small adapter instead of every weight, which cuts cost and keeps the base model reusable. Why the correct answer wins: A Bedrock evaluation job scores every candidate on the same labelled prompts before a choice is made.

### Question 5 — A

Answer: Right-size the model to the task difficulty. A model no larger than the task needs keeps the per-answer price low for a narrow, repetitive question. A model no larger than the task needs is the largest single cost lever. Local study-map skill 1.3 (Foundation Model Selection and Benchmarking), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Correct. A model no larger than the task needs is the largest single cost lever. In this case: A model no larger than the task needs keeps the per-answer price low for a narrow, repetitive question.
- **B:** Incorrect for this question. A cross-Region inference profile spreads traffic across Regions so a local capacity shortage is absorbed. Why the correct answer wins: A model no larger than the task needs keeps the per-answer price low for a narrow, repetitive question.
- **C:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: A model no larger than the task needs keeps the per-answer price low for a narrow, repetitive question.
- **D:** Incorrect for this question. A full fine-tune changes all weights, which is expensive and gives one model per task. Why the correct answer wins: A model no larger than the task needs keeps the per-answer price low for a narrow, repetitive question.

### Question 6 — B

Answer: Put the model identifier in AWS AppConfig and switch it without a deploy. A configuration flag changes the model identifier per request path without shipping new application code. Local study-map skill 1.4 (Model Routing and Provider Abstraction), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. A hardcoded identifier forces a code change and a release to try another model. Why the correct answer wins: A configuration flag changes the model identifier per request path without shipping new application code.
- **B:** Correct. In this case: A configuration flag changes the model identifier per request path without shipping new application code.
- **C:** Incorrect for this question. Direct calls from every app scatter keys, quotas, and logging across teams. Why the correct answer wins: A configuration flag changes the model identifier per request path without shipping new application code.
- **D:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: A configuration flag changes the model identifier per request path without shipping new application code.

### Question 7 — A

Answer: Route the call through Amazon Bedrock cross-Region inference. A cross-Region inference profile spreads traffic so a local capacity shortage does not fail the request. Local study-map skill 1.5 (Resilience and Cross-Region Inference), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Correct. In this case: A cross-Region inference profile spreads traffic so a local capacity shortage does not fail the request.
- **B:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: A cross-Region inference profile spreads traffic so a local capacity shortage does not fail the request.
- **C:** Incorrect for this question. A key in an environment variable leaks through images, logs, and job definitions. Why the correct answer wins: A cross-Region inference profile spreads traffic so a local capacity shortage does not fail the request.
- **D:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: A cross-Region inference profile spreads traffic so a local capacity shortage does not fail the request.

### Question 8 — B

Answer: Fall back to a second model when the first is unavailable. A fallback model keeps the feature answering during a Regional degradation, at a stated quality cost. A fallback keeps the feature available when one model or Region degrades. Local study-map skill 1.5 (Resilience and Cross-Region Inference), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: A fallback model keeps the feature answering during a Regional degradation, at a stated quality cost.
- **B:** Correct. A fallback keeps the feature available when one model or Region degrades. In this case: A fallback model keeps the feature answering during a Regional degradation, at a stated quality cost.
- **C:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: A fallback model keeps the feature answering during a Regional degradation, at a stated quality cost.
- **D:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: A fallback model keeps the feature answering during a Regional degradation, at a stated quality cost.

### Question 9 — A

Answer: Pin the model version instead of tracking the latest alias. Pinning the model version keeps behaviour stable until an upgrade is deliberately evaluated. Local study-map skill 1.6 (Customisation Lifecycle and Rollback), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Correct. In this case: Pinning the model version keeps behaviour stable until an upgrade is deliberately evaluated.
- **B:** Incorrect for this question. Direct calls from every app scatter keys, quotas, and logging across teams. Why the correct answer wins: Pinning the model version keeps behaviour stable until an upgrade is deliberately evaluated.
- **C:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: Pinning the model version keeps behaviour stable until an upgrade is deliberately evaluated.
- **D:** Incorrect for this question. A full fine-tune changes all weights, which is expensive and gives one model per task. Why the correct answer wins: Pinning the model version keeps behaviour stable until an upgrade is deliberately evaluated.

### Question 10 — C

Answer: Enforce freshness and completeness rules with AWS Glue Data Quality. Rule sets score freshness and completeness and stop the batch before anything is embedded. Local study-map skill 1.7 (Data Validation for Model Inputs), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. Structure failures appear in the logs before a downstream parser breaks. Why the correct answer wins: Rule sets score freshness and completeness and stop the batch before anything is embedded.
- **B:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: Rule sets score freshness and completeness and stop the batch before anything is embedded.
- **C:** Correct. In this case: Rule sets score freshness and completeness and stop the batch before anything is embedded.
- **D:** Incorrect for this question. Macie finds sensitive data at rest so the corpus can be cleaned before indexing. Why the correct answer wins: Rule sets score freshness and completeness and stop the batch before anything is embedded.

### Question 11 — D

Answer: Normalise the text with a model call before indexing. A reformatting pass cleans inconsistent headings and units before embedding. Local study-map skill 1.7 (Data Validation for Model Inputs), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. A dialog-shaped request keeps speaker roles and prior turns in the order the model expects. Why the correct answer wins: A reformatting pass cleans inconsistent headings and units before embedding.
- **B:** Incorrect for this question. A single blob loses the field boundaries the model needs to answer precisely. Why the correct answer wins: A reformatting pass cleans inconsistent headings and units before embedding.
- **C:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: A reformatting pass cleans inconsistent headings and units before embedding.
- **D:** Correct. In this case: A reformatting pass cleans inconsistent headings and units before embedding.

### Question 12 — C

Answer: Extract the text from scanned pages with Amazon Textract. OCR returns the text and form fields from each scanned page so it can be indexed as text. Local study-map skill 1.8 (Multimodal Ingestion and Processing), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. A shared embedding space lets an image query match a text description. Why the correct answer wins: OCR returns the text and form fields from each scanned page so it can be indexed as text.
- **B:** Incorrect for this question. Transcribe turns speech into timestamped text that retrieval can search. Why the correct answer wins: OCR returns the text and form fields from each scanned page so it can be indexed as text.
- **C:** Correct. In this case: OCR returns the text and form fields from each scanned page so it can be indexed as text.
- **D:** Incorrect for this question. Entity extraction puts product codes and names in metadata for exact filtering. Why the correct answer wins: OCR returns the text and form fields from each scanned page so it can be indexed as text.

### Question 13 — C

Answer: Format the turns as an alternating conversation structure. A dialog-shaped request keeps speaker roles and prior turns in the order the model expects. Local study-map skill 1.9 (Request Formatting and Enrichment), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. A token cap bounds the cost of a runaway answer and the latency of every call. Why the correct answer wins: A dialog-shaped request keeps speaker roles and prior turns in the order the model expects.
- **B:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: A dialog-shaped request keeps speaker roles and prior turns in the order the model expects.
- **C:** Correct. In this case: A dialog-shaped request keeps speaker roles and prior turns in the order the model expects.
- **D:** Incorrect for this question. A single blob loses the field boundaries the model needs to answer precisely. Why the correct answer wins: A dialog-shaped request keeps speaker roles and prior turns in the order the model expects.

### Question 14 — D

Answer: Send the request as the JSON body the model expects. The model API expects the prompt, parameters, and model identifier in one JSON body. Local study-map skill 1.9 (Request Formatting and Enrichment), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: The model API expects the prompt, parameters, and model identifier in one JSON body.
- **B:** Incorrect for this question. A single blob loses the field boundaries the model needs to answer precisely. Why the correct answer wins: The model API expects the prompt, parameters, and model identifier in one JSON body.
- **C:** Incorrect for this question. A dialog-shaped request keeps speaker roles and prior turns in the order the model expects. Why the correct answer wins: The model API expects the prompt, parameters, and model identifier in one JSON body.
- **D:** Correct. In this case: The model API expects the prompt, parameters, and model identifier in one JSON body.

### Question 15 — D

Answer: Keep the source corpus in Amazon S3 and index references into it. S3 holds the authoritative documents while the index stores only chunks and pointers. Local study-map skill 1.10 (Vector Store Architecture), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. DynamoDB serves key lookups fast and can hold vectors beside their metadata for small corpora. Why the correct answer wins: S3 holds the authoritative documents while the index stores only chunks and pointers.
- **B:** Incorrect for this question. Neptune answers relationship traversals that a similarity search cannot express. Why the correct answer wins: S3 holds the authoritative documents while the index stores only chunks and pointers.
- **C:** Incorrect for this question. DocumentDB stores JSON documents in their original shape for retrieval and display. Why the correct answer wins: S3 holds the authoritative documents while the index stores only chunks and pointers.
- **D:** Correct. In this case: S3 holds the authoritative documents while the index stores only chunks and pointers.

### Question 16 — D

Answer: Partition the corpus into per-tenant namespaces. Separate namespaces keep one tenant from retrieving another tenant content. Local study-map skill 1.11 (Metadata Frameworks and Index Maintenance), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. A metadata filter removes out-of-scope documents so the ranking only sees eligible chunks. Why the correct answer wins: Separate namespaces keep one tenant from retrieving another tenant content.
- **B:** Incorrect for this question. More passages raise recall and also lengthen the prompt and the cost per call. Why the correct answer wins: Separate namespaces keep one tenant from retrieving another tenant content.
- **C:** Incorrect for this question. A threshold keeps marginal passages out of the prompt that would only add noise. Why the correct answer wins: Separate namespaces keep one tenant from retrieving another tenant content.
- **D:** Correct. In this case: Separate namespaces keep one tenant from retrieving another tenant content.

### Question 17 — B

Answer: Re-embed the corpus when the embedding model changes. Vectors from two different models are not comparable, so the whole index must be rebuilt. Local study-map skill 1.11 (Metadata Frameworks and Index Maintenance), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: Vectors from two different models are not comparable, so the whole index must be rebuilt.
- **B:** Correct. In this case: Vectors from two different models are not comparable, so the whole index must be rebuilt.
- **C:** Incorrect for this question. Mixing vector spaces silently breaks similarity, because distances no longer mean the same thing. Why the correct answer wins: Vectors from two different models are not comparable, so the whole index must be rebuilt.
- **D:** Incorrect for this question. Scheduled rebuilds are simple and leave a window in which answers lag the source. Why the correct answer wins: Vectors from two different models are not comparable, so the whole index must be rebuilt.

### Question 18 — A

Answer: Generate embeddings with an Amazon Titan text embedding model. A Titan embedding model gives a documented dimension and a stable vector space. Local study-map skill 1.12 (Chunking and Embedding Strategy), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Correct. In this case: A Titan embedding model gives a documented dimension and a stable vector space.
- **B:** Incorrect for this question. A shared embedding space lets an image query match a text description. Why the correct answer wins: A Titan embedding model gives a documented dimension and a stable vector space.
- **C:** Incorrect for this question. Domain-tuned embeddings move relevant passages closer for vocabulary the base model misses. Why the correct answer wins: A Titan embedding model gives a documented dimension and a stable vector space.
- **D:** Incorrect for this question. Mixing vector spaces silently breaks similarity, because distances no longer mean the same thing. Why the correct answer wins: A Titan embedding model gives a documented dimension and a stable vector space.

### Question 19 — B, D

Answers: Combine keyword and vector retrieval and merge the ranked lists; Rerank the retrieved passages with an Amazon Bedrock reranker. Hybrid retrieval catches the exact identifier and a reranker fixes the order of the shortlist. Hybrid retrieval catches exact identifiers that a vector search alone can miss. A reranker scores the shortlist against the query and lifts precision before the prompt is built. Local study-map skill 1.13 (Hybrid Retrieval and Reranking), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. Larger chunks carry more context but dilute the embedding and crowd the prompt window. Why the correct answer wins: Hybrid retrieval catches the exact identifier and a reranker fixes the order of the shortlist.
- **B:** Correct. A reranker scores the shortlist against the query and lifts precision before the prompt is built. In this case: Hybrid retrieval catches the exact identifier and a reranker fixes the order of the shortlist.
- **C:** Incorrect for this question. Mixing vector spaces silently breaks similarity, because distances no longer mean the same thing. Why the correct answer wins: Hybrid retrieval catches the exact identifier and a reranker fixes the order of the shortlist.
- **D:** Correct. Hybrid retrieval catches exact identifiers that a vector search alone can miss. In this case: Hybrid retrieval catches the exact identifier and a reranker fixes the order of the shortlist.
- **E:** Incorrect for this question. More passages raise recall and also lengthen the prompt and the cost per call. Why the correct answer wins: Hybrid retrieval catches the exact identifier and a reranker fixes the order of the shortlist.

### Question 20 — B

Answer: Drop passages below a relevance score threshold. A threshold keeps marginal passages out of the prompt that would only add noise. Local study-map skill 1.13 (Hybrid Retrieval and Reranking), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. Expansion bridges vocabulary gaps between how users ask and how documents are written. Why the correct answer wins: A threshold keeps marginal passages out of the prompt that would only add noise.
- **B:** Correct. In this case: A threshold keeps marginal passages out of the prompt that would only add noise.
- **C:** Incorrect for this question. Semantic splitting places boundaries at topic shifts rather than at a character count. Why the correct answer wins: A threshold keeps marginal passages out of the prompt that would only add noise.
- **D:** Incorrect for this question. More passages raise recall and also lengthen the prompt and the cost per call. Why the correct answer wins: A threshold keeps marginal passages out of the prompt that would only add noise.

### Question 21 — A

Answer: Break a multi-part question into separate retrievals. Decomposition retrieves evidence for each sub-question instead of averaging them into one query. Local study-map skill 1.14 (Query Transformation and Handling), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Correct. In this case: Decomposition retrieves evidence for each sub-question instead of averaging them into one query.
- **B:** Incorrect for this question. Expansion bridges vocabulary gaps between how users ask and how documents are written. Why the correct answer wins: Decomposition retrieves evidence for each sub-question instead of averaging them into one query.
- **C:** Incorrect for this question. More passages raise recall and also lengthen the prompt and the cost per call. Why the correct answer wins: Decomposition retrieves evidence for each sub-question instead of averaging them into one query.
- **D:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: Decomposition retrieves evidence for each sub-question instead of averaging them into one query.

### Question 22 — D

Answer: Constrain the response with a JSON schema. A schema makes the output machine-parseable and rejects prose that breaks the contract. Local study-map skill 1.15 (Prompt Engineering and Governance), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. A token cap bounds the cost of a runaway answer and the latency of every call. Why the correct answer wins: A schema makes the output machine-parseable and rejects prose that breaks the contract.
- **B:** Incorrect for this question. A single blob loses the field boundaries the model needs to answer precisely. Why the correct answer wins: A schema makes the output machine-parseable and rejects prose that breaks the contract.
- **C:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: A schema makes the output machine-parseable and rejects prose that breaks the contract.
- **D:** Correct. In this case: A schema makes the output machine-parseable and rejects prose that breaks the contract.

### Question 23 — B

Answer: Lower the temperature for factual answers. Low temperature narrows sampling so repeatable factual answers stay stable. Local study-map skill 1.15 (Prompt Engineering and Governance), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. Examples show the model the output contract that instructions alone leave ambiguous. Why the correct answer wins: Low temperature narrows sampling so repeatable factual answers stay stable.
- **B:** Correct. In this case: Low temperature narrows sampling so repeatable factual answers stay stable.
- **C:** Incorrect for this question. A token cap bounds the cost of a runaway answer and the latency of every call. Why the correct answer wins: Low temperature narrows sampling so repeatable factual answers stay stable.
- **D:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: Low temperature narrows sampling so repeatable factual answers stay stable.

### Question 24 — C

Answer: Run the agent on Amazon Bedrock AgentCore. AgentCore supplies managed runtime, identity, memory, and observability for agents. Local study-map skill 2.1 (Agent Memory and State), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. Prompt-only memory forgets everything the moment the context window is trimmed. Why the correct answer wins: AgentCore supplies managed runtime, identity, memory, and observability for agents.
- **B:** Incorrect for this question. Direct calls from every app scatter keys, quotas, and logging across teams. Why the correct answer wins: AgentCore supplies managed runtime, identity, memory, and observability for agents.
- **C:** Correct. In this case: AgentCore supplies managed runtime, identity, memory, and observability for agents.
- **D:** Incorrect for this question. A Lambda tool is stateless, cheap at low volume, and scales per request. Why the correct answer wins: AgentCore supplies managed runtime, identity, memory, and observability for agents.

### Question 25 — C

Answer: Summarise the conversation before adding more turns. A running summary keeps long sessions inside the window at low token cost. Local study-map skill 2.1 (Agent Memory and State), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. Larger chunks carry more context but dilute the embedding and crowd the prompt window. Why the correct answer wins: A running summary keeps long sessions inside the window at low token cost.
- **B:** Incorrect for this question. A single blob loses the field boundaries the model needs to answer precisely. Why the correct answer wins: A running summary keeps long sessions inside the window at low token cost.
- **C:** Correct. In this case: A running summary keeps long sessions inside the window at low token cost.
- **D:** Incorrect for this question. Prompt-only memory forgets everything the moment the context window is trimmed. Why the correct answer wins: A running summary keeps long sessions inside the window at low token cost.

### Question 26 — B

Answer: Aggregate answers from several models with custom logic. An aggregation step can compare candidate answers before one is returned. Local study-map skill 2.2 (Agent Orchestration Patterns), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: An aggregation step can compare candidate answers before one is returned.
- **B:** Correct. In this case: An aggregation step can compare candidate answers before one is returned.
- **C:** Incorrect for this question. One agent with every tool makes tool choice ambiguous and permissions broad. Why the correct answer wins: An aggregation step can compare candidate answers before one is returned.
- **D:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: An aggregation step can compare candidate answers before one is returned.

### Question 27 — C, D

Answers: Set an explicit step and budget limit on the agent loop; Require human approval before the agent performs the action. An approval gate keeps an irreversible action with a person and a hard limit ends a runaway loop. A hard limit stops a loop that would otherwise consume tokens without converging. An approval gate keeps an irreversible side effect under human control. Local study-map skill 2.2 (Agent Orchestration Patterns), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. One agent with every tool makes tool choice ambiguous and permissions broad. Why the correct answer wins: An approval gate keeps an irreversible action with a person and a hard limit ends a runaway loop.
- **B:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: An approval gate keeps an irreversible action with a person and a hard limit ends a runaway loop.
- **C:** Correct. An approval gate keeps an irreversible side effect under human control. In this case: An approval gate keeps an irreversible action with a person and a hard limit ends a runaway loop.
- **D:** Correct. A hard limit stops a loop that would otherwise consume tokens without converging. In this case: An approval gate keeps an irreversible action with a person and a hard limit ends a runaway loop.
- **E:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: An approval gate keeps an irreversible action with a person and a hard limit ends a runaway loop.

### Question 28 — B

Answer: Validate tool arguments against a schema before calling. Schema validation rejects a malformed argument instead of sending it to the system of record. Local study-map skill 2.3 (Tool Reliability and Safeguards), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: Schema validation rejects a malformed argument instead of sending it to the system of record.
- **B:** Correct. In this case: Schema validation rejects a malformed argument instead of sending it to the system of record.
- **C:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: Schema validation rejects a malformed argument instead of sending it to the system of record.
- **D:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: Schema validation rejects a malformed argument instead of sending it to the system of record.

### Question 29 — A

Answer: Bound each tool call with a timeout and a fallback. A timeout keeps one slow dependency from stalling the whole agent turn. Local study-map skill 2.3 (Tool Reliability and Safeguards), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Correct. In this case: A timeout keeps one slow dependency from stalling the whole agent turn.
- **B:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: A timeout keeps one slow dependency from stalling the whole agent turn.
- **C:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: A timeout keeps one slow dependency from stalling the whole agent turn.
- **D:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: A timeout keeps one slow dependency from stalling the whole agent turn.

### Question 30 — D

Answer: Buy Amazon Bedrock provisioned throughput for the model. Provisioned throughput reserves model units and gives a predictable token-per-minute ceiling. Local study-map skill 2.4 (Foundation Model Deployment and Capacity), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: Provisioned throughput reserves model units and gives a predictable token-per-minute ceiling.
- **B:** Incorrect for this question. On-demand Bedrock inference bills per token with no committed capacity, which suits spiky or unproven demand. Why the correct answer wins: Provisioned throughput reserves model units and gives a predictable token-per-minute ceiling.
- **C:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: Provisioned throughput reserves model units and gives a predictable token-per-minute ceiling.
- **D:** Correct. In this case: Provisioned throughput reserves model units and gives a predictable token-per-minute ceiling.

### Question 31 — B, C

Answers: Buy Amazon Bedrock provisioned throughput for the model; Run the work as an Amazon Bedrock batch inference job. Provisioned throughput guarantees the interactive path and batch inference prices the offline volume lower. Provisioned throughput reserves model units and gives a predictable token-per-minute ceiling. Batch inference trades turnaround time for a lower price on large offline volumes. Local study-map skill 2.4 (Foundation Model Deployment and Capacity), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. On-demand Bedrock inference bills per token with no committed capacity, which suits spiky or unproven demand. Why the correct answer wins: Provisioned throughput guarantees the interactive path and batch inference prices the offline volume lower.
- **B:** Correct. Provisioned throughput reserves model units and gives a predictable token-per-minute ceiling. In this case: Provisioned throughput guarantees the interactive path and batch inference prices the offline volume lower.
- **C:** Correct. Batch inference trades turnaround time for a lower price on large offline volumes. In this case: Provisioned throughput guarantees the interactive path and batch inference prices the offline volume lower.
- **D:** Incorrect for this question. A synchronous call is simplest and makes the user wait for the final token. Why the correct answer wins: Provisioned throughput guarantees the interactive path and batch inference prices the offline volume lower.
- **E:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: Provisioned throughput guarantees the interactive path and batch inference prices the offline volume lower.

### Question 32 — D

Answer: Route domain events through Amazon EventBridge. EventBridge decouples producers from the GenAI consumer with rules and filtering. Local study-map skill 2.5 (Enterprise Integration Patterns), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. A queue absorbs bursts and lets a worker retry a failed model call. Why the correct answer wins: EventBridge decouples producers from the GenAI consumer with rules and filtering.
- **B:** Incorrect for this question. SNS delivers one event to many subscribers without the caller tracking them. Why the correct answer wins: EventBridge decouples producers from the GenAI consumer with rules and filtering.
- **C:** Incorrect for this question. AppFlow copies data from supported SaaS sources without custom connectors. Why the correct answer wins: EventBridge decouples producers from the GenAI consumer with rules and filtering.
- **D:** Correct. In this case: EventBridge decouples producers from the GenAI consumer with rules and filtering.

### Question 33 — A

Answer: Buffer the work in an Amazon SQS queue. A queue absorbs bursts and lets a worker retry a failed model call. Local study-map skill 2.5 (Enterprise Integration Patterns), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Correct. In this case: A queue absorbs bursts and lets a worker retry a failed model call.
- **B:** Incorrect for this question. SNS delivers one event to many subscribers without the caller tracking them. Why the correct answer wins: A queue absorbs bursts and lets a worker retry a failed model call.
- **C:** Incorrect for this question. API Gateway adds authentication, throttling, request validation, and streaming to the model call. Why the correct answer wins: A queue absorbs bursts and lets a worker retry a failed model call.
- **D:** Incorrect for this question. A synchronous call is simplest and makes the user wait for the final token. Why the correct answer wins: A queue absorbs bursts and lets a worker retry a failed model call.

### Question 34 — B

Answer: Give the task an IAM role scoped to the resources it uses. A scoped role issues temporary credentials with only the needed permissions. Local study-map skill 2.6 (Identity for Model Access), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. A key in an environment variable leaks through images, logs, and job definitions. Why the correct answer wins: A scoped role issues temporary credentials with only the needed permissions.
- **B:** Correct. In this case: A scoped role issues temporary credentials with only the needed permissions.
- **C:** Incorrect for this question. Transfer Family accepts SFTP uploads into S3 without a server to run. Why the correct answer wins: A scoped role issues temporary credentials with only the needed permissions.
- **D:** Incorrect for this question. A public bucket exposes the corpus to everyone the index was meant to constrain. Why the correct answer wins: A scoped role issues temporary credentials with only the needed permissions.

### Question 35 — C

Answer: Put one internal GenAI gateway in front of every model call. A gateway centralises credentials, quotas, logging, and model routing for all teams. Local study-map skill 2.7 (CI/CD and GenAI Gateway), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. Direct calls from every app scatter keys, quotas, and logging across teams. Why the correct answer wins: A gateway centralises credentials, quotas, logging, and model routing for all teams.
- **B:** Incorrect for this question. A key in an environment variable leaks through images, logs, and job definitions. Why the correct answer wins: A gateway centralises credentials, quotas, logging, and model routing for all teams.
- **C:** Correct. In this case: A gateway centralises credentials, quotas, logging, and model routing for all teams.
- **D:** Incorrect for this question. A hardcoded identifier forces a code change and a release to try another model. Why the correct answer wins: A gateway centralises credentials, quotas, logging, and model routing for all teams.

### Question 36 — C, D

Answers: Release the assistant through AWS CodePipeline; Run the evaluation suite in AWS CodeBuild. A pipeline ties the stages together and the build runs the evaluation suite before deployment. A pipeline ties source, build, test, and deploy into one auditable flow. CodeBuild runs the tests and quality gates as part of the release. Local study-map skill 2.7 (CI/CD and GenAI Gateway), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: A pipeline ties the stages together and the build runs the evaluation suite before deployment.
- **B:** Incorrect for this question. Direct calls from every app scatter keys, quotas, and logging across teams. Why the correct answer wins: A pipeline ties the stages together and the build runs the evaluation suite before deployment.
- **C:** Correct. CodeBuild runs the tests and quality gates as part of the release. In this case: A pipeline ties the stages together and the build runs the evaluation suite before deployment.
- **D:** Correct. A pipeline ties source, build, test, and deploy into one auditable flow. In this case: A pipeline ties the stages together and the build runs the evaluation suite before deployment.
- **E:** Incorrect for this question. A key in an environment variable leaks through images, logs, and job definitions. Why the correct answer wins: A pipeline ties the stages together and the build runs the evaluation suite before deployment.

### Question 37 — C

Answer: Stream tokens as server-sent events. Server-sent events deliver incremental text over ordinary HTTP. Local study-map skill 2.8 (Streaming and Asynchronous APIs), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. A synchronous call is simplest and makes the user wait for the final token. Why the correct answer wins: Server-sent events deliver incremental text over ordinary HTTP.
- **B:** Incorrect for this question. Asynchronous processing suits long generations that outlast an API timeout. Why the correct answer wins: Server-sent events deliver incremental text over ordinary HTTP.
- **C:** Correct. In this case: Server-sent events deliver incremental text over ordinary HTTP.
- **D:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: Server-sent events deliver incremental text over ordinary HTTP.

### Question 38 — D

Answer: Retry throttled calls with exponential backoff and jitter. Backoff with jitter spreads retries so a throttled client does not stampede the service. Local study-map skill 2.9 (API Resilience and Backoff), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: Backoff with jitter spreads retries so a throttled client does not stampede the service.
- **B:** Incorrect for this question. A circuit breaker stops sending traffic to a dependency that is already failing. Why the correct answer wins: Backoff with jitter spreads retries so a throttled client does not stampede the service.
- **C:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: Backoff with jitter spreads retries so a throttled client does not stampede the service.
- **D:** Correct. In this case: Backoff with jitter spreads retries so a throttled client does not stampede the service.

### Question 39 — A

Answer: Open a circuit breaker after repeated dependency failures. A circuit breaker stops sending traffic to a dependency that is already failing. Local study-map skill 2.9 (API Resilience and Backoff), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Correct. In this case: A circuit breaker stops sending traffic to a dependency that is already failing.
- **B:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: A circuit breaker stops sending traffic to a dependency that is already failing.
- **C:** Incorrect for this question. A synchronous call is simplest and makes the user wait for the final token. Why the correct answer wins: A circuit breaker stops sending traffic to a dependency that is already failing.
- **D:** Incorrect for this question. Backoff with jitter spreads retries so a throttled client does not stampede the service. Why the correct answer wins: A circuit breaker stops sending traffic to a dependency that is already failing.

### Question 40 — B

Answer: Expose the assistant through AWS AppSync. AppSync gives a managed GraphQL API with subscriptions for live responses. Local study-map skill 2.10 (Application Integration and Low Code), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. Edge logic trims, redacts, or routes a request before it crosses to the model Region. Why the correct answer wins: AppSync gives a managed GraphQL API with subscriptions for live responses.
- **B:** Correct. In this case: AppSync gives a managed GraphQL API with subscriptions for live responses.
- **C:** Incorrect for this question. API Gateway adds authentication, throttling, request validation, and streaming to the model call. Why the correct answer wins: AppSync gives a managed GraphQL API with subscriptions for live responses.
- **D:** Incorrect for this question. Server-sent events deliver incremental text over ordinary HTTP. Why the correct answer wins: AppSync gives a managed GraphQL API with subscriptions for live responses.

### Question 41 — D

Answer: Run the request shaping logic at the edge with Lambda@Edge. Edge logic trims, redacts, or routes a request before it crosses to the model Region. Local study-map skill 2.10 (Application Integration and Low Code), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. An edge cache answers identical requests without reaching the model. Why the correct answer wins: Edge logic trims, redacts, or routes a request before it crosses to the model Region.
- **B:** Incorrect for this question. API Gateway adds authentication, throttling, request validation, and streaming to the model call. Why the correct answer wins: Edge logic trims, redacts, or routes a request before it crosses to the model Region.
- **C:** Incorrect for this question. Direct calls from every app scatter keys, quotas, and logging across teams. Why the correct answer wins: Edge logic trims, redacts, or routes a request before it crosses to the model Region.
- **D:** Correct. In this case: Edge logic trims, redacts, or routes a request before it crosses to the model Region.

### Question 42 — D

Answer: Generate and explain the integration code with Amazon Q Developer. Q Developer drafts and explains SDK calls inside the editor, which speeds up the plumbing. Local study-map skill 2.11 (Developer Productivity Tooling), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. A pipeline ties source, build, test, and deploy into one auditable flow. Why the correct answer wins: Q Developer drafts and explains SDK calls inside the editor, which speeds up the plumbing.
- **B:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: Q Developer drafts and explains SDK calls inside the editor, which speeds up the plumbing.
- **C:** Incorrect for this question. CodeBuild runs the tests and quality gates as part of the release. Why the correct answer wins: Q Developer drafts and explains SDK calls inside the editor, which speeds up the plumbing.
- **D:** Correct. In this case: Q Developer drafts and explains SDK calls inside the editor, which speeds up the plumbing.

### Question 43 — A

Answer: Query the prompt and response logs with CloudWatch Logs Insights. Logs Insights correlates a spike in errors with the prompts that caused them. Local study-map skill 2.12 (Integration Troubleshooting), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Correct. In this case: Logs Insights correlates a spike in errors with the prompts that caused them.
- **B:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: Logs Insights correlates a spike in errors with the prompts that caused them.
- **C:** Incorrect for this question. A trace shows which hop in the chain added the latency. Why the correct answer wins: Logs Insights correlates a spike in errors with the prompts that caused them.
- **D:** Incorrect for this question. CloudTrail records who changed models, keys, and guardrails. Why the correct answer wins: Logs Insights correlates a spike in errors with the prompts that caused them.

### Question 44 — D

Answer: Apply Amazon Bedrock Guardrails content filters. Content filters score and block harmful input and output on the request path. Local study-map skill 3.1 (Content Safety Controls), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. A token cap bounds the cost of a runaway answer and the latency of every call. Why the correct answer wins: Content filters score and block harmful input and output on the request path.
- **B:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: Content filters score and block harmful input and output on the request path.
- **C:** Incorrect for this question. Low temperature narrows sampling so repeatable factual answers stay stable. Why the correct answer wins: Content filters score and block harmful input and output on the request path.
- **D:** Correct. In this case: Content filters score and block harmful input and output on the request path.

### Question 45 — B, C

Answers: Define denied topics in Amazon Bedrock Guardrails; Enable sensitive-information filters in Amazon Bedrock Guardrails. Denied topics refuse the ruled-out subject and the sensitive-information filter masks personal data. Denied topics refuse the subject areas the business has ruled out. PII filters detect and mask personal data in prompts and responses. Local study-map skill 3.1 (Content Safety Controls), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: Denied topics refuse the ruled-out subject and the sensitive-information filter masks personal data.
- **B:** Correct. PII filters detect and mask personal data in prompts and responses. In this case: Denied topics refuse the ruled-out subject and the sensitive-information filter masks personal data.
- **C:** Correct. Denied topics refuse the subject areas the business has ruled out. In this case: Denied topics refuse the ruled-out subject and the sensitive-information filter masks personal data.
- **D:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: Denied topics refuse the ruled-out subject and the sensitive-information filter masks personal data.
- **E:** Incorrect for this question. A token cap bounds the cost of a runaway answer and the latency of every call. Why the correct answer wins: Denied topics refuse the ruled-out subject and the sensitive-information filter masks personal data.

### Question 46 — C

Answer: Require the answer to cite the retrieved passage. A citation makes each claim traceable to a source the reader can check. Local study-map skill 3.2 (Grounding and Hallucination Reduction), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. A token cap bounds the cost of a runaway answer and the latency of every call. Why the correct answer wins: A citation makes each claim traceable to a source the reader can check.
- **B:** Incorrect for this question. An escalation path keeps consequential answers with a human owner. Why the correct answer wins: A citation makes each claim traceable to a source the reader can check.
- **C:** Correct. In this case: A citation makes each claim traceable to a source the reader can check.
- **D:** Incorrect for this question. A score lets the interface route low-confidence answers to a human. Why the correct answer wins: A citation makes each claim traceable to a source the reader can check.

### Question 47 — A

Answer: Enable the contextual grounding check in Guardrails. The grounding check compares the response with the retrieved source and flags unsupported claims. Local study-map skill 3.2 (Grounding and Hallucination Reduction), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Correct. In this case: The grounding check compares the response with the retrieved source and flags unsupported claims.
- **B:** Incorrect for this question. Low temperature narrows sampling so repeatable factual answers stay stable. Why the correct answer wins: The grounding check compares the response with the retrieved source and flags unsupported claims.
- **C:** Incorrect for this question. A schema makes the output machine-parseable and rejects prose that breaks the contract. Why the correct answer wins: The grounding check compares the response with the retrieved source and flags unsupported claims.
- **D:** Incorrect for this question. Similarity scoring is fast and tolerant of wording, but blind to a contradicted fact. Why the correct answer wins: The grounding check compares the response with the retrieved source and flags unsupported claims.

### Question 48 — B

Answer: Screen inputs for instruction override and jailbreak patterns. A pre-filter catches text that tries to replace the system instruction. Local study-map skill 3.3 (Prompt Injection Defence), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. Low temperature narrows sampling so repeatable factual answers stay stable. Why the correct answer wins: A pre-filter catches text that tries to replace the system instruction.
- **B:** Correct. In this case: A pre-filter catches text that tries to replace the system instruction.
- **C:** Incorrect for this question. A token cap bounds the cost of a runaway answer and the latency of every call. Why the correct answer wins: A pre-filter catches text that tries to replace the system instruction.
- **D:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: A pre-filter catches text that tries to replace the system instruction.

### Question 49 — D

Answer: Run an adversarial prompt suite before each release. A hostile test set finds regressions in refusal behaviour before users do. Local study-map skill 3.3 (Prompt Injection Defence), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. A golden set with known answers catches a regression the moment it ships. Why the correct answer wins: A hostile test set finds regressions in refusal behaviour before users do.
- **B:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: A hostile test set finds regressions in refusal behaviour before users do.
- **C:** Incorrect for this question. A rubric with human scores gives a reference the automatic metrics can be checked against. Why the correct answer wins: A hostile test set finds regressions in refusal behaviour before users do.
- **D:** Correct. In this case: A hostile test set finds regressions in refusal behaviour before users do.

### Question 50 — B

Answer: Mask direct identifiers before the record is stored. Masking removes names and account numbers while keeping the record usable. Local study-map skill 3.4 (Privacy and PII Protection), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. Macie finds sensitive data at rest so the corpus can be cleaned before indexing. Why the correct answer wins: Masking removes names and account numbers while keeping the record usable.
- **B:** Correct. In this case: Masking removes names and account numbers while keeping the record usable.
- **C:** Incorrect for this question. Masking at the boundary keeps personal data out of the model request entirely. Why the correct answer wins: Masking removes names and account numbers while keeping the record usable.
- **D:** Incorrect for this question. PII filters detect and mask personal data in prompts and responses. Why the correct answer wins: Masking removes names and account numbers while keeping the record usable.

### Question 51 — B, D

Answers: Scan the data store with Amazon Macie; Detect personal data with Amazon Comprehend. Macie finds sensitive data at rest and Comprehend identifies the entities to remove. Macie finds sensitive data at rest so the corpus can be cleaned before indexing. Comprehend identifies entities and PII so they can be masked before the model sees them. Local study-map skill 3.4 (Privacy and PII Protection), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: Macie finds sensitive data at rest and Comprehend identifies the entities to remove.
- **B:** Correct. Macie finds sensitive data at rest so the corpus can be cleaned before indexing. In this case: Macie finds sensitive data at rest and Comprehend identifies the entities to remove.
- **C:** Incorrect for this question. A key in an environment variable leaks through images, logs, and job definitions. Why the correct answer wins: Macie finds sensitive data at rest and Comprehend identifies the entities to remove.
- **D:** Correct. Comprehend identifies entities and PII so they can be masked before the model sees them. In this case: Macie finds sensitive data at rest and Comprehend identifies the entities to remove.
- **E:** Incorrect for this question. Content filters score and block harmful input and output on the request path. Why the correct answer wins: Macie finds sensitive data at rest and Comprehend identifies the entities to remove.

### Question 52 — D

Answer: Call the model through an interface VPC endpoint. A private endpoint keeps model traffic off the public internet. Local study-map skill 3.5 (Network and Data Isolation), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. An edge cache answers identical requests without reaching the model. Why the correct answer wins: A private endpoint keeps model traffic off the public internet.
- **B:** Incorrect for this question. A key in an environment variable leaks through images, logs, and job definitions. Why the correct answer wins: A private endpoint keeps model traffic off the public internet.
- **C:** Incorrect for this question. A public bucket exposes the corpus to everyone the index was meant to constrain. Why the correct answer wins: A private endpoint keeps model traffic off the public internet.
- **D:** Correct. In this case: A private endpoint keeps model traffic off the public internet.

### Question 53 — C

Answer: Deploy the workload in private subnets. Private subnets remove inbound internet routing from the compute tier. Local study-map skill 3.5 (Network and Data Isolation), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. An edge cache answers identical requests without reaching the model. Why the correct answer wins: Private subnets remove inbound internet routing from the compute tier.
- **B:** Incorrect for this question. Direct calls from every app scatter keys, quotas, and logging across teams. Why the correct answer wins: Private subnets remove inbound internet routing from the compute tier.
- **C:** Correct. In this case: Private subnets remove inbound internet routing from the compute tier.
- **D:** Incorrect for this question. A public bucket exposes the corpus to everyone the index was meant to constrain. Why the correct answer wins: Private subnets remove inbound internet routing from the compute tier.

### Question 54 — C

Answer: Record control-plane activity in AWS CloudTrail. CloudTrail records who changed models, keys, and guardrails. Local study-map skill 3.6 (Governance, Lineage, and Audit), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: CloudTrail records who changed models, keys, and guardrails.
- **B:** Incorrect for this question. Invocation logs capture the request, the response, and the token counts. Why the correct answer wins: CloudTrail records who changed models, keys, and guardrails.
- **C:** Correct. In this case: CloudTrail records who changed models, keys, and guardrails.
- **D:** Incorrect for this question. Grafana combines model, infrastructure, and business metrics on one screen. Why the correct answer wins: CloudTrail records who changed models, keys, and guardrails.

### Question 55 — A, B

Answers: Record data lineage in the AWS Glue Data Catalog; Turn on Amazon Bedrock model invocation logging. Lineage ties the answer to its corpus version and invocation logs hold the request and the response. Lineage shows which corpus and version produced an answer. Invocation logs capture the request, the response, and the token counts. Local study-map skill 3.6 (Governance, Lineage, and Audit), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Correct. Lineage shows which corpus and version produced an answer. In this case: Lineage ties the answer to its corpus version and invocation logs hold the request and the response.
- **B:** Correct. Invocation logs capture the request, the response, and the token counts. In this case: Lineage ties the answer to its corpus version and invocation logs hold the request and the response.
- **C:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: Lineage ties the answer to its corpus version and invocation logs hold the request and the response.
- **D:** Incorrect for this question. A key in an environment variable leaks through images, logs, and job definitions. Why the correct answer wins: Lineage ties the answer to its corpus version and invocation logs hold the request and the response.
- **E:** Incorrect for this question. Low temperature narrows sampling so repeatable factual answers stay stable. Why the correct answer wins: Lineage ties the answer to its corpus version and invocation logs hold the request and the response.

### Question 56 — A

Answer: Publish a model card with the model version. A model card documents intended use and known limits for reviewers. Local study-map skill 3.7 (Responsible AI and Transparency), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Correct. In this case: A model card documents intended use and known limits for reviewers.
- **B:** Incorrect for this question. A schema makes the output machine-parseable and rejects prose that breaks the contract. Why the correct answer wins: A model card documents intended use and known limits for reviewers.
- **C:** Incorrect for this question. A Bedrock evaluation job scores candidate models on your prompts and metrics before you choose. Why the correct answer wins: A model card documents intended use and known limits for reviewers.
- **D:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: A model card documents intended use and known limits for reviewers.

### Question 57 — A

Answer: Return a confidence score with each answer. A score lets the interface route low-confidence answers to a human. Local study-map skill 3.7 (Responsible AI and Transparency), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Correct. In this case: A score lets the interface route low-confidence answers to a human.
- **B:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: A score lets the interface route low-confidence answers to a human.
- **C:** Incorrect for this question. A token cap bounds the cost of a runaway answer and the latency of every call. Why the correct answer wins: A score lets the interface route low-confidence answers to a human.
- **D:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: A score lets the interface route low-confidence answers to a human.

### Question 58 — A

Answer: Alert when fairness metrics move beyond a band. A drift alert catches a fairness regression after a model or prompt change. Local study-map skill 3.8 (Fairness and Compliance Monitoring), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Correct. In this case: A drift alert catches a fairness regression after a model or prompt change.
- **B:** Incorrect for this question. Anomaly detection finds an unexpected token bill without a fixed threshold. Why the correct answer wins: A drift alert catches a fairness regression after a model or prompt change.
- **C:** Incorrect for this question. A latency alarm fires on the symptom users feel. Why the correct answer wins: A drift alert catches a fairness regression after a model or prompt change.
- **D:** Incorrect for this question. Segment metrics expose a quality gap that an overall average hides. Why the correct answer wins: A drift alert catches a fairness regression after a model or prompt change.

### Question 59 — D

Answer: Prune older turns from the context window. Dropping stale turns cuts input tokens without losing the current instruction. Local study-map skill 4.1 (Token Cost Efficiency), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Incorrect for this question. More passages raise recall and also lengthen the prompt and the cost per call. Why the correct answer wins: Dropping stale turns cuts input tokens without losing the current instruction.
- **B:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: Dropping stale turns cuts input tokens without losing the current instruction.
- **C:** Incorrect for this question. Larger chunks carry more context but dilute the embedding and crowd the prompt window. Why the correct answer wins: Dropping stale turns cuts input tokens without losing the current instruction.
- **D:** Correct. In this case: Dropping stale turns cuts input tokens without losing the current instruction.

### Question 60 — B

Answer: Cap the response length in the request. A token cap bounds the cost of a runaway answer and the latency of every call. Local study-map skill 4.1 (Token Cost Efficiency), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Incorrect for this question. A single blob loses the field boundaries the model needs to answer precisely. Why the correct answer wins: A token cap bounds the cost of a runaway answer and the latency of every call.
- **B:** Correct. In this case: A token cap bounds the cost of a runaway answer and the latency of every call.
- **C:** Incorrect for this question. More passages raise recall and also lengthen the prompt and the cost per call. Why the correct answer wins: A token cap bounds the cost of a runaway answer and the latency of every call.
- **D:** Incorrect for this question. Larger chunks carry more context but dilute the embedding and crowd the prompt window. Why the correct answer wins: A token cap bounds the cost of a runaway answer and the latency of every call.

### Question 61 — C

Answer: Cache the stable prompt prefix with prompt caching. Prompt caching reuses processed prefix tokens, which cuts latency and input cost on repeat calls. Local study-map skill 4.2 (Model Tiering and Caching), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Incorrect for this question. A semantic cache serves a near-duplicate question without a model call. Why the correct answer wins: Prompt caching reuses processed prefix tokens, which cuts latency and input cost on repeat calls.
- **B:** Incorrect for this question. A hash cache is exact and avoids a false hit between similar questions. Why the correct answer wins: Prompt caching reuses processed prefix tokens, which cuts latency and input cost on repeat calls.
- **C:** Correct. In this case: Prompt caching reuses processed prefix tokens, which cuts latency and input cost on repeat calls.
- **D:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: Prompt caching reuses processed prefix tokens, which cuts latency and input cost on repeat calls.

### Question 62 — A, B

Answers: Send routine prompts to a small model and hard prompts to a large one; Cache the response under a hash of the normalised request. Routing keeps easy prompts on a small model and an exact cache removes repeat calls entirely. Tiered routing spends the large model only on the requests that need it. A hash cache is exact and avoids a false hit between similar questions. Local study-map skill 4.2 (Model Tiering and Caching), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Correct. A hash cache is exact and avoids a false hit between similar questions. In this case: Routing keeps easy prompts on a small model and an exact cache removes repeat calls entirely.
- **B:** Correct. Tiered routing spends the large model only on the requests that need it. In this case: Routing keeps easy prompts on a small model and an exact cache removes repeat calls entirely.
- **C:** Incorrect for this question. A full fine-tune changes all weights, which is expensive and gives one model per task. Why the correct answer wins: Routing keeps easy prompts on a small model and an exact cache removes repeat calls entirely.
- **D:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: Routing keeps easy prompts on a small model and an exact cache removes repeat calls entirely.
- **E:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: Routing keeps easy prompts on a small model and an exact cache removes repeat calls entirely.

### Question 63 — A

Answer: Issue independent model calls in parallel. Parallel calls cut wall-clock time for sub-tasks that do not depend on each other. Local study-map skill 4.3 (Throughput and Latency Optimisation), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Correct. In this case: Parallel calls cut wall-clock time for sub-tasks that do not depend on each other.
- **B:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: Parallel calls cut wall-clock time for sub-tasks that do not depend on each other.
- **C:** Incorrect for this question. Batch inference trades turnaround time for a lower price on large offline volumes. Why the correct answer wins: Parallel calls cut wall-clock time for sub-tasks that do not depend on each other.
- **D:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: Parallel calls cut wall-clock time for sub-tasks that do not depend on each other.

### Question 64 — C, E

Answers: Choose a lower-latency model for the interactive path; Stream tokens as they are generated. A latency-optimised model shortens each call and streaming improves perceived speed. A smaller or latency-optimised model answers faster at some quality cost. Streaming lowers perceived latency without changing total generation time. Local study-map skill 4.3 (Throughput and Latency Optimisation), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: A latency-optimised model shortens each call and streaming improves perceived speed.
- **B:** Incorrect for this question. Batch inference trades turnaround time for a lower price on large offline volumes. Why the correct answer wins: A latency-optimised model shortens each call and streaming improves perceived speed.
- **C:** Correct. A smaller or latency-optimised model answers faster at some quality cost. In this case: A latency-optimised model shortens each call and streaming improves perceived speed.
- **D:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: A latency-optimised model shortens each call and streaming improves perceived speed.
- **E:** Correct. Streaming lowers perceived latency without changing total generation time. In this case: A latency-optimised model shortens each call and streaming improves perceived speed.

### Question 65 — C

Answer: Turn on Amazon Bedrock model invocation logging. Invocation logs capture the request, the response, and the token counts. Local study-map skill 4.4 (GenAI Observability), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: Invocation logs capture the request, the response, and the token counts.
- **B:** Incorrect for this question. CloudTrail records who changed models, keys, and guardrails. Why the correct answer wins: Invocation logs capture the request, the response, and the token counts.
- **C:** Correct. In this case: Invocation logs capture the request, the response, and the token counts.
- **D:** Incorrect for this question. A model card documents intended use and known limits for reviewers. Why the correct answer wins: Invocation logs capture the request, the response, and the token counts.

### Question 66 — C, D

Answers: Publish token usage as CloudWatch metrics; Alarm on p95 latency and error rate. Token metrics show where spend comes from and a latency alarm fires on the symptom users feel. Local study-map skill 4.4 (GenAI Observability), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Incorrect for this question. A model card documents intended use and known limits for reviewers. Why the correct answer wins: Token metrics show where spend comes from and a latency alarm fires on the symptom users feel.
- **B:** Incorrect for this question. Anomaly detection finds an unexpected token bill without a fixed threshold. Why the correct answer wins: Token metrics show where spend comes from and a latency alarm fires on the symptom users feel.
- **C:** Correct. In this case: Token metrics show where spend comes from and a latency alarm fires on the symptom users feel.
- **D:** Correct. In this case: Token metrics show where spend comes from and a latency alarm fires on the symptom users feel.
- **E:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: Token metrics show where spend comes from and a latency alarm fires on the symptom users feel.

### Question 67 — B

Answer: Cover the steady compute with a Savings Plan. A Savings Plan discounts the predictable part of the compute baseline. Local study-map skill 4.5 (Cost Attribution and Governance), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Incorrect for this question. A budget alert stops one tenant from consuming the shared quota. Why the correct answer wins: A Savings Plan discounts the predictable part of the compute baseline.
- **B:** Correct. In this case: A Savings Plan discounts the predictable part of the compute baseline.
- **C:** Incorrect for this question. Anomaly detection finds an unexpected token bill without a fixed threshold. Why the correct answer wins: A Savings Plan discounts the predictable part of the compute baseline.
- **D:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: A Savings Plan discounts the predictable part of the compute baseline.

### Question 68 — C

Answer: Score how directly the answer addresses the question. Relevance separates an off-topic answer from a factually wrong one. Local study-map skill 5.1 (GenAI Evaluation Metrics), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Incorrect for this question. Embedding-based similarity credits a correct paraphrase that word overlap misses. Why the correct answer wins: Relevance separates an off-topic answer from a factually wrong one.
- **B:** Incorrect for this question. Recall shows whether the answer was missing evidence before generation began. Why the correct answer wins: Relevance separates an off-topic answer from a factually wrong one.
- **C:** Correct. In this case: Relevance separates an off-topic answer from a factually wrong one.
- **D:** Incorrect for this question. Overlap metrics are cheap and reward wording that matches the references. Why the correct answer wins: Relevance separates an off-topic answer from a factually wrong one.

### Question 69 — C, E

Answers: Report BERTScore for semantic similarity to the reference; Measure whether each claim is supported by the retrieved context. Embedding similarity credits a faithful paraphrase and the grounding metric catches an invented claim. Embedding-based similarity credits a correct paraphrase that word overlap misses. A faithfulness check separates a grounded answer from a fluent invention. Local study-map skill 5.1 (GenAI Evaluation Metrics), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Incorrect for this question. Recall shows whether the answer was missing evidence before generation began. Why the correct answer wins: Embedding similarity credits a faithful paraphrase and the grounding metric catches an invented claim.
- **B:** Incorrect for this question. Overlap metrics are cheap and reward wording that matches the references. Why the correct answer wins: Embedding similarity credits a faithful paraphrase and the grounding metric catches an invented claim.
- **C:** Correct. Embedding-based similarity credits a correct paraphrase that word overlap misses. In this case: Embedding similarity credits a faithful paraphrase and the grounding metric catches an invented claim.
- **D:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: Embedding similarity credits a faithful paraphrase and the grounding metric catches an invented claim.
- **E:** Correct. A faithfulness check separates a grounded answer from a fluent invention. In this case: Embedding similarity credits a faithful paraphrase and the grounding metric catches an invented claim.

### Question 70 — B

Answer: Send a small traffic share to the new prompt and watch the metrics. A canary limits the blast radius of a prompt or model change. Local study-map skill 5.2 (Model Comparison and Traffic Testing), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Incorrect for this question. An A/B test measures the difference on real traffic before a full switch. Why the correct answer wins: A canary limits the blast radius of a prompt or model change.
- **B:** Correct. In this case: A canary limits the blast radius of a prompt or model change.
- **C:** Incorrect for this question. A rubric with human scores gives a reference the automatic metrics can be checked against. Why the correct answer wins: A canary limits the blast radius of a prompt or model change.
- **D:** Incorrect for this question. Shadow traffic compares answers with no user exposure. Why the correct answer wins: A canary limits the blast radius of a prompt or model change.

### Question 71 — A

Answer: Run the release against a curated golden question set. A golden set with known answers catches a regression the moment it ships. Local study-map skill 5.3 (Regression Testing and Quality Gates), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Correct. In this case: A golden set with known answers catches a regression the moment it ships.
- **B:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: A golden set with known answers catches a regression the moment it ships.
- **C:** Incorrect for this question. A rubric with human scores gives a reference the automatic metrics can be checked against. Why the correct answer wins: A golden set with known answers catches a regression the moment it ships.
- **D:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: A golden set with known answers catches a regression the moment it ships.

### Question 72 — C, E

Answers: Block the release when evaluation drops below the threshold; Run a prompt regression suite before promoting a version. A quality gate blocks the regression and a per-template suite proves each wording before promotion. A quality gate stops a measurable regression from reaching production. A fixed suite of prompts and expected properties catches a wording change that breaks behaviour. Local study-map skill 5.3 (Regression Testing and Quality Gates), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: A quality gate blocks the regression and a per-template suite proves each wording before promotion.
- **B:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: A quality gate blocks the regression and a per-template suite proves each wording before promotion.
- **C:** Correct. A quality gate stops a measurable regression from reaching production. In this case: A quality gate blocks the regression and a per-template suite proves each wording before promotion.
- **D:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: A quality gate blocks the regression and a per-template suite proves each wording before promotion.
- **E:** Correct. A fixed suite of prompts and expected properties catches a wording change that breaks behaviour. In this case: A quality gate blocks the regression and a per-template suite proves each wording before promotion.

### Question 73 — B

Answer: Measure whether the retrieved passages were relevant. Retrieval precision explains a wrong answer that the model was given bad context for. Local study-map skill 5.4 (Retrieval and Agent Evaluation), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Incorrect for this question. Tool accuracy locates the failure inside the agent loop rather than at the answer. Why the correct answer wins: Retrieval precision explains a wrong answer that the model was given bad context for.
- **B:** Correct. In this case: Retrieval precision explains a wrong answer that the model was given bad context for.
- **C:** Incorrect for this question. Recall shows whether the answer was missing evidence before generation began. Why the correct answer wins: Retrieval precision explains a wrong answer that the model was given bad context for.
- **D:** Incorrect for this question. Overlap metrics are cheap and reward wording that matches the references. Why the correct answer wins: Retrieval precision explains a wrong answer that the model was given bad context for.

### Question 74 — C, D

Answers: Measure whether the agent called the right tool with the right arguments; Measure the share of agent tasks completed end to end. Tool accuracy locates the wrong call and completion rate shows whether the task ended. Tool accuracy locates the failure inside the agent loop rather than at the answer. Completion rate is the outcome metric for an agent that must actually finish work. Local study-map skill 5.4 (Retrieval and Agent Evaluation), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Incorrect for this question. Embedding-based similarity credits a correct paraphrase that word overlap misses. Why the correct answer wins: Tool accuracy locates the wrong call and completion rate shows whether the task ended.
- **B:** Incorrect for this question. Overlap metrics are cheap and reward wording that matches the references. Why the correct answer wins: Tool accuracy locates the wrong call and completion rate shows whether the task ended.
- **C:** Correct. Tool accuracy locates the failure inside the agent loop rather than at the answer. In this case: Tool accuracy locates the wrong call and completion rate shows whether the task ended.
- **D:** Correct. Completion rate is the outcome metric for an agent that must actually finish work. In this case: Tool accuracy locates the wrong call and completion rate shows whether the task ended.
- **E:** Incorrect for this question. Retrieval precision explains a wrong answer that the model was given bad context for. Why the correct answer wins: Tool accuracy locates the wrong call and completion rate shows whether the task ended.

### Question 75 — C

Answer: Log the token count and check for truncated prompts. A truncation check shows whether the model ever saw the end of the instruction. Local study-map skill 5.5 (GenAI Troubleshooting), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Incorrect for this question. Logs Insights correlates a spike in errors with the prompts that caused it. Why the correct answer wins: A truncation check shows whether the model ever saw the end of the instruction.
- **B:** Incorrect for this question. Overflow protection keeps the prompt inside the model limit instead of truncating silently. Why the correct answer wins: A truncation check shows whether the model ever saw the end of the instruction.
- **C:** Correct. In this case: A truncation check shows whether the model ever saw the end of the instruction.
- **D:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: A truncation check shows whether the model ever saw the end of the instruction.
