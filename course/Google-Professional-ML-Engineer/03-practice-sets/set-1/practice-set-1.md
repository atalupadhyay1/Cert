# Google Cloud Professional Machine Learning Engineer — Full-Length Mock Exam 1

Professional Machine Learning Engineer · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study or drag-and-drop item is reproduced. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Architecting low-code AI solutions (Low-Code AI and Foundational Models)

### 1. A retail team needs a monthly demand forecast per store with a confidence band. What should be built?

- A. Create a BigQuery ML ARIMA_PLUS time series model
- B. Create a BigQuery ML logistic regression model
- C. Create a BigQuery ML k-means model
- D. Create a BigQuery ML boosted tree classifier

### 2. A bank must predict whether a loan defaults, and the risk team wants the model metrics before launch. Which two steps apply? Select two.

- A. Create a BigQuery ML logistic regression model
- B. Create a BigQuery ML k-means model
- C. Import the TensorFlow model into BigQuery ML
- D. Store the predictions in a nested JSON column
- E. Inspect the metrics with ML.EVALUATE

### 3. Feature scaling must apply identically at training and at scoring time. What should be used?

- A. Declare the feature transformations in the TRANSFORM clause
- B. Summarise the model with ML.GLOBAL_EXPLAIN
- C. Score the rows with ML.PREDICT
- D. Reserve BigQuery slots for the training job

### 4. A trained BigQuery ML model must score a table of new customers from SQL. What should be used?

- A. Inspect the metrics with ML.EVALUATE
- B. Score the rows with ML.PREDICT
- C. Import the TensorFlow model into BigQuery ML
- D. Read the contribution of each feature with ML.EXPLAIN_PREDICT

### 5. A marketing team has labelled campaign data but nobody who can write model code. What should be used?

- A. Export the AutoML model as an artifact
- B. Set a training budget in node hours
- C. Train a custom model on Agent Platform
- D. Use AutoML so the team needs no modelling code

### 6. An AutoML dataset must be split so no customer appears in both training and test. What should be configured?

- A. Set a training budget in node hours
- B. Define a manual split column with train, validation, and test
- C. Disable early stopping for the final run
- D. Let AutoML choose the data split

### 7. Support replies must follow the house tone, and the examples already sit in BigQuery. What should be done?

- A. Create a BigQuery ML remote model over Gemini
- B. Fine-tune a Gemini model from BigQuery
- C. Start with prompt and context engineering
- D. Ground the prompt with retrieval instead of fine-tuning

### 8. A team must compare licensing and deployment options across several open models. Where should it look?

- A. Select the model from Model Garden
- B. Deploy an open-weight model from Model Garden
- C. Embed the documents with the text embedding model
- D. Choose the larger Gemini model for quality

### 9. Scanned invoices must yield structured line items with layout awareness. What should be used?

- A. Use the Vision API
- B. Use Document AI with a specialised processor
- C. Use the Translation API
- D. Use the Speech-to-Text API

### 10. A product team needs object labels on 200 images next week and has no labelled training set. What should it do?

- A. Send the image and the question in one multimodal request
- B. Call the prebuilt API rather than training a model
- C. Train an Agent Platform AutoML image model
- D. Deploy an open-weight model from Model Garden

### 11. A nightly summarisation job resends the same 40-page policy document, and latency is irrelevant. Which two changes reduce cost? Select two.

- A. Choose the larger Gemini model for quality
- B. Request a quota increase for the model
- C. Cache the long shared context
- D. Stream the response tokens to the client
- E. Send the offline work through the batch API

### 12. A chat feature returns resource-exhausted errors at peak and must keep answering. What should be added?

- A. Call the model in the region that serves the users
- B. Fall back to a smaller model when the primary is throttled
- C. Choose the larger Gemini model for quality
- D. Request a quota increase for the model

---

## Domain 2 — Collaborating within and across teams to manage data and models (Data, Features, Notebooks, and Experiments)

### 13. A 400 GB table already sits in BigQuery and the transformation is a set-based join. What should be used?

- A. Preprocess in BigQuery with SQL
- B. Preprocess in memory with pandas
- C. Preprocess with a Dataflow pipeline
- D. Preprocess with Spark on Dataproc

### 14. A churn dataset holds email addresses, and the model must not learn from future months. Which two steps apply? Select two.

- A. De-identify the fields with Sensitive Data Protection
- B. Add a crossed feature for the interacting pair
- C. Split the data by time rather than at random
- D. Let AutoML choose the data split
- E. Hash the identifiers with a salted key before training

### 15. A two-million-row CSV must be explored on a laptop before any design decision. What should be used?

- A. Preprocess in memory with pandas
- B. Preprocess in BigQuery with SQL
- C. Catalog and profile the data with Dataplex
- D. Preprocess with a Dataflow pipeline

### 16. Online scoring and offline training must read the same churn feature definition. What should be used?

- A. Register the feature in Agent Platform Feature Store
- B. Normalise the numeric feature before training
- C. Add a crossed feature for the interacting pair
- D. Stream the new records through Dataflow into the training store

### 17. A training job needs the feature value as it stood on the order date. Which read path provides that?

- A. Read the historical features from the offline store
- B. Serve the feature from the online store
- C. Enable feature monitoring on the feature group
- D. Bucketize the continuous feature

### 18. The model must still join on a customer key that must not be reversible in the dataset. What should be done?

- A. De-identify the fields with Sensitive Data Protection
- B. Drop the identifier columns before the training dataset is written
- C. Hash the identifiers with a salted key before training
- D. Restrict the raw bucket to a privileged service account

### 19. Only the training service account may touch the raw export. What should be applied?

- A. Restrict the raw bucket to a privileged service account
- B. Drop the identifier columns before the training dataset is written
- C. De-identify the fields with Sensitive Data Protection
- D. Catalog and profile the data with Dataplex

### 20. A notebook must reach internal data and must not be openable from the internet. What should be configured?

- A. Pin the runtime to a custom container image
- B. Set an idle shutdown schedule
- C. Attach the runtime to the shared VPC subnet
- D. Create the runtime with no public IP

### 21. Thirty analysts leave notebooks running overnight and the bill is climbing. What should be set?

- A. Pin the runtime to a custom container image
- B. Set an idle shutdown schedule
- C. Use an Agent Platform Workbench instance
- D. Create the runtime with no public IP

### 22. Forty training runs must be compared on validation loss before a model is chosen. What should be used?

- A. Log the run to Agent Platform Experiments
- B. Enable step caching
- C. Track artifacts and lineage in ML Metadata
- D. Set the random seed in the training code

### 23. A rerun of the same code produces a different score each time. What should be added?

- A. Set the random seed in the training code
- B. Express the workflow as a Kubeflow pipeline
- C. Track artifacts and lineage in ML Metadata
- D. Log the run to Agent Platform Experiments

### 24. A team needs a reproducible multi-step workflow and has never built one. Which two choices fit? Select two.

- A. Log the run to Agent Platform Experiments
- B. Pin the runtime to a custom container image
- C. Express the workflow as a Kubeflow pipeline
- D. Start from a Google-provided pipeline template
- E. Orchestrate with Managed Service for Apache Airflow

### 25. The workflow must coordinate a BigQuery load, a Spark job outside the ML platform, and a model deployment. What should orchestrate it?

- A. Orchestrate with Managed Service for Apache Airflow
- B. Express the workflow as a Kubeflow pipeline
- C. Orchestrate the steps in Agent Platform Pipelines
- D. Use Ray on Agent Platform for the distributed compute

### 26. A fraud model flags 0.4 per cent of transactions, and the team must choose an operating threshold. Which two metrics help? Select two.

- A. Inspect the confusion matrix at the operating threshold
- B. Report RMSE for the regression target
- C. Report MAPE when the error must be read as a percentage
- D. Report precision-recall AUC for the rare class
- E. Report ROC AUC

### 27. Two thousand free-text answers must be scored for helpfulness after each release. What should be used?

- A. Measure the safety metrics on a fixed prompt set
- B. Measure groundedness against the retrieved context
- C. Score the answers with an LLM-as-a-judge rubric
- D. Sample the answers for expert human review

### 28. An auditor asks which dataset version produced the deployed model. What should be recorded?

- A. Track artifacts and lineage in ML Metadata
- B. Log the run to Agent Platform Experiments
- C. Enable step caching
- D. Register the model in Agent Platform Model Registry

---

## Domain 3 — Scaling prototypes into ML models (Training at Scale and Model Choice)

### 29. One series has four years of hourly history and almost no covariates. What model type fits?

- A. Choose a deep neural network
- B. Choose a classical time series model
- C. Use TabNet as the custom training algorithm
- D. Choose a foundation model

### 30. The task is summarising free-text support tickets with a few hundred examples. What model type fits?

- A. Use TabNet as the custom training algorithm
- B. Choose a deep neural network
- C. Choose a foundation model
- D. Choose a classical time series model

### 31. The team has two data analysts and no ML engineer, and the deadline is six weeks. What should drive the product choice?

- A. Train a custom model on Agent Platform
- B. Choose the product the team can actually operate
- C. Train with Agent Platform AutoML
- D. Build the model in BigQuery ML

### 32. A 2 TB feature table must produce a daily propensity score with the least new infrastructure. What should be used?

- A. Train a custom model on Agent Platform
- B. Use TabNet as the custom training algorithm
- C. Train with Agent Platform AutoML
- D. Build the model in BigQuery ML

### 33. A new ranking model must be judged on live traffic without changing what users see, then exposed to a small share. Which two strategies apply in order? Select two.

- A. Roll out a canary with a small traffic share
- B. Run the new model in shadow mode
- C. Deploy blue/green with an instant switch
- D. Split traffic between two models in an A/B test
- E. Replace the model version in place

### 34. The business needs the previous model restorable within seconds during a launch. What should be used?

- A. Roll out a canary with a small traffic share
- B. Deploy blue/green with an instant switch
- C. Split traffic between two models in an A/B test
- D. Replace the model version in place

### 35. A declined applicant asks which factors drove the decision, answered online. What should be used?

- A. Summarise the model with ML.GLOBAL_EXPLAIN
- B. Use integrated gradients for the image model
- C. Publish a model card with the intended use and limits
- D. Use sampled Shapley on the endpoint

### 36. A regulator requires an explanation by construction, not a post-hoc approximation. What should be chosen?

- A. Use sampled Shapley on the endpoint
- B. Report the feature attributions to the reviewer
- C. Choose an inherently interpretable model
- D. Explain with Shapley values

### 37. A distributed trainer must read 2 TB efficiently from object storage. What format should the data be written in?

- A. Read the training data directly from BigQuery
- B. Write the training data as TFRecord shards in Cloud Storage
- C. Stream the new records through Dataflow into the training store
- D. Write the training data as Parquet in Cloud Storage

### 38. A tabular dataset is scanned by column for training and analysis. What format fits?

- A. Read the training data directly from BigQuery
- B. Stream the new records through Dataflow into the training store
- C. Write the training data as TFRecord shards in Cloud Storage
- D. Write the training data as Parquet in Cloud Storage

### 39. A schema change upstream silently broke last month's training batch. What should the pipeline add?

- A. Validate the schema and quarantine rejected rows
- B. Stream the new records through Dataflow into the training store
- C. Read the training data directly from BigQuery
- D. Deduplicate on the event key in the ingestion step

### 40. Retried events arrive twice and inflate the training set. What should the ingestion step do?

- A. Deduplicate on the event key in the ingestion step
- B. Validate the schema and quarantine rejected rows
- C. Stream the new records through Dataflow into the training store
- D. Write the training data as Parquet in Cloud Storage

### 41. A trainer depends on a library version the prebuilt image does not ship. What should be used?

- A. Train with Agent Platform AutoML
- B. Package the trainer as a Python package
- C. Run a custom container on Agent Platform
- D. Use a prebuilt serving container

### 42. A plain scikit-learn script must run remotely with the fewest moving parts. What should be used?

- A. Use a prebuilt serving container
- B. Run a custom container on Agent Platform
- C. Package the trainer as a Python package
- D. Export the AutoML model as an artifact

### 43. The training job fails with an out-of-memory error after a few hundred steps. What should be tried first?

- A. Request accelerator quota for the region
- B. Reduce the per-replica batch size
- C. Verify each worker reads a distinct shard
- D. Lower the learning rate

### 44. The job fails immediately reading the input path with a 403. What is the cause?

- A. Lower the learning rate
- B. Request accelerator quota for the region
- C. Pin the framework version in the container
- D. Grant the training service account access to the bucket

### 45. Eighty trial configurations must be searched, and half of them are hopeless after ten epochs. Which two choices apply? Select two.

- A. Set the random seed in the training code
- B. Set a training budget in node hours
- C. Report the business metric from the trainer
- D. Run a hyperparameter tuning job
- E. Enable early stopping of poor trials

### 46. The search keeps optimising accuracy while the business is paid on revenue per session. What must change?

- A. Report the business metric from the trainer
- B. Cap the search with a trial count and a parallel budget
- C. Run a hyperparameter tuning job
- D. Choose Bayesian optimisation for the search

### 47. The model answers correctly but does not know this month's product catalogue. What should be done first?

- A. Start with prompt and context engineering
- B. Fine-tune the full model
- C. Ground the prompt with retrieval instead of fine-tuning
- D. Fine-tune with a parameter-efficient adapter

### 48. A 30-billion-parameter model must train synchronously across a tightly coupled fabric. What should be used?

- A. Serve on CPU only
- B. Serve on L4 GPUs
- C. Train on A100 GPUs
- D. Train on a TPU slice

### 49. A long job must survive preemption across eight replicas. Which two settings are required? Select two.

- A. Serve on CPU only
- B. Checkpoint to Cloud Storage and resume from the last step
- C. Configure the job as multi-worker with a chief
- D. Use data parallelism
- E. Scale the batch size with the worker count

---

## Domain 4 — Serving and scaling models (Serving, Packaging, and Scaling Endpoints)

### 50. Twelve million records must be scored once a night with no latency requirement. What should be used?

- A. Send the events to a streaming prediction path
- B. Deploy to an online endpoint
- C. Run batch prediction
- D. Batch the requests inside the client

