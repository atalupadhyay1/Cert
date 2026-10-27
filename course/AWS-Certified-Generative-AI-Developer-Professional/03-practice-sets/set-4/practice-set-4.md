# AWS Certified Generative AI Developer - Professional (AIP-C01) — Full-Length Mock Exam 4

Generative AI Developer · 75 questions · 180 minutes · scaled passing score 750 of 1000

Blueprint-weighted mock exam. Item mix: 60 multiple-choice and 15 multiple-response items (the selection count is stated in each multi-response stem). The published exam has 75 questions in 180 minutes, of which 65 are scored and 10 are unscored, and AWS does not identify the unscored items. AWS publishes no split between multiple-choice and multiple-response items, so the 15-item multi-response block is an authoring choice. At 75 items in 180 minutes this set matches the published pacing at about 144 seconds per item, including the same unscored proportion. The published format has no case-study component, so no case-study item appears here. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied AWS exam items.

## Questions

---

## Domain 1 — Foundation Model Integration, Data Management, and Compliance (31%) — Model integration, data pipelines, vector stores, retrieval, and prompts

### 1. A publisher is designing one assistant for news, lifestyle, and video brands and wants safety enforced once rather than per brand. Which two choices belong in the reference design? Select two.

- A. Apply Amazon Bedrock Guardrails content filters
- B. Let each application call the model API directly
- C. Put one internal GenAI gateway in front of every model call
- D. Use one frontier model for every request
- E. Hardcode one model identifier in the application source

### 2. An editorial board will approve a headline assistant only if the model choice is evidenced and the unit economics are known. Which two artefacts make that case? Select two.

- A. Run a full fine-tune of every model weight
- B. Let each application call the model API directly
- C. Compare the candidates with an Amazon Bedrock model evaluation job
- D. Use one frontier model for every request
- E. Compare quality per thousand tokens across candidates

### 3. Before funding an ad-copy generator, the team must show copywriters would ship its drafts. What should the pilot produce?

- A. Report BERTScore for semantic similarity to the reference
- B. Have reviewers score a sample against a written rubric
- C. Compare the candidates with an Amazon Bedrock model evaluation job
- D. Report ROUGE and BLEU against the reference answers

### 4. A newsroom tool turns a published article into a three-line summary, and it runs thousands of times a day. Which model choice fits?

- A. Run a full fine-tune of every model weight
- B. Right-size the model to the task difficulty
- C. Route the call through Amazon Bedrock cross-Region inference
- D. Use one frontier model for every request

### 5. Two models are shortlisted for headline generation and the desk has rated a thousand existing headlines. How should the choice be made?

- A. Use one frontier model for every request
- B. Compare the candidates with an Amazon Bedrock model evaluation job
- C. Run a full fine-tune of every model weight
- D. Fine-tune with low-rank adaptation adapters

### 6. One title wants a different model from the rest of the group next week, without a deployment. What allows that?

- A. Keep the prompt as a string constant in the application code
- B. Let each application call the model API directly
- C. Put the model identifier in AWS AppConfig and switch it without a deploy
- D. Hardcode one model identifier in the application source

### 7. A live election broadcast triples assistant traffic, and the primary Region starts throttling. What absorbs the spike?

- A. Store the model API key in an environment variable
- B. Retry the failed call until it succeeds
- C. Keep a GPU endpoint running for occasional requests
- D. Route the call through Amazon Bedrock cross-Region inference

### 8. A provider outage hits during a launch and the newsroom would rather have shorter captions than none. What design meets that?

- A. Fall back to a second model when the first is unavailable
- B. Use one frontier model for every request
- C. Retry the failed call until it succeeds
- D. Raise the temperature for creative variants

### 9. A large model writes good summaries at a price the publisher will not keep paying, and the task never changes. What lifecycle move fits?

- A. Let each application call the model API directly
- B. Distil the large model into a smaller task-specific model
- C. Keep the prompt as a string constant in the application code
- D. Run a full fine-tune of every model weight

### 10. Article metadata arrives from five CMS instances and sometimes lacks a rights flag or a canonical URL. What should reject the bad batch?

- A. Set an explicit CloudWatch Logs retention period
- B. Validate response structure and log the failures
- C. Enforce freshness and completeness rules with AWS Glue Data Quality
- D. Scan the data store with Amazon Macie

### 11. Editors filter the archive by person and organisation, and those values must be exact. What should extraction add while indexing?

- A. Normalise the text with a model call before indexing
- B. Concatenate all fields into one unlabelled text block
- C. Format the turns as an alternating conversation structure
- D. Extract entities with Amazon Comprehend before indexing

### 12. A photo desk wants to find images with a text description and find articles with an image. What connects the two modalities?

- A. Transcribe the call recordings with Amazon Transcribe
- B. Extract the text from scanned pages with Amazon Textract
- C. Generate embeddings with an Amazon Titan text embedding model
- D. Embed text and images with one multimodal model

### 13. A writing assistant must respect the order of editor instructions and its own earlier drafts. How should the request be built?

- A. Raise the temperature for creative variants
- B. Format the turns as an alternating conversation structure
- C. Concatenate all fields into one unlabelled text block
- D. Cap the response length in the request

### 14. A developer gets a body validation error from the model endpoint while the prompt reads correctly. What is wrong?

- A. Format the turns as an alternating conversation structure
- B. Concatenate all fields into one unlabelled text block
- C. Keep the prompt as a string constant in the application code
- D. Send the request as the JSON body the model expects

### 15. The archive holds eighty million article chunks and must support filtered search by section and date at scale. Where should the vectors live?

- A. Keep the source documents in Amazon DocumentDB
- B. Store the knowledge graph in Amazon Neptune
- C. Keep embeddings and metadata in Amazon DynamoDB
- D. Index the vectors in Amazon OpenSearch Service with k-NN search

### 16. Archive content includes licensed material that may not be quoted after its rights window. What keeps it out of answers?

- A. Drop passages below a relevance score threshold
- B. Filter the search by document metadata before the similarity ranking
- C. Re-embed the corpus when the embedding model changes
- D. Raise the number of retrieved passages per query

### 17. Breaking stories must be searchable within a minute of publication, and the corpus is far too large to rebuild. What keeps it current?

- A. Cache every answer with no expiry
- B. Rebuild the index on a schedule and accept staleness between runs
- C. Re-embed the corpus when the embedding model changes
- D. Update the index incrementally when a source document changes

### 18. Interview transcripts switch topic without headings, so fixed windows slice through answers. How should the split be chosen?

- A. Keep old vectors and embed new documents with the newer model
- B. Split where the embedding similarity between sentences drops
- C. Split documents into fixed-size token windows with overlap
- D. Increase the chunk size so every answer fits in one chunk

### 19. A news archive search must match named entities exactly and must stop padding answers with weakly related pieces. Which two changes do both? Select two.

- A. Raise the number of retrieved passages per query
- B. Keep old vectors and embed new documents with the newer model
- C. Drop passages below a relevance score threshold
- D. Increase the chunk size so every answer fits in one chunk
- E. Combine keyword and vector retrieval and merge the ranked lists

### 20. The right article is retrieved but ranked seventh behind loosely related pieces. What improves the order of the shortlist?

- A. Rerank the retrieved passages with an Amazon Bedrock reranker
- B. Expand the user query into related terms before retrieval
- C. Split where the embedding similarity between sentences drops
- D. Raise the number of retrieved passages per query

### 21. An editor asks one question about both a defamation policy and a corrections policy. What should happen before retrieval?

- A. Expand the user query into related terms before retrieval
- B. Raise the number of retrieved passages per query
- C. Cache every answer with no expiry
- D. Break a multi-part question into separate retrievals

### 22. The assistant must always write in the publisher's voice and never speculate about unnamed sources. Where do those rules belong?

- A. Put the role, tone, and boundaries in the system prompt
- B. Raise the temperature for creative variants
- C. Keep the prompt as a string constant in the application code
- D. Cap the response length in the request

### 23. Drafts keep missing the house style for captions, and describing the style in prose has not worked. What should the prompt add?

- A. Keep the prompt as a string constant in the application code
- B. Add worked examples of the expected answer shape
- C. Cap the response length in the request
- D. Raise the temperature for creative variants

---

## Domain 2 — Implementation and Integration (26%) — Agents, deployment, enterprise integration, APIs, and developer tooling

### 24. A research agent must remember the angle it is chasing across a dozen turns and survive a restart. Where should that state live?

- A. Keep conversation and task memory in Amazon DynamoDB
- B. Cache every answer with no expiry
- C. Set an explicit CloudWatch Logs retention period
- D. Keep memory only in the prompt of the current turn

### 25. A long editorial session reaches a hundred turns and resending them all is expensive. What keeps the cost bounded?

- A. Increase the chunk size so every answer fits in one chunk
- B. Keep memory only in the prompt of the current turn
- C. Concatenate all fields into one unlabelled text block
- D. Summarise the conversation before adding more turns

### 26. The newsroom wants an open-source agent loop it can host itself and point at any model. What fits?

- A. Keep the prompt as a string constant in the application code
- B. Build the agent with Strands Agents
- C. Give one agent every tool in the platform
- D. Return the whole answer from one synchronous call

### 27. A fact-checking agent sometimes loops between search tools until the editor gives up. Which two controls stop that? Select two.

- A. Retry the failed call until it succeeds
- B. Set an explicit step and budget limit on the agent loop
- C. Give one agent every tool in the platform
- D. Raise the temperature for creative variants
- E. Bound each tool call with a timeout and a fallback

### 28. An agent passes a section name the CMS does not recognise and the publish call fails late. Where should that be caught?

- A. Set an explicit CloudWatch Logs retention period
- B. Retry the failed call until it succeeds
- C. Validate tool arguments against a schema before calling
- D. Cache every answer with no expiry

### 29. A publishing tool can unpublish any article in the group although the agent only needs drafts. What limits the risk?

- A. Make the document bucket publicly readable
- B. Store the model API key in an environment variable
- C. Cache every answer with no expiry
- D. Scope the tool role to only the actions it needs

### 30. A live results desk needs a guaranteed token ceiling during a two-hour broadcast. What should be arranged in advance?

- A. Buy Amazon Bedrock provisioned throughput for the model
- B. Call the model on demand through Amazon Bedrock
- C. Use one frontier model for every request
- D. Keep a GPU endpoint running for occasional requests

### 31. A broadcaster needs instant captioning during matches and cheap overnight transcript summaries. Which two capacity patterns fit both? Select two.

- A. Buy Amazon Bedrock provisioned throughput for the model
- B. Keep a GPU endpoint running for occasional requests
- C. Use one frontier model for every request
- D. Run the work as an Amazon Bedrock batch inference job
- E. Retry the failed call until it succeeds

### 32. A published story must trigger tagging, summarisation, and social variants, and new consumers keep appearing. What connects them?

