# AWS Certified Machine Learning Engineer – Associate (MLA-C02) — Full-Length Mock Exam 3

Machine Learning Engineer · 65 questions · 130 minutes · scaled passing score 720 of 1000

Blueprint-weighted mock exam. Item mix: 50 multiple-choice and 15 multiple-response items (the selection count is stated in each multi-response stem). The published exam has 65 questions in 130 minutes, of which 50 are scored and 15 are unscored, and AWS does not identify the unscored items. AWS publishes no split between multiple-choice and multiple-response items, so the 15-item multi-response block is an authoring choice. At 65 items in 130 minutes this set matches the published pacing at about 120 seconds per item. AWS is currently delivering MLA-C02 as a beta of 85 questions in 170 minutes with the extra items unscored; this set follows the published 65-question form. The published format has no case-study component, so no case-study item appears here. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied AWS exam items.

## Questions

---

## Domain 1 — Data Preparation for ML and AI (28%) — Ingestion, storage, feature engineering, embeddings, and data quality

### 1. Pathology images are analysed once at ingest and then read repeatedly for training, so storage cost per terabyte now dominates the budget. What should the stored format and location be?

- A. Land the dataset as Parquet in Amazon S3
- B. Land the raw JSON events in Amazon S3 unchanged
- C. Attach a gp3 Amazon EBS volume to the training instance
- D. Use Amazon FSx for Lustre for the training file system

### 2. A notebook cluster of six hosts must read and write the same small set of clinical reference tables concurrently. What storage fits?

- A. Mount a shared Amazon EFS file system on every training host
- B. Use S3 Intelligent-Tiering for the unevenly accessed corpus
- C. Use Amazon FSx for Lustre for the training file system
- D. Attach a gp3 Amazon EBS volume to the training instance

### 3. Wearable readings must land in the lake within a minute as compact objects, with no consumer application to operate. What fits?

- A. Ingest the events with Amazon Kinesis Data Streams
- B. Deliver the stream to Amazon S3 with Amazon Data Firehose
- C. Transform each stream record with AWS Lambda
- D. Ingest the events through Amazon MSK

### 4. Archived trial documents are read perhaps twice a year but must be kept for a decade at the lowest storage price. What fits?

- A. Apply S3 Object Lock to the regulated training data
- B. Archive the raw corpus to an S3 Glacier storage class
- C. Use S3 Intelligent-Tiering for the unevenly accessed corpus
- D. Expire intermediate artefacts with an S3 lifecycle rule

### 5. A study reads one patient cohort and one date range per training job from a bucket that holds twelve years of records. What should the layout support?

- A. Use Amazon FSx for Lustre for the training file system
- B. Land the raw JSON events in Amazon S3 unchanged
- C. Land the dataset as Parquet in Amazon S3
- D. Partition the S3 prefix by event date

### 6. The raw device payloads must be preserved byte for byte for regulatory re-analysis, even after the cleaned version exists. Why keep them in their original form?

- A. Apply S3 Object Lock to the regulated training data
- B. Land the dataset as Parquet in Amazon S3
- C. Attach a gp3 Amazon EBS volume to the training instance
- D. Land the raw JSON events in Amazon S3 unchanged

### 7. Clinical extracts from four hospitals must be normalised on a schedule with no cluster to operate, and the result must be discoverable from Athena. Which two services fit? Select two.

- A. Profile and clean the data with AWS Glue DataBrew
- B. Transform each stream record with AWS Lambda
- C. Process the data with Spark on Amazon EMR
- D. Transform the data with an AWS Glue ETL job
- E. Register the tables in the AWS Glue Data Catalog

### 8. Each arriving sensor record needs a light unit conversion and a validity filter before it is stored. What fits?

- A. Transform the data with an AWS Glue ETL job
- B. Prepare the data in SageMaker Data Wrangler
- C. Process the data with Spark on Amazon EMR
- D. Transform each stream record with AWS Lambda

### 9. A triage endpoint must read the latest vitals summary for a patient with minimal latency at request time. What serves that read?

- A. Publish the features to the SageMaker Feature Store online store
- B. Ingest the cleaned rows into a SageMaker Feature Group
- C. Register the tables in the AWS Glue Data Catalog
- D. Keep the point-in-time history in the Feature Store offline store

### 10. Vitals are missing for some admissions because a monitor was not attached, and those rows must still be usable. What should be done?

- A. Impute missing numeric values with the median
- B. Drop every row that has any missing field
- C. Clip extreme outliers to a defined percentile
- D. Bin the continuous age column into ranges

### 11. Columns range from heart rate to lab concentrations in different units, and the rare positive outcome must appear in every split. Which two steps fit? Select two.

- A. Standardise the numeric columns before training
- B. Stratify the train, validation and test splits by label
- C. Bin the continuous age column into ranges
- D. Shuffle the rows before every epoch
- E. Remove duplicate rows before splitting

### 12. Ninety million radiology report chunks are searched occasionally for research, and the cost of an always-on index is not justified. What fits?

- A. Index the vectors in Amazon OpenSearch Service with k-NN search
- B. Keep the vectors in Amazon S3 with a vector index
- C. Load every vector into the application process on each request
- D. Store the vectors in Amazon RDS for PostgreSQL with pgvector

### 13. A clinician must find prior scans that resemble a new image, and the same index must answer text descriptions of findings. Which two components fit? Select two.

- A. Combine keyword and vector retrieval
- B. Store the vectors in Amazon RDS for PostgreSQL with pgvector
- C. Index the vectors in Amazon OpenSearch Service with k-NN search
- D. Generate the embeddings with an Amazon Bedrock embedding model
- E. Embed the images and captions with one multimodal model

### 14. Training transcripts contain patient names and record numbers that must never influence the model or appear in output. What should happen first?

- A. Tokenise the text with the target model tokeniser
- B. Store source, date and section metadata with each chunk
- C. Mask and redact personal identifiers before training
- D. Chunk the documents on semantic boundaries such as headings

### 15. A nightly load must fail rather than train when a required field is null, and later drift comparison needs the accepted statistics stored. Which two controls fit? Select two.

- A. Evaluate AWS Glue Data Quality rules on the prepared table
- B. Enforce a schema contract on the ingested records
- C. Expire intermediate artefacts with an S3 lifecycle rule
- D. Profile the incoming data and store the statistics as a baseline
- E. Profile and clean the data with AWS Glue DataBrew

### 16. Radiologists must label a balanced sample of scans with a second-reader review process. What fits?

- A. Send the unlabelled records to Amazon SageMaker Ground Truth
- B. Use automated data labelling with a human review sample in Ground Truth
- C. Mask and redact personal identifiers before training
- D. Remove duplicate rows before splitting

### 17. A multimodal diagnostic set has far more images than matching text reports, and the text branch is under-trained. What should be addressed?

- A. Reweight the under-represented group in the loss
- B. Measure bias with SageMaker Clarify before training
- C. Rebalance the numeric, text and image assets in the set
- D. Stratify the train, validation and test splits by label

### 18. A handful of device readings report heart rates in the thousands because of a firmware fault, and they dominate the loss. What should be applied?

- A. Drop every row that has any missing field
- B. Clip extreme outliers to a defined percentile
- C. Impute missing numeric values with the median
- D. Generate synthetic minority samples to rebalance the classes

---

## Domain 2 — ML Model and Foundation Model (FM) Development (24%) — Model and FM selection, tuning, customisation, and evaluation

### 19. A dosage relationship is close to linear, must be auditable, and has few features and modest data. Which model fits?

- A. Use Random Cut Forest for anomaly scoring
- B. Train the tabular classifier with the XGBoost built-in algorithm
- C. Forecast the series with the DeepAR algorithm
- D. Train with the linear learner algorithm

### 20. Three separately trained readmission models each score well, and the team wants the most accurate single result available for launch. What fits?

- A. Average several models into an ensemble
- B. Train with the linear learner algorithm
- C. Use the k-nearest-neighbours algorithm
- D. Train the tabular classifier with the XGBoost built-in algorithm

### 21. Trial eligibility notes must be converted into vectors for similarity search without hosting any model. What fits?

- A. Select an Amazon Nova foundation model in Amazon Bedrock
- B. Select an Anthropic Claude model in Amazon Bedrock
- C. Select a Titan embedding model in Amazon Bedrock
- D. Download open weights and host them on your own endpoint

### 22. A clinical summariser must reason over a forty-page discharge packet in one request. Which model choice fits?

- A. Download open weights and host them on your own endpoint
- B. Select an Amazon Nova foundation model in Amazon Bedrock
- C. Select a Titan embedding model in Amazon Bedrock
- D. Select an Anthropic Claude model in Amazon Bedrock

### 23. A large model writes excellent summaries but is too slow and costly to serve at ward scale, and the summaries must stay close in quality. What fits?

- A. Distil the large model into a smaller student model
- B. Run full-parameter fine-tuning on the curated corpus
- C. Fine-tune with parameter-efficient adapters such as LoRA
- D. Run continued pre-training on the domain corpus

### 24. The model must learn hospital-specific abbreviations, and the tuning budget covers only a small number of trainable parameters. Which two techniques fit? Select two.

- A. Run full-parameter fine-tuning on the curated corpus
- B. Start with task-specific prompt engineering before any training
- C. Distil the large model into a smaller student model
- D. Fine-tune with parameter-efficient adapters such as LoRA
- E. Run continued pre-training on the domain corpus

### 25. Retrieval matches short sentences well, but the answer needs the surrounding protocol section for context. What pattern fits?

- A. Index parent sections and retrieve their child chunks
- B. Store source, date and section metadata with each chunk
- C. Split the documents into fixed-size overlapping chunks
- D. Chunk the documents on semantic boundaries such as headings

### 26. Twelve thousand clinician dictations must become searchable text with speaker labels. What fits?

- A. Extract the form fields with Amazon Textract
- B. Detect entities and sentiment with Amazon Comprehend
- C. Detect objects and text in images with Amazon Rekognition
- D. Transcribe the calls with Amazon Transcribe

### 27. The training script depends on a compiled imaging library that no managed framework image includes. What is required?

- A. Start from a SageMaker JumpStart model
- B. Train the tabular classifier with the XGBoost built-in algorithm
- C. Bring a custom training container image
- D. Package the training code in script mode with a supported framework

### 28. Every trial runs its full epoch budget even when validation has not improved for fifteen rounds, and the tuning bill is dominated by wasted epochs. What fits?

