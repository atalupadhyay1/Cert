# Google Cloud Professional Machine Learning Engineer — Full-Length Mock Exam 2

Professional Machine Learning Engineer · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study or drag-and-drop item is reproduced. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Architecting low-code AI solutions (Low-Code AI and Foundational Models)

### 1. A marketing team wants to group customers into behavioural segments with no target column. What should be built?

- A. Create a BigQuery ML k-means model
- B. Create a BigQuery ML ARIMA_PLUS time series model
- C. Create a BigQuery ML logistic regression model
- D. Create a BigQuery ML linear regression model

### 2. A pricing model must capture interactions between region and weekday, and each quote must be explainable. Which two choices apply? Select two.

- A. Read the contribution of each feature with ML.EXPLAIN_PREDICT
- B. Import the TensorFlow model into BigQuery ML
- C. Store the predictions in a nested JSON column
- D. Create a BigQuery ML boosted tree classifier
- E. Create a BigQuery ML deep neural network

### 3. The business asks for precision and recall on the holdout before launch. What should be used?

- A. Inspect the metrics with ML.EVALUATE
- B. Reserve BigQuery slots for the training job
- C. Score the rows with ML.PREDICT
- D. Summarise the model with ML.GLOBAL_EXPLAIN

### 4. An auditor asks which inputs matter most across the whole risk model. What should be used?

- A. Read the contribution of each feature with ML.EXPLAIN_PREDICT
- B. Score the rows with ML.PREDICT
- C. Summarise the model with ML.GLOBAL_EXPLAIN
- D. Declare the feature transformations in the TRANSFORM clause

### 5. A fixed training budget must be shared across six AutoML experiments this month. What should be configured?

- A. Define a manual split column with train, validation, and test
- B. Export the AutoML model as an artifact
- C. Let AutoML choose the data split
- D. Set a training budget in node hours

### 6. An AutoML model must be served in a container outside the managed endpoint. What should be done?

- A. Export the AutoML model as an artifact
- B. Set a training budget in node hours
- C. Use AutoML so the team needs no modelling code
- D. Train an Agent Platform AutoML tabular model

### 7. A large review table must be summarised per row without copying it anywhere. What should be used?

- A. Ground the prompt with retrieval instead of fine-tuning
- B. Create a BigQuery ML remote model over Gemini
- C. Fine-tune a Gemini model from BigQuery
- D. Use Gemini Enterprise Agent Platform

### 8. A claims photo and the customer's description must be assessed together in one call. What should be used?

- A. Use Document AI with a specialised processor
- B. Send the image and the question in one multimodal request
- C. Use the Vision API
- D. Use the Translation API

### 9. Call-centre audio must become searchable text with domain vocabulary. What should be used?

- A. Use the Speech-to-Text API
- B. Use the Video Intelligence API
- C. Use the Translation API
- D. Use the Natural Language API

### 10. A support corpus in nine languages must be normalised into one before analysis. What should be used?

- A. Use the Natural Language API
- B. Use the Speech-to-Text API
- C. Use the Translation API
- D. Use the Vision API

### 11. Users in one country report slow answers, and traffic is capped well below demand. Which two changes apply? Select two.

- A. Request a quota increase for the model
- B. Call the model in the region that serves the users
- C. Constrain the output with a schema and a token limit
- D. Stream the response tokens to the client
- E. Fall back to a smaller model when the primary is throttled

### 12. A chat interface feels slow although total generation time is unchanged. What should be done?

- A. Cache the long shared context
- B. Stream the response tokens to the client
- C. Send the offline work through the batch API
- D. Constrain the output with a schema and a token limit

---

## Domain 2 — Collaborating within and across teams to manage data and models (Data, Features, Notebooks, and Experiments)

### 13. A streaming source must be cleaned with the same logic that cleans the nightly batch. What should be used?

- A. Preprocess with Spark on Dataproc
- B. Preprocess with a Dataflow pipeline
- C. Preprocess in memory with pandas
- D. Preprocess in BigQuery with SQL

### 14. A model scores suspiciously high and one customer appears in both splits. Which two fixes apply? Select two.

- A. Drop the identifier columns before the training dataset is written
- B. Split the data by time rather than at random
- C. Split by entity so one customer never spans train and test
- D. Remove the post-outcome column from the features
- E. Normalise the numeric feature before training

### 15. A team already owns 40 PySpark jobs that must keep running unchanged. What should be used?

- A. Preprocess with Spark on Dataproc
- B. Preprocess in memory with pandas
- C. Preprocess in BigQuery with SQL
- D. Preprocess with a Dataflow pipeline

### 16. A single entity's latest feature value must be returned in under 10 ms at serving. What should be used?

- A. Read the historical features from the offline store
- B. Enable feature monitoring on the feature group
- C. Serve the feature from the online store
- D. Add a crossed feature for the interacting pair

### 17. One feature silently changed distribution while the model metric stayed flat. What should be enabled?

- A. Serve the feature from the online store
- B. Enable Model Monitoring on the endpoint
- C. Register the feature in Agent Platform Feature Store
- D. Enable feature monitoring on the feature group

### 18. A national identifier is in the extract but no model needs it. What is the safest action?

- A. De-identify the fields with Sensitive Data Protection
- B. Hash the identifiers with a salted key before training
- C. Restrict the raw bucket to a privileged service account
- D. Drop the identifier columns before the training dataset is written

### 19. Free-text notes contain card numbers that must stay readable in shape but unusable. What should be used?

- A. Drop the identifier columns before the training dataset is written
- B. Restrict the raw bucket to a privileged service account
- C. Hash the identifiers with a salted key before training
- D. De-identify the fields with Sensitive Data Protection

### 20. Two analysts get different results from the same notebook. What should be configured?

- A. Use an Agent Platform Workbench instance
- B. Use Colab Enterprise
- C. Set an idle shutdown schedule
- D. Pin the runtime to a custom container image

### 21. The notebook must query a database that has no public address. What should be done?

- A. Create the runtime with no public IP
- B. Use an Agent Platform Workbench instance
- C. Set an idle shutdown schedule
- D. Attach the runtime to the shared VPC subnet

### 22. Six model families must be ranked before the best one is taken forward. What should be done?

- A. Track artifacts and lineage in ML Metadata
- B. Set the random seed in the training code
- C. Enable step caching
- D. Compare the runs on the validation metric

### 23. A reviewer asks which code commit produced the artifact under investigation. What should be consulted?

- A. Log the run to Agent Platform Experiments
- B. Track artifacts and lineage in ML Metadata
- C. Register the model in Agent Platform Model Registry
- D. Enable step caching

### 24. A container-per-step workflow must run on the managed service and be reusable by another team. Which two choices fit? Select two.

- A. Use Ray on Agent Platform for the distributed compute
- B. Start from a Google-provided pipeline template
- C. Log the run to Agent Platform Experiments
- D. Express the workflow as a Kubeflow pipeline
- E. Orchestrate with Managed Service for Apache Airflow

### 25. Experiment tracking must be upgraded to a scheduled, reproducible multi-step workflow inside the platform. What should be used?

- A. Orchestrate the steps in Agent Platform Pipelines
- B. Log the run to Agent Platform Experiments
- C. Express the workflow as a Kubeflow pipeline
- D. Orchestrate with Managed Service for Apache Airflow

### 26. A demand forecast is read by planners in percentage terms, and the order point must be set. Which two practices apply? Select two.

- A. Choose the threshold from the cost of each error type
- B. Report MAPE when the error must be read as a percentage
- C. Report ROC AUC
- D. Report RMSE for the regression target
- E. Report precision-recall AUC for the rare class

### 27. An assistant cites internal policy documents and must not invent claims. What should be measured?

- A. Sample the answers for expert human review
- B. Measure the safety metrics on a fixed prompt set
- C. Measure groundedness against the retrieved context
- D. Score the answers with an LLM-as-a-judge rubric

### 28. A scientist needs every hyperparameter and metric of each run in one place. What should be used?

- A. Register the model in Agent Platform Model Registry
- B. Track artifacts and lineage in ML Metadata
- C. Log the run to Agent Platform Experiments
- D. Enable step caching

---

## Domain 3 — Scaling prototypes into ML models (Training at Scale and Model Choice)

### 29. A wide tabular dataset with strong interactions must be modelled from scratch. What model type fits?

- A. Choose a foundation model
- B. Choose a classical time series model
- C. Use TabNet as the custom training algorithm
- D. Choose a deep neural network

### 30. A custom tabular model must stay interpretable while using attention. Which algorithm fits?

- A. Use TabNet as the custom training algorithm
- B. Choose a classical time series model
- C. Choose a deep neural network
- D. Choose a foundation model

### 31. A team has labelled images and no deep-learning engineer. What should be used?

- A. Train a custom model on Agent Platform
- B. Use TabNet as the custom training algorithm
- C. Train with Agent Platform AutoML
- D. Build the model in BigQuery ML

### 32. A bespoke loss function is required and no managed trainer offers it. What should be used?

- A. Train with Agent Platform AutoML
- B. Train a custom model on Agent Platform
- C. Use TabNet as the custom training algorithm
- D. Build the model in BigQuery ML

### 33. Two recommendation models must be compared on revenue with a controlled share each, then limited exposure before full launch. Which two strategies apply? Select two.

- A. Run the new model in shadow mode
- B. Deploy blue/green with an instant switch
- C. Split traffic between two models in an A/B test
- D. Roll out a canary with a small traffic share
- E. Replace the model version in place

### 34. A new model must be scored on live traffic with its answers discarded. What strategy is described?

- A. Split traffic between two models in an A/B test
- B. Replace the model version in place
- C. Deploy blue/green with an instant switch
- D. Run the new model in shadow mode

### 35. A batch report must explain the drivers for each of 50,000 decisions. What should be used?

- A. Use sampled Shapley on the endpoint
- B. Explain with Shapley values
- C. Use integrated gradients for the image model
- D. Summarise the model with ML.GLOBAL_EXPLAIN

### 36. A reviewer must see which inputs moved one specific decision. What should be reported?

- A. Report the feature attributions to the reviewer
- B. Publish a model card with the intended use and limits
- C. Choose an inherently interpretable model
- D. Explain with Shapley values

### 37. Training must query the latest labelled rows without any copy step. What should be used?

- A. Stream the new records through Dataflow into the training store
- B. Read the training data directly from BigQuery
- C. Write the training data as TFRecord shards in Cloud Storage
- D. Write the training data as Parquet in Cloud Storage

### 38. A feature table is read column-wise by several frameworks. What format fits?

- A. Stream the new records through Dataflow into the training store
- B. Write the training data as Parquet in Cloud Storage
- C. Read the training data directly from BigQuery
- D. Write the training data as TFRecord shards in Cloud Storage

### 39. The clickstream must sit in the training store before the next window closes. What should be used?

- A. Stream the new records through Dataflow into the training store
- B. Deduplicate on the event key in the ingestion step
- C. Write the training data as TFRecord shards in Cloud Storage
- D. Read the training data directly from BigQuery

### 40. A malformed batch must be quarantined instead of failing the whole pipeline. What should be added?

- A. Validate the schema and quarantine rejected rows
- B. Deduplicate on the event key in the ingestion step
- C. Write the training data as Parquet in Cloud Storage
- D. Stream the new records through Dataflow into the training store

### 41. A standard TensorFlow trainer must run remotely without writing a Dockerfile. What should be used?

- A. Package the trainer as a Python package
- B. Run a custom container on Agent Platform
- C. Use a prebuilt serving container
- D. Export the AutoML model as an artifact

### 42. The trainer needs a system library that is absent from every Google image. What should be used?

- A. Use a prebuilt serving container
- B. Package the trainer as a Python package
- C. Run a custom container on Agent Platform
- D. Train with Agent Platform AutoML

### 43. A GPU job fails before any code runs in a region with no accelerator quota. What is the cause?

- A. Request accelerator quota for the region
- B. Pin the framework version in the container
- C. Reduce the per-replica batch size
- D. Grant the training service account access to the bucket

### 44. The loss becomes NaN after the first few hundred steps. What should be tried first?

- A. Grant the training service account access to the bucket
- B. Lower the learning rate
- C. Verify each worker reads a distinct shard
- D. Reduce the per-replica batch size

### 45. The search space is large, each trial is expensive, and the deadline is fixed. Which two choices apply? Select two.

- A. Choose Bayesian optimisation for the search
- B. Cap the search with a trial count and a parallel budget
- C. Enable early stopping of poor trials
- D. Report the business metric from the trainer
- E. Set the random seed in the training code

### 46. Nine of ten trials are clearly losing after two epochs and the queue is saturated. What should be enabled?

- A. Choose Bayesian optimisation for the search
- B. Cap the search with a trial count and a parallel budget
- C. Run a hyperparameter tuning job
- D. Enable early stopping of poor trials

### 47. A model must follow the house tone, and only one accelerator is available. What should be used?

- A. Distil the large model into a smaller one
- B. Fine-tune with a parameter-efficient adapter
- C. Fine-tune the full model
- D. Ground the prompt with retrieval instead of fine-tuning

### 48. A PyTorch codebase expects CUDA and needs mixed-precision training. What should be used?

- A. Serve on L4 GPUs
- B. Serve on CPU only
- C. Train on A100 GPUs
- D. Train on a TPU slice

### 49. A model fits on one device, and throughput must rise without changing the architecture. Which two choices apply? Select two.

- A. Scale the batch size with the worker count
- B. Serve on CPU only
- C. Configure the job as multi-worker with a chief
- D. Use model parallelism
- E. Use data parallelism

---

## Domain 4 — Serving and scaling models (Serving, Packaging, and Scaling Endpoints)

### 50. A pricing service must answer a single request in real time. What should be used?

- A. Deploy to an online endpoint
- B. Batch the requests inside the client
- C. Run batch prediction
- D. Send the events to a streaming prediction path

