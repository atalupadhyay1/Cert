# AWS Certified Machine Learning Engineer – Associate (MLA-C02) — Full-Length Mock Exam 2

Machine Learning Engineer · 65 questions · 130 minutes · scaled passing score 720 of 1000

Blueprint-weighted mock exam. Item mix: 50 multiple-choice and 15 multiple-response items (the selection count is stated in each multi-response stem). The published exam has 65 questions in 130 minutes, of which 50 are scored and 15 are unscored, and AWS does not identify the unscored items. AWS publishes no split between multiple-choice and multiple-response items, so the 15-item multi-response block is an authoring choice. At 65 items in 130 minutes this set matches the published pacing at about 120 seconds per item. AWS is currently delivering MLA-C02 as a beta of 85 questions in 170 minutes with the extra items unscored; this set follows the published 65-question form. The published format has no case-study component, so no case-study item appears here. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied AWS exam items.

## Questions

---

## Domain 1 — Data Preparation for ML and AI (28%) — Ingestion, storage, feature engineering, embeddings, and data quality

### 1. Fraud analysts query core-banking extracts with Athena while a Spark job reads the same tables, and the two disagree about column types. What should hold the schema?

- A. Land the dataset as Parquet in Amazon S3
- B. Use Amazon FSx for Lustre for the training file system
- C. Mount a shared Amazon EFS file system on every training host
- D. Register the tables in the AWS Glue Data Catalog

### 2. A single notebook instance needs a fast local scratch disk for a shuffle that spills, and nothing else will mount it. What storage fits?

- A. Attach a gp3 Amazon EBS volume to the training instance
- B. Use S3 Intelligent-Tiering for the unevenly accessed corpus
- C. Mount a shared Amazon EFS file system on every training host
- D. Use Amazon FSx for Lustre for the training file system

### 3. The fraud platform already runs Kafka clients and topic tooling, and the team wants to keep that programming model on AWS. What should ingest the events?

- A. Deliver the stream to Amazon S3 with Amazon Data Firehose
- B. Transform each stream record with AWS Lambda
- C. Ingest the events with Amazon Kinesis Data Streams
- D. Ingest the events through Amazon MSK

### 4. Monthly model snapshots must move to cheaper storage after ninety days and be deleted after three years, all automatically. What should be configured?

- A. Use S3 Intelligent-Tiering for the unevenly accessed corpus
- B. Archive the raw corpus to an S3 Glacier storage class
- C. Apply S3 Object Lock to the regulated training data
- D. Expire intermediate artefacts with an S3 lifecycle rule

### 5. A claims feed arrives as nested JSON with irregular fields, and a human must inspect a single claim straight from the stored object. Why keep the raw JSON?

- A. Attach a gp3 Amazon EBS volume to the training instance
- B. Mount a shared Amazon EFS file system on every training host
- C. Land the raw JSON events in Amazon S3 unchanged
- D. Land the dataset as Parquet in Amazon S3

### 6. Fraud features are rebuilt for one region and one week at a time, yet each run scans every region for five years. What should the layout support?

- A. Mount a shared Amazon EFS file system on every training host
- B. Partition the S3 prefix by event date
- C. Use S3 Intelligent-Tiering for the unevenly accessed corpus
- D. Land the raw JSON events in Amazon S3 unchanged

### 7. An analyst must profile and normalise claims columns interactively without writing code, and the cleaned output must be queryable by every engine. Which two services fit? Select two.

- A. Prepare the data in SageMaker Data Wrangler
- B. Profile and clean the data with AWS Glue DataBrew
- C. Replicate the operational tables with AWS Database Migration Service
- D. Process the data with Spark on Amazon EMR
- E. Register the tables in the AWS Glue Data Catalog

### 8. A nightly job must rerun the same transformation over five years of history with custom Scala libraries, on a cluster sized for the job. What fits?

- A. Transform the data with an AWS Glue ETL job
- B. Process the data with Spark on Amazon EMR
- C. Profile and clean the data with AWS Glue DataBrew
- D. Transform each stream record with AWS Lambda

### 9. A chargeback model must be trained on the customer features that existed at the moment of each transaction, not today's values. What provides that?

- A. Publish the features to the SageMaker Feature Store online store
- B. Ingest the cleaned rows into a SageMaker Feature Group
- C. Keep the point-in-time history in the Feature Store offline store
- D. Register the tables in the AWS Glue Data Catalog

### 10. Numeric columns need scaling, and the categorical product family must become model input without implying an order. Which two steps fit? Select two.

- A. Fit the scaler on the training split only
- B. Apply a log transform to the skewed amount column
- C. Standardise the numeric columns before training
- D. Bin the continuous age column into ranges
- E. One-hot encode the categorical columns

### 11. Claim amounts follow a long-tailed distribution, and the regression keeps chasing the few very large claims. What transformation fits?

- A. One-hot encode the categorical columns
- B. Bin the continuous age column into ranges
- C. Standardise the numeric columns before training
- D. Apply a log transform to the skewed amount column

### 12. Policy clauses must be searched by meaning and must stay joined to the relational table of policy numbers the application already queries. Which two components fit? Select two.

- A. Generate the embeddings with an Amazon Bedrock embedding model
- B. Keep the vectors in Amazon S3 with a vector index
- C. Load every vector into the application process on each request
- D. Index the vectors in Amazon OpenSearch Service with k-NN search
- E. Store the vectors in Amazon RDS for PostgreSQL with pgvector

### 13. Adjusters search by exact claim number as often as by description, and vector search alone returns nothing useful for an exact identifier. What should be added?

- A. Combine keyword and vector retrieval
- B. Store the vectors in Amazon RDS for PostgreSQL with pgvector
- C. Add a reranking step after retrieval
- D. Index the vectors in Amazon OpenSearch Service with k-NN search

### 14. Token counts for a hosted model keep exceeding its context limit even though the same text fit before a model change. What should the pipeline use?

- A. Mask and redact personal identifiers before training
- B. Split the documents into fixed-size overlapping chunks
- C. Tokenise the text with the target model tokeniser
- D. Chunk the documents on semantic boundaries such as headings

### 15. An instruction-tuning set contains empty responses and prompts paired with the wrong answer, and it was assembled from three vendors. What check is missing?

- A. Profile the incoming data and store the statistics as a baseline
- B. Validate each prompt-response pair before it enters the training set
- C. Evaluate AWS Glue Data Quality rules on the prepared table
- D. Enforce a schema contract on the ingested records

### 16. Fraud analysts must label five thousand disputed transactions, and the labels need adjudication between two analysts plus an audit trail. What fits?

- A. Mask and redact personal identifiers before training
- B. Use automated data labelling with a human review sample in Ground Truth
- C. Send the unlabelled records to Amazon SageMaker Ground Truth
- D. Augment the image set with rotations, crops and flips

### 17. A credit model has been measured as under-scoring one age band, and the business will not exclude any applicant group from the data. What mitigation fits?

- A. Reweight the under-represented group in the loss
- B. Rebalance the numeric, text and image assets in the set
- C. Measure bias with SageMaker Clarify before training
- D. Stratify the train, validation and test splits by label

### 18. A fraud set is one percent positive, and the same disputed transaction was exported into both the training and the validation split. Which two steps fit? Select two.

- A. Generate synthetic minority samples to rebalance the classes
- B. Clip extreme outliers to a defined percentile
- C. Impute missing numeric values with the median
- D. One-hot encode the categorical columns
- E. Remove duplicate rows before splitting

---

## Domain 2 — ML Model and Foundation Model (FM) Development (24%) — Model and FM selection, tuning, customisation, and evaluation

### 19. Unlabelled payment events must be scored for how unusual they look against the last ninety days, with no fraud labels available yet. Which algorithm fits?

- A. Train the tabular classifier with the XGBoost built-in algorithm
- B. Train with the linear learner algorithm
- C. Forecast the series with the DeepAR algorithm
- D. Use Random Cut Forest for anomaly scoring

### 20. A treasury team needs probabilistic cash-flow forecasts across two thousand related accounts. Which algorithm fits?

- A. Forecast the series with the DeepAR algorithm
- B. Train the tabular classifier with the XGBoost built-in algorithm
- C. Train with the linear learner algorithm
- D. Use the k-nearest-neighbours algorithm

### 21. A claims assistant needs short, cheap, low-latency answers at very high volume, and the workload does not need long context. Which model choice fits?

- A. Select an Amazon Nova foundation model in Amazon Bedrock
- B. Download open weights and host them on your own endpoint
- C. Select an Anthropic Claude model in Amazon Bedrock
- D. Select a Titan embedding model in Amazon Bedrock

### 22. A model must run inside a dedicated endpoint for a residency reason, with full control of the weights and the container. What is required?

- A. Start from a SageMaker JumpStart model
- B. Download open weights and host them on your own endpoint
- C. Select an Amazon Nova foundation model in Amazon Bedrock
- D. Select an Anthropic Claude model in Amazon Bedrock

### 23. A first attempt at the claims assistant is underperforming, and the team wants to try a better instruction template before spending on training. Which two steps fit, in that order? Select two.

- A. Run continued pre-training on the domain corpus
- B. Start with task-specific prompt engineering before any training
- C. Run full-parameter fine-tuning on the curated corpus
- D. Distil the large model into a smaller student model
- E. Fine-tune with parameter-efficient adapters such as LoRA

### 24. A generic model must acquire a new underwriting decision style across a large curated corpus, and the team accepts a longer training run. What fits?

- A. Fine-tune with parameter-efficient adapters such as LoRA
- B. Distil the large model into a smaller student model
- C. Run continued pre-training on the domain corpus
- D. Run full-parameter fine-tuning on the curated corpus

### 25. Retrieval returns the right clauses but ranks a tangential clause first, which pushes the answer off course. What should be added?

- A. Store source, date and section metadata with each chunk
- B. Combine keyword and vector retrieval
- C. Index parent sections and retrieve their child chunks
- D. Add a reranking step after retrieval

### 26. KYC correspondence must be screened for entities and sentiment at scale with no custom model to train. Which service fits?

- A. Extract the form fields with Amazon Textract
- B. Detect entities and sentiment with Amazon Comprehend
- C. Transcribe the calls with Amazon Transcribe
- D. Detect objects and text in images with Amazon Rekognition

### 27. A small team needs a pre-trained text classifier deployed this week, with a supported deployment template and no training data of its own. What fits?

- A. Bring a custom training container image
- B. Train the tabular classifier with the XGBoost built-in algorithm
- C. Start from a SageMaker JumpStart model
- D. Package the training code in script mode with a supported framework

### 28. Tuning is optimising accuracy while the business cares about recall on the positive class, and the chosen winner performs badly in production. What should change?

