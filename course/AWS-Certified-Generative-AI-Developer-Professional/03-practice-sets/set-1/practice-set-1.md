# AWS Certified Generative AI Developer - Professional (AIP-C01) — Full-Length Mock Exam 1

Generative AI Developer · 75 questions · 180 minutes · scaled passing score 750 of 1000

Blueprint-weighted mock exam. Item mix: 60 multiple-choice and 15 multiple-response items (the selection count is stated in each multi-response stem). The published exam has 75 questions in 180 minutes, of which 65 are scored and 10 are unscored, and AWS does not identify the unscored items. AWS publishes no split between multiple-choice and multiple-response items, so the 15-item multi-response block is an authoring choice. At 75 items in 180 minutes this set matches the published pacing at about 144 seconds per item, including the same unscored proportion. The published format has no case-study component, so no case-study item appears here. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied AWS exam items.

## Questions

---

## Domain 1 — Foundation Model Integration, Data Management, and Compliance (31%) — Model integration, data pipelines, vector stores, retrieval, and prompts

### 1. A retail team must prove that a product-question assistant answers acceptably before anyone buys reserved model capacity. Which two choices make that proof possible? Select two.

- A. Run the release against a curated golden question set
- B. Run a full fine-tune of every model weight
- C. Buy Amazon Bedrock provisioned throughput for the model
- D. Use one frontier model for every request
- E. Call the model on demand through Amazon Bedrock

### 2. A retailer wants a second product team to reuse the assistant foundation rather than rebuild it. Which two components should the reference architecture standardise? Select two.

- A. Let each application call the model API directly
- B. Version the prompt in Amazon Bedrock Prompt Management
- C. Hardcode one model identifier in the application source
- D. Put one internal GenAI gateway in front of every model call
- E. Keep the prompt as a string constant in the application code

### 3. A pilot assistant answers well but nobody can say whether expansion is affordable. Which measurement should the team add before requesting budget?

- A. Use one frontier model for every request
- B. Compare quality per thousand tokens across candidates
- C. Run a full fine-tune of every model weight
- D. Buy Amazon Bedrock provisioned throughput for the model

### 4. Three foundation models are candidates for catalogue classification in twelve languages and the team has sample labels for each language. How should the candidates be compared?

- A. Use one frontier model for every request
- B. Buy Amazon Bedrock provisioned throughput for the model
- C. Compare the candidates with an Amazon Bedrock model evaluation job
- D. Fine-tune with low-rank adaptation adapters

### 5. Store staff need one-sentence answers about return policy from a fixed document that changes twice a year. Which model choice fits that workload?

- A. Run a full fine-tune of every model weight
- B. Use one frontier model for every request
- C. Route the call through Amazon Bedrock cross-Region inference
- D. Right-size the model to the task difficulty

### 6. Merchandising wants to try a different model for the gift-guide experience next week without a code release. What makes that trial possible?

- A. Let each application call the model API directly
- B. Hardcode one model identifier in the application source
- C. Put the model identifier in AWS AppConfig and switch it without a deploy
- D. Keep the prompt as a string constant in the application code

### 7. During a flash sale the chosen model throttles requests in the primary Region while capacity sits unused in another Region. What should absorb the overflow?

- A. Route the call through Amazon Bedrock cross-Region inference
- B. Retry the failed call until it succeeds
- C. Keep a GPU endpoint running for occasional requests
- D. Run a full fine-tune of every model weight

### 8. One Region hosting the assistant degrades, and the business prefers shorter, plainer answers to an outage. What design meets that preference?

- A. Fall back to a second model when the first is unavailable
- B. Use one frontier model for every request
- C. Retry the failed call until it succeeds
- D. Store the model API key in an environment variable

### 9. A customised model passed evaluation last quarter, but answers changed after the provider rolled the model forward. What prevents that surprise?

- A. Run a full fine-tune of every model weight
- B. Keep the prompt as a string constant in the application code
- C. Let each application call the model API directly
- D. Pin the model version instead of tracking the latest alias

### 10. Supplier catalogue feeds arrive nightly with missing sizes and duplicate rows, and a bad batch must not reach the index. What should guard the ingestion step?

- A. Set an explicit CloudWatch Logs retention period
- B. Validate response structure and log the failures
- C. Enforce freshness and completeness rules with AWS Glue Data Quality
- D. Scan the data store with Amazon Macie

### 11. Product codes and brand names must stay filterable after documents are chunked for retrieval. What should extraction add during ingestion?

- A. Normalise the text with a model call before indexing
- B. Format the turns as an alternating conversation structure
- C. Concatenate all fields into one unlabelled text block
- D. Extract entities with Amazon Comprehend before indexing

### 12. Warranty cards arrive as scanned images and customers ask questions about their terms. What turns those pages into searchable text?

- A. Extract the text from scanned pages with Amazon Textract
- B. Normalise the text with a model call before indexing
- C. Extract entities with Amazon Comprehend before indexing
- D. Transcribe the call recordings with Amazon Transcribe

### 13. A developer gets a validation error when calling a foundation model through the Amazon Bedrock API. What should the request body follow?

- A. Concatenate all fields into one unlabelled text block
- B. Send the request as the JSON body the model expects
- C. Keep the prompt as a string constant in the application code
- D. Format the turns as an alternating conversation structure

### 14. A shopping assistant must respect speaker roles and keep the last three exchanges in order. How should the input be arranged?

- A. Concatenate all fields into one unlabelled text block
- B. Format the turns as an alternating conversation structure
- C. Raise the temperature for creative variants
- D. Keep the prompt as a string constant in the application code

### 15. A loyalty programme holds forty thousand product descriptions with structured attributes and needs both attribute filtering and similarity search. Where should the vectors live if the team already runs DynamoDB?

- A. Keep embeddings and metadata in Amazon DynamoDB
- B. Store the vectors in Amazon Aurora PostgreSQL with pgvector
- C. Index the vectors in Amazon OpenSearch Service with k-NN search
- D. Store the knowledge graph in Amazon Neptune

### 16. A search assistant answers questions from documents that span eight brands, and a query about one brand keeps returning another brand's policy. What should be applied before ranking?

- A. Raise the number of retrieved passages per query
- B. Drop passages below a relevance score threshold
- C. Expand the user query into related terms before retrieval
- D. Filter the search by document metadata before the similarity ranking

### 17. Price-list updates must be searchable within seconds of the file landing in Amazon S3. What keeps the index current that quickly?

- A. Rebuild the index on a schedule and accept staleness between runs
- B. Cache every answer with no expiry
- C. Re-embed the corpus when the embedding model changes
- D. Trigger re-indexing from Amazon S3 event notifications

### 18. A retailer's manuals use nested headings, and a retrieved chunk without its parent heading reads as a policy for the wrong product line. Which split follows the content?

- A. Split documents into fixed-size token windows with overlap
- B. Split by document structure into sections and subsections
- C. Keep old vectors and embed new documents with the newer model
- D. Increase the chunk size so every answer fits in one chunk

### 19. Shoppers search by exact SKU as often as by description, and the top results are often relevant but out of order. Which two changes address both problems? Select two.

- A. Keep old vectors and embed new documents with the newer model
- B. Combine keyword and vector retrieval and merge the ranked lists
- C. Raise the number of retrieved passages per query
- D. Drop passages below a relevance score threshold
- E. Rerank the retrieved passages with an Amazon Bedrock reranker

### 20. A product support assistant must match precise clauses yet give the model enough surrounding text to explain them. Which indexing pattern does both?

- A. Index small child chunks and return the larger parent to the model
- B. Raise the number of retrieved passages per query
- C. Split documents into fixed-size token windows with overlap
- D. Increase the chunk size so every answer fits in one chunk

### 21. In a chat about a jacket, the follow-up question is only does it come in navy, and retrieval returns generic colour pages. What should run before the search?

- A. Fine-tune the embedding model on labelled query and passage pairs
- B. Raise the number of retrieved passages per query
- C. Expand the user query into related terms before retrieval
- D. Rewrite the query using the conversation history first

### 22. A store assistant sometimes adopts the tone of a customer complaint it is answering. Where should the role and tone boundaries live?

- A. Raise the temperature for creative variants
- B. Cap the response length in the request
- C. Put the role, tone, and boundaries in the system prompt
- D. Keep the prompt as a string constant in the application code

### 23. Order-status answers must populate a fixed set of fields in the mobile app. What guarantees the response shape?

- A. Cap the response length in the request
- B. Constrain the response with a JSON schema
- C. Raise the temperature for creative variants
- D. Concatenate all fields into one unlabelled text block

---

## Domain 2 — Implementation and Integration (26%) — Agents, deployment, enterprise integration, APIs, and developer tooling

### 24. A returns agent must remember an order number across several turns and survive a redeployment mid-conversation. Where should that state live?

- A. Cache every answer with no expiry
- B. Keep memory only in the prompt of the current turn
- C. Set an explicit CloudWatch Logs retention period
- D. Keep conversation and task memory in Amazon DynamoDB

### 25. A delivery-tracking agent needs managed session memory and a place to run its reasoning loop. Which service provides both?

- A. Run the agent on Amazon Bedrock AgentCore
- B. Implement the tool as an AWS Lambda function
- C. Keep memory only in the prompt of the current turn
- D. Let each application call the model API directly

### 26. A retail engineering team wants an open-source agent loop with tools and memory that is not tied to one model provider. What fits that requirement?

- A. Keep the prompt as a string constant in the application code
- B. Return the whole answer from one synchronous call
- C. Give one agent every tool in the platform
- D. Build the agent with Strands Agents

### 27. A stock-check agent sometimes loops between two tools until the request times out. Which two controls fix that? Select two.

- A. Raise the temperature for creative variants
- B. Give one agent every tool in the platform
- C. Retry the failed call until it succeeds
- D. Set an explicit step and budget limit on the agent loop
- E. Coordinate the steps in AWS Step Functions

### 28. An agent passes a date in the wrong format to the order system and the call fails deep inside the transaction. Where should the argument be checked?

- A. Raise the temperature for creative variants
- B. Validate tool arguments against a schema before calling
- C. Retry the failed call until it succeeds
- D. Cache every answer with no expiry

### 29. One inventory tool occasionally hangs for minutes and stalls the whole agent turn. What contains that failure?

- A. Set an explicit CloudWatch Logs retention period
- B. Keep a GPU endpoint running for occasional requests
- C. Bound each tool call with a timeout and a fallback
- D. Retry the failed call until it succeeds

### 30. A checkout assistant serves a steady twenty million tokens an hour and keeps hitting on-demand throttles. What should the team buy?

- A. Buy Amazon Bedrock provisioned throughput for the model
- B. Use one frontier model for every request
- C. Keep a GPU endpoint running for occasional requests
- D. Call the model on demand through Amazon Bedrock

### 31. A launch-day promotion is expected to send a burst far above normal traffic to the assistant. Which two controls protect shared capacity? Select two.

- A. Set per-client throttling at the API layer
- B. Call the model on demand through Amazon Bedrock
- C. Buffer the work in an Amazon SQS queue
- D. Retry the failed call until it succeeds
- E. Return the whole answer from one synchronous call

