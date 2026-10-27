# AWS Certified Machine Learning Engineer – Associate (MLA-C02) — Full-Length Mock Exam 1

Machine Learning Engineer · 65 questions · 130 minutes · scaled passing score 720 of 1000

Blueprint-weighted mock exam. Item mix: 50 multiple-choice and 15 multiple-response items (the selection count is stated in each multi-response stem). The published exam has 65 questions in 130 minutes, of which 50 are scored and 15 are unscored, and AWS does not identify the unscored items. AWS publishes no split between multiple-choice and multiple-response items, so the 15-item multi-response block is an authoring choice. At 65 items in 130 minutes this set matches the published pacing at about 120 seconds per item. AWS is currently delivering MLA-C02 as a beta of 85 questions in 170 minutes with the extra items unscored; this set follows the published 65-question form. The published format has no case-study component, so no case-study item appears here. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied AWS exam items.

## Questions

---

## Domain 1 — Data Preparation for ML and AI (28%) — Ingestion, storage, feature engineering, embeddings, and data quality

### 1. A recommender needs the latest customer profile for each page view, at single-digit millisecond latency and hundreds of times a second. Where should those profiles live?

- A. Mount a shared Amazon EFS file system on every training host
- B. Land the dataset as Parquet in Amazon S3
- C. Use Amazon FSx for Lustre for the training file system
- D. Serve low-latency feature lookups from Amazon DynamoDB

### 2. A four-node training job reads two terabytes of shards per epoch, and the shared file system has become the bottleneck. What should the job read from?

- A. Use S3 Intelligent-Tiering for the unevenly accessed corpus
- B. Mount a shared Amazon EFS file system on every training host
- C. Use Amazon FSx for Lustre for the training file system
- D. Attach a gp3 Amazon EBS volume to the training instance

### 3. Order events must stay in arrival order, and three consumers each read the stream at their own pace. What should ingest them?

- A. Ingest the events with Amazon Kinesis Data Streams
- B. Transform the data with an AWS Glue ETL job
- C. Deliver the stream to Amazon S3 with Amazon Data Firehose
- D. Transform each stream record with AWS Lambda

### 4. Auditors require that the dataset behind a promotion decision cannot be altered or deleted for seven years. What should be applied to it?

- A. Archive the raw corpus to an S3 Glacier storage class
- B. Apply S3 Object Lock to the regulated training data
- C. Use S3 Intelligent-Tiering for the unevenly accessed corpus
- D. Expire intermediate artefacts with an S3 lifecycle rule

### 5. Every nightly feature rebuild reads three hundred gigabytes of CSV extracts, and the job is bound by reading whole rows. What should the stored format become?

- A. Land the raw JSON events in Amazon S3 unchanged
- B. Land the dataset as Parquet in Amazon S3
- C. Attach a gp3 Amazon EBS volume to the training instance
- D. Mount a shared Amazon EFS file system on every training host

### 6. Feature jobs read the last thirty days from a five-year bucket, yet every run scans the entire prefix. What should change in the layout?

- A. Expire intermediate artefacts with an S3 lifecycle rule
- B. Mount a shared Amazon EFS file system on every training host
- C. Land the raw JSON events in Amazon S3 unchanged
- D. Partition the S3 prefix by event date

### 7. Changes in the operational order database must appear in the lake within the hour, without custom extract code to maintain. What should copy them?

- A. Transform the data with an AWS Glue ETL job
- B. Ingest the events with Amazon Kinesis Data Streams
- C. Process the data with Spark on Amazon EMR
- D. Replicate the operational tables with AWS Database Migration Service

### 8. Point-of-sale extracts must be joined with web events nightly with no cluster to operate, and Athena and Redshift must read the same table definitions. Which two services fit? Select two.

- A. Process the data with Spark on Amazon EMR
- B. Profile and clean the data with AWS Glue DataBrew
- C. Prepare the data in SageMaker Data Wrangler
- D. Register the tables in the AWS Glue Data Catalog
- E. Transform the data with an AWS Glue ETL job

### 9. A discount feature is computed by one team and must have exactly the same value in training and in the live request path. What should be created?

- A. Publish the features to the SageMaker Feature Store online store
- B. Ingest the cleaned rows into a SageMaker Feature Group
- C. Register the tables in the AWS Glue Data Catalog
- D. Keep the point-in-time history in the Feature Store offline store

### 10. A neural model diverges while the same features behave well for a tree model, because the columns range from counts to currency amounts. What should be added?

- A. Apply a log transform to the skewed amount column
- B. Bin the continuous age column into ranges
- C. Standardise the numeric columns before training
- D. One-hot encode the categorical columns

### 11. A three percent positive class disappears from some validation folds, so the reported metric jumps between runs. What should the split do?

- A. Remove duplicate rows before splitting
- B. Generate synthetic minority samples to rebalance the classes
- C. Shuffle the rows before every epoch
- D. Stratify the train, validation and test splits by label

### 12. Eighty million product descriptions must be searched by meaning with metadata filters, through a managed index. What should hold the vectors?

- A. Load every vector into the application process on each request
- B. Keep the vectors in Amazon S3 with a vector index
- C. Store the vectors in Amazon RDS for PostgreSQL with pgvector
- D. Index the vectors in Amazon OpenSearch Service with k-NN search

### 13. A catalogue team must turn descriptions into vectors and then answer similarity queries over them. Which two components are needed? Select two.

- A. Index the vectors in Amazon OpenSearch Service with k-NN search
- B. Add a reranking step after retrieval
- C. Generate the embeddings with an Amazon Bedrock embedding model
- D. Expire intermediate artefacts with an S3 lifecycle rule
- E. Serve low-latency feature lookups from Amazon DynamoDB

### 14. Support articles are long documents with clear headings, and retrieval keeps returning halves of two unrelated sections. What should change first?

- A. Store source, date and section metadata with each chunk
- B. Chunk the documents on semantic boundaries such as headings
- C. Split the documents into fixed-size overlapping chunks
- D. Tokenise the text with the target model tokeniser

### 15. A staging table keeps arriving with nulls in required fields and with columns whose type changed between files. Which two controls should run before training? Select two.

- A. Evaluate AWS Glue Data Quality rules on the prepared table
- B. Profile and clean the data with AWS Glue DataBrew
- C. Enforce a schema contract on the ingested records
- D. Profile the incoming data and store the statistics as a baseline
- E. Expire intermediate artefacts with an S3 lifecycle rule

### 16. Two hundred thousand product photos need labels, a small expert team is available, and the budget only covers review of uncertain cases. What should be used?

- A. Augment the image set with rotations, crops and flips
- B. Use automated data labelling with a human review sample in Ground Truth
- C. Send the unlabelled records to Amazon SageMaker Ground Truth
- D. Mask and redact personal identifiers before training

### 17. Before training a promotion-eligibility model, the team must quantify how under-represented one customer group is. What should run first?

- A. Measure bias with SageMaker Clarify before training
- B. Stratify the train, validation and test splits by label
- C. Augment the image set with rotations, crops and flips
- D. Reweight the under-represented group in the loss

### 18. A spend column is heavily skewed, has missing values, and contains a handful of impossible extremes that distort the model. Which two cleaning steps fit? Select two.

- A. One-hot encode the categorical columns
- B. Remove duplicate rows before splitting
- C. Impute missing numeric values with the median
- D. Clip extreme outliers to a defined percentile
- E. Drop every row that has any missing field

---

## Domain 2 — ML Model and Foundation Model (FM) Development (24%) — Model and FM selection, tuning, customisation, and evaluation

### 19. A churn model has forty mixed tabular features and needs a strong baseline within a day. Which approach fits?

- A. Train with the linear learner algorithm
- B. Use the k-nearest-neighbours algorithm
- C. Forecast the series with the DeepAR algorithm
- D. Train the tabular classifier with the XGBoost built-in algorithm

### 20. A regulator requires a specific reason code for every declined promotion, and the reason must be visible per applicant. What should the model choice favour?

- A. Choose an interpretable model for the regulated decision
- B. Average several models into an ensemble
- C. Start with the largest available model for every request
- D. Train the tabular classifier with the XGBoost built-in algorithm

### 21. A merchandising assistant must answer over whole 150-page supplier catalogues in a single request through a managed API. Which model choice fits?

- A. Select an Anthropic Claude model in Amazon Bedrock
- B. Select a Titan embedding model in Amazon Bedrock
- C. Download open weights and host them on your own endpoint
- D. Select an Amazon Nova foundation model in Amazon Bedrock

### 22. Eighty million product descriptions must become vectors for semantic search. Which Bedrock capability fits?

- A. Select an Amazon Nova foundation model in Amazon Bedrock
- B. Select an Anthropic Claude model in Amazon Bedrock
- C. Select a Titan embedding model in Amazon Bedrock
- D. Download open weights and host them on your own endpoint

### 23. Eight thousand support transcripts should tune a hosted model, the GPU budget is small, and the existing behaviour must not be lost. What should be done?

- A. Run continued pre-training on the domain corpus
- B. Start with task-specific prompt engineering before any training
- C. Fine-tune with parameter-efficient adapters such as LoRA
- D. Run full-parameter fine-tuning on the curated corpus

### 24. The model must learn unfamiliar internal product vocabulary, and its original general behaviour must survive that training. Which two techniques fit? Select two.

- A. Distil the large model into a smaller student model
- B. Mix replay samples from the original distribution into fine-tuning
- C. Run continued pre-training on the domain corpus
- D. Start with task-specific prompt engineering before any training
- E. Run full-parameter fine-tuning on the curated corpus

### 25. An assistant must cite the current returns policy, which changes every week, and retraining each week is not acceptable. What should be built?

- A. Run full-parameter fine-tuning on the curated corpus
- B. Start with task-specific prompt engineering before any training
- C. Run continued pre-training on the domain corpus
- D. Build retrieval-augmented generation instead of fine-tuning

### 26. Ten thousand scanned supplier invoices must become structured line-item fields. Which service fits?

- A. Detect entities and sentiment with Amazon Comprehend
- B. Detect objects and text in images with Amazon Rekognition
- C. Transcribe the calls with Amazon Transcribe
- D. Extract the form fields with Amazon Textract

### 27. A team has a scikit-learn pipeline with custom preprocessing that must run inside a managed training job. What should they use?

- A. Bring a custom training container image
- B. Package the training code in script mode with a supported framework
- C. Train the tabular classifier with the XGBoost built-in algorithm
- D. Start from a SageMaker JumpStart model

### 28. Twelve hyperparameters must be searched with a fixed budget of fifty trials, and previous trials should inform the next ones. Which search fits?

