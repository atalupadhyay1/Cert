# AWS Certified Generative AI Developer - Professional (AIP-C01) — Full-Length Mock Exam 2

Generative AI Developer · 75 questions · 180 minutes · scaled passing score 750 of 1000

Blueprint-weighted mock exam. Item mix: 60 multiple-choice and 15 multiple-response items (the selection count is stated in each multi-response stem). The published exam has 75 questions in 180 minutes, of which 65 are scored and 10 are unscored, and AWS does not identify the unscored items. AWS publishes no split between multiple-choice and multiple-response items, so the 15-item multi-response block is an authoring choice. At 75 items in 180 minutes this set matches the published pacing at about 144 seconds per item, including the same unscored proportion. The published format has no case-study component, so no case-study item appears here. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied AWS exam items.

## Questions

---

## Domain 1 — Foundation Model Integration, Data Management, and Compliance (31%) — Model integration, data pipelines, vector stores, retrieval, and prompts

### 1. An insurer wants to add a second business line to the same assistant platform next year. Which two decisions today keep that addition cheap? Select two.

- A. Use one frontier model for every request
- B. Hardcode one model identifier in the application source
- C. Compare the candidates with an Amazon Bedrock model evaluation job
- D. Let each application call the model API directly
- E. Put one internal GenAI gateway in front of every model call

### 2. A claims assistant must reuse the same instructions and the same policy corpus across three channels. Which two components carry that reuse? Select two.

- A. Version the prompt in Amazon Bedrock Prompt Management
- B. Concatenate all fields into one unlabelled text block
- C. Use an Amazon Bedrock knowledge base with a managed vector store
- D. Let each application call the model API directly
- E. Keep the prompt as a string constant in the application code

### 3. Before funding a claims summariser, the team must show that summaries are accurate enough for adjusters to trust. What should the pilot produce?

- A. Buy Amazon Bedrock provisioned throughput for the model
- B. Have reviewers score a sample against a written rubric
- C. Run a full fine-tune of every model weight
- D. Use one frontier model for every request

### 4. Underwriting will only accept a model it can host inside its own VPC because the documents cannot leave the network. Which option fits that constraint?

- A. Use one frontier model for every request
- B. Right-size the model to the task difficulty
- C. Call the model on demand through Amazon Bedrock
- D. Deploy the model from Amazon SageMaker JumpStart

### 5. Two Bedrock models are shortlisted for classifying claim narratives, and the team has two thousand anonymised labelled claims. How should the choice be made?

- A. Use one frontier model for every request
- B. Compare the candidates with an Amazon Bedrock model evaluation job
- C. Run a full fine-tune of every model weight
- D. Fine-tune with low-rank adaptation adapters

### 6. Most customer questions are balance and branch lookups, while a minority need policy interpretation. How should the traffic be split?

- A. Use one frontier model for every request
- B. Send routine prompts to a small model and hard prompts to a large one
- C. Run a full fine-tune of every model weight
- D. Put the model identifier in AWS AppConfig and switch it without a deploy

### 7. The model is throttled in the Region where the insurer holds residency approval, and an approved second Region has spare capacity. What should route the overflow?

- A. Route the call through Amazon Bedrock cross-Region inference
- B. Store the model API key in an environment variable
- C. Keep a GPU endpoint running for occasional requests
- D. Retry the failed call until it succeeds

### 8. A Regional outage takes the primary model offline during business hours and the insurer accepts plainer answers. What should the application do?

- A. Retry the failed call until it succeeds
- B. Raise the temperature for creative variants
- C. Fall back to a second model when the first is unavailable
- D. Use one frontier model for every request

### 9. A tuned claims model must keep the same guardrails and invocation logging as the managed models it replaces. How should the weights be hosted?

- A. Import the customised model weights into Amazon Bedrock
- B. Deploy the model from Amazon SageMaker JumpStart
- C. Run a full fine-tune of every model weight
- D. Host the model on a SageMaker AI real-time endpoint

### 10. A nightly claims feed occasionally arrives with missing policy identifiers and duplicate claim rows. What should reject the bad batch?

- A. Enforce freshness and completeness rules with AWS Glue Data Quality
- B. Scan the data store with Amazon Macie
- C. Set an explicit CloudWatch Logs retention period
- D. Validate response structure and log the failures

### 11. Scanned policy endorsements mix units, dates, and heading styles, and retrieval quality suffers. What should run before embedding?

- A. Concatenate all fields into one unlabelled text block
- B. Normalise the text with a model call before indexing
- C. Format the turns as an alternating conversation structure
- D. Raise the temperature for creative variants

### 12. Compliance must search six years of recorded calls for mentions of a fee that was later withdrawn. What makes those calls searchable?

- A. Transcribe the call recordings with Amazon Transcribe
- B. Extract the text from scanned pages with Amazon Textract
- C. Normalise the text with a model call before indexing
- D. Extract entities with Amazon Comprehend before indexing

### 13. The assistant must see the system instruction plus alternating customer and agent turns in order. How should the request be built?

- A. Concatenate all fields into one unlabelled text block
- B. Cap the response length in the request
- C. Raise the temperature for creative variants
- D. Format the turns as an alternating conversation structure

### 14. A developer receives a parameter validation error from the model endpoint even though the prompt looks correct. What is missing from the call?

- A. Keep the prompt as a string constant in the application code
- B. Concatenate all fields into one unlabelled text block
- C. Send the request as the JSON body the model expects
- D. Format the turns as an alternating conversation structure

### 15. Claims chunks must be searched by similarity while also joining to relational policy rows the insurer already keeps. Where should the embeddings live?

- A. Keep embeddings and metadata in Amazon DynamoDB
- B. Store the knowledge graph in Amazon Neptune
- C. Keep the source corpus in Amazon S3 and index references into it
- D. Store the vectors in Amazon Aurora PostgreSQL with pgvector

### 16. Superseded policy versions stay in the corpus for audit, but answers must only cite the version in force. What enforces that?

- A. Filter the search by document metadata before the similarity ranking
- B. Drop passages below a relevance score threshold
- C. Raise the number of retrieved passages per query
- D. Re-embed the corpus when the embedding model changes

### 17. Policy documents change only in a monthly publishing cycle and immediate indexing is not required. Which maintenance pattern fits?

- A. Rebuild the index on a schedule and accept staleness between runs
- B. Re-embed the corpus when the embedding model changes
- C. Cache every answer with no expiry
- D. Trigger re-indexing from Amazon S3 event notifications

### 18. Call transcripts are unstructured and switch topic mid-page, so fixed windows cut through arguments. How should the split be chosen?

- A. Split documents into fixed-size token windows with overlap
- B. Keep old vectors and embed new documents with the newer model
- C. Increase the chunk size so every answer fits in one chunk
- D. Split where the embedding similarity between sentences drops

### 19. A policy assistant retrieves useful passages but buries the governing clause beneath general text. Which two changes lift it? Select two.

- A. Increase the chunk size so every answer fits in one chunk
- B. Drop passages below a relevance score threshold
- C. Keep old vectors and embed new documents with the newer model
- D. Raise the number of retrieved passages per query
- E. Rerank the retrieved passages with an Amazon Bedrock reranker

### 20. Adjusters search by claim number and by description, and vector search alone misses the number. What retrieval mode covers both?

- A. Expand the user query into related terms before retrieval
- B. Split where the embedding similarity between sentences drops
- C. Raise the number of retrieved passages per query
- D. Combine keyword and vector retrieval and merge the ranked lists

### 21. A customer asks one question that covers both a premium change and a coverage exclusion. What should happen before retrieval?

- A. Cache every answer with no expiry
- B. Expand the user query into related terms before retrieval
- C. Break a multi-part question into separate retrievals
- D. Raise the number of retrieved passages per query

### 22. Retrieved policy text occasionally reads as an instruction and derails the answer. What prompt structure reduces that risk?

- A. Wrap context, instructions, and question in labelled sections
- B. Keep the prompt as a string constant in the application code
- C. Raise the temperature for creative variants
- D. Cap the response length in the request

### 23. Compliance must review any wording change before it reaches customers. What enforces that step?

- A. Keep the prompt as a string constant in the application code
- B. Hardcode one model identifier in the application source
- C. Require approval before a prompt version is promoted
- D. Raise the temperature for creative variants

---

## Domain 2 — Implementation and Integration (26%) — Agents, deployment, enterprise integration, APIs, and developer tooling

### 24. A claims agent must hold the claim number and the last four turns while the caller is transferred between teams. Where should that state live?

- A. Keep memory only in the prompt of the current turn
- B. Cache every answer with no expiry
- C. Set an explicit CloudWatch Logs retention period
- D. Keep conversation and task memory in Amazon DynamoDB

### 25. A long fraud investigation produces a hundred turns and the model must stay coherent without resending them all. What keeps it cheap?

- A. Keep memory only in the prompt of the current turn
- B. Summarise the conversation before adding more turns
- C. Increase the chunk size so every answer fits in one chunk
- D. Concatenate all fields into one unlabelled text block

### 26. Claims triage, fraud checks, and payout status each need a different tool set and prompt. How should the work be divided?

- A. Keep the prompt as a string constant in the application code
- B. Coordinate the specialists with AWS Agent Squad
- C. Return the whole answer from one synchronous call
- D. Give one agent every tool in the platform

### 27. An underwriting agent must show each reasoning step and must never loop indefinitely. Which two controls satisfy both demands? Select two.

- A. Give one agent every tool in the platform
- B. Set an explicit step and budget limit on the agent loop
- C. Raise the temperature for creative variants
- D. Retry the failed call until it succeeds
- E. Orchestrate the reasoning loop in AWS Step Functions

### 28. An agent sends a policy identifier with a trailing space and the downstream call fails after a long round trip. Where should that be caught?

- A. Validate tool arguments against a schema before calling
- B. Retry the failed call until it succeeds
- C. Set an explicit CloudWatch Logs retention period
- D. Cache every answer with no expiry

### 29. A payment-status tool can read far more accounts than the agent needs to answer a question. What limits the blast radius?

- A. Cache every answer with no expiry
- B. Scope the tool role to only the actions it needs
- C. Store the model API key in an environment variable
- D. Make the document bucket publicly readable

### 30. Claims intake runs at a predictable load all day and the team is tired of throttle retries. What should it buy?

- A. Keep a GPU endpoint running for occasional requests
- B. Buy Amazon Bedrock provisioned throughput for the model
- C. Call the model on demand through Amazon Bedrock
- D. Use one frontier model for every request

### 31. End-of-day document summarisation is large, non-interactive, and must finish before midnight, while the customer channel needs steady interactive capacity. Which two patterns fit? Select two.

- A. Return the whole answer from one synchronous call
- B. Call the model on demand through Amazon Bedrock
- C. Buy Amazon Bedrock provisioned throughput for the model
- D. Retry the failed call until it succeeds
- E. Run the work as an Amazon Bedrock batch inference job

