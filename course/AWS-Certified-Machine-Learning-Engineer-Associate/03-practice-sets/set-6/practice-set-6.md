# AWS Certified Machine Learning Engineer – Associate (MLA-C02) — Full-Length Mock Exam 6

Machine Learning Engineer · 65 questions · 130 minutes · scaled passing score 720 of 1000

Blueprint-weighted mock exam. Item mix: 50 multiple-choice and 15 multiple-response items (the selection count is stated in each multi-response stem). The published exam has 65 questions in 130 minutes, of which 50 are scored and 15 are unscored, and AWS does not identify the unscored items. AWS publishes no split between multiple-choice and multiple-response items, so the 15-item multi-response block is an authoring choice. At 65 items in 130 minutes this set matches the published pacing at about 120 seconds per item. AWS is currently delivering MLA-C02 as a beta of 85 questions in 170 minutes with the extra items unscored; this set follows the published 65-question form. The published format has no case-study component, so no case-study item appears here. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied AWS exam items.

## Questions

---

## Domain 1 — Data Preparation for ML and AI (28%) — Ingestion, storage, feature engineering, embeddings, and data quality

### 1. Parcel scans are being throttled at exactly the same point every morning, and the error names a limit rather than a timeout. What should be done first?

- A. Transform each stream record with AWS Lambda
- B. Raise the Kinesis shard count to match the write rate
- C. Increase the Firehose buffer size and interval
- D. Request a service quota increase for the throttled resource

### 2. A driver app asks for the current delivery window of one parcel, one row at a time, thousands of times a minute. What store serves that?

- A. Use Amazon FSx for Lustre for the training file system
- B. Serve low-latency feature lookups from Amazon DynamoDB
- C. Land the dataset as Parquet in Amazon S3
- D. Index the vectors in Amazon OpenSearch Service with k-NN search

### 3. A warehouse scanner fleet will quadruple its write rate next quarter, and the stream is already at its throughput ceiling. What should be raised?

- A. Transform the data with an AWS Glue ETL job
- B. Raise the Kinesis shard count to match the write rate
- C. Deliver the stream to Amazon S3 with Amazon Data Firehose
- D. Ingest the events through Amazon MSK

### 4. Signed proof-of-delivery images must be retained for eleven years and are almost never opened after the dispute window closes. What fits?

- A. Archive the raw corpus to an S3 Glacier storage class
- B. Expire intermediate artefacts with an S3 lifecycle rule
- C. Apply S3 Object Lock to the regulated training data
- D. Use S3 Intelligent-Tiering for the unevenly accessed corpus

### 5. Delivery features read six of fifty scan columns and always restrict to one depot and one day. Which two storage choices fit? Select two.

- A. Land the raw JSON events in Amazon S3 unchanged
- B. Partition the S3 prefix by event date
- C. Attach a gp3 Amazon EBS volume to the training instance
- D. Mount a shared Amazon EFS file system on every training host
- E. Land the dataset as Parquet in Amazon S3

### 6. A disputes team must replay the exact scanner message that produced a wrong delivery time. Why keep the untouched original beside the cleaned table?

- A. Land the dataset as Parquet in Amazon S3
- B. Partition the S3 prefix by event date
- C. Land the raw JSON events in Amazon S3 unchanged
- D. Apply S3 Object Lock to the regulated training data

### 7. Route optimisation history spanning nine years must be replayed with custom GeoSpark libraries on a cluster sized to the job. What fits?

- A. Transform each stream record with AWS Lambda
- B. Transform the data with an AWS Glue ETL job
- C. Profile and clean the data with AWS Glue DataBrew
- D. Process the data with Spark on Amazon EMR

### 8. Depot, fleet and customer extracts must be merged on a nightly schedule, and the team has no servers it wants to operate. What fits?

- A. Transform the data with an AWS Glue ETL job
- B. Prepare the data in SageMaker Data Wrangler
- C. Process the data with Spark on Amazon EMR
- D. Register the tables in the AWS Glue Data Catalog

### 9. A late-delivery model must train on the depot features that were known when each parcel was dispatched, not today's values. What supplies that?

- A. Register the tables in the AWS Glue Data Catalog
- B. Keep the point-in-time history in the Feature Store offline store
- C. Publish the features to the SageMaker Feature Store online store
- D. Ingest the cleaned rows into a SageMaker Feature Group

### 10. Distance in metres and parcel weight in grams are fed to a gradient model, and the distance column dominates every split. What preparation fits?

- A. Bin the continuous age column into ranges
- B. Standardise the numeric columns before training
- C. Apply a log transform to the skewed amount column
- D. One-hot encode the categorical columns

### 11. Delivery delay is heavily right-skewed, and the late-parcel label appears rarely and unevenly across splits. Which two steps fit? Select two.

- A. Apply a log transform to the skewed amount column
- B. Stratify the train, validation and test splits by label
- C. Shuffle the rows before every epoch
- D. Standardise the numeric columns before training
- E. One-hot encode the categorical columns

### 12. Drivers must search forty million delivery notes by meaning, filtered to their own region, through a managed index. What fits?

- A. Load every vector into the application process on each request
- B. Store the vectors in Amazon RDS for PostgreSQL with pgvector
- C. Index the vectors in Amazon OpenSearch Service with k-NN search
- D. Keep the vectors in Amazon S3 with a vector index

### 13. Support macros must become searchable vectors, and agents search by exact parcel number as often as by wording. Which two components fit? Select two.

- A. Fine-tune the embedding model on the domain question-answer pairs
- B. Combine keyword and vector retrieval
- C. Add a reranking step after retrieval
- D. Generate the embeddings with an Amazon Bedrock embedding model
- E. Index the vectors in Amazon OpenSearch Service with k-NN search

### 14. A customs rulebook is organised by numbered sections, and retrieval keeps returning text that straddles two unrelated rules. What should change first?

- A. Store source, date and section metadata with each chunk
- B. Chunk the documents on semantic boundaries such as headings
- C. Split the documents into fixed-size overlapping chunks
- D. Index parent sections and retrieve their child chunks

### 15. The nightly depot load must stop rather than train when a required scan field is empty, and later comparisons need accepted statistics stored. Which two controls fit? Select two.

- A. Enforce a schema contract on the ingested records
- B. Profile and clean the data with AWS Glue DataBrew
- C. Expire intermediate artefacts with an S3 lifecycle rule
- D. Evaluate AWS Glue Data Quality rules on the prepared table
- E. Profile the incoming data and store the statistics as a baseline

### 16. Two hundred thousand delivery photos need damage labels, and only a handful of claims specialists can judge the ambiguous ones. What fits?

- A. Send the unlabelled records to Amazon SageMaker Ground Truth
- B. Use automated data labelling with a human review sample in Ground Truth
- C. Remove duplicate rows before splitting
- D. Mask and redact personal identifiers before training

### 17. A damage-detection set has far fewer annotated images than matching text reports, so the image branch trails the text branch. What should be addressed?

- A. Stratify the train, validation and test splits by label
- B. Reweight the under-represented group in the loss
- C. Measure bias with SageMaker Clarify before training
- D. Rebalance the numeric, text and image assets in the set

### 18. Late deliveries are 1.2 percent of records, and the business accepts the current class mix as it is. What fits?

- A. Generate synthetic minority samples to rebalance the classes
- B. Drop every row that has any missing field
- C. Clip extreme outliers to a defined percentile
- D. Set class weights instead of resampling

---

## Domain 2 — ML Model and Foundation Model (FM) Development (24%) — Model and FM selection, tuning, customisation, and evaluation

### 19. A depot planner needs a distribution of expected parcel volume per hour for the next fortnight. What fits?

- A. Forecast the series with the DeepAR algorithm
- B. Use Random Cut Forest for anomaly scoring
- C. Train the tabular classifier with the XGBoost built-in algorithm
- D. Train with the linear learner algorithm

### 20. An auditor must see the exact contribution of distance and weight to each late-delivery score. What model choice fits?

- A. Average several models into an ensemble
- B. Train the tabular classifier with the XGBoost built-in algorithm
- C. Use the k-nearest-neighbours algorithm
- D. Train with the linear learner algorithm

### 21. A driver-messaging assistant answers one-line questions at very high volume and needs the lowest cost per answer. Which model choice fits?

- A. Select an Amazon Nova foundation model in Amazon Bedrock
- B. Download open weights and host them on your own endpoint
- C. Select an Anthropic Claude model in Amazon Bedrock
- D. Select a Titan embedding model in Amazon Bedrock

### 22. Support macros must become vectors for similarity search with no model hosts. What fits?

- A. Download open weights and host them on your own endpoint
- B. Select an Anthropic Claude model in Amazon Bedrock
- C. Select an Amazon Nova foundation model in Amazon Bedrock
- D. Select a Titan embedding model in Amazon Bedrock

### 23. A large assistant writes excellent replies but is far too expensive at contact-centre volume, and reply quality must stay close. What fits?

- A. Run continued pre-training on the domain corpus
- B. Distil the large model into a smaller student model
- C. Fine-tune with parameter-efficient adapters such as LoRA
- D. Run full-parameter fine-tuning on the curated corpus

### 24. The assistant must adopt the carrier's claim codes, and its general politeness and safety behaviour must not degrade. Which two techniques fit? Select two.

- A. Run continued pre-training on the domain corpus
- B. Fine-tune with parameter-efficient adapters such as LoRA
- C. Start with task-specific prompt engineering before any training
- D. Mix replay samples from the original distribution into fine-tuning
- E. Run full-parameter fine-tuning on the curated corpus

### 25. Retrieval matches a single policy sentence well, but the answer needs the surrounding clause to be correct. What pattern fits?

- A. Index parent sections and retrieve their child chunks
- B. Split the documents into fixed-size overlapping chunks
- C. Store source, date and section metadata with each chunk
- D. Chunk the documents on semantic boundaries such as headings

### 26. Two hundred thousand photographed customs forms must become structured fields. What fits?

- A. Extract the form fields with Amazon Textract
- B. Transcribe the calls with Amazon Transcribe
- C. Detect objects and text in images with Amazon Rekognition
- D. Detect entities and sentiment with Amazon Comprehend

### 27. A LightGBM training script uses only standard libraries and should run inside a managed framework container. What fits?

- A. Start from a SageMaker JumpStart model
- B. Package the training code in script mode with a supported framework
- C. Train the tabular classifier with the XGBoost built-in algorithm
- D. Bring a custom training container image

