# Google Cloud Professional Machine Learning Engineer — Full-Length Mock Exam 3

Professional Machine Learning Engineer · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study or drag-and-drop item is reproduced. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Architecting low-code AI solutions (Low-Code AI and Foundational Models)

### 1. A facilities team must estimate next month's energy cost per site. What should be built?

- A. Create a BigQuery ML logistic regression model
- B. Create a BigQuery ML linear regression model
- C. Create a BigQuery ML ARIMA_PLUS time series model
- D. Create a BigQuery ML k-means model

### 2. A deep model in BigQuery must fit a complex tabular pattern, and the training bill must be capped. Which two choices apply? Select two.

- A. Reserve BigQuery slots for the training job
- B. Declare the feature transformations in the TRANSFORM clause
- C. Create a BigQuery ML deep neural network
- D. Store the predictions in a nested JSON column
- E. Create a BigQuery ML AutoML model

### 3. An existing TensorFlow model must score BigQuery rows from SQL. What should be done?

- A. Declare the feature transformations in the TRANSFORM clause
- B. Inspect the metrics with ML.EVALUATE
- C. Score the rows with ML.PREDICT
- D. Import the TensorFlow model into BigQuery ML

### 4. Each scored row must return several labels with their scores in one field. What should be used?

- A. Summarise the model with ML.GLOBAL_EXPLAIN
- B. Store the predictions in a nested JSON column
- C. Declare the feature transformations in the TRANSFORM clause
- D. Score the rows with ML.PREDICT

### 5. An AutoML tabular dataset is large and a reproducible default split is acceptable. What should be used?

- A. Use AutoML so the team needs no modelling code
- B. Let AutoML choose the data split
- C. Set a training budget in node hours
- D. Define a manual split column with train, validation, and test

### 6. A credit team has 300 labelled columns of application data and wants a managed model. What should be used?

- A. Train an Agent Platform AutoML image model
- B. Train an Agent Platform AutoML text model
- C. Train an Agent Platform AutoML forecasting model
- D. Train an Agent Platform AutoML tabular model

### 7. A remote Gemini model in BigQuery cannot call the endpoint. What is missing?

- A. Import the TensorFlow model into BigQuery ML
- B. Create the Cloud resource connection for the remote model
- C. Create a BigQuery ML remote model over Gemini
- D. Fine-tune a Gemini model from BigQuery

### 8. A high-volume classification task must cost as little as possible per call. What should be used?

- A. Choose the larger Gemini model for quality
- B. Embed the documents with the text embedding model
- C. Deploy an open-weight model from Model Garden
- D. Choose the smaller Gemini model for latency and cost

### 9. A warehouse app must detect and count boxes in photos without training. What should be used?

- A. Use the Speech-to-Text API
- B. Use the Vision API
- C. Use Document AI with a specialised processor
- D. Use the Video Intelligence API

### 10. Footage must be scanned for shot boundaries and explicit content. What should be used?

- A. Use the Video Intelligence API
- B. Use the Vision API
- C. Use the Natural Language API
- D. Use Document AI with a specialised processor

### 11. Answers are long, rambling, and often unsupported. Which two changes improve both cost and quality? Select two.

- A. Cache the long shared context
- B. Send the offline work through the batch API
- C. Constrain the output with a schema and a token limit
- D. Ground the answer in retrieved documents
- E. Stream the response tokens to the client

### 12. A batch job hits a per-minute token ceiling that retries cannot fix. What should be done?

- A. Cache the long shared context
- B. Fall back to a smaller model when the primary is throttled
- C. Call the model in the region that serves the users
- D. Request a quota increase for the model

---

## Domain 2 — Collaborating within and across teams to manage data and models (Data, Features, Notebooks, and Experiments)

### 13. Nobody can say which tables hold customer records across nine projects. What should be used?

- A. Catalog and profile the data with Dataplex
- B. Preprocess in memory with pandas
- C. Preprocess with a Dataflow pipeline
- D. Preprocess in BigQuery with SQL

### 14. A time series model scored well offline and failed in production. Which two changes address that? Select two.

- A. Validate the schema and quarantine rejected rows
- B. Bucketize the continuous feature
- C. Split the data by time rather than at random
- D. Hash the identifiers with a salted key before training
- E. Remove the post-outcome column from the features

### 15. Daily aggregates must be produced where the 5 TB table already lives. What should be used?

- A. Preprocess in BigQuery with SQL
- B. Preprocess with a Dataflow pipeline
- C. Preprocess with Spark on Dataproc
- D. Preprocess in memory with pandas

### 16. A single feature started arriving null one day a week. What should be enabled?

- A. Add a crossed feature for the interacting pair
- B. Enable Model Monitoring on the endpoint
- C. Enable feature monitoring on the feature group
- D. Serve the feature from the online store

### 17. A linear model must represent the interaction between two categorical fields. What should be added?

- A. Add a crossed feature for the interacting pair
- B. Register the feature in Agent Platform Feature Store
- C. Normalise the numeric feature before training
- D. Bucketize the continuous feature

### 18. A free-text comment field is stored in the training extract verbatim. What should be done first?

- A. Hash the identifiers with a salted key before training
- B. Drop the identifier columns before the training dataset is written
- C. De-identify the fields with Sensitive Data Protection
- D. Restrict the raw bucket to a privileged service account

### 19. A dataset must keep usable surrogates for phone numbers in a test environment. What should be used?

- A. Hash the identifiers with a salted key before training
- B. Drop the identifier columns before the training dataset is written
- C. Restrict the raw bucket to a privileged service account
- D. De-identify the fields with Sensitive Data Protection

### 20. A notebook must run inside the project VPC on a managed instance. What should be used?

- A. Pin the runtime to a custom container image
- B. Use an Agent Platform Workbench instance
- C. Use Colab Enterprise
- D. Set an idle shutdown schedule

### 21. A data scientist wants a familiar notebook with managed runtimes and IAM. What should be used?

- A. Create the runtime with no public IP
- B. Pin the runtime to a custom container image
- C. Use an Agent Platform Workbench instance
- D. Use Colab Enterprise

### 22. The same feature-engineering step reruns on every experiment. What should be enabled?

- A. Set the random seed in the training code
- B. Track artifacts and lineage in ML Metadata
- C. Enable step caching
- D. Log the run to Agent Platform Experiments

### 23. Two engineers get different baselines from identical code. What should be added?

- A. Compare the runs on the validation metric
- B. Log the run to Agent Platform Experiments
- C. Track artifacts and lineage in ML Metadata
- D. Set the random seed in the training code

### 24. A team needs scheduled runs with per-step lineage and may later move the same pipeline to GKE. Which two choices fit? Select two.

- A. Orchestrate the steps in Agent Platform Pipelines
- B. Use Ray on Agent Platform for the distributed compute
- C. Orchestrate with Managed Service for Apache Airflow
- D. Log the run to Agent Platform Experiments
- E. Express the workflow as a Kubeflow pipeline

### 25. A reinforcement-learning workload needs many distributed Python actors. What should be used?

- A. Orchestrate with Managed Service for Apache Airflow
- B. Express the workflow as a Kubeflow pipeline
- C. Use Ray on Agent Platform for the distributed compute
- D. Orchestrate the steps in Agent Platform Pipelines

### 26. A defect detector faces 0.2 per cent positives, and the judge must be trusted. Which two practices apply? Select two.

- A. Report MAPE when the error must be read as a percentage
- B. Report precision-recall AUC for the rare class
- C. Sample the answers for expert human review
- D. Report ROC AUC
- E. Score the answers with an LLM-as-a-judge rubric

### 27. A ranking model's threshold will be chosen later by the product team. What should be reported?

- A. Report precision-recall AUC for the rare class
- B. Inspect the confusion matrix at the operating threshold
- C. Report ROC AUC
- D. Report RMSE for the regression target

### 28. An auditor asks which dataset and code produced the deployed weights. What should be consulted?

- A. Register the model in Agent Platform Model Registry
- B. Log the run to Agent Platform Experiments
- C. Track artifacts and lineage in ML Metadata
- D. Enable step caching

---

## Domain 3 — Scaling prototypes into ML models (Training at Scale and Model Choice)

### 29. A single call-centre series has strong weekly seasonality and no covariates. What model type fits?

- A. Use TabNet as the custom training algorithm
- B. Choose a classical time series model
- C. Choose a foundation model
- D. Choose a deep neural network

### 30. A contract-review tool must extract obligations from unseen documents. What model type fits?

- A. Use TabNet as the custom training algorithm
- B. Choose a deep neural network
- C. Choose a foundation model
- D. Choose a classical time series model

### 31. A 3 TB event table must produce hourly scores with no new serving stack. What should be used?

- A. Build the model in BigQuery ML
- B. Train a custom model on Agent Platform
- C. Use TabNet as the custom training algorithm
- D. Train with Agent Platform AutoML

### 32. The only engineer who understood the last model has left the team. What should drive the next product choice?

- A. Train with Agent Platform AutoML
- B. Train a custom model on Agent Platform
- C. Choose the product the team can actually operate
- D. Build the model in BigQuery ML

### 33. A new model must be compared with the incumbent on the same population, then held at a small share. Which two strategies apply? Select two.

- A. Replace the model version in place
- B. Run the new model in shadow mode
- C. Roll out a canary with a small traffic share
- D. Split traffic between two models in an A/B test
- E. Deploy blue/green with an instant switch

### 34. The previous version must be restored in seconds with no rebuild. What should be used?

- A. Deploy blue/green with an instant switch
- B. Replace the model version in place
- C. Roll out a canary with a small traffic share
- D. Run the new model in shadow mode

### 35. A model owner wants the top features across a BigQuery ML model in one report. What should be used?

- A. Explain with Shapley values
- B. Use sampled Shapley on the endpoint
- C. Read the contribution of each feature with ML.EXPLAIN_PREDICT
- D. Summarise the model with ML.GLOBAL_EXPLAIN

### 36. A defect-detection image model must explain one rejected part. What should be used?

- A. Use integrated gradients for the image model
- B. Choose an inherently interpretable model
- C. Explain with Shapley values
- D. Use sampled Shapley on the endpoint

### 37. Eight workers must stream 3 TB of records efficiently during training. What format should be used?

- A. Read the training data directly from BigQuery
- B. Write the training data as Parquet in Cloud Storage
- C. Write the training data as TFRecord shards in Cloud Storage
- D. Stream the new records through Dataflow into the training store

### 38. The labelled table changes hourly and must be read at its latest state. What should be used?

- A. Write the training data as Parquet in Cloud Storage
- B. Write the training data as TFRecord shards in Cloud Storage
- C. Read the training data directly from BigQuery
- D. Stream the new records through Dataflow into the training store

### 39. A sensor feed must reach the training store without a nightly batch. What should be used?

- A. Deduplicate on the event key in the ingestion step
- B. Write the training data as Parquet in Cloud Storage
- C. Validate the schema and quarantine rejected rows
- D. Stream the new records through Dataflow into the training store

### 40. The same order event is retried and counted twice in training. What should be added?

- A. Read the training data directly from BigQuery
- B. Stream the new records through Dataflow into the training store
- C. Validate the schema and quarantine rejected rows
- D. Deduplicate on the event key in the ingestion step

### 41. A short PyTorch script must run on the managed trainer with minimal packaging. What should be used?

- A. Export the AutoML model as an artifact
- B. Package the trainer as a Python package
- C. Run a custom container on Agent Platform
- D. Use a prebuilt serving container

### 42. Gradient aggregation dominates the step time across 32 workers. What should be enabled?

- A. Set the reduction server for the all-reduce
- B. Use data parallelism
- C. Configure the job as multi-worker with a chief
- D. Use model parallelism

### 43. Every worker reads the same first shard and the loss is odd. What is the cause?

- A. Verify each worker reads a distinct shard
- B. Lower the learning rate
- C. Reduce the per-replica batch size
- D. Request accelerator quota for the region

### 44. The remote run behaves differently from the local one with identical code. What is the likely cause?

- A. Grant the training service account access to the bucket
- B. Reduce the per-replica batch size
- C. Lower the learning rate
- D. Pin the framework version in the container

### 45. The search must explore many configurations and optimise the revenue metric. Which two choices apply? Select two.

- A. Run a hyperparameter tuning job
- B. Enable early stopping of poor trials
- C. Report the business metric from the trainer
- D. Choose Bayesian optimisation for the search
- E. Set the random seed in the training code

### 46. A search must finish before a fixed date with a known number of trials. What should be set?

- A. Report the business metric from the trainer
- B. Enable early stopping of poor trials
- C. Choose Bayesian optimisation for the search
- D. Cap the search with a trial count and a parallel budget

### 47. The model knows the facts but keeps breaking the required report format. What should be done?

- A. Start with prompt and context engineering
- B. Fine-tune the full model
- C. Fine-tune when the model must follow a house style or output contract
- D. Ground the prompt with retrieval instead of fine-tuning

### 48. A JAX model must run on GPUs with high memory bandwidth. What should be used?

- A. Train on a TPU slice
- B. Train on A100 GPUs
- C. Serve on CPU only
- D. Serve on L4 GPUs

### 49. A model does not fit on one device, and the job must survive preemption. Which two choices apply? Select two.

- A. Checkpoint to Cloud Storage and resume from the last step
- B. Scale the batch size with the worker count
- C. Use model parallelism
- D. Use data parallelism
- E. Serve on CPU only

---

## Domain 4 — Serving and scaling models (Serving, Packaging, and Scaling Endpoints)

### 50. A mobile app calls a model for one user action at a time. What should be used?

- A. Send the events to a streaming prediction path
- B. Run batch prediction
- C. Batch the requests inside the client
- D. Deploy to an online endpoint

### 51. A nightly rescore runs over 40 million rows and needs no warm capacity. Which two choices apply? Select two.