### 51. A checkout risk score must answer in under 100 ms, including after a quiet period. Which two choices apply? Select two.

- A. Send the events to a streaming prediction path
- B. Deploy to an online endpoint
- C. Enable autoscaling on the endpoint
- D. Run batch prediction
- E. Set a minimum replica count

### 52. Each transaction must be scored as it arrives rather than on a schedule. What should be used?

- A. Send the events to a streaming prediction path
- B. Batch the requests inside the client
- C. Run batch prediction
- D. Deploy to an online endpoint

### 53. A model needs bespoke postprocessing that must run inside the serving container. What should be added?

- A. Push the serving image to Artifact Registry
- B. Deploy the version and move the alias
- C. Add a custom prediction routine to the container
- D. Use a prebuilt serving container

### 54. A serving image must be stored with IAM and vulnerability metadata. Where should it go?

- A. Attach a GPU to the serving replica
- B. Register the model in Agent Platform Model Registry
- C. Push the serving image to Artifact Registry
- D. Run a custom container on Agent Platform

### 55. A rollback must be a pointer move rather than a redeploy. What should be used?

- A. Deploy blue/green with an instant switch
- B. Split traffic between two deployed versions
- C. Register the model in Agent Platform Model Registry
- D. Deploy the version and move the alias

### 56. Model versions and their metrics must live in one catalog the team can browse. What should be used?

- A. Push the serving image to Artifact Registry
- B. Track artifacts and lineage in ML Metadata
- C. Log the run to Agent Platform Experiments
- D. Register the model in Agent Platform Model Registry

### 57. Two model versions must be compared on the same population with a defined share each. Which two controls apply? Select two.

- A. Split traffic between two models in an A/B test
- B. Serve the feature from the online store
- C. Replace the model version in place
- D. Run batch prediction
- E. Split traffic between two deployed versions

### 58. A low-risk internal model can be replaced in place with no comparison needed. What strategy is described?

- A. Split traffic between two models in an A/B test
- B. Roll out a canary with a small traffic share
- C. Replace the model version in place
- D. Run the new model in shadow mode

### 59. The feature is computed by different code in the notebook and the endpoint. What should be done?

- A. Keep the preprocessing inside the exported model
- B. Share one transformation library between training and serving
- C. Register the feature in Agent Platform Feature Store
- D. Add an explicit data validation step

### 60. Preprocessing must not be able to drift because the endpoint never runs it separately. What should be used?

- A. Deploy the version and move the alias
- B. Register the feature in Agent Platform Feature Store
- C. Share one transformation library between training and serving
- D. Keep the preprocessing inside the exported model

### 61. A hospital model may be reachable only from the project VPC. What should be deployed?

- A. Use a dedicated endpoint
- B. Deploy with a private endpoint only
- C. Enable autoscaling on the endpoint
- D. Use a shared public endpoint

### 62. A model needs its own capacity so another team's traffic cannot starve it. What should be used?

- A. Deploy with a private endpoint only
- B. Split traffic between two deployed versions
- C. Use a shared public endpoint
- D. Use a dedicated endpoint

### 63. A vision model must answer in 40 ms and CPU inference takes 300 ms. What should be used?

- A. Serve on CPU only
- B. Raise the concurrency per replica
- C. Attach a GPU to the serving replica
- D. Deploy to an Edge TPU device

### 64. A camera on a remote site has no reliable network and must classify on-device. What should be used?

- A. Enable autoscaling on the endpoint
- B. Serve on CPU only
- C. Deploy to an Edge TPU device
- D. Attach a GPU to the serving replica

### 65. An endpoint throttles at peak while each replica sits half idle. Which two settings address that? Select two.

- A. Raise the concurrency per replica
- B. Raise the maximum replica count
- C. Attach a GPU to the serving replica
- D. Set a minimum replica count
- E. Batch the requests inside the client

### 66. Traffic varies tenfold across the day and capacity should follow it. What should be enabled?

- A. Raise the concurrency per replica
- B. Set a minimum replica count
- C. Raise the maximum replica count
- D. Enable autoscaling on the endpoint

### 67. A caller can wait 200 ms and pays for per-request overhead on tiny payloads. What should the client do?

- A. Batch the requests inside the client
- B. Enable autoscaling on the endpoint
- C. Raise the concurrency per replica
- D. Run batch prediction

### 68. An endpoint must return per-prediction attributions and stay warm overnight. Which two settings apply? Select two.

- A. Batch the requests inside the client
- B. Set a minimum replica count
- C. Push the serving image to Artifact Registry
- D. Configure explanation metadata for the endpoint
- E. Deploy the version and move the alias

### 69. Cost per request must fall on an endpoint that is correct but over-provisioned. What should be tuned first?

- A. Raise the concurrency per replica
- B. Batch the requests inside the client
- C. Raise the maximum replica count
- D. Attach a GPU to the serving replica

---

## Domain 5 — Automating and orchestrating ML pipelines (Pipelines, Retraining, and CI/CD/CT)

### 70. A bad batch once reached training and produced a nonsense model. What should the pipeline add?

- A. Gate the deployment on a model evaluation threshold
- B. Deduplicate on the event key in the ingestion step
- C. Enable step caching
- D. Add an explicit data validation step

### 71. A new model must not reach production unless it beats the incumbent. What should the pipeline add?

- A. Add an explicit data validation step
- B. Retrain when the production metric drops
- C. Enable step caching
- D. Gate the deployment on a model evaluation threshold

### 72. The team has been tuning against the same held-out rows for months. Which two steps restore a trustworthy estimate? Select two.

- A. Enable step caching
- B. Set the random seed in the training code
- C. Inspect the confusion matrix at the operating threshold
- D. Keep the test set out of every tuning decision
- E. Report ROC AUC

### 73. Every step is a container inside the ML platform and must record lineage. What should orchestrate it?

- A. Use Ray on Agent Platform for the distributed compute
- B. Trigger the build and deploy from Cloud Build
- C. Orchestrate the steps in Agent Platform Pipelines
- D. Orchestrate with Managed Service for Apache Airflow

### 74. A Python-native distributed workload does not fit a container-per-step pipeline. What should be used?

- A. Orchestrate the steps in Agent Platform Pipelines
- B. Orchestrate with Managed Service for Apache Airflow
- C. Express the workflow as a Kubeflow pipeline
- D. Use Ray on Agent Platform for the distributed compute

### 75. Build, test, and deploy must run in one recorded, reproducible job. What should be used?

- A. Orchestrate the steps in Agent Platform Pipelines
- B. Trigger the build and deploy from Cloud Build
- C. Orchestrate with Managed Service for Apache Airflow
- D. Add a Cloud Scheduler trigger to the pipeline

### 76. A retraining pipeline must start every Monday at 02:00. What should be added?

- A. Add a Cloud Scheduler trigger to the pipeline
- B. Trigger the build and deploy from Cloud Build
- C. Trigger the pipeline from the arrival of new data
- D. Retrain on a fixed schedule

### 77. Training and serving must not compute a feature differently after either changes. What should be used?

- A. Deploy the version and move the alias
- B. Register the feature in Agent Platform Feature Store
- C. Enable step caching
- D. Share one transformation library between training and serving

### 78. One feature definition must serve both the pipeline and the endpoint. Which two components apply? Select two.

- A. Deduplicate on the event key in the ingestion step
- B. Preprocess in memory with pandas
- C. Register the model in Agent Platform Model Registry
- D. Serve the feature from the online store
- E. Register the feature in Agent Platform Feature Store

### 79. A nine-step pipeline reruns unchanged steps on every trigger and wastes an hour. What should be enabled?

- A. Add an explicit data validation step
- B. Enable step caching
- C. Set the random seed in the training code
- D. Share one transformation library between training and serving

### 80. Backfill training must reproduce the feature as it stood at each historical order. What should be read?

- A. Enable feature monitoring on the feature group
- B. Add a crossed feature for the interacting pair
- C. Serve the feature from the online store
- D. Read the historical features from the offline store

### 81. Input distributions move unpredictably and a calendar retrain is often too late. What policy fits?

- A. Retrain on a fixed schedule
- B. Retrain when drift crosses the threshold
- C. Retrain when the production metric drops
- D. Retrain only on a manual request

### 82. The business metric is measured weekly and is the only signal that matters. What policy fits?

- A. Retrain on a fixed schedule
- B. Retrain when drift crosses the threshold
- C. Retrain when the production metric drops
- D. Retrain only on a manual request

### 83. The model has gone stale twice because nobody remembered to trigger a retrain. What policy fits?

- A. Retrain on a fixed schedule
- B. Retrain when drift crosses the threshold
- C. Retrain when the production metric drops
- D. Retrain only on a manual request

### 84. Retraining must ride the same automated pipeline as the code changes. What should be adopted?

- A. Retrain on a fixed schedule
- B. Enable step caching
- C. Extend CI/CD into continuous training
- D. Trigger the build and deploy from Cloud Build

### 85. A retrain must start when a new labelled batch lands rather than on a clock. What should be used?

- A. Trigger the pipeline from the arrival of new data
- B. Trigger the build and deploy from Cloud Build
- C. Retrain only on a manual request
- D. Add a Cloud Scheduler trigger to the pipeline

### 86. A schema change must fail the pipeline before any compute is spent training. What should be added?

- A. Add an explicit data validation step
- B. Gate the deployment on a model evaluation threshold
- C. Retrain when drift crosses the threshold
- D. Enable step caching

### 87. A candidate that fails the acceptance test must never reach users. What should the pipeline add?

- A. Enable step caching
- B. Add an explicit data validation step
- C. Retrain only on a manual request
- D. Gate the deployment on a model evaluation threshold

---

## Domain 6 — Monitoring AI solutions (Responsible AI, Monitoring, and Drift)

### 88. A customer-facing assistant must resist prompt injection and block harmful output. Which two controls apply? Select two.

- A. Configure the model safety filters
- B. Put the boundary in the system instruction
- C. Constrain the response to a JSON schema
- D. Redact the pattern-matchable fields with a regex
- E. Screen the prompts and responses with Model Armor

### 89. A known account-number pattern must never reach the model prompt. What should be applied first?

- A. Constrain the response to a JSON schema
- B. Screen the prompts and responses with Model Armor
- C. Put the boundary in the system instruction
- D. Redact the pattern-matchable fields with a regex

### 90. The integration expects typed fields and the model replies in sentences. What should be configured?

- A. Put the boundary in the system instruction
- B. Constrain the response to a JSON schema
- C. Screen the prompts and responses with Model Armor
- D. Configure the model safety filters

### 91. The same model must be tracked for disparate impact after launch. What should be enabled?

- A. Publish a model card with the intended use and limits
- B. Monitor the outcome rate across the protected groups
- C. Slice the evaluation metrics by the sensitive attribute
- D. Document the dataset with a data card

### 92. The aggregate error rate looks fine but one group may be worse off. What should be produced?

- A. Document the dataset with a data card
- B. Publish a model card with the intended use and limits
- C. Slice the evaluation metrics by the sensitive attribute
- D. Monitor the outcome rate across the protected groups

### 93. A reviewer asks which features matter most across the whole BigQuery ML model. What should be used?

- A. Publish a model card with the intended use and limits
- B. Use integrated gradients for the image model
- C. Summarise the model with ML.GLOBAL_EXPLAIN
- D. Explain with Shapley values

### 94. An image classifier must show which pixels drove one prediction. What should be used?

- A. Explain with Shapley values
- B. Read the contribution of each feature with ML.EXPLAIN_PREDICT
- C. Use integrated gradients for the image model
- D. Use sampled Shapley on the endpoint

### 95. A deployed model must be compared continuously with its training baseline. What should be enabled?

- A. Track tokens and cost per request
- B. Track p95 latency per model version
- C. Log the prompt and response with redaction
- D. Enable Model Monitoring on the endpoint

### 96. A drift alert fires every night and the team has stopped reading it. What should be revisited?

- A. Track p95 latency per model version
- B. Set the monitoring threshold from the acceptable error budget
- C. Route the monitoring alert to the owning team
- D. Score a sample of live answers with the evaluation rubric

### 97. Accuracy fell over a year although the inputs look unchanged. Which two practices explain and detect that? Select two.

- A. Watch for feature attribution drift
- B. Watch for data drift
- C. Join the delayed ground truth back to the predictions
- D. Watch for concept drift
- E. Watch the prediction distribution

### 98. A model performs well offline and badly the moment it is deployed. What should be investigated?

- A. Watch for concept drift
- B. Watch for training-serving skew
- C. Watch for data drift
- D. Watch for feature attribution drift

### 99. A generative assistant answers plausibly but quality quietly declined after a model update. What should be added?

- A. Enable Model Monitoring on the endpoint
- B. Track tokens and cost per request
- C. Score a sample of live answers with the evaluation rubric
- D. Track p95 latency per model version

### 100. A bad answer was reported by a user and the team cannot reconstruct it. What should be added?

- A. Track tokens and cost per request
- B. Track p95 latency per model version
- C. Log the prompt and response with redaction
- D. Enable Model Monitoring on the endpoint

---

## Answer key and explanations

### Question 1 — A

Answer: Create a BigQuery ML ARIMA_PLUS time series model. ARIMA_PLUS models seasonality and trend and returns a forecast interval per period. Local study-map skill 1.1 (BigQuery ML Model Building), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: ARIMA_PLUS models seasonality and trend and returns a forecast interval per period.
- **B:** Incorrect for this question. Logistic regression predicts a binary outcome and trains inside BigQuery with SQL. Why the correct answer wins: ARIMA_PLUS models seasonality and trend and returns a forecast interval per period.
- **C:** Incorrect for this question. K-means segments rows into unsupervised clusters without a labelled target. Why the correct answer wins: ARIMA_PLUS models seasonality and trend and returns a forecast interval per period.
- **D:** Incorrect for this question. Boosted trees capture non-linear interactions in tabular data while staying in SQL. Why the correct answer wins: ARIMA_PLUS models seasonality and trend and returns a forecast interval per period.

### Question 2 — A, E