### 32. Order events must reach the assistant with filtering by event type, and new consumers keep being added. What connects them?

- A. Route domain events through Amazon EventBridge
- B. Fan the result out with Amazon SNS
- C. Move SaaS records in with Amazon AppFlow
- D. Buffer the work in an Amazon SQS queue

### 33. A nightly batch of fifty thousand review summaries must not lose work when a model call fails. What should sit between the job and the model?

- A. Fan the result out with Amazon SNS
- B. Front the model with Amazon API Gateway
- C. Return the whole answer from one synchronous call
- D. Buffer the work in an Amazon SQS queue

### 34. The assistant runs in a container and must read one bucket and call one model. How should it obtain permission?

- A. Store the model API key in an environment variable
- B. Give the task an IAM role scoped to the resources it uses
- C. Receive partner files over AWS Transfer Family
- D. Make the document bucket publicly readable

### 35. Five product teams each call the model API from their own service and their keys and quotas are impossible to audit. What should the platform team introduce?

- A. Let each application call the model API directly
- B. Hardcode one model identifier in the application source
- C. Store the model API key in an environment variable
- D. Put one internal GenAI gateway in front of every model call

### 36. A prompt change must be tested against a fixed question set before it can reach shoppers. Which two services carry that release path? Select two.

- A. Keep the prompt as a string constant in the application code
- B. Run the evaluation suite in AWS CodeBuild
- C. Release the assistant through AWS CodePipeline
- D. Let each application call the model API directly
- E. Store the model API key in an environment variable

### 37. Shoppers abandon the assistant when they stare at a blank panel for eight seconds before the answer appears. What improves the experience without changing total generation time?

- A. Return the whole answer from one synchronous call
- B. Queue the prompt and return a job identifier for polling
- C. Stream tokens as server-sent events
- D. Keep a GPU endpoint running for occasional requests

### 38. A client is throttled during a traffic spike and its immediate retries make the throttling worse. What retry policy should it adopt?

- A. Open a circuit breaker after repeated dependency failures
- B. Retry the failed call until it succeeds
- C. Keep a GPU endpoint running for occasional requests
- D. Retry throttled calls with exponential backoff and jitter

### 39. A dependency behind the assistant has been returning errors instantly for ten minutes and every request now waits on it. What stops the pile-up?

- A. Open a circuit breaker after repeated dependency failures
- B. Retry the failed call until it succeeds
- C. Return the whole answer from one synchronous call
- D. Retry throttled calls with exponential backoff and jitter

### 40. The assistant needs per-client authentication, request validation, and throttling before a model is called. What should front it?

- A. Serve repeatable responses from Amazon CloudFront
- B. Build the interface with AWS Amplify
- C. Front the model with Amazon API Gateway
- D. Let each application call the model API directly

### 41. A small retail team needs a hosted storefront chat widget without building a front-end pipeline. What accelerates that work?

- A. Stream tokens as server-sent events
- B. Build the interface with AWS Amplify
- C. Run the request shaping logic at the edge with Lambda@Edge
- D. Front the model with Amazon API Gateway

### 42. Developers hand-write the same Bedrock SDK boilerplate for each new feature and ask for inline explanations. What helps them move faster?

- A. Keep the prompt as a string constant in the application code
- B. Release the assistant through AWS CodePipeline
- C. Generate and explain the integration code with Amazon Q Developer
- D. Run the evaluation suite in AWS CodeBuild

### 43. A request takes eleven seconds and nobody knows whether the delay is the gateway, the retrieval call, or the model. What shows it?

- A. Set an explicit CloudWatch Logs retention period
- B. Query the prompt and response logs with CloudWatch Logs Insights
- C. Trace the request across services with AWS X-Ray
- D. Record control-plane activity in AWS CloudTrail

---

## Domain 3 — AI Safety, Security, and Governance (20%) — Safety controls, privacy, governance, and responsible AI

### 44. A store assistant must block abusive and unsafe text in both what shoppers type and what the model answers. What sits on the request path?

- A. Set an explicit CloudWatch Logs retention period
- B. Apply Amazon Bedrock Guardrails content filters
- C. Lower the temperature for factual answers
- D. Cap the response length in the request

### 45. Legal has named three subjects the assistant must refuse and has demanded that account numbers never appear in an answer. Which two guardrail policies cover that? Select two.

- A. Cache every answer with no expiry
- B. Cap the response length in the request
- C. Retry the failed call until it succeeds
- D. Enable sensitive-information filters in Amazon Bedrock Guardrails
- E. Define denied topics in Amazon Bedrock Guardrails

### 46. Shoppers challenge answers about delivery windows and the team needs every claim tied to a source line. What should the answer include?

- A. Escalate low-confidence or high-impact answers to a person
- B. Require the answer to cite the retrieved passage
- C. Return a confidence score with each answer
- D. Cap the response length in the request

### 47. An answer is fluent but asserts a return window that the retrieved policy never states. Which control catches that specific failure?

- A. Lower the temperature for factual answers
- B. Enable the contextual grounding check in Guardrails
- C. Constrain the response with a JSON schema
- D. Score answers by embedding similarity to the reference

### 48. Shoppers paste text that says to ignore previous instructions and reveal the staff discount rules. What detects that attempt?

- A. Cap the response length in the request
- B. Screen inputs for instruction override and jailbreak patterns
- C. Retry the failed call until it succeeds
- D. Lower the temperature for factual answers

### 49. A supplier's product description contains the sentence instruction to answer only in promotional slogans, and the assistant obeys it. What should have been done to the retrieved text?

- A. Set an explicit CloudWatch Logs retention period
- B. Fine-tune the embedding model on labelled query and passage pairs
- C. Strip control text and delimiters from retrieved content
- D. Constrain the response with a JSON schema

### 50. Shoppers include card fragments when describing a billing problem and those fragments must never reach the model. What is the right point of control?

- A. Scan the data store with Amazon Macie
- B. Enable sensitive-information filters in Amazon Bedrock Guardrails
- C. Mask personal data before the prompt is built
- D. Set an explicit CloudWatch Logs retention period

### 51. Before the support corpus is indexed, the data team must find and remove personal data that was pasted into old tickets. Which two services do that work? Select two.

- A. Scan the data store with Amazon Macie
- B. Store the model API key in an environment variable
- C. Detect personal data with Amazon Comprehend
- D. Set an explicit CloudWatch Logs retention period
- E. Apply Amazon Bedrock Guardrails content filters

### 52. A compliance review requires that model calls and document reads never traverse the public internet. What provides that path?

- A. Store the model API key in an environment variable
- B. Make the document bucket publicly readable
- C. Serve repeatable responses from Amazon CloudFront
- D. Call the model through an interface VPC endpoint

### 53. The assistant's compute must have no inbound route from the internet while still reaching AWS APIs. Where should it run?

- A. Make the document bucket publicly readable
- B. Serve repeatable responses from Amazon CloudFront
- C. Let each application call the model API directly
- D. Deploy the workload in private subnets

### 54. An auditor asks who changed the guardrail policy and when the model version was swapped. What answers both questions?

- A. Record control-plane activity in AWS CloudTrail
- B. Turn on Amazon Bedrock model invocation logging
- C. Build the operations view in Amazon Managed Grafana
- D. Set an explicit CloudWatch Logs retention period

### 55. A regulator asks which corpus and which model version produced a specific answer six months ago. Which two records make that reconstruction possible? Select two.

- A. Cache every answer with no expiry
- B. Pin the model version instead of tracking the latest alias
- C. Store the model API key in an environment variable
- D. Lower the temperature for factual answers
- E. Record data lineage in the AWS Glue Data Catalog

### 56. Reviewers must understand what the assistant is not intended to answer before it goes live. What documents that?

- A. Publish a model card with the model version
- B. Constrain the response with a JSON schema
- C. Compare the candidates with an Amazon Bedrock model evaluation job
- D. Set an explicit CloudWatch Logs retention period

### 57. The assistant handles refund exceptions, and a wrong answer costs real money. What should happen when confidence is low?

- A. Escalate low-confidence or high-impact answers to a person
- B. Raise the temperature for creative variants
- C. Cap the response length in the request
- D. Cache every answer with no expiry

### 58. Answer quality for one language community fell after a prompt change and nobody noticed for a month. What would have surfaced it?

- A. Report fairness metrics per user segment
- B. Alert when fairness metrics move beyond a band
- C. Detect spend spikes with AWS Cost Anomaly Detection
- D. Alarm on p95 latency and error rate

---

## Domain 4 — Operational Efficiency and Optimization for GenAI Applications (12%) — Token cost, latency, throughput, and observability

### 59. Long support sessions carry forty earlier turns, and the input bill grows with every message. What should the assistant do with the older turns?

- A. Prune older turns from the context window
- B. Increase the chunk size so every answer fits in one chunk
- C. Raise the number of retrieved passages per query
- D. Raise the temperature for creative variants

### 60. A shopping session can run for an hour and the conversation must stay coherent without resending every turn. What keeps it inside the window cheaply?

- A. Concatenate all fields into one unlabelled text block
- B. Raise the number of retrieved passages per query
- C. Summarise the conversation before adding more turns
- D. Increase the chunk size so every answer fits in one chunk

### 61. Thousands of shoppers ask the same return question with slightly different wording every hour. What avoids paying for each variation?

- A. Cache every answer with no expiry
- B. Keep a GPU endpoint running for occasional requests
- C. Cache answers by embedding similarity to earlier questions
- D. Cache the response under a hash of the normalised request

### 62. A retailer wants to cut model spend without dropping answer quality on hard questions. Which two levers act on the request itself? Select two.

- A. Cache every answer with no expiry
- B. Use one frontier model for every request
- C. Run a full fine-tune of every model weight
- D. Cache the response under a hash of the normalised request
- E. Send routine prompts to a small model and hard prompts to a large one

### 63. An eight-second answer feels broken even when the total time is acceptable. What changes the perception without changing total generation time?

- A. Return the whole answer from one synchronous call
- B. Run the work as an Amazon Bedrock batch inference job
- C. Keep a GPU endpoint running for occasional requests
- D. Stream tokens as they are generated

### 64. A checkout help panel must answer in under two seconds, and its three lookups are independent. Which two changes attack that target? Select two.

- A. Retry the failed call until it succeeds
- B. Use one frontier model for every request
- C. Issue independent model calls in parallel
- D. Run the work as an Amazon Bedrock batch inference job
- E. Choose a lower-latency model for the interactive path

### 65. Answers became shorter and cheaper overnight and the team needs the exact prompts and responses from that hour. What supplies them?

- A. Record control-plane activity in AWS CloudTrail
- B. Turn on Amazon Bedrock model invocation logging
- C. Publish a model card with the model version
- D. Set an explicit CloudWatch Logs retention period

### 66. Operations wants one dashboard that shows spend by model and warns before shoppers feel a slowdown. Which two signals belong on it? Select two.

- A. Alarm on p95 latency and error rate
- B. Detect spend spikes with AWS Cost Anomaly Detection
- C. Publish a model card with the model version
- D. Set an explicit CloudWatch Logs retention period
- E. Publish token usage as CloudWatch metrics