- A. Use Bayesian search over a defined objective metric
- B. Run a hand-written grid of training jobs
- C. Use random search over a small range
- D. Enable early stopping on the validation metric

### 29. A team must run the hyperparameter search as a service and must be sure the search optimises the metric that reflects business value. Which two elements are needed? Select two.

- A. Keep a managed warm pool for the training cluster
- B. Run a hand-written grid of training jobs
- C. Tune hyperparameters with SageMaker automatic model tuning
- D. Define the tuning objective on the validation metric that matters
- E. Enable early stopping on the validation metric

### 30. Training already runs on reclaimed Spot capacity, four hours of progress were lost last week, and trials that plateau still run to completion. Which two changes fit? Select two.

- A. Checkpoint to Amazon S3 so an interrupted job resumes
- B. Run training on managed Spot training capacity
- C. Add training data and keep a held-out validation split
- D. Keep a managed warm pool for the training cluster
- E. Enable early stopping on the validation metric

### 31. A model must rank customers by purchase likelihood, and the business will choose the cut-off later. Which reported metric fits?

- A. Report RMSE for the regression
- B. Inspect the confusion matrix on the minority class
- C. Report ROC-AUC for the ranking task
- D. Report F1 on the holdout set

### 32. On a three percent positive class, the team must report one balanced score and must see which class the model keeps confusing. Which two fit? Select two.

- A. Report ROC-AUC for the ranking task
- B. Pick the threshold from the precision-recall curve
- C. Inspect the confusion matrix on the minority class
- D. Report RMSE for the regression
- E. Report F1 on the holdout set

### 33. Generated product summaries are being scored, paraphrases are acceptable, and exact word overlap is penalising good answers. Which metric fits?

- A. Score the answers with BERTScore
- B. Score the generated summaries with BLEU
- C. Report RMSE for the regression
- D. Score the generated summaries with ROUGE

### 34. Two runs of the same notebook report different F1 scores and nobody can tell which data snapshot each used. What is missing?

- A. Log runs with MLflow on SageMaker AI
- B. Register the approved version in the SageMaker Model Registry
- C. Pin the data snapshot, code version and hyperparameters for each run
- D. Record a performance baseline and monitor drift against it

---

## Domain 3 — Deployment and Orchestration of ML and AI Workflows (24%) — Inference infrastructure, scaling, CI/CD, and orchestration

### 35. Each product page must score a recommendation in under 100 milliseconds, all day, at steady volume. Which deployment fits?

- A. Deploy a real-time SageMaker AI endpoint
- B. Deploy a serverless inference endpoint
- C. Use asynchronous inference with results written to Amazon S3
- D. Run a batch transform job over the stored records

### 36. Forty million rows are rescored nightly, and separately some twenty-minute document jobs are submitted by API with results collected from S3. Which two deployment methods fit? Select two.

- A. Buy provisioned throughput for the Bedrock model
- B. Deploy a real-time SageMaker AI endpoint
- C. Run a batch transform job over the stored records
- D. Deploy a serverless inference endpoint
- E. Use asynchronous inference with results written to Amazon S3

### 37. Four hundred small per-store models are each called a few times an hour, and hosting one endpoint per model is unaffordable. What fits?

- A. Run a batch transform job over the stored records
- B. Deploy a serverless inference endpoint
- C. Host many small models behind one multi-model endpoint
- D. Run several containers behind one endpoint

### 38. Weights fine-tuned outside AWS must be served on Bedrock infrastructure under the same API as hosted models. What should be used?

- A. Import the fine-tuned weights with Bedrock custom model import
- B. Buy provisioned throughput for the Bedrock model
- C. Start from a SageMaker JumpStart model
- D. Download open weights and host them on your own endpoint

### 39. A checkout assistant calls a Bedrock model at a steady high volume, and throttling during peak is unacceptable. What should be purchased?

- A. Compare provisioned throughput against on-demand spend
- B. Right-size the instance family against the measured latency
- C. Buy provisioned throughput for the Bedrock model
- D. Call the Bedrock model on demand

### 40. An assistant must answer from current policy documents and must also call an order-lookup API during the same conversation. What must be deployed together?

- A. Store the prompt templates in Amazon Bedrock Prompt Management
- B. Persist the agent session state between turns
- C. Schedule a knowledge base sync when documents change
- D. Deploy the agent with its action groups and knowledge base

### 41. The training image needs specific CUDA libraries and must be versioned so the service pulls exactly that build. Where should the image live?

- A. Store the container image in Amazon ECR
- B. Bring a custom training container image
- C. Build and test the model image with AWS CodeBuild
- D. Run the container on Amazon ECS

### 42. Traffic doubles every evening at six and returns to normal by ten, and each instance handles forty requests a second. Which policy fits?

- A. Scale the endpoint to zero outside business hours
- B. Auto scale the endpoint on a target-tracking policy
- C. Keep provisioned concurrency ready for the burst window
- D. Auto scale on a step policy with CloudWatch alarms

### 43. GPU endpoints are expensive when idle, and each request is heavy enough that invocation count misleads the scaler. Which two settings fit? Select two.

- A. Auto scale the endpoint on a target-tracking policy
- B. Auto scale on a step policy with CloudWatch alarms
- C. Keep a managed warm pool for the training cluster
- D. Scale on GPU utilisation rather than invocation count
- E. Scale the endpoint to zero outside business hours

### 44. Model containers must reach S3 and the model registry without any traffic crossing the internet, and must accept no inbound connection from outside the VPC. Which two steps fit? Select two.

- A. Place the endpoint and model containers in private subnets
- B. Create an interface VPC endpoint for the service
- C. Restrict the security group to the application subnet
- D. Route the private subnet through a NAT gateway
- E. Allow ingress from any address on the endpoint port

### 45. Every commit must build the training image and run the unit tests in a clean environment before anything is deployed. Which service performs that step?

- A. Orchestrate the release with AWS CodePipeline
- B. Build and test the model image with AWS CodeBuild
- C. Shift traffic with AWS CodeDeploy
- D. Keep the pipeline source in AWS CodeCommit

### 46. Releases must follow defined stages in order, and a model whose evaluation metric misses the agreed bar must not reach production. Which two components fit? Select two.

- A. Keep the pipeline source in AWS CodeCommit
- B. Connect the external repository with AWS CodeConnections
- C. Fail the pipeline when the evaluation threshold is missed
- D. Orchestrate the release with AWS CodePipeline
- E. Shift traffic with AWS CodeDeploy

### 47. Auditors must trace each deployed model to its training run and see that a human approved that version. Where should that be recorded?

- A. Log runs with MLflow on SageMaker AI
- B. Require a manual approval before the version is deployed
- C. Register the approved version in the SageMaker Model Registry
- D. Store the prompt templates in Amazon Bedrock Prompt Management

### 48. A new ranking model must reach only five percent of traffic until its metrics are reviewed. Which strategy fits?

- A. Replace the production version in a single switch
- B. Send a small share of traffic to the new version first
- C. Shift traffic to the new version in equal steps
- D. Mirror traffic to the new model without serving its answers

### 49. A replacement model must be compared against production on live traffic without any customer seeing its answers. Which strategy fits?

- A. Send a small share of traffic to the new version first
- B. Replace the production version in a single switch
- C. Split traffic between variants and compare the outcome metric
- D. Mirror traffic to the new model without serving its answers

### 50. Processing, training and registration must run as one scheduled workflow with lineage between the steps and no custom orchestration code. What fits?

- A. Orchestrate the steps with AWS Step Functions
- B. Define the workflow as a SageMaker pipeline
- C. Orchestrate the release with AWS CodePipeline
- D. Trigger the retraining run with an EventBridge schedule

---

## Domain 4 — Operating, Monitoring, and Securing ML and AI Solutions (24%) — Monitoring, cost control, identity, network isolation, and guardrails

### 51. Two weeks after a promotion campaign, the live request distribution no longer matches training and predictions have degraded. What should have been enabled?

- A. Enable a model quality monitor with ground-truth labels
- B. Enable a bias drift monitor
- C. Enable feature attribution drift monitoring
- D. Enable a data drift monitor on the endpoint

### 52. True purchase outcomes arrive seven days after each prediction, and the team must prove whether accuracy actually fell. Which two elements fit? Select two.

- A. Enable a data drift monitor on the endpoint
- B. Alarm on the CloudWatch latency and error metrics
- C. Enable a model quality monitor with ground-truth labels
- D. Enable CloudWatch generative AI observability for the model calls
- E. Record a performance baseline and monitor drift against it

### 53. The on-call engineer must be paged when endpoint latency exceeds 200 milliseconds or errors pass one percent. What should be configured?

- A. Build a CloudWatch dashboard for the pipeline metrics
- B. Alarm on the CloudWatch latency and error metrics
- C. Query the inference logs with CloudWatch Logs Insights
- D. Trace the pipeline service calls with AWS X-Ray

### 54. Requests failed yesterday afternoon and the team needs the failing request pattern from millions of log lines. What should be used?

- A. Alarm on the CloudWatch latency and error metrics
- B. Build a CloudWatch dashboard for the pipeline metrics
- C. Track resource configuration with AWS Config
- D. Query the inference logs with CloudWatch Logs Insights

### 55. Every assistant call must record the prompt, the token counts and the latency so cost and quality can be reviewed later. What should be enabled?

- A. Alarm on the CloudWatch latency and error metrics
- B. Enable CloudWatch generative AI observability for the model calls
- C. Trace agent tool calls with Bedrock AgentCore Observability
- D. Trace the pipeline service calls with AWS X-Ray

### 56. Inference runs at a predictable steady volume all year, and the finance team wants a lower effective rate for that commitment. What fits?

- A. Cover the steady inference load with a Savings Plan
- B. Right-size the instance family against the measured latency
- C. Break the spend down by endpoint with AWS Cost Explorer
- D. Move the offline scoring to batch transform

### 57. An endpoint costs more than expected, its p95 latency is already met, and the load is steady. Which two levers cut cost without hurting that latency? Select two.

- A. Scale the endpoint to zero outside business hours
- B. Allow ingress from any address on the endpoint port
- C. Cover the steady inference load with a Savings Plan
- D. Right-size the instance family against the measured latency
- E. Start with the largest available model for every request

### 58. Generated marketing copy is billed mostly on output length, and responses are running far longer than the template needs. What should be set?

- A. Cache embeddings for documents that have not changed
- B. Route routine requests to a smaller model
- C. Cap the output tokens per request
- D. Trim the retrieved context sent to the model