### 28. Every tuning trial runs its full epoch budget although validation has not improved for twelve rounds. What should be enabled?

- A. Enable early stopping on the validation metric
- B. Use Bayesian search over a defined objective metric
- C. Tune hyperparameters with SageMaker automatic model tuning
- D. Define the tuning objective on the validation metric that matters

### 29. The tuner must optimise on-time delivery rather than raw accuracy, and later trials should be chosen from earlier evidence. Which two elements fit? Select two.

- A. Define the tuning objective on the validation metric that matters
- B. Use Bayesian search over a defined objective metric
- C. Run a hand-written grid of training jobs
- D. Use random search over a small range
- E. Enable early stopping on the validation metric

### 30. Training runs on reclaimable capacity, a run was lost last week, and successive jobs waste twenty minutes provisioning. Which two changes fit? Select two.

- A. Run training on managed Spot training capacity
- B. Shard the model across instances with model parallelism
- C. Keep a managed warm pool for the training cluster
- D. Split each batch across instances with data parallelism
- E. Checkpoint to Amazon S3 so an interrupted job resumes

### 31. Dispatchers keep asking which kind of mistake the late-delivery model makes most often. What should be shown?

- A. Report RMSE for the regression
- B. Report ROC-AUC for the ranking task
- C. Inspect the confusion matrix on the minority class
- D. Report F1 on the holdout set

### 32. Two models must be compared as a ranking for late parcels, and promised delivery windows must be reported in hours of error. Which two metrics fit? Select two.

- A. Report accuracy alone on a 2 percent positive class
- B. Report F1 on the holdout set
- C. Report ROC-AUC for the ranking task
- D. Report RMSE for the regression
- E. Score the generated summaries with BLEU

### 33. Generated customer replies are graded against reference replies, and a well-phrased paraphrase is being scored as wrong. What fits?

- A. Score the answers with BERTScore
- B. Score the generated summaries with ROUGE
- C. Score the generated summaries with BLEU
- D. Report RMSE for the regression

### 34. Two analysts reproduce the same late-delivery experiment and get different numbers, and neither can say which snapshot they used. What is missing?

- A. Run an Amazon Bedrock model evaluation job
- B. Register the approved version in the SageMaker Model Registry
- C. Pin the data snapshot, code version and hyperparameters for each run
- D. Log runs with MLflow on SageMaker AI

---

## Domain 3 — Deployment and Orchestration of ML and AI Workflows (24%) — Inference infrastructure, scaling, CI/CD, and orchestration

### 35. A route-optimisation request takes four minutes, and the caller collects the answer from S3 when it is ready. What fits?

- A. Deploy a serverless inference endpoint
- B. Use asynchronous inference with results written to Amazon S3
- C. Deploy a real-time SageMaker AI endpoint
- D. Run a batch transform job over the stored records

### 36. Every parcel is rescored once a night in bulk, and a dispatcher console needs an immediate score on demand. Which two methods fit? Select two.

- A. Run a batch transform job over the stored records
- B. Deploy a serverless inference endpoint
- C. Host many small models behind one multi-model endpoint
- D. Deploy a real-time SageMaker AI endpoint
- E. Use asynchronous inference with results written to Amazon S3

### 37. Address normalisation and the late-delivery model must execute behind a single endpoint invocation. What fits?

- A. Deploy a real-time SageMaker AI endpoint
- B. Host many small models behind one multi-model endpoint
- C. Run a batch transform job over the stored records
- D. Run several containers behind one endpoint

### 38. Weights tuned outside AWS must answer through the Bedrock API with no container platform to operate. What fits?

- A. Buy provisioned throughput for the Bedrock model
- B. Start from a SageMaker JumpStart model
- C. Import the fine-tuned weights with Bedrock custom model import
- D. Download open weights and host them on your own endpoint

### 39. The driver assistant must never be throttled, and its volume does not vary enough to justify per-call pricing alone. What should be bought?

- A. Call the Bedrock model on demand
- B. Buy provisioned throughput for the Bedrock model
- C. Right-size the endpoint with SageMaker Inference Recommender
- D. Compare provisioned throughput against on-demand spend

### 40. A support agent must recall the order number given two turns earlier in the same chat. What should be implemented?

- A. Schedule a knowledge base sync when documents change
- B. Store the prompt templates in Amazon Bedrock Prompt Management
- C. Persist the agent session state between turns
- D. Deploy the agent with its action groups and knowledge base

### 41. The dispatch service already runs on Kubernetes elsewhere and must keep its manifests and tooling. What fits?

- A. Run the job on AWS Batch
- B. Serve the model from an AWS Lambda function
- C. Run the container on Amazon EKS
- D. Run the container on Amazon ECS

### 42. A depot planning endpoint is used only between four and eight each morning, and idle hours dominate its bill. What should be configured?

- A. Auto scale the endpoint on a target-tracking policy
- B. Scale the endpoint to zero outside business hours
- C. Keep a managed warm pool for the training cluster
- D. Auto scale on a step policy with CloudWatch alarms

### 43. Each call holds the accelerator for seconds, so instance count lags the queue, and the morning rush must not meet a cold start. Which two settings fit? Select two.

- A. Scale on GPU utilisation rather than invocation count
- B. Auto scale on a step policy with CloudWatch alarms
- C. Auto scale the endpoint on a target-tracking policy
- D. Keep provisioned concurrency ready for the burst window
- E. Scale the endpoint to zero outside business hours

### 44. The late-delivery endpoint must have no route to the internet and must reach S3 privately. Where should it sit?

- A. Create an interface VPC endpoint for the service
- B. Route the private subnet through a NAT gateway
- C. Place the endpoint and model containers in private subnets
- D. Allow ingress from any address on the endpoint port

### 45. The pipeline reads a repository hosted outside AWS, and every commit must build and test the image in a clean environment. Which two services fit? Select two.

- A. Connect the external repository with AWS CodeConnections
- B. Orchestrate the release with AWS CodePipeline
- C. Build and test the model image with AWS CodeBuild
- D. Keep the pipeline source in AWS CodeCommit
- E. Shift traffic with AWS CodeDeploy

### 46. Releases must follow an ordered sequence of stages with recorded outcomes and an approval between them. What fits?

- A. Fail the pipeline when the evaluation threshold is missed
- B. Build and test the model image with AWS CodeBuild
- C. Shift traffic with AWS CodeDeploy
- D. Orchestrate the release with AWS CodePipeline

### 47. A support lead must confirm which approved reply model is live in each region and when it was approved. What fits?

- A. Log runs with MLflow on SageMaker AI
- B. Store the prompt templates in Amazon Bedrock Prompt Management
- C. Keep the pipeline source in AWS CodeCommit
- D. Register the approved version in the SageMaker Model Registry

### 48. A carrier wants the reply model swapped across every region in one step because the change window is ten minutes. Which strategy should be argued against?

- A. Send a small share of traffic to the new version first
- B. Shift traffic to the new version in equal steps
- C. Replace the production version in a single switch
- D. Stand the new version beside the old and switch traffic

### 49. A new reply model must be scored on real conversations without customers seeing it, then exposed to a tiny share before wider rollout. Which two strategies fit? Select two.

- A. Stand the new version beside the old and switch traffic
- B. Send a small share of traffic to the new version first
- C. Replace the production version in a single switch
- D. Mirror traffic to the new model without serving its answers
- E. Shift traffic to the new version in equal steps

### 50. Training must stop for manager sign-off, run a long evaluation, then take different paths depending on the outcome. What fits?

- A. Orchestrate the steps with AWS Step Functions
- B. Orchestrate the release with AWS CodePipeline
- C. Define the workflow as a SageMaker pipeline
- D. Trigger the retraining run with an EventBridge schedule

---

## Domain 4 — Operating, Monitoring, and Securing ML and AI Solutions (24%) — Monitoring, cost control, identity, network isolation, and guardrails

### 51. Inputs look stable, yet the late-delivery model has begun leaning on a postcode field it previously ignored. What should be monitored?

- A. Enable feature attribution drift monitoring
- B. Enable a bias drift monitor
- C. Enable a data drift monitor on the endpoint
- D. Enable a model quality monitor with ground-truth labels

### 52. Delivery outcomes arrive two days after each prediction, and one depot's customers must be watched for a changing outcome rate. Which two monitors fit? Select two.

- A. Enable feature attribution drift monitoring
- B. Enable a model quality monitor with ground-truth labels
- C. Alarm on the CloudWatch latency and error metrics
- D. Enable a data drift monitor on the endpoint
- E. Enable a bias drift monitor

### 53. A tracking request crosses an API, a normaliser and an endpoint, and nobody can say which hop adds the delay. What fits?

- A. Trace the pipeline service calls with AWS X-Ray
- B. Query the inference logs with CloudWatch Logs Insights
- C. Build a CloudWatch dashboard for the pipeline metrics
- D. Track resource configuration with AWS Config

### 54. The operations room wants one continuously refreshed screen of latency, errors and queue depth. What fits?

- A. Query the inference logs with CloudWatch Logs Insights
- B. Trace the pipeline service calls with AWS X-Ray
- C. Build a CloudWatch dashboard for the pipeline metrics
- D. Alarm on the CloudWatch latency and error metrics

### 55. A support agent occasionally fails after the third tool call, and the team needs to see each tool invocation and its result. What fits?

- A. Alarm on the CloudWatch latency and error metrics
- B. Trace the pipeline service calls with AWS X-Ray
- C. Enable CloudWatch generative AI observability for the model calls
- D. Trace agent tool calls with Bedrock AgentCore Observability

### 56. Inference runs at a flat, predictable volume every hour of the year. What should be bought to lower the rate?

- A. Right-size the instance family against the measured latency
- B. Move the offline scoring to batch transform
- C. Break the spend down by endpoint with AWS Cost Explorer
- D. Cover the steady inference load with a Savings Plan

### 57. The endpoint family is twice the measured need, and a nightly bulk rescore keeps an idle endpoint alive by day. Which two changes fit? Select two.

- A. Start with the largest available model for every request
- B. Move the offline scoring to batch transform
- C. Scale the endpoint to zero outside business hours
- D. Right-size the instance family against the measured latency
- E. Cover the steady inference load with a Savings Plan

### 58. The customs index is rebuilt daily although fewer than one percent of documents changed. What should be added?

- A. Route routine requests to a smaller model
- B. Cache embeddings for documents that have not changed
- C. Trim the retrieved context sent to the model
- D. Cap the output tokens per request