### 67. Finance cannot tell which product team caused last month's model bill. What makes the attribution possible?

- A. Keep a GPU endpoint running for occasional requests
- B. Cover the steady compute with a Savings Plan
- C. Break down spend by application tag in AWS Cost Explorer
- D. Detect spend spikes with AWS Cost Anomaly Detection

---

## Domain 5 — Testing, Validation, and Troubleshooting (11%) — Evaluation, validation, regression testing, and diagnosis

### 68. An answer reads well and cites a policy, but two of its claims appear nowhere in the retrieved text. Which metric exposes that?

- A. Score how directly the answer addresses the question
- B. Report BERTScore for semantic similarity to the reference
- C. Measure whether each claim is supported by the retrieved context
- D. Report ROUGE and BLEU against the reference answers

### 69. Two prompt versions answer the same question set, and the second paraphrases more than the first. Which two scores stay fair to a correct paraphrase? Select two.

- A. Report ROUGE and BLEU against the reference answers
- B. Measure whether the needed passage was retrieved at all
- C. Raise the temperature for creative variants
- D. Report BERTScore for semantic similarity to the reference
- E. Score how directly the answer addresses the question

### 70. Two models must be compared on a week of real shopper traffic to see which converts better. What design answers that question?

- A. Split traffic between two model versions and compare outcomes
- B. Have reviewers score a sample against a written rubric
- C. Send a small traffic share to the new prompt and watch the metrics
- D. Mirror production traffic to the new version and compare offline

### 71. A one-word prompt edit broke the JSON shape the mobile app expects, and nobody caught it before release. What would have caught it?

- A. Cache every answer with no expiry
- B. Run the release against a curated golden question set
- C. Have reviewers score a sample against a written rubric
- D. Run a prompt regression suite before promoting a version

### 72. A retailer wants a prompt change stopped automatically when quality drops, and wants multi-turn paths exercised before release. Which two practices deliver that? Select two.

- A. Block the release when evaluation drops below the threshold
- B. Replay scripted user journeys against the new version
- C. Raise the temperature for creative variants
- D. Cache every answer with no expiry
- E. Retry the failed call until it succeeds

### 73. The order-change agent answers politely but only finishes half the requests end to end. What measures that gap?

- A. Measure the share of agent tasks completed end to end
- B. Report ROUGE and BLEU against the reference answers
- C. Measure whether the agent called the right tool with the right arguments
- D. Measure whether the needed passage was retrieved at all

### 74. Shoppers get answers built from the wrong policy section, and the team must know whether the right passage was ever retrieved. Which two retrieval scores answer that? Select two.

- A. Report ROUGE and BLEU against the reference answers
- B. Measure whether the retrieved passages were relevant
- C. Measure whether the needed passage was retrieved at all
- D. Report BERTScore for semantic similarity to the reference
- E. Measure whether the agent called the right tool with the right arguments

### 75. Answers ignore the final instruction whenever a long attachment is included, and nothing logs an error. What should be inspected first?

- A. Trim or chunk the request when it exceeds the context window
- B. Log the token count and check for truncated prompts
- C. Cache every answer with no expiry
- D. Query the prompt and response logs with CloudWatch Logs Insights

---

## Answer key and explanations

### Question 1 — A, E

Answers: Call the model on demand through Amazon Bedrock; Run the release against a curated golden question set. On-demand calls bill per token and a curated question set measures quality, so the proof costs little and produces evidence. On-demand Bedrock inference bills per token with no committed capacity, which suits spiky or unproven demand. A golden set with known answers catches a regression the moment it ships. Local study-map skill 1.1 (GenAI Solution Architecture), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Correct. A golden set with known answers catches a regression the moment it ships. In this case: On-demand calls bill per token and a curated question set measures quality, so the proof costs little and produces evidence.
- **B:** Incorrect for this question. A full fine-tune changes all weights, which is expensive and gives one model per task. Why the correct answer wins: On-demand calls bill per token and a curated question set measures quality, so the proof costs little and produces evidence.
- **C:** Incorrect for this question. Provisioned throughput reserves model units and gives a predictable token-per-minute ceiling. Why the correct answer wins: On-demand calls bill per token and a curated question set measures quality, so the proof costs little and produces evidence.
- **D:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: On-demand calls bill per token and a curated question set measures quality, so the proof costs little and produces evidence.
- **E:** Correct. On-demand Bedrock inference bills per token with no committed capacity, which suits spiky or unproven demand. In this case: On-demand calls bill per token and a curated question set measures quality, so the proof costs little and produces evidence.

### Question 2 — B, D

Answers: Put one internal GenAI gateway in front of every model call; Version the prompt in Amazon Bedrock Prompt Management. A shared gateway and versioned prompt templates are the two pieces every team would otherwise rebuild differently. A gateway centralises credentials, quotas, logging, and model routing for all teams. Prompt Management stores versions and variables so the same template serves every environment. Local study-map skill 1.1 (GenAI Solution Architecture), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. Direct calls from every app scatter keys, quotas, and logging across teams. Why the correct answer wins: A shared gateway and versioned prompt templates are the two pieces every team would otherwise rebuild differently.
- **B:** Correct. Prompt Management stores versions and variables so the same template serves every environment. In this case: A shared gateway and versioned prompt templates are the two pieces every team would otherwise rebuild differently.
- **C:** Incorrect for this question. A hardcoded identifier forces a code change and a release to try another model. Why the correct answer wins: A shared gateway and versioned prompt templates are the two pieces every team would otherwise rebuild differently.
- **D:** Correct. A gateway centralises credentials, quotas, logging, and model routing for all teams. In this case: A shared gateway and versioned prompt templates are the two pieces every team would otherwise rebuild differently.
- **E:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: A shared gateway and versioned prompt templates are the two pieces every team would otherwise rebuild differently.

### Question 3 — B

Answer: Compare quality per thousand tokens across candidates. Quality per thousand tokens shows whether a cheaper model is good enough or the spend is unavoidable. Quality per unit of spend separates a cheaper model that is good enough from a false economy. Local study-map skill 1.2 (Proof-of-Concept Validation), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: Quality per thousand tokens shows whether a cheaper model is good enough or the spend is unavoidable.
- **B:** Correct. Quality per unit of spend separates a cheaper model that is good enough from a false economy. In this case: Quality per thousand tokens shows whether a cheaper model is good enough or the spend is unavoidable.
- **C:** Incorrect for this question. A full fine-tune changes all weights, which is expensive and gives one model per task. Why the correct answer wins: Quality per thousand tokens shows whether a cheaper model is good enough or the spend is unavoidable.
- **D:** Incorrect for this question. Provisioned throughput reserves model units and gives a predictable token-per-minute ceiling. Why the correct answer wins: Quality per thousand tokens shows whether a cheaper model is good enough or the spend is unavoidable.

### Question 4 — C

Answer: Compare the candidates with an Amazon Bedrock model evaluation job. A Bedrock evaluation job scores every candidate on the same labelled prompts before a choice is made. A Bedrock evaluation job scores candidate models on your prompts and metrics before you choose. Local study-map skill 1.3 (Foundation Model Selection and Benchmarking), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: A Bedrock evaluation job scores every candidate on the same labelled prompts before a choice is made.
- **B:** Incorrect for this question. Provisioned throughput reserves model units and gives a predictable token-per-minute ceiling. Why the correct answer wins: A Bedrock evaluation job scores every candidate on the same labelled prompts before a choice is made.
- **C:** Correct. A Bedrock evaluation job scores candidate models on your prompts and metrics before you choose. In this case: A Bedrock evaluation job scores every candidate on the same labelled prompts before a choice is made.
- **D:** Incorrect for this question. LoRA trains a small adapter instead of every weight, which cuts cost and keeps the base model reusable. Why the correct answer wins: A Bedrock evaluation job scores every candidate on the same labelled prompts before a choice is made.

### Question 5 — D

Answer: Right-size the model to the task difficulty. A model no larger than the task needs keeps the per-answer price low for a narrow, repetitive question. A model no larger than the task needs is the largest single cost lever. Local study-map skill 1.3 (Foundation Model Selection and Benchmarking), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. A full fine-tune changes all weights, which is expensive and gives one model per task. Why the correct answer wins: A model no larger than the task needs keeps the per-answer price low for a narrow, repetitive question.
- **B:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: A model no larger than the task needs keeps the per-answer price low for a narrow, repetitive question.
- **C:** Incorrect for this question. A cross-Region inference profile spreads traffic across Regions so a local capacity shortage is absorbed. Why the correct answer wins: A model no larger than the task needs keeps the per-answer price low for a narrow, repetitive question.
- **D:** Correct. A model no larger than the task needs is the largest single cost lever. In this case: A model no larger than the task needs keeps the per-answer price low for a narrow, repetitive question.

### Question 6 — C

Answer: Put the model identifier in AWS AppConfig and switch it without a deploy. A configuration flag changes the model identifier per request path without shipping new application code. Local study-map skill 1.4 (Model Routing and Provider Abstraction), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. Direct calls from every app scatter keys, quotas, and logging across teams. Why the correct answer wins: A configuration flag changes the model identifier per request path without shipping new application code.
- **B:** Incorrect for this question. A hardcoded identifier forces a code change and a release to try another model. Why the correct answer wins: A configuration flag changes the model identifier per request path without shipping new application code.
- **C:** Correct. In this case: A configuration flag changes the model identifier per request path without shipping new application code.
- **D:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: A configuration flag changes the model identifier per request path without shipping new application code.

### Question 7 — A

Answer: Route the call through Amazon Bedrock cross-Region inference. A cross-Region inference profile spreads traffic so a local capacity shortage does not fail the request. Local study-map skill 1.5 (Resilience and Cross-Region Inference), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Correct. In this case: A cross-Region inference profile spreads traffic so a local capacity shortage does not fail the request.
- **B:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: A cross-Region inference profile spreads traffic so a local capacity shortage does not fail the request.
- **C:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: A cross-Region inference profile spreads traffic so a local capacity shortage does not fail the request.
- **D:** Incorrect for this question. A full fine-tune changes all weights, which is expensive and gives one model per task. Why the correct answer wins: A cross-Region inference profile spreads traffic so a local capacity shortage does not fail the request.

### Question 8 — A

Answer: Fall back to a second model when the first is unavailable. A fallback model keeps the feature answering during a Regional degradation, at a stated quality cost. A fallback keeps the feature available when one model or Region degrades. Local study-map skill 1.5 (Resilience and Cross-Region Inference), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Correct. A fallback keeps the feature available when one model or Region degrades. In this case: A fallback model keeps the feature answering during a Regional degradation, at a stated quality cost.
- **B:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: A fallback model keeps the feature answering during a Regional degradation, at a stated quality cost.
- **C:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: A fallback model keeps the feature answering during a Regional degradation, at a stated quality cost.
- **D:** Incorrect for this question. A key in an environment variable leaks through images, logs, and job definitions. Why the correct answer wins: A fallback model keeps the feature answering during a Regional degradation, at a stated quality cost.

### Question 9 — D