- A. Enable early stopping on the validation metric
- B. Tune hyperparameters with SageMaker automatic model tuning
- C. Run a hand-written grid of training jobs
- D. Define the tuning objective on the validation metric that matters

### 29. Tuning must be a managed search, and it must optimise the metric that reflects clinical review capacity rather than raw accuracy. Which two elements fit? Select two.

- A. Define the tuning objective on the validation metric that matters
- B. Use random search over a small range
- C. Tune hyperparameters with SageMaker automatic model tuning
- D. Run a hand-written grid of training jobs
- E. Enable early stopping on the validation metric

### 30. A single model no longer fits on one device, and a reclaimed instance must not restart the run. Which two changes fit? Select two.

- A. Run training on managed Spot training capacity
- B. Checkpoint to Amazon S3 so an interrupted job resumes
- C. Keep a managed warm pool for the training cluster
- D. Split each batch across instances with data parallelism
- E. Shard the model across instances with model parallelism

### 31. A screening model for a two percent condition is being reported as 97 percent accurate, and the team is about to declare success. Which reported metric is misleading here?

- A. Report ROC-AUC for the ranking task
- B. Report accuracy alone on a 2 percent positive class
- C. Report F1 on the holdout set
- D. Pick the threshold from the precision-recall curve

### 32. The screening model must be reported with one balanced score, and reviewers need the counts of missed and false alarms. Which two outputs fit? Select two.

- A. Inspect the confusion matrix on the minority class
- B. Report RMSE for the regression
- C. Report accuracy alone on a 2 percent positive class
- D. Report F1 on the holdout set
- E. Score the generated summaries with BLEU

### 33. A judge model is already scoring summaries, and the clinical board requires proof that the judge agrees with experts. What must be added?

- A. Score the generated summaries with ROUGE
- B. Add a human review loop for a sample of answers
- C. Use an LLM-as-a-judge rubric for the open-ended answers
- D. Score the answers with BERTScore

### 34. A research team runs the same experiment weekly and cannot compare parameters, metrics and artefacts across runs. What fits?

- A. Store the prompt templates in Amazon Bedrock Prompt Management
- B. Register the approved version in the SageMaker Model Registry
- C. Log runs with MLflow on SageMaker AI
- D. Run an Amazon Bedrock model evaluation job

---

## Domain 3 — Deployment and Orchestration of ML and AI Workflows (24%) — Inference infrastructure, scaling, CI/CD, and orchestration

### 35. A research tool calls a diagnostic model a few times an hour and may sit idle for days. What fits?

- A. Use asynchronous inference with results written to Amazon S3
- B. Run a batch transform job over the stored records
- C. Deploy a serverless inference endpoint
- D. Deploy a real-time SageMaker AI endpoint

### 36. The ward application needs an immediate answer per patient, and a separate nightly job must score the full cohort. Which two methods fit? Select two.

- A. Use asynchronous inference with results written to Amazon S3
- B. Host many small models behind one multi-model endpoint
- C. Run a batch transform job over the stored records
- D. Deploy a real-time SageMaker AI endpoint
- E. Deploy a serverless inference endpoint

### 37. Each hospital site has its own small readmission model, and one endpoint per site is unaffordable at their call volume. What fits?

- A. Run several containers behind one endpoint
- B. Host many small models behind one multi-model endpoint
- C. Deploy a real-time SageMaker AI endpoint
- D. Run a batch transform job over the stored records

### 38. The ward assistant meets its latency target on an untested instance family, and the team must choose the cheapest family that holds that latency. What should be used?

- A. Compare provisioned throughput against on-demand spend
- B. Call the Bedrock model on demand
- C. Import the fine-tuned weights with Bedrock custom model import
- D. Right-size the endpoint with SageMaker Inference Recommender

### 39. A pilot team calls a hosted model a few hundred times a day and cannot forecast volume. What fits?

- A. Compare provisioned throughput against on-demand spend
- B. Import the fine-tuned weights with Bedrock custom model import
- C. Call the Bedrock model on demand
- D. Buy provisioned throughput for the Bedrock model

### 40. Guidelines are updated every Monday, and the assistant keeps answering from last month's text. What should be scheduled?

- A. Store the prompt templates in Amazon Bedrock Prompt Management
- B. Persist the agent session state between turns
- C. Schedule a knowledge base sync when documents change
- D. Deploy the agent with its action groups and knowledge base

### 41. The inference container must run continuously behind a load balancer with rolling replacements. What fits?

- A. Serve the model from an AWS Lambda function
- B. Run the container on Amazon ECS
- C. Run the job on AWS Batch
- D. Run the container on Amazon EKS

### 42. Each request occupies a GPU for several seconds, so invocation count barely changes while the queue grows. What should the scaling policy track?

- A. Auto scale the endpoint on a target-tracking policy
- B. Scale on GPU utilisation rather than invocation count
- C. Auto scale on a step policy with CloudWatch alarms
- D. Scale the endpoint to zero outside business hours

### 43. Load rises smoothly through the morning clinic, and the first patient of the day must not wait for a cold start. Which two settings fit? Select two.

- A. Auto scale on a step policy with CloudWatch alarms
- B. Keep provisioned concurrency ready for the burst window
- C. Keep a managed warm pool for the training cluster
- D. Auto scale the endpoint on a target-tracking policy
- E. Scale the endpoint to zero outside business hours

### 44. The imaging endpoint must have no inbound internet path and must reach S3 through a private endpoint. Where should it be placed?

- A. Restrict the security group to the application subnet
- B. Allow ingress from any address on the endpoint port
- C. Place the endpoint and model containers in private subnets
- D. Route the private subnet through a NAT gateway

### 45. Every commit must build and test the model image, and a model that fails its evaluation must not proceed. Which two elements fit? Select two.

- A. Shift traffic with AWS CodeDeploy
- B. Build and test the model image with AWS CodeBuild
- C. Orchestrate the release with AWS CodePipeline
- D. Keep the pipeline source in AWS CodeCommit
- E. Fail the pipeline when the evaluation threshold is missed

### 46. Traffic must shift to the new model version in steps and roll back when an alarm fires. What fits?

- A. Build and test the model image with AWS CodeBuild
- B. Shift traffic with AWS CodeDeploy
- C. Connect the external repository with AWS CodeConnections
- D. Orchestrate the release with AWS CodePipeline

### 47. Each approved model must link to its training run, its data snapshot and the approver. What fits?

- A. Keep the pipeline source in AWS CodeCommit
- B. Log runs with MLflow on SageMaker AI
- C. Store the prompt templates in Amazon Bedrock Prompt Management
- D. Register the approved version in the SageMaker Model Registry

### 48. A new triage model must be scored against live cases for a month with no clinician seeing its recommendation. What fits?

- A. Mirror traffic to the new model without serving its answers
- B. Send a small share of traffic to the new version first
- C. Stand the new version beside the old and switch traffic
- D. Replace the production version in a single switch

### 49. The board requires a human sign-off before any new triage version serves patients, and the first exposure must be small. Which two controls fit? Select two.

- A. Replace the production version in a single switch
- B. Require a manual approval before the version is deployed
- C. Mirror traffic to the new model without serving its answers
- D. Shift traffic to the new version in equal steps
- E. Send a small share of traffic to the new version first

### 50. Training must wait for a human approval, then run a long evaluation, then branch on the result, across several AWS services. What fits?

- A. Orchestrate the release with AWS CodePipeline
- B. Orchestrate the steps with AWS Step Functions
- C. Define the workflow as a SageMaker pipeline
- D. Trigger the retraining run with an EventBridge schedule

---

## Domain 4 — Operating, Monitoring, and Securing ML and AI Solutions (24%) — Monitoring, cost control, identity, network isolation, and guardrails

### 51. Input distributions are unchanged, yet the model now relies on a lab value that used to be ignored. What should be monitored?

- A. Enable feature attribution drift monitoring
- B. Enable a data drift monitor on the endpoint
- C. Enable a model quality monitor with ground-truth labels
- D. Enable a bias drift monitor

### 52. A new scanner changes the pixel distribution, and readmission labels arrive after thirty days. Which two monitors fit? Select two.

- A. Enable a bias drift monitor
- B. Alarm on the CloudWatch latency and error metrics
- C. Enable a data drift monitor on the endpoint
- D. Enable a model quality monitor with ground-truth labels
- E. Enable feature attribution drift monitoring

### 53. Requests failed between two and three yesterday, and the team needs the shared failing field across a million log lines. What fits?

- A. Alarm on the CloudWatch latency and error metrics
- B. Trace the pipeline service calls with AWS X-Ray
- C. Query the inference logs with CloudWatch Logs Insights
- D. Build a CloudWatch dashboard for the pipeline metrics

### 54. A request crosses an API, a preprocessing service and an endpoint, and nobody can say which hop adds the delay. What fits?

- A. Track resource configuration with AWS Config
- B. Trace the pipeline service calls with AWS X-Ray
- C. Query the inference logs with CloudWatch Logs Insights
- D. Build a CloudWatch dashboard for the pipeline metrics

### 55. Prompt and completion token counts must be recorded for every assistant call so weekly cost reviews are possible. What fits?

- A. Trace agent tool calls with Bedrock AgentCore Observability
- B. Enable CloudWatch generative AI observability for the model calls
- C. Alarm on the CloudWatch latency and error metrics
- D. Trace the pipeline service calls with AWS X-Ray

### 56. The endpoint meets its latency target on an instance family that is twice the measured requirement. What should be done?

- A. Break the spend down by endpoint with AWS Cost Explorer
- B. Cover the steady inference load with a Savings Plan
- C. Scale the endpoint to zero outside business hours
- D. Right-size the instance family against the measured latency

### 57. A steady year-round inference load needs a lower rate, and finance needs to see which model drives the bill. Which two tools fit? Select two.

- A. Break the spend down by endpoint with AWS Cost Explorer
- B. Set an AWS Budget alert on the ML account
- C. Right-size the instance family against the measured latency
- D. Cover the steady inference load with a Savings Plan
- E. Move the offline scoring to batch transform

### 58. Most requests are simple lookups while a few need deep reasoning, and every request currently goes to the largest model. What should be added?

- A. Route routine requests to a smaller model
- B. Cap the output tokens per request
- C. Cache embeddings for documents that have not changed
- D. Trim the retrieved context sent to the model