### 59. Most driver questions are one-line status checks, yet every one is answered by the largest model. What should be added?

- A. Cache embeddings for documents that have not changed
- B. Trim the retrieved context sent to the model
- C. Cap the output tokens per request
- D. Route routine requests to a smaller model

### 60. A training job needs its own identity and must read only the depot prefix it was built for. Which two controls fit? Select two.

- A. Create a long-lived access key for the integration
- B. Attach one policy to an IAM group the engineers belong to
- C. Attach a policy scoped to the one bucket prefix
- D. Use the account root user for pipeline administration
- E. Give the training job a scoped IAM execution role

### 61. Carrier-owned parcel data sits in its own account, and the central pipeline needs temporary access with nothing long-lived stored. What should be created?

- A. Attach one policy to an IAM group the engineers belong to
- B. Use the account root user for pipeline administration
- C. Create a role the other account can assume
- D. Create a long-lived access key for the integration

### 62. The training bucket must be reachable only through the VPC endpoint even from a valid identity elsewhere. What should be applied?

- A. Deny access to the bucket unless the request comes through the VPC endpoint
- B. Create an interface VPC endpoint for the service
- C. Place the endpoint and model containers in private subnets
- D. Restrict the security group to the application subnet

### 63. The carrier tracking API token must rotate monthly without redeploying the agent. What fits?

- A. Store the model API credential in AWS Secrets Manager
- B. Apply Amazon Bedrock Guardrails to the model responses
- C. Track resource configuration with AWS Config
- D. Encrypt the artefacts with a customer managed KMS key

### 64. A customer assistant must decline questions about competitor pricing while still answering everything else. What fits?

- A. Redact personal data before the prompt reaches the model
- B. Screen the training text for unsafe content
- C. Configure a denied-topics policy for the assistant
- D. Apply Amazon Bedrock Guardrails to the model responses

### 65. Every reply-service image must be checked for known vulnerabilities before it can be deployed. What fits?

- A. Record the API calls with AWS CloudTrail
- B. Scan the built image with Amazon Inspector
- C. Track resource configuration with AWS Config
- D. Review the pipeline code with Amazon CodeGuru

---

## Answer key and explanations

### Question 1 — D

Answer: Request a service quota increase for the throttled resource. A throttled call at a service limit is fixed by raising that limit. Local study-map skill 1.1 (Ingestion Sources and Storage Choice), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. A function per record suits lightweight enrichment and filtering of a stream. Why the correct answer wins: A throttled call at a service limit is fixed by raising that limit.
- **B:** Incorrect for this question. Throughput on a data stream is capped per shard, so capacity follows the shard count. Why the correct answer wins: A throttled call at a service limit is fixed by raising that limit.
- **C:** Incorrect for this question. A larger buffer trades delivery latency for fewer, bigger S3 objects. Why the correct answer wins: A throttled call at a service limit is fixed by raising that limit.
- **D:** Correct. In this case: A throttled call at a service limit is fixed by raising that limit.

### Question 2 — B

Answer: Serve low-latency feature lookups from Amazon DynamoDB. A key-value store answers each single-row read in milliseconds. DynamoDB answers key lookups at single-digit millisecond latency. Local study-map skill 1.1 (Ingestion Sources and Storage Choice), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Lustre delivers the high throughput a multi-node training job needs from shared storage. Why the correct answer wins: A key-value store answers each single-row read in milliseconds.
- **B:** Correct. DynamoDB answers key lookups at single-digit millisecond latency. In this case: A key-value store answers each single-row read in milliseconds.
- **C:** Incorrect for this question. Columnar Parquet files in S3 are read in column subsets, which suits repeated training scans. Why the correct answer wins: A key-value store answers each single-row read in milliseconds.
- **D:** Incorrect for this question. OpenSearch provides a managed vector index with filtered k-nearest-neighbour search. Why the correct answer wins: A key-value store answers each single-row read in milliseconds.

### Question 3 — B

Answer: Raise the Kinesis shard count to match the write rate. Stream throughput is capped per shard, so capacity follows the shard count. Local study-map skill 1.2 (Streaming Ingestion), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Glue runs a managed Spark job against catalogued sources and writes the prepared output. Why the correct answer wins: Stream throughput is capped per shard, so capacity follows the shard count.
- **B:** Correct. In this case: Stream throughput is capped per shard, so capacity follows the shard count.
- **C:** Incorrect for this question. Firehose batches the stream into S3 objects without a consumer to operate. Why the correct answer wins: Stream throughput is capped per shard, so capacity follows the shard count.
- **D:** Incorrect for this question. MSK runs managed Kafka, which suits teams already using Kafka clients and topics. Why the correct answer wins: Stream throughput is capped per shard, so capacity follows the shard count.

### Question 4 — A

Answer: Archive the raw corpus to an S3 Glacier storage class. An archive class is priced for data that is kept but rarely read. Local study-map skill 1.3 (Storage Class and Retention), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Correct. In this case: An archive class is priced for data that is kept but rarely read.
- **B:** Incorrect for this question. A lifecycle rule deletes the derived copies on a schedule, so storage does not grow forever. Why the correct answer wins: An archive class is priced for data that is kept but rarely read.
- **C:** Incorrect for this question. Object Lock prevents the retained objects from being altered or deleted for the stated period. Why the correct answer wins: An archive class is priced for data that is kept but rarely read.
- **D:** Incorrect for this question. Intelligent-Tiering moves objects between access tiers as usage changes, with no rules to write. Why the correct answer wins: An archive class is priced for data that is kept but rarely read.

### Question 5 — B, E

Answers: Land the dataset as Parquet in Amazon S3; Partition the S3 prefix by event date. A columnar file reads only the needed columns, and depot and date prefixes skip the rest. Columnar Parquet files in S3 are read in column subsets, which suits repeated training scans. Date partitioning lets a query or a training job skip the prefixes it does not need. Local study-map skill 1.4 (Data Formats and Partitioning), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Raw JSON is readable but forces every query to parse whole records. Why the correct answer wins: A columnar file reads only the needed columns, and depot and date prefixes skip the rest.
- **B:** Correct. Date partitioning lets a query or a training job skip the prefixes it does not need. In this case: A columnar file reads only the needed columns, and depot and date prefixes skip the rest.
- **C:** Incorrect for this question. EBS is block storage bound to one instance, which suits a single host and not a fleet. Why the correct answer wins: A columnar file reads only the needed columns, and depot and date prefixes skip the rest.
- **D:** Incorrect for this question. EFS gives many hosts one POSIX file system, which suits shared code and small data. Why the correct answer wins: A columnar file reads only the needed columns, and depot and date prefixes skip the rest.
- **E:** Correct. Columnar Parquet files in S3 are read in column subsets, which suits repeated training scans. In this case: A columnar file reads only the needed columns, and depot and date prefixes skip the rest.

### Question 6 — C

Answer: Land the raw JSON events in Amazon S3 unchanged. An unaltered original can be re-read without any transformation having been applied. Raw JSON is readable but forces every query to parse whole records. Local study-map skill 1.4 (Data Formats and Partitioning), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Columnar Parquet files in S3 are read in column subsets, which suits repeated training scans. Why the correct answer wins: An unaltered original can be re-read without any transformation having been applied.
- **B:** Incorrect for this question. Date partitioning lets a query or a training job skip the prefixes it does not need. Why the correct answer wins: An unaltered original can be re-read without any transformation having been applied.
- **C:** Correct. Raw JSON is readable but forces every query to parse whole records. In this case: An unaltered original can be re-read without any transformation having been applied.
- **D:** Incorrect for this question. Object Lock prevents the retained objects from being altered or deleted for the stated period. Why the correct answer wins: An unaltered original can be re-read without any transformation having been applied.

### Question 7 — D

Answer: Process the data with Spark on Amazon EMR. A sized managed cluster suits a heavy custom replay over a long history. EMR gives a managed Spark cluster sized for the processing job. Local study-map skill 1.5 (Merge and Transform Tooling), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. A function per record suits lightweight enrichment and filtering of a stream. Why the correct answer wins: A sized managed cluster suits a heavy custom replay over a long history.
- **B:** Incorrect for this question. Glue runs a managed Spark job against catalogued sources and writes the prepared output. Why the correct answer wins: A sized managed cluster suits a heavy custom replay over a long history.
- **C:** Incorrect for this question. DataBrew provides a visual recipe for profiling, cleaning and normalising columns. Why the correct answer wins: A sized managed cluster suits a heavy custom replay over a long history.
- **D:** Correct. EMR gives a managed Spark cluster sized for the processing job. In this case: A sized managed cluster suits a heavy custom replay over a long history.

### Question 8 — A

Answer: Transform the data with an AWS Glue ETL job. A managed transform job performs the merge without servers to run. Glue runs a managed Spark job against catalogued sources and writes the prepared output. Local study-map skill 1.5 (Merge and Transform Tooling), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Correct. Glue runs a managed Spark job against catalogued sources and writes the prepared output. In this case: A managed transform job performs the merge without servers to run.
- **B:** Incorrect for this question. Data Wrangler builds a reusable preparation flow and can export it into a pipeline. Why the correct answer wins: A managed transform job performs the merge without servers to run.
- **C:** Incorrect for this question. EMR gives a managed Spark cluster sized for the processing job. Why the correct answer wins: A managed transform job performs the merge without servers to run.
- **D:** Incorrect for this question. The catalog gives every engine the same table definitions and schemas. Why the correct answer wins: A managed transform job performs the merge without servers to run.

### Question 9 — B

Answer: Keep the point-in-time history in the Feature Store offline store. Point-in-time history returns the values current at the event. The offline store keeps timestamped values so training reads the values that existed at the time. Local study-map skill 1.6 (Feature Store), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. The catalog gives every engine the same table definitions and schemas. Why the correct answer wins: Point-in-time history returns the values current at the event.
- **B:** Correct. The offline store keeps timestamped values so training reads the values that existed at the time. In this case: Point-in-time history returns the values current at the event.
- **C:** Incorrect for this question. The online store serves the latest feature values for low-latency inference lookups. Why the correct answer wins: Point-in-time history returns the values current at the event.
- **D:** Incorrect for this question. A feature group gives one definition that both training and inference read. Why the correct answer wins: Point-in-time history returns the values current at the event.

### Question 10 — B

