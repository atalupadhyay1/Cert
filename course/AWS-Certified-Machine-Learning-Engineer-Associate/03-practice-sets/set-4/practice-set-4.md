# AWS Certified Machine Learning Engineer – Associate (MLA-C02) — Full-Length Mock Exam 4

Machine Learning Engineer · 65 questions · 130 minutes · scaled passing score 720 of 1000

Blueprint-weighted mock exam. Item mix: 50 multiple-choice and 15 multiple-response items (the selection count is stated in each multi-response stem). The published exam has 65 questions in 130 minutes, of which 50 are scored and 15 are unscored, and AWS does not identify the unscored items. AWS publishes no split between multiple-choice and multiple-response items, so the 15-item multi-response block is an authoring choice. At 65 items in 130 minutes this set matches the published pacing at about 120 seconds per item. AWS is currently delivering MLA-C02 as a beta of 85 questions in 170 minutes with the extra items unscored; this set follows the published 65-question form. The published format has no case-study component, so no case-study item appears here. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied AWS exam items.

## Questions

---

## Domain 1 — Data Preparation for ML and AI (28%) — Ingestion, storage, feature engineering, embeddings, and data quality

### 1. Vibration telemetry from forty thousand machines must arrive in order and be read by both an alerting consumer and a training consumer. What should ingest it?

- A. Transform each stream record with AWS Lambda
- B. Ingest the events through Amazon MSK
- C. Ingest the events with Amazon Kinesis Data Streams
- D. Deliver the stream to Amazon S3 with Amazon Data Firehose

### 2. Safety-certification evidence must be preserved in a state that cannot be edited for the life of the product. What should be applied?

- A. Expire intermediate artefacts with an S3 lifecycle rule
- B. Archive the raw corpus to an S3 Glacier storage class
- C. Apply S3 Object Lock to the regulated training data
- D. Use S3 Intelligent-Tiering for the unevenly accessed corpus

### 3. Each vibration record needs a unit conversion and a threshold flag before it is written to the stream. What fits?

- A. Transform the data with an AWS Glue ETL job
- B. Process the data with Spark on Amazon EMR
- C. Transform each stream record with AWS Lambda
- D. Deliver the stream to Amazon S3 with Amazon Data Firehose

### 4. Sensor archives are read intensively for a month after a fault and then never again, and nobody can predict which files those will be. What fits?

- A. Archive the raw corpus to an S3 Glacier storage class
- B. Use S3 Intelligent-Tiering for the unevenly accessed corpus
- C. Land the dataset as Parquet in Amazon S3
- D. Expire intermediate artefacts with an S3 lifecycle rule

### 5. Training jobs read ten of ninety signal columns and always filter to one plant and one week. Which two storage choices fit? Select two.

- A. Land the raw JSON events in Amazon S3 unchanged
- B. Mount a shared Amazon EFS file system on every training host
- C. Attach a gp3 Amazon EBS volume to the training instance
- D. Land the dataset as Parquet in Amazon S3
- E. Partition the S3 prefix by event date

### 6. A field engineer must open one archived message exactly as the machine sent it during an incident review. Why preserve the original encoding?

- A. Land the dataset as Parquet in Amazon S3
- B. Partition the S3 prefix by event date
- C. Land the raw JSON events in Amazon S3 unchanged
- D. Apply S3 Object Lock to the regulated training data

### 7. Factory historian exports must be joined and deduplicated nightly at scale, and the team has no cluster operators. What fits?

- A. Prepare the data in SageMaker Data Wrangler
- B. Transform the data with an AWS Glue ETL job
- C. Profile and clean the data with AWS Glue DataBrew
- D. Process the data with Spark on Amazon EMR

### 8. A process engineer needs to explore, join and visualise signal tables with no code before handing the flow to the pipeline. What fits?

- A. Prepare the data in SageMaker Data Wrangler
- B. Transform each stream record with AWS Lambda
- C. Profile and clean the data with AWS Glue DataBrew
- D. Transform the data with an AWS Glue ETL job

### 9. A remaining-useful-life feature is computed by one team and must be identical in offline training and in the online scoring path. What should be created?

- A. Publish the features to the SageMaker Feature Store online store
- B. Ingest the cleaned rows into a SageMaker Feature Group
- C. Keep the point-in-time history in the Feature Store offline store
- D. Register the tables in the AWS Glue Data Catalog

### 10. A vibration amplitude column spans five orders of magnitude, and the tree model splits poorly on the raw values. What preparation fits?

- A. Bin the continuous age column into ranges
- B. Apply a log transform to the skewed amount column
- C. Standardise the numeric columns before training
- D. One-hot encode the categorical columns

### 11. Line identifiers are unordered categories, and batches arrive sorted by timestamp so the model learns the order. Which two steps fit? Select two.

- A. Stratify the train, validation and test splits by label
- B. Shuffle the rows before every epoch
- C. One-hot encode the categorical columns
- D. Bin the continuous age column into ranges
- E. Standardise the numeric columns before training

### 12. Only twenty thousand maintenance notes exist, and the search must answer inside the existing service process with no new managed index. What fits?

- A. Keep the vectors in Amazon S3 with a vector index
- B. Index the vectors in Amazon OpenSearch Service with k-NN search
- C. Store the vectors in Amazon RDS for PostgreSQL with pgvector
- D. Load every vector into the application process on each request

### 13. Maintenance queries keep missing the right procedure, and the note vocabulary is highly domain specific. Which two improvements fit? Select two.

- A. Fine-tune the embedding model on the domain question-answer pairs
- B. Add a reranking step after retrieval
- C. Generate the embeddings with an Amazon Bedrock embedding model
- D. Combine keyword and vector retrieval
- E. Index the vectors in Amazon OpenSearch Service with k-NN search

### 14. A retrieval prototype needs a predictable chunk size to fit a fixed context budget, and the manuals have no reliable headings. What fits?

- A. Index parent sections and retrieve their child chunks
- B. Chunk the documents on semantic boundaries such as headings
- C. Store source, date and section metadata with each chunk
- D. Split the documents into fixed-size overlapping chunks

### 15. A firmware update added two fields and renamed one, and training silently accepted the changed rows. What would have caught it?

- A. Remove duplicate rows before splitting
- B. Profile the incoming data and store the statistics as a baseline
- C. Evaluate AWS Glue Data Quality rules on the prepared table
- D. Enforce a schema contract on the ingested records

### 16. A million machine-sound clips need labels, and only a small acoustics team can judge the ambiguous ones. What fits?

- A. Augment the image set with rotations, crops and flips
- B. Send the unlabelled records to Amazon SageMaker Ground Truth
- C. Use automated data labelling with a human review sample in Ground Truth
- D. Rebalance the numeric, text and image assets in the set

### 17. A predictive-maintenance model performs unevenly across machine generations, and the team must quantify that before mitigating. What should run first?

- A. Rebalance the numeric, text and image assets in the set
- B. Stratify the train, validation and test splits by label
- C. Reweight the under-represented group in the loss
- D. Measure bias with SageMaker Clarify before training

### 18. Failures are 0.5 percent of records, and some sensor columns are null when a probe was offline. Which two steps fit? Select two.

- A. Impute missing numeric values with the median
- B. Set class weights instead of resampling
- C. Clip extreme outliers to a defined percentile
- D. Drop every row that has any missing field
- E. Generate synthetic minority samples to rebalance the classes

---

## Domain 2 — ML Model and Foundation Model (FM) Development (24%) — Model and FM selection, tuning, customisation, and evaluation

### 19. A quality inspector needs to find the twenty most similar past defects from a small labelled set. What fits?

- A. Use Random Cut Forest for anomaly scoring
- B. Train the tabular classifier with the XGBoost built-in algorithm
- C. Use the k-nearest-neighbours algorithm
- D. Forecast the series with the DeepAR algorithm

### 20. A failure-in-thirty-days classifier has sixty sensor features with non-linear interactions and plenty of history. What fits?

- A. Use the k-nearest-neighbours algorithm
- B. Train with the linear learner algorithm
- C. Train the tabular classifier with the XGBoost built-in algorithm
- D. Forecast the series with the DeepAR algorithm

### 21. A shift-handover assistant must summarise short logs cheaply and quickly at high volume, with no long-context need. Which model choice fits?

- A. Select an Amazon Nova foundation model in Amazon Bedrock
- B. Select a Titan embedding model in Amazon Bedrock
- C. Select an Anthropic Claude model in Amazon Bedrock
- D. Download open weights and host them on your own endpoint

### 22. A model must run inside the plant network on a dedicated endpoint, and the team wants full control of the container. What is required?

- A. Select an Anthropic Claude model in Amazon Bedrock
- B. Start from a SageMaker JumpStart model
- C. Select an Amazon Nova foundation model in Amazon Bedrock
- D. Download open weights and host them on your own endpoint

### 23. The handover summaries are too wordy, and nobody has yet tried a stricter instruction and a worked example. What should be tried first?

- A. Run continued pre-training on the domain corpus
- B. Start with task-specific prompt engineering before any training
- C. Run full-parameter fine-tuning on the curated corpus
- D. Fine-tune with parameter-efficient adapters such as LoRA

### 24. The assistant must adopt the plant's own fault taxonomy, and its general safety language must not degrade. Which two techniques fit? Select two.

- A. Fine-tune with parameter-efficient adapters such as LoRA
- B. Run full-parameter fine-tuning on the curated corpus
- C. Distil the large model into a smaller student model
- D. Mix replay samples from the original distribution into fine-tuning
- E. Run continued pre-training on the domain corpus

### 25. Engineers search by exact fault code as often as by description, and pure vector search misses the codes. What should be added?

- A. Index parent sections and retrieve their child chunks
- B. Combine keyword and vector retrieval
- C. Add a reranking step after retrieval
- D. Store source, date and section metadata with each chunk

### 26. Camera frames on the line must be checked for missing components and for labels with readable text. Which service fits?

- A. Detect objects and text in images with Amazon Rekognition
- B. Detect entities and sentiment with Amazon Comprehend
- C. Transcribe the calls with Amazon Transcribe
- D. Extract the form fields with Amazon Textract

### 27. The team's PyTorch training script uses only standard libraries and must run inside a managed framework container. What fits?

- A. Bring a custom training container image
- B. Start from a SageMaker JumpStart model
- C. Package the training code in script mode with a supported framework
- D. Train the tabular classifier with the XGBoost built-in algorithm

### 28. Two hyperparameters must be sampled at random across wide ranges for a quick sanity check before any serious tuning. What fits?