### 32. A first notice of loss must reach several downstream services, and new consumers are added each quarter. What connects them?

- A. Route domain events through Amazon EventBridge
- B. Buffer the work in an Amazon SQS queue
- C. Move SaaS records in with Amazon AppFlow
- D. Fan the result out with Amazon SNS

### 33. A statement-summary job must survive a model outage without losing work already queued. What should sit in front of the model?

- A. Buffer the work in an Amazon SQS queue
- B. Return the whole answer from one synchronous call
- C. Front the model with Amazon API Gateway
- D. Fan the result out with Amazon SNS

### 34. Policyholders sign in to a self-service portal that calls the assistant, and each request must carry an identity. What issues those tokens?

- A. Make the document bucket publicly readable
- B. Give the task an IAM role scoped to the resources it uses
- C. Authenticate users with Amazon Cognito
- D. Store the model API key in an environment variable

### 35. Four insurance brands share one model contract, and each brand's keys and quotas are audited separately. What should the platform provide?

- A. Store the model API key in an environment variable
- B. Let each application call the model API directly
- C. Put one internal GenAI gateway in front of every model call
- D. Hardcode one model identifier in the application source

### 36. A new prompt and model pairing must be proven on a small share of real traffic before a full switch. Which two services deliver that path? Select two.

- A. Store the model API key in an environment variable
- B. Let each application call the model API directly
- C. Keep the prompt as a string constant in the application code
- D. Run the evaluation suite in AWS CodeBuild
- E. Shift traffic with an AWS CodeDeploy canary deployment

### 37. A medical-record summary can take four minutes, longer than the API gateway timeout allows. What pattern fits?

- A. Stream tokens as server-sent events
- B. Queue the prompt and return a job identifier for polling
- C. Stream tokens over WebSockets through API Gateway
- D. Return the whole answer from one synchronous call

### 38. A quoting service hammers the model after each throttle and the queue keeps growing. What retry policy fixes it?

- A. Keep a GPU endpoint running for occasional requests
- B. Retry the failed call until it succeeds
- C. Retry throttled calls with exponential backoff and jitter
- D. Open a circuit breaker after repeated dependency failures

### 39. A downstream ratings service has been failing every call for an hour and each request waits three seconds on it. What should open?

- A. Open a circuit breaker after repeated dependency failures
- B. Return the whole answer from one synchronous call
- C. Retry throttled calls with exponential backoff and jitter
- D. Retry the failed call until it succeeds

### 40. Brokers need a documented endpoint with authentication, request validation, and per-broker quotas. What should expose the assistant?

- A. Serve repeatable responses from Amazon CloudFront
- B. Build the interface with AWS Amplify
- C. Let each application call the model API directly
- D. Front the model with Amazon API Gateway

### 41. An advisor dashboard needs a single query for claims, policies, and assistant answers with live updates. What API style fits?

- A. Stream tokens as server-sent events
- B. Front the model with Amazon API Gateway
- C. Run the request shaping logic at the edge with Lambda@Edge
- D. Expose the assistant through AWS AppSync

### 42. The integration team writes the same pagination and retry code for each model feature. What reduces that repetition?

- A. Keep the prompt as a string constant in the application code
- B. Release the assistant through AWS CodePipeline
- C. Generate and explain the integration code with Amazon Q Developer
- D. Run the evaluation suite in AWS CodeBuild

### 43. Support reports that answers to one product became wrong yesterday, and the team needs the exact prompts behind those answers. What finds them?

- A. Record control-plane activity in AWS CloudTrail
- B. Trace the request across services with AWS X-Ray
- C. Query the prompt and response logs with CloudWatch Logs Insights
- D. Set an explicit CloudWatch Logs retention period

---

## Domain 3 — AI Safety, Security, and Governance (20%) — Safety controls, privacy, governance, and responsible AI

### 44. A policyholder becomes abusive in a chat about a declined claim, and the assistant must not mirror the tone. What sits on both the input and output path?

- A. Apply Amazon Bedrock Guardrails content filters
- B. Lower the temperature for factual answers
- C. Set an explicit CloudWatch Logs retention period
- D. Cap the response length in the request

### 45. An insurer must refuse advice on tax treatment and must verify that answers about a settlement follow the written policy. Which two guardrail features do that? Select two.

- A. Cap the response length in the request
- B. Retry the failed call until it succeeds
- C. Cache every answer with no expiry
- D. Define denied topics in Amazon Bedrock Guardrails
- E. Add automated reasoning checks for policy statements

### 46. Complaints handlers must be able to open the clause behind every answer the assistant gives. What should the answer carry?

- A. Escalate low-confidence or high-impact answers to a person
- B. Require the answer to cite the retrieved passage
- C. Cap the response length in the request
- D. Return a confidence score with each answer

### 47. A customer asks how much the premium rises if the excess doubles, and the numbers exist in a rating table. How should the figure be produced?

- A. Lower the temperature for factual answers
- B. Return a confidence score with each answer
- C. Constrain the response with a JSON schema
- D. Translate the question into SQL and run it on the database

### 48. A broker pastes text instructing the assistant to reveal another broker's commission schedule. What catches that attempt?

- A. Retry the failed call until it succeeds
- B. Cap the response length in the request
- C. Screen inputs for instruction override and jailbreak patterns
- D. Lower the temperature for factual answers

### 49. Before each release, the security team wants evidence that the assistant still refuses known hostile prompts. What runs that check?

- A. Cache every answer with no expiry
- B. Run the release against a curated golden question set
- C. Run an adversarial prompt suite before each release
- D. Have reviewers score a sample against a written rubric

### 50. Callers read out account numbers when describing a dispute, and those numbers must never enter the model request. What is the right control point?

- A. Scan the data store with Amazon Macie
- B. Set an explicit CloudWatch Logs retention period
- C. Mask personal data before the prompt is built
- D. Enable sensitive-information filters in Amazon Bedrock Guardrails

### 51. Personal data must be detected in the stored transcripts and also masked if it slips into a generated answer. Which two controls cover both points? Select two.

- A. Store the model API key in an environment variable
- B. Apply Amazon Bedrock Guardrails content filters
- C. Detect personal data with Amazon Comprehend
- D. Set an explicit CloudWatch Logs retention period
- E. Enable sensitive-information filters in Amazon Bedrock Guardrails

### 52. The insurer's security standard forbids model traffic leaving the private network path. What provides it?

- A. Call the model through an interface VPC endpoint
- B. Store the model API key in an environment variable
- C. Make the document bucket publicly readable
- D. Serve repeatable responses from Amazon CloudFront

### 53. A public quote endpoint is being probed with malformed requests that consume model capacity. What blocks them first?

- A. Make the document bucket publicly readable
- B. Serve repeatable responses from Amazon CloudFront
- C. Deploy the workload in private subnets
- D. Put AWS WAF rules in front of the public endpoint

### 54. An examiner asks who approved the model change and when the guardrail was relaxed. What records both?

- A. Build the operations view in Amazon Managed Grafana
- B. Set an explicit CloudWatch Logs retention period
- C. Record control-plane activity in AWS CloudTrail
- D. Turn on Amazon Bedrock model invocation logging

### 55. A disputed answer must be reconstructed with the corpus version and the exact request that produced it. Which two records allow that? Select two.

- A. Lower the temperature for factual answers
- B. Cache every answer with no expiry
- C. Store the model API key in an environment variable
- D. Record data lineage in the AWS Glue Data Catalog
- E. Turn on Amazon Bedrock model invocation logging

### 56. A new claims model must disclose its intended use and known limits to the risk committee. What documents that?

- A. Publish a model card with the model version
- B. Constrain the response with a JSON schema
- C. Compare the candidates with an Amazon Bedrock model evaluation job
- D. Set an explicit CloudWatch Logs retention period

### 57. The interface should warn a customer when the assistant is unsure rather than state a figure flatly. What supports that warning?

- A. Cache every answer with no expiry
- B. Raise the temperature for creative variants
- C. Cap the response length in the request
- D. Return a confidence score with each answer

### 58. An insurer must report answer quality separately for each customer segment every quarter. What produces that report?

- A. Alert when fairness metrics move beyond a band
- B. Detect spend spikes with AWS Cost Anomaly Detection
- C. Alarm on p95 latency and error rate
- D. Report fairness metrics per user segment

---

## Domain 4 — Operational Efficiency and Optimization for GenAI Applications (12%) — Token cost, latency, throughput, and observability

### 59. Broker chats carry thirty earlier turns and the input charge grows with each one. What should be done with the stale turns?

- A. Raise the temperature for creative variants
- B. Prune older turns from the context window
- C. Raise the number of retrieved passages per query
- D. Increase the chunk size so every answer fits in one chunk

### 60. Some answers run to nine paragraphs when a two-sentence summary is what the customer wants. What bounds the spend per call?

- A. Increase the chunk size so every answer fits in one chunk
- B. Cap the response length in the request
- C. Concatenate all fields into one unlabelled text block
- D. Raise the number of retrieved passages per query

### 61. A nightly batch asks the identical two thousand questions every evening. What removes most of that spend?

- A. Cache answers by embedding similarity to earlier questions
- B. Keep a GPU endpoint running for occasional requests
- C. Cache every answer with no expiry
- D. Cache the response under a hash of the normalised request

### 62. A price-comparison assistant answers a million questions a month, most of them near-duplicates of earlier ones. Which two levers cut cost most? Select two.

- A. Send routine prompts to a small model and hard prompts to a large one
- B. Cache answers by embedding similarity to earlier questions
- C. Cache every answer with no expiry
- D. Run a full fine-tune of every model weight
- E. Use one frontier model for every request

### 63. The most common questions are predictable and their answers change once a day. What removes them from the interactive path?

- A. Keep a GPU endpoint running for occasional requests
- B. Precompute answers for predictable questions on a schedule
- C. Return the whole answer from one synchronous call
- D. Stream tokens as they are generated

### 64. A renewal-season surge must be served without throttling and without buying capacity for the peak week. Which two practices address it? Select two.

- A. Retry the failed call until it succeeds
- B. Run the work as an Amazon Bedrock batch inference job
- C. Use one frontier model for every request
- D. Plan capacity from measured tokens per minute
- E. Issue independent model calls in parallel

### 65. Operations wants one screen showing model latency, error rate, and cost beside the claims backlog. What provides it?

- A. Set an explicit CloudWatch Logs retention period
- B. Record control-plane activity in AWS CloudTrail
- C. Build the operations view in Amazon Managed Grafana
- D. Publish a model card with the model version

### 66. The insurer wants to hear about an assistant outage before customers do and to catch slow answers early. Which two controls deliver that? Select two.

- A. Detect spend spikes with AWS Cost Anomaly Detection
- B. Alarm on p95 latency and error rate
- C. Probe the endpoint with CloudWatch Synthetics
- D. Publish a model card with the model version
- E. Set an explicit CloudWatch Logs retention period