- A. Define the tuning objective on the validation metric that matters
- B. Run a hand-written grid of training jobs
- C. Use random search over a small range
- D. Enable early stopping on the validation metric

### 29. A managed service must run the search, and later trials should be chosen from what earlier trials revealed. Which two elements fit? Select two.

- A. Use random search over a small range
- B. Run a hand-written grid of training jobs
- C. Use Bayesian search over a defined objective metric
- D. Tune hyperparameters with SageMaker automatic model tuning
- E. Keep a managed warm pool for the training cluster

### 30. Training accuracy has reached 0.99 while validation sits at 0.71, and the gap is widening with each epoch. Which two responses fit? Select two.

- A. Average several models into an ensemble
- B. Increase model capacity and train for more epochs
- C. Add regularisation and reduce model capacity
- D. Checkpoint to Amazon S3 so an interrupted job resumes
- E. Add training data and keep a held-out validation split

### 31. A fraud model must be released at a threshold, and the team needs to see the trade-off between missed fraud and false alarms before choosing it. Which two outputs fit? Select two.

- A. Inspect the confusion matrix on the minority class
- B. Report accuracy alone on a 2 percent positive class
- C. Report ROC-AUC for the ranking task
- D. Pick the threshold from the precision-recall curve
- E. Report RMSE for the regression

### 32. A claims-severity regressor must be reported in currency units that a business reader can interpret. Which metric fits?

- A. Score the generated summaries with BLEU
- B. Report ROC-AUC for the ranking task
- C. Report RMSE for the regression
- D. Report F1 on the holdout set

### 33. Explanations written by the model must be graded for helpfulness and tone, where no single reference answer exists. What fits?

- A. Add a human review loop for a sample of answers
- B. Score the generated summaries with ROUGE
- C. Use an LLM-as-a-judge rubric for the open-ended answers
- D. Score the generated summaries with BLEU

### 34. Two candidate models must be compared on the same evaluation dataset through a managed job that reports the score. What fits?

- A. Log runs with MLflow on SageMaker AI
- B. Run an Amazon Bedrock model evaluation job
- C. Store the prompt templates in Amazon Bedrock Prompt Management
- D. Register the approved version in the SageMaker Model Registry

---

## Domain 3 — Deployment and Orchestration of ML and AI Workflows (24%) — Inference infrastructure, scaling, CI/CD, and orchestration

### 35. Most requests arrive all day at steady load, and a separate internal tool is called a few times an hour and may go idle. Which two deployment methods fit? Select two.

- A. Deploy a real-time SageMaker AI endpoint
- B. Use asynchronous inference with results written to Amazon S3
- C. Host many small models behind one multi-model endpoint
- D. Deploy a serverless inference endpoint
- E. Run a batch transform job over the stored records

### 36. Every night the whole policy portfolio must be rescored, and nothing calls the model during the day. What fits?

- A. Run a batch transform job over the stored records
- B. Deploy a serverless inference endpoint
- C. Deploy a real-time SageMaker AI endpoint
- D. Use asynchronous inference with results written to Amazon S3

### 37. A preprocessing step and the model must run behind one endpoint call so the raw request never leaves the endpoint. What fits?

- A. Host many small models behind one multi-model endpoint
- B. Run several containers behind one endpoint
- C. Deploy a serverless inference endpoint
- D. Deploy a real-time SageMaker AI endpoint

### 38. The main claims assistant runs at a steady high volume, and throttling during the month-end peak has already delayed responses. What should be purchased?

- A. Right-size the endpoint with SageMaker Inference Recommender
- B. Compare provisioned throughput against on-demand spend
- C. Buy provisioned throughput for the Bedrock model
- D. Call the Bedrock model on demand

### 39. A vendor supplied fine-tuned weights that must be served through the Bedrock API without building a hosting stack. What fits?

- A. Import the fine-tuned weights with Bedrock custom model import
- B. Start from a SageMaker JumpStart model
- C. Buy provisioned throughput for the Bedrock model
- D. Download open weights and host them on your own endpoint

### 40. A claims agent must remember the policy number collected three turns earlier without resending the whole conversation on every call. What should be implemented?

- A. Store the prompt templates in Amazon Bedrock Prompt Management
- B. Schedule a knowledge base sync when documents change
- C. Deploy the agent with its action groups and knowledge base
- D. Persist the agent session state between turns

### 41. A monthly risk simulation must run for six hours on forty machines and then stop, with no service to keep running. What fits?

- A. Run the container on Amazon ECS
- B. Run the job on AWS Batch
- C. Serve the model from an AWS Lambda function
- D. Run the container on Amazon EKS

### 42. Fraud checks spike sharply at month end, and a cold start during that spike is unacceptable. Which two settings fit? Select two.

- A. Auto scale on a step policy with CloudWatch alarms
- B. Scale the endpoint to zero outside business hours
- C. Auto scale the endpoint on a target-tracking policy
- D. Keep provisioned concurrency ready for the burst window
- E. Scale on GPU utilisation rather than invocation count

### 43. An internal underwriting model is used only between nine and five on weekdays, and idle nights are the largest cost line. What should be configured?

- A. Keep a managed warm pool for the training cluster
- B. Auto scale the endpoint on a target-tracking policy
- C. Scale the endpoint to zero outside business hours
- D. Auto scale on a step policy with CloudWatch alarms

### 44. An underwriting endpoint must accept calls only from the application subnet and from nowhere else inside the VPC. What should be applied?

- A. Allow ingress from any address on the endpoint port
- B. Create an interface VPC endpoint for the service
- C. Restrict the security group to the application subnet
- D. Place the endpoint and model containers in private subnets

### 45. Releases must move through build and test stages in a defined order, and the image build must happen in a clean managed environment. Which two services fit? Select two.

- A. Keep the pipeline source in AWS CodeCommit
- B. Shift traffic with AWS CodeDeploy
- C. Connect the external repository with AWS CodeConnections
- D. Build and test the model image with AWS CodeBuild
- E. Orchestrate the release with AWS CodePipeline

### 46. The pipeline must read a repository hosted outside AWS without mirroring it into another service. What should be configured?

- A. Connect the external repository with AWS CodeConnections
- B. Orchestrate the release with AWS CodePipeline
- C. Keep the pipeline source in AWS CodeCommit
- D. Build and test the model image with AWS CodeBuild

### 47. Auditors want every prompt change versioned, reviewable and reversible without a code release. What fits?

- A. Register the approved version in the SageMaker Model Registry
- B. Store the prompt templates in Amazon Bedrock Prompt Management
- C. Keep the pipeline source in AWS CodeCommit
- D. Log runs with MLflow on SageMaker AI

### 48. A new fraud threshold model must never receive more new traffic than has been validated, and the shift must be gradual across checks. Which two strategies fit? Select two.

- A. Stand the new version beside the old and switch traffic
- B. Mirror traffic to the new model without serving its answers
- C. Replace the production version in a single switch
- D. Send a small share of traffic to the new version first
- E. Shift traffic to the new version in equal steps

### 49. The previous model must stay warm and switchable within seconds if the new one misbehaves. What fits?

- A. Replace the production version in a single switch
- B. Send a small share of traffic to the new version first
- C. Stand the new version beside the old and switch traffic
- D. Mirror traffic to the new model without serving its answers

### 50. Retraining must start on the first Sunday of each month without a cron host or a human trigger. What fits?

- A. Define the workflow as a SageMaker pipeline
- B. Orchestrate the release with AWS CodePipeline
- C. Trigger the retraining run with an EventBridge schedule
- D. Orchestrate the steps with AWS Step Functions

---

## Domain 4 — Operating, Monitoring, and Securing ML and AI Solutions (24%) — Monitoring, cost control, identity, network isolation, and guardrails

### 51. Chargeback outcomes arrive after thirty days, and the team must prove whether the model got worse once those labels land. What fits?

- A. Enable a bias drift monitor
- B. Enable a data drift monitor on the endpoint
- C. Enable feature attribution drift monitoring
- D. Enable a model quality monitor with ground-truth labels

### 52. The input mix shifted after a new card product launched, and one age band must be watched for a changing outcome rate. Which two monitors fit? Select two.

- A. Alarm on the CloudWatch latency and error metrics
- B. Enable feature attribution drift monitoring
- C. Enable a bias drift monitor
- D. Enable a data drift monitor on the endpoint
- E. Enable a model quality monitor with ground-truth labels

### 53. Executives want one view of endpoint latency, error rate and queue depth, refreshed continuously. What fits?

- A. Trace the pipeline service calls with AWS X-Ray
- B. Build a CloudWatch dashboard for the pipeline metrics
- C. Query the inference logs with CloudWatch Logs Insights
- D. Alarm on the CloudWatch latency and error metrics

### 54. A batch of scoring requests returned wrong values yesterday, and the team needs the common pattern across millions of log lines. What fits?

- A. Query the inference logs with CloudWatch Logs Insights
- B. Track resource configuration with AWS Config
- C. Build a CloudWatch dashboard for the pipeline metrics
- D. Alarm on the CloudWatch latency and error metrics

### 55. A multi-step claims agent sometimes stops after two of five tool calls, and the team cannot see which tool stalled. What fits?

- A. Trace the pipeline service calls with AWS X-Ray
- B. Trace agent tool calls with Bedrock AgentCore Observability
- C. Enable CloudWatch generative AI observability for the model calls
- D. Alarm on the CloudWatch latency and error metrics

### 56. The monthly ML bill doubled and nobody can say which endpoint caused it. What fits?

- A. Set an AWS Budget alert on the ML account
- B. Move the offline scoring to batch transform
- C. Cover the steady inference load with a Savings Plan
- D. Break the spend down by endpoint with AWS Cost Explorer

### 57. Scores are produced overnight in bulk while an idle endpoint waits, and the endpoint family is larger than the measured latency needs. Which two changes fit? Select two.

- A. Move the offline scoring to batch transform
- B. Start with the largest available model for every request
- C. Scale the endpoint to zero outside business hours
- D. Right-size the instance family against the measured latency
- E. Cover the steady inference load with a Savings Plan

### 58. The assistant must never spend more than a fixed amount per call, because output length varies wildly. What should be set?

- A. Route routine requests to a smaller model
- B. Trim the retrieved context sent to the model
- C. Cache embeddings for documents that have not changed
- D. Cap the output tokens per request

### 59. The policy index is rebuilt weekly even though most documents are unchanged, and embedding spend grows each week. What should be added?

- A. Cache embeddings for documents that have not changed
- B. Compare provisioned throughput against on-demand spend
- C. Trim the retrieved context sent to the model
- D. Route routine requests to a smaller model

### 60. Fifty analysts need a shared permission set that is reviewed quarterly, and no account in the organisation may enable an unapproved Region. Which two controls fit? Select two.

