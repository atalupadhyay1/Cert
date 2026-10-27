# AWS Certified Generative AI Developer - Professional (AIP-C01) — Full-Length Mock Exam 5

Generative AI Developer · 75 questions · 180 minutes · scaled passing score 750 of 1000

Blueprint-weighted mock exam. Item mix: 60 multiple-choice and 15 multiple-response items (the selection count is stated in each multi-response stem). The published exam has 75 questions in 180 minutes, of which 65 are scored and 10 are unscored, and AWS does not identify the unscored items. AWS publishes no split between multiple-choice and multiple-response items, so the 15-item multi-response block is an authoring choice. At 75 items in 180 minutes this set matches the published pacing at about 144 seconds per item, including the same unscored proportion. The published format has no case-study component, so no case-study item appears here. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied AWS exam items.

## Questions

---

## Domain 1 — Foundation Model Integration, Data Management, and Compliance (31%) — Model integration, data pipelines, vector stores, retrieval, and prompts

### 1. A manufacturer must keep some inference on the plant floor for latency while sharing one model contract with the cloud. Which two architectural choices fit? Select two.

- A. Run the inference component on AWS Outposts
- B. Put one internal GenAI gateway in front of every model call
- C. Hardcode one model identifier in the application source
- D. Use one frontier model for every request
- E. Let each application call the model API directly

### 2. Twelve plants will use the same maintenance assistant, and each plant maintains its own manual set. Which two components make that reuse practical? Select two.

- A. Keep the prompt as a string constant in the application code
- B. Version the prompt in Amazon Bedrock Prompt Management
- C. Let each application call the model API directly
- D. Concatenate all fields into one unlabelled text block
- E. Use an Amazon Bedrock knowledge base with a managed vector store

### 3. Before a work-instruction assistant is funded, technicians must confirm the drafts are safe to follow. What should the pilot produce?

- A. Report ROUGE and BLEU against the reference answers
- B. Compare the candidates with an Amazon Bedrock model evaluation job
- C. Use one frontier model for every request
- D. Have reviewers score a sample against a written rubric

### 4. Three models are candidates for classifying fault reports, and four hundred reports carry engineer-assigned categories. How should the choice be made?

- A. Use one frontier model for every request
- B. Compare the candidates with an Amazon Bedrock model evaluation job
- C. Fine-tune with low-rank adaptation adapters
- D. Run a full fine-tune of every model weight

### 5. A handheld tool maps twelve spoken commands to machine actions and must respond instantly offline of the cloud. Which model choice fits?

- A. Route the call through Amazon Bedrock cross-Region inference
- B. Right-size the model to the task difficulty
- C. Run a full fine-tune of every model weight
- D. Use one frontier model for every request

### 6. One plant wants to trial a different model for shift handover notes next month without a release. What allows that?

- A. Hardcode one model identifier in the application source
- B. Let each application call the model API directly
- C. Put the model identifier in AWS AppConfig and switch it without a deploy
- D. Keep the prompt as a string constant in the application code

### 7. A model is throttled in the plant's home Region during a production ramp while a neighbouring Region has capacity. What absorbs the overflow?

- A. Keep a GPU endpoint running for occasional requests
- B. Retry the failed call until it succeeds
- C. Route the call through Amazon Bedrock cross-Region inference
- D. Store the model API key in an environment variable

### 8. A Regional outage stops the assistant, and supervisors would rather have shorter answers than none. What design meets that?

- A. Use one frontier model for every request
- B. Fall back to a second model when the first is unavailable
- C. Retry the failed call until it succeeds
- D. Raise the temperature for creative variants

### 9. Each product line needs its own tone and vocabulary, and the base model must stay shared. What training approach fits?

- A. Fine-tune with low-rank adaptation adapters
- B. Keep the prompt as a string constant in the application code
- C. Let each application call the model API directly
- D. Run a full fine-tune of every model weight

### 10. Sensor metadata arrives from three historians and sometimes lacks a line identifier or timestamp. What should reject the bad batch?

- A. Validate response structure and log the failures
- B. Enforce freshness and completeness rules with AWS Glue Data Quality
- C. Scan the data store with Amazon Macie
- D. Set an explicit CloudWatch Logs retention period

### 11. Engineers search by part number and asset tag, and those values must be exact. What should extraction add during ingestion?

- A. Extract entities with Amazon Comprehend before indexing
- B. Format the turns as an alternating conversation structure
- C. Normalise the text with a model call before indexing
- D. Concatenate all fields into one unlabelled text block

### 12. Technicians record spoken notes after each repair and want them searchable by symptom. What turns those recordings into text?

- A. Extract entities with Amazon Comprehend before indexing
- B. Extract the text from scanned pages with Amazon Textract
- C. Transcribe the call recordings with Amazon Transcribe
- D. Normalise the text with a model call before indexing

### 13. A developer gets a body validation error from the model endpoint while the prompt looks correct. What is missing?

- A. Format the turns as an alternating conversation structure
- B. Concatenate all fields into one unlabelled text block
- C. Keep the prompt as a string constant in the application code
- D. Send the request as the JSON body the model expects

### 14. A shift handover assistant must see who said what, in order, across several turns. How should the request be arranged?

- A. Cap the response length in the request
- B. Concatenate all fields into one unlabelled text block
- C. Raise the temperature for creative variants
- D. Format the turns as an alternating conversation structure

### 15. A reliability assistant must answer which procedures apply to a part that belongs to a machine on a specific line, following those relationships. Where should that structure live?

- A. Keep embeddings and metadata in Amazon DynamoDB
- B. Store the knowledge graph in Amazon Neptune
- C. Keep the source documents in Amazon DocumentDB
- D. Keep the source corpus in Amazon S3 and index references into it

### 16. One index serves five plants, and an answer for one plant must never quote another plant's procedure. What enforces that?

- A. Drop passages below a relevance score threshold
- B. Re-embed the corpus when the embedding model changes
- C. Raise the number of retrieved passages per query
- D. Filter the search by document metadata before the similarity ranking

### 17. Manuals are republished once a month and immediate indexing is not required. Which maintenance pattern fits?

- A. Trigger re-indexing from Amazon S3 event notifications
- B. Re-embed the corpus when the embedding model changes
- C. Cache every answer with no expiry
- D. Rebuild the index on a schedule and accept staleness between runs

### 18. Procedures are flat numbered steps with no headings, and the context budget requires uniform chunk sizes with overlap. Which split fits?

- A. Split documents into fixed-size token windows with overlap
- B. Increase the chunk size so every answer fits in one chunk
- C. Keep old vectors and embed new documents with the newer model
- D. Split by document structure into sections and subsections

### 19. Technicians search by asset tag as often as by fault description, and the best passage often ranks fifth. Which two changes address both? Select two.

- A. Combine keyword and vector retrieval and merge the ranked lists
- B. Raise the number of retrieved passages per query
- C. Drop passages below a relevance score threshold
- D. Rerank the retrieved passages with an Amazon Bedrock reranker
- E. Keep old vectors and embed new documents with the newer model

### 20. Technicians use trade slang while the manuals use formal terms, so correct passages never surface. What bridges that gap?

- A. Split where the embedding similarity between sentences drops
- B. Rerank the retrieved passages with an Amazon Bedrock reranker
- C. Raise the number of retrieved passages per query
- D. Expand the user query into related terms before retrieval

### 21. In a repair chat the follow-up is only what about the older model, and retrieval returns the current procedure. What should run first?

- A. Break a multi-part question into separate retrievals
- B. Fine-tune the embedding model on labelled query and passage pairs
- C. Rewrite the query using the conversation history first
- D. Raise the number of retrieved passages per query

### 22. A troubleshooting assistant jumps to a fix without listing the checks, and engineers cannot audit its reasoning. What should the instruction require?

- A. Keep the prompt as a string constant in the application code
- B. Cap the response length in the request
- C. Ask the model to reason step by step before answering
- D. Raise the temperature for creative variants

### 23. An inspection workflow runs five prompt steps with one branch on the inspection result. What runs that as a managed chain?

- A. Build the chain in Amazon Bedrock Prompt Flows
- B. Let each application call the model API directly
- C. Keep the prompt as a string constant in the application code
- D. Cache the stable prompt prefix with prompt caching

---

## Domain 2 — Implementation and Integration (26%) — Agents, deployment, enterprise integration, APIs, and developer tooling

### 24. A field-service agent must remember the machine serial and prior steps while an engineer walks the line. Where should that state live?

- A. Set an explicit CloudWatch Logs retention period
- B. Keep conversation and task memory in Amazon DynamoDB
- C. Keep memory only in the prompt of the current turn
- D. Cache every answer with no expiry

### 25. A maintenance session runs for two hours and resending every turn is expensive. What keeps the context small?

- A. Summarise the conversation before adding more turns
- B. Increase the chunk size so every answer fits in one chunk
- C. Concatenate all fields into one unlabelled text block
- D. Keep memory only in the prompt of the current turn

### 26. Welding, paint, and packaging each need their own tools, vocabulary, and escalation rules. How should the assistant be built?

- A. Give one agent every tool in the platform
- B. Keep the prompt as a string constant in the application code
- C. Return the whole answer from one synchronous call
- D. Give each domain its own agent with its own tools

### 27. An agent can stop a production line, and its reasoning loop must never run away. Which two controls are required? Select two.

- A. Require human approval before the agent performs the action
- B. Set an explicit step and budget limit on the agent loop
- C. Give one agent every tool in the platform
- D. Retry the failed call until it succeeds
- E. Raise the temperature for creative variants

### 28. The historian query hangs for minutes during shift change and freezes the agent turn. What contains that?

- A. Retry the failed call until it succeeds
- B. Keep a GPU endpoint running for occasional requests
- C. Set an explicit CloudWatch Logs retention period
- D. Bound each tool call with a timeout and a fallback

### 29. A tool runs a few hundred times a day, holds no state, and needs no custom runtime. How should it be implemented?

- A. Keep a GPU endpoint running for occasional requests
- B. Return the whole answer from one synchronous call
- C. Run the MCP server on Amazon ECS
- D. Implement the tool as an AWS Lambda function

### 30. Each plant uses the assistant in short bursts at shift change and never sustains load. What pricing model fits?

- A. Keep a GPU endpoint running for occasional requests
- B. Use one frontier model for every request
- C. Buy Amazon Bedrock provisioned throughput for the model
- D. Call the model on demand through Amazon Bedrock

### 31. A manufacturer has a custom defect-detection model plus a managed foundation model for explanations. Which two hosting choices fit each? Select two.

- A. Call the model on demand through Amazon Bedrock
- B. Return the whole answer from one synchronous call
- C. Retry the failed call until it succeeds
- D. Keep a GPU endpoint running for occasional requests
- E. Host the model on a SageMaker AI real-time endpoint

### 32. A tool server holds pooled database connections and must stay warm between requests. Where should it run?

- A. Implement the tool as an AWS Lambda function
- B. Return the whole answer from one synchronous call
- C. Keep a GPU endpoint running for occasional requests
- D. Run the MCP server on Amazon ECS