### 59. Twelve retrieved passages are sent on every call, and evaluation shows that only the first three are ever used. What should change?

- A. Compare provisioned throughput against on-demand spend
- B. Cap the output tokens per request
- C. Trim the retrieved context sent to the model
- D. Cache embeddings for documents that have not changed

### 60. A pipeline currently runs with the account root credentials and with a key created three years ago. Which two practices must stop? Select two.

- A. Create a long-lived access key for the integration
- B. Attach one policy to an IAM group the engineers belong to
- C. Use the account root user for pipeline administration
- D. Create a role the other account can assume
- E. Give the training job a scoped IAM execution role

### 61. Twenty researchers need an identical read-only permission set that is reviewed each quarter. What should be created?

- A. Attach one policy to an IAM group the engineers belong to
- B. Create a long-lived access key for the integration
- C. Use the account root user for pipeline administration
- D. Create a role the other account can assume

### 62. The endpoint security group currently accepts traffic from any address, and only the application subnet should reach it. What should change?

- A. Allow ingress from any address on the endpoint port
- B. Create an interface VPC endpoint for the service
- C. Restrict the security group to the application subnet
- D. Place the endpoint and model containers in private subnets

### 63. Recorded consultations used for training must be encrypted with a key the hospital can revoke when consent is withdrawn. What fits?

- A. Store the model API credential in AWS Secrets Manager
- B. Track resource configuration with AWS Config
- C. Apply Amazon Bedrock Guardrails to the model responses
- D. Encrypt the artefacts with a customer managed KMS key

### 64. Identifiers must never reach the model at all, even if the model would not repeat them. What should be applied?

- A. Screen the training text for unsafe content
- B. Apply Amazon Bedrock Guardrails to the model responses
- C. Configure a denied-topics policy for the assistant
- D. Redact personal data before the prompt reaches the model

### 65. Every training bucket must be shown to have had encryption enabled continuously for the last year. What fits?

- A. Query the inference logs with CloudWatch Logs Insights
- B. Record the API calls with AWS CloudTrail
- C. Scan the built image with Amazon Inspector
- D. Track resource configuration with AWS Config

---

## Answer key and explanations

### Question 1 — A

Answer: Land the dataset as Parquet in Amazon S3. A columnar, compressed object format in S3 lowers cost per terabyte for repeated scans. Columnar Parquet files in S3 are read in column subsets, which suits repeated training scans. Local study-map skill 1.1 (Ingestion Sources and Storage Choice), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Correct. Columnar Parquet files in S3 are read in column subsets, which suits repeated training scans. In this case: A columnar, compressed object format in S3 lowers cost per terabyte for repeated scans.
- **B:** Incorrect for this question. Raw JSON is readable but forces every query to parse whole records. Why the correct answer wins: A columnar, compressed object format in S3 lowers cost per terabyte for repeated scans.
- **C:** Incorrect for this question. EBS is block storage bound to one instance, which suits a single host and not a fleet. Why the correct answer wins: A columnar, compressed object format in S3 lowers cost per terabyte for repeated scans.
- **D:** Incorrect for this question. Lustre delivers the high throughput a multi-node training job needs from shared storage. Why the correct answer wins: A columnar, compressed object format in S3 lowers cost per terabyte for repeated scans.

### Question 2 — A

Answer: Mount a shared Amazon EFS file system on every training host. A shared file system gives every host the same concurrent view. EFS gives many hosts one POSIX file system, which suits shared code and small data. Local study-map skill 1.1 (Ingestion Sources and Storage Choice), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Correct. EFS gives many hosts one POSIX file system, which suits shared code and small data. In this case: A shared file system gives every host the same concurrent view.
- **B:** Incorrect for this question. Intelligent-Tiering moves objects between access tiers as usage changes, with no rules to write. Why the correct answer wins: A shared file system gives every host the same concurrent view.
- **C:** Incorrect for this question. Lustre delivers the high throughput a multi-node training job needs from shared storage. Why the correct answer wins: A shared file system gives every host the same concurrent view.
- **D:** Incorrect for this question. EBS is block storage bound to one instance, which suits a single host and not a fleet. Why the correct answer wins: A shared file system gives every host the same concurrent view.

### Question 3 — B

Answer: Deliver the stream to Amazon S3 with Amazon Data Firehose. A delivery stream batches the readings into objects without a consumer to run. Local study-map skill 1.2 (Streaming Ingestion), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Kinesis holds an ordered stream that several consumers can read at their own pace. Why the correct answer wins: A delivery stream batches the readings into objects without a consumer to run.
- **B:** Correct. In this case: A delivery stream batches the readings into objects without a consumer to run.
- **C:** Incorrect for this question. A function per record suits lightweight enrichment and filtering of a stream. Why the correct answer wins: A delivery stream batches the readings into objects without a consumer to run.
- **D:** Incorrect for this question. MSK runs managed Kafka, which suits teams already using Kafka clients and topics. Why the correct answer wins: A delivery stream batches the readings into objects without a consumer to run.

### Question 4 — B

Answer: Archive the raw corpus to an S3 Glacier storage class. An archive class is priced for data that is kept but rarely read. Local study-map skill 1.3 (Storage Class and Retention), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Object Lock prevents the retained objects from being altered or deleted for the stated period. Why the correct answer wins: An archive class is priced for data that is kept but rarely read.
- **B:** Correct. In this case: An archive class is priced for data that is kept but rarely read.
- **C:** Incorrect for this question. Intelligent-Tiering moves objects between access tiers as usage changes, with no rules to write. Why the correct answer wins: An archive class is priced for data that is kept but rarely read.
- **D:** Incorrect for this question. A lifecycle rule deletes the derived copies on a schedule, so storage does not grow forever. Why the correct answer wins: An archive class is priced for data that is kept but rarely read.

### Question 5 — D

Answer: Partition the S3 prefix by event date. Cohort and date prefixes let each job read only its own slice. Date partitioning lets a query or a training job skip the prefixes it does not need. Local study-map skill 1.4 (Data Formats and Partitioning), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Lustre delivers the high throughput a multi-node training job needs from shared storage. Why the correct answer wins: Cohort and date prefixes let each job read only its own slice.
- **B:** Incorrect for this question. Raw JSON is readable but forces every query to parse whole records. Why the correct answer wins: Cohort and date prefixes let each job read only its own slice.
- **C:** Incorrect for this question. Columnar Parquet files in S3 are read in column subsets, which suits repeated training scans. Why the correct answer wins: Cohort and date prefixes let each job read only its own slice.
- **D:** Correct. Date partitioning lets a query or a training job skip the prefixes it does not need. In this case: Cohort and date prefixes let each job read only its own slice.

### Question 6 — D

Answer: Land the raw JSON events in Amazon S3 unchanged. A faithful original record allows later re-derivation that a transformed copy cannot. Raw JSON is readable but forces every query to parse whole records. Local study-map skill 1.4 (Data Formats and Partitioning), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Object Lock prevents the retained objects from being altered or deleted for the stated period. Why the correct answer wins: A faithful original record allows later re-derivation that a transformed copy cannot.
- **B:** Incorrect for this question. Columnar Parquet files in S3 are read in column subsets, which suits repeated training scans. Why the correct answer wins: A faithful original record allows later re-derivation that a transformed copy cannot.
- **C:** Incorrect for this question. EBS is block storage bound to one instance, which suits a single host and not a fleet. Why the correct answer wins: A faithful original record allows later re-derivation that a transformed copy cannot.
- **D:** Correct. Raw JSON is readable but forces every query to parse whole records. In this case: A faithful original record allows later re-derivation that a transformed copy cannot.

### Question 7 — D, E

Answers: Transform the data with an AWS Glue ETL job; Register the tables in the AWS Glue Data Catalog. A managed transform job does the normalisation, and the catalog publishes it for discovery. Glue runs a managed Spark job against catalogued sources and writes the prepared output. The catalog gives every engine the same table definitions and schemas. Local study-map skill 1.5 (Merge and Transform Tooling), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. DataBrew provides a visual recipe for profiling, cleaning and normalising columns. Why the correct answer wins: A managed transform job does the normalisation, and the catalog publishes it for discovery.
- **B:** Incorrect for this question. A function per record suits lightweight enrichment and filtering of a stream. Why the correct answer wins: A managed transform job does the normalisation, and the catalog publishes it for discovery.
- **C:** Incorrect for this question. EMR gives a managed Spark cluster sized for the processing job. Why the correct answer wins: A managed transform job does the normalisation, and the catalog publishes it for discovery.
- **D:** Correct. Glue runs a managed Spark job against catalogued sources and writes the prepared output. In this case: A managed transform job does the normalisation, and the catalog publishes it for discovery.
- **E:** Correct. The catalog gives every engine the same table definitions and schemas. In this case: A managed transform job does the normalisation, and the catalog publishes it for discovery.

### Question 8 — D

Answer: Transform each stream record with AWS Lambda. A function per record suits lightweight enrichment at the edge of the pipeline. Local study-map skill 1.5 (Merge and Transform Tooling), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Glue runs a managed Spark job against catalogued sources and writes the prepared output. Why the correct answer wins: A function per record suits lightweight enrichment at the edge of the pipeline.
- **B:** Incorrect for this question. Data Wrangler builds a reusable preparation flow and can export it into a pipeline. Why the correct answer wins: A function per record suits lightweight enrichment at the edge of the pipeline.
- **C:** Incorrect for this question. EMR gives a managed Spark cluster sized for the processing job. Why the correct answer wins: A function per record suits lightweight enrichment at the edge of the pipeline.
- **D:** Correct. In this case: A function per record suits lightweight enrichment at the edge of the pipeline.

### Question 9 — A

Answer: Publish the features to the SageMaker Feature Store online store. The online store returns the latest feature values for low-latency inference. Local study-map skill 1.6 (Feature Store), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Correct. In this case: The online store returns the latest feature values for low-latency inference.
- **B:** Incorrect for this question. A feature group gives one definition that both training and inference read. Why the correct answer wins: The online store returns the latest feature values for low-latency inference.
- **C:** Incorrect for this question. The catalog gives every engine the same table definitions and schemas. Why the correct answer wins: The online store returns the latest feature values for low-latency inference.
- **D:** Incorrect for this question. The offline store keeps timestamped values so training reads the values that existed at the time. Why the correct answer wins: The online store returns the latest feature values for low-latency inference.