- A. Use Bayesian search over a defined objective metric
- B. Use random search over a small range
- C. Tune hyperparameters with SageMaker automatic model tuning
- D. Define the tuning objective on the validation metric that matters

### 29. The tuning run must be a managed service, and each trial must stop once its validation curve flattens. Which two elements fit? Select two.

- A. Use random search over a small range
- B. Enable early stopping on the validation metric
- C. Define the tuning objective on the validation metric that matters
- D. Run a hand-written grid of training jobs
- E. Tune hyperparameters with SageMaker automatic model tuning

### 30. A large batch of independent trials each fits on one device, and the gap between jobs is dominated by provisioning time. Which two changes fit? Select two.

- A. Run training on managed Spot training capacity
- B. Shard the model across instances with model parallelism
- C. Keep a managed warm pool for the training cluster
- D. Checkpoint to Amazon S3 so an interrupted job resumes
- E. Split each batch across instances with data parallelism

### 31. The maintenance team can service only a fixed number of machines per week, so a single operating point must be chosen from the score. What fits?

- A. Inspect the confusion matrix on the minority class
- B. Report F1 on the holdout set
- C. Pick the threshold from the precision-recall curve
- D. Report ROC-AUC for the ranking task

### 32. The model must be compared across two thresholds as a ranking, and a single balanced score is needed for the release note. Which two metrics fit? Select two.

- A. Report accuracy alone on a 2 percent positive class
- B. Report RMSE for the regression
- C. Score the generated summaries with BLEU
- D. Report F1 on the holdout set
- E. Report ROC-AUC for the ranking task

### 33. Shift reports generated by two model versions must be compared for meaning, and either wording is acceptable. What fits?

- A. Score the generated summaries with BLEU
- B. Measure semantic similarity to the reference answer
- C. Score the generated summaries with ROUGE
- D. Report RMSE for the regression

### 34. Nobody can say whether this quarter's model is better or worse than the one running now. What should have been recorded?

- A. Log runs with MLflow on SageMaker AI
- B. Record a performance baseline and monitor drift against it
- C. Run an Amazon Bedrock model evaluation job
- D. Register the approved version in the SageMaker Model Registry

---

## Domain 3 — Deployment and Orchestration of ML and AI Workflows (24%) — Inference infrastructure, scaling, CI/CD, and orchestration

### 35. The line controller needs an answer within a second, and a separate long-running anomaly report is requested through an API with results in S3. Which two methods fit? Select two.

- A. Host many small models behind one multi-model endpoint
- B. Deploy a real-time SageMaker AI endpoint
- C. Use asynchronous inference with results written to Amazon S3
- D. Run a batch transform job over the stored records
- E. Deploy a serverless inference endpoint

### 36. An engineer's diagnostic tool is used a few times a shift and must cost nothing when idle. What fits?

- A. Run a batch transform job over the stored records
- B. Use asynchronous inference with results written to Amazon S3
- C. Deploy a real-time SageMaker AI endpoint
- D. Deploy a serverless inference endpoint

### 37. One identical model is deployed per plant, and each plant calls it rarely enough that dedicated endpoints waste money. What fits?

- A. Deploy a real-time SageMaker AI endpoint
- B. Run a batch transform job over the stored records
- C. Run several containers behind one endpoint
- D. Host many small models behind one multi-model endpoint

### 38. Fine-tuned weights produced outside AWS must be served through the Bedrock API without a hosting stack. What fits?

- A. Call the Bedrock model on demand
- B. Buy provisioned throughput for the Bedrock model
- C. Right-size the endpoint with SageMaker Inference Recommender
- D. Import the fine-tuned weights with Bedrock custom model import

### 39. Before committing to a monthly reservation, finance wants to know the volume at which it becomes cheaper than paying per call. What should be done?

- A. Buy provisioned throughput for the Bedrock model
- B. Right-size the endpoint with SageMaker Inference Recommender
- C. Call the Bedrock model on demand
- D. Compare provisioned throughput against on-demand spend

### 40. A maintenance agent must call a work-order API and read the equipment manual during the same conversation. What must be deployed together?

- A. Persist the agent session state between turns
- B. Store the prompt templates in Amazon Bedrock Prompt Management
- C. Schedule a knowledge base sync when documents change
- D. Deploy the agent with its action groups and knowledge base

### 41. A distributed training run lasts nine days across thirty-two accelerators and cannot afford to lose the cluster mid-run. What fits?

- A. Run the workload on a SageMaker HyperPod cluster
- B. Run the container on Amazon ECS
- C. Run the container on Amazon EKS
- D. Run the job on AWS Batch

### 42. Alarms fire in bands as the line restarts and load jumps by multiples, not smoothly. What policy suits those bands?

- A. Scale the endpoint to zero outside business hours
- B. Auto scale on a step policy with CloudWatch alarms
- C. Auto scale the endpoint on a target-tracking policy
- D. Keep provisioned concurrency ready for the burst window

### 43. Load follows the production shift smoothly, and each request occupies the accelerator for seconds so invocation count misleads. Which two settings fit? Select two.

- A. Scale on GPU utilisation rather than invocation count
- B. Auto scale on a step policy with CloudWatch alarms
- C. Scale the endpoint to zero outside business hours
- D. Auto scale the endpoint on a target-tracking policy
- E. Keep a managed warm pool for the training cluster

### 44. Endpoint containers need to reach S3 and CloudWatch with no internet path and no NAT gateway cost. What should be created?

- A. Route the private subnet through a NAT gateway
- B. Create an interface VPC endpoint for the service
- C. Restrict the security group to the application subnet
- D. Allow ingress from any address on the endpoint port

### 45. The team wants its source history in an AWS-managed repository and the release to run through ordered stages. Which two services fit? Select two.

- A. Build and test the model image with AWS CodeBuild
- B. Connect the external repository with AWS CodeConnections
- C. Keep the pipeline source in AWS CodeCommit
- D. Shift traffic with AWS CodeDeploy
- E. Orchestrate the release with AWS CodePipeline

### 46. Traffic must shift between model versions and roll back automatically when an alarm fires. What fits?

- A. Build and test the model image with AWS CodeBuild
- B. Fail the pipeline when the evaluation threshold is missed
- C. Shift traffic with AWS CodeDeploy
- D. Orchestrate the release with AWS CodePipeline

### 47. Each plant runs a different approved model, and the operator must prove which version each plant is serving. What fits?

- A. Register the approved version in the SageMaker Model Registry
- B. Log runs with MLflow on SageMaker AI
- C. Store the prompt templates in Amazon Bedrock Prompt Management
- D. Keep the pipeline source in AWS CodeCommit

### 48. A single plant with one line, no rollback path and a change window of four minutes is asked to adopt a new model. Which strategy is the wrong choice here?

- A. Mirror traffic to the new model without serving its answers
- B. Stand the new version beside the old and switch traffic
- C. Replace the production version in a single switch
- D. Send a small share of traffic to the new version first

### 49. The first plant to adopt the new model must be protected from a bad release, and the shift across plants must be evenly paced. Which two strategies fit? Select two.

- A. Mirror traffic to the new model without serving its answers
- B. Send a small share of traffic to the new version first
- C. Stand the new version beside the old and switch traffic
- D. Shift traffic to the new version in equal steps
- E. Replace the production version in a single switch

### 50. Sensor drift monitoring must trigger a retraining run every night at two, with no host to schedule it. What fits?

- A. Trigger the retraining run with an EventBridge schedule
- B. Orchestrate the steps with AWS Step Functions
- C. Define the workflow as a SageMaker pipeline
- D. Orchestrate the release with AWS CodePipeline

---

## Domain 4 — Operating, Monitoring, and Securing ML and AI Solutions (24%) — Monitoring, cost control, identity, network isolation, and guardrails

### 51. A new lubricant changes the vibration signature, and the model was trained on the old signature. What should have been enabled?

- A. Enable a data drift monitor on the endpoint
- B. Enable a bias drift monitor
- C. Enable feature attribution drift monitoring
- D. Enable a model quality monitor with ground-truth labels

### 52. Failure labels arrive a week late, and the team suspects the model now leans on a single sensor. Which two monitors fit? Select two.

- A. Enable feature attribution drift monitoring
- B. Enable a bias drift monitor
- C. Alarm on the CloudWatch latency and error metrics
- D. Enable a data drift monitor on the endpoint
- E. Enable a model quality monitor with ground-truth labels

### 53. The maintenance queue must page someone when endpoint latency exceeds the line cycle time. What fits?

- A. Alarm on the CloudWatch latency and error metrics
- B. Query the inference logs with CloudWatch Logs Insights
- C. Build a CloudWatch dashboard for the pipeline metrics
- D. Trace the pipeline service calls with AWS X-Ray

### 54. The plant manager wants one screen showing throughput, latency and error rate across every endpoint. What fits?

- A. Build a CloudWatch dashboard for the pipeline metrics
- B. Trace the pipeline service calls with AWS X-Ray
- C. Query the inference logs with CloudWatch Logs Insights
- D. Alarm on the CloudWatch latency and error metrics

### 55. A maintenance agent sometimes calls the work-order API twice for one request, and the team needs to see each tool call. What fits?

- A. Trace agent tool calls with Bedrock AgentCore Observability
- B. Alarm on the CloudWatch latency and error metrics
- C. Trace the pipeline service calls with AWS X-Ray
- D. Enable CloudWatch generative AI observability for the model calls

### 56. All predictions are needed once a shift, six hours after the data lands, and an always-on endpoint waits between shifts. What should replace it?

- A. Cover the steady inference load with a Savings Plan
- B. Move the offline scoring to batch transform
- C. Scale the endpoint to zero outside business hours
- D. Right-size the instance family against the measured latency

### 57. The endpoint family is twice the measured requirement, and the remaining hours are steady through the year. Which two changes fit? Select two.

- A. Right-size the instance family against the measured latency
- B. Break the spend down by endpoint with AWS Cost Explorer
- C. Cover the steady inference load with a Savings Plan
- D. Set an AWS Budget alert on the ML account
- E. Move the offline scoring to batch transform

### 58. The equipment manual index is refreshed nightly although only two documents change each week. What should be added?

- A. Cache embeddings for documents that have not changed
- B. Compare provisioned throughput against on-demand spend
- C. Route routine requests to a smaller model
- D. Trim the retrieved context sent to the model

### 59. A handover summary must never exceed a fixed cost per call, and model output length varies widely. What should be set?

- A. Route routine requests to a smaller model
- B. Trim the retrieved context sent to the model
- C. Cache embeddings for documents that have not changed
- D. Cap the output tokens per request