- A. Fan the result out with Amazon SNS
- B. Route domain events through Amazon EventBridge
- C. Move SaaS records in with Amazon AppFlow
- D. Buffer the work in an Amazon SQS queue

### 33. A finished article summary must reach three notification services at once. What delivers one event to all of them?

- A. Return the whole answer from one synchronous call
- B. Buffer the work in an Amazon SQS queue
- C. Fan the result out with Amazon SNS
- D. Move SaaS records in with Amazon AppFlow

### 34. A title-level service needs temporary credentials to invoke one model and read one prefix, with no stored secret. What should it assume?

- A. Store the model API key in an environment variable
- B. Receive partner files over AWS Transfer Family
- C. Give the task an IAM role scoped to the resources it uses
- D. Make the document bucket publicly readable

### 35. Eight titles call the model API directly and nobody can see group-wide spend or revoke a key quickly. What should be introduced?

- A. Put one internal GenAI gateway in front of every model call
- B. Hardcode one model identifier in the application source
- C. Store the model API key in an environment variable
- D. Let each application call the model API directly

### 36. A prompt change must be tested against known stories before it reaches any title. Which two pieces carry that release path? Select two.

- A. Release the assistant through AWS CodePipeline
- B. Let each application call the model API directly
- C. Keep the prompt as a string constant in the application code
- D. Store the model API key in an environment variable
- E. Run a prompt regression suite before promoting a version

### 37. A live blog assistant must show text as it is generated over ordinary HTTP. What fits?

- A. Queue the prompt and return a job identifier for polling
- B. Keep a GPU endpoint running for occasional requests
- C. Return the whole answer from one synchronous call
- D. Stream tokens as server-sent events

### 38. Clients are throttled during a breaking story and their instant retries make it worse. What retry policy should they adopt?

- A. Open a circuit breaker after repeated dependency failures
- B. Retry the failed call until it succeeds
- C. Retry throttled calls with exponential backoff and jitter
- D. Keep a GPU endpoint running for occasional requests

### 39. The image service has failed every call for fifteen minutes while articles keep waiting on it. What should open?

- A. Retry the failed call until it succeeds
- B. Retry throttled calls with exponential backoff and jitter
- C. Return the whole answer from one synchronous call
- D. Open a circuit breaker after repeated dependency failures

### 40. Partner newsrooms need authenticated access with per-partner quotas and request validation. What should expose the assistant?

- A. Serve repeatable responses from Amazon CloudFront
- B. Build the interface with AWS Amplify
- C. Front the model with Amazon API Gateway
- D. Let each application call the model API directly

### 41. Anonymous readers all receive the same generated summary of the day's top story. What removes repeat model calls for them?

- A. Front the model with Amazon API Gateway
- B. Make the document bucket publicly readable
- C. Serve repeatable responses from Amazon CloudFront
- D. Run the request shaping logic at the edge with Lambda@Edge

### 42. Developers rebuild the same SDK plumbing for every new editorial tool. What reduces that effort?

- A. Generate and explain the integration code with Amazon Q Developer
- B. Keep the prompt as a string constant in the application code
- C. Release the assistant through AWS CodePipeline
- D. Run the evaluation suite in AWS CodeBuild

### 43. A publish request takes fourteen seconds, and the delay could be the CMS, the retrieval call, or the model. What shows it?

- A. Query the prompt and response logs with CloudWatch Logs Insights
- B. Trace the request across services with AWS X-Ray
- C. Record control-plane activity in AWS CloudTrail
- D. Set an explicit CloudWatch Logs retention period

---

## Domain 3 — AI Safety, Security, and Governance (20%) — Safety controls, privacy, governance, and responsible AI

### 44. A comment summariser can surface harassment from the comments it reads and can also produce it. What covers both directions?

- A. Apply Amazon Bedrock Guardrails content filters
- B. Lower the temperature for factual answers
- C. Set an explicit CloudWatch Logs retention period
- D. Cap the response length in the request

### 45. A brand assistant must refuse political endorsements and must not repeat a reader's email address. Which two guardrail policies cover that? Select two.

- A. Define denied topics in Amazon Bedrock Guardrails
- B. Cap the response length in the request
- C. Retry the failed call until it succeeds
- D. Enable sensitive-information filters in Amazon Bedrock Guardrails
- E. Cache every answer with no expiry

### 46. Fact-checkers must open the passage behind every claim the assistant makes. What should each answer carry?

- A. Escalate low-confidence or high-impact answers to a person
- B. Return a confidence score with each answer
- C. Require the answer to cite the retrieved passage
- D. Cap the response length in the request

### 47. An editor asks how many subscribers cancelled in March, and the figures sit in a warehouse table. How should the number be produced?

- A. Lower the temperature for factual answers
- B. Constrain the response with a JSON schema
- C. Translate the question into SQL and run it on the database
- D. Return a confidence score with each answer

### 48. A reader pastes text instructing the assistant to publish an unverified correction. What detects that attempt?

- A. Lower the temperature for factual answers
- B. Cap the response length in the request
- C. Screen inputs for instruction override and jailbreak patterns
- D. Retry the failed call until it succeeds

### 49. Security wants a standing hostile-prompt test that runs on every candidate build of the captioning assistant. What should be added to the pipeline?

- A. Have reviewers score a sample against a written rubric
- B. Run the release against a curated golden question set
- C. Run an adversarial prompt suite before each release
- D. Cache every answer with no expiry

### 50. Interview notes are stored for years, and contributor phone numbers must not survive in the stored copy. What should be applied at write time?

- A. Scan the data store with Amazon Macie
- B. Mask direct identifiers before the record is stored
- C. Mask personal data before the prompt is built
- D. Enable sensitive-information filters in Amazon Bedrock Guardrails

### 51. Personal data must be found in the stored archive and masked if it appears in a generated caption. Which two controls cover both points? Select two.

- A. Store the model API key in an environment variable
- B. Apply Amazon Bedrock Guardrails content filters
- C. Enable sensitive-information filters in Amazon Bedrock Guardrails
- D. Detect personal data with Amazon Comprehend
- E. Set an explicit CloudWatch Logs retention period

### 52. Group policy forbids model traffic leaving the private network path even for public content. What provides that?

- A. Call the model through an interface VPC endpoint
- B. Store the model API key in an environment variable
- C. Make the document bucket publicly readable
- D. Serve repeatable responses from Amazon CloudFront

### 53. A reader-facing endpoint keeps receiving malformed probes that consume model quota. What should absorb them at the edge?

- A. Put AWS WAF rules in front of the public endpoint
- B. Make the document bucket publicly readable
- C. Deploy the workload in private subnets
- D. Serve repeatable responses from Amazon CloudFront

### 54. An audit asks who changed the guardrail policy and when the model version was switched. What records both?

- A. Build the operations view in Amazon Managed Grafana
- B. Set an explicit CloudWatch Logs retention period
- C. Turn on Amazon Bedrock model invocation logging
- D. Record control-plane activity in AWS CloudTrail

### 55. A retracted article produced an answer that is now disputed, and the desk needs the corpus version plus the exact request. Which two records allow that? Select two.

- A. Turn on Amazon Bedrock model invocation logging
- B. Store the model API key in an environment variable
- C. Cache every answer with no expiry
- D. Record data lineage in the AWS Glue Data Catalog
- E. Lower the temperature for factual answers

### 56. Reviewers need the intended use and known limits of a captioning model before it ships. What documents that?

- A. Publish a model card with the model version
- B. Constrain the response with a JSON schema
- C. Set an explicit CloudWatch Logs retention period
- D. Compare the candidates with an Amazon Bedrock model evaluation job

### 57. The interface should flag an uncertain answer rather than present a guess as fact. What supports that flag?

- A. Raise the temperature for creative variants
- B. Return a confidence score with each answer
- C. Cap the response length in the request
- D. Cache every answer with no expiry

### 58. Coverage quality for one language edition fell after a model change and nobody noticed for a month. What would have surfaced it?

- A. Detect spend spikes with AWS Cost Anomaly Detection
- B. Alarm on p95 latency and error rate
- C. Report fairness metrics per user segment
- D. Alert when fairness metrics move beyond a band

---

## Domain 4 — Operational Efficiency and Optimization for GenAI Applications (12%) — Token cost, latency, throughput, and observability

### 59. Editorial sessions carry forty earlier turns and the input charge grows with each one. What should happen to the stale turns?

- A. Raise the number of retrieved passages per query
- B. Prune older turns from the context window
- C. Raise the temperature for creative variants
- D. Increase the chunk size so every answer fits in one chunk

### 60. Some captions run to nine sentences when the layout allows two. What bounds spend per call?

- A. Concatenate all fields into one unlabelled text block
- B. Raise the number of retrieved passages per query
- C. Increase the chunk size so every answer fits in one chunk
- D. Cap the response length in the request

### 61. Every request sends the same long style guide before a short brief. What reduces the charge for the repeated prefix?

- A. Cache answers by embedding similarity to earlier questions
- B. Cache every answer with no expiry
- C. Cache the stable prompt prefix with prompt caching
- D. Cache the response under a hash of the normalised request

### 62. A publisher handles a million reader questions a month, most of them near-duplicates of earlier ones. Which two levers cut spend most? Select two.

- A. Send routine prompts to a small model and hard prompts to a large one
- B. Cache answers by embedding similarity to earlier questions
- C. Cache every answer with no expiry
- D. Run a full fine-tune of every model weight
- E. Use one frontier model for every request

### 63. A live blog panel must answer in under two seconds and quality can drop slightly. What is the direct lever?

- A. Retry the failed call until it succeeds
- B. Choose a lower-latency model for the interactive path
- C. Use one frontier model for every request
- D. Run the work as an Amazon Bedrock batch inference job

### 64. Readers abandon a blank panel while a long answer generates, and the most common answers change once a day. Which two changes help? Select two.

- A. Precompute answers for predictable questions on a schedule
- B. Keep a GPU endpoint running for occasional requests
- C. Stream tokens as they are generated
- D. Run the work as an Amazon Bedrock batch inference job
- E. Retry the failed call until it succeeds

### 65. The publisher wants to learn about an assistant outage before readers complain. What detects it proactively?

- A. Record control-plane activity in AWS CloudTrail
- B. Publish a model card with the model version
- C. Set an explicit CloudWatch Logs retention period
- D. Probe the endpoint with CloudWatch Synthetics

### 66. Finance wants spend broken down by title and an alert when it spikes unexpectedly. Which two capabilities provide that? Select two.

- A. Detect spend spikes with AWS Cost Anomaly Detection
- B. Set an explicit CloudWatch Logs retention period
- C. Publish a model card with the model version
- D. Alarm on p95 latency and error rate
- E. Publish token usage as CloudWatch metrics

### 67. The platform runs a steady GPU baseline all year for image captioning. What discounts that predictable capacity?