- A. Run batch prediction
- B. Attach a GPU to the serving replica
- C. Set a minimum replica count
- D. Send the events to a streaming prediction path
- E. Batch the requests inside the client

### 52. A fraud signal must be produced as events arrive rather than hourly. What should be used?

- A. Deploy to an online endpoint
- B. Batch the requests inside the client
- C. Send the events to a streaming prediction path
- D. Run batch prediction

### 53. A model needs tokenisation and postprocessing inside the same container. What should be added?

- A. Add a custom prediction routine to the container
- B. Push the serving image to Artifact Registry
- C. Use a prebuilt serving container
- D. Deploy the version and move the alias

### 54. A serving image must be pulled by the endpoint from a registry with IAM. Where should it be pushed?

- A. Use a prebuilt serving container
- B. Push the serving image to Artifact Registry
- C. Register the model in Agent Platform Model Registry
- D. Run a custom container on Agent Platform

### 55. The traffic must follow the label the release team moves, not an internal id. What should be used?

- A. Replace the model version in place
- B. Deploy the version and move the alias
- C. Split traffic between two deployed versions
- D. Register the model in Agent Platform Model Registry

### 56. An investigator asks which training data produced the deployed weights. What should be consulted?

- A. Track artifacts and lineage in ML Metadata
- B. Register the model in Agent Platform Model Registry
- C. Push the serving image to Artifact Registry
- D. Log the run to Agent Platform Experiments

### 57. A new ranker must be scored on live traffic without affecting users, then exposed gradually. Which two strategies apply? Select two.

- A. Run the new model in shadow mode
- B. Replace the model version in place
- C. Roll out a canary with a small traffic share
- D. Deploy blue/green with an instant switch
- E. Split traffic between two models in an A/B test

### 58. Two model variants must be compared on a business metric with equal populations. What strategy is described?

- A. Split traffic between two models in an A/B test
- B. Replace the model version in place
- C. Run the new model in shadow mode
- D. Roll out a canary with a small traffic share

### 59. The same feature is computed twice in two languages and the results differ. What should be done?

- A. Register the feature in Agent Platform Feature Store
- B. Enable step caching
- C. Share one transformation library between training and serving
- D. Deploy the version and move the alias

### 60. A transformation must travel with the artifact so the endpoint cannot skip it. What should be done?

- A. Register the feature in Agent Platform Feature Store
- B. Share one transformation library between training and serving
- C. Keep the preprocessing inside the exported model
- D. Configure explanation metadata for the endpoint

### 61. A model must be callable only from inside the VPC, with no public surface. What should be deployed?

- A. Use a dedicated endpoint
- B. Deploy with a private endpoint only
- C. Attach a GPU to the serving replica
- D. Use a shared public endpoint

### 62. One model needs guaranteed capacity that no other tenant can consume. What should be used?

- A. Deploy with a private endpoint only
- B. Use a shared public endpoint
- C. Split traffic between two deployed versions
- D. Use a dedicated endpoint

### 63. A 3 GB model must be served cheaply with a 60 ms target. What should be used?

- A. Serve on L4 GPUs
- B. Train on A100 GPUs
- C. Serve on CPU only
- D. Train on a TPU slice

### 64. A very large model must be served with high throughput on TPUs. What should be used?

- A. Train on A100 GPUs
- B. Serve on L4 GPUs
- C. Train on a TPU slice
- D. Serve on CPU only

### 65. An endpoint is expensive per request and slow to absorb a spike. Which two settings address both? Select two.

- A. Batch the requests inside the client
- B. Set a minimum replica count
- C. Raise the concurrency per replica
- D. Enable autoscaling on the endpoint
- E. Raise the maximum replica count

### 66. A sudden spike must not scale past the approved budget. What should be set?

- A. Raise the concurrency per replica
- B. Raise the maximum replica count
- C. Attach a GPU to the serving replica
- D. Set a minimum replica count

### 67. A batch of 200 independent requests arrives at once and the client controls the call. What should it do?

- A. Batch the requests inside the client
- B. Run batch prediction
- C. Raise the concurrency per replica
- D. Enable autoscaling on the endpoint

### 68. A model must return per-prediction attributions and cost less per request. Which two changes apply? Select two.

- A. Push the serving image to Artifact Registry
- B. Deploy the version and move the alias
- C. Raise the concurrency per replica
- D. Batch the requests inside the client
- E. Configure explanation metadata for the endpoint

### 69. A real-time scorer must hold 30 ms at p99 and CPU inference cannot reach it. What should be changed?

- A. Raise the concurrency per replica
- B. Raise the maximum replica count
- C. Batch the requests inside the client
- D. Attach a GPU to the serving replica

---

## Domain 5 — Automating and orchestrating ML pipelines (Pipelines, Retraining, and CI/CD/CT)

### 70. A pipeline deploys whatever it trains, even when the score falls. What should be added?

- A. Gate the deployment on a model evaluation threshold
- B. Retrain when the production metric drops
- C. Add an explicit data validation step
- D. Enable step caching

### 71. Nulls and wrong types arrive weekly and only fail at training time. What should be added?

- A. Gate the deployment on a model evaluation threshold
- B. Add an explicit data validation step
- C. Enable step caching
- D. Validate the schema and quarantine rejected rows

### 72. Feature selection has already looked at the final holdout, and malformed batches still reach training. Which two changes restore trust? Select two.

- A. Add an explicit data validation step
- B. Inspect the confusion matrix at the operating threshold
- C. Set the random seed in the training code
- D. Enable step caching
- E. Keep the test set out of every tuning decision

### 73. The workflow must wait on a third-party SFTP drop and an external scoring API. What should orchestrate it?

- A. Express the workflow as a Kubeflow pipeline
- B. Use Ray on Agent Platform for the distributed compute
- C. Orchestrate with Managed Service for Apache Airflow
- D. Orchestrate the steps in Agent Platform Pipelines

### 74. Every step must be retried, cached, and recorded with lineage in one platform. What should be used?

- A. Orchestrate with Managed Service for Apache Airflow
- B. Orchestrate the steps in Agent Platform Pipelines
- C. Use Ray on Agent Platform for the distributed compute
- D. Express the workflow as a Kubeflow pipeline

### 75. The container build and the deployment must be one audited job. What should be used?

- A. Add a Cloud Scheduler trigger to the pipeline
- B. Orchestrate the steps in Agent Platform Pipelines
- C. Trigger the build and deploy from Cloud Build
- D. Enable step caching

### 76. The same container-per-step workflow must also run on an existing GKE cluster. What should be used?

- A. Express the workflow as a Kubeflow pipeline
- B. Orchestrate with Managed Service for Apache Airflow
- C. Use Ray on Agent Platform for the distributed compute
- D. Trigger the build and deploy from Cloud Build

### 77. Preprocessing must be inside the artifact so a caller cannot skip it. What should be used?

- A. Enable step caching
- B. Share one transformation library between training and serving
- C. Register the feature in Agent Platform Feature Store
- D. Keep the preprocessing inside the exported model

### 78. A feature must be computed identically in both paths and served at low latency. Which two components apply? Select two.

- A. Serve the feature from the online store
- B. Read the historical features from the offline store
- C. Share one transformation library between training and serving
- D. Register the model in Agent Platform Model Registry
- E. Deduplicate on the event key in the ingestion step

### 79. An unchanged preprocessing step costs 40 minutes on every trigger. What should be enabled?

- A. Enable step caching
- B. Gate the deployment on a model evaluation threshold
- C. Add an explicit data validation step
- D. Retrain when drift crosses the threshold

### 80. A backfill must rebuild features as they stood on each past order date. What should be read?

- A. Enable feature monitoring on the feature group
- B. Add a crossed feature for the interacting pair
- C. Read the historical features from the offline store
- D. Serve the feature from the online store

### 81. A pricing model degrades whenever competitor behaviour shifts without warning. What policy fits?

- A. Retrain when drift crosses the threshold
- B. Retrain when the production metric drops
- C. Retrain only on a manual request
- D. Retrain on a fixed schedule

### 82. Retraining weekly is auditable and the data changes slowly. What policy fits?

- A. Retrain when drift crosses the threshold
- B. Retrain on a fixed schedule
- C. Retrain when the production metric drops
- D. Retrain only on a manual request

### 83. A monthly dashboard proves quality falls but nothing triggers a retrain. What policy fits?

- A. Retrain only on a manual request
- B. Retrain when drift crosses the threshold
- C. Retrain on a fixed schedule
- D. Retrain when the production metric drops

### 84. Retrain, evaluate, and promote must be one automated path with no manual step. What should be adopted?

- A. Extend CI/CD into continuous training
- B. Retrain on a fixed schedule
- C. Enable step caching
- D. Trigger the pipeline from the arrival of new data

### 85. A batch of new labels lands irregularly and must start a run. What should be used?

- A. Retrain only on a manual request
- B. Add a Cloud Scheduler trigger to the pipeline
- C. Trigger the build and deploy from Cloud Build
- D. Trigger the pipeline from the arrival of new data

### 86. A quarterly model refresh must start on a fixed date for audit reasons. What should be added?

- A. Retrain when the production metric drops
- B. Add a Cloud Scheduler trigger to the pipeline
- C. Trigger the pipeline from the arrival of new data
- D. Trigger the build and deploy from Cloud Build

### 87. A Python training loop must coordinate many distributed actors in one process group. What should be used?

- A. Orchestrate with Managed Service for Apache Airflow
- B. Use Ray on Agent Platform for the distributed compute
- C. Trigger the build and deploy from Cloud Build
- D. Express the workflow as a Kubeflow pipeline

---

## Domain 6 — Monitoring AI solutions (Responsible AI, Monitoring, and Drift)

### 88. A public assistant must resist injected instructions and return parseable JSON. Which two controls apply? Select two.

- A. Configure the model safety filters
- B. Put the boundary in the system instruction
- C. Screen the prompts and responses with Model Armor
- D. Redact the pattern-matchable fields with a regex
- E. Constrain the response to a JSON schema

### 89. Order numbers keep appearing in prompts sent to an external model. What should be applied?

- A. Constrain the response to a JSON schema
- B. Screen the prompts and responses with Model Armor
- C. Redact the pattern-matchable fields with a regex
- D. Put the boundary in the system instruction

### 90. An assistant must decline questions outside its remit. What should be configured?

- A. Screen the prompts and responses with Model Armor
- B. Configure the model safety filters
- C. Put the boundary in the system instruction
- D. Constrain the response to a JSON schema

### 91. A partner dataset arrives with no documentation of how it was collected. What should be produced?

- A. Slice the evaluation metrics by the sensitive attribute
- B. Publish a model card with the intended use and limits
- C. Document the dataset with a data card
- D. Monitor the outcome rate across the protected groups

### 92. A model is being reused outside the population it was trained on. What should be published?

- A. Slice the evaluation metrics by the sensitive attribute
- B. Publish a model card with the intended use and limits
- C. Monitor the outcome rate across the protected groups
- D. Document the dataset with a data card

### 93. A lender must justify every refusal from last quarter to an auditor. What should be used?

- A. Use integrated gradients for the image model
- B. Report the feature attributions to the reviewer
- C. Use sampled Shapley on the endpoint
- D. Explain with Shapley values

### 94. A supervisor must read the model's logic directly, not an approximation. What should be chosen?

- A. Report the feature attributions to the reviewer
- B. Use sampled Shapley on the endpoint
- C. Explain with Shapley values
- D. Choose an inherently interpretable model

### 95. A model that behaved in testing must be watched against that behaviour after release. What should be enabled?

- A. Route the monitoring alert to the owning team
- B. Set the monitoring threshold from the acceptable error budget
- C. Enable Model Monitoring on the endpoint
- D. Track p95 latency per model version

### 96. Alerts fire several times a day and have been muted. What should be revisited?

- A. Score a sample of live answers with the evaluation rubric
- B. Set the monitoring threshold from the acceptable error budget
- C. Log the prompt and response with redaction
- D. Route the monitoring alert to the owning team

### 97. Quality fell while the inputs stayed stable, and labels arrive late. Which two practices apply? Select two.

- A. Watch for concept drift
- B. Watch the prediction distribution
- C. Join the delayed ground truth back to the predictions
- D. Watch for feature attribution drift
- E. Watch for data drift

### 98. A model is strong offline and weak on day one of deployment. What should be investigated?

- A. Watch for training-serving skew
- B. Watch for data drift
- C. Watch for concept drift
- D. Watch the prediction distribution

### 99. A summarisation service's cost jumped after a prompt change. What should be tracked?

- A. Score a sample of live answers with the evaluation rubric
- B. Track tokens and cost per request
- C. Enable Model Monitoring on the endpoint
- D. Track p95 latency per model version

### 100. An assistant must be checked for answer quality after each model swap. What should be added?

- A. Score a sample of live answers with the evaluation rubric
- B. Enable Model Monitoring on the endpoint
- C. Track p95 latency per model version
- D. Track tokens and cost per request

---

## Answer key and explanations

### Question 1 — B

Answer: Create a BigQuery ML linear regression model. Linear regression predicts a continuous value such as revenue or demand. Local study-map skill 1.1 (BigQuery ML Model Building), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Logistic regression predicts a binary outcome and trains inside BigQuery with SQL. Why the correct answer wins: Linear regression predicts a continuous value such as revenue or demand.
- **B:** Correct. In this case: Linear regression predicts a continuous value such as revenue or demand.
- **C:** Incorrect for this question. ARIMA_PLUS models seasonality and trend and returns a forecast interval per period. Why the correct answer wins: Linear regression predicts a continuous value such as revenue or demand.
- **D:** Incorrect for this question. K-means segments rows into unsupervised clusters without a labelled target. Why the correct answer wins: Linear regression predicts a continuous value such as revenue or demand.

### Question 2 — A, C