### 60. A training job needs its own identity, and it should read only one prefix of the data lake. Which two controls fit? Select two.

- A. Attach one policy to an IAM group the engineers belong to
- B. Give the training job a scoped IAM execution role
- C. Attach a policy scoped to the one bucket prefix
- D. Create a long-lived access key for the integration
- E. Use the account root user for pipeline administration

### 61. A pipeline in the central account must read plant data in a plant-owned account without a shared key. What fits?

- A. Attach one policy to an IAM group the engineers belong to
- B. Create a long-lived access key for the integration
- C. Create a role the other account can assume
- D. Use the account root user for pipeline administration

### 62. An endpoint security group was changed to allow traffic from any address, and the audit flagged it. Which setting must not remain?

- A. Restrict the security group to the application subnet
- B. Allow ingress from any address on the endpoint port
- C. Create an interface VPC endpoint for the service
- D. Place the endpoint and model containers in private subnets

### 63. The work-order API token must be rotated every thirty days without a redeployment. What fits?

- A. Store the model API credential in AWS Secrets Manager
- B. Apply Amazon Bedrock Guardrails to the model responses
- C. Encrypt the artefacts with a customer managed KMS key
- D. Track resource configuration with AWS Config

### 64. An assistant must refuse to give repair advice on equipment it has no certification for, through one managed control. What fits?

- A. Screen the training text for unsafe content
- B. Apply Amazon Bedrock Guardrails to the model responses
- C. Configure a denied-topics policy for the assistant
- D. Redact personal data before the prompt reaches the model

### 65. A model endpoint was reconfigured during an incident, and the team must identify the caller and the exact API call. What holds that evidence?

- A. Scan the built image with Amazon Inspector
- B. Track resource configuration with AWS Config
- C. Query the inference logs with CloudWatch Logs Insights
- D. Record the API calls with AWS CloudTrail

---

## Answer key and explanations

### Question 1 — C

Answer: Ingest the events with Amazon Kinesis Data Streams. An ordered stream lets several consumers read the same log independently. Kinesis holds an ordered stream that several consumers can read at their own pace. Local study-map skill 1.1 (Ingestion Sources and Storage Choice), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. A function per record suits lightweight enrichment and filtering of a stream. Why the correct answer wins: An ordered stream lets several consumers read the same log independently.
- **B:** Incorrect for this question. MSK runs managed Kafka, which suits teams already using Kafka clients and topics. Why the correct answer wins: An ordered stream lets several consumers read the same log independently.
- **C:** Correct. Kinesis holds an ordered stream that several consumers can read at their own pace. In this case: An ordered stream lets several consumers read the same log independently.
- **D:** Incorrect for this question. Firehose batches the stream into S3 objects without a consumer to operate. Why the correct answer wins: An ordered stream lets several consumers read the same log independently.

### Question 2 — C

Answer: Apply S3 Object Lock to the regulated training data. Object Lock holds the objects immutable for the retention period. Object Lock prevents the retained objects from being altered or deleted for the stated period. Local study-map skill 1.1 (Ingestion Sources and Storage Choice), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. A lifecycle rule deletes the derived copies on a schedule, so storage does not grow forever. Why the correct answer wins: Object Lock holds the objects immutable for the retention period.
- **B:** Incorrect for this question. An archive class is priced for data that is kept but rarely read. Why the correct answer wins: Object Lock holds the objects immutable for the retention period.
- **C:** Correct. Object Lock prevents the retained objects from being altered or deleted for the stated period. In this case: Object Lock holds the objects immutable for the retention period.
- **D:** Incorrect for this question. Intelligent-Tiering moves objects between access tiers as usage changes, with no rules to write. Why the correct answer wins: Object Lock holds the objects immutable for the retention period.

### Question 3 — C

Answer: Transform each stream record with AWS Lambda. A function per record suits lightweight enrichment inside the stream. Local study-map skill 1.2 (Streaming Ingestion), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Glue runs a managed Spark job against catalogued sources and writes the prepared output. Why the correct answer wins: A function per record suits lightweight enrichment inside the stream.
- **B:** Incorrect for this question. EMR gives a managed Spark cluster sized for the processing job. Why the correct answer wins: A function per record suits lightweight enrichment inside the stream.
- **C:** Correct. In this case: A function per record suits lightweight enrichment inside the stream.
- **D:** Incorrect for this question. Firehose batches the stream into S3 objects without a consumer to operate. Why the correct answer wins: A function per record suits lightweight enrichment inside the stream.

### Question 4 — B

Answer: Use S3 Intelligent-Tiering for the unevenly accessed corpus. Intelligent tiering follows the access pattern without rules to write. Intelligent-Tiering moves objects between access tiers as usage changes, with no rules to write. Local study-map skill 1.3 (Storage Class and Retention), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. An archive class is priced for data that is kept but rarely read. Why the correct answer wins: Intelligent tiering follows the access pattern without rules to write.
- **B:** Correct. Intelligent-Tiering moves objects between access tiers as usage changes, with no rules to write. In this case: Intelligent tiering follows the access pattern without rules to write.
- **C:** Incorrect for this question. Columnar Parquet files in S3 are read in column subsets, which suits repeated training scans. Why the correct answer wins: Intelligent tiering follows the access pattern without rules to write.
- **D:** Incorrect for this question. A lifecycle rule deletes the derived copies on a schedule, so storage does not grow forever. Why the correct answer wins: Intelligent tiering follows the access pattern without rules to write.

### Question 5 — D, E

Answers: Land the dataset as Parquet in Amazon S3; Partition the S3 prefix by event date. A columnar format reads only the needed columns, and plant and date prefixes skip the rest. Columnar Parquet files in S3 are read in column subsets, which suits repeated training scans. Date partitioning lets a query or a training job skip the prefixes it does not need. Local study-map skill 1.4 (Data Formats and Partitioning), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Raw JSON is readable but forces every query to parse whole records. Why the correct answer wins: A columnar format reads only the needed columns, and plant and date prefixes skip the rest.
- **B:** Incorrect for this question. EFS gives many hosts one POSIX file system, which suits shared code and small data. Why the correct answer wins: A columnar format reads only the needed columns, and plant and date prefixes skip the rest.
- **C:** Incorrect for this question. EBS is block storage bound to one instance, which suits a single host and not a fleet. Why the correct answer wins: A columnar format reads only the needed columns, and plant and date prefixes skip the rest.
- **D:** Correct. Columnar Parquet files in S3 are read in column subsets, which suits repeated training scans. In this case: A columnar format reads only the needed columns, and plant and date prefixes skip the rest.
- **E:** Correct. Date partitioning lets a query or a training job skip the prefixes it does not need. In this case: A columnar format reads only the needed columns, and plant and date prefixes skip the rest.

### Question 6 — C

Answer: Land the raw JSON events in Amazon S3 unchanged. A faithful copy can be read without the schema a columnar rewrite imposes. Raw JSON is readable but forces every query to parse whole records. Local study-map skill 1.4 (Data Formats and Partitioning), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Columnar Parquet files in S3 are read in column subsets, which suits repeated training scans. Why the correct answer wins: A faithful copy can be read without the schema a columnar rewrite imposes.
- **B:** Incorrect for this question. Date partitioning lets a query or a training job skip the prefixes it does not need. Why the correct answer wins: A faithful copy can be read without the schema a columnar rewrite imposes.
- **C:** Correct. Raw JSON is readable but forces every query to parse whole records. In this case: A faithful copy can be read without the schema a columnar rewrite imposes.
- **D:** Incorrect for this question. Object Lock prevents the retained objects from being altered or deleted for the stated period. Why the correct answer wins: A faithful copy can be read without the schema a columnar rewrite imposes.

### Question 7 — B

Answer: Transform the data with an AWS Glue ETL job. A managed transform job performs the join with no cluster to run. Glue runs a managed Spark job against catalogued sources and writes the prepared output. Local study-map skill 1.5 (Merge and Transform Tooling), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Data Wrangler builds a reusable preparation flow and can export it into a pipeline. Why the correct answer wins: A managed transform job performs the join with no cluster to run.
- **B:** Correct. Glue runs a managed Spark job against catalogued sources and writes the prepared output. In this case: A managed transform job performs the join with no cluster to run.
- **C:** Incorrect for this question. DataBrew provides a visual recipe for profiling, cleaning and normalising columns. Why the correct answer wins: A managed transform job performs the join with no cluster to run.
- **D:** Incorrect for this question. EMR gives a managed Spark cluster sized for the processing job. Why the correct answer wins: A managed transform job performs the join with no cluster to run.

### Question 8 — A

Answer: Prepare the data in SageMaker Data Wrangler. A visual preparation flow can be built and then exported into the pipeline. Data Wrangler builds a reusable preparation flow and can export it into a pipeline. Local study-map skill 1.5 (Merge and Transform Tooling), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Correct. Data Wrangler builds a reusable preparation flow and can export it into a pipeline. In this case: A visual preparation flow can be built and then exported into the pipeline.
- **B:** Incorrect for this question. A function per record suits lightweight enrichment and filtering of a stream. Why the correct answer wins: A visual preparation flow can be built and then exported into the pipeline.
- **C:** Incorrect for this question. DataBrew provides a visual recipe for profiling, cleaning and normalising columns. Why the correct answer wins: A visual preparation flow can be built and then exported into the pipeline.
- **D:** Incorrect for this question. Glue runs a managed Spark job against catalogued sources and writes the prepared output. Why the correct answer wins: A visual preparation flow can be built and then exported into the pipeline.

### Question 9 — B

Answer: Ingest the cleaned rows into a SageMaker Feature Group. A feature group is the single definition both paths read. A feature group gives one definition that both training and inference read. Local study-map skill 1.6 (Feature Store), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. The online store serves the latest feature values for low-latency inference lookups. Why the correct answer wins: A feature group is the single definition both paths read.
- **B:** Correct. A feature group gives one definition that both training and inference read. In this case: A feature group is the single definition both paths read.
- **C:** Incorrect for this question. The offline store keeps timestamped values so training reads the values that existed at the time. Why the correct answer wins: A feature group is the single definition both paths read.
- **D:** Incorrect for this question. The catalog gives every engine the same table definitions and schemas. Why the correct answer wins: A feature group is the single definition both paths read.

### Question 10 — A