### Question 10 — A

Answer: Impute missing numeric values with the median. Median imputation keeps the admission using a robust central value. Median imputation is robust to a skewed distribution and keeps the row. Local study-map skill 1.7 (Feature Engineering and Scaling), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Correct. Median imputation is robust to a skewed distribution and keeps the row. In this case: Median imputation keeps the admission using a robust central value.
- **B:** Incorrect for this question. Dropping rows discards information and can bias the set towards complete records. Why the correct answer wins: Median imputation keeps the admission using a robust central value.
- **C:** Incorrect for this question. Clipping caps the influence of a few extreme values without deleting the records. Why the correct answer wins: Median imputation keeps the admission using a robust central value.
- **D:** Incorrect for this question. Binning trades resolution for robustness to small variations inside a range. Why the correct answer wins: Median imputation keeps the admission using a robust central value.

### Question 11 — A, B

Answers: Standardise the numeric columns before training; Stratify the train, validation and test splits by label. Scaling makes the units comparable, and stratification keeps the rare label in each split. Scaling puts the numeric columns on comparable ranges so no column dominates the fit. Stratifying keeps the label proportions the same in every split. Local study-map skill 1.7 (Feature Engineering and Scaling), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Correct. Scaling puts the numeric columns on comparable ranges so no column dominates the fit. In this case: Scaling makes the units comparable, and stratification keeps the rare label in each split.
- **B:** Correct. Stratifying keeps the label proportions the same in every split. In this case: Scaling makes the units comparable, and stratification keeps the rare label in each split.
- **C:** Incorrect for this question. Binning trades resolution for robustness to small variations inside a range. Why the correct answer wins: Scaling makes the units comparable, and stratification keeps the rare label in each split.
- **D:** Incorrect for this question. Shuffling stops the batch order from encoding an accidental pattern. Why the correct answer wins: Scaling makes the units comparable, and stratification keeps the rare label in each split.
- **E:** Incorrect for this question. Duplicates that straddle splits leak the same row into training and evaluation. Why the correct answer wins: Scaling makes the units comparable, and stratification keeps the rare label in each split.

### Question 12 — B

Answer: Keep the vectors in Amazon S3 with a vector index. An object-store-backed vector index suits a large, cost-sensitive, less frequently read corpus. Local study-map skill 1.8 (Vector Stores and Embeddings), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. OpenSearch provides a managed vector index with filtered k-nearest-neighbour search. Why the correct answer wins: An object-store-backed vector index suits a large, cost-sensitive, less frequently read corpus.
- **B:** Correct. In this case: An object-store-backed vector index suits a large, cost-sensitive, less frequently read corpus.
- **C:** Incorrect for this question. Rebuilding the index per request cannot hold a large corpus or a latency target. Why the correct answer wins: An object-store-backed vector index suits a large, cost-sensitive, less frequently read corpus.
- **D:** Incorrect for this question. pgvector keeps vectors beside relational rows the application already queries. Why the correct answer wins: An object-store-backed vector index suits a large, cost-sensitive, less frequently read corpus.

### Question 13 — C, E

Answers: Embed the images and captions with one multimodal model; Index the vectors in Amazon OpenSearch Service with k-NN search. A multimodal model places images and text in one space, and a vector index serves both queries. A shared multimodal space lets an image query match a text description. OpenSearch provides a managed vector index with filtered k-nearest-neighbour search. Local study-map skill 1.8 (Vector Stores and Embeddings), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Hybrid retrieval catches exact identifiers that a vector search alone can miss. Why the correct answer wins: A multimodal model places images and text in one space, and a vector index serves both queries.
- **B:** Incorrect for this question. pgvector keeps vectors beside relational rows the application already queries. Why the correct answer wins: A multimodal model places images and text in one space, and a vector index serves both queries.
- **C:** Correct. OpenSearch provides a managed vector index with filtered k-nearest-neighbour search. In this case: A multimodal model places images and text in one space, and a vector index serves both queries.
- **D:** Incorrect for this question. A managed embedding model converts text into vectors without hosts to run. Why the correct answer wins: A multimodal model places images and text in one space, and a vector index serves both queries.
- **E:** Correct. A shared multimodal space lets an image query match a text description. In this case: A multimodal model places images and text in one space, and a vector index serves both queries.

### Question 14 — C

Answer: Mask and redact personal identifiers before training. Redaction removes the identifiers before the text reaches training. Removing the identifiers stops the model from learning or echoing personal data. Local study-map skill 1.9 (Text Pre-processing and Chunking), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Using the model own tokeniser keeps token counts and truncation consistent with inference. Why the correct answer wins: Redaction removes the identifiers before the text reaches training.
- **B:** Incorrect for this question. Metadata lets retrieval filter by source or recency and lets answers cite the document. Why the correct answer wins: Redaction removes the identifiers before the text reaches training.
- **C:** Correct. Removing the identifiers stops the model from learning or echoing personal data. In this case: Redaction removes the identifiers before the text reaches training.
- **D:** Incorrect for this question. Semantic chunks keep a coherent passage together, which improves what retrieval returns. Why the correct answer wins: Redaction removes the identifiers before the text reaches training.

### Question 15 — A, D