Answers: Create a BigQuery ML deep neural network; Reserve BigQuery slots for the training job. The DNN model type fits non-linear patterns, and a reservation bounds the cost and the wait time. The DNN model type fits non-linear patterns too complex for a linear model. Training consumes slots, so a reservation bounds the cost and the wait time. Local study-map skill 1.1 (BigQuery ML Model Building), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. Training consumes slots, so a reservation bounds the cost and the wait time. In this case: The DNN model type fits non-linear patterns, and a reservation bounds the cost and the wait time.
- **B:** Incorrect for this question. TRANSFORM keeps preprocessing inside the model, so prediction applies the same steps. Why the correct answer wins: The DNN model type fits non-linear patterns, and a reservation bounds the cost and the wait time.
- **C:** Correct. The DNN model type fits non-linear patterns too complex for a linear model. In this case: The DNN model type fits non-linear patterns, and a reservation bounds the cost and the wait time.
- **D:** Incorrect for this question. A nested column keeps per-row structured output such as labels and scores together. Why the correct answer wins: The DNN model type fits non-linear patterns, and a reservation bounds the cost and the wait time.
- **E:** Incorrect for this question. The AutoML model type in BigQuery ML searches architectures without leaving SQL. Why the correct answer wins: The DNN model type fits non-linear patterns, and a reservation bounds the cost and the wait time.

### Question 3 — D

Answer: Import the TensorFlow model into BigQuery ML. Importing brings an already-trained model into BigQuery so SQL can score it. Local study-map skill 1.2 (BigQuery ML Feature Engineering and Prediction), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. TRANSFORM keeps preprocessing inside the model, so prediction applies the same steps. Why the correct answer wins: Importing brings an already-trained model into BigQuery so SQL can score it.
- **B:** Incorrect for this question. ML.EVALUATE returns the model metrics against a labelled dataset. Why the correct answer wins: Importing brings an already-trained model into BigQuery so SQL can score it.
- **C:** Incorrect for this question. ML.PREDICT applies a trained model and returns the label and its probability. Why the correct answer wins: Importing brings an already-trained model into BigQuery so SQL can score it.
- **D:** Correct. In this case: Importing brings an already-trained model into BigQuery so SQL can score it.

### Question 4 — B

Answer: Store the predictions in a nested JSON column. A nested column keeps per-row structured output together. Local study-map skill 1.2 (BigQuery ML Feature Engineering and Prediction), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. ML.GLOBAL_EXPLAIN ranks the features that matter most across the whole model. Why the correct answer wins: A nested column keeps per-row structured output together.
- **B:** Correct. In this case: A nested column keeps per-row structured output together.
- **C:** Incorrect for this question. TRANSFORM keeps preprocessing inside the model, so prediction applies the same steps. Why the correct answer wins: A nested column keeps per-row structured output together.
- **D:** Incorrect for this question. ML.PREDICT applies a trained model and returns the label and its probability. Why the correct answer wins: A nested column keeps per-row structured output together.

### Question 5 — B

Answer: Let AutoML choose the data split. AutoML uses a reproducible default split when the dataset is large enough to do so. Local study-map skill 1.3 (Agent Platform AutoML), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. AutoML is the no-code path, which matters when the team has data skills but no ML engineers. Why the correct answer wins: AutoML uses a reproducible default split when the dataset is large enough to do so.
- **B:** Correct. In this case: AutoML uses a reproducible default split when the dataset is large enough to do so.
- **C:** Incorrect for this question. A node-hour budget caps how long AutoML searches, which bounds the cost. Why the correct answer wins: AutoML uses a reproducible default split when the dataset is large enough to do so.
- **D:** Incorrect for this question. A manual split is required when the split must follow time or a grouping column. Why the correct answer wins: AutoML uses a reproducible default split when the dataset is large enough to do so.

### Question 6 — D

Answer: Train an Agent Platform AutoML tabular model. AutoML tabular selects the architecture and tuning for a structured dataset. Local study-map skill 1.3 (Agent Platform AutoML), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. AutoML image trains classification or object detection from labelled images. Why the correct answer wins: AutoML tabular selects the architecture and tuning for a structured dataset.
- **B:** Incorrect for this question. AutoML text trains classification, extraction, or sentiment from labelled text. Why the correct answer wins: AutoML tabular selects the architecture and tuning for a structured dataset.
- **C:** Incorrect for this question. AutoML forecasting builds a time series model with covariates and backtesting. Why the correct answer wins: AutoML tabular selects the architecture and tuning for a structured dataset.
- **D:** Correct. In this case: AutoML tabular selects the architecture and tuning for a structured dataset.

### Question 7 — B

Answer: Create the Cloud resource connection for the remote model. A remote model needs a connection and its service account before it can call an endpoint. Local study-map skill 1.4 (Gemini Fine-Tuning with BigQuery), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Importing brings an already-trained model into BigQuery so SQL can score it. Why the correct answer wins: A remote model needs a connection and its service account before it can call an endpoint.
- **B:** Correct. In this case: A remote model needs a connection and its service account before it can call an endpoint.
- **C:** Incorrect for this question. A remote model calls the Gemini endpoint from SQL, so generation runs where the data lives. Why the correct answer wins: A remote model needs a connection and its service account before it can call an endpoint.
- **D:** Incorrect for this question. Fine-tuning adapts a foundation model to the domain using rows that stay in BigQuery. Why the correct answer wins: A remote model needs a connection and its service account before it can call an endpoint.

### Question 8 — D