- A. Cover the steady compute with a Savings Plan
- B. Alert when a tenant crosses its monthly token budget
- C. Detect spend spikes with AWS Cost Anomaly Detection
- D. Keep a GPU endpoint running for occasional requests

---

## Domain 5 — Testing, Validation, and Troubleshooting (11%) — Evaluation, validation, regression testing, and diagnosis

### 68. Answers are accurate but often address a different question than the editor asked. Which score exposes that?

- A. Score how directly the answer addresses the question
- B. Report BERTScore for semantic similarity to the reference
- C. Measure whether the needed passage was retrieved at all
- D. Report ROUGE and BLEU against the reference answers

### 69. Fifty thousand drafts a month must be scored on a rubric, and the score must be defensible. Which two steps make that possible? Select two.

- A. Report ROUGE and BLEU against the reference answers
- B. Score candidate answers with a judge model on a fixed rubric
- C. Raise the temperature for creative variants
- D. Measure whether the needed passage was retrieved at all
- E. Have reviewers score a sample against a written rubric

### 70. Two prompt variants must be compared on real reader traffic over a fortnight. What design answers that?

- A. Split traffic between two model versions and compare outcomes
- B. Have reviewers score a sample against a written rubric
- C. Send a small traffic share to the new prompt and watch the metrics
- D. Mirror production traffic to the new version and compare offline

### 71. A model refresh must not break the two hundred editorial questions the desk already trusts. What should the release replay?

- A. Set an explicit CloudWatch Logs retention period
- B. Have reviewers score a sample against a written rubric
- C. Run the release against a curated golden question set
- D. Cache every answer with no expiry

### 72. The desk wants a release held back automatically when quality drops, plus a readable view of what changed. Which two practices deliver both? Select two.

- A. Cache every answer with no expiry
- B. Diff the new responses against the previous version
- C. Raise the temperature for creative variants
- D. Retry the failed call until it succeeds
- E. Block the release when evaluation drops below the threshold

### 73. The prompt is filled with loosely related passages that dilute the answer. Which retrieval score exposes that?

- A. Report ROUGE and BLEU against the reference answers
- B. Measure whether the needed passage was retrieved at all
- C. Measure whether the retrieved passages were relevant
- D. Measure whether the agent called the right tool with the right arguments

### 74. A research agent cites the wrong source tool and sometimes leaves a task half finished. Which two measurements separate those failures? Select two.

- A. Measure whether the agent called the right tool with the right arguments
- B. Report ROUGE and BLEU against the reference answers
- C. Measure whether the retrieved passages were relevant
- D. Measure the share of agent tasks completed end to end
- E. Report BERTScore for semantic similarity to the reference

### 75. A request with a full transcript now fails outright because it exceeds the model limit. What should be handled first?

- A. Trim or chunk the request when it exceeds the context window
- B. Cache every answer with no expiry
- C. Log the token count and check for truncated prompts
- D. Set an explicit CloudWatch Logs retention period

---

## Answer key and explanations

### Question 1 — A, C

Answers: Put one internal GenAI gateway in front of every model call; Apply Amazon Bedrock Guardrails content filters. A shared gateway centralises access and one guardrail policy applies the same safety rules to every brand. A gateway centralises credentials, quotas, logging, and model routing for all teams. Content filters score and block harmful input and output on the request path. Local study-map skill 1.1 (GenAI Solution Architecture), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Correct. Content filters score and block harmful input and output on the request path. In this case: A shared gateway centralises access and one guardrail policy applies the same safety rules to every brand.
- **B:** Incorrect for this question. Direct calls from every app scatter keys, quotas, and logging across teams. Why the correct answer wins: A shared gateway centralises access and one guardrail policy applies the same safety rules to every brand.
- **C:** Correct. A gateway centralises credentials, quotas, logging, and model routing for all teams. In this case: A shared gateway centralises access and one guardrail policy applies the same safety rules to every brand.
- **D:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: A shared gateway centralises access and one guardrail policy applies the same safety rules to every brand.
- **E:** Incorrect for this question. A hardcoded identifier forces a code change and a release to try another model. Why the correct answer wins: A shared gateway centralises access and one guardrail policy applies the same safety rules to every brand.

### Question 2 — C, E

Answers: Compare the candidates with an Amazon Bedrock model evaluation job; Compare quality per thousand tokens across candidates. A model evaluation job compares candidates on editor-rated prompts and quality per thousand tokens prices the choice. A Bedrock evaluation job scores candidate models on your prompts and metrics before you choose. Quality per unit of spend separates a cheaper model that is good enough from a false economy. Local study-map skill 1.1 (GenAI Solution Architecture), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. A full fine-tune changes all weights, which is expensive and gives one model per task. Why the correct answer wins: A model evaluation job compares candidates on editor-rated prompts and quality per thousand tokens prices the choice.
- **B:** Incorrect for this question. Direct calls from every app scatter keys, quotas, and logging across teams. Why the correct answer wins: A model evaluation job compares candidates on editor-rated prompts and quality per thousand tokens prices the choice.
- **C:** Correct. A Bedrock evaluation job scores candidate models on your prompts and metrics before you choose. In this case: A model evaluation job compares candidates on editor-rated prompts and quality per thousand tokens prices the choice.
- **D:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: A model evaluation job compares candidates on editor-rated prompts and quality per thousand tokens prices the choice.
- **E:** Correct. Quality per unit of spend separates a cheaper model that is good enough from a false economy. In this case: A model evaluation job compares candidates on editor-rated prompts and quality per thousand tokens prices the choice.

### Question 3 — B

Answer: Have reviewers score a sample against a written rubric. A rubric with human scores gives a reference the automatic metrics can be checked against. Local study-map skill 1.2 (Proof-of-Concept Validation), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. Embedding-based similarity credits a correct paraphrase that word overlap misses. Why the correct answer wins: A rubric with human scores gives a reference the automatic metrics can be checked against.
- **B:** Correct. In this case: A rubric with human scores gives a reference the automatic metrics can be checked against.
- **C:** Incorrect for this question. A Bedrock evaluation job scores candidate models on your prompts and metrics before you choose. Why the correct answer wins: A rubric with human scores gives a reference the automatic metrics can be checked against.
- **D:** Incorrect for this question. Overlap metrics are cheap and reward wording that matches the references. Why the correct answer wins: A rubric with human scores gives a reference the automatic metrics can be checked against.

### Question 4 — B

Answer: Right-size the model to the task difficulty. A model no larger than the task needs keeps the per-answer price low for a narrow, repetitive question. A model no larger than the task needs is the largest single cost lever. Local study-map skill 1.3 (Foundation Model Selection and Benchmarking), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. A full fine-tune changes all weights, which is expensive and gives one model per task. Why the correct answer wins: A model no larger than the task needs keeps the per-answer price low for a narrow, repetitive question.
- **B:** Correct. A model no larger than the task needs is the largest single cost lever. In this case: A model no larger than the task needs keeps the per-answer price low for a narrow, repetitive question.
- **C:** Incorrect for this question. A cross-Region inference profile spreads traffic across Regions so a local capacity shortage is absorbed. Why the correct answer wins: A model no larger than the task needs keeps the per-answer price low for a narrow, repetitive question.
- **D:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: A model no larger than the task needs keeps the per-answer price low for a narrow, repetitive question.

### Question 5 — B

Answer: Compare the candidates with an Amazon Bedrock model evaluation job. A Bedrock evaluation job scores every candidate on the same labelled prompts before a choice is made. A Bedrock evaluation job scores candidate models on your prompts and metrics before you choose. Local study-map skill 1.3 (Foundation Model Selection and Benchmarking), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: A Bedrock evaluation job scores every candidate on the same labelled prompts before a choice is made.
- **B:** Correct. A Bedrock evaluation job scores candidate models on your prompts and metrics before you choose. In this case: A Bedrock evaluation job scores every candidate on the same labelled prompts before a choice is made.
- **C:** Incorrect for this question. A full fine-tune changes all weights, which is expensive and gives one model per task. Why the correct answer wins: A Bedrock evaluation job scores every candidate on the same labelled prompts before a choice is made.
- **D:** Incorrect for this question. LoRA trains a small adapter instead of every weight, which cuts cost and keeps the base model reusable. Why the correct answer wins: A Bedrock evaluation job scores every candidate on the same labelled prompts before a choice is made.

### Question 6 — C

Answer: Put the model identifier in AWS AppConfig and switch it without a deploy. A configuration flag changes the model identifier per request path without shipping new application code. Local study-map skill 1.4 (Model Routing and Provider Abstraction), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: A configuration flag changes the model identifier per request path without shipping new application code.
- **B:** Incorrect for this question. Direct calls from every app scatter keys, quotas, and logging across teams. Why the correct answer wins: A configuration flag changes the model identifier per request path without shipping new application code.
- **C:** Correct. In this case: A configuration flag changes the model identifier per request path without shipping new application code.
- **D:** Incorrect for this question. A hardcoded identifier forces a code change and a release to try another model. Why the correct answer wins: A configuration flag changes the model identifier per request path without shipping new application code.

### Question 7 — D

Answer: Route the call through Amazon Bedrock cross-Region inference. A cross-Region inference profile spreads traffic so a local capacity shortage does not fail the request. Local study-map skill 1.5 (Resilience and Cross-Region Inference), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. A key in an environment variable leaks through images, logs, and job definitions. Why the correct answer wins: A cross-Region inference profile spreads traffic so a local capacity shortage does not fail the request.
- **B:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: A cross-Region inference profile spreads traffic so a local capacity shortage does not fail the request.
- **C:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: A cross-Region inference profile spreads traffic so a local capacity shortage does not fail the request.
- **D:** Correct. In this case: A cross-Region inference profile spreads traffic so a local capacity shortage does not fail the request.

### Question 8 — A

Answer: Fall back to a second model when the first is unavailable. A fallback model keeps the feature answering during a Regional degradation, at a stated quality cost. A fallback keeps the feature available when one model or Region degrades. Local study-map skill 1.5 (Resilience and Cross-Region Inference), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Correct. A fallback keeps the feature available when one model or Region degrades. In this case: A fallback model keeps the feature answering during a Regional degradation, at a stated quality cost.
- **B:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: A fallback model keeps the feature answering during a Regional degradation, at a stated quality cost.
- **C:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: A fallback model keeps the feature answering during a Regional degradation, at a stated quality cost.
- **D:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: A fallback model keeps the feature answering during a Regional degradation, at a stated quality cost.

### Question 9 — B

Answer: Distil the large model into a smaller task-specific model. Distillation transfers behaviour to a cheaper model for a narrow, high-volume task. Local study-map skill 1.6 (Customisation Lifecycle and Rollback), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. Direct calls from every app scatter keys, quotas, and logging across teams. Why the correct answer wins: Distillation transfers behaviour to a cheaper model for a narrow, high-volume task.
- **B:** Correct. In this case: Distillation transfers behaviour to a cheaper model for a narrow, high-volume task.
- **C:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: Distillation transfers behaviour to a cheaper model for a narrow, high-volume task.
- **D:** Incorrect for this question. A full fine-tune changes all weights, which is expensive and gives one model per task. Why the correct answer wins: Distillation transfers behaviour to a cheaper model for a narrow, high-volume task.