### 51. One workload is a nightly file and another is a per-event score. Which two paths apply? Select two.

- A. Run batch prediction
- B. Deploy to an online endpoint
- C. Batch the requests inside the client
- D. Attach a GPU to the serving replica
- E. Send the events to a streaming prediction path

### 52. Throughput is limited by round trips rather than by the model itself. What should the client do?

- A. Run batch prediction
- B. Batch the requests inside the client
- C. Enable autoscaling on the endpoint
- D. Raise the concurrency per replica

### 53. A scikit-learn model must be served without writing a handler. What should be used?

- A. Attach a GPU to the serving replica
- B. Add a custom prediction routine to the container
- C. Push the serving image to Artifact Registry
- D. Use a prebuilt serving container

### 54. Every serving image must carry a scan result before deployment. Where should the images live?

- A. Use a prebuilt serving container
- B. Enable autoscaling on the endpoint
- C. Push the serving image to Artifact Registry
- D. Register the model in Agent Platform Model Registry

### 55. Analysts must browse model versions with their metrics and lineage. What should be used?

- A. Track artifacts and lineage in ML Metadata
- B. Push the serving image to Artifact Registry
- C. Register the model in Agent Platform Model Registry
- D. Log the run to Agent Platform Experiments

### 56. The endpoint must always serve the version the team last approved. What should be used?

- A. Register the model in Agent Platform Model Registry
- B. Split traffic between two deployed versions
- C. Deploy blue/green with an instant switch
- D. Deploy the version and move the alias

### 57. A risky model must reach five per cent of traffic and hold there for a day. Which two controls apply? Select two.

- A. Run batch prediction
- B. Replace the model version in place
- C. Run the new model in shadow mode
- D. Roll out a canary with a small traffic share
- E. Split traffic between two deployed versions

### 58. Two variants must be compared on conversion with equal-sized populations. What strategy is described?

- A. Split traffic between two models in an A/B test
- B. Run the new model in shadow mode
- C. Replace the model version in place
- D. Roll out a canary with a small traffic share

### 59. The endpoint recomputes a feature with code that no longer matches the trainer's. What should be used?

- A. Register the feature in Agent Platform Feature Store
- B. Share one transformation library between training and serving
- C. Deploy the version and move the alias
- D. Enable step caching

### 60. A transformation bug keeps appearing only in production. What should be done?

- A. Keep the preprocessing inside the exported model
- B. Register the feature in Agent Platform Feature Store
- C. Share one transformation library between training and serving
- D. Add an explicit data validation step

### 61. A prototype must be callable immediately with no deployment step or capacity planning. What should be used?

- A. Use a shared public endpoint
- B. Attach a GPU to the serving replica
- C. Use a dedicated endpoint
- D. Deploy with a private endpoint only

### 62. A regulated model must not share capacity with any other tenant. What should be used?

- A. Deploy with a private endpoint only
- B. Use a shared public endpoint
- C. Use a dedicated endpoint
- D. Enable autoscaling on the endpoint

### 63. A 2 GB model needs acceleration at the lowest serving cost. What should be used?

- A. Serve on L4 GPUs
- B. Train on a TPU slice
- C. Serve on CPU only
- D. Train on A100 GPUs

### 64. A small model answers in 30 ms on CPU with a 500 ms budget. What should be chosen?

- A. Deploy to an Edge TPU device
- B. Attach a GPU to the serving replica
- C. Serve on CPU only
- D. Serve on L4 GPUs

### 65. A service must stay warm at all times but also stop scaling before the budget is blown. Which two settings bound it? Select two.

- A. Batch the requests inside the client
- B. Raise the maximum replica count
- C. Set a minimum replica count
- D. Raise the concurrency per replica
- E. Attach a GPU to the serving replica

### 66. Each replica serves one request at a time and the fleet is oversized. What should be raised?

- A. Attach a GPU to the serving replica
- B. Raise the maximum replica count
- C. Batch the requests inside the client
- D. Raise the concurrency per replica

### 67. Traffic spikes every lunchtime and capacity must follow without a person. What should be enabled?

- A. Enable autoscaling on the endpoint
- B. Raise the maximum replica count
- C. Batch the requests inside the client
- D. Set a minimum replica count

### 68. An endpoint must return attributions for each prediction on a model that already meets latency. Which two steps apply? Select two.

- A. Configure explanation metadata for the endpoint
- B. Deploy the version and move the alias
- C. Register the model in Agent Platform Model Registry
- D. Batch the requests inside the client
- E. Set a minimum replica count

### 69. A larger model now misses the latency target that the old one met on CPU. What should be changed?

- A. Raise the concurrency per replica
- B. Raise the maximum replica count
- C. Batch the requests inside the client
- D. Attach a GPU to the serving replica

---

## Domain 5 — Automating and orchestrating ML pipelines (Pipelines, Retraining, and CI/CD/CT)

### 70. A pipeline promotes every model it trains, including worse ones. What should be added?

- A. Add an explicit data validation step
- B. Enable step caching
- C. Gate the deployment on a model evaluation threshold
- D. Retrain when drift crosses the threshold

### 71. Upstream nulls must fail the run before any training compute is spent. What should be added?

- A. Enable step caching
- B. Gate the deployment on a model evaluation threshold
- C. Validate the schema and quarantine rejected rows
- D. Add an explicit data validation step

### 72. A rare-event model must be judged despite heavy imbalance and then operated at a chosen point. Which two practices apply? Select two.

- A. Enable step caching
- B. Choose the threshold from the cost of each error type
- C. Report ROC AUC
- D. Report MAPE when the error must be read as a percentage
- E. Report precision-recall AUC for the rare class

### 73. A nightly chain must coordinate a data warehouse load, a vendor API call, and a model refresh. What should orchestrate it?

- A. Use Ray on Agent Platform for the distributed compute
- B. Express the workflow as a Kubeflow pipeline
- C. Orchestrate the steps in Agent Platform Pipelines
- D. Orchestrate with Managed Service for Apache Airflow

### 74. Every training step must be a container with lineage recorded against the model. What should be used?

- A. Orchestrate with Managed Service for Apache Airflow
- B. Orchestrate the steps in Agent Platform Pipelines
- C. Express the workflow as a Kubeflow pipeline
- D. Use Ray on Agent Platform for the distributed compute

### 75. A distributed Python workload mixes data loading and training in one process. What should be used?

- A. Express the workflow as a Kubeflow pipeline
- B. Orchestrate with Managed Service for Apache Airflow
- C. Use Ray on Agent Platform for the distributed compute
- D. Orchestrate the steps in Agent Platform Pipelines

### 76. Deployment must start only after the unit tests and the container build succeed. What should be used?

- A. Enable step caching
- B. Orchestrate the steps in Agent Platform Pipelines
- C. Trigger the build and deploy from Cloud Build
- D. Add a Cloud Scheduler trigger to the pipeline

### 77. A feature uses the same formula in two repositories and they have diverged. What should be done?

- A. Share one transformation library between training and serving
- B. Enable step caching
- C. Keep the preprocessing inside the exported model
- D. Register the feature in Agent Platform Feature Store

### 78. A backfill and the online path must read one governed definition. Which two components apply? Select two.

- A. Read the historical features from the offline store
- B. Deduplicate on the event key in the ingestion step
- C. Register the model in Agent Platform Model Registry
- D. Preprocess in memory with pandas
- E. Register the feature in Agent Platform Feature Store

### 79. A schema change upstream must stop the training run immediately. What should be added?

- A. Enable step caching
- B. Gate the deployment on a model evaluation threshold
- C. Add an explicit data validation step
- D. Share one transformation library between training and serving

### 80. The endpoint needs the freshest feature value for one entity per request. What should be read?

- A. Serve the feature from the online store
- B. Read the historical features from the offline store
- C. Add a crossed feature for the interacting pair
- D. Enable feature monitoring on the feature group

### 81. Behaviour changes on a known weekly cycle and a fixed cadence is easy to audit. What policy fits?

- A. Retrain only on a manual request
- B. Retrain when drift crosses the threshold
- C. Retrain when the production metric drops
- D. Retrain on a fixed schedule

### 82. The only trustworthy signal is the weekly business metric. What policy fits?

- A. Retrain when drift crosses the threshold
- B. Retrain when the production metric drops
- C. Retrain on a fixed schedule
- D. Retrain only on a manual request

### 83. Retraining, evaluation, and promotion must all be automated in one path. What should be adopted?

- A. Retrain on a fixed schedule
- B. Extend CI/CD into continuous training
- C. Enable step caching
- D. Trigger the pipeline from the arrival of new data

### 84. Identical steps rerun for forty minutes on every deployment. What should be enabled?

- A. Enable step caching
- B. Retrain when drift crosses the threshold
- C. Add an explicit data validation step
- D. Gate the deployment on a model evaluation threshold

### 85. A monthly compliance retrain must start on the first working day. What should be added?

- A. Trigger the pipeline from the arrival of new data
- B. Retrain when the production metric drops
- C. Trigger the build and deploy from Cloud Build
- D. Add a Cloud Scheduler trigger to the pipeline

### 86. A new labelled batch arrives irregularly and must start the retrain at once. What should be used?

- A. Retrain only on a manual request
- B. Trigger the build and deploy from Cloud Build
- C. Trigger the pipeline from the arrival of new data
- D. Add a Cloud Scheduler trigger to the pipeline

### 87. A batch scoring pipeline must start at 23:00 every weekday. What should be added?

- A. Express the workflow as a Kubeflow pipeline
- B. Add a Cloud Scheduler trigger to the pipeline
- C. Trigger the pipeline from the arrival of new data
- D. Use Ray on Agent Platform for the distributed compute

---

## Domain 6 — Monitoring AI solutions (Responsible AI, Monitoring, and Drift)

### 88. An internal assistant must refuse out-of-scope requests and return parseable fields. Which two controls apply? Select two.

- A. Configure the model safety filters
- B. Redact the pattern-matchable fields with a regex
- C. Screen the prompts and responses with Model Armor
- D. Constrain the response to a JSON schema
- E. Put the boundary in the system instruction

### 89. A consumer-facing chat surface must block harmful categories by policy. What should be configured?

- A. Redact the pattern-matchable fields with a regex
- B. Constrain the response to a JSON schema
- C. Configure the model safety filters
- D. Screen the prompts and responses with Model Armor

### 90. Ten-digit account numbers keep appearing in prompts sent to a vendor model. What should be applied?

- A. Put the boundary in the system instruction
- B. Redact the pattern-matchable fields with a regex
- C. Configure the model safety filters
- D. Constrain the response to a JSON schema

### 91. A lending model must be evaluated for equal error rates across groups. What should be produced?

- A. Monitor the outcome rate across the protected groups
- B. Slice the evaluation metrics by the sensitive attribute
- C. Publish a model card with the intended use and limits
- D. Document the dataset with a data card

### 92. A new dataset arrives from a partner and its provenance is unknown. What should be produced?

- A. Slice the evaluation metrics by the sensitive attribute
- B. Monitor the outcome rate across the protected groups
- C. Document the dataset with a data card
- D. Publish a model card with the intended use and limits

### 93. An online decision must be explained per request with a bounded compute cost. What should be used?

- A. Explain with Shapley values
- B. Summarise the model with ML.GLOBAL_EXPLAIN
- C. Use integrated gradients for the image model
- D. Use sampled Shapley on the endpoint

### 94. Downstream teams keep using a model outside its intended population. What should be published?

- A. Choose an inherently interpretable model
- B. Publish a model card with the intended use and limits
- C. Report the feature attributions to the reviewer
- D. Document the dataset with a data card

### 95. A drift signal exists but no one is told when it fires. What should be added?

- A. Set the monitoring threshold from the acceptable error budget
- B. Route the monitoring alert to the owning team
- C. Track p95 latency per model version
- D. Log the prompt and response with redaction

### 96. A regression hides behind an unchanged average response time. What should be tracked?

- A. Enable Model Monitoring on the endpoint
- B. Track tokens and cost per request
- C. Track p95 latency per model version
- D. Route the monitoring alert to the owning team

### 97. No labels will arrive for a month, and quality must still be watched. Which two signals apply? Select two.

- A. Watch for data drift
- B. Watch for feature attribution drift
- C. Watch for concept drift
- D. Join the delayed ground truth back to the predictions
- E. Watch the prediction distribution

### 98. The same features are present but different ones now drive the prediction. What is this called?

- A. Watch for data drift
- B. Join the delayed ground truth back to the predictions
- C. Watch for concept drift
- D. Watch for feature attribution drift

### 99. A generative feature's monthly bill tripled with no traffic change. What should be tracked?

- A. Track p95 latency per model version
- B. Enable Model Monitoring on the endpoint
- C. Score a sample of live answers with the evaluation rubric
- D. Track tokens and cost per request

### 100. A summarisation feature must be checked for fidelity after every prompt change. What should be added?

- A. Score a sample of live answers with the evaluation rubric
- B. Track tokens and cost per request
- C. Enable Model Monitoring on the endpoint
- D. Track p95 latency per model version

---

## Answer key and explanations

### Question 1 — A

Answer: Create a BigQuery ML k-means model. K-means segments rows into unsupervised clusters without a labelled target. Local study-map skill 1.1 (BigQuery ML Model Building), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: K-means segments rows into unsupervised clusters without a labelled target.
- **B:** Incorrect for this question. ARIMA_PLUS models seasonality and trend and returns a forecast interval per period. Why the correct answer wins: K-means segments rows into unsupervised clusters without a labelled target.
- **C:** Incorrect for this question. Logistic regression predicts a binary outcome and trains inside BigQuery with SQL. Why the correct answer wins: K-means segments rows into unsupervised clusters without a labelled target.
- **D:** Incorrect for this question. Linear regression predicts a continuous value such as revenue or demand. Why the correct answer wins: K-means segments rows into unsupervised clusters without a labelled target.

