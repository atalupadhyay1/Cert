# Google Cloud Professional Machine Learning Engineer — Full-Length Mock Exam 5

Professional Machine Learning Engineer · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study or drag-and-drop item is reproduced. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Architecting low-code AI solutions (Low-Code AI and Foundational Models)

### 1. A research group wants to discover natural groupings in survey responses. What should be built?

- A. Create a BigQuery ML ARIMA_PLUS time series model
- B. Create a BigQuery ML logistic regression model
- C. Create a BigQuery ML k-means model
- D. Create a BigQuery ML linear regression model

### 2. A weekly forecast must carry a prediction interval, and the planners must see what drives it. Which two choices apply? Select two.

- A. Import the TensorFlow model into BigQuery ML
- B. Create a BigQuery ML ARIMA_PLUS time series model
- C. Summarise the model with ML.GLOBAL_EXPLAIN
- D. Store the predictions in a nested JSON column
- E. Create a BigQuery ML k-means model

### 3. A model must not depend on the caller preparing the features correctly. What should be used?

- A. Import the TensorFlow model into BigQuery ML
- B. Score the rows with ML.PREDICT
- C. Inspect the metrics with ML.EVALUATE
- D. Declare the feature transformations in the TRANSFORM clause

### 4. A batch of new rows must be scored from SQL each morning. What should be used?

- A. Inspect the metrics with ML.EVALUATE
- B. Read the contribution of each feature with ML.EXPLAIN_PREDICT
- C. Score the rows with ML.PREDICT
- D. Summarise the model with ML.GLOBAL_EXPLAIN

### 5. Six AutoML runs must fit inside one monthly budget. What should be configured?

- A. Let AutoML choose the data split
- B. Set a training budget in node hours
- C. Define a manual split column with train, validation, and test
- D. Export the AutoML model as an artifact

### 6. The last quarter must never be trained on during a forecasting AutoML run. What should be done?

- A. Define a manual split column with train, validation, and test
- B. Set a training budget in node hours
- C. Let AutoML choose the data split
- D. Export the AutoML model as an artifact

### 7. Labelled support answers already sit in BigQuery and the tone must match. What should be done?

- A. Start with prompt and context engineering
- B. Fine-tune a Gemini model from BigQuery
- C. Fine-tune with a parameter-efficient adapter
- D. Create a BigQuery ML remote model over Gemini

### 8. A team must compare a first-party model with two open-weight options. Where should it look?

- A. Select the model from Model Garden
- B. Generate the images with Imagen
- C. Choose the smaller Gemini model for latency and cost
- D. Embed the documents with the text embedding model

### 9. Recorded calls must become text with industry vocabulary recognised. What should be used?

- A. Use the Video Intelligence API
- B. Use the Speech-to-Text API
- C. Use the Translation API
- D. Use Document AI with a specialised processor

### 10. Handwritten delivery notes must be read into structured fields with layout awareness. What should be used?

- A. Use Document AI with a specialised processor
- B. Use the Vision API
- C. Use the Speech-to-Text API
- D. Use the Natural Language API

### 11. A long system prompt is resent on every call and answers run to several paragraphs. Which two changes cut cost? Select two.

- A. Cache the long shared context
- B. Stream the response tokens to the client
- C. Choose the larger Gemini model for quality
- D. Constrain the output with a schema and a token limit
- E. Send the offline work through the batch API

### 12. A single-country user base reports cross-region latency on every call. What should be used?

- A. Fall back to a smaller model when the primary is throttled
- B. Request a quota increase for the model
- C. Call the model in the region that serves the users
- D. Stream the response tokens to the client

---

## Domain 2 — Collaborating within and across teams to manage data and models (Data, Features, Notebooks, and Experiments)

### 13. A team has 60 existing PySpark jobs and wants to reuse them unchanged. What should be used?

- A. Preprocess with a Dataflow pipeline
- B. Preprocess with Spark on Dataproc
- C. Preprocess in BigQuery with SQL
- D. Preprocess in memory with pandas

### 14. A model scores 0.99 offline and collapses in production, and one customer spans splits. Which two fixes apply? Select two.

- A. Split the data by time rather than at random
- B. Split by entity so one customer never spans train and test
- C. Drop the identifier columns before the training dataset is written
- D. Normalise the numeric feature before training
- E. Remove the post-outcome column from the features

### 15. A data-governance lead must find unclassified sensitive tables across projects. What should be used?

- A. Preprocess in BigQuery with SQL
- B. Preprocess with a Dataflow pipeline
- C. Preprocess with Spark on Dataproc
- D. Catalog and profile the data with Dataplex

### 16. Training and serving must share one feature definition and version it. What should be used?

- A. Enable feature monitoring on the feature group
- B. Serve the feature from the online store
- C. Register the feature in Agent Platform Feature Store
- D. Bucketize the continuous feature

### 17. A continuous feature has a clearly non-linear effect on the target. What should be applied?

- A. Normalise the numeric feature before training
- B. Bucketize the continuous feature
- C. Add a crossed feature for the interacting pair
- D. Register the feature in Agent Platform Feature Store

### 18. A dataset must keep phone numbers usable in tests but not readable. What should be used?

- A. Hash the identifiers with a salted key before training
- B. Restrict the raw bucket to a privileged service account
- C. Drop the identifier columns before the training dataset is written
- D. De-identify the fields with Sensitive Data Protection

### 19. A notes field contains free text that no feature needs. What is the safest action?

- A. Restrict the raw bucket to a privileged service account
- B. Hash the identifiers with a salted key before training
- C. De-identify the fields with Sensitive Data Protection
- D. Drop the identifier columns before the training dataset is written

### 20. A runtime must boot an image that already carries the team's pinned libraries. What should be configured?

- A. Attach the runtime to the shared VPC subnet
- B. Create the runtime with no public IP
- C. Set an idle shutdown schedule
- D. Pin the runtime to a custom container image

### 21. A runtime must have no public address at all. What should be configured?

- A. Set an idle shutdown schedule
- B. Create the runtime with no public IP
- C. Attach the runtime to the shared VPC subnet
- D. Pin the runtime to a custom container image

### 22. A lead must compare loss curves and hyperparameters across runs. What should be used?

- A. Set the random seed in the training code
- B. Enable step caching
- C. Track artifacts and lineage in ML Metadata
- D. Log the run to Agent Platform Experiments

### 23. Several model families must be ranked without touching the test set. What should be done?

- A. Log the run to Agent Platform Experiments
- B. Set the random seed in the training code
- C. Track artifacts and lineage in ML Metadata
- D. Compare the runs on the validation metric

### 24. A first pipeline must be scheduled with lineage and must not be bespoke. Which two choices fit? Select two.

- A. Start from a Google-provided pipeline template
- B. Use Ray on Agent Platform for the distributed compute
- C. Orchestrate the steps in Agent Platform Pipelines
- D. Orchestrate with Managed Service for Apache Airflow
- E. Log the run to Agent Platform Experiments

### 25. A team only needs to track runs and compare metrics, not orchestrate steps. What should be used?

- A. Log the run to Agent Platform Experiments
- B. Enable step caching
- C. Express the workflow as a Kubeflow pipeline
- D. Orchestrate the steps in Agent Platform Pipelines

### 26. Five thousand generated answers must be scored, and the scorer must be trustworthy. Which two practices apply? Select two.

- A. Measure the safety metrics on a fixed prompt set
- B. Sample the answers for expert human review
- C. Measure groundedness against the retrieved context
- D. Score the answers with an LLM-as-a-judge rubric
- E. Report precision-recall AUC for the rare class

### 27. A forecast must be reported to planners as a percentage error. What should be used?

- A. Report MAPE when the error must be read as a percentage
- B. Report ROC AUC
- C. Report RMSE for the regression target
- D. Report precision-recall AUC for the rare class

### 28. A dataset version and code commit must be linked to the model artifact. What should be recorded?

- A. Track artifacts and lineage in ML Metadata
- B. Log the run to Agent Platform Experiments
- C. Register the model in Agent Platform Model Registry
- D. Push the serving image to Artifact Registry

---

## Domain 3 — Scaling prototypes into ML models (Training at Scale and Model Choice)

### 29. The regulator wants per-feature attention weights from a tabular model. Which algorithm fits?

- A. Use TabNet as the custom training algorithm
- B. Choose a deep neural network
- C. Choose a foundation model
- D. Choose a classical time series model

### 30. Thirty store series share strong seasonality and few covariates. What model type fits?

- A. Choose a foundation model
- B. Use TabNet as the custom training algorithm
- C. Choose a classical time series model
- D. Choose a deep neural network

### 31. A research team needs a custom loss and a custom evaluation loop. What should be used?

- A. Use TabNet as the custom training algorithm
- B. Train with Agent Platform AutoML
- C. Train a custom model on Agent Platform
- D. Build the model in BigQuery ML

### 32. A team has labelled data, no ML engineer, and a six-week deadline. What should be used?

- A. Train with Agent Platform AutoML
- B. Build the model in BigQuery ML
- C. Train a custom model on Agent Platform
- D. Use TabNet as the custom training algorithm

### 33. A new model must be scored on live traffic invisibly, then shown to a small share. Which two strategies apply? Select two.

- A. Run the new model in shadow mode
- B. Roll out a canary with a small traffic share
- C. Split traffic between two models in an A/B test
- D. Deploy blue/green with an instant switch
- E. Replace the model version in place

### 34. A candidate ranker must score real traffic while every user still sees the incumbent's order. What should be done?

- A. Run the new model in shadow mode
- B. Roll out a canary with a small traffic share
- C. Split traffic between two models in an A/B test
- D. Replace the model version in place

### 35. Per-row feature contributions must be exported alongside each score in SQL. What should be used?

- A. Summarise the model with ML.GLOBAL_EXPLAIN
- B. Use sampled Shapley on the endpoint
- C. Read the contribution of each feature with ML.EXPLAIN_PREDICT
- D. Explain with Shapley values

### 36. A regulation demands an explanation by construction. What should be chosen?

- A. Explain with Shapley values
- B. Use sampled Shapley on the endpoint
- C. Choose an inherently interpretable model
- D. Report the feature attributions to the reviewer

### 37. A tabular training set is read column-wise by several frameworks. What format fits?

- A. Stream the new records through Dataflow into the training store
- B. Write the training data as Parquet in Cloud Storage
- C. Read the training data directly from BigQuery
- D. Write the training data as TFRecord shards in Cloud Storage

### 38. Training must read the latest labellings with no copy step. What should be used?

- A. Write the training data as Parquet in Cloud Storage
- B. Write the training data as TFRecord shards in Cloud Storage
- C. Read the training data directly from BigQuery
- D. Stream the new records through Dataflow into the training store

### 39. A malformed batch must be quarantined rather than failing the run. What should be added?

- A. Stream the new records through Dataflow into the training store
- B. Write the training data as TFRecord shards in Cloud Storage
- C. Validate the schema and quarantine rejected rows
- D. Deduplicate on the event key in the ingestion step

### 40. An event feed must be continuously folded into the training set. What should be used?

- A. Stream the new records through Dataflow into the training store
- B. Validate the schema and quarantine rejected rows
- C. Deduplicate on the event key in the ingestion step
- D. Read the training data directly from BigQuery

### 41. A short XGBoost script must run remotely with no Dockerfile. What should be used?

- A. Package the trainer as a Python package
- B. Run a custom container on Agent Platform
- C. Use a prebuilt serving container
- D. Export the AutoML model as an artifact

### 42. A pinned CUDA build and a private wheel index are both required at training time. What should be used?

- A. Train with Agent Platform AutoML
- B. Use a prebuilt serving container
- C. Run a custom container on Agent Platform
- D. Package the trainer as a Python package

### 43. Memory is exhausted a few hundred steps into training. What should be tried first?

- A. Request accelerator quota for the region
- B. Reduce the per-replica batch size
- C. Lower the learning rate
- D. Pin the framework version in the container

### 44. A TPU job fails immediately in a region with no TPU quota. What is the cause?

- A. Grant the training service account access to the bucket
- B. Lower the learning rate
- C. Pin the framework version in the container
- D. Request accelerator quota for the region

### 45. Many configurations must be explored inside a fixed cost envelope. Which two choices apply? Select two.

- A. Cap the search with a trial count and a parallel budget
- B. Set the random seed in the training code
- C. Enable early stopping of poor trials
- D. Choose Bayesian optimisation for the search
- E. Run a hyperparameter tuning job

### 46. The search maximises accuracy while the contract pays on margin. What must change?

- A. Choose Bayesian optimisation for the search
- B. Cap the search with a trial count and a parallel budget
- C. Report the business metric from the trainer
- D. Run a hyperparameter tuning job

### 47. A new language and writing system must be learned and a large labelled corpus exists. What should be done?

- A. Ground the prompt with retrieval instead of fine-tuning
- B. Start with prompt and context engineering
- C. Fine-tune the full model
- D. Fine-tune with a parameter-efficient adapter

### 48. A very large transformer must train synchronously across a coupled fabric. What should be used?

- A. Train on a TPU slice
- B. Serve on CPU only
- C. Serve on L4 GPUs
- D. Train on A100 GPUs

### 49. A model fits on one GPU and must use sixteen of them efficiently. Which two choices apply? Select two.

- A. Configure the job as multi-worker with a chief
- B. Train on A100 GPUs
- C. Scale the batch size with the worker count
- D. Use data parallelism
- E. Use model parallelism

---

## Domain 4 — Serving and scaling models (Serving, Packaging, and Scaling Endpoints)