### Question 10 — C

Answer: Enforce freshness and completeness rules with AWS Glue Data Quality. Rule sets score freshness and completeness and stop the batch before anything is embedded. Local study-map skill 1.7 (Data Validation for Model Inputs), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: Rule sets score freshness and completeness and stop the batch before anything is embedded.
- **B:** Incorrect for this question. Structure failures appear in the logs before a downstream parser breaks. Why the correct answer wins: Rule sets score freshness and completeness and stop the batch before anything is embedded.
- **C:** Correct. In this case: Rule sets score freshness and completeness and stop the batch before anything is embedded.
- **D:** Incorrect for this question. Macie finds sensitive data at rest so the corpus can be cleaned before indexing. Why the correct answer wins: Rule sets score freshness and completeness and stop the batch before anything is embedded.

### Question 11 — D

Answer: Extract entities with Amazon Comprehend before indexing. Entity extraction puts product codes and names in metadata for exact filtering. Local study-map skill 1.7 (Data Validation for Model Inputs), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. A reformatting pass cleans inconsistent headings and units before embedding. Why the correct answer wins: Entity extraction puts product codes and names in metadata for exact filtering.
- **B:** Incorrect for this question. A single blob loses the field boundaries the model needs to answer precisely. Why the correct answer wins: Entity extraction puts product codes and names in metadata for exact filtering.
- **C:** Incorrect for this question. A dialog-shaped request keeps speaker roles and prior turns in the order the model expects. Why the correct answer wins: Entity extraction puts product codes and names in metadata for exact filtering.
- **D:** Correct. In this case: Entity extraction puts product codes and names in metadata for exact filtering.

### Question 12 — D

Answer: Embed text and images with one multimodal model. A shared embedding space lets an image query match a text description. Local study-map skill 1.8 (Multimodal Ingestion and Processing), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. Transcribe turns speech into timestamped text that retrieval can search. Why the correct answer wins: A shared embedding space lets an image query match a text description.
- **B:** Incorrect for this question. Textract returns text and form fields from an image so it can be indexed as text. Why the correct answer wins: A shared embedding space lets an image query match a text description.
- **C:** Incorrect for this question. A Titan embedding model gives a documented dimension and a stable vector space. Why the correct answer wins: A shared embedding space lets an image query match a text description.
- **D:** Correct. In this case: A shared embedding space lets an image query match a text description.

### Question 13 — B

Answer: Format the turns as an alternating conversation structure. A dialog-shaped request keeps speaker roles and prior turns in the order the model expects. Local study-map skill 1.9 (Request Formatting and Enrichment), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: A dialog-shaped request keeps speaker roles and prior turns in the order the model expects.
- **B:** Correct. In this case: A dialog-shaped request keeps speaker roles and prior turns in the order the model expects.
- **C:** Incorrect for this question. A single blob loses the field boundaries the model needs to answer precisely. Why the correct answer wins: A dialog-shaped request keeps speaker roles and prior turns in the order the model expects.
- **D:** Incorrect for this question. A token cap bounds the cost of a runaway answer and the latency of every call. Why the correct answer wins: A dialog-shaped request keeps speaker roles and prior turns in the order the model expects.

### Question 14 — D

Answer: Send the request as the JSON body the model expects. The model API expects the prompt, parameters, and model identifier in one JSON body. Local study-map skill 1.9 (Request Formatting and Enrichment), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. A dialog-shaped request keeps speaker roles and prior turns in the order the model expects. Why the correct answer wins: The model API expects the prompt, parameters, and model identifier in one JSON body.
- **B:** Incorrect for this question. A single blob loses the field boundaries the model needs to answer precisely. Why the correct answer wins: The model API expects the prompt, parameters, and model identifier in one JSON body.
- **C:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: The model API expects the prompt, parameters, and model identifier in one JSON body.
- **D:** Correct. In this case: The model API expects the prompt, parameters, and model identifier in one JSON body.

### Question 15 — D

Answer: Index the vectors in Amazon OpenSearch Service with k-NN search. OpenSearch combines vector search with the filtering and sharding of a search engine. Local study-map skill 1.10 (Vector Store Architecture), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. DocumentDB stores JSON documents in their original shape for retrieval and display. Why the correct answer wins: OpenSearch combines vector search with the filtering and sharding of a search engine.
- **B:** Incorrect for this question. Neptune answers relationship traversals that a similarity search cannot express. Why the correct answer wins: OpenSearch combines vector search with the filtering and sharding of a search engine.
- **C:** Incorrect for this question. DynamoDB serves key lookups fast and can hold vectors beside their metadata for small corpora. Why the correct answer wins: OpenSearch combines vector search with the filtering and sharding of a search engine.
- **D:** Correct. In this case: OpenSearch combines vector search with the filtering and sharding of a search engine.

### Question 16 — B

Answer: Filter the search by document metadata before the similarity ranking. A metadata filter removes out-of-scope documents so the ranking only sees eligible chunks. Local study-map skill 1.11 (Metadata Frameworks and Index Maintenance), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. A threshold keeps marginal passages out of the prompt that would only add noise. Why the correct answer wins: A metadata filter removes out-of-scope documents so the ranking only sees eligible chunks.
- **B:** Correct. In this case: A metadata filter removes out-of-scope documents so the ranking only sees eligible chunks.
- **C:** Incorrect for this question. Vectors from two different models are not comparable, so the whole index must be rebuilt. Why the correct answer wins: A metadata filter removes out-of-scope documents so the ranking only sees eligible chunks.
- **D:** Incorrect for this question. More passages raise recall and also lengthen the prompt and the cost per call. Why the correct answer wins: A metadata filter removes out-of-scope documents so the ranking only sees eligible chunks.

### Question 17 — D

Answer: Update the index incrementally when a source document changes. Incremental updates keep the index current without re-embedding the whole corpus. Local study-map skill 1.11 (Metadata Frameworks and Index Maintenance), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: Incremental updates keep the index current without re-embedding the whole corpus.
- **B:** Incorrect for this question. Scheduled rebuilds are simple and leave a window in which answers lag the source. Why the correct answer wins: Incremental updates keep the index current without re-embedding the whole corpus.
- **C:** Incorrect for this question. Vectors from two different models are not comparable, so the whole index must be rebuilt. Why the correct answer wins: Incremental updates keep the index current without re-embedding the whole corpus.
- **D:** Correct. In this case: Incremental updates keep the index current without re-embedding the whole corpus.

### Question 18 — B

Answer: Split where the embedding similarity between sentences drops. Semantic splitting places boundaries at topic shifts rather than at a character count. Local study-map skill 1.12 (Chunking and Embedding Strategy), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. Mixing vector spaces silently breaks similarity, because distances no longer mean the same thing. Why the correct answer wins: Semantic splitting places boundaries at topic shifts rather than at a character count.
- **B:** Correct. In this case: Semantic splitting places boundaries at topic shifts rather than at a character count.
- **C:** Incorrect for this question. Fixed windows are predictable and cheap, and overlap preserves text that straddles a boundary. Why the correct answer wins: Semantic splitting places boundaries at topic shifts rather than at a character count.
- **D:** Incorrect for this question. Larger chunks carry more context but dilute the embedding and crowd the prompt window. Why the correct answer wins: Semantic splitting places boundaries at topic shifts rather than at a character count.

### Question 19 — C, E

Answers: Combine keyword and vector retrieval and merge the ranked lists; Drop passages below a relevance score threshold. Hybrid retrieval catches exact identifiers and a threshold removes passages too weak to matter. Hybrid retrieval catches exact identifiers that a vector search alone can miss. A threshold keeps marginal passages out of the prompt that would only add noise. Local study-map skill 1.13 (Hybrid Retrieval and Reranking), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. More passages raise recall and also lengthen the prompt and the cost per call. Why the correct answer wins: Hybrid retrieval catches exact identifiers and a threshold removes passages too weak to matter.
- **B:** Incorrect for this question. Mixing vector spaces silently breaks similarity, because distances no longer mean the same thing. Why the correct answer wins: Hybrid retrieval catches exact identifiers and a threshold removes passages too weak to matter.
- **C:** Correct. A threshold keeps marginal passages out of the prompt that would only add noise. In this case: Hybrid retrieval catches exact identifiers and a threshold removes passages too weak to matter.
- **D:** Incorrect for this question. Larger chunks carry more context but dilute the embedding and crowd the prompt window. Why the correct answer wins: Hybrid retrieval catches exact identifiers and a threshold removes passages too weak to matter.
- **E:** Correct. Hybrid retrieval catches exact identifiers that a vector search alone can miss. In this case: Hybrid retrieval catches exact identifiers and a threshold removes passages too weak to matter.

### Question 20 — A

Answer: Rerank the retrieved passages with an Amazon Bedrock reranker. A reranker scores the shortlist against the query and lifts precision before the prompt is built. Local study-map skill 1.13 (Hybrid Retrieval and Reranking), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Correct. In this case: A reranker scores the shortlist against the query and lifts precision before the prompt is built.
- **B:** Incorrect for this question. Expansion bridges vocabulary gaps between how users ask and how documents are written. Why the correct answer wins: A reranker scores the shortlist against the query and lifts precision before the prompt is built.
- **C:** Incorrect for this question. Semantic splitting places boundaries at topic shifts rather than at a character count. Why the correct answer wins: A reranker scores the shortlist against the query and lifts precision before the prompt is built.
- **D:** Incorrect for this question. More passages raise recall and also lengthen the prompt and the cost per call. Why the correct answer wins: A reranker scores the shortlist against the query and lifts precision before the prompt is built.

### Question 21 — D

Answer: Break a multi-part question into separate retrievals. Decomposition retrieves evidence for each sub-question instead of averaging them into one query. Local study-map skill 1.14 (Query Transformation and Handling), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. Expansion bridges vocabulary gaps between how users ask and how documents are written. Why the correct answer wins: Decomposition retrieves evidence for each sub-question instead of averaging them into one query.
- **B:** Incorrect for this question. More passages raise recall and also lengthen the prompt and the cost per call. Why the correct answer wins: Decomposition retrieves evidence for each sub-question instead of averaging them into one query.
- **C:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: Decomposition retrieves evidence for each sub-question instead of averaging them into one query.
- **D:** Correct. In this case: Decomposition retrieves evidence for each sub-question instead of averaging them into one query.

### Question 22 — A