Answer: Pin the model version instead of tracking the latest alias. Pinning the model version keeps behaviour stable until an upgrade is deliberately evaluated. Local study-map skill 1.6 (Customisation Lifecycle and Rollback), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. A full fine-tune changes all weights, which is expensive and gives one model per task. Why the correct answer wins: Pinning the model version keeps behaviour stable until an upgrade is deliberately evaluated.
- **B:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: Pinning the model version keeps behaviour stable until an upgrade is deliberately evaluated.
- **C:** Incorrect for this question. Direct calls from every app scatter keys, quotas, and logging across teams. Why the correct answer wins: Pinning the model version keeps behaviour stable until an upgrade is deliberately evaluated.
- **D:** Correct. In this case: Pinning the model version keeps behaviour stable until an upgrade is deliberately evaluated.

### Question 10 — C

Answer: Enforce freshness and completeness rules with AWS Glue Data Quality. Rule sets score freshness and completeness and stop the batch before anything is embedded. Local study-map skill 1.7 (Data Validation for Model Inputs), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: Rule sets score freshness and completeness and stop the batch before anything is embedded.
- **B:** Incorrect for this question. Structure failures appear in the logs before a downstream parser breaks. Why the correct answer wins: Rule sets score freshness and completeness and stop the batch before anything is embedded.
- **C:** Correct. In this case: Rule sets score freshness and completeness and stop the batch before anything is embedded.
- **D:** Incorrect for this question. Macie finds sensitive data at rest so the corpus can be cleaned before indexing. Why the correct answer wins: Rule sets score freshness and completeness and stop the batch before anything is embedded.

### Question 11 — D

Answer: Extract entities with Amazon Comprehend before indexing. Entity extraction writes product codes and names into metadata so filters can use exact values. Local study-map skill 1.7 (Data Validation for Model Inputs), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. A reformatting pass cleans inconsistent headings and units before embedding. Why the correct answer wins: Entity extraction writes product codes and names into metadata so filters can use exact values.
- **B:** Incorrect for this question. A dialog-shaped request keeps speaker roles and prior turns in the order the model expects. Why the correct answer wins: Entity extraction writes product codes and names into metadata so filters can use exact values.
- **C:** Incorrect for this question. A single blob loses the field boundaries the model needs to answer precisely. Why the correct answer wins: Entity extraction writes product codes and names into metadata so filters can use exact values.
- **D:** Correct. In this case: Entity extraction writes product codes and names into metadata so filters can use exact values.

### Question 12 — A

Answer: Extract the text from scanned pages with Amazon Textract. OCR returns the text and form fields from each scanned page so it can be indexed as text. Local study-map skill 1.8 (Multimodal Ingestion and Processing), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Correct. In this case: OCR returns the text and form fields from each scanned page so it can be indexed as text.
- **B:** Incorrect for this question. A reformatting pass cleans inconsistent headings and units before embedding. Why the correct answer wins: OCR returns the text and form fields from each scanned page so it can be indexed as text.
- **C:** Incorrect for this question. Entity extraction puts product codes and names in metadata for exact filtering. Why the correct answer wins: OCR returns the text and form fields from each scanned page so it can be indexed as text.
- **D:** Incorrect for this question. Transcribe turns speech into timestamped text that retrieval can search. Why the correct answer wins: OCR returns the text and form fields from each scanned page so it can be indexed as text.

### Question 13 — B

Answer: Send the request as the JSON body the model expects. The model API expects the prompt, parameters, and model identifier in one JSON body. Local study-map skill 1.9 (Request Formatting and Enrichment), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. A single blob loses the field boundaries the model needs to answer precisely. Why the correct answer wins: The model API expects the prompt, parameters, and model identifier in one JSON body.
- **B:** Correct. In this case: The model API expects the prompt, parameters, and model identifier in one JSON body.
- **C:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: The model API expects the prompt, parameters, and model identifier in one JSON body.
- **D:** Incorrect for this question. A dialog-shaped request keeps speaker roles and prior turns in the order the model expects. Why the correct answer wins: The model API expects the prompt, parameters, and model identifier in one JSON body.

### Question 14 — B

Answer: Format the turns as an alternating conversation structure. A dialog-shaped request keeps speaker roles and prior turns in the order the model expects. Local study-map skill 1.9 (Request Formatting and Enrichment), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. A single blob loses the field boundaries the model needs to answer precisely. Why the correct answer wins: A dialog-shaped request keeps speaker roles and prior turns in the order the model expects.
- **B:** Correct. In this case: A dialog-shaped request keeps speaker roles and prior turns in the order the model expects.
- **C:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: A dialog-shaped request keeps speaker roles and prior turns in the order the model expects.
- **D:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: A dialog-shaped request keeps speaker roles and prior turns in the order the model expects.

### Question 15 — A

Answer: Keep embeddings and metadata in Amazon DynamoDB. DynamoDB serves key lookups fast and can hold vectors beside their metadata for a compact corpus. Local study-map skill 1.10 (Vector Store Architecture), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Correct. In this case: DynamoDB serves key lookups fast and can hold vectors beside their metadata for a compact corpus.
- **B:** Incorrect for this question. pgvector keeps embeddings beside relational rows so one query can filter and search together. Why the correct answer wins: DynamoDB serves key lookups fast and can hold vectors beside their metadata for a compact corpus.
- **C:** Incorrect for this question. OpenSearch combines vector search with the filtering and sharding of a search engine. Why the correct answer wins: DynamoDB serves key lookups fast and can hold vectors beside their metadata for a compact corpus.
- **D:** Incorrect for this question. Neptune answers relationship traversals that a similarity search cannot express. Why the correct answer wins: DynamoDB serves key lookups fast and can hold vectors beside their metadata for a compact corpus.

### Question 16 — D

Answer: Filter the search by document metadata before the similarity ranking. A metadata filter removes out-of-scope documents so the ranking only sees eligible chunks. Local study-map skill 1.11 (Metadata Frameworks and Index Maintenance), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. More passages raise recall and also lengthen the prompt and the cost per call. Why the correct answer wins: A metadata filter removes out-of-scope documents so the ranking only sees eligible chunks.
- **B:** Incorrect for this question. A threshold keeps marginal passages out of the prompt that would only add noise. Why the correct answer wins: A metadata filter removes out-of-scope documents so the ranking only sees eligible chunks.
- **C:** Incorrect for this question. Expansion bridges vocabulary gaps between how users ask and how documents are written. Why the correct answer wins: A metadata filter removes out-of-scope documents so the ranking only sees eligible chunks.
- **D:** Correct. In this case: A metadata filter removes out-of-scope documents so the ranking only sees eligible chunks.

### Question 17 — D

Answer: Trigger re-indexing from Amazon S3 event notifications. Event notifications start a sync as soon as a document lands or changes, which keeps lag to seconds. Local study-map skill 1.11 (Metadata Frameworks and Index Maintenance), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. Scheduled rebuilds are simple and leave a window in which answers lag the source. Why the correct answer wins: Event notifications start a sync as soon as a document lands or changes, which keeps lag to seconds.
- **B:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: Event notifications start a sync as soon as a document lands or changes, which keeps lag to seconds.
- **C:** Incorrect for this question. Vectors from two different models are not comparable, so the whole index must be rebuilt. Why the correct answer wins: Event notifications start a sync as soon as a document lands or changes, which keeps lag to seconds.
- **D:** Correct. In this case: Event notifications start a sync as soon as a document lands or changes, which keeps lag to seconds.

### Question 18 — B

Answer: Split by document structure into sections and subsections. Structural chunks follow headings, so a retrieved chunk carries a coherent argument. Local study-map skill 1.12 (Chunking and Embedding Strategy), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. Fixed windows are predictable and cheap, and overlap preserves text that straddles a boundary. Why the correct answer wins: Structural chunks follow headings, so a retrieved chunk carries a coherent argument.
- **B:** Correct. In this case: Structural chunks follow headings, so a retrieved chunk carries a coherent argument.
- **C:** Incorrect for this question. Mixing vector spaces silently breaks similarity, because distances no longer mean the same thing. Why the correct answer wins: Structural chunks follow headings, so a retrieved chunk carries a coherent argument.
- **D:** Incorrect for this question. Larger chunks carry more context but dilute the embedding and crowd the prompt window. Why the correct answer wins: Structural chunks follow headings, so a retrieved chunk carries a coherent argument.

### Question 19 — B, E

Answers: Combine keyword and vector retrieval and merge the ranked lists; Rerank the retrieved passages with an Amazon Bedrock reranker. Hybrid retrieval catches the exact identifier and a reranker fixes the order of the shortlist. Hybrid retrieval catches exact identifiers that a vector search alone can miss. A reranker scores the shortlist against the query and lifts precision before the prompt is built. Local study-map skill 1.13 (Hybrid Retrieval and Reranking), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. Mixing vector spaces silently breaks similarity, because distances no longer mean the same thing. Why the correct answer wins: Hybrid retrieval catches the exact identifier and a reranker fixes the order of the shortlist.
- **B:** Correct. Hybrid retrieval catches exact identifiers that a vector search alone can miss. In this case: Hybrid retrieval catches the exact identifier and a reranker fixes the order of the shortlist.
- **C:** Incorrect for this question. More passages raise recall and also lengthen the prompt and the cost per call. Why the correct answer wins: Hybrid retrieval catches the exact identifier and a reranker fixes the order of the shortlist.
- **D:** Incorrect for this question. A threshold keeps marginal passages out of the prompt that would only add noise. Why the correct answer wins: Hybrid retrieval catches the exact identifier and a reranker fixes the order of the shortlist.
- **E:** Correct. A reranker scores the shortlist against the query and lifts precision before the prompt is built. In this case: Hybrid retrieval catches the exact identifier and a reranker fixes the order of the shortlist.

### Question 20 — A

Answer: Index small child chunks and return the larger parent to the model. Parent-child retrieval matches on precise text and supplies surrounding context to the model. Local study-map skill 1.13 (Hybrid Retrieval and Reranking), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Correct. In this case: Parent-child retrieval matches on precise text and supplies surrounding context to the model.
- **B:** Incorrect for this question. More passages raise recall and also lengthen the prompt and the cost per call. Why the correct answer wins: Parent-child retrieval matches on precise text and supplies surrounding context to the model.
- **C:** Incorrect for this question. Fixed windows are predictable and cheap, and overlap preserves text that straddles a boundary. Why the correct answer wins: Parent-child retrieval matches on precise text and supplies surrounding context to the model.
- **D:** Incorrect for this question. Larger chunks carry more context but dilute the embedding and crowd the prompt window. Why the correct answer wins: Parent-child retrieval matches on precise text and supplies surrounding context to the model.

### Question 21 — D

Answer: Rewrite the query using the conversation history first. History-aware rewriting turns a follow-up such as and the second one into a standalone query. Local study-map skill 1.14 (Query Transformation and Handling), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. Domain-tuned embeddings move relevant passages closer for vocabulary the base model misses. Why the correct answer wins: History-aware rewriting turns a follow-up such as and the second one into a standalone query.
- **B:** Incorrect for this question. More passages raise recall and also lengthen the prompt and the cost per call. Why the correct answer wins: History-aware rewriting turns a follow-up such as and the second one into a standalone query.
- **C:** Incorrect for this question. Expansion bridges vocabulary gaps between how users ask and how documents are written. Why the correct answer wins: History-aware rewriting turns a follow-up such as and the second one into a standalone query.
- **D:** Correct. In this case: History-aware rewriting turns a follow-up such as and the second one into a standalone query.

