# Google Cloud Professional Machine Learning Engineer — Full-Length Mock Exam 4

Professional Machine Learning Engineer · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study or drag-and-drop item is reproduced. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Architecting low-code AI solutions (Low-Code AI and Foundational Models)

### 1. A churn model on a wide table must capture non-linear interactions in SQL. What should be built?

- A. Create a BigQuery ML boosted tree classifier
- B. Create a BigQuery ML linear regression model
- C. Create a BigQuery ML ARIMA_PLUS time series model
- D. Create a BigQuery ML k-means model

### 2. A subscription model must return a probability, and scaling must apply at scoring time. Which two choices apply? Select two.

- A. Declare the feature transformations in the TRANSFORM clause
- B. Import the TensorFlow model into BigQuery ML
- C. Create a BigQuery ML k-means model
- D. Store the predictions in a nested JSON column
- E. Create a BigQuery ML logistic regression model

### 3. A model's precision must be confirmed before it is exposed to the business. What should be used?

- A. Score the rows with ML.PREDICT
- B. Declare the feature transformations in the TRANSFORM clause
- C. Summarise the model with ML.GLOBAL_EXPLAIN
- D. Inspect the metrics with ML.EVALUATE

### 4. A declined customer asks why their score was low, one row at a time. What should be used?

- A. Summarise the model with ML.GLOBAL_EXPLAIN
- B. Score the rows with ML.PREDICT
- C. Store the predictions in a nested JSON column
- D. Read the contribution of each feature with ML.EXPLAIN_PREDICT

### 5. A quality team has 4,000 labelled photos of defects and wants a managed model. What should be used?

- A. Train an Agent Platform AutoML tabular model
- B. Train an Agent Platform AutoML image model
- C. Train an Agent Platform AutoML forecasting model
- D. Train an Agent Platform AutoML text model

### 6. A support team has labelled ticket categories and wants a managed classifier. What should be used?

- A. Train an Agent Platform AutoML tabular model
- B. Train an Agent Platform AutoML forecasting model
- C. Train an Agent Platform AutoML image model
- D. Train an Agent Platform AutoML text model

### 7. Product descriptions must follow a house voice, and the examples are already in BigQuery. What should be done?

- A. Fine-tune the full model
- B. Create a BigQuery ML remote model over Gemini
- C. Start with prompt and context engineering
- D. Fine-tune a Gemini model from BigQuery

### 8. A retrieval step needs a vector for every knowledge-base article. What should be used?

- A. Generate the images with Imagen
- B. Choose the larger Gemini model for quality
- C. Generate the video with Veo
- D. Embed the documents with the text embedding model

### 9. A four-language knowledge base must be unified before indexing. What should be used?

- A. Use the Translation API
- B. Use the Speech-to-Text API
- C. Use the Natural Language API
- D. Use Document AI with a specialised processor

### 10. Customer reviews must be split into entities and sentiment without a custom model. What should be used?

- A. Use Document AI with a specialised processor
- B. Use the Vision API
- C. Use the Natural Language API
- D. Use the Translation API

### 11. A high-volume assistant resends a 20-page policy and only needs short answers. Which two changes cut cost most? Select two.

- A. Choose the smaller Gemini model for latency and cost
- B. Call the model in the region that serves the users
- C. Request a quota increase for the model
- D. Cache the long shared context
- E. Send the offline work through the batch API

### 12. Ten thousand product descriptions must be generated overnight at the lowest price. What should be used?

- A. Send the offline work through the batch API
- B. Request a quota increase for the model
- C. Cache the long shared context
- D. Stream the response tokens to the client

---

## Domain 2 — Collaborating within and across teams to manage data and models (Data, Features, Notebooks, and Experiments)

### 13. A 300 MB sample must be explored interactively before the design is fixed. What should be used?

- A. Preprocess with a Dataflow pipeline
- B. Preprocess in BigQuery with SQL
- C. Preprocess in memory with pandas
- D. Preprocess with Spark on Dataproc

### 14. A customer dataset holds free-text notes, and one customer must not span splits. Which two steps apply? Select two.

- A. Split the data by time rather than at random
- B. Add a crossed feature for the interacting pair
- C. Split by entity so one customer never spans train and test
- D. De-identify the fields with Sensitive Data Protection
- E. Drop the identifier columns before the training dataset is written

### 15. A 12 TB transformation must run without provisioning or sizing a cluster. What should be used?

- A. Preprocess with a Dataflow pipeline
- B. Preprocess in memory with pandas
- C. Preprocess in BigQuery with SQL
- D. Preprocess with Spark on Dataproc

### 16. The endpoint must fetch one entity's latest feature in milliseconds. What should be used?

- A. Serve the feature from the online store
- B. Read the historical features from the offline store
- C. Add a crossed feature for the interacting pair
- D. Enable feature monitoring on the feature group

### 17. One feature has values in the millions and the model keeps diverging. What should be applied?

- A. Normalise the numeric feature before training
- B. Add a crossed feature for the interacting pair
- C. Register the feature in Agent Platform Feature Store
- D. Bucketize the continuous feature

### 18. The model must join on an account key that must not be reversible in the extract. What should be done?

- A. Hash the identifiers with a salted key before training
- B. Drop the identifier columns before the training dataset is written
- C. De-identify the fields with Sensitive Data Protection
- D. Restrict the raw bucket to a privileged service account

### 19. Only one service account may read the raw customer export. What should be applied?

- A. Restrict the raw bucket to a privileged service account
- B. Drop the identifier columns before the training dataset is written
- C. Hash the identifiers with a salted key before training
- D. De-identify the fields with Sensitive Data Protection

### 20. A team of forty data scientists leaves runtimes idle all night. What should be set?

- A. Use Colab Enterprise
- B. Use an Agent Platform Workbench instance
- C. Create the runtime with no public IP
- D. Set an idle shutdown schedule

### 21. Two teams must reproduce each other's notebook results exactly. What should be configured?

- A. Set an idle shutdown schedule
- B. Use Colab Enterprise
- C. Attach the runtime to the shared VPC subnet
- D. Pin the runtime to a custom container image

### 22. A model lead must compare the validation loss of every run this week. What should be used?

- A. Enable step caching
- B. Track artifacts and lineage in ML Metadata
- C. Set the random seed in the training code
- D. Log the run to Agent Platform Experiments

### 23. A feature step is unchanged yet costs an hour on every run. What should be enabled?

- A. Log the run to Agent Platform Experiments
- B. Track artifacts and lineage in ML Metadata
- C. Enable step caching
- D. Compare the runs on the validation metric

### 24. A workflow must wait on an external file drop and then run an audited build. Which two choices fit? Select two.

- A. Trigger the build and deploy from Cloud Build
- B. Express the workflow as a Kubeflow pipeline
- C. Orchestrate with Managed Service for Apache Airflow
- D. Use Ray on Agent Platform for the distributed compute
- E. Log the run to Agent Platform Experiments

### 25. A container-per-step workflow must run on the team's own GKE cluster. What should be used?

- A. Orchestrate with Managed Service for Apache Airflow
- B. Orchestrate the steps in Agent Platform Pipelines
- C. Express the workflow as a Kubeflow pipeline
- D. Use Ray on Agent Platform for the distributed compute

### 26. A model must be operated at a specific false-negative rate for a safety rule. Which two practices apply? Select two.

- A. Choose the threshold from the cost of each error type
- B. Inspect the confusion matrix at the operating threshold
- C. Report RMSE for the regression target
- D. Report ROC AUC
- E. Report MAPE when the error must be read as a percentage

### 27. A delivery-time model must report its typical error in minutes. What should be used?

- A. Report precision-recall AUC for the rare class
- B. Report MAPE when the error must be read as a percentage
- C. Report RMSE for the regression target
- D. Report ROC AUC

### 28. A reviewer asks which dataset version fed the model in production. What should be recorded?

- A. Enable step caching
- B. Log the run to Agent Platform Experiments
- C. Track artifacts and lineage in ML Metadata
- D. Register the model in Agent Platform Model Registry

---

## Domain 3 — Scaling prototypes into ML models (Training at Scale and Model Choice)

### 29. A translation-quality task must be judged without a labelled corpus. What model type fits?

- A. Choose a classical time series model
- B. Choose a deep neural network
- C. Use TabNet as the custom training algorithm
- D. Choose a foundation model

### 30. A recommender has 900 dense features and millions of rows. What model type fits?

- A. Use TabNet as the custom training algorithm
- B. Choose a classical time series model
- C. Choose a foundation model
- D. Choose a deep neural network

### 31. A supply team wants a managed forecast with covariates and backtesting. What should be used?

- A. Train an Agent Platform AutoML forecasting model
- B. Train an Agent Platform AutoML text model
- C. Train an Agent Platform AutoML image model
- D. Train an Agent Platform AutoML tabular model

### 32. The scores must be joined to the warehouse table hourly without a serving stack. What should be used?

- A. Build the model in BigQuery ML
- B. Train a custom model on Agent Platform
- C. Train with Agent Platform AutoML
- D. Use TabNet as the custom training algorithm

### 33. Two models must be compared on the same population, and the old one must be restorable instantly. Which two strategies apply? Select two.

- A. Split traffic between two models in an A/B test
- B. Replace the model version in place
- C. Run the new model in shadow mode
- D. Roll out a canary with a small traffic share
- E. Deploy blue/green with an instant switch

### 34. An internal tool with ten users can take the new version immediately. What strategy is described?

- A. Roll out a canary with a small traffic share
- B. Replace the model version in place
- C. Split traffic between two models in an A/B test
- D. Run the new model in shadow mode

### 35. A fraud review must show why one transaction scored high while the analyst watches. What should be used?

- A. Use sampled Shapley on the endpoint
- B. Read the contribution of each feature with ML.EXPLAIN_PREDICT
- C. Explain with Shapley values
- D. Publish a model card with the intended use and limits

### 36. A human reviewer must see which inputs drove one case they are examining. What should be shown?

- A. Choose an inherently interpretable model
- B. Summarise the model with ML.GLOBAL_EXPLAIN
- C. Report the feature attributions to the reviewer
- D. Publish a model card with the intended use and limits

### 37. A vision trainer must stream records from object storage at high throughput. What format should be used?

- A. Stream the new records through Dataflow into the training store
- B. Write the training data as Parquet in Cloud Storage
- C. Read the training data directly from BigQuery
- D. Write the training data as TFRecord shards in Cloud Storage

### 38. A clickstream must land in the training store within minutes of the event. What should be used?

- A. Stream the new records through Dataflow into the training store
- B. Write the training data as TFRecord shards in Cloud Storage
- C. Write the training data as Parquet in Cloud Storage
- D. Read the training data directly from BigQuery

### 39. A retried producer inflates the training counts by three per cent. What should be added?

- A. Validate the schema and quarantine rejected rows
- B. Read the training data directly from BigQuery
- C. Deduplicate on the event key in the ingestion step
- D. Stream the new records through Dataflow into the training store

### 40. A batch with an unexpected column type must fail visibly rather than silently. What should be added?

- A. Write the training data as TFRecord shards in Cloud Storage
- B. Validate the schema and quarantine rejected rows
- C. Stream the new records through Dataflow into the training store
- D. Deduplicate on the event key in the ingestion step

### 41. A trainer needs a pinned CUDA version and a custom system library. What should be used?

- A. Export the AutoML model as an artifact
- B. Run a custom container on Agent Platform
- C. Use a prebuilt serving container
- D. Package the trainer as a Python package

### 42. A small scikit-learn trainer must run remotely without a Dockerfile. What should be used?

- A. Use a prebuilt serving container
- B. Package the trainer as a Python package
- C. Train with Agent Platform AutoML
- D. Run a custom container on Agent Platform

### 43. The batch is already at the minimum and the model still exhausts memory. What should be enabled?

- A. Reduce the per-replica batch size
- B. Lower the learning rate
- C. Enable gradient checkpointing
- D. Request accelerator quota for the region

### 44. The job fails at step zero reading the input path with a 403. What is the cause?

- A. Pin the framework version in the container
- B. Grant the training service account access to the bucket
- C. Request accelerator quota for the region
- D. Verify each worker reads a distinct shard

### 45. A wide search space must be explored efficiently with expensive trials. Which two choices apply? Select two.

- A. Enable early stopping of poor trials
- B. Run a hyperparameter tuning job
- C. Set the random seed in the training code
- D. Cap the search with a trial count and a parallel budget
- E. Choose Bayesian optimisation for the search

### 46. Most trials are clearly losing early and the accelerator queue is full. What should be enabled?

- A. Choose Bayesian optimisation for the search
- B. Cap the search with a trial count and a parallel budget
- C. Run a hyperparameter tuning job
- D. Enable early stopping of poor trials

### 47. A large model meets quality but is too expensive to serve at the required volume. What should be done?

- A. Ground the prompt with retrieval instead of fine-tuning
- B. Distil the large model into a smaller one
- C. Fine-tune the full model
- D. Fine-tune with a parameter-efficient adapter

### 48. A 40 MB model must be trained in an hour on a small dataset. What should be used?

- A. Serve on L4 GPUs
- B. Train on a TPU slice
- C. Serve on CPU only
- D. Train on A100 GPUs

### 49. A model fits on one device and must train four times faster. Which two choices apply? Select two.

- A. Train on a TPU slice
- B. Configure the job as multi-worker with a chief
- C. Use model parallelism
- D. Use data parallelism
- E. Scale the batch size with the worker count

---

## Domain 4 — Serving and scaling models (Serving, Packaging, and Scaling Endpoints)

### 50. A monthly risk report must be regenerated for every customer. What should be used?

- A. Deploy to an online endpoint
- B. Run batch prediction
- C. Send the events to a streaming prediction path
- D. Batch the requests inside the client