Answer: Put the role, tone, and boundaries in the system prompt. The system prompt sets behaviour once and outranks stray instructions in the user turn. Local study-map skill 1.15 (Prompt Engineering and Governance), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Correct. In this case: The system prompt sets behaviour once and outranks stray instructions in the user turn.
- **B:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: The system prompt sets behaviour once and outranks stray instructions in the user turn.
- **C:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: The system prompt sets behaviour once and outranks stray instructions in the user turn.
- **D:** Incorrect for this question. A token cap bounds the cost of a runaway answer and the latency of every call. Why the correct answer wins: The system prompt sets behaviour once and outranks stray instructions in the user turn.

### Question 23 — B

Answer: Add worked examples of the expected answer shape. Examples show the model the output contract that instructions alone leave ambiguous. Local study-map skill 1.15 (Prompt Engineering and Governance), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: Examples show the model the output contract that instructions alone leave ambiguous.
- **B:** Correct. In this case: Examples show the model the output contract that instructions alone leave ambiguous.
- **C:** Incorrect for this question. A token cap bounds the cost of a runaway answer and the latency of every call. Why the correct answer wins: Examples show the model the output contract that instructions alone leave ambiguous.
- **D:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: Examples show the model the output contract that instructions alone leave ambiguous.

### Question 24 — A

Answer: Keep conversation and task memory in Amazon DynamoDB. DynamoDB gives the agent a durable per-session store keyed by session identifier. Local study-map skill 2.1 (Agent Memory and State), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Correct. In this case: DynamoDB gives the agent a durable per-session store keyed by session identifier.
- **B:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: DynamoDB gives the agent a durable per-session store keyed by session identifier.
- **C:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: DynamoDB gives the agent a durable per-session store keyed by session identifier.
- **D:** Incorrect for this question. Prompt-only memory forgets everything the moment the context window is trimmed. Why the correct answer wins: DynamoDB gives the agent a durable per-session store keyed by session identifier.

### Question 25 — D

Answer: Summarise the conversation before adding more turns. A running summary keeps long sessions inside the window at low token cost. Local study-map skill 2.1 (Agent Memory and State), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. Larger chunks carry more context but dilute the embedding and crowd the prompt window. Why the correct answer wins: A running summary keeps long sessions inside the window at low token cost.
- **B:** Incorrect for this question. Prompt-only memory forgets everything the moment the context window is trimmed. Why the correct answer wins: A running summary keeps long sessions inside the window at low token cost.
- **C:** Incorrect for this question. A single blob loses the field boundaries the model needs to answer precisely. Why the correct answer wins: A running summary keeps long sessions inside the window at low token cost.
- **D:** Correct. In this case: A running summary keeps long sessions inside the window at low token cost.

### Question 26 — B

Answer: Build the agent with Strands Agents. Strands gives an open-source agent loop with tools, memory, and model-agnostic wiring. Local study-map skill 2.2 (Agent Orchestration Patterns), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: Strands gives an open-source agent loop with tools, memory, and model-agnostic wiring.
- **B:** Correct. In this case: Strands gives an open-source agent loop with tools, memory, and model-agnostic wiring.
- **C:** Incorrect for this question. One agent with every tool makes tool choice ambiguous and permissions broad. Why the correct answer wins: Strands gives an open-source agent loop with tools, memory, and model-agnostic wiring.
- **D:** Incorrect for this question. A synchronous call is simplest and makes the user wait for the final token. Why the correct answer wins: Strands gives an open-source agent loop with tools, memory, and model-agnostic wiring.

### Question 27 — B, E

Answers: Set an explicit step and budget limit on the agent loop; Bound each tool call with a timeout and a fallback. A hard limit ends a non-converging loop and a timeout keeps one slow tool from stalling the turn. A hard limit stops a loop that would otherwise consume tokens without converging. A timeout keeps one slow dependency from stalling the whole agent turn. Local study-map skill 2.2 (Agent Orchestration Patterns), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: A hard limit ends a non-converging loop and a timeout keeps one slow tool from stalling the turn.
- **B:** Correct. A hard limit stops a loop that would otherwise consume tokens without converging. In this case: A hard limit ends a non-converging loop and a timeout keeps one slow tool from stalling the turn.
- **C:** Incorrect for this question. One agent with every tool makes tool choice ambiguous and permissions broad. Why the correct answer wins: A hard limit ends a non-converging loop and a timeout keeps one slow tool from stalling the turn.
- **D:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: A hard limit ends a non-converging loop and a timeout keeps one slow tool from stalling the turn.
- **E:** Correct. A timeout keeps one slow dependency from stalling the whole agent turn. In this case: A hard limit ends a non-converging loop and a timeout keeps one slow tool from stalling the turn.

### Question 28 — C

Answer: Validate tool arguments against a schema before calling. Schema validation rejects a malformed argument instead of sending it to the system of record. Local study-map skill 2.3 (Tool Reliability and Safeguards), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: Schema validation rejects a malformed argument instead of sending it to the system of record.
- **B:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: Schema validation rejects a malformed argument instead of sending it to the system of record.
- **C:** Correct. In this case: Schema validation rejects a malformed argument instead of sending it to the system of record.
- **D:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: Schema validation rejects a malformed argument instead of sending it to the system of record.

### Question 29 — D

Answer: Scope the tool role to only the actions it needs. A narrow role limits what a misdirected agent call can actually change. Local study-map skill 2.3 (Tool Reliability and Safeguards), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. A public bucket exposes the corpus to everyone the index was meant to constrain. Why the correct answer wins: A narrow role limits what a misdirected agent call can actually change.
- **B:** Incorrect for this question. A key in an environment variable leaks through images, logs, and job definitions. Why the correct answer wins: A narrow role limits what a misdirected agent call can actually change.
- **C:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: A narrow role limits what a misdirected agent call can actually change.
- **D:** Correct. In this case: A narrow role limits what a misdirected agent call can actually change.

### Question 30 — A

Answer: Buy Amazon Bedrock provisioned throughput for the model. Provisioned throughput reserves model units and gives a predictable token-per-minute ceiling. Local study-map skill 2.4 (Foundation Model Deployment and Capacity), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Correct. In this case: Provisioned throughput reserves model units and gives a predictable token-per-minute ceiling.
- **B:** Incorrect for this question. On-demand Bedrock inference bills per token with no committed capacity, which suits spiky or unproven demand. Why the correct answer wins: Provisioned throughput reserves model units and gives a predictable token-per-minute ceiling.
- **C:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: Provisioned throughput reserves model units and gives a predictable token-per-minute ceiling.
- **D:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: Provisioned throughput reserves model units and gives a predictable token-per-minute ceiling.

### Question 31 — A, D

Answers: Buy Amazon Bedrock provisioned throughput for the model; Run the work as an Amazon Bedrock batch inference job. Provisioned throughput guarantees the live path and batch inference prices the offline volume lower. Provisioned throughput reserves model units and gives a predictable token-per-minute ceiling. Batch inference trades turnaround time for a lower price on large offline volumes. Local study-map skill 2.4 (Foundation Model Deployment and Capacity), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Correct. Provisioned throughput reserves model units and gives a predictable token-per-minute ceiling. In this case: Provisioned throughput guarantees the live path and batch inference prices the offline volume lower.
- **B:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: Provisioned throughput guarantees the live path and batch inference prices the offline volume lower.
- **C:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: Provisioned throughput guarantees the live path and batch inference prices the offline volume lower.
- **D:** Correct. Batch inference trades turnaround time for a lower price on large offline volumes. In this case: Provisioned throughput guarantees the live path and batch inference prices the offline volume lower.
- **E:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: Provisioned throughput guarantees the live path and batch inference prices the offline volume lower.

### Question 32 — B

Answer: Route domain events through Amazon EventBridge. EventBridge decouples producers from the GenAI consumer with rules and filtering. Local study-map skill 2.5 (Enterprise Integration Patterns), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. SNS delivers one event to many subscribers without the caller tracking them. Why the correct answer wins: EventBridge decouples producers from the GenAI consumer with rules and filtering.
- **B:** Correct. In this case: EventBridge decouples producers from the GenAI consumer with rules and filtering.
- **C:** Incorrect for this question. AppFlow copies data from supported SaaS sources without custom connectors. Why the correct answer wins: EventBridge decouples producers from the GenAI consumer with rules and filtering.
- **D:** Incorrect for this question. A queue absorbs bursts and lets a worker retry a failed model call. Why the correct answer wins: EventBridge decouples producers from the GenAI consumer with rules and filtering.

### Question 33 — C

Answer: Fan the result out with Amazon SNS. SNS delivers one event to many subscribers without the caller tracking them. Local study-map skill 2.5 (Enterprise Integration Patterns), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. A synchronous call is simplest and makes the user wait for the final token. Why the correct answer wins: SNS delivers one event to many subscribers without the caller tracking them.
- **B:** Incorrect for this question. A queue absorbs bursts and lets a worker retry a failed model call. Why the correct answer wins: SNS delivers one event to many subscribers without the caller tracking them.
- **C:** Correct. In this case: SNS delivers one event to many subscribers without the caller tracking them.
- **D:** Incorrect for this question. AppFlow copies data from supported SaaS sources without custom connectors. Why the correct answer wins: SNS delivers one event to many subscribers without the caller tracking them.

### Question 34 — C

Answer: Give the task an IAM role scoped to the resources it uses. A scoped role issues temporary credentials with only the needed permissions. Local study-map skill 2.6 (Identity for Model Access), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. A key in an environment variable leaks through images, logs, and job definitions. Why the correct answer wins: A scoped role issues temporary credentials with only the needed permissions.
- **B:** Incorrect for this question. Transfer Family accepts SFTP uploads into S3 without a server to run. Why the correct answer wins: A scoped role issues temporary credentials with only the needed permissions.
- **C:** Correct. In this case: A scoped role issues temporary credentials with only the needed permissions.
- **D:** Incorrect for this question. A public bucket exposes the corpus to everyone the index was meant to constrain. Why the correct answer wins: A scoped role issues temporary credentials with only the needed permissions.

### Question 35 — A

Answer: Put one internal GenAI gateway in front of every model call. A gateway centralises credentials, quotas, logging, and model routing for all teams. Local study-map skill 2.7 (CI/CD and GenAI Gateway), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Correct. In this case: A gateway centralises credentials, quotas, logging, and model routing for all teams.
- **B:** Incorrect for this question. A hardcoded identifier forces a code change and a release to try another model. Why the correct answer wins: A gateway centralises credentials, quotas, logging, and model routing for all teams.
- **C:** Incorrect for this question. A key in an environment variable leaks through images, logs, and job definitions. Why the correct answer wins: A gateway centralises credentials, quotas, logging, and model routing for all teams.
- **D:** Incorrect for this question. Direct calls from every app scatter keys, quotas, and logging across teams. Why the correct answer wins: A gateway centralises credentials, quotas, logging, and model routing for all teams.

### Question 36 — A, E