### Question 2 — A, D

Answers: Create a BigQuery ML boosted tree classifier; Read the contribution of each feature with ML.EXPLAIN_PREDICT. Boosted trees capture non-linear interactions, and ML.EXPLAIN_PREDICT attributes each prediction. Boosted trees capture non-linear interactions in tabular data while staying in SQL. ML.EXPLAIN_PREDICT attributes each prediction to the features that moved it. Local study-map skill 1.1 (BigQuery ML Model Building), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. ML.EXPLAIN_PREDICT attributes each prediction to the features that moved it. In this case: Boosted trees capture non-linear interactions, and ML.EXPLAIN_PREDICT attributes each prediction.
- **B:** Incorrect for this question. Importing brings an already-trained model into BigQuery so SQL can score it. Why the correct answer wins: Boosted trees capture non-linear interactions, and ML.EXPLAIN_PREDICT attributes each prediction.
- **C:** Incorrect for this question. A nested column keeps per-row structured output such as labels and scores together. Why the correct answer wins: Boosted trees capture non-linear interactions, and ML.EXPLAIN_PREDICT attributes each prediction.
- **D:** Correct. Boosted trees capture non-linear interactions in tabular data while staying in SQL. In this case: Boosted trees capture non-linear interactions, and ML.EXPLAIN_PREDICT attributes each prediction.
- **E:** Incorrect for this question. The DNN model type fits non-linear patterns too complex for a linear model. Why the correct answer wins: Boosted trees capture non-linear interactions, and ML.EXPLAIN_PREDICT attributes each prediction.

### Question 3 — A

Answer: Inspect the metrics with ML.EVALUATE. ML.EVALUATE returns the model metrics against a labelled dataset. Local study-map skill 1.2 (BigQuery ML Feature Engineering and Prediction), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: ML.EVALUATE returns the model metrics against a labelled dataset.
- **B:** Incorrect for this question. Training consumes slots, so a reservation bounds the cost and the wait time. Why the correct answer wins: ML.EVALUATE returns the model metrics against a labelled dataset.
- **C:** Incorrect for this question. ML.PREDICT applies a trained model and returns the label and its probability. Why the correct answer wins: ML.EVALUATE returns the model metrics against a labelled dataset.
- **D:** Incorrect for this question. ML.GLOBAL_EXPLAIN ranks the features that matter most across the whole model. Why the correct answer wins: ML.EVALUATE returns the model metrics against a labelled dataset.

### Question 4 — C

Answer: Summarise the model with ML.GLOBAL_EXPLAIN. ML.GLOBAL_EXPLAIN ranks the features that matter most across the whole model. Local study-map skill 1.2 (BigQuery ML Feature Engineering and Prediction), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. ML.EXPLAIN_PREDICT attributes each prediction to the features that moved it. Why the correct answer wins: ML.GLOBAL_EXPLAIN ranks the features that matter most across the whole model.
- **B:** Incorrect for this question. ML.PREDICT applies a trained model and returns the label and its probability. Why the correct answer wins: ML.GLOBAL_EXPLAIN ranks the features that matter most across the whole model.
- **C:** Correct. In this case: ML.GLOBAL_EXPLAIN ranks the features that matter most across the whole model.
- **D:** Incorrect for this question. TRANSFORM keeps preprocessing inside the model, so prediction applies the same steps. Why the correct answer wins: ML.GLOBAL_EXPLAIN ranks the features that matter most across the whole model.

### Question 5 — D

Answer: Set a training budget in node hours. A node-hour budget caps how long AutoML searches, which bounds the cost. Local study-map skill 1.3 (Agent Platform AutoML), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A manual split is required when the split must follow time or a grouping column. Why the correct answer wins: A node-hour budget caps how long AutoML searches, which bounds the cost.
- **B:** Incorrect for this question. Export produces a container-ready artifact that can be served outside the managed endpoint. Why the correct answer wins: A node-hour budget caps how long AutoML searches, which bounds the cost.
- **C:** Incorrect for this question. AutoML uses a reproducible default split when the dataset is large enough to do so. Why the correct answer wins: A node-hour budget caps how long AutoML searches, which bounds the cost.
- **D:** Correct. In this case: A node-hour budget caps how long AutoML searches, which bounds the cost.

### Question 6 — A

Answer: Export the AutoML model as an artifact. Export produces a container-ready artifact that can be served outside the managed endpoint. Local study-map skill 1.3 (Agent Platform AutoML), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Export produces a container-ready artifact that can be served outside the managed endpoint.
- **B:** Incorrect for this question. A node-hour budget caps how long AutoML searches, which bounds the cost. Why the correct answer wins: Export produces a container-ready artifact that can be served outside the managed endpoint.
- **C:** Incorrect for this question. AutoML is the no-code path, which matters when the team has data skills but no ML engineers. Why the correct answer wins: Export produces a container-ready artifact that can be served outside the managed endpoint.
- **D:** Incorrect for this question. AutoML tabular selects the architecture and tuning for a structured dataset. Why the correct answer wins: Export produces a container-ready artifact that can be served outside the managed endpoint.

### Question 7 — B

Answer: Create a BigQuery ML remote model over Gemini. A remote model calls the Gemini endpoint from SQL, so generation runs where the data lives. Local study-map skill 1.4 (Gemini Fine-Tuning with BigQuery), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Retrieval is the cheaper answer when the problem is missing knowledge rather than missing behaviour. Why the correct answer wins: A remote model calls the Gemini endpoint from SQL, so generation runs where the data lives.
- **B:** Correct. In this case: A remote model calls the Gemini endpoint from SQL, so generation runs where the data lives.
- **C:** Incorrect for this question. Fine-tuning adapts a foundation model to the domain using rows that stay in BigQuery. Why the correct answer wins: A remote model calls the Gemini endpoint from SQL, so generation runs where the data lives.
- **D:** Incorrect for this question. Agent Platform is the current name for the managed ML platform that hosts training, pipelines, registry, and endpoints. Why the correct answer wins: A remote model calls the Gemini endpoint from SQL, so generation runs where the data lives.

### Question 8 — B