### 59. A RAG assistant sends twelve retrieved passages on every call, and most of that text never reaches the answer. What should change first?

- A. Trim the retrieved context sent to the model
- B. Compare provisioned throughput against on-demand spend
- C. Cache embeddings for documents that have not changed
- D. Cap the output tokens per request

### 60. A training job must read one prefix of the data lake and must not be able to reach any other bucket. What should the policy scope be?

- A. Attach one policy to an IAM group the engineers belong to
- B. Give the training job a scoped IAM execution role
- C. Attach a policy scoped to the one bucket prefix
- D. Use the account root user for pipeline administration

### 61. A pipeline in one account must read data in another, and no long-lived key may be stored anywhere. Which two elements fit? Select two.

- A. Create a role the other account can assume
- B. Attach one policy to an IAM group the engineers belong to
- C. Use the account root user for pipeline administration
- D. Create a long-lived access key for the integration
- E. Give the training job a scoped IAM execution role

### 62. The model endpoint must accept connections only from the application subnet and must have no internet route. What should be configured?

- A. Place the endpoint and model containers in private subnets
- B. Create an interface VPC endpoint for the service
- C. Route the private subnet through a NAT gateway
- D. Allow ingress from any address on the endpoint port

### 63. Model artefacts must be encrypted with a key the team can disable on its own authority when a project closes. What should be used?

- A. Encrypt the artefacts with a customer managed KMS key
- B. Track resource configuration with AWS Config
- C. Store the model API credential in AWS Secrets Manager
- D. Apply Amazon Bedrock Guardrails to the model responses

### 64. A shopping assistant must refuse medical-advice topics and mask personal data in its responses, through one managed control on the response path. What fits?

- A. Redact personal data before the prompt reaches the model
- B. Screen the training text for unsafe content
- C. Apply Amazon Bedrock Guardrails to the model responses
- D. Scan the built image with Amazon Inspector

### 65. An endpoint was deleted on a Sunday and the team must know which identity made the call and from where. What holds that evidence?

- A. Track resource configuration with AWS Config
- B. Record the API calls with AWS CloudTrail
- C. Query the inference logs with CloudWatch Logs Insights
- D. Trace the pipeline service calls with AWS X-Ray

---

## Answer key and explanations

### Question 1 — D

Answer: Serve low-latency feature lookups from Amazon DynamoDB. A key-value store answers each lookup in milliseconds without scanning a dataset. DynamoDB answers key lookups at single-digit millisecond latency. Local study-map skill 1.1 (Ingestion Sources and Storage Choice), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. EFS gives many hosts one POSIX file system, which suits shared code and small data. Why the correct answer wins: A key-value store answers each lookup in milliseconds without scanning a dataset.
- **B:** Incorrect for this question. Columnar Parquet files in S3 are read in column subsets, which suits repeated training scans. Why the correct answer wins: A key-value store answers each lookup in milliseconds without scanning a dataset.
- **C:** Incorrect for this question. Lustre delivers the high throughput a multi-node training job needs from shared storage. Why the correct answer wins: A key-value store answers each lookup in milliseconds without scanning a dataset.
- **D:** Correct. DynamoDB answers key lookups at single-digit millisecond latency. In this case: A key-value store answers each lookup in milliseconds without scanning a dataset.

### Question 2 — C

Answer: Use Amazon FSx for Lustre for the training file system. Lustre delivers the throughput a multi-node training job needs from shared storage. Local study-map skill 1.1 (Ingestion Sources and Storage Choice), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Intelligent-Tiering moves objects between access tiers as usage changes, with no rules to write. Why the correct answer wins: Lustre delivers the throughput a multi-node training job needs from shared storage.
- **B:** Incorrect for this question. EFS gives many hosts one POSIX file system, which suits shared code and small data. Why the correct answer wins: Lustre delivers the throughput a multi-node training job needs from shared storage.
- **C:** Correct. In this case: Lustre delivers the throughput a multi-node training job needs from shared storage.
- **D:** Incorrect for this question. EBS is block storage bound to one instance, which suits a single host and not a fleet. Why the correct answer wins: Lustre delivers the throughput a multi-node training job needs from shared storage.

### Question 3 — A

Answer: Ingest the events with Amazon Kinesis Data Streams. A data stream keeps one ordered log that several consumers read independently. Kinesis holds an ordered stream that several consumers can read at their own pace. Local study-map skill 1.2 (Streaming Ingestion), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Correct. Kinesis holds an ordered stream that several consumers can read at their own pace. In this case: A data stream keeps one ordered log that several consumers read independently.
- **B:** Incorrect for this question. Glue runs a managed Spark job against catalogued sources and writes the prepared output. Why the correct answer wins: A data stream keeps one ordered log that several consumers read independently.
- **C:** Incorrect for this question. Firehose batches the stream into S3 objects without a consumer to operate. Why the correct answer wins: A data stream keeps one ordered log that several consumers read independently.
- **D:** Incorrect for this question. A function per record suits lightweight enrichment and filtering of a stream. Why the correct answer wins: A data stream keeps one ordered log that several consumers read independently.

### Question 4 — B

Answer: Apply S3 Object Lock to the regulated training data. Object Lock holds the objects immutable for the stated retention period. Object Lock prevents the retained objects from being altered or deleted for the stated period. Local study-map skill 1.3 (Storage Class and Retention), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. An archive class is priced for data that is kept but rarely read. Why the correct answer wins: Object Lock holds the objects immutable for the stated retention period.
- **B:** Correct. Object Lock prevents the retained objects from being altered or deleted for the stated period. In this case: Object Lock holds the objects immutable for the stated retention period.
- **C:** Incorrect for this question. Intelligent-Tiering moves objects between access tiers as usage changes, with no rules to write. Why the correct answer wins: Object Lock holds the objects immutable for the stated retention period.
- **D:** Incorrect for this question. A lifecycle rule deletes the derived copies on a schedule, so storage does not grow forever. Why the correct answer wins: Object Lock holds the objects immutable for the stated retention period.

### Question 5 — B

Answer: Land the dataset as Parquet in Amazon S3. Columnar Parquet lets the rebuild read only the columns it uses. Columnar Parquet files in S3 are read in column subsets, which suits repeated training scans. Local study-map skill 1.4 (Data Formats and Partitioning), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Raw JSON is readable but forces every query to parse whole records. Why the correct answer wins: Columnar Parquet lets the rebuild read only the columns it uses.
- **B:** Correct. Columnar Parquet files in S3 are read in column subsets, which suits repeated training scans. In this case: Columnar Parquet lets the rebuild read only the columns it uses.
- **C:** Incorrect for this question. EBS is block storage bound to one instance, which suits a single host and not a fleet. Why the correct answer wins: Columnar Parquet lets the rebuild read only the columns it uses.
- **D:** Incorrect for this question. EFS gives many hosts one POSIX file system, which suits shared code and small data. Why the correct answer wins: Columnar Parquet lets the rebuild read only the columns it uses.

### Question 6 — D

Answer: Partition the S3 prefix by event date. Date prefixes let the job skip the partitions it does not need. Local study-map skill 1.4 (Data Formats and Partitioning), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. A lifecycle rule deletes the derived copies on a schedule, so storage does not grow forever. Why the correct answer wins: Date prefixes let the job skip the partitions it does not need.
- **B:** Incorrect for this question. EFS gives many hosts one POSIX file system, which suits shared code and small data. Why the correct answer wins: Date prefixes let the job skip the partitions it does not need.
- **C:** Incorrect for this question. Raw JSON is readable but forces every query to parse whole records. Why the correct answer wins: Date prefixes let the job skip the partitions it does not need.
- **D:** Correct. In this case: Date prefixes let the job skip the partitions it does not need.

### Question 7 — D

Answer: Replicate the operational tables with AWS Database Migration Service. A replication task keeps copying committed changes from the source database. DMS copies and keeps replicating rows from the source database without custom extract code. Local study-map skill 1.5 (Merge and Transform Tooling), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Glue runs a managed Spark job against catalogued sources and writes the prepared output. Why the correct answer wins: A replication task keeps copying committed changes from the source database.
- **B:** Incorrect for this question. Kinesis holds an ordered stream that several consumers can read at their own pace. Why the correct answer wins: A replication task keeps copying committed changes from the source database.
- **C:** Incorrect for this question. EMR gives a managed Spark cluster sized for the processing job. Why the correct answer wins: A replication task keeps copying committed changes from the source database.
- **D:** Correct. DMS copies and keeps replicating rows from the source database without custom extract code. In this case: A replication task keeps copying committed changes from the source database.

### Question 8 — D, E

Answers: Transform the data with an AWS Glue ETL job; Register the tables in the AWS Glue Data Catalog. A managed Spark job performs the join, and the catalog supplies one schema to every engine. Glue runs a managed Spark job against catalogued sources and writes the prepared output. The catalog gives every engine the same table definitions and schemas. Local study-map skill 1.5 (Merge and Transform Tooling), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. EMR gives a managed Spark cluster sized for the processing job. Why the correct answer wins: A managed Spark job performs the join, and the catalog supplies one schema to every engine.
- **B:** Incorrect for this question. DataBrew provides a visual recipe for profiling, cleaning and normalising columns. Why the correct answer wins: A managed Spark job performs the join, and the catalog supplies one schema to every engine.
- **C:** Incorrect for this question. Data Wrangler builds a reusable preparation flow and can export it into a pipeline. Why the correct answer wins: A managed Spark job performs the join, and the catalog supplies one schema to every engine.
- **D:** Correct. The catalog gives every engine the same table definitions and schemas. In this case: A managed Spark job performs the join, and the catalog supplies one schema to every engine.
- **E:** Correct. Glue runs a managed Spark job against catalogued sources and writes the prepared output. In this case: A managed Spark job performs the join, and the catalog supplies one schema to every engine.

### Question 9 — B

Answer: Ingest the cleaned rows into a SageMaker Feature Group. A feature group is the one definition that both training and inference read. Local study-map skill 1.6 (Feature Store), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. The online store serves the latest feature values for low-latency inference lookups. Why the correct answer wins: A feature group is the one definition that both training and inference read.
- **B:** Correct. In this case: A feature group is the one definition that both training and inference read.
- **C:** Incorrect for this question. The catalog gives every engine the same table definitions and schemas. Why the correct answer wins: A feature group is the one definition that both training and inference read.
- **D:** Incorrect for this question. The offline store keeps timestamped values so training reads the values that existed at the time. Why the correct answer wins: A feature group is the one definition that both training and inference read.

### Question 10 — C