### 50. A support console needs one prediction per click. What should be used?

- A. Batch the requests inside the client
- B. Send the events to a streaming prediction path
- C. Deploy to an online endpoint
- D. Run batch prediction

### 51. One consumer reads a file each night and another needs a score per event. Which two paths apply? Select two.

- A. Batch the requests inside the client
- B. Deploy to an online endpoint
- C. Run batch prediction
- D. Send the events to a streaming prediction path
- E. Attach a GPU to the serving replica

### 52. A mobile client issues a call per screen and the round trip dominates latency. What should the client do?

- A. Run batch prediction
- B. Batch the requests inside the client
- C. Raise the concurrency per replica
- D. Enable autoscaling on the endpoint

### 53. A scikit-learn model must go live without bespoke request handling. What should be used?

- A. Push the serving image to Artifact Registry
- B. Attach a GPU to the serving replica
- C. Add a custom prediction routine to the container
- D. Use a prebuilt serving container

### 54. Custom postprocessing must run inside the serving container. What should be added?

- A. Deploy the version and move the alias
- B. Push the serving image to Artifact Registry
- C. Add a custom prediction routine to the container
- D. Use a prebuilt serving container

### 55. Traffic must move between two versions without touching the artifacts. What should be used?

- A. Split traffic between two deployed versions
- B. Register the model in Agent Platform Model Registry
- C. Deploy the version and move the alias
- D. Deploy blue/green with an instant switch

### 56. Reviewers need the metrics and lineage attached to each shipped model. What should be used?

- A. Log the run to Agent Platform Experiments
- B. Push the serving image to Artifact Registry
- C. Track artifacts and lineage in ML Metadata
- D. Register the model in Agent Platform Model Registry

### 57. Two models must be compared on equal populations, and the old one must be restorable at once. Which two strategies apply? Select two.

- A. Replace the model version in place
- B. Deploy blue/green with an instant switch
- C. Split traffic between two models in an A/B test
- D. Roll out a canary with a small traffic share
- E. Run the new model in shadow mode

### 58. A risky model must reach one per cent of traffic and hold there. What strategy is described?

- A. Replace the model version in place
- B. Roll out a canary with a small traffic share
- C. Run the new model in shadow mode
- D. Split traffic between two models in an A/B test

### 59. A feature must be looked up at request time instead of recomputed from raw events. What should be used?

- A. Register the feature in Agent Platform Feature Store
- B. Deploy the version and move the alias
- C. Enable step caching
- D. Share one transformation library between training and serving

### 60. Two codebases compute the same feature and have diverged. What should be done?

- A. Register the feature in Agent Platform Feature Store
- B. Add an explicit data validation step
- C. Keep the preprocessing inside the exported model
- D. Share one transformation library between training and serving

### 61. A model must be reachable only from inside the VPC. What should be deployed?

- A. Use a shared public endpoint
- B. Deploy with a private endpoint only
- C. Use a dedicated endpoint
- D. Attach a GPU to the serving replica

### 62. A demo must be callable today without reserving capacity. What should be used?

- A. Use a shared public endpoint
- B. Enable autoscaling on the endpoint
- C. Deploy with a private endpoint only
- D. Use a dedicated endpoint

### 63. A 4 GB model must serve cheaply at 50 ms. What should be used?

- A. Serve on L4 GPUs
- B. Train on a TPU slice
- C. Train on A100 GPUs
- D. Serve on CPU only

### 64. A vision endpoint misses its latency target on CPU. What should be used?

- A. Attach a GPU to the serving replica
- B. Deploy to an Edge TPU device
- C. Raise the concurrency per replica
- D. Serve on CPU only

### 65. Traffic must be absorbed automatically but must not exceed an approved budget. Which two settings apply? Select two.

- A. Enable autoscaling on the endpoint
- B. Set a minimum replica count
- C. Raise the concurrency per replica
- D. Batch the requests inside the client
- E. Raise the maximum replica count

### 66. A replica sits idle while three calls queue behind one. What should be raised?

- A. Raise the concurrency per replica
- B. Raise the maximum replica count
- C. Batch the requests inside the client
- D. Set a minimum replica count

### 67. The first request after a quiet night takes several seconds. What should be set?

- A. Raise the maximum replica count
- B. Batch the requests inside the client
- C. Set a minimum replica count
- D. Raise the concurrency per replica

### 68. An endpoint must cut cost per request and still meet a tight latency target. Which two changes apply? Select two.

- A. Raise the concurrency per replica
- B. Attach a GPU to the serving replica
- C. Raise the maximum replica count
- D. Batch the requests inside the client
- E. Set a minimum replica count

### 69. An endpoint must return attributions for each prediction. What should be configured?

- A. Push the serving image to Artifact Registry
- B. Batch the requests inside the client
- C. Deploy the version and move the alias
- D. Configure explanation metadata for the endpoint

---

## Domain 5 — Automating and orchestrating ML pipelines (Pipelines, Retraining, and CI/CD/CT)

### 70. A pipeline must reject a batch whose schema changed before training. What should be added?

- A. Gate the deployment on a model evaluation threshold
- B. Add an explicit data validation step
- C. Enable step caching
- D. Validate the schema and quarantine rejected rows

### 71. A model must beat the incumbent before it is promoted. What should be added?

- A. Gate the deployment on a model evaluation threshold
- B. Keep the test set out of every tuning decision
- C. Add an explicit data validation step
- D. Enable step caching

### 72. The holdout has been reused for tuning, and the operating point must be fixed. Which two practices apply? Select two.

- A. Enable step caching
- B. Report ROC AUC
- C. Choose the threshold from the cost of each error type
- D. Report MAPE when the error must be read as a percentage
- E. Keep the test set out of every tuning decision

### 73. Steps must be cached containers with per-artifact lineage. What should be used?

- A. Orchestrate with Managed Service for Apache Airflow
- B. Express the workflow as a Kubeflow pipeline
- C. Use Ray on Agent Platform for the distributed compute
- D. Orchestrate the steps in Agent Platform Pipelines

### 74. A nightly chain must reconcile a partner's SFTP upload with the warehouse before a deploy. What should orchestrate it?

- A. Trigger the build and deploy from Cloud Build
- B. Orchestrate the steps in Agent Platform Pipelines
- C. Use Ray on Agent Platform for the distributed compute
- D. Orchestrate with Managed Service for Apache Airflow

### 75. A Python driver must fan work out to a cluster of remote workers. What should be used?

- A. Express the workflow as a Kubeflow pipeline
- B. Use Ray on Agent Platform for the distributed compute
- C. Orchestrate with Managed Service for Apache Airflow
- D. Orchestrate the steps in Agent Platform Pipelines

### 76. A commit must rebuild the image and deploy it to staging under review. What should be used?

- A. Add a Cloud Scheduler trigger to the pipeline
- B. Trigger the build and deploy from Cloud Build
- C. Orchestrate the steps in Agent Platform Pipelines
- D. Enable step caching

### 77. Most steps produce identical artifacts on every scheduled run. What should be enabled?

- A. Retrain when drift crosses the threshold
- B. Enable step caching
- C. Add an explicit data validation step
- D. Gate the deployment on a model evaluation threshold

### 78. Preprocessing must travel with the artifact, and a backfill must rebuild history. Which two choices apply? Select two.

- A. Deduplicate on the event key in the ingestion step
- B. Keep the preprocessing inside the exported model
- C. Register the model in Agent Platform Model Registry
- D. Read the historical features from the offline store
- E. Serve the feature from the online store

### 79. One ratio is computed by the training job and again by the endpoint, and the two disagree. What should be done?

- A. Keep the preprocessing inside the exported model
- B. Share one transformation library between training and serving
- C. Enable step caching
- D. Register the feature in Agent Platform Feature Store

### 80. A renamed column must be quarantined instead of reaching the trainer. What should be added?

- A. Share one transformation library between training and serving
- B. Enable step caching
- C. Deduplicate on the event key in the ingestion step
- D. Validate the schema and quarantine rejected rows

### 81. Input distributions move without warning and the calendar is too slow. What policy fits?

- A. Retrain when drift crosses the threshold
- B. Retrain when the production metric drops
- C. Retrain on a fixed schedule
- D. Retrain only on a manual request

### 82. Two models went stale because nobody remembered to trigger a retrain. What policy fits?

- A. Retrain when drift crosses the threshold
- B. Retrain when the production metric drops
- C. Retrain on a fixed schedule
- D. Retrain only on a manual request

### 83. Chargeback volume climbed while every offline score stayed flat. What policy fits?

- A. Retrain on a fixed schedule
- B. Retrain when drift crosses the threshold
- C. Retrain only on a manual request
- D. Retrain when the production metric drops

### 84. Retrain and promotion must be automatic in one path. What should be adopted?

- A. Enable step caching
- B. Extend CI/CD into continuous training
- C. Trigger the pipeline from the arrival of new data
- D. Retrain only on a manual request

### 85. A storage notification must kick off retraining with no human in the loop. What should be used?

- A. Retrain only on a manual request
- B. Add a Cloud Scheduler trigger to the pipeline
- C. Trigger the build and deploy from Cloud Build
- D. Trigger the pipeline from the arrival of new data

### 86. Promotion must depend on beating the incumbent rather than on a calendar date. What should the pipeline add?

- A. Retrain when drift crosses the threshold
- B. Add an explicit data validation step
- C. Enable step caching
- D. Gate the deployment on a model evaluation threshold

### 87. An auditor asks who built the released image and what went into it. What should be used?

- A. Add a Cloud Scheduler trigger to the pipeline
- B. Retrain only on a manual request
- C. Trigger the build and deploy from Cloud Build
- D. Enable step caching

---

## Domain 6 — Monitoring AI solutions (Responsible AI, Monitoring, and Drift)

### 88. Account numbers must never reach the model, and the reply must be parseable. Which two controls apply? Select two.

- A. Screen the prompts and responses with Model Armor
- B. Constrain the response to a JSON schema
- C. Redact the pattern-matchable fields with a regex
- D. Configure the model safety filters
- E. Put the boundary in the system instruction

### 89. An assistant is being probed with injected instructions. What should be added?

- A. Constrain the response to a JSON schema
- B. Put the boundary in the system instruction
- C. Screen the prompts and responses with Model Armor
- D. Configure the model safety filters

### 90. A clinical assistant must refuse questions outside its approved scope. What should be configured?

- A. Constrain the response to a JSON schema
- B. Put the boundary in the system instruction
- C. Screen the prompts and responses with Model Armor
- D. Configure the model safety filters

### 91. A pricing model must be watched for disparate impact in production. What should be enabled?

- A. Publish a model card with the intended use and limits
- B. Slice the evaluation metrics by the sensitive attribute
- C. Document the dataset with a data card
- D. Monitor the outcome rate across the protected groups

### 92. A dataset's provenance and known gaps must be documented. What should be produced?

- A. Document the dataset with a data card
- B. Monitor the outcome rate across the protected groups
- C. Publish a model card with the intended use and limits
- D. Slice the evaluation metrics by the sensitive attribute

### 93. A support agent needs the drivers of one live score inside the chat window. What should be used?

- A. Explain with Shapley values
- B. Summarise the model with ML.GLOBAL_EXPLAIN
- C. Use sampled Shapley on the endpoint
- D. Use integrated gradients for the image model

### 94. A reviewer must see which inputs drove one specific decision. What should be shown?

- A. Publish a model card with the intended use and limits
- B. Report the feature attributions to the reviewer
- C. Choose an inherently interpretable model
- D. Summarise the model with ML.GLOBAL_EXPLAIN

### 95. Alerts fire nightly and the team has muted the channel. What should be revisited?

- A. Route the monitoring alert to the owning team
- B. Set the monitoring threshold from the acceptable error budget
- C. Score a sample of live answers with the evaluation rubric
- D. Track p95 latency per model version

### 96. A released model must be checked against the data profile it learned from. What should be enabled?

- A. Enable Model Monitoring on the endpoint
- B. Track p95 latency per model version
- C. Route the monitoring alert to the owning team
- D. Log the prompt and response with redaction

### 97. The inputs look stable but different features now drive the score, and accuracy fell. Which two signals explain it? Select two.

- A. Join the delayed ground truth back to the predictions
- B. Watch for feature attribution drift
- C. Watch for concept drift
- D. Watch the prediction distribution
- E. Watch for data drift

### 98. The live input distribution has moved away from the training set. What is this called?

- A. Join the delayed ground truth back to the predictions
- B. Watch for data drift
- C. Watch for training-serving skew
- D. Watch for concept drift

### 99. A generative feature's cost tripled after a prompt change with flat traffic. What should be tracked?

- A. Enable Model Monitoring on the endpoint
- B. Track p95 latency per model version
- C. Score a sample of live answers with the evaluation rubric
- D. Track tokens and cost per request

### 100. The monthly audit must explain a sample of historic decisions after the fact. What should be used?

- A. Report the feature attributions to the reviewer
- B. Use sampled Shapley on the endpoint
- C. Explain with Shapley values
- D. Use integrated gradients for the image model

---

## Answer key and explanations

### Question 1 — C

Answer: Create a BigQuery ML k-means model. K-means segments rows into unsupervised clusters without a labelled target. Local study-map skill 1.1 (BigQuery ML Model Building), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. ARIMA_PLUS models seasonality and trend and returns a forecast interval per period. Why the correct answer wins: K-means segments rows into unsupervised clusters without a labelled target.
- **B:** Incorrect for this question. Logistic regression predicts a binary outcome and trains inside BigQuery with SQL. Why the correct answer wins: K-means segments rows into unsupervised clusters without a labelled target.
- **C:** Correct. In this case: K-means segments rows into unsupervised clusters without a labelled target.
- **D:** Incorrect for this question. Linear regression predicts a continuous value such as revenue or demand. Why the correct answer wins: K-means segments rows into unsupervised clusters without a labelled target.