### 67. One brokerages division consumed most of the shared model quota last month without warning. What should be added?

- A. Cover the steady compute with a Savings Plan
- B. Alert when a tenant crosses its monthly token budget
- C. Detect spend spikes with AWS Cost Anomaly Detection
- D. Keep a GPU endpoint running for occasional requests

---

## Domain 5 — Testing, Validation, and Troubleshooting (11%) — Evaluation, validation, regression testing, and diagnosis

### 68. Legal reviewers must judge whether settlement letters are accurate, and their verdict is the ground truth. What produces that reference?

- A. Have reviewers score a sample against a written rubric
- B. Score how directly the answer addresses the question
- C. Report ROUGE and BLEU against the reference answers
- D. Report BERTScore for semantic similarity to the reference

### 69. Ten thousand answers a day need scoring against a rubric, and the score must be defensible to an auditor. Which two steps make that possible? Select two.

- A. Measure the judge model against expert labels first
- B. Score candidate answers with a judge model on a fixed rubric
- C. Report ROUGE and BLEU against the reference answers
- D. Measure whether the needed passage was retrieved at all
- E. Raise the temperature for creative variants

### 70. A regulator will not allow any customer to see the new model until its answers have been compared at scale. What fits?

- A. Split traffic between two model versions and compare outcomes
- B. Mirror production traffic to the new version and compare offline
- C. Send a small traffic share to the new prompt and watch the metrics
- D. Have reviewers score a sample against a written rubric

### 71. A model upgrade must not break two hundred known policy questions. What should the release run against?

- A. Cache every answer with no expiry
- B. Set an explicit CloudWatch Logs retention period
- C. Run the release against a curated golden question set
- D. Have reviewers score a sample against a written rubric

### 72. A release must stop automatically when quality drops, and reviewers want to see what changed in the wording. Which two practices deliver both? Select two.

- A. Raise the temperature for creative variants
- B. Diff the new responses against the previous version
- C. Retry the failed call until it succeeds
- D. Cache every answer with no expiry
- E. Block the release when evaluation drops below the threshold

### 73. A claims agent picks the payout tool when the question was about policy status. What isolates that failure?

- A. Report ROUGE and BLEU against the reference answers
- B. Measure whether the needed passage was retrieved at all
- C. Measure the share of agent tasks completed end to end
- D. Measure whether the agent called the right tool with the right arguments

### 74. A claims agent fails some requests, and the team needs to know both whether it found the right documents and whether it finished the job. Which two metrics answer that? Select two.

- A. Report ROUGE and BLEU against the reference answers
- B. Measure whether the needed passage was retrieved at all
- C. Report BERTScore for semantic similarity to the reference
- D. Measure the share of agent tasks completed end to end
- E. Measure whether the agent called the right tool with the right arguments

### 75. A multi-step claim enquiry gave a confident wrong answer, and the request succeeded end to end. What should be inspected?

- A. Log the token count and check for truncated prompts
- B. Trace the request across services with AWS X-Ray
- C. Cache every answer with no expiry
- D. Inspect the agent reasoning trace for the failed task

---

## Answer key and explanations

### Question 1 — C, E

Answers: Put one internal GenAI gateway in front of every model call; Compare the candidates with an Amazon Bedrock model evaluation job. A shared gateway isolates callers from model choices and an evaluation job makes each new candidate defensible. A gateway centralises credentials, quotas, logging, and model routing for all teams. A Bedrock evaluation job scores candidate models on your prompts and metrics before you choose. Local study-map skill 1.1 (GenAI Solution Architecture), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: A shared gateway isolates callers from model choices and an evaluation job makes each new candidate defensible.
- **B:** Incorrect for this question. A hardcoded identifier forces a code change and a release to try another model. Why the correct answer wins: A shared gateway isolates callers from model choices and an evaluation job makes each new candidate defensible.
- **C:** Correct. A Bedrock evaluation job scores candidate models on your prompts and metrics before you choose. In this case: A shared gateway isolates callers from model choices and an evaluation job makes each new candidate defensible.
- **D:** Incorrect for this question. Direct calls from every app scatter keys, quotas, and logging across teams. Why the correct answer wins: A shared gateway isolates callers from model choices and an evaluation job makes each new candidate defensible.
- **E:** Correct. A gateway centralises credentials, quotas, logging, and model routing for all teams. In this case: A shared gateway isolates callers from model choices and an evaluation job makes each new candidate defensible.

### Question 2 — A, C

Answers: Version the prompt in Amazon Bedrock Prompt Management; Use an Amazon Bedrock knowledge base with a managed vector store. Versioned prompt templates and a managed knowledge base are the reusable pieces every channel shares. Prompt Management stores versions and variables so the same template serves every environment. A managed knowledge base handles ingestion, chunking, embedding and sync with little code. Local study-map skill 1.1 (GenAI Solution Architecture), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Correct. Prompt Management stores versions and variables so the same template serves every environment. In this case: Versioned prompt templates and a managed knowledge base are the reusable pieces every channel shares.
- **B:** Incorrect for this question. A single blob loses the field boundaries the model needs to answer precisely. Why the correct answer wins: Versioned prompt templates and a managed knowledge base are the reusable pieces every channel shares.
- **C:** Correct. A managed knowledge base handles ingestion, chunking, embedding and sync with little code. In this case: Versioned prompt templates and a managed knowledge base are the reusable pieces every channel shares.
- **D:** Incorrect for this question. Direct calls from every app scatter keys, quotas, and logging across teams. Why the correct answer wins: Versioned prompt templates and a managed knowledge base are the reusable pieces every channel shares.
- **E:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: Versioned prompt templates and a managed knowledge base are the reusable pieces every channel shares.

### Question 3 — B

Answer: Have reviewers score a sample against a written rubric. A rubric with human scores gives a reference the automatic metrics can be checked against. Local study-map skill 1.2 (Proof-of-Concept Validation), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. Provisioned throughput reserves model units and gives a predictable token-per-minute ceiling. Why the correct answer wins: A rubric with human scores gives a reference the automatic metrics can be checked against.
- **B:** Correct. In this case: A rubric with human scores gives a reference the automatic metrics can be checked against.
- **C:** Incorrect for this question. A full fine-tune changes all weights, which is expensive and gives one model per task. Why the correct answer wins: A rubric with human scores gives a reference the automatic metrics can be checked against.
- **D:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: A rubric with human scores gives a reference the automatic metrics can be checked against.

### Question 4 — D

Answer: Deploy the model from Amazon SageMaker JumpStart. JumpStart supplies prebuilt models and notebooks for hosting on SageMaker AI endpoints. Local study-map skill 1.3 (Foundation Model Selection and Benchmarking), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: JumpStart supplies prebuilt models and notebooks for hosting on SageMaker AI endpoints.
- **B:** Incorrect for this question. A model no larger than the task needs is the largest single cost lever. Why the correct answer wins: JumpStart supplies prebuilt models and notebooks for hosting on SageMaker AI endpoints.
- **C:** Incorrect for this question. On-demand Bedrock inference bills per token with no committed capacity, which suits spiky or unproven demand. Why the correct answer wins: JumpStart supplies prebuilt models and notebooks for hosting on SageMaker AI endpoints.
- **D:** Correct. In this case: JumpStart supplies prebuilt models and notebooks for hosting on SageMaker AI endpoints.

### Question 5 — B

Answer: Compare the candidates with an Amazon Bedrock model evaluation job. A Bedrock evaluation job scores every candidate on the same labelled prompts before a choice is made. A Bedrock evaluation job scores candidate models on your prompts and metrics before you choose. Local study-map skill 1.3 (Foundation Model Selection and Benchmarking), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: A Bedrock evaluation job scores every candidate on the same labelled prompts before a choice is made.
- **B:** Correct. A Bedrock evaluation job scores candidate models on your prompts and metrics before you choose. In this case: A Bedrock evaluation job scores every candidate on the same labelled prompts before a choice is made.
- **C:** Incorrect for this question. A full fine-tune changes all weights, which is expensive and gives one model per task. Why the correct answer wins: A Bedrock evaluation job scores every candidate on the same labelled prompts before a choice is made.
- **D:** Incorrect for this question. LoRA trains a small adapter instead of every weight, which cuts cost and keeps the base model reusable. Why the correct answer wins: A Bedrock evaluation job scores every candidate on the same labelled prompts before a choice is made.

### Question 6 — B

Answer: Send routine prompts to a small model and hard prompts to a large one. Tiered routing spends the large model only on the requests that need it. Local study-map skill 1.4 (Model Routing and Provider Abstraction), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: Tiered routing spends the large model only on the requests that need it.
- **B:** Correct. In this case: Tiered routing spends the large model only on the requests that need it.
- **C:** Incorrect for this question. A full fine-tune changes all weights, which is expensive and gives one model per task. Why the correct answer wins: Tiered routing spends the large model only on the requests that need it.
- **D:** Incorrect for this question. A configuration flag changes the model per request path without shipping new code. Why the correct answer wins: Tiered routing spends the large model only on the requests that need it.

### Question 7 — A

Answer: Route the call through Amazon Bedrock cross-Region inference. A cross-Region inference profile spreads traffic so a local capacity shortage does not fail the request. Local study-map skill 1.5 (Resilience and Cross-Region Inference), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Correct. In this case: A cross-Region inference profile spreads traffic so a local capacity shortage does not fail the request.
- **B:** Incorrect for this question. A key in an environment variable leaks through images, logs, and job definitions. Why the correct answer wins: A cross-Region inference profile spreads traffic so a local capacity shortage does not fail the request.
- **C:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: A cross-Region inference profile spreads traffic so a local capacity shortage does not fail the request.
- **D:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: A cross-Region inference profile spreads traffic so a local capacity shortage does not fail the request.

### Question 8 — C

Answer: Fall back to a second model when the first is unavailable. A fallback model keeps the feature answering during a Regional degradation, at a stated quality cost. A fallback keeps the feature available when one model or Region degrades. Local study-map skill 1.5 (Resilience and Cross-Region Inference), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: A fallback model keeps the feature answering during a Regional degradation, at a stated quality cost.
- **B:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: A fallback model keeps the feature answering during a Regional degradation, at a stated quality cost.
- **C:** Correct. A fallback keeps the feature available when one model or Region degrades. In this case: A fallback model keeps the feature answering during a Regional degradation, at a stated quality cost.
- **D:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: A fallback model keeps the feature answering during a Regional degradation, at a stated quality cost.

### Question 9 — A