Answers: Evaluate AWS Glue Data Quality rules on the prepared table; Profile the incoming data and store the statistics as a baseline. Quality rules fail the job on invalid rows, and the stored profile becomes the drift baseline. Data Quality rules fail the job on nulls, duplicates or range violations before training starts. A stored profile is what later drift comparison is measured against. Local study-map skill 1.10 (Data Quality Validation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Correct. Data Quality rules fail the job on nulls, duplicates or range violations before training starts. In this case: Quality rules fail the job on invalid rows, and the stored profile becomes the drift baseline.
- **B:** Incorrect for this question. A schema check rejects records whose fields changed shape before they corrupt the set. Why the correct answer wins: Quality rules fail the job on invalid rows, and the stored profile becomes the drift baseline.
- **C:** Incorrect for this question. A lifecycle rule deletes the derived copies on a schedule, so storage does not grow forever. Why the correct answer wins: Quality rules fail the job on invalid rows, and the stored profile becomes the drift baseline.
- **D:** Correct. A stored profile is what later drift comparison is measured against. In this case: Quality rules fail the job on invalid rows, and the stored profile becomes the drift baseline.
- **E:** Incorrect for this question. DataBrew provides a visual recipe for profiling, cleaning and normalising columns. Why the correct answer wins: Quality rules fail the job on invalid rows, and the stored profile becomes the drift baseline.

### Question 16 — A

Answer: Send the unlabelled records to Amazon SageMaker Ground Truth. Managed labelling handles the workforce, review and quality reporting. Ground Truth manages the labelling workforce, instructions and quality checks. Local study-map skill 1.11 (Labelling and Annotation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Correct. Ground Truth manages the labelling workforce, instructions and quality checks. In this case: Managed labelling handles the workforce, review and quality reporting.
- **B:** Incorrect for this question. Active learning labels most records automatically and sends only uncertain ones to a person. Why the correct answer wins: Managed labelling handles the workforce, review and quality reporting.
- **C:** Incorrect for this question. Removing the identifiers stops the model from learning or echoing personal data. Why the correct answer wins: Managed labelling handles the workforce, review and quality reporting.
- **D:** Incorrect for this question. Duplicates that straddle splits leak the same row into training and evaluation. Why the correct answer wins: Managed labelling handles the workforce, review and quality reporting.

### Question 17 — C

Answer: Rebalance the numeric, text and image assets in the set. A modality with far fewer examples is under-trained even when labels look balanced. Local study-map skill 1.12 (Bias Detection and Mitigation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Reweighting the loss changes what the model is optimised for without discarding data. Why the correct answer wins: A modality with far fewer examples is under-trained even when labels look balanced.
- **B:** Incorrect for this question. Clarify reports label and feature bias metrics so the imbalance is quantified first. Why the correct answer wins: A modality with far fewer examples is under-trained even when labels look balanced.
- **C:** Correct. In this case: A modality with far fewer examples is under-trained even when labels look balanced.
- **D:** Incorrect for this question. Stratifying keeps the label proportions the same in every split. Why the correct answer wins: A modality with far fewer examples is under-trained even when labels look balanced.

### Question 18 — B

Answer: Clip extreme outliers to a defined percentile. Clipping caps the influence of impossible values without deleting the admission. Local study-map skill 1.13 (Cleaning and Class Imbalance), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Dropping rows discards information and can bias the set towards complete records. Why the correct answer wins: Clipping caps the influence of impossible values without deleting the admission.
- **B:** Correct. In this case: Clipping caps the influence of impossible values without deleting the admission.
- **C:** Incorrect for this question. Median imputation is robust to a skewed distribution and keeps the row. Why the correct answer wins: Clipping caps the influence of impossible values without deleting the admission.
- **D:** Incorrect for this question. Synthetic minority sampling gives the learner more examples of the rare class. Why the correct answer wins: Clipping caps the influence of impossible values without deleting the admission.

### Question 19 — D

Answer: Train with the linear learner algorithm. A linear model is cheap and interpretable when the relationship is nearly linear. Local study-map skill 2.1 (Model and Algorithm Selection), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. Random Cut Forest assigns an anomaly score to each observation against the learned shape. Why the correct answer wins: A linear model is cheap and interpretable when the relationship is nearly linear.
- **B:** Incorrect for this question. Gradient-boosted trees are the usual strong baseline for tabular data. Why the correct answer wins: A linear model is cheap and interpretable when the relationship is nearly linear.
- **C:** Incorrect for this question. DeepAR learns across many related time series and returns probabilistic forecasts. Why the correct answer wins: A linear model is cheap and interpretable when the relationship is nearly linear.
- **D:** Correct. In this case: A linear model is cheap and interpretable when the relationship is nearly linear.

### Question 20 — A

Answer: Average several models into an ensemble. Averaging several fits reduces the variance any one of them carries. An ensemble reduces variance from any single model fit. Local study-map skill 2.1 (Model and Algorithm Selection), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Correct. An ensemble reduces variance from any single model fit. In this case: Averaging several fits reduces the variance any one of them carries.
- **B:** Incorrect for this question. A linear model is cheap and interpretable when the relationship is close to linear. Why the correct answer wins: Averaging several fits reduces the variance any one of them carries.
- **C:** Incorrect for this question. Nearest neighbours suit a small, low-dimensional similarity problem. Why the correct answer wins: Averaging several fits reduces the variance any one of them carries.
- **D:** Incorrect for this question. Gradient-boosted trees are the usual strong baseline for tabular data. Why the correct answer wins: Averaging several fits reduces the variance any one of them carries.

### Question 21 — C

Answer: Select a Titan embedding model in Amazon Bedrock. An embedding model produces the vectors through a managed API. A Titan embedding model turns text into vectors for search and clustering. Local study-map skill 2.2 (Foundation Model Selection), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. Nova models are reached through the Bedrock API with no infrastructure to host. Why the correct answer wins: An embedding model produces the vectors through a managed API.
- **B:** Incorrect for this question. Claude models are available through Bedrock for long-context reasoning tasks. Why the correct answer wins: An embedding model produces the vectors through a managed API.
- **C:** Correct. A Titan embedding model turns text into vectors for search and clustering. In this case: An embedding model produces the vectors through a managed API.
- **D:** Incorrect for this question. Self-hosting gives full control but puts model operations on your team. Why the correct answer wins: An embedding model produces the vectors through a managed API.

### Question 22 — D

Answer: Select an Anthropic Claude model in Amazon Bedrock. A long context window is what the packet length requires. Claude models are available through Bedrock for long-context reasoning tasks. Local study-map skill 2.2 (Foundation Model Selection), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. Self-hosting gives full control but puts model operations on your team. Why the correct answer wins: A long context window is what the packet length requires.
- **B:** Incorrect for this question. Nova models are reached through the Bedrock API with no infrastructure to host. Why the correct answer wins: A long context window is what the packet length requires.
- **C:** Incorrect for this question. A Titan embedding model turns text into vectors for search and clustering. Why the correct answer wins: A long context window is what the packet length requires.
- **D:** Correct. Claude models are available through Bedrock for long-context reasoning tasks. In this case: A long context window is what the packet length requires.

### Question 23 — A

Answer: Distil the large model into a smaller student model. Distillation moves the large model behaviour into a smaller, cheaper model. Local study-map skill 2.3 (Fine-tuning and Customisation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Correct. In this case: Distillation moves the large model behaviour into a smaller, cheaper model.
- **B:** Incorrect for this question. Full fine-tuning updates every weight and needs more data, memory and care. Why the correct answer wins: Distillation moves the large model behaviour into a smaller, cheaper model.
- **C:** Incorrect for this question. Adapters train a small number of parameters, which lowers cost and the risk of forgetting. Why the correct answer wins: Distillation moves the large model behaviour into a smaller, cheaper model.
- **D:** Incorrect for this question. Continued pre-training adapts the model to domain vocabulary before task tuning. Why the correct answer wins: Distillation moves the large model behaviour into a smaller, cheaper model.

### Question 24 — D, E

Answers: Fine-tune with parameter-efficient adapters such as LoRA; Run continued pre-training on the domain corpus. Continued pre-training adds the vocabulary, and adapters keep the trainable count small. Adapters train a small number of parameters, which lowers cost and the risk of forgetting. Continued pre-training adapts the model to domain vocabulary before task tuning. Local study-map skill 2.3 (Fine-tuning and Customisation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. Full fine-tuning updates every weight and needs more data, memory and care. Why the correct answer wins: Continued pre-training adds the vocabulary, and adapters keep the trainable count small.
- **B:** Incorrect for this question. A well-structured prompt often meets the requirement without a training run. Why the correct answer wins: Continued pre-training adds the vocabulary, and adapters keep the trainable count small.
- **C:** Incorrect for this question. Distillation transfers the large model behaviour into a cheaper model to serve. Why the correct answer wins: Continued pre-training adds the vocabulary, and adapters keep the trainable count small.
- **D:** Correct. Adapters train a small number of parameters, which lowers cost and the risk of forgetting. In this case: Continued pre-training adds the vocabulary, and adapters keep the trainable count small.
- **E:** Correct. Continued pre-training adapts the model to domain vocabulary before task tuning. In this case: Continued pre-training adds the vocabulary, and adapters keep the trainable count small.

### Question 25 — A

Answer: Index parent sections and retrieve their child chunks. Small child chunks match precisely while the parent section supplies context. Local study-map skill 2.4 (RAG Architecture Patterns), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Correct. In this case: Small child chunks match precisely while the parent section supplies context.
- **B:** Incorrect for this question. Metadata lets retrieval filter by source or recency and lets answers cite the document. Why the correct answer wins: Small child chunks match precisely while the parent section supplies context.
- **C:** Incorrect for this question. Overlapping fixed chunks bound the context size and avoid cutting a sentence in half. Why the correct answer wins: Small child chunks match precisely while the parent section supplies context.
- **D:** Incorrect for this question. Semantic chunks keep a coherent passage together, which improves what retrieval returns. Why the correct answer wins: Small child chunks match precisely while the parent section supplies context.

### Question 26 — D

Answer: Transcribe the calls with Amazon Transcribe. Managed speech-to-text with speaker labelling covers dictation. Transcribe converts speech to text and can label speakers. Local study-map skill 2.5 (Managed AI Services), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. Textract reads forms and tables into structured fields without a custom model. Why the correct answer wins: Managed speech-to-text with speaker labelling covers dictation.
- **B:** Incorrect for this question. Comprehend provides managed entity, key-phrase and sentiment analysis. Why the correct answer wins: Managed speech-to-text with speaker labelling covers dictation.
- **C:** Incorrect for this question. Rekognition provides managed image and video analysis for common labels and text. Why the correct answer wins: Managed speech-to-text with speaker labelling covers dictation.
- **D:** Correct. Transcribe converts speech to text and can label speakers. In this case: Managed speech-to-text with speaker labelling covers dictation.

### Question 27 — C

Answer: Bring a custom training container image. A custom image is needed when the managed images cannot carry the dependency. Local study-map skill 2.6 (Built-in Algorithms and Script Mode), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. JumpStart supplies a pre-trained model and its deployment template. Why the correct answer wins: A custom image is needed when the managed images cannot carry the dependency.
- **B:** Incorrect for this question. Gradient-boosted trees are the usual strong baseline for tabular data. Why the correct answer wins: A custom image is needed when the managed images cannot carry the dependency.
- **C:** Correct. In this case: A custom image is needed when the managed images cannot carry the dependency.
- **D:** Incorrect for this question. Script mode runs your own training script inside a managed framework container. Why the correct answer wins: A custom image is needed when the managed images cannot carry the dependency.

### Question 28 — A

Answer: Enable early stopping on the validation metric. Early stopping ends a trial once validation stops improving. Local study-map skill 2.7 (Hyperparameter Tuning), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Correct. In this case: Early stopping ends a trial once validation stops improving.
- **B:** Incorrect for this question. Automatic model tuning runs the search over a stated objective metric. Why the correct answer wins: Early stopping ends a trial once validation stops improving.
- **C:** Incorrect for this question. A manual grid costs a job per combination and adapts to nothing. Why the correct answer wins: Early stopping ends a trial once validation stops improving.
- **D:** Incorrect for this question. The search optimises exactly the metric it is given, so the metric must match the goal. Why the correct answer wins: Early stopping ends a trial once validation stops improving.

### Question 29 — A, C

Answers: Define the tuning objective on the validation metric that matters; Tune hyperparameters with SageMaker automatic model tuning. The managed search runs the trials, and the objective metric defines the target. The search optimises exactly the metric it is given, so the metric must match the goal. Automatic model tuning runs the search over a stated objective metric. Local study-map skill 2.7 (Hyperparameter Tuning), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Correct. The search optimises exactly the metric it is given, so the metric must match the goal. In this case: The managed search runs the trials, and the objective metric defines the target.
- **B:** Incorrect for this question. Random search is a cheap baseline but ignores what earlier trials learned. Why the correct answer wins: The managed search runs the trials, and the objective metric defines the target.
- **C:** Correct. Automatic model tuning runs the search over a stated objective metric. In this case: The managed search runs the trials, and the objective metric defines the target.
- **D:** Incorrect for this question. A manual grid costs a job per combination and adapts to nothing. Why the correct answer wins: The managed search runs the trials, and the objective metric defines the target.
- **E:** Incorrect for this question. Early stopping ends a trial once the validation metric stops improving. Why the correct answer wins: The managed search runs the trials, and the objective metric defines the target.

### Question 30 — B, E

Answers: Shard the model across instances with model parallelism; Checkpoint to Amazon S3 so an interrupted job resumes. Model parallelism shards the weights, and checkpoints let the job resume. Model parallelism is needed when the model weights do not fit on a single device. Checkpoints let a reclaimed instance continue from the last saved state. Local study-map skill 2.8 (Training Efficiency and Regularisation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. Spot capacity lowers the cost of a job that can checkpoint and resume. Why the correct answer wins: Model parallelism shards the weights, and checkpoints let the job resume.
- **B:** Correct. Checkpoints let a reclaimed instance continue from the last saved state. In this case: Model parallelism shards the weights, and checkpoints let the job resume.
- **C:** Incorrect for this question. A warm pool removes the provisioning delay between consecutive training jobs. Why the correct answer wins: Model parallelism shards the weights, and checkpoints let the job resume.
- **D:** Incorrect for this question. Data parallelism shortens wall-clock training when the model still fits on one device. Why the correct answer wins: Model parallelism shards the weights, and checkpoints let the job resume.
- **E:** Correct. Model parallelism is needed when the model weights do not fit on a single device. In this case: Model parallelism shards the weights, and checkpoints let the job resume.

### Question 31 — B

Answer: Report accuracy alone on a 2 percent positive class. Accuracy on a rare class is dominated by the majority class. Local study-map skill 2.9 (Classic Model Evaluation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. ROC-AUC measures how well the scores separate the classes across thresholds. Why the correct answer wins: Accuracy on a rare class is dominated by the majority class.
- **B:** Correct. In this case: Accuracy on a rare class is dominated by the majority class.
- **C:** Incorrect for this question. F1 balances precision and recall, which suits an uneven class mix. Why the correct answer wins: Accuracy on a rare class is dominated by the majority class.
- **D:** Incorrect for this question. The operating threshold should follow the cost of a false positive against a false negative. Why the correct answer wins: Accuracy on a rare class is dominated by the majority class.

### Question 32 — A, D

Answers: Report F1 on the holdout set; Inspect the confusion matrix on the minority class. F1 balances the two error types, and the matrix supplies the counts. F1 balances precision and recall, which suits an uneven class mix. The confusion matrix shows which class the model keeps confusing. Local study-map skill 2.9 (Classic Model Evaluation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Correct. The confusion matrix shows which class the model keeps confusing. In this case: F1 balances the two error types, and the matrix supplies the counts.
- **B:** Incorrect for this question. RMSE expresses the typical error in the target units and penalises large misses. Why the correct answer wins: F1 balances the two error types, and the matrix supplies the counts.
- **C:** Incorrect for this question. Accuracy on a rare class is dominated by the majority and hides missed positives. Why the correct answer wins: F1 balances the two error types, and the matrix supplies the counts.
- **D:** Correct. F1 balances precision and recall, which suits an uneven class mix. In this case: F1 balances the two error types, and the matrix supplies the counts.
- **E:** Incorrect for this question. BLEU measures n-gram overlap with the reference summaries. Why the correct answer wins: F1 balances the two error types, and the matrix supplies the counts.

### Question 33 — B

Answer: Add a human review loop for a sample of answers. Sampled expert review is how a judge rubric is validated. Local study-map skill 2.10 (GenAI and NLP Evaluation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. ROUGE measures recall of reference n-grams, which suits summarisation. Why the correct answer wins: Sampled expert review is how a judge rubric is validated.
- **B:** Correct. In this case: Sampled expert review is how a judge rubric is validated.
- **C:** Incorrect for this question. A rubric-driven judge scales qualitative review of free-text answers. Why the correct answer wins: Sampled expert review is how a judge rubric is validated.
- **D:** Incorrect for this question. BERTScore compares contextual embeddings, so a paraphrase can still score well. Why the correct answer wins: Sampled expert review is how a judge rubric is validated.

### Question 34 — C

Answer: Log runs with MLflow on SageMaker AI. Run tracking keeps parameters, metrics and artefacts comparable. Local study-map skill 2.11 (Experiment Tracking and Baselines), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. Prompt Management versions templates so a prompt change is reviewable and reversible. Why the correct answer wins: Run tracking keeps parameters, metrics and artefacts comparable.
- **B:** Incorrect for this question. The registry holds model versions and their approval status for deployment. Why the correct answer wins: Run tracking keeps parameters, metrics and artefacts comparable.
- **C:** Correct. In this case: Run tracking keeps parameters, metrics and artefacts comparable.
- **D:** Incorrect for this question. Bedrock evaluation scores model output against built-in or custom metrics. Why the correct answer wins: Run tracking keeps parameters, metrics and artefacts comparable.

### Question 35 — C

Answer: Deploy a serverless inference endpoint. Serverless inference scales to zero and suits intermittent calls. Local study-map skill 3.1 (Inference Strategy), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. Asynchronous inference queues large or long requests and returns results through S3. Why the correct answer wins: Serverless inference scales to zero and suits intermittent calls.
- **B:** Incorrect for this question. Batch transform scores a stored dataset with no endpoint to keep running. Why the correct answer wins: Serverless inference scales to zero and suits intermittent calls.
- **C:** Correct. In this case: Serverless inference scales to zero and suits intermittent calls.
- **D:** Incorrect for this question. A real-time endpoint answers synchronous requests with a persistent host behind it. Why the correct answer wins: Serverless inference scales to zero and suits intermittent calls.

### Question 36 — C, D

Answers: Deploy a real-time SageMaker AI endpoint; Run a batch transform job over the stored records. A real-time endpoint answers the bedside call, and batch transform scores the cohort. A real-time endpoint answers synchronous requests with a persistent host behind it. Batch transform scores a stored dataset with no endpoint to keep running. Local study-map skill 3.1 (Inference Strategy), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. Asynchronous inference queues large or long requests and returns results through S3. Why the correct answer wins: A real-time endpoint answers the bedside call, and batch transform scores the cohort.
- **B:** Incorrect for this question. A multi-model endpoint loads models on demand from S3 behind shared hosting capacity. Why the correct answer wins: A real-time endpoint answers the bedside call, and batch transform scores the cohort.
- **C:** Correct. Batch transform scores a stored dataset with no endpoint to keep running. In this case: A real-time endpoint answers the bedside call, and batch transform scores the cohort.
- **D:** Correct. A real-time endpoint answers synchronous requests with a persistent host behind it. In this case: A real-time endpoint answers the bedside call, and batch transform scores the cohort.
- **E:** Incorrect for this question. Serverless inference scales to zero and suits intermittent, short requests. Why the correct answer wins: A real-time endpoint answers the bedside call, and batch transform scores the cohort.

### Question 37 — B

Answer: Host many small models behind one multi-model endpoint. A multi-model endpoint loads models on demand behind shared capacity. Local study-map skill 3.2 (Endpoint Architecture), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. A multi-container endpoint chains containers such as preprocessing and inference. Why the correct answer wins: A multi-model endpoint loads models on demand behind shared capacity.
- **B:** Correct. In this case: A multi-model endpoint loads models on demand behind shared capacity.
- **C:** Incorrect for this question. A real-time endpoint answers synchronous requests with a persistent host behind it. Why the correct answer wins: A multi-model endpoint loads models on demand behind shared capacity.
- **D:** Incorrect for this question. Batch transform scores a stored dataset with no endpoint to keep running. Why the correct answer wins: A multi-model endpoint loads models on demand behind shared capacity.

### Question 38 — D

Answer: Right-size the endpoint with SageMaker Inference Recommender. The recommender benchmarks instance types against the latency and throughput target. Local study-map skill 3.3 (Foundation Model Deployment), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. The reservation only pays off when the steady volume exceeds the break-even point. Why the correct answer wins: The recommender benchmarks instance types against the latency and throughput target.
- **B:** Incorrect for this question. On-demand calls need no reservation and suit bursty, lower-volume traffic. Why the correct answer wins: The recommender benchmarks instance types against the latency and throughput target.
- **C:** Incorrect for this question. Custom model import runs your own fine-tuned weights on Bedrock infrastructure. Why the correct answer wins: The recommender benchmarks instance types against the latency and throughput target.
- **D:** Correct. In this case: The recommender benchmarks instance types against the latency and throughput target.

### Question 39 — C

Answer: Call the Bedrock model on demand. On-demand calls need no reservation at low, unpredictable volume. On-demand calls need no reservation and suit bursty, lower-volume traffic. Local study-map skill 3.3 (Foundation Model Deployment), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. The reservation only pays off when the steady volume exceeds the break-even point. Why the correct answer wins: On-demand calls need no reservation at low, unpredictable volume.
- **B:** Incorrect for this question. Custom model import runs your own fine-tuned weights on Bedrock infrastructure. Why the correct answer wins: On-demand calls need no reservation at low, unpredictable volume.
- **C:** Correct. On-demand calls need no reservation and suit bursty, lower-volume traffic. In this case: On-demand calls need no reservation at low, unpredictable volume.
- **D:** Incorrect for this question. Provisioned throughput reserves model capacity for predictable, high-volume traffic. Why the correct answer wins: On-demand calls need no reservation at low, unpredictable volume.

### Question 40 — C

Answer: Schedule a knowledge base sync when documents change. A knowledge base sync re-indexes changed documents. A sync re-indexes changed documents so retrieval does not serve stale passages. Local study-map skill 3.4 (Agents and Retrieval Runtime), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. Prompt Management versions templates so a prompt change is reviewable and reversible. Why the correct answer wins: A knowledge base sync re-indexes changed documents.
- **B:** Incorrect for this question. Persisted session state keeps multi-turn context without resending the whole history. Why the correct answer wins: A knowledge base sync re-indexes changed documents.
- **C:** Correct. A sync re-indexes changed documents so retrieval does not serve stale passages. In this case: A knowledge base sync re-indexes changed documents.
- **D:** Incorrect for this question. An agent needs its tools, knowledge base and instructions deployed together as one unit. Why the correct answer wins: A knowledge base sync re-indexes changed documents.

### Question 41 — B

Answer: Run the container on Amazon ECS. A container service keeps the container running and replaces tasks on a rolling basis. ECS schedules the container on managed cluster capacity. Local study-map skill 3.5 (Containers and Compute Provisioning), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. Lambda suits a small model and spiky traffic but not a large model resident in memory. Why the correct answer wins: A container service keeps the container running and replaces tasks on a rolling basis.
- **B:** Correct. ECS schedules the container on managed cluster capacity. In this case: A container service keeps the container running and replaces tasks on a rolling basis.
- **C:** Incorrect for this question. AWS Batch queues the job and provisions capacity for the run. Why the correct answer wins: A container service keeps the container running and replaces tasks on a rolling basis.
- **D:** Incorrect for this question. EKS runs the container under Kubernetes for teams already standardised on it. Why the correct answer wins: A container service keeps the container running and replaces tasks on a rolling basis.

### Question 42 — B

Answer: Scale on GPU utilisation rather than invocation count. GPU utilisation reflects the real bottleneck when every call is expensive. Local study-map skill 3.6 (Autoscaling and Concurrency), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. Target tracking holds a metric such as invocations per instance near a chosen value. Why the correct answer wins: GPU utilisation reflects the real bottleneck when every call is expensive.
- **B:** Correct. In this case: GPU utilisation reflects the real bottleneck when every call is expensive.
- **C:** Incorrect for this question. Step scaling adds capacity in bands as the alarm breaches, which suits sharp bursts. Why the correct answer wins: GPU utilisation reflects the real bottleneck when every call is expensive.
- **D:** Incorrect for this question. A scale-to-zero policy removes the idle cost when nothing calls the endpoint. Why the correct answer wins: GPU utilisation reflects the real bottleneck when every call is expensive.

### Question 43 — B, D

Answers: Auto scale the endpoint on a target-tracking policy; Keep provisioned concurrency ready for the burst window. Target tracking follows the smooth rise, and warm capacity avoids the first-call delay. Target tracking holds a metric such as invocations per instance near a chosen value. Provisioned concurrency pre-warms capacity so the burst does not meet a cold start. Local study-map skill 3.6 (Autoscaling and Concurrency), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. Step scaling adds capacity in bands as the alarm breaches, which suits sharp bursts. Why the correct answer wins: Target tracking follows the smooth rise, and warm capacity avoids the first-call delay.
- **B:** Correct. Provisioned concurrency pre-warms capacity so the burst does not meet a cold start. In this case: Target tracking follows the smooth rise, and warm capacity avoids the first-call delay.
- **C:** Incorrect for this question. A warm pool removes the provisioning delay between consecutive training jobs. Why the correct answer wins: Target tracking follows the smooth rise, and warm capacity avoids the first-call delay.
- **D:** Correct. Target tracking holds a metric such as invocations per instance near a chosen value. In this case: Target tracking follows the smooth rise, and warm capacity avoids the first-call delay.
- **E:** Incorrect for this question. A scale-to-zero policy removes the idle cost when nothing calls the endpoint. Why the correct answer wins: Target tracking follows the smooth rise, and warm capacity avoids the first-call delay.

### Question 44 — C

Answer: Place the endpoint and model containers in private subnets. Private subnets remove the inbound internet path while the endpoint keeps traffic private. Private subnets remove the inbound internet path to the model hosts. Local study-map skill 3.7 (VPC Networking for Endpoints), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. A security group scoped to the caller subnet allows only the intended traffic. Why the correct answer wins: Private subnets remove the inbound internet path while the endpoint keeps traffic private.
- **B:** Incorrect for this question. An open ingress rule exposes the model to anything that can reach the VPC. Why the correct answer wins: Private subnets remove the inbound internet path while the endpoint keeps traffic private.
- **C:** Correct. Private subnets remove the inbound internet path to the model hosts. In this case: Private subnets remove the inbound internet path while the endpoint keeps traffic private.
- **D:** Incorrect for this question. A NAT gateway gives private hosts outbound access without accepting inbound traffic. Why the correct answer wins: Private subnets remove the inbound internet path while the endpoint keeps traffic private.

### Question 45 — B, E

Answers: Build and test the model image with AWS CodeBuild; Fail the pipeline when the evaluation threshold is missed. A build service runs the build and tests, and a quality gate blocks the failing model. CodeBuild runs the build and the automated tests in a clean managed environment. A quality gate blocks a release whose measured metric is below the agreed bar. Local study-map skill 3.8 (CI/CD Pipelines), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. CodeDeploy performs the traffic shift and can roll back on an alarm. Why the correct answer wins: A build service runs the build and tests, and a quality gate blocks the failing model.
- **B:** Correct. CodeBuild runs the build and the automated tests in a clean managed environment. In this case: A build service runs the build and tests, and a quality gate blocks the failing model.
- **C:** Incorrect for this question. CodePipeline sequences the build, test and deploy stages and records each outcome. Why the correct answer wins: A build service runs the build and tests, and a quality gate blocks the failing model.
- **D:** Incorrect for this question. CodeCommit is the managed Git repository the pipeline reads from. Why the correct answer wins: A build service runs the build and tests, and a quality gate blocks the failing model.
- **E:** Correct. A quality gate blocks a release whose measured metric is below the agreed bar. In this case: A build service runs the build and tests, and a quality gate blocks the failing model.

### Question 46 — B

Answer: Shift traffic with AWS CodeDeploy. A deployment service performs the shift and the automatic rollback. CodeDeploy performs the traffic shift and can roll back on an alarm. Local study-map skill 3.8 (CI/CD Pipelines), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. CodeBuild runs the build and the automated tests in a clean managed environment. Why the correct answer wins: A deployment service performs the shift and the automatic rollback.
- **B:** Correct. CodeDeploy performs the traffic shift and can roll back on an alarm. In this case: A deployment service performs the shift and the automatic rollback.
- **C:** Incorrect for this question. CodeConnections lets the pipeline read a repository hosted elsewhere. Why the correct answer wins: A deployment service performs the shift and the automatic rollback.
- **D:** Incorrect for this question. CodePipeline sequences the build, test and deploy stages and records each outcome. Why the correct answer wins: A deployment service performs the shift and the automatic rollback.

### Question 47 — D

Answer: Register the approved version in the SageMaker Model Registry. A registry stores versions with lineage and approval status. The registry holds model versions and their approval status for deployment. Local study-map skill 3.9 (Model Registry and Versioning), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. CodeCommit is the managed Git repository the pipeline reads from. Why the correct answer wins: A registry stores versions with lineage and approval status.
- **B:** Incorrect for this question. Run logging keeps parameters, metrics and artefacts comparable across experiments. Why the correct answer wins: A registry stores versions with lineage and approval status.
- **C:** Incorrect for this question. Prompt Management versions templates so a prompt change is reviewable and reversible. Why the correct answer wins: A registry stores versions with lineage and approval status.
- **D:** Correct. The registry holds model versions and their approval status for deployment. In this case: A registry stores versions with lineage and approval status.

### Question 48 — A

Answer: Mirror traffic to the new model without serving its answers. Mirrored traffic collects the comparison with no user exposure. Local study-map skill 3.10 (Deployment Strategy and Rollback), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Correct. In this case: Mirrored traffic collects the comparison with no user exposure.
- **B:** Incorrect for this question. A canary release limits the blast radius of a bad model to the canary share. Why the correct answer wins: Mirrored traffic collects the comparison with no user exposure.
- **C:** Incorrect for this question. Blue/green keeps the previous version ready for an immediate switch back. Why the correct answer wins: Mirrored traffic collects the comparison with no user exposure.
- **D:** Incorrect for this question. A single switch gives a bad model the whole traffic share at once. Why the correct answer wins: Mirrored traffic collects the comparison with no user exposure.

### Question 49 — B, E

Answers: Send a small share of traffic to the new version first; Require a manual approval before the version is deployed. An approval gate enforces the sign-off, and a canary limits the exposure. A canary release limits the blast radius of a bad model to the canary share. An approval gate stops a model from reaching production on an automated pass alone. Local study-map skill 3.10 (Deployment Strategy and Rollback), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. A single switch gives a bad model the whole traffic share at once. Why the correct answer wins: An approval gate enforces the sign-off, and a canary limits the exposure.
- **B:** Correct. An approval gate stops a model from reaching production on an automated pass alone. In this case: An approval gate enforces the sign-off, and a canary limits the exposure.
- **C:** Incorrect for this question. Mirroring collects comparison data with no user impact. Why the correct answer wins: An approval gate enforces the sign-off, and a canary limits the exposure.
- **D:** Incorrect for this question. A linear shift moves traffic gradually while the metrics are watched. Why the correct answer wins: An approval gate enforces the sign-off, and a canary limits the exposure.
- **E:** Correct. A canary release limits the blast radius of a bad model to the canary share. In this case: An approval gate enforces the sign-off, and a canary limits the exposure.

### Question 50 — B

Answer: Orchestrate the steps with AWS Step Functions. A state machine coordinates the steps, the wait and the branching. Step Functions coordinates long-running steps and service calls with retries and branching. Local study-map skill 3.11 (Orchestration and Retraining), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. CodePipeline sequences the build, test and deploy stages and records each outcome. Why the correct answer wins: A state machine coordinates the steps, the wait and the branching.
- **B:** Correct. Step Functions coordinates long-running steps and service calls with retries and branching. In this case: A state machine coordinates the steps, the wait and the branching.
- **C:** Incorrect for this question. A SageMaker pipeline expresses the processing, training and registration steps as one DAG. Why the correct answer wins: A state machine coordinates the steps, the wait and the branching.
- **D:** Incorrect for this question. A schedule starts the pipeline on a fixed cadence without an external cron host. Why the correct answer wins: A state machine coordinates the steps, the wait and the branching.

### Question 51 — A

Answer: Enable feature attribution drift monitoring. Attribution drift shows that the model now depends on different features. Local study-map skill 4.1 (Drift and Model Monitoring), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Correct. In this case: Attribution drift shows that the model now depends on different features.
- **B:** Incorrect for this question. A data drift monitor compares the live request distribution against the training baseline. Why the correct answer wins: Attribution drift shows that the model now depends on different features.
- **C:** Incorrect for this question. A quality monitor scores live predictions once the true labels arrive. Why the correct answer wins: Attribution drift shows that the model now depends on different features.
- **D:** Incorrect for this question. A bias monitor watches whether the outcome distribution shifts for a protected group. Why the correct answer wins: Attribution drift shows that the model now depends on different features.

### Question 52 — C, D

Answers: Enable a data drift monitor on the endpoint; Enable a model quality monitor with ground-truth labels. A data drift monitor catches the changed inputs, and a quality monitor scores the labels when they land. A data drift monitor compares the live request distribution against the training baseline. A quality monitor scores live predictions once the true labels arrive. Local study-map skill 4.1 (Drift and Model Monitoring), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. A bias monitor watches whether the outcome distribution shifts for a protected group. Why the correct answer wins: A data drift monitor catches the changed inputs, and a quality monitor scores the labels when they land.
- **B:** Incorrect for this question. An alarm on the endpoint metrics pages someone when the service degrades. Why the correct answer wins: A data drift monitor catches the changed inputs, and a quality monitor scores the labels when they land.
- **C:** Correct. A data drift monitor compares the live request distribution against the training baseline. In this case: A data drift monitor catches the changed inputs, and a quality monitor scores the labels when they land.
- **D:** Correct. A quality monitor scores live predictions once the true labels arrive. In this case: A data drift monitor catches the changed inputs, and a quality monitor scores the labels when they land.
- **E:** Incorrect for this question. Attribution drift shows that the model now relies on different features than it did. Why the correct answer wins: A data drift monitor catches the changed inputs, and a quality monitor scores the labels when they land.

### Question 53 — C

Answer: Query the inference logs with CloudWatch Logs Insights. Log querying exposes the common pattern behind the failures. Logs Insights filters and aggregates the request logs to find the failing pattern. Local study-map skill 4.2 (Metrics and Dashboards), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. An alarm on the endpoint metrics pages someone when the service degrades. Why the correct answer wins: Log querying exposes the common pattern behind the failures.
- **B:** Incorrect for this question. X-Ray shows where a request spends its time across the services it touches. Why the correct answer wins: Log querying exposes the common pattern behind the failures.
- **C:** Correct. Logs Insights filters and aggregates the request logs to find the failing pattern. In this case: Log querying exposes the common pattern behind the failures.
- **D:** Incorrect for this question. A dashboard puts the operating metrics in one view for the team. Why the correct answer wins: Log querying exposes the common pattern behind the failures.

### Question 54 — B

Answer: Trace the pipeline service calls with AWS X-Ray. Tracing shows where each request spends its time across services. Local study-map skill 4.2 (Metrics and Dashboards), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. Config records how each resource was configured and evaluates it against rules. Why the correct answer wins: Tracing shows where each request spends its time across services.
- **B:** Correct. In this case: Tracing shows where each request spends its time across services.
- **C:** Incorrect for this question. Logs Insights filters and aggregates the request logs to find the failing pattern. Why the correct answer wins: Tracing shows where each request spends its time across services.
- **D:** Incorrect for this question. A dashboard puts the operating metrics in one view for the team. Why the correct answer wins: Tracing shows where each request spends its time across services.

### Question 55 — B

Answer: Enable CloudWatch generative AI observability for the model calls. Generative AI observability records tokens, prompts and latency per call. Local study-map skill 4.3 (GenAI Observability), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. Agent tracing shows which tool call failed or stalled inside a multi-step task. Why the correct answer wins: Generative AI observability records tokens, prompts and latency per call.
- **B:** Correct. In this case: Generative AI observability records tokens, prompts and latency per call.
- **C:** Incorrect for this question. An alarm on the endpoint metrics pages someone when the service degrades. Why the correct answer wins: Generative AI observability records tokens, prompts and latency per call.
- **D:** Incorrect for this question. X-Ray shows where a request spends its time across the services it touches. Why the correct answer wins: Generative AI observability records tokens, prompts and latency per call.

### Question 56 — D

Answer: Right-size the instance family against the measured latency. Right-sizing matches the family to the measured workload. Matching the family to the measured workload avoids paying for capacity the model cannot use. Local study-map skill 4.4 (Cost Optimisation and Purchasing), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. Cost Explorer groups the bill by service and by tag so the expensive resource is visible. Why the correct answer wins: Right-sizing matches the family to the measured workload.
- **B:** Incorrect for this question. A Savings Plan discounts a predictable hourly spend on eligible compute. Why the correct answer wins: Right-sizing matches the family to the measured workload.
- **C:** Incorrect for this question. A scale-to-zero policy removes the idle cost when nothing calls the endpoint. Why the correct answer wins: Right-sizing matches the family to the measured workload.
- **D:** Correct. Matching the family to the measured workload avoids paying for capacity the model cannot use. In this case: Right-sizing matches the family to the measured workload.

### Question 57 — A, D

Answers: Cover the steady inference load with a Savings Plan; Break the spend down by endpoint with AWS Cost Explorer. A plan discounts the steady hours, and cost analysis attributes the spend. A Savings Plan discounts a predictable hourly spend on eligible compute. Cost Explorer groups the bill by service and by tag so the expensive resource is visible. Local study-map skill 4.4 (Cost Optimisation and Purchasing), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Correct. Cost Explorer groups the bill by service and by tag so the expensive resource is visible. In this case: A plan discounts the steady hours, and cost analysis attributes the spend.
- **B:** Incorrect for this question. A budget alerts when forecast or actual spend crosses the agreed amount. Why the correct answer wins: A plan discounts the steady hours, and cost analysis attributes the spend.
- **C:** Incorrect for this question. Matching the family to the measured workload avoids paying for capacity the model cannot use. Why the correct answer wins: A plan discounts the steady hours, and cost analysis attributes the spend.
- **D:** Correct. A Savings Plan discounts a predictable hourly spend on eligible compute. In this case: A plan discounts the steady hours, and cost analysis attributes the spend.
- **E:** Incorrect for this question. Batch scoring removes the idle endpoint that an always-on deployment would keep. Why the correct answer wins: A plan discounts the steady hours, and cost analysis attributes the spend.

### Question 58 — A

Answer: Route routine requests to a smaller model. Routing routine requests to a smaller model keeps the large one for hard cases. Local study-map skill 4.5 (Inference Cost and Token Usage), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Correct. In this case: Routing routine requests to a smaller model keeps the large one for hard cases.
- **B:** Incorrect for this question. Output tokens dominate generation cost, so a cap bounds the spend per call. Why the correct answer wins: Routing routine requests to a smaller model keeps the large one for hard cases.
- **C:** Incorrect for this question. Re-embedding an unchanged document is wasted spend on every refresh. Why the correct answer wins: Routing routine requests to a smaller model keeps the large one for hard cases.
- **D:** Incorrect for this question. Sending fewer retrieved tokens lowers both cost and latency on every call. Why the correct answer wins: Routing routine requests to a smaller model keeps the large one for hard cases.

### Question 59 — C

Answer: Trim the retrieved context sent to the model. Sending fewer retrieved tokens lowers cost and latency per call. Local study-map skill 4.5 (Inference Cost and Token Usage), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. The reservation only pays off when the steady volume exceeds the break-even point. Why the correct answer wins: Sending fewer retrieved tokens lowers cost and latency per call.
- **B:** Incorrect for this question. Output tokens dominate generation cost, so a cap bounds the spend per call. Why the correct answer wins: Sending fewer retrieved tokens lowers cost and latency per call.
- **C:** Correct. In this case: Sending fewer retrieved tokens lowers cost and latency per call.
- **D:** Incorrect for this question. Re-embedding an unchanged document is wasted spend on every refresh. Why the correct answer wins: Sending fewer retrieved tokens lowers cost and latency per call.

### Question 60 — A, C

Answers: Use the account root user for pipeline administration; Create a long-lived access key for the integration. Root use cannot be limited by policy, and an old key keeps working after the project ends. The root user cannot be limited by policy, so daily use magnifies any mistake. A long-lived key keeps working after the project ends unless someone retires it. Local study-map skill 4.6 (IAM and Credentials), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Correct. A long-lived key keeps working after the project ends unless someone retires it. In this case: Root use cannot be limited by policy, and an old key keeps working after the project ends.
- **B:** Incorrect for this question. A group policy keeps the shared permission set in one reviewable place. Why the correct answer wins: Root use cannot be limited by policy, and an old key keeps working after the project ends.
- **C:** Correct. The root user cannot be limited by policy, so daily use magnifies any mistake. In this case: Root use cannot be limited by policy, and an old key keeps working after the project ends.
- **D:** Incorrect for this question. A cross-account role issues temporary credentials without sharing a key. Why the correct answer wins: Root use cannot be limited by policy, and an old key keeps working after the project ends.
- **E:** Incorrect for this question. An execution role grants the job only the permissions its inputs and outputs need. Why the correct answer wins: Root use cannot be limited by policy, and an old key keeps working after the project ends.

### Question 61 — A

Answer: Attach one policy to an IAM group the engineers belong to. A group policy keeps the shared permission in one reviewable place. Local study-map skill 4.6 (IAM and Credentials), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Correct. In this case: A group policy keeps the shared permission in one reviewable place.
- **B:** Incorrect for this question. A long-lived key keeps working after the project ends unless someone retires it. Why the correct answer wins: A group policy keeps the shared permission in one reviewable place.
- **C:** Incorrect for this question. The root user cannot be limited by policy, so daily use magnifies any mistake. Why the correct answer wins: A group policy keeps the shared permission in one reviewable place.
- **D:** Incorrect for this question. A cross-account role issues temporary credentials without sharing a key. Why the correct answer wins: A group policy keeps the shared permission in one reviewable place.

### Question 62 — C

Answer: Restrict the security group to the application subnet. Scoping the group to the caller subnet admits only the intended traffic. Local study-map skill 4.7 (Network Isolation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. An open ingress rule exposes the model to anything that can reach the VPC. Why the correct answer wins: Scoping the group to the caller subnet admits only the intended traffic.
- **B:** Incorrect for this question. A private endpoint keeps the service traffic inside the VPC without a NAT gateway. Why the correct answer wins: Scoping the group to the caller subnet admits only the intended traffic.
- **C:** Correct. In this case: Scoping the group to the caller subnet admits only the intended traffic.
- **D:** Incorrect for this question. Private subnets remove the inbound internet path to the model hosts. Why the correct answer wins: Scoping the group to the caller subnet admits only the intended traffic.

### Question 63 — D

Answer: Encrypt the artefacts with a customer managed KMS key. A customer managed key lets the hospital disable access on its own authority. A customer managed key lets the team control the key policy and revoke access. Local study-map skill 4.8 (Encryption and Secrets), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. Secrets Manager holds the credential centrally and can rotate it. Why the correct answer wins: A customer managed key lets the hospital disable access on its own authority.
- **B:** Incorrect for this question. Config records how each resource was configured and evaluates it against rules. Why the correct answer wins: A customer managed key lets the hospital disable access on its own authority.
- **C:** Incorrect for this question. Guardrails filters denied topics, sensitive data and unsafe content in the response path. Why the correct answer wins: A customer managed key lets the hospital disable access on its own authority.
- **D:** Correct. A customer managed key lets the team control the key policy and revoke access. In this case: A customer managed key lets the hospital disable access on its own authority.

### Question 64 — D

Answer: Redact personal data before the prompt reaches the model. Redaction at the boundary keeps the data out of the request entirely. Local study-map skill 4.9 (Guardrails and Responsible AI), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. Safety screening keeps prohibited material out of the model weights. Why the correct answer wins: Redaction at the boundary keeps the data out of the request entirely.
- **B:** Incorrect for this question. Guardrails filters denied topics, sensitive data and unsafe content in the response path. Why the correct answer wins: Redaction at the boundary keeps the data out of the request entirely.
- **C:** Incorrect for this question. A denied-topics policy refuses the subject areas the business has ruled out. Why the correct answer wins: Redaction at the boundary keeps the data out of the request entirely.
- **D:** Correct. In this case: Redaction at the boundary keeps the data out of the request entirely.

### Question 65 — D

Answer: Track resource configuration with AWS Config. Configuration history records each resource's settings over time. Config records how each resource was configured and evaluates it against rules. Local study-map skill 4.10 (Audit and Vulnerability Scanning), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. Logs Insights filters and aggregates the request logs to find the failing pattern. Why the correct answer wins: Configuration history records each resource's settings over time.
- **B:** Incorrect for this question. CloudTrail records who called which API, when and from where. Why the correct answer wins: Configuration history records each resource's settings over time.
- **C:** Incorrect for this question. Inspector reports known vulnerabilities in the image before it is deployed. Why the correct answer wins: Configuration history records each resource's settings over time.
- **D:** Correct. Config records how each resource was configured and evaluates it against rules. In this case: Configuration history records each resource's settings over time.