Answers: Release the assistant through AWS CodePipeline; Run a prompt regression suite before promoting a version. A pipeline ties the stages together and the regression suite proves the prompt before deployment. A pipeline ties source, build, test, and deploy into one auditable flow. A fixed suite of prompts and expected properties catches a wording change that breaks behaviour. Local study-map skill 2.7 (CI/CD and GenAI Gateway), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Correct. A pipeline ties source, build, test, and deploy into one auditable flow. In this case: A pipeline ties the stages together and the regression suite proves the prompt before deployment.
- **B:** Incorrect for this question. Direct calls from every app scatter keys, quotas, and logging across teams. Why the correct answer wins: A pipeline ties the stages together and the regression suite proves the prompt before deployment.
- **C:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: A pipeline ties the stages together and the regression suite proves the prompt before deployment.
- **D:** Incorrect for this question. A key in an environment variable leaks through images, logs, and job definitions. Why the correct answer wins: A pipeline ties the stages together and the regression suite proves the prompt before deployment.
- **E:** Correct. A fixed suite of prompts and expected properties catches a wording change that breaks behaviour. In this case: A pipeline ties the stages together and the regression suite proves the prompt before deployment.

### Question 37 — D

Answer: Stream tokens as server-sent events. Server-sent events deliver incremental text over ordinary HTTP. Local study-map skill 2.8 (Streaming and Asynchronous APIs), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. Asynchronous processing suits long generations that outlast an API timeout. Why the correct answer wins: Server-sent events deliver incremental text over ordinary HTTP.
- **B:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: Server-sent events deliver incremental text over ordinary HTTP.
- **C:** Incorrect for this question. A synchronous call is simplest and makes the user wait for the final token. Why the correct answer wins: Server-sent events deliver incremental text over ordinary HTTP.
- **D:** Correct. In this case: Server-sent events deliver incremental text over ordinary HTTP.

### Question 38 — C

Answer: Retry throttled calls with exponential backoff and jitter. Backoff with jitter spreads retries so a throttled client does not stampede the service. Local study-map skill 2.9 (API Resilience and Backoff), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. A circuit breaker stops sending traffic to a dependency that is already failing. Why the correct answer wins: Backoff with jitter spreads retries so a throttled client does not stampede the service.
- **B:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: Backoff with jitter spreads retries so a throttled client does not stampede the service.
- **C:** Correct. In this case: Backoff with jitter spreads retries so a throttled client does not stampede the service.
- **D:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: Backoff with jitter spreads retries so a throttled client does not stampede the service.

### Question 39 — D

Answer: Open a circuit breaker after repeated dependency failures. A circuit breaker stops sending traffic to a dependency that is already failing. Local study-map skill 2.9 (API Resilience and Backoff), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: A circuit breaker stops sending traffic to a dependency that is already failing.
- **B:** Incorrect for this question. Backoff with jitter spreads retries so a throttled client does not stampede the service. Why the correct answer wins: A circuit breaker stops sending traffic to a dependency that is already failing.
- **C:** Incorrect for this question. A synchronous call is simplest and makes the user wait for the final token. Why the correct answer wins: A circuit breaker stops sending traffic to a dependency that is already failing.
- **D:** Correct. In this case: A circuit breaker stops sending traffic to a dependency that is already failing.

### Question 40 — C

Answer: Front the model with Amazon API Gateway. API Gateway adds authentication, throttling, request validation, and streaming to the model call. Local study-map skill 2.10 (Application Integration and Low Code), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. An edge cache answers identical requests without reaching the model. Why the correct answer wins: API Gateway adds authentication, throttling, request validation, and streaming to the model call.
- **B:** Incorrect for this question. Amplify supplies declarative UI and hosting for the client that talks to the assistant. Why the correct answer wins: API Gateway adds authentication, throttling, request validation, and streaming to the model call.
- **C:** Correct. In this case: API Gateway adds authentication, throttling, request validation, and streaming to the model call.
- **D:** Incorrect for this question. Direct calls from every app scatter keys, quotas, and logging across teams. Why the correct answer wins: API Gateway adds authentication, throttling, request validation, and streaming to the model call.

### Question 41 — C

Answer: Serve repeatable responses from Amazon CloudFront. An edge cache answers identical requests without reaching the model. Local study-map skill 2.10 (Application Integration and Low Code), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. API Gateway adds authentication, throttling, request validation, and streaming to the model call. Why the correct answer wins: An edge cache answers identical requests without reaching the model.
- **B:** Incorrect for this question. A public bucket exposes the corpus to everyone the index was meant to constrain. Why the correct answer wins: An edge cache answers identical requests without reaching the model.
- **C:** Correct. In this case: An edge cache answers identical requests without reaching the model.
- **D:** Incorrect for this question. Edge logic trims, redacts, or routes a request before it crosses to the model Region. Why the correct answer wins: An edge cache answers identical requests without reaching the model.

### Question 42 — A

Answer: Generate and explain the integration code with Amazon Q Developer. Q Developer drafts and explains SDK calls inside the editor, which speeds up the plumbing. Local study-map skill 2.11 (Developer Productivity Tooling), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Correct. In this case: Q Developer drafts and explains SDK calls inside the editor, which speeds up the plumbing.
- **B:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: Q Developer drafts and explains SDK calls inside the editor, which speeds up the plumbing.
- **C:** Incorrect for this question. A pipeline ties source, build, test, and deploy into one auditable flow. Why the correct answer wins: Q Developer drafts and explains SDK calls inside the editor, which speeds up the plumbing.
- **D:** Incorrect for this question. CodeBuild runs the tests and quality gates as part of the release. Why the correct answer wins: Q Developer drafts and explains SDK calls inside the editor, which speeds up the plumbing.

### Question 43 — B

Answer: Trace the request across services with AWS X-Ray. A trace shows which hop in the chain added the latency. Local study-map skill 2.12 (Integration Troubleshooting), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. Logs Insights correlates a spike in errors with the prompts that caused it. Why the correct answer wins: A trace shows which hop in the chain added the latency.
- **B:** Correct. In this case: A trace shows which hop in the chain added the latency.
- **C:** Incorrect for this question. CloudTrail records who changed models, keys, and guardrails. Why the correct answer wins: A trace shows which hop in the chain added the latency.
- **D:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: A trace shows which hop in the chain added the latency.

### Question 44 — A

Answer: Apply Amazon Bedrock Guardrails content filters. Content filters score and block harmful input and output on the request path. Local study-map skill 3.1 (Content Safety Controls), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Correct. In this case: Content filters score and block harmful input and output on the request path.
- **B:** Incorrect for this question. Low temperature narrows sampling so repeatable factual answers stay stable. Why the correct answer wins: Content filters score and block harmful input and output on the request path.
- **C:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: Content filters score and block harmful input and output on the request path.
- **D:** Incorrect for this question. A token cap bounds the cost of a runaway answer and the latency of every call. Why the correct answer wins: Content filters score and block harmful input and output on the request path.

### Question 45 — A, D

Answers: Define denied topics in Amazon Bedrock Guardrails; Enable sensitive-information filters in Amazon Bedrock Guardrails. Denied topics refuse the ruled-out subjects and the sensitive-information filter masks personal data. Denied topics refuse the subject areas the business has ruled out. PII filters detect and mask personal data in prompts and responses. Local study-map skill 3.1 (Content Safety Controls), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Correct. Denied topics refuse the subject areas the business has ruled out. In this case: Denied topics refuse the ruled-out subjects and the sensitive-information filter masks personal data.
- **B:** Incorrect for this question. A token cap bounds the cost of a runaway answer and the latency of every call. Why the correct answer wins: Denied topics refuse the ruled-out subjects and the sensitive-information filter masks personal data.
- **C:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: Denied topics refuse the ruled-out subjects and the sensitive-information filter masks personal data.
- **D:** Correct. PII filters detect and mask personal data in prompts and responses. In this case: Denied topics refuse the ruled-out subjects and the sensitive-information filter masks personal data.
- **E:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: Denied topics refuse the ruled-out subjects and the sensitive-information filter masks personal data.

### Question 46 — C

Answer: Require the answer to cite the retrieved passage. A citation makes each claim traceable to a source the reader can check. Local study-map skill 3.2 (Grounding and Hallucination Reduction), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. An escalation path keeps consequential answers with a human owner. Why the correct answer wins: A citation makes each claim traceable to a source the reader can check.
- **B:** Incorrect for this question. A score lets the interface route low-confidence answers to a human. Why the correct answer wins: A citation makes each claim traceable to a source the reader can check.
- **C:** Correct. In this case: A citation makes each claim traceable to a source the reader can check.
- **D:** Incorrect for this question. A token cap bounds the cost of a runaway answer and the latency of every call. Why the correct answer wins: A citation makes each claim traceable to a source the reader can check.

### Question 47 — C

Answer: Translate the question into SQL and run it on the database. Deterministic query generation avoids asking a model to compute figures from memory. Local study-map skill 3.2 (Grounding and Hallucination Reduction), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. Low temperature narrows sampling so repeatable factual answers stay stable. Why the correct answer wins: Deterministic query generation avoids asking a model to compute figures from memory.
- **B:** Incorrect for this question. A schema makes the output machine-parseable and rejects prose that breaks the contract. Why the correct answer wins: Deterministic query generation avoids asking a model to compute figures from memory.
- **C:** Correct. In this case: Deterministic query generation avoids asking a model to compute figures from memory.
- **D:** Incorrect for this question. A score lets the interface route low-confidence answers to a human. Why the correct answer wins: Deterministic query generation avoids asking a model to compute figures from memory.

### Question 48 — C

Answer: Screen inputs for instruction override and jailbreak patterns. A pre-filter catches text that tries to replace the system instruction. Local study-map skill 3.3 (Prompt Injection Defence), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. Low temperature narrows sampling so repeatable factual answers stay stable. Why the correct answer wins: A pre-filter catches text that tries to replace the system instruction.
- **B:** Incorrect for this question. A token cap bounds the cost of a runaway answer and the latency of every call. Why the correct answer wins: A pre-filter catches text that tries to replace the system instruction.
- **C:** Correct. In this case: A pre-filter catches text that tries to replace the system instruction.
- **D:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: A pre-filter catches text that tries to replace the system instruction.

### Question 49 — C

Answer: Run an adversarial prompt suite before each release. A hostile test set finds regressions in refusal behaviour before users do. Local study-map skill 3.3 (Prompt Injection Defence), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. A rubric with human scores gives a reference the automatic metrics can be checked against. Why the correct answer wins: A hostile test set finds regressions in refusal behaviour before users do.
- **B:** Incorrect for this question. A golden set with known answers catches a regression the moment it ships. Why the correct answer wins: A hostile test set finds regressions in refusal behaviour before users do.
- **C:** Correct. In this case: A hostile test set finds regressions in refusal behaviour before users do.
- **D:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: A hostile test set finds regressions in refusal behaviour before users do.