- A. Create a long-lived access key for the integration
- B. Attach one policy to an IAM group the engineers belong to
- C. Use the account root user for pipeline administration
- D. Apply a service control policy at the organisation level
- E. Create a role the other account can assume

### 61. An application needs programmatic access to a Bedrock model, and the security team refuses long-lived IAM keys in configuration files. What fits?

- A. Attach one policy to an IAM group the engineers belong to
- B. Use the account root user for pipeline administration
- C. Create a long-lived access key for the integration
- D. Issue a Bedrock API key for the calling application

### 62. The training bucket must be readable only from inside the VPC, even if a valid identity calls it from elsewhere. What should be applied?

- A. Deny access to the bucket unless the request comes through the VPC endpoint
- B. Restrict the security group to the application subnet
- C. Create an interface VPC endpoint for the service
- D. Place the endpoint and model containers in private subnets

### 63. The model provider credential must be rotated every thirty days with no redeployment. What fits?

- A. Track resource configuration with AWS Config
- B. Store the model API credential in AWS Secrets Manager
- C. Apply Amazon Bedrock Guardrails to the model responses
- D. Encrypt the artefacts with a customer managed KMS key

### 64. An assistant must refuse to discuss competitor products while leaving other questions untouched. What fits?

- A. Configure a denied-topics policy for the assistant
- B. Screen the training text for unsafe content
- C. Apply Amazon Bedrock Guardrails to the model responses
- D. Redact personal data before the prompt reaches the model

### 65. Every image built by the pipeline must be checked for known vulnerabilities before it can be deployed. What fits?

- A. Record the API calls with AWS CloudTrail
- B. Scan the built image with Amazon Inspector
- C. Review the pipeline code with Amazon CodeGuru
- D. Track resource configuration with AWS Config

---

## Answer key and explanations

### Question 1 — D

Answer: Register the tables in the AWS Glue Data Catalog. A shared catalog gives every engine one definition of the table. Local study-map skill 1.1 (Ingestion Sources and Storage Choice), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Columnar Parquet files in S3 are read in column subsets, which suits repeated training scans. Why the correct answer wins: A shared catalog gives every engine one definition of the table.
- **B:** Incorrect for this question. Lustre delivers the high throughput a multi-node training job needs from shared storage. Why the correct answer wins: A shared catalog gives every engine one definition of the table.
- **C:** Incorrect for this question. EFS gives many hosts one POSIX file system, which suits shared code and small data. Why the correct answer wins: A shared catalog gives every engine one definition of the table.
- **D:** Correct. In this case: A shared catalog gives every engine one definition of the table.

### Question 2 — A

Answer: Attach a gp3 Amazon EBS volume to the training instance. Block storage attached to that one instance is the right shape for node-local scratch. EBS is block storage bound to one instance, which suits a single host and not a fleet. Local study-map skill 1.1 (Ingestion Sources and Storage Choice), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Correct. EBS is block storage bound to one instance, which suits a single host and not a fleet. In this case: Block storage attached to that one instance is the right shape for node-local scratch.
- **B:** Incorrect for this question. Intelligent-Tiering moves objects between access tiers as usage changes, with no rules to write. Why the correct answer wins: Block storage attached to that one instance is the right shape for node-local scratch.
- **C:** Incorrect for this question. EFS gives many hosts one POSIX file system, which suits shared code and small data. Why the correct answer wins: Block storage attached to that one instance is the right shape for node-local scratch.
- **D:** Incorrect for this question. Lustre delivers the high throughput a multi-node training job needs from shared storage. Why the correct answer wins: Block storage attached to that one instance is the right shape for node-local scratch.

### Question 3 — D

Answer: Ingest the events through Amazon MSK. Managed Kafka keeps the existing client code and topic model. MSK runs managed Kafka, which suits teams already using Kafka clients and topics. Local study-map skill 1.2 (Streaming Ingestion), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Firehose batches the stream into S3 objects without a consumer to operate. Why the correct answer wins: Managed Kafka keeps the existing client code and topic model.
- **B:** Incorrect for this question. A function per record suits lightweight enrichment and filtering of a stream. Why the correct answer wins: Managed Kafka keeps the existing client code and topic model.
- **C:** Incorrect for this question. Kinesis holds an ordered stream that several consumers can read at their own pace. Why the correct answer wins: Managed Kafka keeps the existing client code and topic model.
- **D:** Correct. MSK runs managed Kafka, which suits teams already using Kafka clients and topics. In this case: Managed Kafka keeps the existing client code and topic model.

### Question 4 — D

Answer: Expire intermediate artefacts with an S3 lifecycle rule. A lifecycle rule transitions and expires the objects on a schedule. A lifecycle rule deletes the derived copies on a schedule, so storage does not grow forever. Local study-map skill 1.3 (Storage Class and Retention), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Intelligent-Tiering moves objects between access tiers as usage changes, with no rules to write. Why the correct answer wins: A lifecycle rule transitions and expires the objects on a schedule.
- **B:** Incorrect for this question. An archive class is priced for data that is kept but rarely read. Why the correct answer wins: A lifecycle rule transitions and expires the objects on a schedule.
- **C:** Incorrect for this question. Object Lock prevents the retained objects from being altered or deleted for the stated period. Why the correct answer wins: A lifecycle rule transitions and expires the objects on a schedule.
- **D:** Correct. A lifecycle rule deletes the derived copies on a schedule, so storage does not grow forever. In this case: A lifecycle rule transitions and expires the objects on a schedule.

### Question 5 — C

Answer: Land the raw JSON events in Amazon S3 unchanged. A self-describing record can be read without the table definition that a columnar file needs. Raw JSON is readable but forces every query to parse whole records. Local study-map skill 1.4 (Data Formats and Partitioning), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. EBS is block storage bound to one instance, which suits a single host and not a fleet. Why the correct answer wins: A self-describing record can be read without the table definition that a columnar file needs.
- **B:** Incorrect for this question. EFS gives many hosts one POSIX file system, which suits shared code and small data. Why the correct answer wins: A self-describing record can be read without the table definition that a columnar file needs.
- **C:** Correct. Raw JSON is readable but forces every query to parse whole records. In this case: A self-describing record can be read without the table definition that a columnar file needs.
- **D:** Incorrect for this question. Columnar Parquet files in S3 are read in column subsets, which suits repeated training scans. Why the correct answer wins: A self-describing record can be read without the table definition that a columnar file needs.

### Question 6 — B

Answer: Partition the S3 prefix by event date. Region and date prefixes let a run read only its own slice. Date partitioning lets a query or a training job skip the prefixes it does not need. Local study-map skill 1.4 (Data Formats and Partitioning), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. EFS gives many hosts one POSIX file system, which suits shared code and small data. Why the correct answer wins: Region and date prefixes let a run read only its own slice.
- **B:** Correct. Date partitioning lets a query or a training job skip the prefixes it does not need. In this case: Region and date prefixes let a run read only its own slice.
- **C:** Incorrect for this question. Intelligent-Tiering moves objects between access tiers as usage changes, with no rules to write. Why the correct answer wins: Region and date prefixes let a run read only its own slice.
- **D:** Incorrect for this question. Raw JSON is readable but forces every query to parse whole records. Why the correct answer wins: Region and date prefixes let a run read only its own slice.

### Question 7 — B, E

Answers: Profile and clean the data with AWS Glue DataBrew; Register the tables in the AWS Glue Data Catalog. A visual recipe performs the profiling and cleaning, and the catalog publishes the result. DataBrew provides a visual recipe for profiling, cleaning and normalising columns. The catalog gives every engine the same table definitions and schemas. Local study-map skill 1.5 (Merge and Transform Tooling), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Data Wrangler builds a reusable preparation flow and can export it into a pipeline. Why the correct answer wins: A visual recipe performs the profiling and cleaning, and the catalog publishes the result.
- **B:** Correct. DataBrew provides a visual recipe for profiling, cleaning and normalising columns. In this case: A visual recipe performs the profiling and cleaning, and the catalog publishes the result.
- **C:** Incorrect for this question. DMS copies and keeps replicating rows from the source database without custom extract code. Why the correct answer wins: A visual recipe performs the profiling and cleaning, and the catalog publishes the result.
- **D:** Incorrect for this question. EMR gives a managed Spark cluster sized for the processing job. Why the correct answer wins: A visual recipe performs the profiling and cleaning, and the catalog publishes the result.
- **E:** Correct. The catalog gives every engine the same table definitions and schemas. In this case: A visual recipe performs the profiling and cleaning, and the catalog publishes the result.

### Question 8 — B

Answer: Process the data with Spark on Amazon EMR. A managed Spark cluster suits a heavy custom transformation over a large history. EMR gives a managed Spark cluster sized for the processing job. Local study-map skill 1.5 (Merge and Transform Tooling), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Glue runs a managed Spark job against catalogued sources and writes the prepared output. Why the correct answer wins: A managed Spark cluster suits a heavy custom transformation over a large history.
- **B:** Correct. EMR gives a managed Spark cluster sized for the processing job. In this case: A managed Spark cluster suits a heavy custom transformation over a large history.
- **C:** Incorrect for this question. DataBrew provides a visual recipe for profiling, cleaning and normalising columns. Why the correct answer wins: A managed Spark cluster suits a heavy custom transformation over a large history.
- **D:** Incorrect for this question. A function per record suits lightweight enrichment and filtering of a stream. Why the correct answer wins: A managed Spark cluster suits a heavy custom transformation over a large history.

### Question 9 — C

Answer: Keep the point-in-time history in the Feature Store offline store. Point-in-time history returns the values that were current when the event happened. The offline store keeps timestamped values so training reads the values that existed at the time. Local study-map skill 1.6 (Feature Store), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. The online store serves the latest feature values for low-latency inference lookups. Why the correct answer wins: Point-in-time history returns the values that were current when the event happened.
- **B:** Incorrect for this question. A feature group gives one definition that both training and inference read. Why the correct answer wins: Point-in-time history returns the values that were current when the event happened.
- **C:** Correct. The offline store keeps timestamped values so training reads the values that existed at the time. In this case: Point-in-time history returns the values that were current when the event happened.
- **D:** Incorrect for this question. The catalog gives every engine the same table definitions and schemas. Why the correct answer wins: Point-in-time history returns the values that were current when the event happened.

### Question 10 — A, E