### 33. Twenty years of maintenance records sit on an on-premises file server and must move to Amazon S3 with verification. What should move them?

- A. Receive partner files over AWS Transfer Family
- B. Transfer the on-premises corpus with AWS DataSync
- C. Move SaaS records in with Amazon AppFlow
- D. Make the document bucket publicly readable

### 34. A plant service must assume temporary credentials for exactly one bucket prefix and one model, with nothing stored on disk. What should it use?

- A. Store the model API key in an environment variable
- B. Receive partner files over AWS Transfer Family
- C. Give the task an IAM role scoped to the resources it uses
- D. Make the document bucket publicly readable

### 35. Twelve plants call the model API with their own keys and nobody can see group-wide usage. What should the platform provide?

- A. Put one internal GenAI gateway in front of every model call
- B. Store the model API key in an environment variable
- C. Let each application call the model API directly
- D. Hardcode one model identifier in the application source

### 36. The same assistant must be deployed identically to twelve plants from one definition. Which two pieces deliver that? Select two.

- A. Release the assistant through AWS CodePipeline
- B. Store the model API key in an environment variable
- C. Keep the prompt as a string constant in the application code
- D. Define the resources in AWS CDK
- E. Let each application call the model API directly

### 37. A full-shift video summary takes several minutes to generate and the browser will not wait. What pattern fits?

- A. Queue the prompt and return a job identifier for polling
- B. Stream tokens as server-sent events
- C. Return the whole answer from one synchronous call
- D. Stream tokens over WebSockets through API Gateway

### 38. Clients are throttled during a ramp and their instant retries deepen the throttling. What retry policy should they adopt?

- A. Retry the failed call until it succeeds
- B. Retry throttled calls with exponential backoff and jitter
- C. Open a circuit breaker after repeated dependency failures
- D. Keep a GPU endpoint running for occasional requests

### 39. The maintenance system has failed every call for half an hour and requests keep waiting on it. What should open?

- A. Retry the failed call until it succeeds
- B. Retry throttled calls with exponential backoff and jitter
- C. Return the whole answer from one synchronous call
- D. Open a circuit breaker after repeated dependency failures

### 40. Supervisors need authenticated access to the maintenance assistant with per-site throttling and payload validation. What should sit in front of it?

- A. Serve repeatable responses from Amazon CloudFront
- B. Let each application call the model API directly
- C. Build the interface with AWS Amplify
- D. Front the model with Amazon API Gateway

### 41. A steady API runs all day in containers and the team does not want to manage nodes or a cluster. What fits?

- A. Run the service on AWS Fargate
- B. Build the interface with AWS Amplify
- C. Deploy the web service on AWS App Runner
- D. Run the workload on Amazon EKS

### 42. Engineers rewrite the same SDK plumbing for each new plant tool. What reduces that effort?

- A. Keep the prompt as a string constant in the application code
- B. Run the evaluation suite in AWS CodeBuild
- C. Generate and explain the integration code with Amazon Q Developer
- D. Release the assistant through AWS CodePipeline

### 43. A plant request takes twelve seconds, and the delay could be the historian, retrieval, or the model. What shows the hop?

- A. Trace the request across services with AWS X-Ray
- B. Record control-plane activity in AWS CloudTrail
- C. Set an explicit CloudWatch Logs retention period
- D. Query the prompt and response logs with CloudWatch Logs Insights

---

## Domain 3 — AI Safety, Security, and Governance (20%) — Safety controls, privacy, governance, and responsible AI

### 44. A shift assistant reads operator complaints and answers them, and neither side should carry abuse. What covers both?

- A. Cap the response length in the request
- B. Apply Amazon Bedrock Guardrails content filters
- C. Lower the temperature for factual answers
- D. Set an explicit CloudWatch Logs retention period

### 45. The assistant must refuse to discuss one product line under legal review and must prove an answer follows the lockout procedure. Which two guardrail features do that? Select two.

- A. Retry the failed call until it succeeds
- B. Add automated reasoning checks for policy statements
- C. Cap the response length in the request
- D. Cache every answer with no expiry
- E. Define denied topics in Amazon Bedrock Guardrails

### 46. Auditors must open the procedure clause behind every safety instruction the assistant gives. What should the answer carry?

- A. Require the answer to cite the retrieved passage
- B. Return a confidence score with each answer
- C. Cap the response length in the request
- D. Escalate low-confidence or high-impact answers to a person

### 47. An answer states a torque value the retrieved manual never contains. Which control catches that?

- A. Enable the contextual grounding check in Guardrails
- B. Constrain the response with a JSON schema
- C. Score answers by embedding similarity to the reference
- D. Lower the temperature for factual answers

### 48. A contractor pastes text telling the assistant to ignore the safety checklist. What detects that attempt?

- A. Screen inputs for instruction override and jailbreak patterns
- B. Cap the response length in the request
- C. Retry the failed call until it succeeds
- D. Lower the temperature for factual answers

### 49. A supplier manual contains the sentence disregard previous steps, and the assistant skips a check. What should have been done to the retrieved text?

- A. Fine-tune the embedding model on labelled query and passage pairs
- B. Constrain the response with a JSON schema
- C. Strip control text and delimiters from retrieved content
- D. Set an explicit CloudWatch Logs retention period

### 50. Operators type their badge numbers and personal phone numbers into the assistant, and those must not reach the model. What is the right control point?

- A. Scan the data store with Amazon Macie
- B. Mask personal data before the prompt is built
- C. Set an explicit CloudWatch Logs retention period
- D. Enable sensitive-information filters in Amazon Bedrock Guardrails

### 51. Before old incident reports are indexed, identifiers must be found and removed from the stored copy. Which two steps do that? Select two.

- A. Detect personal data with Amazon Comprehend
- B. Apply Amazon Bedrock Guardrails content filters
- C. Set an explicit CloudWatch Logs retention period
- D. Store the model API key in an environment variable
- E. Mask direct identifiers before the record is stored

### 52. Plant policy forbids the assistant calling the model over any public route. Which building block keeps that traffic private?

- A. Make the document bucket publicly readable
- B. Call the model through an interface VPC endpoint
- C. Serve repeatable responses from Amazon CloudFront
- D. Store the model API key in an environment variable

### 53. Which control keeps the maintenance corpus readable only from inside the VPC?

- A. Store the model API key in an environment variable
- B. Serve repeatable responses from Amazon CloudFront
- C. Call the model through an interface VPC endpoint
- D. Make the document bucket publicly readable

### 54. Audit logs must be kept for seven years and then deleted automatically to match the records policy. What implements that?

- A. Record control-plane activity in AWS CloudTrail
- B. Set an explicit CloudWatch Logs retention period
- C. Turn on Amazon Bedrock model invocation logging
- D. Publish a model card with the model version

### 55. A maintenance instruction is disputed and the plant must show the manual version and the exact prompt behind it. Which two records allow that? Select two.

- A. Cache every answer with no expiry
- B. Turn on Amazon Bedrock model invocation logging
- C. Store the model API key in an environment variable
- D. Lower the temperature for factual answers
- E. Record data lineage in the AWS Glue Data Catalog

### 56. The safety committee needs the intended use and known limits of a new fault-classification model. What documents that?

- A. Compare the candidates with an Amazon Bedrock model evaluation job
- B. Set an explicit CloudWatch Logs retention period
- C. Publish a model card with the model version
- D. Constrain the response with a JSON schema

### 57. A wrong answer from the assistant could stop a line unnecessarily. What should happen when confidence is low?

- A. Cache every answer with no expiry
- B. Cap the response length in the request
- C. Escalate low-confidence or high-impact answers to a person
- D. Raise the temperature for creative variants

### 58. Quality must be reported separately for each plant and shift pattern every quarter. What produces that view?

- A. Detect spend spikes with AWS Cost Anomaly Detection
- B. Alarm on p95 latency and error rate
- C. Report fairness metrics per user segment
- D. Alert when fairness metrics move beyond a band

---

## Domain 4 — Operational Efficiency and Optimization for GenAI Applications (12%) — Token cost, latency, throughput, and observability

### 59. A handover thread between shifts keeps every message, and the resend charge now dominates the bill. What should be dropped from it?

- A. Increase the chunk size so every answer fits in one chunk
- B. Prune older turns from the context window
- C. Raise the temperature for creative variants
- D. Raise the number of retrieved passages per query

### 60. Twelve passages are sent when two would answer the question, and each call is expensive. What should change?

- A. Raise the temperature for creative variants
- B. Retrieve fewer passages per answer
- C. Raise the number of retrieved passages per query
- D. Increase the chunk size so every answer fits in one chunk

### 61. The same fifty status questions are asked at every shift change. What removes most of that spend?

- A. Cache the response under a hash of the normalised request
- B. Keep a GPU endpoint running for occasional requests
- C. Cache every answer with no expiry
- D. Cache answers by embedding similarity to earlier questions

### 62. Every call resends a long safety preamble, and most questions only need a small model. Which two levers cut cost most? Select two.

- A. Cache the stable prompt prefix with prompt caching
- B. Cache every answer with no expiry
- C. Run a full fine-tune of every model weight
- D. Use one frontier model for every request
- E. Send routine prompts to a small model and hard prompts to a large one

### 63. Shift reports are requested at the same times every day and their inputs are known in advance. What removes them from the interactive path?

- A. Keep a GPU endpoint running for occasional requests
- B. Stream tokens as they are generated
- C. Return the whole answer from one synchronous call
- D. Precompute answers for predictable questions on a schedule

### 64. A ramp doubles traffic for two hours and operators must see text immediately. Which two practices address both needs? Select two.

- A. Run the work as an Amazon Bedrock batch inference job
- B. Use one frontier model for every request
- C. Plan capacity from measured tokens per minute
- D. Stream tokens as they are generated
- E. Retry the failed call until it succeeds

### 65. Operators complain that answers pause for seconds before appearing. What detects the slowdown before they do?

- A. Alarm on p95 latency and error rate
- B. Detect spend spikes with AWS Cost Anomaly Detection
- C. Set an explicit CloudWatch Logs retention period
- D. Publish a model card with the model version

### 66. Finance wants spend per plant and an alert when a plant's usage jumps unexpectedly. Which two capabilities provide that? Select two.

- A. Publish a model card with the model version
- B. Publish token usage as CloudWatch metrics
- C. Alarm on p95 latency and error rate
- D. Set an explicit CloudWatch Logs retention period
- E. Detect spend spikes with AWS Cost Anomaly Detection

### 67. Nobody can say which plant drove last quarter's model bill. What makes attribution possible?

- A. Detect spend spikes with AWS Cost Anomaly Detection
- B. Keep a GPU endpoint running for occasional requests
- C. Cover the steady compute with a Savings Plan
- D. Break down spend by application tag in AWS Cost Explorer

---

## Domain 5 — Testing, Validation, and Troubleshooting (11%) — Evaluation, validation, regression testing, and diagnosis

### 68. An instruction reads well but cites a lockout step that appears nowhere in the manual. Which metric exposes that?

- A. Score how directly the answer addresses the question
- B. Report BERTScore for semantic similarity to the reference
- C. Measure whether each claim is supported by the retrieved context
- D. Report ROUGE and BLEU against the reference answers