### Question 50 — B

Answer: Mask direct identifiers before the record is stored. Masking removes names and account numbers while keeping the record usable. Local study-map skill 3.4 (Privacy and PII Protection), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. Macie finds sensitive data at rest so the corpus can be cleaned before indexing. Why the correct answer wins: Masking removes names and account numbers while keeping the record usable.
- **B:** Correct. In this case: Masking removes names and account numbers while keeping the record usable.
- **C:** Incorrect for this question. Masking at the boundary keeps personal data out of the model request entirely. Why the correct answer wins: Masking removes names and account numbers while keeping the record usable.
- **D:** Incorrect for this question. PII filters detect and mask personal data in prompts and responses. Why the correct answer wins: Masking removes names and account numbers while keeping the record usable.

### Question 51 — C, D

Answers: Detect personal data with Amazon Comprehend; Enable sensitive-information filters in Amazon Bedrock Guardrails. Comprehend identifies the entities in storage and the sensitive-information filter masks what reaches the reader. Comprehend identifies entities and PII so they can be masked before the model sees them. PII filters detect and mask personal data in prompts and responses. Local study-map skill 3.4 (Privacy and PII Protection), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. A key in an environment variable leaks through images, logs, and job definitions. Why the correct answer wins: Comprehend identifies the entities in storage and the sensitive-information filter masks what reaches the reader.
- **B:** Incorrect for this question. Content filters score and block harmful input and output on the request path. Why the correct answer wins: Comprehend identifies the entities in storage and the sensitive-information filter masks what reaches the reader.
- **C:** Correct. PII filters detect and mask personal data in prompts and responses. In this case: Comprehend identifies the entities in storage and the sensitive-information filter masks what reaches the reader.
- **D:** Correct. Comprehend identifies entities and PII so they can be masked before the model sees them. In this case: Comprehend identifies the entities in storage and the sensitive-information filter masks what reaches the reader.
- **E:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: Comprehend identifies the entities in storage and the sensitive-information filter masks what reaches the reader.

### Question 52 — A

Answer: Call the model through an interface VPC endpoint. A private endpoint keeps model traffic off the public internet. Local study-map skill 3.5 (Network and Data Isolation), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Correct. In this case: A private endpoint keeps model traffic off the public internet.
- **B:** Incorrect for this question. A key in an environment variable leaks through images, logs, and job definitions. Why the correct answer wins: A private endpoint keeps model traffic off the public internet.
- **C:** Incorrect for this question. A public bucket exposes the corpus to everyone the index was meant to constrain. Why the correct answer wins: A private endpoint keeps model traffic off the public internet.
- **D:** Incorrect for this question. An edge cache answers identical requests without reaching the model. Why the correct answer wins: A private endpoint keeps model traffic off the public internet.

### Question 53 — A

Answer: Put AWS WAF rules in front of the public endpoint. WAF blocks known bad request patterns before they consume model capacity. Local study-map skill 3.5 (Network and Data Isolation), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Correct. In this case: WAF blocks known bad request patterns before they consume model capacity.
- **B:** Incorrect for this question. A public bucket exposes the corpus to everyone the index was meant to constrain. Why the correct answer wins: WAF blocks known bad request patterns before they consume model capacity.
- **C:** Incorrect for this question. Private subnets remove inbound internet routing from the compute tier. Why the correct answer wins: WAF blocks known bad request patterns before they consume model capacity.
- **D:** Incorrect for this question. An edge cache answers identical requests without reaching the model. Why the correct answer wins: WAF blocks known bad request patterns before they consume model capacity.

### Question 54 — D

Answer: Record control-plane activity in AWS CloudTrail. CloudTrail records who changed models, keys, and guardrails. Local study-map skill 3.6 (Governance, Lineage, and Audit), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. Grafana combines model, infrastructure, and business metrics on one screen. Why the correct answer wins: CloudTrail records who changed models, keys, and guardrails.
- **B:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: CloudTrail records who changed models, keys, and guardrails.
- **C:** Incorrect for this question. Invocation logs capture the request, the response, and the token counts. Why the correct answer wins: CloudTrail records who changed models, keys, and guardrails.
- **D:** Correct. In this case: CloudTrail records who changed models, keys, and guardrails.

### Question 55 — A, D

Answers: Turn on Amazon Bedrock model invocation logging; Record data lineage in the AWS Glue Data Catalog. Lineage ties the answer to its corpus version and invocation logs hold the request and the response. Invocation logs capture the request, the response, and the token counts. Lineage shows which corpus and version produced an answer. Local study-map skill 3.6 (Governance, Lineage, and Audit), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Correct. Invocation logs capture the request, the response, and the token counts. In this case: Lineage ties the answer to its corpus version and invocation logs hold the request and the response.
- **B:** Incorrect for this question. A key in an environment variable leaks through images, logs, and job definitions. Why the correct answer wins: Lineage ties the answer to its corpus version and invocation logs hold the request and the response.
- **C:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: Lineage ties the answer to its corpus version and invocation logs hold the request and the response.
- **D:** Correct. Lineage shows which corpus and version produced an answer. In this case: Lineage ties the answer to its corpus version and invocation logs hold the request and the response.
- **E:** Incorrect for this question. Low temperature narrows sampling so repeatable factual answers stay stable. Why the correct answer wins: Lineage ties the answer to its corpus version and invocation logs hold the request and the response.

### Question 56 — A

Answer: Publish a model card with the model version. A model card documents intended use and known limits for reviewers. Local study-map skill 3.7 (Responsible AI and Transparency), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Correct. In this case: A model card documents intended use and known limits for reviewers.
- **B:** Incorrect for this question. A schema makes the output machine-parseable and rejects prose that breaks the contract. Why the correct answer wins: A model card documents intended use and known limits for reviewers.
- **C:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: A model card documents intended use and known limits for reviewers.
- **D:** Incorrect for this question. A Bedrock evaluation job scores candidate models on your prompts and metrics before you choose. Why the correct answer wins: A model card documents intended use and known limits for reviewers.

### Question 57 — B

Answer: Return a confidence score with each answer. A score lets the interface route low-confidence answers to a human. Local study-map skill 3.7 (Responsible AI and Transparency), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: A score lets the interface route low-confidence answers to a human.
- **B:** Correct. In this case: A score lets the interface route low-confidence answers to a human.
- **C:** Incorrect for this question. A token cap bounds the cost of a runaway answer and the latency of every call. Why the correct answer wins: A score lets the interface route low-confidence answers to a human.
- **D:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: A score lets the interface route low-confidence answers to a human.

### Question 58 — D

Answer: Alert when fairness metrics move beyond a band. A drift alert catches a fairness regression after a model or prompt change. Local study-map skill 3.8 (Fairness and Compliance Monitoring), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. Anomaly detection finds an unexpected token bill without a fixed threshold. Why the correct answer wins: A drift alert catches a fairness regression after a model or prompt change.
- **B:** Incorrect for this question. A latency alarm fires on the symptom users feel. Why the correct answer wins: A drift alert catches a fairness regression after a model or prompt change.
- **C:** Incorrect for this question. Segment metrics expose a quality gap that an overall average hides. Why the correct answer wins: A drift alert catches a fairness regression after a model or prompt change.
- **D:** Correct. In this case: A drift alert catches a fairness regression after a model or prompt change.

### Question 59 — B

Answer: Prune older turns from the context window. Dropping stale turns cuts input tokens without losing the current instruction. Local study-map skill 4.1 (Token Cost Efficiency), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Incorrect for this question. More passages raise recall and also lengthen the prompt and the cost per call. Why the correct answer wins: Dropping stale turns cuts input tokens without losing the current instruction.
- **B:** Correct. In this case: Dropping stale turns cuts input tokens without losing the current instruction.
- **C:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: Dropping stale turns cuts input tokens without losing the current instruction.
- **D:** Incorrect for this question. Larger chunks carry more context but dilute the embedding and crowd the prompt window. Why the correct answer wins: Dropping stale turns cuts input tokens without losing the current instruction.

### Question 60 — D

Answer: Cap the response length in the request. A token cap bounds the cost of a runaway answer and the latency of every call. Local study-map skill 4.1 (Token Cost Efficiency), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Incorrect for this question. A single blob loses the field boundaries the model needs to answer precisely. Why the correct answer wins: A token cap bounds the cost of a runaway answer and the latency of every call.
- **B:** Incorrect for this question. More passages raise recall and also lengthen the prompt and the cost per call. Why the correct answer wins: A token cap bounds the cost of a runaway answer and the latency of every call.
- **C:** Incorrect for this question. Larger chunks carry more context but dilute the embedding and crowd the prompt window. Why the correct answer wins: A token cap bounds the cost of a runaway answer and the latency of every call.
- **D:** Correct. In this case: A token cap bounds the cost of a runaway answer and the latency of every call.

### Question 61 — C

Answer: Cache the stable prompt prefix with prompt caching. Prompt caching reuses processed prefix tokens, which cuts latency and input cost on repeat calls. Local study-map skill 4.2 (Model Tiering and Caching), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Incorrect for this question. A semantic cache serves a near-duplicate question without a model call. Why the correct answer wins: Prompt caching reuses processed prefix tokens, which cuts latency and input cost on repeat calls.
- **B:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: Prompt caching reuses processed prefix tokens, which cuts latency and input cost on repeat calls.
- **C:** Correct. In this case: Prompt caching reuses processed prefix tokens, which cuts latency and input cost on repeat calls.
- **D:** Incorrect for this question. A hash cache is exact and avoids a false hit between similar questions. Why the correct answer wins: Prompt caching reuses processed prefix tokens, which cuts latency and input cost on repeat calls.

### Question 62 — A, B

Answers: Send routine prompts to a small model and hard prompts to a large one; Cache answers by embedding similarity to earlier questions. Routing keeps easy prompts on a small model and a semantic cache removes near-duplicate calls. Tiered routing spends the large model only on the requests that need it. A semantic cache serves a near-duplicate question without a model call. Local study-map skill 4.2 (Model Tiering and Caching), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Correct. Tiered routing spends the large model only on the requests that need it. In this case: Routing keeps easy prompts on a small model and a semantic cache removes near-duplicate calls.
- **B:** Correct. A semantic cache serves a near-duplicate question without a model call. In this case: Routing keeps easy prompts on a small model and a semantic cache removes near-duplicate calls.
- **C:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: Routing keeps easy prompts on a small model and a semantic cache removes near-duplicate calls.
- **D:** Incorrect for this question. A full fine-tune changes all weights, which is expensive and gives one model per task. Why the correct answer wins: Routing keeps easy prompts on a small model and a semantic cache removes near-duplicate calls.
- **E:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: Routing keeps easy prompts on a small model and a semantic cache removes near-duplicate calls.

### Question 63 — B