### Question 22 — C

Answer: Put the role, tone, and boundaries in the system prompt. The system prompt sets behaviour once and outranks stray instructions in the user turn. Local study-map skill 1.15 (Prompt Engineering and Governance), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: The system prompt sets behaviour once and outranks stray instructions in the user turn.
- **B:** Incorrect for this question. A token cap bounds the cost of a runaway answer and the latency of every call. Why the correct answer wins: The system prompt sets behaviour once and outranks stray instructions in the user turn.
- **C:** Correct. In this case: The system prompt sets behaviour once and outranks stray instructions in the user turn.
- **D:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: The system prompt sets behaviour once and outranks stray instructions in the user turn.

### Question 23 — B

Answer: Constrain the response with a JSON schema. A schema makes the output machine-parseable and rejects prose that breaks the contract. Local study-map skill 1.15 (Prompt Engineering and Governance), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. A token cap bounds the cost of a runaway answer and the latency of every call. Why the correct answer wins: A schema makes the output machine-parseable and rejects prose that breaks the contract.
- **B:** Correct. In this case: A schema makes the output machine-parseable and rejects prose that breaks the contract.
- **C:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: A schema makes the output machine-parseable and rejects prose that breaks the contract.
- **D:** Incorrect for this question. A single blob loses the field boundaries the model needs to answer precisely. Why the correct answer wins: A schema makes the output machine-parseable and rejects prose that breaks the contract.

### Question 24 — D

Answer: Keep conversation and task memory in Amazon DynamoDB. DynamoDB gives the agent a durable per-session store keyed by session identifier. Local study-map skill 2.1 (Agent Memory and State), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: DynamoDB gives the agent a durable per-session store keyed by session identifier.
- **B:** Incorrect for this question. Prompt-only memory forgets everything the moment the context window is trimmed. Why the correct answer wins: DynamoDB gives the agent a durable per-session store keyed by session identifier.
- **C:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: DynamoDB gives the agent a durable per-session store keyed by session identifier.
- **D:** Correct. In this case: DynamoDB gives the agent a durable per-session store keyed by session identifier.

### Question 25 — A

Answer: Run the agent on Amazon Bedrock AgentCore. AgentCore supplies managed runtime, identity, memory, and observability for agents. Local study-map skill 2.1 (Agent Memory and State), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Correct. In this case: AgentCore supplies managed runtime, identity, memory, and observability for agents.
- **B:** Incorrect for this question. A Lambda tool is stateless, cheap at low volume, and scales per request. Why the correct answer wins: AgentCore supplies managed runtime, identity, memory, and observability for agents.
- **C:** Incorrect for this question. Prompt-only memory forgets everything the moment the context window is trimmed. Why the correct answer wins: AgentCore supplies managed runtime, identity, memory, and observability for agents.
- **D:** Incorrect for this question. Direct calls from every app scatter keys, quotas, and logging across teams. Why the correct answer wins: AgentCore supplies managed runtime, identity, memory, and observability for agents.

### Question 26 — D

Answer: Build the agent with Strands Agents. Strands gives an open-source agent loop with tools, memory, and model-agnostic wiring. Local study-map skill 2.2 (Agent Orchestration Patterns), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: Strands gives an open-source agent loop with tools, memory, and model-agnostic wiring.
- **B:** Incorrect for this question. A synchronous call is simplest and makes the user wait for the final token. Why the correct answer wins: Strands gives an open-source agent loop with tools, memory, and model-agnostic wiring.
- **C:** Incorrect for this question. One agent with every tool makes tool choice ambiguous and permissions broad. Why the correct answer wins: Strands gives an open-source agent loop with tools, memory, and model-agnostic wiring.
- **D:** Correct. In this case: Strands gives an open-source agent loop with tools, memory, and model-agnostic wiring.

### Question 27 — D, E

Answers: Set an explicit step and budget limit on the agent loop; Coordinate the steps in AWS Step Functions. A hard limit ends a non-converging loop and a state machine makes each step visible and retryable. A hard limit stops a loop that would otherwise consume tokens without converging. A state machine keeps multi-step work ordered, retryable, and auditable. Local study-map skill 2.2 (Agent Orchestration Patterns), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: A hard limit ends a non-converging loop and a state machine makes each step visible and retryable.
- **B:** Incorrect for this question. One agent with every tool makes tool choice ambiguous and permissions broad. Why the correct answer wins: A hard limit ends a non-converging loop and a state machine makes each step visible and retryable.
- **C:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: A hard limit ends a non-converging loop and a state machine makes each step visible and retryable.
- **D:** Correct. A hard limit stops a loop that would otherwise consume tokens without converging. In this case: A hard limit ends a non-converging loop and a state machine makes each step visible and retryable.
- **E:** Correct. A state machine keeps multi-step work ordered, retryable, and auditable. In this case: A hard limit ends a non-converging loop and a state machine makes each step visible and retryable.

### Question 28 — B

Answer: Validate tool arguments against a schema before calling. Schema validation rejects a malformed argument instead of sending it to the system of record. Local study-map skill 2.3 (Tool Reliability and Safeguards), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: Schema validation rejects a malformed argument instead of sending it to the system of record.
- **B:** Correct. In this case: Schema validation rejects a malformed argument instead of sending it to the system of record.
- **C:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: Schema validation rejects a malformed argument instead of sending it to the system of record.
- **D:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: Schema validation rejects a malformed argument instead of sending it to the system of record.

### Question 29 — C

Answer: Bound each tool call with a timeout and a fallback. A timeout keeps one slow dependency from stalling the whole agent turn. Local study-map skill 2.3 (Tool Reliability and Safeguards), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: A timeout keeps one slow dependency from stalling the whole agent turn.
- **B:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: A timeout keeps one slow dependency from stalling the whole agent turn.
- **C:** Correct. In this case: A timeout keeps one slow dependency from stalling the whole agent turn.
- **D:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: A timeout keeps one slow dependency from stalling the whole agent turn.

### Question 30 — A

Answer: Buy Amazon Bedrock provisioned throughput for the model. Provisioned throughput reserves model units and gives a predictable token-per-minute ceiling. Local study-map skill 2.4 (Foundation Model Deployment and Capacity), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Correct. In this case: Provisioned throughput reserves model units and gives a predictable token-per-minute ceiling.
- **B:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: Provisioned throughput reserves model units and gives a predictable token-per-minute ceiling.
- **C:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: Provisioned throughput reserves model units and gives a predictable token-per-minute ceiling.
- **D:** Incorrect for this question. On-demand Bedrock inference bills per token with no committed capacity, which suits spiky or unproven demand. Why the correct answer wins: Provisioned throughput reserves model units and gives a predictable token-per-minute ceiling.

### Question 31 — A, C

Answers: Set per-client throttling at the API layer; Buffer the work in an Amazon SQS queue. A per-client quota protects shared capacity and a queue absorbs the burst instead of failing it. A per-client quota protects shared model capacity from one noisy caller. A queue absorbs bursts and lets a worker retry a failed model call. Local study-map skill 2.4 (Foundation Model Deployment and Capacity), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Correct. A per-client quota protects shared model capacity from one noisy caller. In this case: A per-client quota protects shared capacity and a queue absorbs the burst instead of failing it.
- **B:** Incorrect for this question. On-demand Bedrock inference bills per token with no committed capacity, which suits spiky or unproven demand. Why the correct answer wins: A per-client quota protects shared capacity and a queue absorbs the burst instead of failing it.
- **C:** Correct. A queue absorbs bursts and lets a worker retry a failed model call. In this case: A per-client quota protects shared capacity and a queue absorbs the burst instead of failing it.
- **D:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: A per-client quota protects shared capacity and a queue absorbs the burst instead of failing it.
- **E:** Incorrect for this question. A synchronous call is simplest and makes the user wait for the final token. Why the correct answer wins: A per-client quota protects shared capacity and a queue absorbs the burst instead of failing it.

### Question 32 — A

Answer: Route domain events through Amazon EventBridge. EventBridge decouples producers from the GenAI consumer with rules and filtering. Local study-map skill 2.5 (Enterprise Integration Patterns), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Correct. In this case: EventBridge decouples producers from the GenAI consumer with rules and filtering.
- **B:** Incorrect for this question. SNS delivers one event to many subscribers without the caller tracking them. Why the correct answer wins: EventBridge decouples producers from the GenAI consumer with rules and filtering.
- **C:** Incorrect for this question. AppFlow copies data from supported SaaS sources without custom connectors. Why the correct answer wins: EventBridge decouples producers from the GenAI consumer with rules and filtering.
- **D:** Incorrect for this question. A queue absorbs bursts and lets a worker retry a failed model call. Why the correct answer wins: EventBridge decouples producers from the GenAI consumer with rules and filtering.

### Question 33 — D

Answer: Buffer the work in an Amazon SQS queue. A queue absorbs bursts and lets a worker retry a failed model call. Local study-map skill 2.5 (Enterprise Integration Patterns), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. SNS delivers one event to many subscribers without the caller tracking them. Why the correct answer wins: A queue absorbs bursts and lets a worker retry a failed model call.
- **B:** Incorrect for this question. API Gateway adds authentication, throttling, request validation, and streaming to the model call. Why the correct answer wins: A queue absorbs bursts and lets a worker retry a failed model call.
- **C:** Incorrect for this question. A synchronous call is simplest and makes the user wait for the final token. Why the correct answer wins: A queue absorbs bursts and lets a worker retry a failed model call.
- **D:** Correct. In this case: A queue absorbs bursts and lets a worker retry a failed model call.

### Question 34 — B

Answer: Give the task an IAM role scoped to the resources it uses. A scoped role issues temporary credentials with only the needed permissions. Local study-map skill 2.6 (Identity for Model Access), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. A key in an environment variable leaks through images, logs, and job definitions. Why the correct answer wins: A scoped role issues temporary credentials with only the needed permissions.
- **B:** Correct. In this case: A scoped role issues temporary credentials with only the needed permissions.
- **C:** Incorrect for this question. Transfer Family accepts SFTP uploads into S3 without a server to run. Why the correct answer wins: A scoped role issues temporary credentials with only the needed permissions.
- **D:** Incorrect for this question. A public bucket exposes the corpus to everyone the index was meant to constrain. Why the correct answer wins: A scoped role issues temporary credentials with only the needed permissions.

### Question 35 — D