### 69. Twenty thousand answers a day need rubric scoring, and the result must survive an audit. Which two steps make that possible? Select two.

- A. Measure the judge model against expert labels first
- B. Raise the temperature for creative variants
- C. Score candidate answers with a judge model on a fixed rubric
- D. Measure whether the needed passage was retrieved at all
- E. Report ROUGE and BLEU against the reference answers

### 70. A new model must be compared on live plant traffic without any operator seeing it. What fits?

- A. Have reviewers score a sample against a written rubric
- B. Send a small traffic share to the new prompt and watch the metrics
- C. Mirror production traffic to the new version and compare offline
- D. Split traffic between two model versions and compare outcomes

### 71. A model refresh must not break the two hundred safety questions the plants already rely on. What should the release replay?

- A. Set an explicit CloudWatch Logs retention period
- B. Have reviewers score a sample against a written rubric
- C. Run the release against a curated golden question set
- D. Cache every answer with no expiry

### 72. A release must be blocked automatically when quality drops, and multi-step escalation paths must be exercised first. Which two practices deliver that? Select two.

- A. Retry the failed call until it succeeds
- B. Replay scripted user journeys against the new version
- C. Cache every answer with no expiry
- D. Raise the temperature for creative variants
- E. Block the release when evaluation drops below the threshold

### 73. A maintenance agent queries the wrong historian tag and returns another machine's readings. What isolates that failure?

- A. Measure whether the needed passage was retrieved at all
- B. Measure whether the agent called the right tool with the right arguments
- C. Measure the share of agent tasks completed end to end
- D. Report ROUGE and BLEU against the reference answers

### 74. A plant assistant sometimes misses the governing procedure and sometimes abandons a work order. Which two metrics separate those failures? Select two.

- A. Report BERTScore for semantic similarity to the reference
- B. Measure whether the needed passage was retrieved at all
- C. Measure the share of agent tasks completed end to end
- D. Measure whether the retrieved passages were relevant
- E. Report ROUGE and BLEU against the reference answers

### 75. A multi-step diagnosis returned a confident wrong fix and every service call succeeded. What should be inspected?

- A. Inspect the agent reasoning trace for the failed task
- B. Trace the request across services with AWS X-Ray
- C. Cache every answer with no expiry
- D. Log the token count and check for truncated prompts

---

## Answer key and explanations

### Question 1 — A, B

Answers: Put one internal GenAI gateway in front of every model call; Run the inference component on AWS Outposts. A shared gateway keeps one contract and Outposts puts the latency-critical part beside the machinery. A gateway centralises credentials, quotas, logging, and model routing for all teams. Outposts keeps compute and data on premises where residency or latency demands it. Local study-map skill 1.1 (GenAI Solution Architecture), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Correct. Outposts keeps compute and data on premises where residency or latency demands it. In this case: A shared gateway keeps one contract and Outposts puts the latency-critical part beside the machinery.
- **B:** Correct. A gateway centralises credentials, quotas, logging, and model routing for all teams. In this case: A shared gateway keeps one contract and Outposts puts the latency-critical part beside the machinery.
- **C:** Incorrect for this question. A hardcoded identifier forces a code change and a release to try another model. Why the correct answer wins: A shared gateway keeps one contract and Outposts puts the latency-critical part beside the machinery.
- **D:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: A shared gateway keeps one contract and Outposts puts the latency-critical part beside the machinery.
- **E:** Incorrect for this question. Direct calls from every app scatter keys, quotas, and logging across teams. Why the correct answer wins: A shared gateway keeps one contract and Outposts puts the latency-critical part beside the machinery.

### Question 2 — B, E

Answers: Version the prompt in Amazon Bedrock Prompt Management; Use an Amazon Bedrock knowledge base with a managed vector store. Versioned prompt templates keep instructions identical and a managed knowledge base holds each plant corpus. Prompt Management stores versions and variables so the same template serves every environment. A managed knowledge base handles ingestion, chunking, embedding and sync with little code. Local study-map skill 1.1 (GenAI Solution Architecture), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: Versioned prompt templates keep instructions identical and a managed knowledge base holds each plant corpus.
- **B:** Correct. Prompt Management stores versions and variables so the same template serves every environment. In this case: Versioned prompt templates keep instructions identical and a managed knowledge base holds each plant corpus.
- **C:** Incorrect for this question. Direct calls from every app scatter keys, quotas, and logging across teams. Why the correct answer wins: Versioned prompt templates keep instructions identical and a managed knowledge base holds each plant corpus.
- **D:** Incorrect for this question. A single blob loses the field boundaries the model needs to answer precisely. Why the correct answer wins: Versioned prompt templates keep instructions identical and a managed knowledge base holds each plant corpus.
- **E:** Correct. A managed knowledge base handles ingestion, chunking, embedding and sync with little code. In this case: Versioned prompt templates keep instructions identical and a managed knowledge base holds each plant corpus.

### Question 3 — D

Answer: Have reviewers score a sample against a written rubric. A rubric with human scores gives a reference the automatic metrics can be checked against. Local study-map skill 1.2 (Proof-of-Concept Validation), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. Overlap metrics are cheap and reward wording that matches the references. Why the correct answer wins: A rubric with human scores gives a reference the automatic metrics can be checked against.
- **B:** Incorrect for this question. A Bedrock evaluation job scores candidate models on your prompts and metrics before you choose. Why the correct answer wins: A rubric with human scores gives a reference the automatic metrics can be checked against.
- **C:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: A rubric with human scores gives a reference the automatic metrics can be checked against.
- **D:** Correct. In this case: A rubric with human scores gives a reference the automatic metrics can be checked against.

### Question 4 — B

Answer: Compare the candidates with an Amazon Bedrock model evaluation job. A Bedrock evaluation job scores every candidate on the same labelled prompts before a choice is made. A Bedrock evaluation job scores candidate models on your prompts and metrics before you choose. Local study-map skill 1.3 (Foundation Model Selection and Benchmarking), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: A Bedrock evaluation job scores every candidate on the same labelled prompts before a choice is made.
- **B:** Correct. A Bedrock evaluation job scores candidate models on your prompts and metrics before you choose. In this case: A Bedrock evaluation job scores every candidate on the same labelled prompts before a choice is made.
- **C:** Incorrect for this question. LoRA trains a small adapter instead of every weight, which cuts cost and keeps the base model reusable. Why the correct answer wins: A Bedrock evaluation job scores every candidate on the same labelled prompts before a choice is made.
- **D:** Incorrect for this question. A full fine-tune changes all weights, which is expensive and gives one model per task. Why the correct answer wins: A Bedrock evaluation job scores every candidate on the same labelled prompts before a choice is made.

### Question 5 — B

Answer: Right-size the model to the task difficulty. A model no larger than the task needs keeps the per-answer price low for a narrow, repetitive question. A model no larger than the task needs is the largest single cost lever. Local study-map skill 1.3 (Foundation Model Selection and Benchmarking), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. A cross-Region inference profile spreads traffic across Regions so a local capacity shortage is absorbed. Why the correct answer wins: A model no larger than the task needs keeps the per-answer price low for a narrow, repetitive question.
- **B:** Correct. A model no larger than the task needs is the largest single cost lever. In this case: A model no larger than the task needs keeps the per-answer price low for a narrow, repetitive question.
- **C:** Incorrect for this question. A full fine-tune changes all weights, which is expensive and gives one model per task. Why the correct answer wins: A model no larger than the task needs keeps the per-answer price low for a narrow, repetitive question.
- **D:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: A model no larger than the task needs keeps the per-answer price low for a narrow, repetitive question.

### Question 6 — C

Answer: Put the model identifier in AWS AppConfig and switch it without a deploy. A configuration flag changes the model identifier per request path without shipping new application code. Local study-map skill 1.4 (Model Routing and Provider Abstraction), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. A hardcoded identifier forces a code change and a release to try another model. Why the correct answer wins: A configuration flag changes the model identifier per request path without shipping new application code.
- **B:** Incorrect for this question. Direct calls from every app scatter keys, quotas, and logging across teams. Why the correct answer wins: A configuration flag changes the model identifier per request path without shipping new application code.
- **C:** Correct. In this case: A configuration flag changes the model identifier per request path without shipping new application code.
- **D:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: A configuration flag changes the model identifier per request path without shipping new application code.

### Question 7 — C

Answer: Route the call through Amazon Bedrock cross-Region inference. A cross-Region inference profile spreads traffic so a local capacity shortage does not fail the request. Local study-map skill 1.5 (Resilience and Cross-Region Inference), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: A cross-Region inference profile spreads traffic so a local capacity shortage does not fail the request.
- **B:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: A cross-Region inference profile spreads traffic so a local capacity shortage does not fail the request.
- **C:** Correct. In this case: A cross-Region inference profile spreads traffic so a local capacity shortage does not fail the request.
- **D:** Incorrect for this question. A key in an environment variable leaks through images, logs, and job definitions. Why the correct answer wins: A cross-Region inference profile spreads traffic so a local capacity shortage does not fail the request.

### Question 8 — B

Answer: Fall back to a second model when the first is unavailable. A fallback model keeps the feature answering during a Regional degradation, at a stated quality cost. A fallback keeps the feature available when one model or Region degrades. Local study-map skill 1.5 (Resilience and Cross-Region Inference), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: A fallback model keeps the feature answering during a Regional degradation, at a stated quality cost.
- **B:** Correct. A fallback keeps the feature available when one model or Region degrades. In this case: A fallback model keeps the feature answering during a Regional degradation, at a stated quality cost.
- **C:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: A fallback model keeps the feature answering during a Regional degradation, at a stated quality cost.
- **D:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: A fallback model keeps the feature answering during a Regional degradation, at a stated quality cost.

### Question 9 — A

Answer: Fine-tune with low-rank adaptation adapters. LoRA trains a small adapter instead of every weight, which cuts cost and keeps the base model reusable. Local study-map skill 1.6 (Customisation Lifecycle and Rollback), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Correct. In this case: LoRA trains a small adapter instead of every weight, which cuts cost and keeps the base model reusable.
- **B:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: LoRA trains a small adapter instead of every weight, which cuts cost and keeps the base model reusable.
- **C:** Incorrect for this question. Direct calls from every app scatter keys, quotas, and logging across teams. Why the correct answer wins: LoRA trains a small adapter instead of every weight, which cuts cost and keeps the base model reusable.
- **D:** Incorrect for this question. A full fine-tune changes all weights, which is expensive and gives one model per task. Why the correct answer wins: LoRA trains a small adapter instead of every weight, which cuts cost and keeps the base model reusable.

### Question 10 — B

Answer: Enforce freshness and completeness rules with AWS Glue Data Quality. Rule sets score freshness and completeness and stop the batch before anything is embedded. Local study-map skill 1.7 (Data Validation for Model Inputs), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. Structure failures appear in the logs before a downstream parser breaks. Why the correct answer wins: Rule sets score freshness and completeness and stop the batch before anything is embedded.
- **B:** Correct. In this case: Rule sets score freshness and completeness and stop the batch before anything is embedded.
- **C:** Incorrect for this question. Macie finds sensitive data at rest so the corpus can be cleaned before indexing. Why the correct answer wins: Rule sets score freshness and completeness and stop the batch before anything is embedded.
- **D:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: Rule sets score freshness and completeness and stop the batch before anything is embedded.