### Question 2 — B, C

Answers: Create a BigQuery ML ARIMA_PLUS time series model; Summarise the model with ML.GLOBAL_EXPLAIN. ARIMA_PLUS returns an interval per period, and ML.GLOBAL_EXPLAIN reports the drivers. ARIMA_PLUS models seasonality and trend and returns a forecast interval per period. ML.GLOBAL_EXPLAIN ranks the features that matter most across the whole model. Local study-map skill 1.1 (BigQuery ML Model Building), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Importing brings an already-trained model into BigQuery so SQL can score it. Why the correct answer wins: ARIMA_PLUS returns an interval per period, and ML.GLOBAL_EXPLAIN reports the drivers.
- **B:** Correct. ARIMA_PLUS models seasonality and trend and returns a forecast interval per period. In this case: ARIMA_PLUS returns an interval per period, and ML.GLOBAL_EXPLAIN reports the drivers.
- **C:** Correct. ML.GLOBAL_EXPLAIN ranks the features that matter most across the whole model. In this case: ARIMA_PLUS returns an interval per period, and ML.GLOBAL_EXPLAIN reports the drivers.
- **D:** Incorrect for this question. A nested column keeps per-row structured output such as labels and scores together. Why the correct answer wins: ARIMA_PLUS returns an interval per period, and ML.GLOBAL_EXPLAIN reports the drivers.
- **E:** Incorrect for this question. K-means segments rows into unsupervised clusters without a labelled target. Why the correct answer wins: ARIMA_PLUS returns an interval per period, and ML.GLOBAL_EXPLAIN reports the drivers.

### Question 3 — D

Answer: Declare the feature transformations in the TRANSFORM clause. TRANSFORM keeps preprocessing inside the model. Local study-map skill 1.2 (BigQuery ML Feature Engineering and Prediction), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Importing brings an already-trained model into BigQuery so SQL can score it. Why the correct answer wins: TRANSFORM keeps preprocessing inside the model.
- **B:** Incorrect for this question. ML.PREDICT applies a trained model and returns the label and its probability. Why the correct answer wins: TRANSFORM keeps preprocessing inside the model.
- **C:** Incorrect for this question. ML.EVALUATE returns the model metrics against a labelled dataset. Why the correct answer wins: TRANSFORM keeps preprocessing inside the model.
- **D:** Correct. In this case: TRANSFORM keeps preprocessing inside the model.

### Question 4 — C

Answer: Score the rows with ML.PREDICT. ML.PREDICT applies a trained model and returns the label and its probability. Local study-map skill 1.2 (BigQuery ML Feature Engineering and Prediction), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. ML.EVALUATE returns the model metrics against a labelled dataset. Why the correct answer wins: ML.PREDICT applies a trained model and returns the label and its probability.
- **B:** Incorrect for this question. ML.EXPLAIN_PREDICT attributes each prediction to the features that moved it. Why the correct answer wins: ML.PREDICT applies a trained model and returns the label and its probability.
- **C:** Correct. In this case: ML.PREDICT applies a trained model and returns the label and its probability.
- **D:** Incorrect for this question. ML.GLOBAL_EXPLAIN ranks the features that matter most across the whole model. Why the correct answer wins: ML.PREDICT applies a trained model and returns the label and its probability.

### Question 5 — B

Answer: Set a training budget in node hours. A node-hour budget caps how long AutoML searches. Local study-map skill 1.3 (Agent Platform AutoML), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. AutoML uses a reproducible default split when the dataset is large enough to do so. Why the correct answer wins: A node-hour budget caps how long AutoML searches.
- **B:** Correct. In this case: A node-hour budget caps how long AutoML searches.
- **C:** Incorrect for this question. A manual split is required when the split must follow time or a grouping column. Why the correct answer wins: A node-hour budget caps how long AutoML searches.
- **D:** Incorrect for this question. Export produces a container-ready artifact that can be served outside the managed endpoint. Why the correct answer wins: A node-hour budget caps how long AutoML searches.

### Question 6 — A

Answer: Define a manual split column with train, validation, and test. A manual split column keeps the holdout period out of training. A manual split is required when the split must follow time or a grouping column. Local study-map skill 1.3 (Agent Platform AutoML), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. A manual split is required when the split must follow time or a grouping column. In this case: A manual split column keeps the holdout period out of training.
- **B:** Incorrect for this question. A node-hour budget caps how long AutoML searches, which bounds the cost. Why the correct answer wins: A manual split column keeps the holdout period out of training.
- **C:** Incorrect for this question. AutoML uses a reproducible default split when the dataset is large enough to do so. Why the correct answer wins: A manual split column keeps the holdout period out of training.
- **D:** Incorrect for this question. Export produces a container-ready artifact that can be served outside the managed endpoint. Why the correct answer wins: A manual split column keeps the holdout period out of training.

### Question 7 — B

Answer: Fine-tune a Gemini model from BigQuery. Fine-tuning adapts a foundation model to the domain using rows that stay in BigQuery. Local study-map skill 1.4 (Gemini Fine-Tuning with BigQuery), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A better prompt is the cheapest experiment and often removes the need to tune at all. Why the correct answer wins: Fine-tuning adapts a foundation model to the domain using rows that stay in BigQuery.
- **B:** Correct. In this case: Fine-tuning adapts a foundation model to the domain using rows that stay in BigQuery.
- **C:** Incorrect for this question. A parameter-efficient adapter trains a small number of weights and keeps the base model intact. Why the correct answer wins: Fine-tuning adapts a foundation model to the domain using rows that stay in BigQuery.
- **D:** Incorrect for this question. A remote model calls the Gemini endpoint from SQL, so generation runs where the data lives. Why the correct answer wins: Fine-tuning adapts a foundation model to the domain using rows that stay in BigQuery.

### Question 8 — A