Answer: Bin the continuous age column into ranges. Binning trades resolution for robustness across a very wide range. Binning trades resolution for robustness to small variations inside a range. Local study-map skill 1.7 (Feature Engineering and Scaling), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Correct. Binning trades resolution for robustness to small variations inside a range. In this case: Binning trades resolution for robustness across a very wide range.
- **B:** Incorrect for this question. A log transform compresses the long tail of a heavily skewed amount distribution. Why the correct answer wins: Binning trades resolution for robustness across a very wide range.
- **C:** Incorrect for this question. Scaling puts the numeric columns on comparable ranges so no column dominates the fit. Why the correct answer wins: Binning trades resolution for robustness across a very wide range.
- **D:** Incorrect for this question. One-hot encoding turns unordered categories into separate binary columns. Why the correct answer wins: Binning trades resolution for robustness across a very wide range.

### Question 11 — B, C

Answers: One-hot encode the categorical columns; Shuffle the rows before every epoch. One-hot encoding keeps the categories unordered, and shuffling removes the order artefact. One-hot encoding turns unordered categories into separate binary columns. Shuffling stops the batch order from encoding an accidental pattern. Local study-map skill 1.7 (Feature Engineering and Scaling), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Stratifying keeps the label proportions the same in every split. Why the correct answer wins: One-hot encoding keeps the categories unordered, and shuffling removes the order artefact.
- **B:** Correct. Shuffling stops the batch order from encoding an accidental pattern. In this case: One-hot encoding keeps the categories unordered, and shuffling removes the order artefact.
- **C:** Correct. One-hot encoding turns unordered categories into separate binary columns. In this case: One-hot encoding keeps the categories unordered, and shuffling removes the order artefact.
- **D:** Incorrect for this question. Binning trades resolution for robustness to small variations inside a range. Why the correct answer wins: One-hot encoding keeps the categories unordered, and shuffling removes the order artefact.
- **E:** Incorrect for this question. Scaling puts the numeric columns on comparable ranges so no column dominates the fit. Why the correct answer wins: One-hot encoding keeps the categories unordered, and shuffling removes the order artefact.

### Question 12 — D

Answer: Load every vector into the application process on each request. An in-process index is enough when the corpus is small and already resident. Rebuilding the index per request cannot hold a large corpus or a latency target. Local study-map skill 1.8 (Vector Stores and Embeddings), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. An S3-backed index suits a large, cost-sensitive corpus read less often. Why the correct answer wins: An in-process index is enough when the corpus is small and already resident.
- **B:** Incorrect for this question. OpenSearch provides a managed vector index with filtered k-nearest-neighbour search. Why the correct answer wins: An in-process index is enough when the corpus is small and already resident.
- **C:** Incorrect for this question. pgvector keeps vectors beside relational rows the application already queries. Why the correct answer wins: An in-process index is enough when the corpus is small and already resident.
- **D:** Correct. Rebuilding the index per request cannot hold a large corpus or a latency target. In this case: An in-process index is enough when the corpus is small and already resident.

### Question 13 — A, B

Answers: Fine-tune the embedding model on the domain question-answer pairs; Add a reranking step after retrieval. Domain tuning of the embedding model and a reranking step both lift relevance. Domain tuning moves relevant passages closer to their questions in the vector space. A reranker reorders the retrieved passages by relevance before they reach the model. Local study-map skill 1.8 (Vector Stores and Embeddings), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Correct. Domain tuning moves relevant passages closer to their questions in the vector space. In this case: Domain tuning of the embedding model and a reranking step both lift relevance.
- **B:** Correct. A reranker reorders the retrieved passages by relevance before they reach the model. In this case: Domain tuning of the embedding model and a reranking step both lift relevance.
- **C:** Incorrect for this question. A managed embedding model converts text into vectors without hosts to run. Why the correct answer wins: Domain tuning of the embedding model and a reranking step both lift relevance.
- **D:** Incorrect for this question. Hybrid retrieval catches exact identifiers that a vector search alone can miss. Why the correct answer wins: Domain tuning of the embedding model and a reranking step both lift relevance.
- **E:** Incorrect for this question. OpenSearch provides a managed vector index with filtered k-nearest-neighbour search. Why the correct answer wins: Domain tuning of the embedding model and a reranking step both lift relevance.

### Question 14 — D

Answer: Split the documents into fixed-size overlapping chunks. Fixed overlapping chunks bound the context size when structure is unavailable. Overlapping fixed chunks bound the context size and avoid cutting a sentence in half. Local study-map skill 1.9 (Text Pre-processing and Chunking), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Small child chunks match a query precisely while the parent supplies full context. Why the correct answer wins: Fixed overlapping chunks bound the context size when structure is unavailable.
- **B:** Incorrect for this question. Semantic chunks keep a coherent passage together, which improves what retrieval returns. Why the correct answer wins: Fixed overlapping chunks bound the context size when structure is unavailable.
- **C:** Incorrect for this question. Metadata lets retrieval filter by source or recency and lets answers cite the document. Why the correct answer wins: Fixed overlapping chunks bound the context size when structure is unavailable.
- **D:** Correct. Overlapping fixed chunks bound the context size and avoid cutting a sentence in half. In this case: Fixed overlapping chunks bound the context size when structure is unavailable.

### Question 15 — D