Answer: Import the customised model weights into Amazon Bedrock. Custom model import brings your own weights under Bedrock inference and guardrail features. Local study-map skill 1.6 (Customisation Lifecycle and Rollback), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Correct. In this case: Custom model import brings your own weights under Bedrock inference and guardrail features.
- **B:** Incorrect for this question. JumpStart supplies prebuilt models and notebooks for hosting on SageMaker AI endpoints. Why the correct answer wins: Custom model import brings your own weights under Bedrock inference and guardrail features.
- **C:** Incorrect for this question. A full fine-tune changes all weights, which is expensive and gives one model per task. Why the correct answer wins: Custom model import brings your own weights under Bedrock inference and guardrail features.
- **D:** Incorrect for this question. A SageMaker AI endpoint gives full control over the container, instance and scaling policy. Why the correct answer wins: Custom model import brings your own weights under Bedrock inference and guardrail features.

### Question 10 — A

Answer: Enforce freshness and completeness rules with AWS Glue Data Quality. Rule sets score freshness and completeness and stop the batch before anything is embedded. Local study-map skill 1.7 (Data Validation for Model Inputs), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Correct. In this case: Rule sets score freshness and completeness and stop the batch before anything is embedded.
- **B:** Incorrect for this question. Macie finds sensitive data at rest so the corpus can be cleaned before indexing. Why the correct answer wins: Rule sets score freshness and completeness and stop the batch before anything is embedded.
- **C:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: Rule sets score freshness and completeness and stop the batch before anything is embedded.
- **D:** Incorrect for this question. Structure failures appear in the logs before a downstream parser breaks. Why the correct answer wins: Rule sets score freshness and completeness and stop the batch before anything is embedded.

### Question 11 — B

Answer: Normalise the text with a model call before indexing. A reformatting pass cleans inconsistent headings and units before embedding. Local study-map skill 1.7 (Data Validation for Model Inputs), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. A single blob loses the field boundaries the model needs to answer precisely. Why the correct answer wins: A reformatting pass cleans inconsistent headings and units before embedding.
- **B:** Correct. In this case: A reformatting pass cleans inconsistent headings and units before embedding.
- **C:** Incorrect for this question. A dialog-shaped request keeps speaker roles and prior turns in the order the model expects. Why the correct answer wins: A reformatting pass cleans inconsistent headings and units before embedding.
- **D:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: A reformatting pass cleans inconsistent headings and units before embedding.

### Question 12 — A

Answer: Transcribe the call recordings with Amazon Transcribe. Transcribe turns speech into timestamped text that retrieval can search. Local study-map skill 1.8 (Multimodal Ingestion and Processing), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Correct. In this case: Transcribe turns speech into timestamped text that retrieval can search.
- **B:** Incorrect for this question. Textract returns text and form fields from an image so it can be indexed as text. Why the correct answer wins: Transcribe turns speech into timestamped text that retrieval can search.
- **C:** Incorrect for this question. A reformatting pass cleans inconsistent headings and units before embedding. Why the correct answer wins: Transcribe turns speech into timestamped text that retrieval can search.
- **D:** Incorrect for this question. Entity extraction puts product codes and names in metadata for exact filtering. Why the correct answer wins: Transcribe turns speech into timestamped text that retrieval can search.

### Question 13 — D

Answer: Format the turns as an alternating conversation structure. A dialog-shaped request keeps speaker roles and prior turns in the order the model expects. Local study-map skill 1.9 (Request Formatting and Enrichment), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. A single blob loses the field boundaries the model needs to answer precisely. Why the correct answer wins: A dialog-shaped request keeps speaker roles and prior turns in the order the model expects.
- **B:** Incorrect for this question. A token cap bounds the cost of a runaway answer and the latency of every call. Why the correct answer wins: A dialog-shaped request keeps speaker roles and prior turns in the order the model expects.
- **C:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: A dialog-shaped request keeps speaker roles and prior turns in the order the model expects.
- **D:** Correct. In this case: A dialog-shaped request keeps speaker roles and prior turns in the order the model expects.

### Question 14 — C

Answer: Send the request as the JSON body the model expects. The model API expects the prompt, parameters, and model identifier in one JSON body. Local study-map skill 1.9 (Request Formatting and Enrichment), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: The model API expects the prompt, parameters, and model identifier in one JSON body.
- **B:** Incorrect for this question. A single blob loses the field boundaries the model needs to answer precisely. Why the correct answer wins: The model API expects the prompt, parameters, and model identifier in one JSON body.
- **C:** Correct. In this case: The model API expects the prompt, parameters, and model identifier in one JSON body.
- **D:** Incorrect for this question. A dialog-shaped request keeps speaker roles and prior turns in the order the model expects. Why the correct answer wins: The model API expects the prompt, parameters, and model identifier in one JSON body.

### Question 15 — D

Answer: Store the vectors in Amazon Aurora PostgreSQL with pgvector. pgvector keeps embeddings beside relational rows so one query can filter and search together. Local study-map skill 1.10 (Vector Store Architecture), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. DynamoDB serves key lookups fast and can hold vectors beside their metadata for small corpora. Why the correct answer wins: pgvector keeps embeddings beside relational rows so one query can filter and search together.
- **B:** Incorrect for this question. Neptune answers relationship traversals that a similarity search cannot express. Why the correct answer wins: pgvector keeps embeddings beside relational rows so one query can filter and search together.
- **C:** Incorrect for this question. S3 holds the authoritative documents while the index stores only chunks and pointers. Why the correct answer wins: pgvector keeps embeddings beside relational rows so one query can filter and search together.
- **D:** Correct. In this case: pgvector keeps embeddings beside relational rows so one query can filter and search together.

### Question 16 — A

Answer: Filter the search by document metadata before the similarity ranking. A metadata filter removes out-of-scope documents so the ranking only sees eligible chunks. Local study-map skill 1.11 (Metadata Frameworks and Index Maintenance), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Correct. In this case: A metadata filter removes out-of-scope documents so the ranking only sees eligible chunks.
- **B:** Incorrect for this question. A threshold keeps marginal passages out of the prompt that would only add noise. Why the correct answer wins: A metadata filter removes out-of-scope documents so the ranking only sees eligible chunks.
- **C:** Incorrect for this question. More passages raise recall and also lengthen the prompt and the cost per call. Why the correct answer wins: A metadata filter removes out-of-scope documents so the ranking only sees eligible chunks.
- **D:** Incorrect for this question. Vectors from two different models are not comparable, so the whole index must be rebuilt. Why the correct answer wins: A metadata filter removes out-of-scope documents so the ranking only sees eligible chunks.

### Question 17 — A

Answer: Rebuild the index on a schedule and accept staleness between runs. Scheduled rebuilds are simple and leave a window in which answers lag the source. Local study-map skill 1.11 (Metadata Frameworks and Index Maintenance), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Correct. In this case: Scheduled rebuilds are simple and leave a window in which answers lag the source.
- **B:** Incorrect for this question. Vectors from two different models are not comparable, so the whole index must be rebuilt. Why the correct answer wins: Scheduled rebuilds are simple and leave a window in which answers lag the source.
- **C:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: Scheduled rebuilds are simple and leave a window in which answers lag the source.
- **D:** Incorrect for this question. Event notifications start a sync as soon as a document lands or changes, which keeps lag to seconds. Why the correct answer wins: Scheduled rebuilds are simple and leave a window in which answers lag the source.

### Question 18 — D

Answer: Split where the embedding similarity between sentences drops. Semantic splitting places boundaries at topic shifts rather than at a character count. Local study-map skill 1.12 (Chunking and Embedding Strategy), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. Fixed windows are predictable and cheap, and overlap preserves text that straddles a boundary. Why the correct answer wins: Semantic splitting places boundaries at topic shifts rather than at a character count.
- **B:** Incorrect for this question. Mixing vector spaces silently breaks similarity, because distances no longer mean the same thing. Why the correct answer wins: Semantic splitting places boundaries at topic shifts rather than at a character count.
- **C:** Incorrect for this question. Larger chunks carry more context but dilute the embedding and crowd the prompt window. Why the correct answer wins: Semantic splitting places boundaries at topic shifts rather than at a character count.
- **D:** Correct. In this case: Semantic splitting places boundaries at topic shifts rather than at a character count.

### Question 19 — B, E

Answers: Rerank the retrieved passages with an Amazon Bedrock reranker; Drop passages below a relevance score threshold. A reranker reorders the shortlist and a threshold removes passages too weak to matter. A reranker scores the shortlist against the query and lifts precision before the prompt is built. A threshold keeps marginal passages out of the prompt that would only add noise. Local study-map skill 1.13 (Hybrid Retrieval and Reranking), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. Larger chunks carry more context but dilute the embedding and crowd the prompt window. Why the correct answer wins: A reranker reorders the shortlist and a threshold removes passages too weak to matter.
- **B:** Correct. A threshold keeps marginal passages out of the prompt that would only add noise. In this case: A reranker reorders the shortlist and a threshold removes passages too weak to matter.
- **C:** Incorrect for this question. Mixing vector spaces silently breaks similarity, because distances no longer mean the same thing. Why the correct answer wins: A reranker reorders the shortlist and a threshold removes passages too weak to matter.
- **D:** Incorrect for this question. More passages raise recall and also lengthen the prompt and the cost per call. Why the correct answer wins: A reranker reorders the shortlist and a threshold removes passages too weak to matter.
- **E:** Correct. A reranker scores the shortlist against the query and lifts precision before the prompt is built. In this case: A reranker reorders the shortlist and a threshold removes passages too weak to matter.

### Question 20 — D

Answer: Combine keyword and vector retrieval and merge the ranked lists. Hybrid retrieval catches exact identifiers that a vector search alone can miss. Local study-map skill 1.13 (Hybrid Retrieval and Reranking), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. Expansion bridges vocabulary gaps between how users ask and how documents are written. Why the correct answer wins: Hybrid retrieval catches exact identifiers that a vector search alone can miss.
- **B:** Incorrect for this question. Semantic splitting places boundaries at topic shifts rather than at a character count. Why the correct answer wins: Hybrid retrieval catches exact identifiers that a vector search alone can miss.
- **C:** Incorrect for this question. More passages raise recall and also lengthen the prompt and the cost per call. Why the correct answer wins: Hybrid retrieval catches exact identifiers that a vector search alone can miss.
- **D:** Correct. In this case: Hybrid retrieval catches exact identifiers that a vector search alone can miss.

### Question 21 — C

Answer: Break a multi-part question into separate retrievals. Decomposition retrieves evidence for each sub-question instead of averaging them into one query. Local study-map skill 1.14 (Query Transformation and Handling), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: Decomposition retrieves evidence for each sub-question instead of averaging them into one query.
- **B:** Incorrect for this question. Expansion bridges vocabulary gaps between how users ask and how documents are written. Why the correct answer wins: Decomposition retrieves evidence for each sub-question instead of averaging them into one query.
- **C:** Correct. In this case: Decomposition retrieves evidence for each sub-question instead of averaging them into one query.
- **D:** Incorrect for this question. More passages raise recall and also lengthen the prompt and the cost per call. Why the correct answer wins: Decomposition retrieves evidence for each sub-question instead of averaging them into one query.

### Question 22 — A