Answer: Choose the smaller Gemini model for latency and cost. The smaller model answers faster and cheaper, which suits high-volume simple tasks. Local study-map skill 1.5 (Model Garden Model Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The larger model gives the best reasoning quality at a higher cost per token. Why the correct answer wins: The smaller model answers faster and cheaper, which suits high-volume simple tasks.
- **B:** Incorrect for this question. Embeddings turn text into vectors, which is what a retrieval step searches. Why the correct answer wins: The smaller model answers faster and cheaper, which suits high-volume simple tasks.
- **C:** Incorrect for this question. An open-weight model can be tuned and self-hosted when a proprietary endpoint does not fit. Why the correct answer wins: The smaller model answers faster and cheaper, which suits high-volume simple tasks.
- **D:** Correct. In this case: The smaller model answers faster and cheaper, which suits high-volume simple tasks.

### Question 9 — B

Answer: Use the Vision API. The prebuilt Vision model labels, detects, and reads text without training a model. Local study-map skill 1.6 (Industry AI APIs), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The speech model transcribes audio, including domain phrases through adaptation. Why the correct answer wins: The prebuilt Vision model labels, detects, and reads text without training a model.
- **B:** Correct. In this case: The prebuilt Vision model labels, detects, and reads text without training a model.
- **C:** Incorrect for this question. A Document AI processor extracts structured fields from forms with layout awareness. Why the correct answer wins: The prebuilt Vision model labels, detects, and reads text without training a model.
- **D:** Incorrect for this question. Video Intelligence detects shots, labels, and explicit content in video. Why the correct answer wins: The prebuilt Vision model labels, detects, and reads text without training a model.

### Question 10 — A

Answer: Use the Video Intelligence API. Video Intelligence detects shots, labels, and explicit content in video. Local study-map skill 1.6 (Industry AI APIs), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Video Intelligence detects shots, labels, and explicit content in video.
- **B:** Incorrect for this question. The prebuilt Vision model labels, detects, and reads text without training a model. Why the correct answer wins: Video Intelligence detects shots, labels, and explicit content in video.
- **C:** Incorrect for this question. The Natural Language API returns entities, sentiment, and syntax without a custom model. Why the correct answer wins: Video Intelligence detects shots, labels, and explicit content in video.
- **D:** Incorrect for this question. A Document AI processor extracts structured fields from forms with layout awareness. Why the correct answer wins: Video Intelligence detects shots, labels, and explicit content in video.

### Question 11 — C, D

Answers: Constrain the output with a schema and a token limit; Ground the answer in retrieved documents. A bounded output cuts latency and cost, and grounding reduces unsupported answers. A bounded output cuts both latency and cost per request. Grounding reduces unsupported answers and keeps the prompt short. Local study-map skill 1.7 (Gemini Application Optimization), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Context caching bills the repeated prefix once instead of on every request. Why the correct answer wins: A bounded output cuts latency and cost, and grounding reduces unsupported answers.
- **B:** Incorrect for this question. The batch path trades latency for a lower price on non-interactive requests. Why the correct answer wins: A bounded output cuts latency and cost, and grounding reduces unsupported answers.
- **C:** Correct. A bounded output cuts both latency and cost per request. In this case: A bounded output cuts latency and cost, and grounding reduces unsupported answers.
- **D:** Correct. Grounding reduces unsupported answers and keeps the prompt short. In this case: A bounded output cuts latency and cost, and grounding reduces unsupported answers.
- **E:** Incorrect for this question. Streaming improves perceived latency without reducing total generation time. Why the correct answer wins: A bounded output cuts latency and cost, and grounding reduces unsupported answers.

### Question 12 — D

Answer: Request a quota increase for the model. Throughput is capped by quota, so a quota ceiling cannot be solved by retries. Local study-map skill 1.7 (Gemini Application Optimization), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Context caching bills the repeated prefix once instead of on every request. Why the correct answer wins: Throughput is capped by quota, so a quota ceiling cannot be solved by retries.
- **B:** Incorrect for this question. A fallback keeps the application answering when the primary model returns resource-exhausted. Why the correct answer wins: Throughput is capped by quota, so a quota ceiling cannot be solved by retries.
- **C:** Incorrect for this question. A regional endpoint removes cross-region latency and satisfies residency rules. Why the correct answer wins: Throughput is capped by quota, so a quota ceiling cannot be solved by retries.
- **D:** Correct. In this case: Throughput is capped by quota, so a quota ceiling cannot be solved by retries.

### Question 13 — A

Answer: Catalog and profile the data with Dataplex. Dataplex discovers, profiles, and applies policy across the lakehouse in one control plane. Local study-map skill 2.1 (Preprocessing Tool Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Dataplex discovers, profiles, and applies policy across the lakehouse in one control plane.
- **B:** Incorrect for this question. In-memory processing is the simplest option and stops working once the data exceeds the worker memory. Why the correct answer wins: Dataplex discovers, profiles, and applies policy across the lakehouse in one control plane.
- **C:** Incorrect for this question. Dataflow runs the same Beam code in batch and streaming and scales without provisioning. Why the correct answer wins: Dataplex discovers, profiles, and applies policy across the lakehouse in one control plane.
- **D:** Incorrect for this question. SQL over BigQuery is the cheapest option when the data already sits there and the logic is set-based. Why the correct answer wins: Dataplex discovers, profiles, and applies policy across the lakehouse in one control plane.

### Question 14 — A, C

Answers: Split the data by time rather than at random; Validate the schema and quarantine rejected rows. A time-based split prevents learning from the future, and schema validation stops malformed batches. A time-based split prevents the model from learning from the future. Rejecting rows into a side table makes a schema break visible instead of silent. Local study-map skill 2.1 (Preprocessing Tool Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. Rejecting rows into a side table makes a schema break visible instead of silent. In this case: A time-based split prevents learning from the future, and schema validation stops malformed batches.
- **B:** Incorrect for this question. Bucketing converts a non-linear relationship into a form a linear model can fit. Why the correct answer wins: A time-based split prevents learning from the future, and schema validation stops malformed batches.
- **C:** Correct. A time-based split prevents the model from learning from the future. In this case: A time-based split prevents learning from the future, and schema validation stops malformed batches.
- **D:** Incorrect for this question. A salted hash keeps the join key usable while removing the direct identifier. Why the correct answer wins: A time-based split prevents learning from the future, and schema validation stops malformed batches.
- **E:** Incorrect for this question. A column written after the outcome encodes the answer and inflates the score. Why the correct answer wins: A time-based split prevents learning from the future, and schema validation stops malformed batches.

### Question 15 — A

Answer: Preprocess in BigQuery with SQL. SQL over BigQuery is the cheapest option when the data already sits there. Local study-map skill 2.1 (Preprocessing Tool Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: SQL over BigQuery is the cheapest option when the data already sits there.
- **B:** Incorrect for this question. Dataflow runs the same Beam code in batch and streaming and scales without provisioning. Why the correct answer wins: SQL over BigQuery is the cheapest option when the data already sits there.
- **C:** Incorrect for this question. Spark suits large transformations the team already has as Scala or PySpark code. Why the correct answer wins: SQL over BigQuery is the cheapest option when the data already sits there.
- **D:** Incorrect for this question. In-memory processing is the simplest option and stops working once the data exceeds the worker memory. Why the correct answer wins: SQL over BigQuery is the cheapest option when the data already sits there.

### Question 16 — C

Answer: Enable feature monitoring on the feature group. Feature monitoring reports distribution changes per feature, not just per model. Local study-map skill 2.2 (Feature Store), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A crossed feature lets a linear model express the interaction it cannot learn alone. Why the correct answer wins: Feature monitoring reports distribution changes per feature, not just per model.
- **B:** Incorrect for this question. Model Monitoring compares live traffic with the training baseline and reports skew and drift. Why the correct answer wins: Feature monitoring reports distribution changes per feature, not just per model.
- **C:** Correct. In this case: Feature monitoring reports distribution changes per feature, not just per model.
- **D:** Incorrect for this question. The online store returns the latest feature value at low latency for a single entity. Why the correct answer wins: Feature monitoring reports distribution changes per feature, not just per model.

### Question 17 — A

Answer: Add a crossed feature for the interacting pair. A crossed feature lets a linear model express the interaction it cannot learn alone. Local study-map skill 2.2 (Feature Store), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: A crossed feature lets a linear model express the interaction it cannot learn alone.
- **B:** Incorrect for this question. Feature Store keeps one definition that both training and serving read. Why the correct answer wins: A crossed feature lets a linear model express the interaction it cannot learn alone.
- **C:** Incorrect for this question. Scaling keeps one large-magnitude feature from dominating the gradient. Why the correct answer wins: A crossed feature lets a linear model express the interaction it cannot learn alone.
- **D:** Incorrect for this question. Bucketing converts a non-linear relationship into a form a linear model can fit. Why the correct answer wins: A crossed feature lets a linear model express the interaction it cannot learn alone.

### Question 18 — B

Answer: Drop the identifier columns before the training dataset is written. Dropping the field removes the exposure entirely when the model does not need it. Local study-map skill 2.3 (PII Handling and Data Privacy), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A salted hash keeps the join key usable while removing the direct identifier. Why the correct answer wins: Dropping the field removes the exposure entirely when the model does not need it.
- **B:** Correct. In this case: Dropping the field removes the exposure entirely when the model does not need it.
- **C:** Incorrect for this question. Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts PII. Why the correct answer wins: Dropping the field removes the exposure entirely when the model does not need it.
- **D:** Incorrect for this question. Restricting the bucket limits who can copy the raw data in the first place. Why the correct answer wins: Dropping the field removes the exposure entirely when the model does not need it.

### Question 19 — D

Answer: De-identify the fields with Sensitive Data Protection. Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts PII. Local study-map skill 2.3 (PII Handling and Data Privacy), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A salted hash keeps the join key usable while removing the direct identifier. Why the correct answer wins: Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts PII.
- **B:** Incorrect for this question. Dropping the field removes the exposure entirely when the model does not need it. Why the correct answer wins: Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts PII.
- **C:** Incorrect for this question. Restricting the bucket limits who can copy the raw data in the first place. Why the correct answer wins: Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts PII.
- **D:** Correct. In this case: Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts PII.

### Question 20 — B

Answer: Use an Agent Platform Workbench instance. Workbench is the managed notebook instance inside the project VPC. Local study-map skill 2.4 (Notebook Environments and Security), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A pinned image makes the environment reproducible across users. Why the correct answer wins: Workbench is the managed notebook instance inside the project VPC.
- **B:** Correct. In this case: Workbench is the managed notebook instance inside the project VPC.
- **C:** Incorrect for this question. Colab Enterprise adds managed runtimes, VPC connectivity, and IAM to the Colab experience. Why the correct answer wins: Workbench is the managed notebook instance inside the project VPC.
- **D:** Incorrect for this question. Idle shutdown stops paying for a notebook nobody is using. Why the correct answer wins: Workbench is the managed notebook instance inside the project VPC.

### Question 21 — D

Answer: Use Colab Enterprise. Colab Enterprise adds managed runtimes, VPC connectivity, and IAM to the Colab experience. Local study-map skill 2.4 (Notebook Environments and Security), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A private-IP runtime reaches the data through the VPC and cannot be opened from the internet. Why the correct answer wins: Colab Enterprise adds managed runtimes, VPC connectivity, and IAM to the Colab experience.
- **B:** Incorrect for this question. A pinned image makes the environment reproducible across users. Why the correct answer wins: Colab Enterprise adds managed runtimes, VPC connectivity, and IAM to the Colab experience.
- **C:** Incorrect for this question. Workbench is the managed notebook instance inside the project VPC. Why the correct answer wins: Colab Enterprise adds managed runtimes, VPC connectivity, and IAM to the Colab experience.
- **D:** Correct. In this case: Colab Enterprise adds managed runtimes, VPC connectivity, and IAM to the Colab experience.

### Question 22 — C

Answer: Enable step caching. Caching skips an unchanged step on a rerun and shortens the pipeline. Local study-map skill 2.5 (Experiment Tracking), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A fixed seed makes a rerun reproducible when the rest of the environment is pinned. Why the correct answer wins: Caching skips an unchanged step on a rerun and shortens the pipeline.
- **B:** Incorrect for this question. ML Metadata records which data and code produced which artifact. Why the correct answer wins: Caching skips an unchanged step on a rerun and shortens the pipeline.
- **C:** Correct. In this case: Caching skips an unchanged step on a rerun and shortens the pipeline.
- **D:** Incorrect for this question. Experiments records parameters, metrics, and artifacts per run so runs can be compared. Why the correct answer wins: Caching skips an unchanged step on a rerun and shortens the pipeline.

### Question 23 — D

Answer: Set the random seed in the training code. A fixed seed makes a rerun reproducible when the environment is pinned. Local study-map skill 2.5 (Experiment Tracking), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Comparing on the validation metric keeps model selection independent of the test set. Why the correct answer wins: A fixed seed makes a rerun reproducible when the environment is pinned.
- **B:** Incorrect for this question. Experiments records parameters, metrics, and artifacts per run so runs can be compared. Why the correct answer wins: A fixed seed makes a rerun reproducible when the environment is pinned.
- **C:** Incorrect for this question. ML Metadata records which data and code produced which artifact. Why the correct answer wins: A fixed seed makes a rerun reproducible when the environment is pinned.
- **D:** Correct. In this case: A fixed seed makes a rerun reproducible when the environment is pinned.

### Question 24 — A, E

Answers: Orchestrate the steps in Agent Platform Pipelines; Express the workflow as a Kubeflow pipeline. Pipelines runs each step as a container with lineage, and a Kubeflow pipeline can run on GKE. Kubeflow pipelines give a container-per-step pipeline that runs on the managed service or on GKE. Local study-map skill 2.6 (Development Environment Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Pipelines runs each step as a container with lineage, and a Kubeflow pipeline can run on GKE.
- **B:** Incorrect for this question. Ray fits a Python-native distributed workload that is not a container-per-step pipeline. Why the correct answer wins: Pipelines runs each step as a container with lineage, and a Kubeflow pipeline can run on GKE.
- **C:** Incorrect for this question. Airflow expresses cross-system dependencies and schedules outside the ML platform. Why the correct answer wins: Pipelines runs each step as a container with lineage, and a Kubeflow pipeline can run on GKE.
- **D:** Incorrect for this question. Experiments records parameters, metrics, and artifacts per run so runs can be compared. Why the correct answer wins: Pipelines runs each step as a container with lineage, and a Kubeflow pipeline can run on GKE.
- **E:** Correct. Kubeflow pipelines give a container-per-step pipeline that runs on the managed service or on GKE. In this case: Pipelines runs each step as a container with lineage, and a Kubeflow pipeline can run on GKE.

### Question 25 — C

Answer: Use Ray on Agent Platform for the distributed compute. Ray fits a Python-native distributed workload that is not a container-per-step pipeline. Local study-map skill 2.6 (Development Environment Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Airflow expresses cross-system dependencies and schedules outside the ML platform. Why the correct answer wins: Ray fits a Python-native distributed workload that is not a container-per-step pipeline.
- **B:** Incorrect for this question. Kubeflow pipelines give a container-per-step pipeline that runs on the managed service or on GKE. Why the correct answer wins: Ray fits a Python-native distributed workload that is not a container-per-step pipeline.
- **C:** Correct. In this case: Ray fits a Python-native distributed workload that is not a container-per-step pipeline.
- **D:** Incorrect for this question. Pipelines runs each step as a container with caching, lineage, and retry. Why the correct answer wins: Ray fits a Python-native distributed workload that is not a container-per-step pipeline.

### Question 26 — B, C

Answers: Report precision-recall AUC for the rare class; Sample the answers for expert human review. Precision-recall AUC stays informative when positives are rare, and human review calibrates the judge. Precision-recall AUC stays informative when the positive class is rare. Human review remains the reference standard for a sample the judge is calibrated against. Local study-map skill 2.7 (Evaluation Metrics and LLM-as-a-Judge), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. MAPE expresses the error relative to the actual value, which business readers understand. Why the correct answer wins: Precision-recall AUC stays informative when positives are rare, and human review calibrates the judge.
- **B:** Correct. Precision-recall AUC stays informative when the positive class is rare. In this case: Precision-recall AUC stays informative when positives are rare, and human review calibrates the judge.
- **C:** Correct. Human review remains the reference standard for a sample the judge is calibrated against. In this case: Precision-recall AUC stays informative when positives are rare, and human review calibrates the judge.
- **D:** Incorrect for this question. ROC AUC measures ranking quality across thresholds and hides class imbalance. Why the correct answer wins: Precision-recall AUC stays informative when positives are rare, and human review calibrates the judge.
- **E:** Incorrect for this question. A rubric-driven judge scales the evaluation of free-text answers beyond human review. Why the correct answer wins: Precision-recall AUC stays informative when positives are rare, and human review calibrates the judge.

### Question 27 — C

Answer: Report ROC AUC. ROC AUC measures ranking quality across thresholds. Local study-map skill 2.7 (Evaluation Metrics and LLM-as-a-Judge), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Precision-recall AUC stays informative when the positive class is rare. Why the correct answer wins: ROC AUC measures ranking quality across thresholds.
- **B:** Incorrect for this question. The matrix shows the false-positive and false-negative split the business will feel. Why the correct answer wins: ROC AUC measures ranking quality across thresholds.
- **C:** Correct. In this case: ROC AUC measures ranking quality across thresholds.
- **D:** Incorrect for this question. RMSE expresses the typical error in the units of the target. Why the correct answer wins: ROC AUC measures ranking quality across thresholds.

### Question 28 — C

Answer: Track artifacts and lineage in ML Metadata. ML Metadata records which data and code produced which artifact. Local study-map skill 2.8 (Metadata and Lineage), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The registry versions the model artifact and links it to its lineage and metrics. Why the correct answer wins: ML Metadata records which data and code produced which artifact.
- **B:** Incorrect for this question. Experiments records parameters, metrics, and artifacts per run so runs can be compared. Why the correct answer wins: ML Metadata records which data and code produced which artifact.
- **C:** Correct. In this case: ML Metadata records which data and code produced which artifact.
- **D:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: ML Metadata records which data and code produced which artifact.

### Question 29 — B

Answer: Choose a classical time series model. A classical time series model suits a single series with strong seasonality. Local study-map skill 3.1 (Model Type Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. TabNet gives an interpretable attentive tabular model inside custom training. Why the correct answer wins: A classical time series model suits a single series with strong seasonality.
- **B:** Correct. In this case: A classical time series model suits a single series with strong seasonality.
- **C:** Incorrect for this question. A foundation model suits an open-ended language or multimodal task where labelled data is scarce. Why the correct answer wins: A classical time series model suits a single series with strong seasonality.
- **D:** Incorrect for this question. A DNN suits a large tabular or unstructured dataset where interactions matter. Why the correct answer wins: A classical time series model suits a single series with strong seasonality.

### Question 30 — C

Answer: Choose a foundation model. A foundation model suits an open-ended language task where labelled data is scarce. Local study-map skill 3.1 (Model Type Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. TabNet gives an interpretable attentive tabular model inside custom training. Why the correct answer wins: A foundation model suits an open-ended language task where labelled data is scarce.
- **B:** Incorrect for this question. A DNN suits a large tabular or unstructured dataset where interactions matter. Why the correct answer wins: A foundation model suits an open-ended language task where labelled data is scarce.
- **C:** Correct. In this case: A foundation model suits an open-ended language task where labelled data is scarce.
- **D:** Incorrect for this question. A classical time series model suits a single series with strong seasonality and little covariate data. Why the correct answer wins: A foundation model suits an open-ended language task where labelled data is scarce.

### Question 31 — A

Answer: Build the model in BigQuery ML. BigQuery ML keeps training next to the data and removes a separate serving pipeline. Local study-map skill 3.2 (Product Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: BigQuery ML keeps training next to the data and removes a separate serving pipeline.
- **B:** Incorrect for this question. Custom training keeps full control of the framework and the loss. Why the correct answer wins: BigQuery ML keeps training next to the data and removes a separate serving pipeline.
- **C:** Incorrect for this question. TabNet gives an interpretable attentive tabular model inside custom training. Why the correct answer wins: BigQuery ML keeps training next to the data and removes a separate serving pipeline.
- **D:** Incorrect for this question. AutoML removes architecture search and tuning from the team while keeping a managed endpoint. Why the correct answer wins: BigQuery ML keeps training next to the data and removes a separate serving pipeline.

### Question 32 — C

Answer: Choose the product the team can actually operate. A product the team cannot debug becomes an outage with a schedule. Local study-map skill 3.2 (Product Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. AutoML removes architecture search and tuning from the team while keeping a managed endpoint. Why the correct answer wins: A product the team cannot debug becomes an outage with a schedule.
- **B:** Incorrect for this question. Custom training keeps full control of the framework and the loss. Why the correct answer wins: A product the team cannot debug becomes an outage with a schedule.
- **C:** Correct. In this case: A product the team cannot debug becomes an outage with a schedule.
- **D:** Incorrect for this question. BigQuery ML keeps training next to the data and removes a separate serving pipeline. Why the correct answer wins: A product the team cannot debug becomes an outage with a schedule.

### Question 33 — C, D

Answers: Roll out a canary with a small traffic share; Split traffic between two models in an A/B test. A/B testing compares two models on one population, and a canary holds a small share. A canary limits the blast radius while the new model is compared with the old one. A/B testing compares two models on the same population with a traffic split. Local study-map skill 3.3 (Deployment Strategy Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. An in-place replacement exposes every request to the new version at once. Why the correct answer wins: A/B testing compares two models on one population, and a canary holds a small share.
- **B:** Incorrect for this question. Shadow mode scores live traffic without serving its answers, so the comparison costs nothing to users. Why the correct answer wins: A/B testing compares two models on one population, and a canary holds a small share.
- **C:** Correct. A canary limits the blast radius while the new model is compared with the old one. In this case: A/B testing compares two models on one population, and a canary holds a small share.
- **D:** Correct. A/B testing compares two models on the same population with a traffic split. In this case: A/B testing compares two models on one population, and a canary holds a small share.
- **E:** Incorrect for this question. Two identical deployments let the switch be reversed immediately. Why the correct answer wins: A/B testing compares two models on one population, and a canary holds a small share.

### Question 34 — A

Answer: Deploy blue/green with an instant switch. Two identical deployments let the switch be reversed immediately. Local study-map skill 3.3 (Deployment Strategy Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Two identical deployments let the switch be reversed immediately.
- **B:** Incorrect for this question. An in-place replacement exposes every request to the new version at once. Why the correct answer wins: Two identical deployments let the switch be reversed immediately.
- **C:** Incorrect for this question. A canary limits the blast radius while the new model is compared with the old one. Why the correct answer wins: Two identical deployments let the switch be reversed immediately.
- **D:** Incorrect for this question. Shadow mode scores live traffic without serving its answers, so the comparison costs nothing to users. Why the correct answer wins: Two identical deployments let the switch be reversed immediately.

### Question 35 — D

Answer: Summarise the model with ML.GLOBAL_EXPLAIN. ML.GLOBAL_EXPLAIN ranks the features that matter most across the whole model. Local study-map skill 3.4 (Interpretability), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Shapley values attribute a prediction to its features with a consistent baseline. Why the correct answer wins: ML.GLOBAL_EXPLAIN ranks the features that matter most across the whole model.
- **B:** Incorrect for this question. Sampled Shapley explains individual online predictions with a bounded compute cost. Why the correct answer wins: ML.GLOBAL_EXPLAIN ranks the features that matter most across the whole model.
- **C:** Incorrect for this question. ML.EXPLAIN_PREDICT attributes each prediction to the features that moved it. Why the correct answer wins: ML.GLOBAL_EXPLAIN ranks the features that matter most across the whole model.
- **D:** Correct. In this case: ML.GLOBAL_EXPLAIN ranks the features that matter most across the whole model.

### Question 36 — A

Answer: Use integrated gradients for the image model. Integrated gradients attributes an image prediction to the pixels that moved it. Local study-map skill 3.4 (Interpretability), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Integrated gradients attributes an image prediction to the pixels that moved it.
- **B:** Incorrect for this question. A linear or tree model can be read directly when regulation demands an explanation by construction. Why the correct answer wins: Integrated gradients attributes an image prediction to the pixels that moved it.
- **C:** Incorrect for this question. Shapley values attribute a prediction to its features with a consistent baseline. Why the correct answer wins: Integrated gradients attributes an image prediction to the pixels that moved it.
- **D:** Incorrect for this question. Sampled Shapley explains individual online predictions with a bounded compute cost. Why the correct answer wins: Integrated gradients attributes an image prediction to the pixels that moved it.

### Question 37 — C

Answer: Write the training data as TFRecord shards in Cloud Storage. Sharded TFRecord is the efficient read format for distributed training. Local study-map skill 3.5 (Training Data Organization), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Reading from BigQuery avoids a copy and keeps the query pushdown. Why the correct answer wins: Sharded TFRecord is the efficient read format for distributed training.
- **B:** Incorrect for this question. Parquet is columnar and cheap to scan for tabular training data. Why the correct answer wins: Sharded TFRecord is the efficient read format for distributed training.
- **C:** Correct. In this case: Sharded TFRecord is the efficient read format for distributed training.
- **D:** Incorrect for this question. A streaming path keeps the training data current without a nightly copy. Why the correct answer wins: Sharded TFRecord is the efficient read format for distributed training.

### Question 38 — C

Answer: Read the training data directly from BigQuery. Reading from BigQuery avoids a copy and keeps the query pushdown. Local study-map skill 3.5 (Training Data Organization), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Parquet is columnar and cheap to scan for tabular training data. Why the correct answer wins: Reading from BigQuery avoids a copy and keeps the query pushdown.
- **B:** Incorrect for this question. Sharded TFRecord is the efficient read format for distributed training. Why the correct answer wins: Reading from BigQuery avoids a copy and keeps the query pushdown.
- **C:** Correct. In this case: Reading from BigQuery avoids a copy and keeps the query pushdown.
- **D:** Incorrect for this question. A streaming path keeps the training data current without a nightly copy. Why the correct answer wins: Reading from BigQuery avoids a copy and keeps the query pushdown.

### Question 39 — D

Answer: Stream the new records through Dataflow into the training store. A streaming path keeps the training data current without a nightly copy. Local study-map skill 3.6 (Ingestion into Training Pipelines), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Deduplicating at ingest stops duplicated records inflating the training set. Why the correct answer wins: A streaming path keeps the training data current without a nightly copy.
- **B:** Incorrect for this question. Parquet is columnar and cheap to scan for tabular training data. Why the correct answer wins: A streaming path keeps the training data current without a nightly copy.
- **C:** Incorrect for this question. Rejecting rows into a side table makes a schema break visible instead of silent. Why the correct answer wins: A streaming path keeps the training data current without a nightly copy.
- **D:** Correct. In this case: A streaming path keeps the training data current without a nightly copy.

### Question 40 — D

Answer: Deduplicate on the event key in the ingestion step. Deduplicating at ingest stops duplicated records inflating the training set. Local study-map skill 3.6 (Ingestion into Training Pipelines), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Reading from BigQuery avoids a copy and keeps the query pushdown. Why the correct answer wins: Deduplicating at ingest stops duplicated records inflating the training set.
- **B:** Incorrect for this question. A streaming path keeps the training data current without a nightly copy. Why the correct answer wins: Deduplicating at ingest stops duplicated records inflating the training set.
- **C:** Incorrect for this question. Rejecting rows into a side table makes a schema break visible instead of silent. Why the correct answer wins: Deduplicating at ingest stops duplicated records inflating the training set.
- **D:** Correct. In this case: Deduplicating at ingest stops duplicated records inflating the training set.

### Question 41 — B

Answer: Package the trainer as a Python package. The prebuilt container installs the package, which is the lightest way to run custom code. Local study-map skill 3.7 (Custom Training and SDKs), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Export produces a container-ready artifact that can be served outside the managed endpoint. Why the correct answer wins: The prebuilt container installs the package, which is the lightest way to run custom code.
- **B:** Correct. In this case: The prebuilt container installs the package, which is the lightest way to run custom code.
- **C:** Incorrect for this question. A custom container carries its own framework and dependencies into the managed training job. Why the correct answer wins: The prebuilt container installs the package, which is the lightest way to run custom code.
- **D:** Incorrect for this question. A prebuilt container already implements the framework handler, so no serving code is written. Why the correct answer wins: The prebuilt container installs the package, which is the lightest way to run custom code.

### Question 42 — A

Answer: Set the reduction server for the all-reduce. The reduction server offloads gradient aggregation and shortens the training step. Local study-map skill 3.7 (Custom Training and SDKs), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: The reduction server offloads gradient aggregation and shortens the training step.
- **B:** Incorrect for this question. Data parallelism replicates the model and splits each batch across the workers. Why the correct answer wins: The reduction server offloads gradient aggregation and shortens the training step.
- **C:** Incorrect for this question. Multi-worker gives each replica a shard of the data and a defined chief. Why the correct answer wins: The reduction server offloads gradient aggregation and shortens the training step.
- **D:** Incorrect for this question. Model parallelism splits the layers across devices when one model does not fit on one. Why the correct answer wins: The reduction server offloads gradient aggregation and shortens the training step.

### Question 43 — A

Answer: Verify each worker reads a distinct shard. Duplicated shards silently shrink the effective dataset and skew the loss. Local study-map skill 3.8 (Training Failure Troubleshooting), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Duplicated shards silently shrink the effective dataset and skew the loss.
- **B:** Incorrect for this question. A loss that becomes NaN usually reflects a step size too large for the data scale. Why the correct answer wins: Duplicated shards silently shrink the effective dataset and skew the loss.
- **C:** Incorrect for this question. The out-of-memory error is a memory-per-step problem, so the batch is the first lever. Why the correct answer wins: Duplicated shards silently shrink the effective dataset and skew the loss.
- **D:** Incorrect for this question. Accelerator quota is regional and blocks the job before the code runs. Why the correct answer wins: Duplicated shards silently shrink the effective dataset and skew the loss.

### Question 44 — D

Answer: Pin the framework version in the container. A framework mismatch between local and remote runs changes behaviour without changing the code. Local study-map skill 3.8 (Training Failure Troubleshooting), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A permission error on the input is a missing IAM binding, not a model problem. Why the correct answer wins: A framework mismatch between local and remote runs changes behaviour without changing the code.
- **B:** Incorrect for this question. The out-of-memory error is a memory-per-step problem, so the batch is the first lever. Why the correct answer wins: A framework mismatch between local and remote runs changes behaviour without changing the code.
- **C:** Incorrect for this question. A loss that becomes NaN usually reflects a step size too large for the data scale. Why the correct answer wins: A framework mismatch between local and remote runs changes behaviour without changing the code.
- **D:** Correct. In this case: A framework mismatch between local and remote runs changes behaviour without changing the code.

### Question 45 — A, C

Answers: Run a hyperparameter tuning job; Report the business metric from the trainer. The tuning service searches in parallel, and it optimises the metric the trainer reports. The tuning service searches the space in parallel and reports the best trial. The search optimises the metric the trainer reports, so it must be the one that matters. Local study-map skill 3.9 (Hyperparameter Tuning), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. The tuning service searches the space in parallel and reports the best trial. In this case: The tuning service searches in parallel, and it optimises the metric the trainer reports.
- **B:** Incorrect for this question. Early stopping frees capacity from trials that cannot win. Why the correct answer wins: The tuning service searches in parallel, and it optimises the metric the trainer reports.
- **C:** Correct. The search optimises the metric the trainer reports, so it must be the one that matters. In this case: The tuning service searches in parallel, and it optimises the metric the trainer reports.
- **D:** Incorrect for this question. Bayesian search spends fewer trials to reach a good configuration. Why the correct answer wins: The tuning service searches in parallel, and it optimises the metric the trainer reports.
- **E:** Incorrect for this question. A fixed seed makes a rerun reproducible when the rest of the environment is pinned. Why the correct answer wins: The tuning service searches in parallel, and it optimises the metric the trainer reports.

### Question 46 — D

Answer: Cap the search with a trial count and a parallel budget. The budget bounds both the cost and the wall-clock time of the search. Local study-map skill 3.9 (Hyperparameter Tuning), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The search optimises the metric the trainer reports, so it must be the one that matters. Why the correct answer wins: The budget bounds both the cost and the wall-clock time of the search.
- **B:** Incorrect for this question. Early stopping frees capacity from trials that cannot win. Why the correct answer wins: The budget bounds both the cost and the wall-clock time of the search.
- **C:** Incorrect for this question. Bayesian search spends fewer trials to reach a good configuration. Why the correct answer wins: The budget bounds both the cost and the wall-clock time of the search.
- **D:** Correct. In this case: The budget bounds both the cost and the wall-clock time of the search.

### Question 47 — C

Answer: Fine-tune when the model must follow a house style or output contract. Tuning changes behaviour; retrieval changes knowledge. Style and format are behaviour. Local study-map skill 3.10 (Fine-Tuning Decisions), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A better prompt is the cheapest experiment and often removes the need to tune at all. Why the correct answer wins: Tuning changes behaviour; retrieval changes knowledge. Style and format are behaviour.
- **B:** Incorrect for this question. Full fine-tuning updates every weight and needs the most data and accelerator memory. Why the correct answer wins: Tuning changes behaviour; retrieval changes knowledge. Style and format are behaviour.
- **C:** Correct. In this case: Tuning changes behaviour; retrieval changes knowledge. Style and format are behaviour.
- **D:** Incorrect for this question. Retrieval is the cheaper answer when the problem is missing knowledge rather than missing behaviour. Why the correct answer wins: Tuning changes behaviour; retrieval changes knowledge. Style and format are behaviour.

### Question 48 — B

Answer: Train on A100 GPUs. A100 GPUs suit mixed-precision training where the framework expects CUDA. Local study-map skill 3.11 (Hardware and Accelerator Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A TPU slice gives a tightly coupled accelerator fabric for large synchronous training. Why the correct answer wins: A100 GPUs suit mixed-precision training where the framework expects CUDA.
- **B:** Correct. In this case: A100 GPUs suit mixed-precision training where the framework expects CUDA.
- **C:** Incorrect for this question. CPU serving is the cheapest option for a small model with a generous latency budget. Why the correct answer wins: A100 GPUs suit mixed-precision training where the framework expects CUDA.
- **D:** Incorrect for this question. An L4 GPU gives low-cost inference acceleration for a modest model. Why the correct answer wins: A100 GPUs suit mixed-precision training where the framework expects CUDA.

### Question 49 — A, C

Answers: Use model parallelism; Checkpoint to Cloud Storage and resume from the last step. Model parallelism splits the layers across devices, and a checkpoint turns preemption into a delay. Model parallelism splits the layers across devices when one model does not fit on one. A checkpoint turns a preemption into a delay rather than a restart. Local study-map skill 3.12 (Distributed Training), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. A checkpoint turns a preemption into a delay rather than a restart. In this case: Model parallelism splits the layers across devices, and a checkpoint turns preemption into a delay.
- **B:** Incorrect for this question. A larger global batch keeps each worker busy after the split. Why the correct answer wins: Model parallelism splits the layers across devices, and a checkpoint turns preemption into a delay.
- **C:** Correct. Model parallelism splits the layers across devices when one model does not fit on one. In this case: Model parallelism splits the layers across devices, and a checkpoint turns preemption into a delay.
- **D:** Incorrect for this question. Data parallelism replicates the model and splits each batch across the workers. Why the correct answer wins: Model parallelism splits the layers across devices, and a checkpoint turns preemption into a delay.
- **E:** Incorrect for this question. CPU serving is the cheapest option for a small model with a generous latency budget. Why the correct answer wins: Model parallelism splits the layers across devices, and a checkpoint turns preemption into a delay.

### Question 50 — D

Answer: Deploy to an online endpoint. An endpoint keeps capacity ready for low-latency per-request predictions. Local study-map skill 4.1 (Batch and Online Inference), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Streaming answers each event as it arrives rather than on a schedule. Why the correct answer wins: An endpoint keeps capacity ready for low-latency per-request predictions.
- **B:** Incorrect for this question. Batch prediction reads a file or table and writes predictions without holding serving capacity. Why the correct answer wins: An endpoint keeps capacity ready for low-latency per-request predictions.
- **C:** Incorrect for this question. Batching amortises the per-request overhead when the caller can wait. Why the correct answer wins: An endpoint keeps capacity ready for low-latency per-request predictions.
- **D:** Correct. In this case: An endpoint keeps capacity ready for low-latency per-request predictions.

### Question 51 — A, C

Answers: Run batch prediction; Set a minimum replica count. Batch prediction needs no serving capacity, and no minimum replica keeps the cost to the scan. Batch prediction reads a file or table and writes predictions without holding serving capacity. A minimum replica keeps capacity warm so the first request after a quiet period is fast. Local study-map skill 4.1 (Batch and Online Inference), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. Batch prediction reads a file or table and writes predictions without holding serving capacity. In this case: Batch prediction needs no serving capacity, and no minimum replica keeps the cost to the scan.
- **B:** Incorrect for this question. A GPU shortens inference time enough to meet a tight latency target. Why the correct answer wins: Batch prediction needs no serving capacity, and no minimum replica keeps the cost to the scan.
- **C:** Correct. A minimum replica keeps capacity warm so the first request after a quiet period is fast. In this case: Batch prediction needs no serving capacity, and no minimum replica keeps the cost to the scan.
- **D:** Incorrect for this question. Streaming answers each event as it arrives rather than on a schedule. Why the correct answer wins: Batch prediction needs no serving capacity, and no minimum replica keeps the cost to the scan.
- **E:** Incorrect for this question. Batching amortises the per-request overhead when the caller can wait. Why the correct answer wins: Batch prediction needs no serving capacity, and no minimum replica keeps the cost to the scan.

### Question 52 — C

Answer: Send the events to a streaming prediction path. Streaming answers each event as it arrives rather than on a schedule. Local study-map skill 4.1 (Batch and Online Inference), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. An endpoint keeps capacity ready for low-latency per-request predictions. Why the correct answer wins: Streaming answers each event as it arrives rather than on a schedule.
- **B:** Incorrect for this question. Batching amortises the per-request overhead when the caller can wait. Why the correct answer wins: Streaming answers each event as it arrives rather than on a schedule.
- **C:** Correct. In this case: Streaming answers each event as it arrives rather than on a schedule.
- **D:** Incorrect for this question. Batch prediction reads a file or table and writes predictions without holding serving capacity. Why the correct answer wins: Streaming answers each event as it arrives rather than on a schedule.

### Question 53 — A

Answer: Add a custom prediction routine to the container. The routine runs the preprocessing and postprocessing inside the serving container. Local study-map skill 4.2 (Packaging and Custom Containers), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: The routine runs the preprocessing and postprocessing inside the serving container.
- **B:** Incorrect for this question. Artifact Registry holds the image with IAM and vulnerability metadata. Why the correct answer wins: The routine runs the preprocessing and postprocessing inside the serving container.
- **C:** Incorrect for this question. A prebuilt container already implements the framework handler, so no serving code is written. Why the correct answer wins: The routine runs the preprocessing and postprocessing inside the serving container.
- **D:** Incorrect for this question. An alias decouples the served version name from the artifact id, so a rollback is a pointer move. Why the correct answer wins: The routine runs the preprocessing and postprocessing inside the serving container.

### Question 54 — B

Answer: Push the serving image to Artifact Registry. Artifact Registry holds the image with IAM and vulnerability metadata. Local study-map skill 4.2 (Packaging and Custom Containers), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A prebuilt container already implements the framework handler, so no serving code is written. Why the correct answer wins: Artifact Registry holds the image with IAM and vulnerability metadata.
- **B:** Correct. In this case: Artifact Registry holds the image with IAM and vulnerability metadata.
- **C:** Incorrect for this question. The registry versions the model artifact and links it to its lineage and metrics. Why the correct answer wins: Artifact Registry holds the image with IAM and vulnerability metadata.
- **D:** Incorrect for this question. A custom container carries its own framework and dependencies into the managed training job. Why the correct answer wins: Artifact Registry holds the image with IAM and vulnerability metadata.

### Question 55 — B

Answer: Deploy the version and move the alias. An alias decouples the served version name from the artifact id. Local study-map skill 4.3 (Model Registry and Versioning), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. An in-place replacement exposes every request to the new version at once. Why the correct answer wins: An alias decouples the served version name from the artifact id.
- **B:** Correct. In this case: An alias decouples the served version name from the artifact id.
- **C:** Incorrect for this question. A traffic split sends a defined share to each version on the same endpoint. Why the correct answer wins: An alias decouples the served version name from the artifact id.
- **D:** Incorrect for this question. The registry versions the model artifact and links it to its lineage and metrics. Why the correct answer wins: An alias decouples the served version name from the artifact id.

### Question 56 — A

Answer: Track artifacts and lineage in ML Metadata. ML Metadata records which data and code produced which artifact. Local study-map skill 4.3 (Model Registry and Versioning), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: ML Metadata records which data and code produced which artifact.
- **B:** Incorrect for this question. The registry versions the model artifact and links it to its lineage and metrics. Why the correct answer wins: ML Metadata records which data and code produced which artifact.
- **C:** Incorrect for this question. Artifact Registry holds the image with IAM and vulnerability metadata. Why the correct answer wins: ML Metadata records which data and code produced which artifact.
- **D:** Incorrect for this question. Experiments records parameters, metrics, and artifacts per run so runs can be compared. Why the correct answer wins: ML Metadata records which data and code produced which artifact.

### Question 57 — A, C

Answers: Run the new model in shadow mode; Roll out a canary with a small traffic share. Shadow mode serves nothing to users, and a canary limits the exposure. Shadow mode scores live traffic without serving its answers, so the comparison costs nothing to users. A canary limits the blast radius while the new model is compared with the old one. Local study-map skill 4.4 (Model Rollout Strategies), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. Shadow mode scores live traffic without serving its answers, so the comparison costs nothing to users. In this case: Shadow mode serves nothing to users, and a canary limits the exposure.
- **B:** Incorrect for this question. An in-place replacement exposes every request to the new version at once. Why the correct answer wins: Shadow mode serves nothing to users, and a canary limits the exposure.
- **C:** Correct. A canary limits the blast radius while the new model is compared with the old one. In this case: Shadow mode serves nothing to users, and a canary limits the exposure.
- **D:** Incorrect for this question. Two identical deployments let the switch be reversed immediately. Why the correct answer wins: Shadow mode serves nothing to users, and a canary limits the exposure.
- **E:** Incorrect for this question. A/B testing compares two models on the same population with a traffic split. Why the correct answer wins: Shadow mode serves nothing to users, and a canary limits the exposure.

### Question 58 — A

Answer: Split traffic between two models in an A/B test. A/B testing compares two models on the same population. Local study-map skill 4.4 (Model Rollout Strategies), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: A/B testing compares two models on the same population.
- **B:** Incorrect for this question. An in-place replacement exposes every request to the new version at once. Why the correct answer wins: A/B testing compares two models on the same population.
- **C:** Incorrect for this question. Shadow mode scores live traffic without serving its answers, so the comparison costs nothing to users. Why the correct answer wins: A/B testing compares two models on the same population.
- **D:** Incorrect for this question. A canary limits the blast radius while the new model is compared with the old one. Why the correct answer wins: A/B testing compares two models on the same population.

### Question 59 — C

Answer: Share one transformation library between training and serving. Shared code removes the class of bug where the two paths compute a feature differently. Local study-map skill 4.5 (Inference Preprocessing and Postprocessing), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Feature Store keeps one definition that both training and serving read. Why the correct answer wins: Shared code removes the class of bug where the two paths compute a feature differently.
- **B:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: Shared code removes the class of bug where the two paths compute a feature differently.
- **C:** Correct. In this case: Shared code removes the class of bug where the two paths compute a feature differently.
- **D:** Incorrect for this question. An alias decouples the served version name from the artifact id, so a rollback is a pointer move. Why the correct answer wins: Shared code removes the class of bug where the two paths compute a feature differently.

### Question 60 — C

Answer: Keep the preprocessing inside the exported model. Preprocessing inside the artifact cannot drift between the two paths. Local study-map skill 4.5 (Inference Preprocessing and Postprocessing), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Feature Store keeps one definition that both training and serving read. Why the correct answer wins: Preprocessing inside the artifact cannot drift between the two paths.
- **B:** Incorrect for this question. Shared code removes the class of bug where the two paths compute a feature differently. Why the correct answer wins: Preprocessing inside the artifact cannot drift between the two paths.
- **C:** Correct. In this case: Preprocessing inside the artifact cannot drift between the two paths.
- **D:** Incorrect for this question. Explanation metadata tells the endpoint which inputs to attribute over. Why the correct answer wins: Preprocessing inside the artifact cannot drift between the two paths.

### Question 61 — B

Answer: Deploy with a private endpoint only. A private endpoint is reachable only from the VPC. Local study-map skill 4.6 (Endpoint Types and Access), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A dedicated endpoint gives the model its own capacity instead of sharing a pool. Why the correct answer wins: A private endpoint is reachable only from the VPC.
- **B:** Correct. In this case: A private endpoint is reachable only from the VPC.
- **C:** Incorrect for this question. A GPU shortens inference time enough to meet a tight latency target. Why the correct answer wins: A private endpoint is reachable only from the VPC.
- **D:** Incorrect for this question. A shared endpoint removes the deployment step but gives no control over capacity or residency. Why the correct answer wins: A private endpoint is reachable only from the VPC.

### Question 62 — D

Answer: Use a dedicated endpoint. A dedicated endpoint gives the model its own capacity. Local study-map skill 4.6 (Endpoint Types and Access), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A private endpoint is reachable only from the VPC and shares no public surface. Why the correct answer wins: A dedicated endpoint gives the model its own capacity.
- **B:** Incorrect for this question. A shared endpoint removes the deployment step but gives no control over capacity or residency. Why the correct answer wins: A dedicated endpoint gives the model its own capacity.
- **C:** Incorrect for this question. A traffic split sends a defined share to each version on the same endpoint. Why the correct answer wins: A dedicated endpoint gives the model its own capacity.
- **D:** Correct. In this case: A dedicated endpoint gives the model its own capacity.

### Question 63 — A

Answer: Serve on L4 GPUs. An L4 GPU gives low-cost inference acceleration for a modest model. Local study-map skill 4.7 (Serving Hardware), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: An L4 GPU gives low-cost inference acceleration for a modest model.
- **B:** Incorrect for this question. A100 GPUs suit mixed-precision training where the framework expects CUDA. Why the correct answer wins: An L4 GPU gives low-cost inference acceleration for a modest model.
- **C:** Incorrect for this question. CPU serving is the cheapest option for a small model with a generous latency budget. Why the correct answer wins: An L4 GPU gives low-cost inference acceleration for a modest model.
- **D:** Incorrect for this question. A TPU slice gives a tightly coupled accelerator fabric for large synchronous training. Why the correct answer wins: An L4 GPU gives low-cost inference acceleration for a modest model.

### Question 64 — C

Answer: Train on a TPU slice. A TPU slice gives a tightly coupled accelerator fabric for large models. Local study-map skill 4.7 (Serving Hardware), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A100 GPUs suit mixed-precision training where the framework expects CUDA. Why the correct answer wins: A TPU slice gives a tightly coupled accelerator fabric for large models.
- **B:** Incorrect for this question. An L4 GPU gives low-cost inference acceleration for a modest model. Why the correct answer wins: A TPU slice gives a tightly coupled accelerator fabric for large models.
- **C:** Correct. In this case: A TPU slice gives a tightly coupled accelerator fabric for large models.
- **D:** Incorrect for this question. CPU serving is the cheapest option for a small model with a generous latency budget. Why the correct answer wins: A TPU slice gives a tightly coupled accelerator fabric for large models.

### Question 65 — C, D

Answers: Raise the concurrency per replica; Enable autoscaling on the endpoint. Concurrency lowers cost per request, and autoscaling adds replicas with the traffic. Concurrency fills each replica before another is started, which lowers cost per request. Autoscaling adds replicas with the traffic and removes them afterwards. Local study-map skill 4.8 (Serving Throughput and Scaling), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Batching amortises the per-request overhead when the caller can wait. Why the correct answer wins: Concurrency lowers cost per request, and autoscaling adds replicas with the traffic.
- **B:** Incorrect for this question. A minimum replica keeps capacity warm so the first request after a quiet period is fast. Why the correct answer wins: Concurrency lowers cost per request, and autoscaling adds replicas with the traffic.
- **C:** Correct. Concurrency fills each replica before another is started, which lowers cost per request. In this case: Concurrency lowers cost per request, and autoscaling adds replicas with the traffic.
- **D:** Correct. Autoscaling adds replicas with the traffic and removes them afterwards. In this case: Concurrency lowers cost per request, and autoscaling adds replicas with the traffic.
- **E:** Incorrect for this question. The ceiling caps how far the endpoint scales, and therefore the throughput it can absorb. Why the correct answer wins: Concurrency lowers cost per request, and autoscaling adds replicas with the traffic.

### Question 66 — B

Answer: Raise the maximum replica count. The ceiling caps how far the endpoint scales. Local study-map skill 4.8 (Serving Throughput and Scaling), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Concurrency fills each replica before another is started, which lowers cost per request. Why the correct answer wins: The ceiling caps how far the endpoint scales.
- **B:** Correct. In this case: The ceiling caps how far the endpoint scales.
- **C:** Incorrect for this question. A GPU shortens inference time enough to meet a tight latency target. Why the correct answer wins: The ceiling caps how far the endpoint scales.
- **D:** Incorrect for this question. A minimum replica keeps capacity warm so the first request after a quiet period is fast. Why the correct answer wins: The ceiling caps how far the endpoint scales.

### Question 67 — A

Answer: Batch the requests inside the client. Batching amortises the per-request overhead when the caller can wait. Local study-map skill 4.8 (Serving Throughput and Scaling), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Batching amortises the per-request overhead when the caller can wait.
- **B:** Incorrect for this question. Batch prediction reads a file or table and writes predictions without holding serving capacity. Why the correct answer wins: Batching amortises the per-request overhead when the caller can wait.
- **C:** Incorrect for this question. Concurrency fills each replica before another is started, which lowers cost per request. Why the correct answer wins: Batching amortises the per-request overhead when the caller can wait.
- **D:** Incorrect for this question. Autoscaling adds replicas with the traffic and removes them afterwards. Why the correct answer wins: Batching amortises the per-request overhead when the caller can wait.

### Question 68 — C, E

Answers: Raise the concurrency per replica; Configure explanation metadata for the endpoint. Explanation metadata enables attributions, and concurrency lowers the cost per request. Concurrency fills each replica before another is started, which lowers cost per request. Explanation metadata tells the endpoint which inputs to attribute over. Local study-map skill 4.9 (Production Tuning), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Artifact Registry holds the image with IAM and vulnerability metadata. Why the correct answer wins: Explanation metadata enables attributions, and concurrency lowers the cost per request.
- **B:** Incorrect for this question. An alias decouples the served version name from the artifact id, so a rollback is a pointer move. Why the correct answer wins: Explanation metadata enables attributions, and concurrency lowers the cost per request.
- **C:** Correct. Concurrency fills each replica before another is started, which lowers cost per request. In this case: Explanation metadata enables attributions, and concurrency lowers the cost per request.
- **D:** Incorrect for this question. Batching amortises the per-request overhead when the caller can wait. Why the correct answer wins: Explanation metadata enables attributions, and concurrency lowers the cost per request.
- **E:** Correct. Explanation metadata tells the endpoint which inputs to attribute over. In this case: Explanation metadata enables attributions, and concurrency lowers the cost per request.

### Question 69 — D

Answer: Attach a GPU to the serving replica. A GPU shortens inference time enough to meet a tight latency target. Local study-map skill 4.9 (Production Tuning), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Concurrency fills each replica before another is started, which lowers cost per request. Why the correct answer wins: A GPU shortens inference time enough to meet a tight latency target.
- **B:** Incorrect for this question. The ceiling caps how far the endpoint scales, and therefore the throughput it can absorb. Why the correct answer wins: A GPU shortens inference time enough to meet a tight latency target.
- **C:** Incorrect for this question. Batching amortises the per-request overhead when the caller can wait. Why the correct answer wins: A GPU shortens inference time enough to meet a tight latency target.
- **D:** Correct. In this case: A GPU shortens inference time enough to meet a tight latency target.

### Question 70 — A

Answer: Gate the deployment on a model evaluation threshold. The gate promotes a model only when it beats the incumbent. Local study-map skill 5.1 (Data and Model Validation), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: The gate promotes a model only when it beats the incumbent.
- **B:** Incorrect for this question. Metric-triggered retraining reacts to actual quality loss. Why the correct answer wins: The gate promotes a model only when it beats the incumbent.
- **C:** Incorrect for this question. A validation step stops a bad batch before it reaches training. Why the correct answer wins: The gate promotes a model only when it beats the incumbent.
- **D:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: The gate promotes a model only when it beats the incumbent.

### Question 71 — D

Answer: Validate the schema and quarantine rejected rows. Rejecting rows into a side table makes a schema break visible instead of silent. Local study-map skill 5.1 (Data and Model Validation), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The gate promotes a model only when it beats the incumbent on the agreed metric. Why the correct answer wins: Rejecting rows into a side table makes a schema break visible instead of silent.
- **B:** Incorrect for this question. A validation step stops a bad batch before it reaches training. Why the correct answer wins: Rejecting rows into a side table makes a schema break visible instead of silent.
- **C:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: Rejecting rows into a side table makes a schema break visible instead of silent.
- **D:** Correct. In this case: Rejecting rows into a side table makes a schema break visible instead of silent.

### Question 72 — A, E

Answers: Keep the test set out of every tuning decision; Add an explicit data validation step. A locked test set restores an unbiased estimate, and validation stops a bad batch early. A test set that has been used for tuning no longer estimates generalisation. A validation step stops a bad batch before it reaches training. Local study-map skill 5.1 (Data and Model Validation), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. A validation step stops a bad batch before it reaches training. In this case: A locked test set restores an unbiased estimate, and validation stops a bad batch early.
- **B:** Incorrect for this question. The matrix shows the false-positive and false-negative split the business will feel. Why the correct answer wins: A locked test set restores an unbiased estimate, and validation stops a bad batch early.
- **C:** Incorrect for this question. A fixed seed makes a rerun reproducible when the rest of the environment is pinned. Why the correct answer wins: A locked test set restores an unbiased estimate, and validation stops a bad batch early.
- **D:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: A locked test set restores an unbiased estimate, and validation stops a bad batch early.
- **E:** Correct. A test set that has been used for tuning no longer estimates generalisation. In this case: A locked test set restores an unbiased estimate, and validation stops a bad batch early.

### Question 73 — C

Answer: Orchestrate with Managed Service for Apache Airflow. Airflow expresses cross-system dependencies and schedules outside the ML platform. Local study-map skill 5.2 (Pipeline Orchestration Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Kubeflow pipelines give a container-per-step pipeline that runs on the managed service or on GKE. Why the correct answer wins: Airflow expresses cross-system dependencies and schedules outside the ML platform.
- **B:** Incorrect for this question. Ray fits a Python-native distributed workload that is not a container-per-step pipeline. Why the correct answer wins: Airflow expresses cross-system dependencies and schedules outside the ML platform.
- **C:** Correct. In this case: Airflow expresses cross-system dependencies and schedules outside the ML platform.
- **D:** Incorrect for this question. Pipelines runs each step as a container with caching, lineage, and retry. Why the correct answer wins: Airflow expresses cross-system dependencies and schedules outside the ML platform.

### Question 74 — B

Answer: Orchestrate the steps in Agent Platform Pipelines. Pipelines runs each step as a container with caching, lineage, and retry. Local study-map skill 5.2 (Pipeline Orchestration Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Airflow expresses cross-system dependencies and schedules outside the ML platform. Why the correct answer wins: Pipelines runs each step as a container with caching, lineage, and retry.
- **B:** Correct. In this case: Pipelines runs each step as a container with caching, lineage, and retry.
- **C:** Incorrect for this question. Ray fits a Python-native distributed workload that is not a container-per-step pipeline. Why the correct answer wins: Pipelines runs each step as a container with caching, lineage, and retry.
- **D:** Incorrect for this question. Kubeflow pipelines give a container-per-step pipeline that runs on the managed service or on GKE. Why the correct answer wins: Pipelines runs each step as a container with caching, lineage, and retry.

### Question 75 — C

Answer: Trigger the build and deploy from Cloud Build. Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance. Local study-map skill 5.2 (Pipeline Orchestration Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The scheduler starts the pipeline on the cadence the retraining policy defines. Why the correct answer wins: Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance.
- **B:** Incorrect for this question. Pipelines runs each step as a container with caching, lineage, and retry. Why the correct answer wins: Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance.
- **C:** Correct. In this case: Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance.
- **D:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance.

### Question 76 — A

Answer: Express the workflow as a Kubeflow pipeline. A Kubeflow pipeline can run on the managed service or on GKE. Kubeflow pipelines give a container-per-step pipeline that runs on the managed service or on GKE. Local study-map skill 5.2 (Pipeline Orchestration Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. Kubeflow pipelines give a container-per-step pipeline that runs on the managed service or on GKE. In this case: A Kubeflow pipeline can run on the managed service or on GKE.
- **B:** Incorrect for this question. Airflow expresses cross-system dependencies and schedules outside the ML platform. Why the correct answer wins: A Kubeflow pipeline can run on the managed service or on GKE.
- **C:** Incorrect for this question. Ray fits a Python-native distributed workload that is not a container-per-step pipeline. Why the correct answer wins: A Kubeflow pipeline can run on the managed service or on GKE.
- **D:** Incorrect for this question. Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance. Why the correct answer wins: A Kubeflow pipeline can run on the managed service or on GKE.

### Question 77 — D

Answer: Keep the preprocessing inside the exported model. Preprocessing inside the artifact cannot drift between training and serving. Local study-map skill 5.3 (Train and Serve Consistency), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: Preprocessing inside the artifact cannot drift between training and serving.
- **B:** Incorrect for this question. Shared code removes the class of bug where the two paths compute a feature differently. Why the correct answer wins: Preprocessing inside the artifact cannot drift between training and serving.
- **C:** Incorrect for this question. Feature Store keeps one definition that both training and serving read. Why the correct answer wins: Preprocessing inside the artifact cannot drift between training and serving.
- **D:** Correct. In this case: Preprocessing inside the artifact cannot drift between training and serving.

### Question 78 — A, C

Answers: Share one transformation library between training and serving; Serve the feature from the online store. Shared code removes divergence, and the online store returns the latest value quickly. Shared code removes the class of bug where the two paths compute a feature differently. The online store returns the latest feature value at low latency for a single entity. Local study-map skill 5.3 (Train and Serve Consistency), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. The online store returns the latest feature value at low latency for a single entity. In this case: Shared code removes divergence, and the online store returns the latest value quickly.
- **B:** Incorrect for this question. The offline store returns point-in-time values for training. Why the correct answer wins: Shared code removes divergence, and the online store returns the latest value quickly.
- **C:** Correct. Shared code removes the class of bug where the two paths compute a feature differently. In this case: Shared code removes divergence, and the online store returns the latest value quickly.
- **D:** Incorrect for this question. The registry versions the model artifact and links it to its lineage and metrics. Why the correct answer wins: Shared code removes divergence, and the online store returns the latest value quickly.
- **E:** Incorrect for this question. Deduplicating at ingest stops duplicated records inflating the training set. Why the correct answer wins: Shared code removes divergence, and the online store returns the latest value quickly.

### Question 79 — A

Answer: Enable step caching. Caching skips an unchanged step on a rerun. Local study-map skill 5.3 (Train and Serve Consistency), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Caching skips an unchanged step on a rerun.
- **B:** Incorrect for this question. The gate promotes a model only when it beats the incumbent on the agreed metric. Why the correct answer wins: Caching skips an unchanged step on a rerun.
- **C:** Incorrect for this question. A validation step stops a bad batch before it reaches training. Why the correct answer wins: Caching skips an unchanged step on a rerun.
- **D:** Incorrect for this question. Drift-triggered retraining responds to change instead of to the calendar. Why the correct answer wins: Caching skips an unchanged step on a rerun.

### Question 80 — C

Answer: Read the historical features from the offline store. The offline store returns point-in-time values for training. Local study-map skill 5.3 (Train and Serve Consistency), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Feature monitoring reports distribution changes per feature, not just per model. Why the correct answer wins: The offline store returns point-in-time values for training.
- **B:** Incorrect for this question. A crossed feature lets a linear model express the interaction it cannot learn alone. Why the correct answer wins: The offline store returns point-in-time values for training.
- **C:** Correct. In this case: The offline store returns point-in-time values for training.
- **D:** Incorrect for this question. The online store returns the latest feature value at low latency for a single entity. Why the correct answer wins: The offline store returns point-in-time values for training.

### Question 81 — A

Answer: Retrain when drift crosses the threshold. Drift-triggered retraining responds to change instead of to the calendar. Local study-map skill 5.4 (Retraining Policy), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Drift-triggered retraining responds to change instead of to the calendar.
- **B:** Incorrect for this question. Metric-triggered retraining reacts to actual quality loss. Why the correct answer wins: Drift-triggered retraining responds to change instead of to the calendar.
- **C:** Incorrect for this question. Manual retraining leaves the model stale whenever the trigger is forgotten. Why the correct answer wins: Drift-triggered retraining responds to change instead of to the calendar.
- **D:** Incorrect for this question. A fixed schedule is simple to reason about when the data changes predictably. Why the correct answer wins: Drift-triggered retraining responds to change instead of to the calendar.

### Question 82 — B

Answer: Retrain on a fixed schedule. A fixed schedule is simple to reason about when the data changes predictably. Local study-map skill 5.4 (Retraining Policy), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Drift-triggered retraining responds to change instead of to the calendar. Why the correct answer wins: A fixed schedule is simple to reason about when the data changes predictably.
- **B:** Correct. In this case: A fixed schedule is simple to reason about when the data changes predictably.
- **C:** Incorrect for this question. Metric-triggered retraining reacts to actual quality loss. Why the correct answer wins: A fixed schedule is simple to reason about when the data changes predictably.
- **D:** Incorrect for this question. Manual retraining leaves the model stale whenever the trigger is forgotten. Why the correct answer wins: A fixed schedule is simple to reason about when the data changes predictably.

### Question 83 — D

Answer: Retrain when the production metric drops. Metric-triggered retraining reacts to actual quality loss. Local study-map skill 5.4 (Retraining Policy), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Manual retraining leaves the model stale whenever the trigger is forgotten. Why the correct answer wins: Metric-triggered retraining reacts to actual quality loss.
- **B:** Incorrect for this question. Drift-triggered retraining responds to change instead of to the calendar. Why the correct answer wins: Metric-triggered retraining reacts to actual quality loss.
- **C:** Incorrect for this question. A fixed schedule is simple to reason about when the data changes predictably. Why the correct answer wins: Metric-triggered retraining reacts to actual quality loss.
- **D:** Correct. In this case: Metric-triggered retraining reacts to actual quality loss.

### Question 84 — A

Answer: Extend CI/CD into continuous training. Continuous training adds the retrain and validate step to the same pipeline. Local study-map skill 5.5 (CI/CD/CT with Cloud Build), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Continuous training adds the retrain and validate step to the same pipeline.
- **B:** Incorrect for this question. A fixed schedule is simple to reason about when the data changes predictably. Why the correct answer wins: Continuous training adds the retrain and validate step to the same pipeline.
- **C:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: Continuous training adds the retrain and validate step to the same pipeline.
- **D:** Incorrect for this question. An event trigger retrains when data lands instead of on a fixed clock. Why the correct answer wins: Continuous training adds the retrain and validate step to the same pipeline.

### Question 85 — D

Answer: Trigger the pipeline from the arrival of new data. An event trigger retrains when data lands instead of on a fixed clock. Local study-map skill 5.5 (CI/CD/CT with Cloud Build), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Manual retraining leaves the model stale whenever the trigger is forgotten. Why the correct answer wins: An event trigger retrains when data lands instead of on a fixed clock.
- **B:** Incorrect for this question. The scheduler starts the pipeline on the cadence the retraining policy defines. Why the correct answer wins: An event trigger retrains when data lands instead of on a fixed clock.
- **C:** Incorrect for this question. Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance. Why the correct answer wins: An event trigger retrains when data lands instead of on a fixed clock.
- **D:** Correct. In this case: An event trigger retrains when data lands instead of on a fixed clock.

### Question 86 — B

Answer: Add a Cloud Scheduler trigger to the pipeline. The scheduler starts the pipeline on the cadence the retraining policy defines. Local study-map skill 5.5 (CI/CD/CT with Cloud Build), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Metric-triggered retraining reacts to actual quality loss. Why the correct answer wins: The scheduler starts the pipeline on the cadence the retraining policy defines.
- **B:** Correct. In this case: The scheduler starts the pipeline on the cadence the retraining policy defines.
- **C:** Incorrect for this question. An event trigger retrains when data lands instead of on a fixed clock. Why the correct answer wins: The scheduler starts the pipeline on the cadence the retraining policy defines.
- **D:** Incorrect for this question. Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance. Why the correct answer wins: The scheduler starts the pipeline on the cadence the retraining policy defines.

### Question 87 — B

Answer: Use Ray on Agent Platform for the distributed compute. Ray fits a Python-native distributed workload that is not a container-per-step pipeline. Local study-map skill 5.2 (Pipeline Orchestration Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Airflow expresses cross-system dependencies and schedules outside the ML platform. Why the correct answer wins: Ray fits a Python-native distributed workload that is not a container-per-step pipeline.
- **B:** Correct. In this case: Ray fits a Python-native distributed workload that is not a container-per-step pipeline.
- **C:** Incorrect for this question. Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance. Why the correct answer wins: Ray fits a Python-native distributed workload that is not a container-per-step pipeline.
- **D:** Incorrect for this question. Kubeflow pipelines give a container-per-step pipeline that runs on the managed service or on GKE. Why the correct answer wins: Ray fits a Python-native distributed workload that is not a container-per-step pipeline.

### Question 88 — C, E

Answers: Screen the prompts and responses with Model Armor; Constrain the response to a JSON schema. Model Armor detects prompt injection, and a schema stops free text reaching the code. Model Armor detects prompt injection, jailbreak attempts, and unsafe content. A schema stops the model returning free text that downstream code cannot parse. Local study-map skill 6.1 (Secure AI and Prompt Protection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Safety filters block categories of harmful output at the model call. Why the correct answer wins: Model Armor detects prompt injection, and a schema stops free text reaching the code.
- **B:** Incorrect for this question. A system instruction states what the assistant must refuse, though it is not a security control on its own. Why the correct answer wins: Model Armor detects prompt injection, and a schema stops free text reaching the code.
- **C:** Correct. Model Armor detects prompt injection, jailbreak attempts, and unsafe content. In this case: Model Armor detects prompt injection, and a schema stops free text reaching the code.
- **D:** Incorrect for this question. A regex removes a known identifier pattern before the prompt leaves the service. Why the correct answer wins: Model Armor detects prompt injection, and a schema stops free text reaching the code.
- **E:** Correct. A schema stops the model returning free text that downstream code cannot parse. In this case: Model Armor detects prompt injection, and a schema stops free text reaching the code.

### Question 89 — C

Answer: Redact the pattern-matchable fields with a regex. A regex removes a known identifier pattern before the prompt leaves the service. Local study-map skill 6.1 (Secure AI and Prompt Protection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A schema stops the model returning free text that downstream code cannot parse. Why the correct answer wins: A regex removes a known identifier pattern before the prompt leaves the service.
- **B:** Incorrect for this question. Model Armor detects prompt injection, jailbreak attempts, and unsafe content. Why the correct answer wins: A regex removes a known identifier pattern before the prompt leaves the service.
- **C:** Correct. In this case: A regex removes a known identifier pattern before the prompt leaves the service.
- **D:** Incorrect for this question. A system instruction states what the assistant must refuse, though it is not a security control on its own. Why the correct answer wins: A regex removes a known identifier pattern before the prompt leaves the service.

### Question 90 — C

Answer: Put the boundary in the system instruction. A system instruction states what the assistant must refuse. Local study-map skill 6.1 (Secure AI and Prompt Protection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Model Armor detects prompt injection, jailbreak attempts, and unsafe content. Why the correct answer wins: A system instruction states what the assistant must refuse.
- **B:** Incorrect for this question. Safety filters block categories of harmful output at the model call. Why the correct answer wins: A system instruction states what the assistant must refuse.
- **C:** Correct. In this case: A system instruction states what the assistant must refuse.
- **D:** Incorrect for this question. A schema stops the model returning free text that downstream code cannot parse. Why the correct answer wins: A system instruction states what the assistant must refuse.

### Question 91 — C

Answer: Document the dataset with a data card. The card records provenance, intended use, and known gaps for the dataset. Local study-map skill 6.2 (Responsible AI and Bias), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A sliced metric shows a gap that the aggregate metric hides. Why the correct answer wins: The card records provenance, intended use, and known gaps for the dataset.
- **B:** Incorrect for this question. The card states where the model may be used and where it must not. Why the correct answer wins: The card records provenance, intended use, and known gaps for the dataset.
- **C:** Correct. In this case: The card records provenance, intended use, and known gaps for the dataset.
- **D:** Incorrect for this question. A per-group outcome rate is the first evidence of disparate impact. Why the correct answer wins: The card records provenance, intended use, and known gaps for the dataset.

### Question 92 — B

Answer: Publish a model card with the intended use and limits. The card states where the model may be used and where it must not. Local study-map skill 6.2 (Responsible AI and Bias), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A sliced metric shows a gap that the aggregate metric hides. Why the correct answer wins: The card states where the model may be used and where it must not.
- **B:** Correct. In this case: The card states where the model may be used and where it must not.
- **C:** Incorrect for this question. A per-group outcome rate is the first evidence of disparate impact. Why the correct answer wins: The card states where the model may be used and where it must not.
- **D:** Incorrect for this question. The card records provenance, intended use, and known gaps for the dataset. Why the correct answer wins: The card states where the model may be used and where it must not.

### Question 93 — D

Answer: Explain with Shapley values. Shapley values attribute a prediction to its features against a consistent baseline. Local study-map skill 6.3 (Explainability), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Integrated gradients attributes an image prediction to the pixels that moved it. Why the correct answer wins: Shapley values attribute a prediction to its features against a consistent baseline.
- **B:** Incorrect for this question. Attribution shows which inputs drove the decision in the case the reviewer is examining. Why the correct answer wins: Shapley values attribute a prediction to its features against a consistent baseline.
- **C:** Incorrect for this question. Sampled Shapley explains individual online predictions with a bounded compute cost. Why the correct answer wins: Shapley values attribute a prediction to its features against a consistent baseline.
- **D:** Correct. In this case: Shapley values attribute a prediction to its features against a consistent baseline.

### Question 94 — D

Answer: Choose an inherently interpretable model. A linear or tree model can be read directly when regulation demands an explanation by construction. Local study-map skill 6.3 (Explainability), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Attribution shows which inputs drove the decision in the case the reviewer is examining. Why the correct answer wins: A linear or tree model can be read directly when regulation demands an explanation by construction.
- **B:** Incorrect for this question. Sampled Shapley explains individual online predictions with a bounded compute cost. Why the correct answer wins: A linear or tree model can be read directly when regulation demands an explanation by construction.
- **C:** Incorrect for this question. Shapley values attribute a prediction to its features with a consistent baseline. Why the correct answer wins: A linear or tree model can be read directly when regulation demands an explanation by construction.
- **D:** Correct. In this case: A linear or tree model can be read directly when regulation demands an explanation by construction.

### Question 95 — C

Answer: Enable Model Monitoring on the endpoint. Model Monitoring compares live traffic with the training baseline. Local study-map skill 6.4 (Model Monitoring Configuration), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. An alert with no owner is a dashboard nobody reads. Why the correct answer wins: Model Monitoring compares live traffic with the training baseline.
- **B:** Incorrect for this question. The threshold expresses how much drift the business can absorb before someone acts. Why the correct answer wins: Model Monitoring compares live traffic with the training baseline.
- **C:** Correct. In this case: Model Monitoring compares live traffic with the training baseline.
- **D:** Incorrect for this question. A percentile latency per version shows a regression that an average hides. Why the correct answer wins: Model Monitoring compares live traffic with the training baseline.

### Question 96 — B

Answer: Set the monitoring threshold from the acceptable error budget. The threshold expresses how much drift the business can absorb. Local study-map skill 6.4 (Model Monitoring Configuration), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Continuous sampling catches quality regressions that drift metrics cannot see. Why the correct answer wins: The threshold expresses how much drift the business can absorb.
- **B:** Correct. In this case: The threshold expresses how much drift the business can absorb.
- **C:** Incorrect for this question. Redacted logs make a bad answer diagnosable without storing sensitive text. Why the correct answer wins: The threshold expresses how much drift the business can absorb.
- **D:** Incorrect for this question. An alert with no owner is a dashboard nobody reads. Why the correct answer wins: The threshold expresses how much drift the business can absorb.

### Question 97 — A, C

Answers: Watch for concept drift; Join the delayed ground truth back to the predictions. Concept drift changes the feature-target relationship, and the delayed ground truth makes it measurable. Concept drift is a change in the relationship between the features and the target. Without the labelled outcome, quality can only be inferred from the inputs and outputs. Local study-map skill 6.5 (Skew and Drift Types), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. Concept drift is a change in the relationship between the features and the target. In this case: Concept drift changes the feature-target relationship, and the delayed ground truth makes it measurable.
- **B:** Incorrect for this question. A shift in the output distribution is often the first visible symptom. Why the correct answer wins: Concept drift changes the feature-target relationship, and the delayed ground truth makes it measurable.
- **C:** Correct. Without the labelled outcome, quality can only be inferred from the inputs and outputs. In this case: Concept drift changes the feature-target relationship, and the delayed ground truth makes it measurable.
- **D:** Incorrect for this question. Attribution drift is a change in which features drive the prediction. Why the correct answer wins: Concept drift changes the feature-target relationship, and the delayed ground truth makes it measurable.
- **E:** Incorrect for this question. Data drift is a change in the input distribution after the model shipped. Why the correct answer wins: Concept drift changes the feature-target relationship, and the delayed ground truth makes it measurable.

### Question 98 — A

Answer: Watch for training-serving skew. Skew compares the live feature distribution with the training distribution. Local study-map skill 6.5 (Skew and Drift Types), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Skew compares the live feature distribution with the training distribution.
- **B:** Incorrect for this question. Data drift is a change in the input distribution after the model shipped. Why the correct answer wins: Skew compares the live feature distribution with the training distribution.
- **C:** Incorrect for this question. Concept drift is a change in the relationship between the features and the target. Why the correct answer wins: Skew compares the live feature distribution with the training distribution.
- **D:** Incorrect for this question. A shift in the output distribution is often the first visible symptom. Why the correct answer wins: Skew compares the live feature distribution with the training distribution.

### Question 99 — B

Answer: Track tokens and cost per request. Token accounting attributes generative cost to the feature that caused it. Local study-map skill 6.6 (Generative AI Monitoring), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Continuous sampling catches quality regressions that drift metrics cannot see. Why the correct answer wins: Token accounting attributes generative cost to the feature that caused it.
- **B:** Correct. In this case: Token accounting attributes generative cost to the feature that caused it.
- **C:** Incorrect for this question. Model Monitoring compares live traffic with the training baseline and reports skew and drift. Why the correct answer wins: Token accounting attributes generative cost to the feature that caused it.
- **D:** Incorrect for this question. A percentile latency per version shows a regression that an average hides. Why the correct answer wins: Token accounting attributes generative cost to the feature that caused it.

### Question 100 — A

Answer: Score a sample of live answers with the evaluation rubric. Continuous sampling catches quality regressions that drift metrics cannot see. Local study-map skill 6.6 (Generative AI Monitoring), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Continuous sampling catches quality regressions that drift metrics cannot see.
- **B:** Incorrect for this question. Model Monitoring compares live traffic with the training baseline and reports skew and drift. Why the correct answer wins: Continuous sampling catches quality regressions that drift metrics cannot see.
- **C:** Incorrect for this question. A percentile latency per version shows a regression that an average hides. Why the correct answer wins: Continuous sampling catches quality regressions that drift metrics cannot see.
- **D:** Incorrect for this question. Token accounting attributes generative cost to the feature that caused it. Why the correct answer wins: Continuous sampling catches quality regressions that drift metrics cannot see.