Answers: Fit the scaler on the training split only; One-hot encode the categorical columns. The scaler is fitted on training data only, and one-hot encoding keeps categories unordered. Fitting on the training split keeps holdout statistics out of the transformation. One-hot encoding turns unordered categories into separate binary columns. Local study-map skill 1.7 (Feature Engineering and Scaling), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Correct. Fitting on the training split keeps holdout statistics out of the transformation. In this case: The scaler is fitted on training data only, and one-hot encoding keeps categories unordered.
- **B:** Incorrect for this question. A log transform compresses the long tail of a heavily skewed amount distribution. Why the correct answer wins: The scaler is fitted on training data only, and one-hot encoding keeps categories unordered.
- **C:** Incorrect for this question. Scaling puts the numeric columns on comparable ranges so no column dominates the fit. Why the correct answer wins: The scaler is fitted on training data only, and one-hot encoding keeps categories unordered.
- **D:** Incorrect for this question. Binning trades resolution for robustness to small variations inside a range. Why the correct answer wins: The scaler is fitted on training data only, and one-hot encoding keeps categories unordered.
- **E:** Correct. One-hot encoding turns unordered categories into separate binary columns. In this case: The scaler is fitted on training data only, and one-hot encoding keeps categories unordered.

### Question 11 — D

Answer: Apply a log transform to the skewed amount column. A log transform compresses the tail so the few large values stop dominating the fit. A log transform compresses the long tail of a heavily skewed amount distribution. Local study-map skill 1.7 (Feature Engineering and Scaling), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. One-hot encoding turns unordered categories into separate binary columns. Why the correct answer wins: A log transform compresses the tail so the few large values stop dominating the fit.
- **B:** Incorrect for this question. Binning trades resolution for robustness to small variations inside a range. Why the correct answer wins: A log transform compresses the tail so the few large values stop dominating the fit.
- **C:** Incorrect for this question. Scaling puts the numeric columns on comparable ranges so no column dominates the fit. Why the correct answer wins: A log transform compresses the tail so the few large values stop dominating the fit.
- **D:** Correct. A log transform compresses the long tail of a heavily skewed amount distribution. In this case: A log transform compresses the tail so the few large values stop dominating the fit.

### Question 12 — A, E

Answers: Store the vectors in Amazon RDS for PostgreSQL with pgvector; Generate the embeddings with an Amazon Bedrock embedding model. Vectors stored beside the relational rows keep the join, and an embedding model produces the vectors. pgvector keeps vectors beside relational rows the application already queries. A managed embedding model converts text into vectors without hosts to run. Local study-map skill 1.8 (Vector Stores and Embeddings), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Correct. A managed embedding model converts text into vectors without hosts to run. In this case: Vectors stored beside the relational rows keep the join, and an embedding model produces the vectors.
- **B:** Incorrect for this question. An S3-backed index suits a large, cost-sensitive corpus read less often. Why the correct answer wins: Vectors stored beside the relational rows keep the join, and an embedding model produces the vectors.
- **C:** Incorrect for this question. Rebuilding the index per request cannot hold a large corpus or a latency target. Why the correct answer wins: Vectors stored beside the relational rows keep the join, and an embedding model produces the vectors.
- **D:** Incorrect for this question. OpenSearch provides a managed vector index with filtered k-nearest-neighbour search. Why the correct answer wins: Vectors stored beside the relational rows keep the join, and an embedding model produces the vectors.
- **E:** Correct. pgvector keeps vectors beside relational rows the application already queries. In this case: Vectors stored beside the relational rows keep the join, and an embedding model produces the vectors.

### Question 13 — A

Answer: Combine keyword and vector retrieval. Combining keyword and vector retrieval catches the exact identifiers. Hybrid retrieval catches exact identifiers that a vector search alone can miss. Local study-map skill 1.8 (Vector Stores and Embeddings), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Correct. Hybrid retrieval catches exact identifiers that a vector search alone can miss. In this case: Combining keyword and vector retrieval catches the exact identifiers.
- **B:** Incorrect for this question. pgvector keeps vectors beside relational rows the application already queries. Why the correct answer wins: Combining keyword and vector retrieval catches the exact identifiers.
- **C:** Incorrect for this question. A reranker reorders the retrieved passages by relevance before they reach the model. Why the correct answer wins: Combining keyword and vector retrieval catches the exact identifiers.
- **D:** Incorrect for this question. OpenSearch provides a managed vector index with filtered k-nearest-neighbour search. Why the correct answer wins: Combining keyword and vector retrieval catches the exact identifiers.

### Question 14 — C

Answer: Tokenise the text with the target model tokeniser. The target model tokeniser is what defines its token counts and truncation. Using the model own tokeniser keeps token counts and truncation consistent with inference. Local study-map skill 1.9 (Text Pre-processing and Chunking), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Removing the identifiers stops the model from learning or echoing personal data. Why the correct answer wins: The target model tokeniser is what defines its token counts and truncation.
- **B:** Incorrect for this question. Overlapping fixed chunks bound the context size and avoid cutting a sentence in half. Why the correct answer wins: The target model tokeniser is what defines its token counts and truncation.
- **C:** Correct. Using the model own tokeniser keeps token counts and truncation consistent with inference. In this case: The target model tokeniser is what defines its token counts and truncation.
- **D:** Incorrect for this question. Semantic chunks keep a coherent passage together, which improves what retrieval returns. Why the correct answer wins: The target model tokeniser is what defines its token counts and truncation.

### Question 15 — B