Answer: Wrap context, instructions, and question in labelled sections. Labeled sections stop retrieved text from being read as an instruction. Local study-map skill 1.15 (Prompt Engineering and Governance), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Correct. In this case: Labeled sections stop retrieved text from being read as an instruction.
- **B:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: Labeled sections stop retrieved text from being read as an instruction.
- **C:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: Labeled sections stop retrieved text from being read as an instruction.
- **D:** Incorrect for this question. A token cap bounds the cost of a runaway answer and the latency of every call. Why the correct answer wins: Labeled sections stop retrieved text from being read as an instruction.

### Question 23 — C

Answer: Require approval before a prompt version is promoted. An approval step keeps an unreviewed prompt change out of production traffic. Local study-map skill 1.15 (Prompt Engineering and Governance), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: An approval step keeps an unreviewed prompt change out of production traffic.
- **B:** Incorrect for this question. A hardcoded identifier forces a code change and a release to try another model. Why the correct answer wins: An approval step keeps an unreviewed prompt change out of production traffic.
- **C:** Correct. In this case: An approval step keeps an unreviewed prompt change out of production traffic.
- **D:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: An approval step keeps an unreviewed prompt change out of production traffic.

### Question 24 — D

Answer: Keep conversation and task memory in Amazon DynamoDB. DynamoDB gives the agent a durable per-session store keyed by session identifier. Local study-map skill 2.1 (Agent Memory and State), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. Prompt-only memory forgets everything the moment the context window is trimmed. Why the correct answer wins: DynamoDB gives the agent a durable per-session store keyed by session identifier.
- **B:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: DynamoDB gives the agent a durable per-session store keyed by session identifier.
- **C:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: DynamoDB gives the agent a durable per-session store keyed by session identifier.
- **D:** Correct. In this case: DynamoDB gives the agent a durable per-session store keyed by session identifier.

### Question 25 — B

Answer: Summarise the conversation before adding more turns. A running summary keeps long sessions inside the window at low token cost. Local study-map skill 2.1 (Agent Memory and State), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. Prompt-only memory forgets everything the moment the context window is trimmed. Why the correct answer wins: A running summary keeps long sessions inside the window at low token cost.
- **B:** Correct. In this case: A running summary keeps long sessions inside the window at low token cost.
- **C:** Incorrect for this question. Larger chunks carry more context but dilute the embedding and crowd the prompt window. Why the correct answer wins: A running summary keeps long sessions inside the window at low token cost.
- **D:** Incorrect for this question. A single blob loses the field boundaries the model needs to answer precisely. Why the correct answer wins: A running summary keeps long sessions inside the window at low token cost.

### Question 26 — B

Answer: Coordinate the specialists with AWS Agent Squad. Agent Squad routes a request to the specialist agent that can handle it. Local study-map skill 2.2 (Agent Orchestration Patterns), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: Agent Squad routes a request to the specialist agent that can handle it.
- **B:** Correct. In this case: Agent Squad routes a request to the specialist agent that can handle it.
- **C:** Incorrect for this question. A synchronous call is simplest and makes the user wait for the final token. Why the correct answer wins: Agent Squad routes a request to the specialist agent that can handle it.
- **D:** Incorrect for this question. One agent with every tool makes tool choice ambiguous and permissions broad. Why the correct answer wins: Agent Squad routes a request to the specialist agent that can handle it.

### Question 27 — B, E

Answers: Orchestrate the reasoning loop in AWS Step Functions; Set an explicit step and budget limit on the agent loop. A state machine makes every step visible and retryable while a hard limit ends a non-converging loop. A state machine makes each reasoning step visible, retryable, and bounded. A hard limit stops a loop that would otherwise consume tokens without converging. Local study-map skill 2.2 (Agent Orchestration Patterns), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. One agent with every tool makes tool choice ambiguous and permissions broad. Why the correct answer wins: A state machine makes every step visible and retryable while a hard limit ends a non-converging loop.
- **B:** Correct. A hard limit stops a loop that would otherwise consume tokens without converging. In this case: A state machine makes every step visible and retryable while a hard limit ends a non-converging loop.
- **C:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: A state machine makes every step visible and retryable while a hard limit ends a non-converging loop.
- **D:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: A state machine makes every step visible and retryable while a hard limit ends a non-converging loop.
- **E:** Correct. A state machine makes each reasoning step visible, retryable, and bounded. In this case: A state machine makes every step visible and retryable while a hard limit ends a non-converging loop.

### Question 28 — A

Answer: Validate tool arguments against a schema before calling. Schema validation rejects a malformed argument instead of sending it to the system of record. Local study-map skill 2.3 (Tool Reliability and Safeguards), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Correct. In this case: Schema validation rejects a malformed argument instead of sending it to the system of record.
- **B:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: Schema validation rejects a malformed argument instead of sending it to the system of record.
- **C:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: Schema validation rejects a malformed argument instead of sending it to the system of record.
- **D:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: Schema validation rejects a malformed argument instead of sending it to the system of record.

### Question 29 — B

Answer: Scope the tool role to only the actions it needs. A narrow role limits what a misdirected agent call can actually change. Local study-map skill 2.3 (Tool Reliability and Safeguards), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: A narrow role limits what a misdirected agent call can actually change.
- **B:** Correct. In this case: A narrow role limits what a misdirected agent call can actually change.
- **C:** Incorrect for this question. A key in an environment variable leaks through images, logs, and job definitions. Why the correct answer wins: A narrow role limits what a misdirected agent call can actually change.
- **D:** Incorrect for this question. A public bucket exposes the corpus to everyone the index was meant to constrain. Why the correct answer wins: A narrow role limits what a misdirected agent call can actually change.

### Question 30 — B

Answer: Buy Amazon Bedrock provisioned throughput for the model. Provisioned throughput reserves model units and gives a predictable token-per-minute ceiling. Local study-map skill 2.4 (Foundation Model Deployment and Capacity), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: Provisioned throughput reserves model units and gives a predictable token-per-minute ceiling.
- **B:** Correct. In this case: Provisioned throughput reserves model units and gives a predictable token-per-minute ceiling.
- **C:** Incorrect for this question. On-demand Bedrock inference bills per token with no committed capacity, which suits spiky or unproven demand. Why the correct answer wins: Provisioned throughput reserves model units and gives a predictable token-per-minute ceiling.
- **D:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: Provisioned throughput reserves model units and gives a predictable token-per-minute ceiling.

### Question 31 — C, E

Answers: Run the work as an Amazon Bedrock batch inference job; Buy Amazon Bedrock provisioned throughput for the model. Batch inference serves the offline volume cheaply and provisioned throughput covers the steady interactive channel. Batch inference trades turnaround time for a lower price on large offline volumes. Provisioned throughput reserves model units and gives a predictable token-per-minute ceiling. Local study-map skill 2.4 (Foundation Model Deployment and Capacity), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. A synchronous call is simplest and makes the user wait for the final token. Why the correct answer wins: Batch inference serves the offline volume cheaply and provisioned throughput covers the steady interactive channel.
- **B:** Incorrect for this question. On-demand Bedrock inference bills per token with no committed capacity, which suits spiky or unproven demand. Why the correct answer wins: Batch inference serves the offline volume cheaply and provisioned throughput covers the steady interactive channel.
- **C:** Correct. Provisioned throughput reserves model units and gives a predictable token-per-minute ceiling. In this case: Batch inference serves the offline volume cheaply and provisioned throughput covers the steady interactive channel.
- **D:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: Batch inference serves the offline volume cheaply and provisioned throughput covers the steady interactive channel.
- **E:** Correct. Batch inference trades turnaround time for a lower price on large offline volumes. In this case: Batch inference serves the offline volume cheaply and provisioned throughput covers the steady interactive channel.

### Question 32 — A

Answer: Route domain events through Amazon EventBridge. EventBridge decouples producers from the GenAI consumer with rules and filtering. Local study-map skill 2.5 (Enterprise Integration Patterns), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Correct. In this case: EventBridge decouples producers from the GenAI consumer with rules and filtering.
- **B:** Incorrect for this question. A queue absorbs bursts and lets a worker retry a failed model call. Why the correct answer wins: EventBridge decouples producers from the GenAI consumer with rules and filtering.
- **C:** Incorrect for this question. AppFlow copies data from supported SaaS sources without custom connectors. Why the correct answer wins: EventBridge decouples producers from the GenAI consumer with rules and filtering.
- **D:** Incorrect for this question. SNS delivers one event to many subscribers without the caller tracking them. Why the correct answer wins: EventBridge decouples producers from the GenAI consumer with rules and filtering.

### Question 33 — A

Answer: Buffer the work in an Amazon SQS queue. A queue absorbs bursts and lets a worker retry a failed model call. Local study-map skill 2.5 (Enterprise Integration Patterns), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Correct. In this case: A queue absorbs bursts and lets a worker retry a failed model call.
- **B:** Incorrect for this question. A synchronous call is simplest and makes the user wait for the final token. Why the correct answer wins: A queue absorbs bursts and lets a worker retry a failed model call.
- **C:** Incorrect for this question. API Gateway adds authentication, throttling, request validation, and streaming to the model call. Why the correct answer wins: A queue absorbs bursts and lets a worker retry a failed model call.
- **D:** Incorrect for this question. SNS delivers one event to many subscribers without the caller tracking them. Why the correct answer wins: A queue absorbs bursts and lets a worker retry a failed model call.

### Question 34 — C

Answer: Authenticate users with Amazon Cognito. Cognito issues scoped tokens so each request carries an identity. Local study-map skill 2.6 (Identity for Model Access), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. A public bucket exposes the corpus to everyone the index was meant to constrain. Why the correct answer wins: Cognito issues scoped tokens so each request carries an identity.
- **B:** Incorrect for this question. A scoped role issues temporary credentials with only the needed permissions. Why the correct answer wins: Cognito issues scoped tokens so each request carries an identity.
- **C:** Correct. In this case: Cognito issues scoped tokens so each request carries an identity.
- **D:** Incorrect for this question. A key in an environment variable leaks through images, logs, and job definitions. Why the correct answer wins: Cognito issues scoped tokens so each request carries an identity.

### Question 35 — C

Answer: Put one internal GenAI gateway in front of every model call. A gateway centralises credentials, quotas, logging, and model routing for all teams. Local study-map skill 2.7 (CI/CD and GenAI Gateway), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. A key in an environment variable leaks through images, logs, and job definitions. Why the correct answer wins: A gateway centralises credentials, quotas, logging, and model routing for all teams.
- **B:** Incorrect for this question. Direct calls from every app scatter keys, quotas, and logging across teams. Why the correct answer wins: A gateway centralises credentials, quotas, logging, and model routing for all teams.
- **C:** Correct. In this case: A gateway centralises credentials, quotas, logging, and model routing for all teams.
- **D:** Incorrect for this question. A hardcoded identifier forces a code change and a release to try another model. Why the correct answer wins: A gateway centralises credentials, quotas, logging, and model routing for all teams.