Answer: Put one internal GenAI gateway in front of every model call. A gateway centralises credentials, quotas, logging, and model routing for all teams. Local study-map skill 2.7 (CI/CD and GenAI Gateway), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. Direct calls from every app scatter keys, quotas, and logging across teams. Why the correct answer wins: A gateway centralises credentials, quotas, logging, and model routing for all teams.
- **B:** Incorrect for this question. A hardcoded identifier forces a code change and a release to try another model. Why the correct answer wins: A gateway centralises credentials, quotas, logging, and model routing for all teams.
- **C:** Incorrect for this question. A key in an environment variable leaks through images, logs, and job definitions. Why the correct answer wins: A gateway centralises credentials, quotas, logging, and model routing for all teams.
- **D:** Correct. In this case: A gateway centralises credentials, quotas, logging, and model routing for all teams.

### Question 36 — B, C

Answers: Release the assistant through AWS CodePipeline; Run the evaluation suite in AWS CodeBuild. A pipeline ties the stages together and the build runs the evaluation suite before deployment. A pipeline ties source, build, test, and deploy into one auditable flow. CodeBuild runs the tests and quality gates as part of the release. Local study-map skill 2.7 (CI/CD and GenAI Gateway), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: A pipeline ties the stages together and the build runs the evaluation suite before deployment.
- **B:** Correct. CodeBuild runs the tests and quality gates as part of the release. In this case: A pipeline ties the stages together and the build runs the evaluation suite before deployment.
- **C:** Correct. A pipeline ties source, build, test, and deploy into one auditable flow. In this case: A pipeline ties the stages together and the build runs the evaluation suite before deployment.
- **D:** Incorrect for this question. Direct calls from every app scatter keys, quotas, and logging across teams. Why the correct answer wins: A pipeline ties the stages together and the build runs the evaluation suite before deployment.
- **E:** Incorrect for this question. A key in an environment variable leaks through images, logs, and job definitions. Why the correct answer wins: A pipeline ties the stages together and the build runs the evaluation suite before deployment.

### Question 37 — C

Answer: Stream tokens as server-sent events. Streaming lowers perceived latency without changing total generation time. Server-sent events deliver incremental text over ordinary HTTP. Local study-map skill 2.8 (Streaming and Asynchronous APIs), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. A synchronous call is simplest and makes the user wait for the final token. Why the correct answer wins: Streaming lowers perceived latency without changing total generation time.
- **B:** Incorrect for this question. Asynchronous processing suits long generations that outlast an API timeout. Why the correct answer wins: Streaming lowers perceived latency without changing total generation time.
- **C:** Correct. Server-sent events deliver incremental text over ordinary HTTP. In this case: Streaming lowers perceived latency without changing total generation time.
- **D:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: Streaming lowers perceived latency without changing total generation time.

### Question 38 — D

Answer: Retry throttled calls with exponential backoff and jitter. Backoff with jitter spreads retries so a throttled client does not stampede the service. Local study-map skill 2.9 (API Resilience and Backoff), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. A circuit breaker stops sending traffic to a dependency that is already failing. Why the correct answer wins: Backoff with jitter spreads retries so a throttled client does not stampede the service.
- **B:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: Backoff with jitter spreads retries so a throttled client does not stampede the service.
- **C:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: Backoff with jitter spreads retries so a throttled client does not stampede the service.
- **D:** Correct. In this case: Backoff with jitter spreads retries so a throttled client does not stampede the service.

### Question 39 — A

Answer: Open a circuit breaker after repeated dependency failures. A circuit breaker stops sending traffic to a dependency that is already failing. Local study-map skill 2.9 (API Resilience and Backoff), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Correct. In this case: A circuit breaker stops sending traffic to a dependency that is already failing.
- **B:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: A circuit breaker stops sending traffic to a dependency that is already failing.
- **C:** Incorrect for this question. A synchronous call is simplest and makes the user wait for the final token. Why the correct answer wins: A circuit breaker stops sending traffic to a dependency that is already failing.
- **D:** Incorrect for this question. Backoff with jitter spreads retries so a throttled client does not stampede the service. Why the correct answer wins: A circuit breaker stops sending traffic to a dependency that is already failing.

### Question 40 — C

Answer: Front the model with Amazon API Gateway. API Gateway adds authentication, throttling, request validation, and streaming to the model call. Local study-map skill 2.10 (Application Integration and Low Code), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. An edge cache answers identical requests without reaching the model. Why the correct answer wins: API Gateway adds authentication, throttling, request validation, and streaming to the model call.
- **B:** Incorrect for this question. Amplify supplies declarative UI and hosting for the client that talks to the assistant. Why the correct answer wins: API Gateway adds authentication, throttling, request validation, and streaming to the model call.
- **C:** Correct. In this case: API Gateway adds authentication, throttling, request validation, and streaming to the model call.
- **D:** Incorrect for this question. Direct calls from every app scatter keys, quotas, and logging across teams. Why the correct answer wins: API Gateway adds authentication, throttling, request validation, and streaming to the model call.

### Question 41 — B

Answer: Build the interface with AWS Amplify. Amplify supplies declarative UI and hosting for the client that talks to the assistant. Local study-map skill 2.10 (Application Integration and Low Code), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. Server-sent events deliver incremental text over ordinary HTTP. Why the correct answer wins: Amplify supplies declarative UI and hosting for the client that talks to the assistant.
- **B:** Correct. In this case: Amplify supplies declarative UI and hosting for the client that talks to the assistant.
- **C:** Incorrect for this question. Edge logic trims, redacts, or routes a request before it crosses to the model Region. Why the correct answer wins: Amplify supplies declarative UI and hosting for the client that talks to the assistant.
- **D:** Incorrect for this question. API Gateway adds authentication, throttling, request validation, and streaming to the model call. Why the correct answer wins: Amplify supplies declarative UI and hosting for the client that talks to the assistant.

### Question 42 — C

Answer: Generate and explain the integration code with Amazon Q Developer. Q Developer drafts and explains SDK calls inside the editor, which speeds up the plumbing. Local study-map skill 2.11 (Developer Productivity Tooling), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: Q Developer drafts and explains SDK calls inside the editor, which speeds up the plumbing.
- **B:** Incorrect for this question. A pipeline ties source, build, test, and deploy into one auditable flow. Why the correct answer wins: Q Developer drafts and explains SDK calls inside the editor, which speeds up the plumbing.
- **C:** Correct. In this case: Q Developer drafts and explains SDK calls inside the editor, which speeds up the plumbing.
- **D:** Incorrect for this question. CodeBuild runs the tests and quality gates as part of the release. Why the correct answer wins: Q Developer drafts and explains SDK calls inside the editor, which speeds up the plumbing.

### Question 43 — C

Answer: Trace the request across services with AWS X-Ray. A trace shows which hop in the chain added the latency. Local study-map skill 2.12 (Integration Troubleshooting), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: A trace shows which hop in the chain added the latency.
- **B:** Incorrect for this question. Logs Insights correlates a spike in errors with the prompts that caused it. Why the correct answer wins: A trace shows which hop in the chain added the latency.
- **C:** Correct. In this case: A trace shows which hop in the chain added the latency.
- **D:** Incorrect for this question. CloudTrail records who changed models, keys, and guardrails. Why the correct answer wins: A trace shows which hop in the chain added the latency.

### Question 44 — B

Answer: Apply Amazon Bedrock Guardrails content filters. Content filters score and block harmful input and output on the request path. Local study-map skill 3.1 (Content Safety Controls), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: Content filters score and block harmful input and output on the request path.
- **B:** Correct. In this case: Content filters score and block harmful input and output on the request path.
- **C:** Incorrect for this question. Low temperature narrows sampling so repeatable factual answers stay stable. Why the correct answer wins: Content filters score and block harmful input and output on the request path.
- **D:** Incorrect for this question. A token cap bounds the cost of a runaway answer and the latency of every call. Why the correct answer wins: Content filters score and block harmful input and output on the request path.

### Question 45 — D, E

Answers: Define denied topics in Amazon Bedrock Guardrails; Enable sensitive-information filters in Amazon Bedrock Guardrails. Denied topics refuse the ruled-out subjects and the sensitive-information filter masks personal data. Denied topics refuse the subject areas the business has ruled out. PII filters detect and mask personal data in prompts and responses. Local study-map skill 3.1 (Content Safety Controls), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: Denied topics refuse the ruled-out subjects and the sensitive-information filter masks personal data.
- **B:** Incorrect for this question. A token cap bounds the cost of a runaway answer and the latency of every call. Why the correct answer wins: Denied topics refuse the ruled-out subjects and the sensitive-information filter masks personal data.
- **C:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: Denied topics refuse the ruled-out subjects and the sensitive-information filter masks personal data.
- **D:** Correct. PII filters detect and mask personal data in prompts and responses. In this case: Denied topics refuse the ruled-out subjects and the sensitive-information filter masks personal data.
- **E:** Correct. Denied topics refuse the subject areas the business has ruled out. In this case: Denied topics refuse the ruled-out subjects and the sensitive-information filter masks personal data.

### Question 46 — B

Answer: Require the answer to cite the retrieved passage. A citation makes each claim traceable to a source the reader can check. Local study-map skill 3.2 (Grounding and Hallucination Reduction), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. An escalation path keeps consequential answers with a human owner. Why the correct answer wins: A citation makes each claim traceable to a source the reader can check.
- **B:** Correct. In this case: A citation makes each claim traceable to a source the reader can check.
- **C:** Incorrect for this question. A score lets the interface route low-confidence answers to a human. Why the correct answer wins: A citation makes each claim traceable to a source the reader can check.
- **D:** Incorrect for this question. A token cap bounds the cost of a runaway answer and the latency of every call. Why the correct answer wins: A citation makes each claim traceable to a source the reader can check.

### Question 47 — B

Answer: Enable the contextual grounding check in Guardrails. The grounding check compares the response with the retrieved source and flags unsupported claims. Local study-map skill 3.2 (Grounding and Hallucination Reduction), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. Low temperature narrows sampling so repeatable factual answers stay stable. Why the correct answer wins: The grounding check compares the response with the retrieved source and flags unsupported claims.
- **B:** Correct. In this case: The grounding check compares the response with the retrieved source and flags unsupported claims.
- **C:** Incorrect for this question. A schema makes the output machine-parseable and rejects prose that breaks the contract. Why the correct answer wins: The grounding check compares the response with the retrieved source and flags unsupported claims.
- **D:** Incorrect for this question. Similarity scoring is fast and tolerant of wording, but blind to a contradicted fact. Why the correct answer wins: The grounding check compares the response with the retrieved source and flags unsupported claims.

### Question 48 — B

Answer: Screen inputs for instruction override and jailbreak patterns. A pre-filter catches text that tries to replace the system instruction. Local study-map skill 3.3 (Prompt Injection Defence), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. A token cap bounds the cost of a runaway answer and the latency of every call. Why the correct answer wins: A pre-filter catches text that tries to replace the system instruction.
- **B:** Correct. In this case: A pre-filter catches text that tries to replace the system instruction.
- **C:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: A pre-filter catches text that tries to replace the system instruction.
- **D:** Incorrect for this question. Low temperature narrows sampling so repeatable factual answers stay stable. Why the correct answer wins: A pre-filter catches text that tries to replace the system instruction.

### Question 49 — C