Answer: Send the image and the question in one multimodal request. A multimodal request removes the need for a separate captioning or OCR stage. Local study-map skill 1.5 (Model Garden Model Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A Document AI processor extracts structured fields from forms with layout awareness. Why the correct answer wins: A multimodal request removes the need for a separate captioning or OCR stage.
- **B:** Correct. In this case: A multimodal request removes the need for a separate captioning or OCR stage.
- **C:** Incorrect for this question. The prebuilt Vision model labels, detects, and reads text without training a model. Why the correct answer wins: A multimodal request removes the need for a separate captioning or OCR stage.
- **D:** Incorrect for this question. The translation model handles a large language set without custom training. Why the correct answer wins: A multimodal request removes the need for a separate captioning or OCR stage.

### Question 9 — A

Answer: Use the Speech-to-Text API. The speech model transcribes audio, including domain phrases through adaptation. Local study-map skill 1.6 (Industry AI APIs), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: The speech model transcribes audio, including domain phrases through adaptation.
- **B:** Incorrect for this question. Video Intelligence detects shots, labels, and explicit content in video. Why the correct answer wins: The speech model transcribes audio, including domain phrases through adaptation.
- **C:** Incorrect for this question. The translation model handles a large language set without custom training. Why the correct answer wins: The speech model transcribes audio, including domain phrases through adaptation.
- **D:** Incorrect for this question. The Natural Language API returns entities, sentiment, and syntax without a custom model. Why the correct answer wins: The speech model transcribes audio, including domain phrases through adaptation.

### Question 10 — C

Answer: Use the Translation API. The translation model handles a large language set without custom training. Local study-map skill 1.6 (Industry AI APIs), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The Natural Language API returns entities, sentiment, and syntax without a custom model. Why the correct answer wins: The translation model handles a large language set without custom training.
- **B:** Incorrect for this question. The speech model transcribes audio, including domain phrases through adaptation. Why the correct answer wins: The translation model handles a large language set without custom training.
- **C:** Correct. In this case: The translation model handles a large language set without custom training.
- **D:** Incorrect for this question. The prebuilt Vision model labels, detects, and reads text without training a model. Why the correct answer wins: The translation model handles a large language set without custom training.

### Question 11 — A, B

Answers: Call the model in the region that serves the users; Request a quota increase for the model. A regional endpoint removes cross-region latency, and throughput is capped by quota. A regional endpoint removes cross-region latency and satisfies residency rules. Throughput is capped by quota, so a quota ceiling cannot be solved by retries. Local study-map skill 1.7 (Gemini Application Optimization), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. Throughput is capped by quota, so a quota ceiling cannot be solved by retries. In this case: A regional endpoint removes cross-region latency, and throughput is capped by quota.
- **B:** Correct. A regional endpoint removes cross-region latency and satisfies residency rules. In this case: A regional endpoint removes cross-region latency, and throughput is capped by quota.
- **C:** Incorrect for this question. A bounded output cuts both latency and cost per request. Why the correct answer wins: A regional endpoint removes cross-region latency, and throughput is capped by quota.
- **D:** Incorrect for this question. Streaming improves perceived latency without reducing total generation time. Why the correct answer wins: A regional endpoint removes cross-region latency, and throughput is capped by quota.
- **E:** Incorrect for this question. A fallback keeps the application answering when the primary model returns resource-exhausted. Why the correct answer wins: A regional endpoint removes cross-region latency, and throughput is capped by quota.

### Question 12 — B

Answer: Stream the response tokens to the client. Streaming improves perceived latency without reducing total generation time. Local study-map skill 1.7 (Gemini Application Optimization), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Context caching bills the repeated prefix once instead of on every request. Why the correct answer wins: Streaming improves perceived latency without reducing total generation time.
- **B:** Correct. In this case: Streaming improves perceived latency without reducing total generation time.
- **C:** Incorrect for this question. The batch path trades latency for a lower price on non-interactive requests. Why the correct answer wins: Streaming improves perceived latency without reducing total generation time.
- **D:** Incorrect for this question. A bounded output cuts both latency and cost per request. Why the correct answer wins: Streaming improves perceived latency without reducing total generation time.

### Question 13 — B

Answer: Preprocess with a Dataflow pipeline. Dataflow runs the same Beam code in batch and streaming and scales without provisioning. Local study-map skill 2.1 (Preprocessing Tool Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Spark suits large transformations the team already has as Scala or PySpark code. Why the correct answer wins: Dataflow runs the same Beam code in batch and streaming and scales without provisioning.
- **B:** Correct. In this case: Dataflow runs the same Beam code in batch and streaming and scales without provisioning.
- **C:** Incorrect for this question. In-memory processing is the simplest option and stops working once the data exceeds the worker memory. Why the correct answer wins: Dataflow runs the same Beam code in batch and streaming and scales without provisioning.
- **D:** Incorrect for this question. SQL over BigQuery is the cheapest option when the data already sits there and the logic is set-based. Why the correct answer wins: Dataflow runs the same Beam code in batch and streaming and scales without provisioning.

### Question 14 — C, D

Answers: Split by entity so one customer never spans train and test; Remove the post-outcome column from the features. Grouping the split prevents leakage between rows, and a post-outcome column encodes the answer. Grouping the split prevents leakage between the training and evaluation rows. A column written after the outcome encodes the answer and inflates the score. Local study-map skill 2.1 (Preprocessing Tool Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Dropping the field removes the exposure entirely when the model does not need it. Why the correct answer wins: Grouping the split prevents leakage between rows, and a post-outcome column encodes the answer.
- **B:** Incorrect for this question. A time-based split prevents the model from learning from the future. Why the correct answer wins: Grouping the split prevents leakage between rows, and a post-outcome column encodes the answer.
- **C:** Correct. Grouping the split prevents leakage between the training and evaluation rows. In this case: Grouping the split prevents leakage between rows, and a post-outcome column encodes the answer.
- **D:** Correct. A column written after the outcome encodes the answer and inflates the score. In this case: Grouping the split prevents leakage between rows, and a post-outcome column encodes the answer.
- **E:** Incorrect for this question. Scaling keeps one large-magnitude feature from dominating the gradient. Why the correct answer wins: Grouping the split prevents leakage between rows, and a post-outcome column encodes the answer.

### Question 15 — A

Answer: Preprocess with Spark on Dataproc. Spark suits large transformations the team already has as Scala or PySpark code. Local study-map skill 2.1 (Preprocessing Tool Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Spark suits large transformations the team already has as Scala or PySpark code.
- **B:** Incorrect for this question. In-memory processing is the simplest option and stops working once the data exceeds the worker memory. Why the correct answer wins: Spark suits large transformations the team already has as Scala or PySpark code.
- **C:** Incorrect for this question. SQL over BigQuery is the cheapest option when the data already sits there and the logic is set-based. Why the correct answer wins: Spark suits large transformations the team already has as Scala or PySpark code.
- **D:** Incorrect for this question. Dataflow runs the same Beam code in batch and streaming and scales without provisioning. Why the correct answer wins: Spark suits large transformations the team already has as Scala or PySpark code.

### Question 16 — C

Answer: Serve the feature from the online store. The online store returns the latest feature value at low latency for a single entity. Local study-map skill 2.2 (Feature Store), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The offline store returns point-in-time values for training. Why the correct answer wins: The online store returns the latest feature value at low latency for a single entity.
- **B:** Incorrect for this question. Feature monitoring reports distribution changes per feature, not just per model. Why the correct answer wins: The online store returns the latest feature value at low latency for a single entity.
- **C:** Correct. In this case: The online store returns the latest feature value at low latency for a single entity.
- **D:** Incorrect for this question. A crossed feature lets a linear model express the interaction it cannot learn alone. Why the correct answer wins: The online store returns the latest feature value at low latency for a single entity.

### Question 17 — D

Answer: Enable feature monitoring on the feature group. Feature monitoring reports distribution changes per feature, not just per model. Local study-map skill 2.2 (Feature Store), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The online store returns the latest feature value at low latency for a single entity. Why the correct answer wins: Feature monitoring reports distribution changes per feature, not just per model.
- **B:** Incorrect for this question. Model Monitoring compares live traffic with the training baseline and reports skew and drift. Why the correct answer wins: Feature monitoring reports distribution changes per feature, not just per model.
- **C:** Incorrect for this question. Feature Store keeps one definition that both training and serving read. Why the correct answer wins: Feature monitoring reports distribution changes per feature, not just per model.
- **D:** Correct. In this case: Feature monitoring reports distribution changes per feature, not just per model.

### Question 18 — D

Answer: Drop the identifier columns before the training dataset is written. Dropping the field removes the exposure entirely when the model does not need it. Local study-map skill 2.3 (PII Handling and Data Privacy), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts PII. Why the correct answer wins: Dropping the field removes the exposure entirely when the model does not need it.
- **B:** Incorrect for this question. A salted hash keeps the join key usable while removing the direct identifier. Why the correct answer wins: Dropping the field removes the exposure entirely when the model does not need it.
- **C:** Incorrect for this question. Restricting the bucket limits who can copy the raw data in the first place. Why the correct answer wins: Dropping the field removes the exposure entirely when the model does not need it.
- **D:** Correct. In this case: Dropping the field removes the exposure entirely when the model does not need it.

### Question 19 — D

Answer: De-identify the fields with Sensitive Data Protection. Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts PII. Local study-map skill 2.3 (PII Handling and Data Privacy), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Dropping the field removes the exposure entirely when the model does not need it. Why the correct answer wins: Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts PII.
- **B:** Incorrect for this question. Restricting the bucket limits who can copy the raw data in the first place. Why the correct answer wins: Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts PII.
- **C:** Incorrect for this question. A salted hash keeps the join key usable while removing the direct identifier. Why the correct answer wins: Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts PII.
- **D:** Correct. In this case: Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts PII.

### Question 20 — D

Answer: Pin the runtime to a custom container image. A pinned image makes the environment reproducible across users. Local study-map skill 2.4 (Notebook Environments and Security), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Workbench is the managed notebook instance inside the project VPC. Why the correct answer wins: A pinned image makes the environment reproducible across users.
- **B:** Incorrect for this question. Colab Enterprise adds managed runtimes, VPC connectivity, and IAM to the Colab experience. Why the correct answer wins: A pinned image makes the environment reproducible across users.
- **C:** Incorrect for this question. Idle shutdown stops paying for a notebook nobody is using. Why the correct answer wins: A pinned image makes the environment reproducible across users.
- **D:** Correct. In this case: A pinned image makes the environment reproducible across users.

### Question 21 — D

Answer: Attach the runtime to the shared VPC subnet. The subnet attachment gives the notebook the route to internal data sources. Local study-map skill 2.4 (Notebook Environments and Security), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A private-IP runtime reaches the data through the VPC and cannot be opened from the internet. Why the correct answer wins: The subnet attachment gives the notebook the route to internal data sources.
- **B:** Incorrect for this question. Workbench is the managed notebook instance inside the project VPC. Why the correct answer wins: The subnet attachment gives the notebook the route to internal data sources.
- **C:** Incorrect for this question. Idle shutdown stops paying for a notebook nobody is using. Why the correct answer wins: The subnet attachment gives the notebook the route to internal data sources.
- **D:** Correct. In this case: The subnet attachment gives the notebook the route to internal data sources.

### Question 22 — D

Answer: Compare the runs on the validation metric. Comparing on the validation metric keeps model selection independent of the test set. Local study-map skill 2.5 (Experiment Tracking), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. ML Metadata records which data and code produced which artifact. Why the correct answer wins: Comparing on the validation metric keeps model selection independent of the test set.
- **B:** Incorrect for this question. A fixed seed makes a rerun reproducible when the rest of the environment is pinned. Why the correct answer wins: Comparing on the validation metric keeps model selection independent of the test set.
- **C:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: Comparing on the validation metric keeps model selection independent of the test set.
- **D:** Correct. In this case: Comparing on the validation metric keeps model selection independent of the test set.

### Question 23 — B

Answer: Track artifacts and lineage in ML Metadata. ML Metadata records which data and code produced which artifact. Local study-map skill 2.5 (Experiment Tracking), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Experiments records parameters, metrics, and artifacts per run so runs can be compared. Why the correct answer wins: ML Metadata records which data and code produced which artifact.
- **B:** Correct. In this case: ML Metadata records which data and code produced which artifact.
- **C:** Incorrect for this question. The registry versions the model artifact and links it to its lineage and metrics. Why the correct answer wins: ML Metadata records which data and code produced which artifact.
- **D:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: ML Metadata records which data and code produced which artifact.

### Question 24 — B, D

Answers: Express the workflow as a Kubeflow pipeline; Start from a Google-provided pipeline template. A Kubeflow pipeline is container-per-step, and a template encodes the validated step order. Kubeflow pipelines give a container-per-step pipeline that runs on the managed service or on GKE. A template encodes the validated step order, so the first pipeline is not bespoke. Local study-map skill 2.6 (Development Environment Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Ray fits a Python-native distributed workload that is not a container-per-step pipeline. Why the correct answer wins: A Kubeflow pipeline is container-per-step, and a template encodes the validated step order.
- **B:** Correct. A template encodes the validated step order, so the first pipeline is not bespoke. In this case: A Kubeflow pipeline is container-per-step, and a template encodes the validated step order.
- **C:** Incorrect for this question. Experiments records parameters, metrics, and artifacts per run so runs can be compared. Why the correct answer wins: A Kubeflow pipeline is container-per-step, and a template encodes the validated step order.
- **D:** Correct. Kubeflow pipelines give a container-per-step pipeline that runs on the managed service or on GKE. In this case: A Kubeflow pipeline is container-per-step, and a template encodes the validated step order.
- **E:** Incorrect for this question. Airflow expresses cross-system dependencies and schedules outside the ML platform. Why the correct answer wins: A Kubeflow pipeline is container-per-step, and a template encodes the validated step order.

### Question 25 — A

Answer: Orchestrate the steps in Agent Platform Pipelines. Pipelines runs each step as a container with caching, lineage, and retry. Local study-map skill 2.6 (Development Environment Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Pipelines runs each step as a container with caching, lineage, and retry.
- **B:** Incorrect for this question. Experiments records parameters, metrics, and artifacts per run so runs can be compared. Why the correct answer wins: Pipelines runs each step as a container with caching, lineage, and retry.
- **C:** Incorrect for this question. Kubeflow pipelines give a container-per-step pipeline that runs on the managed service or on GKE. Why the correct answer wins: Pipelines runs each step as a container with caching, lineage, and retry.
- **D:** Incorrect for this question. Airflow expresses cross-system dependencies and schedules outside the ML platform. Why the correct answer wins: Pipelines runs each step as a container with caching, lineage, and retry.

### Question 26 — A, B

Answers: Report MAPE when the error must be read as a percentage; Choose the threshold from the cost of each error type. MAPE expresses the error relative to the actual value, and the threshold follows the cost of each error. MAPE expresses the error relative to the actual value, which business readers understand. The decision threshold follows the relative cost of a false positive and a false negative. Local study-map skill 2.7 (Evaluation Metrics and LLM-as-a-Judge), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. The decision threshold follows the relative cost of a false positive and a false negative. In this case: MAPE expresses the error relative to the actual value, and the threshold follows the cost of each error.
- **B:** Correct. MAPE expresses the error relative to the actual value, which business readers understand. In this case: MAPE expresses the error relative to the actual value, and the threshold follows the cost of each error.
- **C:** Incorrect for this question. ROC AUC measures ranking quality across thresholds and hides class imbalance. Why the correct answer wins: MAPE expresses the error relative to the actual value, and the threshold follows the cost of each error.
- **D:** Incorrect for this question. RMSE expresses the typical error in the units of the target. Why the correct answer wins: MAPE expresses the error relative to the actual value, and the threshold follows the cost of each error.
- **E:** Incorrect for this question. Precision-recall AUC stays informative when the positive class is rare. Why the correct answer wins: MAPE expresses the error relative to the actual value, and the threshold follows the cost of each error.

### Question 27 — C

Answer: Measure groundedness against the retrieved context. Groundedness checks whether each claim is supported by the documents that were retrieved. Local study-map skill 2.7 (Evaluation Metrics and LLM-as-a-Judge), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Human review remains the reference standard for a sample the judge is calibrated against. Why the correct answer wins: Groundedness checks whether each claim is supported by the documents that were retrieved.
- **B:** Incorrect for this question. A fixed prompt set makes the safety score comparable between releases. Why the correct answer wins: Groundedness checks whether each claim is supported by the documents that were retrieved.
- **C:** Correct. In this case: Groundedness checks whether each claim is supported by the documents that were retrieved.
- **D:** Incorrect for this question. A rubric-driven judge scales the evaluation of free-text answers beyond human review. Why the correct answer wins: Groundedness checks whether each claim is supported by the documents that were retrieved.

### Question 28 — C

Answer: Log the run to Agent Platform Experiments. Experiments records parameters, metrics, and artifacts per run so runs can be compared. Local study-map skill 2.8 (Metadata and Lineage), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The registry versions the model artifact and links it to its lineage and metrics. Why the correct answer wins: Experiments records parameters, metrics, and artifacts per run so runs can be compared.
- **B:** Incorrect for this question. ML Metadata records which data and code produced which artifact. Why the correct answer wins: Experiments records parameters, metrics, and artifacts per run so runs can be compared.
- **C:** Correct. In this case: Experiments records parameters, metrics, and artifacts per run so runs can be compared.
- **D:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: Experiments records parameters, metrics, and artifacts per run so runs can be compared.

### Question 29 — D

Answer: Choose a deep neural network. A DNN suits a large tabular dataset where interactions matter. Local study-map skill 3.1 (Model Type Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A foundation model suits an open-ended language or multimodal task where labelled data is scarce. Why the correct answer wins: A DNN suits a large tabular dataset where interactions matter.
- **B:** Incorrect for this question. A classical time series model suits a single series with strong seasonality and little covariate data. Why the correct answer wins: A DNN suits a large tabular dataset where interactions matter.
- **C:** Incorrect for this question. TabNet gives an interpretable attentive tabular model inside custom training. Why the correct answer wins: A DNN suits a large tabular dataset where interactions matter.
- **D:** Correct. In this case: A DNN suits a large tabular dataset where interactions matter.

### Question 30 — A

Answer: Use TabNet as the custom training algorithm. TabNet gives an interpretable attentive tabular model inside custom training. Local study-map skill 3.1 (Model Type Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: TabNet gives an interpretable attentive tabular model inside custom training.
- **B:** Incorrect for this question. A classical time series model suits a single series with strong seasonality and little covariate data. Why the correct answer wins: TabNet gives an interpretable attentive tabular model inside custom training.
- **C:** Incorrect for this question. A DNN suits a large tabular or unstructured dataset where interactions matter. Why the correct answer wins: TabNet gives an interpretable attentive tabular model inside custom training.
- **D:** Incorrect for this question. A foundation model suits an open-ended language or multimodal task where labelled data is scarce. Why the correct answer wins: TabNet gives an interpretable attentive tabular model inside custom training.

### Question 31 — C

Answer: Train with Agent Platform AutoML. AutoML removes architecture search and tuning from the team while keeping a managed endpoint. Local study-map skill 3.2 (Product Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Custom training keeps full control of the framework and the loss. Why the correct answer wins: AutoML removes architecture search and tuning from the team while keeping a managed endpoint.
- **B:** Incorrect for this question. TabNet gives an interpretable attentive tabular model inside custom training. Why the correct answer wins: AutoML removes architecture search and tuning from the team while keeping a managed endpoint.
- **C:** Correct. In this case: AutoML removes architecture search and tuning from the team while keeping a managed endpoint.
- **D:** Incorrect for this question. BigQuery ML keeps training next to the data and removes a separate serving pipeline. Why the correct answer wins: AutoML removes architecture search and tuning from the team while keeping a managed endpoint.

### Question 32 — B

Answer: Train a custom model on Agent Platform. Custom training keeps full control of the framework and the loss. Local study-map skill 3.2 (Product Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. AutoML removes architecture search and tuning from the team while keeping a managed endpoint. Why the correct answer wins: Custom training keeps full control of the framework and the loss.
- **B:** Correct. In this case: Custom training keeps full control of the framework and the loss.
- **C:** Incorrect for this question. TabNet gives an interpretable attentive tabular model inside custom training. Why the correct answer wins: Custom training keeps full control of the framework and the loss.
- **D:** Incorrect for this question. BigQuery ML keeps training next to the data and removes a separate serving pipeline. Why the correct answer wins: Custom training keeps full control of the framework and the loss.

### Question 33 — C, D

Answers: Split traffic between two models in an A/B test; Roll out a canary with a small traffic share. A/B testing compares two models on one population, and a canary limits the exposure. A/B testing compares two models on the same population with a traffic split. A canary limits the blast radius while the new model is compared with the old one. Local study-map skill 3.3 (Deployment Strategy Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Shadow mode scores live traffic without serving its answers, so the comparison costs nothing to users. Why the correct answer wins: A/B testing compares two models on one population, and a canary limits the exposure.
- **B:** Incorrect for this question. Two identical deployments let the switch be reversed immediately. Why the correct answer wins: A/B testing compares two models on one population, and a canary limits the exposure.
- **C:** Correct. A/B testing compares two models on the same population with a traffic split. In this case: A/B testing compares two models on one population, and a canary limits the exposure.
- **D:** Correct. A canary limits the blast radius while the new model is compared with the old one. In this case: A/B testing compares two models on one population, and a canary limits the exposure.
- **E:** Incorrect for this question. An in-place replacement exposes every request to the new version at once. Why the correct answer wins: A/B testing compares two models on one population, and a canary limits the exposure.

### Question 34 — D

Answer: Run the new model in shadow mode. Shadow mode scores live traffic without serving its answers. Local study-map skill 3.3 (Deployment Strategy Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A/B testing compares two models on the same population with a traffic split. Why the correct answer wins: Shadow mode scores live traffic without serving its answers.
- **B:** Incorrect for this question. An in-place replacement exposes every request to the new version at once. Why the correct answer wins: Shadow mode scores live traffic without serving its answers.
- **C:** Incorrect for this question. Two identical deployments let the switch be reversed immediately. Why the correct answer wins: Shadow mode scores live traffic without serving its answers.
- **D:** Correct. In this case: Shadow mode scores live traffic without serving its answers.

### Question 35 — B

Answer: Explain with Shapley values. Shapley values attribute a prediction to its features with a consistent baseline. Local study-map skill 3.4 (Interpretability), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Sampled Shapley explains individual online predictions with a bounded compute cost. Why the correct answer wins: Shapley values attribute a prediction to its features with a consistent baseline.
- **B:** Correct. In this case: Shapley values attribute a prediction to its features with a consistent baseline.
- **C:** Incorrect for this question. Integrated gradients attributes an image prediction to the pixels that moved it. Why the correct answer wins: Shapley values attribute a prediction to its features with a consistent baseline.
- **D:** Incorrect for this question. ML.GLOBAL_EXPLAIN ranks the features that matter most across the whole model. Why the correct answer wins: Shapley values attribute a prediction to its features with a consistent baseline.

### Question 36 — A

Answer: Report the feature attributions to the reviewer. Attribution shows which inputs drove the decision in the case being examined. Local study-map skill 3.4 (Interpretability), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Attribution shows which inputs drove the decision in the case being examined.
- **B:** Incorrect for this question. The card states where the model may be used and where it must not. Why the correct answer wins: Attribution shows which inputs drove the decision in the case being examined.
- **C:** Incorrect for this question. A linear or tree model can be read directly when regulation demands an explanation by construction. Why the correct answer wins: Attribution shows which inputs drove the decision in the case being examined.
- **D:** Incorrect for this question. Shapley values attribute a prediction to its features with a consistent baseline. Why the correct answer wins: Attribution shows which inputs drove the decision in the case being examined.

### Question 37 — B

Answer: Read the training data directly from BigQuery. Reading from BigQuery avoids a copy and keeps the query pushdown. Local study-map skill 3.5 (Training Data Organization), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A streaming path keeps the training data current without a nightly copy. Why the correct answer wins: Reading from BigQuery avoids a copy and keeps the query pushdown.
- **B:** Correct. In this case: Reading from BigQuery avoids a copy and keeps the query pushdown.
- **C:** Incorrect for this question. Sharded TFRecord is the efficient read format for distributed training. Why the correct answer wins: Reading from BigQuery avoids a copy and keeps the query pushdown.
- **D:** Incorrect for this question. Parquet is columnar and cheap to scan for tabular training data. Why the correct answer wins: Reading from BigQuery avoids a copy and keeps the query pushdown.

### Question 38 — B

Answer: Write the training data as Parquet in Cloud Storage. Parquet is columnar and cheap to scan for tabular training data. Local study-map skill 3.5 (Training Data Organization), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A streaming path keeps the training data current without a nightly copy. Why the correct answer wins: Parquet is columnar and cheap to scan for tabular training data.
- **B:** Correct. In this case: Parquet is columnar and cheap to scan for tabular training data.
- **C:** Incorrect for this question. Reading from BigQuery avoids a copy and keeps the query pushdown. Why the correct answer wins: Parquet is columnar and cheap to scan for tabular training data.
- **D:** Incorrect for this question. Sharded TFRecord is the efficient read format for distributed training. Why the correct answer wins: Parquet is columnar and cheap to scan for tabular training data.

### Question 39 — A

Answer: Stream the new records through Dataflow into the training store. A streaming path keeps the training data current without a nightly copy. Local study-map skill 3.6 (Ingestion into Training Pipelines), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: A streaming path keeps the training data current without a nightly copy.
- **B:** Incorrect for this question. Deduplicating at ingest stops duplicated records inflating the training set. Why the correct answer wins: A streaming path keeps the training data current without a nightly copy.
- **C:** Incorrect for this question. Sharded TFRecord is the efficient read format for distributed training. Why the correct answer wins: A streaming path keeps the training data current without a nightly copy.
- **D:** Incorrect for this question. Reading from BigQuery avoids a copy and keeps the query pushdown. Why the correct answer wins: A streaming path keeps the training data current without a nightly copy.

### Question 40 — A

Answer: Validate the schema and quarantine rejected rows. Rejecting rows into a side table makes a schema break visible instead of silent. Local study-map skill 3.6 (Ingestion into Training Pipelines), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Rejecting rows into a side table makes a schema break visible instead of silent.
- **B:** Incorrect for this question. Deduplicating at ingest stops duplicated records inflating the training set. Why the correct answer wins: Rejecting rows into a side table makes a schema break visible instead of silent.
- **C:** Incorrect for this question. Parquet is columnar and cheap to scan for tabular training data. Why the correct answer wins: Rejecting rows into a side table makes a schema break visible instead of silent.
- **D:** Incorrect for this question. A streaming path keeps the training data current without a nightly copy. Why the correct answer wins: Rejecting rows into a side table makes a schema break visible instead of silent.

### Question 41 — C

Answer: Use a prebuilt serving container. The prebuilt container already implements the framework handler. Local study-map skill 3.7 (Custom Training and SDKs), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The prebuilt container installs the package, which is the lightest way to run custom code. Why the correct answer wins: The prebuilt container already implements the framework handler.
- **B:** Incorrect for this question. A custom container carries its own framework and dependencies into the managed training job. Why the correct answer wins: The prebuilt container already implements the framework handler.
- **C:** Correct. In this case: The prebuilt container already implements the framework handler.
- **D:** Incorrect for this question. Export produces a container-ready artifact that can be served outside the managed endpoint. Why the correct answer wins: The prebuilt container already implements the framework handler.

### Question 42 — C

Answer: Run a custom container on Agent Platform. A custom container carries its own framework and dependencies into the managed training job. Local study-map skill 3.7 (Custom Training and SDKs), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A prebuilt container already implements the framework handler, so no serving code is written. Why the correct answer wins: A custom container carries its own framework and dependencies into the managed training job.
- **B:** Incorrect for this question. The prebuilt container installs the package, which is the lightest way to run custom code. Why the correct answer wins: A custom container carries its own framework and dependencies into the managed training job.
- **C:** Correct. In this case: A custom container carries its own framework and dependencies into the managed training job.
- **D:** Incorrect for this question. AutoML removes architecture search and tuning from the team while keeping a managed endpoint. Why the correct answer wins: A custom container carries its own framework and dependencies into the managed training job.

### Question 43 — A

Answer: Request accelerator quota for the region. Accelerator quota is regional and blocks the job before the code runs. Local study-map skill 3.8 (Training Failure Troubleshooting), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Accelerator quota is regional and blocks the job before the code runs.
- **B:** Incorrect for this question. A framework mismatch between local and remote runs changes behaviour without changing the code. Why the correct answer wins: Accelerator quota is regional and blocks the job before the code runs.
- **C:** Incorrect for this question. The out-of-memory error is a memory-per-step problem, so the batch is the first lever. Why the correct answer wins: Accelerator quota is regional and blocks the job before the code runs.
- **D:** Incorrect for this question. A permission error on the input is a missing IAM binding, not a model problem. Why the correct answer wins: Accelerator quota is regional and blocks the job before the code runs.

### Question 44 — B

Answer: Lower the learning rate. A loss that becomes NaN usually reflects a step size too large for the data scale. Local study-map skill 3.8 (Training Failure Troubleshooting), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A permission error on the input is a missing IAM binding, not a model problem. Why the correct answer wins: A loss that becomes NaN usually reflects a step size too large for the data scale.
- **B:** Correct. In this case: A loss that becomes NaN usually reflects a step size too large for the data scale.
- **C:** Incorrect for this question. Duplicated shards silently shrink the effective dataset and skew the loss. Why the correct answer wins: A loss that becomes NaN usually reflects a step size too large for the data scale.
- **D:** Incorrect for this question. The out-of-memory error is a memory-per-step problem, so the batch is the first lever. Why the correct answer wins: A loss that becomes NaN usually reflects a step size too large for the data scale.

### Question 45 — A, B

Answers: Choose Bayesian optimisation for the search; Cap the search with a trial count and a parallel budget. Bayesian search spends fewer trials, and the budget bounds cost and wall-clock time. Bayesian search spends fewer trials to reach a good configuration. The budget bounds both the cost and the wall-clock time of the search. Local study-map skill 3.9 (Hyperparameter Tuning), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. Bayesian search spends fewer trials to reach a good configuration. In this case: Bayesian search spends fewer trials, and the budget bounds cost and wall-clock time.
- **B:** Correct. The budget bounds both the cost and the wall-clock time of the search. In this case: Bayesian search spends fewer trials, and the budget bounds cost and wall-clock time.
- **C:** Incorrect for this question. Early stopping frees capacity from trials that cannot win. Why the correct answer wins: Bayesian search spends fewer trials, and the budget bounds cost and wall-clock time.
- **D:** Incorrect for this question. The search optimises the metric the trainer reports, so it must be the one that matters. Why the correct answer wins: Bayesian search spends fewer trials, and the budget bounds cost and wall-clock time.
- **E:** Incorrect for this question. A fixed seed makes a rerun reproducible when the rest of the environment is pinned. Why the correct answer wins: Bayesian search spends fewer trials, and the budget bounds cost and wall-clock time.

### Question 46 — D

Answer: Enable early stopping of poor trials. Early stopping frees capacity from trials that cannot win. Local study-map skill 3.9 (Hyperparameter Tuning), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Bayesian search spends fewer trials to reach a good configuration. Why the correct answer wins: Early stopping frees capacity from trials that cannot win.
- **B:** Incorrect for this question. The budget bounds both the cost and the wall-clock time of the search. Why the correct answer wins: Early stopping frees capacity from trials that cannot win.
- **C:** Incorrect for this question. The tuning service searches the space in parallel and reports the best trial. Why the correct answer wins: Early stopping frees capacity from trials that cannot win.
- **D:** Correct. In this case: Early stopping frees capacity from trials that cannot win.

### Question 47 — B

Answer: Fine-tune with a parameter-efficient adapter. A parameter-efficient adapter trains a small number of weights and keeps the base model intact. Local study-map skill 3.10 (Fine-Tuning Decisions), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Distillation moves the quality of the teacher into a model cheap enough to serve. Why the correct answer wins: A parameter-efficient adapter trains a small number of weights and keeps the base model intact.
- **B:** Correct. In this case: A parameter-efficient adapter trains a small number of weights and keeps the base model intact.
- **C:** Incorrect for this question. Full fine-tuning updates every weight and needs the most data and accelerator memory. Why the correct answer wins: A parameter-efficient adapter trains a small number of weights and keeps the base model intact.
- **D:** Incorrect for this question. Retrieval is the cheaper answer when the problem is missing knowledge rather than missing behaviour. Why the correct answer wins: A parameter-efficient adapter trains a small number of weights and keeps the base model intact.

### Question 48 — C

Answer: Train on A100 GPUs. A100 GPUs suit mixed-precision training where the framework expects CUDA. Local study-map skill 3.11 (Hardware and Accelerator Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. An L4 GPU gives low-cost inference acceleration for a modest model. Why the correct answer wins: A100 GPUs suit mixed-precision training where the framework expects CUDA.
- **B:** Incorrect for this question. CPU serving is the cheapest option for a small model with a generous latency budget. Why the correct answer wins: A100 GPUs suit mixed-precision training where the framework expects CUDA.
- **C:** Correct. In this case: A100 GPUs suit mixed-precision training where the framework expects CUDA.
- **D:** Incorrect for this question. A TPU slice gives a tightly coupled accelerator fabric for large synchronous training. Why the correct answer wins: A100 GPUs suit mixed-precision training where the framework expects CUDA.

### Question 49 — A, E

Answers: Use data parallelism; Scale the batch size with the worker count. Data parallelism splits each batch across workers, and a larger global batch keeps each worker busy. Data parallelism replicates the model and splits each batch across the workers. A larger global batch keeps each worker busy after the split. Local study-map skill 3.12 (Distributed Training), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. A larger global batch keeps each worker busy after the split. In this case: Data parallelism splits each batch across workers, and a larger global batch keeps each worker busy.
- **B:** Incorrect for this question. CPU serving is the cheapest option for a small model with a generous latency budget. Why the correct answer wins: Data parallelism splits each batch across workers, and a larger global batch keeps each worker busy.
- **C:** Incorrect for this question. Multi-worker gives each replica a shard of the data and a defined chief. Why the correct answer wins: Data parallelism splits each batch across workers, and a larger global batch keeps each worker busy.
- **D:** Incorrect for this question. Model parallelism splits the layers across devices when one model does not fit on one. Why the correct answer wins: Data parallelism splits each batch across workers, and a larger global batch keeps each worker busy.
- **E:** Correct. Data parallelism replicates the model and splits each batch across the workers. In this case: Data parallelism splits each batch across workers, and a larger global batch keeps each worker busy.

### Question 50 — A

Answer: Deploy to an online endpoint. An endpoint keeps capacity ready for low-latency per-request predictions. Local study-map skill 4.1 (Batch and Online Inference), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: An endpoint keeps capacity ready for low-latency per-request predictions.
- **B:** Incorrect for this question. Batching amortises the per-request overhead when the caller can wait. Why the correct answer wins: An endpoint keeps capacity ready for low-latency per-request predictions.
- **C:** Incorrect for this question. Batch prediction reads a file or table and writes predictions without holding serving capacity. Why the correct answer wins: An endpoint keeps capacity ready for low-latency per-request predictions.
- **D:** Incorrect for this question. Streaming answers each event as it arrives rather than on a schedule. Why the correct answer wins: An endpoint keeps capacity ready for low-latency per-request predictions.

### Question 51 — A, E

Answers: Run batch prediction; Send the events to a streaming prediction path. Batch prediction reads a file without serving capacity, and streaming answers each event as it arrives. Batch prediction reads a file or table and writes predictions without holding serving capacity. Streaming answers each event as it arrives rather than on a schedule. Local study-map skill 4.1 (Batch and Online Inference), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. Batch prediction reads a file or table and writes predictions without holding serving capacity. In this case: Batch prediction reads a file without serving capacity, and streaming answers each event as it arrives.
- **B:** Incorrect for this question. An endpoint keeps capacity ready for low-latency per-request predictions. Why the correct answer wins: Batch prediction reads a file without serving capacity, and streaming answers each event as it arrives.
- **C:** Incorrect for this question. Batching amortises the per-request overhead when the caller can wait. Why the correct answer wins: Batch prediction reads a file without serving capacity, and streaming answers each event as it arrives.
- **D:** Incorrect for this question. A GPU shortens inference time enough to meet a tight latency target. Why the correct answer wins: Batch prediction reads a file without serving capacity, and streaming answers each event as it arrives.
- **E:** Correct. Streaming answers each event as it arrives rather than on a schedule. In this case: Batch prediction reads a file without serving capacity, and streaming answers each event as it arrives.

### Question 52 — B

Answer: Batch the requests inside the client. Batching amortises the per-request overhead when the caller can wait. Local study-map skill 4.1 (Batch and Online Inference), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Batch prediction reads a file or table and writes predictions without holding serving capacity. Why the correct answer wins: Batching amortises the per-request overhead when the caller can wait.
- **B:** Correct. In this case: Batching amortises the per-request overhead when the caller can wait.
- **C:** Incorrect for this question. Autoscaling adds replicas with the traffic and removes them afterwards. Why the correct answer wins: Batching amortises the per-request overhead when the caller can wait.
- **D:** Incorrect for this question. Concurrency fills each replica before another is started, which lowers cost per request. Why the correct answer wins: Batching amortises the per-request overhead when the caller can wait.

### Question 53 — D

Answer: Use a prebuilt serving container. A prebuilt container already implements the framework handler, so no serving code is written. Local study-map skill 4.2 (Packaging and Custom Containers), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A GPU shortens inference time enough to meet a tight latency target. Why the correct answer wins: A prebuilt container already implements the framework handler, so no serving code is written.
- **B:** Incorrect for this question. The routine runs the preprocessing and postprocessing inside the serving container. Why the correct answer wins: A prebuilt container already implements the framework handler, so no serving code is written.
- **C:** Incorrect for this question. Artifact Registry holds the image with IAM and vulnerability metadata. Why the correct answer wins: A prebuilt container already implements the framework handler, so no serving code is written.
- **D:** Correct. In this case: A prebuilt container already implements the framework handler, so no serving code is written.

### Question 54 — C

Answer: Push the serving image to Artifact Registry. Artifact Registry holds the image with IAM and vulnerability metadata. Local study-map skill 4.2 (Packaging and Custom Containers), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A prebuilt container already implements the framework handler, so no serving code is written. Why the correct answer wins: Artifact Registry holds the image with IAM and vulnerability metadata.
- **B:** Incorrect for this question. Autoscaling adds replicas with the traffic and removes them afterwards. Why the correct answer wins: Artifact Registry holds the image with IAM and vulnerability metadata.
- **C:** Correct. In this case: Artifact Registry holds the image with IAM and vulnerability metadata.
- **D:** Incorrect for this question. The registry versions the model artifact and links it to its lineage and metrics. Why the correct answer wins: Artifact Registry holds the image with IAM and vulnerability metadata.

### Question 55 — C

Answer: Register the model in Agent Platform Model Registry. The registry versions the model artifact and links it to its lineage and metrics. Local study-map skill 4.3 (Model Registry and Versioning), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. ML Metadata records which data and code produced which artifact. Why the correct answer wins: The registry versions the model artifact and links it to its lineage and metrics.
- **B:** Incorrect for this question. Artifact Registry holds the image with IAM and vulnerability metadata. Why the correct answer wins: The registry versions the model artifact and links it to its lineage and metrics.
- **C:** Correct. In this case: The registry versions the model artifact and links it to its lineage and metrics.
- **D:** Incorrect for this question. Experiments records parameters, metrics, and artifacts per run so runs can be compared. Why the correct answer wins: The registry versions the model artifact and links it to its lineage and metrics.

### Question 56 — D

Answer: Deploy the version and move the alias. An alias decouples the served version name from the artifact id. Local study-map skill 4.3 (Model Registry and Versioning), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The registry versions the model artifact and links it to its lineage and metrics. Why the correct answer wins: An alias decouples the served version name from the artifact id.
- **B:** Incorrect for this question. A traffic split sends a defined share to each version on the same endpoint. Why the correct answer wins: An alias decouples the served version name from the artifact id.
- **C:** Incorrect for this question. Two identical deployments let the switch be reversed immediately. Why the correct answer wins: An alias decouples the served version name from the artifact id.
- **D:** Correct. In this case: An alias decouples the served version name from the artifact id.

### Question 57 — D, E

Answers: Roll out a canary with a small traffic share; Split traffic between two deployed versions. A canary limits the blast radius, and the traffic split holds a defined share on the endpoint. A canary limits the blast radius while the new model is compared with the old one. A traffic split sends a defined share to each version on the same endpoint. Local study-map skill 4.4 (Model Rollout Strategies), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Batch prediction reads a file or table and writes predictions without holding serving capacity. Why the correct answer wins: A canary limits the blast radius, and the traffic split holds a defined share on the endpoint.
- **B:** Incorrect for this question. An in-place replacement exposes every request to the new version at once. Why the correct answer wins: A canary limits the blast radius, and the traffic split holds a defined share on the endpoint.
- **C:** Incorrect for this question. Shadow mode scores live traffic without serving its answers, so the comparison costs nothing to users. Why the correct answer wins: A canary limits the blast radius, and the traffic split holds a defined share on the endpoint.
- **D:** Correct. A canary limits the blast radius while the new model is compared with the old one. In this case: A canary limits the blast radius, and the traffic split holds a defined share on the endpoint.
- **E:** Correct. A traffic split sends a defined share to each version on the same endpoint. In this case: A canary limits the blast radius, and the traffic split holds a defined share on the endpoint.

### Question 58 — A

Answer: Split traffic between two models in an A/B test. A/B testing compares two models on the same population with a traffic split. Local study-map skill 4.4 (Model Rollout Strategies), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: A/B testing compares two models on the same population with a traffic split.
- **B:** Incorrect for this question. Shadow mode scores live traffic without serving its answers, so the comparison costs nothing to users. Why the correct answer wins: A/B testing compares two models on the same population with a traffic split.
- **C:** Incorrect for this question. An in-place replacement exposes every request to the new version at once. Why the correct answer wins: A/B testing compares two models on the same population with a traffic split.
- **D:** Incorrect for this question. A canary limits the blast radius while the new model is compared with the old one. Why the correct answer wins: A/B testing compares two models on the same population with a traffic split.

### Question 59 — B

Answer: Share one transformation library between training and serving. Shared code removes the class of bug where the paths differ. Shared code removes the class of bug where the two paths compute a feature differently. Local study-map skill 4.5 (Inference Preprocessing and Postprocessing), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Feature Store keeps one definition that both training and serving read. Why the correct answer wins: Shared code removes the class of bug where the paths differ.
- **B:** Correct. Shared code removes the class of bug where the two paths compute a feature differently. In this case: Shared code removes the class of bug where the paths differ.
- **C:** Incorrect for this question. An alias decouples the served version name from the artifact id, so a rollback is a pointer move. Why the correct answer wins: Shared code removes the class of bug where the paths differ.
- **D:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: Shared code removes the class of bug where the paths differ.

### Question 60 — A

Answer: Keep the preprocessing inside the exported model. Preprocessing inside the artifact cannot drift between the two paths. Local study-map skill 4.5 (Inference Preprocessing and Postprocessing), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Preprocessing inside the artifact cannot drift between the two paths.
- **B:** Incorrect for this question. Feature Store keeps one definition that both training and serving read. Why the correct answer wins: Preprocessing inside the artifact cannot drift between the two paths.
- **C:** Incorrect for this question. Shared code removes the class of bug where the two paths compute a feature differently. Why the correct answer wins: Preprocessing inside the artifact cannot drift between the two paths.
- **D:** Incorrect for this question. A validation step stops a bad batch before it reaches training. Why the correct answer wins: Preprocessing inside the artifact cannot drift between the two paths.

### Question 61 — A

Answer: Use a shared public endpoint. A shared endpoint removes the deployment step but gives no control over capacity. Local study-map skill 4.6 (Endpoint Types and Access), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: A shared endpoint removes the deployment step but gives no control over capacity.
- **B:** Incorrect for this question. A GPU shortens inference time enough to meet a tight latency target. Why the correct answer wins: A shared endpoint removes the deployment step but gives no control over capacity.
- **C:** Incorrect for this question. A dedicated endpoint gives the model its own capacity instead of sharing a pool. Why the correct answer wins: A shared endpoint removes the deployment step but gives no control over capacity.
- **D:** Incorrect for this question. A private endpoint is reachable only from the VPC and shares no public surface. Why the correct answer wins: A shared endpoint removes the deployment step but gives no control over capacity.

### Question 62 — C

Answer: Use a dedicated endpoint. A dedicated endpoint gives the model its own capacity instead of sharing a pool. Local study-map skill 4.6 (Endpoint Types and Access), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A private endpoint is reachable only from the VPC and shares no public surface. Why the correct answer wins: A dedicated endpoint gives the model its own capacity instead of sharing a pool.
- **B:** Incorrect for this question. A shared endpoint removes the deployment step but gives no control over capacity or residency. Why the correct answer wins: A dedicated endpoint gives the model its own capacity instead of sharing a pool.
- **C:** Correct. In this case: A dedicated endpoint gives the model its own capacity instead of sharing a pool.
- **D:** Incorrect for this question. Autoscaling adds replicas with the traffic and removes them afterwards. Why the correct answer wins: A dedicated endpoint gives the model its own capacity instead of sharing a pool.

### Question 63 — A

Answer: Serve on L4 GPUs. An L4 GPU gives low-cost inference acceleration for a modest model. Local study-map skill 4.7 (Serving Hardware), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: An L4 GPU gives low-cost inference acceleration for a modest model.
- **B:** Incorrect for this question. A TPU slice gives a tightly coupled accelerator fabric for large synchronous training. Why the correct answer wins: An L4 GPU gives low-cost inference acceleration for a modest model.
- **C:** Incorrect for this question. CPU serving is the cheapest option for a small model with a generous latency budget. Why the correct answer wins: An L4 GPU gives low-cost inference acceleration for a modest model.
- **D:** Incorrect for this question. A100 GPUs suit mixed-precision training where the framework expects CUDA. Why the correct answer wins: An L4 GPU gives low-cost inference acceleration for a modest model.

### Question 64 — C

Answer: Serve on CPU only. CPU serving is the cheapest option for a small model with a generous latency budget. Local study-map skill 4.7 (Serving Hardware), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. An Edge TPU runs a quantised model on-device where the network cannot be relied on. Why the correct answer wins: CPU serving is the cheapest option for a small model with a generous latency budget.
- **B:** Incorrect for this question. A GPU shortens inference time enough to meet a tight latency target. Why the correct answer wins: CPU serving is the cheapest option for a small model with a generous latency budget.
- **C:** Correct. In this case: CPU serving is the cheapest option for a small model with a generous latency budget.
- **D:** Incorrect for this question. An L4 GPU gives low-cost inference acceleration for a modest model. Why the correct answer wins: CPU serving is the cheapest option for a small model with a generous latency budget.

### Question 65 — B, C

Answers: Set a minimum replica count; Raise the maximum replica count. A minimum replica keeps capacity warm, and the ceiling caps how far it scales. A minimum replica keeps capacity warm so the first request after a quiet period is fast. The ceiling caps how far the endpoint scales, and therefore the throughput it can absorb. Local study-map skill 4.8 (Serving Throughput and Scaling), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Batching amortises the per-request overhead when the caller can wait. Why the correct answer wins: A minimum replica keeps capacity warm, and the ceiling caps how far it scales.
- **B:** Correct. The ceiling caps how far the endpoint scales, and therefore the throughput it can absorb. In this case: A minimum replica keeps capacity warm, and the ceiling caps how far it scales.
- **C:** Correct. A minimum replica keeps capacity warm so the first request after a quiet period is fast. In this case: A minimum replica keeps capacity warm, and the ceiling caps how far it scales.
- **D:** Incorrect for this question. Concurrency fills each replica before another is started, which lowers cost per request. Why the correct answer wins: A minimum replica keeps capacity warm, and the ceiling caps how far it scales.
- **E:** Incorrect for this question. A GPU shortens inference time enough to meet a tight latency target. Why the correct answer wins: A minimum replica keeps capacity warm, and the ceiling caps how far it scales.

### Question 66 — D

Answer: Raise the concurrency per replica. Concurrency fills each replica before another is started. Local study-map skill 4.8 (Serving Throughput and Scaling), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A GPU shortens inference time enough to meet a tight latency target. Why the correct answer wins: Concurrency fills each replica before another is started.
- **B:** Incorrect for this question. The ceiling caps how far the endpoint scales, and therefore the throughput it can absorb. Why the correct answer wins: Concurrency fills each replica before another is started.
- **C:** Incorrect for this question. Batching amortises the per-request overhead when the caller can wait. Why the correct answer wins: Concurrency fills each replica before another is started.
- **D:** Correct. In this case: Concurrency fills each replica before another is started.

### Question 67 — A

Answer: Enable autoscaling on the endpoint. Autoscaling adds replicas with the traffic and removes them afterwards. Local study-map skill 4.8 (Serving Throughput and Scaling), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Autoscaling adds replicas with the traffic and removes them afterwards.
- **B:** Incorrect for this question. The ceiling caps how far the endpoint scales, and therefore the throughput it can absorb. Why the correct answer wins: Autoscaling adds replicas with the traffic and removes them afterwards.
- **C:** Incorrect for this question. Batching amortises the per-request overhead when the caller can wait. Why the correct answer wins: Autoscaling adds replicas with the traffic and removes them afterwards.
- **D:** Incorrect for this question. A minimum replica keeps capacity warm so the first request after a quiet period is fast. Why the correct answer wins: Autoscaling adds replicas with the traffic and removes them afterwards.

### Question 68 — A, C

Answers: Configure explanation metadata for the endpoint; Register the model in Agent Platform Model Registry. Explanation metadata tells the endpoint which inputs to attribute over, and the registry holds the version that is deployed. The registry versions the model artifact and links it to its lineage and metrics. Local study-map skill 4.9 (Production Tuning), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Explanation metadata tells the endpoint which inputs to attribute over, and the registry holds the version that is deployed.
- **B:** Incorrect for this question. An alias decouples the served version name from the artifact id, so a rollback is a pointer move. Why the correct answer wins: Explanation metadata tells the endpoint which inputs to attribute over, and the registry holds the version that is deployed.
- **C:** Correct. The registry versions the model artifact and links it to its lineage and metrics. In this case: Explanation metadata tells the endpoint which inputs to attribute over, and the registry holds the version that is deployed.
- **D:** Incorrect for this question. Batching amortises the per-request overhead when the caller can wait. Why the correct answer wins: Explanation metadata tells the endpoint which inputs to attribute over, and the registry holds the version that is deployed.
- **E:** Incorrect for this question. A minimum replica keeps capacity warm so the first request after a quiet period is fast. Why the correct answer wins: Explanation metadata tells the endpoint which inputs to attribute over, and the registry holds the version that is deployed.

### Question 69 — D

Answer: Attach a GPU to the serving replica. A GPU shortens inference time enough to meet a tight latency target. Local study-map skill 4.9 (Production Tuning), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Concurrency fills each replica before another is started, which lowers cost per request. Why the correct answer wins: A GPU shortens inference time enough to meet a tight latency target.
- **B:** Incorrect for this question. The ceiling caps how far the endpoint scales, and therefore the throughput it can absorb. Why the correct answer wins: A GPU shortens inference time enough to meet a tight latency target.
- **C:** Incorrect for this question. Batching amortises the per-request overhead when the caller can wait. Why the correct answer wins: A GPU shortens inference time enough to meet a tight latency target.
- **D:** Correct. In this case: A GPU shortens inference time enough to meet a tight latency target.

### Question 70 — C

Answer: Gate the deployment on a model evaluation threshold. The gate promotes a model only when it beats the incumbent on the agreed metric. Local study-map skill 5.1 (Data and Model Validation), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A validation step stops a bad batch before it reaches training. Why the correct answer wins: The gate promotes a model only when it beats the incumbent on the agreed metric.
- **B:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: The gate promotes a model only when it beats the incumbent on the agreed metric.
- **C:** Correct. In this case: The gate promotes a model only when it beats the incumbent on the agreed metric.
- **D:** Incorrect for this question. Drift-triggered retraining responds to change instead of to the calendar. Why the correct answer wins: The gate promotes a model only when it beats the incumbent on the agreed metric.

### Question 71 — D

Answer: Add an explicit data validation step. A validation step stops a bad batch before it reaches training. Local study-map skill 5.1 (Data and Model Validation), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: A validation step stops a bad batch before it reaches training.
- **B:** Incorrect for this question. The gate promotes a model only when it beats the incumbent on the agreed metric. Why the correct answer wins: A validation step stops a bad batch before it reaches training.
- **C:** Incorrect for this question. Rejecting rows into a side table makes a schema break visible instead of silent. Why the correct answer wins: A validation step stops a bad batch before it reaches training.
- **D:** Correct. In this case: A validation step stops a bad batch before it reaches training.

### Question 72 — B, E

Answers: Report precision-recall AUC for the rare class; Choose the threshold from the cost of each error type. Precision-recall AUC stays informative when positives are rare, and the threshold follows the cost of errors. Precision-recall AUC stays informative when the positive class is rare. The decision threshold follows the relative cost of a false positive and a false negative. Local study-map skill 5.1 (Data and Model Validation), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: Precision-recall AUC stays informative when positives are rare, and the threshold follows the cost of errors.
- **B:** Correct. The decision threshold follows the relative cost of a false positive and a false negative. In this case: Precision-recall AUC stays informative when positives are rare, and the threshold follows the cost of errors.
- **C:** Incorrect for this question. ROC AUC measures ranking quality across thresholds and hides class imbalance. Why the correct answer wins: Precision-recall AUC stays informative when positives are rare, and the threshold follows the cost of errors.
- **D:** Incorrect for this question. MAPE expresses the error relative to the actual value, which business readers understand. Why the correct answer wins: Precision-recall AUC stays informative when positives are rare, and the threshold follows the cost of errors.
- **E:** Correct. Precision-recall AUC stays informative when the positive class is rare. In this case: Precision-recall AUC stays informative when positives are rare, and the threshold follows the cost of errors.

### Question 73 — D

Answer: Orchestrate with Managed Service for Apache Airflow. Airflow expresses cross-system dependencies and schedules outside the ML platform. Local study-map skill 5.2 (Pipeline Orchestration Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Ray fits a Python-native distributed workload that is not a container-per-step pipeline. Why the correct answer wins: Airflow expresses cross-system dependencies and schedules outside the ML platform.
- **B:** Incorrect for this question. Kubeflow pipelines give a container-per-step pipeline that runs on the managed service or on GKE. Why the correct answer wins: Airflow expresses cross-system dependencies and schedules outside the ML platform.
- **C:** Incorrect for this question. Pipelines runs each step as a container with caching, lineage, and retry. Why the correct answer wins: Airflow expresses cross-system dependencies and schedules outside the ML platform.
- **D:** Correct. In this case: Airflow expresses cross-system dependencies and schedules outside the ML platform.

### Question 74 — B

Answer: Orchestrate the steps in Agent Platform Pipelines. Pipelines runs each step as a container with caching, lineage, and retry. Local study-map skill 5.2 (Pipeline Orchestration Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Airflow expresses cross-system dependencies and schedules outside the ML platform. Why the correct answer wins: Pipelines runs each step as a container with caching, lineage, and retry.
- **B:** Correct. In this case: Pipelines runs each step as a container with caching, lineage, and retry.
- **C:** Incorrect for this question. Kubeflow pipelines give a container-per-step pipeline that runs on the managed service or on GKE. Why the correct answer wins: Pipelines runs each step as a container with caching, lineage, and retry.
- **D:** Incorrect for this question. Ray fits a Python-native distributed workload that is not a container-per-step pipeline. Why the correct answer wins: Pipelines runs each step as a container with caching, lineage, and retry.

### Question 75 — C

Answer: Use Ray on Agent Platform for the distributed compute. Ray fits a Python-native distributed workload that is not a container-per-step pipeline. Local study-map skill 5.2 (Pipeline Orchestration Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Kubeflow pipelines give a container-per-step pipeline that runs on the managed service or on GKE. Why the correct answer wins: Ray fits a Python-native distributed workload that is not a container-per-step pipeline.
- **B:** Incorrect for this question. Airflow expresses cross-system dependencies and schedules outside the ML platform. Why the correct answer wins: Ray fits a Python-native distributed workload that is not a container-per-step pipeline.
- **C:** Correct. In this case: Ray fits a Python-native distributed workload that is not a container-per-step pipeline.
- **D:** Incorrect for this question. Pipelines runs each step as a container with caching, lineage, and retry. Why the correct answer wins: Ray fits a Python-native distributed workload that is not a container-per-step pipeline.

### Question 76 — C

Answer: Trigger the build and deploy from Cloud Build. Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance. Local study-map skill 5.2 (Pipeline Orchestration Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance.
- **B:** Incorrect for this question. Pipelines runs each step as a container with caching, lineage, and retry. Why the correct answer wins: Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance.
- **C:** Correct. In this case: Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance.
- **D:** Incorrect for this question. The scheduler starts the pipeline on the cadence the retraining policy defines. Why the correct answer wins: Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance.

### Question 77 — A

Answer: Share one transformation library between training and serving. Shared code removes the class of bug where the two paths compute a feature differently. Local study-map skill 5.3 (Train and Serve Consistency), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Shared code removes the class of bug where the two paths compute a feature differently.
- **B:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: Shared code removes the class of bug where the two paths compute a feature differently.
- **C:** Incorrect for this question. Preprocessing inside the artifact cannot drift between the two paths. Why the correct answer wins: Shared code removes the class of bug where the two paths compute a feature differently.
- **D:** Incorrect for this question. Feature Store keeps one definition that both training and serving read. Why the correct answer wins: Shared code removes the class of bug where the two paths compute a feature differently.

### Question 78 — A, E

Answers: Register the feature in Agent Platform Feature Store; Read the historical features from the offline store. Feature Store keeps one definition, and the offline store returns point-in-time values. Feature Store keeps one definition that both training and serving read. The offline store returns point-in-time values for training. Local study-map skill 5.3 (Train and Serve Consistency), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. The offline store returns point-in-time values for training. In this case: Feature Store keeps one definition, and the offline store returns point-in-time values.
- **B:** Incorrect for this question. Deduplicating at ingest stops duplicated records inflating the training set. Why the correct answer wins: Feature Store keeps one definition, and the offline store returns point-in-time values.
- **C:** Incorrect for this question. The registry versions the model artifact and links it to its lineage and metrics. Why the correct answer wins: Feature Store keeps one definition, and the offline store returns point-in-time values.
- **D:** Incorrect for this question. In-memory processing is the simplest option and stops working once the data exceeds the worker memory. Why the correct answer wins: Feature Store keeps one definition, and the offline store returns point-in-time values.
- **E:** Correct. Feature Store keeps one definition that both training and serving read. In this case: Feature Store keeps one definition, and the offline store returns point-in-time values.

### Question 79 — C

Answer: Add an explicit data validation step. A validation step stops a bad batch before it reaches training. Local study-map skill 5.3 (Train and Serve Consistency), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: A validation step stops a bad batch before it reaches training.
- **B:** Incorrect for this question. The gate promotes a model only when it beats the incumbent on the agreed metric. Why the correct answer wins: A validation step stops a bad batch before it reaches training.
- **C:** Correct. In this case: A validation step stops a bad batch before it reaches training.
- **D:** Incorrect for this question. Shared code removes the class of bug where the two paths compute a feature differently. Why the correct answer wins: A validation step stops a bad batch before it reaches training.

### Question 80 — A

Answer: Serve the feature from the online store. The online store returns the latest feature value at low latency for a single entity. Local study-map skill 5.3 (Train and Serve Consistency), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: The online store returns the latest feature value at low latency for a single entity.
- **B:** Incorrect for this question. The offline store returns point-in-time values for training. Why the correct answer wins: The online store returns the latest feature value at low latency for a single entity.
- **C:** Incorrect for this question. A crossed feature lets a linear model express the interaction it cannot learn alone. Why the correct answer wins: The online store returns the latest feature value at low latency for a single entity.
- **D:** Incorrect for this question. Feature monitoring reports distribution changes per feature, not just per model. Why the correct answer wins: The online store returns the latest feature value at low latency for a single entity.

### Question 81 — D

Answer: Retrain on a fixed schedule. A fixed schedule is simple to reason about when the data changes predictably. Local study-map skill 5.4 (Retraining Policy), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Manual retraining leaves the model stale whenever the trigger is forgotten. Why the correct answer wins: A fixed schedule is simple to reason about when the data changes predictably.
- **B:** Incorrect for this question. Drift-triggered retraining responds to change instead of to the calendar. Why the correct answer wins: A fixed schedule is simple to reason about when the data changes predictably.
- **C:** Incorrect for this question. Metric-triggered retraining reacts to actual quality loss. Why the correct answer wins: A fixed schedule is simple to reason about when the data changes predictably.
- **D:** Correct. In this case: A fixed schedule is simple to reason about when the data changes predictably.

### Question 82 — B

Answer: Retrain when the production metric drops. Metric-triggered retraining reacts to actual quality loss. Local study-map skill 5.4 (Retraining Policy), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Drift-triggered retraining responds to change instead of to the calendar. Why the correct answer wins: Metric-triggered retraining reacts to actual quality loss.
- **B:** Correct. In this case: Metric-triggered retraining reacts to actual quality loss.
- **C:** Incorrect for this question. A fixed schedule is simple to reason about when the data changes predictably. Why the correct answer wins: Metric-triggered retraining reacts to actual quality loss.
- **D:** Incorrect for this question. Manual retraining leaves the model stale whenever the trigger is forgotten. Why the correct answer wins: Metric-triggered retraining reacts to actual quality loss.

### Question 83 — B

Answer: Extend CI/CD into continuous training. Continuous training adds the retrain and validate step to the same automated pipeline. Local study-map skill 5.4 (Retraining Policy), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A fixed schedule is simple to reason about when the data changes predictably. Why the correct answer wins: Continuous training adds the retrain and validate step to the same automated pipeline.
- **B:** Correct. In this case: Continuous training adds the retrain and validate step to the same automated pipeline.
- **C:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: Continuous training adds the retrain and validate step to the same automated pipeline.
- **D:** Incorrect for this question. An event trigger retrains when data lands instead of on a fixed clock. Why the correct answer wins: Continuous training adds the retrain and validate step to the same automated pipeline.

### Question 84 — A

Answer: Enable step caching. Caching skips an unchanged step on a rerun and shortens the pipeline. Local study-map skill 5.5 (CI/CD/CT with Cloud Build), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Caching skips an unchanged step on a rerun and shortens the pipeline.
- **B:** Incorrect for this question. Drift-triggered retraining responds to change instead of to the calendar. Why the correct answer wins: Caching skips an unchanged step on a rerun and shortens the pipeline.
- **C:** Incorrect for this question. A validation step stops a bad batch before it reaches training. Why the correct answer wins: Caching skips an unchanged step on a rerun and shortens the pipeline.
- **D:** Incorrect for this question. The gate promotes a model only when it beats the incumbent on the agreed metric. Why the correct answer wins: Caching skips an unchanged step on a rerun and shortens the pipeline.

### Question 85 — D

Answer: Add a Cloud Scheduler trigger to the pipeline. The scheduler starts the pipeline on the cadence the retraining policy defines. Local study-map skill 5.5 (CI/CD/CT with Cloud Build), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. An event trigger retrains when data lands instead of on a fixed clock. Why the correct answer wins: The scheduler starts the pipeline on the cadence the retraining policy defines.
- **B:** Incorrect for this question. Metric-triggered retraining reacts to actual quality loss. Why the correct answer wins: The scheduler starts the pipeline on the cadence the retraining policy defines.
- **C:** Incorrect for this question. Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance. Why the correct answer wins: The scheduler starts the pipeline on the cadence the retraining policy defines.
- **D:** Correct. In this case: The scheduler starts the pipeline on the cadence the retraining policy defines.

### Question 86 — C

Answer: Trigger the pipeline from the arrival of new data. An event trigger retrains when data lands instead of on a fixed clock. Local study-map skill 5.5 (CI/CD/CT with Cloud Build), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Manual retraining leaves the model stale whenever the trigger is forgotten. Why the correct answer wins: An event trigger retrains when data lands instead of on a fixed clock.
- **B:** Incorrect for this question. Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance. Why the correct answer wins: An event trigger retrains when data lands instead of on a fixed clock.
- **C:** Correct. In this case: An event trigger retrains when data lands instead of on a fixed clock.
- **D:** Incorrect for this question. The scheduler starts the pipeline on the cadence the retraining policy defines. Why the correct answer wins: An event trigger retrains when data lands instead of on a fixed clock.

### Question 87 — B

Answer: Add a Cloud Scheduler trigger to the pipeline. The scheduler starts the pipeline on the cadence the retraining policy defines. Local study-map skill 5.2 (Pipeline Orchestration Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Kubeflow pipelines give a container-per-step pipeline that runs on the managed service or on GKE. Why the correct answer wins: The scheduler starts the pipeline on the cadence the retraining policy defines.
- **B:** Correct. In this case: The scheduler starts the pipeline on the cadence the retraining policy defines.
- **C:** Incorrect for this question. An event trigger retrains when data lands instead of on a fixed clock. Why the correct answer wins: The scheduler starts the pipeline on the cadence the retraining policy defines.
- **D:** Incorrect for this question. Ray fits a Python-native distributed workload that is not a container-per-step pipeline. Why the correct answer wins: The scheduler starts the pipeline on the cadence the retraining policy defines.

### Question 88 — D, E

Answers: Put the boundary in the system instruction; Constrain the response to a JSON schema. The system instruction states what to refuse, and a schema stops free text reaching the code. A system instruction states what the assistant must refuse, though it is not a security control on its own. A schema stops the model returning free text that downstream code cannot parse. Local study-map skill 6.1 (Secure AI and Prompt Protection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Safety filters block categories of harmful output at the model call. Why the correct answer wins: The system instruction states what to refuse, and a schema stops free text reaching the code.
- **B:** Incorrect for this question. A regex removes a known identifier pattern before the prompt leaves the service. Why the correct answer wins: The system instruction states what to refuse, and a schema stops free text reaching the code.
- **C:** Incorrect for this question. Model Armor detects prompt injection, jailbreak attempts, and unsafe content. Why the correct answer wins: The system instruction states what to refuse, and a schema stops free text reaching the code.
- **D:** Correct. A schema stops the model returning free text that downstream code cannot parse. In this case: The system instruction states what to refuse, and a schema stops free text reaching the code.
- **E:** Correct. A system instruction states what the assistant must refuse, though it is not a security control on its own. In this case: The system instruction states what to refuse, and a schema stops free text reaching the code.

### Question 89 — C

Answer: Configure the model safety filters. Safety filters block categories of harmful output at the model call. Local study-map skill 6.1 (Secure AI and Prompt Protection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A regex removes a known identifier pattern before the prompt leaves the service. Why the correct answer wins: Safety filters block categories of harmful output at the model call.
- **B:** Incorrect for this question. A schema stops the model returning free text that downstream code cannot parse. Why the correct answer wins: Safety filters block categories of harmful output at the model call.
- **C:** Correct. In this case: Safety filters block categories of harmful output at the model call.
- **D:** Incorrect for this question. Model Armor detects prompt injection, jailbreak attempts, and unsafe content. Why the correct answer wins: Safety filters block categories of harmful output at the model call.

### Question 90 — B

Answer: Redact the pattern-matchable fields with a regex. A regex removes a known identifier pattern before the prompt leaves the service. Local study-map skill 6.1 (Secure AI and Prompt Protection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A system instruction states what the assistant must refuse, though it is not a security control on its own. Why the correct answer wins: A regex removes a known identifier pattern before the prompt leaves the service.
- **B:** Correct. In this case: A regex removes a known identifier pattern before the prompt leaves the service.
- **C:** Incorrect for this question. Safety filters block categories of harmful output at the model call. Why the correct answer wins: A regex removes a known identifier pattern before the prompt leaves the service.
- **D:** Incorrect for this question. A schema stops the model returning free text that downstream code cannot parse. Why the correct answer wins: A regex removes a known identifier pattern before the prompt leaves the service.

### Question 91 — B

Answer: Slice the evaluation metrics by the sensitive attribute. A sliced metric shows a gap that the aggregate metric hides. Local study-map skill 6.2 (Responsible AI and Bias), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A per-group outcome rate is the first evidence of disparate impact. Why the correct answer wins: A sliced metric shows a gap that the aggregate metric hides.
- **B:** Correct. In this case: A sliced metric shows a gap that the aggregate metric hides.
- **C:** Incorrect for this question. The card states where the model may be used and where it must not. Why the correct answer wins: A sliced metric shows a gap that the aggregate metric hides.
- **D:** Incorrect for this question. The card records provenance, intended use, and known gaps for the dataset. Why the correct answer wins: A sliced metric shows a gap that the aggregate metric hides.

### Question 92 — C

Answer: Document the dataset with a data card. The card records provenance, intended use, and known gaps for the dataset. Local study-map skill 6.2 (Responsible AI and Bias), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A sliced metric shows a gap that the aggregate metric hides. Why the correct answer wins: The card records provenance, intended use, and known gaps for the dataset.
- **B:** Incorrect for this question. A per-group outcome rate is the first evidence of disparate impact. Why the correct answer wins: The card records provenance, intended use, and known gaps for the dataset.
- **C:** Correct. In this case: The card records provenance, intended use, and known gaps for the dataset.
- **D:** Incorrect for this question. The card states where the model may be used and where it must not. Why the correct answer wins: The card records provenance, intended use, and known gaps for the dataset.

### Question 93 — D

Answer: Use sampled Shapley on the endpoint. Sampled Shapley explains individual online predictions with a bounded compute cost. Local study-map skill 6.3 (Explainability), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Shapley values attribute a prediction to its features with a consistent baseline. Why the correct answer wins: Sampled Shapley explains individual online predictions with a bounded compute cost.
- **B:** Incorrect for this question. ML.GLOBAL_EXPLAIN ranks the features that matter most across the whole model. Why the correct answer wins: Sampled Shapley explains individual online predictions with a bounded compute cost.
- **C:** Incorrect for this question. Integrated gradients attributes an image prediction to the pixels that moved it. Why the correct answer wins: Sampled Shapley explains individual online predictions with a bounded compute cost.
- **D:** Correct. In this case: Sampled Shapley explains individual online predictions with a bounded compute cost.

### Question 94 — B

Answer: Publish a model card with the intended use and limits. The card states where the model may be used and where it must not. Local study-map skill 6.3 (Explainability), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A linear or tree model can be read directly when regulation demands an explanation by construction. Why the correct answer wins: The card states where the model may be used and where it must not.
- **B:** Correct. In this case: The card states where the model may be used and where it must not.
- **C:** Incorrect for this question. Attribution shows which inputs drove the decision in the case the reviewer is examining. Why the correct answer wins: The card states where the model may be used and where it must not.
- **D:** Incorrect for this question. The card records provenance, intended use, and known gaps for the dataset. Why the correct answer wins: The card states where the model may be used and where it must not.

### Question 95 — B

Answer: Route the monitoring alert to the owning team. An alert with no owner is a dashboard nobody reads. Local study-map skill 6.4 (Model Monitoring Configuration), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The threshold expresses how much drift the business can absorb before someone acts. Why the correct answer wins: An alert with no owner is a dashboard nobody reads.
- **B:** Correct. In this case: An alert with no owner is a dashboard nobody reads.
- **C:** Incorrect for this question. A percentile latency per version shows a regression that an average hides. Why the correct answer wins: An alert with no owner is a dashboard nobody reads.
- **D:** Incorrect for this question. Redacted logs make a bad answer diagnosable without storing sensitive text. Why the correct answer wins: An alert with no owner is a dashboard nobody reads.

### Question 96 — C

Answer: Track p95 latency per model version. A percentile latency per version shows a regression that an average hides. Local study-map skill 6.4 (Model Monitoring Configuration), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Model Monitoring compares live traffic with the training baseline and reports skew and drift. Why the correct answer wins: A percentile latency per version shows a regression that an average hides.
- **B:** Incorrect for this question. Token accounting attributes generative cost to the feature that caused it. Why the correct answer wins: A percentile latency per version shows a regression that an average hides.
- **C:** Correct. In this case: A percentile latency per version shows a regression that an average hides.
- **D:** Incorrect for this question. An alert with no owner is a dashboard nobody reads. Why the correct answer wins: A percentile latency per version shows a regression that an average hides.

### Question 97 — A, E

Answers: Watch for data drift; Watch the prediction distribution. Data drift is a change in the input distribution, and a shift in the output distribution is an early symptom. Data drift is a change in the input distribution after the model shipped. A shift in the output distribution is often the first visible symptom. Local study-map skill 6.5 (Skew and Drift Types), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. Data drift is a change in the input distribution after the model shipped. In this case: Data drift is a change in the input distribution, and a shift in the output distribution is an early symptom.
- **B:** Incorrect for this question. Attribution drift is a change in which features drive the prediction. Why the correct answer wins: Data drift is a change in the input distribution, and a shift in the output distribution is an early symptom.
- **C:** Incorrect for this question. Concept drift is a change in the relationship between the features and the target. Why the correct answer wins: Data drift is a change in the input distribution, and a shift in the output distribution is an early symptom.
- **D:** Incorrect for this question. Without the labelled outcome, quality can only be inferred from the inputs and outputs. Why the correct answer wins: Data drift is a change in the input distribution, and a shift in the output distribution is an early symptom.
- **E:** Correct. A shift in the output distribution is often the first visible symptom. In this case: Data drift is a change in the input distribution, and a shift in the output distribution is an early symptom.

### Question 98 — D

Answer: Watch for feature attribution drift. Attribution drift is a change in which features drive the prediction. Local study-map skill 6.5 (Skew and Drift Types), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Data drift is a change in the input distribution after the model shipped. Why the correct answer wins: Attribution drift is a change in which features drive the prediction.
- **B:** Incorrect for this question. Without the labelled outcome, quality can only be inferred from the inputs and outputs. Why the correct answer wins: Attribution drift is a change in which features drive the prediction.
- **C:** Incorrect for this question. Concept drift is a change in the relationship between the features and the target. Why the correct answer wins: Attribution drift is a change in which features drive the prediction.
- **D:** Correct. In this case: Attribution drift is a change in which features drive the prediction.

### Question 99 — D

Answer: Track tokens and cost per request. Token accounting attributes generative cost to the feature that caused it. Local study-map skill 6.6 (Generative AI Monitoring), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A percentile latency per version shows a regression that an average hides. Why the correct answer wins: Token accounting attributes generative cost to the feature that caused it.
- **B:** Incorrect for this question. Model Monitoring compares live traffic with the training baseline and reports skew and drift. Why the correct answer wins: Token accounting attributes generative cost to the feature that caused it.
- **C:** Incorrect for this question. Continuous sampling catches quality regressions that drift metrics cannot see. Why the correct answer wins: Token accounting attributes generative cost to the feature that caused it.
- **D:** Correct. In this case: Token accounting attributes generative cost to the feature that caused it.

### Question 100 — A

Answer: Score a sample of live answers with the evaluation rubric. Continuous sampling catches quality regressions that drift metrics cannot see. Local study-map skill 6.6 (Generative AI Monitoring), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Continuous sampling catches quality regressions that drift metrics cannot see.
- **B:** Incorrect for this question. Token accounting attributes generative cost to the feature that caused it. Why the correct answer wins: Continuous sampling catches quality regressions that drift metrics cannot see.
- **C:** Incorrect for this question. Model Monitoring compares live traffic with the training baseline and reports skew and drift. Why the correct answer wins: Continuous sampling catches quality regressions that drift metrics cannot see.
- **D:** Incorrect for this question. A percentile latency per version shows a regression that an average hides. Why the correct answer wins: Continuous sampling catches quality regressions that drift metrics cannot see.