### Question 11 — A

Answer: Extract entities with Amazon Comprehend before indexing. Entity extraction puts product codes and names in metadata for exact filtering. Local study-map skill 1.7 (Data Validation for Model Inputs), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Correct. In this case: Entity extraction puts product codes and names in metadata for exact filtering.
- **B:** Incorrect for this question. A dialog-shaped request keeps speaker roles and prior turns in the order the model expects. Why the correct answer wins: Entity extraction puts product codes and names in metadata for exact filtering.
- **C:** Incorrect for this question. A reformatting pass cleans inconsistent headings and units before embedding. Why the correct answer wins: Entity extraction puts product codes and names in metadata for exact filtering.
- **D:** Incorrect for this question. A single blob loses the field boundaries the model needs to answer precisely. Why the correct answer wins: Entity extraction puts product codes and names in metadata for exact filtering.

### Question 12 — C

Answer: Transcribe the call recordings with Amazon Transcribe. Transcribe turns speech into timestamped text that retrieval can search. Local study-map skill 1.8 (Multimodal Ingestion and Processing), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. Entity extraction puts product codes and names in metadata for exact filtering. Why the correct answer wins: Transcribe turns speech into timestamped text that retrieval can search.
- **B:** Incorrect for this question. Textract returns text and form fields from an image so it can be indexed as text. Why the correct answer wins: Transcribe turns speech into timestamped text that retrieval can search.
- **C:** Correct. In this case: Transcribe turns speech into timestamped text that retrieval can search.
- **D:** Incorrect for this question. A reformatting pass cleans inconsistent headings and units before embedding. Why the correct answer wins: Transcribe turns speech into timestamped text that retrieval can search.

### Question 13 — D

Answer: Send the request as the JSON body the model expects. The model API expects the prompt, parameters, and model identifier in one JSON body. Local study-map skill 1.9 (Request Formatting and Enrichment), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. A dialog-shaped request keeps speaker roles and prior turns in the order the model expects. Why the correct answer wins: The model API expects the prompt, parameters, and model identifier in one JSON body.
- **B:** Incorrect for this question. A single blob loses the field boundaries the model needs to answer precisely. Why the correct answer wins: The model API expects the prompt, parameters, and model identifier in one JSON body.
- **C:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: The model API expects the prompt, parameters, and model identifier in one JSON body.
- **D:** Correct. In this case: The model API expects the prompt, parameters, and model identifier in one JSON body.

### Question 14 — D

Answer: Format the turns as an alternating conversation structure. A dialog-shaped request keeps speaker roles and prior turns in the order the model expects. Local study-map skill 1.9 (Request Formatting and Enrichment), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. A token cap bounds the cost of a runaway answer and the latency of every call. Why the correct answer wins: A dialog-shaped request keeps speaker roles and prior turns in the order the model expects.
- **B:** Incorrect for this question. A single blob loses the field boundaries the model needs to answer precisely. Why the correct answer wins: A dialog-shaped request keeps speaker roles and prior turns in the order the model expects.
- **C:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: A dialog-shaped request keeps speaker roles and prior turns in the order the model expects.
- **D:** Correct. In this case: A dialog-shaped request keeps speaker roles and prior turns in the order the model expects.

### Question 15 — B

Answer: Store the knowledge graph in Amazon Neptune. Neptune answers relationship traversals that a similarity search cannot express. Local study-map skill 1.10 (Vector Store Architecture), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. DynamoDB serves key lookups fast and can hold vectors beside their metadata for small corpora. Why the correct answer wins: Neptune answers relationship traversals that a similarity search cannot express.
- **B:** Correct. In this case: Neptune answers relationship traversals that a similarity search cannot express.
- **C:** Incorrect for this question. DocumentDB stores JSON documents in their original shape for retrieval and display. Why the correct answer wins: Neptune answers relationship traversals that a similarity search cannot express.
- **D:** Incorrect for this question. S3 holds the authoritative documents while the index stores only chunks and pointers. Why the correct answer wins: Neptune answers relationship traversals that a similarity search cannot express.

### Question 16 — D

Answer: Filter the search by document metadata before the similarity ranking. A metadata filter removes out-of-scope documents so the ranking only sees eligible chunks. Local study-map skill 1.11 (Metadata Frameworks and Index Maintenance), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. A threshold keeps marginal passages out of the prompt that would only add noise. Why the correct answer wins: A metadata filter removes out-of-scope documents so the ranking only sees eligible chunks.
- **B:** Incorrect for this question. Vectors from two different models are not comparable, so the whole index must be rebuilt. Why the correct answer wins: A metadata filter removes out-of-scope documents so the ranking only sees eligible chunks.
- **C:** Incorrect for this question. More passages raise recall and also lengthen the prompt and the cost per call. Why the correct answer wins: A metadata filter removes out-of-scope documents so the ranking only sees eligible chunks.
- **D:** Correct. In this case: A metadata filter removes out-of-scope documents so the ranking only sees eligible chunks.

### Question 17 — D

Answer: Rebuild the index on a schedule and accept staleness between runs. Scheduled rebuilds are simple and leave a window in which answers lag the source. Local study-map skill 1.11 (Metadata Frameworks and Index Maintenance), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. Event notifications start a sync as soon as a document lands or changes, which keeps lag to seconds. Why the correct answer wins: Scheduled rebuilds are simple and leave a window in which answers lag the source.
- **B:** Incorrect for this question. Vectors from two different models are not comparable, so the whole index must be rebuilt. Why the correct answer wins: Scheduled rebuilds are simple and leave a window in which answers lag the source.
- **C:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: Scheduled rebuilds are simple and leave a window in which answers lag the source.
- **D:** Correct. In this case: Scheduled rebuilds are simple and leave a window in which answers lag the source.

### Question 18 — A

Answer: Split documents into fixed-size token windows with overlap. Fixed windows are predictable and cheap, and overlap preserves text that straddles a boundary. Local study-map skill 1.12 (Chunking and Embedding Strategy), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Correct. In this case: Fixed windows are predictable and cheap, and overlap preserves text that straddles a boundary.
- **B:** Incorrect for this question. Larger chunks carry more context but dilute the embedding and crowd the prompt window. Why the correct answer wins: Fixed windows are predictable and cheap, and overlap preserves text that straddles a boundary.
- **C:** Incorrect for this question. Mixing vector spaces silently breaks similarity, because distances no longer mean the same thing. Why the correct answer wins: Fixed windows are predictable and cheap, and overlap preserves text that straddles a boundary.
- **D:** Incorrect for this question. Structural chunks follow headings, so a retrieved chunk carries a coherent argument. Why the correct answer wins: Fixed windows are predictable and cheap, and overlap preserves text that straddles a boundary.

### Question 19 — A, D

Answers: Combine keyword and vector retrieval and merge the ranked lists; Rerank the retrieved passages with an Amazon Bedrock reranker. Hybrid retrieval catches the exact identifier and a reranker fixes the order of the shortlist. Hybrid retrieval catches exact identifiers that a vector search alone can miss. A reranker scores the shortlist against the query and lifts precision before the prompt is built. Local study-map skill 1.13 (Hybrid Retrieval and Reranking), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Correct. Hybrid retrieval catches exact identifiers that a vector search alone can miss. In this case: Hybrid retrieval catches the exact identifier and a reranker fixes the order of the shortlist.
- **B:** Incorrect for this question. More passages raise recall and also lengthen the prompt and the cost per call. Why the correct answer wins: Hybrid retrieval catches the exact identifier and a reranker fixes the order of the shortlist.
- **C:** Incorrect for this question. A threshold keeps marginal passages out of the prompt that would only add noise. Why the correct answer wins: Hybrid retrieval catches the exact identifier and a reranker fixes the order of the shortlist.
- **D:** Correct. A reranker scores the shortlist against the query and lifts precision before the prompt is built. In this case: Hybrid retrieval catches the exact identifier and a reranker fixes the order of the shortlist.
- **E:** Incorrect for this question. Mixing vector spaces silently breaks similarity, because distances no longer mean the same thing. Why the correct answer wins: Hybrid retrieval catches the exact identifier and a reranker fixes the order of the shortlist.

### Question 20 — D

Answer: Expand the user query into related terms before retrieval. Expansion bridges vocabulary gaps between how users ask and how documents are written. Local study-map skill 1.13 (Hybrid Retrieval and Reranking), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. Semantic splitting places boundaries at topic shifts rather than at a character count. Why the correct answer wins: Expansion bridges vocabulary gaps between how users ask and how documents are written.
- **B:** Incorrect for this question. A reranker scores the shortlist against the query and lifts precision before the prompt is built. Why the correct answer wins: Expansion bridges vocabulary gaps between how users ask and how documents are written.
- **C:** Incorrect for this question. More passages raise recall and also lengthen the prompt and the cost per call. Why the correct answer wins: Expansion bridges vocabulary gaps between how users ask and how documents are written.
- **D:** Correct. In this case: Expansion bridges vocabulary gaps between how users ask and how documents are written.

### Question 21 — C

Answer: Rewrite the query using the conversation history first. History-aware rewriting turns a follow-up such as and the second one into a standalone query. Local study-map skill 1.14 (Query Transformation and Handling), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. Decomposition retrieves evidence for each sub-question instead of averaging them into one query. Why the correct answer wins: History-aware rewriting turns a follow-up such as and the second one into a standalone query.
- **B:** Incorrect for this question. Domain-tuned embeddings move relevant passages closer for vocabulary the base model misses. Why the correct answer wins: History-aware rewriting turns a follow-up such as and the second one into a standalone query.
- **C:** Correct. In this case: History-aware rewriting turns a follow-up such as and the second one into a standalone query.
- **D:** Incorrect for this question. More passages raise recall and also lengthen the prompt and the cost per call. Why the correct answer wins: History-aware rewriting turns a follow-up such as and the second one into a standalone query.

### Question 22 — C

Answer: Ask the model to reason step by step before answering. Explicit steps improve multi-step reasoning and expose where an answer went wrong. Local study-map skill 1.15 (Prompt Engineering and Governance), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: Explicit steps improve multi-step reasoning and expose where an answer went wrong.
- **B:** Incorrect for this question. A token cap bounds the cost of a runaway answer and the latency of every call. Why the correct answer wins: Explicit steps improve multi-step reasoning and expose where an answer went wrong.
- **C:** Correct. In this case: Explicit steps improve multi-step reasoning and expose where an answer went wrong.
- **D:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: Explicit steps improve multi-step reasoning and expose where an answer went wrong.

### Question 23 — A