Answer: Select the model from Model Garden. Model Garden lists first-party and open models with deployment and licensing options. Local study-map skill 1.5 (Model Garden Model Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Model Garden lists first-party and open models with deployment and licensing options.
- **B:** Incorrect for this question. Imagen is the text-to-image model in the Google Cloud generative AI family. Why the correct answer wins: Model Garden lists first-party and open models with deployment and licensing options.
- **C:** Incorrect for this question. The smaller model answers faster and cheaper, which suits high-volume simple tasks. Why the correct answer wins: Model Garden lists first-party and open models with deployment and licensing options.
- **D:** Incorrect for this question. Embeddings turn text into vectors, which is what a retrieval step searches. Why the correct answer wins: Model Garden lists first-party and open models with deployment and licensing options.

### Question 9 — B

Answer: Use the Speech-to-Text API. The speech model transcribes audio, including domain phrases through adaptation. Local study-map skill 1.6 (Industry AI APIs), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Video Intelligence detects shots, labels, and explicit content in video. Why the correct answer wins: The speech model transcribes audio, including domain phrases through adaptation.
- **B:** Correct. In this case: The speech model transcribes audio, including domain phrases through adaptation.
- **C:** Incorrect for this question. The translation model handles a large language set without custom training. Why the correct answer wins: The speech model transcribes audio, including domain phrases through adaptation.
- **D:** Incorrect for this question. A Document AI processor extracts structured fields from forms with layout awareness. Why the correct answer wins: The speech model transcribes audio, including domain phrases through adaptation.

### Question 10 — A

Answer: Use Document AI with a specialised processor. A Document AI processor extracts structured fields with layout awareness. Local study-map skill 1.6 (Industry AI APIs), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: A Document AI processor extracts structured fields with layout awareness.
- **B:** Incorrect for this question. The prebuilt Vision model labels, detects, and reads text without training a model. Why the correct answer wins: A Document AI processor extracts structured fields with layout awareness.
- **C:** Incorrect for this question. The speech model transcribes audio, including domain phrases through adaptation. Why the correct answer wins: A Document AI processor extracts structured fields with layout awareness.
- **D:** Incorrect for this question. The Natural Language API returns entities, sentiment, and syntax without a custom model. Why the correct answer wins: A Document AI processor extracts structured fields with layout awareness.

### Question 11 — A, D

Answers: Cache the long shared context; Constrain the output with a schema and a token limit. Caching bills the repeated prefix once, and a bounded output cuts cost per request. Context caching bills the repeated prefix once instead of on every request. A bounded output cuts both latency and cost per request. Local study-map skill 1.7 (Gemini Application Optimization), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. Context caching bills the repeated prefix once instead of on every request. In this case: Caching bills the repeated prefix once, and a bounded output cuts cost per request.
- **B:** Incorrect for this question. Streaming improves perceived latency without reducing total generation time. Why the correct answer wins: Caching bills the repeated prefix once, and a bounded output cuts cost per request.
- **C:** Incorrect for this question. The larger model gives the best reasoning quality at a higher cost per token. Why the correct answer wins: Caching bills the repeated prefix once, and a bounded output cuts cost per request.
- **D:** Correct. A bounded output cuts both latency and cost per request. In this case: Caching bills the repeated prefix once, and a bounded output cuts cost per request.
- **E:** Incorrect for this question. The batch path trades latency for a lower price on non-interactive requests. Why the correct answer wins: Caching bills the repeated prefix once, and a bounded output cuts cost per request.

### Question 12 — C

Answer: Call the model in the region that serves the users. A regional endpoint removes cross-region latency and satisfies residency rules. Local study-map skill 1.7 (Gemini Application Optimization), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A fallback keeps the application answering when the primary model returns resource-exhausted. Why the correct answer wins: A regional endpoint removes cross-region latency and satisfies residency rules.
- **B:** Incorrect for this question. Throughput is capped by quota, so a quota ceiling cannot be solved by retries. Why the correct answer wins: A regional endpoint removes cross-region latency and satisfies residency rules.
- **C:** Correct. In this case: A regional endpoint removes cross-region latency and satisfies residency rules.
- **D:** Incorrect for this question. Streaming improves perceived latency without reducing total generation time. Why the correct answer wins: A regional endpoint removes cross-region latency and satisfies residency rules.

### Question 13 — B

Answer: Preprocess with Spark on Dataproc. Spark suits large transformations the team already has as Scala or PySpark code. Local study-map skill 2.1 (Preprocessing Tool Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Dataflow runs the same Beam code in batch and streaming and scales without provisioning. Why the correct answer wins: Spark suits large transformations the team already has as Scala or PySpark code.
- **B:** Correct. In this case: Spark suits large transformations the team already has as Scala or PySpark code.
- **C:** Incorrect for this question. SQL over BigQuery is the cheapest option when the data already sits there and the logic is set-based. Why the correct answer wins: Spark suits large transformations the team already has as Scala or PySpark code.
- **D:** Incorrect for this question. In-memory processing is the simplest option and stops working once the data exceeds the worker memory. Why the correct answer wins: Spark suits large transformations the team already has as Scala or PySpark code.

### Question 14 — B, E

Answers: Remove the post-outcome column from the features; Split by entity so one customer never spans train and test. A post-outcome column encodes the answer, and a grouped split prevents leakage. A column written after the outcome encodes the answer and inflates the score. Grouping the split prevents leakage between the training and evaluation rows. Local study-map skill 2.1 (Preprocessing Tool Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A time-based split prevents the model from learning from the future. Why the correct answer wins: A post-outcome column encodes the answer, and a grouped split prevents leakage.
- **B:** Correct. Grouping the split prevents leakage between the training and evaluation rows. In this case: A post-outcome column encodes the answer, and a grouped split prevents leakage.
- **C:** Incorrect for this question. Dropping the field removes the exposure entirely when the model does not need it. Why the correct answer wins: A post-outcome column encodes the answer, and a grouped split prevents leakage.
- **D:** Incorrect for this question. Scaling keeps one large-magnitude feature from dominating the gradient. Why the correct answer wins: A post-outcome column encodes the answer, and a grouped split prevents leakage.
- **E:** Correct. A column written after the outcome encodes the answer and inflates the score. In this case: A post-outcome column encodes the answer, and a grouped split prevents leakage.

### Question 15 — D

Answer: Catalog and profile the data with Dataplex. Dataplex discovers, profiles, and applies policy across the lakehouse. Local study-map skill 2.1 (Preprocessing Tool Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. SQL over BigQuery is the cheapest option when the data already sits there and the logic is set-based. Why the correct answer wins: Dataplex discovers, profiles, and applies policy across the lakehouse.
- **B:** Incorrect for this question. Dataflow runs the same Beam code in batch and streaming and scales without provisioning. Why the correct answer wins: Dataplex discovers, profiles, and applies policy across the lakehouse.
- **C:** Incorrect for this question. Spark suits large transformations the team already has as Scala or PySpark code. Why the correct answer wins: Dataplex discovers, profiles, and applies policy across the lakehouse.
- **D:** Correct. In this case: Dataplex discovers, profiles, and applies policy across the lakehouse.

### Question 16 — C

Answer: Register the feature in Agent Platform Feature Store. Feature Store keeps one definition that both training and serving read. Local study-map skill 2.2 (Feature Store), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Feature monitoring reports distribution changes per feature, not just per model. Why the correct answer wins: Feature Store keeps one definition that both training and serving read.
- **B:** Incorrect for this question. The online store returns the latest feature value at low latency for a single entity. Why the correct answer wins: Feature Store keeps one definition that both training and serving read.
- **C:** Correct. In this case: Feature Store keeps one definition that both training and serving read.
- **D:** Incorrect for this question. Bucketing converts a non-linear relationship into a form a linear model can fit. Why the correct answer wins: Feature Store keeps one definition that both training and serving read.

### Question 17 — B

Answer: Bucketize the continuous feature. Bucketing converts a non-linear relationship into a form a linear model can fit. Local study-map skill 2.2 (Feature Store), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Scaling keeps one large-magnitude feature from dominating the gradient. Why the correct answer wins: Bucketing converts a non-linear relationship into a form a linear model can fit.
- **B:** Correct. In this case: Bucketing converts a non-linear relationship into a form a linear model can fit.
- **C:** Incorrect for this question. A crossed feature lets a linear model express the interaction it cannot learn alone. Why the correct answer wins: Bucketing converts a non-linear relationship into a form a linear model can fit.
- **D:** Incorrect for this question. Feature Store keeps one definition that both training and serving read. Why the correct answer wins: Bucketing converts a non-linear relationship into a form a linear model can fit.

### Question 18 — D

Answer: De-identify the fields with Sensitive Data Protection. Sensitive Data Protection can tokenize or format-preservingly encrypt PII. Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts PII. Local study-map skill 2.3 (PII Handling and Data Privacy), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A salted hash keeps the join key usable while removing the direct identifier. Why the correct answer wins: Sensitive Data Protection can tokenize or format-preservingly encrypt PII.
- **B:** Incorrect for this question. Restricting the bucket limits who can copy the raw data in the first place. Why the correct answer wins: Sensitive Data Protection can tokenize or format-preservingly encrypt PII.
- **C:** Incorrect for this question. Dropping the field removes the exposure entirely when the model does not need it. Why the correct answer wins: Sensitive Data Protection can tokenize or format-preservingly encrypt PII.
- **D:** Correct. Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts PII. In this case: Sensitive Data Protection can tokenize or format-preservingly encrypt PII.

### Question 19 — D

Answer: Drop the identifier columns before the training dataset is written. Dropping the field removes the exposure entirely. Local study-map skill 2.3 (PII Handling and Data Privacy), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Restricting the bucket limits who can copy the raw data in the first place. Why the correct answer wins: Dropping the field removes the exposure entirely.
- **B:** Incorrect for this question. A salted hash keeps the join key usable while removing the direct identifier. Why the correct answer wins: Dropping the field removes the exposure entirely.
- **C:** Incorrect for this question. Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts PII. Why the correct answer wins: Dropping the field removes the exposure entirely.
- **D:** Correct. In this case: Dropping the field removes the exposure entirely.

### Question 20 — D

Answer: Pin the runtime to a custom container image. A runtime pinned to that image starts with the libraries already installed. A pinned image makes the environment reproducible across users. Local study-map skill 2.4 (Notebook Environments and Security), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The subnet attachment gives the notebook the route to internal data sources. Why the correct answer wins: A runtime pinned to that image starts with the libraries already installed.
- **B:** Incorrect for this question. A private-IP runtime reaches the data through the VPC and cannot be opened from the internet. Why the correct answer wins: A runtime pinned to that image starts with the libraries already installed.
- **C:** Incorrect for this question. Idle shutdown stops paying for a notebook nobody is using. Why the correct answer wins: A runtime pinned to that image starts with the libraries already installed.
- **D:** Correct. A pinned image makes the environment reproducible across users. In this case: A runtime pinned to that image starts with the libraries already installed.

### Question 21 — B

Answer: Create the runtime with no public IP. A private-IP runtime reaches the data through the VPC. Local study-map skill 2.4 (Notebook Environments and Security), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Idle shutdown stops paying for a notebook nobody is using. Why the correct answer wins: A private-IP runtime reaches the data through the VPC.
- **B:** Correct. In this case: A private-IP runtime reaches the data through the VPC.
- **C:** Incorrect for this question. The subnet attachment gives the notebook the route to internal data sources. Why the correct answer wins: A private-IP runtime reaches the data through the VPC.
- **D:** Incorrect for this question. A pinned image makes the environment reproducible across users. Why the correct answer wins: A private-IP runtime reaches the data through the VPC.

### Question 22 — D

Answer: Log the run to Agent Platform Experiments. Experiments records parameters, metrics, and artifacts per run. Local study-map skill 2.5 (Experiment Tracking), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A fixed seed makes a rerun reproducible when the rest of the environment is pinned. Why the correct answer wins: Experiments records parameters, metrics, and artifacts per run.
- **B:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: Experiments records parameters, metrics, and artifacts per run.
- **C:** Incorrect for this question. ML Metadata records which data and code produced which artifact. Why the correct answer wins: Experiments records parameters, metrics, and artifacts per run.
- **D:** Correct. In this case: Experiments records parameters, metrics, and artifacts per run.

### Question 23 — D

Answer: Compare the runs on the validation metric. Comparing on the validation metric keeps selection independent of the test set. Local study-map skill 2.5 (Experiment Tracking), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Experiments records parameters, metrics, and artifacts per run so runs can be compared. Why the correct answer wins: Comparing on the validation metric keeps selection independent of the test set.
- **B:** Incorrect for this question. A fixed seed makes a rerun reproducible when the rest of the environment is pinned. Why the correct answer wins: Comparing on the validation metric keeps selection independent of the test set.
- **C:** Incorrect for this question. ML Metadata records which data and code produced which artifact. Why the correct answer wins: Comparing on the validation metric keeps selection independent of the test set.
- **D:** Correct. In this case: Comparing on the validation metric keeps selection independent of the test set.

### Question 24 — A, C

Answers: Orchestrate the steps in Agent Platform Pipelines; Start from a Google-provided pipeline template. Pipelines runs each step as a container with lineage, and a template encodes the validated order. Pipelines runs each step as a container with caching, lineage, and retry. A template encodes the validated step order, so the first pipeline is not bespoke. Local study-map skill 2.6 (Development Environment Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. A template encodes the validated step order, so the first pipeline is not bespoke. In this case: Pipelines runs each step as a container with lineage, and a template encodes the validated order.
- **B:** Incorrect for this question. Ray fits a Python-native distributed workload that is not a container-per-step pipeline. Why the correct answer wins: Pipelines runs each step as a container with lineage, and a template encodes the validated order.
- **C:** Correct. Pipelines runs each step as a container with caching, lineage, and retry. In this case: Pipelines runs each step as a container with lineage, and a template encodes the validated order.
- **D:** Incorrect for this question. Airflow expresses cross-system dependencies and schedules outside the ML platform. Why the correct answer wins: Pipelines runs each step as a container with lineage, and a template encodes the validated order.
- **E:** Incorrect for this question. Experiments records parameters, metrics, and artifacts per run so runs can be compared. Why the correct answer wins: Pipelines runs each step as a container with lineage, and a template encodes the validated order.

### Question 25 — A

Answer: Log the run to Agent Platform Experiments. Experiments records parameters, metrics, and artifacts per run. Local study-map skill 2.6 (Development Environment Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Experiments records parameters, metrics, and artifacts per run.
- **B:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: Experiments records parameters, metrics, and artifacts per run.
- **C:** Incorrect for this question. Kubeflow pipelines give a container-per-step pipeline that runs on the managed service or on GKE. Why the correct answer wins: Experiments records parameters, metrics, and artifacts per run.
- **D:** Incorrect for this question. Pipelines runs each step as a container with caching, lineage, and retry. Why the correct answer wins: Experiments records parameters, metrics, and artifacts per run.

### Question 26 — B, D

Answers: Score the answers with an LLM-as-a-judge rubric; Sample the answers for expert human review. A rubric-driven judge scales the evaluation, and human review calibrates the judge. A rubric-driven judge scales the evaluation of free-text answers beyond human review. Human review remains the reference standard for a sample the judge is calibrated against. Local study-map skill 2.7 (Evaluation Metrics and LLM-as-a-Judge), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A fixed prompt set makes the safety score comparable between releases. Why the correct answer wins: A rubric-driven judge scales the evaluation, and human review calibrates the judge.
- **B:** Correct. Human review remains the reference standard for a sample the judge is calibrated against. In this case: A rubric-driven judge scales the evaluation, and human review calibrates the judge.
- **C:** Incorrect for this question. Groundedness checks whether each claim is supported by the documents that were retrieved. Why the correct answer wins: A rubric-driven judge scales the evaluation, and human review calibrates the judge.
- **D:** Correct. A rubric-driven judge scales the evaluation of free-text answers beyond human review. In this case: A rubric-driven judge scales the evaluation, and human review calibrates the judge.
- **E:** Incorrect for this question. Precision-recall AUC stays informative when the positive class is rare. Why the correct answer wins: A rubric-driven judge scales the evaluation, and human review calibrates the judge.

### Question 27 — A

Answer: Report MAPE when the error must be read as a percentage. MAPE expresses the error relative to the actual value. Local study-map skill 2.7 (Evaluation Metrics and LLM-as-a-Judge), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: MAPE expresses the error relative to the actual value.
- **B:** Incorrect for this question. ROC AUC measures ranking quality across thresholds and hides class imbalance. Why the correct answer wins: MAPE expresses the error relative to the actual value.
- **C:** Incorrect for this question. RMSE expresses the typical error in the units of the target. Why the correct answer wins: MAPE expresses the error relative to the actual value.
- **D:** Incorrect for this question. Precision-recall AUC stays informative when the positive class is rare. Why the correct answer wins: MAPE expresses the error relative to the actual value.

### Question 28 — A

Answer: Track artifacts and lineage in ML Metadata. ML Metadata records which data and code produced which artifact. Local study-map skill 2.8 (Metadata and Lineage), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: ML Metadata records which data and code produced which artifact.
- **B:** Incorrect for this question. Experiments records parameters, metrics, and artifacts per run so runs can be compared. Why the correct answer wins: ML Metadata records which data and code produced which artifact.
- **C:** Incorrect for this question. The registry versions the model artifact and links it to its lineage and metrics. Why the correct answer wins: ML Metadata records which data and code produced which artifact.
- **D:** Incorrect for this question. Artifact Registry holds the image with IAM and vulnerability metadata. Why the correct answer wins: ML Metadata records which data and code produced which artifact.

### Question 29 — A

Answer: Use TabNet as the custom training algorithm. TabNet gives an interpretable attentive tabular model. Local study-map skill 3.1 (Model Type Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: TabNet gives an interpretable attentive tabular model.
- **B:** Incorrect for this question. A DNN suits a large tabular or unstructured dataset where interactions matter. Why the correct answer wins: TabNet gives an interpretable attentive tabular model.
- **C:** Incorrect for this question. A foundation model suits an open-ended language or multimodal task where labelled data is scarce. Why the correct answer wins: TabNet gives an interpretable attentive tabular model.
- **D:** Incorrect for this question. A classical time series model suits a single series with strong seasonality and little covariate data. Why the correct answer wins: TabNet gives an interpretable attentive tabular model.

### Question 30 — C

Answer: Choose a classical time series model. A classical time series model suits a single series with strong seasonality. Local study-map skill 3.1 (Model Type Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A foundation model suits an open-ended language or multimodal task where labelled data is scarce. Why the correct answer wins: A classical time series model suits a single series with strong seasonality.
- **B:** Incorrect for this question. TabNet gives an interpretable attentive tabular model inside custom training. Why the correct answer wins: A classical time series model suits a single series with strong seasonality.
- **C:** Correct. In this case: A classical time series model suits a single series with strong seasonality.
- **D:** Incorrect for this question. A DNN suits a large tabular or unstructured dataset where interactions matter. Why the correct answer wins: A classical time series model suits a single series with strong seasonality.

### Question 31 — C

Answer: Train a custom model on Agent Platform. Custom training keeps full control of the framework and the loss. Local study-map skill 3.2 (Product Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. TabNet gives an interpretable attentive tabular model inside custom training. Why the correct answer wins: Custom training keeps full control of the framework and the loss.
- **B:** Incorrect for this question. AutoML removes architecture search and tuning from the team while keeping a managed endpoint. Why the correct answer wins: Custom training keeps full control of the framework and the loss.
- **C:** Correct. In this case: Custom training keeps full control of the framework and the loss.
- **D:** Incorrect for this question. BigQuery ML keeps training next to the data and removes a separate serving pipeline. Why the correct answer wins: Custom training keeps full control of the framework and the loss.

### Question 32 — A

Answer: Train with Agent Platform AutoML. AutoML removes architecture search and tuning from the team. Local study-map skill 3.2 (Product Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: AutoML removes architecture search and tuning from the team.
- **B:** Incorrect for this question. BigQuery ML keeps training next to the data and removes a separate serving pipeline. Why the correct answer wins: AutoML removes architecture search and tuning from the team.
- **C:** Incorrect for this question. Custom training keeps full control of the framework and the loss. Why the correct answer wins: AutoML removes architecture search and tuning from the team.
- **D:** Incorrect for this question. TabNet gives an interpretable attentive tabular model inside custom training. Why the correct answer wins: AutoML removes architecture search and tuning from the team.

### Question 33 — A, B

Answers: Roll out a canary with a small traffic share; Run the new model in shadow mode. Shadow mode serves nothing to users, and a canary limits the exposure. A canary limits the blast radius while the new model is compared with the old one. Shadow mode scores live traffic without serving its answers, so the comparison costs nothing to users. Local study-map skill 3.3 (Deployment Strategy Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. Shadow mode scores live traffic without serving its answers, so the comparison costs nothing to users. In this case: Shadow mode serves nothing to users, and a canary limits the exposure.
- **B:** Correct. A canary limits the blast radius while the new model is compared with the old one. In this case: Shadow mode serves nothing to users, and a canary limits the exposure.
- **C:** Incorrect for this question. A/B testing compares two models on the same population with a traffic split. Why the correct answer wins: Shadow mode serves nothing to users, and a canary limits the exposure.
- **D:** Incorrect for this question. Two identical deployments let the switch be reversed immediately. Why the correct answer wins: Shadow mode serves nothing to users, and a canary limits the exposure.
- **E:** Incorrect for this question. An in-place replacement exposes every request to the new version at once. Why the correct answer wins: Shadow mode serves nothing to users, and a canary limits the exposure.

### Question 34 — A

Answer: Run the new model in shadow mode. Shadow mode scores live traffic without serving its answers to users. Local study-map skill 3.3 (Deployment Strategy Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Shadow mode scores live traffic without serving its answers to users.
- **B:** Incorrect for this question. A canary limits the blast radius while the new model is compared with the old one. Why the correct answer wins: Shadow mode scores live traffic without serving its answers to users.
- **C:** Incorrect for this question. A/B testing compares two models on the same population with a traffic split. Why the correct answer wins: Shadow mode scores live traffic without serving its answers to users.
- **D:** Incorrect for this question. An in-place replacement exposes every request to the new version at once. Why the correct answer wins: Shadow mode scores live traffic without serving its answers to users.

### Question 35 — C

Answer: Read the contribution of each feature with ML.EXPLAIN_PREDICT. ML.EXPLAIN_PREDICT returns the contribution of each feature for a scored row. ML.EXPLAIN_PREDICT attributes each prediction to the features that moved it. Local study-map skill 3.4 (Interpretability), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. ML.GLOBAL_EXPLAIN ranks the features that matter most across the whole model. Why the correct answer wins: ML.EXPLAIN_PREDICT returns the contribution of each feature for a scored row.
- **B:** Incorrect for this question. Sampled Shapley explains individual online predictions with a bounded compute cost. Why the correct answer wins: ML.EXPLAIN_PREDICT returns the contribution of each feature for a scored row.
- **C:** Correct. ML.EXPLAIN_PREDICT attributes each prediction to the features that moved it. In this case: ML.EXPLAIN_PREDICT returns the contribution of each feature for a scored row.
- **D:** Incorrect for this question. Shapley values attribute a prediction to its features with a consistent baseline. Why the correct answer wins: ML.EXPLAIN_PREDICT returns the contribution of each feature for a scored row.

### Question 36 — C

Answer: Choose an inherently interpretable model. A linear or tree model can be read directly. Local study-map skill 3.4 (Interpretability), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Shapley values attribute a prediction to its features with a consistent baseline. Why the correct answer wins: A linear or tree model can be read directly.
- **B:** Incorrect for this question. Sampled Shapley explains individual online predictions with a bounded compute cost. Why the correct answer wins: A linear or tree model can be read directly.
- **C:** Correct. In this case: A linear or tree model can be read directly.
- **D:** Incorrect for this question. Attribution shows which inputs drove the decision in the case the reviewer is examining. Why the correct answer wins: A linear or tree model can be read directly.

### Question 37 — B

Answer: Write the training data as Parquet in Cloud Storage. Parquet is columnar and cheap to scan. Local study-map skill 3.5 (Training Data Organization), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A streaming path keeps the training data current without a nightly copy. Why the correct answer wins: Parquet is columnar and cheap to scan.
- **B:** Correct. In this case: Parquet is columnar and cheap to scan.
- **C:** Incorrect for this question. Reading from BigQuery avoids a copy and keeps the query pushdown. Why the correct answer wins: Parquet is columnar and cheap to scan.
- **D:** Incorrect for this question. Sharded TFRecord is the efficient read format for distributed training. Why the correct answer wins: Parquet is columnar and cheap to scan.

### Question 38 — C

Answer: Read the training data directly from BigQuery. Reading from BigQuery avoids a copy and keeps the query pushdown. Local study-map skill 3.5 (Training Data Organization), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Parquet is columnar and cheap to scan for tabular training data. Why the correct answer wins: Reading from BigQuery avoids a copy and keeps the query pushdown.
- **B:** Incorrect for this question. Sharded TFRecord is the efficient read format for distributed training. Why the correct answer wins: Reading from BigQuery avoids a copy and keeps the query pushdown.
- **C:** Correct. In this case: Reading from BigQuery avoids a copy and keeps the query pushdown.
- **D:** Incorrect for this question. A streaming path keeps the training data current without a nightly copy. Why the correct answer wins: Reading from BigQuery avoids a copy and keeps the query pushdown.

### Question 39 — C

Answer: Validate the schema and quarantine rejected rows. Rejecting rows into a side table makes a schema break visible. Local study-map skill 3.6 (Ingestion into Training Pipelines), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A streaming path keeps the training data current without a nightly copy. Why the correct answer wins: Rejecting rows into a side table makes a schema break visible.
- **B:** Incorrect for this question. Sharded TFRecord is the efficient read format for distributed training. Why the correct answer wins: Rejecting rows into a side table makes a schema break visible.
- **C:** Correct. In this case: Rejecting rows into a side table makes a schema break visible.
- **D:** Incorrect for this question. Deduplicating at ingest stops duplicated records inflating the training set. Why the correct answer wins: Rejecting rows into a side table makes a schema break visible.

### Question 40 — A

Answer: Stream the new records through Dataflow into the training store. A streaming path keeps the training data current. Local study-map skill 3.6 (Ingestion into Training Pipelines), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: A streaming path keeps the training data current.
- **B:** Incorrect for this question. Rejecting rows into a side table makes a schema break visible instead of silent. Why the correct answer wins: A streaming path keeps the training data current.
- **C:** Incorrect for this question. Deduplicating at ingest stops duplicated records inflating the training set. Why the correct answer wins: A streaming path keeps the training data current.
- **D:** Incorrect for this question. Reading from BigQuery avoids a copy and keeps the query pushdown. Why the correct answer wins: A streaming path keeps the training data current.

### Question 41 — A

Answer: Package the trainer as a Python package. The prebuilt container installs the package. Local study-map skill 3.7 (Custom Training and SDKs), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: The prebuilt container installs the package.
- **B:** Incorrect for this question. A custom container carries its own framework and dependencies into the managed training job. Why the correct answer wins: The prebuilt container installs the package.
- **C:** Incorrect for this question. A prebuilt container already implements the framework handler, so no serving code is written. Why the correct answer wins: The prebuilt container installs the package.
- **D:** Incorrect for this question. Export produces a container-ready artifact that can be served outside the managed endpoint. Why the correct answer wins: The prebuilt container installs the package.

### Question 42 — C

Answer: Run a custom container on Agent Platform. A custom container carries its own framework and dependencies. Local study-map skill 3.7 (Custom Training and SDKs), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. AutoML removes architecture search and tuning from the team while keeping a managed endpoint. Why the correct answer wins: A custom container carries its own framework and dependencies.
- **B:** Incorrect for this question. A prebuilt container already implements the framework handler, so no serving code is written. Why the correct answer wins: A custom container carries its own framework and dependencies.
- **C:** Correct. In this case: A custom container carries its own framework and dependencies.
- **D:** Incorrect for this question. The prebuilt container installs the package, which is the lightest way to run custom code. Why the correct answer wins: A custom container carries its own framework and dependencies.

### Question 43 — B

Answer: Reduce the per-replica batch size. The out-of-memory error is a memory-per-step problem. Local study-map skill 3.8 (Training Failure Troubleshooting), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Accelerator quota is regional and blocks the job before the code runs. Why the correct answer wins: The out-of-memory error is a memory-per-step problem.
- **B:** Correct. In this case: The out-of-memory error is a memory-per-step problem.
- **C:** Incorrect for this question. A loss that becomes NaN usually reflects a step size too large for the data scale. Why the correct answer wins: The out-of-memory error is a memory-per-step problem.
- **D:** Incorrect for this question. A framework mismatch between local and remote runs changes behaviour without changing the code. Why the correct answer wins: The out-of-memory error is a memory-per-step problem.

### Question 44 — D

Answer: Request accelerator quota for the region. Accelerator quota is regional and blocks the job before the code runs. Local study-map skill 3.8 (Training Failure Troubleshooting), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A permission error on the input is a missing IAM binding, not a model problem. Why the correct answer wins: Accelerator quota is regional and blocks the job before the code runs.
- **B:** Incorrect for this question. A loss that becomes NaN usually reflects a step size too large for the data scale. Why the correct answer wins: Accelerator quota is regional and blocks the job before the code runs.
- **C:** Incorrect for this question. A framework mismatch between local and remote runs changes behaviour without changing the code. Why the correct answer wins: Accelerator quota is regional and blocks the job before the code runs.
- **D:** Correct. In this case: Accelerator quota is regional and blocks the job before the code runs.

### Question 45 — A, E

Answers: Run a hyperparameter tuning job; Cap the search with a trial count and a parallel budget. The tuning service searches in parallel, and the budget bounds cost and time. The tuning service searches the space in parallel and reports the best trial. The budget bounds both the cost and the wall-clock time of the search. Local study-map skill 3.9 (Hyperparameter Tuning), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. The budget bounds both the cost and the wall-clock time of the search. In this case: The tuning service searches in parallel, and the budget bounds cost and time.
- **B:** Incorrect for this question. A fixed seed makes a rerun reproducible when the rest of the environment is pinned. Why the correct answer wins: The tuning service searches in parallel, and the budget bounds cost and time.
- **C:** Incorrect for this question. Early stopping frees capacity from trials that cannot win. Why the correct answer wins: The tuning service searches in parallel, and the budget bounds cost and time.
- **D:** Incorrect for this question. Bayesian search spends fewer trials to reach a good configuration. Why the correct answer wins: The tuning service searches in parallel, and the budget bounds cost and time.
- **E:** Correct. The tuning service searches the space in parallel and reports the best trial. In this case: The tuning service searches in parallel, and the budget bounds cost and time.

### Question 46 — C

Answer: Report the business metric from the trainer. The search optimises the metric the trainer reports. Local study-map skill 3.9 (Hyperparameter Tuning), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Bayesian search spends fewer trials to reach a good configuration. Why the correct answer wins: The search optimises the metric the trainer reports.
- **B:** Incorrect for this question. The budget bounds both the cost and the wall-clock time of the search. Why the correct answer wins: The search optimises the metric the trainer reports.
- **C:** Correct. In this case: The search optimises the metric the trainer reports.
- **D:** Incorrect for this question. The tuning service searches the space in parallel and reports the best trial. Why the correct answer wins: The search optimises the metric the trainer reports.

### Question 47 — C

Answer: Fine-tune the full model. Full fine-tuning updates every weight and needs the most data. Local study-map skill 3.10 (Fine-Tuning Decisions), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Retrieval is the cheaper answer when the problem is missing knowledge rather than missing behaviour. Why the correct answer wins: Full fine-tuning updates every weight and needs the most data.
- **B:** Incorrect for this question. A better prompt is the cheapest experiment and often removes the need to tune at all. Why the correct answer wins: Full fine-tuning updates every weight and needs the most data.
- **C:** Correct. In this case: Full fine-tuning updates every weight and needs the most data.
- **D:** Incorrect for this question. A parameter-efficient adapter trains a small number of weights and keeps the base model intact. Why the correct answer wins: Full fine-tuning updates every weight and needs the most data.

### Question 48 — A

Answer: Train on a TPU slice. A TPU slice gives a tightly coupled accelerator fabric. Local study-map skill 3.11 (Hardware and Accelerator Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: A TPU slice gives a tightly coupled accelerator fabric.
- **B:** Incorrect for this question. CPU serving is the cheapest option for a small model with a generous latency budget. Why the correct answer wins: A TPU slice gives a tightly coupled accelerator fabric.
- **C:** Incorrect for this question. An L4 GPU gives low-cost inference acceleration for a modest model. Why the correct answer wins: A TPU slice gives a tightly coupled accelerator fabric.
- **D:** Incorrect for this question. A100 GPUs suit mixed-precision training where the framework expects CUDA. Why the correct answer wins: A TPU slice gives a tightly coupled accelerator fabric.

### Question 49 — C, D

Answers: Use data parallelism; Scale the batch size with the worker count. Data parallelism splits the batch, and a larger global batch keeps workers busy. Data parallelism replicates the model and splits each batch across the workers. A larger global batch keeps each worker busy after the split. Local study-map skill 3.12 (Distributed Training), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Multi-worker gives each replica a shard of the data and a defined chief. Why the correct answer wins: Data parallelism splits the batch, and a larger global batch keeps workers busy.
- **B:** Incorrect for this question. A100 GPUs suit mixed-precision training where the framework expects CUDA. Why the correct answer wins: Data parallelism splits the batch, and a larger global batch keeps workers busy.
- **C:** Correct. A larger global batch keeps each worker busy after the split. In this case: Data parallelism splits the batch, and a larger global batch keeps workers busy.
- **D:** Correct. Data parallelism replicates the model and splits each batch across the workers. In this case: Data parallelism splits the batch, and a larger global batch keeps workers busy.
- **E:** Incorrect for this question. Model parallelism splits the layers across devices when one model does not fit on one. Why the correct answer wins: Data parallelism splits the batch, and a larger global batch keeps workers busy.

### Question 50 — C

Answer: Deploy to an online endpoint. An endpoint keeps capacity ready for per-request predictions. Local study-map skill 4.1 (Batch and Online Inference), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Batching amortises the per-request overhead when the caller can wait. Why the correct answer wins: An endpoint keeps capacity ready for per-request predictions.
- **B:** Incorrect for this question. Streaming answers each event as it arrives rather than on a schedule. Why the correct answer wins: An endpoint keeps capacity ready for per-request predictions.
- **C:** Correct. In this case: An endpoint keeps capacity ready for per-request predictions.
- **D:** Incorrect for this question. Batch prediction reads a file or table and writes predictions without holding serving capacity. Why the correct answer wins: An endpoint keeps capacity ready for per-request predictions.

### Question 51 — C, D

Answers: Run batch prediction; Send the events to a streaming prediction path. Batch prediction handles the file, and streaming answers each event. Batch prediction reads a file or table and writes predictions without holding serving capacity. Streaming answers each event as it arrives rather than on a schedule. Local study-map skill 4.1 (Batch and Online Inference), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Batching amortises the per-request overhead when the caller can wait. Why the correct answer wins: Batch prediction handles the file, and streaming answers each event.
- **B:** Incorrect for this question. An endpoint keeps capacity ready for low-latency per-request predictions. Why the correct answer wins: Batch prediction handles the file, and streaming answers each event.
- **C:** Correct. Batch prediction reads a file or table and writes predictions without holding serving capacity. In this case: Batch prediction handles the file, and streaming answers each event.
- **D:** Correct. Streaming answers each event as it arrives rather than on a schedule. In this case: Batch prediction handles the file, and streaming answers each event.
- **E:** Incorrect for this question. A GPU shortens inference time enough to meet a tight latency target. Why the correct answer wins: Batch prediction handles the file, and streaming answers each event.

### Question 52 — B

Answer: Batch the requests inside the client. Batching amortises the per-request overhead when the caller can tolerate a short wait. Local study-map skill 4.1 (Batch and Online Inference), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Batch prediction reads a file or table and writes predictions without holding serving capacity. Why the correct answer wins: Batching amortises the per-request overhead when the caller can tolerate a short wait.
- **B:** Correct. In this case: Batching amortises the per-request overhead when the caller can tolerate a short wait.
- **C:** Incorrect for this question. Concurrency fills each replica before another is started, which lowers cost per request. Why the correct answer wins: Batching amortises the per-request overhead when the caller can tolerate a short wait.
- **D:** Incorrect for this question. Autoscaling adds replicas with the traffic and removes them afterwards. Why the correct answer wins: Batching amortises the per-request overhead when the caller can tolerate a short wait.

### Question 53 — D

Answer: Use a prebuilt serving container. A prebuilt container already implements the serving interface for that framework. A prebuilt container already implements the framework handler, so no serving code is written. Local study-map skill 4.2 (Packaging and Custom Containers), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Artifact Registry holds the image with IAM and vulnerability metadata. Why the correct answer wins: A prebuilt container already implements the serving interface for that framework.
- **B:** Incorrect for this question. A GPU shortens inference time enough to meet a tight latency target. Why the correct answer wins: A prebuilt container already implements the serving interface for that framework.
- **C:** Incorrect for this question. The routine runs the preprocessing and postprocessing inside the serving container. Why the correct answer wins: A prebuilt container already implements the serving interface for that framework.
- **D:** Correct. A prebuilt container already implements the framework handler, so no serving code is written. In this case: A prebuilt container already implements the serving interface for that framework.

### Question 54 — C

Answer: Add a custom prediction routine to the container. The routine runs preprocessing and postprocessing inside the container. Local study-map skill 4.2 (Packaging and Custom Containers), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. An alias decouples the served version name from the artifact id, so a rollback is a pointer move. Why the correct answer wins: The routine runs preprocessing and postprocessing inside the container.
- **B:** Incorrect for this question. Artifact Registry holds the image with IAM and vulnerability metadata. Why the correct answer wins: The routine runs preprocessing and postprocessing inside the container.
- **C:** Correct. In this case: The routine runs preprocessing and postprocessing inside the container.
- **D:** Incorrect for this question. A prebuilt container already implements the framework handler, so no serving code is written. Why the correct answer wins: The routine runs preprocessing and postprocessing inside the container.

### Question 55 — C

Answer: Deploy the version and move the alias. An alias decouples the served version from the artifact id. An alias decouples the served version name from the artifact id, so a rollback is a pointer move. Local study-map skill 4.3 (Model Registry and Versioning), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A traffic split sends a defined share to each version on the same endpoint. Why the correct answer wins: An alias decouples the served version from the artifact id.
- **B:** Incorrect for this question. The registry versions the model artifact and links it to its lineage and metrics. Why the correct answer wins: An alias decouples the served version from the artifact id.
- **C:** Correct. An alias decouples the served version name from the artifact id, so a rollback is a pointer move. In this case: An alias decouples the served version from the artifact id.
- **D:** Incorrect for this question. Two identical deployments let the switch be reversed immediately. Why the correct answer wins: An alias decouples the served version from the artifact id.

### Question 56 — D

Answer: Register the model in Agent Platform Model Registry. The registry versions the artifact and links it to lineage. Local study-map skill 4.3 (Model Registry and Versioning), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Experiments records parameters, metrics, and artifacts per run so runs can be compared. Why the correct answer wins: The registry versions the artifact and links it to lineage.
- **B:** Incorrect for this question. Artifact Registry holds the image with IAM and vulnerability metadata. Why the correct answer wins: The registry versions the artifact and links it to lineage.
- **C:** Incorrect for this question. ML Metadata records which data and code produced which artifact. Why the correct answer wins: The registry versions the artifact and links it to lineage.
- **D:** Correct. In this case: The registry versions the artifact and links it to lineage.

### Question 57 — B, C

Answers: Split traffic between two models in an A/B test; Deploy blue/green with an instant switch. A/B testing compares two models, and two deployments allow an instant reversal. A/B testing compares two models on the same population with a traffic split. Two identical deployments let the switch be reversed immediately. Local study-map skill 4.4 (Model Rollout Strategies), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. An in-place replacement exposes every request to the new version at once. Why the correct answer wins: A/B testing compares two models, and two deployments allow an instant reversal.
- **B:** Correct. Two identical deployments let the switch be reversed immediately. In this case: A/B testing compares two models, and two deployments allow an instant reversal.
- **C:** Correct. A/B testing compares two models on the same population with a traffic split. In this case: A/B testing compares two models, and two deployments allow an instant reversal.
- **D:** Incorrect for this question. A canary limits the blast radius while the new model is compared with the old one. Why the correct answer wins: A/B testing compares two models, and two deployments allow an instant reversal.
- **E:** Incorrect for this question. Shadow mode scores live traffic without serving its answers, so the comparison costs nothing to users. Why the correct answer wins: A/B testing compares two models, and two deployments allow an instant reversal.

### Question 58 — B

Answer: Roll out a canary with a small traffic share. A canary limits the blast radius while signals are compared. Local study-map skill 4.4 (Model Rollout Strategies), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. An in-place replacement exposes every request to the new version at once. Why the correct answer wins: A canary limits the blast radius while signals are compared.
- **B:** Correct. In this case: A canary limits the blast radius while signals are compared.
- **C:** Incorrect for this question. Shadow mode scores live traffic without serving its answers, so the comparison costs nothing to users. Why the correct answer wins: A canary limits the blast radius while signals are compared.
- **D:** Incorrect for this question. A/B testing compares two models on the same population with a traffic split. Why the correct answer wins: A canary limits the blast radius while signals are compared.

### Question 59 — A

Answer: Register the feature in Agent Platform Feature Store. Feature Store keeps one definition for both paths. Feature Store keeps one definition that both training and serving read. Local study-map skill 4.5 (Inference Preprocessing and Postprocessing), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. Feature Store keeps one definition that both training and serving read. In this case: Feature Store keeps one definition for both paths.
- **B:** Incorrect for this question. An alias decouples the served version name from the artifact id, so a rollback is a pointer move. Why the correct answer wins: Feature Store keeps one definition for both paths.
- **C:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: Feature Store keeps one definition for both paths.
- **D:** Incorrect for this question. Shared code removes the class of bug where the two paths compute a feature differently. Why the correct answer wins: Feature Store keeps one definition for both paths.

### Question 60 — D

Answer: Share one transformation library between training and serving. Shared code removes the class of bug where the paths differ. Shared code removes the class of bug where the two paths compute a feature differently. Local study-map skill 4.5 (Inference Preprocessing and Postprocessing), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Feature Store keeps one definition that both training and serving read. Why the correct answer wins: Shared code removes the class of bug where the paths differ.
- **B:** Incorrect for this question. A validation step stops a bad batch before it reaches training. Why the correct answer wins: Shared code removes the class of bug where the paths differ.
- **C:** Incorrect for this question. Preprocessing inside the artifact cannot drift between the two paths. Why the correct answer wins: Shared code removes the class of bug where the paths differ.
- **D:** Correct. Shared code removes the class of bug where the two paths compute a feature differently. In this case: Shared code removes the class of bug where the paths differ.

### Question 61 — B

Answer: Deploy with a private endpoint only. A private endpoint is reachable only from the VPC. Local study-map skill 4.6 (Endpoint Types and Access), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A shared endpoint removes the deployment step but gives no control over capacity or residency. Why the correct answer wins: A private endpoint is reachable only from the VPC.
- **B:** Correct. In this case: A private endpoint is reachable only from the VPC.
- **C:** Incorrect for this question. A dedicated endpoint gives the model its own capacity instead of sharing a pool. Why the correct answer wins: A private endpoint is reachable only from the VPC.
- **D:** Incorrect for this question. A GPU shortens inference time enough to meet a tight latency target. Why the correct answer wins: A private endpoint is reachable only from the VPC.

### Question 62 — A

Answer: Use a shared public endpoint. A shared endpoint removes the deployment step. Local study-map skill 4.6 (Endpoint Types and Access), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: A shared endpoint removes the deployment step.
- **B:** Incorrect for this question. Autoscaling adds replicas with the traffic and removes them afterwards. Why the correct answer wins: A shared endpoint removes the deployment step.
- **C:** Incorrect for this question. A private endpoint is reachable only from the VPC and shares no public surface. Why the correct answer wins: A shared endpoint removes the deployment step.
- **D:** Incorrect for this question. A dedicated endpoint gives the model its own capacity instead of sharing a pool. Why the correct answer wins: A shared endpoint removes the deployment step.

### Question 63 — A

Answer: Serve on L4 GPUs. An L4 GPU gives low-cost inference acceleration. Local study-map skill 4.7 (Serving Hardware), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: An L4 GPU gives low-cost inference acceleration.
- **B:** Incorrect for this question. A TPU slice gives a tightly coupled accelerator fabric for large synchronous training. Why the correct answer wins: An L4 GPU gives low-cost inference acceleration.
- **C:** Incorrect for this question. A100 GPUs suit mixed-precision training where the framework expects CUDA. Why the correct answer wins: An L4 GPU gives low-cost inference acceleration.
- **D:** Incorrect for this question. CPU serving is the cheapest option for a small model with a generous latency budget. Why the correct answer wins: An L4 GPU gives low-cost inference acceleration.

### Question 64 — A

Answer: Attach a GPU to the serving replica. A GPU shortens inference time enough to meet the target. Local study-map skill 4.7 (Serving Hardware), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: A GPU shortens inference time enough to meet the target.
- **B:** Incorrect for this question. An Edge TPU runs a quantised model on-device where the network cannot be relied on. Why the correct answer wins: A GPU shortens inference time enough to meet the target.
- **C:** Incorrect for this question. Concurrency fills each replica before another is started, which lowers cost per request. Why the correct answer wins: A GPU shortens inference time enough to meet the target.
- **D:** Incorrect for this question. CPU serving is the cheapest option for a small model with a generous latency budget. Why the correct answer wins: A GPU shortens inference time enough to meet the target.

### Question 65 — A, E

Answers: Enable autoscaling on the endpoint; Raise the maximum replica count. Autoscaling adds replicas with traffic, and the ceiling caps how far it scales. Autoscaling adds replicas with the traffic and removes them afterwards. The ceiling caps how far the endpoint scales, and therefore the throughput it can absorb. Local study-map skill 4.8 (Serving Throughput and Scaling), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. Autoscaling adds replicas with the traffic and removes them afterwards. In this case: Autoscaling adds replicas with traffic, and the ceiling caps how far it scales.
- **B:** Incorrect for this question. A minimum replica keeps capacity warm so the first request after a quiet period is fast. Why the correct answer wins: Autoscaling adds replicas with traffic, and the ceiling caps how far it scales.
- **C:** Incorrect for this question. Concurrency fills each replica before another is started, which lowers cost per request. Why the correct answer wins: Autoscaling adds replicas with traffic, and the ceiling caps how far it scales.
- **D:** Incorrect for this question. Batching amortises the per-request overhead when the caller can wait. Why the correct answer wins: Autoscaling adds replicas with traffic, and the ceiling caps how far it scales.
- **E:** Correct. The ceiling caps how far the endpoint scales, and therefore the throughput it can absorb. In this case: Autoscaling adds replicas with traffic, and the ceiling caps how far it scales.

### Question 66 — A

Answer: Raise the concurrency per replica. Concurrency fills each replica before another is started. Local study-map skill 4.8 (Serving Throughput and Scaling), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Concurrency fills each replica before another is started.
- **B:** Incorrect for this question. The ceiling caps how far the endpoint scales, and therefore the throughput it can absorb. Why the correct answer wins: Concurrency fills each replica before another is started.
- **C:** Incorrect for this question. Batching amortises the per-request overhead when the caller can wait. Why the correct answer wins: Concurrency fills each replica before another is started.
- **D:** Incorrect for this question. A minimum replica keeps capacity warm so the first request after a quiet period is fast. Why the correct answer wins: Concurrency fills each replica before another is started.

### Question 67 — C

Answer: Set a minimum replica count. A minimum replica keeps capacity warm so the first request after a quiet period is fast. Local study-map skill 4.8 (Serving Throughput and Scaling), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The ceiling caps how far the endpoint scales, and therefore the throughput it can absorb. Why the correct answer wins: A minimum replica keeps capacity warm so the first request after a quiet period is fast.
- **B:** Incorrect for this question. Batching amortises the per-request overhead when the caller can wait. Why the correct answer wins: A minimum replica keeps capacity warm so the first request after a quiet period is fast.
- **C:** Correct. In this case: A minimum replica keeps capacity warm so the first request after a quiet period is fast.
- **D:** Incorrect for this question. Concurrency fills each replica before another is started, which lowers cost per request. Why the correct answer wins: A minimum replica keeps capacity warm so the first request after a quiet period is fast.

### Question 68 — A, B

Answers: Raise the concurrency per replica; Attach a GPU to the serving replica. Concurrency lowers the cost per request, and a GPU shortens inference time. Concurrency fills each replica before another is started, which lowers cost per request. A GPU shortens inference time enough to meet a tight latency target. Local study-map skill 4.9 (Production Tuning), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. Concurrency fills each replica before another is started, which lowers cost per request. In this case: Concurrency lowers the cost per request, and a GPU shortens inference time.
- **B:** Correct. A GPU shortens inference time enough to meet a tight latency target. In this case: Concurrency lowers the cost per request, and a GPU shortens inference time.
- **C:** Incorrect for this question. The ceiling caps how far the endpoint scales, and therefore the throughput it can absorb. Why the correct answer wins: Concurrency lowers the cost per request, and a GPU shortens inference time.
- **D:** Incorrect for this question. Batching amortises the per-request overhead when the caller can wait. Why the correct answer wins: Concurrency lowers the cost per request, and a GPU shortens inference time.
- **E:** Incorrect for this question. A minimum replica keeps capacity warm so the first request after a quiet period is fast. Why the correct answer wins: Concurrency lowers the cost per request, and a GPU shortens inference time.

### Question 69 — D

Answer: Configure explanation metadata for the endpoint. Explanation metadata tells the endpoint which inputs to attribute over. Local study-map skill 4.9 (Production Tuning), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Artifact Registry holds the image with IAM and vulnerability metadata. Why the correct answer wins: Explanation metadata tells the endpoint which inputs to attribute over.
- **B:** Incorrect for this question. Batching amortises the per-request overhead when the caller can wait. Why the correct answer wins: Explanation metadata tells the endpoint which inputs to attribute over.
- **C:** Incorrect for this question. An alias decouples the served version name from the artifact id, so a rollback is a pointer move. Why the correct answer wins: Explanation metadata tells the endpoint which inputs to attribute over.
- **D:** Correct. In this case: Explanation metadata tells the endpoint which inputs to attribute over.

### Question 70 — B

Answer: Add an explicit data validation step. A validation step stops a bad batch before it reaches training. Local study-map skill 5.1 (Data and Model Validation), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The gate promotes a model only when it beats the incumbent on the agreed metric. Why the correct answer wins: A validation step stops a bad batch before it reaches training.
- **B:** Correct. In this case: A validation step stops a bad batch before it reaches training.
- **C:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: A validation step stops a bad batch before it reaches training.
- **D:** Incorrect for this question. Rejecting rows into a side table makes a schema break visible instead of silent. Why the correct answer wins: A validation step stops a bad batch before it reaches training.

### Question 71 — A

Answer: Gate the deployment on a model evaluation threshold. The gate promotes a model only when it beats the incumbent. Local study-map skill 5.1 (Data and Model Validation), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: The gate promotes a model only when it beats the incumbent.
- **B:** Incorrect for this question. A test set that has been used for tuning no longer estimates generalisation. Why the correct answer wins: The gate promotes a model only when it beats the incumbent.
- **C:** Incorrect for this question. A validation step stops a bad batch before it reaches training. Why the correct answer wins: The gate promotes a model only when it beats the incumbent.
- **D:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: The gate promotes a model only when it beats the incumbent.

### Question 72 — C, E

Answers: Keep the test set out of every tuning decision; Choose the threshold from the cost of each error type. A locked test set restores an unbiased estimate, and the threshold follows the cost of errors. A test set that has been used for tuning no longer estimates generalisation. The decision threshold follows the relative cost of a false positive and a false negative. Local study-map skill 5.1 (Data and Model Validation), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: A locked test set restores an unbiased estimate, and the threshold follows the cost of errors.
- **B:** Incorrect for this question. ROC AUC measures ranking quality across thresholds and hides class imbalance. Why the correct answer wins: A locked test set restores an unbiased estimate, and the threshold follows the cost of errors.
- **C:** Correct. The decision threshold follows the relative cost of a false positive and a false negative. In this case: A locked test set restores an unbiased estimate, and the threshold follows the cost of errors.
- **D:** Incorrect for this question. MAPE expresses the error relative to the actual value, which business readers understand. Why the correct answer wins: A locked test set restores an unbiased estimate, and the threshold follows the cost of errors.
- **E:** Correct. A test set that has been used for tuning no longer estimates generalisation. In this case: A locked test set restores an unbiased estimate, and the threshold follows the cost of errors.

### Question 73 — D

Answer: Orchestrate the steps in Agent Platform Pipelines. Pipelines runs each step as a container with caching and lineage. Local study-map skill 5.2 (Pipeline Orchestration Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Airflow expresses cross-system dependencies and schedules outside the ML platform. Why the correct answer wins: Pipelines runs each step as a container with caching and lineage.
- **B:** Incorrect for this question. Kubeflow pipelines give a container-per-step pipeline that runs on the managed service or on GKE. Why the correct answer wins: Pipelines runs each step as a container with caching and lineage.
- **C:** Incorrect for this question. Ray fits a Python-native distributed workload that is not a container-per-step pipeline. Why the correct answer wins: Pipelines runs each step as a container with caching and lineage.
- **D:** Correct. In this case: Pipelines runs each step as a container with caching and lineage.

### Question 74 — D

Answer: Orchestrate with Managed Service for Apache Airflow. Airflow expresses cross-system dependencies and schedules outside the ML platform. Local study-map skill 5.2 (Pipeline Orchestration Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance. Why the correct answer wins: Airflow expresses cross-system dependencies and schedules outside the ML platform.
- **B:** Incorrect for this question. Pipelines runs each step as a container with caching, lineage, and retry. Why the correct answer wins: Airflow expresses cross-system dependencies and schedules outside the ML platform.
- **C:** Incorrect for this question. Ray fits a Python-native distributed workload that is not a container-per-step pipeline. Why the correct answer wins: Airflow expresses cross-system dependencies and schedules outside the ML platform.
- **D:** Correct. In this case: Airflow expresses cross-system dependencies and schedules outside the ML platform.

### Question 75 — B

Answer: Use Ray on Agent Platform for the distributed compute. Ray fits a Python-native distributed workload. Local study-map skill 5.2 (Pipeline Orchestration Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Kubeflow pipelines give a container-per-step pipeline that runs on the managed service or on GKE. Why the correct answer wins: Ray fits a Python-native distributed workload.
- **B:** Correct. In this case: Ray fits a Python-native distributed workload.
- **C:** Incorrect for this question. Airflow expresses cross-system dependencies and schedules outside the ML platform. Why the correct answer wins: Ray fits a Python-native distributed workload.
- **D:** Incorrect for this question. Pipelines runs each step as a container with caching, lineage, and retry. Why the correct answer wins: Ray fits a Python-native distributed workload.

### Question 76 — B

Answer: Trigger the build and deploy from Cloud Build. A Cloud Build trigger runs the build and deploy steps from the repository event. Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance. Local study-map skill 5.2 (Pipeline Orchestration Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The scheduler starts the pipeline on the cadence the retraining policy defines. Why the correct answer wins: A Cloud Build trigger runs the build and deploy steps from the repository event.
- **B:** Correct. Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance. In this case: A Cloud Build trigger runs the build and deploy steps from the repository event.
- **C:** Incorrect for this question. Pipelines runs each step as a container with caching, lineage, and retry. Why the correct answer wins: A Cloud Build trigger runs the build and deploy steps from the repository event.
- **D:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: A Cloud Build trigger runs the build and deploy steps from the repository event.

### Question 77 — B

Answer: Enable step caching. Caching skips an unchanged step on a rerun. Local study-map skill 5.3 (Train and Serve Consistency), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Drift-triggered retraining responds to change instead of to the calendar. Why the correct answer wins: Caching skips an unchanged step on a rerun.
- **B:** Correct. In this case: Caching skips an unchanged step on a rerun.
- **C:** Incorrect for this question. A validation step stops a bad batch before it reaches training. Why the correct answer wins: Caching skips an unchanged step on a rerun.
- **D:** Incorrect for this question. The gate promotes a model only when it beats the incumbent on the agreed metric. Why the correct answer wins: Caching skips an unchanged step on a rerun.

### Question 78 — B, D

Answers: Keep the preprocessing inside the exported model; Read the historical features from the offline store. Preprocessing inside the artifact cannot drift, and the offline store returns point-in-time values. Preprocessing inside the artifact cannot drift between the two paths. The offline store returns point-in-time values for training. Local study-map skill 5.3 (Train and Serve Consistency), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Deduplicating at ingest stops duplicated records inflating the training set. Why the correct answer wins: Preprocessing inside the artifact cannot drift, and the offline store returns point-in-time values.
- **B:** Correct. Preprocessing inside the artifact cannot drift between the two paths. In this case: Preprocessing inside the artifact cannot drift, and the offline store returns point-in-time values.
- **C:** Incorrect for this question. The registry versions the model artifact and links it to its lineage and metrics. Why the correct answer wins: Preprocessing inside the artifact cannot drift, and the offline store returns point-in-time values.
- **D:** Correct. The offline store returns point-in-time values for training. In this case: Preprocessing inside the artifact cannot drift, and the offline store returns point-in-time values.
- **E:** Incorrect for this question. The online store returns the latest feature value at low latency for a single entity. Why the correct answer wins: Preprocessing inside the artifact cannot drift, and the offline store returns point-in-time values.

### Question 79 — B

Answer: Share one transformation library between training and serving. Shared code removes the class of bug where the paths differ. Shared code removes the class of bug where the two paths compute a feature differently. Local study-map skill 5.3 (Train and Serve Consistency), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Preprocessing inside the artifact cannot drift between the two paths. Why the correct answer wins: Shared code removes the class of bug where the paths differ.
- **B:** Correct. Shared code removes the class of bug where the two paths compute a feature differently. In this case: Shared code removes the class of bug where the paths differ.
- **C:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: Shared code removes the class of bug where the paths differ.
- **D:** Incorrect for this question. Feature Store keeps one definition that both training and serving read. Why the correct answer wins: Shared code removes the class of bug where the paths differ.

### Question 80 — D

Answer: Validate the schema and quarantine rejected rows. Rejecting rows into a side table makes a schema break visible. Local study-map skill 5.3 (Train and Serve Consistency), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Shared code removes the class of bug where the two paths compute a feature differently. Why the correct answer wins: Rejecting rows into a side table makes a schema break visible.
- **B:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: Rejecting rows into a side table makes a schema break visible.
- **C:** Incorrect for this question. Deduplicating at ingest stops duplicated records inflating the training set. Why the correct answer wins: Rejecting rows into a side table makes a schema break visible.
- **D:** Correct. In this case: Rejecting rows into a side table makes a schema break visible.

### Question 81 — A

Answer: Retrain when drift crosses the threshold. Drift-triggered retraining responds to change in the inputs instead of to the calendar. Local study-map skill 5.4 (Retraining Policy), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Drift-triggered retraining responds to change in the inputs instead of to the calendar.
- **B:** Incorrect for this question. Metric-triggered retraining reacts to actual quality loss. Why the correct answer wins: Drift-triggered retraining responds to change in the inputs instead of to the calendar.
- **C:** Incorrect for this question. A fixed schedule is simple to reason about when the data changes predictably. Why the correct answer wins: Drift-triggered retraining responds to change in the inputs instead of to the calendar.
- **D:** Incorrect for this question. Manual retraining leaves the model stale whenever the trigger is forgotten. Why the correct answer wins: Drift-triggered retraining responds to change in the inputs instead of to the calendar.

### Question 82 — D

Answer: Retrain only on a manual request. Manual retraining leaves the model stale. Local study-map skill 5.4 (Retraining Policy), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Drift-triggered retraining responds to change instead of to the calendar. Why the correct answer wins: Manual retraining leaves the model stale.
- **B:** Incorrect for this question. Metric-triggered retraining reacts to actual quality loss. Why the correct answer wins: Manual retraining leaves the model stale.
- **C:** Incorrect for this question. A fixed schedule is simple to reason about when the data changes predictably. Why the correct answer wins: Manual retraining leaves the model stale.
- **D:** Correct. In this case: Manual retraining leaves the model stale.

### Question 83 — D

Answer: Retrain when the production metric drops. Metric-triggered retraining reacts to actual quality loss. Local study-map skill 5.4 (Retraining Policy), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A fixed schedule is simple to reason about when the data changes predictably. Why the correct answer wins: Metric-triggered retraining reacts to actual quality loss.
- **B:** Incorrect for this question. Drift-triggered retraining responds to change instead of to the calendar. Why the correct answer wins: Metric-triggered retraining reacts to actual quality loss.
- **C:** Incorrect for this question. Manual retraining leaves the model stale whenever the trigger is forgotten. Why the correct answer wins: Metric-triggered retraining reacts to actual quality loss.
- **D:** Correct. In this case: Metric-triggered retraining reacts to actual quality loss.

### Question 84 — B

Answer: Extend CI/CD into continuous training. Continuous training adds the retrain and validate step. Local study-map skill 5.5 (CI/CD/CT with Cloud Build), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: Continuous training adds the retrain and validate step.
- **B:** Correct. In this case: Continuous training adds the retrain and validate step.
- **C:** Incorrect for this question. An event trigger retrains when data lands instead of on a fixed clock. Why the correct answer wins: Continuous training adds the retrain and validate step.
- **D:** Incorrect for this question. Manual retraining leaves the model stale whenever the trigger is forgotten. Why the correct answer wins: Continuous training adds the retrain and validate step.

### Question 85 — D

Answer: Trigger the pipeline from the arrival of new data. An event trigger retrains when data lands. Local study-map skill 5.5 (CI/CD/CT with Cloud Build), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Manual retraining leaves the model stale whenever the trigger is forgotten. Why the correct answer wins: An event trigger retrains when data lands.
- **B:** Incorrect for this question. The scheduler starts the pipeline on the cadence the retraining policy defines. Why the correct answer wins: An event trigger retrains when data lands.
- **C:** Incorrect for this question. Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance. Why the correct answer wins: An event trigger retrains when data lands.
- **D:** Correct. In this case: An event trigger retrains when data lands.

### Question 86 — D

Answer: Gate the deployment on a model evaluation threshold. The gate promotes a model only when it beats the incumbent. Local study-map skill 5.5 (CI/CD/CT with Cloud Build), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Drift-triggered retraining responds to change instead of to the calendar. Why the correct answer wins: The gate promotes a model only when it beats the incumbent.
- **B:** Incorrect for this question. A validation step stops a bad batch before it reaches training. Why the correct answer wins: The gate promotes a model only when it beats the incumbent.
- **C:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: The gate promotes a model only when it beats the incumbent.
- **D:** Correct. In this case: The gate promotes a model only when it beats the incumbent.

### Question 87 — C

Answer: Trigger the build and deploy from Cloud Build. Cloud Build keeps the provenance of every build and deploy step. Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance. Local study-map skill 5.2 (Pipeline Orchestration Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The scheduler starts the pipeline on the cadence the retraining policy defines. Why the correct answer wins: Cloud Build keeps the provenance of every build and deploy step.
- **B:** Incorrect for this question. Manual retraining leaves the model stale whenever the trigger is forgotten. Why the correct answer wins: Cloud Build keeps the provenance of every build and deploy step.
- **C:** Correct. Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance. In this case: Cloud Build keeps the provenance of every build and deploy step.
- **D:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: Cloud Build keeps the provenance of every build and deploy step.

### Question 88 — B, C

Answers: Redact the pattern-matchable fields with a regex; Constrain the response to a JSON schema. A regex removes a known identifier pattern, and a schema stops unparseable free text. A regex removes a known identifier pattern before the prompt leaves the service. A schema stops the model returning free text that downstream code cannot parse. Local study-map skill 6.1 (Secure AI and Prompt Protection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Model Armor detects prompt injection, jailbreak attempts, and unsafe content. Why the correct answer wins: A regex removes a known identifier pattern, and a schema stops unparseable free text.
- **B:** Correct. A schema stops the model returning free text that downstream code cannot parse. In this case: A regex removes a known identifier pattern, and a schema stops unparseable free text.
- **C:** Correct. A regex removes a known identifier pattern before the prompt leaves the service. In this case: A regex removes a known identifier pattern, and a schema stops unparseable free text.
- **D:** Incorrect for this question. Safety filters block categories of harmful output at the model call. Why the correct answer wins: A regex removes a known identifier pattern, and a schema stops unparseable free text.
- **E:** Incorrect for this question. A system instruction states what the assistant must refuse, though it is not a security control on its own. Why the correct answer wins: A regex removes a known identifier pattern, and a schema stops unparseable free text.

### Question 89 — C

Answer: Screen the prompts and responses with Model Armor. Model Armor detects prompt injection and jailbreak attempts. Local study-map skill 6.1 (Secure AI and Prompt Protection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A schema stops the model returning free text that downstream code cannot parse. Why the correct answer wins: Model Armor detects prompt injection and jailbreak attempts.
- **B:** Incorrect for this question. A system instruction states what the assistant must refuse, though it is not a security control on its own. Why the correct answer wins: Model Armor detects prompt injection and jailbreak attempts.
- **C:** Correct. In this case: Model Armor detects prompt injection and jailbreak attempts.
- **D:** Incorrect for this question. Safety filters block categories of harmful output at the model call. Why the correct answer wins: Model Armor detects prompt injection and jailbreak attempts.

### Question 90 — B

Answer: Put the boundary in the system instruction. A system instruction states what the assistant must refuse. Local study-map skill 6.1 (Secure AI and Prompt Protection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A schema stops the model returning free text that downstream code cannot parse. Why the correct answer wins: A system instruction states what the assistant must refuse.
- **B:** Correct. In this case: A system instruction states what the assistant must refuse.
- **C:** Incorrect for this question. Model Armor detects prompt injection, jailbreak attempts, and unsafe content. Why the correct answer wins: A system instruction states what the assistant must refuse.
- **D:** Incorrect for this question. Safety filters block categories of harmful output at the model call. Why the correct answer wins: A system instruction states what the assistant must refuse.

### Question 91 — D

Answer: Monitor the outcome rate across the protected groups. A per-group outcome rate is the first evidence of disparate impact. Local study-map skill 6.2 (Responsible AI and Bias), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The card states where the model may be used and where it must not. Why the correct answer wins: A per-group outcome rate is the first evidence of disparate impact.
- **B:** Incorrect for this question. A sliced metric shows a gap that the aggregate metric hides. Why the correct answer wins: A per-group outcome rate is the first evidence of disparate impact.
- **C:** Incorrect for this question. The card records provenance, intended use, and known gaps for the dataset. Why the correct answer wins: A per-group outcome rate is the first evidence of disparate impact.
- **D:** Correct. In this case: A per-group outcome rate is the first evidence of disparate impact.

### Question 92 — A

Answer: Document the dataset with a data card. The card records provenance, intended use, and known gaps. Local study-map skill 6.2 (Responsible AI and Bias), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: The card records provenance, intended use, and known gaps.
- **B:** Incorrect for this question. A per-group outcome rate is the first evidence of disparate impact. Why the correct answer wins: The card records provenance, intended use, and known gaps.
- **C:** Incorrect for this question. The card states where the model may be used and where it must not. Why the correct answer wins: The card records provenance, intended use, and known gaps.
- **D:** Incorrect for this question. A sliced metric shows a gap that the aggregate metric hides. Why the correct answer wins: The card records provenance, intended use, and known gaps.

### Question 93 — C

Answer: Use sampled Shapley on the endpoint. Sampled Shapley explains individual online predictions. Local study-map skill 6.3 (Explainability), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Shapley values attribute a prediction to its features with a consistent baseline. Why the correct answer wins: Sampled Shapley explains individual online predictions.
- **B:** Incorrect for this question. ML.GLOBAL_EXPLAIN ranks the features that matter most across the whole model. Why the correct answer wins: Sampled Shapley explains individual online predictions.
- **C:** Correct. In this case: Sampled Shapley explains individual online predictions.
- **D:** Incorrect for this question. Integrated gradients attributes an image prediction to the pixels that moved it. Why the correct answer wins: Sampled Shapley explains individual online predictions.

### Question 94 — B

Answer: Report the feature attributions to the reviewer. Attribution shows which inputs drove the decision. Local study-map skill 6.3 (Explainability), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The card states where the model may be used and where it must not. Why the correct answer wins: Attribution shows which inputs drove the decision.
- **B:** Correct. In this case: Attribution shows which inputs drove the decision.
- **C:** Incorrect for this question. A linear or tree model can be read directly when regulation demands an explanation by construction. Why the correct answer wins: Attribution shows which inputs drove the decision.
- **D:** Incorrect for this question. ML.GLOBAL_EXPLAIN ranks the features that matter most across the whole model. Why the correct answer wins: Attribution shows which inputs drove the decision.

### Question 95 — B

Answer: Set the monitoring threshold from the acceptable error budget. The threshold expresses how much drift is acceptable. The threshold expresses how much drift the business can absorb before someone acts. Local study-map skill 6.4 (Model Monitoring Configuration), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. An alert with no owner is a dashboard nobody reads. Why the correct answer wins: The threshold expresses how much drift is acceptable.
- **B:** Correct. The threshold expresses how much drift the business can absorb before someone acts. In this case: The threshold expresses how much drift is acceptable.
- **C:** Incorrect for this question. Continuous sampling catches quality regressions that drift metrics cannot see. Why the correct answer wins: The threshold expresses how much drift is acceptable.
- **D:** Incorrect for this question. A percentile latency per version shows a regression that an average hides. Why the correct answer wins: The threshold expresses how much drift is acceptable.

### Question 96 — A

Answer: Enable Model Monitoring on the endpoint. Model Monitoring compares live traffic with the baseline. Local study-map skill 6.4 (Model Monitoring Configuration), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Model Monitoring compares live traffic with the baseline.
- **B:** Incorrect for this question. A percentile latency per version shows a regression that an average hides. Why the correct answer wins: Model Monitoring compares live traffic with the baseline.
- **C:** Incorrect for this question. An alert with no owner is a dashboard nobody reads. Why the correct answer wins: Model Monitoring compares live traffic with the baseline.
- **D:** Incorrect for this question. Redacted logs make a bad answer diagnosable without storing sensitive text. Why the correct answer wins: Model Monitoring compares live traffic with the baseline.

### Question 97 — B, C

Answers: Watch for concept drift; Watch for feature attribution drift. Attribution drift changes which features drive the prediction, and concept drift changes the relationship itself. Concept drift is a change in the relationship between the features and the target. Attribution drift is a change in which features drive the prediction. Local study-map skill 6.5 (Skew and Drift Types), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Without the labelled outcome, quality can only be inferred from the inputs and outputs. Why the correct answer wins: Attribution drift changes which features drive the prediction, and concept drift changes the relationship itself.
- **B:** Correct. Attribution drift is a change in which features drive the prediction. In this case: Attribution drift changes which features drive the prediction, and concept drift changes the relationship itself.
- **C:** Correct. Concept drift is a change in the relationship between the features and the target. In this case: Attribution drift changes which features drive the prediction, and concept drift changes the relationship itself.
- **D:** Incorrect for this question. A shift in the output distribution is often the first visible symptom. Why the correct answer wins: Attribution drift changes which features drive the prediction, and concept drift changes the relationship itself.
- **E:** Incorrect for this question. Data drift is a change in the input distribution after the model shipped. Why the correct answer wins: Attribution drift changes which features drive the prediction, and concept drift changes the relationship itself.

### Question 98 — B

Answer: Watch for data drift. Data drift is a change in the input distribution after the model shipped. Local study-map skill 6.5 (Skew and Drift Types), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Without the labelled outcome, quality can only be inferred from the inputs and outputs. Why the correct answer wins: Data drift is a change in the input distribution after the model shipped.
- **B:** Correct. In this case: Data drift is a change in the input distribution after the model shipped.
- **C:** Incorrect for this question. Skew compares the live feature distribution with the training distribution. Why the correct answer wins: Data drift is a change in the input distribution after the model shipped.
- **D:** Incorrect for this question. Concept drift is a change in the relationship between the features and the target. Why the correct answer wins: Data drift is a change in the input distribution after the model shipped.

### Question 99 — D

Answer: Track tokens and cost per request. Token accounting attributes generative cost to the feature that caused it. Local study-map skill 6.6 (Generative AI Monitoring), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Model Monitoring compares live traffic with the training baseline and reports skew and drift. Why the correct answer wins: Token accounting attributes generative cost to the feature that caused it.
- **B:** Incorrect for this question. A percentile latency per version shows a regression that an average hides. Why the correct answer wins: Token accounting attributes generative cost to the feature that caused it.
- **C:** Incorrect for this question. Continuous sampling catches quality regressions that drift metrics cannot see. Why the correct answer wins: Token accounting attributes generative cost to the feature that caused it.
- **D:** Correct. In this case: Token accounting attributes generative cost to the feature that caused it.

### Question 100 — C

Answer: Explain with Shapley values. Shapley values attribute a prediction to its features against a consistent baseline. Local study-map skill 6.3 (Explainability), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Attribution shows which inputs drove the decision in the case the reviewer is examining. Why the correct answer wins: Shapley values attribute a prediction to its features against a consistent baseline.
- **B:** Incorrect for this question. Sampled Shapley explains individual online predictions with a bounded compute cost. Why the correct answer wins: Shapley values attribute a prediction to its features against a consistent baseline.
- **C:** Correct. In this case: Shapley values attribute a prediction to its features against a consistent baseline.
- **D:** Incorrect for this question. Integrated gradients attributes an image prediction to the pixels that moved it. Why the correct answer wins: Shapley values attribute a prediction to its features against a consistent baseline.