### Question 36 — D, E

Answers: Shift traffic with an AWS CodeDeploy canary deployment; Run the evaluation suite in AWS CodeBuild. The canary limits exposure to a small traffic share and the build runs the evaluation first. A canary exposes a small share of traffic to the new version before the rest follows. CodeBuild runs the tests and quality gates as part of the release. Local study-map skill 2.7 (CI/CD and GenAI Gateway), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. A key in an environment variable leaks through images, logs, and job definitions. Why the correct answer wins: The canary limits exposure to a small traffic share and the build runs the evaluation first.
- **B:** Incorrect for this question. Direct calls from every app scatter keys, quotas, and logging across teams. Why the correct answer wins: The canary limits exposure to a small traffic share and the build runs the evaluation first.
- **C:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: The canary limits exposure to a small traffic share and the build runs the evaluation first.
- **D:** Correct. CodeBuild runs the tests and quality gates as part of the release. In this case: The canary limits exposure to a small traffic share and the build runs the evaluation first.
- **E:** Correct. A canary exposes a small share of traffic to the new version before the rest follows. In this case: The canary limits exposure to a small traffic share and the build runs the evaluation first.

### Question 37 — B

Answer: Queue the prompt and return a job identifier for polling. Asynchronous processing suits long generations that outlast an API timeout. Local study-map skill 2.8 (Streaming and Asynchronous APIs), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. Server-sent events deliver incremental text over ordinary HTTP. Why the correct answer wins: Asynchronous processing suits long generations that outlast an API timeout.
- **B:** Correct. In this case: Asynchronous processing suits long generations that outlast an API timeout.
- **C:** Incorrect for this question. A WebSocket keeps one connection open for incremental tokens. Why the correct answer wins: Asynchronous processing suits long generations that outlast an API timeout.
- **D:** Incorrect for this question. A synchronous call is simplest and makes the user wait for the final token. Why the correct answer wins: Asynchronous processing suits long generations that outlast an API timeout.

### Question 38 — C

Answer: Retry throttled calls with exponential backoff and jitter. Backoff with jitter spreads retries so a throttled client does not stampede the service. Local study-map skill 2.9 (API Resilience and Backoff), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: Backoff with jitter spreads retries so a throttled client does not stampede the service.
- **B:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: Backoff with jitter spreads retries so a throttled client does not stampede the service.
- **C:** Correct. In this case: Backoff with jitter spreads retries so a throttled client does not stampede the service.
- **D:** Incorrect for this question. A circuit breaker stops sending traffic to a dependency that is already failing. Why the correct answer wins: Backoff with jitter spreads retries so a throttled client does not stampede the service.

### Question 39 — A

Answer: Open a circuit breaker after repeated dependency failures. A circuit breaker stops sending traffic to a dependency that is already failing. Local study-map skill 2.9 (API Resilience and Backoff), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Correct. In this case: A circuit breaker stops sending traffic to a dependency that is already failing.
- **B:** Incorrect for this question. A synchronous call is simplest and makes the user wait for the final token. Why the correct answer wins: A circuit breaker stops sending traffic to a dependency that is already failing.
- **C:** Incorrect for this question. Backoff with jitter spreads retries so a throttled client does not stampede the service. Why the correct answer wins: A circuit breaker stops sending traffic to a dependency that is already failing.
- **D:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: A circuit breaker stops sending traffic to a dependency that is already failing.

### Question 40 — D

Answer: Front the model with Amazon API Gateway. API Gateway adds authentication, throttling, request validation, and streaming to the model call. Local study-map skill 2.10 (Application Integration and Low Code), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. An edge cache answers identical requests without reaching the model. Why the correct answer wins: API Gateway adds authentication, throttling, request validation, and streaming to the model call.
- **B:** Incorrect for this question. Amplify supplies declarative UI and hosting for the client that talks to the assistant. Why the correct answer wins: API Gateway adds authentication, throttling, request validation, and streaming to the model call.
- **C:** Incorrect for this question. Direct calls from every app scatter keys, quotas, and logging across teams. Why the correct answer wins: API Gateway adds authentication, throttling, request validation, and streaming to the model call.
- **D:** Correct. In this case: API Gateway adds authentication, throttling, request validation, and streaming to the model call.

### Question 41 — D

Answer: Expose the assistant through AWS AppSync. AppSync gives a managed GraphQL API with subscriptions for live responses. Local study-map skill 2.10 (Application Integration and Low Code), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. Server-sent events deliver incremental text over ordinary HTTP. Why the correct answer wins: AppSync gives a managed GraphQL API with subscriptions for live responses.
- **B:** Incorrect for this question. API Gateway adds authentication, throttling, request validation, and streaming to the model call. Why the correct answer wins: AppSync gives a managed GraphQL API with subscriptions for live responses.
- **C:** Incorrect for this question. Edge logic trims, redacts, or routes a request before it crosses to the model Region. Why the correct answer wins: AppSync gives a managed GraphQL API with subscriptions for live responses.
- **D:** Correct. In this case: AppSync gives a managed GraphQL API with subscriptions for live responses.

### Question 42 — C

Answer: Generate and explain the integration code with Amazon Q Developer. Q Developer drafts and explains SDK calls inside the editor, which speeds up the plumbing. Local study-map skill 2.11 (Developer Productivity Tooling), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: Q Developer drafts and explains SDK calls inside the editor, which speeds up the plumbing.
- **B:** Incorrect for this question. A pipeline ties source, build, test, and deploy into one auditable flow. Why the correct answer wins: Q Developer drafts and explains SDK calls inside the editor, which speeds up the plumbing.
- **C:** Correct. In this case: Q Developer drafts and explains SDK calls inside the editor, which speeds up the plumbing.
- **D:** Incorrect for this question. CodeBuild runs the tests and quality gates as part of the release. Why the correct answer wins: Q Developer drafts and explains SDK calls inside the editor, which speeds up the plumbing.

### Question 43 — C

Answer: Query the prompt and response logs with CloudWatch Logs Insights. Logs Insights correlates a spike in errors with the prompts that caused it. Local study-map skill 2.12 (Integration Troubleshooting), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. CloudTrail records who changed models, keys, and guardrails. Why the correct answer wins: Logs Insights correlates a spike in errors with the prompts that caused it.
- **B:** Incorrect for this question. A trace shows which hop in the chain added the latency. Why the correct answer wins: Logs Insights correlates a spike in errors with the prompts that caused it.
- **C:** Correct. In this case: Logs Insights correlates a spike in errors with the prompts that caused it.
- **D:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: Logs Insights correlates a spike in errors with the prompts that caused it.

### Question 44 — A

Answer: Apply Amazon Bedrock Guardrails content filters. Content filters score and block harmful input and output on the request path. Local study-map skill 3.1 (Content Safety Controls), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Correct. In this case: Content filters score and block harmful input and output on the request path.
- **B:** Incorrect for this question. Low temperature narrows sampling so repeatable factual answers stay stable. Why the correct answer wins: Content filters score and block harmful input and output on the request path.
- **C:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: Content filters score and block harmful input and output on the request path.
- **D:** Incorrect for this question. A token cap bounds the cost of a runaway answer and the latency of every call. Why the correct answer wins: Content filters score and block harmful input and output on the request path.

### Question 45 — D, E

Answers: Define denied topics in Amazon Bedrock Guardrails; Add automated reasoning checks for policy statements. Denied topics refuse the ruled-out subject and reasoning checks verify a response against encoded policy rules. Denied topics refuse the subject areas the business has ruled out. Reasoning checks verify a response against encoded policy rules rather than a similarity score. Local study-map skill 3.1 (Content Safety Controls), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. A token cap bounds the cost of a runaway answer and the latency of every call. Why the correct answer wins: Denied topics refuse the ruled-out subject and reasoning checks verify a response against encoded policy rules.
- **B:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: Denied topics refuse the ruled-out subject and reasoning checks verify a response against encoded policy rules.
- **C:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: Denied topics refuse the ruled-out subject and reasoning checks verify a response against encoded policy rules.
- **D:** Correct. Denied topics refuse the subject areas the business has ruled out. In this case: Denied topics refuse the ruled-out subject and reasoning checks verify a response against encoded policy rules.
- **E:** Correct. Reasoning checks verify a response against encoded policy rules rather than a similarity score. In this case: Denied topics refuse the ruled-out subject and reasoning checks verify a response against encoded policy rules.

### Question 46 — B

Answer: Require the answer to cite the retrieved passage. A citation makes each claim traceable to a source the reader can check. Local study-map skill 3.2 (Grounding and Hallucination Reduction), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. An escalation path keeps consequential answers with a human owner. Why the correct answer wins: A citation makes each claim traceable to a source the reader can check.
- **B:** Correct. In this case: A citation makes each claim traceable to a source the reader can check.
- **C:** Incorrect for this question. A token cap bounds the cost of a runaway answer and the latency of every call. Why the correct answer wins: A citation makes each claim traceable to a source the reader can check.
- **D:** Incorrect for this question. A score lets the interface route low-confidence answers to a human. Why the correct answer wins: A citation makes each claim traceable to a source the reader can check.

### Question 47 — D

Answer: Translate the question into SQL and run it on the database. Deterministic query generation avoids asking a model to compute figures from memory. Local study-map skill 3.2 (Grounding and Hallucination Reduction), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. Low temperature narrows sampling so repeatable factual answers stay stable. Why the correct answer wins: Deterministic query generation avoids asking a model to compute figures from memory.
- **B:** Incorrect for this question. A score lets the interface route low-confidence answers to a human. Why the correct answer wins: Deterministic query generation avoids asking a model to compute figures from memory.
- **C:** Incorrect for this question. A schema makes the output machine-parseable and rejects prose that breaks the contract. Why the correct answer wins: Deterministic query generation avoids asking a model to compute figures from memory.
- **D:** Correct. In this case: Deterministic query generation avoids asking a model to compute figures from memory.

### Question 48 — C

Answer: Screen inputs for instruction override and jailbreak patterns. A pre-filter catches text that tries to replace the system instruction. Local study-map skill 3.3 (Prompt Injection Defence), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: A pre-filter catches text that tries to replace the system instruction.
- **B:** Incorrect for this question. A token cap bounds the cost of a runaway answer and the latency of every call. Why the correct answer wins: A pre-filter catches text that tries to replace the system instruction.
- **C:** Correct. In this case: A pre-filter catches text that tries to replace the system instruction.
- **D:** Incorrect for this question. Low temperature narrows sampling so repeatable factual answers stay stable. Why the correct answer wins: A pre-filter catches text that tries to replace the system instruction.

### Question 49 — C