Answer: Enforce a schema contract on the ingested records. A schema check rejects records whose fields changed shape. Local study-map skill 1.10 (Data Quality Validation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Duplicates that straddle splits leak the same row into training and evaluation. Why the correct answer wins: A schema check rejects records whose fields changed shape.
- **B:** Incorrect for this question. A stored profile is what later drift comparison is measured against. Why the correct answer wins: A schema check rejects records whose fields changed shape.
- **C:** Incorrect for this question. Data Quality rules fail the job on nulls, duplicates or range violations before training starts. Why the correct answer wins: A schema check rejects records whose fields changed shape.
- **D:** Correct. In this case: A schema check rejects records whose fields changed shape.

### Question 16 — C

Answer: Use automated data labelling with a human review sample in Ground Truth. Active learning labels most clips automatically and routes uncertain ones to the expert. Active learning labels most records automatically and sends only uncertain ones to a person. Local study-map skill 1.11 (Labelling and Annotation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Augmentation adds plausible variation that the original photographs did not contain. Why the correct answer wins: Active learning labels most clips automatically and routes uncertain ones to the expert.
- **B:** Incorrect for this question. Ground Truth manages the labelling workforce, instructions and quality checks. Why the correct answer wins: Active learning labels most clips automatically and routes uncertain ones to the expert.
- **C:** Correct. Active learning labels most records automatically and sends only uncertain ones to a person. In this case: Active learning labels most clips automatically and routes uncertain ones to the expert.
- **D:** Incorrect for this question. A modality with far fewer examples is under-trained even when the label mix looks even. Why the correct answer wins: Active learning labels most clips automatically and routes uncertain ones to the expert.

### Question 17 — D

Answer: Measure bias with SageMaker Clarify before training. Bias metrics quantify the imbalance before any mitigation is chosen. Clarify reports label and feature bias metrics so the imbalance is quantified first. Local study-map skill 1.12 (Bias Detection and Mitigation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. A modality with far fewer examples is under-trained even when the label mix looks even. Why the correct answer wins: Bias metrics quantify the imbalance before any mitigation is chosen.
- **B:** Incorrect for this question. Stratifying keeps the label proportions the same in every split. Why the correct answer wins: Bias metrics quantify the imbalance before any mitigation is chosen.
- **C:** Incorrect for this question. Reweighting the loss changes what the model is optimised for without discarding data. Why the correct answer wins: Bias metrics quantify the imbalance before any mitigation is chosen.
- **D:** Correct. Clarify reports label and feature bias metrics so the imbalance is quantified first. In this case: Bias metrics quantify the imbalance before any mitigation is chosen.

### Question 18 — A, B

Answers: Set class weights instead of resampling; Impute missing numeric values with the median. Class weights raise the cost of a missed failure, and median imputation keeps those rows. Class weights raise the cost of a minority mistake without inventing rows. Median imputation is robust to a skewed distribution and keeps the row. Local study-map skill 1.13 (Cleaning and Class Imbalance), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Correct. Median imputation is robust to a skewed distribution and keeps the row. In this case: Class weights raise the cost of a missed failure, and median imputation keeps those rows.
- **B:** Correct. Class weights raise the cost of a minority mistake without inventing rows. In this case: Class weights raise the cost of a missed failure, and median imputation keeps those rows.
- **C:** Incorrect for this question. Clipping caps the influence of a few extreme values without deleting the records. Why the correct answer wins: Class weights raise the cost of a missed failure, and median imputation keeps those rows.
- **D:** Incorrect for this question. Dropping rows discards information and can bias the set towards complete records. Why the correct answer wins: Class weights raise the cost of a missed failure, and median imputation keeps those rows.
- **E:** Incorrect for this question. Synthetic minority sampling gives the learner more examples of the rare class. Why the correct answer wins: Class weights raise the cost of a missed failure, and median imputation keeps those rows.

### Question 19 — C

Answer: Use the k-nearest-neighbours algorithm. Nearest neighbours answer a small similarity question directly. Nearest neighbours suit a small, low-dimensional similarity problem. Local study-map skill 2.1 (Model and Algorithm Selection), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. Random Cut Forest assigns an anomaly score to each observation against the learned shape. Why the correct answer wins: Nearest neighbours answer a small similarity question directly.
- **B:** Incorrect for this question. Gradient-boosted trees are the usual strong baseline for tabular data. Why the correct answer wins: Nearest neighbours answer a small similarity question directly.
- **C:** Correct. Nearest neighbours suit a small, low-dimensional similarity problem. In this case: Nearest neighbours answer a small similarity question directly.
- **D:** Incorrect for this question. DeepAR learns across many related time series and returns probabilistic forecasts. Why the correct answer wins: Nearest neighbours answer a small similarity question directly.

### Question 20 — C

Answer: Train the tabular classifier with the XGBoost built-in algorithm. Gradient-boosted trees capture the interactions and give a strong baseline. Gradient-boosted trees are the usual strong baseline for tabular data. Local study-map skill 2.1 (Model and Algorithm Selection), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. Nearest neighbours suit a small, low-dimensional similarity problem. Why the correct answer wins: Gradient-boosted trees capture the interactions and give a strong baseline.
- **B:** Incorrect for this question. A linear model is cheap and interpretable when the relationship is close to linear. Why the correct answer wins: Gradient-boosted trees capture the interactions and give a strong baseline.
- **C:** Correct. Gradient-boosted trees are the usual strong baseline for tabular data. In this case: Gradient-boosted trees capture the interactions and give a strong baseline.
- **D:** Incorrect for this question. DeepAR learns across many related time series and returns probabilistic forecasts. Why the correct answer wins: Gradient-boosted trees capture the interactions and give a strong baseline.

### Question 21 — A

Answer: Select an Amazon Nova foundation model in Amazon Bedrock. Matching model size to a short-answer task controls cost and latency. Nova models are reached through the Bedrock API with no infrastructure to host. Local study-map skill 2.2 (Foundation Model Selection), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Correct. Nova models are reached through the Bedrock API with no infrastructure to host. In this case: Matching model size to a short-answer task controls cost and latency.
- **B:** Incorrect for this question. A Titan embedding model turns text into vectors for search and clustering. Why the correct answer wins: Matching model size to a short-answer task controls cost and latency.
- **C:** Incorrect for this question. Claude models are available through Bedrock for long-context reasoning tasks. Why the correct answer wins: Matching model size to a short-answer task controls cost and latency.
- **D:** Incorrect for this question. Self-hosting gives full control but puts model operations on your team. Why the correct answer wins: Matching model size to a short-answer task controls cost and latency.

### Question 22 — D

Answer: Download open weights and host them on your own endpoint. Self-hosting gives control of weights and container at the cost of operating them. Self-hosting gives full control but puts model operations on your team. Local study-map skill 2.2 (Foundation Model Selection), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. Claude models are available through Bedrock for long-context reasoning tasks. Why the correct answer wins: Self-hosting gives control of weights and container at the cost of operating them.
- **B:** Incorrect for this question. JumpStart supplies a pre-trained model and its deployment template. Why the correct answer wins: Self-hosting gives control of weights and container at the cost of operating them.
- **C:** Incorrect for this question. Nova models are reached through the Bedrock API with no infrastructure to host. Why the correct answer wins: Self-hosting gives control of weights and container at the cost of operating them.
- **D:** Correct. Self-hosting gives full control but puts model operations on your team. In this case: Self-hosting gives control of weights and container at the cost of operating them.

### Question 23 — B

Answer: Start with task-specific prompt engineering before any training. A better-structured prompt often meets the requirement without a training run. Local study-map skill 2.3 (Fine-tuning and Customisation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. Continued pre-training adapts the model to domain vocabulary before task tuning. Why the correct answer wins: A better-structured prompt often meets the requirement without a training run.
- **B:** Correct. In this case: A better-structured prompt often meets the requirement without a training run.
- **C:** Incorrect for this question. Full fine-tuning updates every weight and needs more data, memory and care. Why the correct answer wins: A better-structured prompt often meets the requirement without a training run.
- **D:** Incorrect for this question. Adapters train a small number of parameters, which lowers cost and the risk of forgetting. Why the correct answer wins: A better-structured prompt often meets the requirement without a training run.

### Question 24 — A, D

Answers: Fine-tune with parameter-efficient adapters such as LoRA; Mix replay samples from the original distribution into fine-tuning. Adapters add the taxonomy cheaply, and replay samples preserve the earlier behaviour. Adapters train a small number of parameters, which lowers cost and the risk of forgetting. Replay samples keep the earlier behaviour from being overwritten by the narrow new data. Local study-map skill 2.3 (Fine-tuning and Customisation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Correct. Adapters train a small number of parameters, which lowers cost and the risk of forgetting. In this case: Adapters add the taxonomy cheaply, and replay samples preserve the earlier behaviour.
- **B:** Incorrect for this question. Full fine-tuning updates every weight and needs more data, memory and care. Why the correct answer wins: Adapters add the taxonomy cheaply, and replay samples preserve the earlier behaviour.
- **C:** Incorrect for this question. Distillation transfers the large model behaviour into a cheaper model to serve. Why the correct answer wins: Adapters add the taxonomy cheaply, and replay samples preserve the earlier behaviour.
- **D:** Correct. Replay samples keep the earlier behaviour from being overwritten by the narrow new data. In this case: Adapters add the taxonomy cheaply, and replay samples preserve the earlier behaviour.
- **E:** Incorrect for this question. Continued pre-training adapts the model to domain vocabulary before task tuning. Why the correct answer wins: Adapters add the taxonomy cheaply, and replay samples preserve the earlier behaviour.

### Question 25 — B

Answer: Combine keyword and vector retrieval. Combining keyword and vector retrieval catches exact codes. Hybrid retrieval catches exact identifiers that a vector search alone can miss. Local study-map skill 2.4 (RAG Architecture Patterns), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. Small child chunks match a query precisely while the parent supplies full context. Why the correct answer wins: Combining keyword and vector retrieval catches exact codes.
- **B:** Correct. Hybrid retrieval catches exact identifiers that a vector search alone can miss. In this case: Combining keyword and vector retrieval catches exact codes.
- **C:** Incorrect for this question. A reranker reorders the retrieved passages by relevance before they reach the model. Why the correct answer wins: Combining keyword and vector retrieval catches exact codes.
- **D:** Incorrect for this question. Metadata lets retrieval filter by source or recency and lets answers cite the document. Why the correct answer wins: Combining keyword and vector retrieval catches exact codes.

### Question 26 — A

Answer: Detect objects and text in images with Amazon Rekognition. Managed image analysis covers common object and text detection. Rekognition provides managed image and video analysis for common labels and text. Local study-map skill 2.5 (Managed AI Services), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Correct. Rekognition provides managed image and video analysis for common labels and text. In this case: Managed image analysis covers common object and text detection.
- **B:** Incorrect for this question. Comprehend provides managed entity, key-phrase and sentiment analysis. Why the correct answer wins: Managed image analysis covers common object and text detection.
- **C:** Incorrect for this question. Transcribe converts speech to text and can label speakers. Why the correct answer wins: Managed image analysis covers common object and text detection.
- **D:** Incorrect for this question. Textract reads forms and tables into structured fields without a custom model. Why the correct answer wins: Managed image analysis covers common object and text detection.

### Question 27 — C

Answer: Package the training code in script mode with a supported framework. Script mode runs your own script inside a managed framework container. Local study-map skill 2.6 (Built-in Algorithms and Script Mode), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. A custom image is needed only when the managed framework images cannot carry the dependencies. Why the correct answer wins: Script mode runs your own script inside a managed framework container.
- **B:** Incorrect for this question. JumpStart supplies a pre-trained model and its deployment template. Why the correct answer wins: Script mode runs your own script inside a managed framework container.
- **C:** Correct. In this case: Script mode runs your own script inside a managed framework container.
- **D:** Incorrect for this question. Gradient-boosted trees are the usual strong baseline for tabular data. Why the correct answer wins: Script mode runs your own script inside a managed framework container.

### Question 28 — B

Answer: Use random search over a small range. Random search is a cheap first look across wide ranges. Random search is a cheap baseline but ignores what earlier trials learned. Local study-map skill 2.7 (Hyperparameter Tuning), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. Bayesian search spends the trial budget on the region of the space that looks promising. Why the correct answer wins: Random search is a cheap first look across wide ranges.
- **B:** Correct. Random search is a cheap baseline but ignores what earlier trials learned. In this case: Random search is a cheap first look across wide ranges.
- **C:** Incorrect for this question. Automatic model tuning runs the search over a stated objective metric. Why the correct answer wins: Random search is a cheap first look across wide ranges.
- **D:** Incorrect for this question. The search optimises exactly the metric it is given, so the metric must match the goal. Why the correct answer wins: Random search is a cheap first look across wide ranges.

### Question 29 — B, E

Answers: Tune hyperparameters with SageMaker automatic model tuning; Enable early stopping on the validation metric. Automatic model tuning runs the trials, and early stopping ends the plateaued ones. Automatic model tuning runs the search over a stated objective metric. Early stopping ends a trial once the validation metric stops improving. Local study-map skill 2.7 (Hyperparameter Tuning), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. Random search is a cheap baseline but ignores what earlier trials learned. Why the correct answer wins: Automatic model tuning runs the trials, and early stopping ends the plateaued ones.
- **B:** Correct. Early stopping ends a trial once the validation metric stops improving. In this case: Automatic model tuning runs the trials, and early stopping ends the plateaued ones.
- **C:** Incorrect for this question. The search optimises exactly the metric it is given, so the metric must match the goal. Why the correct answer wins: Automatic model tuning runs the trials, and early stopping ends the plateaued ones.
- **D:** Incorrect for this question. A manual grid costs a job per combination and adapts to nothing. Why the correct answer wins: Automatic model tuning runs the trials, and early stopping ends the plateaued ones.
- **E:** Correct. Automatic model tuning runs the search over a stated objective metric. In this case: Automatic model tuning runs the trials, and early stopping ends the plateaued ones.

### Question 30 — C, E

Answers: Split each batch across instances with data parallelism; Keep a managed warm pool for the training cluster. Data parallelism shortens each trial, and a warm pool removes provisioning delay. Data parallelism shortens wall-clock training when the model still fits on one device. A warm pool removes the provisioning delay between consecutive training jobs. Local study-map skill 2.8 (Training Efficiency and Regularisation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. Spot capacity lowers the cost of a job that can checkpoint and resume. Why the correct answer wins: Data parallelism shortens each trial, and a warm pool removes provisioning delay.
- **B:** Incorrect for this question. Model parallelism is needed when the model weights do not fit on a single device. Why the correct answer wins: Data parallelism shortens each trial, and a warm pool removes provisioning delay.
- **C:** Correct. A warm pool removes the provisioning delay between consecutive training jobs. In this case: Data parallelism shortens each trial, and a warm pool removes provisioning delay.
- **D:** Incorrect for this question. Checkpoints let a reclaimed instance continue from the last saved state. Why the correct answer wins: Data parallelism shortens each trial, and a warm pool removes provisioning delay.
- **E:** Correct. Data parallelism shortens wall-clock training when the model still fits on one device. In this case: Data parallelism shortens each trial, and a warm pool removes provisioning delay.

### Question 31 — C

Answer: Pick the threshold from the precision-recall curve. The precision-recall curve shows what each operating point costs. The operating threshold should follow the cost of a false positive against a false negative. Local study-map skill 2.9 (Classic Model Evaluation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. The confusion matrix shows which class the model keeps confusing. Why the correct answer wins: The precision-recall curve shows what each operating point costs.
- **B:** Incorrect for this question. F1 balances precision and recall, which suits an uneven class mix. Why the correct answer wins: The precision-recall curve shows what each operating point costs.
- **C:** Correct. The operating threshold should follow the cost of a false positive against a false negative. In this case: The precision-recall curve shows what each operating point costs.
- **D:** Incorrect for this question. ROC-AUC measures how well the scores separate the classes across thresholds. Why the correct answer wins: The precision-recall curve shows what each operating point costs.

### Question 32 — D, E

Answers: Report ROC-AUC for the ranking task; Report F1 on the holdout set. AUC compares ranking across thresholds, and F1 gives the balanced single score. ROC-AUC measures how well the scores separate the classes across thresholds. F1 balances precision and recall, which suits an uneven class mix. Local study-map skill 2.9 (Classic Model Evaluation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. Accuracy on a rare class is dominated by the majority and hides missed positives. Why the correct answer wins: AUC compares ranking across thresholds, and F1 gives the balanced single score.
- **B:** Incorrect for this question. RMSE expresses the typical error in the target units and penalises large misses. Why the correct answer wins: AUC compares ranking across thresholds, and F1 gives the balanced single score.
- **C:** Incorrect for this question. BLEU measures n-gram overlap with the reference summaries. Why the correct answer wins: AUC compares ranking across thresholds, and F1 gives the balanced single score.
- **D:** Correct. F1 balances precision and recall, which suits an uneven class mix. In this case: AUC compares ranking across thresholds, and F1 gives the balanced single score.
- **E:** Correct. ROC-AUC measures how well the scores separate the classes across thresholds. In this case: AUC compares ranking across thresholds, and F1 gives the balanced single score.

### Question 33 — B

Answer: Measure semantic similarity to the reference answer. Embedding similarity tolerates wording changes that an n-gram metric penalises. Local study-map skill 2.10 (GenAI and NLP Evaluation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. BLEU measures n-gram overlap with the reference summaries. Why the correct answer wins: Embedding similarity tolerates wording changes that an n-gram metric penalises.
- **B:** Correct. In this case: Embedding similarity tolerates wording changes that an n-gram metric penalises.
- **C:** Incorrect for this question. ROUGE measures recall of reference n-grams, which suits summarisation. Why the correct answer wins: Embedding similarity tolerates wording changes that an n-gram metric penalises.
- **D:** Incorrect for this question. RMSE expresses the typical error in the target units and penalises large misses. Why the correct answer wins: Embedding similarity tolerates wording changes that an n-gram metric penalises.

### Question 34 — B

Answer: Record a performance baseline and monitor drift against it. A stored baseline is the reference any later comparison needs. A stored baseline is the reference a drift monitor compares production against. Local study-map skill 2.11 (Experiment Tracking and Baselines), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. Run logging keeps parameters, metrics and artefacts comparable across experiments. Why the correct answer wins: A stored baseline is the reference any later comparison needs.
- **B:** Correct. A stored baseline is the reference a drift monitor compares production against. In this case: A stored baseline is the reference any later comparison needs.
- **C:** Incorrect for this question. Bedrock evaluation scores model output against built-in or custom metrics. Why the correct answer wins: A stored baseline is the reference any later comparison needs.
- **D:** Incorrect for this question. The registry holds model versions and their approval status for deployment. Why the correct answer wins: A stored baseline is the reference any later comparison needs.

### Question 35 — B, C

Answers: Deploy a real-time SageMaker AI endpoint; Use asynchronous inference with results written to Amazon S3. A real-time endpoint answers the controller, and asynchronous inference handles the long report. A real-time endpoint answers synchronous requests with a persistent host behind it. Asynchronous inference queues large or long requests and returns results through S3. Local study-map skill 3.1 (Inference Strategy), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. A multi-model endpoint loads models on demand from S3 behind shared hosting capacity. Why the correct answer wins: A real-time endpoint answers the controller, and asynchronous inference handles the long report.
- **B:** Correct. A real-time endpoint answers synchronous requests with a persistent host behind it. In this case: A real-time endpoint answers the controller, and asynchronous inference handles the long report.
- **C:** Correct. Asynchronous inference queues large or long requests and returns results through S3. In this case: A real-time endpoint answers the controller, and asynchronous inference handles the long report.
- **D:** Incorrect for this question. Batch transform scores a stored dataset with no endpoint to keep running. Why the correct answer wins: A real-time endpoint answers the controller, and asynchronous inference handles the long report.
- **E:** Incorrect for this question. Serverless inference scales to zero and suits intermittent, short requests. Why the correct answer wins: A real-time endpoint answers the controller, and asynchronous inference handles the long report.

### Question 36 — D

Answer: Deploy a serverless inference endpoint. Serverless inference scales to zero between calls. Serverless inference scales to zero and suits intermittent, short requests. Local study-map skill 3.1 (Inference Strategy), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. Batch transform scores a stored dataset with no endpoint to keep running. Why the correct answer wins: Serverless inference scales to zero between calls.
- **B:** Incorrect for this question. Asynchronous inference queues large or long requests and returns results through S3. Why the correct answer wins: Serverless inference scales to zero between calls.
- **C:** Incorrect for this question. A real-time endpoint answers synchronous requests with a persistent host behind it. Why the correct answer wins: Serverless inference scales to zero between calls.
- **D:** Correct. Serverless inference scales to zero and suits intermittent, short requests. In this case: Serverless inference scales to zero between calls.

### Question 37 — D

Answer: Host many small models behind one multi-model endpoint. A multi-model endpoint loads models on demand behind shared capacity. Local study-map skill 3.2 (Endpoint Architecture), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. A real-time endpoint answers synchronous requests with a persistent host behind it. Why the correct answer wins: A multi-model endpoint loads models on demand behind shared capacity.
- **B:** Incorrect for this question. Batch transform scores a stored dataset with no endpoint to keep running. Why the correct answer wins: A multi-model endpoint loads models on demand behind shared capacity.
- **C:** Incorrect for this question. A multi-container endpoint chains containers such as preprocessing and inference. Why the correct answer wins: A multi-model endpoint loads models on demand behind shared capacity.
- **D:** Correct. In this case: A multi-model endpoint loads models on demand behind shared capacity.

### Question 38 — D

Answer: Import the fine-tuned weights with Bedrock custom model import. Importing the custom model runs those weights on Bedrock infrastructure. Local study-map skill 3.3 (Foundation Model Deployment), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. On-demand calls need no reservation and suit bursty, lower-volume traffic. Why the correct answer wins: Importing the custom model runs those weights on Bedrock infrastructure.
- **B:** Incorrect for this question. Provisioned throughput reserves model capacity for predictable, high-volume traffic. Why the correct answer wins: Importing the custom model runs those weights on Bedrock infrastructure.
- **C:** Incorrect for this question. Inference Recommender benchmarks instance types against the latency and throughput target. Why the correct answer wins: Importing the custom model runs those weights on Bedrock infrastructure.
- **D:** Correct. In this case: Importing the custom model runs those weights on Bedrock infrastructure.

### Question 39 — D

Answer: Compare provisioned throughput against on-demand spend. Comparing the two spend models finds the break-even volume. The reservation only pays off when the steady volume exceeds the break-even point. Local study-map skill 3.3 (Foundation Model Deployment), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. Provisioned throughput reserves model capacity for predictable, high-volume traffic. Why the correct answer wins: Comparing the two spend models finds the break-even volume.
- **B:** Incorrect for this question. Inference Recommender benchmarks instance types against the latency and throughput target. Why the correct answer wins: Comparing the two spend models finds the break-even volume.
- **C:** Incorrect for this question. On-demand calls need no reservation and suit bursty, lower-volume traffic. Why the correct answer wins: Comparing the two spend models finds the break-even volume.
- **D:** Correct. The reservation only pays off when the steady volume exceeds the break-even point. In this case: Comparing the two spend models finds the break-even volume.

### Question 40 — D

Answer: Deploy the agent with its action groups and knowledge base. An agent carries its tools, knowledge base and instructions as one unit. Local study-map skill 3.4 (Agents and Retrieval Runtime), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. Persisted session state keeps multi-turn context without resending the whole history. Why the correct answer wins: An agent carries its tools, knowledge base and instructions as one unit.
- **B:** Incorrect for this question. Prompt Management versions templates so a prompt change is reviewable and reversible. Why the correct answer wins: An agent carries its tools, knowledge base and instructions as one unit.
- **C:** Incorrect for this question. A sync re-indexes changed documents so retrieval does not serve stale passages. Why the correct answer wins: An agent carries its tools, knowledge base and instructions as one unit.
- **D:** Correct. In this case: An agent carries its tools, knowledge base and instructions as one unit.

### Question 41 — A

Answer: Run the workload on a SageMaker HyperPod cluster. A resilient cluster keeps a long distributed run alive across failures. HyperPod keeps a resilient cluster for long distributed training runs. Local study-map skill 3.5 (Containers and Compute Provisioning), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Correct. HyperPod keeps a resilient cluster for long distributed training runs. In this case: A resilient cluster keeps a long distributed run alive across failures.
- **B:** Incorrect for this question. ECS schedules the container on managed cluster capacity. Why the correct answer wins: A resilient cluster keeps a long distributed run alive across failures.
- **C:** Incorrect for this question. EKS runs the container under Kubernetes for teams already standardised on it. Why the correct answer wins: A resilient cluster keeps a long distributed run alive across failures.
- **D:** Incorrect for this question. AWS Batch queues the job and provisions capacity for the run. Why the correct answer wins: A resilient cluster keeps a long distributed run alive across failures.

### Question 42 — B

Answer: Auto scale on a step policy with CloudWatch alarms. Step scaling adds capacity in steps as the alarm breaches. Local study-map skill 3.6 (Autoscaling and Concurrency), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. A scale-to-zero policy removes the idle cost when nothing calls the endpoint. Why the correct answer wins: Step scaling adds capacity in steps as the alarm breaches.
- **B:** Correct. In this case: Step scaling adds capacity in steps as the alarm breaches.
- **C:** Incorrect for this question. Target tracking holds a metric such as invocations per instance near a chosen value. Why the correct answer wins: Step scaling adds capacity in steps as the alarm breaches.
- **D:** Incorrect for this question. Provisioned concurrency pre-warms capacity so the burst does not meet a cold start. Why the correct answer wins: Step scaling adds capacity in steps as the alarm breaches.

### Question 43 — A, D

Answers: Auto scale the endpoint on a target-tracking policy; Scale on GPU utilisation rather than invocation count. Target tracking follows the shift, and accelerator utilisation reflects the bottleneck. Target tracking holds a metric such as invocations per instance near a chosen value. GPU utilisation reflects the real bottleneck when each request is expensive. Local study-map skill 3.6 (Autoscaling and Concurrency), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Correct. GPU utilisation reflects the real bottleneck when each request is expensive. In this case: Target tracking follows the shift, and accelerator utilisation reflects the bottleneck.
- **B:** Incorrect for this question. Step scaling adds capacity in bands as the alarm breaches, which suits sharp bursts. Why the correct answer wins: Target tracking follows the shift, and accelerator utilisation reflects the bottleneck.
- **C:** Incorrect for this question. A scale-to-zero policy removes the idle cost when nothing calls the endpoint. Why the correct answer wins: Target tracking follows the shift, and accelerator utilisation reflects the bottleneck.
- **D:** Correct. Target tracking holds a metric such as invocations per instance near a chosen value. In this case: Target tracking follows the shift, and accelerator utilisation reflects the bottleneck.
- **E:** Incorrect for this question. A warm pool removes the provisioning delay between consecutive training jobs. Why the correct answer wins: Target tracking follows the shift, and accelerator utilisation reflects the bottleneck.

### Question 44 — B

Answer: Create an interface VPC endpoint for the service. A private endpoint keeps the service traffic inside the VPC. Local study-map skill 3.7 (VPC Networking for Endpoints), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. A NAT gateway gives private hosts outbound access without accepting inbound traffic. Why the correct answer wins: A private endpoint keeps the service traffic inside the VPC.
- **B:** Correct. In this case: A private endpoint keeps the service traffic inside the VPC.
- **C:** Incorrect for this question. A security group scoped to the caller subnet allows only the intended traffic. Why the correct answer wins: A private endpoint keeps the service traffic inside the VPC.
- **D:** Incorrect for this question. An open ingress rule exposes the model to anything that can reach the VPC. Why the correct answer wins: A private endpoint keeps the service traffic inside the VPC.

### Question 45 — C, E

Answers: Orchestrate the release with AWS CodePipeline; Keep the pipeline source in AWS CodeCommit. A managed repository holds the history, and a pipeline runs the stages. CodePipeline sequences the build, test and deploy stages and records each outcome. CodeCommit is the managed Git repository the pipeline reads from. Local study-map skill 3.8 (CI/CD Pipelines), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. CodeBuild runs the build and the automated tests in a clean managed environment. Why the correct answer wins: A managed repository holds the history, and a pipeline runs the stages.
- **B:** Incorrect for this question. CodeConnections lets the pipeline read a repository hosted elsewhere. Why the correct answer wins: A managed repository holds the history, and a pipeline runs the stages.
- **C:** Correct. CodeCommit is the managed Git repository the pipeline reads from. In this case: A managed repository holds the history, and a pipeline runs the stages.
- **D:** Incorrect for this question. CodeDeploy performs the traffic shift and can roll back on an alarm. Why the correct answer wins: A managed repository holds the history, and a pipeline runs the stages.
- **E:** Correct. CodePipeline sequences the build, test and deploy stages and records each outcome. In this case: A managed repository holds the history, and a pipeline runs the stages.

### Question 46 — C

Answer: Shift traffic with AWS CodeDeploy. A deployment service performs the shift and the automatic rollback. CodeDeploy performs the traffic shift and can roll back on an alarm. Local study-map skill 3.8 (CI/CD Pipelines), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. CodeBuild runs the build and the automated tests in a clean managed environment. Why the correct answer wins: A deployment service performs the shift and the automatic rollback.
- **B:** Incorrect for this question. A quality gate blocks a release whose measured metric is below the agreed bar. Why the correct answer wins: A deployment service performs the shift and the automatic rollback.
- **C:** Correct. CodeDeploy performs the traffic shift and can roll back on an alarm. In this case: A deployment service performs the shift and the automatic rollback.
- **D:** Incorrect for this question. CodePipeline sequences the build, test and deploy stages and records each outcome. Why the correct answer wins: A deployment service performs the shift and the automatic rollback.

### Question 47 — A

Answer: Register the approved version in the SageMaker Model Registry. A registry holds the versions and their approval status. Local study-map skill 3.9 (Model Registry and Versioning), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Correct. In this case: A registry holds the versions and their approval status.
- **B:** Incorrect for this question. Run logging keeps parameters, metrics and artefacts comparable across experiments. Why the correct answer wins: A registry holds the versions and their approval status.
- **C:** Incorrect for this question. Prompt Management versions templates so a prompt change is reviewable and reversible. Why the correct answer wins: A registry holds the versions and their approval status.
- **D:** Incorrect for this question. CodeCommit is the managed Git repository the pipeline reads from. Why the correct answer wins: A registry holds the versions and their approval status.

### Question 48 — C

Answer: Replace the production version in a single switch. A single switch gives a bad model the entire line at once. A single switch gives a bad model the whole traffic share at once. Local study-map skill 3.10 (Deployment Strategy and Rollback), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. Mirroring collects comparison data with no user impact. Why the correct answer wins: A single switch gives a bad model the entire line at once.
- **B:** Incorrect for this question. Blue/green keeps the previous version ready for an immediate switch back. Why the correct answer wins: A single switch gives a bad model the entire line at once.
- **C:** Correct. A single switch gives a bad model the whole traffic share at once. In this case: A single switch gives a bad model the entire line at once.
- **D:** Incorrect for this question. A canary release limits the blast radius of a bad model to the canary share. Why the correct answer wins: A single switch gives a bad model the entire line at once.

### Question 49 — B, D

Answers: Send a small share of traffic to the new version first; Shift traffic to the new version in equal steps. A canary limits exposure, and a linear shift moves traffic in equal steps. A canary release limits the blast radius of a bad model to the canary share. A linear shift moves traffic gradually while the metrics are watched. Local study-map skill 3.10 (Deployment Strategy and Rollback), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. Mirroring collects comparison data with no user impact. Why the correct answer wins: A canary limits exposure, and a linear shift moves traffic in equal steps.
- **B:** Correct. A canary release limits the blast radius of a bad model to the canary share. In this case: A canary limits exposure, and a linear shift moves traffic in equal steps.
- **C:** Incorrect for this question. Blue/green keeps the previous version ready for an immediate switch back. Why the correct answer wins: A canary limits exposure, and a linear shift moves traffic in equal steps.
- **D:** Correct. A linear shift moves traffic gradually while the metrics are watched. In this case: A canary limits exposure, and a linear shift moves traffic in equal steps.
- **E:** Incorrect for this question. A single switch gives a bad model the whole traffic share at once. Why the correct answer wins: A canary limits exposure, and a linear shift moves traffic in equal steps.

### Question 50 — A

Answer: Trigger the retraining run with an EventBridge schedule. A schedule starts the workflow on a fixed cadence. A schedule starts the pipeline on a fixed cadence without an external cron host. Local study-map skill 3.11 (Orchestration and Retraining), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Correct. A schedule starts the pipeline on a fixed cadence without an external cron host. In this case: A schedule starts the workflow on a fixed cadence.
- **B:** Incorrect for this question. Step Functions coordinates long-running steps and service calls with retries and branching. Why the correct answer wins: A schedule starts the workflow on a fixed cadence.
- **C:** Incorrect for this question. A SageMaker pipeline expresses the processing, training and registration steps as one DAG. Why the correct answer wins: A schedule starts the workflow on a fixed cadence.
- **D:** Incorrect for this question. CodePipeline sequences the build, test and deploy stages and records each outcome. Why the correct answer wins: A schedule starts the workflow on a fixed cadence.

### Question 51 — A

Answer: Enable a data drift monitor on the endpoint. A data drift monitor compares live inputs against the training baseline. Local study-map skill 4.1 (Drift and Model Monitoring), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Correct. In this case: A data drift monitor compares live inputs against the training baseline.
- **B:** Incorrect for this question. A bias monitor watches whether the outcome distribution shifts for a protected group. Why the correct answer wins: A data drift monitor compares live inputs against the training baseline.
- **C:** Incorrect for this question. Attribution drift shows that the model now relies on different features than it did. Why the correct answer wins: A data drift monitor compares live inputs against the training baseline.
- **D:** Incorrect for this question. A quality monitor scores live predictions once the true labels arrive. Why the correct answer wins: A data drift monitor compares live inputs against the training baseline.

### Question 52 — A, E

Answers: Enable a model quality monitor with ground-truth labels; Enable feature attribution drift monitoring. A quality monitor scores the labels when they arrive, and attribution drift shows the new reliance. A quality monitor scores live predictions once the true labels arrive. Attribution drift shows that the model now relies on different features than it did. Local study-map skill 4.1 (Drift and Model Monitoring), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Correct. Attribution drift shows that the model now relies on different features than it did. In this case: A quality monitor scores the labels when they arrive, and attribution drift shows the new reliance.
- **B:** Incorrect for this question. A bias monitor watches whether the outcome distribution shifts for a protected group. Why the correct answer wins: A quality monitor scores the labels when they arrive, and attribution drift shows the new reliance.
- **C:** Incorrect for this question. An alarm on the endpoint metrics pages someone when the service degrades. Why the correct answer wins: A quality monitor scores the labels when they arrive, and attribution drift shows the new reliance.
- **D:** Incorrect for this question. A data drift monitor compares the live request distribution against the training baseline. Why the correct answer wins: A quality monitor scores the labels when they arrive, and attribution drift shows the new reliance.
- **E:** Correct. A quality monitor scores live predictions once the true labels arrive. In this case: A quality monitor scores the labels when they arrive, and attribution drift shows the new reliance.

### Question 53 — A

Answer: Alarm on the CloudWatch latency and error metrics. An alarm on the endpoint metrics pages when the threshold is crossed. An alarm on the endpoint metrics pages someone when the service degrades. Local study-map skill 4.2 (Metrics and Dashboards), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Correct. An alarm on the endpoint metrics pages someone when the service degrades. In this case: An alarm on the endpoint metrics pages when the threshold is crossed.
- **B:** Incorrect for this question. Logs Insights filters and aggregates the request logs to find the failing pattern. Why the correct answer wins: An alarm on the endpoint metrics pages when the threshold is crossed.
- **C:** Incorrect for this question. A dashboard puts the operating metrics in one view for the team. Why the correct answer wins: An alarm on the endpoint metrics pages when the threshold is crossed.
- **D:** Incorrect for this question. X-Ray shows where a request spends its time across the services it touches. Why the correct answer wins: An alarm on the endpoint metrics pages when the threshold is crossed.

### Question 54 — A

Answer: Build a CloudWatch dashboard for the pipeline metrics. A dashboard puts the operating metrics in one view. Local study-map skill 4.2 (Metrics and Dashboards), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Correct. In this case: A dashboard puts the operating metrics in one view.
- **B:** Incorrect for this question. X-Ray shows where a request spends its time across the services it touches. Why the correct answer wins: A dashboard puts the operating metrics in one view.
- **C:** Incorrect for this question. Logs Insights filters and aggregates the request logs to find the failing pattern. Why the correct answer wins: A dashboard puts the operating metrics in one view.
- **D:** Incorrect for this question. An alarm on the endpoint metrics pages someone when the service degrades. Why the correct answer wins: A dashboard puts the operating metrics in one view.

### Question 55 — A

Answer: Trace agent tool calls with Bedrock AgentCore Observability. Agent tracing shows each tool call and where the agent repeated itself. Agent tracing shows which tool call failed or stalled inside a multi-step task. Local study-map skill 4.3 (GenAI Observability), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Correct. Agent tracing shows which tool call failed or stalled inside a multi-step task. In this case: Agent tracing shows each tool call and where the agent repeated itself.
- **B:** Incorrect for this question. An alarm on the endpoint metrics pages someone when the service degrades. Why the correct answer wins: Agent tracing shows each tool call and where the agent repeated itself.
- **C:** Incorrect for this question. X-Ray shows where a request spends its time across the services it touches. Why the correct answer wins: Agent tracing shows each tool call and where the agent repeated itself.
- **D:** Incorrect for this question. Generative AI observability records prompts, token counts and latency per model call. Why the correct answer wins: Agent tracing shows each tool call and where the agent repeated itself.

### Question 56 — B

Answer: Move the offline scoring to batch transform. Batch scoring removes the idle endpoint an always-on deployment keeps. Local study-map skill 4.4 (Cost Optimisation and Purchasing), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. A Savings Plan discounts a predictable hourly spend on eligible compute. Why the correct answer wins: Batch scoring removes the idle endpoint an always-on deployment keeps.
- **B:** Correct. In this case: Batch scoring removes the idle endpoint an always-on deployment keeps.
- **C:** Incorrect for this question. A scale-to-zero policy removes the idle cost when nothing calls the endpoint. Why the correct answer wins: Batch scoring removes the idle endpoint an always-on deployment keeps.
- **D:** Incorrect for this question. Matching the family to the measured workload avoids paying for capacity the model cannot use. Why the correct answer wins: Batch scoring removes the idle endpoint an always-on deployment keeps.

### Question 57 — A, C

Answers: Right-size the instance family against the measured latency; Cover the steady inference load with a Savings Plan. Right-sizing matches capacity to the workload, and a plan discounts the steady hours. Matching the family to the measured workload avoids paying for capacity the model cannot use. A Savings Plan discounts a predictable hourly spend on eligible compute. Local study-map skill 4.4 (Cost Optimisation and Purchasing), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Correct. Matching the family to the measured workload avoids paying for capacity the model cannot use. In this case: Right-sizing matches capacity to the workload, and a plan discounts the steady hours.
- **B:** Incorrect for this question. Cost Explorer groups the bill by service and by tag so the expensive resource is visible. Why the correct answer wins: Right-sizing matches capacity to the workload, and a plan discounts the steady hours.
- **C:** Correct. A Savings Plan discounts a predictable hourly spend on eligible compute. In this case: Right-sizing matches capacity to the workload, and a plan discounts the steady hours.
- **D:** Incorrect for this question. A budget alerts when forecast or actual spend crosses the agreed amount. Why the correct answer wins: Right-sizing matches capacity to the workload, and a plan discounts the steady hours.
- **E:** Incorrect for this question. Batch scoring removes the idle endpoint that an always-on deployment would keep. Why the correct answer wins: Right-sizing matches capacity to the workload, and a plan discounts the steady hours.

### Question 58 — A

Answer: Cache embeddings for documents that have not changed. Caching embeddings skips work for unchanged documents. Re-embedding an unchanged document is wasted spend on every refresh. Local study-map skill 4.5 (Inference Cost and Token Usage), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Correct. Re-embedding an unchanged document is wasted spend on every refresh. In this case: Caching embeddings skips work for unchanged documents.
- **B:** Incorrect for this question. The reservation only pays off when the steady volume exceeds the break-even point. Why the correct answer wins: Caching embeddings skips work for unchanged documents.
- **C:** Incorrect for this question. Routing easy requests to a cheaper model keeps the large model for hard cases. Why the correct answer wins: Caching embeddings skips work for unchanged documents.
- **D:** Incorrect for this question. Sending fewer retrieved tokens lowers both cost and latency on every call. Why the correct answer wins: Caching embeddings skips work for unchanged documents.

### Question 59 — D

Answer: Cap the output tokens per request. A token cap bounds the spend on each call. Output tokens dominate generation cost, so a cap bounds the spend per call. Local study-map skill 4.5 (Inference Cost and Token Usage), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. Routing easy requests to a cheaper model keeps the large model for hard cases. Why the correct answer wins: A token cap bounds the spend on each call.
- **B:** Incorrect for this question. Sending fewer retrieved tokens lowers both cost and latency on every call. Why the correct answer wins: A token cap bounds the spend on each call.
- **C:** Incorrect for this question. Re-embedding an unchanged document is wasted spend on every refresh. Why the correct answer wins: A token cap bounds the spend on each call.
- **D:** Correct. Output tokens dominate generation cost, so a cap bounds the spend per call. In this case: A token cap bounds the spend on each call.

### Question 60 — B, C

Answers: Give the training job a scoped IAM execution role; Attach a policy scoped to the one bucket prefix. An execution role gives the job an identity, and the policy scopes it to the prefix. An execution role grants the job only the permissions its inputs and outputs need. Scoping to the prefix stops a compromised job from reaching the rest of the data lake. Local study-map skill 4.6 (IAM and Credentials), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. A group policy keeps the shared permission set in one reviewable place. Why the correct answer wins: An execution role gives the job an identity, and the policy scopes it to the prefix.
- **B:** Correct. An execution role grants the job only the permissions its inputs and outputs need. In this case: An execution role gives the job an identity, and the policy scopes it to the prefix.
- **C:** Correct. Scoping to the prefix stops a compromised job from reaching the rest of the data lake. In this case: An execution role gives the job an identity, and the policy scopes it to the prefix.
- **D:** Incorrect for this question. A long-lived key keeps working after the project ends unless someone retires it. Why the correct answer wins: An execution role gives the job an identity, and the policy scopes it to the prefix.
- **E:** Incorrect for this question. The root user cannot be limited by policy, so daily use magnifies any mistake. Why the correct answer wins: An execution role gives the job an identity, and the policy scopes it to the prefix.

### Question 61 — C

Answer: Create a role the other account can assume. A role assumption issues temporary credentials across the boundary. A cross-account role issues temporary credentials without sharing a key. Local study-map skill 4.6 (IAM and Credentials), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. A group policy keeps the shared permission set in one reviewable place. Why the correct answer wins: A role assumption issues temporary credentials across the boundary.
- **B:** Incorrect for this question. A long-lived key keeps working after the project ends unless someone retires it. Why the correct answer wins: A role assumption issues temporary credentials across the boundary.
- **C:** Correct. A cross-account role issues temporary credentials without sharing a key. In this case: A role assumption issues temporary credentials across the boundary.
- **D:** Incorrect for this question. The root user cannot be limited by policy, so daily use magnifies any mistake. Why the correct answer wins: A role assumption issues temporary credentials across the boundary.

### Question 62 — B

Answer: Allow ingress from any address on the endpoint port. An open ingress rule exposes the model to anything that can reach the VPC. Local study-map skill 4.7 (Network Isolation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. A security group scoped to the caller subnet allows only the intended traffic. Why the correct answer wins: An open ingress rule exposes the model to anything that can reach the VPC.
- **B:** Correct. In this case: An open ingress rule exposes the model to anything that can reach the VPC.
- **C:** Incorrect for this question. A private endpoint keeps the service traffic inside the VPC without a NAT gateway. Why the correct answer wins: An open ingress rule exposes the model to anything that can reach the VPC.
- **D:** Incorrect for this question. Private subnets remove the inbound internet path to the model hosts. Why the correct answer wins: An open ingress rule exposes the model to anything that can reach the VPC.

### Question 63 — A

Answer: Store the model API credential in AWS Secrets Manager. A managed secret store rotates the credential centrally. Secrets Manager holds the credential centrally and can rotate it. Local study-map skill 4.8 (Encryption and Secrets), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Correct. Secrets Manager holds the credential centrally and can rotate it. In this case: A managed secret store rotates the credential centrally.
- **B:** Incorrect for this question. Guardrails filters denied topics, sensitive data and unsafe content in the response path. Why the correct answer wins: A managed secret store rotates the credential centrally.
- **C:** Incorrect for this question. A customer managed key lets the team control the key policy and revoke access. Why the correct answer wins: A managed secret store rotates the credential centrally.
- **D:** Incorrect for this question. Config records how each resource was configured and evaluates it against rules. Why the correct answer wins: A managed secret store rotates the credential centrally.

### Question 64 — B

Answer: Apply Amazon Bedrock Guardrails to the model responses. Guardrails refuses the denied topics on the response path. Guardrails filters denied topics, sensitive data and unsafe content in the response path. Local study-map skill 4.9 (Guardrails and Responsible AI), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. Safety screening keeps prohibited material out of the model weights. Why the correct answer wins: Guardrails refuses the denied topics on the response path.
- **B:** Correct. Guardrails filters denied topics, sensitive data and unsafe content in the response path. In this case: Guardrails refuses the denied topics on the response path.
- **C:** Incorrect for this question. A denied-topics policy refuses the subject areas the business has ruled out. Why the correct answer wins: Guardrails refuses the denied topics on the response path.
- **D:** Incorrect for this question. Redaction at the boundary keeps personal data out of the model request entirely. Why the correct answer wins: Guardrails refuses the denied topics on the response path.

### Question 65 — D

Answer: Record the API calls with AWS CloudTrail. The audit trail records who called which API and from where. Local study-map skill 4.10 (Audit and Vulnerability Scanning), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. Inspector reports known vulnerabilities in the image before it is deployed. Why the correct answer wins: The audit trail records who called which API and from where.
- **B:** Incorrect for this question. Config records how each resource was configured and evaluates it against rules. Why the correct answer wins: The audit trail records who called which API and from where.
- **C:** Incorrect for this question. Logs Insights filters and aggregates the request logs to find the failing pattern. Why the correct answer wins: The audit trail records who called which API and from where.
- **D:** Correct. In this case: The audit trail records who called which API and from where.