Answer: Standardise the numeric columns before training. Scaling puts columns on comparable ranges so none dominates. Local study-map skill 1.7 (Feature Engineering and Scaling), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Binning trades resolution for robustness to small variations inside a range. Why the correct answer wins: Scaling puts columns on comparable ranges so none dominates.
- **B:** Correct. In this case: Scaling puts columns on comparable ranges so none dominates.
- **C:** Incorrect for this question. A log transform compresses the long tail of a heavily skewed amount distribution. Why the correct answer wins: Scaling puts columns on comparable ranges so none dominates.
- **D:** Incorrect for this question. One-hot encoding turns unordered categories into separate binary columns. Why the correct answer wins: Scaling puts columns on comparable ranges so none dominates.

### Question 11 — A, B

Answers: Apply a log transform to the skewed amount column; Stratify the train, validation and test splits by label. A log transform compresses the skewed delay, and stratification keeps the rare label in each split. A log transform compresses the long tail of a heavily skewed amount distribution. Stratifying keeps the label proportions the same in every split. Local study-map skill 1.7 (Feature Engineering and Scaling), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Correct. A log transform compresses the long tail of a heavily skewed amount distribution. In this case: A log transform compresses the skewed delay, and stratification keeps the rare label in each split.
- **B:** Correct. Stratifying keeps the label proportions the same in every split. In this case: A log transform compresses the skewed delay, and stratification keeps the rare label in each split.
- **C:** Incorrect for this question. Shuffling stops the batch order from encoding an accidental pattern. Why the correct answer wins: A log transform compresses the skewed delay, and stratification keeps the rare label in each split.
- **D:** Incorrect for this question. Scaling puts the numeric columns on comparable ranges so no column dominates the fit. Why the correct answer wins: A log transform compresses the skewed delay, and stratification keeps the rare label in each split.
- **E:** Incorrect for this question. One-hot encoding turns unordered categories into separate binary columns. Why the correct answer wins: A log transform compresses the skewed delay, and stratification keeps the rare label in each split.

### Question 12 — C

Answer: Index the vectors in Amazon OpenSearch Service with k-NN search. A managed vector index supports filtered nearest-neighbour search at that scale. OpenSearch provides a managed vector index with filtered k-nearest-neighbour search. Local study-map skill 1.8 (Vector Stores and Embeddings), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Rebuilding the index per request cannot hold a large corpus or a latency target. Why the correct answer wins: A managed vector index supports filtered nearest-neighbour search at that scale.
- **B:** Incorrect for this question. pgvector keeps vectors beside relational rows the application already queries. Why the correct answer wins: A managed vector index supports filtered nearest-neighbour search at that scale.
- **C:** Correct. OpenSearch provides a managed vector index with filtered k-nearest-neighbour search. In this case: A managed vector index supports filtered nearest-neighbour search at that scale.
- **D:** Incorrect for this question. An S3-backed index suits a large, cost-sensitive corpus read less often. Why the correct answer wins: A managed vector index supports filtered nearest-neighbour search at that scale.

### Question 13 — B, D

Answers: Generate the embeddings with an Amazon Bedrock embedding model; Combine keyword and vector retrieval. An embedding model produces the vectors, and hybrid retrieval preserves the exact-number search. A managed embedding model converts text into vectors without hosts to run. Hybrid retrieval catches exact identifiers that a vector search alone can miss. Local study-map skill 1.8 (Vector Stores and Embeddings), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Domain tuning moves relevant passages closer to their questions in the vector space. Why the correct answer wins: An embedding model produces the vectors, and hybrid retrieval preserves the exact-number search.
- **B:** Correct. Hybrid retrieval catches exact identifiers that a vector search alone can miss. In this case: An embedding model produces the vectors, and hybrid retrieval preserves the exact-number search.
- **C:** Incorrect for this question. A reranker reorders the retrieved passages by relevance before they reach the model. Why the correct answer wins: An embedding model produces the vectors, and hybrid retrieval preserves the exact-number search.
- **D:** Correct. A managed embedding model converts text into vectors without hosts to run. In this case: An embedding model produces the vectors, and hybrid retrieval preserves the exact-number search.
- **E:** Incorrect for this question. OpenSearch provides a managed vector index with filtered k-nearest-neighbour search. Why the correct answer wins: An embedding model produces the vectors, and hybrid retrieval preserves the exact-number search.

### Question 14 — B

Answer: Chunk the documents on semantic boundaries such as headings. Splitting on section boundaries keeps one rule inside each chunk. Semantic chunks keep a coherent passage together, which improves what retrieval returns. Local study-map skill 1.9 (Text Pre-processing and Chunking), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Metadata lets retrieval filter by source or recency and lets answers cite the document. Why the correct answer wins: Splitting on section boundaries keeps one rule inside each chunk.
- **B:** Correct. Semantic chunks keep a coherent passage together, which improves what retrieval returns. In this case: Splitting on section boundaries keeps one rule inside each chunk.
- **C:** Incorrect for this question. Overlapping fixed chunks bound the context size and avoid cutting a sentence in half. Why the correct answer wins: Splitting on section boundaries keeps one rule inside each chunk.
- **D:** Incorrect for this question. Small child chunks match a query precisely while the parent supplies full context. Why the correct answer wins: Splitting on section boundaries keeps one rule inside each chunk.

### Question 15 — D, E