Answer: Strip control text and delimiters from retrieved content. Sanitising retrieved text stops it from being parsed as an instruction. Local study-map skill 3.3 (Prompt Injection Defence), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: Sanitising retrieved text stops it from being parsed as an instruction.
- **B:** Incorrect for this question. Domain-tuned embeddings move relevant passages closer for vocabulary the base model misses. Why the correct answer wins: Sanitising retrieved text stops it from being parsed as an instruction.
- **C:** Correct. In this case: Sanitising retrieved text stops it from being parsed as an instruction.
- **D:** Incorrect for this question. A schema makes the output machine-parseable and rejects prose that breaks the contract. Why the correct answer wins: Sanitising retrieved text stops it from being parsed as an instruction.

### Question 50 — C

Answer: Mask personal data before the prompt is built. Masking at the boundary keeps personal data out of the model request entirely. Local study-map skill 3.4 (Privacy and PII Protection), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. Macie finds sensitive data at rest so the corpus can be cleaned before indexing. Why the correct answer wins: Masking at the boundary keeps personal data out of the model request entirely.
- **B:** Incorrect for this question. PII filters detect and mask personal data in prompts and responses. Why the correct answer wins: Masking at the boundary keeps personal data out of the model request entirely.
- **C:** Correct. In this case: Masking at the boundary keeps personal data out of the model request entirely.
- **D:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: Masking at the boundary keeps personal data out of the model request entirely.

### Question 51 — A, C

Answers: Detect personal data with Amazon Comprehend; Scan the data store with Amazon Macie. Comprehend identifies the entities and Macie finds sensitive data at rest in the store. Comprehend identifies entities and PII so they can be masked before the model sees them. Macie finds sensitive data at rest so the corpus can be cleaned before indexing. Local study-map skill 3.4 (Privacy and PII Protection), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Correct. Macie finds sensitive data at rest so the corpus can be cleaned before indexing. In this case: Comprehend identifies the entities and Macie finds sensitive data at rest in the store.
- **B:** Incorrect for this question. A key in an environment variable leaks through images, logs, and job definitions. Why the correct answer wins: Comprehend identifies the entities and Macie finds sensitive data at rest in the store.
- **C:** Correct. Comprehend identifies entities and PII so they can be masked before the model sees them. In this case: Comprehend identifies the entities and Macie finds sensitive data at rest in the store.
- **D:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: Comprehend identifies the entities and Macie finds sensitive data at rest in the store.
- **E:** Incorrect for this question. Content filters score and block harmful input and output on the request path. Why the correct answer wins: Comprehend identifies the entities and Macie finds sensitive data at rest in the store.

### Question 52 — D

Answer: Call the model through an interface VPC endpoint. A private endpoint keeps model traffic off the public internet. Local study-map skill 3.5 (Network and Data Isolation), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. A key in an environment variable leaks through images, logs, and job definitions. Why the correct answer wins: A private endpoint keeps model traffic off the public internet.
- **B:** Incorrect for this question. A public bucket exposes the corpus to everyone the index was meant to constrain. Why the correct answer wins: A private endpoint keeps model traffic off the public internet.
- **C:** Incorrect for this question. An edge cache answers identical requests without reaching the model. Why the correct answer wins: A private endpoint keeps model traffic off the public internet.
- **D:** Correct. In this case: A private endpoint keeps model traffic off the public internet.

### Question 53 — D

Answer: Deploy the workload in private subnets. Private subnets remove inbound internet routing from the compute tier. Local study-map skill 3.5 (Network and Data Isolation), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. A public bucket exposes the corpus to everyone the index was meant to constrain. Why the correct answer wins: Private subnets remove inbound internet routing from the compute tier.
- **B:** Incorrect for this question. An edge cache answers identical requests without reaching the model. Why the correct answer wins: Private subnets remove inbound internet routing from the compute tier.
- **C:** Incorrect for this question. Direct calls from every app scatter keys, quotas, and logging across teams. Why the correct answer wins: Private subnets remove inbound internet routing from the compute tier.
- **D:** Correct. In this case: Private subnets remove inbound internet routing from the compute tier.

### Question 54 — A

Answer: Record control-plane activity in AWS CloudTrail. CloudTrail records who changed models, keys, and guardrails. Local study-map skill 3.6 (Governance, Lineage, and Audit), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Correct. In this case: CloudTrail records who changed models, keys, and guardrails.
- **B:** Incorrect for this question. Invocation logs capture the request, the response, and the token counts. Why the correct answer wins: CloudTrail records who changed models, keys, and guardrails.
- **C:** Incorrect for this question. Grafana combines model, infrastructure, and business metrics on one screen. Why the correct answer wins: CloudTrail records who changed models, keys, and guardrails.
- **D:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: CloudTrail records who changed models, keys, and guardrails.

### Question 55 — B, E

Answers: Record data lineage in the AWS Glue Data Catalog; Pin the model version instead of tracking the latest alias. Lineage ties the answer to its corpus version and the pinned model identifies the generator. Lineage shows which corpus and version produced an answer. A pinned version keeps behaviour stable until an upgrade is evaluated. Local study-map skill 3.6 (Governance, Lineage, and Audit), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: Lineage ties the answer to its corpus version and the pinned model identifies the generator.
- **B:** Correct. A pinned version keeps behaviour stable until an upgrade is evaluated. In this case: Lineage ties the answer to its corpus version and the pinned model identifies the generator.
- **C:** Incorrect for this question. A key in an environment variable leaks through images, logs, and job definitions. Why the correct answer wins: Lineage ties the answer to its corpus version and the pinned model identifies the generator.
- **D:** Incorrect for this question. Low temperature narrows sampling so repeatable factual answers stay stable. Why the correct answer wins: Lineage ties the answer to its corpus version and the pinned model identifies the generator.
- **E:** Correct. Lineage shows which corpus and version produced an answer. In this case: Lineage ties the answer to its corpus version and the pinned model identifies the generator.

### Question 56 — A

Answer: Publish a model card with the model version. A model card documents intended use and known limits for reviewers. Local study-map skill 3.7 (Responsible AI and Transparency), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Correct. In this case: A model card documents intended use and known limits for reviewers.
- **B:** Incorrect for this question. A schema makes the output machine-parseable and rejects prose that breaks the contract. Why the correct answer wins: A model card documents intended use and known limits for reviewers.
- **C:** Incorrect for this question. A Bedrock evaluation job scores candidate models on your prompts and metrics before you choose. Why the correct answer wins: A model card documents intended use and known limits for reviewers.
- **D:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: A model card documents intended use and known limits for reviewers.

### Question 57 — A

Answer: Escalate low-confidence or high-impact answers to a person. An escalation path keeps consequential answers with a human owner. Local study-map skill 3.7 (Responsible AI and Transparency), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Correct. In this case: An escalation path keeps consequential answers with a human owner.
- **B:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: An escalation path keeps consequential answers with a human owner.
- **C:** Incorrect for this question. A token cap bounds the cost of a runaway answer and the latency of every call. Why the correct answer wins: An escalation path keeps consequential answers with a human owner.
- **D:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: An escalation path keeps consequential answers with a human owner.

### Question 58 — B

Answer: Alert when fairness metrics move beyond a band. A drift alert catches a fairness regression after a model or prompt change. Local study-map skill 3.8 (Fairness and Compliance Monitoring), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. Segment metrics expose a quality gap that an overall average hides. Why the correct answer wins: A drift alert catches a fairness regression after a model or prompt change.
- **B:** Correct. In this case: A drift alert catches a fairness regression after a model or prompt change.
- **C:** Incorrect for this question. Anomaly detection finds an unexpected token bill without a fixed threshold. Why the correct answer wins: A drift alert catches a fairness regression after a model or prompt change.
- **D:** Incorrect for this question. A latency alarm fires on the symptom users feel. Why the correct answer wins: A drift alert catches a fairness regression after a model or prompt change.

### Question 59 — A

Answer: Prune older turns from the context window. Dropping stale turns cuts input tokens without losing the current instruction. Local study-map skill 4.1 (Token Cost Efficiency), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Correct. In this case: Dropping stale turns cuts input tokens without losing the current instruction.
- **B:** Incorrect for this question. Larger chunks carry more context but dilute the embedding and crowd the prompt window. Why the correct answer wins: Dropping stale turns cuts input tokens without losing the current instruction.
- **C:** Incorrect for this question. More passages raise recall and also lengthen the prompt and the cost per call. Why the correct answer wins: Dropping stale turns cuts input tokens without losing the current instruction.
- **D:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: Dropping stale turns cuts input tokens without losing the current instruction.

### Question 60 — C

Answer: Summarise the conversation before adding more turns. A running summary keeps long sessions inside the window at low token cost. Local study-map skill 4.1 (Token Cost Efficiency), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Incorrect for this question. A single blob loses the field boundaries the model needs to answer precisely. Why the correct answer wins: A running summary keeps long sessions inside the window at low token cost.
- **B:** Incorrect for this question. More passages raise recall and also lengthen the prompt and the cost per call. Why the correct answer wins: A running summary keeps long sessions inside the window at low token cost.
- **C:** Correct. In this case: A running summary keeps long sessions inside the window at low token cost.
- **D:** Incorrect for this question. Larger chunks carry more context but dilute the embedding and crowd the prompt window. Why the correct answer wins: A running summary keeps long sessions inside the window at low token cost.

### Question 61 — C

Answer: Cache answers by embedding similarity to earlier questions. A semantic cache serves a near-duplicate question without a model call. Local study-map skill 4.2 (Model Tiering and Caching), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: A semantic cache serves a near-duplicate question without a model call.
- **B:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: A semantic cache serves a near-duplicate question without a model call.
- **C:** Correct. In this case: A semantic cache serves a near-duplicate question without a model call.
- **D:** Incorrect for this question. A hash cache is exact and avoids a false hit between similar questions. Why the correct answer wins: A semantic cache serves a near-duplicate question without a model call.

### Question 62 — D, E

Answers: Send routine prompts to a small model and hard prompts to a large one; Cache the response under a hash of the normalised request. Routing sends easy prompts to a small model and an exact cache removes repeat calls entirely. Tiered routing spends the large model only on the requests that need it. A hash cache is exact and avoids a false hit between similar questions. Local study-map skill 4.2 (Model Tiering and Caching), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: Routing sends easy prompts to a small model and an exact cache removes repeat calls entirely.
- **B:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: Routing sends easy prompts to a small model and an exact cache removes repeat calls entirely.
- **C:** Incorrect for this question. A full fine-tune changes all weights, which is expensive and gives one model per task. Why the correct answer wins: Routing sends easy prompts to a small model and an exact cache removes repeat calls entirely.
- **D:** Correct. A hash cache is exact and avoids a false hit between similar questions. In this case: Routing sends easy prompts to a small model and an exact cache removes repeat calls entirely.
- **E:** Correct. Tiered routing spends the large model only on the requests that need it. In this case: Routing sends easy prompts to a small model and an exact cache removes repeat calls entirely.

### Question 63 — D