### 51. A trading alert must answer in under 50 ms even after an idle period. Which two choices apply? Select two.

- A. Send the events to a streaming prediction path
- B. Deploy to an online endpoint
- C. Run batch prediction
- D. Batch the requests inside the client
- E. Set a minimum replica count

### 52. Each meter reading must be scored as it arrives. What should be used?

- A. Batch the requests inside the client
- B. Deploy to an online endpoint
- C. Run batch prediction
- D. Send the events to a streaming prediction path

### 53. An XGBoost model must be served with no handler code. What should be used?

- A. Attach a GPU to the serving replica
- B. Run a custom container on Agent Platform
- C. Push the serving image to Artifact Registry
- D. Use a prebuilt serving container

### 54. The serving image must be scanned and access-controlled before deployment. Where should it be pushed?

- A. Push the serving image to Artifact Registry
- B. Use a prebuilt serving container
- C. Enable autoscaling on the endpoint
- D. Register the model in Agent Platform Model Registry

### 55. A rollback must not require a rebuild or a redeploy. What should be used?

- A. Register the model in Agent Platform Model Registry
- B. Split traffic between two deployed versions
- C. Deploy the version and move the alias
- D. Replace the model version in place

### 56. A model catalog must show each version with its metrics and lineage. What should be used?

- A. Track artifacts and lineage in ML Metadata
- B. Push the serving image to Artifact Registry
- C. Log the run to Agent Platform Experiments
- D. Register the model in Agent Platform Model Registry

### 57. A new model must take one per cent of traffic and hold there while metrics are watched. Which two controls apply? Select two.

- A. Split traffic between two deployed versions
- B. Run batch prediction
- C. Run the new model in shadow mode
- D. Roll out a canary with a small traffic share
- E. Replace the model version in place

### 58. A model must be evaluated on live traffic while users see no change. What strategy is described?

- A. Split traffic between two models in an A/B test
- B. Replace the model version in place
- C. Run the new model in shadow mode
- D. Roll out a canary with a small traffic share

### 59. A preprocessing difference appears only after deployment. What should be done?

- A. Keep the preprocessing inside the exported model
- B. Share one transformation library between training and serving
- C. Register the feature in Agent Platform Feature Store
- D. Enable step caching

### 60. The endpoint must read the exact feature value the training row used. What should be used?

- A. Register the feature in Agent Platform Feature Store
- B. Add an explicit data validation step
- C. Share one transformation library between training and serving
- D. Deploy the version and move the alias

### 61. A model needs capacity no other workload can consume. What should be used?

- A. Use a shared public endpoint
- B. Deploy with a private endpoint only
- C. Use a dedicated endpoint
- D. Enable autoscaling on the endpoint

### 62. A model must be unreachable from the public internet entirely. What should be deployed?

- A. Use a shared public endpoint
- B. Use a dedicated endpoint
- C. Deploy with a private endpoint only
- D. Attach a GPU to the serving replica

### 63. A speech model needs 25 ms inference and CPU does not meet it. What should be used?

- A. Raise the concurrency per replica
- B. Attach a GPU to the serving replica
- C. Serve on CPU only
- D. Deploy to an Edge TPU device

### 64. A field device must classify locally with no network and a tiny power budget. What should be used?

- A. Deploy to an Edge TPU device
- B. Attach a GPU to the serving replica
- C. Serve on CPU only
- D. Serve on L4 GPUs

### 65. A service must absorb a spike automatically and stop over-paying per request. Which two settings apply? Select two.

- A. Raise the concurrency per replica
- B. Set a minimum replica count
- C. Enable autoscaling on the endpoint
- D. Raise the maximum replica count
- E. Batch the requests inside the client

### 66. The first request after an idle hour takes three seconds. What should be set?

- A. Batch the requests inside the client
- B. Raise the maximum replica count
- C. Raise the concurrency per replica
- D. Set a minimum replica count

### 67. The client can tolerate 150 ms and sends thousands of small payloads. What should it do?

- A. Run batch prediction
- B. Enable autoscaling on the endpoint
- C. Raise the concurrency per replica
- D. Batch the requests inside the client

### 68. An endpoint must stay within an approved ceiling and return per-prediction attributions. Which two settings apply? Select two.

- A. Push the serving image to Artifact Registry
- B. Set a minimum replica count
- C. Raise the maximum replica count
- D. Deploy the version and move the alias
- E. Configure explanation metadata for the endpoint

### 69. The endpoint is correct but each replica handles only one call at a time. What should be raised?

- A. Raise the maximum replica count
- B. Raise the concurrency per replica
- C. Attach a GPU to the serving replica
- D. Batch the requests inside the client

---

## Domain 5 — Automating and orchestrating ML pipelines (Pipelines, Retraining, and CI/CD/CT)

### 70. A retrain must be blocked when it does not beat the production model. What should be added?

- A. Add an explicit data validation step
- B. Enable step caching
- C. Gate the deployment on a model evaluation threshold
- D. Keep the test set out of every tuning decision

### 71. An upstream schema change must stop the pipeline before training starts. What should be added?

- A. Add an explicit data validation step
- B. Validate the schema and quarantine rejected rows
- C. Gate the deployment on a model evaluation threshold
- D. Enable step caching

### 72. The holdout has been reused for tuning, and positives are very rare. Which two practices apply? Select two.

- A. Report ROC AUC
- B. Report MAPE when the error must be read as a percentage
- C. Report precision-recall AUC for the rare class
- D. Keep the test set out of every tuning decision
- E. Inspect the confusion matrix at the operating threshold

### 73. Each step must be a cached container with lineage recorded per artifact. What should be used?

- A. Use Ray on Agent Platform for the distributed compute
- B. Express the workflow as a Kubeflow pipeline
- C. Orchestrate the steps in Agent Platform Pipelines
- D. Orchestrate with Managed Service for Apache Airflow

### 74. A daily chain must coordinate a warehouse load, a vendor SFTP drop, and a deploy. What should orchestrate it?

- A. Orchestrate the steps in Agent Platform Pipelines
- B. Express the workflow as a Kubeflow pipeline
- C. Orchestrate with Managed Service for Apache Airflow
- D. Use Ray on Agent Platform for the distributed compute

### 75. Every release must be reproducible from the recorded job. What should be used?

- A. Add a Cloud Scheduler trigger to the pipeline
- B. Trigger the build and deploy from Cloud Build
- C. Enable step caching
- D. Orchestrate the steps in Agent Platform Pipelines

### 76. A scoring pipeline must run at 04:00 every day. What should be added?

- A. Retrain only on a manual request
- B. Add a Cloud Scheduler trigger to the pipeline
- C. Trigger the pipeline from the arrival of new data
- D. Use Ray on Agent Platform for the distributed compute

### 77. Two repositories compute the same ratio and have drifted apart. What should be done?

- A. Register the feature in Agent Platform Feature Store
- B. Enable step caching
- C. Keep the preprocessing inside the exported model
- D. Share one transformation library between training and serving

### 78. Training must read point-in-time history and serving must read the latest value from one definition. Which two components apply? Select two.

- A. Register the feature in Agent Platform Feature Store
- B. Register the model in Agent Platform Model Registry
- C. Preprocess in memory with pandas
- D. Deduplicate on the event key in the ingestion step
- E. Read the historical features from the offline store

### 79. An unchanged step reruns for thirty minutes on every deployment. What should be enabled?

- A. Gate the deployment on a model evaluation threshold
- B. Enable step caching
- C. Retrain when drift crosses the threshold
- D. Add an explicit data validation step

### 80. Serving must read the value written minutes ago rather than a nightly export. What should be read?

- A. Read the historical features from the offline store
- B. Serve the feature from the online store
- C. Add a crossed feature for the interacting pair
- D. Enable feature monitoring on the feature group

### 81. The business metric is the only agreed signal of model health. What policy fits?

- A. Retrain on a fixed schedule
- B. Retrain when drift crosses the threshold
- C. Retrain only on a manual request
- D. Retrain when the production metric drops

### 82. Competitor pricing shifts the input distribution without warning. What policy fits?

- A. Retrain only on a manual request
- B. Retrain on a fixed schedule
- C. Retrain when drift crosses the threshold
- D. Retrain when the production metric drops

### 83. Retrain and promotion must be automatic with no manual approval step. What should be adopted?

- A. Trigger the pipeline from the arrival of new data
- B. Extend CI/CD into continuous training
- C. Retrain only on a manual request
- D. Enable step caching

### 84. A new labelled batch must start a retrain as soon as it lands. What should be used?

- A. Trigger the pipeline from the arrival of new data
- B. Add a Cloud Scheduler trigger to the pipeline
- C. Retrain only on a manual request
- D. Trigger the build and deploy from Cloud Build

### 85. A deployment must be blocked when the evaluation slips below the threshold. What should the pipeline add?

- A. Add an explicit data validation step
- B. Retrain when drift crosses the threshold
- C. Enable step caching
- D. Gate the deployment on a model evaluation threshold

### 86. A regulator requires a documented retrain cadence rather than an event. What policy fits?

- A. Retrain when drift crosses the threshold
- B. Retrain on a fixed schedule
- C. Retrain when the production metric drops
- D. Retrain only on a manual request

### 87. A reinforcement-learning workload needs actor processes that hold state between steps. What should be used?

- A. Orchestrate with Managed Service for Apache Airflow
- B. Express the workflow as a Kubeflow pipeline
- C. Use Ray on Agent Platform for the distributed compute
- D. Trigger the build and deploy from Cloud Build

---

## Domain 6 — Monitoring AI solutions (Responsible AI, Monitoring, and Drift)

### 88. A public assistant must resist jailbreak attempts and block harmful categories. Which two controls apply? Select two.

- A. Put the boundary in the system instruction
- B. Redact the pattern-matchable fields with a regex
- C. Constrain the response to a JSON schema
- D. Screen the prompts and responses with Model Armor
- E. Configure the model safety filters

### 89. Downstream code cannot parse the model's prose answers. What should be configured?

- A. Put the boundary in the system instruction
- B. Constrain the response to a JSON schema
- C. Configure the model safety filters
- D. Screen the prompts and responses with Model Armor

### 90. Member identifiers keep leaking into prompts sent to an external model. What should be applied?

- A. Redact the pattern-matchable fields with a regex
- B. Put the boundary in the system instruction
- C. Screen the prompts and responses with Model Armor
- D. Constrain the response to a JSON schema

### 91. A hiring model must be watched for disparate impact after launch. What should be enabled?

- A. Document the dataset with a data card
- B. Monitor the outcome rate across the protected groups
- C. Slice the evaluation metrics by the sensitive attribute
- D. Publish a model card with the intended use and limits

### 92. The aggregate error is stable but one group may be worse off. What should be produced?

- A. Monitor the outcome rate across the protected groups
- B. Document the dataset with a data card
- C. Slice the evaluation metrics by the sensitive attribute
- D. Publish a model card with the intended use and limits

### 93. A radiograph model must show which pixels drove one prediction. What should be used?

- A. Use integrated gradients for the image model
- B. Explain with Shapley values
- C. Summarise the model with ML.GLOBAL_EXPLAIN
- D. Use sampled Shapley on the endpoint

### 94. Downstream teams must know the limits of the model they are integrating. What should be published?

- A. Report the feature attributions to the reviewer
- B. Choose an inherently interpretable model
- C. Document the dataset with a data card
- D. Publish a model card with the intended use and limits

### 95. Consumers report odd scores and the team has no view of the live distribution. What should be enabled?

- A. Track p95 latency per model version
- B. Enable Model Monitoring on the endpoint
- C. Set the monitoring threshold from the acceptable error budget
- D. Route the monitoring alert to the owning team

### 96. Drift is detected but nobody is paged. What should be added?

- A. Route the monitoring alert to the owning team
- B. Log the prompt and response with redaction
- C. Score a sample of live answers with the evaluation rubric
- D. Set the monitoring threshold from the acceptable error budget

### 97. Outcome labels trail by weeks, and the score spread has widened. Which two signals apply? Select two.

- A. Watch the prediction distribution
- B. Watch for feature attribution drift
- C. Watch for data drift
- D. Join the delayed ground truth back to the predictions
- E. Watch for concept drift

### 98. A model is accurate offline and inaccurate on the first day in production. What should be investigated?

- A. Watch for data drift
- B. Watch for training-serving skew
- C. Watch for concept drift
- D. Watch for feature attribution drift

### 99. A user reports a wrong answer and the team cannot reconstruct the prompt. What should be added?

- A. Track tokens and cost per request
- B. Log the prompt and response with redaction
- C. Track p95 latency per model version
- D. Enable Model Monitoring on the endpoint

### 100. A generative feature must be scored for fidelity on a sample of live answers. What should be added?

- A. Track tokens and cost per request
- B. Track p95 latency per model version
- C. Score a sample of live answers with the evaluation rubric
- D. Enable Model Monitoring on the endpoint

---

## Answer key and explanations

### Question 1 — A

Answer: Create a BigQuery ML boosted tree classifier. Boosted trees capture non-linear interactions in tabular data while staying in SQL. Local study-map skill 1.1 (BigQuery ML Model Building), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Boosted trees capture non-linear interactions in tabular data while staying in SQL.
- **B:** Incorrect for this question. Linear regression predicts a continuous value such as revenue or demand. Why the correct answer wins: Boosted trees capture non-linear interactions in tabular data while staying in SQL.
- **C:** Incorrect for this question. ARIMA_PLUS models seasonality and trend and returns a forecast interval per period. Why the correct answer wins: Boosted trees capture non-linear interactions in tabular data while staying in SQL.
- **D:** Incorrect for this question. K-means segments rows into unsupervised clusters without a labelled target. Why the correct answer wins: Boosted trees capture non-linear interactions in tabular data while staying in SQL.