Answer: Choose a lower-latency model for the interactive path. A smaller or latency-optimised model answers faster at some quality cost. Local study-map skill 4.3 (Throughput and Latency Optimisation), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: A smaller or latency-optimised model answers faster at some quality cost.
- **B:** Correct. In this case: A smaller or latency-optimised model answers faster at some quality cost.
- **C:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: A smaller or latency-optimised model answers faster at some quality cost.
- **D:** Incorrect for this question. Batch inference trades turnaround time for a lower price on large offline volumes. Why the correct answer wins: A smaller or latency-optimised model answers faster at some quality cost.

### Question 64 — A, C

Answers: Stream tokens as they are generated; Precompute answers for predictable questions on a schedule. Streaming lowers perceived latency and precomputation moves repeatable work into a cheap batch window. Streaming lowers perceived latency without changing total generation time. Local study-map skill 4.3 (Throughput and Latency Optimisation), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Correct. In this case: Streaming lowers perceived latency and precomputation moves repeatable work into a cheap batch window.
- **B:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: Streaming lowers perceived latency and precomputation moves repeatable work into a cheap batch window.
- **C:** Correct. Streaming lowers perceived latency without changing total generation time. In this case: Streaming lowers perceived latency and precomputation moves repeatable work into a cheap batch window.
- **D:** Incorrect for this question. Batch inference trades turnaround time for a lower price on large offline volumes. Why the correct answer wins: Streaming lowers perceived latency and precomputation moves repeatable work into a cheap batch window.
- **E:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: Streaming lowers perceived latency and precomputation moves repeatable work into a cheap batch window.

### Question 65 — D

Answer: Probe the endpoint with CloudWatch Synthetics. A synthetic canary detects an outage before a user reports it. Local study-map skill 4.4 (GenAI Observability), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Incorrect for this question. CloudTrail records who changed models, keys, and guardrails. Why the correct answer wins: A synthetic canary detects an outage before a user reports it.
- **B:** Incorrect for this question. A model card documents intended use and known limits for reviewers. Why the correct answer wins: A synthetic canary detects an outage before a user reports it.
- **C:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: A synthetic canary detects an outage before a user reports it.
- **D:** Correct. In this case: A synthetic canary detects an outage before a user reports it.

### Question 66 — A, E

Answers: Publish token usage as CloudWatch metrics; Detect spend spikes with AWS Cost Anomaly Detection. Token metrics show where spend comes from and anomaly detection finds an unexpected bill. Token metrics per model and tenant show where spend and latency come from. Anomaly detection finds an unexpected token bill without a fixed threshold. Local study-map skill 4.4 (GenAI Observability), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Correct. Anomaly detection finds an unexpected token bill without a fixed threshold. In this case: Token metrics show where spend comes from and anomaly detection finds an unexpected bill.
- **B:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: Token metrics show where spend comes from and anomaly detection finds an unexpected bill.
- **C:** Incorrect for this question. A model card documents intended use and known limits for reviewers. Why the correct answer wins: Token metrics show where spend comes from and anomaly detection finds an unexpected bill.
- **D:** Incorrect for this question. A latency alarm fires on the symptom users feel. Why the correct answer wins: Token metrics show where spend comes from and anomaly detection finds an unexpected bill.
- **E:** Correct. Token metrics per model and tenant show where spend and latency come from. In this case: Token metrics show where spend comes from and anomaly detection finds an unexpected bill.

### Question 67 — A

Answer: Cover the steady compute with a Savings Plan. A Savings Plan discounts the predictable part of the compute baseline. Local study-map skill 4.5 (Cost Attribution and Governance), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Correct. In this case: A Savings Plan discounts the predictable part of the compute baseline.
- **B:** Incorrect for this question. A budget alert stops one tenant from consuming the shared quota. Why the correct answer wins: A Savings Plan discounts the predictable part of the compute baseline.
- **C:** Incorrect for this question. Anomaly detection finds an unexpected token bill without a fixed threshold. Why the correct answer wins: A Savings Plan discounts the predictable part of the compute baseline.
- **D:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: A Savings Plan discounts the predictable part of the compute baseline.

### Question 68 — A

Answer: Score how directly the answer addresses the question. Relevance separates an off-topic answer from a factually wrong one. Local study-map skill 5.1 (GenAI Evaluation Metrics), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Correct. In this case: Relevance separates an off-topic answer from a factually wrong one.
- **B:** Incorrect for this question. Embedding-based similarity credits a correct paraphrase that word overlap misses. Why the correct answer wins: Relevance separates an off-topic answer from a factually wrong one.
- **C:** Incorrect for this question. Recall shows whether the answer was missing evidence before generation began. Why the correct answer wins: Relevance separates an off-topic answer from a factually wrong one.
- **D:** Incorrect for this question. Overlap metrics are cheap and reward wording that matches the references. Why the correct answer wins: Relevance separates an off-topic answer from a factually wrong one.

### Question 69 — B, E

Answers: Score candidate answers with a judge model on a fixed rubric; Have reviewers score a sample against a written rubric. A judge model scales the scoring and a human rubric supplies the reference it is checked against. A judge model scales subjective scoring and needs its own agreement check. A rubric with human scores gives a reference the automatic metrics can be checked against. Local study-map skill 5.1 (GenAI Evaluation Metrics), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Incorrect for this question. Overlap metrics are cheap and reward wording that matches the references. Why the correct answer wins: A judge model scales the scoring and a human rubric supplies the reference it is checked against.
- **B:** Correct. A judge model scales subjective scoring and needs its own agreement check. In this case: A judge model scales the scoring and a human rubric supplies the reference it is checked against.
- **C:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: A judge model scales the scoring and a human rubric supplies the reference it is checked against.
- **D:** Incorrect for this question. Recall shows whether the answer was missing evidence before generation began. Why the correct answer wins: A judge model scales the scoring and a human rubric supplies the reference it is checked against.
- **E:** Correct. A rubric with human scores gives a reference the automatic metrics can be checked against. In this case: A judge model scales the scoring and a human rubric supplies the reference it is checked against.

### Question 70 — A

Answer: Split traffic between two model versions and compare outcomes. An A/B test measures the difference on real traffic before a full switch. Local study-map skill 5.2 (Model Comparison and Traffic Testing), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Correct. In this case: An A/B test measures the difference on real traffic before a full switch.
- **B:** Incorrect for this question. A rubric with human scores gives a reference the automatic metrics can be checked against. Why the correct answer wins: An A/B test measures the difference on real traffic before a full switch.
- **C:** Incorrect for this question. A canary limits the blast radius of a prompt or model change. Why the correct answer wins: An A/B test measures the difference on real traffic before a full switch.
- **D:** Incorrect for this question. Shadow traffic compares answers with no user exposure. Why the correct answer wins: An A/B test measures the difference on real traffic before a full switch.

### Question 71 — C

Answer: Run the release against a curated golden question set. A golden set with known answers catches a regression the moment it ships. Local study-map skill 5.3 (Regression Testing and Quality Gates), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: A golden set with known answers catches a regression the moment it ships.
- **B:** Incorrect for this question. A rubric with human scores gives a reference the automatic metrics can be checked against. Why the correct answer wins: A golden set with known answers catches a regression the moment it ships.
- **C:** Correct. In this case: A golden set with known answers catches a regression the moment it ships.
- **D:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: A golden set with known answers catches a regression the moment it ships.

### Question 72 — B, E

Answers: Block the release when evaluation drops below the threshold; Diff the new responses against the previous version. A quality gate blocks the regression and a diff highlights the wording changes behind it. A quality gate stops a measurable regression from reaching production. Local study-map skill 5.3 (Regression Testing and Quality Gates), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: A quality gate blocks the regression and a diff highlights the wording changes behind it.
- **B:** Correct. In this case: A quality gate blocks the regression and a diff highlights the wording changes behind it.
- **C:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: A quality gate blocks the regression and a diff highlights the wording changes behind it.
- **D:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: A quality gate blocks the regression and a diff highlights the wording changes behind it.
- **E:** Correct. A quality gate stops a measurable regression from reaching production. In this case: A quality gate blocks the regression and a diff highlights the wording changes behind it.

### Question 73 — C

Answer: Measure whether the retrieved passages were relevant. Retrieval precision explains a wrong answer that the model was given bad context for. Local study-map skill 5.4 (Retrieval and Agent Evaluation), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Incorrect for this question. Overlap metrics are cheap and reward wording that matches the references. Why the correct answer wins: Retrieval precision explains a wrong answer that the model was given bad context for.
- **B:** Incorrect for this question. Recall shows whether the answer was missing evidence before generation began. Why the correct answer wins: Retrieval precision explains a wrong answer that the model was given bad context for.
- **C:** Correct. In this case: Retrieval precision explains a wrong answer that the model was given bad context for.
- **D:** Incorrect for this question. Tool accuracy locates the failure inside the agent loop rather than at the answer. Why the correct answer wins: Retrieval precision explains a wrong answer that the model was given bad context for.

### Question 74 — A, D

Answers: Measure whether the agent called the right tool with the right arguments; Measure the share of agent tasks completed end to end. Tool accuracy locates the wrong call and completion rate shows whether the task ended. Tool accuracy locates the failure inside the agent loop rather than at the answer. Completion rate is the outcome metric for an agent that must actually finish work. Local study-map skill 5.4 (Retrieval and Agent Evaluation), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Correct. Tool accuracy locates the failure inside the agent loop rather than at the answer. In this case: Tool accuracy locates the wrong call and completion rate shows whether the task ended.
- **B:** Incorrect for this question. Overlap metrics are cheap and reward wording that matches the references. Why the correct answer wins: Tool accuracy locates the wrong call and completion rate shows whether the task ended.
- **C:** Incorrect for this question. Retrieval precision explains a wrong answer that the model was given bad context for. Why the correct answer wins: Tool accuracy locates the wrong call and completion rate shows whether the task ended.
- **D:** Correct. Completion rate is the outcome metric for an agent that must actually finish work. In this case: Tool accuracy locates the wrong call and completion rate shows whether the task ended.
- **E:** Incorrect for this question. Embedding-based similarity credits a correct paraphrase that word overlap misses. Why the correct answer wins: Tool accuracy locates the wrong call and completion rate shows whether the task ended.

### Question 75 — A

Answer: Trim or chunk the request when it exceeds the context window. Overflow protection keeps the prompt inside the model limit instead of truncating silently. Local study-map skill 5.5 (GenAI Troubleshooting), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Correct. In this case: Overflow protection keeps the prompt inside the model limit instead of truncating silently.
- **B:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: Overflow protection keeps the prompt inside the model limit instead of truncating silently.
- **C:** Incorrect for this question. A truncation check shows whether the model ever saw the end of the instruction. Why the correct answer wins: Overflow protection keeps the prompt inside the model limit instead of truncating silently.
- **D:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: Overflow protection keeps the prompt inside the model limit instead of truncating silently.