Answer: Stream tokens as they are generated. Streaming lowers perceived latency without changing total generation time. Local study-map skill 4.3 (Throughput and Latency Optimisation), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Incorrect for this question. A synchronous call is simplest and makes the user wait for the final token. Why the correct answer wins: Streaming lowers perceived latency without changing total generation time.
- **B:** Incorrect for this question. Batch inference trades turnaround time for a lower price on large offline volumes. Why the correct answer wins: Streaming lowers perceived latency without changing total generation time.
- **C:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: Streaming lowers perceived latency without changing total generation time.
- **D:** Correct. In this case: Streaming lowers perceived latency without changing total generation time.

### Question 64 — C, E

Answers: Issue independent model calls in parallel; Choose a lower-latency model for the interactive path. Parallel calls cut wall-clock time and a latency-optimised model shortens each call. Parallel calls cut wall-clock time for sub-tasks that do not depend on each other. A smaller or latency-optimised model answers faster at some quality cost. Local study-map skill 4.3 (Throughput and Latency Optimisation), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: Parallel calls cut wall-clock time and a latency-optimised model shortens each call.
- **B:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: Parallel calls cut wall-clock time and a latency-optimised model shortens each call.
- **C:** Correct. Parallel calls cut wall-clock time for sub-tasks that do not depend on each other. In this case: Parallel calls cut wall-clock time and a latency-optimised model shortens each call.
- **D:** Incorrect for this question. Batch inference trades turnaround time for a lower price on large offline volumes. Why the correct answer wins: Parallel calls cut wall-clock time and a latency-optimised model shortens each call.
- **E:** Correct. A smaller or latency-optimised model answers faster at some quality cost. In this case: Parallel calls cut wall-clock time and a latency-optimised model shortens each call.

### Question 65 — B

Answer: Turn on Amazon Bedrock model invocation logging. Invocation logs capture the request, the response, and the token counts. Local study-map skill 4.4 (GenAI Observability), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Incorrect for this question. CloudTrail records who changed models, keys, and guardrails. Why the correct answer wins: Invocation logs capture the request, the response, and the token counts.
- **B:** Correct. In this case: Invocation logs capture the request, the response, and the token counts.
- **C:** Incorrect for this question. A model card documents intended use and known limits for reviewers. Why the correct answer wins: Invocation logs capture the request, the response, and the token counts.
- **D:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: Invocation logs capture the request, the response, and the token counts.

### Question 66 — A, E

Answers: Publish token usage as CloudWatch metrics; Alarm on p95 latency and error rate. Token metrics show where spend comes from and a latency alarm fires on the symptom users feel. Local study-map skill 4.4 (GenAI Observability), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Correct. In this case: Token metrics show where spend comes from and a latency alarm fires on the symptom users feel.
- **B:** Incorrect for this question. Anomaly detection finds an unexpected token bill without a fixed threshold. Why the correct answer wins: Token metrics show where spend comes from and a latency alarm fires on the symptom users feel.
- **C:** Incorrect for this question. A model card documents intended use and known limits for reviewers. Why the correct answer wins: Token metrics show where spend comes from and a latency alarm fires on the symptom users feel.
- **D:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: Token metrics show where spend comes from and a latency alarm fires on the symptom users feel.
- **E:** Correct. In this case: Token metrics show where spend comes from and a latency alarm fires on the symptom users feel.

### Question 67 — C

Answer: Break down spend by application tag in AWS Cost Explorer. Tag-based cost views attribute the token bill to the team that caused it. Local study-map skill 4.5 (Cost Attribution and Governance), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: Tag-based cost views attribute the token bill to the team that caused it.
- **B:** Incorrect for this question. A Savings Plan discounts the predictable part of the compute baseline. Why the correct answer wins: Tag-based cost views attribute the token bill to the team that caused it.
- **C:** Correct. In this case: Tag-based cost views attribute the token bill to the team that caused it.
- **D:** Incorrect for this question. Anomaly detection finds an unexpected token bill without a fixed threshold. Why the correct answer wins: Tag-based cost views attribute the token bill to the team that caused it.

### Question 68 — C

Answer: Measure whether each claim is supported by the retrieved context. A faithfulness check separates a grounded answer from a fluent invention. Local study-map skill 5.1 (GenAI Evaluation Metrics), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Incorrect for this question. Relevance separates an off-topic answer from a factually wrong one. Why the correct answer wins: A faithfulness check separates a grounded answer from a fluent invention.
- **B:** Incorrect for this question. Embedding-based similarity credits a correct paraphrase that word overlap misses. Why the correct answer wins: A faithfulness check separates a grounded answer from a fluent invention.
- **C:** Correct. In this case: A faithfulness check separates a grounded answer from a fluent invention.
- **D:** Incorrect for this question. Overlap metrics are cheap and reward wording that matches the references. Why the correct answer wins: A faithfulness check separates a grounded answer from a fluent invention.

### Question 69 — D, E

Answers: Report BERTScore for semantic similarity to the reference; Score how directly the answer addresses the question. Embedding similarity credits a correct paraphrase and relevance measures whether the answer addresses the question. Embedding-based similarity credits a correct paraphrase that word overlap misses. Relevance separates an off-topic answer from a factually wrong one. Local study-map skill 5.1 (GenAI Evaluation Metrics), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Incorrect for this question. Overlap metrics are cheap and reward wording that matches the references. Why the correct answer wins: Embedding similarity credits a correct paraphrase and relevance measures whether the answer addresses the question.
- **B:** Incorrect for this question. Recall shows whether the answer was missing evidence before generation began. Why the correct answer wins: Embedding similarity credits a correct paraphrase and relevance measures whether the answer addresses the question.
- **C:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: Embedding similarity credits a correct paraphrase and relevance measures whether the answer addresses the question.
- **D:** Correct. Embedding-based similarity credits a correct paraphrase that word overlap misses. In this case: Embedding similarity credits a correct paraphrase and relevance measures whether the answer addresses the question.
- **E:** Correct. Relevance separates an off-topic answer from a factually wrong one. In this case: Embedding similarity credits a correct paraphrase and relevance measures whether the answer addresses the question.

### Question 70 — A

Answer: Split traffic between two model versions and compare outcomes. An A/B test measures the difference on real traffic before a full switch. Local study-map skill 5.2 (Model Comparison and Traffic Testing), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Correct. In this case: An A/B test measures the difference on real traffic before a full switch.
- **B:** Incorrect for this question. A rubric with human scores gives a reference the automatic metrics can be checked against. Why the correct answer wins: An A/B test measures the difference on real traffic before a full switch.
- **C:** Incorrect for this question. A canary limits the blast radius of a prompt or model change. Why the correct answer wins: An A/B test measures the difference on real traffic before a full switch.
- **D:** Incorrect for this question. Shadow traffic compares answers with no user exposure. Why the correct answer wins: An A/B test measures the difference on real traffic before a full switch.

### Question 71 — D

Answer: Run a prompt regression suite before promoting a version. A fixed suite of prompts and expected properties catches a wording change that breaks behaviour. Local study-map skill 5.3 (Regression Testing and Quality Gates), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: A fixed suite of prompts and expected properties catches a wording change that breaks behaviour.
- **B:** Incorrect for this question. A golden set with known answers catches a regression the moment it ships. Why the correct answer wins: A fixed suite of prompts and expected properties catches a wording change that breaks behaviour.
- **C:** Incorrect for this question. A rubric with human scores gives a reference the automatic metrics can be checked against. Why the correct answer wins: A fixed suite of prompts and expected properties catches a wording change that breaks behaviour.
- **D:** Correct. In this case: A fixed suite of prompts and expected properties catches a wording change that breaks behaviour.

### Question 72 — A, B

Answers: Block the release when evaluation drops below the threshold; Replay scripted user journeys against the new version. A quality gate blocks the regression and scripted journeys exercise paths single prompts never reach. A quality gate stops a measurable regression from reaching production. Local study-map skill 5.3 (Regression Testing and Quality Gates), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Correct. A quality gate stops a measurable regression from reaching production. In this case: A quality gate blocks the regression and scripted journeys exercise paths single prompts never reach.
- **B:** Correct. In this case: A quality gate blocks the regression and scripted journeys exercise paths single prompts never reach.
- **C:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: A quality gate blocks the regression and scripted journeys exercise paths single prompts never reach.
- **D:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: A quality gate blocks the regression and scripted journeys exercise paths single prompts never reach.
- **E:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: A quality gate blocks the regression and scripted journeys exercise paths single prompts never reach.

### Question 73 — A

Answer: Measure the share of agent tasks completed end to end. Completion rate is the outcome metric for an agent that must actually finish work. Local study-map skill 5.4 (Retrieval and Agent Evaluation), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Correct. In this case: Completion rate is the outcome metric for an agent that must actually finish work.
- **B:** Incorrect for this question. Overlap metrics are cheap and reward wording that matches the references. Why the correct answer wins: Completion rate is the outcome metric for an agent that must actually finish work.
- **C:** Incorrect for this question. Tool accuracy locates the failure inside the agent loop rather than at the answer. Why the correct answer wins: Completion rate is the outcome metric for an agent that must actually finish work.
- **D:** Incorrect for this question. Recall shows whether the answer was missing evidence before generation began. Why the correct answer wins: Completion rate is the outcome metric for an agent that must actually finish work.

### Question 74 — B, C

Answers: Measure whether the needed passage was retrieved at all; Measure whether the retrieved passages were relevant. Recall shows whether the needed passage was retrieved and precision shows whether the shortlist was relevant. Recall shows whether the answer was missing evidence before generation began. Retrieval precision explains a wrong answer that the model was given bad context for. Local study-map skill 5.4 (Retrieval and Agent Evaluation), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Incorrect for this question. Overlap metrics are cheap and reward wording that matches the references. Why the correct answer wins: Recall shows whether the needed passage was retrieved and precision shows whether the shortlist was relevant.
- **B:** Correct. Retrieval precision explains a wrong answer that the model was given bad context for. In this case: Recall shows whether the needed passage was retrieved and precision shows whether the shortlist was relevant.
- **C:** Correct. Recall shows whether the answer was missing evidence before generation began. In this case: Recall shows whether the needed passage was retrieved and precision shows whether the shortlist was relevant.
- **D:** Incorrect for this question. Embedding-based similarity credits a correct paraphrase that word overlap misses. Why the correct answer wins: Recall shows whether the needed passage was retrieved and precision shows whether the shortlist was relevant.
- **E:** Incorrect for this question. Tool accuracy locates the failure inside the agent loop rather than at the answer. Why the correct answer wins: Recall shows whether the needed passage was retrieved and precision shows whether the shortlist was relevant.

### Question 75 — B

Answer: Log the token count and check for truncated prompts. A truncation check shows whether the model ever saw the end of the instruction. Local study-map skill 5.5 (GenAI Troubleshooting), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Incorrect for this question. Overflow protection keeps the prompt inside the model limit instead of truncating silently. Why the correct answer wins: A truncation check shows whether the model ever saw the end of the instruction.
- **B:** Correct. In this case: A truncation check shows whether the model ever saw the end of the instruction.
- **C:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: A truncation check shows whether the model ever saw the end of the instruction.
- **D:** Incorrect for this question. Logs Insights correlates a spike in errors with the prompts that caused it. Why the correct answer wins: A truncation check shows whether the model ever saw the end of the instruction.