### Question 2 — A, E

Answers: Create a BigQuery ML logistic regression model; Declare the feature transformations in the TRANSFORM clause. Logistic regression returns a probability, and TRANSFORM keeps preprocessing inside the model. Logistic regression predicts a binary outcome and trains inside BigQuery with SQL. TRANSFORM keeps preprocessing inside the model, so prediction applies the same steps. Local study-map skill 1.1 (BigQuery ML Model Building), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. TRANSFORM keeps preprocessing inside the model, so prediction applies the same steps. In this case: Logistic regression returns a probability, and TRANSFORM keeps preprocessing inside the model.
- **B:** Incorrect for this question. Importing brings an already-trained model into BigQuery so SQL can score it. Why the correct answer wins: Logistic regression returns a probability, and TRANSFORM keeps preprocessing inside the model.
- **C:** Incorrect for this question. K-means segments rows into unsupervised clusters without a labelled target. Why the correct answer wins: Logistic regression returns a probability, and TRANSFORM keeps preprocessing inside the model.
- **D:** Incorrect for this question. A nested column keeps per-row structured output such as labels and scores together. Why the correct answer wins: Logistic regression returns a probability, and TRANSFORM keeps preprocessing inside the model.
- **E:** Correct. Logistic regression predicts a binary outcome and trains inside BigQuery with SQL. In this case: Logistic regression returns a probability, and TRANSFORM keeps preprocessing inside the model.

### Question 3 — D

Answer: Inspect the metrics with ML.EVALUATE. ML.EVALUATE returns the model metrics against a labelled dataset. Local study-map skill 1.2 (BigQuery ML Feature Engineering and Prediction), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. ML.PREDICT applies a trained model and returns the label and its probability. Why the correct answer wins: ML.EVALUATE returns the model metrics against a labelled dataset.
- **B:** Incorrect for this question. TRANSFORM keeps preprocessing inside the model, so prediction applies the same steps. Why the correct answer wins: ML.EVALUATE returns the model metrics against a labelled dataset.
- **C:** Incorrect for this question. ML.GLOBAL_EXPLAIN ranks the features that matter most across the whole model. Why the correct answer wins: ML.EVALUATE returns the model metrics against a labelled dataset.
- **D:** Correct. In this case: ML.EVALUATE returns the model metrics against a labelled dataset.

### Question 4 — D

Answer: Read the contribution of each feature with ML.EXPLAIN_PREDICT. ML.EXPLAIN_PREDICT attributes each prediction to the features that moved it. Local study-map skill 1.2 (BigQuery ML Feature Engineering and Prediction), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. ML.GLOBAL_EXPLAIN ranks the features that matter most across the whole model. Why the correct answer wins: ML.EXPLAIN_PREDICT attributes each prediction to the features that moved it.
- **B:** Incorrect for this question. ML.PREDICT applies a trained model and returns the label and its probability. Why the correct answer wins: ML.EXPLAIN_PREDICT attributes each prediction to the features that moved it.
- **C:** Incorrect for this question. A nested column keeps per-row structured output such as labels and scores together. Why the correct answer wins: ML.EXPLAIN_PREDICT attributes each prediction to the features that moved it.
- **D:** Correct. In this case: ML.EXPLAIN_PREDICT attributes each prediction to the features that moved it.

### Question 5 — B

Answer: Train an Agent Platform AutoML image model. AutoML image trains classification or object detection from labelled images. Local study-map skill 1.3 (Agent Platform AutoML), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. AutoML tabular selects the architecture and tuning for a structured dataset. Why the correct answer wins: AutoML image trains classification or object detection from labelled images.
- **B:** Correct. In this case: AutoML image trains classification or object detection from labelled images.
- **C:** Incorrect for this question. AutoML forecasting builds a time series model with covariates and backtesting. Why the correct answer wins: AutoML image trains classification or object detection from labelled images.
- **D:** Incorrect for this question. AutoML text trains classification, extraction, or sentiment from labelled text. Why the correct answer wins: AutoML image trains classification or object detection from labelled images.

### Question 6 — D

Answer: Train an Agent Platform AutoML text model. AutoML text trains classification from labelled text. Local study-map skill 1.3 (Agent Platform AutoML), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. AutoML tabular selects the architecture and tuning for a structured dataset. Why the correct answer wins: AutoML text trains classification from labelled text.
- **B:** Incorrect for this question. AutoML forecasting builds a time series model with covariates and backtesting. Why the correct answer wins: AutoML text trains classification from labelled text.
- **C:** Incorrect for this question. AutoML image trains classification or object detection from labelled images. Why the correct answer wins: AutoML text trains classification from labelled text.
- **D:** Correct. In this case: AutoML text trains classification from labelled text.

### Question 7 — D

Answer: Fine-tune a Gemini model from BigQuery. Fine-tuning adapts a foundation model to the domain using rows that stay in BigQuery. Local study-map skill 1.4 (Gemini Fine-Tuning with BigQuery), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Full fine-tuning updates every weight and needs the most data and accelerator memory. Why the correct answer wins: Fine-tuning adapts a foundation model to the domain using rows that stay in BigQuery.
- **B:** Incorrect for this question. A remote model calls the Gemini endpoint from SQL, so generation runs where the data lives. Why the correct answer wins: Fine-tuning adapts a foundation model to the domain using rows that stay in BigQuery.
- **C:** Incorrect for this question. A better prompt is the cheapest experiment and often removes the need to tune at all. Why the correct answer wins: Fine-tuning adapts a foundation model to the domain using rows that stay in BigQuery.
- **D:** Correct. In this case: Fine-tuning adapts a foundation model to the domain using rows that stay in BigQuery.

### Question 8 — D