Answer: Build the chain in Amazon Bedrock Prompt Flows. Prompt Flows runs sequential and branching prompt steps as one managed workflow. Local study-map skill 1.15 (Prompt Engineering and Governance), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 1 (foundation model integration, data management, and compliance, 31 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain1.html.

- **A:** Correct. In this case: Prompt Flows runs sequential and branching prompt steps as one managed workflow.
- **B:** Incorrect for this question. Direct calls from every app scatter keys, quotas, and logging across teams. Why the correct answer wins: Prompt Flows runs sequential and branching prompt steps as one managed workflow.
- **C:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: Prompt Flows runs sequential and branching prompt steps as one managed workflow.
- **D:** Incorrect for this question. Prompt caching reuses processed prefix tokens, which cuts latency and input cost on repeat calls. Why the correct answer wins: Prompt Flows runs sequential and branching prompt steps as one managed workflow.

### Question 24 — B

Answer: Keep conversation and task memory in Amazon DynamoDB. DynamoDB gives the agent a durable per-session store keyed by session identifier. Local study-map skill 2.1 (Agent Memory and State), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: DynamoDB gives the agent a durable per-session store keyed by session identifier.
- **B:** Correct. In this case: DynamoDB gives the agent a durable per-session store keyed by session identifier.
- **C:** Incorrect for this question. Prompt-only memory forgets everything the moment the context window is trimmed. Why the correct answer wins: DynamoDB gives the agent a durable per-session store keyed by session identifier.
- **D:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: DynamoDB gives the agent a durable per-session store keyed by session identifier.

### Question 25 — A

Answer: Summarise the conversation before adding more turns. A running summary keeps long sessions inside the window at low token cost. Local study-map skill 2.1 (Agent Memory and State), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Correct. In this case: A running summary keeps long sessions inside the window at low token cost.
- **B:** Incorrect for this question. Larger chunks carry more context but dilute the embedding and crowd the prompt window. Why the correct answer wins: A running summary keeps long sessions inside the window at low token cost.
- **C:** Incorrect for this question. A single blob loses the field boundaries the model needs to answer precisely. Why the correct answer wins: A running summary keeps long sessions inside the window at low token cost.
- **D:** Incorrect for this question. Prompt-only memory forgets everything the moment the context window is trimmed. Why the correct answer wins: A running summary keeps long sessions inside the window at low token cost.

### Question 26 — D

Answer: Give each domain its own agent with its own tools. Specialist agents keep tool sets small and prompts focused on one domain. Local study-map skill 2.2 (Agent Orchestration Patterns), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. One agent with every tool makes tool choice ambiguous and permissions broad. Why the correct answer wins: Specialist agents keep tool sets small and prompts focused on one domain.
- **B:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: Specialist agents keep tool sets small and prompts focused on one domain.
- **C:** Incorrect for this question. A synchronous call is simplest and makes the user wait for the final token. Why the correct answer wins: Specialist agents keep tool sets small and prompts focused on one domain.
- **D:** Correct. In this case: Specialist agents keep tool sets small and prompts focused on one domain.

### Question 27 — A, B

Answers: Require human approval before the agent performs the action; Set an explicit step and budget limit on the agent loop. An approval gate keeps an irreversible side effect with a person and a hard limit ends a runaway loop. An approval gate keeps an irreversible side effect under human control. A hard limit stops a loop that would otherwise consume tokens without converging. Local study-map skill 2.2 (Agent Orchestration Patterns), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Correct. An approval gate keeps an irreversible side effect under human control. In this case: An approval gate keeps an irreversible side effect with a person and a hard limit ends a runaway loop.
- **B:** Correct. A hard limit stops a loop that would otherwise consume tokens without converging. In this case: An approval gate keeps an irreversible side effect with a person and a hard limit ends a runaway loop.
- **C:** Incorrect for this question. One agent with every tool makes tool choice ambiguous and permissions broad. Why the correct answer wins: An approval gate keeps an irreversible side effect with a person and a hard limit ends a runaway loop.
- **D:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: An approval gate keeps an irreversible side effect with a person and a hard limit ends a runaway loop.
- **E:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: An approval gate keeps an irreversible side effect with a person and a hard limit ends a runaway loop.

### Question 28 — D

Answer: Bound each tool call with a timeout and a fallback. A timeout keeps one slow dependency from stalling the whole agent turn. Local study-map skill 2.3 (Tool Reliability and Safeguards), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: A timeout keeps one slow dependency from stalling the whole agent turn.
- **B:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: A timeout keeps one slow dependency from stalling the whole agent turn.
- **C:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: A timeout keeps one slow dependency from stalling the whole agent turn.
- **D:** Correct. In this case: A timeout keeps one slow dependency from stalling the whole agent turn.

### Question 29 — D

Answer: Implement the tool as an AWS Lambda function. A Lambda tool is stateless, cheap at low volume, and scales per request. Local study-map skill 2.3 (Tool Reliability and Safeguards), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: A Lambda tool is stateless, cheap at low volume, and scales per request.
- **B:** Incorrect for this question. A synchronous call is simplest and makes the user wait for the final token. Why the correct answer wins: A Lambda tool is stateless, cheap at low volume, and scales per request.
- **C:** Incorrect for this question. A container gives a long-lived tool server dependencies and connection pooling. Why the correct answer wins: A Lambda tool is stateless, cheap at low volume, and scales per request.
- **D:** Correct. In this case: A Lambda tool is stateless, cheap at low volume, and scales per request.

### Question 30 — D

Answer: Call the model on demand through Amazon Bedrock. On-demand Bedrock inference bills per token with no committed capacity, which suits spiky or unproven demand. Local study-map skill 2.4 (Foundation Model Deployment and Capacity), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: On-demand Bedrock inference bills per token with no committed capacity, which suits spiky or unproven demand.
- **B:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: On-demand Bedrock inference bills per token with no committed capacity, which suits spiky or unproven demand.
- **C:** Incorrect for this question. Provisioned throughput reserves model units and gives a predictable token-per-minute ceiling. Why the correct answer wins: On-demand Bedrock inference bills per token with no committed capacity, which suits spiky or unproven demand.
- **D:** Correct. In this case: On-demand Bedrock inference bills per token with no committed capacity, which suits spiky or unproven demand.

### Question 31 — A, E

Answers: Host the model on a SageMaker AI real-time endpoint; Call the model on demand through Amazon Bedrock. A SageMaker AI endpoint hosts the custom container and on-demand Bedrock serves the managed model. A SageMaker AI endpoint gives full control over the container, instance and scaling policy. On-demand Bedrock inference bills per token with no committed capacity, which suits spiky or unproven demand. Local study-map skill 2.4 (Foundation Model Deployment and Capacity), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Correct. On-demand Bedrock inference bills per token with no committed capacity, which suits spiky or unproven demand. In this case: A SageMaker AI endpoint hosts the custom container and on-demand Bedrock serves the managed model.
- **B:** Incorrect for this question. A synchronous call is simplest and makes the user wait for the final token. Why the correct answer wins: A SageMaker AI endpoint hosts the custom container and on-demand Bedrock serves the managed model.
- **C:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: A SageMaker AI endpoint hosts the custom container and on-demand Bedrock serves the managed model.
- **D:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: A SageMaker AI endpoint hosts the custom container and on-demand Bedrock serves the managed model.
- **E:** Correct. A SageMaker AI endpoint gives full control over the container, instance and scaling policy. In this case: A SageMaker AI endpoint hosts the custom container and on-demand Bedrock serves the managed model.

### Question 32 — D

Answer: Run the MCP server on Amazon ECS. A container gives a long-lived tool server dependencies and connection pooling. Local study-map skill 2.5 (Enterprise Integration Patterns), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. A Lambda tool is stateless, cheap at low volume, and scales per request. Why the correct answer wins: A container gives a long-lived tool server dependencies and connection pooling.
- **B:** Incorrect for this question. A synchronous call is simplest and makes the user wait for the final token. Why the correct answer wins: A container gives a long-lived tool server dependencies and connection pooling.
- **C:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: A container gives a long-lived tool server dependencies and connection pooling.
- **D:** Correct. In this case: A container gives a long-lived tool server dependencies and connection pooling.

### Question 33 — B

Answer: Transfer the on-premises corpus with AWS DataSync. DataSync moves large file sets with verification and incremental transfer. Local study-map skill 2.5 (Enterprise Integration Patterns), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. Transfer Family accepts SFTP uploads into S3 without a server to run. Why the correct answer wins: DataSync moves large file sets with verification and incremental transfer.
- **B:** Correct. In this case: DataSync moves large file sets with verification and incremental transfer.
- **C:** Incorrect for this question. AppFlow copies data from supported SaaS sources without custom connectors. Why the correct answer wins: DataSync moves large file sets with verification and incremental transfer.
- **D:** Incorrect for this question. A public bucket exposes the corpus to everyone the index was meant to constrain. Why the correct answer wins: DataSync moves large file sets with verification and incremental transfer.

### Question 34 — C

Answer: Give the task an IAM role scoped to the resources it uses. A scoped role issues temporary credentials with only the needed permissions. Local study-map skill 2.6 (Identity for Model Access), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. A key in an environment variable leaks through images, logs, and job definitions. Why the correct answer wins: A scoped role issues temporary credentials with only the needed permissions.
- **B:** Incorrect for this question. Transfer Family accepts SFTP uploads into S3 without a server to run. Why the correct answer wins: A scoped role issues temporary credentials with only the needed permissions.
- **C:** Correct. In this case: A scoped role issues temporary credentials with only the needed permissions.
- **D:** Incorrect for this question. A public bucket exposes the corpus to everyone the index was meant to constrain. Why the correct answer wins: A scoped role issues temporary credentials with only the needed permissions.

### Question 35 — A

Answer: Put one internal GenAI gateway in front of every model call. A gateway centralises credentials, quotas, logging, and model routing for all teams. Local study-map skill 2.7 (CI/CD and GenAI Gateway), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Correct. In this case: A gateway centralises credentials, quotas, logging, and model routing for all teams.
- **B:** Incorrect for this question. A key in an environment variable leaks through images, logs, and job definitions. Why the correct answer wins: A gateway centralises credentials, quotas, logging, and model routing for all teams.
- **C:** Incorrect for this question. Direct calls from every app scatter keys, quotas, and logging across teams. Why the correct answer wins: A gateway centralises credentials, quotas, logging, and model routing for all teams.
- **D:** Incorrect for this question. A hardcoded identifier forces a code change and a release to try another model. Why the correct answer wins: A gateway centralises credentials, quotas, logging, and model routing for all teams.

### Question 36 — A, D

Answers: Define the resources in AWS CDK; Release the assistant through AWS CodePipeline. A CDK stack makes each environment reproducible and a pipeline releases the same artefact to all. CDK expresses the stack as code so environments are reproducible. A pipeline ties source, build, test, and deploy into one auditable flow. Local study-map skill 2.7 (CI/CD and GenAI Gateway), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Correct. A pipeline ties source, build, test, and deploy into one auditable flow. In this case: A CDK stack makes each environment reproducible and a pipeline releases the same artefact to all.
- **B:** Incorrect for this question. A key in an environment variable leaks through images, logs, and job definitions. Why the correct answer wins: A CDK stack makes each environment reproducible and a pipeline releases the same artefact to all.
- **C:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: A CDK stack makes each environment reproducible and a pipeline releases the same artefact to all.
- **D:** Correct. CDK expresses the stack as code so environments are reproducible. In this case: A CDK stack makes each environment reproducible and a pipeline releases the same artefact to all.
- **E:** Incorrect for this question. Direct calls from every app scatter keys, quotas, and logging across teams. Why the correct answer wins: A CDK stack makes each environment reproducible and a pipeline releases the same artefact to all.

### Question 37 — A

Answer: Queue the prompt and return a job identifier for polling. Asynchronous processing suits long generations that outlast an API timeout. Local study-map skill 2.8 (Streaming and Asynchronous APIs), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Correct. In this case: Asynchronous processing suits long generations that outlast an API timeout.
- **B:** Incorrect for this question. Server-sent events deliver incremental text over ordinary HTTP. Why the correct answer wins: Asynchronous processing suits long generations that outlast an API timeout.
- **C:** Incorrect for this question. A synchronous call is simplest and makes the user wait for the final token. Why the correct answer wins: Asynchronous processing suits long generations that outlast an API timeout.
- **D:** Incorrect for this question. A WebSocket keeps one connection open for incremental tokens. Why the correct answer wins: Asynchronous processing suits long generations that outlast an API timeout.

### Question 38 — B

Answer: Retry throttled calls with exponential backoff and jitter. Backoff with jitter spreads retries so a throttled client does not stampede the service. Local study-map skill 2.9 (API Resilience and Backoff), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: Backoff with jitter spreads retries so a throttled client does not stampede the service.
- **B:** Correct. In this case: Backoff with jitter spreads retries so a throttled client does not stampede the service.
- **C:** Incorrect for this question. A circuit breaker stops sending traffic to a dependency that is already failing. Why the correct answer wins: Backoff with jitter spreads retries so a throttled client does not stampede the service.
- **D:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: Backoff with jitter spreads retries so a throttled client does not stampede the service.

### Question 39 — D

Answer: Open a circuit breaker after repeated dependency failures. A circuit breaker stops sending traffic to a dependency that is already failing. Local study-map skill 2.9 (API Resilience and Backoff), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: A circuit breaker stops sending traffic to a dependency that is already failing.
- **B:** Incorrect for this question. Backoff with jitter spreads retries so a throttled client does not stampede the service. Why the correct answer wins: A circuit breaker stops sending traffic to a dependency that is already failing.
- **C:** Incorrect for this question. A synchronous call is simplest and makes the user wait for the final token. Why the correct answer wins: A circuit breaker stops sending traffic to a dependency that is already failing.
- **D:** Correct. In this case: A circuit breaker stops sending traffic to a dependency that is already failing.

### Question 40 — D

Answer: Front the model with Amazon API Gateway. API Gateway adds authentication, throttling, request validation, and streaming to the model call. Local study-map skill 2.10 (Application Integration and Low Code), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. An edge cache answers identical requests without reaching the model. Why the correct answer wins: API Gateway adds authentication, throttling, request validation, and streaming to the model call.
- **B:** Incorrect for this question. Direct calls from every app scatter keys, quotas, and logging across teams. Why the correct answer wins: API Gateway adds authentication, throttling, request validation, and streaming to the model call.
- **C:** Incorrect for this question. Amplify supplies declarative UI and hosting for the client that talks to the assistant. Why the correct answer wins: API Gateway adds authentication, throttling, request validation, and streaming to the model call.
- **D:** Correct. In this case: API Gateway adds authentication, throttling, request validation, and streaming to the model call.

### Question 41 — A

Answer: Run the service on AWS Fargate. Fargate runs containers without managing instances and suits steady API traffic. Local study-map skill 2.10 (Application Integration and Low Code), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Correct. In this case: Fargate runs containers without managing instances and suits steady API traffic.
- **B:** Incorrect for this question. Amplify supplies declarative UI and hosting for the client that talks to the assistant. Why the correct answer wins: Fargate runs containers without managing instances and suits steady API traffic.
- **C:** Incorrect for this question. App Runner builds and runs a container from source with managed scaling. Why the correct answer wins: Fargate runs containers without managing instances and suits steady API traffic.
- **D:** Incorrect for this question. EKS suits teams already operating Kubernetes with GPU and custom networking needs. Why the correct answer wins: Fargate runs containers without managing instances and suits steady API traffic.

### Question 42 — C

Answer: Generate and explain the integration code with Amazon Q Developer. Q Developer drafts and explains SDK calls inside the editor, which speeds up the plumbing. Local study-map skill 2.11 (Developer Productivity Tooling), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Incorrect for this question. A prompt in code needs a deployment for every wording change and leaves no version history. Why the correct answer wins: Q Developer drafts and explains SDK calls inside the editor, which speeds up the plumbing.
- **B:** Incorrect for this question. CodeBuild runs the tests and quality gates as part of the release. Why the correct answer wins: Q Developer drafts and explains SDK calls inside the editor, which speeds up the plumbing.
- **C:** Correct. In this case: Q Developer drafts and explains SDK calls inside the editor, which speeds up the plumbing.
- **D:** Incorrect for this question. A pipeline ties source, build, test, and deploy into one auditable flow. Why the correct answer wins: Q Developer drafts and explains SDK calls inside the editor, which speeds up the plumbing.

### Question 43 — A

Answer: Trace the request across services with AWS X-Ray. A trace shows which hop in the chain added the latency. Local study-map skill 2.12 (Integration Troubleshooting), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 2 (implementation and integration, 26 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain2.html.

- **A:** Correct. In this case: A trace shows which hop in the chain added the latency.
- **B:** Incorrect for this question. CloudTrail records who changed models, keys, and guardrails. Why the correct answer wins: A trace shows which hop in the chain added the latency.
- **C:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: A trace shows which hop in the chain added the latency.
- **D:** Incorrect for this question. Logs Insights correlates a spike in errors with the prompts that caused it. Why the correct answer wins: A trace shows which hop in the chain added the latency.

### Question 44 — B

Answer: Apply Amazon Bedrock Guardrails content filters. Content filters score and block harmful input and output on the request path. Local study-map skill 3.1 (Content Safety Controls), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. A token cap bounds the cost of a runaway answer and the latency of every call. Why the correct answer wins: Content filters score and block harmful input and output on the request path.
- **B:** Correct. In this case: Content filters score and block harmful input and output on the request path.
- **C:** Incorrect for this question. Low temperature narrows sampling so repeatable factual answers stay stable. Why the correct answer wins: Content filters score and block harmful input and output on the request path.
- **D:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: Content filters score and block harmful input and output on the request path.

### Question 45 — B, E

Answers: Define denied topics in Amazon Bedrock Guardrails; Add automated reasoning checks for policy statements. Denied topics refuse the ruled-out subject and reasoning checks verify a response against encoded policy rules. Denied topics refuse the subject areas the business has ruled out. Reasoning checks verify a response against encoded policy rules rather than a similarity score. Local study-map skill 3.1 (Content Safety Controls), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: Denied topics refuse the ruled-out subject and reasoning checks verify a response against encoded policy rules.
- **B:** Correct. Reasoning checks verify a response against encoded policy rules rather than a similarity score. In this case: Denied topics refuse the ruled-out subject and reasoning checks verify a response against encoded policy rules.
- **C:** Incorrect for this question. A token cap bounds the cost of a runaway answer and the latency of every call. Why the correct answer wins: Denied topics refuse the ruled-out subject and reasoning checks verify a response against encoded policy rules.
- **D:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: Denied topics refuse the ruled-out subject and reasoning checks verify a response against encoded policy rules.
- **E:** Correct. Denied topics refuse the subject areas the business has ruled out. In this case: Denied topics refuse the ruled-out subject and reasoning checks verify a response against encoded policy rules.

### Question 46 — A

Answer: Require the answer to cite the retrieved passage. A citation makes each claim traceable to a source the reader can check. Local study-map skill 3.2 (Grounding and Hallucination Reduction), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Correct. In this case: A citation makes each claim traceable to a source the reader can check.
- **B:** Incorrect for this question. A score lets the interface route low-confidence answers to a human. Why the correct answer wins: A citation makes each claim traceable to a source the reader can check.
- **C:** Incorrect for this question. A token cap bounds the cost of a runaway answer and the latency of every call. Why the correct answer wins: A citation makes each claim traceable to a source the reader can check.
- **D:** Incorrect for this question. An escalation path keeps consequential answers with a human owner. Why the correct answer wins: A citation makes each claim traceable to a source the reader can check.

### Question 47 — A

Answer: Enable the contextual grounding check in Guardrails. The grounding check compares the response with the retrieved source and flags unsupported claims. Local study-map skill 3.2 (Grounding and Hallucination Reduction), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Correct. In this case: The grounding check compares the response with the retrieved source and flags unsupported claims.
- **B:** Incorrect for this question. A schema makes the output machine-parseable and rejects prose that breaks the contract. Why the correct answer wins: The grounding check compares the response with the retrieved source and flags unsupported claims.
- **C:** Incorrect for this question. Similarity scoring is fast and tolerant of wording, but blind to a contradicted fact. Why the correct answer wins: The grounding check compares the response with the retrieved source and flags unsupported claims.
- **D:** Incorrect for this question. Low temperature narrows sampling so repeatable factual answers stay stable. Why the correct answer wins: The grounding check compares the response with the retrieved source and flags unsupported claims.

### Question 48 — A

Answer: Screen inputs for instruction override and jailbreak patterns. A pre-filter catches text that tries to replace the system instruction. Local study-map skill 3.3 (Prompt Injection Defence), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Correct. In this case: A pre-filter catches text that tries to replace the system instruction.
- **B:** Incorrect for this question. A token cap bounds the cost of a runaway answer and the latency of every call. Why the correct answer wins: A pre-filter catches text that tries to replace the system instruction.
- **C:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: A pre-filter catches text that tries to replace the system instruction.
- **D:** Incorrect for this question. Low temperature narrows sampling so repeatable factual answers stay stable. Why the correct answer wins: A pre-filter catches text that tries to replace the system instruction.

### Question 49 — C

Answer: Strip control text and delimiters from retrieved content. Sanitising retrieved text stops it from being parsed as an instruction. Local study-map skill 3.3 (Prompt Injection Defence), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. Domain-tuned embeddings move relevant passages closer for vocabulary the base model misses. Why the correct answer wins: Sanitising retrieved text stops it from being parsed as an instruction.
- **B:** Incorrect for this question. A schema makes the output machine-parseable and rejects prose that breaks the contract. Why the correct answer wins: Sanitising retrieved text stops it from being parsed as an instruction.
- **C:** Correct. In this case: Sanitising retrieved text stops it from being parsed as an instruction.
- **D:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: Sanitising retrieved text stops it from being parsed as an instruction.

### Question 50 — B

Answer: Mask personal data before the prompt is built. Masking at the boundary keeps personal data out of the model request entirely. Local study-map skill 3.4 (Privacy and PII Protection), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. Macie finds sensitive data at rest so the corpus can be cleaned before indexing. Why the correct answer wins: Masking at the boundary keeps personal data out of the model request entirely.
- **B:** Correct. In this case: Masking at the boundary keeps personal data out of the model request entirely.
- **C:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: Masking at the boundary keeps personal data out of the model request entirely.
- **D:** Incorrect for this question. PII filters detect and mask personal data in prompts and responses. Why the correct answer wins: Masking at the boundary keeps personal data out of the model request entirely.

### Question 51 — A, E

Answers: Detect personal data with Amazon Comprehend; Mask direct identifiers before the record is stored. Comprehend identifies the entities and masking removes them while keeping the record usable. Comprehend identifies entities and PII so they can be masked before the model sees them. Masking removes names and account numbers while keeping the record usable. Local study-map skill 3.4 (Privacy and PII Protection), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Correct. Comprehend identifies entities and PII so they can be masked before the model sees them. In this case: Comprehend identifies the entities and masking removes them while keeping the record usable.
- **B:** Incorrect for this question. Content filters score and block harmful input and output on the request path. Why the correct answer wins: Comprehend identifies the entities and masking removes them while keeping the record usable.
- **C:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: Comprehend identifies the entities and masking removes them while keeping the record usable.
- **D:** Incorrect for this question. A key in an environment variable leaks through images, logs, and job definitions. Why the correct answer wins: Comprehend identifies the entities and masking removes them while keeping the record usable.
- **E:** Correct. Masking removes names and account numbers while keeping the record usable. In this case: Comprehend identifies the entities and masking removes them while keeping the record usable.

### Question 52 — B

Answer: Call the model through an interface VPC endpoint. A private endpoint keeps model traffic off the public internet. Local study-map skill 3.5 (Network and Data Isolation), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. A public bucket exposes the corpus to everyone the index was meant to constrain. Why the correct answer wins: A private endpoint keeps model traffic off the public internet.
- **B:** Correct. In this case: A private endpoint keeps model traffic off the public internet.
- **C:** Incorrect for this question. An edge cache answers identical requests without reaching the model. Why the correct answer wins: A private endpoint keeps model traffic off the public internet.
- **D:** Incorrect for this question. A key in an environment variable leaks through images, logs, and job definitions. Why the correct answer wins: A private endpoint keeps model traffic off the public internet.

### Question 53 — C

Answer: Call the model through an interface VPC endpoint. Private subnets remove inbound internet routing from the compute tier. A private endpoint keeps model traffic off the public internet. Local study-map skill 3.5 (Network and Data Isolation), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. A key in an environment variable leaks through images, logs, and job definitions. Why the correct answer wins: Private subnets remove inbound internet routing from the compute tier.
- **B:** Incorrect for this question. An edge cache answers identical requests without reaching the model. Why the correct answer wins: Private subnets remove inbound internet routing from the compute tier.
- **C:** Correct. A private endpoint keeps model traffic off the public internet. In this case: Private subnets remove inbound internet routing from the compute tier.
- **D:** Incorrect for this question. A public bucket exposes the corpus to everyone the index was meant to constrain. Why the correct answer wins: Private subnets remove inbound internet routing from the compute tier.

### Question 54 — B

Answer: Set an explicit CloudWatch Logs retention period. A retention period bounds storage cost and matches the data policy. Local study-map skill 3.6 (Governance, Lineage, and Audit), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. CloudTrail records who changed models, keys, and guardrails. Why the correct answer wins: A retention period bounds storage cost and matches the data policy.
- **B:** Correct. In this case: A retention period bounds storage cost and matches the data policy.
- **C:** Incorrect for this question. Invocation logs capture the request, the response, and the token counts. Why the correct answer wins: A retention period bounds storage cost and matches the data policy.
- **D:** Incorrect for this question. A model card documents intended use and known limits for reviewers. Why the correct answer wins: A retention period bounds storage cost and matches the data policy.

### Question 55 — B, E

Answers: Record data lineage in the AWS Glue Data Catalog; Turn on Amazon Bedrock model invocation logging. Lineage ties the answer to its corpus version and invocation logs hold the request and the response. Lineage shows which corpus and version produced an answer. Invocation logs capture the request, the response, and the token counts. Local study-map skill 3.6 (Governance, Lineage, and Audit), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: Lineage ties the answer to its corpus version and invocation logs hold the request and the response.
- **B:** Correct. Invocation logs capture the request, the response, and the token counts. In this case: Lineage ties the answer to its corpus version and invocation logs hold the request and the response.
- **C:** Incorrect for this question. A key in an environment variable leaks through images, logs, and job definitions. Why the correct answer wins: Lineage ties the answer to its corpus version and invocation logs hold the request and the response.
- **D:** Incorrect for this question. Low temperature narrows sampling so repeatable factual answers stay stable. Why the correct answer wins: Lineage ties the answer to its corpus version and invocation logs hold the request and the response.
- **E:** Correct. Lineage shows which corpus and version produced an answer. In this case: Lineage ties the answer to its corpus version and invocation logs hold the request and the response.

### Question 56 — C

Answer: Publish a model card with the model version. A model card documents intended use and known limits for reviewers. Local study-map skill 3.7 (Responsible AI and Transparency), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. A Bedrock evaluation job scores candidate models on your prompts and metrics before you choose. Why the correct answer wins: A model card documents intended use and known limits for reviewers.
- **B:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: A model card documents intended use and known limits for reviewers.
- **C:** Correct. In this case: A model card documents intended use and known limits for reviewers.
- **D:** Incorrect for this question. A schema makes the output machine-parseable and rejects prose that breaks the contract. Why the correct answer wins: A model card documents intended use and known limits for reviewers.

### Question 57 — C

Answer: Escalate low-confidence or high-impact answers to a person. An escalation path keeps consequential answers with a human owner. Local study-map skill 3.7 (Responsible AI and Transparency), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: An escalation path keeps consequential answers with a human owner.
- **B:** Incorrect for this question. A token cap bounds the cost of a runaway answer and the latency of every call. Why the correct answer wins: An escalation path keeps consequential answers with a human owner.
- **C:** Correct. In this case: An escalation path keeps consequential answers with a human owner.
- **D:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: An escalation path keeps consequential answers with a human owner.

### Question 58 — C

Answer: Report fairness metrics per user segment. Segment metrics expose a quality gap that an overall average hides. Local study-map skill 3.8 (Fairness and Compliance Monitoring), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 3 (AI safety, security, and governance, 20 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain3.html.

- **A:** Incorrect for this question. Anomaly detection finds an unexpected token bill without a fixed threshold. Why the correct answer wins: Segment metrics expose a quality gap that an overall average hides.
- **B:** Incorrect for this question. A latency alarm fires on the symptom users feel. Why the correct answer wins: Segment metrics expose a quality gap that an overall average hides.
- **C:** Correct. In this case: Segment metrics expose a quality gap that an overall average hides.
- **D:** Incorrect for this question. A drift alert catches a fairness regression after a model or prompt change. Why the correct answer wins: Segment metrics expose a quality gap that an overall average hides.

### Question 59 — B

Answer: Prune older turns from the context window. Dropping stale turns cuts input tokens without losing the current instruction. Local study-map skill 4.1 (Token Cost Efficiency), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Incorrect for this question. Larger chunks carry more context but dilute the embedding and crowd the prompt window. Why the correct answer wins: Dropping stale turns cuts input tokens without losing the current instruction.
- **B:** Correct. In this case: Dropping stale turns cuts input tokens without losing the current instruction.
- **C:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: Dropping stale turns cuts input tokens without losing the current instruction.
- **D:** Incorrect for this question. More passages raise recall and also lengthen the prompt and the cost per call. Why the correct answer wins: Dropping stale turns cuts input tokens without losing the current instruction.

### Question 60 — B

Answer: Retrieve fewer passages per answer. Fewer passages shrink the prompt, which lowers both cost and latency. Local study-map skill 4.1 (Token Cost Efficiency), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: Fewer passages shrink the prompt, which lowers both cost and latency.
- **B:** Correct. In this case: Fewer passages shrink the prompt, which lowers both cost and latency.
- **C:** Incorrect for this question. More passages raise recall and also lengthen the prompt and the cost per call. Why the correct answer wins: Fewer passages shrink the prompt, which lowers both cost and latency.
- **D:** Incorrect for this question. Larger chunks carry more context but dilute the embedding and crowd the prompt window. Why the correct answer wins: Fewer passages shrink the prompt, which lowers both cost and latency.

### Question 61 — A

Answer: Cache the response under a hash of the normalised request. A hash cache is exact and avoids a false hit between similar questions. Local study-map skill 4.2 (Model Tiering and Caching), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Correct. In this case: A hash cache is exact and avoids a false hit between similar questions.
- **B:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: A hash cache is exact and avoids a false hit between similar questions.
- **C:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: A hash cache is exact and avoids a false hit between similar questions.
- **D:** Incorrect for this question. A semantic cache serves a near-duplicate question without a model call. Why the correct answer wins: A hash cache is exact and avoids a false hit between similar questions.

### Question 62 — A, E

Answers: Send routine prompts to a small model and hard prompts to a large one; Cache the stable prompt prefix with prompt caching. Prompt caching reuses the processed prefix and tiered routing keeps easy questions on a small model. Tiered routing spends the large model only on the requests that need it. Prompt caching reuses processed prefix tokens, which cuts latency and input cost on repeat calls. Local study-map skill 4.2 (Model Tiering and Caching), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Correct. Prompt caching reuses processed prefix tokens, which cuts latency and input cost on repeat calls. In this case: Prompt caching reuses the processed prefix and tiered routing keeps easy questions on a small model.
- **B:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: Prompt caching reuses the processed prefix and tiered routing keeps easy questions on a small model.
- **C:** Incorrect for this question. A full fine-tune changes all weights, which is expensive and gives one model per task. Why the correct answer wins: Prompt caching reuses the processed prefix and tiered routing keeps easy questions on a small model.
- **D:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: Prompt caching reuses the processed prefix and tiered routing keeps easy questions on a small model.
- **E:** Correct. Tiered routing spends the large model only on the requests that need it. In this case: Prompt caching reuses the processed prefix and tiered routing keeps easy questions on a small model.

### Question 63 — D

Answer: Precompute answers for predictable questions on a schedule. Precomputation moves repeatable work into a cheap batch window. Local study-map skill 4.3 (Throughput and Latency Optimisation), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: Precomputation moves repeatable work into a cheap batch window.
- **B:** Incorrect for this question. Streaming lowers perceived latency without changing total generation time. Why the correct answer wins: Precomputation moves repeatable work into a cheap batch window.
- **C:** Incorrect for this question. A synchronous call is simplest and makes the user wait for the final token. Why the correct answer wins: Precomputation moves repeatable work into a cheap batch window.
- **D:** Correct. In this case: Precomputation moves repeatable work into a cheap batch window.

### Question 64 — C, D

Answers: Plan capacity from measured tokens per minute; Stream tokens as they are generated. Capacity sized from observed token throughput prevents throttling and streaming improves perceived speed. Capacity sized from observed token throughput avoids both throttling and idle spend. Streaming lowers perceived latency without changing total generation time. Local study-map skill 4.3 (Throughput and Latency Optimisation), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Incorrect for this question. Batch inference trades turnaround time for a lower price on large offline volumes. Why the correct answer wins: Capacity sized from observed token throughput prevents throttling and streaming improves perceived speed.
- **B:** Incorrect for this question. One model for every request keeps the code simple but pays frontier prices for trivial prompts. Why the correct answer wins: Capacity sized from observed token throughput prevents throttling and streaming improves perceived speed.
- **C:** Correct. Capacity sized from observed token throughput avoids both throttling and idle spend. In this case: Capacity sized from observed token throughput prevents throttling and streaming improves perceived speed.
- **D:** Correct. Streaming lowers perceived latency without changing total generation time. In this case: Capacity sized from observed token throughput prevents throttling and streaming improves perceived speed.
- **E:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: Capacity sized from observed token throughput prevents throttling and streaming improves perceived speed.

### Question 65 — A

Answer: Alarm on p95 latency and error rate. A latency alarm fires on the symptom users feel. Local study-map skill 4.4 (GenAI Observability), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Correct. In this case: A latency alarm fires on the symptom users feel.
- **B:** Incorrect for this question. Anomaly detection finds an unexpected token bill without a fixed threshold. Why the correct answer wins: A latency alarm fires on the symptom users feel.
- **C:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: A latency alarm fires on the symptom users feel.
- **D:** Incorrect for this question. A model card documents intended use and known limits for reviewers. Why the correct answer wins: A latency alarm fires on the symptom users feel.

### Question 66 — B, E

Answers: Publish token usage as CloudWatch metrics; Detect spend spikes with AWS Cost Anomaly Detection. Token metrics show where spend comes from and anomaly detection finds an unexpected bill. Token metrics per model and tenant show where spend and latency come from. Anomaly detection finds an unexpected token bill without a fixed threshold. Local study-map skill 4.4 (GenAI Observability), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Incorrect for this question. A model card documents intended use and known limits for reviewers. Why the correct answer wins: Token metrics show where spend comes from and anomaly detection finds an unexpected bill.
- **B:** Correct. Token metrics per model and tenant show where spend and latency come from. In this case: Token metrics show where spend comes from and anomaly detection finds an unexpected bill.
- **C:** Incorrect for this question. A latency alarm fires on the symptom users feel. Why the correct answer wins: Token metrics show where spend comes from and anomaly detection finds an unexpected bill.
- **D:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: Token metrics show where spend comes from and anomaly detection finds an unexpected bill.
- **E:** Correct. Anomaly detection finds an unexpected token bill without a fixed threshold. In this case: Token metrics show where spend comes from and anomaly detection finds an unexpected bill.

### Question 67 — D

Answer: Break down spend by application tag in AWS Cost Explorer. Tag-based cost views attribute the token bill to the team that caused it. Local study-map skill 4.5 (Cost Attribution and Governance), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 4 (operational efficiency and optimization, 12 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain4.html.

- **A:** Incorrect for this question. Anomaly detection finds an unexpected token bill without a fixed threshold. Why the correct answer wins: Tag-based cost views attribute the token bill to the team that caused it.
- **B:** Incorrect for this question. An idle endpoint bills for capacity that sits unused between requests. Why the correct answer wins: Tag-based cost views attribute the token bill to the team that caused it.
- **C:** Incorrect for this question. A Savings Plan discounts the predictable part of the compute baseline. Why the correct answer wins: Tag-based cost views attribute the token bill to the team that caused it.
- **D:** Correct. In this case: Tag-based cost views attribute the token bill to the team that caused it.

### Question 68 — C

Answer: Measure whether each claim is supported by the retrieved context. A faithfulness check separates a grounded answer from a fluent invention. Local study-map skill 5.1 (GenAI Evaluation Metrics), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Incorrect for this question. Relevance separates an off-topic answer from a factually wrong one. Why the correct answer wins: A faithfulness check separates a grounded answer from a fluent invention.
- **B:** Incorrect for this question. Embedding-based similarity credits a correct paraphrase that word overlap misses. Why the correct answer wins: A faithfulness check separates a grounded answer from a fluent invention.
- **C:** Correct. In this case: A faithfulness check separates a grounded answer from a fluent invention.
- **D:** Incorrect for this question. Overlap metrics are cheap and reward wording that matches the references. Why the correct answer wins: A faithfulness check separates a grounded answer from a fluent invention.

### Question 69 — A, C

Answers: Score candidate answers with a judge model on a fixed rubric; Measure the judge model against expert labels first. A judge model scales the scoring and an agreement check shows whether it matches expert labels. A judge model scales subjective scoring and needs its own agreement check. Agreement with experts shows whether the judge can be trusted on this task. Local study-map skill 5.1 (GenAI Evaluation Metrics), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Correct. Agreement with experts shows whether the judge can be trusted on this task. In this case: A judge model scales the scoring and an agreement check shows whether it matches expert labels.
- **B:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: A judge model scales the scoring and an agreement check shows whether it matches expert labels.
- **C:** Correct. A judge model scales subjective scoring and needs its own agreement check. In this case: A judge model scales the scoring and an agreement check shows whether it matches expert labels.
- **D:** Incorrect for this question. Recall shows whether the answer was missing evidence before generation began. Why the correct answer wins: A judge model scales the scoring and an agreement check shows whether it matches expert labels.
- **E:** Incorrect for this question. Overlap metrics are cheap and reward wording that matches the references. Why the correct answer wins: A judge model scales the scoring and an agreement check shows whether it matches expert labels.

### Question 70 — C

Answer: Mirror production traffic to the new version and compare offline. Shadow traffic compares answers with no user exposure. Local study-map skill 5.2 (Model Comparison and Traffic Testing), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Incorrect for this question. A rubric with human scores gives a reference the automatic metrics can be checked against. Why the correct answer wins: Shadow traffic compares answers with no user exposure.
- **B:** Incorrect for this question. A canary limits the blast radius of a prompt or model change. Why the correct answer wins: Shadow traffic compares answers with no user exposure.
- **C:** Correct. In this case: Shadow traffic compares answers with no user exposure.
- **D:** Incorrect for this question. An A/B test measures the difference on real traffic before a full switch. Why the correct answer wins: Shadow traffic compares answers with no user exposure.

### Question 71 — C

Answer: Run the release against a curated golden question set. A golden set with known answers catches a regression the moment it ships. Local study-map skill 5.3 (Regression Testing and Quality Gates), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Incorrect for this question. A retention period bounds storage cost and matches the data policy. Why the correct answer wins: A golden set with known answers catches a regression the moment it ships.
- **B:** Incorrect for this question. A rubric with human scores gives a reference the automatic metrics can be checked against. Why the correct answer wins: A golden set with known answers catches a regression the moment it ships.
- **C:** Correct. In this case: A golden set with known answers catches a regression the moment it ships.
- **D:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: A golden set with known answers catches a regression the moment it ships.

### Question 72 — B, E

Answers: Block the release when evaluation drops below the threshold; Replay scripted user journeys against the new version. A quality gate blocks the regression and scripted journeys exercise paths single prompts never reach. A quality gate stops a measurable regression from reaching production. Local study-map skill 5.3 (Regression Testing and Quality Gates), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Incorrect for this question. Unbounded retries turn a short dependency outage into a long queue backlog. Why the correct answer wins: A quality gate blocks the regression and scripted journeys exercise paths single prompts never reach.
- **B:** Correct. In this case: A quality gate blocks the regression and scripted journeys exercise paths single prompts never reach.
- **C:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: A quality gate blocks the regression and scripted journeys exercise paths single prompts never reach.
- **D:** Incorrect for this question. Higher temperature widens sampling, which suits brainstorming and not factual lookup. Why the correct answer wins: A quality gate blocks the regression and scripted journeys exercise paths single prompts never reach.
- **E:** Correct. A quality gate stops a measurable regression from reaching production. In this case: A quality gate blocks the regression and scripted journeys exercise paths single prompts never reach.

### Question 73 — B

Answer: Measure whether the agent called the right tool with the right arguments. Tool accuracy locates the failure inside the agent loop rather than at the answer. Local study-map skill 5.4 (Retrieval and Agent Evaluation), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Incorrect for this question. Recall shows whether the answer was missing evidence before generation began. Why the correct answer wins: Tool accuracy locates the failure inside the agent loop rather than at the answer.
- **B:** Correct. In this case: Tool accuracy locates the failure inside the agent loop rather than at the answer.
- **C:** Incorrect for this question. Completion rate is the outcome metric for an agent that must actually finish work. Why the correct answer wins: Tool accuracy locates the failure inside the agent loop rather than at the answer.
- **D:** Incorrect for this question. Overlap metrics are cheap and reward wording that matches the references. Why the correct answer wins: Tool accuracy locates the failure inside the agent loop rather than at the answer.

### Question 74 — B, C

Answers: Measure whether the needed passage was retrieved at all; Measure the share of agent tasks completed end to end. Recall shows whether the needed passage was retrieved and completion rate shows whether the task ended. Recall shows whether the answer was missing evidence before generation began. Completion rate is the outcome metric for an agent that must actually finish work. Local study-map skill 5.4 (Retrieval and Agent Evaluation), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Incorrect for this question. Embedding-based similarity credits a correct paraphrase that word overlap misses. Why the correct answer wins: Recall shows whether the needed passage was retrieved and completion rate shows whether the task ended.
- **B:** Correct. Recall shows whether the answer was missing evidence before generation began. In this case: Recall shows whether the needed passage was retrieved and completion rate shows whether the task ended.
- **C:** Correct. Completion rate is the outcome metric for an agent that must actually finish work. In this case: Recall shows whether the needed passage was retrieved and completion rate shows whether the task ended.
- **D:** Incorrect for this question. Retrieval precision explains a wrong answer that the model was given bad context for. Why the correct answer wins: Recall shows whether the needed passage was retrieved and completion rate shows whether the task ended.
- **E:** Incorrect for this question. Overlap metrics are cheap and reward wording that matches the references. Why the correct answer wins: Recall shows whether the needed passage was retrieved and completion rate shows whether the task ended.

### Question 75 — A

Answer: Inspect the agent reasoning trace for the failed task. The trace shows which step misread the request or the tool result. Local study-map skill 5.5 (GenAI Troubleshooting), mapped to the official guide: AWS Certified Generative AI Developer - Professional (AIP-C01) exam guide. Primary reference: AIP-C01 exam guide, content domain 5 (testing, validation, and troubleshooting, 11 percent): https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01-domain5.html.

- **A:** Correct. In this case: The trace shows which step misread the request or the tool result.
- **B:** Incorrect for this question. A trace shows which hop in the chain added the latency. Why the correct answer wins: The trace shows which step misread the request or the tool result.
- **C:** Incorrect for this question. Answers without expiry keep serving text that the corpus has already corrected. Why the correct answer wins: The trace shows which step misread the request or the tool result.
- **D:** Incorrect for this question. A truncation check shows whether the model ever saw the end of the instruction. Why the correct answer wins: The trace shows which step misread the request or the tool result.