Answer: Run an adversarial prompt suite before each release. A hostile test set finds regressions in refusal behaviour before users do. Local study-map skill 3.3 (Prompt Injection Defence), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: A hostile test set finds regressions in refusal behaviour before users do.
- **B:** Incorrect for this question. A golden set with known answers catches a regression the moment it ships. Why the correct answer wins: A hostile test set finds regressions in refusal behaviour before users do.
- **C:** Correct. In this case: A hostile test set finds regressions in refusal behaviour before users do.
- **D:** Incorrect for this question. A rubric with human scores gives a reference the automatic metrics can be checked against. Why the correct answer wins: A hostile test set finds regressions in refusal behaviour before users do.

### Question 50 — C

Answer: Mask personal data before the prompt is built. Masking at the boundary keeps personal data out of the model request entirely. Local study-map skill 3.4 (Privacy and PII Protection), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. Macie finds sensitive data at rest so the corpus can be cleaned before indexing. Why the correct answer wins: Masking at the boundary keeps personal data out of the model request entirely.
- **B:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: Masking at the boundary keeps personal data out of the model request entirely.
- **C:** Correct. In this case: Masking at the boundary keeps personal data out of the model request entirely.
- **D:** Incorrect for this question. PII filters detect and mask personal data in prompts and responses. Why the correct answer wins: Masking at the boundary keeps personal data out of the model request entirely.

### Question 51 — C, E

Answers: Detect personal data with Amazon Comprehend; Enable sensitive-information filters in Amazon Bedrock Guardrails. Comprehend identifies the entities in storage and the sensitive-information filter masks what reaches the user. Comprehend identifies entities and PII so they can be masked before the model sees them. PII filters detect and mask personal data in prompts and responses. Local study-map skill 3.4 (Privacy and PII Protection), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. A key in an environment variable leaks through images, logs, and job definitions. Why the correct answer wins: Comprehend identifies the entities in storage and the sensitive-information filter masks what reaches the user.
- **B:** Incorrect for this question. Content filters score and block harmful input and output on the request path. Why the correct answer wins: Comprehend identifies the entities in storage and the sensitive-information filter masks what reaches the user.
- **C:** Correct. Comprehend identifies entities and PII so they can be masked before the model sees them. In this case: Comprehend identifies the entities in storage and the sensitive-information filter masks what reaches the user.
- **D:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: Comprehend identifies the entities in storage and the sensitive-information filter masks what reaches the user.
- **E:** Correct. PII filters detect and mask personal data in prompts and responses. In this case: Comprehend identifies the entities in storage and the sensitive-information filter masks what reaches the user.

### Question 52 — A

Answer: Call the model through an interface VPC endpoint. A private endpoint keeps model traffic off the public internet. Local study-map skill 3.5 (Network and Data Isolation), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Correct. In this case: A private endpoint keeps model traffic off the public internet.
- **B:** Incorrect for this question. A key in an environment variable leaks through images, logs, and job definitions. Why the correct answer wins: A private endpoint keeps model traffic off the public internet.
- **C:** Incorrect for this question. A public bucket exposes the corpus to everyone the index was meant to constrain. Why the correct answer wins: A private endpoint keeps model traffic off the public internet.
- **D:** Incorrect for this question. An edge cache answers identical requests without reaching the model. Why the correct answer wins: A private endpoint keeps model traffic off the public internet.

### Question 53 — D

Answer: Put AWS WAF rules in front of the public endpoint. WAF blocks known bad request patterns before they consume model capacity. Local study-map skill 3.5 (Network and Data Isolation), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. A public bucket exposes the corpus to everyone the index was meant to constrain. Why the correct answer wins: WAF blocks known bad request patterns before they consume model capacity.
- **B:** Incorrect for this question. An edge cache answers identical requests without reaching the model. Why the correct answer wins: WAF blocks known bad request patterns before they consume model capacity.
- **C:** Incorrect for this question. Private subnets remove inbound internet routing from the compute tier. Why the correct answer wins: WAF blocks known bad request patterns before they consume model capacity.
- **D:** Correct. In this case: WAF blocks known bad request patterns before they consume model capacity.

### Question 54 — C

Answer: Record control-plane activity in AWS CloudTrail. CloudTrail records who changed models, keys, and guardrails. Local study-map skill 3.6 (Governance, Lineage, and Audit), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. Grafana combines model, infrastructure, and business metrics on one screen. Why the correct answer wins: CloudTrail records who changed models, keys, and guardrails.
- **B:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: CloudTrail records who changed models, keys, and guardrails.
- **C:** Correct. In this case: CloudTrail records who changed models, keys, and guardrails.
- **D:** Incorrect for this question. Invocation logs capture the request, the response, and the token counts. Why the correct answer wins: CloudTrail records who changed models, keys, and guardrails.

### Question 55 — D, E

Answers: Record data lineage in the AWS Glue Data Catalog; Turn on Amazon Bedrock model invocation logging. Lineage ties the answer to its corpus version and invocation logs hold the request and the response. Lineage shows which corpus and version produced an answer. Invocation logs capture the request, the response, and the token counts. Local study-map skill 3.6 (Governance, Lineage, and Audit), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. Low temperature narrows sampling so repeatable factual answers stay stable. Why the correct answer wins: Lineage ties the answer to its corpus version and invocation logs hold the request and the response.
- **B:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: Lineage ties the answer to its corpus version and invocation logs hold the request and the response.
- **C:** Incorrect for this question. A key in an environment variable leaks through images, logs, and job definitions. Why the correct answer wins: Lineage ties the answer to its corpus version and invocation logs hold the request and the response.
- **D:** Correct. Lineage shows which corpus and version produced an answer. In this case: Lineage ties the answer to its corpus version and invocation logs hold the request and the response.
- **E:** Correct. Invocation logs capture the request, the response, and the token counts. In this case: Lineage ties the answer to its corpus version and invocation logs hold the request and the response.

### Question 56 — A

Answer: Publish a model card with the model version. A model card documents intended use and known limits for reviewers. Local study-map skill 3.7 (Responsible AI and Transparency), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Correct. In this case: A model card documents intended use and known limits for reviewers.
- **B:** Incorrect for this question. A schema makes the output machine-parseable and rejects prose that breaks the contract. Why the correct answer wins: A model card documents intended use and known limits for reviewers.
- **C:** Incorrect for this question. A Bedrock evaluation job scores candidate models on your prompts and metrics before you choose. Why the correct answer wins: A model card documents intended use and known limits for reviewers.
- **D:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: A model card documents intended use and known limits for reviewers.

### Question 57 — D

Answer: Return a confidence score with each answer. A score lets the interface route low-confidence answers to a human. Local study-map skill 3.7 (Responsible AI and Transparency), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: A score lets the interface route low-confidence answers to a human.
- **B:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: A score lets the interface route low-confidence answers to a human.
- **C:** Incorrect for this question. A token cap bounds the cost of a runaway answer and the latency of every call. Why the correct answer wins: A score lets the interface route low-confidence answers to a human.
- **D:** Correct. In this case: A score lets the interface route low-confidence answers to a human.

### Question 58 — D

Answer: Report fairness metrics per user segment. Segment metrics expose a quality gap that an overall average hides. Local study-map skill 3.8 (Fairness and Compliance Monitoring), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. A drift alert catches a fairness regression after a model or prompt change. Why the correct answer wins: Segment metrics expose a quality gap that an overall average hides.
- **B:** Incorrect for this question. Anomaly detection finds an unexpected token bill without a fixed threshold. Why the correct answer wins: Segment metrics expose a quality gap that an overall average hides.
- **C:** Incorrect for this question. A latency alarm fires on the symptom users feel. Why the correct answer wins: Segment metrics expose a quality gap that an overall average hides.
- **D:** Correct. In this case: Segment metrics expose a quality gap that an overall average hides.

### Question 59 — B

Answer: Prune older turns from the context window. Dropping stale turns cuts input tokens without losing the current instruction. Local study-map skill 4.1 (Token Cost Efficiency), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: Dropping stale turns cuts input tokens without losing the current instruction.
- **B:** Correct. In this case: Dropping stale turns cuts input tokens without losing the current instruction.
- **C:** Incorrect for this question. More passages raise recall and also lengthen the prompt and the cost per call. Why the correct answer wins: Dropping stale turns cuts input tokens without losing the current instruction.
- **D:** Incorrect for this question. Larger chunks carry more context but dilute the embedding and crowd the prompt window. Why the correct answer wins: Dropping stale turns cuts input tokens without losing the current instruction.

### Question 60 — B

Answer: Cap the response length in the request. A token cap bounds the cost of a runaway answer and the latency of every call. Local study-map skill 4.1 (Token Cost Efficiency), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Incorrect for this question. Larger chunks carry more context but dilute the embedding and crowd the prompt window. Why the correct answer wins: A token cap bounds the cost of a runaway answer and the latency of every call.
- **B:** Correct. In this case: A token cap bounds the cost of a runaway answer and the latency of every call.
- **C:** Incorrect for this question. A single blob loses the field boundaries the model needs to answer precisely. Why the correct answer wins: A token cap bounds the cost of a runaway answer and the latency of every call.
- **D:** Incorrect for this question. More passages raise recall and also lengthen the prompt and the cost per call. Why the correct answer wins: A token cap bounds the cost of a runaway answer and the latency of every call.

### Question 61 — D

Answer: Cache the response under a hash of the normalised request. A hash cache is exact and avoids a false hit between similar questions. Local study-map skill 4.2 (Model Tiering and Caching), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Incorrect for this question. A semantic cache serves a near-duplicate question without a model call. Why the correct answer wins: A hash cache is exact and avoids a false hit between similar questions.
- **B:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: A hash cache is exact and avoids a false hit between similar questions.
- **C:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: A hash cache is exact and avoids a false hit between similar questions.
- **D:** Correct. In this case: A hash cache is exact and avoids a false hit between similar questions.

### Question 62 — A, B

Answers: Send routine prompts to a small model and hard prompts to a large one; Cache answers by embedding similarity to earlier questions. Routing sends easy prompts to a small model and a semantic cache removes near-duplicate calls. Tiered routing spends the large model only on the requests that need it. A semantic cache serves a near-duplicate question without a model call. Local study-map skill 4.2 (Model Tiering and Caching), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Correct. Tiered routing spends the large model only on the requests that need it. In this case: Routing sends easy prompts to a small model and a semantic cache removes near-duplicate calls.
- **B:** Correct. A semantic cache serves a near-duplicate question without a model call. In this case: Routing sends easy prompts to a small model and a semantic cache removes near-duplicate calls.
- **C:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: Routing sends easy prompts to a small model and a semantic cache removes near-duplicate calls.
- **D:** Incorrect for this question. A full fine-tune changes all weights, which is expensive and gives one model per task. Why the correct answer wins: Routing sends easy prompts to a small model and a semantic cache removes near-duplicate calls.
- **E:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: Routing sends easy prompts to a small model and a semantic cache removes near-duplicate calls.

### Question 63 — B