Answers: Create a BigQuery ML logistic regression model; Inspect the metrics with ML.EVALUATE. Logistic regression predicts a binary outcome, and ML.EVALUATE returns the metrics against a labelled dataset. Logistic regression predicts a binary outcome and trains inside BigQuery with SQL. ML.EVALUATE returns the model metrics against a labelled dataset. Local study-map skill 1.1 (BigQuery ML Model Building), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. Logistic regression predicts a binary outcome and trains inside BigQuery with SQL. In this case: Logistic regression predicts a binary outcome, and ML.EVALUATE returns the metrics against a labelled dataset.
- **B:** Incorrect for this question. K-means segments rows into unsupervised clusters without a labelled target. Why the correct answer wins: Logistic regression predicts a binary outcome, and ML.EVALUATE returns the metrics against a labelled dataset.
- **C:** Incorrect for this question. Importing brings an already-trained model into BigQuery so SQL can score it. Why the correct answer wins: Logistic regression predicts a binary outcome, and ML.EVALUATE returns the metrics against a labelled dataset.
- **D:** Incorrect for this question. A nested column keeps per-row structured output such as labels and scores together. Why the correct answer wins: Logistic regression predicts a binary outcome, and ML.EVALUATE returns the metrics against a labelled dataset.
- **E:** Correct. ML.EVALUATE returns the model metrics against a labelled dataset. In this case: Logistic regression predicts a binary outcome, and ML.EVALUATE returns the metrics against a labelled dataset.

### Question 3 — A

Answer: Declare the feature transformations in the TRANSFORM clause. TRANSFORM keeps preprocessing inside the model, so prediction applies the same steps. Local study-map skill 1.2 (BigQuery ML Feature Engineering and Prediction), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: TRANSFORM keeps preprocessing inside the model, so prediction applies the same steps.
- **B:** Incorrect for this question. ML.GLOBAL_EXPLAIN ranks the features that matter most across the whole model. Why the correct answer wins: TRANSFORM keeps preprocessing inside the model, so prediction applies the same steps.
- **C:** Incorrect for this question. ML.PREDICT applies a trained model and returns the label and its probability. Why the correct answer wins: TRANSFORM keeps preprocessing inside the model, so prediction applies the same steps.
- **D:** Incorrect for this question. Training consumes slots, so a reservation bounds the cost and the wait time. Why the correct answer wins: TRANSFORM keeps preprocessing inside the model, so prediction applies the same steps.

### Question 4 — B

Answer: Score the rows with ML.PREDICT. ML.PREDICT applies a trained model and returns the label and its probability. Local study-map skill 1.2 (BigQuery ML Feature Engineering and Prediction), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. ML.EVALUATE returns the model metrics against a labelled dataset. Why the correct answer wins: ML.PREDICT applies a trained model and returns the label and its probability.
- **B:** Correct. In this case: ML.PREDICT applies a trained model and returns the label and its probability.
- **C:** Incorrect for this question. Importing brings an already-trained model into BigQuery so SQL can score it. Why the correct answer wins: ML.PREDICT applies a trained model and returns the label and its probability.
- **D:** Incorrect for this question. ML.EXPLAIN_PREDICT attributes each prediction to the features that moved it. Why the correct answer wins: ML.PREDICT applies a trained model and returns the label and its probability.

### Question 5 — D

Answer: Use AutoML so the team needs no modelling code. AutoML is the no-code path, which matters when the team has data skills but no ML engineers. Local study-map skill 1.3 (Agent Platform AutoML), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Export produces a container-ready artifact that can be served outside the managed endpoint. Why the correct answer wins: AutoML is the no-code path, which matters when the team has data skills but no ML engineers.
- **B:** Incorrect for this question. A node-hour budget caps how long AutoML searches, which bounds the cost. Why the correct answer wins: AutoML is the no-code path, which matters when the team has data skills but no ML engineers.
- **C:** Incorrect for this question. Custom training keeps full control of the framework and the loss. Why the correct answer wins: AutoML is the no-code path, which matters when the team has data skills but no ML engineers.
- **D:** Correct. In this case: AutoML is the no-code path, which matters when the team has data skills but no ML engineers.

### Question 6 — B

Answer: Define a manual split column with train, validation, and test. A manual split is required when the split must follow a grouping column. Local study-map skill 1.3 (Agent Platform AutoML), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A node-hour budget caps how long AutoML searches, which bounds the cost. Why the correct answer wins: A manual split is required when the split must follow a grouping column.
- **B:** Correct. In this case: A manual split is required when the split must follow a grouping column.
- **C:** Incorrect for this question. Turning early stopping off for the last run lets the model use the full budget. Why the correct answer wins: A manual split is required when the split must follow a grouping column.
- **D:** Incorrect for this question. AutoML uses a reproducible default split when the dataset is large enough to do so. Why the correct answer wins: A manual split is required when the split must follow a grouping column.

### Question 7 — B

Answer: Fine-tune a Gemini model from BigQuery. Fine-tuning adapts a foundation model to the domain using rows that stay in BigQuery. Local study-map skill 1.4 (Gemini Fine-Tuning with BigQuery), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A remote model calls the Gemini endpoint from SQL, so generation runs where the data lives. Why the correct answer wins: Fine-tuning adapts a foundation model to the domain using rows that stay in BigQuery.
- **B:** Correct. In this case: Fine-tuning adapts a foundation model to the domain using rows that stay in BigQuery.
- **C:** Incorrect for this question. A better prompt is the cheapest experiment and often removes the need to tune at all. Why the correct answer wins: Fine-tuning adapts a foundation model to the domain using rows that stay in BigQuery.
- **D:** Incorrect for this question. Retrieval is the cheaper answer when the problem is missing knowledge rather than missing behaviour. Why the correct answer wins: Fine-tuning adapts a foundation model to the domain using rows that stay in BigQuery.

### Question 8 — A