Answers: Evaluate AWS Glue Data Quality rules on the prepared table; Profile the incoming data and store the statistics as a baseline. Quality rules fail the job on invalid rows, and the stored profile becomes the comparison point. Data Quality rules fail the job on nulls, duplicates or range violations before training starts. A stored profile is what later drift comparison is measured against. Local study-map skill 1.10 (Data Quality Validation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. A schema check rejects records whose fields changed shape before they corrupt the set. Why the correct answer wins: Quality rules fail the job on invalid rows, and the stored profile becomes the comparison point.
- **B:** Incorrect for this question. DataBrew provides a visual recipe for profiling, cleaning and normalising columns. Why the correct answer wins: Quality rules fail the job on invalid rows, and the stored profile becomes the comparison point.
- **C:** Incorrect for this question. A lifecycle rule deletes the derived copies on a schedule, so storage does not grow forever. Why the correct answer wins: Quality rules fail the job on invalid rows, and the stored profile becomes the comparison point.
- **D:** Correct. Data Quality rules fail the job on nulls, duplicates or range violations before training starts. In this case: Quality rules fail the job on invalid rows, and the stored profile becomes the comparison point.
- **E:** Correct. A stored profile is what later drift comparison is measured against. In this case: Quality rules fail the job on invalid rows, and the stored profile becomes the comparison point.

### Question 16 — B

Answer: Use automated data labelling with a human review sample in Ground Truth. Active learning labels most photos automatically and sends uncertain ones to a specialist. Local study-map skill 1.11 (Labelling and Annotation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Ground Truth manages the labelling workforce, instructions and quality checks. Why the correct answer wins: Active learning labels most photos automatically and sends uncertain ones to a specialist.
- **B:** Correct. In this case: Active learning labels most photos automatically and sends uncertain ones to a specialist.
- **C:** Incorrect for this question. Duplicates that straddle splits leak the same row into training and evaluation. Why the correct answer wins: Active learning labels most photos automatically and sends uncertain ones to a specialist.
- **D:** Incorrect for this question. Removing the identifiers stops the model from learning or echoing personal data. Why the correct answer wins: Active learning labels most photos automatically and sends uncertain ones to a specialist.

### Question 17 — D

Answer: Rebalance the numeric, text and image assets in the set. A modality with far fewer examples is under-trained even when labels look balanced. Local study-map skill 1.12 (Bias Detection and Mitigation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Stratifying keeps the label proportions the same in every split. Why the correct answer wins: A modality with far fewer examples is under-trained even when labels look balanced.
- **B:** Incorrect for this question. Reweighting the loss changes what the model is optimised for without discarding data. Why the correct answer wins: A modality with far fewer examples is under-trained even when labels look balanced.
- **C:** Incorrect for this question. Clarify reports label and feature bias metrics so the imbalance is quantified first. Why the correct answer wins: A modality with far fewer examples is under-trained even when labels look balanced.
- **D:** Correct. In this case: A modality with far fewer examples is under-trained even when labels look balanced.

### Question 18 — D

Answer: Set class weights instead of resampling. Class weights raise the cost of a minority mistake without inventing rows. Local study-map skill 1.13 (Cleaning and Class Imbalance), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Synthetic minority sampling gives the learner more examples of the rare class. Why the correct answer wins: Class weights raise the cost of a minority mistake without inventing rows.
- **B:** Incorrect for this question. Dropping rows discards information and can bias the set towards complete records. Why the correct answer wins: Class weights raise the cost of a minority mistake without inventing rows.
- **C:** Incorrect for this question. Clipping caps the influence of a few extreme values without deleting the records. Why the correct answer wins: Class weights raise the cost of a minority mistake without inventing rows.
- **D:** Correct. In this case: Class weights raise the cost of a minority mistake without inventing rows.

### Question 19 — A

Answer: Forecast the series with the DeepAR algorithm. DeepAR returns probabilistic forecasts from related series. Local study-map skill 2.1 (Model and Algorithm Selection), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Correct. In this case: DeepAR returns probabilistic forecasts from related series.
- **B:** Incorrect for this question. Random Cut Forest assigns an anomaly score to each observation against the learned shape. Why the correct answer wins: DeepAR returns probabilistic forecasts from related series.
- **C:** Incorrect for this question. Gradient-boosted trees are the usual strong baseline for tabular data. Why the correct answer wins: DeepAR returns probabilistic forecasts from related series.
- **D:** Incorrect for this question. A linear model is cheap and interpretable when the relationship is close to linear. Why the correct answer wins: DeepAR returns probabilistic forecasts from related series.

### Question 20 — D

Answer: Train with the linear learner algorithm. A linear model states each feature contribution directly. A linear model is cheap and interpretable when the relationship is close to linear. Local study-map skill 2.1 (Model and Algorithm Selection), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. An ensemble reduces variance from any single model fit. Why the correct answer wins: A linear model states each feature contribution directly.
- **B:** Incorrect for this question. Gradient-boosted trees are the usual strong baseline for tabular data. Why the correct answer wins: A linear model states each feature contribution directly.
- **C:** Incorrect for this question. Nearest neighbours suit a small, low-dimensional similarity problem. Why the correct answer wins: A linear model states each feature contribution directly.
- **D:** Correct. A linear model is cheap and interpretable when the relationship is close to linear. In this case: A linear model states each feature contribution directly.

### Question 21 — A

Answer: Select an Amazon Nova foundation model in Amazon Bedrock. A smaller model matched to short answers keeps cost per call low. Nova models are reached through the Bedrock API with no infrastructure to host. Local study-map skill 2.2 (Foundation Model Selection), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Correct. Nova models are reached through the Bedrock API with no infrastructure to host. In this case: A smaller model matched to short answers keeps cost per call low.
- **B:** Incorrect for this question. Self-hosting gives full control but puts model operations on your team. Why the correct answer wins: A smaller model matched to short answers keeps cost per call low.
- **C:** Incorrect for this question. Claude models are available through Bedrock for long-context reasoning tasks. Why the correct answer wins: A smaller model matched to short answers keeps cost per call low.
- **D:** Incorrect for this question. A Titan embedding model turns text into vectors for search and clustering. Why the correct answer wins: A smaller model matched to short answers keeps cost per call low.

### Question 22 — D

Answer: Select a Titan embedding model in Amazon Bedrock. An embedding model produces the vectors through a managed API. A Titan embedding model turns text into vectors for search and clustering. Local study-map skill 2.2 (Foundation Model Selection), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. Self-hosting gives full control but puts model operations on your team. Why the correct answer wins: An embedding model produces the vectors through a managed API.
- **B:** Incorrect for this question. Claude models are available through Bedrock for long-context reasoning tasks. Why the correct answer wins: An embedding model produces the vectors through a managed API.
- **C:** Incorrect for this question. Nova models are reached through the Bedrock API with no infrastructure to host. Why the correct answer wins: An embedding model produces the vectors through a managed API.
- **D:** Correct. A Titan embedding model turns text into vectors for search and clustering. In this case: An embedding model produces the vectors through a managed API.

### Question 23 — B

Answer: Distil the large model into a smaller student model. Distillation transfers the large model behaviour into a cheaper one. Local study-map skill 2.3 (Fine-tuning and Customisation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. Continued pre-training adapts the model to domain vocabulary before task tuning. Why the correct answer wins: Distillation transfers the large model behaviour into a cheaper one.
- **B:** Correct. In this case: Distillation transfers the large model behaviour into a cheaper one.
- **C:** Incorrect for this question. Adapters train a small number of parameters, which lowers cost and the risk of forgetting. Why the correct answer wins: Distillation transfers the large model behaviour into a cheaper one.
- **D:** Incorrect for this question. Full fine-tuning updates every weight and needs more data, memory and care. Why the correct answer wins: Distillation transfers the large model behaviour into a cheaper one.

### Question 24 — B, D

Answers: Fine-tune with parameter-efficient adapters such as LoRA; Mix replay samples from the original distribution into fine-tuning. Adapters teach the codes cheaply, and replay samples preserve the earlier behaviour. Adapters train a small number of parameters, which lowers cost and the risk of forgetting. Replay samples keep the earlier behaviour from being overwritten by the narrow new data. Local study-map skill 2.3 (Fine-tuning and Customisation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. Continued pre-training adapts the model to domain vocabulary before task tuning. Why the correct answer wins: Adapters teach the codes cheaply, and replay samples preserve the earlier behaviour.
- **B:** Correct. Adapters train a small number of parameters, which lowers cost and the risk of forgetting. In this case: Adapters teach the codes cheaply, and replay samples preserve the earlier behaviour.
- **C:** Incorrect for this question. A well-structured prompt often meets the requirement without a training run. Why the correct answer wins: Adapters teach the codes cheaply, and replay samples preserve the earlier behaviour.
- **D:** Correct. Replay samples keep the earlier behaviour from being overwritten by the narrow new data. In this case: Adapters teach the codes cheaply, and replay samples preserve the earlier behaviour.
- **E:** Incorrect for this question. Full fine-tuning updates every weight and needs more data, memory and care. Why the correct answer wins: Adapters teach the codes cheaply, and replay samples preserve the earlier behaviour.

### Question 25 — A

Answer: Index parent sections and retrieve their child chunks. Small children match precisely while the parent clause supplies context. Local study-map skill 2.4 (RAG Architecture Patterns), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Correct. In this case: Small children match precisely while the parent clause supplies context.
- **B:** Incorrect for this question. Overlapping fixed chunks bound the context size and avoid cutting a sentence in half. Why the correct answer wins: Small children match precisely while the parent clause supplies context.
- **C:** Incorrect for this question. Metadata lets retrieval filter by source or recency and lets answers cite the document. Why the correct answer wins: Small children match precisely while the parent clause supplies context.
- **D:** Incorrect for this question. Semantic chunks keep a coherent passage together, which improves what retrieval returns. Why the correct answer wins: Small children match precisely while the parent clause supplies context.

### Question 26 — A

Answer: Extract the form fields with Amazon Textract. Form extraction turns photographed documents into structured fields. Textract reads forms and tables into structured fields without a custom model. Local study-map skill 2.5 (Managed AI Services), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Correct. Textract reads forms and tables into structured fields without a custom model. In this case: Form extraction turns photographed documents into structured fields.
- **B:** Incorrect for this question. Transcribe converts speech to text and can label speakers. Why the correct answer wins: Form extraction turns photographed documents into structured fields.
- **C:** Incorrect for this question. Rekognition provides managed image and video analysis for common labels and text. Why the correct answer wins: Form extraction turns photographed documents into structured fields.
- **D:** Incorrect for this question. Comprehend provides managed entity, key-phrase and sentiment analysis. Why the correct answer wins: Form extraction turns photographed documents into structured fields.

### Question 27 — B

Answer: Package the training code in script mode with a supported framework. Script mode runs your own script inside a managed container. Local study-map skill 2.6 (Built-in Algorithms and Script Mode), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. JumpStart supplies a pre-trained model and its deployment template. Why the correct answer wins: Script mode runs your own script inside a managed container.
- **B:** Correct. In this case: Script mode runs your own script inside a managed container.
- **C:** Incorrect for this question. Gradient-boosted trees are the usual strong baseline for tabular data. Why the correct answer wins: Script mode runs your own script inside a managed container.
- **D:** Incorrect for this question. A custom image is needed only when the managed framework images cannot carry the dependencies. Why the correct answer wins: Script mode runs your own script inside a managed container.

### Question 28 — A

Answer: Enable early stopping on the validation metric. Early stopping ends a trial once validation stops improving. Local study-map skill 2.7 (Hyperparameter Tuning), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Correct. In this case: Early stopping ends a trial once validation stops improving.
- **B:** Incorrect for this question. Bayesian search spends the trial budget on the region of the space that looks promising. Why the correct answer wins: Early stopping ends a trial once validation stops improving.
- **C:** Incorrect for this question. Automatic model tuning runs the search over a stated objective metric. Why the correct answer wins: Early stopping ends a trial once validation stops improving.
- **D:** Incorrect for this question. The search optimises exactly the metric it is given, so the metric must match the goal. Why the correct answer wins: Early stopping ends a trial once validation stops improving.

### Question 29 — A, B

Answers: Define the tuning objective on the validation metric that matters; Use Bayesian search over a defined objective metric. The objective defines what is optimised, and Bayesian search uses earlier results. The search optimises exactly the metric it is given, so the metric must match the goal. Bayesian search spends the trial budget on the region of the space that looks promising. Local study-map skill 2.7 (Hyperparameter Tuning), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Correct. The search optimises exactly the metric it is given, so the metric must match the goal. In this case: The objective defines what is optimised, and Bayesian search uses earlier results.
- **B:** Correct. Bayesian search spends the trial budget on the region of the space that looks promising. In this case: The objective defines what is optimised, and Bayesian search uses earlier results.
- **C:** Incorrect for this question. A manual grid costs a job per combination and adapts to nothing. Why the correct answer wins: The objective defines what is optimised, and Bayesian search uses earlier results.
- **D:** Incorrect for this question. Random search is a cheap baseline but ignores what earlier trials learned. Why the correct answer wins: The objective defines what is optimised, and Bayesian search uses earlier results.
- **E:** Incorrect for this question. Early stopping ends a trial once the validation metric stops improving. Why the correct answer wins: The objective defines what is optimised, and Bayesian search uses earlier results.

### Question 30 — C, E

Answers: Checkpoint to Amazon S3 so an interrupted job resumes; Keep a managed warm pool for the training cluster. Checkpoints let a reclaimed run resume, and a warm pool removes provisioning delay. Checkpoints let a reclaimed instance continue from the last saved state. A warm pool removes the provisioning delay between consecutive training jobs. Local study-map skill 2.8 (Training Efficiency and Regularisation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. Spot capacity lowers the cost of a job that can checkpoint and resume. Why the correct answer wins: Checkpoints let a reclaimed run resume, and a warm pool removes provisioning delay.
- **B:** Incorrect for this question. Model parallelism is needed when the model weights do not fit on a single device. Why the correct answer wins: Checkpoints let a reclaimed run resume, and a warm pool removes provisioning delay.
- **C:** Correct. A warm pool removes the provisioning delay between consecutive training jobs. In this case: Checkpoints let a reclaimed run resume, and a warm pool removes provisioning delay.
- **D:** Incorrect for this question. Data parallelism shortens wall-clock training when the model still fits on one device. Why the correct answer wins: Checkpoints let a reclaimed run resume, and a warm pool removes provisioning delay.
- **E:** Correct. Checkpoints let a reclaimed instance continue from the last saved state. In this case: Checkpoints let a reclaimed run resume, and a warm pool removes provisioning delay.

### Question 31 — C

Answer: Inspect the confusion matrix on the minority class. The matrix exposes which class the model confuses. Local study-map skill 2.9 (Classic Model Evaluation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. RMSE expresses the typical error in the target units and penalises large misses. Why the correct answer wins: The matrix exposes which class the model confuses.
- **B:** Incorrect for this question. ROC-AUC measures how well the scores separate the classes across thresholds. Why the correct answer wins: The matrix exposes which class the model confuses.
- **C:** Correct. In this case: The matrix exposes which class the model confuses.
- **D:** Incorrect for this question. F1 balances precision and recall, which suits an uneven class mix. Why the correct answer wins: The matrix exposes which class the model confuses.

### Question 32 — C, D

Answers: Report ROC-AUC for the ranking task; Report RMSE for the regression. AUC compares the ranking, and RMSE reports the error in hours. ROC-AUC measures how well the scores separate the classes across thresholds. RMSE expresses the typical error in the target units and penalises large misses. Local study-map skill 2.9 (Classic Model Evaluation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. Accuracy on a rare class is dominated by the majority and hides missed positives. Why the correct answer wins: AUC compares the ranking, and RMSE reports the error in hours.
- **B:** Incorrect for this question. F1 balances precision and recall, which suits an uneven class mix. Why the correct answer wins: AUC compares the ranking, and RMSE reports the error in hours.
- **C:** Correct. ROC-AUC measures how well the scores separate the classes across thresholds. In this case: AUC compares the ranking, and RMSE reports the error in hours.
- **D:** Correct. RMSE expresses the typical error in the target units and penalises large misses. In this case: AUC compares the ranking, and RMSE reports the error in hours.
- **E:** Incorrect for this question. BLEU measures n-gram overlap with the reference summaries. Why the correct answer wins: AUC compares the ranking, and RMSE reports the error in hours.

### Question 33 — A

Answer: Score the answers with BERTScore. Contextual embedding comparison credits a paraphrase. BERTScore compares contextual embeddings, so a paraphrase can still score well. Local study-map skill 2.10 (GenAI and NLP Evaluation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Correct. BERTScore compares contextual embeddings, so a paraphrase can still score well. In this case: Contextual embedding comparison credits a paraphrase.
- **B:** Incorrect for this question. ROUGE measures recall of reference n-grams, which suits summarisation. Why the correct answer wins: Contextual embedding comparison credits a paraphrase.
- **C:** Incorrect for this question. BLEU measures n-gram overlap with the reference summaries. Why the correct answer wins: Contextual embedding comparison credits a paraphrase.
- **D:** Incorrect for this question. RMSE expresses the typical error in the target units and penalises large misses. Why the correct answer wins: Contextual embedding comparison credits a paraphrase.

### Question 34 — C

Answer: Pin the data snapshot, code version and hyperparameters for each run. Pinned inputs are what make a run reproducible. Local study-map skill 2.11 (Experiment Tracking and Baselines), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. Bedrock evaluation scores model output against built-in or custom metrics. Why the correct answer wins: Pinned inputs are what make a run reproducible.
- **B:** Incorrect for this question. The registry holds model versions and their approval status for deployment. Why the correct answer wins: Pinned inputs are what make a run reproducible.
- **C:** Correct. In this case: Pinned inputs are what make a run reproducible.
- **D:** Incorrect for this question. Run logging keeps parameters, metrics and artefacts comparable across experiments. Why the correct answer wins: Pinned inputs are what make a run reproducible.

### Question 35 — B

Answer: Use asynchronous inference with results written to Amazon S3. Asynchronous inference queues long requests and delivers results through S3. Local study-map skill 3.1 (Inference Strategy), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. Serverless inference scales to zero and suits intermittent, short requests. Why the correct answer wins: Asynchronous inference queues long requests and delivers results through S3.
- **B:** Correct. In this case: Asynchronous inference queues long requests and delivers results through S3.
- **C:** Incorrect for this question. A real-time endpoint answers synchronous requests with a persistent host behind it. Why the correct answer wins: Asynchronous inference queues long requests and delivers results through S3.
- **D:** Incorrect for this question. Batch transform scores a stored dataset with no endpoint to keep running. Why the correct answer wins: Asynchronous inference queues long requests and delivers results through S3.

### Question 36 — A, D

Answers: Run a batch transform job over the stored records; Deploy a real-time SageMaker AI endpoint. Batch transform covers the nightly sweep, and a real-time endpoint answers the console. Batch transform scores a stored dataset with no endpoint to keep running. A real-time endpoint answers synchronous requests with a persistent host behind it. Local study-map skill 3.1 (Inference Strategy), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Correct. Batch transform scores a stored dataset with no endpoint to keep running. In this case: Batch transform covers the nightly sweep, and a real-time endpoint answers the console.
- **B:** Incorrect for this question. Serverless inference scales to zero and suits intermittent, short requests. Why the correct answer wins: Batch transform covers the nightly sweep, and a real-time endpoint answers the console.
- **C:** Incorrect for this question. A multi-model endpoint loads models on demand from S3 behind shared hosting capacity. Why the correct answer wins: Batch transform covers the nightly sweep, and a real-time endpoint answers the console.
- **D:** Correct. A real-time endpoint answers synchronous requests with a persistent host behind it. In this case: Batch transform covers the nightly sweep, and a real-time endpoint answers the console.
- **E:** Incorrect for this question. Asynchronous inference queues large or long requests and returns results through S3. Why the correct answer wins: Batch transform covers the nightly sweep, and a real-time endpoint answers the console.

### Question 37 — D

Answer: Run several containers behind one endpoint. A multi-container endpoint chains the two containers behind one call. A multi-container endpoint chains containers such as preprocessing and inference. Local study-map skill 3.2 (Endpoint Architecture), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. A real-time endpoint answers synchronous requests with a persistent host behind it. Why the correct answer wins: A multi-container endpoint chains the two containers behind one call.
- **B:** Incorrect for this question. A multi-model endpoint loads models on demand from S3 behind shared hosting capacity. Why the correct answer wins: A multi-container endpoint chains the two containers behind one call.
- **C:** Incorrect for this question. Batch transform scores a stored dataset with no endpoint to keep running. Why the correct answer wins: A multi-container endpoint chains the two containers behind one call.
- **D:** Correct. A multi-container endpoint chains containers such as preprocessing and inference. In this case: A multi-container endpoint chains the two containers behind one call.

### Question 38 — C

Answer: Import the fine-tuned weights with Bedrock custom model import. Importing the custom model serves those weights on Bedrock infrastructure. Local study-map skill 3.3 (Foundation Model Deployment), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. Provisioned throughput reserves model capacity for predictable, high-volume traffic. Why the correct answer wins: Importing the custom model serves those weights on Bedrock infrastructure.
- **B:** Incorrect for this question. JumpStart supplies a pre-trained model and its deployment template. Why the correct answer wins: Importing the custom model serves those weights on Bedrock infrastructure.
- **C:** Correct. In this case: Importing the custom model serves those weights on Bedrock infrastructure.
- **D:** Incorrect for this question. Self-hosting gives full control but puts model operations on your team. Why the correct answer wins: Importing the custom model serves those weights on Bedrock infrastructure.

### Question 39 — B

Answer: Buy provisioned throughput for the Bedrock model. Reserved capacity removes throttling at a steady, predictable volume. Provisioned throughput reserves model capacity for predictable, high-volume traffic. Local study-map skill 3.3 (Foundation Model Deployment), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. On-demand calls need no reservation and suit bursty, lower-volume traffic. Why the correct answer wins: Reserved capacity removes throttling at a steady, predictable volume.
- **B:** Correct. Provisioned throughput reserves model capacity for predictable, high-volume traffic. In this case: Reserved capacity removes throttling at a steady, predictable volume.
- **C:** Incorrect for this question. Inference Recommender benchmarks instance types against the latency and throughput target. Why the correct answer wins: Reserved capacity removes throttling at a steady, predictable volume.
- **D:** Incorrect for this question. The reservation only pays off when the steady volume exceeds the break-even point. Why the correct answer wins: Reserved capacity removes throttling at a steady, predictable volume.

### Question 40 — C

Answer: Persist the agent session state between turns. Persisted session state carries context between turns. Persisted session state keeps multi-turn context without resending the whole history. Local study-map skill 3.4 (Agents and Retrieval Runtime), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. A sync re-indexes changed documents so retrieval does not serve stale passages. Why the correct answer wins: Persisted session state carries context between turns.
- **B:** Incorrect for this question. Prompt Management versions templates so a prompt change is reviewable and reversible. Why the correct answer wins: Persisted session state carries context between turns.
- **C:** Correct. Persisted session state keeps multi-turn context without resending the whole history. In this case: Persisted session state carries context between turns.
- **D:** Incorrect for this question. An agent needs its tools, knowledge base and instructions deployed together as one unit. Why the correct answer wins: Persisted session state carries context between turns.

### Question 41 — C

Answer: Run the container on Amazon EKS. A managed Kubernetes cluster keeps the existing manifests and tooling. EKS runs the container under Kubernetes for teams already standardised on it. Local study-map skill 3.5 (Containers and Compute Provisioning), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. AWS Batch queues the job and provisions capacity for the run. Why the correct answer wins: A managed Kubernetes cluster keeps the existing manifests and tooling.
- **B:** Incorrect for this question. Lambda suits a small model and spiky traffic but not a large model resident in memory. Why the correct answer wins: A managed Kubernetes cluster keeps the existing manifests and tooling.
- **C:** Correct. EKS runs the container under Kubernetes for teams already standardised on it. In this case: A managed Kubernetes cluster keeps the existing manifests and tooling.
- **D:** Incorrect for this question. ECS schedules the container on managed cluster capacity. Why the correct answer wins: A managed Kubernetes cluster keeps the existing manifests and tooling.

### Question 42 — B

Answer: Scale the endpoint to zero outside business hours. Scaling to zero outside those hours removes the idle cost. A scale-to-zero policy removes the idle cost when nothing calls the endpoint. Local study-map skill 3.6 (Autoscaling and Concurrency), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. Target tracking holds a metric such as invocations per instance near a chosen value. Why the correct answer wins: Scaling to zero outside those hours removes the idle cost.
- **B:** Correct. A scale-to-zero policy removes the idle cost when nothing calls the endpoint. In this case: Scaling to zero outside those hours removes the idle cost.
- **C:** Incorrect for this question. A warm pool removes the provisioning delay between consecutive training jobs. Why the correct answer wins: Scaling to zero outside those hours removes the idle cost.
- **D:** Incorrect for this question. Step scaling adds capacity in bands as the alarm breaches, which suits sharp bursts. Why the correct answer wins: Scaling to zero outside those hours removes the idle cost.

### Question 43 — A, D

Answers: Scale on GPU utilisation rather than invocation count; Keep provisioned concurrency ready for the burst window. Accelerator utilisation reflects the bottleneck, and warm capacity covers the rush. GPU utilisation reflects the real bottleneck when each request is expensive. Provisioned concurrency pre-warms capacity so the burst does not meet a cold start. Local study-map skill 3.6 (Autoscaling and Concurrency), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Correct. GPU utilisation reflects the real bottleneck when each request is expensive. In this case: Accelerator utilisation reflects the bottleneck, and warm capacity covers the rush.
- **B:** Incorrect for this question. Step scaling adds capacity in bands as the alarm breaches, which suits sharp bursts. Why the correct answer wins: Accelerator utilisation reflects the bottleneck, and warm capacity covers the rush.
- **C:** Incorrect for this question. Target tracking holds a metric such as invocations per instance near a chosen value. Why the correct answer wins: Accelerator utilisation reflects the bottleneck, and warm capacity covers the rush.
- **D:** Correct. Provisioned concurrency pre-warms capacity so the burst does not meet a cold start. In this case: Accelerator utilisation reflects the bottleneck, and warm capacity covers the rush.
- **E:** Incorrect for this question. A scale-to-zero policy removes the idle cost when nothing calls the endpoint. Why the correct answer wins: Accelerator utilisation reflects the bottleneck, and warm capacity covers the rush.

### Question 44 — C

Answer: Place the endpoint and model containers in private subnets. Private subnets remove the internet path while a private endpoint keeps S3 traffic inside. Private subnets remove the inbound internet path to the model hosts. Local study-map skill 3.7 (VPC Networking for Endpoints), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. A private endpoint keeps the service traffic inside the VPC without a NAT gateway. Why the correct answer wins: Private subnets remove the internet path while a private endpoint keeps S3 traffic inside.
- **B:** Incorrect for this question. A NAT gateway gives private hosts outbound access without accepting inbound traffic. Why the correct answer wins: Private subnets remove the internet path while a private endpoint keeps S3 traffic inside.
- **C:** Correct. Private subnets remove the inbound internet path to the model hosts. In this case: Private subnets remove the internet path while a private endpoint keeps S3 traffic inside.
- **D:** Incorrect for this question. An open ingress rule exposes the model to anything that can reach the VPC. Why the correct answer wins: Private subnets remove the internet path while a private endpoint keeps S3 traffic inside.

### Question 45 — A, C

Answers: Build and test the model image with AWS CodeBuild; Connect the external repository with AWS CodeConnections. A connection reads the external repository, and a build service runs the build and tests. CodeBuild runs the build and the automated tests in a clean managed environment. CodeConnections lets the pipeline read a repository hosted elsewhere. Local study-map skill 3.8 (CI/CD Pipelines), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Correct. CodeConnections lets the pipeline read a repository hosted elsewhere. In this case: A connection reads the external repository, and a build service runs the build and tests.
- **B:** Incorrect for this question. CodePipeline sequences the build, test and deploy stages and records each outcome. Why the correct answer wins: A connection reads the external repository, and a build service runs the build and tests.
- **C:** Correct. CodeBuild runs the build and the automated tests in a clean managed environment. In this case: A connection reads the external repository, and a build service runs the build and tests.
- **D:** Incorrect for this question. CodeCommit is the managed Git repository the pipeline reads from. Why the correct answer wins: A connection reads the external repository, and a build service runs the build and tests.
- **E:** Incorrect for this question. CodeDeploy performs the traffic shift and can roll back on an alarm. Why the correct answer wins: A connection reads the external repository, and a build service runs the build and tests.

### Question 46 — D

Answer: Orchestrate the release with AWS CodePipeline. A pipeline sequences the stages and records each outcome. CodePipeline sequences the build, test and deploy stages and records each outcome. Local study-map skill 3.8 (CI/CD Pipelines), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. A quality gate blocks a release whose measured metric is below the agreed bar. Why the correct answer wins: A pipeline sequences the stages and records each outcome.
- **B:** Incorrect for this question. CodeBuild runs the build and the automated tests in a clean managed environment. Why the correct answer wins: A pipeline sequences the stages and records each outcome.
- **C:** Incorrect for this question. CodeDeploy performs the traffic shift and can roll back on an alarm. Why the correct answer wins: A pipeline sequences the stages and records each outcome.
- **D:** Correct. CodePipeline sequences the build, test and deploy stages and records each outcome. In this case: A pipeline sequences the stages and records each outcome.

### Question 47 — D

Answer: Register the approved version in the SageMaker Model Registry. A registry stores versions with their approval status. The registry holds model versions and their approval status for deployment. Local study-map skill 3.9 (Model Registry and Versioning), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. Run logging keeps parameters, metrics and artefacts comparable across experiments. Why the correct answer wins: A registry stores versions with their approval status.
- **B:** Incorrect for this question. Prompt Management versions templates so a prompt change is reviewable and reversible. Why the correct answer wins: A registry stores versions with their approval status.
- **C:** Incorrect for this question. CodeCommit is the managed Git repository the pipeline reads from. Why the correct answer wins: A registry stores versions with their approval status.
- **D:** Correct. The registry holds model versions and their approval status for deployment. In this case: A registry stores versions with their approval status.

### Question 48 — C

Answer: Replace the production version in a single switch. A single global switch leaves no share of traffic on the proven version. A single switch gives a bad model the whole traffic share at once. Local study-map skill 3.10 (Deployment Strategy and Rollback), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. A canary release limits the blast radius of a bad model to the canary share. Why the correct answer wins: A single global switch leaves no share of traffic on the proven version.
- **B:** Incorrect for this question. A linear shift moves traffic gradually while the metrics are watched. Why the correct answer wins: A single global switch leaves no share of traffic on the proven version.
- **C:** Correct. A single switch gives a bad model the whole traffic share at once. In this case: A single global switch leaves no share of traffic on the proven version.
- **D:** Incorrect for this question. Blue/green keeps the previous version ready for an immediate switch back. Why the correct answer wins: A single global switch leaves no share of traffic on the proven version.

### Question 49 — B, D

Answers: Send a small share of traffic to the new version first; Mirror traffic to the new model without serving its answers. Mirroring collects the comparison, and a canary limits the first exposure. A canary release limits the blast radius of a bad model to the canary share. Mirroring collects comparison data with no user impact. Local study-map skill 3.10 (Deployment Strategy and Rollback), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. Blue/green keeps the previous version ready for an immediate switch back. Why the correct answer wins: Mirroring collects the comparison, and a canary limits the first exposure.
- **B:** Correct. A canary release limits the blast radius of a bad model to the canary share. In this case: Mirroring collects the comparison, and a canary limits the first exposure.
- **C:** Incorrect for this question. A single switch gives a bad model the whole traffic share at once. Why the correct answer wins: Mirroring collects the comparison, and a canary limits the first exposure.
- **D:** Correct. Mirroring collects comparison data with no user impact. In this case: Mirroring collects the comparison, and a canary limits the first exposure.
- **E:** Incorrect for this question. A linear shift moves traffic gradually while the metrics are watched. Why the correct answer wins: Mirroring collects the comparison, and a canary limits the first exposure.

### Question 50 — A

Answer: Orchestrate the steps with AWS Step Functions. A state machine coordinates the wait, the steps and the branching. Step Functions coordinates long-running steps and service calls with retries and branching. Local study-map skill 3.11 (Orchestration and Retraining), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Correct. Step Functions coordinates long-running steps and service calls with retries and branching. In this case: A state machine coordinates the wait, the steps and the branching.
- **B:** Incorrect for this question. CodePipeline sequences the build, test and deploy stages and records each outcome. Why the correct answer wins: A state machine coordinates the wait, the steps and the branching.
- **C:** Incorrect for this question. A SageMaker pipeline expresses the processing, training and registration steps as one DAG. Why the correct answer wins: A state machine coordinates the wait, the steps and the branching.
- **D:** Incorrect for this question. A schedule starts the pipeline on a fixed cadence without an external cron host. Why the correct answer wins: A state machine coordinates the wait, the steps and the branching.

### Question 51 — A

Answer: Enable feature attribution drift monitoring. Attribution drift reveals a changed dependence on features. Attribution drift shows that the model now relies on different features than it did. Local study-map skill 4.1 (Drift and Model Monitoring), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Correct. Attribution drift shows that the model now relies on different features than it did. In this case: Attribution drift reveals a changed dependence on features.
- **B:** Incorrect for this question. A bias monitor watches whether the outcome distribution shifts for a protected group. Why the correct answer wins: Attribution drift reveals a changed dependence on features.
- **C:** Incorrect for this question. A data drift monitor compares the live request distribution against the training baseline. Why the correct answer wins: Attribution drift reveals a changed dependence on features.
- **D:** Incorrect for this question. A quality monitor scores live predictions once the true labels arrive. Why the correct answer wins: Attribution drift reveals a changed dependence on features.

### Question 52 — B, E

Answers: Enable a model quality monitor with ground-truth labels; Enable a bias drift monitor. A quality monitor scores the delayed labels, and a bias monitor watches the depot cohort. A quality monitor scores live predictions once the true labels arrive. A bias monitor watches whether the outcome distribution shifts for a protected group. Local study-map skill 4.1 (Drift and Model Monitoring), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. Attribution drift shows that the model now relies on different features than it did. Why the correct answer wins: A quality monitor scores the delayed labels, and a bias monitor watches the depot cohort.
- **B:** Correct. A quality monitor scores live predictions once the true labels arrive. In this case: A quality monitor scores the delayed labels, and a bias monitor watches the depot cohort.
- **C:** Incorrect for this question. An alarm on the endpoint metrics pages someone when the service degrades. Why the correct answer wins: A quality monitor scores the delayed labels, and a bias monitor watches the depot cohort.
- **D:** Incorrect for this question. A data drift monitor compares the live request distribution against the training baseline. Why the correct answer wins: A quality monitor scores the delayed labels, and a bias monitor watches the depot cohort.
- **E:** Correct. A bias monitor watches whether the outcome distribution shifts for a protected group. In this case: A quality monitor scores the delayed labels, and a bias monitor watches the depot cohort.

### Question 53 — A

Answer: Trace the pipeline service calls with AWS X-Ray. Tracing shows where a request spends its time across services. Local study-map skill 4.2 (Metrics and Dashboards), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Correct. In this case: Tracing shows where a request spends its time across services.
- **B:** Incorrect for this question. Logs Insights filters and aggregates the request logs to find the failing pattern. Why the correct answer wins: Tracing shows where a request spends its time across services.
- **C:** Incorrect for this question. A dashboard puts the operating metrics in one view for the team. Why the correct answer wins: Tracing shows where a request spends its time across services.
- **D:** Incorrect for this question. Config records how each resource was configured and evaluates it against rules. Why the correct answer wins: Tracing shows where a request spends its time across services.

### Question 54 — C

Answer: Build a CloudWatch dashboard for the pipeline metrics. A dashboard presents the operating metrics in one view. Local study-map skill 4.2 (Metrics and Dashboards), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. Logs Insights filters and aggregates the request logs to find the failing pattern. Why the correct answer wins: A dashboard presents the operating metrics in one view.
- **B:** Incorrect for this question. X-Ray shows where a request spends its time across the services it touches. Why the correct answer wins: A dashboard presents the operating metrics in one view.
- **C:** Correct. In this case: A dashboard presents the operating metrics in one view.
- **D:** Incorrect for this question. An alarm on the endpoint metrics pages someone when the service degrades. Why the correct answer wins: A dashboard presents the operating metrics in one view.

### Question 55 — D

Answer: Trace agent tool calls with Bedrock AgentCore Observability. Agent tracing records every tool call and where it stalled. Agent tracing shows which tool call failed or stalled inside a multi-step task. Local study-map skill 4.3 (GenAI Observability), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. An alarm on the endpoint metrics pages someone when the service degrades. Why the correct answer wins: Agent tracing records every tool call and where it stalled.
- **B:** Incorrect for this question. X-Ray shows where a request spends its time across the services it touches. Why the correct answer wins: Agent tracing records every tool call and where it stalled.
- **C:** Incorrect for this question. Generative AI observability records prompts, token counts and latency per model call. Why the correct answer wins: Agent tracing records every tool call and where it stalled.
- **D:** Correct. Agent tracing shows which tool call failed or stalled inside a multi-step task. In this case: Agent tracing records every tool call and where it stalled.

### Question 56 — D

Answer: Cover the steady inference load with a Savings Plan. A plan discounts a predictable hourly spend. Local study-map skill 4.4 (Cost Optimisation and Purchasing), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. Matching the family to the measured workload avoids paying for capacity the model cannot use. Why the correct answer wins: A plan discounts a predictable hourly spend.
- **B:** Incorrect for this question. Batch scoring removes the idle endpoint that an always-on deployment would keep. Why the correct answer wins: A plan discounts a predictable hourly spend.
- **C:** Incorrect for this question. Cost Explorer groups the bill by service and by tag so the expensive resource is visible. Why the correct answer wins: A plan discounts a predictable hourly spend.
- **D:** Correct. In this case: A plan discounts a predictable hourly spend.

### Question 57 — B, D

Answers: Right-size the instance family against the measured latency; Move the offline scoring to batch transform. Right-sizing matches the workload, and batch scoring removes the idle endpoint. Matching the family to the measured workload avoids paying for capacity the model cannot use. Batch scoring removes the idle endpoint that an always-on deployment would keep. Local study-map skill 4.4 (Cost Optimisation and Purchasing), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. Sizing every request for the hardest case spends latency and money on easy requests. Why the correct answer wins: Right-sizing matches the workload, and batch scoring removes the idle endpoint.
- **B:** Correct. Batch scoring removes the idle endpoint that an always-on deployment would keep. In this case: Right-sizing matches the workload, and batch scoring removes the idle endpoint.
- **C:** Incorrect for this question. A scale-to-zero policy removes the idle cost when nothing calls the endpoint. Why the correct answer wins: Right-sizing matches the workload, and batch scoring removes the idle endpoint.
- **D:** Correct. Matching the family to the measured workload avoids paying for capacity the model cannot use. In this case: Right-sizing matches the workload, and batch scoring removes the idle endpoint.
- **E:** Incorrect for this question. A Savings Plan discounts a predictable hourly spend on eligible compute. Why the correct answer wins: Right-sizing matches the workload, and batch scoring removes the idle endpoint.

### Question 58 — B

Answer: Cache embeddings for documents that have not changed. Caching embeddings skips the work for documents that did not change. Re-embedding an unchanged document is wasted spend on every refresh. Local study-map skill 4.5 (Inference Cost and Token Usage), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. Routing easy requests to a cheaper model keeps the large model for hard cases. Why the correct answer wins: Caching embeddings skips the work for documents that did not change.
- **B:** Correct. Re-embedding an unchanged document is wasted spend on every refresh. In this case: Caching embeddings skips the work for documents that did not change.
- **C:** Incorrect for this question. Sending fewer retrieved tokens lowers both cost and latency on every call. Why the correct answer wins: Caching embeddings skips the work for documents that did not change.
- **D:** Incorrect for this question. Output tokens dominate generation cost, so a cap bounds the spend per call. Why the correct answer wins: Caching embeddings skips the work for documents that did not change.

### Question 59 — D

Answer: Route routine requests to a smaller model. Routing trivial questions to a smaller model keeps the large one for hard cases. Routing easy requests to a cheaper model keeps the large model for hard cases. Local study-map skill 4.5 (Inference Cost and Token Usage), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. Re-embedding an unchanged document is wasted spend on every refresh. Why the correct answer wins: Routing trivial questions to a smaller model keeps the large one for hard cases.
- **B:** Incorrect for this question. Sending fewer retrieved tokens lowers both cost and latency on every call. Why the correct answer wins: Routing trivial questions to a smaller model keeps the large one for hard cases.
- **C:** Incorrect for this question. Output tokens dominate generation cost, so a cap bounds the spend per call. Why the correct answer wins: Routing trivial questions to a smaller model keeps the large one for hard cases.
- **D:** Correct. Routing easy requests to a cheaper model keeps the large model for hard cases. In this case: Routing trivial questions to a smaller model keeps the large one for hard cases.

### Question 60 — C, E

Answers: Give the training job a scoped IAM execution role; Attach a policy scoped to the one bucket prefix. An execution role gives the job an identity, and the prefix policy scopes its reads. An execution role grants the job only the permissions its inputs and outputs need. Scoping to the prefix stops a compromised job from reaching the rest of the data lake. Local study-map skill 4.6 (IAM and Credentials), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. A long-lived key keeps working after the project ends unless someone retires it. Why the correct answer wins: An execution role gives the job an identity, and the prefix policy scopes its reads.
- **B:** Incorrect for this question. A group policy keeps the shared permission set in one reviewable place. Why the correct answer wins: An execution role gives the job an identity, and the prefix policy scopes its reads.
- **C:** Correct. Scoping to the prefix stops a compromised job from reaching the rest of the data lake. In this case: An execution role gives the job an identity, and the prefix policy scopes its reads.
- **D:** Incorrect for this question. The root user cannot be limited by policy, so daily use magnifies any mistake. Why the correct answer wins: An execution role gives the job an identity, and the prefix policy scopes its reads.
- **E:** Correct. An execution role grants the job only the permissions its inputs and outputs need. In this case: An execution role gives the job an identity, and the prefix policy scopes its reads.

### Question 61 — C

Answer: Create a role the other account can assume. A role assumption issues temporary credentials across the account boundary. A cross-account role issues temporary credentials without sharing a key. Local study-map skill 4.6 (IAM and Credentials), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. A group policy keeps the shared permission set in one reviewable place. Why the correct answer wins: A role assumption issues temporary credentials across the account boundary.
- **B:** Incorrect for this question. The root user cannot be limited by policy, so daily use magnifies any mistake. Why the correct answer wins: A role assumption issues temporary credentials across the account boundary.
- **C:** Correct. A cross-account role issues temporary credentials without sharing a key. In this case: A role assumption issues temporary credentials across the account boundary.
- **D:** Incorrect for this question. A long-lived key keeps working after the project ends unless someone retires it. Why the correct answer wins: A role assumption issues temporary credentials across the account boundary.

### Question 62 — A

Answer: Deny access to the bucket unless the request comes through the VPC endpoint. A condition on the endpoint denies every other path. A condition on the endpoint keeps the data off every path except the private one. Local study-map skill 4.7 (Network Isolation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Correct. A condition on the endpoint keeps the data off every path except the private one. In this case: A condition on the endpoint denies every other path.
- **B:** Incorrect for this question. A private endpoint keeps the service traffic inside the VPC without a NAT gateway. Why the correct answer wins: A condition on the endpoint denies every other path.
- **C:** Incorrect for this question. Private subnets remove the inbound internet path to the model hosts. Why the correct answer wins: A condition on the endpoint denies every other path.
- **D:** Incorrect for this question. A security group scoped to the caller subnet allows only the intended traffic. Why the correct answer wins: A condition on the endpoint denies every other path.

### Question 63 — A

Answer: Store the model API credential in AWS Secrets Manager. A managed secret store rotates the credential centrally. Secrets Manager holds the credential centrally and can rotate it. Local study-map skill 4.8 (Encryption and Secrets), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Correct. Secrets Manager holds the credential centrally and can rotate it. In this case: A managed secret store rotates the credential centrally.
- **B:** Incorrect for this question. Guardrails filters denied topics, sensitive data and unsafe content in the response path. Why the correct answer wins: A managed secret store rotates the credential centrally.
- **C:** Incorrect for this question. Config records how each resource was configured and evaluates it against rules. Why the correct answer wins: A managed secret store rotates the credential centrally.
- **D:** Incorrect for this question. A customer managed key lets the team control the key policy and revoke access. Why the correct answer wins: A managed secret store rotates the credential centrally.

### Question 64 — C

Answer: Configure a denied-topics policy for the assistant. A denied-topics policy refuses the ruled-out area. A denied-topics policy refuses the subject areas the business has ruled out. Local study-map skill 4.9 (Guardrails and Responsible AI), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. Redaction at the boundary keeps personal data out of the model request entirely. Why the correct answer wins: A denied-topics policy refuses the ruled-out area.
- **B:** Incorrect for this question. Safety screening keeps prohibited material out of the model weights. Why the correct answer wins: A denied-topics policy refuses the ruled-out area.
- **C:** Correct. A denied-topics policy refuses the subject areas the business has ruled out. In this case: A denied-topics policy refuses the ruled-out area.
- **D:** Incorrect for this question. Guardrails filters denied topics, sensitive data and unsafe content in the response path. Why the correct answer wins: A denied-topics policy refuses the ruled-out area.

### Question 65 — B

Answer: Scan the built image with Amazon Inspector. A vulnerability scan reports findings before deployment. Inspector reports known vulnerabilities in the image before it is deployed. Local study-map skill 4.10 (Audit and Vulnerability Scanning), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. CloudTrail records who called which API, when and from where. Why the correct answer wins: A vulnerability scan reports findings before deployment.
- **B:** Correct. Inspector reports known vulnerabilities in the image before it is deployed. In this case: A vulnerability scan reports findings before deployment.
- **C:** Incorrect for this question. Config records how each resource was configured and evaluates it against rules. Why the correct answer wins: A vulnerability scan reports findings before deployment.
- **D:** Incorrect for this question. CodeGuru reviews the source for defects and inefficiencies. Why the correct answer wins: A vulnerability scan reports findings before deployment.