Answer: Precompute answers for predictable questions on a schedule. Precomputation moves repeatable work into a cheap batch window. Local study-map skill 4.3 (Throughput and Latency Optimisation), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: Precomputation moves repeatable work into a cheap batch window.
- **B:** Correct. In this case: Precomputation moves repeatable work into a cheap batch window.
- **C:** Incorrect for this question. A synchronous call is simplest and makes the user wait for the final token. Why the correct answer wins: Precomputation moves repeatable work into a cheap batch window.
- **D:** Incorrect for this question. Streaming lowers perceived latency without changing total generation time. Why the correct answer wins: Precomputation moves repeatable work into a cheap batch window.

### Question 64 — D, E

Answers: Plan capacity from measured tokens per minute; Issue independent model calls in parallel. Capacity sized from observed token throughput avoids throttling and parallel calls cut wall-clock time. Parallel calls cut wall-clock time for sub-tasks that do not depend on each other. Local study-map skill 4.3 (Throughput and Latency Optimisation), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: Capacity sized from observed token throughput avoids throttling and parallel calls cut wall-clock time.
- **B:** Incorrect for this question. Batch inference trades turnaround time for a lower price on large offline volumes. Why the correct answer wins: Capacity sized from observed token throughput avoids throttling and parallel calls cut wall-clock time.
- **C:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: Capacity sized from observed token throughput avoids throttling and parallel calls cut wall-clock time.
- **D:** Correct. In this case: Capacity sized from observed token throughput avoids throttling and parallel calls cut wall-clock time.
- **E:** Correct. Parallel calls cut wall-clock time for sub-tasks that do not depend on each other. In this case: Capacity sized from observed token throughput avoids throttling and parallel calls cut wall-clock time.

### Question 65 — C

Answer: Build the operations view in Amazon Managed Grafana. Grafana combines model, infrastructure, and business metrics on one screen. Local study-map skill 4.4 (GenAI Observability), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: Grafana combines model, infrastructure, and business metrics on one screen.
- **B:** Incorrect for this question. CloudTrail records who changed models, keys, and guardrails. Why the correct answer wins: Grafana combines model, infrastructure, and business metrics on one screen.
- **C:** Correct. In this case: Grafana combines model, infrastructure, and business metrics on one screen.
- **D:** Incorrect for this question. A model card documents intended use and known limits for reviewers. Why the correct answer wins: Grafana combines model, infrastructure, and business metrics on one screen.

### Question 66 — B, C

Answers: Probe the endpoint with CloudWatch Synthetics; Alarm on p95 latency and error rate. A synthetic canary detects an outage early and a latency alarm fires on the symptom users feel. A synthetic canary detects an outage before a user reports it. Local study-map skill 4.4 (GenAI Observability), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Incorrect for this question. Anomaly detection finds an unexpected token bill without a fixed threshold. Why the correct answer wins: A synthetic canary detects an outage early and a latency alarm fires on the symptom users feel.
- **B:** Correct. In this case: A synthetic canary detects an outage early and a latency alarm fires on the symptom users feel.
- **C:** Correct. A synthetic canary detects an outage before a user reports it. In this case: A synthetic canary detects an outage early and a latency alarm fires on the symptom users feel.
- **D:** Incorrect for this question. A model card documents intended use and known limits for reviewers. Why the correct answer wins: A synthetic canary detects an outage early and a latency alarm fires on the symptom users feel.
- **E:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: A synthetic canary detects an outage early and a latency alarm fires on the symptom users feel.

### Question 67 — B

Answer: Alert when a tenant crosses its monthly token budget. A budget alert stops one tenant from consuming the shared quota. Local study-map skill 4.5 (Cost Attribution and Governance), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Incorrect for this question. A Savings Plan discounts the predictable part of the compute baseline. Why the correct answer wins: A budget alert stops one tenant from consuming the shared quota.
- **B:** Correct. In this case: A budget alert stops one tenant from consuming the shared quota.
- **C:** Incorrect for this question. Anomaly detection finds an unexpected token bill without a fixed threshold. Why the correct answer wins: A budget alert stops one tenant from consuming the shared quota.
- **D:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: A budget alert stops one tenant from consuming the shared quota.

### Question 68 — A

Answer: Have reviewers score a sample against a written rubric. A rubric with human scores gives a reference the automatic metrics can be checked against. Local study-map skill 5.1 (GenAI Evaluation Metrics), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Correct. In this case: A rubric with human scores gives a reference the automatic metrics can be checked against.
- **B:** Incorrect for this question. Relevance separates an off-topic answer from a factually wrong one. Why the correct answer wins: A rubric with human scores gives a reference the automatic metrics can be checked against.
- **C:** Incorrect for this question. Overlap metrics are cheap and reward wording that matches the references. Why the correct answer wins: A rubric with human scores gives a reference the automatic metrics can be checked against.
- **D:** Incorrect for this question. Embedding-based similarity credits a correct paraphrase that word overlap misses. Why the correct answer wins: A rubric with human scores gives a reference the automatic metrics can be checked against.

### Question 69 — A, B

Answers: Score candidate answers with a judge model on a fixed rubric; Measure the judge model against expert labels first. A judge model scales the scoring and an agreement check shows whether it matches expert labels. A judge model scales subjective scoring and needs its own agreement check. Agreement with experts shows whether the judge can be trusted on this task. Local study-map skill 5.1 (GenAI Evaluation Metrics), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Correct. Agreement with experts shows whether the judge can be trusted on this task. In this case: A judge model scales the scoring and an agreement check shows whether it matches expert labels.
- **B:** Correct. A judge model scales subjective scoring and needs its own agreement check. In this case: A judge model scales the scoring and an agreement check shows whether it matches expert labels.
- **C:** Incorrect for this question. Overlap metrics are cheap and reward wording that matches the references. Why the correct answer wins: A judge model scales the scoring and an agreement check shows whether it matches expert labels.
- **D:** Incorrect for this question. Recall shows whether the answer was missing evidence before generation began. Why the correct answer wins: A judge model scales the scoring and an agreement check shows whether it matches expert labels.
- **E:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: A judge model scales the scoring and an agreement check shows whether it matches expert labels.

### Question 70 — B

Answer: Mirror production traffic to the new version and compare offline. Shadow traffic compares answers with no user exposure. Local study-map skill 5.2 (Model Comparison and Traffic Testing), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Incorrect for this question. An A/B test measures the difference on real traffic before a full switch. Why the correct answer wins: Shadow traffic compares answers with no user exposure.
- **B:** Correct. In this case: Shadow traffic compares answers with no user exposure.
- **C:** Incorrect for this question. A canary limits the blast radius of a prompt or model change. Why the correct answer wins: Shadow traffic compares answers with no user exposure.
- **D:** Incorrect for this question. A rubric with human scores gives a reference the automatic metrics can be checked against. Why the correct answer wins: Shadow traffic compares answers with no user exposure.

### Question 71 — C

Answer: Run the release against a curated golden question set. A golden set with known answers catches a regression the moment it ships. Local study-map skill 5.3 (Regression Testing and Quality Gates), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: A golden set with known answers catches a regression the moment it ships.
- **B:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: A golden set with known answers catches a regression the moment it ships.
- **C:** Correct. In this case: A golden set with known answers catches a regression the moment it ships.
- **D:** Incorrect for this question. A rubric with human scores gives a reference the automatic metrics can be checked against. Why the correct answer wins: A golden set with known answers catches a regression the moment it ships.

### Question 72 — B, E

Answers: Block the release when evaluation drops below the threshold; Diff the new responses against the previous version. A quality gate blocks the regression and a diff highlights the wording changes behind it. A quality gate stops a measurable regression from reaching production. Local study-map skill 5.3 (Regression Testing and Quality Gates), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: A quality gate blocks the regression and a diff highlights the wording changes behind it.
- **B:** Correct. In this case: A quality gate blocks the regression and a diff highlights the wording changes behind it.
- **C:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: A quality gate blocks the regression and a diff highlights the wording changes behind it.
- **D:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: A quality gate blocks the regression and a diff highlights the wording changes behind it.
- **E:** Correct. A quality gate stops a measurable regression from reaching production. In this case: A quality gate blocks the regression and a diff highlights the wording changes behind it.

### Question 73 — D

Answer: Measure whether the agent called the right tool with the right arguments. Tool accuracy locates the failure inside the agent loop rather than at the answer. Local study-map skill 5.4 (Retrieval and Agent Evaluation), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Incorrect for this question. Overlap metrics are cheap and reward wording that matches the references. Why the correct answer wins: Tool accuracy locates the failure inside the agent loop rather than at the answer.
- **B:** Incorrect for this question. Recall shows whether the answer was missing evidence before generation began. Why the correct answer wins: Tool accuracy locates the failure inside the agent loop rather than at the answer.
- **C:** Incorrect for this question. Completion rate is the outcome metric for an agent that must actually finish work. Why the correct answer wins: Tool accuracy locates the failure inside the agent loop rather than at the answer.
- **D:** Correct. In this case: Tool accuracy locates the failure inside the agent loop rather than at the answer.

### Question 74 — B, D

Answers: Measure whether the needed passage was retrieved at all; Measure the share of agent tasks completed end to end. Recall shows whether the needed passage was retrieved and completion rate shows whether the task ended. Recall shows whether the answer was missing evidence before generation began. Completion rate is the outcome metric for an agent that must actually finish work. Local study-map skill 5.4 (Retrieval and Agent Evaluation), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Incorrect for this question. Overlap metrics are cheap and reward wording that matches the references. Why the correct answer wins: Recall shows whether the needed passage was retrieved and completion rate shows whether the task ended.
- **B:** Correct. Recall shows whether the answer was missing evidence before generation began. In this case: Recall shows whether the needed passage was retrieved and completion rate shows whether the task ended.
- **C:** Incorrect for this question. Embedding-based similarity credits a correct paraphrase that word overlap misses. Why the correct answer wins: Recall shows whether the needed passage was retrieved and completion rate shows whether the task ended.
- **D:** Correct. Completion rate is the outcome metric for an agent that must actually finish work. In this case: Recall shows whether the needed passage was retrieved and completion rate shows whether the task ended.
- **E:** Incorrect for this question. Tool accuracy locates the failure inside the agent loop rather than at the answer. Why the correct answer wins: Recall shows whether the needed passage was retrieved and completion rate shows whether the task ended.

### Question 75 — D

Answer: Inspect the agent reasoning trace for the failed task. The trace shows which step misread the request or the tool result. Local study-map skill 5.5 (GenAI Troubleshooting), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Incorrect for this question. A truncation check shows whether the model ever saw the end of the instruction. Why the correct answer wins: The trace shows which step misread the request or the tool result.
- **B:** Incorrect for this question. A trace shows which hop in the chain added the latency. Why the correct answer wins: The trace shows which step misread the request or the tool result.
- **C:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: The trace shows which step misread the request or the tool result.
- **D:** Correct. In this case: The trace shows which step misread the request or the tool result.