Answer: Standardise the numeric columns before training. Scaling puts the numeric columns on comparable ranges before fitting. Local study-map skill 1.7 (Feature Engineering and Scaling), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. A log transform compresses the long tail of a heavily skewed amount distribution. Why the correct answer wins: Scaling puts the numeric columns on comparable ranges before fitting.
- **B:** Incorrect for this question. Binning trades resolution for robustness to small variations inside a range. Why the correct answer wins: Scaling puts the numeric columns on comparable ranges before fitting.
- **C:** Correct. In this case: Scaling puts the numeric columns on comparable ranges before fitting.
- **D:** Incorrect for this question. One-hot encoding turns unordered categories into separate binary columns. Why the correct answer wins: Scaling puts the numeric columns on comparable ranges before fitting.

### Question 11 — D

Answer: Stratify the train, validation and test splits by label. Stratifying keeps the label proportion in every fold. Local study-map skill 1.7 (Feature Engineering and Scaling), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Duplicates that straddle splits leak the same row into training and evaluation. Why the correct answer wins: Stratifying keeps the label proportion in every fold.
- **B:** Incorrect for this question. Synthetic minority sampling gives the learner more examples of the rare class. Why the correct answer wins: Stratifying keeps the label proportion in every fold.
- **C:** Incorrect for this question. Shuffling stops the batch order from encoding an accidental pattern. Why the correct answer wins: Stratifying keeps the label proportion in every fold.
- **D:** Correct. In this case: Stratifying keeps the label proportion in every fold.

### Question 12 — D

Answer: Index the vectors in Amazon OpenSearch Service with k-NN search. A managed vector index supports filtered nearest-neighbour search at that scale. OpenSearch provides a managed vector index with filtered k-nearest-neighbour search. Local study-map skill 1.8 (Vector Stores and Embeddings), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Rebuilding the index per request cannot hold a large corpus or a latency target. Why the correct answer wins: A managed vector index supports filtered nearest-neighbour search at that scale.
- **B:** Incorrect for this question. An S3-backed index suits a large, cost-sensitive corpus read less often. Why the correct answer wins: A managed vector index supports filtered nearest-neighbour search at that scale.
- **C:** Incorrect for this question. pgvector keeps vectors beside relational rows the application already queries. Why the correct answer wins: A managed vector index supports filtered nearest-neighbour search at that scale.
- **D:** Correct. OpenSearch provides a managed vector index with filtered k-nearest-neighbour search. In this case: A managed vector index supports filtered nearest-neighbour search at that scale.

### Question 13 — A, C

Answers: Generate the embeddings with an Amazon Bedrock embedding model; Index the vectors in Amazon OpenSearch Service with k-NN search. An embedding model produces the vectors, and the vector index answers the queries. A managed embedding model converts text into vectors without hosts to run. OpenSearch provides a managed vector index with filtered k-nearest-neighbour search. Local study-map skill 1.8 (Vector Stores and Embeddings), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Correct. OpenSearch provides a managed vector index with filtered k-nearest-neighbour search. In this case: An embedding model produces the vectors, and the vector index answers the queries.
- **B:** Incorrect for this question. A reranker reorders the retrieved passages by relevance before they reach the model. Why the correct answer wins: An embedding model produces the vectors, and the vector index answers the queries.
- **C:** Correct. A managed embedding model converts text into vectors without hosts to run. In this case: An embedding model produces the vectors, and the vector index answers the queries.
- **D:** Incorrect for this question. A lifecycle rule deletes the derived copies on a schedule, so storage does not grow forever. Why the correct answer wins: An embedding model produces the vectors, and the vector index answers the queries.
- **E:** Incorrect for this question. DynamoDB answers key lookups at single-digit millisecond latency. Why the correct answer wins: An embedding model produces the vectors, and the vector index answers the queries.

### Question 14 — B

Answer: Chunk the documents on semantic boundaries such as headings. Chunking on headings keeps one coherent passage inside each chunk. Semantic chunks keep a coherent passage together, which improves what retrieval returns. Local study-map skill 1.9 (Text Pre-processing and Chunking), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Metadata lets retrieval filter by source or recency and lets answers cite the document. Why the correct answer wins: Chunking on headings keeps one coherent passage inside each chunk.
- **B:** Correct. Semantic chunks keep a coherent passage together, which improves what retrieval returns. In this case: Chunking on headings keeps one coherent passage inside each chunk.
- **C:** Incorrect for this question. Overlapping fixed chunks bound the context size and avoid cutting a sentence in half. Why the correct answer wins: Chunking on headings keeps one coherent passage inside each chunk.
- **D:** Incorrect for this question. Using the model own tokeniser keeps token counts and truncation consistent with inference. Why the correct answer wins: Chunking on headings keeps one coherent passage inside each chunk.

### Question 15 — A, C