Answer: Select the model from Model Garden. Model Garden lists first-party and open models with their deployment and licensing options. Local study-map skill 1.5 (Model Garden Model Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Model Garden lists first-party and open models with their deployment and licensing options.
- **B:** Incorrect for this question. An open-weight model can be tuned and self-hosted when a proprietary endpoint does not fit. Why the correct answer wins: Model Garden lists first-party and open models with their deployment and licensing options.
- **C:** Incorrect for this question. Embeddings turn text into vectors, which is what a retrieval step searches. Why the correct answer wins: Model Garden lists first-party and open models with their deployment and licensing options.
- **D:** Incorrect for this question. The larger model gives the best reasoning quality at a higher cost per token. Why the correct answer wins: Model Garden lists first-party and open models with their deployment and licensing options.

### Question 9 — B

Answer: Use Document AI with a specialised processor. A Document AI processor extracts structured fields from forms with layout awareness. Local study-map skill 1.6 (Industry AI APIs), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The prebuilt Vision model labels, detects, and reads text without training a model. Why the correct answer wins: A Document AI processor extracts structured fields from forms with layout awareness.
- **B:** Correct. In this case: A Document AI processor extracts structured fields from forms with layout awareness.
- **C:** Incorrect for this question. The translation model handles a large language set without custom training. Why the correct answer wins: A Document AI processor extracts structured fields from forms with layout awareness.
- **D:** Incorrect for this question. The speech model transcribes audio, including domain phrases through adaptation. Why the correct answer wins: A Document AI processor extracts structured fields from forms with layout awareness.

### Question 10 — B

Answer: Call the prebuilt API rather than training a model. When the task is a standard perception task, the prebuilt API is faster and cheaper than training. Local study-map skill 1.6 (Industry AI APIs), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A multimodal request removes the need for a separate captioning or OCR stage. Why the correct answer wins: When the task is a standard perception task, the prebuilt API is faster and cheaper than training.
- **B:** Correct. In this case: When the task is a standard perception task, the prebuilt API is faster and cheaper than training.
- **C:** Incorrect for this question. AutoML image trains classification or object detection from labelled images. Why the correct answer wins: When the task is a standard perception task, the prebuilt API is faster and cheaper than training.
- **D:** Incorrect for this question. An open-weight model can be tuned and self-hosted when a proprietary endpoint does not fit. Why the correct answer wins: When the task is a standard perception task, the prebuilt API is faster and cheaper than training.

### Question 11 — C, E

Answers: Cache the long shared context; Send the offline work through the batch API. Caching bills the repeated prefix once, and the batch path trades latency for a lower price. Context caching bills the repeated prefix once instead of on every request. The batch path trades latency for a lower price on non-interactive requests. Local study-map skill 1.7 (Gemini Application Optimization), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The larger model gives the best reasoning quality at a higher cost per token. Why the correct answer wins: Caching bills the repeated prefix once, and the batch path trades latency for a lower price.
- **B:** Incorrect for this question. Throughput is capped by quota, so a quota ceiling cannot be solved by retries. Why the correct answer wins: Caching bills the repeated prefix once, and the batch path trades latency for a lower price.
- **C:** Correct. Context caching bills the repeated prefix once instead of on every request. In this case: Caching bills the repeated prefix once, and the batch path trades latency for a lower price.
- **D:** Incorrect for this question. Streaming improves perceived latency without reducing total generation time. Why the correct answer wins: Caching bills the repeated prefix once, and the batch path trades latency for a lower price.
- **E:** Correct. The batch path trades latency for a lower price on non-interactive requests. In this case: Caching bills the repeated prefix once, and the batch path trades latency for a lower price.

### Question 12 — B

Answer: Fall back to a smaller model when the primary is throttled. A fallback keeps the application answering when the primary model is throttled. Local study-map skill 1.7 (Gemini Application Optimization), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A regional endpoint removes cross-region latency and satisfies residency rules. Why the correct answer wins: A fallback keeps the application answering when the primary model is throttled.
- **B:** Correct. In this case: A fallback keeps the application answering when the primary model is throttled.
- **C:** Incorrect for this question. The larger model gives the best reasoning quality at a higher cost per token. Why the correct answer wins: A fallback keeps the application answering when the primary model is throttled.
- **D:** Incorrect for this question. Throughput is capped by quota, so a quota ceiling cannot be solved by retries. Why the correct answer wins: A fallback keeps the application answering when the primary model is throttled.

### Question 13 — A

Answer: Preprocess in BigQuery with SQL. SQL over BigQuery is the cheapest option when the data already sits there and the logic is set-based. Local study-map skill 2.1 (Preprocessing Tool Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: SQL over BigQuery is the cheapest option when the data already sits there and the logic is set-based.
- **B:** Incorrect for this question. In-memory processing is the simplest option and stops working once the data exceeds the worker memory. Why the correct answer wins: SQL over BigQuery is the cheapest option when the data already sits there and the logic is set-based.
- **C:** Incorrect for this question. Dataflow runs the same Beam code in batch and streaming and scales without provisioning. Why the correct answer wins: SQL over BigQuery is the cheapest option when the data already sits there and the logic is set-based.
- **D:** Incorrect for this question. Spark suits large transformations the team already has as Scala or PySpark code. Why the correct answer wins: SQL over BigQuery is the cheapest option when the data already sits there and the logic is set-based.

### Question 14 — A, C

Answers: De-identify the fields with Sensitive Data Protection; Split the data by time rather than at random. Sensitive Data Protection removes the identifiers, and a time-based split prevents learning from the future. Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts PII. A time-based split prevents the model from learning from the future. Local study-map skill 2.1 (Preprocessing Tool Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts PII. In this case: Sensitive Data Protection removes the identifiers, and a time-based split prevents learning from the future.
- **B:** Incorrect for this question. A crossed feature lets a linear model express the interaction it cannot learn alone. Why the correct answer wins: Sensitive Data Protection removes the identifiers, and a time-based split prevents learning from the future.
- **C:** Correct. A time-based split prevents the model from learning from the future. In this case: Sensitive Data Protection removes the identifiers, and a time-based split prevents learning from the future.
- **D:** Incorrect for this question. AutoML uses a reproducible default split when the dataset is large enough to do so. Why the correct answer wins: Sensitive Data Protection removes the identifiers, and a time-based split prevents learning from the future.
- **E:** Incorrect for this question. A salted hash keeps the join key usable while removing the direct identifier. Why the correct answer wins: Sensitive Data Protection removes the identifiers, and a time-based split prevents learning from the future.

### Question 15 — A

Answer: Preprocess in memory with pandas. In-memory processing is simplest for exploration while the data still fits in memory. In-memory processing is the simplest option and stops working once the data exceeds the worker memory. Local study-map skill 2.1 (Preprocessing Tool Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In-memory processing is the simplest option and stops working once the data exceeds the worker memory. In this case: In-memory processing is simplest for exploration while the data still fits in memory.
- **B:** Incorrect for this question. SQL over BigQuery is the cheapest option when the data already sits there and the logic is set-based. Why the correct answer wins: In-memory processing is simplest for exploration while the data still fits in memory.
- **C:** Incorrect for this question. Dataplex discovers, profiles, and applies policy across the lakehouse in one control plane. Why the correct answer wins: In-memory processing is simplest for exploration while the data still fits in memory.
- **D:** Incorrect for this question. Dataflow runs the same Beam code in batch and streaming and scales without provisioning. Why the correct answer wins: In-memory processing is simplest for exploration while the data still fits in memory.

### Question 16 — A

Answer: Register the feature in Agent Platform Feature Store. Feature Store keeps one definition that both training and serving read. Local study-map skill 2.2 (Feature Store), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Feature Store keeps one definition that both training and serving read.
- **B:** Incorrect for this question. Scaling keeps one large-magnitude feature from dominating the gradient. Why the correct answer wins: Feature Store keeps one definition that both training and serving read.
- **C:** Incorrect for this question. A crossed feature lets a linear model express the interaction it cannot learn alone. Why the correct answer wins: Feature Store keeps one definition that both training and serving read.
- **D:** Incorrect for this question. A streaming path keeps the training data current without a nightly copy. Why the correct answer wins: Feature Store keeps one definition that both training and serving read.

### Question 17 — A

Answer: Read the historical features from the offline store. The offline store returns point-in-time values for training. Local study-map skill 2.2 (Feature Store), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: The offline store returns point-in-time values for training.
- **B:** Incorrect for this question. The online store returns the latest feature value at low latency for a single entity. Why the correct answer wins: The offline store returns point-in-time values for training.
- **C:** Incorrect for this question. Feature monitoring reports distribution changes per feature, not just per model. Why the correct answer wins: The offline store returns point-in-time values for training.
- **D:** Incorrect for this question. Bucketing converts a non-linear relationship into a form a linear model can fit. Why the correct answer wins: The offline store returns point-in-time values for training.

### Question 18 — C

Answer: Hash the identifiers with a salted key before training. A salted hash keeps the join key usable while removing the direct identifier. Local study-map skill 2.3 (PII Handling and Data Privacy), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts PII. Why the correct answer wins: A salted hash keeps the join key usable while removing the direct identifier.
- **B:** Incorrect for this question. Dropping the field removes the exposure entirely when the model does not need it. Why the correct answer wins: A salted hash keeps the join key usable while removing the direct identifier.
- **C:** Correct. In this case: A salted hash keeps the join key usable while removing the direct identifier.
- **D:** Incorrect for this question. Restricting the bucket limits who can copy the raw data in the first place. Why the correct answer wins: A salted hash keeps the join key usable while removing the direct identifier.

### Question 19 — A

Answer: Restrict the raw bucket to a privileged service account. Restricting the bucket limits who can copy the raw data in the first place. Local study-map skill 2.3 (PII Handling and Data Privacy), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Restricting the bucket limits who can copy the raw data in the first place.
- **B:** Incorrect for this question. Dropping the field removes the exposure entirely when the model does not need it. Why the correct answer wins: Restricting the bucket limits who can copy the raw data in the first place.
- **C:** Incorrect for this question. Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts PII. Why the correct answer wins: Restricting the bucket limits who can copy the raw data in the first place.
- **D:** Incorrect for this question. Dataplex discovers, profiles, and applies policy across the lakehouse in one control plane. Why the correct answer wins: Restricting the bucket limits who can copy the raw data in the first place.

### Question 20 — D

Answer: Create the runtime with no public IP. A private-IP runtime reaches the data through the VPC and cannot be opened from the internet. Local study-map skill 2.4 (Notebook Environments and Security), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A pinned image makes the environment reproducible across users. Why the correct answer wins: A private-IP runtime reaches the data through the VPC and cannot be opened from the internet.
- **B:** Incorrect for this question. Idle shutdown stops paying for a notebook nobody is using. Why the correct answer wins: A private-IP runtime reaches the data through the VPC and cannot be opened from the internet.
- **C:** Incorrect for this question. The subnet attachment gives the notebook the route to internal data sources. Why the correct answer wins: A private-IP runtime reaches the data through the VPC and cannot be opened from the internet.
- **D:** Correct. In this case: A private-IP runtime reaches the data through the VPC and cannot be opened from the internet.

### Question 21 — B

Answer: Set an idle shutdown schedule. Idle shutdown stops paying for a notebook nobody is using. Local study-map skill 2.4 (Notebook Environments and Security), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A pinned image makes the environment reproducible across users. Why the correct answer wins: Idle shutdown stops paying for a notebook nobody is using.
- **B:** Correct. In this case: Idle shutdown stops paying for a notebook nobody is using.
- **C:** Incorrect for this question. Workbench is the managed notebook instance inside the project VPC. Why the correct answer wins: Idle shutdown stops paying for a notebook nobody is using.
- **D:** Incorrect for this question. A private-IP runtime reaches the data through the VPC and cannot be opened from the internet. Why the correct answer wins: Idle shutdown stops paying for a notebook nobody is using.

### Question 22 — A

Answer: Log the run to Agent Platform Experiments. Experiments records parameters, metrics, and artifacts per run so runs can be compared. Local study-map skill 2.5 (Experiment Tracking), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Experiments records parameters, metrics, and artifacts per run so runs can be compared.
- **B:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: Experiments records parameters, metrics, and artifacts per run so runs can be compared.
- **C:** Incorrect for this question. ML Metadata records which data and code produced which artifact. Why the correct answer wins: Experiments records parameters, metrics, and artifacts per run so runs can be compared.
- **D:** Incorrect for this question. A fixed seed makes a rerun reproducible when the rest of the environment is pinned. Why the correct answer wins: Experiments records parameters, metrics, and artifacts per run so runs can be compared.

### Question 23 — A

Answer: Set the random seed in the training code. A fixed seed makes a rerun reproducible when the rest of the environment is pinned. Local study-map skill 2.5 (Experiment Tracking), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: A fixed seed makes a rerun reproducible when the rest of the environment is pinned.
- **B:** Incorrect for this question. Kubeflow pipelines give a container-per-step pipeline that runs on the managed service or on GKE. Why the correct answer wins: A fixed seed makes a rerun reproducible when the rest of the environment is pinned.
- **C:** Incorrect for this question. ML Metadata records which data and code produced which artifact. Why the correct answer wins: A fixed seed makes a rerun reproducible when the rest of the environment is pinned.
- **D:** Incorrect for this question. Experiments records parameters, metrics, and artifacts per run so runs can be compared. Why the correct answer wins: A fixed seed makes a rerun reproducible when the rest of the environment is pinned.

### Question 24 — C, D

Answers: Start from a Google-provided pipeline template; Express the workflow as a Kubeflow pipeline. A template encodes the validated step order, and a container-per-step pipeline runs it on the managed service. A template encodes the validated step order, so the first pipeline is not bespoke. Kubeflow pipelines give a container-per-step pipeline that runs on the managed service or on GKE. Local study-map skill 2.6 (Development Environment Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Experiments records parameters, metrics, and artifacts per run so runs can be compared. Why the correct answer wins: A template encodes the validated step order, and a container-per-step pipeline runs it on the managed service.
- **B:** Incorrect for this question. A pinned image makes the environment reproducible across users. Why the correct answer wins: A template encodes the validated step order, and a container-per-step pipeline runs it on the managed service.
- **C:** Correct. Kubeflow pipelines give a container-per-step pipeline that runs on the managed service or on GKE. In this case: A template encodes the validated step order, and a container-per-step pipeline runs it on the managed service.
- **D:** Correct. A template encodes the validated step order, so the first pipeline is not bespoke. In this case: A template encodes the validated step order, and a container-per-step pipeline runs it on the managed service.
- **E:** Incorrect for this question. Airflow expresses cross-system dependencies and schedules outside the ML platform. Why the correct answer wins: A template encodes the validated step order, and a container-per-step pipeline runs it on the managed service.

### Question 25 — A

Answer: Orchestrate with Managed Service for Apache Airflow. Airflow expresses cross-system dependencies and schedules outside the ML platform. Local study-map skill 2.6 (Development Environment Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Airflow expresses cross-system dependencies and schedules outside the ML platform.
- **B:** Incorrect for this question. Kubeflow pipelines give a container-per-step pipeline that runs on the managed service or on GKE. Why the correct answer wins: Airflow expresses cross-system dependencies and schedules outside the ML platform.
- **C:** Incorrect for this question. Pipelines runs each step as a container with caching, lineage, and retry. Why the correct answer wins: Airflow expresses cross-system dependencies and schedules outside the ML platform.
- **D:** Incorrect for this question. Ray fits a Python-native distributed workload that is not a container-per-step pipeline. Why the correct answer wins: Airflow expresses cross-system dependencies and schedules outside the ML platform.

### Question 26 — A, D

Answers: Report precision-recall AUC for the rare class; Inspect the confusion matrix at the operating threshold. Precision-recall AUC stays informative when positives are rare, and the matrix shows the error split at the threshold. Precision-recall AUC stays informative when the positive class is rare. The matrix shows the false-positive and false-negative split the business will feel. Local study-map skill 2.7 (Evaluation Metrics and LLM-as-a-Judge), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. The matrix shows the false-positive and false-negative split the business will feel. In this case: Precision-recall AUC stays informative when positives are rare, and the matrix shows the error split at the threshold.
- **B:** Incorrect for this question. RMSE expresses the typical error in the units of the target. Why the correct answer wins: Precision-recall AUC stays informative when positives are rare, and the matrix shows the error split at the threshold.
- **C:** Incorrect for this question. MAPE expresses the error relative to the actual value, which business readers understand. Why the correct answer wins: Precision-recall AUC stays informative when positives are rare, and the matrix shows the error split at the threshold.
- **D:** Correct. Precision-recall AUC stays informative when the positive class is rare. In this case: Precision-recall AUC stays informative when positives are rare, and the matrix shows the error split at the threshold.
- **E:** Incorrect for this question. ROC AUC measures ranking quality across thresholds and hides class imbalance. Why the correct answer wins: Precision-recall AUC stays informative when positives are rare, and the matrix shows the error split at the threshold.

### Question 27 — C

Answer: Score the answers with an LLM-as-a-judge rubric. A rubric-driven judge scales the evaluation of free-text answers beyond human review. Local study-map skill 2.7 (Evaluation Metrics and LLM-as-a-Judge), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A fixed prompt set makes the safety score comparable between releases. Why the correct answer wins: A rubric-driven judge scales the evaluation of free-text answers beyond human review.
- **B:** Incorrect for this question. Groundedness checks whether each claim is supported by the documents that were retrieved. Why the correct answer wins: A rubric-driven judge scales the evaluation of free-text answers beyond human review.
- **C:** Correct. In this case: A rubric-driven judge scales the evaluation of free-text answers beyond human review.
- **D:** Incorrect for this question. Human review remains the reference standard for a sample the judge is calibrated against. Why the correct answer wins: A rubric-driven judge scales the evaluation of free-text answers beyond human review.

### Question 28 — A

Answer: Track artifacts and lineage in ML Metadata. ML Metadata records which data and code produced which artifact. Local study-map skill 2.8 (Metadata and Lineage), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: ML Metadata records which data and code produced which artifact.
- **B:** Incorrect for this question. Experiments records parameters, metrics, and artifacts per run so runs can be compared. Why the correct answer wins: ML Metadata records which data and code produced which artifact.
- **C:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: ML Metadata records which data and code produced which artifact.
- **D:** Incorrect for this question. The registry versions the model artifact and links it to its lineage and metrics. Why the correct answer wins: ML Metadata records which data and code produced which artifact.

### Question 29 — B

Answer: Choose a classical time series model. A classical time series model suits a single series with strong seasonality and little covariate data. Local study-map skill 3.1 (Model Type Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A DNN suits a large tabular or unstructured dataset where interactions matter. Why the correct answer wins: A classical time series model suits a single series with strong seasonality and little covariate data.
- **B:** Correct. In this case: A classical time series model suits a single series with strong seasonality and little covariate data.
- **C:** Incorrect for this question. TabNet gives an interpretable attentive tabular model inside custom training. Why the correct answer wins: A classical time series model suits a single series with strong seasonality and little covariate data.
- **D:** Incorrect for this question. A foundation model suits an open-ended language or multimodal task where labelled data is scarce. Why the correct answer wins: A classical time series model suits a single series with strong seasonality and little covariate data.

### Question 30 — C

Answer: Choose a foundation model. A foundation model suits an open-ended language task where labelled data is scarce. Local study-map skill 3.1 (Model Type Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. TabNet gives an interpretable attentive tabular model inside custom training. Why the correct answer wins: A foundation model suits an open-ended language task where labelled data is scarce.
- **B:** Incorrect for this question. A DNN suits a large tabular or unstructured dataset where interactions matter. Why the correct answer wins: A foundation model suits an open-ended language task where labelled data is scarce.
- **C:** Correct. In this case: A foundation model suits an open-ended language task where labelled data is scarce.
- **D:** Incorrect for this question. A classical time series model suits a single series with strong seasonality and little covariate data. Why the correct answer wins: A foundation model suits an open-ended language task where labelled data is scarce.

### Question 31 — B

Answer: Choose the product the team can actually operate. A product the team cannot debug becomes an outage with a schedule. Local study-map skill 3.2 (Product Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Custom training keeps full control of the framework and the loss. Why the correct answer wins: A product the team cannot debug becomes an outage with a schedule.
- **B:** Correct. In this case: A product the team cannot debug becomes an outage with a schedule.
- **C:** Incorrect for this question. AutoML removes architecture search and tuning from the team while keeping a managed endpoint. Why the correct answer wins: A product the team cannot debug becomes an outage with a schedule.
- **D:** Incorrect for this question. BigQuery ML keeps training next to the data and removes a separate serving pipeline. Why the correct answer wins: A product the team cannot debug becomes an outage with a schedule.

### Question 32 — D

Answer: Build the model in BigQuery ML. BigQuery ML keeps training next to the data and removes a separate serving pipeline. Local study-map skill 3.2 (Product Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Custom training keeps full control of the framework and the loss. Why the correct answer wins: BigQuery ML keeps training next to the data and removes a separate serving pipeline.
- **B:** Incorrect for this question. TabNet gives an interpretable attentive tabular model inside custom training. Why the correct answer wins: BigQuery ML keeps training next to the data and removes a separate serving pipeline.
- **C:** Incorrect for this question. AutoML removes architecture search and tuning from the team while keeping a managed endpoint. Why the correct answer wins: BigQuery ML keeps training next to the data and removes a separate serving pipeline.
- **D:** Correct. In this case: BigQuery ML keeps training next to the data and removes a separate serving pipeline.

### Question 33 — A, B

Answers: Run the new model in shadow mode; Roll out a canary with a small traffic share. Shadow mode scores live traffic without serving it, and a canary then limits the exposure. Shadow mode scores live traffic without serving its answers, so the comparison costs nothing to users. A canary limits the blast radius while the new model is compared with the old one. Local study-map skill 3.3 (Deployment Strategy Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. A canary limits the blast radius while the new model is compared with the old one. In this case: Shadow mode scores live traffic without serving it, and a canary then limits the exposure.
- **B:** Correct. Shadow mode scores live traffic without serving its answers, so the comparison costs nothing to users. In this case: Shadow mode scores live traffic without serving it, and a canary then limits the exposure.
- **C:** Incorrect for this question. Two identical deployments let the switch be reversed immediately. Why the correct answer wins: Shadow mode scores live traffic without serving it, and a canary then limits the exposure.
- **D:** Incorrect for this question. A/B testing compares two models on the same population with a traffic split. Why the correct answer wins: Shadow mode scores live traffic without serving it, and a canary then limits the exposure.
- **E:** Incorrect for this question. An in-place replacement exposes every request to the new version at once. Why the correct answer wins: Shadow mode scores live traffic without serving it, and a canary then limits the exposure.

### Question 34 — B

Answer: Deploy blue/green with an instant switch. Two identical deployments let the switch be reversed immediately. Local study-map skill 3.3 (Deployment Strategy Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A canary limits the blast radius while the new model is compared with the old one. Why the correct answer wins: Two identical deployments let the switch be reversed immediately.
- **B:** Correct. In this case: Two identical deployments let the switch be reversed immediately.
- **C:** Incorrect for this question. A/B testing compares two models on the same population with a traffic split. Why the correct answer wins: Two identical deployments let the switch be reversed immediately.
- **D:** Incorrect for this question. An in-place replacement exposes every request to the new version at once. Why the correct answer wins: Two identical deployments let the switch be reversed immediately.

### Question 35 — D

Answer: Use sampled Shapley on the endpoint. Sampled Shapley explains individual online predictions with a bounded compute cost. Local study-map skill 3.4 (Interpretability), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. ML.GLOBAL_EXPLAIN ranks the features that matter most across the whole model. Why the correct answer wins: Sampled Shapley explains individual online predictions with a bounded compute cost.
- **B:** Incorrect for this question. Integrated gradients attributes an image prediction to the pixels that moved it. Why the correct answer wins: Sampled Shapley explains individual online predictions with a bounded compute cost.
- **C:** Incorrect for this question. The card states where the model may be used and where it must not. Why the correct answer wins: Sampled Shapley explains individual online predictions with a bounded compute cost.
- **D:** Correct. In this case: Sampled Shapley explains individual online predictions with a bounded compute cost.

### Question 36 — C

Answer: Choose an inherently interpretable model. A linear or tree model can be read directly when regulation demands an explanation by construction. Local study-map skill 3.4 (Interpretability), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Sampled Shapley explains individual online predictions with a bounded compute cost. Why the correct answer wins: A linear or tree model can be read directly when regulation demands an explanation by construction.
- **B:** Incorrect for this question. Attribution shows which inputs drove the decision in the case the reviewer is examining. Why the correct answer wins: A linear or tree model can be read directly when regulation demands an explanation by construction.
- **C:** Correct. In this case: A linear or tree model can be read directly when regulation demands an explanation by construction.
- **D:** Incorrect for this question. Shapley values attribute a prediction to its features with a consistent baseline. Why the correct answer wins: A linear or tree model can be read directly when regulation demands an explanation by construction.

### Question 37 — B

Answer: Write the training data as TFRecord shards in Cloud Storage. Sharded TFRecord is the efficient read format for distributed training. Local study-map skill 3.5 (Training Data Organization), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Reading from BigQuery avoids a copy and keeps the query pushdown. Why the correct answer wins: Sharded TFRecord is the efficient read format for distributed training.
- **B:** Correct. In this case: Sharded TFRecord is the efficient read format for distributed training.
- **C:** Incorrect for this question. A streaming path keeps the training data current without a nightly copy. Why the correct answer wins: Sharded TFRecord is the efficient read format for distributed training.
- **D:** Incorrect for this question. Parquet is columnar and cheap to scan for tabular training data. Why the correct answer wins: Sharded TFRecord is the efficient read format for distributed training.

### Question 38 — D

Answer: Write the training data as Parquet in Cloud Storage. Parquet is columnar and cheap to scan for tabular training data. Local study-map skill 3.5 (Training Data Organization), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Reading from BigQuery avoids a copy and keeps the query pushdown. Why the correct answer wins: Parquet is columnar and cheap to scan for tabular training data.
- **B:** Incorrect for this question. A streaming path keeps the training data current without a nightly copy. Why the correct answer wins: Parquet is columnar and cheap to scan for tabular training data.
- **C:** Incorrect for this question. Sharded TFRecord is the efficient read format for distributed training. Why the correct answer wins: Parquet is columnar and cheap to scan for tabular training data.
- **D:** Correct. In this case: Parquet is columnar and cheap to scan for tabular training data.

### Question 39 — A

Answer: Validate the schema and quarantine rejected rows. Rejecting rows into a side table makes a schema break visible instead of silent. Local study-map skill 3.6 (Ingestion into Training Pipelines), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Rejecting rows into a side table makes a schema break visible instead of silent.
- **B:** Incorrect for this question. A streaming path keeps the training data current without a nightly copy. Why the correct answer wins: Rejecting rows into a side table makes a schema break visible instead of silent.
- **C:** Incorrect for this question. Reading from BigQuery avoids a copy and keeps the query pushdown. Why the correct answer wins: Rejecting rows into a side table makes a schema break visible instead of silent.
- **D:** Incorrect for this question. Deduplicating at ingest stops duplicated records inflating the training set. Why the correct answer wins: Rejecting rows into a side table makes a schema break visible instead of silent.

### Question 40 — A

Answer: Deduplicate on the event key in the ingestion step. Deduplicating at ingest stops duplicated records inflating the training set. Local study-map skill 3.6 (Ingestion into Training Pipelines), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Deduplicating at ingest stops duplicated records inflating the training set.
- **B:** Incorrect for this question. Rejecting rows into a side table makes a schema break visible instead of silent. Why the correct answer wins: Deduplicating at ingest stops duplicated records inflating the training set.
- **C:** Incorrect for this question. A streaming path keeps the training data current without a nightly copy. Why the correct answer wins: Deduplicating at ingest stops duplicated records inflating the training set.
- **D:** Incorrect for this question. Parquet is columnar and cheap to scan for tabular training data. Why the correct answer wins: Deduplicating at ingest stops duplicated records inflating the training set.

### Question 41 — C

Answer: Run a custom container on Agent Platform. A custom container carries its own framework and dependencies into the managed training job. Local study-map skill 3.7 (Custom Training and SDKs), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. AutoML removes architecture search and tuning from the team while keeping a managed endpoint. Why the correct answer wins: A custom container carries its own framework and dependencies into the managed training job.
- **B:** Incorrect for this question. The prebuilt container installs the package, which is the lightest way to run custom code. Why the correct answer wins: A custom container carries its own framework and dependencies into the managed training job.
- **C:** Correct. In this case: A custom container carries its own framework and dependencies into the managed training job.
- **D:** Incorrect for this question. A prebuilt container already implements the framework handler, so no serving code is written. Why the correct answer wins: A custom container carries its own framework and dependencies into the managed training job.

### Question 42 — C

Answer: Package the trainer as a Python package. The prebuilt container installs the package, which is the lightest way to run custom code. Local study-map skill 3.7 (Custom Training and SDKs), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A prebuilt container already implements the framework handler, so no serving code is written. Why the correct answer wins: The prebuilt container installs the package, which is the lightest way to run custom code.
- **B:** Incorrect for this question. A custom container carries its own framework and dependencies into the managed training job. Why the correct answer wins: The prebuilt container installs the package, which is the lightest way to run custom code.
- **C:** Correct. In this case: The prebuilt container installs the package, which is the lightest way to run custom code.
- **D:** Incorrect for this question. Export produces a container-ready artifact that can be served outside the managed endpoint. Why the correct answer wins: The prebuilt container installs the package, which is the lightest way to run custom code.

### Question 43 — B

Answer: Reduce the per-replica batch size. The out-of-memory error is a memory-per-step problem, so the batch is the first lever. Local study-map skill 3.8 (Training Failure Troubleshooting), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Accelerator quota is regional and blocks the job before the code runs. Why the correct answer wins: The out-of-memory error is a memory-per-step problem, so the batch is the first lever.
- **B:** Correct. In this case: The out-of-memory error is a memory-per-step problem, so the batch is the first lever.
- **C:** Incorrect for this question. Duplicated shards silently shrink the effective dataset and skew the loss. Why the correct answer wins: The out-of-memory error is a memory-per-step problem, so the batch is the first lever.
- **D:** Incorrect for this question. A loss that becomes NaN usually reflects a step size too large for the data scale. Why the correct answer wins: The out-of-memory error is a memory-per-step problem, so the batch is the first lever.

### Question 44 — D

Answer: Grant the training service account access to the bucket. A permission error on the input is a missing IAM binding, not a model problem. Local study-map skill 3.8 (Training Failure Troubleshooting), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A loss that becomes NaN usually reflects a step size too large for the data scale. Why the correct answer wins: A permission error on the input is a missing IAM binding, not a model problem.
- **B:** Incorrect for this question. Accelerator quota is regional and blocks the job before the code runs. Why the correct answer wins: A permission error on the input is a missing IAM binding, not a model problem.
- **C:** Incorrect for this question. A framework mismatch between local and remote runs changes behaviour without changing the code. Why the correct answer wins: A permission error on the input is a missing IAM binding, not a model problem.
- **D:** Correct. In this case: A permission error on the input is a missing IAM binding, not a model problem.

### Question 45 — D, E

Answers: Run a hyperparameter tuning job; Enable early stopping of poor trials. The tuning service searches in parallel, and early stopping frees capacity from trials that cannot win. The tuning service searches the space in parallel and reports the best trial. Local study-map skill 3.9 (Hyperparameter Tuning), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A fixed seed makes a rerun reproducible when the rest of the environment is pinned. Why the correct answer wins: The tuning service searches in parallel, and early stopping frees capacity from trials that cannot win.
- **B:** Incorrect for this question. A node-hour budget caps how long AutoML searches, which bounds the cost. Why the correct answer wins: The tuning service searches in parallel, and early stopping frees capacity from trials that cannot win.
- **C:** Incorrect for this question. The search optimises the metric the trainer reports, so it must be the one that matters. Why the correct answer wins: The tuning service searches in parallel, and early stopping frees capacity from trials that cannot win.
- **D:** Correct. The tuning service searches the space in parallel and reports the best trial. In this case: The tuning service searches in parallel, and early stopping frees capacity from trials that cannot win.
- **E:** Correct. In this case: The tuning service searches in parallel, and early stopping frees capacity from trials that cannot win.

### Question 46 — A

Answer: Report the business metric from the trainer. The search optimises the metric the trainer reports, so it must be the one that matters. Local study-map skill 3.9 (Hyperparameter Tuning), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: The search optimises the metric the trainer reports, so it must be the one that matters.
- **B:** Incorrect for this question. The budget bounds both the cost and the wall-clock time of the search. Why the correct answer wins: The search optimises the metric the trainer reports, so it must be the one that matters.
- **C:** Incorrect for this question. The tuning service searches the space in parallel and reports the best trial. Why the correct answer wins: The search optimises the metric the trainer reports, so it must be the one that matters.
- **D:** Incorrect for this question. Bayesian search spends fewer trials to reach a good configuration. Why the correct answer wins: The search optimises the metric the trainer reports, so it must be the one that matters.

### Question 47 — C

Answer: Ground the prompt with retrieval instead of fine-tuning. Retrieval is the cheaper answer when the problem is missing knowledge rather than missing behaviour. Local study-map skill 3.10 (Fine-Tuning Decisions), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A better prompt is the cheapest experiment and often removes the need to tune at all. Why the correct answer wins: Retrieval is the cheaper answer when the problem is missing knowledge rather than missing behaviour.
- **B:** Incorrect for this question. Full fine-tuning updates every weight and needs the most data and accelerator memory. Why the correct answer wins: Retrieval is the cheaper answer when the problem is missing knowledge rather than missing behaviour.
- **C:** Correct. In this case: Retrieval is the cheaper answer when the problem is missing knowledge rather than missing behaviour.
- **D:** Incorrect for this question. A parameter-efficient adapter trains a small number of weights and keeps the base model intact. Why the correct answer wins: Retrieval is the cheaper answer when the problem is missing knowledge rather than missing behaviour.

### Question 48 — D

Answer: Train on a TPU slice. A TPU slice gives a tightly coupled accelerator fabric for large synchronous training. Local study-map skill 3.11 (Hardware and Accelerator Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. CPU serving is the cheapest option for a small model with a generous latency budget. Why the correct answer wins: A TPU slice gives a tightly coupled accelerator fabric for large synchronous training.
- **B:** Incorrect for this question. An L4 GPU gives low-cost inference acceleration for a modest model. Why the correct answer wins: A TPU slice gives a tightly coupled accelerator fabric for large synchronous training.
- **C:** Incorrect for this question. A100 GPUs suit mixed-precision training where the framework expects CUDA. Why the correct answer wins: A TPU slice gives a tightly coupled accelerator fabric for large synchronous training.
- **D:** Correct. In this case: A TPU slice gives a tightly coupled accelerator fabric for large synchronous training.

### Question 49 — B, C

Answers: Configure the job as multi-worker with a chief; Checkpoint to Cloud Storage and resume from the last step. Multi-worker gives each replica a shard and a chief, and a checkpoint turns preemption into a delay. Multi-worker gives each replica a shard of the data and a defined chief. A checkpoint turns a preemption into a delay rather than a restart. Local study-map skill 3.12 (Distributed Training), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. CPU serving is the cheapest option for a small model with a generous latency budget. Why the correct answer wins: Multi-worker gives each replica a shard and a chief, and a checkpoint turns preemption into a delay.
- **B:** Correct. A checkpoint turns a preemption into a delay rather than a restart. In this case: Multi-worker gives each replica a shard and a chief, and a checkpoint turns preemption into a delay.
- **C:** Correct. Multi-worker gives each replica a shard of the data and a defined chief. In this case: Multi-worker gives each replica a shard and a chief, and a checkpoint turns preemption into a delay.
- **D:** Incorrect for this question. Data parallelism replicates the model and splits each batch across the workers. Why the correct answer wins: Multi-worker gives each replica a shard and a chief, and a checkpoint turns preemption into a delay.
- **E:** Incorrect for this question. A larger global batch keeps each worker busy after the split. Why the correct answer wins: Multi-worker gives each replica a shard and a chief, and a checkpoint turns preemption into a delay.

### Question 50 — C

Answer: Run batch prediction. Batch prediction reads a file and writes predictions without holding serving capacity. Local study-map skill 4.1 (Batch and Online Inference), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Streaming answers each event as it arrives rather than on a schedule. Why the correct answer wins: Batch prediction reads a file and writes predictions without holding serving capacity.
- **B:** Incorrect for this question. An endpoint keeps capacity ready for low-latency per-request predictions. Why the correct answer wins: Batch prediction reads a file and writes predictions without holding serving capacity.
- **C:** Correct. In this case: Batch prediction reads a file and writes predictions without holding serving capacity.
- **D:** Incorrect for this question. Batching amortises the per-request overhead when the caller can wait. Why the correct answer wins: Batch prediction reads a file and writes predictions without holding serving capacity.

### Question 51 — B, E

Answers: Deploy to an online endpoint; Set a minimum replica count. An endpoint keeps capacity ready, and a minimum replica count keeps it warm. An endpoint keeps capacity ready for low-latency per-request predictions. A minimum replica keeps capacity warm so the first request after a quiet period is fast. Local study-map skill 4.1 (Batch and Online Inference), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Streaming answers each event as it arrives rather than on a schedule. Why the correct answer wins: An endpoint keeps capacity ready, and a minimum replica count keeps it warm.
- **B:** Correct. An endpoint keeps capacity ready for low-latency per-request predictions. In this case: An endpoint keeps capacity ready, and a minimum replica count keeps it warm.
- **C:** Incorrect for this question. Autoscaling adds replicas with the traffic and removes them afterwards. Why the correct answer wins: An endpoint keeps capacity ready, and a minimum replica count keeps it warm.
- **D:** Incorrect for this question. Batch prediction reads a file or table and writes predictions without holding serving capacity. Why the correct answer wins: An endpoint keeps capacity ready, and a minimum replica count keeps it warm.
- **E:** Correct. A minimum replica keeps capacity warm so the first request after a quiet period is fast. In this case: An endpoint keeps capacity ready, and a minimum replica count keeps it warm.

### Question 52 — A

Answer: Send the events to a streaming prediction path. Streaming answers each event as it arrives rather than on a schedule. Local study-map skill 4.1 (Batch and Online Inference), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Streaming answers each event as it arrives rather than on a schedule.
- **B:** Incorrect for this question. Batching amortises the per-request overhead when the caller can wait. Why the correct answer wins: Streaming answers each event as it arrives rather than on a schedule.
- **C:** Incorrect for this question. Batch prediction reads a file or table and writes predictions without holding serving capacity. Why the correct answer wins: Streaming answers each event as it arrives rather than on a schedule.
- **D:** Incorrect for this question. An endpoint keeps capacity ready for low-latency per-request predictions. Why the correct answer wins: Streaming answers each event as it arrives rather than on a schedule.

### Question 53 — C

Answer: Add a custom prediction routine to the container. The routine runs the preprocessing and postprocessing inside the serving container. Local study-map skill 4.2 (Packaging and Custom Containers), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Artifact Registry holds the image with IAM and vulnerability metadata. Why the correct answer wins: The routine runs the preprocessing and postprocessing inside the serving container.
- **B:** Incorrect for this question. An alias decouples the served version name from the artifact id, so a rollback is a pointer move. Why the correct answer wins: The routine runs the preprocessing and postprocessing inside the serving container.
- **C:** Correct. In this case: The routine runs the preprocessing and postprocessing inside the serving container.
- **D:** Incorrect for this question. A prebuilt container already implements the framework handler, so no serving code is written. Why the correct answer wins: The routine runs the preprocessing and postprocessing inside the serving container.

### Question 54 — C

Answer: Push the serving image to Artifact Registry. Artifact Registry holds the image with IAM and vulnerability metadata. Local study-map skill 4.2 (Packaging and Custom Containers), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A GPU shortens inference time enough to meet a tight latency target. Why the correct answer wins: Artifact Registry holds the image with IAM and vulnerability metadata.
- **B:** Incorrect for this question. The registry versions the model artifact and links it to its lineage and metrics. Why the correct answer wins: Artifact Registry holds the image with IAM and vulnerability metadata.
- **C:** Correct. In this case: Artifact Registry holds the image with IAM and vulnerability metadata.
- **D:** Incorrect for this question. A custom container carries its own framework and dependencies into the managed training job. Why the correct answer wins: Artifact Registry holds the image with IAM and vulnerability metadata.

### Question 55 — D

Answer: Deploy the version and move the alias. An alias decouples the served version name from the artifact id, so a rollback is a pointer move. Local study-map skill 4.3 (Model Registry and Versioning), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Two identical deployments let the switch be reversed immediately. Why the correct answer wins: An alias decouples the served version name from the artifact id, so a rollback is a pointer move.
- **B:** Incorrect for this question. A traffic split sends a defined share to each version on the same endpoint. Why the correct answer wins: An alias decouples the served version name from the artifact id, so a rollback is a pointer move.
- **C:** Incorrect for this question. The registry versions the model artifact and links it to its lineage and metrics. Why the correct answer wins: An alias decouples the served version name from the artifact id, so a rollback is a pointer move.
- **D:** Correct. In this case: An alias decouples the served version name from the artifact id, so a rollback is a pointer move.

### Question 56 — D

Answer: Register the model in Agent Platform Model Registry. The registry versions the model artifact and links it to its lineage and metrics. Local study-map skill 4.3 (Model Registry and Versioning), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Artifact Registry holds the image with IAM and vulnerability metadata. Why the correct answer wins: The registry versions the model artifact and links it to its lineage and metrics.
- **B:** Incorrect for this question. ML Metadata records which data and code produced which artifact. Why the correct answer wins: The registry versions the model artifact and links it to its lineage and metrics.
- **C:** Incorrect for this question. Experiments records parameters, metrics, and artifacts per run so runs can be compared. Why the correct answer wins: The registry versions the model artifact and links it to its lineage and metrics.
- **D:** Correct. In this case: The registry versions the model artifact and links it to its lineage and metrics.

### Question 57 — A, E

Answers: Split traffic between two models in an A/B test; Split traffic between two deployed versions. A/B testing compares two models on one population, and the traffic split sends a defined share to each version. A/B testing compares two models on the same population with a traffic split. A traffic split sends a defined share to each version on the same endpoint. Local study-map skill 4.4 (Model Rollout Strategies), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. A/B testing compares two models on the same population with a traffic split. In this case: A/B testing compares two models on one population, and the traffic split sends a defined share to each version.
- **B:** Incorrect for this question. The online store returns the latest feature value at low latency for a single entity. Why the correct answer wins: A/B testing compares two models on one population, and the traffic split sends a defined share to each version.
- **C:** Incorrect for this question. An in-place replacement exposes every request to the new version at once. Why the correct answer wins: A/B testing compares two models on one population, and the traffic split sends a defined share to each version.
- **D:** Incorrect for this question. Batch prediction reads a file or table and writes predictions without holding serving capacity. Why the correct answer wins: A/B testing compares two models on one population, and the traffic split sends a defined share to each version.
- **E:** Correct. A traffic split sends a defined share to each version on the same endpoint. In this case: A/B testing compares two models on one population, and the traffic split sends a defined share to each version.

### Question 58 — C

Answer: Replace the model version in place. An in-place replacement exposes every request to the new version at once. Local study-map skill 4.4 (Model Rollout Strategies), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A/B testing compares two models on the same population with a traffic split. Why the correct answer wins: An in-place replacement exposes every request to the new version at once.
- **B:** Incorrect for this question. A canary limits the blast radius while the new model is compared with the old one. Why the correct answer wins: An in-place replacement exposes every request to the new version at once.
- **C:** Correct. In this case: An in-place replacement exposes every request to the new version at once.
- **D:** Incorrect for this question. Shadow mode scores live traffic without serving its answers, so the comparison costs nothing to users. Why the correct answer wins: An in-place replacement exposes every request to the new version at once.

### Question 59 — B

Answer: Share one transformation library between training and serving. Shared code removes the class of bug where the two paths compute a feature differently. Local study-map skill 4.5 (Inference Preprocessing and Postprocessing), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Preprocessing inside the artifact cannot drift between the two paths. Why the correct answer wins: Shared code removes the class of bug where the two paths compute a feature differently.
- **B:** Correct. In this case: Shared code removes the class of bug where the two paths compute a feature differently.
- **C:** Incorrect for this question. Feature Store keeps one definition that both training and serving read. Why the correct answer wins: Shared code removes the class of bug where the two paths compute a feature differently.
- **D:** Incorrect for this question. A validation step stops a bad batch before it reaches training. Why the correct answer wins: Shared code removes the class of bug where the two paths compute a feature differently.

### Question 60 — D

Answer: Keep the preprocessing inside the exported model. Preprocessing inside the artifact cannot drift between the two paths. Local study-map skill 4.5 (Inference Preprocessing and Postprocessing), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. An alias decouples the served version name from the artifact id, so a rollback is a pointer move. Why the correct answer wins: Preprocessing inside the artifact cannot drift between the two paths.
- **B:** Incorrect for this question. Feature Store keeps one definition that both training and serving read. Why the correct answer wins: Preprocessing inside the artifact cannot drift between the two paths.
- **C:** Incorrect for this question. Shared code removes the class of bug where the two paths compute a feature differently. Why the correct answer wins: Preprocessing inside the artifact cannot drift between the two paths.
- **D:** Correct. In this case: Preprocessing inside the artifact cannot drift between the two paths.

### Question 61 — B

Answer: Deploy with a private endpoint only. A private endpoint is reachable only from the VPC and shares no public surface. Local study-map skill 4.6 (Endpoint Types and Access), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A dedicated endpoint gives the model its own capacity instead of sharing a pool. Why the correct answer wins: A private endpoint is reachable only from the VPC and shares no public surface.
- **B:** Correct. In this case: A private endpoint is reachable only from the VPC and shares no public surface.
- **C:** Incorrect for this question. Autoscaling adds replicas with the traffic and removes them afterwards. Why the correct answer wins: A private endpoint is reachable only from the VPC and shares no public surface.
- **D:** Incorrect for this question. A shared endpoint removes the deployment step but gives no control over capacity or residency. Why the correct answer wins: A private endpoint is reachable only from the VPC and shares no public surface.

### Question 62 — D

Answer: Use a dedicated endpoint. A dedicated endpoint gives the model its own capacity instead of sharing a pool. Local study-map skill 4.6 (Endpoint Types and Access), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A private endpoint is reachable only from the VPC and shares no public surface. Why the correct answer wins: A dedicated endpoint gives the model its own capacity instead of sharing a pool.
- **B:** Incorrect for this question. A traffic split sends a defined share to each version on the same endpoint. Why the correct answer wins: A dedicated endpoint gives the model its own capacity instead of sharing a pool.
- **C:** Incorrect for this question. A shared endpoint removes the deployment step but gives no control over capacity or residency. Why the correct answer wins: A dedicated endpoint gives the model its own capacity instead of sharing a pool.
- **D:** Correct. In this case: A dedicated endpoint gives the model its own capacity instead of sharing a pool.

### Question 63 — C

Answer: Attach a GPU to the serving replica. A GPU shortens inference time enough to meet a tight latency target. Local study-map skill 4.7 (Serving Hardware), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. CPU serving is the cheapest option for a small model with a generous latency budget. Why the correct answer wins: A GPU shortens inference time enough to meet a tight latency target.
- **B:** Incorrect for this question. Concurrency fills each replica before another is started, which lowers cost per request. Why the correct answer wins: A GPU shortens inference time enough to meet a tight latency target.
- **C:** Correct. In this case: A GPU shortens inference time enough to meet a tight latency target.
- **D:** Incorrect for this question. An Edge TPU runs a quantised model on-device where the network cannot be relied on. Why the correct answer wins: A GPU shortens inference time enough to meet a tight latency target.

### Question 64 — C

Answer: Deploy to an Edge TPU device. An Edge TPU runs a quantised model on-device where the network cannot be relied on. Local study-map skill 4.7 (Serving Hardware), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Autoscaling adds replicas with the traffic and removes them afterwards. Why the correct answer wins: An Edge TPU runs a quantised model on-device where the network cannot be relied on.
- **B:** Incorrect for this question. CPU serving is the cheapest option for a small model with a generous latency budget. Why the correct answer wins: An Edge TPU runs a quantised model on-device where the network cannot be relied on.
- **C:** Correct. In this case: An Edge TPU runs a quantised model on-device where the network cannot be relied on.
- **D:** Incorrect for this question. A GPU shortens inference time enough to meet a tight latency target. Why the correct answer wins: An Edge TPU runs a quantised model on-device where the network cannot be relied on.

### Question 65 — A, B

Answers: Raise the maximum replica count; Raise the concurrency per replica. The ceiling caps how far it scales, and concurrency fills each replica before another starts. The ceiling caps how far the endpoint scales, and therefore the throughput it can absorb. Concurrency fills each replica before another is started, which lowers cost per request. Local study-map skill 4.8 (Serving Throughput and Scaling), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. Concurrency fills each replica before another is started, which lowers cost per request. In this case: The ceiling caps how far it scales, and concurrency fills each replica before another starts.
- **B:** Correct. The ceiling caps how far the endpoint scales, and therefore the throughput it can absorb. In this case: The ceiling caps how far it scales, and concurrency fills each replica before another starts.
- **C:** Incorrect for this question. A GPU shortens inference time enough to meet a tight latency target. Why the correct answer wins: The ceiling caps how far it scales, and concurrency fills each replica before another starts.
- **D:** Incorrect for this question. A minimum replica keeps capacity warm so the first request after a quiet period is fast. Why the correct answer wins: The ceiling caps how far it scales, and concurrency fills each replica before another starts.
- **E:** Incorrect for this question. Batching amortises the per-request overhead when the caller can wait. Why the correct answer wins: The ceiling caps how far it scales, and concurrency fills each replica before another starts.

### Question 66 — D

Answer: Enable autoscaling on the endpoint. Autoscaling adds replicas with the traffic and removes them afterwards. Local study-map skill 4.8 (Serving Throughput and Scaling), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Concurrency fills each replica before another is started, which lowers cost per request. Why the correct answer wins: Autoscaling adds replicas with the traffic and removes them afterwards.
- **B:** Incorrect for this question. A minimum replica keeps capacity warm so the first request after a quiet period is fast. Why the correct answer wins: Autoscaling adds replicas with the traffic and removes them afterwards.
- **C:** Incorrect for this question. The ceiling caps how far the endpoint scales, and therefore the throughput it can absorb. Why the correct answer wins: Autoscaling adds replicas with the traffic and removes them afterwards.
- **D:** Correct. In this case: Autoscaling adds replicas with the traffic and removes them afterwards.

### Question 67 — A

Answer: Batch the requests inside the client. Batching amortises the per-request overhead when the caller can wait. Local study-map skill 4.8 (Serving Throughput and Scaling), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Batching amortises the per-request overhead when the caller can wait.
- **B:** Incorrect for this question. Autoscaling adds replicas with the traffic and removes them afterwards. Why the correct answer wins: Batching amortises the per-request overhead when the caller can wait.
- **C:** Incorrect for this question. Concurrency fills each replica before another is started, which lowers cost per request. Why the correct answer wins: Batching amortises the per-request overhead when the caller can wait.
- **D:** Incorrect for this question. Batch prediction reads a file or table and writes predictions without holding serving capacity. Why the correct answer wins: Batching amortises the per-request overhead when the caller can wait.

### Question 68 — B, D

Answers: Configure explanation metadata for the endpoint; Set a minimum replica count. Explanation metadata tells the endpoint which inputs to attribute over, and a minimum replica keeps capacity warm. A minimum replica keeps capacity warm so the first request after a quiet period is fast. Local study-map skill 4.9 (Production Tuning), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Batching amortises the per-request overhead when the caller can wait. Why the correct answer wins: Explanation metadata tells the endpoint which inputs to attribute over, and a minimum replica keeps capacity warm.
- **B:** Correct. A minimum replica keeps capacity warm so the first request after a quiet period is fast. In this case: Explanation metadata tells the endpoint which inputs to attribute over, and a minimum replica keeps capacity warm.
- **C:** Incorrect for this question. Artifact Registry holds the image with IAM and vulnerability metadata. Why the correct answer wins: Explanation metadata tells the endpoint which inputs to attribute over, and a minimum replica keeps capacity warm.
- **D:** Correct. In this case: Explanation metadata tells the endpoint which inputs to attribute over, and a minimum replica keeps capacity warm.
- **E:** Incorrect for this question. An alias decouples the served version name from the artifact id, so a rollback is a pointer move. Why the correct answer wins: Explanation metadata tells the endpoint which inputs to attribute over, and a minimum replica keeps capacity warm.

### Question 69 — A

Answer: Raise the concurrency per replica. Concurrency fills each replica before another is started, which lowers cost per request. Local study-map skill 4.9 (Production Tuning), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Concurrency fills each replica before another is started, which lowers cost per request.
- **B:** Incorrect for this question. Batching amortises the per-request overhead when the caller can wait. Why the correct answer wins: Concurrency fills each replica before another is started, which lowers cost per request.
- **C:** Incorrect for this question. The ceiling caps how far the endpoint scales, and therefore the throughput it can absorb. Why the correct answer wins: Concurrency fills each replica before another is started, which lowers cost per request.
- **D:** Incorrect for this question. A GPU shortens inference time enough to meet a tight latency target. Why the correct answer wins: Concurrency fills each replica before another is started, which lowers cost per request.

### Question 70 — D

Answer: Add an explicit data validation step. A validation step stops a bad batch before it reaches training. Local study-map skill 5.1 (Data and Model Validation), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The gate promotes a model only when it beats the incumbent on the agreed metric. Why the correct answer wins: A validation step stops a bad batch before it reaches training.
- **B:** Incorrect for this question. Deduplicating at ingest stops duplicated records inflating the training set. Why the correct answer wins: A validation step stops a bad batch before it reaches training.
- **C:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: A validation step stops a bad batch before it reaches training.
- **D:** Correct. In this case: A validation step stops a bad batch before it reaches training.

### Question 71 — D

Answer: Gate the deployment on a model evaluation threshold. The gate promotes a model only when it beats the incumbent on the agreed metric. Local study-map skill 5.1 (Data and Model Validation), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A validation step stops a bad batch before it reaches training. Why the correct answer wins: The gate promotes a model only when it beats the incumbent on the agreed metric.
- **B:** Incorrect for this question. Metric-triggered retraining reacts to actual quality loss. Why the correct answer wins: The gate promotes a model only when it beats the incumbent on the agreed metric.
- **C:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: The gate promotes a model only when it beats the incumbent on the agreed metric.
- **D:** Correct. In this case: The gate promotes a model only when it beats the incumbent on the agreed metric.

### Question 72 — C, D

Answers: Keep the test set out of every tuning decision; Inspect the confusion matrix at the operating threshold. A locked test set restores an unbiased estimate, and the matrix shows the error split at the chosen operating point. A test set that has been used for tuning no longer estimates generalisation. The matrix shows the false-positive and false-negative split the business will feel. Local study-map skill 5.1 (Data and Model Validation), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: A locked test set restores an unbiased estimate, and the matrix shows the error split at the chosen operating point.
- **B:** Incorrect for this question. A fixed seed makes a rerun reproducible when the rest of the environment is pinned. Why the correct answer wins: A locked test set restores an unbiased estimate, and the matrix shows the error split at the chosen operating point.
- **C:** Correct. The matrix shows the false-positive and false-negative split the business will feel. In this case: A locked test set restores an unbiased estimate, and the matrix shows the error split at the chosen operating point.
- **D:** Correct. A test set that has been used for tuning no longer estimates generalisation. In this case: A locked test set restores an unbiased estimate, and the matrix shows the error split at the chosen operating point.
- **E:** Incorrect for this question. ROC AUC measures ranking quality across thresholds and hides class imbalance. Why the correct answer wins: A locked test set restores an unbiased estimate, and the matrix shows the error split at the chosen operating point.

### Question 73 — C

Answer: Orchestrate the steps in Agent Platform Pipelines. Pipelines runs each step as a container with caching, lineage, and retry. Local study-map skill 5.2 (Pipeline Orchestration Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Ray fits a Python-native distributed workload that is not a container-per-step pipeline. Why the correct answer wins: Pipelines runs each step as a container with caching, lineage, and retry.
- **B:** Incorrect for this question. Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance. Why the correct answer wins: Pipelines runs each step as a container with caching, lineage, and retry.
- **C:** Correct. In this case: Pipelines runs each step as a container with caching, lineage, and retry.
- **D:** Incorrect for this question. Airflow expresses cross-system dependencies and schedules outside the ML platform. Why the correct answer wins: Pipelines runs each step as a container with caching, lineage, and retry.

### Question 74 — D

Answer: Use Ray on Agent Platform for the distributed compute. Ray fits a Python-native distributed workload that is not a container-per-step pipeline. Local study-map skill 5.2 (Pipeline Orchestration Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Pipelines runs each step as a container with caching, lineage, and retry. Why the correct answer wins: Ray fits a Python-native distributed workload that is not a container-per-step pipeline.
- **B:** Incorrect for this question. Airflow expresses cross-system dependencies and schedules outside the ML platform. Why the correct answer wins: Ray fits a Python-native distributed workload that is not a container-per-step pipeline.
- **C:** Incorrect for this question. Kubeflow pipelines give a container-per-step pipeline that runs on the managed service or on GKE. Why the correct answer wins: Ray fits a Python-native distributed workload that is not a container-per-step pipeline.
- **D:** Correct. In this case: Ray fits a Python-native distributed workload that is not a container-per-step pipeline.

### Question 75 — B

Answer: Trigger the build and deploy from Cloud Build. Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance. Local study-map skill 5.2 (Pipeline Orchestration Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Pipelines runs each step as a container with caching, lineage, and retry. Why the correct answer wins: Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance.
- **B:** Correct. In this case: Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance.
- **C:** Incorrect for this question. Airflow expresses cross-system dependencies and schedules outside the ML platform. Why the correct answer wins: Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance.
- **D:** Incorrect for this question. The scheduler starts the pipeline on the cadence the retraining policy defines. Why the correct answer wins: Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance.

### Question 76 — A

Answer: Add a Cloud Scheduler trigger to the pipeline. The scheduler starts the pipeline on the cadence the retraining policy defines. Local study-map skill 5.2 (Pipeline Orchestration Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: The scheduler starts the pipeline on the cadence the retraining policy defines.
- **B:** Incorrect for this question. Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance. Why the correct answer wins: The scheduler starts the pipeline on the cadence the retraining policy defines.
- **C:** Incorrect for this question. An event trigger retrains when data lands instead of on a fixed clock. Why the correct answer wins: The scheduler starts the pipeline on the cadence the retraining policy defines.
- **D:** Incorrect for this question. A fixed schedule is simple to reason about when the data changes predictably. Why the correct answer wins: The scheduler starts the pipeline on the cadence the retraining policy defines.

### Question 77 — D

Answer: Share one transformation library between training and serving. Shared code removes the class of bug where the two paths compute a feature differently. Local study-map skill 5.3 (Train and Serve Consistency), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. An alias decouples the served version name from the artifact id, so a rollback is a pointer move. Why the correct answer wins: Shared code removes the class of bug where the two paths compute a feature differently.
- **B:** Incorrect for this question. Feature Store keeps one definition that both training and serving read. Why the correct answer wins: Shared code removes the class of bug where the two paths compute a feature differently.
- **C:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: Shared code removes the class of bug where the two paths compute a feature differently.
- **D:** Correct. In this case: Shared code removes the class of bug where the two paths compute a feature differently.

### Question 78 — D, E

Answers: Register the feature in Agent Platform Feature Store; Serve the feature from the online store. Feature Store keeps one definition, and the online store returns the latest value at low latency. Feature Store keeps one definition that both training and serving read. Local study-map skill 5.3 (Train and Serve Consistency), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Deduplicating at ingest stops duplicated records inflating the training set. Why the correct answer wins: Feature Store keeps one definition, and the online store returns the latest value at low latency.
- **B:** Incorrect for this question. In-memory processing is the simplest option and stops working once the data exceeds the worker memory. Why the correct answer wins: Feature Store keeps one definition, and the online store returns the latest value at low latency.
- **C:** Incorrect for this question. The registry versions the model artifact and links it to its lineage and metrics. Why the correct answer wins: Feature Store keeps one definition, and the online store returns the latest value at low latency.
- **D:** Correct. In this case: Feature Store keeps one definition, and the online store returns the latest value at low latency.
- **E:** Correct. Feature Store keeps one definition that both training and serving read. In this case: Feature Store keeps one definition, and the online store returns the latest value at low latency.

### Question 79 — B

Answer: Enable step caching. Caching skips an unchanged step on a rerun and shortens the pipeline. Local study-map skill 5.3 (Train and Serve Consistency), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A validation step stops a bad batch before it reaches training. Why the correct answer wins: Caching skips an unchanged step on a rerun and shortens the pipeline.
- **B:** Correct. In this case: Caching skips an unchanged step on a rerun and shortens the pipeline.
- **C:** Incorrect for this question. A fixed seed makes a rerun reproducible when the rest of the environment is pinned. Why the correct answer wins: Caching skips an unchanged step on a rerun and shortens the pipeline.
- **D:** Incorrect for this question. Shared code removes the class of bug where the two paths compute a feature differently. Why the correct answer wins: Caching skips an unchanged step on a rerun and shortens the pipeline.

### Question 80 — D

Answer: Read the historical features from the offline store. The offline store returns point-in-time values for training. Local study-map skill 5.3 (Train and Serve Consistency), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Feature monitoring reports distribution changes per feature, not just per model. Why the correct answer wins: The offline store returns point-in-time values for training.
- **B:** Incorrect for this question. A crossed feature lets a linear model express the interaction it cannot learn alone. Why the correct answer wins: The offline store returns point-in-time values for training.
- **C:** Incorrect for this question. The online store returns the latest feature value at low latency for a single entity. Why the correct answer wins: The offline store returns point-in-time values for training.
- **D:** Correct. In this case: The offline store returns point-in-time values for training.

### Question 81 — B

Answer: Retrain when drift crosses the threshold. Drift-triggered retraining responds to change instead of to the calendar. Local study-map skill 5.4 (Retraining Policy), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A fixed schedule is simple to reason about when the data changes predictably. Why the correct answer wins: Drift-triggered retraining responds to change instead of to the calendar.
- **B:** Correct. In this case: Drift-triggered retraining responds to change instead of to the calendar.
- **C:** Incorrect for this question. Metric-triggered retraining reacts to actual quality loss. Why the correct answer wins: Drift-triggered retraining responds to change instead of to the calendar.
- **D:** Incorrect for this question. Manual retraining leaves the model stale whenever the trigger is forgotten. Why the correct answer wins: Drift-triggered retraining responds to change instead of to the calendar.

### Question 82 — C

Answer: Retrain when the production metric drops. Metric-triggered retraining reacts to actual quality loss. Local study-map skill 5.4 (Retraining Policy), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A fixed schedule is simple to reason about when the data changes predictably. Why the correct answer wins: Metric-triggered retraining reacts to actual quality loss.
- **B:** Incorrect for this question. Drift-triggered retraining responds to change instead of to the calendar. Why the correct answer wins: Metric-triggered retraining reacts to actual quality loss.
- **C:** Correct. In this case: Metric-triggered retraining reacts to actual quality loss.
- **D:** Incorrect for this question. Manual retraining leaves the model stale whenever the trigger is forgotten. Why the correct answer wins: Metric-triggered retraining reacts to actual quality loss.

### Question 83 — D

Answer: Retrain only on a manual request. Manual retraining leaves the model stale whenever the trigger is forgotten. Local study-map skill 5.4 (Retraining Policy), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A fixed schedule is simple to reason about when the data changes predictably. Why the correct answer wins: Manual retraining leaves the model stale whenever the trigger is forgotten.
- **B:** Incorrect for this question. Drift-triggered retraining responds to change instead of to the calendar. Why the correct answer wins: Manual retraining leaves the model stale whenever the trigger is forgotten.
- **C:** Incorrect for this question. Metric-triggered retraining reacts to actual quality loss. Why the correct answer wins: Manual retraining leaves the model stale whenever the trigger is forgotten.
- **D:** Correct. In this case: Manual retraining leaves the model stale whenever the trigger is forgotten.

### Question 84 — C

Answer: Extend CI/CD into continuous training. Continuous training adds the retrain and validate step to the same automated pipeline. Local study-map skill 5.5 (CI/CD/CT with Cloud Build), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A fixed schedule is simple to reason about when the data changes predictably. Why the correct answer wins: Continuous training adds the retrain and validate step to the same automated pipeline.
- **B:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: Continuous training adds the retrain and validate step to the same automated pipeline.
- **C:** Correct. In this case: Continuous training adds the retrain and validate step to the same automated pipeline.
- **D:** Incorrect for this question. Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance. Why the correct answer wins: Continuous training adds the retrain and validate step to the same automated pipeline.

### Question 85 — A

Answer: Trigger the pipeline from the arrival of new data. An event trigger retrains when data lands instead of on a fixed clock. Local study-map skill 5.5 (CI/CD/CT with Cloud Build), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: An event trigger retrains when data lands instead of on a fixed clock.
- **B:** Incorrect for this question. Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance. Why the correct answer wins: An event trigger retrains when data lands instead of on a fixed clock.
- **C:** Incorrect for this question. Manual retraining leaves the model stale whenever the trigger is forgotten. Why the correct answer wins: An event trigger retrains when data lands instead of on a fixed clock.
- **D:** Incorrect for this question. The scheduler starts the pipeline on the cadence the retraining policy defines. Why the correct answer wins: An event trigger retrains when data lands instead of on a fixed clock.

### Question 86 — A

Answer: Add an explicit data validation step. A validation step stops a bad batch before it reaches training. Local study-map skill 5.5 (CI/CD/CT with Cloud Build), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: A validation step stops a bad batch before it reaches training.
- **B:** Incorrect for this question. The gate promotes a model only when it beats the incumbent on the agreed metric. Why the correct answer wins: A validation step stops a bad batch before it reaches training.
- **C:** Incorrect for this question. Drift-triggered retraining responds to change instead of to the calendar. Why the correct answer wins: A validation step stops a bad batch before it reaches training.
- **D:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: A validation step stops a bad batch before it reaches training.

### Question 87 — D

Answer: Gate the deployment on a model evaluation threshold. The gate promotes a model only when it beats the incumbent on the agreed metric. Local study-map skill 5.5 (CI/CD/CT with Cloud Build), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: The gate promotes a model only when it beats the incumbent on the agreed metric.
- **B:** Incorrect for this question. A validation step stops a bad batch before it reaches training. Why the correct answer wins: The gate promotes a model only when it beats the incumbent on the agreed metric.
- **C:** Incorrect for this question. Manual retraining leaves the model stale whenever the trigger is forgotten. Why the correct answer wins: The gate promotes a model only when it beats the incumbent on the agreed metric.
- **D:** Correct. In this case: The gate promotes a model only when it beats the incumbent on the agreed metric.

### Question 88 — A, E

Answers: Screen the prompts and responses with Model Armor; Configure the model safety filters. Model Armor detects prompt injection, and the safety filters block categories of harmful output. Model Armor detects prompt injection, jailbreak attempts, and unsafe content. Safety filters block categories of harmful output at the model call. Local study-map skill 6.1 (Secure AI and Prompt Protection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. Safety filters block categories of harmful output at the model call. In this case: Model Armor detects prompt injection, and the safety filters block categories of harmful output.
- **B:** Incorrect for this question. A system instruction states what the assistant must refuse, though it is not a security control on its own. Why the correct answer wins: Model Armor detects prompt injection, and the safety filters block categories of harmful output.
- **C:** Incorrect for this question. A schema stops the model returning free text that downstream code cannot parse. Why the correct answer wins: Model Armor detects prompt injection, and the safety filters block categories of harmful output.
- **D:** Incorrect for this question. A regex removes a known identifier pattern before the prompt leaves the service. Why the correct answer wins: Model Armor detects prompt injection, and the safety filters block categories of harmful output.
- **E:** Correct. Model Armor detects prompt injection, jailbreak attempts, and unsafe content. In this case: Model Armor detects prompt injection, and the safety filters block categories of harmful output.

### Question 89 — D

Answer: Redact the pattern-matchable fields with a regex. A regex removes a known identifier pattern before the prompt leaves the service. Local study-map skill 6.1 (Secure AI and Prompt Protection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A schema stops the model returning free text that downstream code cannot parse. Why the correct answer wins: A regex removes a known identifier pattern before the prompt leaves the service.
- **B:** Incorrect for this question. Model Armor detects prompt injection, jailbreak attempts, and unsafe content. Why the correct answer wins: A regex removes a known identifier pattern before the prompt leaves the service.
- **C:** Incorrect for this question. A system instruction states what the assistant must refuse, though it is not a security control on its own. Why the correct answer wins: A regex removes a known identifier pattern before the prompt leaves the service.
- **D:** Correct. In this case: A regex removes a known identifier pattern before the prompt leaves the service.

### Question 90 — B

Answer: Constrain the response to a JSON schema. A schema stops the model returning free text that downstream code cannot parse. Local study-map skill 6.1 (Secure AI and Prompt Protection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A system instruction states what the assistant must refuse, though it is not a security control on its own. Why the correct answer wins: A schema stops the model returning free text that downstream code cannot parse.
- **B:** Correct. In this case: A schema stops the model returning free text that downstream code cannot parse.
- **C:** Incorrect for this question. Model Armor detects prompt injection, jailbreak attempts, and unsafe content. Why the correct answer wins: A schema stops the model returning free text that downstream code cannot parse.
- **D:** Incorrect for this question. Safety filters block categories of harmful output at the model call. Why the correct answer wins: A schema stops the model returning free text that downstream code cannot parse.

### Question 91 — B

Answer: Monitor the outcome rate across the protected groups. A per-group outcome rate is the first evidence of disparate impact. Local study-map skill 6.2 (Responsible AI and Bias), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The card states where the model may be used and where it must not. Why the correct answer wins: A per-group outcome rate is the first evidence of disparate impact.
- **B:** Correct. In this case: A per-group outcome rate is the first evidence of disparate impact.
- **C:** Incorrect for this question. A sliced metric shows a gap that the aggregate metric hides. Why the correct answer wins: A per-group outcome rate is the first evidence of disparate impact.
- **D:** Incorrect for this question. The card records provenance, intended use, and known gaps for the dataset. Why the correct answer wins: A per-group outcome rate is the first evidence of disparate impact.

### Question 92 — C

Answer: Slice the evaluation metrics by the sensitive attribute. A sliced metric shows a gap that the aggregate metric hides. Local study-map skill 6.2 (Responsible AI and Bias), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The card records provenance, intended use, and known gaps for the dataset. Why the correct answer wins: A sliced metric shows a gap that the aggregate metric hides.
- **B:** Incorrect for this question. The card states where the model may be used and where it must not. Why the correct answer wins: A sliced metric shows a gap that the aggregate metric hides.
- **C:** Correct. In this case: A sliced metric shows a gap that the aggregate metric hides.
- **D:** Incorrect for this question. A per-group outcome rate is the first evidence of disparate impact. Why the correct answer wins: A sliced metric shows a gap that the aggregate metric hides.

### Question 93 — C

Answer: Summarise the model with ML.GLOBAL_EXPLAIN. ML.GLOBAL_EXPLAIN ranks the features that matter most across the whole model. Local study-map skill 6.3 (Explainability), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The card states where the model may be used and where it must not. Why the correct answer wins: ML.GLOBAL_EXPLAIN ranks the features that matter most across the whole model.
- **B:** Incorrect for this question. Integrated gradients attributes an image prediction to the pixels that moved it. Why the correct answer wins: ML.GLOBAL_EXPLAIN ranks the features that matter most across the whole model.
- **C:** Correct. In this case: ML.GLOBAL_EXPLAIN ranks the features that matter most across the whole model.
- **D:** Incorrect for this question. Shapley values attribute a prediction to its features with a consistent baseline. Why the correct answer wins: ML.GLOBAL_EXPLAIN ranks the features that matter most across the whole model.

### Question 94 — C

Answer: Use integrated gradients for the image model. Integrated gradients attributes an image prediction to the pixels that moved it. Local study-map skill 6.3 (Explainability), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Shapley values attribute a prediction to its features with a consistent baseline. Why the correct answer wins: Integrated gradients attributes an image prediction to the pixels that moved it.
- **B:** Incorrect for this question. ML.EXPLAIN_PREDICT attributes each prediction to the features that moved it. Why the correct answer wins: Integrated gradients attributes an image prediction to the pixels that moved it.
- **C:** Correct. In this case: Integrated gradients attributes an image prediction to the pixels that moved it.
- **D:** Incorrect for this question. Sampled Shapley explains individual online predictions with a bounded compute cost. Why the correct answer wins: Integrated gradients attributes an image prediction to the pixels that moved it.

### Question 95 — D

Answer: Enable Model Monitoring on the endpoint. Model Monitoring compares live traffic with the training baseline and reports skew and drift. Local study-map skill 6.4 (Model Monitoring Configuration), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Token accounting attributes generative cost to the feature that caused it. Why the correct answer wins: Model Monitoring compares live traffic with the training baseline and reports skew and drift.
- **B:** Incorrect for this question. A percentile latency per version shows a regression that an average hides. Why the correct answer wins: Model Monitoring compares live traffic with the training baseline and reports skew and drift.
- **C:** Incorrect for this question. Redacted logs make a bad answer diagnosable without storing sensitive text. Why the correct answer wins: Model Monitoring compares live traffic with the training baseline and reports skew and drift.
- **D:** Correct. In this case: Model Monitoring compares live traffic with the training baseline and reports skew and drift.

### Question 96 — B

Answer: Set the monitoring threshold from the acceptable error budget. The threshold expresses how much drift the business can absorb before someone acts. Local study-map skill 6.4 (Model Monitoring Configuration), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A percentile latency per version shows a regression that an average hides. Why the correct answer wins: The threshold expresses how much drift the business can absorb before someone acts.
- **B:** Correct. In this case: The threshold expresses how much drift the business can absorb before someone acts.
- **C:** Incorrect for this question. An alert with no owner is a dashboard nobody reads. Why the correct answer wins: The threshold expresses how much drift the business can absorb before someone acts.
- **D:** Incorrect for this question. Continuous sampling catches quality regressions that drift metrics cannot see. Why the correct answer wins: The threshold expresses how much drift the business can absorb before someone acts.

### Question 97 — C, D

Answers: Watch for concept drift; Join the delayed ground truth back to the predictions. Concept drift is a change in the feature-target relationship, and the delayed ground truth makes it measurable. Concept drift is a change in the relationship between the features and the target. Without the labelled outcome, quality can only be inferred from the inputs and outputs. Local study-map skill 6.5 (Skew and Drift Types), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Attribution drift is a change in which features drive the prediction. Why the correct answer wins: Concept drift is a change in the feature-target relationship, and the delayed ground truth makes it measurable.
- **B:** Incorrect for this question. Data drift is a change in the input distribution after the model shipped. Why the correct answer wins: Concept drift is a change in the feature-target relationship, and the delayed ground truth makes it measurable.
- **C:** Correct. Without the labelled outcome, quality can only be inferred from the inputs and outputs. In this case: Concept drift is a change in the feature-target relationship, and the delayed ground truth makes it measurable.
- **D:** Correct. Concept drift is a change in the relationship between the features and the target. In this case: Concept drift is a change in the feature-target relationship, and the delayed ground truth makes it measurable.
- **E:** Incorrect for this question. A shift in the output distribution is often the first visible symptom. Why the correct answer wins: Concept drift is a change in the feature-target relationship, and the delayed ground truth makes it measurable.

### Question 98 — B

Answer: Watch for training-serving skew. Skew compares the live feature distribution with the training distribution. Local study-map skill 6.5 (Skew and Drift Types), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Concept drift is a change in the relationship between the features and the target. Why the correct answer wins: Skew compares the live feature distribution with the training distribution.
- **B:** Correct. In this case: Skew compares the live feature distribution with the training distribution.
- **C:** Incorrect for this question. Data drift is a change in the input distribution after the model shipped. Why the correct answer wins: Skew compares the live feature distribution with the training distribution.
- **D:** Incorrect for this question. Attribution drift is a change in which features drive the prediction. Why the correct answer wins: Skew compares the live feature distribution with the training distribution.

### Question 99 — C

Answer: Score a sample of live answers with the evaluation rubric. Continuous sampling catches quality regressions that drift metrics cannot see. Local study-map skill 6.6 (Generative AI Monitoring), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Model Monitoring compares live traffic with the training baseline and reports skew and drift. Why the correct answer wins: Continuous sampling catches quality regressions that drift metrics cannot see.
- **B:** Incorrect for this question. Token accounting attributes generative cost to the feature that caused it. Why the correct answer wins: Continuous sampling catches quality regressions that drift metrics cannot see.
- **C:** Correct. In this case: Continuous sampling catches quality regressions that drift metrics cannot see.
- **D:** Incorrect for this question. A percentile latency per version shows a regression that an average hides. Why the correct answer wins: Continuous sampling catches quality regressions that drift metrics cannot see.

### Question 100 — C

Answer: Log the prompt and response with redaction. Redacted logs make a bad answer diagnosable without storing sensitive text. Local study-map skill 6.6 (Generative AI Monitoring), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Token accounting attributes generative cost to the feature that caused it. Why the correct answer wins: Redacted logs make a bad answer diagnosable without storing sensitive text.
- **B:** Incorrect for this question. A percentile latency per version shows a regression that an average hides. Why the correct answer wins: Redacted logs make a bad answer diagnosable without storing sensitive text.
- **C:** Correct. In this case: Redacted logs make a bad answer diagnosable without storing sensitive text.
- **D:** Incorrect for this question. Model Monitoring compares live traffic with the training baseline and reports skew and drift. Why the correct answer wins: Redacted logs make a bad answer diagnosable without storing sensitive text.