Answer: Embed the documents with the text embedding model. Embeddings turn text into vectors, which is what a retrieval step searches. Local study-map skill 1.5 (Model Garden Model Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Imagen is the text-to-image model in the Google Cloud generative AI family. Why the correct answer wins: Embeddings turn text into vectors, which is what a retrieval step searches.
- **B:** Incorrect for this question. The larger model gives the best reasoning quality at a higher cost per token. Why the correct answer wins: Embeddings turn text into vectors, which is what a retrieval step searches.
- **C:** Incorrect for this question. Veo is the text-to-video model family offered through the platform. Why the correct answer wins: Embeddings turn text into vectors, which is what a retrieval step searches.
- **D:** Correct. In this case: Embeddings turn text into vectors, which is what a retrieval step searches.

### Question 9 — A

Answer: Use the Translation API. The translation model handles a large language set without custom training. Local study-map skill 1.6 (Industry AI APIs), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: The translation model handles a large language set without custom training.
- **B:** Incorrect for this question. The speech model transcribes audio, including domain phrases through adaptation. Why the correct answer wins: The translation model handles a large language set without custom training.
- **C:** Incorrect for this question. The Natural Language API returns entities, sentiment, and syntax without a custom model. Why the correct answer wins: The translation model handles a large language set without custom training.
- **D:** Incorrect for this question. A Document AI processor extracts structured fields from forms with layout awareness. Why the correct answer wins: The translation model handles a large language set without custom training.

### Question 10 — C

Answer: Use the Natural Language API. The Natural Language API returns entities, sentiment, and syntax without a custom model. Local study-map skill 1.6 (Industry AI APIs), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A Document AI processor extracts structured fields from forms with layout awareness. Why the correct answer wins: The Natural Language API returns entities, sentiment, and syntax without a custom model.
- **B:** Incorrect for this question. The prebuilt Vision model labels, detects, and reads text without training a model. Why the correct answer wins: The Natural Language API returns entities, sentiment, and syntax without a custom model.
- **C:** Correct. In this case: The Natural Language API returns entities, sentiment, and syntax without a custom model.
- **D:** Incorrect for this question. The translation model handles a large language set without custom training. Why the correct answer wins: The Natural Language API returns entities, sentiment, and syntax without a custom model.

### Question 11 — A, D

Answers: Cache the long shared context; Choose the smaller Gemini model for latency and cost. Caching bills the repeated prefix once, and the smaller model answers faster and cheaper. Context caching bills the repeated prefix once instead of on every request. The smaller model answers faster and cheaper, which suits high-volume simple tasks. Local study-map skill 1.7 (Gemini Application Optimization), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. The smaller model answers faster and cheaper, which suits high-volume simple tasks. In this case: Caching bills the repeated prefix once, and the smaller model answers faster and cheaper.
- **B:** Incorrect for this question. A regional endpoint removes cross-region latency and satisfies residency rules. Why the correct answer wins: Caching bills the repeated prefix once, and the smaller model answers faster and cheaper.
- **C:** Incorrect for this question. Throughput is capped by quota, so a quota ceiling cannot be solved by retries. Why the correct answer wins: Caching bills the repeated prefix once, and the smaller model answers faster and cheaper.
- **D:** Correct. Context caching bills the repeated prefix once instead of on every request. In this case: Caching bills the repeated prefix once, and the smaller model answers faster and cheaper.
- **E:** Incorrect for this question. The batch path trades latency for a lower price on non-interactive requests. Why the correct answer wins: Caching bills the repeated prefix once, and the smaller model answers faster and cheaper.

### Question 12 — A

Answer: Send the offline work through the batch API. The batch path trades latency for a lower price on non-interactive requests. Local study-map skill 1.7 (Gemini Application Optimization), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: The batch path trades latency for a lower price on non-interactive requests.
- **B:** Incorrect for this question. Throughput is capped by quota, so a quota ceiling cannot be solved by retries. Why the correct answer wins: The batch path trades latency for a lower price on non-interactive requests.
- **C:** Incorrect for this question. Context caching bills the repeated prefix once instead of on every request. Why the correct answer wins: The batch path trades latency for a lower price on non-interactive requests.
- **D:** Incorrect for this question. Streaming improves perceived latency without reducing total generation time. Why the correct answer wins: The batch path trades latency for a lower price on non-interactive requests.

### Question 13 — C

Answer: Preprocess in memory with pandas. In-memory processing is simplest while the data still fits in memory. In-memory processing is the simplest option and stops working once the data exceeds the worker memory. Local study-map skill 2.1 (Preprocessing Tool Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Dataflow runs the same Beam code in batch and streaming and scales without provisioning. Why the correct answer wins: In-memory processing is simplest while the data still fits in memory.
- **B:** Incorrect for this question. SQL over BigQuery is the cheapest option when the data already sits there and the logic is set-based. Why the correct answer wins: In-memory processing is simplest while the data still fits in memory.
- **C:** Correct. In-memory processing is the simplest option and stops working once the data exceeds the worker memory. In this case: In-memory processing is simplest while the data still fits in memory.
- **D:** Incorrect for this question. Spark suits large transformations the team already has as Scala or PySpark code. Why the correct answer wins: In-memory processing is simplest while the data still fits in memory.

### Question 14 — C, D

Answers: De-identify the fields with Sensitive Data Protection; Split by entity so one customer never spans train and test. Sensitive Data Protection removes the identifiers, and a grouped split prevents leakage. Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts PII. Grouping the split prevents leakage between the training and evaluation rows. Local study-map skill 2.1 (Preprocessing Tool Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A time-based split prevents the model from learning from the future. Why the correct answer wins: Sensitive Data Protection removes the identifiers, and a grouped split prevents leakage.
- **B:** Incorrect for this question. A crossed feature lets a linear model express the interaction it cannot learn alone. Why the correct answer wins: Sensitive Data Protection removes the identifiers, and a grouped split prevents leakage.
- **C:** Correct. Grouping the split prevents leakage between the training and evaluation rows. In this case: Sensitive Data Protection removes the identifiers, and a grouped split prevents leakage.
- **D:** Correct. Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts PII. In this case: Sensitive Data Protection removes the identifiers, and a grouped split prevents leakage.
- **E:** Incorrect for this question. Dropping the field removes the exposure entirely when the model does not need it. Why the correct answer wins: Sensitive Data Protection removes the identifiers, and a grouped split prevents leakage.

### Question 15 — A

Answer: Preprocess with a Dataflow pipeline. Dataflow runs the same Beam code in batch and streaming and scales without provisioning. Local study-map skill 2.1 (Preprocessing Tool Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Dataflow runs the same Beam code in batch and streaming and scales without provisioning.
- **B:** Incorrect for this question. In-memory processing is the simplest option and stops working once the data exceeds the worker memory. Why the correct answer wins: Dataflow runs the same Beam code in batch and streaming and scales without provisioning.
- **C:** Incorrect for this question. SQL over BigQuery is the cheapest option when the data already sits there and the logic is set-based. Why the correct answer wins: Dataflow runs the same Beam code in batch and streaming and scales without provisioning.
- **D:** Incorrect for this question. Spark suits large transformations the team already has as Scala or PySpark code. Why the correct answer wins: Dataflow runs the same Beam code in batch and streaming and scales without provisioning.

### Question 16 — A

Answer: Serve the feature from the online store. The online store returns the latest feature value at low latency for a single entity. Local study-map skill 2.2 (Feature Store), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: The online store returns the latest feature value at low latency for a single entity.
- **B:** Incorrect for this question. The offline store returns point-in-time values for training. Why the correct answer wins: The online store returns the latest feature value at low latency for a single entity.
- **C:** Incorrect for this question. A crossed feature lets a linear model express the interaction it cannot learn alone. Why the correct answer wins: The online store returns the latest feature value at low latency for a single entity.
- **D:** Incorrect for this question. Feature monitoring reports distribution changes per feature, not just per model. Why the correct answer wins: The online store returns the latest feature value at low latency for a single entity.

### Question 17 — A

Answer: Normalise the numeric feature before training. Scaling keeps one large-magnitude feature from dominating the gradient. Local study-map skill 2.2 (Feature Store), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Scaling keeps one large-magnitude feature from dominating the gradient.
- **B:** Incorrect for this question. A crossed feature lets a linear model express the interaction it cannot learn alone. Why the correct answer wins: Scaling keeps one large-magnitude feature from dominating the gradient.
- **C:** Incorrect for this question. Feature Store keeps one definition that both training and serving read. Why the correct answer wins: Scaling keeps one large-magnitude feature from dominating the gradient.
- **D:** Incorrect for this question. Bucketing converts a non-linear relationship into a form a linear model can fit. Why the correct answer wins: Scaling keeps one large-magnitude feature from dominating the gradient.

### Question 18 — A

Answer: Hash the identifiers with a salted key before training. A salted hash keeps the join key usable while removing the direct identifier. Local study-map skill 2.3 (PII Handling and Data Privacy), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: A salted hash keeps the join key usable while removing the direct identifier.
- **B:** Incorrect for this question. Dropping the field removes the exposure entirely when the model does not need it. Why the correct answer wins: A salted hash keeps the join key usable while removing the direct identifier.
- **C:** Incorrect for this question. Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts PII. Why the correct answer wins: A salted hash keeps the join key usable while removing the direct identifier.
- **D:** Incorrect for this question. Restricting the bucket limits who can copy the raw data in the first place. Why the correct answer wins: A salted hash keeps the join key usable while removing the direct identifier.

### Question 19 — A

Answer: Restrict the raw bucket to a privileged service account. Restricting the bucket limits who can copy the raw data. Local study-map skill 2.3 (PII Handling and Data Privacy), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Restricting the bucket limits who can copy the raw data.
- **B:** Incorrect for this question. Dropping the field removes the exposure entirely when the model does not need it. Why the correct answer wins: Restricting the bucket limits who can copy the raw data.
- **C:** Incorrect for this question. A salted hash keeps the join key usable while removing the direct identifier. Why the correct answer wins: Restricting the bucket limits who can copy the raw data.
- **D:** Incorrect for this question. Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts PII. Why the correct answer wins: Restricting the bucket limits who can copy the raw data.

### Question 20 — D

Answer: Set an idle shutdown schedule. Idle shutdown stops paying for a notebook nobody is using. Local study-map skill 2.4 (Notebook Environments and Security), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Colab Enterprise adds managed runtimes, VPC connectivity, and IAM to the Colab experience. Why the correct answer wins: Idle shutdown stops paying for a notebook nobody is using.
- **B:** Incorrect for this question. Workbench is the managed notebook instance inside the project VPC. Why the correct answer wins: Idle shutdown stops paying for a notebook nobody is using.
- **C:** Incorrect for this question. A private-IP runtime reaches the data through the VPC and cannot be opened from the internet. Why the correct answer wins: Idle shutdown stops paying for a notebook nobody is using.
- **D:** Correct. In this case: Idle shutdown stops paying for a notebook nobody is using.

### Question 21 — D

Answer: Pin the runtime to a custom container image. A pinned image makes the environment reproducible across users. Local study-map skill 2.4 (Notebook Environments and Security), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Idle shutdown stops paying for a notebook nobody is using. Why the correct answer wins: A pinned image makes the environment reproducible across users.
- **B:** Incorrect for this question. Colab Enterprise adds managed runtimes, VPC connectivity, and IAM to the Colab experience. Why the correct answer wins: A pinned image makes the environment reproducible across users.
- **C:** Incorrect for this question. The subnet attachment gives the notebook the route to internal data sources. Why the correct answer wins: A pinned image makes the environment reproducible across users.
- **D:** Correct. In this case: A pinned image makes the environment reproducible across users.

### Question 22 — D

Answer: Log the run to Agent Platform Experiments. Experiments records parameters, metrics, and artifacts per run. Local study-map skill 2.5 (Experiment Tracking), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: Experiments records parameters, metrics, and artifacts per run.
- **B:** Incorrect for this question. ML Metadata records which data and code produced which artifact. Why the correct answer wins: Experiments records parameters, metrics, and artifacts per run.
- **C:** Incorrect for this question. A fixed seed makes a rerun reproducible when the rest of the environment is pinned. Why the correct answer wins: Experiments records parameters, metrics, and artifacts per run.
- **D:** Correct. In this case: Experiments records parameters, metrics, and artifacts per run.

### Question 23 — C

Answer: Enable step caching. Caching skips an unchanged step on a rerun. Local study-map skill 2.5 (Experiment Tracking), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Experiments records parameters, metrics, and artifacts per run so runs can be compared. Why the correct answer wins: Caching skips an unchanged step on a rerun.
- **B:** Incorrect for this question. ML Metadata records which data and code produced which artifact. Why the correct answer wins: Caching skips an unchanged step on a rerun.
- **C:** Correct. In this case: Caching skips an unchanged step on a rerun.
- **D:** Incorrect for this question. Comparing on the validation metric keeps model selection independent of the test set. Why the correct answer wins: Caching skips an unchanged step on a rerun.

### Question 24 — A, C

Answers: Orchestrate with Managed Service for Apache Airflow; Trigger the build and deploy from Cloud Build. Airflow expresses cross-system dependencies, and Cloud Build records the build and deploy steps. Airflow expresses cross-system dependencies and schedules outside the ML platform. Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance. Local study-map skill 2.6 (Development Environment Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance. In this case: Airflow expresses cross-system dependencies, and Cloud Build records the build and deploy steps.
- **B:** Incorrect for this question. Kubeflow pipelines give a container-per-step pipeline that runs on the managed service or on GKE. Why the correct answer wins: Airflow expresses cross-system dependencies, and Cloud Build records the build and deploy steps.
- **C:** Correct. Airflow expresses cross-system dependencies and schedules outside the ML platform. In this case: Airflow expresses cross-system dependencies, and Cloud Build records the build and deploy steps.
- **D:** Incorrect for this question. Ray fits a Python-native distributed workload that is not a container-per-step pipeline. Why the correct answer wins: Airflow expresses cross-system dependencies, and Cloud Build records the build and deploy steps.
- **E:** Incorrect for this question. Experiments records parameters, metrics, and artifacts per run so runs can be compared. Why the correct answer wins: Airflow expresses cross-system dependencies, and Cloud Build records the build and deploy steps.

### Question 25 — C

Answer: Express the workflow as a Kubeflow pipeline. A Kubeflow pipeline can run on the managed service or on GKE. Kubeflow pipelines give a container-per-step pipeline that runs on the managed service or on GKE. Local study-map skill 2.6 (Development Environment Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Airflow expresses cross-system dependencies and schedules outside the ML platform. Why the correct answer wins: A Kubeflow pipeline can run on the managed service or on GKE.
- **B:** Incorrect for this question. Pipelines runs each step as a container with caching, lineage, and retry. Why the correct answer wins: A Kubeflow pipeline can run on the managed service or on GKE.
- **C:** Correct. Kubeflow pipelines give a container-per-step pipeline that runs on the managed service or on GKE. In this case: A Kubeflow pipeline can run on the managed service or on GKE.
- **D:** Incorrect for this question. Ray fits a Python-native distributed workload that is not a container-per-step pipeline. Why the correct answer wins: A Kubeflow pipeline can run on the managed service or on GKE.

### Question 26 — A, B

Answers: Inspect the confusion matrix at the operating threshold; Choose the threshold from the cost of each error type. The matrix shows the error split at the threshold, and the threshold follows the cost of each error. The matrix shows the false-positive and false-negative split the business will feel. The decision threshold follows the relative cost of a false positive and a false negative. Local study-map skill 2.7 (Evaluation Metrics and LLM-as-a-Judge), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. The decision threshold follows the relative cost of a false positive and a false negative. In this case: The matrix shows the error split at the threshold, and the threshold follows the cost of each error.
- **B:** Correct. The matrix shows the false-positive and false-negative split the business will feel. In this case: The matrix shows the error split at the threshold, and the threshold follows the cost of each error.
- **C:** Incorrect for this question. RMSE expresses the typical error in the units of the target. Why the correct answer wins: The matrix shows the error split at the threshold, and the threshold follows the cost of each error.
- **D:** Incorrect for this question. ROC AUC measures ranking quality across thresholds and hides class imbalance. Why the correct answer wins: The matrix shows the error split at the threshold, and the threshold follows the cost of each error.
- **E:** Incorrect for this question. MAPE expresses the error relative to the actual value, which business readers understand. Why the correct answer wins: The matrix shows the error split at the threshold, and the threshold follows the cost of each error.

### Question 27 — C

Answer: Report RMSE for the regression target. RMSE expresses the typical error in the units of the target. Local study-map skill 2.7 (Evaluation Metrics and LLM-as-a-Judge), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Precision-recall AUC stays informative when the positive class is rare. Why the correct answer wins: RMSE expresses the typical error in the units of the target.
- **B:** Incorrect for this question. MAPE expresses the error relative to the actual value, which business readers understand. Why the correct answer wins: RMSE expresses the typical error in the units of the target.
- **C:** Correct. In this case: RMSE expresses the typical error in the units of the target.
- **D:** Incorrect for this question. ROC AUC measures ranking quality across thresholds and hides class imbalance. Why the correct answer wins: RMSE expresses the typical error in the units of the target.

### Question 28 — C

Answer: Track artifacts and lineage in ML Metadata. ML Metadata records which data and code produced which artifact. Local study-map skill 2.8 (Metadata and Lineage), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: ML Metadata records which data and code produced which artifact.
- **B:** Incorrect for this question. Experiments records parameters, metrics, and artifacts per run so runs can be compared. Why the correct answer wins: ML Metadata records which data and code produced which artifact.
- **C:** Correct. In this case: ML Metadata records which data and code produced which artifact.
- **D:** Incorrect for this question. The registry versions the model artifact and links it to its lineage and metrics. Why the correct answer wins: ML Metadata records which data and code produced which artifact.

### Question 29 — D

Answer: Choose a foundation model. A foundation model suits an open-ended language task where labelled data is scarce. Local study-map skill 3.1 (Model Type Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A classical time series model suits a single series with strong seasonality and little covariate data. Why the correct answer wins: A foundation model suits an open-ended language task where labelled data is scarce.
- **B:** Incorrect for this question. A DNN suits a large tabular or unstructured dataset where interactions matter. Why the correct answer wins: A foundation model suits an open-ended language task where labelled data is scarce.
- **C:** Incorrect for this question. TabNet gives an interpretable attentive tabular model inside custom training. Why the correct answer wins: A foundation model suits an open-ended language task where labelled data is scarce.
- **D:** Correct. In this case: A foundation model suits an open-ended language task where labelled data is scarce.

### Question 30 — D

Answer: Choose a deep neural network. A DNN suits a large tabular dataset where interactions matter. Local study-map skill 3.1 (Model Type Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. TabNet gives an interpretable attentive tabular model inside custom training. Why the correct answer wins: A DNN suits a large tabular dataset where interactions matter.
- **B:** Incorrect for this question. A classical time series model suits a single series with strong seasonality and little covariate data. Why the correct answer wins: A DNN suits a large tabular dataset where interactions matter.
- **C:** Incorrect for this question. A foundation model suits an open-ended language or multimodal task where labelled data is scarce. Why the correct answer wins: A DNN suits a large tabular dataset where interactions matter.
- **D:** Correct. In this case: A DNN suits a large tabular dataset where interactions matter.

### Question 31 — A

Answer: Train an Agent Platform AutoML forecasting model. AutoML forecasting builds a time series model with covariates and backtesting. Local study-map skill 3.2 (Product Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: AutoML forecasting builds a time series model with covariates and backtesting.
- **B:** Incorrect for this question. AutoML text trains classification, extraction, or sentiment from labelled text. Why the correct answer wins: AutoML forecasting builds a time series model with covariates and backtesting.
- **C:** Incorrect for this question. AutoML image trains classification or object detection from labelled images. Why the correct answer wins: AutoML forecasting builds a time series model with covariates and backtesting.
- **D:** Incorrect for this question. AutoML tabular selects the architecture and tuning for a structured dataset. Why the correct answer wins: AutoML forecasting builds a time series model with covariates and backtesting.

### Question 32 — A

Answer: Build the model in BigQuery ML. BigQuery ML keeps training next to the data and removes a separate serving pipeline. Local study-map skill 3.2 (Product Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: BigQuery ML keeps training next to the data and removes a separate serving pipeline.
- **B:** Incorrect for this question. Custom training keeps full control of the framework and the loss. Why the correct answer wins: BigQuery ML keeps training next to the data and removes a separate serving pipeline.
- **C:** Incorrect for this question. AutoML removes architecture search and tuning from the team while keeping a managed endpoint. Why the correct answer wins: BigQuery ML keeps training next to the data and removes a separate serving pipeline.
- **D:** Incorrect for this question. TabNet gives an interpretable attentive tabular model inside custom training. Why the correct answer wins: BigQuery ML keeps training next to the data and removes a separate serving pipeline.

### Question 33 — A, E

Answers: Split traffic between two models in an A/B test; Deploy blue/green with an instant switch. A/B testing compares two models on one population, and two deployments let the switch be reversed. A/B testing compares two models on the same population with a traffic split. Two identical deployments let the switch be reversed immediately. Local study-map skill 3.3 (Deployment Strategy Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. A/B testing compares two models on the same population with a traffic split. In this case: A/B testing compares two models on one population, and two deployments let the switch be reversed.
- **B:** Incorrect for this question. An in-place replacement exposes every request to the new version at once. Why the correct answer wins: A/B testing compares two models on one population, and two deployments let the switch be reversed.
- **C:** Incorrect for this question. Shadow mode scores live traffic without serving its answers, so the comparison costs nothing to users. Why the correct answer wins: A/B testing compares two models on one population, and two deployments let the switch be reversed.
- **D:** Incorrect for this question. A canary limits the blast radius while the new model is compared with the old one. Why the correct answer wins: A/B testing compares two models on one population, and two deployments let the switch be reversed.
- **E:** Correct. Two identical deployments let the switch be reversed immediately. In this case: A/B testing compares two models on one population, and two deployments let the switch be reversed.

### Question 34 — B

Answer: Replace the model version in place. An in-place replacement exposes every request to the new version at once. Local study-map skill 3.3 (Deployment Strategy Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A canary limits the blast radius while the new model is compared with the old one. Why the correct answer wins: An in-place replacement exposes every request to the new version at once.
- **B:** Correct. In this case: An in-place replacement exposes every request to the new version at once.
- **C:** Incorrect for this question. A/B testing compares two models on the same population with a traffic split. Why the correct answer wins: An in-place replacement exposes every request to the new version at once.
- **D:** Incorrect for this question. Shadow mode scores live traffic without serving its answers, so the comparison costs nothing to users. Why the correct answer wins: An in-place replacement exposes every request to the new version at once.

### Question 35 — A

Answer: Use sampled Shapley on the endpoint. Sampled Shapley explains individual online predictions with a bounded compute cost. Local study-map skill 3.4 (Interpretability), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Sampled Shapley explains individual online predictions with a bounded compute cost.
- **B:** Incorrect for this question. ML.EXPLAIN_PREDICT attributes each prediction to the features that moved it. Why the correct answer wins: Sampled Shapley explains individual online predictions with a bounded compute cost.
- **C:** Incorrect for this question. Shapley values attribute a prediction to its features with a consistent baseline. Why the correct answer wins: Sampled Shapley explains individual online predictions with a bounded compute cost.
- **D:** Incorrect for this question. The card states where the model may be used and where it must not. Why the correct answer wins: Sampled Shapley explains individual online predictions with a bounded compute cost.

### Question 36 — C

Answer: Report the feature attributions to the reviewer. Attribution shows which inputs drove the decision in that case. Local study-map skill 3.4 (Interpretability), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A linear or tree model can be read directly when regulation demands an explanation by construction. Why the correct answer wins: Attribution shows which inputs drove the decision in that case.
- **B:** Incorrect for this question. ML.GLOBAL_EXPLAIN ranks the features that matter most across the whole model. Why the correct answer wins: Attribution shows which inputs drove the decision in that case.
- **C:** Correct. In this case: Attribution shows which inputs drove the decision in that case.
- **D:** Incorrect for this question. The card states where the model may be used and where it must not. Why the correct answer wins: Attribution shows which inputs drove the decision in that case.

### Question 37 — D

Answer: Write the training data as TFRecord shards in Cloud Storage. Sharded TFRecord is the efficient read format for distributed training. Local study-map skill 3.5 (Training Data Organization), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A streaming path keeps the training data current without a nightly copy. Why the correct answer wins: Sharded TFRecord is the efficient read format for distributed training.
- **B:** Incorrect for this question. Parquet is columnar and cheap to scan for tabular training data. Why the correct answer wins: Sharded TFRecord is the efficient read format for distributed training.
- **C:** Incorrect for this question. Reading from BigQuery avoids a copy and keeps the query pushdown. Why the correct answer wins: Sharded TFRecord is the efficient read format for distributed training.
- **D:** Correct. In this case: Sharded TFRecord is the efficient read format for distributed training.

### Question 38 — A

Answer: Stream the new records through Dataflow into the training store. A streaming path keeps the training data current without a nightly copy. Local study-map skill 3.5 (Training Data Organization), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: A streaming path keeps the training data current without a nightly copy.
- **B:** Incorrect for this question. Sharded TFRecord is the efficient read format for distributed training. Why the correct answer wins: A streaming path keeps the training data current without a nightly copy.
- **C:** Incorrect for this question. Parquet is columnar and cheap to scan for tabular training data. Why the correct answer wins: A streaming path keeps the training data current without a nightly copy.
- **D:** Incorrect for this question. Reading from BigQuery avoids a copy and keeps the query pushdown. Why the correct answer wins: A streaming path keeps the training data current without a nightly copy.

### Question 39 — C

Answer: Deduplicate on the event key in the ingestion step. Deduplicating at ingest stops duplicated records inflating the training set. Local study-map skill 3.6 (Ingestion into Training Pipelines), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Rejecting rows into a side table makes a schema break visible instead of silent. Why the correct answer wins: Deduplicating at ingest stops duplicated records inflating the training set.
- **B:** Incorrect for this question. Reading from BigQuery avoids a copy and keeps the query pushdown. Why the correct answer wins: Deduplicating at ingest stops duplicated records inflating the training set.
- **C:** Correct. In this case: Deduplicating at ingest stops duplicated records inflating the training set.
- **D:** Incorrect for this question. A streaming path keeps the training data current without a nightly copy. Why the correct answer wins: Deduplicating at ingest stops duplicated records inflating the training set.

### Question 40 — B

Answer: Validate the schema and quarantine rejected rows. Rejecting rows into a side table makes a schema break visible instead of silent. Local study-map skill 3.6 (Ingestion into Training Pipelines), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Sharded TFRecord is the efficient read format for distributed training. Why the correct answer wins: Rejecting rows into a side table makes a schema break visible instead of silent.
- **B:** Correct. In this case: Rejecting rows into a side table makes a schema break visible instead of silent.
- **C:** Incorrect for this question. A streaming path keeps the training data current without a nightly copy. Why the correct answer wins: Rejecting rows into a side table makes a schema break visible instead of silent.
- **D:** Incorrect for this question. Deduplicating at ingest stops duplicated records inflating the training set. Why the correct answer wins: Rejecting rows into a side table makes a schema break visible instead of silent.

### Question 41 — B

Answer: Run a custom container on Agent Platform. A custom container carries its own framework and dependencies. Local study-map skill 3.7 (Custom Training and SDKs), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Export produces a container-ready artifact that can be served outside the managed endpoint. Why the correct answer wins: A custom container carries its own framework and dependencies.
- **B:** Correct. In this case: A custom container carries its own framework and dependencies.
- **C:** Incorrect for this question. A prebuilt container already implements the framework handler, so no serving code is written. Why the correct answer wins: A custom container carries its own framework and dependencies.
- **D:** Incorrect for this question. The prebuilt container installs the package, which is the lightest way to run custom code. Why the correct answer wins: A custom container carries its own framework and dependencies.

### Question 42 — B

Answer: Package the trainer as a Python package. The prebuilt container installs the package, which is the lightest way to run custom code. Local study-map skill 3.7 (Custom Training and SDKs), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A prebuilt container already implements the framework handler, so no serving code is written. Why the correct answer wins: The prebuilt container installs the package, which is the lightest way to run custom code.
- **B:** Correct. In this case: The prebuilt container installs the package, which is the lightest way to run custom code.
- **C:** Incorrect for this question. AutoML removes architecture search and tuning from the team while keeping a managed endpoint. Why the correct answer wins: The prebuilt container installs the package, which is the lightest way to run custom code.
- **D:** Incorrect for this question. A custom container carries its own framework and dependencies into the managed training job. Why the correct answer wins: The prebuilt container installs the package, which is the lightest way to run custom code.

### Question 43 — C

Answer: Enable gradient checkpointing. Checkpointing trades recomputation for activation memory. Local study-map skill 3.8 (Training Failure Troubleshooting), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The out-of-memory error is a memory-per-step problem, so the batch is the first lever. Why the correct answer wins: Checkpointing trades recomputation for activation memory.
- **B:** Incorrect for this question. A loss that becomes NaN usually reflects a step size too large for the data scale. Why the correct answer wins: Checkpointing trades recomputation for activation memory.
- **C:** Correct. In this case: Checkpointing trades recomputation for activation memory.
- **D:** Incorrect for this question. Accelerator quota is regional and blocks the job before the code runs. Why the correct answer wins: Checkpointing trades recomputation for activation memory.

### Question 44 — B

Answer: Grant the training service account access to the bucket. A permission error on the input is a missing IAM binding. Local study-map skill 3.8 (Training Failure Troubleshooting), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A framework mismatch between local and remote runs changes behaviour without changing the code. Why the correct answer wins: A permission error on the input is a missing IAM binding.
- **B:** Correct. In this case: A permission error on the input is a missing IAM binding.
- **C:** Incorrect for this question. Accelerator quota is regional and blocks the job before the code runs. Why the correct answer wins: A permission error on the input is a missing IAM binding.
- **D:** Incorrect for this question. Duplicated shards silently shrink the effective dataset and skew the loss. Why the correct answer wins: A permission error on the input is a missing IAM binding.

### Question 45 — B, E

Answers: Run a hyperparameter tuning job; Choose Bayesian optimisation for the search. The tuning service searches in parallel, and Bayesian search spends fewer trials. The tuning service searches the space in parallel and reports the best trial. Bayesian search spends fewer trials to reach a good configuration. Local study-map skill 3.9 (Hyperparameter Tuning), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Early stopping frees capacity from trials that cannot win. Why the correct answer wins: The tuning service searches in parallel, and Bayesian search spends fewer trials.
- **B:** Correct. The tuning service searches the space in parallel and reports the best trial. In this case: The tuning service searches in parallel, and Bayesian search spends fewer trials.
- **C:** Incorrect for this question. A fixed seed makes a rerun reproducible when the rest of the environment is pinned. Why the correct answer wins: The tuning service searches in parallel, and Bayesian search spends fewer trials.
- **D:** Incorrect for this question. The budget bounds both the cost and the wall-clock time of the search. Why the correct answer wins: The tuning service searches in parallel, and Bayesian search spends fewer trials.
- **E:** Correct. Bayesian search spends fewer trials to reach a good configuration. In this case: The tuning service searches in parallel, and Bayesian search spends fewer trials.

### Question 46 — D

Answer: Enable early stopping of poor trials. Early stopping frees capacity from trials that cannot win. Local study-map skill 3.9 (Hyperparameter Tuning), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Bayesian search spends fewer trials to reach a good configuration. Why the correct answer wins: Early stopping frees capacity from trials that cannot win.
- **B:** Incorrect for this question. The budget bounds both the cost and the wall-clock time of the search. Why the correct answer wins: Early stopping frees capacity from trials that cannot win.
- **C:** Incorrect for this question. The tuning service searches the space in parallel and reports the best trial. Why the correct answer wins: Early stopping frees capacity from trials that cannot win.
- **D:** Correct. In this case: Early stopping frees capacity from trials that cannot win.

### Question 47 — B

Answer: Distil the large model into a smaller one. Distillation moves the quality of the teacher into a model cheap enough to serve. Local study-map skill 3.10 (Fine-Tuning Decisions), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Retrieval is the cheaper answer when the problem is missing knowledge rather than missing behaviour. Why the correct answer wins: Distillation moves the quality of the teacher into a model cheap enough to serve.
- **B:** Correct. In this case: Distillation moves the quality of the teacher into a model cheap enough to serve.
- **C:** Incorrect for this question. Full fine-tuning updates every weight and needs the most data and accelerator memory. Why the correct answer wins: Distillation moves the quality of the teacher into a model cheap enough to serve.
- **D:** Incorrect for this question. A parameter-efficient adapter trains a small number of weights and keeps the base model intact. Why the correct answer wins: Distillation moves the quality of the teacher into a model cheap enough to serve.

### Question 48 — C

Answer: Serve on CPU only. CPU training is enough for a small model on a small dataset. CPU serving is the cheapest option for a small model with a generous latency budget. Local study-map skill 3.11 (Hardware and Accelerator Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. An L4 GPU gives low-cost inference acceleration for a modest model. Why the correct answer wins: CPU training is enough for a small model on a small dataset.
- **B:** Incorrect for this question. A TPU slice gives a tightly coupled accelerator fabric for large synchronous training. Why the correct answer wins: CPU training is enough for a small model on a small dataset.
- **C:** Correct. CPU serving is the cheapest option for a small model with a generous latency budget. In this case: CPU training is enough for a small model on a small dataset.
- **D:** Incorrect for this question. A100 GPUs suit mixed-precision training where the framework expects CUDA. Why the correct answer wins: CPU training is enough for a small model on a small dataset.

### Question 49 — B, D

Answers: Use data parallelism; Configure the job as multi-worker with a chief. Data parallelism replicates the model across workers, and multi-worker gives each a shard and a chief. Data parallelism replicates the model and splits each batch across the workers. Multi-worker gives each replica a shard of the data and a defined chief. Local study-map skill 3.12 (Distributed Training), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A TPU slice gives a tightly coupled accelerator fabric for large synchronous training. Why the correct answer wins: Data parallelism replicates the model across workers, and multi-worker gives each a shard and a chief.
- **B:** Correct. Multi-worker gives each replica a shard of the data and a defined chief. In this case: Data parallelism replicates the model across workers, and multi-worker gives each a shard and a chief.
- **C:** Incorrect for this question. Model parallelism splits the layers across devices when one model does not fit on one. Why the correct answer wins: Data parallelism replicates the model across workers, and multi-worker gives each a shard and a chief.
- **D:** Correct. Data parallelism replicates the model and splits each batch across the workers. In this case: Data parallelism replicates the model across workers, and multi-worker gives each a shard and a chief.
- **E:** Incorrect for this question. A larger global batch keeps each worker busy after the split. Why the correct answer wins: Data parallelism replicates the model across workers, and multi-worker gives each a shard and a chief.

### Question 50 — B

Answer: Run batch prediction. Batch prediction reads a file and writes predictions without holding serving capacity. Local study-map skill 4.1 (Batch and Online Inference), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. An endpoint keeps capacity ready for low-latency per-request predictions. Why the correct answer wins: Batch prediction reads a file and writes predictions without holding serving capacity.
- **B:** Correct. In this case: Batch prediction reads a file and writes predictions without holding serving capacity.
- **C:** Incorrect for this question. Streaming answers each event as it arrives rather than on a schedule. Why the correct answer wins: Batch prediction reads a file and writes predictions without holding serving capacity.
- **D:** Incorrect for this question. Batching amortises the per-request overhead when the caller can wait. Why the correct answer wins: Batch prediction reads a file and writes predictions without holding serving capacity.

### Question 51 — B, E

Answers: Deploy to an online endpoint; Set a minimum replica count. An endpoint keeps capacity ready, and a minimum replica keeps it warm. An endpoint keeps capacity ready for low-latency per-request predictions. A minimum replica keeps capacity warm so the first request after a quiet period is fast. Local study-map skill 4.1 (Batch and Online Inference), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Streaming answers each event as it arrives rather than on a schedule. Why the correct answer wins: An endpoint keeps capacity ready, and a minimum replica keeps it warm.
- **B:** Correct. An endpoint keeps capacity ready for low-latency per-request predictions. In this case: An endpoint keeps capacity ready, and a minimum replica keeps it warm.
- **C:** Incorrect for this question. Batch prediction reads a file or table and writes predictions without holding serving capacity. Why the correct answer wins: An endpoint keeps capacity ready, and a minimum replica keeps it warm.
- **D:** Incorrect for this question. Batching amortises the per-request overhead when the caller can wait. Why the correct answer wins: An endpoint keeps capacity ready, and a minimum replica keeps it warm.
- **E:** Correct. A minimum replica keeps capacity warm so the first request after a quiet period is fast. In this case: An endpoint keeps capacity ready, and a minimum replica keeps it warm.

### Question 52 — D

Answer: Send the events to a streaming prediction path. Streaming answers each event as it arrives rather than on a schedule. Local study-map skill 4.1 (Batch and Online Inference), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Batching amortises the per-request overhead when the caller can wait. Why the correct answer wins: Streaming answers each event as it arrives rather than on a schedule.
- **B:** Incorrect for this question. An endpoint keeps capacity ready for low-latency per-request predictions. Why the correct answer wins: Streaming answers each event as it arrives rather than on a schedule.
- **C:** Incorrect for this question. Batch prediction reads a file or table and writes predictions without holding serving capacity. Why the correct answer wins: Streaming answers each event as it arrives rather than on a schedule.
- **D:** Correct. In this case: Streaming answers each event as it arrives rather than on a schedule.

### Question 53 — D

Answer: Use a prebuilt serving container. A prebuilt container already implements the framework handler. Local study-map skill 4.2 (Packaging and Custom Containers), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A GPU shortens inference time enough to meet a tight latency target. Why the correct answer wins: A prebuilt container already implements the framework handler.
- **B:** Incorrect for this question. A custom container carries its own framework and dependencies into the managed training job. Why the correct answer wins: A prebuilt container already implements the framework handler.
- **C:** Incorrect for this question. Artifact Registry holds the image with IAM and vulnerability metadata. Why the correct answer wins: A prebuilt container already implements the framework handler.
- **D:** Correct. In this case: A prebuilt container already implements the framework handler.

### Question 54 — A

Answer: Push the serving image to Artifact Registry. Artifact Registry holds the image with IAM and vulnerability metadata. Local study-map skill 4.2 (Packaging and Custom Containers), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Artifact Registry holds the image with IAM and vulnerability metadata.
- **B:** Incorrect for this question. A prebuilt container already implements the framework handler, so no serving code is written. Why the correct answer wins: Artifact Registry holds the image with IAM and vulnerability metadata.
- **C:** Incorrect for this question. Autoscaling adds replicas with the traffic and removes them afterwards. Why the correct answer wins: Artifact Registry holds the image with IAM and vulnerability metadata.
- **D:** Incorrect for this question. The registry versions the model artifact and links it to its lineage and metrics. Why the correct answer wins: Artifact Registry holds the image with IAM and vulnerability metadata.

### Question 55 — C

Answer: Deploy the version and move the alias. An alias decouples the served version from the artifact id. An alias decouples the served version name from the artifact id, so a rollback is a pointer move. Local study-map skill 4.3 (Model Registry and Versioning), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The registry versions the model artifact and links it to its lineage and metrics. Why the correct answer wins: An alias decouples the served version from the artifact id.
- **B:** Incorrect for this question. A traffic split sends a defined share to each version on the same endpoint. Why the correct answer wins: An alias decouples the served version from the artifact id.
- **C:** Correct. An alias decouples the served version name from the artifact id, so a rollback is a pointer move. In this case: An alias decouples the served version from the artifact id.
- **D:** Incorrect for this question. An in-place replacement exposes every request to the new version at once. Why the correct answer wins: An alias decouples the served version from the artifact id.

### Question 56 — D

Answer: Register the model in Agent Platform Model Registry. The registry versions the model artifact and links it to its lineage and metrics. Local study-map skill 4.3 (Model Registry and Versioning), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. ML Metadata records which data and code produced which artifact. Why the correct answer wins: The registry versions the model artifact and links it to its lineage and metrics.
- **B:** Incorrect for this question. Artifact Registry holds the image with IAM and vulnerability metadata. Why the correct answer wins: The registry versions the model artifact and links it to its lineage and metrics.
- **C:** Incorrect for this question. Experiments records parameters, metrics, and artifacts per run so runs can be compared. Why the correct answer wins: The registry versions the model artifact and links it to its lineage and metrics.
- **D:** Correct. In this case: The registry versions the model artifact and links it to its lineage and metrics.

### Question 57 — A, D

Answers: Roll out a canary with a small traffic share; Split traffic between two deployed versions. A canary limits the blast radius, and the traffic split holds a defined share. A canary limits the blast radius while the new model is compared with the old one. A traffic split sends a defined share to each version on the same endpoint. Local study-map skill 4.4 (Model Rollout Strategies), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. A traffic split sends a defined share to each version on the same endpoint. In this case: A canary limits the blast radius, and the traffic split holds a defined share.
- **B:** Incorrect for this question. Batch prediction reads a file or table and writes predictions without holding serving capacity. Why the correct answer wins: A canary limits the blast radius, and the traffic split holds a defined share.
- **C:** Incorrect for this question. Shadow mode scores live traffic without serving its answers, so the comparison costs nothing to users. Why the correct answer wins: A canary limits the blast radius, and the traffic split holds a defined share.
- **D:** Correct. A canary limits the blast radius while the new model is compared with the old one. In this case: A canary limits the blast radius, and the traffic split holds a defined share.
- **E:** Incorrect for this question. An in-place replacement exposes every request to the new version at once. Why the correct answer wins: A canary limits the blast radius, and the traffic split holds a defined share.

### Question 58 — C

Answer: Run the new model in shadow mode. Shadow mode scores live traffic without serving its answers. Local study-map skill 4.4 (Model Rollout Strategies), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A/B testing compares two models on the same population with a traffic split. Why the correct answer wins: Shadow mode scores live traffic without serving its answers.
- **B:** Incorrect for this question. An in-place replacement exposes every request to the new version at once. Why the correct answer wins: Shadow mode scores live traffic without serving its answers.
- **C:** Correct. In this case: Shadow mode scores live traffic without serving its answers.
- **D:** Incorrect for this question. A canary limits the blast radius while the new model is compared with the old one. Why the correct answer wins: Shadow mode scores live traffic without serving its answers.

### Question 59 — A

Answer: Keep the preprocessing inside the exported model. Preprocessing inside the artifact cannot drift between the two paths. Local study-map skill 4.5 (Inference Preprocessing and Postprocessing), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Preprocessing inside the artifact cannot drift between the two paths.
- **B:** Incorrect for this question. Shared code removes the class of bug where the two paths compute a feature differently. Why the correct answer wins: Preprocessing inside the artifact cannot drift between the two paths.
- **C:** Incorrect for this question. Feature Store keeps one definition that both training and serving read. Why the correct answer wins: Preprocessing inside the artifact cannot drift between the two paths.
- **D:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: Preprocessing inside the artifact cannot drift between the two paths.

### Question 60 — A

Answer: Register the feature in Agent Platform Feature Store. Feature Store keeps one definition that both training and serving read. Local study-map skill 4.5 (Inference Preprocessing and Postprocessing), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Feature Store keeps one definition that both training and serving read.
- **B:** Incorrect for this question. A validation step stops a bad batch before it reaches training. Why the correct answer wins: Feature Store keeps one definition that both training and serving read.
- **C:** Incorrect for this question. Shared code removes the class of bug where the two paths compute a feature differently. Why the correct answer wins: Feature Store keeps one definition that both training and serving read.
- **D:** Incorrect for this question. An alias decouples the served version name from the artifact id, so a rollback is a pointer move. Why the correct answer wins: Feature Store keeps one definition that both training and serving read.

### Question 61 — C

Answer: Use a dedicated endpoint. A dedicated endpoint gives the model its own capacity. Local study-map skill 4.6 (Endpoint Types and Access), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A shared endpoint removes the deployment step but gives no control over capacity or residency. Why the correct answer wins: A dedicated endpoint gives the model its own capacity.
- **B:** Incorrect for this question. A private endpoint is reachable only from the VPC and shares no public surface. Why the correct answer wins: A dedicated endpoint gives the model its own capacity.
- **C:** Correct. In this case: A dedicated endpoint gives the model its own capacity.
- **D:** Incorrect for this question. Autoscaling adds replicas with the traffic and removes them afterwards. Why the correct answer wins: A dedicated endpoint gives the model its own capacity.

### Question 62 — C

Answer: Deploy with a private endpoint only. A private endpoint is reachable only from the VPC. Local study-map skill 4.6 (Endpoint Types and Access), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A shared endpoint removes the deployment step but gives no control over capacity or residency. Why the correct answer wins: A private endpoint is reachable only from the VPC.
- **B:** Incorrect for this question. A dedicated endpoint gives the model its own capacity instead of sharing a pool. Why the correct answer wins: A private endpoint is reachable only from the VPC.
- **C:** Correct. In this case: A private endpoint is reachable only from the VPC.
- **D:** Incorrect for this question. A GPU shortens inference time enough to meet a tight latency target. Why the correct answer wins: A private endpoint is reachable only from the VPC.

### Question 63 — B

Answer: Attach a GPU to the serving replica. A GPU shortens inference time enough to meet a tight latency target. Local study-map skill 4.7 (Serving Hardware), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Concurrency fills each replica before another is started, which lowers cost per request. Why the correct answer wins: A GPU shortens inference time enough to meet a tight latency target.
- **B:** Correct. In this case: A GPU shortens inference time enough to meet a tight latency target.
- **C:** Incorrect for this question. CPU serving is the cheapest option for a small model with a generous latency budget. Why the correct answer wins: A GPU shortens inference time enough to meet a tight latency target.
- **D:** Incorrect for this question. An Edge TPU runs a quantised model on-device where the network cannot be relied on. Why the correct answer wins: A GPU shortens inference time enough to meet a tight latency target.

### Question 64 — A

Answer: Deploy to an Edge TPU device. An Edge TPU runs a quantised model on-device. Local study-map skill 4.7 (Serving Hardware), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: An Edge TPU runs a quantised model on-device.
- **B:** Incorrect for this question. A GPU shortens inference time enough to meet a tight latency target. Why the correct answer wins: An Edge TPU runs a quantised model on-device.
- **C:** Incorrect for this question. CPU serving is the cheapest option for a small model with a generous latency budget. Why the correct answer wins: An Edge TPU runs a quantised model on-device.
- **D:** Incorrect for this question. An L4 GPU gives low-cost inference acceleration for a modest model. Why the correct answer wins: An Edge TPU runs a quantised model on-device.

### Question 65 — A, C

Answers: Enable autoscaling on the endpoint; Raise the concurrency per replica. Autoscaling adds replicas with the traffic, and concurrency lowers the cost per request. Autoscaling adds replicas with the traffic and removes them afterwards. Concurrency fills each replica before another is started, which lowers cost per request. Local study-map skill 4.8 (Serving Throughput and Scaling), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. Concurrency fills each replica before another is started, which lowers cost per request. In this case: Autoscaling adds replicas with the traffic, and concurrency lowers the cost per request.
- **B:** Incorrect for this question. A minimum replica keeps capacity warm so the first request after a quiet period is fast. Why the correct answer wins: Autoscaling adds replicas with the traffic, and concurrency lowers the cost per request.
- **C:** Correct. Autoscaling adds replicas with the traffic and removes them afterwards. In this case: Autoscaling adds replicas with the traffic, and concurrency lowers the cost per request.
- **D:** Incorrect for this question. The ceiling caps how far the endpoint scales, and therefore the throughput it can absorb. Why the correct answer wins: Autoscaling adds replicas with the traffic, and concurrency lowers the cost per request.
- **E:** Incorrect for this question. Batching amortises the per-request overhead when the caller can wait. Why the correct answer wins: Autoscaling adds replicas with the traffic, and concurrency lowers the cost per request.

### Question 66 — D

Answer: Set a minimum replica count. A minimum replica keeps capacity warm. Local study-map skill 4.8 (Serving Throughput and Scaling), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Batching amortises the per-request overhead when the caller can wait. Why the correct answer wins: A minimum replica keeps capacity warm.
- **B:** Incorrect for this question. The ceiling caps how far the endpoint scales, and therefore the throughput it can absorb. Why the correct answer wins: A minimum replica keeps capacity warm.
- **C:** Incorrect for this question. Concurrency fills each replica before another is started, which lowers cost per request. Why the correct answer wins: A minimum replica keeps capacity warm.
- **D:** Correct. In this case: A minimum replica keeps capacity warm.

### Question 67 — D

Answer: Batch the requests inside the client. Batching amortises the per-request overhead when the caller can wait. Local study-map skill 4.8 (Serving Throughput and Scaling), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Batch prediction reads a file or table and writes predictions without holding serving capacity. Why the correct answer wins: Batching amortises the per-request overhead when the caller can wait.
- **B:** Incorrect for this question. Autoscaling adds replicas with the traffic and removes them afterwards. Why the correct answer wins: Batching amortises the per-request overhead when the caller can wait.
- **C:** Incorrect for this question. Concurrency fills each replica before another is started, which lowers cost per request. Why the correct answer wins: Batching amortises the per-request overhead when the caller can wait.
- **D:** Correct. In this case: Batching amortises the per-request overhead when the caller can wait.

### Question 68 — C, E

Answers: Raise the maximum replica count; Configure explanation metadata for the endpoint. The ceiling caps how far it scales, and explanation metadata enables attributions. The ceiling caps how far the endpoint scales, and therefore the throughput it can absorb. Explanation metadata tells the endpoint which inputs to attribute over. Local study-map skill 4.9 (Production Tuning), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Artifact Registry holds the image with IAM and vulnerability metadata. Why the correct answer wins: The ceiling caps how far it scales, and explanation metadata enables attributions.
- **B:** Incorrect for this question. A minimum replica keeps capacity warm so the first request after a quiet period is fast. Why the correct answer wins: The ceiling caps how far it scales, and explanation metadata enables attributions.
- **C:** Correct. The ceiling caps how far the endpoint scales, and therefore the throughput it can absorb. In this case: The ceiling caps how far it scales, and explanation metadata enables attributions.
- **D:** Incorrect for this question. An alias decouples the served version name from the artifact id, so a rollback is a pointer move. Why the correct answer wins: The ceiling caps how far it scales, and explanation metadata enables attributions.
- **E:** Correct. Explanation metadata tells the endpoint which inputs to attribute over. In this case: The ceiling caps how far it scales, and explanation metadata enables attributions.

### Question 69 — B

Answer: Raise the concurrency per replica. Concurrency fills each replica before another is started. Local study-map skill 4.9 (Production Tuning), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The ceiling caps how far the endpoint scales, and therefore the throughput it can absorb. Why the correct answer wins: Concurrency fills each replica before another is started.
- **B:** Correct. In this case: Concurrency fills each replica before another is started.
- **C:** Incorrect for this question. A GPU shortens inference time enough to meet a tight latency target. Why the correct answer wins: Concurrency fills each replica before another is started.
- **D:** Incorrect for this question. Batching amortises the per-request overhead when the caller can wait. Why the correct answer wins: Concurrency fills each replica before another is started.

### Question 70 — C

Answer: Gate the deployment on a model evaluation threshold. The gate promotes a model only when it beats the incumbent. Local study-map skill 5.1 (Data and Model Validation), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A validation step stops a bad batch before it reaches training. Why the correct answer wins: The gate promotes a model only when it beats the incumbent.
- **B:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: The gate promotes a model only when it beats the incumbent.
- **C:** Correct. In this case: The gate promotes a model only when it beats the incumbent.
- **D:** Incorrect for this question. A test set that has been used for tuning no longer estimates generalisation. Why the correct answer wins: The gate promotes a model only when it beats the incumbent.

### Question 71 — A

Answer: Add an explicit data validation step. A validation step stops a bad batch before it reaches training. Local study-map skill 5.1 (Data and Model Validation), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: A validation step stops a bad batch before it reaches training.
- **B:** Incorrect for this question. Rejecting rows into a side table makes a schema break visible instead of silent. Why the correct answer wins: A validation step stops a bad batch before it reaches training.
- **C:** Incorrect for this question. The gate promotes a model only when it beats the incumbent on the agreed metric. Why the correct answer wins: A validation step stops a bad batch before it reaches training.
- **D:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: A validation step stops a bad batch before it reaches training.

### Question 72 — C, D

Answers: Keep the test set out of every tuning decision; Report precision-recall AUC for the rare class. A locked test set restores an unbiased estimate, and precision-recall AUC handles the imbalance. A test set that has been used for tuning no longer estimates generalisation. Precision-recall AUC stays informative when the positive class is rare. Local study-map skill 5.1 (Data and Model Validation), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. ROC AUC measures ranking quality across thresholds and hides class imbalance. Why the correct answer wins: A locked test set restores an unbiased estimate, and precision-recall AUC handles the imbalance.
- **B:** Incorrect for this question. MAPE expresses the error relative to the actual value, which business readers understand. Why the correct answer wins: A locked test set restores an unbiased estimate, and precision-recall AUC handles the imbalance.
- **C:** Correct. Precision-recall AUC stays informative when the positive class is rare. In this case: A locked test set restores an unbiased estimate, and precision-recall AUC handles the imbalance.
- **D:** Correct. A test set that has been used for tuning no longer estimates generalisation. In this case: A locked test set restores an unbiased estimate, and precision-recall AUC handles the imbalance.
- **E:** Incorrect for this question. The matrix shows the false-positive and false-negative split the business will feel. Why the correct answer wins: A locked test set restores an unbiased estimate, and precision-recall AUC handles the imbalance.

### Question 73 — C

Answer: Orchestrate the steps in Agent Platform Pipelines. Pipelines runs each step as a container with caching, lineage, and retry. Local study-map skill 5.2 (Pipeline Orchestration Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Ray fits a Python-native distributed workload that is not a container-per-step pipeline. Why the correct answer wins: Pipelines runs each step as a container with caching, lineage, and retry.
- **B:** Incorrect for this question. Kubeflow pipelines give a container-per-step pipeline that runs on the managed service or on GKE. Why the correct answer wins: Pipelines runs each step as a container with caching, lineage, and retry.
- **C:** Correct. In this case: Pipelines runs each step as a container with caching, lineage, and retry.
- **D:** Incorrect for this question. Airflow expresses cross-system dependencies and schedules outside the ML platform. Why the correct answer wins: Pipelines runs each step as a container with caching, lineage, and retry.

### Question 74 — C

Answer: Orchestrate with Managed Service for Apache Airflow. Airflow expresses cross-system dependencies and schedules outside the ML platform. Local study-map skill 5.2 (Pipeline Orchestration Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Pipelines runs each step as a container with caching, lineage, and retry. Why the correct answer wins: Airflow expresses cross-system dependencies and schedules outside the ML platform.
- **B:** Incorrect for this question. Kubeflow pipelines give a container-per-step pipeline that runs on the managed service or on GKE. Why the correct answer wins: Airflow expresses cross-system dependencies and schedules outside the ML platform.
- **C:** Correct. In this case: Airflow expresses cross-system dependencies and schedules outside the ML platform.
- **D:** Incorrect for this question. Ray fits a Python-native distributed workload that is not a container-per-step pipeline. Why the correct answer wins: Airflow expresses cross-system dependencies and schedules outside the ML platform.

### Question 75 — B

Answer: Trigger the build and deploy from Cloud Build. Cloud Build runs the pipeline steps with recorded provenance. Local study-map skill 5.2 (Pipeline Orchestration Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The scheduler starts the pipeline on the cadence the retraining policy defines. Why the correct answer wins: Cloud Build runs the pipeline steps with recorded provenance.
- **B:** Correct. In this case: Cloud Build runs the pipeline steps with recorded provenance.
- **C:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: Cloud Build runs the pipeline steps with recorded provenance.
- **D:** Incorrect for this question. Pipelines runs each step as a container with caching, lineage, and retry. Why the correct answer wins: Cloud Build runs the pipeline steps with recorded provenance.

### Question 76 — B

Answer: Add a Cloud Scheduler trigger to the pipeline. The scheduler starts the pipeline on the cadence the policy defines. Local study-map skill 5.2 (Pipeline Orchestration Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Manual retraining leaves the model stale whenever the trigger is forgotten. Why the correct answer wins: The scheduler starts the pipeline on the cadence the policy defines.
- **B:** Correct. In this case: The scheduler starts the pipeline on the cadence the policy defines.
- **C:** Incorrect for this question. An event trigger retrains when data lands instead of on a fixed clock. Why the correct answer wins: The scheduler starts the pipeline on the cadence the policy defines.
- **D:** Incorrect for this question. Ray fits a Python-native distributed workload that is not a container-per-step pipeline. Why the correct answer wins: The scheduler starts the pipeline on the cadence the policy defines.

### Question 77 — D

Answer: Share one transformation library between training and serving. Shared code removes the class of bug where the two paths compute a feature differently. Local study-map skill 5.3 (Train and Serve Consistency), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Feature Store keeps one definition that both training and serving read. Why the correct answer wins: Shared code removes the class of bug where the two paths compute a feature differently.
- **B:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: Shared code removes the class of bug where the two paths compute a feature differently.
- **C:** Incorrect for this question. Preprocessing inside the artifact cannot drift between the two paths. Why the correct answer wins: Shared code removes the class of bug where the two paths compute a feature differently.
- **D:** Correct. In this case: Shared code removes the class of bug where the two paths compute a feature differently.

### Question 78 — A, E

Answers: Register the feature in Agent Platform Feature Store; Read the historical features from the offline store. The offline store returns point-in-time values, and Feature Store keeps one definition. Feature Store keeps one definition that both training and serving read. The offline store returns point-in-time values for training. Local study-map skill 5.3 (Train and Serve Consistency), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. Feature Store keeps one definition that both training and serving read. In this case: The offline store returns point-in-time values, and Feature Store keeps one definition.
- **B:** Incorrect for this question. The registry versions the model artifact and links it to its lineage and metrics. Why the correct answer wins: The offline store returns point-in-time values, and Feature Store keeps one definition.
- **C:** Incorrect for this question. In-memory processing is the simplest option and stops working once the data exceeds the worker memory. Why the correct answer wins: The offline store returns point-in-time values, and Feature Store keeps one definition.
- **D:** Incorrect for this question. Deduplicating at ingest stops duplicated records inflating the training set. Why the correct answer wins: The offline store returns point-in-time values, and Feature Store keeps one definition.
- **E:** Correct. The offline store returns point-in-time values for training. In this case: The offline store returns point-in-time values, and Feature Store keeps one definition.

### Question 79 — B

Answer: Enable step caching. Caching skips an unchanged step on a rerun. Local study-map skill 5.3 (Train and Serve Consistency), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The gate promotes a model only when it beats the incumbent on the agreed metric. Why the correct answer wins: Caching skips an unchanged step on a rerun.
- **B:** Correct. In this case: Caching skips an unchanged step on a rerun.
- **C:** Incorrect for this question. Drift-triggered retraining responds to change instead of to the calendar. Why the correct answer wins: Caching skips an unchanged step on a rerun.
- **D:** Incorrect for this question. A validation step stops a bad batch before it reaches training. Why the correct answer wins: Caching skips an unchanged step on a rerun.

### Question 80 — B

Answer: Serve the feature from the online store. The online store returns the latest value at low latency. Local study-map skill 5.3 (Train and Serve Consistency), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The offline store returns point-in-time values for training. Why the correct answer wins: The online store returns the latest value at low latency.
- **B:** Correct. In this case: The online store returns the latest value at low latency.
- **C:** Incorrect for this question. A crossed feature lets a linear model express the interaction it cannot learn alone. Why the correct answer wins: The online store returns the latest value at low latency.
- **D:** Incorrect for this question. Feature monitoring reports distribution changes per feature, not just per model. Why the correct answer wins: The online store returns the latest value at low latency.

### Question 81 — D

Answer: Retrain when the production metric drops. Metric-triggered retraining reacts to actual quality loss. Local study-map skill 5.4 (Retraining Policy), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A fixed schedule is simple to reason about when the data changes predictably. Why the correct answer wins: Metric-triggered retraining reacts to actual quality loss.
- **B:** Incorrect for this question. Drift-triggered retraining responds to change instead of to the calendar. Why the correct answer wins: Metric-triggered retraining reacts to actual quality loss.
- **C:** Incorrect for this question. Manual retraining leaves the model stale whenever the trigger is forgotten. Why the correct answer wins: Metric-triggered retraining reacts to actual quality loss.
- **D:** Correct. In this case: Metric-triggered retraining reacts to actual quality loss.

### Question 82 — C

Answer: Retrain when drift crosses the threshold. Drift-triggered retraining responds to change instead of to the calendar. Local study-map skill 5.4 (Retraining Policy), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Manual retraining leaves the model stale whenever the trigger is forgotten. Why the correct answer wins: Drift-triggered retraining responds to change instead of to the calendar.
- **B:** Incorrect for this question. A fixed schedule is simple to reason about when the data changes predictably. Why the correct answer wins: Drift-triggered retraining responds to change instead of to the calendar.
- **C:** Correct. In this case: Drift-triggered retraining responds to change instead of to the calendar.
- **D:** Incorrect for this question. Metric-triggered retraining reacts to actual quality loss. Why the correct answer wins: Drift-triggered retraining responds to change instead of to the calendar.

### Question 83 — B

Answer: Extend CI/CD into continuous training. Continuous training adds the retrain and validate step to the same pipeline. Local study-map skill 5.4 (Retraining Policy), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. An event trigger retrains when data lands instead of on a fixed clock. Why the correct answer wins: Continuous training adds the retrain and validate step to the same pipeline.
- **B:** Correct. In this case: Continuous training adds the retrain and validate step to the same pipeline.
- **C:** Incorrect for this question. Manual retraining leaves the model stale whenever the trigger is forgotten. Why the correct answer wins: Continuous training adds the retrain and validate step to the same pipeline.
- **D:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: Continuous training adds the retrain and validate step to the same pipeline.

### Question 84 — A

Answer: Trigger the pipeline from the arrival of new data. An event trigger retrains when data lands instead of on a fixed clock. Local study-map skill 5.5 (CI/CD/CT with Cloud Build), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: An event trigger retrains when data lands instead of on a fixed clock.
- **B:** Incorrect for this question. The scheduler starts the pipeline on the cadence the retraining policy defines. Why the correct answer wins: An event trigger retrains when data lands instead of on a fixed clock.
- **C:** Incorrect for this question. Manual retraining leaves the model stale whenever the trigger is forgotten. Why the correct answer wins: An event trigger retrains when data lands instead of on a fixed clock.
- **D:** Incorrect for this question. Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance. Why the correct answer wins: An event trigger retrains when data lands instead of on a fixed clock.

### Question 85 — D

Answer: Gate the deployment on a model evaluation threshold. The gate promotes a model only when it beats the incumbent. Local study-map skill 5.5 (CI/CD/CT with Cloud Build), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A validation step stops a bad batch before it reaches training. Why the correct answer wins: The gate promotes a model only when it beats the incumbent.
- **B:** Incorrect for this question. Drift-triggered retraining responds to change instead of to the calendar. Why the correct answer wins: The gate promotes a model only when it beats the incumbent.
- **C:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: The gate promotes a model only when it beats the incumbent.
- **D:** Correct. In this case: The gate promotes a model only when it beats the incumbent.

### Question 86 — B

Answer: Retrain on a fixed schedule. A fixed schedule is simple to reason about when the data changes predictably. Local study-map skill 5.5 (CI/CD/CT with Cloud Build), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Drift-triggered retraining responds to change instead of to the calendar. Why the correct answer wins: A fixed schedule is simple to reason about when the data changes predictably.
- **B:** Correct. In this case: A fixed schedule is simple to reason about when the data changes predictably.
- **C:** Incorrect for this question. Metric-triggered retraining reacts to actual quality loss. Why the correct answer wins: A fixed schedule is simple to reason about when the data changes predictably.
- **D:** Incorrect for this question. Manual retraining leaves the model stale whenever the trigger is forgotten. Why the correct answer wins: A fixed schedule is simple to reason about when the data changes predictably.

### Question 87 — C

Answer: Use Ray on Agent Platform for the distributed compute. Ray fits a Python-native distributed workload that is not a container-per-step pipeline. Local study-map skill 5.2 (Pipeline Orchestration Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Airflow expresses cross-system dependencies and schedules outside the ML platform. Why the correct answer wins: Ray fits a Python-native distributed workload that is not a container-per-step pipeline.
- **B:** Incorrect for this question. Kubeflow pipelines give a container-per-step pipeline that runs on the managed service or on GKE. Why the correct answer wins: Ray fits a Python-native distributed workload that is not a container-per-step pipeline.
- **C:** Correct. In this case: Ray fits a Python-native distributed workload that is not a container-per-step pipeline.
- **D:** Incorrect for this question. Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance. Why the correct answer wins: Ray fits a Python-native distributed workload that is not a container-per-step pipeline.

### Question 88 — D, E

Answers: Screen the prompts and responses with Model Armor; Configure the model safety filters. Model Armor detects jailbreak attempts, and the safety filters block harmful output. Model Armor detects prompt injection, jailbreak attempts, and unsafe content. Safety filters block categories of harmful output at the model call. Local study-map skill 6.1 (Secure AI and Prompt Protection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A system instruction states what the assistant must refuse, though it is not a security control on its own. Why the correct answer wins: Model Armor detects jailbreak attempts, and the safety filters block harmful output.
- **B:** Incorrect for this question. A regex removes a known identifier pattern before the prompt leaves the service. Why the correct answer wins: Model Armor detects jailbreak attempts, and the safety filters block harmful output.
- **C:** Incorrect for this question. A schema stops the model returning free text that downstream code cannot parse. Why the correct answer wins: Model Armor detects jailbreak attempts, and the safety filters block harmful output.
- **D:** Correct. Model Armor detects prompt injection, jailbreak attempts, and unsafe content. In this case: Model Armor detects jailbreak attempts, and the safety filters block harmful output.
- **E:** Correct. Safety filters block categories of harmful output at the model call. In this case: Model Armor detects jailbreak attempts, and the safety filters block harmful output.

### Question 89 — B

Answer: Constrain the response to a JSON schema. A schema stops the model returning free text that downstream code cannot parse. Local study-map skill 6.1 (Secure AI and Prompt Protection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A system instruction states what the assistant must refuse, though it is not a security control on its own. Why the correct answer wins: A schema stops the model returning free text that downstream code cannot parse.
- **B:** Correct. In this case: A schema stops the model returning free text that downstream code cannot parse.
- **C:** Incorrect for this question. Safety filters block categories of harmful output at the model call. Why the correct answer wins: A schema stops the model returning free text that downstream code cannot parse.
- **D:** Incorrect for this question. Model Armor detects prompt injection, jailbreak attempts, and unsafe content. Why the correct answer wins: A schema stops the model returning free text that downstream code cannot parse.

### Question 90 — A

Answer: Redact the pattern-matchable fields with a regex. A regex removes a known identifier pattern before the prompt leaves the service. Local study-map skill 6.1 (Secure AI and Prompt Protection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: A regex removes a known identifier pattern before the prompt leaves the service.
- **B:** Incorrect for this question. A system instruction states what the assistant must refuse, though it is not a security control on its own. Why the correct answer wins: A regex removes a known identifier pattern before the prompt leaves the service.
- **C:** Incorrect for this question. Model Armor detects prompt injection, jailbreak attempts, and unsafe content. Why the correct answer wins: A regex removes a known identifier pattern before the prompt leaves the service.
- **D:** Incorrect for this question. A schema stops the model returning free text that downstream code cannot parse. Why the correct answer wins: A regex removes a known identifier pattern before the prompt leaves the service.

### Question 91 — B

Answer: Monitor the outcome rate across the protected groups. A per-group outcome rate is the first evidence of disparate impact. Local study-map skill 6.2 (Responsible AI and Bias), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The card records provenance, intended use, and known gaps for the dataset. Why the correct answer wins: A per-group outcome rate is the first evidence of disparate impact.
- **B:** Correct. In this case: A per-group outcome rate is the first evidence of disparate impact.
- **C:** Incorrect for this question. A sliced metric shows a gap that the aggregate metric hides. Why the correct answer wins: A per-group outcome rate is the first evidence of disparate impact.
- **D:** Incorrect for this question. The card states where the model may be used and where it must not. Why the correct answer wins: A per-group outcome rate is the first evidence of disparate impact.

### Question 92 — C

Answer: Slice the evaluation metrics by the sensitive attribute. A sliced metric shows a gap that the aggregate hides. Local study-map skill 6.2 (Responsible AI and Bias), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A per-group outcome rate is the first evidence of disparate impact. Why the correct answer wins: A sliced metric shows a gap that the aggregate hides.
- **B:** Incorrect for this question. The card records provenance, intended use, and known gaps for the dataset. Why the correct answer wins: A sliced metric shows a gap that the aggregate hides.
- **C:** Correct. In this case: A sliced metric shows a gap that the aggregate hides.
- **D:** Incorrect for this question. The card states where the model may be used and where it must not. Why the correct answer wins: A sliced metric shows a gap that the aggregate hides.

### Question 93 — A

Answer: Use integrated gradients for the image model. Integrated gradients attributes an image prediction to the pixels that moved it. Local study-map skill 6.3 (Explainability), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Integrated gradients attributes an image prediction to the pixels that moved it.
- **B:** Incorrect for this question. Shapley values attribute a prediction to its features with a consistent baseline. Why the correct answer wins: Integrated gradients attributes an image prediction to the pixels that moved it.
- **C:** Incorrect for this question. ML.GLOBAL_EXPLAIN ranks the features that matter most across the whole model. Why the correct answer wins: Integrated gradients attributes an image prediction to the pixels that moved it.
- **D:** Incorrect for this question. Sampled Shapley explains individual online predictions with a bounded compute cost. Why the correct answer wins: Integrated gradients attributes an image prediction to the pixels that moved it.

### Question 94 — D

Answer: Publish a model card with the intended use and limits. The card states where the model may be used and where it must not. Local study-map skill 6.3 (Explainability), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Attribution shows which inputs drove the decision in the case the reviewer is examining. Why the correct answer wins: The card states where the model may be used and where it must not.
- **B:** Incorrect for this question. A linear or tree model can be read directly when regulation demands an explanation by construction. Why the correct answer wins: The card states where the model may be used and where it must not.
- **C:** Incorrect for this question. The card records provenance, intended use, and known gaps for the dataset. Why the correct answer wins: The card states where the model may be used and where it must not.
- **D:** Correct. In this case: The card states where the model may be used and where it must not.

### Question 95 — B

Answer: Enable Model Monitoring on the endpoint. Model Monitoring compares live traffic with the training baseline. Local study-map skill 6.4 (Model Monitoring Configuration), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A percentile latency per version shows a regression that an average hides. Why the correct answer wins: Model Monitoring compares live traffic with the training baseline.
- **B:** Correct. In this case: Model Monitoring compares live traffic with the training baseline.
- **C:** Incorrect for this question. The threshold expresses how much drift the business can absorb before someone acts. Why the correct answer wins: Model Monitoring compares live traffic with the training baseline.
- **D:** Incorrect for this question. An alert with no owner is a dashboard nobody reads. Why the correct answer wins: Model Monitoring compares live traffic with the training baseline.

### Question 96 — A

Answer: Route the monitoring alert to the owning team. An alert with no owner is a dashboard nobody reads. Local study-map skill 6.4 (Model Monitoring Configuration), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: An alert with no owner is a dashboard nobody reads.
- **B:** Incorrect for this question. Redacted logs make a bad answer diagnosable without storing sensitive text. Why the correct answer wins: An alert with no owner is a dashboard nobody reads.
- **C:** Incorrect for this question. Continuous sampling catches quality regressions that drift metrics cannot see. Why the correct answer wins: An alert with no owner is a dashboard nobody reads.
- **D:** Incorrect for this question. The threshold expresses how much drift the business can absorb before someone acts. Why the correct answer wins: An alert with no owner is a dashboard nobody reads.

### Question 97 — A, C

Answers: Watch for data drift; Watch the prediction distribution. Data drift is a change in the input distribution, and a shift in the output distribution is an early symptom. Data drift is a change in the input distribution after the model shipped. A shift in the output distribution is often the first visible symptom. Local study-map skill 6.5 (Skew and Drift Types), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. A shift in the output distribution is often the first visible symptom. In this case: Data drift is a change in the input distribution, and a shift in the output distribution is an early symptom.
- **B:** Incorrect for this question. Attribution drift is a change in which features drive the prediction. Why the correct answer wins: Data drift is a change in the input distribution, and a shift in the output distribution is an early symptom.
- **C:** Correct. Data drift is a change in the input distribution after the model shipped. In this case: Data drift is a change in the input distribution, and a shift in the output distribution is an early symptom.
- **D:** Incorrect for this question. Without the labelled outcome, quality can only be inferred from the inputs and outputs. Why the correct answer wins: Data drift is a change in the input distribution, and a shift in the output distribution is an early symptom.
- **E:** Incorrect for this question. Concept drift is a change in the relationship between the features and the target. Why the correct answer wins: Data drift is a change in the input distribution, and a shift in the output distribution is an early symptom.

### Question 98 — B

Answer: Watch for training-serving skew. Skew compares the live feature distribution with the training distribution. Local study-map skill 6.5 (Skew and Drift Types), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Data drift is a change in the input distribution after the model shipped. Why the correct answer wins: Skew compares the live feature distribution with the training distribution.
- **B:** Correct. In this case: Skew compares the live feature distribution with the training distribution.
- **C:** Incorrect for this question. Concept drift is a change in the relationship between the features and the target. Why the correct answer wins: Skew compares the live feature distribution with the training distribution.
- **D:** Incorrect for this question. Attribution drift is a change in which features drive the prediction. Why the correct answer wins: Skew compares the live feature distribution with the training distribution.

### Question 99 — B

Answer: Log the prompt and response with redaction. Redacted logs make a bad answer diagnosable without storing sensitive text. Local study-map skill 6.6 (Generative AI Monitoring), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Token accounting attributes generative cost to the feature that caused it. Why the correct answer wins: Redacted logs make a bad answer diagnosable without storing sensitive text.
- **B:** Correct. In this case: Redacted logs make a bad answer diagnosable without storing sensitive text.
- **C:** Incorrect for this question. A percentile latency per version shows a regression that an average hides. Why the correct answer wins: Redacted logs make a bad answer diagnosable without storing sensitive text.
- **D:** Incorrect for this question. Model Monitoring compares live traffic with the training baseline and reports skew and drift. Why the correct answer wins: Redacted logs make a bad answer diagnosable without storing sensitive text.

### Question 100 — C

Answer: Score a sample of live answers with the evaluation rubric. Continuous sampling catches quality regressions that drift metrics cannot see. Local study-map skill 6.6 (Generative AI Monitoring), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Token accounting attributes generative cost to the feature that caused it. Why the correct answer wins: Continuous sampling catches quality regressions that drift metrics cannot see.
- **B:** Incorrect for this question. A percentile latency per version shows a regression that an average hides. Why the correct answer wins: Continuous sampling catches quality regressions that drift metrics cannot see.
- **C:** Correct. In this case: Continuous sampling catches quality regressions that drift metrics cannot see.
- **D:** Incorrect for this question. Model Monitoring compares live traffic with the training baseline and reports skew and drift. Why the correct answer wins: Continuous sampling catches quality regressions that drift metrics cannot see.