Answer: Validate each prompt-response pair before it enters the training set. Pair validation catches truncated prompts and mismatched answer pairings. Local study-map skill 1.10 (Data Quality Validation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. A stored profile is what later drift comparison is measured against. Why the correct answer wins: Pair validation catches truncated prompts and mismatched answer pairings.
- **B:** Correct. In this case: Pair validation catches truncated prompts and mismatched answer pairings.
- **C:** Incorrect for this question. Data Quality rules fail the job on nulls, duplicates or range violations before training starts. Why the correct answer wins: Pair validation catches truncated prompts and mismatched answer pairings.
- **D:** Incorrect for this question. A schema check rejects records whose fields changed shape before they corrupt the set. Why the correct answer wins: Pair validation catches truncated prompts and mismatched answer pairings.

### Question 16 — C

Answer: Send the unlabelled records to Amazon SageMaker Ground Truth. Managed labelling handles the workforce, adjudication and quality reporting. Ground Truth manages the labelling workforce, instructions and quality checks. Local study-map skill 1.11 (Labelling and Annotation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Incorrect for this question. Removing the identifiers stops the model from learning or echoing personal data. Why the correct answer wins: Managed labelling handles the workforce, adjudication and quality reporting.
- **B:** Incorrect for this question. Active learning labels most records automatically and sends only uncertain ones to a person. Why the correct answer wins: Managed labelling handles the workforce, adjudication and quality reporting.
- **C:** Correct. Ground Truth manages the labelling workforce, instructions and quality checks. In this case: Managed labelling handles the workforce, adjudication and quality reporting.
- **D:** Incorrect for this question. Augmentation adds plausible variation that the original photographs did not contain. Why the correct answer wins: Managed labelling handles the workforce, adjudication and quality reporting.

### Question 17 — A

Answer: Reweight the under-represented group in the loss. Reweighting the loss changes what the model optimises without discarding records. Local study-map skill 1.12 (Bias Detection and Mitigation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Correct. In this case: Reweighting the loss changes what the model optimises without discarding records.
- **B:** Incorrect for this question. A modality with far fewer examples is under-trained even when the label mix looks even. Why the correct answer wins: Reweighting the loss changes what the model optimises without discarding records.
- **C:** Incorrect for this question. Clarify reports label and feature bias metrics so the imbalance is quantified first. Why the correct answer wins: Reweighting the loss changes what the model optimises without discarding records.
- **D:** Incorrect for this question. Stratifying keeps the label proportions the same in every split. Why the correct answer wins: Reweighting the loss changes what the model optimises without discarding records.

### Question 18 — A, E

Answers: Remove duplicate rows before splitting; Generate synthetic minority samples to rebalance the classes. Deduplication stops the leak, and synthetic minority samples rebalance the classes. Duplicates that straddle splits leak the same row into training and evaluation. Synthetic minority sampling gives the learner more examples of the rare class. Local study-map skill 1.13 (Cleaning and Class Imbalance), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 1 (data preparation for ML and AI, 28 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain1.html.

- **A:** Correct. Synthetic minority sampling gives the learner more examples of the rare class. In this case: Deduplication stops the leak, and synthetic minority samples rebalance the classes.
- **B:** Incorrect for this question. Clipping caps the influence of a few extreme values without deleting the records. Why the correct answer wins: Deduplication stops the leak, and synthetic minority samples rebalance the classes.
- **C:** Incorrect for this question. Median imputation is robust to a skewed distribution and keeps the row. Why the correct answer wins: Deduplication stops the leak, and synthetic minority samples rebalance the classes.
- **D:** Incorrect for this question. One-hot encoding turns unordered categories into separate binary columns. Why the correct answer wins: Deduplication stops the leak, and synthetic minority samples rebalance the classes.
- **E:** Correct. Duplicates that straddle splits leak the same row into training and evaluation. In this case: Deduplication stops the leak, and synthetic minority samples rebalance the classes.

### Question 19 — D

Answer: Use Random Cut Forest for anomaly scoring. Random Cut Forest scores each observation against the learned shape of normal data. Local study-map skill 2.1 (Model and Algorithm Selection), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. Gradient-boosted trees are the usual strong baseline for tabular data. Why the correct answer wins: Random Cut Forest scores each observation against the learned shape of normal data.
- **B:** Incorrect for this question. A linear model is cheap and interpretable when the relationship is close to linear. Why the correct answer wins: Random Cut Forest scores each observation against the learned shape of normal data.
- **C:** Incorrect for this question. DeepAR learns across many related time series and returns probabilistic forecasts. Why the correct answer wins: Random Cut Forest scores each observation against the learned shape of normal data.
- **D:** Correct. In this case: Random Cut Forest scores each observation against the learned shape of normal data.

### Question 20 — A

Answer: Forecast the series with the DeepAR algorithm. DeepAR learns across related series and returns probabilistic forecasts. Local study-map skill 2.1 (Model and Algorithm Selection), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Correct. In this case: DeepAR learns across related series and returns probabilistic forecasts.
- **B:** Incorrect for this question. Gradient-boosted trees are the usual strong baseline for tabular data. Why the correct answer wins: DeepAR learns across related series and returns probabilistic forecasts.
- **C:** Incorrect for this question. A linear model is cheap and interpretable when the relationship is close to linear. Why the correct answer wins: DeepAR learns across related series and returns probabilistic forecasts.
- **D:** Incorrect for this question. Nearest neighbours suit a small, low-dimensional similarity problem. Why the correct answer wins: DeepAR learns across related series and returns probabilistic forecasts.

### Question 21 — A

Answer: Select an Amazon Nova foundation model in Amazon Bedrock. Matching model size to a short-answer task controls latency and cost at volume. Nova models are reached through the Bedrock API with no infrastructure to host. Local study-map skill 2.2 (Foundation Model Selection), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Correct. Nova models are reached through the Bedrock API with no infrastructure to host. In this case: Matching model size to a short-answer task controls latency and cost at volume.
- **B:** Incorrect for this question. Self-hosting gives full control but puts model operations on your team. Why the correct answer wins: Matching model size to a short-answer task controls latency and cost at volume.
- **C:** Incorrect for this question. Claude models are available through Bedrock for long-context reasoning tasks. Why the correct answer wins: Matching model size to a short-answer task controls latency and cost at volume.
- **D:** Incorrect for this question. A Titan embedding model turns text into vectors for search and clustering. Why the correct answer wins: Matching model size to a short-answer task controls latency and cost at volume.

### Question 22 — B

Answer: Download open weights and host them on your own endpoint. Self-hosting gives control of weights and container at the cost of operating them. Self-hosting gives full control but puts model operations on your team. Local study-map skill 2.2 (Foundation Model Selection), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. JumpStart supplies a pre-trained model and its deployment template. Why the correct answer wins: Self-hosting gives control of weights and container at the cost of operating them.
- **B:** Correct. Self-hosting gives full control but puts model operations on your team. In this case: Self-hosting gives control of weights and container at the cost of operating them.
- **C:** Incorrect for this question. Nova models are reached through the Bedrock API with no infrastructure to host. Why the correct answer wins: Self-hosting gives control of weights and container at the cost of operating them.
- **D:** Incorrect for this question. Claude models are available through Bedrock for long-context reasoning tasks. Why the correct answer wins: Self-hosting gives control of weights and container at the cost of operating them.

### Question 23 — B, E

Answers: Fine-tune with parameter-efficient adapters such as LoRA; Start with task-specific prompt engineering before any training. Prompt engineering is the cheap first move, and adapters follow if the prompt is not enough. Adapters train a small number of parameters, which lowers cost and the risk of forgetting. A well-structured prompt often meets the requirement without a training run. Local study-map skill 2.3 (Fine-tuning and Customisation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. Continued pre-training adapts the model to domain vocabulary before task tuning. Why the correct answer wins: Prompt engineering is the cheap first move, and adapters follow if the prompt is not enough.
- **B:** Correct. A well-structured prompt often meets the requirement without a training run. In this case: Prompt engineering is the cheap first move, and adapters follow if the prompt is not enough.
- **C:** Incorrect for this question. Full fine-tuning updates every weight and needs more data, memory and care. Why the correct answer wins: Prompt engineering is the cheap first move, and adapters follow if the prompt is not enough.
- **D:** Incorrect for this question. Distillation transfers the large model behaviour into a cheaper model to serve. Why the correct answer wins: Prompt engineering is the cheap first move, and adapters follow if the prompt is not enough.
- **E:** Correct. Adapters train a small number of parameters, which lowers cost and the risk of forgetting. In this case: Prompt engineering is the cheap first move, and adapters follow if the prompt is not enough.

### Question 24 — D

Answer: Run full-parameter fine-tuning on the curated corpus. Full fine-tuning updates every weight on the larger corpus. Full fine-tuning updates every weight and needs more data, memory and care. Local study-map skill 2.3 (Fine-tuning and Customisation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. Adapters train a small number of parameters, which lowers cost and the risk of forgetting. Why the correct answer wins: Full fine-tuning updates every weight on the larger corpus.
- **B:** Incorrect for this question. Distillation transfers the large model behaviour into a cheaper model to serve. Why the correct answer wins: Full fine-tuning updates every weight on the larger corpus.
- **C:** Incorrect for this question. Continued pre-training adapts the model to domain vocabulary before task tuning. Why the correct answer wins: Full fine-tuning updates every weight on the larger corpus.
- **D:** Correct. Full fine-tuning updates every weight and needs more data, memory and care. In this case: Full fine-tuning updates every weight on the larger corpus.

### Question 25 — D

Answer: Add a reranking step after retrieval. A reranker reorders the retrieved passages by relevance before they reach the model. Local study-map skill 2.4 (RAG Architecture Patterns), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. Metadata lets retrieval filter by source or recency and lets answers cite the document. Why the correct answer wins: A reranker reorders the retrieved passages by relevance before they reach the model.
- **B:** Incorrect for this question. Hybrid retrieval catches exact identifiers that a vector search alone can miss. Why the correct answer wins: A reranker reorders the retrieved passages by relevance before they reach the model.
- **C:** Incorrect for this question. Small child chunks match a query precisely while the parent supplies full context. Why the correct answer wins: A reranker reorders the retrieved passages by relevance before they reach the model.
- **D:** Correct. In this case: A reranker reorders the retrieved passages by relevance before they reach the model.

### Question 26 — B

Answer: Detect entities and sentiment with Amazon Comprehend. Managed entity and sentiment analysis covers the screening need. Comprehend provides managed entity, key-phrase and sentiment analysis. Local study-map skill 2.5 (Managed AI Services), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. Textract reads forms and tables into structured fields without a custom model. Why the correct answer wins: Managed entity and sentiment analysis covers the screening need.
- **B:** Correct. Comprehend provides managed entity, key-phrase and sentiment analysis. In this case: Managed entity and sentiment analysis covers the screening need.
- **C:** Incorrect for this question. Transcribe converts speech to text and can label speakers. Why the correct answer wins: Managed entity and sentiment analysis covers the screening need.
- **D:** Incorrect for this question. Rekognition provides managed image and video analysis for common labels and text. Why the correct answer wins: Managed entity and sentiment analysis covers the screening need.

### Question 27 — C

Answer: Start from a SageMaker JumpStart model. A jump-start model supplies weights and a deployment template. Local study-map skill 2.6 (Built-in Algorithms and Script Mode), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. A custom image is needed only when the managed framework images cannot carry the dependencies. Why the correct answer wins: A jump-start model supplies weights and a deployment template.
- **B:** Incorrect for this question. Gradient-boosted trees are the usual strong baseline for tabular data. Why the correct answer wins: A jump-start model supplies weights and a deployment template.
- **C:** Correct. In this case: A jump-start model supplies weights and a deployment template.
- **D:** Incorrect for this question. Script mode runs your own training script inside a managed framework container. Why the correct answer wins: A jump-start model supplies weights and a deployment template.

### Question 28 — A

Answer: Define the tuning objective on the validation metric that matters. The search optimises exactly the metric it is given. Local study-map skill 2.7 (Hyperparameter Tuning), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Correct. In this case: The search optimises exactly the metric it is given.
- **B:** Incorrect for this question. A manual grid costs a job per combination and adapts to nothing. Why the correct answer wins: The search optimises exactly the metric it is given.
- **C:** Incorrect for this question. Random search is a cheap baseline but ignores what earlier trials learned. Why the correct answer wins: The search optimises exactly the metric it is given.
- **D:** Incorrect for this question. Early stopping ends a trial once the validation metric stops improving. Why the correct answer wins: The search optimises exactly the metric it is given.

### Question 29 — C, D

Answers: Tune hyperparameters with SageMaker automatic model tuning; Use Bayesian search over a defined objective metric. Automatic model tuning runs the search, and Bayesian search uses the earlier results. Automatic model tuning runs the search over a stated objective metric. Bayesian search spends the trial budget on the region of the space that looks promising. Local study-map skill 2.7 (Hyperparameter Tuning), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. Random search is a cheap baseline but ignores what earlier trials learned. Why the correct answer wins: Automatic model tuning runs the search, and Bayesian search uses the earlier results.
- **B:** Incorrect for this question. A manual grid costs a job per combination and adapts to nothing. Why the correct answer wins: Automatic model tuning runs the search, and Bayesian search uses the earlier results.
- **C:** Correct. Bayesian search spends the trial budget on the region of the space that looks promising. In this case: Automatic model tuning runs the search, and Bayesian search uses the earlier results.
- **D:** Correct. Automatic model tuning runs the search over a stated objective metric. In this case: Automatic model tuning runs the search, and Bayesian search uses the earlier results.
- **E:** Incorrect for this question. A warm pool removes the provisioning delay between consecutive training jobs. Why the correct answer wins: Automatic model tuning runs the search, and Bayesian search uses the earlier results.

### Question 30 — C, E

Answers: Add training data and keep a held-out validation split; Add regularisation and reduce model capacity. More representative data and stronger regularisation both reduce variance. More representative data reduces variance without shrinking the model. Regularisation and smaller capacity reduce variance when training error is far below validation. Local study-map skill 2.8 (Training Efficiency and Regularisation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. An ensemble reduces variance from any single model fit. Why the correct answer wins: More representative data and stronger regularisation both reduce variance.
- **B:** Incorrect for this question. Raising capacity addresses underfitting where both training and validation error are high. Why the correct answer wins: More representative data and stronger regularisation both reduce variance.
- **C:** Correct. Regularisation and smaller capacity reduce variance when training error is far below validation. In this case: More representative data and stronger regularisation both reduce variance.
- **D:** Incorrect for this question. Checkpoints let a reclaimed instance continue from the last saved state. Why the correct answer wins: More representative data and stronger regularisation both reduce variance.
- **E:** Correct. More representative data reduces variance without shrinking the model. In this case: More representative data and stronger regularisation both reduce variance.

### Question 31 — A, D

Answers: Pick the threshold from the precision-recall curve; Inspect the confusion matrix on the minority class. The precision-recall curve shows the trade-off, and the confusion matrix shows the counts. The operating threshold should follow the cost of a false positive against a false negative. The confusion matrix shows which class the model keeps confusing. Local study-map skill 2.9 (Classic Model Evaluation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Correct. The confusion matrix shows which class the model keeps confusing. In this case: The precision-recall curve shows the trade-off, and the confusion matrix shows the counts.
- **B:** Incorrect for this question. Accuracy on a rare class is dominated by the majority and hides missed positives. Why the correct answer wins: The precision-recall curve shows the trade-off, and the confusion matrix shows the counts.
- **C:** Incorrect for this question. ROC-AUC measures how well the scores separate the classes across thresholds. Why the correct answer wins: The precision-recall curve shows the trade-off, and the confusion matrix shows the counts.
- **D:** Correct. The operating threshold should follow the cost of a false positive against a false negative. In this case: The precision-recall curve shows the trade-off, and the confusion matrix shows the counts.
- **E:** Incorrect for this question. RMSE expresses the typical error in the target units and penalises large misses. Why the correct answer wins: The precision-recall curve shows the trade-off, and the confusion matrix shows the counts.

### Question 32 — C

Answer: Report RMSE for the regression. RMSE expresses the typical error in the target units. Local study-map skill 2.9 (Classic Model Evaluation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. BLEU measures n-gram overlap with the reference summaries. Why the correct answer wins: RMSE expresses the typical error in the target units.
- **B:** Incorrect for this question. ROC-AUC measures how well the scores separate the classes across thresholds. Why the correct answer wins: RMSE expresses the typical error in the target units.
- **C:** Correct. In this case: RMSE expresses the typical error in the target units.
- **D:** Incorrect for this question. F1 balances precision and recall, which suits an uneven class mix. Why the correct answer wins: RMSE expresses the typical error in the target units.

### Question 33 — C

Answer: Use an LLM-as-a-judge rubric for the open-ended answers. A rubric-driven judge scales qualitative grading of free text. A rubric-driven judge scales qualitative review of free-text answers. Local study-map skill 2.10 (GenAI and NLP Evaluation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. Sampled expert review is how a judge rubric is validated and safety is confirmed. Why the correct answer wins: A rubric-driven judge scales qualitative grading of free text.
- **B:** Incorrect for this question. ROUGE measures recall of reference n-grams, which suits summarisation. Why the correct answer wins: A rubric-driven judge scales qualitative grading of free text.
- **C:** Correct. A rubric-driven judge scales qualitative review of free-text answers. In this case: A rubric-driven judge scales qualitative grading of free text.
- **D:** Incorrect for this question. BLEU measures n-gram overlap with the reference summaries. Why the correct answer wins: A rubric-driven judge scales qualitative grading of free text.

### Question 34 — B

Answer: Run an Amazon Bedrock model evaluation job. A managed evaluation job scores both candidates on the same dataset. Bedrock evaluation scores model output against built-in or custom metrics. Local study-map skill 2.11 (Experiment Tracking and Baselines), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 2 (ML model and foundation model development, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain2.html.

- **A:** Incorrect for this question. Run logging keeps parameters, metrics and artefacts comparable across experiments. Why the correct answer wins: A managed evaluation job scores both candidates on the same dataset.
- **B:** Correct. Bedrock evaluation scores model output against built-in or custom metrics. In this case: A managed evaluation job scores both candidates on the same dataset.
- **C:** Incorrect for this question. Prompt Management versions templates so a prompt change is reviewable and reversible. Why the correct answer wins: A managed evaluation job scores both candidates on the same dataset.
- **D:** Incorrect for this question. The registry holds model versions and their approval status for deployment. Why the correct answer wins: A managed evaluation job scores both candidates on the same dataset.

### Question 35 — A, D

Answers: Deploy a real-time SageMaker AI endpoint; Deploy a serverless inference endpoint. A real-time endpoint holds capacity for the steady load, and serverless handles the idle-prone tool. A real-time endpoint answers synchronous requests with a persistent host behind it. Serverless inference scales to zero and suits intermittent, short requests. Local study-map skill 3.1 (Inference Strategy), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Correct. A real-time endpoint answers synchronous requests with a persistent host behind it. In this case: A real-time endpoint holds capacity for the steady load, and serverless handles the idle-prone tool.
- **B:** Incorrect for this question. Asynchronous inference queues large or long requests and returns results through S3. Why the correct answer wins: A real-time endpoint holds capacity for the steady load, and serverless handles the idle-prone tool.
- **C:** Incorrect for this question. A multi-model endpoint loads models on demand from S3 behind shared hosting capacity. Why the correct answer wins: A real-time endpoint holds capacity for the steady load, and serverless handles the idle-prone tool.
- **D:** Correct. Serverless inference scales to zero and suits intermittent, short requests. In this case: A real-time endpoint holds capacity for the steady load, and serverless handles the idle-prone tool.
- **E:** Incorrect for this question. Batch transform scores a stored dataset with no endpoint to keep running. Why the correct answer wins: A real-time endpoint holds capacity for the steady load, and serverless handles the idle-prone tool.

### Question 36 — A

Answer: Run a batch transform job over the stored records. Batch scoring removes the idle endpoint an always-on deployment would keep. Batch transform scores a stored dataset with no endpoint to keep running. Local study-map skill 3.1 (Inference Strategy), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Correct. Batch transform scores a stored dataset with no endpoint to keep running. In this case: Batch scoring removes the idle endpoint an always-on deployment would keep.
- **B:** Incorrect for this question. Serverless inference scales to zero and suits intermittent, short requests. Why the correct answer wins: Batch scoring removes the idle endpoint an always-on deployment would keep.
- **C:** Incorrect for this question. A real-time endpoint answers synchronous requests with a persistent host behind it. Why the correct answer wins: Batch scoring removes the idle endpoint an always-on deployment would keep.
- **D:** Incorrect for this question. Asynchronous inference queues large or long requests and returns results through S3. Why the correct answer wins: Batch scoring removes the idle endpoint an always-on deployment would keep.

### Question 37 — B

Answer: Run several containers behind one endpoint. A multi-container endpoint chains the two containers behind one call. A multi-container endpoint chains containers such as preprocessing and inference. Local study-map skill 3.2 (Endpoint Architecture), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. A multi-model endpoint loads models on demand from S3 behind shared hosting capacity. Why the correct answer wins: A multi-container endpoint chains the two containers behind one call.
- **B:** Correct. A multi-container endpoint chains containers such as preprocessing and inference. In this case: A multi-container endpoint chains the two containers behind one call.
- **C:** Incorrect for this question. Serverless inference scales to zero and suits intermittent, short requests. Why the correct answer wins: A multi-container endpoint chains the two containers behind one call.
- **D:** Incorrect for this question. A real-time endpoint answers synchronous requests with a persistent host behind it. Why the correct answer wins: A multi-container endpoint chains the two containers behind one call.

### Question 38 — C

Answer: Buy provisioned throughput for the Bedrock model. Reserved capacity keeps the steady volume from being throttled at peak. Provisioned throughput reserves model capacity for predictable, high-volume traffic. Local study-map skill 3.3 (Foundation Model Deployment), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. Inference Recommender benchmarks instance types against the latency and throughput target. Why the correct answer wins: Reserved capacity keeps the steady volume from being throttled at peak.
- **B:** Incorrect for this question. The reservation only pays off when the steady volume exceeds the break-even point. Why the correct answer wins: Reserved capacity keeps the steady volume from being throttled at peak.
- **C:** Correct. Provisioned throughput reserves model capacity for predictable, high-volume traffic. In this case: Reserved capacity keeps the steady volume from being throttled at peak.
- **D:** Incorrect for this question. On-demand calls need no reservation and suit bursty, lower-volume traffic. Why the correct answer wins: Reserved capacity keeps the steady volume from being throttled at peak.

### Question 39 — A

Answer: Import the fine-tuned weights with Bedrock custom model import. Importing the custom model runs those weights on Bedrock infrastructure. Local study-map skill 3.3 (Foundation Model Deployment), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Correct. In this case: Importing the custom model runs those weights on Bedrock infrastructure.
- **B:** Incorrect for this question. JumpStart supplies a pre-trained model and its deployment template. Why the correct answer wins: Importing the custom model runs those weights on Bedrock infrastructure.
- **C:** Incorrect for this question. Provisioned throughput reserves model capacity for predictable, high-volume traffic. Why the correct answer wins: Importing the custom model runs those weights on Bedrock infrastructure.
- **D:** Incorrect for this question. Self-hosting gives full control but puts model operations on your team. Why the correct answer wins: Importing the custom model runs those weights on Bedrock infrastructure.

### Question 40 — D

Answer: Persist the agent session state between turns. Persisted session state carries the context between turns. Persisted session state keeps multi-turn context without resending the whole history. Local study-map skill 3.4 (Agents and Retrieval Runtime), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. Prompt Management versions templates so a prompt change is reviewable and reversible. Why the correct answer wins: Persisted session state carries the context between turns.
- **B:** Incorrect for this question. A sync re-indexes changed documents so retrieval does not serve stale passages. Why the correct answer wins: Persisted session state carries the context between turns.
- **C:** Incorrect for this question. An agent needs its tools, knowledge base and instructions deployed together as one unit. Why the correct answer wins: Persisted session state carries the context between turns.
- **D:** Correct. Persisted session state keeps multi-turn context without resending the whole history. In this case: Persisted session state carries the context between turns.

### Question 41 — B

Answer: Run the job on AWS Batch. A managed batch queue provisions the fleet for the run and releases it. AWS Batch queues the job and provisions capacity for the run. Local study-map skill 3.5 (Containers and Compute Provisioning), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. ECS schedules the container on managed cluster capacity. Why the correct answer wins: A managed batch queue provisions the fleet for the run and releases it.
- **B:** Correct. AWS Batch queues the job and provisions capacity for the run. In this case: A managed batch queue provisions the fleet for the run and releases it.
- **C:** Incorrect for this question. Lambda suits a small model and spiky traffic but not a large model resident in memory. Why the correct answer wins: A managed batch queue provisions the fleet for the run and releases it.
- **D:** Incorrect for this question. EKS runs the container under Kubernetes for teams already standardised on it. Why the correct answer wins: A managed batch queue provisions the fleet for the run and releases it.

### Question 42 — A, D

Answers: Auto scale on a step policy with CloudWatch alarms; Keep provisioned concurrency ready for the burst window. Step scaling adds capacity in bands, and provisioned concurrency avoids the cold start. Step scaling adds capacity in bands as the alarm breaches, which suits sharp bursts. Provisioned concurrency pre-warms capacity so the burst does not meet a cold start. Local study-map skill 3.6 (Autoscaling and Concurrency), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Correct. Step scaling adds capacity in bands as the alarm breaches, which suits sharp bursts. In this case: Step scaling adds capacity in bands, and provisioned concurrency avoids the cold start.
- **B:** Incorrect for this question. A scale-to-zero policy removes the idle cost when nothing calls the endpoint. Why the correct answer wins: Step scaling adds capacity in bands, and provisioned concurrency avoids the cold start.
- **C:** Incorrect for this question. Target tracking holds a metric such as invocations per instance near a chosen value. Why the correct answer wins: Step scaling adds capacity in bands, and provisioned concurrency avoids the cold start.
- **D:** Correct. Provisioned concurrency pre-warms capacity so the burst does not meet a cold start. In this case: Step scaling adds capacity in bands, and provisioned concurrency avoids the cold start.
- **E:** Incorrect for this question. GPU utilisation reflects the real bottleneck when each request is expensive. Why the correct answer wins: Step scaling adds capacity in bands, and provisioned concurrency avoids the cold start.

### Question 43 — C

Answer: Scale the endpoint to zero outside business hours. Scaling to zero outside business hours removes the idle cost. A scale-to-zero policy removes the idle cost when nothing calls the endpoint. Local study-map skill 3.6 (Autoscaling and Concurrency), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. A warm pool removes the provisioning delay between consecutive training jobs. Why the correct answer wins: Scaling to zero outside business hours removes the idle cost.
- **B:** Incorrect for this question. Target tracking holds a metric such as invocations per instance near a chosen value. Why the correct answer wins: Scaling to zero outside business hours removes the idle cost.
- **C:** Correct. A scale-to-zero policy removes the idle cost when nothing calls the endpoint. In this case: Scaling to zero outside business hours removes the idle cost.
- **D:** Incorrect for this question. Step scaling adds capacity in bands as the alarm breaches, which suits sharp bursts. Why the correct answer wins: Scaling to zero outside business hours removes the idle cost.

### Question 44 — C

Answer: Restrict the security group to the application subnet. A security group scoped to the caller subnet admits only that traffic. Local study-map skill 3.7 (VPC Networking for Endpoints), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. An open ingress rule exposes the model to anything that can reach the VPC. Why the correct answer wins: A security group scoped to the caller subnet admits only that traffic.
- **B:** Incorrect for this question. A private endpoint keeps the service traffic inside the VPC without a NAT gateway. Why the correct answer wins: A security group scoped to the caller subnet admits only that traffic.
- **C:** Correct. In this case: A security group scoped to the caller subnet admits only that traffic.
- **D:** Incorrect for this question. Private subnets remove the inbound internet path to the model hosts. Why the correct answer wins: A security group scoped to the caller subnet admits only that traffic.

### Question 45 — D, E

Answers: Orchestrate the release with AWS CodePipeline; Build and test the model image with AWS CodeBuild. A pipeline sequences the stages, and a build service performs the build and tests. CodePipeline sequences the build, test and deploy stages and records each outcome. CodeBuild runs the build and the automated tests in a clean managed environment. Local study-map skill 3.8 (CI/CD Pipelines), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. CodeCommit is the managed Git repository the pipeline reads from. Why the correct answer wins: A pipeline sequences the stages, and a build service performs the build and tests.
- **B:** Incorrect for this question. CodeDeploy performs the traffic shift and can roll back on an alarm. Why the correct answer wins: A pipeline sequences the stages, and a build service performs the build and tests.
- **C:** Incorrect for this question. CodeConnections lets the pipeline read a repository hosted elsewhere. Why the correct answer wins: A pipeline sequences the stages, and a build service performs the build and tests.
- **D:** Correct. CodeBuild runs the build and the automated tests in a clean managed environment. In this case: A pipeline sequences the stages, and a build service performs the build and tests.
- **E:** Correct. CodePipeline sequences the build, test and deploy stages and records each outcome. In this case: A pipeline sequences the stages, and a build service performs the build and tests.

### Question 46 — A

Answer: Connect the external repository with AWS CodeConnections. A connection lets the pipeline read the external repository directly. CodeConnections lets the pipeline read a repository hosted elsewhere. Local study-map skill 3.8 (CI/CD Pipelines), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Correct. CodeConnections lets the pipeline read a repository hosted elsewhere. In this case: A connection lets the pipeline read the external repository directly.
- **B:** Incorrect for this question. CodePipeline sequences the build, test and deploy stages and records each outcome. Why the correct answer wins: A connection lets the pipeline read the external repository directly.
- **C:** Incorrect for this question. CodeCommit is the managed Git repository the pipeline reads from. Why the correct answer wins: A connection lets the pipeline read the external repository directly.
- **D:** Incorrect for this question. CodeBuild runs the build and the automated tests in a clean managed environment. Why the correct answer wins: A connection lets the pipeline read the external repository directly.

### Question 47 — B

Answer: Store the prompt templates in Amazon Bedrock Prompt Management. Prompt management versions templates so each change is reviewable and reversible. Local study-map skill 3.9 (Model Registry and Versioning), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. The registry holds model versions and their approval status for deployment. Why the correct answer wins: Prompt management versions templates so each change is reviewable and reversible.
- **B:** Correct. In this case: Prompt management versions templates so each change is reviewable and reversible.
- **C:** Incorrect for this question. CodeCommit is the managed Git repository the pipeline reads from. Why the correct answer wins: Prompt management versions templates so each change is reviewable and reversible.
- **D:** Incorrect for this question. Run logging keeps parameters, metrics and artefacts comparable across experiments. Why the correct answer wins: Prompt management versions templates so each change is reviewable and reversible.

### Question 48 — D, E

Answers: Send a small share of traffic to the new version first; Shift traffic to the new version in equal steps. A canary caps exposure, and a linear shift moves traffic in measured steps. A canary release limits the blast radius of a bad model to the canary share. A linear shift moves traffic gradually while the metrics are watched. Local study-map skill 3.10 (Deployment Strategy and Rollback), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. Blue/green keeps the previous version ready for an immediate switch back. Why the correct answer wins: A canary caps exposure, and a linear shift moves traffic in measured steps.
- **B:** Incorrect for this question. Mirroring collects comparison data with no user impact. Why the correct answer wins: A canary caps exposure, and a linear shift moves traffic in measured steps.
- **C:** Incorrect for this question. A single switch gives a bad model the whole traffic share at once. Why the correct answer wins: A canary caps exposure, and a linear shift moves traffic in measured steps.
- **D:** Correct. A canary release limits the blast radius of a bad model to the canary share. In this case: A canary caps exposure, and a linear shift moves traffic in measured steps.
- **E:** Correct. A linear shift moves traffic gradually while the metrics are watched. In this case: A canary caps exposure, and a linear shift moves traffic in measured steps.

### Question 49 — C

Answer: Stand the new version beside the old and switch traffic. Blue/green keeps the old version standing for an immediate switch back. Local study-map skill 3.10 (Deployment Strategy and Rollback), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. A single switch gives a bad model the whole traffic share at once. Why the correct answer wins: Blue/green keeps the old version standing for an immediate switch back.
- **B:** Incorrect for this question. A canary release limits the blast radius of a bad model to the canary share. Why the correct answer wins: Blue/green keeps the old version standing for an immediate switch back.
- **C:** Correct. In this case: Blue/green keeps the old version standing for an immediate switch back.
- **D:** Incorrect for this question. Mirroring collects comparison data with no user impact. Why the correct answer wins: Blue/green keeps the old version standing for an immediate switch back.

### Question 50 — C

Answer: Trigger the retraining run with an EventBridge schedule. A schedule starts the workflow on a fixed cadence. A schedule starts the pipeline on a fixed cadence without an external cron host. Local study-map skill 3.11 (Orchestration and Retraining), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 3 (deployment and orchestration of ML and AI workflows, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain3.html.

- **A:** Incorrect for this question. A SageMaker pipeline expresses the processing, training and registration steps as one DAG. Why the correct answer wins: A schedule starts the workflow on a fixed cadence.
- **B:** Incorrect for this question. CodePipeline sequences the build, test and deploy stages and records each outcome. Why the correct answer wins: A schedule starts the workflow on a fixed cadence.
- **C:** Correct. A schedule starts the pipeline on a fixed cadence without an external cron host. In this case: A schedule starts the workflow on a fixed cadence.
- **D:** Incorrect for this question. Step Functions coordinates long-running steps and service calls with retries and branching. Why the correct answer wins: A schedule starts the workflow on a fixed cadence.

### Question 51 — D

Answer: Enable a model quality monitor with ground-truth labels. A quality monitor scores live predictions once the true labels arrive. Local study-map skill 4.1 (Drift and Model Monitoring), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. A bias monitor watches whether the outcome distribution shifts for a protected group. Why the correct answer wins: A quality monitor scores live predictions once the true labels arrive.
- **B:** Incorrect for this question. A data drift monitor compares the live request distribution against the training baseline. Why the correct answer wins: A quality monitor scores live predictions once the true labels arrive.
- **C:** Incorrect for this question. Attribution drift shows that the model now relies on different features than it did. Why the correct answer wins: A quality monitor scores live predictions once the true labels arrive.
- **D:** Correct. In this case: A quality monitor scores live predictions once the true labels arrive.

### Question 52 — C, D

Answers: Enable a data drift monitor on the endpoint; Enable a bias drift monitor. A data drift monitor compares inputs, and a bias monitor watches the group outcome. A data drift monitor compares the live request distribution against the training baseline. A bias monitor watches whether the outcome distribution shifts for a protected group. Local study-map skill 4.1 (Drift and Model Monitoring), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. An alarm on the endpoint metrics pages someone when the service degrades. Why the correct answer wins: A data drift monitor compares inputs, and a bias monitor watches the group outcome.
- **B:** Incorrect for this question. Attribution drift shows that the model now relies on different features than it did. Why the correct answer wins: A data drift monitor compares inputs, and a bias monitor watches the group outcome.
- **C:** Correct. A bias monitor watches whether the outcome distribution shifts for a protected group. In this case: A data drift monitor compares inputs, and a bias monitor watches the group outcome.
- **D:** Correct. A data drift monitor compares the live request distribution against the training baseline. In this case: A data drift monitor compares inputs, and a bias monitor watches the group outcome.
- **E:** Incorrect for this question. A quality monitor scores live predictions once the true labels arrive. Why the correct answer wins: A data drift monitor compares inputs, and a bias monitor watches the group outcome.

### Question 53 — B

Answer: Build a CloudWatch dashboard for the pipeline metrics. A dashboard puts the operating metrics in one continuously refreshed view. Local study-map skill 4.2 (Metrics and Dashboards), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. X-Ray shows where a request spends its time across the services it touches. Why the correct answer wins: A dashboard puts the operating metrics in one continuously refreshed view.
- **B:** Correct. In this case: A dashboard puts the operating metrics in one continuously refreshed view.
- **C:** Incorrect for this question. Logs Insights filters and aggregates the request logs to find the failing pattern. Why the correct answer wins: A dashboard puts the operating metrics in one continuously refreshed view.
- **D:** Incorrect for this question. An alarm on the endpoint metrics pages someone when the service degrades. Why the correct answer wins: A dashboard puts the operating metrics in one continuously refreshed view.

### Question 54 — A

Answer: Query the inference logs with CloudWatch Logs Insights. Log querying aggregates and filters the requests to expose the pattern. Logs Insights filters and aggregates the request logs to find the failing pattern. Local study-map skill 4.2 (Metrics and Dashboards), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Correct. Logs Insights filters and aggregates the request logs to find the failing pattern. In this case: Log querying aggregates and filters the requests to expose the pattern.
- **B:** Incorrect for this question. Config records how each resource was configured and evaluates it against rules. Why the correct answer wins: Log querying aggregates and filters the requests to expose the pattern.
- **C:** Incorrect for this question. A dashboard puts the operating metrics in one view for the team. Why the correct answer wins: Log querying aggregates and filters the requests to expose the pattern.
- **D:** Incorrect for this question. An alarm on the endpoint metrics pages someone when the service degrades. Why the correct answer wins: Log querying aggregates and filters the requests to expose the pattern.

### Question 55 — B

Answer: Trace agent tool calls with Bedrock AgentCore Observability. Agent tracing shows each tool call and where the agent stalled. Agent tracing shows which tool call failed or stalled inside a multi-step task. Local study-map skill 4.3 (GenAI Observability), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. X-Ray shows where a request spends its time across the services it touches. Why the correct answer wins: Agent tracing shows each tool call and where the agent stalled.
- **B:** Correct. Agent tracing shows which tool call failed or stalled inside a multi-step task. In this case: Agent tracing shows each tool call and where the agent stalled.
- **C:** Incorrect for this question. Generative AI observability records prompts, token counts and latency per model call. Why the correct answer wins: Agent tracing shows each tool call and where the agent stalled.
- **D:** Incorrect for this question. An alarm on the endpoint metrics pages someone when the service degrades. Why the correct answer wins: Agent tracing shows each tool call and where the agent stalled.

### Question 56 — D

Answer: Break the spend down by endpoint with AWS Cost Explorer. Cost analysis grouped by service and tag shows which resource drove the change. Cost Explorer groups the bill by service and by tag so the expensive resource is visible. Local study-map skill 4.4 (Cost Optimisation and Purchasing), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. A budget alerts when forecast or actual spend crosses the agreed amount. Why the correct answer wins: Cost analysis grouped by service and tag shows which resource drove the change.
- **B:** Incorrect for this question. Batch scoring removes the idle endpoint that an always-on deployment would keep. Why the correct answer wins: Cost analysis grouped by service and tag shows which resource drove the change.
- **C:** Incorrect for this question. A Savings Plan discounts a predictable hourly spend on eligible compute. Why the correct answer wins: Cost analysis grouped by service and tag shows which resource drove the change.
- **D:** Correct. Cost Explorer groups the bill by service and by tag so the expensive resource is visible. In this case: Cost analysis grouped by service and tag shows which resource drove the change.

### Question 57 — A, D

Answers: Move the offline scoring to batch transform; Right-size the instance family against the measured latency. Batch scoring removes the idle endpoint, and right-sizing matches capacity to the workload. Batch scoring removes the idle endpoint that an always-on deployment would keep. Matching the family to the measured workload avoids paying for capacity the model cannot use. Local study-map skill 4.4 (Cost Optimisation and Purchasing), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Correct. Batch scoring removes the idle endpoint that an always-on deployment would keep. In this case: Batch scoring removes the idle endpoint, and right-sizing matches capacity to the workload.
- **B:** Incorrect for this question. Sizing every request for the hardest case spends latency and money on easy requests. Why the correct answer wins: Batch scoring removes the idle endpoint, and right-sizing matches capacity to the workload.
- **C:** Incorrect for this question. A scale-to-zero policy removes the idle cost when nothing calls the endpoint. Why the correct answer wins: Batch scoring removes the idle endpoint, and right-sizing matches capacity to the workload.
- **D:** Correct. Matching the family to the measured workload avoids paying for capacity the model cannot use. In this case: Batch scoring removes the idle endpoint, and right-sizing matches capacity to the workload.
- **E:** Incorrect for this question. A Savings Plan discounts a predictable hourly spend on eligible compute. Why the correct answer wins: Batch scoring removes the idle endpoint, and right-sizing matches capacity to the workload.

### Question 58 — D

Answer: Cap the output tokens per request. A token cap bounds the spend on each call. Output tokens dominate generation cost, so a cap bounds the spend per call. Local study-map skill 4.5 (Inference Cost and Token Usage), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. Routing easy requests to a cheaper model keeps the large model for hard cases. Why the correct answer wins: A token cap bounds the spend on each call.
- **B:** Incorrect for this question. Sending fewer retrieved tokens lowers both cost and latency on every call. Why the correct answer wins: A token cap bounds the spend on each call.
- **C:** Incorrect for this question. Re-embedding an unchanged document is wasted spend on every refresh. Why the correct answer wins: A token cap bounds the spend on each call.
- **D:** Correct. Output tokens dominate generation cost, so a cap bounds the spend per call. In this case: A token cap bounds the spend on each call.

### Question 59 — A

Answer: Cache embeddings for documents that have not changed. Caching embeddings skips work for documents that did not change. Re-embedding an unchanged document is wasted spend on every refresh. Local study-map skill 4.5 (Inference Cost and Token Usage), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Correct. Re-embedding an unchanged document is wasted spend on every refresh. In this case: Caching embeddings skips work for documents that did not change.
- **B:** Incorrect for this question. The reservation only pays off when the steady volume exceeds the break-even point. Why the correct answer wins: Caching embeddings skips work for documents that did not change.
- **C:** Incorrect for this question. Sending fewer retrieved tokens lowers both cost and latency on every call. Why the correct answer wins: Caching embeddings skips work for documents that did not change.
- **D:** Incorrect for this question. Routing easy requests to a cheaper model keeps the large model for hard cases. Why the correct answer wins: Caching embeddings skips work for documents that did not change.

### Question 60 — B, D

Answers: Apply a service control policy at the organisation level; Attach one policy to an IAM group the engineers belong to. A group policy holds the shared permissions, and a service control policy caps every account. A service control policy caps what any account beneath it can do. A group policy keeps the shared permission set in one reviewable place. Local study-map skill 4.6 (IAM and Credentials), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. A long-lived key keeps working after the project ends unless someone retires it. Why the correct answer wins: A group policy holds the shared permissions, and a service control policy caps every account.
- **B:** Correct. A group policy keeps the shared permission set in one reviewable place. In this case: A group policy holds the shared permissions, and a service control policy caps every account.
- **C:** Incorrect for this question. The root user cannot be limited by policy, so daily use magnifies any mistake. Why the correct answer wins: A group policy holds the shared permissions, and a service control policy caps every account.
- **D:** Correct. A service control policy caps what any account beneath it can do. In this case: A group policy holds the shared permissions, and a service control policy caps every account.
- **E:** Incorrect for this question. A cross-account role issues temporary credentials without sharing a key. Why the correct answer wins: A group policy holds the shared permissions, and a service control policy caps every account.

### Question 61 — D

Answer: Issue a Bedrock API key for the calling application. A scoped API key avoids embedding long-lived IAM credentials. An API key gives short-lived programmatic access without embedding IAM credentials. Local study-map skill 4.6 (IAM and Credentials), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. A group policy keeps the shared permission set in one reviewable place. Why the correct answer wins: A scoped API key avoids embedding long-lived IAM credentials.
- **B:** Incorrect for this question. The root user cannot be limited by policy, so daily use magnifies any mistake. Why the correct answer wins: A scoped API key avoids embedding long-lived IAM credentials.
- **C:** Incorrect for this question. A long-lived key keeps working after the project ends unless someone retires it. Why the correct answer wins: A scoped API key avoids embedding long-lived IAM credentials.
- **D:** Correct. An API key gives short-lived programmatic access without embedding IAM credentials. In this case: A scoped API key avoids embedding long-lived IAM credentials.

### Question 62 — A

Answer: Deny access to the bucket unless the request comes through the VPC endpoint. A condition on the endpoint keeps every other path denied. A condition on the endpoint keeps the data off every path except the private one. Local study-map skill 4.7 (Network Isolation), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Correct. A condition on the endpoint keeps the data off every path except the private one. In this case: A condition on the endpoint keeps every other path denied.
- **B:** Incorrect for this question. A security group scoped to the caller subnet allows only the intended traffic. Why the correct answer wins: A condition on the endpoint keeps every other path denied.
- **C:** Incorrect for this question. A private endpoint keeps the service traffic inside the VPC without a NAT gateway. Why the correct answer wins: A condition on the endpoint keeps every other path denied.
- **D:** Incorrect for this question. Private subnets remove the inbound internet path to the model hosts. Why the correct answer wins: A condition on the endpoint keeps every other path denied.

### Question 63 — B

Answer: Store the model API credential in AWS Secrets Manager. A managed secret store rotates the credential centrally. Secrets Manager holds the credential centrally and can rotate it. Local study-map skill 4.8 (Encryption and Secrets), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. Config records how each resource was configured and evaluates it against rules. Why the correct answer wins: A managed secret store rotates the credential centrally.
- **B:** Correct. Secrets Manager holds the credential centrally and can rotate it. In this case: A managed secret store rotates the credential centrally.
- **C:** Incorrect for this question. Guardrails filters denied topics, sensitive data and unsafe content in the response path. Why the correct answer wins: A managed secret store rotates the credential centrally.
- **D:** Incorrect for this question. A customer managed key lets the team control the key policy and revoke access. Why the correct answer wins: A managed secret store rotates the credential centrally.

### Question 64 — A

Answer: Configure a denied-topics policy for the assistant. A denied-topics policy refuses the ruled-out subject area. Local study-map skill 4.9 (Guardrails and Responsible AI), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Correct. In this case: A denied-topics policy refuses the ruled-out subject area.
- **B:** Incorrect for this question. Safety screening keeps prohibited material out of the model weights. Why the correct answer wins: A denied-topics policy refuses the ruled-out subject area.
- **C:** Incorrect for this question. Guardrails filters denied topics, sensitive data and unsafe content in the response path. Why the correct answer wins: A denied-topics policy refuses the ruled-out subject area.
- **D:** Incorrect for this question. Redaction at the boundary keeps personal data out of the model request entirely. Why the correct answer wins: A denied-topics policy refuses the ruled-out subject area.

### Question 65 — B

Answer: Scan the built image with Amazon Inspector. A vulnerability scan reports the findings before deployment. Inspector reports known vulnerabilities in the image before it is deployed. Local study-map skill 4.10 (Audit and Vulnerability Scanning), mapped to the official guide: AWS Certified Machine Learning Engineer – Associate (MLA-C02) exam guide. Primary reference: MLA-C02 exam guide, content domain 4 (operating, monitoring, and securing ML and AI solutions, 24 percent): https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-02/machine-learning-engineer-associate-02-domain4.html.

- **A:** Incorrect for this question. CloudTrail records who called which API, when and from where. Why the correct answer wins: A vulnerability scan reports the findings before deployment.
- **B:** Correct. Inspector reports known vulnerabilities in the image before it is deployed. In this case: A vulnerability scan reports the findings before deployment.
- **C:** Incorrect for this question. CodeGuru reviews the source for defects and inefficiencies. Why the correct answer wins: A vulnerability scan reports the findings before deployment.
- **D:** Incorrect for this question. Config records how each resource was configured and evaluates it against rules. Why the correct answer wins: A vulnerability scan reports the findings before deployment.