Answers: Evaluate AWS Glue Data Quality rules on the prepared table; Enforce a schema contract on the ingested records. Quality rules fail the job on invalid values, and a schema check rejects changed shapes. Data Quality rules fail the job on nulls, duplicates or range violations before training starts. A schema check rejects records whose fields changed shape before they corrupt the set. Local study-map skill 1.10 (Data Quality Validation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Correct. Data Quality rules fail the job on nulls, duplicates or range violations before training starts. In this case: Quality rules fail the job on invalid values, and a schema check rejects changed shapes.
- **B:** Incorrect for this question. DataBrew provides a visual recipe for profiling, cleaning and normalising columns. Why the correct answer wins: Quality rules fail the job on invalid values, and a schema check rejects changed shapes.
- **C:** Correct. A schema check rejects records whose fields changed shape before they corrupt the set. In this case: Quality rules fail the job on invalid values, and a schema check rejects changed shapes.
- **D:** Incorrect for this question. A stored profile is what later drift comparison is measured against. Why the correct answer wins: Quality rules fail the job on invalid values, and a schema check rejects changed shapes.
- **E:** Incorrect for this question. A lifecycle rule deletes the derived copies on a schedule, so storage does not grow forever. Why the correct answer wins: Quality rules fail the job on invalid values, and a schema check rejects changed shapes.

### Question 16 — B

Answer: Use automated data labelling with a human review sample in Ground Truth. Active learning labels most records automatically and routes only uncertain ones to a person. Local study-map skill 1.11 (Labelling and Annotation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Augmentation adds plausible variation that the original photographs did not contain. Why the correct answer wins: Active learning labels most records automatically and routes only uncertain ones to a person.
- **B:** Correct. In this case: Active learning labels most records automatically and routes only uncertain ones to a person.
- **C:** Incorrect for this question. Ground Truth manages the labelling workforce, instructions and quality checks. Why the correct answer wins: Active learning labels most records automatically and routes only uncertain ones to a person.
- **D:** Incorrect for this question. Removing the identifiers stops the model from learning or echoing personal data. Why the correct answer wins: Active learning labels most records automatically and routes only uncertain ones to a person.

### Question 17 — A

Answer: Measure bias with SageMaker Clarify before training. Bias metrics measure the imbalance so it is quantified before any mitigation. Clarify reports label and feature bias metrics so the imbalance is quantified first. Local study-map skill 1.12 (Bias Detection and Mitigation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Correct. Clarify reports label and feature bias metrics so the imbalance is quantified first. In this case: Bias metrics measure the imbalance so it is quantified before any mitigation.
- **B:** Incorrect for this question. Stratifying keeps the label proportions the same in every split. Why the correct answer wins: Bias metrics measure the imbalance so it is quantified before any mitigation.
- **C:** Incorrect for this question. Augmentation adds plausible variation that the original photographs did not contain. Why the correct answer wins: Bias metrics measure the imbalance so it is quantified before any mitigation.
- **D:** Incorrect for this question. Reweighting the loss changes what the model is optimised for without discarding data. Why the correct answer wins: Bias metrics measure the imbalance so it is quantified before any mitigation.

### Question 18 — C, D

Answers: Impute missing numeric values with the median; Clip extreme outliers to a defined percentile. Median imputation keeps the row, and clipping caps the influence of the extremes. Median imputation is robust to a skewed distribution and keeps the row. Clipping caps the influence of a few extreme values without deleting the records. Local study-map skill 1.13 (Cleaning and Class Imbalance), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. One-hot encoding turns unordered categories into separate binary columns. Why the correct answer wins: Median imputation keeps the row, and clipping caps the influence of the extremes.
- **B:** Incorrect for this question. Duplicates that straddle splits leak the same row into training and evaluation. Why the correct answer wins: Median imputation keeps the row, and clipping caps the influence of the extremes.
- **C:** Correct. Median imputation is robust to a skewed distribution and keeps the row. In this case: Median imputation keeps the row, and clipping caps the influence of the extremes.
- **D:** Correct. Clipping caps the influence of a few extreme values without deleting the records. In this case: Median imputation keeps the row, and clipping caps the influence of the extremes.
- **E:** Incorrect for this question. Dropping rows discards information and can bias the set towards complete records. Why the correct answer wins: Median imputation keeps the row, and clipping caps the influence of the extremes.

### Question 19 — D

Answer: Train the tabular classifier with the XGBoost built-in algorithm. Gradient-boosted trees are the usual strong baseline for tabular data. Local study-map skill 2.1 (Model and Algorithm Selection), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. A linear model is cheap and interpretable when the relationship is close to linear. Why the correct answer wins: Gradient-boosted trees are the usual strong baseline for tabular data.
- **B:** Incorrect for this question. Nearest neighbours suit a small, low-dimensional similarity problem. Why the correct answer wins: Gradient-boosted trees are the usual strong baseline for tabular data.
- **C:** Incorrect for this question. DeepAR learns across many related time series and returns probabilistic forecasts. Why the correct answer wins: Gradient-boosted trees are the usual strong baseline for tabular data.
- **D:** Correct. In this case: Gradient-boosted trees are the usual strong baseline for tabular data.

### Question 20 — A

Answer: Choose an interpretable model for the regulated decision. A decision that must be explained per applicant needs an inspectable model. Local study-map skill 2.1 (Model and Algorithm Selection), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Correct. In this case: A decision that must be explained per applicant needs an inspectable model.
- **B:** Incorrect for this question. An ensemble reduces variance from any single model fit. Why the correct answer wins: A decision that must be explained per applicant needs an inspectable model.
- **C:** Incorrect for this question. Sizing every request for the hardest case spends latency and money on easy requests. Why the correct answer wins: A decision that must be explained per applicant needs an inspectable model.
- **D:** Incorrect for this question. Gradient-boosted trees are the usual strong baseline for tabular data. Why the correct answer wins: A decision that must be explained per applicant needs an inspectable model.

### Question 21 — A

Answer: Select an Anthropic Claude model in Amazon Bedrock. A long context window is what the task needs, and Bedrock serves it without hosts. Claude models are available through Bedrock for long-context reasoning tasks. Local study-map skill 2.2 (Foundation Model Selection), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Correct. Claude models are available through Bedrock for long-context reasoning tasks. In this case: A long context window is what the task needs, and Bedrock serves it without hosts.
- **B:** Incorrect for this question. A Titan embedding model turns text into vectors for search and clustering. Why the correct answer wins: A long context window is what the task needs, and Bedrock serves it without hosts.
- **C:** Incorrect for this question. Self-hosting gives full control but puts model operations on your team. Why the correct answer wins: A long context window is what the task needs, and Bedrock serves it without hosts.
- **D:** Incorrect for this question. Nova models are reached through the Bedrock API with no infrastructure to host. Why the correct answer wins: A long context window is what the task needs, and Bedrock serves it without hosts.

### Question 22 — C

Answer: Select a Titan embedding model in Amazon Bedrock. An embedding model turns each description into a vector without hosting to run. A Titan embedding model turns text into vectors for search and clustering. Local study-map skill 2.2 (Foundation Model Selection), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. Nova models are reached through the Bedrock API with no infrastructure to host. Why the correct answer wins: An embedding model turns each description into a vector without hosting to run.
- **B:** Incorrect for this question. Claude models are available through Bedrock for long-context reasoning tasks. Why the correct answer wins: An embedding model turns each description into a vector without hosting to run.
- **C:** Correct. A Titan embedding model turns text into vectors for search and clustering. In this case: An embedding model turns each description into a vector without hosting to run.
- **D:** Incorrect for this question. Self-hosting gives full control but puts model operations on your team. Why the correct answer wins: An embedding model turns each description into a vector without hosting to run.

### Question 23 — C

Answer: Fine-tune with parameter-efficient adapters such as LoRA. Adapters train few parameters, which lowers cost and the risk of forgetting. Local study-map skill 2.3 (Fine-tuning and Customisation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. Continued pre-training adapts the model to domain vocabulary before task tuning. Why the correct answer wins: Adapters train few parameters, which lowers cost and the risk of forgetting.
- **B:** Incorrect for this question. A well-structured prompt often meets the requirement without a training run. Why the correct answer wins: Adapters train few parameters, which lowers cost and the risk of forgetting.
- **C:** Correct. In this case: Adapters train few parameters, which lowers cost and the risk of forgetting.
- **D:** Incorrect for this question. Full fine-tuning updates every weight and needs more data, memory and care. Why the correct answer wins: Adapters train few parameters, which lowers cost and the risk of forgetting.

### Question 24 — B, C

Answers: Run continued pre-training on the domain corpus; Mix replay samples from the original distribution into fine-tuning. Continued pre-training adds domain vocabulary, and replay samples keep earlier behaviour. Continued pre-training adapts the model to domain vocabulary before task tuning. Replay samples keep the earlier behaviour from being overwritten by the narrow new data. Local study-map skill 2.3 (Fine-tuning and Customisation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. Distillation transfers the large model behaviour into a cheaper model to serve. Why the correct answer wins: Continued pre-training adds domain vocabulary, and replay samples keep earlier behaviour.
- **B:** Correct. Replay samples keep the earlier behaviour from being overwritten by the narrow new data. In this case: Continued pre-training adds domain vocabulary, and replay samples keep earlier behaviour.
- **C:** Correct. Continued pre-training adapts the model to domain vocabulary before task tuning. In this case: Continued pre-training adds domain vocabulary, and replay samples keep earlier behaviour.
- **D:** Incorrect for this question. A well-structured prompt often meets the requirement without a training run. Why the correct answer wins: Continued pre-training adds domain vocabulary, and replay samples keep earlier behaviour.
- **E:** Incorrect for this question. Full fine-tuning updates every weight and needs more data, memory and care. Why the correct answer wins: Continued pre-training adds domain vocabulary, and replay samples keep earlier behaviour.

### Question 25 — D

Answer: Build retrieval-augmented generation instead of fine-tuning. Retrieval grounds answers in current documents without changing model weights. Local study-map skill 2.4 (RAG Architecture Patterns), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. Full fine-tuning updates every weight and needs more data, memory and care. Why the correct answer wins: Retrieval grounds answers in current documents without changing model weights.
- **B:** Incorrect for this question. A well-structured prompt often meets the requirement without a training run. Why the correct answer wins: Retrieval grounds answers in current documents without changing model weights.
- **C:** Incorrect for this question. Continued pre-training adapts the model to domain vocabulary before task tuning. Why the correct answer wins: Retrieval grounds answers in current documents without changing model weights.
- **D:** Correct. In this case: Retrieval grounds answers in current documents without changing model weights.

### Question 26 — D

Answer: Extract the form fields with Amazon Textract. Form and table extraction turns scanned documents into structured fields. Textract reads forms and tables into structured fields without a custom model. Local study-map skill 2.5 (Managed AI Services), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. Comprehend provides managed entity, key-phrase and sentiment analysis. Why the correct answer wins: Form and table extraction turns scanned documents into structured fields.
- **B:** Incorrect for this question. Rekognition provides managed image and video analysis for common labels and text. Why the correct answer wins: Form and table extraction turns scanned documents into structured fields.
- **C:** Incorrect for this question. Transcribe converts speech to text and can label speakers. Why the correct answer wins: Form and table extraction turns scanned documents into structured fields.
- **D:** Correct. Textract reads forms and tables into structured fields without a custom model. In this case: Form and table extraction turns scanned documents into structured fields.

### Question 27 — B

Answer: Package the training code in script mode with a supported framework. Script mode runs your own training script inside a managed framework container. Local study-map skill 2.6 (Built-in Algorithms and Script Mode), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. A custom image is needed only when the managed framework images cannot carry the dependencies. Why the correct answer wins: Script mode runs your own training script inside a managed framework container.
- **B:** Correct. In this case: Script mode runs your own training script inside a managed framework container.
- **C:** Incorrect for this question. Gradient-boosted trees are the usual strong baseline for tabular data. Why the correct answer wins: Script mode runs your own training script inside a managed framework container.
- **D:** Incorrect for this question. JumpStart supplies a pre-trained model and its deployment template. Why the correct answer wins: Script mode runs your own training script inside a managed framework container.

### Question 28 — A

Answer: Use Bayesian search over a defined objective metric. Bayesian search concentrates later trials where the space looks promising. Bayesian search spends the trial budget on the region of the space that looks promising. Local study-map skill 2.7 (Hyperparameter Tuning), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Correct. Bayesian search spends the trial budget on the region of the space that looks promising. In this case: Bayesian search concentrates later trials where the space looks promising.
- **B:** Incorrect for this question. A manual grid costs a job per combination and adapts to nothing. Why the correct answer wins: Bayesian search concentrates later trials where the space looks promising.
- **C:** Incorrect for this question. Random search is a cheap baseline but ignores what earlier trials learned. Why the correct answer wins: Bayesian search concentrates later trials where the space looks promising.
- **D:** Incorrect for this question. Early stopping ends a trial once the validation metric stops improving. Why the correct answer wins: Bayesian search concentrates later trials where the space looks promising.

### Question 29 — C, D

Answers: Tune hyperparameters with SageMaker automatic model tuning; Define the tuning objective on the validation metric that matters. Automatic model tuning runs the search, and the objective metric defines what it optimises. The search optimises exactly the metric it is given, so the metric must match the goal. Local study-map skill 2.7 (Hyperparameter Tuning), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. A warm pool removes the provisioning delay between consecutive training jobs. Why the correct answer wins: Automatic model tuning runs the search, and the objective metric defines what it optimises.
- **B:** Incorrect for this question. A manual grid costs a job per combination and adapts to nothing. Why the correct answer wins: Automatic model tuning runs the search, and the objective metric defines what it optimises.
- **C:** Correct. In this case: Automatic model tuning runs the search, and the objective metric defines what it optimises.
- **D:** Correct. The search optimises exactly the metric it is given, so the metric must match the goal. In this case: Automatic model tuning runs the search, and the objective metric defines what it optimises.
- **E:** Incorrect for this question. Early stopping ends a trial once the validation metric stops improving. Why the correct answer wins: Automatic model tuning runs the search, and the objective metric defines what it optimises.

### Question 30 — A, E

Answers: Checkpoint to Amazon S3 so an interrupted job resumes; Enable early stopping on the validation metric. Checkpoints let a reclaimed instance resume, and early stopping ends plateaued trials. Checkpoints let a reclaimed instance continue from the last saved state. Early stopping ends a trial once the validation metric stops improving. Local study-map skill 2.8 (Training Efficiency and Regularisation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Correct. Checkpoints let a reclaimed instance continue from the last saved state. In this case: Checkpoints let a reclaimed instance resume, and early stopping ends plateaued trials.
- **B:** Incorrect for this question. Spot capacity lowers the cost of a job that can checkpoint and resume. Why the correct answer wins: Checkpoints let a reclaimed instance resume, and early stopping ends plateaued trials.
- **C:** Incorrect for this question. More representative data reduces variance without shrinking the model. Why the correct answer wins: Checkpoints let a reclaimed instance resume, and early stopping ends plateaued trials.
- **D:** Incorrect for this question. A warm pool removes the provisioning delay between consecutive training jobs. Why the correct answer wins: Checkpoints let a reclaimed instance resume, and early stopping ends plateaued trials.
- **E:** Correct. Early stopping ends a trial once the validation metric stops improving. In this case: Checkpoints let a reclaimed instance resume, and early stopping ends plateaued trials.

### Question 31 — C

Answer: Report ROC-AUC for the ranking task. ROC-AUC measures separation across all thresholds rather than at one cut-off. ROC-AUC measures how well the scores separate the classes across thresholds. Local study-map skill 2.9 (Classic Model Evaluation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. RMSE expresses the typical error in the target units and penalises large misses. Why the correct answer wins: ROC-AUC measures separation across all thresholds rather than at one cut-off.
- **B:** Incorrect for this question. The confusion matrix shows which class the model keeps confusing. Why the correct answer wins: ROC-AUC measures separation across all thresholds rather than at one cut-off.
- **C:** Correct. ROC-AUC measures how well the scores separate the classes across thresholds. In this case: ROC-AUC measures separation across all thresholds rather than at one cut-off.
- **D:** Incorrect for this question. F1 balances precision and recall, which suits an uneven class mix. Why the correct answer wins: ROC-AUC measures separation across all thresholds rather than at one cut-off.

### Question 32 — C, E

Answers: Report F1 on the holdout set; Inspect the confusion matrix on the minority class. F1 balances precision and recall, and the confusion matrix shows the confused class. F1 balances precision and recall, which suits an uneven class mix. The confusion matrix shows which class the model keeps confusing. Local study-map skill 2.9 (Classic Model Evaluation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. ROC-AUC measures how well the scores separate the classes across thresholds. Why the correct answer wins: F1 balances precision and recall, and the confusion matrix shows the confused class.
- **B:** Incorrect for this question. The operating threshold should follow the cost of a false positive against a false negative. Why the correct answer wins: F1 balances precision and recall, and the confusion matrix shows the confused class.
- **C:** Correct. The confusion matrix shows which class the model keeps confusing. In this case: F1 balances precision and recall, and the confusion matrix shows the confused class.
- **D:** Incorrect for this question. RMSE expresses the typical error in the target units and penalises large misses. Why the correct answer wins: F1 balances precision and recall, and the confusion matrix shows the confused class.
- **E:** Correct. F1 balances precision and recall, which suits an uneven class mix. In this case: F1 balances precision and recall, and the confusion matrix shows the confused class.

### Question 33 — A

Answer: Score the answers with BERTScore. Contextual embedding comparison credits a paraphrase that an n-gram metric penalises. BERTScore compares contextual embeddings, so a paraphrase can still score well. Local study-map skill 2.10 (GenAI and NLP Evaluation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Correct. BERTScore compares contextual embeddings, so a paraphrase can still score well. In this case: Contextual embedding comparison credits a paraphrase that an n-gram metric penalises.
- **B:** Incorrect for this question. BLEU measures n-gram overlap with the reference summaries. Why the correct answer wins: Contextual embedding comparison credits a paraphrase that an n-gram metric penalises.
- **C:** Incorrect for this question. RMSE expresses the typical error in the target units and penalises large misses. Why the correct answer wins: Contextual embedding comparison credits a paraphrase that an n-gram metric penalises.
- **D:** Incorrect for this question. ROUGE measures recall of reference n-grams, which suits summarisation. Why the correct answer wins: Contextual embedding comparison credits a paraphrase that an n-gram metric penalises.

### Question 34 — C

Answer: Pin the data snapshot, code version and hyperparameters for each run. Pinned data, code and parameters are what make a run reproducible. Pinned inputs are what makes an experiment reproducible later. Local study-map skill 2.11 (Experiment Tracking and Baselines), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. Run logging keeps parameters, metrics and artefacts comparable across experiments. Why the correct answer wins: Pinned data, code and parameters are what make a run reproducible.
- **B:** Incorrect for this question. The registry holds model versions and their approval status for deployment. Why the correct answer wins: Pinned data, code and parameters are what make a run reproducible.
- **C:** Correct. Pinned inputs are what makes an experiment reproducible later. In this case: Pinned data, code and parameters are what make a run reproducible.
- **D:** Incorrect for this question. A stored baseline is the reference a drift monitor compares production against. Why the correct answer wins: Pinned data, code and parameters are what make a run reproducible.

### Question 35 — A

Answer: Deploy a real-time SageMaker AI endpoint. A real-time endpoint keeps a host ready to answer synchronous requests. Local study-map skill 3.1 (Inference Strategy), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Correct. In this case: A real-time endpoint keeps a host ready to answer synchronous requests.
- **B:** Incorrect for this question. Serverless inference scales to zero and suits intermittent, short requests. Why the correct answer wins: A real-time endpoint keeps a host ready to answer synchronous requests.
- **C:** Incorrect for this question. Asynchronous inference queues large or long requests and returns results through S3. Why the correct answer wins: A real-time endpoint keeps a host ready to answer synchronous requests.
- **D:** Incorrect for this question. Batch transform scores a stored dataset with no endpoint to keep running. Why the correct answer wins: A real-time endpoint keeps a host ready to answer synchronous requests.

### Question 36 — C, E

Answers: Run a batch transform job over the stored records; Use asynchronous inference with results written to Amazon S3. Batch transform scores the stored nightly dataset, and asynchronous inference handles the long API jobs. Batch transform scores a stored dataset with no endpoint to keep running. Asynchronous inference queues large or long requests and returns results through S3. Local study-map skill 3.1 (Inference Strategy), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. Provisioned throughput reserves model capacity for predictable, high-volume traffic. Why the correct answer wins: Batch transform scores the stored nightly dataset, and asynchronous inference handles the long API jobs.
- **B:** Incorrect for this question. A real-time endpoint answers synchronous requests with a persistent host behind it. Why the correct answer wins: Batch transform scores the stored nightly dataset, and asynchronous inference handles the long API jobs.
- **C:** Correct. Batch transform scores a stored dataset with no endpoint to keep running. In this case: Batch transform scores the stored nightly dataset, and asynchronous inference handles the long API jobs.
- **D:** Incorrect for this question. Serverless inference scales to zero and suits intermittent, short requests. Why the correct answer wins: Batch transform scores the stored nightly dataset, and asynchronous inference handles the long API jobs.
- **E:** Correct. Asynchronous inference queues large or long requests and returns results through S3. In this case: Batch transform scores the stored nightly dataset, and asynchronous inference handles the long API jobs.

### Question 37 — C

Answer: Host many small models behind one multi-model endpoint. A multi-model endpoint loads models on demand behind shared hosting capacity. Local study-map skill 3.2 (Endpoint Architecture), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. Batch transform scores a stored dataset with no endpoint to keep running. Why the correct answer wins: A multi-model endpoint loads models on demand behind shared hosting capacity.
- **B:** Incorrect for this question. Serverless inference scales to zero and suits intermittent, short requests. Why the correct answer wins: A multi-model endpoint loads models on demand behind shared hosting capacity.
- **C:** Correct. In this case: A multi-model endpoint loads models on demand behind shared hosting capacity.
- **D:** Incorrect for this question. A multi-container endpoint chains containers such as preprocessing and inference. Why the correct answer wins: A multi-model endpoint loads models on demand behind shared hosting capacity.

### Question 38 — A

Answer: Import the fine-tuned weights with Bedrock custom model import. Custom model import runs your own weights on Bedrock managed infrastructure. Local study-map skill 3.3 (Foundation Model Deployment), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Correct. In this case: Custom model import runs your own weights on Bedrock managed infrastructure.
- **B:** Incorrect for this question. Provisioned throughput reserves model capacity for predictable, high-volume traffic. Why the correct answer wins: Custom model import runs your own weights on Bedrock managed infrastructure.
- **C:** Incorrect for this question. JumpStart supplies a pre-trained model and its deployment template. Why the correct answer wins: Custom model import runs your own weights on Bedrock managed infrastructure.
- **D:** Incorrect for this question. Self-hosting gives full control but puts model operations on your team. Why the correct answer wins: Custom model import runs your own weights on Bedrock managed infrastructure.

### Question 39 — C

Answer: Buy provisioned throughput for the Bedrock model. Provisioned throughput reserves capacity so peak traffic is not throttled. Provisioned throughput reserves model capacity for predictable, high-volume traffic. Local study-map skill 3.3 (Foundation Model Deployment), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. The reservation only pays off when the steady volume exceeds the break-even point. Why the correct answer wins: Provisioned throughput reserves capacity so peak traffic is not throttled.
- **B:** Incorrect for this question. Matching the family to the measured workload avoids paying for capacity the model cannot use. Why the correct answer wins: Provisioned throughput reserves capacity so peak traffic is not throttled.
- **C:** Correct. Provisioned throughput reserves model capacity for predictable, high-volume traffic. In this case: Provisioned throughput reserves capacity so peak traffic is not throttled.
- **D:** Incorrect for this question. On-demand calls need no reservation and suit bursty, lower-volume traffic. Why the correct answer wins: Provisioned throughput reserves capacity so peak traffic is not throttled.

### Question 40 — D

Answer: Deploy the agent with its action groups and knowledge base. An agent carries its knowledge base, tools and instructions as one deployed unit. Local study-map skill 3.4 (Agents and Retrieval Runtime), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. Prompt Management versions templates so a prompt change is reviewable and reversible. Why the correct answer wins: An agent carries its knowledge base, tools and instructions as one deployed unit.
- **B:** Incorrect for this question. Persisted session state keeps multi-turn context without resending the whole history. Why the correct answer wins: An agent carries its knowledge base, tools and instructions as one deployed unit.
- **C:** Incorrect for this question. A sync re-indexes changed documents so retrieval does not serve stale passages. Why the correct answer wins: An agent carries its knowledge base, tools and instructions as one deployed unit.
- **D:** Correct. In this case: An agent carries its knowledge base, tools and instructions as one deployed unit.

### Question 41 — A

Answer: Store the container image in Amazon ECR. A registry stores the versioned image that the training service pulls. Local study-map skill 3.5 (Containers and Compute Provisioning), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Correct. In this case: A registry stores the versioned image that the training service pulls.
- **B:** Incorrect for this question. A custom image is needed only when the managed framework images cannot carry the dependencies. Why the correct answer wins: A registry stores the versioned image that the training service pulls.
- **C:** Incorrect for this question. CodeBuild runs the build and the automated tests in a clean managed environment. Why the correct answer wins: A registry stores the versioned image that the training service pulls.
- **D:** Incorrect for this question. ECS schedules the container on managed cluster capacity. Why the correct answer wins: A registry stores the versioned image that the training service pulls.

### Question 42 — B

Answer: Auto scale the endpoint on a target-tracking policy. Target tracking holds a chosen metric near its target as load moves. Target tracking holds a metric such as invocations per instance near a chosen value. Local study-map skill 3.6 (Autoscaling and Concurrency), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. A scale-to-zero policy removes the idle cost when nothing calls the endpoint. Why the correct answer wins: Target tracking holds a chosen metric near its target as load moves.
- **B:** Correct. Target tracking holds a metric such as invocations per instance near a chosen value. In this case: Target tracking holds a chosen metric near its target as load moves.
- **C:** Incorrect for this question. Provisioned concurrency pre-warms capacity so the burst does not meet a cold start. Why the correct answer wins: Target tracking holds a chosen metric near its target as load moves.
- **D:** Incorrect for this question. Step scaling adds capacity in bands as the alarm breaches, which suits sharp bursts. Why the correct answer wins: Target tracking holds a chosen metric near its target as load moves.

### Question 43 — A, D

Answers: Auto scale the endpoint on a target-tracking policy; Scale on GPU utilisation rather than invocation count. Target tracking follows load, and GPU utilisation reflects the real bottleneck. Target tracking holds a metric such as invocations per instance near a chosen value. GPU utilisation reflects the real bottleneck when each request is expensive. Local study-map skill 3.6 (Autoscaling and Concurrency), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Correct. Target tracking holds a metric such as invocations per instance near a chosen value. In this case: Target tracking follows load, and GPU utilisation reflects the real bottleneck.
- **B:** Incorrect for this question. Step scaling adds capacity in bands as the alarm breaches, which suits sharp bursts. Why the correct answer wins: Target tracking follows load, and GPU utilisation reflects the real bottleneck.
- **C:** Incorrect for this question. A warm pool removes the provisioning delay between consecutive training jobs. Why the correct answer wins: Target tracking follows load, and GPU utilisation reflects the real bottleneck.
- **D:** Correct. GPU utilisation reflects the real bottleneck when each request is expensive. In this case: Target tracking follows load, and GPU utilisation reflects the real bottleneck.
- **E:** Incorrect for this question. A scale-to-zero policy removes the idle cost when nothing calls the endpoint. Why the correct answer wins: Target tracking follows load, and GPU utilisation reflects the real bottleneck.

### Question 44 — A, B

Answers: Create an interface VPC endpoint for the service; Place the endpoint and model containers in private subnets. A private endpoint keeps service traffic inside the VPC, and private subnets remove the inbound internet path. A private endpoint keeps the service traffic inside the VPC without a NAT gateway. Private subnets remove the inbound internet path to the model hosts. Local study-map skill 3.7 (VPC Networking for Endpoints), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Correct. Private subnets remove the inbound internet path to the model hosts. In this case: A private endpoint keeps service traffic inside the VPC, and private subnets remove the inbound internet path.
- **B:** Correct. A private endpoint keeps the service traffic inside the VPC without a NAT gateway. In this case: A private endpoint keeps service traffic inside the VPC, and private subnets remove the inbound internet path.
- **C:** Incorrect for this question. A security group scoped to the caller subnet allows only the intended traffic. Why the correct answer wins: A private endpoint keeps service traffic inside the VPC, and private subnets remove the inbound internet path.
- **D:** Incorrect for this question. A NAT gateway gives private hosts outbound access without accepting inbound traffic. Why the correct answer wins: A private endpoint keeps service traffic inside the VPC, and private subnets remove the inbound internet path.
- **E:** Incorrect for this question. An open ingress rule exposes the model to anything that can reach the VPC. Why the correct answer wins: A private endpoint keeps service traffic inside the VPC, and private subnets remove the inbound internet path.

### Question 45 — B

Answer: Build and test the model image with AWS CodeBuild. A managed build service runs the build and the tests in a clean environment. Local study-map skill 3.8 (CI/CD Pipelines), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. CodePipeline sequences the build, test and deploy stages and records each outcome. Why the correct answer wins: A managed build service runs the build and the tests in a clean environment.
- **B:** Correct. In this case: A managed build service runs the build and the tests in a clean environment.
- **C:** Incorrect for this question. CodeDeploy performs the traffic shift and can roll back on an alarm. Why the correct answer wins: A managed build service runs the build and the tests in a clean environment.
- **D:** Incorrect for this question. CodeCommit is the managed Git repository the pipeline reads from. Why the correct answer wins: A managed build service runs the build and the tests in a clean environment.

### Question 46 — C, D

Answers: Orchestrate the release with AWS CodePipeline; Fail the pipeline when the evaluation threshold is missed. A pipeline sequences the stages, and a quality gate blocks a failing model. CodePipeline sequences the build, test and deploy stages and records each outcome. A quality gate blocks a release whose measured metric is below the agreed bar. Local study-map skill 3.8 (CI/CD Pipelines), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. CodeCommit is the managed Git repository the pipeline reads from. Why the correct answer wins: A pipeline sequences the stages, and a quality gate blocks a failing model.
- **B:** Incorrect for this question. CodeConnections lets the pipeline read a repository hosted elsewhere. Why the correct answer wins: A pipeline sequences the stages, and a quality gate blocks a failing model.
- **C:** Correct. A quality gate blocks a release whose measured metric is below the agreed bar. In this case: A pipeline sequences the stages, and a quality gate blocks a failing model.
- **D:** Correct. CodePipeline sequences the build, test and deploy stages and records each outcome. In this case: A pipeline sequences the stages, and a quality gate blocks a failing model.
- **E:** Incorrect for this question. CodeDeploy performs the traffic shift and can roll back on an alarm. Why the correct answer wins: A pipeline sequences the stages, and a quality gate blocks a failing model.

### Question 47 — C

Answer: Register the approved version in the SageMaker Model Registry. A model registry stores versions with their lineage and approval status. Local study-map skill 3.9 (Model Registry and Versioning), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. Run logging keeps parameters, metrics and artefacts comparable across experiments. Why the correct answer wins: A model registry stores versions with their lineage and approval status.
- **B:** Incorrect for this question. An approval gate stops a model from reaching production on an automated pass alone. Why the correct answer wins: A model registry stores versions with their lineage and approval status.
- **C:** Correct. In this case: A model registry stores versions with their lineage and approval status.
- **D:** Incorrect for this question. Prompt Management versions templates so a prompt change is reviewable and reversible. Why the correct answer wins: A model registry stores versions with their lineage and approval status.

### Question 48 — B

Answer: Send a small share of traffic to the new version first. A canary limits exposure to the small share it serves. A canary release limits the blast radius of a bad model to the canary share. Local study-map skill 3.10 (Deployment Strategy and Rollback), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. A single switch gives a bad model the whole traffic share at once. Why the correct answer wins: A canary limits exposure to the small share it serves.
- **B:** Correct. A canary release limits the blast radius of a bad model to the canary share. In this case: A canary limits exposure to the small share it serves.
- **C:** Incorrect for this question. A linear shift moves traffic gradually while the metrics are watched. Why the correct answer wins: A canary limits exposure to the small share it serves.
- **D:** Incorrect for this question. Mirroring collects comparison data with no user impact. Why the correct answer wins: A canary limits exposure to the small share it serves.

### Question 49 — D

Answer: Mirror traffic to the new model without serving its answers. Mirrored traffic collects comparison data with no user impact. Local study-map skill 3.10 (Deployment Strategy and Rollback), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. A canary release limits the blast radius of a bad model to the canary share. Why the correct answer wins: Mirrored traffic collects comparison data with no user impact.
- **B:** Incorrect for this question. A single switch gives a bad model the whole traffic share at once. Why the correct answer wins: Mirrored traffic collects comparison data with no user impact.
- **C:** Incorrect for this question. A live split answers which variant performs better on the real population. Why the correct answer wins: Mirrored traffic collects comparison data with no user impact.
- **D:** Correct. In this case: Mirrored traffic collects comparison data with no user impact.

### Question 50 — B

Answer: Define the workflow as a SageMaker pipeline. A SageMaker pipeline expresses those steps as one managed directed acyclic graph. A SageMaker pipeline expresses the processing, training and registration steps as one DAG. Local study-map skill 3.11 (Orchestration and Retraining), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. Step Functions coordinates long-running steps and service calls with retries and branching. Why the correct answer wins: A SageMaker pipeline expresses those steps as one managed directed acyclic graph.
- **B:** Correct. A SageMaker pipeline expresses the processing, training and registration steps as one DAG. In this case: A SageMaker pipeline expresses those steps as one managed directed acyclic graph.
- **C:** Incorrect for this question. CodePipeline sequences the build, test and deploy stages and records each outcome. Why the correct answer wins: A SageMaker pipeline expresses those steps as one managed directed acyclic graph.
- **D:** Incorrect for this question. A schedule starts the pipeline on a fixed cadence without an external cron host. Why the correct answer wins: A SageMaker pipeline expresses those steps as one managed directed acyclic graph.

### Question 51 — D

Answer: Enable a data drift monitor on the endpoint. A data drift monitor compares live inputs against the training baseline. Local study-map skill 4.1 (Drift and Model Monitoring), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. A quality monitor scores live predictions once the true labels arrive. Why the correct answer wins: A data drift monitor compares live inputs against the training baseline.
- **B:** Incorrect for this question. A bias monitor watches whether the outcome distribution shifts for a protected group. Why the correct answer wins: A data drift monitor compares live inputs against the training baseline.
- **C:** Incorrect for this question. Attribution drift shows that the model now relies on different features than it did. Why the correct answer wins: A data drift monitor compares live inputs against the training baseline.
- **D:** Correct. In this case: A data drift monitor compares live inputs against the training baseline.

### Question 52 — C, E

Answers: Enable a model quality monitor with ground-truth labels; Record a performance baseline and monitor drift against it. A quality monitor scores predictions once labels arrive, against a stored baseline. A stored baseline is the reference a drift monitor compares production against. Local study-map skill 4.1 (Drift and Model Monitoring), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. A data drift monitor compares the live request distribution against the training baseline. Why the correct answer wins: A quality monitor scores predictions once labels arrive, against a stored baseline.
- **B:** Incorrect for this question. An alarm on the endpoint metrics pages someone when the service degrades. Why the correct answer wins: A quality monitor scores predictions once labels arrive, against a stored baseline.
- **C:** Correct. In this case: A quality monitor scores predictions once labels arrive, against a stored baseline.
- **D:** Incorrect for this question. Generative AI observability records prompts, token counts and latency per model call. Why the correct answer wins: A quality monitor scores predictions once labels arrive, against a stored baseline.
- **E:** Correct. A stored baseline is the reference a drift monitor compares production against. In this case: A quality monitor scores predictions once labels arrive, against a stored baseline.

### Question 53 — B

Answer: Alarm on the CloudWatch latency and error metrics. An alarm on the endpoint metrics pages someone when the threshold is crossed. Local study-map skill 4.2 (Metrics and Dashboards), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. A dashboard puts the operating metrics in one view for the team. Why the correct answer wins: An alarm on the endpoint metrics pages someone when the threshold is crossed.
- **B:** Correct. In this case: An alarm on the endpoint metrics pages someone when the threshold is crossed.
- **C:** Incorrect for this question. Logs Insights filters and aggregates the request logs to find the failing pattern. Why the correct answer wins: An alarm on the endpoint metrics pages someone when the threshold is crossed.
- **D:** Incorrect for this question. X-Ray shows where a request spends its time across the services it touches. Why the correct answer wins: An alarm on the endpoint metrics pages someone when the threshold is crossed.

### Question 54 — D

Answer: Query the inference logs with CloudWatch Logs Insights. Log querying filters and aggregates the request logs to expose the pattern. Logs Insights filters and aggregates the request logs to find the failing pattern. Local study-map skill 4.2 (Metrics and Dashboards), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. An alarm on the endpoint metrics pages someone when the service degrades. Why the correct answer wins: Log querying filters and aggregates the request logs to expose the pattern.
- **B:** Incorrect for this question. A dashboard puts the operating metrics in one view for the team. Why the correct answer wins: Log querying filters and aggregates the request logs to expose the pattern.
- **C:** Incorrect for this question. Config records how each resource was configured and evaluates it against rules. Why the correct answer wins: Log querying filters and aggregates the request logs to expose the pattern.
- **D:** Correct. Logs Insights filters and aggregates the request logs to find the failing pattern. In this case: Log querying filters and aggregates the request logs to expose the pattern.

### Question 55 — B

Answer: Enable CloudWatch generative AI observability for the model calls. Generative AI observability records prompts, tokens and latency per call. Local study-map skill 4.3 (GenAI Observability), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. An alarm on the endpoint metrics pages someone when the service degrades. Why the correct answer wins: Generative AI observability records prompts, tokens and latency per call.
- **B:** Correct. In this case: Generative AI observability records prompts, tokens and latency per call.
- **C:** Incorrect for this question. Agent tracing shows which tool call failed or stalled inside a multi-step task. Why the correct answer wins: Generative AI observability records prompts, tokens and latency per call.
- **D:** Incorrect for this question. X-Ray shows where a request spends its time across the services it touches. Why the correct answer wins: Generative AI observability records prompts, tokens and latency per call.

### Question 56 — A

Answer: Cover the steady inference load with a Savings Plan. A Savings Plan discounts a predictable hourly spend on eligible compute. Local study-map skill 4.4 (Cost Optimisation and Purchasing), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Correct. In this case: A Savings Plan discounts a predictable hourly spend on eligible compute.
- **B:** Incorrect for this question. Matching the family to the measured workload avoids paying for capacity the model cannot use. Why the correct answer wins: A Savings Plan discounts a predictable hourly spend on eligible compute.
- **C:** Incorrect for this question. Cost Explorer groups the bill by service and by tag so the expensive resource is visible. Why the correct answer wins: A Savings Plan discounts a predictable hourly spend on eligible compute.
- **D:** Incorrect for this question. Batch scoring removes the idle endpoint that an always-on deployment would keep. Why the correct answer wins: A Savings Plan discounts a predictable hourly spend on eligible compute.

### Question 57 — C, D

Answers: Right-size the instance family against the measured latency; Cover the steady inference load with a Savings Plan. Right-sizing matches capacity to the measured workload, and the plan discounts steady hours. Matching the family to the measured workload avoids paying for capacity the model cannot use. A Savings Plan discounts a predictable hourly spend on eligible compute. Local study-map skill 4.4 (Cost Optimisation and Purchasing), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. A scale-to-zero policy removes the idle cost when nothing calls the endpoint. Why the correct answer wins: Right-sizing matches capacity to the measured workload, and the plan discounts steady hours.
- **B:** Incorrect for this question. An open ingress rule exposes the model to anything that can reach the VPC. Why the correct answer wins: Right-sizing matches capacity to the measured workload, and the plan discounts steady hours.
- **C:** Correct. A Savings Plan discounts a predictable hourly spend on eligible compute. In this case: Right-sizing matches capacity to the measured workload, and the plan discounts steady hours.
- **D:** Correct. Matching the family to the measured workload avoids paying for capacity the model cannot use. In this case: Right-sizing matches capacity to the measured workload, and the plan discounts steady hours.
- **E:** Incorrect for this question. Sizing every request for the hardest case spends latency and money on easy requests. Why the correct answer wins: Right-sizing matches capacity to the measured workload, and the plan discounts steady hours.

### Question 58 — C

Answer: Cap the output tokens per request. Output tokens dominate generation cost, so a cap bounds spend per call. Local study-map skill 4.5 (Inference Cost and Token Usage), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. Re-embedding an unchanged document is wasted spend on every refresh. Why the correct answer wins: Output tokens dominate generation cost, so a cap bounds spend per call.
- **B:** Incorrect for this question. Routing easy requests to a cheaper model keeps the large model for hard cases. Why the correct answer wins: Output tokens dominate generation cost, so a cap bounds spend per call.
- **C:** Correct. In this case: Output tokens dominate generation cost, so a cap bounds spend per call.
- **D:** Incorrect for this question. Sending fewer retrieved tokens lowers both cost and latency on every call. Why the correct answer wins: Output tokens dominate generation cost, so a cap bounds spend per call.

### Question 59 — A

Answer: Trim the retrieved context sent to the model. Sending fewer retrieved tokens lowers cost and latency on every call. Local study-map skill 4.5 (Inference Cost and Token Usage), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Correct. In this case: Sending fewer retrieved tokens lowers cost and latency on every call.
- **B:** Incorrect for this question. The reservation only pays off when the steady volume exceeds the break-even point. Why the correct answer wins: Sending fewer retrieved tokens lowers cost and latency on every call.
- **C:** Incorrect for this question. Re-embedding an unchanged document is wasted spend on every refresh. Why the correct answer wins: Sending fewer retrieved tokens lowers cost and latency on every call.
- **D:** Incorrect for this question. Output tokens dominate generation cost, so a cap bounds the spend per call. Why the correct answer wins: Sending fewer retrieved tokens lowers cost and latency on every call.

### Question 60 — C

Answer: Attach a policy scoped to the one bucket prefix. Scoping to the prefix stops a compromised job from reaching the wider lake. Local study-map skill 4.6 (IAM and Credentials), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. A group policy keeps the shared permission set in one reviewable place. Why the correct answer wins: Scoping to the prefix stops a compromised job from reaching the wider lake.
- **B:** Incorrect for this question. An execution role grants the job only the permissions its inputs and outputs need. Why the correct answer wins: Scoping to the prefix stops a compromised job from reaching the wider lake.
- **C:** Correct. In this case: Scoping to the prefix stops a compromised job from reaching the wider lake.
- **D:** Incorrect for this question. The root user cannot be limited by policy, so daily use magnifies any mistake. Why the correct answer wins: Scoping to the prefix stops a compromised job from reaching the wider lake.

### Question 61 — A, E

Answers: Create a role the other account can assume; Give the training job a scoped IAM execution role. A role assumption issues temporary credentials, and the execution role scopes what the job can do. A cross-account role issues temporary credentials without sharing a key. An execution role grants the job only the permissions its inputs and outputs need. Local study-map skill 4.6 (IAM and Credentials), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Correct. A cross-account role issues temporary credentials without sharing a key. In this case: A role assumption issues temporary credentials, and the execution role scopes what the job can do.
- **B:** Incorrect for this question. A group policy keeps the shared permission set in one reviewable place. Why the correct answer wins: A role assumption issues temporary credentials, and the execution role scopes what the job can do.
- **C:** Incorrect for this question. The root user cannot be limited by policy, so daily use magnifies any mistake. Why the correct answer wins: A role assumption issues temporary credentials, and the execution role scopes what the job can do.
- **D:** Incorrect for this question. A long-lived key keeps working after the project ends unless someone retires it. Why the correct answer wins: A role assumption issues temporary credentials, and the execution role scopes what the job can do.
- **E:** Correct. An execution role grants the job only the permissions its inputs and outputs need. In this case: A role assumption issues temporary credentials, and the execution role scopes what the job can do.

### Question 62 — A

Answer: Place the endpoint and model containers in private subnets. Private subnets remove the inbound internet path to the model hosts. Local study-map skill 4.7 (Network Isolation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Correct. In this case: Private subnets remove the inbound internet path to the model hosts.
- **B:** Incorrect for this question. A private endpoint keeps the service traffic inside the VPC without a NAT gateway. Why the correct answer wins: Private subnets remove the inbound internet path to the model hosts.
- **C:** Incorrect for this question. A NAT gateway gives private hosts outbound access without accepting inbound traffic. Why the correct answer wins: Private subnets remove the inbound internet path to the model hosts.
- **D:** Incorrect for this question. An open ingress rule exposes the model to anything that can reach the VPC. Why the correct answer wins: Private subnets remove the inbound internet path to the model hosts.

### Question 63 — A

Answer: Encrypt the artefacts with a customer managed KMS key. A customer managed key puts the key policy and revocation decision with the team. A customer managed key lets the team control the key policy and revoke access. Local study-map skill 4.8 (Encryption and Secrets), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Correct. A customer managed key lets the team control the key policy and revoke access. In this case: A customer managed key puts the key policy and revocation decision with the team.
- **B:** Incorrect for this question. Config records how each resource was configured and evaluates it against rules. Why the correct answer wins: A customer managed key puts the key policy and revocation decision with the team.
- **C:** Incorrect for this question. Secrets Manager holds the credential centrally and can rotate it. Why the correct answer wins: A customer managed key puts the key policy and revocation decision with the team.
- **D:** Incorrect for this question. Guardrails filters denied topics, sensitive data and unsafe content in the response path. Why the correct answer wins: A customer managed key puts the key policy and revocation decision with the team.

### Question 64 — C

Answer: Apply Amazon Bedrock Guardrails to the model responses. Guardrails filters denied topics and sensitive data in the response path. Local study-map skill 4.9 (Guardrails and Responsible AI), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. Redaction at the boundary keeps personal data out of the model request entirely. Why the correct answer wins: Guardrails filters denied topics and sensitive data in the response path.
- **B:** Incorrect for this question. Safety screening keeps prohibited material out of the model weights. Why the correct answer wins: Guardrails filters denied topics and sensitive data in the response path.
- **C:** Correct. In this case: Guardrails filters denied topics and sensitive data in the response path.
- **D:** Incorrect for this question. Inspector reports known vulnerabilities in the image before it is deployed. Why the correct answer wins: Guardrails filters denied topics and sensitive data in the response path.

### Question 65 — B

Answer: Record the API calls with AWS CloudTrail. The audit trail records who called which API, when and from where. Local study-map skill 4.10 (Audit and Vulnerability Scanning), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. Config records how each resource was configured and evaluates it against rules. Why the correct answer wins: The audit trail records who called which API, when and from where.
- **B:** Correct. In this case: The audit trail records who called which API, when and from where.
- **C:** Incorrect for this question. Logs Insights filters and aggregates the request logs to find the failing pattern. Why the correct answer wins: The audit trail records who called which API, when and from where.
- **D:** Incorrect for this question. X-Ray shows where a request spends its time across the services it touches. Why the correct answer wins: The audit trail records who called which API, when and from where.
