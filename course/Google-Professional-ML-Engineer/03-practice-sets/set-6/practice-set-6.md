# Google Cloud Professional Machine Learning Engineer — Full-Length Mock Exam 6

Professional Machine Learning Engineer · 100 questions · expanded practice bank · passing score not published

Blueprint-weighted mock exam. Item mix: 84 multiple-choice and 16 multiple-select items (the selection count is stated in each multi-select stem). The live exam publishes 50-60 multiple-choice and multiple-select questions and has no case-study component, so this set is larger on purpose and no case-study or drag-and-drop item is reproduced. See the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Google exam items.

## Questions

---

## Domain 1 — Architecting low-code AI solutions (Low-Code AI and Foundational Models)

### 1. A subscription team must predict whether a trial converts, in SQL. What should be built?

- A. Create a BigQuery ML linear regression model
- B. Create a BigQuery ML logistic regression model
- C. Create a BigQuery ML boosted tree classifier
- D. Create a BigQuery ML k-means model

### 2. Customers must be segmented first, then each segment scored with its own model. Which two steps apply? Select two.

- A. Create a BigQuery ML k-means model
- B. Import the TensorFlow model into BigQuery ML
- C. Create a BigQuery ML logistic regression model
- D. Store the predictions in a nested JSON column
- E. Score the rows with ML.PREDICT

### 3. A model owner must show precision and recall on the holdout. What should be used?

- A. Read the contribution of each feature with ML.EXPLAIN_PREDICT
- B. Inspect the metrics with ML.EVALUATE
- C. Declare the feature transformations in the TRANSFORM clause
- D. Score the rows with ML.PREDICT

### 4. The caller must not have to prepare features correctly before scoring. What should be used?

- A. Summarise the model with ML.GLOBAL_EXPLAIN
- B. Score the rows with ML.PREDICT
- C. Declare the feature transformations in the TRANSFORM clause
- D. Inspect the metrics with ML.EVALUATE

### 5. Three AutoML experiments must share one node-hour budget. What should be configured?

- A. Let AutoML choose the data split
- B. Use AutoML so the team needs no modelling code
- C. Export the AutoML model as an artifact
- D. Set a training budget in node hours

### 6. A business analyst with no modelling background must train a classifier. What should be used?

- A. Set a training budget in node hours
- B. Train an Agent Platform AutoML tabular model
- C. Export the AutoML model as an artifact
- D. Use AutoML so the team needs no modelling code

### 7. Customer feedback must be classified in place, inside the warehouse. What should be used?

- A. Create the Cloud resource connection for the remote model
- B. Fine-tune a Gemini model from BigQuery
- C. Import the TensorFlow model into BigQuery ML
- D. Create a BigQuery ML remote model over Gemini

### 8. A low-volume legal analysis task needs the best reasoning quality. What should be used?

- A. Deploy an open-weight model from Model Garden
- B. Embed the documents with the text embedding model
- C. Choose the smaller Gemini model for latency and cost
- D. Choose the larger Gemini model for quality

### 9. Scanned tax forms must yield structured fields with layout awareness. What should be used?

- A. Use Document AI with a specialised processor
- B. Use the Speech-to-Text API
- C. Use the Natural Language API
- D. Use the Vision API

### 10. Recorded site footage must be scanned for shots and explicit content. What should be used?

- A. Use Document AI with a specialised processor
- B. Use the Vision API
- C. Use the Video Intelligence API
- D. Use the Translation API

### 11. A long shared policy is resent every call, and answers are often unsupported. Which two changes help? Select two.

- A. Request a quota increase for the model
- B. Ground the answer in retrieved documents
- C. Cache the long shared context
- D. Choose the larger Gemini model for quality
- E. Stream the response tokens to the client

### 12. A user-facing assistant returns resource-exhausted errors at peak. What should be added?

- A. Request a quota increase for the model
- B. Call the model in the region that serves the users
- C. Fall back to a smaller model when the primary is throttled
- D. Choose the larger Gemini model for quality

---

## Domain 2 — Collaborating within and across teams to manage data and models (Data, Features, Notebooks, and Experiments)

### 13. A 2 TB table must be aggregated where it already lives. What should be used?

- A. Preprocess in memory with pandas
- B. Preprocess with Spark on Dataproc
- C. Preprocess with a Dataflow pipeline
- D. Preprocess in BigQuery with SQL

### 14. An events dataset holds identifiers, and the model must not learn from the future. Which two steps apply? Select two.

- A. De-identify the fields with Sensitive Data Protection
- B. Let AutoML choose the data split
- C. Split the data by time rather than at random
- D. Drop the identifier columns before the training dataset is written
- E. Add a crossed feature for the interacting pair

### 15. A 500 MB extract must be explored in a notebook. What should be used?

- A. Preprocess with a Dataflow pipeline
- B. Preprocess in memory with pandas
- C. Preprocess in BigQuery with SQL
- D. Preprocess with Spark on Dataproc

### 16. A latency-sensitive lookup must return one customer's value inside the request. What should be read?

- A. Read the historical features from the offline store
- B. Add a crossed feature for the interacting pair
- C. Serve the feature from the online store
- D. Enable feature monitoring on the feature group

### 17. Two categorical fields interact and the model is linear. What should be added?

- A. Add a crossed feature for the interacting pair
- B. Bucketize the continuous feature
- C. Normalise the numeric feature before training
- D. Register the feature in Agent Platform Feature Store

### 18. A join key must remain usable but not reversible. What should be done?

- A. Drop the identifier columns before the training dataset is written
- B. Hash the identifiers with a salted key before training
- C. Restrict the raw bucket to a privileged service account
- D. De-identify the fields with Sensitive Data Protection

### 19. Only the training identity may touch the raw export. What should be applied?

- A. Drop the identifier columns before the training dataset is written
- B. Hash the identifiers with a salted key before training
- C. De-identify the fields with Sensitive Data Protection
- D. Restrict the raw bucket to a privileged service account

### 20. A team must run notebooks with project IAM and no VM to patch. What should be used?

- A. Pin the runtime to a custom container image
- B. Create the runtime with no public IP
- C. Use an Agent Platform Workbench instance
- D. Use Colab Enterprise

### 21. A runtime in a private subnet must still read the governed tables. What should be done?

- A. Use an Agent Platform Workbench instance
- B. Create the runtime with no public IP
- C. Attach the runtime to the shared VPC subnet
- D. Set an idle shutdown schedule

### 22. Identical code produces different scores on every rerun. What should be added?

- A. Set the random seed in the training code
- B. Compare the runs on the validation metric
- C. Log the run to Agent Platform Experiments
- D. Track artifacts and lineage in ML Metadata

### 23. A lead must compare metrics and parameters across forty runs. What should be used?

- A. Track artifacts and lineage in ML Metadata
- B. Set the random seed in the training code
- C. Enable step caching
- D. Log the run to Agent Platform Experiments

### 24. A container-per-step workflow must run on the managed service and also on GKE. Which two choices fit? Select two.

- A. Use Ray on Agent Platform for the distributed compute
- B. Log the run to Agent Platform Experiments
- C. Orchestrate with Managed Service for Apache Airflow
- D. Express the workflow as a Kubeflow pipeline
- E. Orchestrate the steps in Agent Platform Pipelines

### 25. A first pipeline must follow the validated step order. What should be used?

- A. Use Ray on Agent Platform for the distributed compute
- B. Start from a Google-provided pipeline template
- C. Orchestrate with Managed Service for Apache Airflow
- D. Express the workflow as a Kubeflow pipeline

### 26. A fraud model faces rare positives, and the operating threshold must be chosen. Which two metrics help? Select two.

- A. Report precision-recall AUC for the rare class
- B. Report RMSE for the regression target
- C. Report MAPE when the error must be read as a percentage
- D. Report ROC AUC
- E. Inspect the confusion matrix at the operating threshold

### 27. Thousands of generated answers must be scored for helpfulness at scale. What should be used?

- A. Measure groundedness against the retrieved context
- B. Score the answers with an LLM-as-a-judge rubric
- C. Sample the answers for expert human review
- D. Measure the safety metrics on a fixed prompt set

### 28. A dataset and code commit must be linked to the artifact under audit. What should be recorded?

- A. Register the model in Agent Platform Model Registry
- B. Enable step caching
- C. Track artifacts and lineage in ML Metadata
- D. Log the run to Agent Platform Experiments

---

## Domain 3 — Scaling prototypes into ML models (Training at Scale and Model Choice)

### 29. A summarisation task has few labels and open-ended output. What model type fits?

- A. Choose a classical time series model
- B. Use TabNet as the custom training algorithm
- C. Choose a foundation model
- D. Choose a deep neural network

### 30. A large tabular dataset has complex interactions and no interpretability mandate. What model type fits?

- A. Choose a deep neural network
- B. Choose a foundation model
- C. Use TabNet as the custom training algorithm
- D. Choose a classical time series model

### 31. A warehouse must score a 1 TB table hourly with no new stack. What should be used?

- A. Build the model in BigQuery ML
- B. Train with Agent Platform AutoML
- C. Train a custom model on Agent Platform
- D. Use TabNet as the custom training algorithm

### 32. A small team with labelled data must ship a managed model quickly. What should be used?

- A. Train with Agent Platform AutoML
- B. Build the model in BigQuery ML
- C. Use TabNet as the custom training algorithm
- D. Train a custom model on Agent Platform

### 33. A risky change must be measured on live traffic invisibly, then exposed to one per cent. Which two strategies apply? Select two.

- A. Deploy blue/green with an instant switch
- B. Roll out a canary with a small traffic share
- C. Run the new model in shadow mode
- D. Split traffic between two models in an A/B test
- E. Replace the model version in place

### 34. The previous version must be restored instantly during a launch. What strategy is described?

- A. Deploy blue/green with an instant switch
- B. Replace the model version in place
- C. Run the new model in shadow mode
- D. Roll out a canary with a small traffic share

### 35. A lending console must explain a decline at the moment the applicant waits. What should be used?

- A. Use sampled Shapley on the endpoint
- B. Use integrated gradients for the image model
- C. Summarise the model with ML.GLOBAL_EXPLAIN
- D. Explain with Shapley values

### 36. A reviewer wants the features that matter most across a BigQuery ML model. What should be used?

- A. Read the contribution of each feature with ML.EXPLAIN_PREDICT
- B. Explain with Shapley values
- C. Use sampled Shapley on the endpoint
- D. Summarise the model with ML.GLOBAL_EXPLAIN

### 37. A distributed trainer must stream shards efficiently. What format should be used?

- A. Write the training data as Parquet in Cloud Storage
- B. Read the training data directly from BigQuery
- C. Stream the new records through Dataflow into the training store
- D. Write the training data as TFRecord shards in Cloud Storage

### 38. Late-arriving events must appear in the training store before the next run starts. What should be used?

- A. Write the training data as TFRecord shards in Cloud Storage
- B. Write the training data as Parquet in Cloud Storage
- C. Stream the new records through Dataflow into the training store
- D. Read the training data directly from BigQuery

### 39. Retried events double-count and inflate the dataset. What should be added?

- A. Write the training data as Parquet in Cloud Storage
- B. Deduplicate on the event key in the ingestion step
- C. Stream the new records through Dataflow into the training store
- D. Validate the schema and quarantine rejected rows

### 40. A type change upstream must be quarantined rather than trained on. What should be added?

- A. Validate the schema and quarantine rejected rows
- B. Deduplicate on the event key in the ingestion step
- C. Stream the new records through Dataflow into the training store
- D. Read the training data directly from BigQuery

### 41. A trainer needs a pinned framework build and a system library. What should be used?

- A. Use a prebuilt serving container
- B. Export the AutoML model as an artifact
- C. Run a custom container on Agent Platform
- D. Package the trainer as a Python package

### 42. A one-file trainer must run remotely without a Dockerfile. What should be used?

- A. Use a prebuilt serving container
- B. Run a custom container on Agent Platform
- C. Package the trainer as a Python package
- D. Train with Agent Platform AutoML

### 43. The trainer runs out of device memory part-way through. What should be tried first?

- A. Enable gradient checkpointing
- B. Request accelerator quota for the region
- C. Reduce the per-replica batch size
- D. Lower the learning rate

### 44. The same code scores differently on the remote trainer than on a laptop. What is the likely cause?

- A. Grant the training service account access to the bucket
- B. Lower the learning rate
- C. Request accelerator quota for the region
- D. Pin the framework version in the container

### 45. Many trials must run, and most lose early. Which two choices apply? Select two.

- A. Enable early stopping of poor trials
- B. Run a hyperparameter tuning job
- C. Report the business metric from the trainer
- D. Cap the search with a trial count and a parallel budget
- E. Choose Bayesian optimisation for the search

### 46. A search must end before a fixed date. What should be set?

- A. Run a hyperparameter tuning job
- B. Cap the search with a trial count and a parallel budget
- C. Enable early stopping of poor trials
- D. Choose Bayesian optimisation for the search

### 47. A house style must be learned with one accelerator available. What should be used?

- A. Fine-tune with a parameter-efficient adapter
- B. Ground the prompt with retrieval instead of fine-tuning
- C. Fine-tune the full model
- D. Distil the large model into a smaller one

### 48. A modest model must be trained cheaply for a few hours. What should be used?

- A. Serve on CPU only
- B. Serve on L4 GPUs
- C. Train on A100 GPUs
- D. Train on a TPU slice

### 49. The model does not fit on one device, and throughput must rise across the devices it does use. Which two choices apply? Select two.

- A. Configure the job as multi-worker with a chief
- B. Use model parallelism
- C. Use data parallelism
- D. Checkpoint to Cloud Storage and resume from the last step
- E. Scale the batch size with the worker count

---

## Domain 4 — Serving and scaling models (Serving, Packaging, and Scaling Endpoints)

### 50. A quarterly portfolio review must rescore every account. What should be used?

- A. Run batch prediction
- B. Batch the requests inside the client
- C. Deploy to an online endpoint
- D. Send the events to a streaming prediction path

### 51. A workload needs a per-click score and a per-event score as data arrives. Which two paths apply? Select two.

- A. Run batch prediction
- B. Attach a GPU to the serving replica
- C. Deploy to an online endpoint
- D. Send the events to a streaming prediction path
- E. Batch the requests inside the client

### 52. A client sends thousands of tiny payloads and pays per-call overhead on each. What should it do?

- A. Enable autoscaling on the endpoint
- B. Raise the concurrency per replica
- C. Run batch prediction
- D. Batch the requests inside the client

### 53. A Keras model must be deployed by a team with no serving code to maintain. What should be used?

- A. Push the serving image to Artifact Registry
- B. Add a custom prediction routine to the container
- C. Use a prebuilt serving container
- D. Attach a GPU to the serving replica

### 54. An image must be scanned before the endpoint pulls it. Where should it be stored?

- A. Use a prebuilt serving container
- B. Enable autoscaling on the endpoint
- C. Register the model in Agent Platform Model Registry
- D. Push the serving image to Artifact Registry

### 55. A catalogue must show versions with their metrics and lineage. What should be used?

- A. Track artifacts and lineage in ML Metadata
- B. Log the run to Agent Platform Experiments
- C. Push the serving image to Artifact Registry
- D. Register the model in Agent Platform Model Registry

### 56. Reverting a bad release must not require a new deployment. What should be used?

- A. Replace the model version in place
- B. Deploy the version and move the alias
- C. Register the model in Agent Platform Model Registry
- D. Split traffic between two deployed versions

### 57. Two models must be compared on equal populations, then limited to a small share. Which two strategies apply? Select two.

- A. Deploy blue/green with an instant switch
- B. Replace the model version in place
- C. Roll out a canary with a small traffic share
- D. Run the new model in shadow mode
- E. Split traffic between two models in an A/B test

### 58. A model must be scored on live traffic while users see nothing new. What strategy is described?

- A. Run the new model in shadow mode
- B. Roll out a canary with a small traffic share
- C. Split traffic between two models in an A/B test
- D. Replace the model version in place

### 59. A metric is defined in the batch job and again in the online service. What should be done?

- A. Enable step caching
- B. Deploy the version and move the alias
- C. Share one transformation library between training and serving
- D. Register the feature in Agent Platform Feature Store

### 60. A caller must not be trusted to apply the correct scaling before scoring. What should be done?

- A. Configure explanation metadata for the endpoint
- B. Keep the preprocessing inside the exported model
- C. Share one transformation library between training and serving
- D. Register the feature in Agent Platform Feature Store

### 61. Two workloads must not compete for the same serving capacity. What should be used?

- A. Deploy with a private endpoint only
- B. Use a dedicated endpoint
- C. Enable autoscaling on the endpoint
- D. Use a shared public endpoint

### 62. A model must have no public surface at all. What should be deployed?

- A. Use a shared public endpoint
- B. Deploy with a private endpoint only
- C. Attach a GPU to the serving replica
- D. Use a dedicated endpoint

### 63. A ranking model misses its 30 ms target on CPU. What should be used?

- A. Serve on CPU only
- B. Deploy to an Edge TPU device
- C. Raise the concurrency per replica
- D. Attach a GPU to the serving replica

### 64. A small model meets its latency budget comfortably without acceleration. What should be chosen?

- A. Serve on CPU only
- B. Deploy to an Edge TPU device
- C. Attach a GPU to the serving replica
- D. Serve on L4 GPUs

### 65. Traffic swings widely, and cost per request must fall. Which two settings apply? Select two.

- A. Enable autoscaling on the endpoint
- B. Batch the requests inside the client
- C. Raise the maximum replica count
- D. Set a minimum replica count
- E. Raise the concurrency per replica

### 66. A spike must not exceed the approved budget. What should be set?

- A. Raise the concurrency per replica
- B. Raise the maximum replica count
- C. Set a minimum replica count
- D. Attach a GPU to the serving replica

### 67. The first call after an idle period takes seconds. What should be set?

- A. Raise the maximum replica count
- B. Batch the requests inside the client
- C. Raise the concurrency per replica
- D. Set a minimum replica count

### 68. An endpoint must cut cost per request and return attributions. Which two changes apply? Select two.

- A. Set a minimum replica count
- B. Deploy the version and move the alias
- C. Configure explanation metadata for the endpoint
- D. Push the serving image to Artifact Registry
- E. Raise the concurrency per replica

### 69. A model copied from research needs 300 ms per call and the product contract is 80 ms. What should be changed?

- A. Raise the concurrency per replica
- B. Raise the maximum replica count
- C. Attach a GPU to the serving replica
- D. Batch the requests inside the client

---

## Domain 5 — Automating and orchestrating ML pipelines (Pipelines, Retraining, and CI/CD/CT)

### 70. A weekly candidate must be rejected unless it improves the current model. What should be added?

- A. Add an explicit data validation step
- B. Gate the deployment on a model evaluation threshold
- C. Retrain when drift crosses the threshold
- D. Enable step caching

### 71. A malformed batch must fail before training begins. What should be added?

- A. Add an explicit data validation step
- B. Enable step caching
- C. Validate the schema and quarantine rejected rows
- D. Gate the deployment on a model evaluation threshold

### 72. Model selection has already peeked at the final holdout, and the classes are unbalanced. Which two practices apply? Select two.

- A. Report MAPE when the error must be read as a percentage
- B. Report precision-recall AUC for the rare class
- C. Inspect the confusion matrix at the operating threshold
- D. Keep the test set out of every tuning decision
- E. Report ROC AUC

### 73. Every step must leave an artifact record that the next run can reuse. What should be used?

- A. Express the workflow as a Kubeflow pipeline
- B. Use Ray on Agent Platform for the distributed compute
- C. Orchestrate with Managed Service for Apache Airflow
- D. Orchestrate the steps in Agent Platform Pipelines

### 74. A chain must wait for a vendor file drop that no ML scheduler can see. What should orchestrate it?

- A. Trigger the build and deploy from Cloud Build
- B. Use Ray on Agent Platform for the distributed compute
- C. Orchestrate with Managed Service for Apache Airflow
- D. Orchestrate the steps in Agent Platform Pipelines

### 75. A sweep must run thousands of Python trials that pass state between them. What should be used?

- A. Orchestrate with Managed Service for Apache Airflow
- B. Use Ray on Agent Platform for the distributed compute
- C. Orchestrate the steps in Agent Platform Pipelines
- D. Express the workflow as a Kubeflow pipeline

### 76. The release process must be one recorded job instead of a runbook. What should be used?

- A. Enable step caching
- B. Trigger the build and deploy from Cloud Build
- C. Add a Cloud Scheduler trigger to the pipeline
- D. Retrain only on a manual request

### 77. A backfill and a live call must return the same value for the same entity. What should be used?

- A. Enable step caching
- B. Share one transformation library between training and serving
- C. Register the feature in Agent Platform Feature Store
- D. Keep the preprocessing inside the exported model

### 78. A historical rebuild and a live request must both get a value for the same entity. Which two read paths apply? Select two.

- A. Preprocess in memory with pandas
- B. Deduplicate on the event key in the ingestion step
- C. Read the historical features from the offline store
- D. Serve the feature from the online store
- E. Register the model in Agent Platform Model Registry

### 79. Rebuilding the feature step burns an hour although its inputs never moved. What should be enabled?

- A. Gate the deployment on a model evaluation threshold
- B. Enable step caching
- C. Retrain when drift crosses the threshold
- D. Add an explicit data validation step

### 80. The same column is derived twice and the two results disagree. What should be used?

- A. Deploy the version and move the alias
- B. Add an explicit data validation step
- C. Register the feature in Agent Platform Feature Store
- D. Share one transformation library between training and serving

### 81. The audit asks when the model is refreshed and expects a fixed answer. What policy fits?

- A. Retrain when the production metric drops
- B. Retrain on a fixed schedule
- C. Retrain when drift crosses the threshold
- D. Retrain only on a manual request

### 82. A supplier changes its pricing structure without notice and the monthly refresh lags. What policy fits?

- A. Retrain only on a manual request
- B. Retrain when the production metric drops
- C. Retrain on a fixed schedule
- D. Retrain when drift crosses the threshold

### 83. A model owner wants the pipeline to retrain and promote with no manual hand-off. What should be adopted?

- A. Enable step caching
- B. Trigger the pipeline from the arrival of new data
- C. Extend CI/CD into continuous training
- D. Retrain only on a manual request

### 84. A Pub/Sub message announcing new labels must begin the retrain. What should be used?

- A. Add a Cloud Scheduler trigger to the pipeline
- B. Trigger the pipeline from the arrival of new data
- C. Trigger the build and deploy from Cloud Build
- D. Retrain only on a manual request

### 85. A release must stop automatically when the acceptance metric regresses. What should the pipeline add?

- A. Retrain when drift crosses the threshold
- B. Add an explicit data validation step
- C. Gate the deployment on a model evaluation threshold
- D. Enable step caching

### 86. Dashboard accuracy fell two points while the inputs held steady. What policy fits?

- A. Retrain when drift crosses the threshold
- B. Retrain on a fixed schedule
- C. Retrain only on a manual request
- D. Retrain when the production metric drops

### 87. The team wants managed orchestration rather than a cluster it has to patch. What should be used?

- A. Orchestrate the steps in Agent Platform Pipelines
- B. Express the workflow as a Kubeflow pipeline
- C. Use Ray on Agent Platform for the distributed compute
- D. Orchestrate with Managed Service for Apache Airflow

---

## Domain 6 — Monitoring AI solutions (Responsible AI, Monitoring, and Drift)

### 88. A public assistant must resist injected instructions and must not echo account numbers. Which two controls apply? Select two.

- A. Constrain the response to a JSON schema
- B. Put the boundary in the system instruction
- C. Redact the pattern-matchable fields with a regex
- D. Configure the model safety filters
- E. Screen the prompts and responses with Model Armor

### 89. A children's app must block self-harm and sexual content by category. What should be configured?

- A. Configure the model safety filters
- B. Redact the pattern-matchable fields with a regex
- C. Constrain the response to a JSON schema
- D. Screen the prompts and responses with Model Armor

### 90. A downstream parser keeps failing on free-text replies. What should be configured?

- A. Configure the model safety filters
- B. Screen the prompts and responses with Model Armor
- C. Constrain the response to a JSON schema
- D. Put the boundary in the system instruction

### 91. Disparate error rates must be reported before a lending model is approved. What should be produced?

- A. Slice the evaluation metrics by the sensitive attribute
- B. Publish a model card with the intended use and limits
- C. Document the dataset with a data card
- D. Monitor the outcome rate across the protected groups

### 92. A second team wants to reuse the model for a different audience. What should be published?

- A. Publish a model card with the intended use and limits
- B. Monitor the outcome rate across the protected groups
- C. Slice the evaluation metrics by the sensitive attribute
- D. Document the dataset with a data card

### 93. A rejected part must show which pixels drove its defect score. What should be used?

- A. Use integrated gradients for the image model
- B. Summarise the model with ML.GLOBAL_EXPLAIN
- C. Use sampled Shapley on the endpoint
- D. Explain with Shapley values

### 94. A lender needs a scorecard whose points a regulator can audit line by line. What should be chosen?

- A. Report the feature attributions to the reviewer
- B. Choose an inherently interpretable model
- C. Explain with Shapley values
- D. Use sampled Shapley on the endpoint

### 95. Drift fires an alert that nobody receives. What should be added?

- A. Set the monitoring threshold from the acceptable error budget
- B. Track p95 latency per model version
- C. Route the monitoring alert to the owning team
- D. Score a sample of live answers with the evaluation rubric

### 96. A scoring service's live inputs must be measured against the training profile. What should be enabled?

- A. Route the monitoring alert to the owning team
- B. Log the prompt and response with redaction
- C. Enable Model Monitoring on the endpoint
- D. Track p95 latency per model version

### 97. A model is strong offline and weak on day one, and the live inputs have shifted. Which two conditions apply? Select two.

- A. Watch for data drift
- B. Watch for concept drift
- C. Watch for feature attribution drift
- D. Watch for training-serving skew
- E. Join the delayed ground truth back to the predictions

### 98. The relationship between the features and the target has changed. What is this called?

- A. Watch the prediction distribution
- B. Watch for feature attribution drift
- C. Watch for data drift
- D. Watch for concept drift

### 99. A prompt change must not silently degrade the answers users see. What should be added?

- A. Score a sample of live answers with the evaluation rubric
- B. Enable Model Monitoring on the endpoint
- C. Track tokens and cost per request
- D. Track p95 latency per model version

### 100. A known national identifier pattern must be masked in prompts by rule. What should be added?

- A. Redact the pattern-matchable fields with a regex
- B. Screen the prompts and responses with Model Armor
- C. Configure the model safety filters
- D. Constrain the response to a JSON schema

---

## Answer key and explanations

### Question 1 — B

Answer: Create a BigQuery ML logistic regression model. Logistic regression predicts a binary outcome and trains inside BigQuery. Local study-map skill 1.1 (BigQuery ML Model Building), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Linear regression predicts a continuous value such as revenue or demand. Why the correct answer wins: Logistic regression predicts a binary outcome and trains inside BigQuery.
- **B:** Correct. In this case: Logistic regression predicts a binary outcome and trains inside BigQuery.
- **C:** Incorrect for this question. Boosted trees capture non-linear interactions in tabular data while staying in SQL. Why the correct answer wins: Logistic regression predicts a binary outcome and trains inside BigQuery.
- **D:** Incorrect for this question. K-means segments rows into unsupervised clusters without a labelled target. Why the correct answer wins: Logistic regression predicts a binary outcome and trains inside BigQuery.

### Question 2 — A, E

Answers: Create a BigQuery ML k-means model; Score the rows with ML.PREDICT. K-means segments without a target, and ML.PREDICT scores the rows. K-means segments rows into unsupervised clusters without a labelled target. ML.PREDICT applies a trained model and returns the label and its probability. Local study-map skill 1.1 (BigQuery ML Model Building), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. K-means segments rows into unsupervised clusters without a labelled target. In this case: K-means segments without a target, and ML.PREDICT scores the rows.
- **B:** Incorrect for this question. Importing brings an already-trained model into BigQuery so SQL can score it. Why the correct answer wins: K-means segments without a target, and ML.PREDICT scores the rows.
- **C:** Incorrect for this question. Logistic regression predicts a binary outcome and trains inside BigQuery with SQL. Why the correct answer wins: K-means segments without a target, and ML.PREDICT scores the rows.
- **D:** Incorrect for this question. A nested column keeps per-row structured output such as labels and scores together. Why the correct answer wins: K-means segments without a target, and ML.PREDICT scores the rows.
- **E:** Correct. ML.PREDICT applies a trained model and returns the label and its probability. In this case: K-means segments without a target, and ML.PREDICT scores the rows.

### Question 3 — B

Answer: Inspect the metrics with ML.EVALUATE. ML.EVALUATE returns the model metrics against a labelled dataset. Local study-map skill 1.2 (BigQuery ML Feature Engineering and Prediction), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. ML.EXPLAIN_PREDICT attributes each prediction to the features that moved it. Why the correct answer wins: ML.EVALUATE returns the model metrics against a labelled dataset.
- **B:** Correct. In this case: ML.EVALUATE returns the model metrics against a labelled dataset.
- **C:** Incorrect for this question. TRANSFORM keeps preprocessing inside the model, so prediction applies the same steps. Why the correct answer wins: ML.EVALUATE returns the model metrics against a labelled dataset.
- **D:** Incorrect for this question. ML.PREDICT applies a trained model and returns the label and its probability. Why the correct answer wins: ML.EVALUATE returns the model metrics against a labelled dataset.

### Question 4 — C

Answer: Declare the feature transformations in the TRANSFORM clause. TRANSFORM keeps preprocessing inside the model so prediction applies it. Local study-map skill 1.2 (BigQuery ML Feature Engineering and Prediction), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. ML.GLOBAL_EXPLAIN ranks the features that matter most across the whole model. Why the correct answer wins: TRANSFORM keeps preprocessing inside the model so prediction applies it.
- **B:** Incorrect for this question. ML.PREDICT applies a trained model and returns the label and its probability. Why the correct answer wins: TRANSFORM keeps preprocessing inside the model so prediction applies it.
- **C:** Correct. In this case: TRANSFORM keeps preprocessing inside the model so prediction applies it.
- **D:** Incorrect for this question. ML.EVALUATE returns the model metrics against a labelled dataset. Why the correct answer wins: TRANSFORM keeps preprocessing inside the model so prediction applies it.

### Question 5 — D

Answer: Set a training budget in node hours. A node-hour budget caps how long AutoML searches. Local study-map skill 1.3 (Agent Platform AutoML), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. AutoML uses a reproducible default split when the dataset is large enough to do so. Why the correct answer wins: A node-hour budget caps how long AutoML searches.
- **B:** Incorrect for this question. AutoML is the no-code path, which matters when the team has data skills but no ML engineers. Why the correct answer wins: A node-hour budget caps how long AutoML searches.
- **C:** Incorrect for this question. Export produces a container-ready artifact that can be served outside the managed endpoint. Why the correct answer wins: A node-hour budget caps how long AutoML searches.
- **D:** Correct. In this case: A node-hour budget caps how long AutoML searches.

### Question 6 — D

Answer: Use AutoML so the team needs no modelling code. AutoML is the no-code path for teams with data skills and no ML engineers. AutoML is the no-code path, which matters when the team has data skills but no ML engineers. Local study-map skill 1.3 (Agent Platform AutoML), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A node-hour budget caps how long AutoML searches, which bounds the cost. Why the correct answer wins: AutoML is the no-code path for teams with data skills and no ML engineers.
- **B:** Incorrect for this question. AutoML tabular selects the architecture and tuning for a structured dataset. Why the correct answer wins: AutoML is the no-code path for teams with data skills and no ML engineers.
- **C:** Incorrect for this question. Export produces a container-ready artifact that can be served outside the managed endpoint. Why the correct answer wins: AutoML is the no-code path for teams with data skills and no ML engineers.
- **D:** Correct. AutoML is the no-code path, which matters when the team has data skills but no ML engineers. In this case: AutoML is the no-code path for teams with data skills and no ML engineers.

### Question 7 — D

Answer: Create a BigQuery ML remote model over Gemini. A remote model calls the Gemini endpoint from SQL where the data lives. Local study-map skill 1.4 (Gemini Fine-Tuning with BigQuery), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A remote model needs a connection and its service account before it can call an endpoint. Why the correct answer wins: A remote model calls the Gemini endpoint from SQL where the data lives.
- **B:** Incorrect for this question. Fine-tuning adapts a foundation model to the domain using rows that stay in BigQuery. Why the correct answer wins: A remote model calls the Gemini endpoint from SQL where the data lives.
- **C:** Incorrect for this question. Importing brings an already-trained model into BigQuery so SQL can score it. Why the correct answer wins: A remote model calls the Gemini endpoint from SQL where the data lives.
- **D:** Correct. In this case: A remote model calls the Gemini endpoint from SQL where the data lives.

### Question 8 — D

Answer: Choose the larger Gemini model for quality. The larger model gives the best reasoning quality at a higher cost per token. Local study-map skill 1.5 (Model Garden Model Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. An open-weight model can be tuned and self-hosted when a proprietary endpoint does not fit. Why the correct answer wins: The larger model gives the best reasoning quality at a higher cost per token.
- **B:** Incorrect for this question. Embeddings turn text into vectors, which is what a retrieval step searches. Why the correct answer wins: The larger model gives the best reasoning quality at a higher cost per token.
- **C:** Incorrect for this question. The smaller model answers faster and cheaper, which suits high-volume simple tasks. Why the correct answer wins: The larger model gives the best reasoning quality at a higher cost per token.
- **D:** Correct. In this case: The larger model gives the best reasoning quality at a higher cost per token.

### Question 9 — A

Answer: Use Document AI with a specialised processor. A Document AI processor extracts structured fields with layout awareness. Local study-map skill 1.6 (Industry AI APIs), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: A Document AI processor extracts structured fields with layout awareness.
- **B:** Incorrect for this question. The speech model transcribes audio, including domain phrases through adaptation. Why the correct answer wins: A Document AI processor extracts structured fields with layout awareness.
- **C:** Incorrect for this question. The Natural Language API returns entities, sentiment, and syntax without a custom model. Why the correct answer wins: A Document AI processor extracts structured fields with layout awareness.
- **D:** Incorrect for this question. The prebuilt Vision model labels, detects, and reads text without training a model. Why the correct answer wins: A Document AI processor extracts structured fields with layout awareness.

### Question 10 — C

Answer: Use the Video Intelligence API. Video Intelligence detects shots, labels, and explicit content. Local study-map skill 1.6 (Industry AI APIs), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A Document AI processor extracts structured fields from forms with layout awareness. Why the correct answer wins: Video Intelligence detects shots, labels, and explicit content.
- **B:** Incorrect for this question. The prebuilt Vision model labels, detects, and reads text without training a model. Why the correct answer wins: Video Intelligence detects shots, labels, and explicit content.
- **C:** Correct. In this case: Video Intelligence detects shots, labels, and explicit content.
- **D:** Incorrect for this question. The translation model handles a large language set without custom training. Why the correct answer wins: Video Intelligence detects shots, labels, and explicit content.

### Question 11 — B, C

Answers: Cache the long shared context; Ground the answer in retrieved documents. Caching bills the prefix once, and grounding reduces unsupported answers. Context caching bills the repeated prefix once instead of on every request. Grounding reduces unsupported answers and keeps the prompt short. Local study-map skill 1.7 (Gemini Application Optimization), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Throughput is capped by quota, so a quota ceiling cannot be solved by retries. Why the correct answer wins: Caching bills the prefix once, and grounding reduces unsupported answers.
- **B:** Correct. Grounding reduces unsupported answers and keeps the prompt short. In this case: Caching bills the prefix once, and grounding reduces unsupported answers.
- **C:** Correct. Context caching bills the repeated prefix once instead of on every request. In this case: Caching bills the prefix once, and grounding reduces unsupported answers.
- **D:** Incorrect for this question. The larger model gives the best reasoning quality at a higher cost per token. Why the correct answer wins: Caching bills the prefix once, and grounding reduces unsupported answers.
- **E:** Incorrect for this question. Streaming improves perceived latency without reducing total generation time. Why the correct answer wins: Caching bills the prefix once, and grounding reduces unsupported answers.

### Question 12 — C

Answer: Fall back to a smaller model when the primary is throttled. A fallback keeps the application answering when the primary is throttled. A fallback keeps the application answering when the primary model returns resource-exhausted. Local study-map skill 1.7 (Gemini Application Optimization), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 1 (architecting low-code AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Throughput is capped by quota, so a quota ceiling cannot be solved by retries. Why the correct answer wins: A fallback keeps the application answering when the primary is throttled.
- **B:** Incorrect for this question. A regional endpoint removes cross-region latency and satisfies residency rules. Why the correct answer wins: A fallback keeps the application answering when the primary is throttled.
- **C:** Correct. A fallback keeps the application answering when the primary model returns resource-exhausted. In this case: A fallback keeps the application answering when the primary is throttled.
- **D:** Incorrect for this question. The larger model gives the best reasoning quality at a higher cost per token. Why the correct answer wins: A fallback keeps the application answering when the primary is throttled.

### Question 13 — D

Answer: Preprocess in BigQuery with SQL. SQL over BigQuery is the cheapest option when the data already sits there. Local study-map skill 2.1 (Preprocessing Tool Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. In-memory processing is the simplest option and stops working once the data exceeds the worker memory. Why the correct answer wins: SQL over BigQuery is the cheapest option when the data already sits there.
- **B:** Incorrect for this question. Spark suits large transformations the team already has as Scala or PySpark code. Why the correct answer wins: SQL over BigQuery is the cheapest option when the data already sits there.
- **C:** Incorrect for this question. Dataflow runs the same Beam code in batch and streaming and scales without provisioning. Why the correct answer wins: SQL over BigQuery is the cheapest option when the data already sits there.
- **D:** Correct. In this case: SQL over BigQuery is the cheapest option when the data already sits there.

### Question 14 — A, C

Answers: De-identify the fields with Sensitive Data Protection; Split the data by time rather than at random. Sensitive Data Protection removes identifiers, and a time split prevents learning from the future. Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts PII. A time-based split prevents the model from learning from the future. Local study-map skill 2.1 (Preprocessing Tool Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts PII. In this case: Sensitive Data Protection removes identifiers, and a time split prevents learning from the future.
- **B:** Incorrect for this question. AutoML uses a reproducible default split when the dataset is large enough to do so. Why the correct answer wins: Sensitive Data Protection removes identifiers, and a time split prevents learning from the future.
- **C:** Correct. A time-based split prevents the model from learning from the future. In this case: Sensitive Data Protection removes identifiers, and a time split prevents learning from the future.
- **D:** Incorrect for this question. Dropping the field removes the exposure entirely when the model does not need it. Why the correct answer wins: Sensitive Data Protection removes identifiers, and a time split prevents learning from the future.
- **E:** Incorrect for this question. A crossed feature lets a linear model express the interaction it cannot learn alone. Why the correct answer wins: Sensitive Data Protection removes identifiers, and a time split prevents learning from the future.

### Question 15 — B

Answer: Preprocess in memory with pandas. In-memory processing is simplest while the data fits in memory. In-memory processing is the simplest option and stops working once the data exceeds the worker memory. Local study-map skill 2.1 (Preprocessing Tool Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Dataflow runs the same Beam code in batch and streaming and scales without provisioning. Why the correct answer wins: In-memory processing is simplest while the data fits in memory.
- **B:** Correct. In-memory processing is the simplest option and stops working once the data exceeds the worker memory. In this case: In-memory processing is simplest while the data fits in memory.
- **C:** Incorrect for this question. SQL over BigQuery is the cheapest option when the data already sits there and the logic is set-based. Why the correct answer wins: In-memory processing is simplest while the data fits in memory.
- **D:** Incorrect for this question. Spark suits large transformations the team already has as Scala or PySpark code. Why the correct answer wins: In-memory processing is simplest while the data fits in memory.

### Question 16 — C

Answer: Serve the feature from the online store. The online store returns the latest value at low latency. Local study-map skill 2.2 (Feature Store), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The offline store returns point-in-time values for training. Why the correct answer wins: The online store returns the latest value at low latency.
- **B:** Incorrect for this question. A crossed feature lets a linear model express the interaction it cannot learn alone. Why the correct answer wins: The online store returns the latest value at low latency.
- **C:** Correct. In this case: The online store returns the latest value at low latency.
- **D:** Incorrect for this question. Feature monitoring reports distribution changes per feature, not just per model. Why the correct answer wins: The online store returns the latest value at low latency.

### Question 17 — A

Answer: Add a crossed feature for the interacting pair. A crossed feature expresses the interaction a linear model cannot learn. Local study-map skill 2.2 (Feature Store), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: A crossed feature expresses the interaction a linear model cannot learn.
- **B:** Incorrect for this question. Bucketing converts a non-linear relationship into a form a linear model can fit. Why the correct answer wins: A crossed feature expresses the interaction a linear model cannot learn.
- **C:** Incorrect for this question. Scaling keeps one large-magnitude feature from dominating the gradient. Why the correct answer wins: A crossed feature expresses the interaction a linear model cannot learn.
- **D:** Incorrect for this question. Feature Store keeps one definition that both training and serving read. Why the correct answer wins: A crossed feature expresses the interaction a linear model cannot learn.

### Question 18 — B

Answer: Hash the identifiers with a salted key before training. A salted hash keeps the join key usable while removing the identifier. Local study-map skill 2.3 (PII Handling and Data Privacy), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Dropping the field removes the exposure entirely when the model does not need it. Why the correct answer wins: A salted hash keeps the join key usable while removing the identifier.
- **B:** Correct. In this case: A salted hash keeps the join key usable while removing the identifier.
- **C:** Incorrect for this question. Restricting the bucket limits who can copy the raw data in the first place. Why the correct answer wins: A salted hash keeps the join key usable while removing the identifier.
- **D:** Incorrect for this question. Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts PII. Why the correct answer wins: A salted hash keeps the join key usable while removing the identifier.

### Question 19 — D

Answer: Restrict the raw bucket to a privileged service account. Restricting the bucket limits who can copy the raw data. Local study-map skill 2.3 (PII Handling and Data Privacy), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Dropping the field removes the exposure entirely when the model does not need it. Why the correct answer wins: Restricting the bucket limits who can copy the raw data.
- **B:** Incorrect for this question. A salted hash keeps the join key usable while removing the direct identifier. Why the correct answer wins: Restricting the bucket limits who can copy the raw data.
- **C:** Incorrect for this question. Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts PII. Why the correct answer wins: Restricting the bucket limits who can copy the raw data.
- **D:** Correct. In this case: Restricting the bucket limits who can copy the raw data.

### Question 20 — D

Answer: Use Colab Enterprise. Colab Enterprise adds managed runtimes, VPC connectivity, and IAM. Local study-map skill 2.4 (Notebook Environments and Security), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A pinned image makes the environment reproducible across users. Why the correct answer wins: Colab Enterprise adds managed runtimes, VPC connectivity, and IAM.
- **B:** Incorrect for this question. A private-IP runtime reaches the data through the VPC and cannot be opened from the internet. Why the correct answer wins: Colab Enterprise adds managed runtimes, VPC connectivity, and IAM.
- **C:** Incorrect for this question. Workbench is the managed notebook instance inside the project VPC. Why the correct answer wins: Colab Enterprise adds managed runtimes, VPC connectivity, and IAM.
- **D:** Correct. In this case: Colab Enterprise adds managed runtimes, VPC connectivity, and IAM.

### Question 21 — C

Answer: Attach the runtime to the shared VPC subnet. The subnet attachment gives the notebook the route to internal sources. Local study-map skill 2.4 (Notebook Environments and Security), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Workbench is the managed notebook instance inside the project VPC. Why the correct answer wins: The subnet attachment gives the notebook the route to internal sources.
- **B:** Incorrect for this question. A private-IP runtime reaches the data through the VPC and cannot be opened from the internet. Why the correct answer wins: The subnet attachment gives the notebook the route to internal sources.
- **C:** Correct. In this case: The subnet attachment gives the notebook the route to internal sources.
- **D:** Incorrect for this question. Idle shutdown stops paying for a notebook nobody is using. Why the correct answer wins: The subnet attachment gives the notebook the route to internal sources.

### Question 22 — A

Answer: Set the random seed in the training code. A fixed seed makes a rerun reproducible. Local study-map skill 2.5 (Experiment Tracking), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: A fixed seed makes a rerun reproducible.
- **B:** Incorrect for this question. Comparing on the validation metric keeps model selection independent of the test set. Why the correct answer wins: A fixed seed makes a rerun reproducible.
- **C:** Incorrect for this question. Experiments records parameters, metrics, and artifacts per run so runs can be compared. Why the correct answer wins: A fixed seed makes a rerun reproducible.
- **D:** Incorrect for this question. ML Metadata records which data and code produced which artifact. Why the correct answer wins: A fixed seed makes a rerun reproducible.

### Question 23 — D

Answer: Log the run to Agent Platform Experiments. Experiments records parameters, metrics, and artifacts per run. Local study-map skill 2.5 (Experiment Tracking), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. ML Metadata records which data and code produced which artifact. Why the correct answer wins: Experiments records parameters, metrics, and artifacts per run.
- **B:** Incorrect for this question. A fixed seed makes a rerun reproducible when the rest of the environment is pinned. Why the correct answer wins: Experiments records parameters, metrics, and artifacts per run.
- **C:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: Experiments records parameters, metrics, and artifacts per run.
- **D:** Correct. In this case: Experiments records parameters, metrics, and artifacts per run.

### Question 24 — D, E

Answers: Express the workflow as a Kubeflow pipeline; Orchestrate the steps in Agent Platform Pipelines. A Kubeflow pipeline can run on either, and Pipelines records lineage per step. Kubeflow pipelines give a container-per-step pipeline that runs on the managed service or on GKE. Pipelines runs each step as a container with caching, lineage, and retry. Local study-map skill 2.6 (Development Environment Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Ray fits a Python-native distributed workload that is not a container-per-step pipeline. Why the correct answer wins: A Kubeflow pipeline can run on either, and Pipelines records lineage per step.
- **B:** Incorrect for this question. Experiments records parameters, metrics, and artifacts per run so runs can be compared. Why the correct answer wins: A Kubeflow pipeline can run on either, and Pipelines records lineage per step.
- **C:** Incorrect for this question. Airflow expresses cross-system dependencies and schedules outside the ML platform. Why the correct answer wins: A Kubeflow pipeline can run on either, and Pipelines records lineage per step.
- **D:** Correct. Kubeflow pipelines give a container-per-step pipeline that runs on the managed service or on GKE. In this case: A Kubeflow pipeline can run on either, and Pipelines records lineage per step.
- **E:** Correct. Pipelines runs each step as a container with caching, lineage, and retry. In this case: A Kubeflow pipeline can run on either, and Pipelines records lineage per step.

### Question 25 — B

Answer: Start from a Google-provided pipeline template. A template encodes the validated step order. Local study-map skill 2.6 (Development Environment Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Ray fits a Python-native distributed workload that is not a container-per-step pipeline. Why the correct answer wins: A template encodes the validated step order.
- **B:** Correct. In this case: A template encodes the validated step order.
- **C:** Incorrect for this question. Airflow expresses cross-system dependencies and schedules outside the ML platform. Why the correct answer wins: A template encodes the validated step order.
- **D:** Incorrect for this question. Kubeflow pipelines give a container-per-step pipeline that runs on the managed service or on GKE. Why the correct answer wins: A template encodes the validated step order.

### Question 26 — A, E

Answers: Report precision-recall AUC for the rare class; Inspect the confusion matrix at the operating threshold. Precision-recall AUC stays informative with rare positives, and the matrix shows the error split. Precision-recall AUC stays informative when the positive class is rare. The matrix shows the false-positive and false-negative split the business will feel. Local study-map skill 2.7 (Evaluation Metrics and LLM-as-a-Judge), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. Precision-recall AUC stays informative when the positive class is rare. In this case: Precision-recall AUC stays informative with rare positives, and the matrix shows the error split.
- **B:** Incorrect for this question. RMSE expresses the typical error in the units of the target. Why the correct answer wins: Precision-recall AUC stays informative with rare positives, and the matrix shows the error split.
- **C:** Incorrect for this question. MAPE expresses the error relative to the actual value, which business readers understand. Why the correct answer wins: Precision-recall AUC stays informative with rare positives, and the matrix shows the error split.
- **D:** Incorrect for this question. ROC AUC measures ranking quality across thresholds and hides class imbalance. Why the correct answer wins: Precision-recall AUC stays informative with rare positives, and the matrix shows the error split.
- **E:** Correct. The matrix shows the false-positive and false-negative split the business will feel. In this case: Precision-recall AUC stays informative with rare positives, and the matrix shows the error split.

### Question 27 — B

Answer: Score the answers with an LLM-as-a-judge rubric. A rubric-driven judge scales evaluation of free-text answers. Local study-map skill 2.7 (Evaluation Metrics and LLM-as-a-Judge), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Groundedness checks whether each claim is supported by the documents that were retrieved. Why the correct answer wins: A rubric-driven judge scales evaluation of free-text answers.
- **B:** Correct. In this case: A rubric-driven judge scales evaluation of free-text answers.
- **C:** Incorrect for this question. Human review remains the reference standard for a sample the judge is calibrated against. Why the correct answer wins: A rubric-driven judge scales evaluation of free-text answers.
- **D:** Incorrect for this question. A fixed prompt set makes the safety score comparable between releases. Why the correct answer wins: A rubric-driven judge scales evaluation of free-text answers.

### Question 28 — C

Answer: Track artifacts and lineage in ML Metadata. ML Metadata records which data and code produced which artifact. Local study-map skill 2.8 (Metadata and Lineage), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 2 (collaborating within and across teams): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The registry versions the model artifact and links it to its lineage and metrics. Why the correct answer wins: ML Metadata records which data and code produced which artifact.
- **B:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: ML Metadata records which data and code produced which artifact.
- **C:** Correct. In this case: ML Metadata records which data and code produced which artifact.
- **D:** Incorrect for this question. Experiments records parameters, metrics, and artifacts per run so runs can be compared. Why the correct answer wins: ML Metadata records which data and code produced which artifact.

### Question 29 — C

Answer: Choose a foundation model. A foundation model suits an open-ended language task with scarce labels. A foundation model suits an open-ended language or multimodal task where labelled data is scarce. Local study-map skill 3.1 (Model Type Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A classical time series model suits a single series with strong seasonality and little covariate data. Why the correct answer wins: A foundation model suits an open-ended language task with scarce labels.
- **B:** Incorrect for this question. TabNet gives an interpretable attentive tabular model inside custom training. Why the correct answer wins: A foundation model suits an open-ended language task with scarce labels.
- **C:** Correct. A foundation model suits an open-ended language or multimodal task where labelled data is scarce. In this case: A foundation model suits an open-ended language task with scarce labels.
- **D:** Incorrect for this question. A DNN suits a large tabular or unstructured dataset where interactions matter. Why the correct answer wins: A foundation model suits an open-ended language task with scarce labels.

### Question 30 — A

Answer: Choose a deep neural network. A DNN suits a large tabular dataset where interactions matter. Local study-map skill 3.1 (Model Type Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: A DNN suits a large tabular dataset where interactions matter.
- **B:** Incorrect for this question. A foundation model suits an open-ended language or multimodal task where labelled data is scarce. Why the correct answer wins: A DNN suits a large tabular dataset where interactions matter.
- **C:** Incorrect for this question. TabNet gives an interpretable attentive tabular model inside custom training. Why the correct answer wins: A DNN suits a large tabular dataset where interactions matter.
- **D:** Incorrect for this question. A classical time series model suits a single series with strong seasonality and little covariate data. Why the correct answer wins: A DNN suits a large tabular dataset where interactions matter.

### Question 31 — A

Answer: Build the model in BigQuery ML. BigQuery ML keeps training next to the data. Local study-map skill 3.2 (Product Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: BigQuery ML keeps training next to the data.
- **B:** Incorrect for this question. AutoML removes architecture search and tuning from the team while keeping a managed endpoint. Why the correct answer wins: BigQuery ML keeps training next to the data.
- **C:** Incorrect for this question. Custom training keeps full control of the framework and the loss. Why the correct answer wins: BigQuery ML keeps training next to the data.
- **D:** Incorrect for this question. TabNet gives an interpretable attentive tabular model inside custom training. Why the correct answer wins: BigQuery ML keeps training next to the data.

### Question 32 — A

Answer: Train with Agent Platform AutoML. AutoML removes architecture search and tuning from the team. Local study-map skill 3.2 (Product Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: AutoML removes architecture search and tuning from the team.
- **B:** Incorrect for this question. BigQuery ML keeps training next to the data and removes a separate serving pipeline. Why the correct answer wins: AutoML removes architecture search and tuning from the team.
- **C:** Incorrect for this question. TabNet gives an interpretable attentive tabular model inside custom training. Why the correct answer wins: AutoML removes architecture search and tuning from the team.
- **D:** Incorrect for this question. Custom training keeps full control of the framework and the loss. Why the correct answer wins: AutoML removes architecture search and tuning from the team.

### Question 33 — B, C

Answers: Run the new model in shadow mode; Roll out a canary with a small traffic share. Shadow mode serves nothing to users, and a canary limits exposure. Shadow mode scores live traffic without serving its answers, so the comparison costs nothing to users. A canary limits the blast radius while the new model is compared with the old one. Local study-map skill 3.3 (Deployment Strategy Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Two identical deployments let the switch be reversed immediately. Why the correct answer wins: Shadow mode serves nothing to users, and a canary limits exposure.
- **B:** Correct. A canary limits the blast radius while the new model is compared with the old one. In this case: Shadow mode serves nothing to users, and a canary limits exposure.
- **C:** Correct. Shadow mode scores live traffic without serving its answers, so the comparison costs nothing to users. In this case: Shadow mode serves nothing to users, and a canary limits exposure.
- **D:** Incorrect for this question. A/B testing compares two models on the same population with a traffic split. Why the correct answer wins: Shadow mode serves nothing to users, and a canary limits exposure.
- **E:** Incorrect for this question. An in-place replacement exposes every request to the new version at once. Why the correct answer wins: Shadow mode serves nothing to users, and a canary limits exposure.

### Question 34 — A

Answer: Deploy blue/green with an instant switch. Two identical deployments let the switch be reversed immediately. Local study-map skill 3.3 (Deployment Strategy Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Two identical deployments let the switch be reversed immediately.
- **B:** Incorrect for this question. An in-place replacement exposes every request to the new version at once. Why the correct answer wins: Two identical deployments let the switch be reversed immediately.
- **C:** Incorrect for this question. Shadow mode scores live traffic without serving its answers, so the comparison costs nothing to users. Why the correct answer wins: Two identical deployments let the switch be reversed immediately.
- **D:** Incorrect for this question. A canary limits the blast radius while the new model is compared with the old one. Why the correct answer wins: Two identical deployments let the switch be reversed immediately.

### Question 35 — A

Answer: Use sampled Shapley on the endpoint. Sampled Shapley explains a single request without a batch job. Sampled Shapley explains individual online predictions with a bounded compute cost. Local study-map skill 3.4 (Interpretability), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. Sampled Shapley explains individual online predictions with a bounded compute cost. In this case: Sampled Shapley explains a single request without a batch job.
- **B:** Incorrect for this question. Integrated gradients attributes an image prediction to the pixels that moved it. Why the correct answer wins: Sampled Shapley explains a single request without a batch job.
- **C:** Incorrect for this question. ML.GLOBAL_EXPLAIN ranks the features that matter most across the whole model. Why the correct answer wins: Sampled Shapley explains a single request without a batch job.
- **D:** Incorrect for this question. Shapley values attribute a prediction to its features with a consistent baseline. Why the correct answer wins: Sampled Shapley explains a single request without a batch job.

### Question 36 — D

Answer: Summarise the model with ML.GLOBAL_EXPLAIN. ML.GLOBAL_EXPLAIN ranks the features that matter most. Local study-map skill 3.4 (Interpretability), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. ML.EXPLAIN_PREDICT attributes each prediction to the features that moved it. Why the correct answer wins: ML.GLOBAL_EXPLAIN ranks the features that matter most.
- **B:** Incorrect for this question. Shapley values attribute a prediction to its features with a consistent baseline. Why the correct answer wins: ML.GLOBAL_EXPLAIN ranks the features that matter most.
- **C:** Incorrect for this question. Sampled Shapley explains individual online predictions with a bounded compute cost. Why the correct answer wins: ML.GLOBAL_EXPLAIN ranks the features that matter most.
- **D:** Correct. In this case: ML.GLOBAL_EXPLAIN ranks the features that matter most.

### Question 37 — D

Answer: Write the training data as TFRecord shards in Cloud Storage. Sharded TFRecord is the efficient read format for distributed training. Local study-map skill 3.5 (Training Data Organization), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Parquet is columnar and cheap to scan for tabular training data. Why the correct answer wins: Sharded TFRecord is the efficient read format for distributed training.
- **B:** Incorrect for this question. Reading from BigQuery avoids a copy and keeps the query pushdown. Why the correct answer wins: Sharded TFRecord is the efficient read format for distributed training.
- **C:** Incorrect for this question. A streaming path keeps the training data current without a nightly copy. Why the correct answer wins: Sharded TFRecord is the efficient read format for distributed training.
- **D:** Correct. In this case: Sharded TFRecord is the efficient read format for distributed training.

### Question 38 — C

Answer: Stream the new records through Dataflow into the training store. A streaming path keeps the training data current. Local study-map skill 3.5 (Training Data Organization), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Sharded TFRecord is the efficient read format for distributed training. Why the correct answer wins: A streaming path keeps the training data current.
- **B:** Incorrect for this question. Parquet is columnar and cheap to scan for tabular training data. Why the correct answer wins: A streaming path keeps the training data current.
- **C:** Correct. In this case: A streaming path keeps the training data current.
- **D:** Incorrect for this question. Reading from BigQuery avoids a copy and keeps the query pushdown. Why the correct answer wins: A streaming path keeps the training data current.

### Question 39 — B

Answer: Deduplicate on the event key in the ingestion step. Deduplicating at ingest stops duplicated records inflating the set. Local study-map skill 3.6 (Ingestion into Training Pipelines), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Parquet is columnar and cheap to scan for tabular training data. Why the correct answer wins: Deduplicating at ingest stops duplicated records inflating the set.
- **B:** Correct. In this case: Deduplicating at ingest stops duplicated records inflating the set.
- **C:** Incorrect for this question. A streaming path keeps the training data current without a nightly copy. Why the correct answer wins: Deduplicating at ingest stops duplicated records inflating the set.
- **D:** Incorrect for this question. Rejecting rows into a side table makes a schema break visible instead of silent. Why the correct answer wins: Deduplicating at ingest stops duplicated records inflating the set.

### Question 40 — A

Answer: Validate the schema and quarantine rejected rows. Rejecting rows into a side table makes a schema break visible. Local study-map skill 3.6 (Ingestion into Training Pipelines), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Rejecting rows into a side table makes a schema break visible.
- **B:** Incorrect for this question. Deduplicating at ingest stops duplicated records inflating the training set. Why the correct answer wins: Rejecting rows into a side table makes a schema break visible.
- **C:** Incorrect for this question. A streaming path keeps the training data current without a nightly copy. Why the correct answer wins: Rejecting rows into a side table makes a schema break visible.
- **D:** Incorrect for this question. Reading from BigQuery avoids a copy and keeps the query pushdown. Why the correct answer wins: Rejecting rows into a side table makes a schema break visible.

### Question 41 — C

Answer: Run a custom container on Agent Platform. A custom container carries its own framework and dependencies. Local study-map skill 3.7 (Custom Training and SDKs), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A prebuilt container already implements the framework handler, so no serving code is written. Why the correct answer wins: A custom container carries its own framework and dependencies.
- **B:** Incorrect for this question. Export produces a container-ready artifact that can be served outside the managed endpoint. Why the correct answer wins: A custom container carries its own framework and dependencies.
- **C:** Correct. In this case: A custom container carries its own framework and dependencies.
- **D:** Incorrect for this question. The prebuilt container installs the package, which is the lightest way to run custom code. Why the correct answer wins: A custom container carries its own framework and dependencies.

### Question 42 — C

Answer: Package the trainer as a Python package. The prebuilt container installs the package. Local study-map skill 3.7 (Custom Training and SDKs), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A prebuilt container already implements the framework handler, so no serving code is written. Why the correct answer wins: The prebuilt container installs the package.
- **B:** Incorrect for this question. A custom container carries its own framework and dependencies into the managed training job. Why the correct answer wins: The prebuilt container installs the package.
- **C:** Correct. In this case: The prebuilt container installs the package.
- **D:** Incorrect for this question. AutoML removes architecture search and tuning from the team while keeping a managed endpoint. Why the correct answer wins: The prebuilt container installs the package.

### Question 43 — C

Answer: Reduce the per-replica batch size. The out-of-memory error is a memory-per-step problem. Local study-map skill 3.8 (Training Failure Troubleshooting), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Checkpointing trades recomputation for activation memory. Why the correct answer wins: The out-of-memory error is a memory-per-step problem.
- **B:** Incorrect for this question. Accelerator quota is regional and blocks the job before the code runs. Why the correct answer wins: The out-of-memory error is a memory-per-step problem.
- **C:** Correct. In this case: The out-of-memory error is a memory-per-step problem.
- **D:** Incorrect for this question. A loss that becomes NaN usually reflects a step size too large for the data scale. Why the correct answer wins: The out-of-memory error is a memory-per-step problem.

### Question 44 — D

Answer: Pin the framework version in the container. A framework mismatch changes behaviour without changing the code. Local study-map skill 3.8 (Training Failure Troubleshooting), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A permission error on the input is a missing IAM binding, not a model problem. Why the correct answer wins: A framework mismatch changes behaviour without changing the code.
- **B:** Incorrect for this question. A loss that becomes NaN usually reflects a step size too large for the data scale. Why the correct answer wins: A framework mismatch changes behaviour without changing the code.
- **C:** Incorrect for this question. Accelerator quota is regional and blocks the job before the code runs. Why the correct answer wins: A framework mismatch changes behaviour without changing the code.
- **D:** Correct. In this case: A framework mismatch changes behaviour without changing the code.

### Question 45 — A, B

Answers: Run a hyperparameter tuning job; Enable early stopping of poor trials. The tuning service searches in parallel, and early stopping frees capacity. The tuning service searches the space in parallel and reports the best trial. Early stopping frees capacity from trials that cannot win. Local study-map skill 3.9 (Hyperparameter Tuning), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. Early stopping frees capacity from trials that cannot win. In this case: The tuning service searches in parallel, and early stopping frees capacity.
- **B:** Correct. The tuning service searches the space in parallel and reports the best trial. In this case: The tuning service searches in parallel, and early stopping frees capacity.
- **C:** Incorrect for this question. The search optimises the metric the trainer reports, so it must be the one that matters. Why the correct answer wins: The tuning service searches in parallel, and early stopping frees capacity.
- **D:** Incorrect for this question. The budget bounds both the cost and the wall-clock time of the search. Why the correct answer wins: The tuning service searches in parallel, and early stopping frees capacity.
- **E:** Incorrect for this question. Bayesian search spends fewer trials to reach a good configuration. Why the correct answer wins: The tuning service searches in parallel, and early stopping frees capacity.

### Question 46 — B

Answer: Cap the search with a trial count and a parallel budget. The budget bounds cost and wall-clock time. Local study-map skill 3.9 (Hyperparameter Tuning), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The tuning service searches the space in parallel and reports the best trial. Why the correct answer wins: The budget bounds cost and wall-clock time.
- **B:** Correct. In this case: The budget bounds cost and wall-clock time.
- **C:** Incorrect for this question. Early stopping frees capacity from trials that cannot win. Why the correct answer wins: The budget bounds cost and wall-clock time.
- **D:** Incorrect for this question. Bayesian search spends fewer trials to reach a good configuration. Why the correct answer wins: The budget bounds cost and wall-clock time.

### Question 47 — A

Answer: Fine-tune with a parameter-efficient adapter. A parameter-efficient adapter trains few weights and keeps the base model intact. Local study-map skill 3.10 (Fine-Tuning Decisions), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: A parameter-efficient adapter trains few weights and keeps the base model intact.
- **B:** Incorrect for this question. Retrieval is the cheaper answer when the problem is missing knowledge rather than missing behaviour. Why the correct answer wins: A parameter-efficient adapter trains few weights and keeps the base model intact.
- **C:** Incorrect for this question. Full fine-tuning updates every weight and needs the most data and accelerator memory. Why the correct answer wins: A parameter-efficient adapter trains few weights and keeps the base model intact.
- **D:** Incorrect for this question. Distillation moves the quality of the teacher into a model cheap enough to serve. Why the correct answer wins: A parameter-efficient adapter trains few weights and keeps the base model intact.

### Question 48 — B

Answer: Serve on L4 GPUs. An L4 GPU gives low-cost acceleration for a modest model. Local study-map skill 3.11 (Hardware and Accelerator Selection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. CPU serving is the cheapest option for a small model with a generous latency budget. Why the correct answer wins: An L4 GPU gives low-cost acceleration for a modest model.
- **B:** Correct. In this case: An L4 GPU gives low-cost acceleration for a modest model.
- **C:** Incorrect for this question. A100 GPUs suit mixed-precision training where the framework expects CUDA. Why the correct answer wins: An L4 GPU gives low-cost acceleration for a modest model.
- **D:** Incorrect for this question. A TPU slice gives a tightly coupled accelerator fabric for large synchronous training. Why the correct answer wins: An L4 GPU gives low-cost acceleration for a modest model.

### Question 49 — B, C

Answers: Use model parallelism; Use data parallelism. Model parallelism splits the layers, and data parallelism splits the batch across replicas. Model parallelism splits the layers across devices when one model does not fit on one. Data parallelism replicates the model and splits each batch across the workers. Local study-map skill 3.12 (Distributed Training), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 3 (scaling prototypes into ML models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Multi-worker gives each replica a shard of the data and a defined chief. Why the correct answer wins: Model parallelism splits the layers, and data parallelism splits the batch across replicas.
- **B:** Correct. Model parallelism splits the layers across devices when one model does not fit on one. In this case: Model parallelism splits the layers, and data parallelism splits the batch across replicas.
- **C:** Correct. Data parallelism replicates the model and splits each batch across the workers. In this case: Model parallelism splits the layers, and data parallelism splits the batch across replicas.
- **D:** Incorrect for this question. A checkpoint turns a preemption into a delay rather than a restart. Why the correct answer wins: Model parallelism splits the layers, and data parallelism splits the batch across replicas.
- **E:** Incorrect for this question. A larger global batch keeps each worker busy after the split. Why the correct answer wins: Model parallelism splits the layers, and data parallelism splits the batch across replicas.

### Question 50 — A

Answer: Run batch prediction. Batch prediction reads a file and writes predictions without serving capacity. Local study-map skill 4.1 (Batch and Online Inference), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Batch prediction reads a file and writes predictions without serving capacity.
- **B:** Incorrect for this question. Batching amortises the per-request overhead when the caller can wait. Why the correct answer wins: Batch prediction reads a file and writes predictions without serving capacity.
- **C:** Incorrect for this question. An endpoint keeps capacity ready for low-latency per-request predictions. Why the correct answer wins: Batch prediction reads a file and writes predictions without serving capacity.
- **D:** Incorrect for this question. Streaming answers each event as it arrives rather than on a schedule. Why the correct answer wins: Batch prediction reads a file and writes predictions without serving capacity.

### Question 51 — C, D

Answers: Deploy to an online endpoint; Send the events to a streaming prediction path. An endpoint keeps capacity ready for per-click calls, and streaming answers each event. An endpoint keeps capacity ready for low-latency per-request predictions. Streaming answers each event as it arrives rather than on a schedule. Local study-map skill 4.1 (Batch and Online Inference), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Batch prediction reads a file or table and writes predictions without holding serving capacity. Why the correct answer wins: An endpoint keeps capacity ready for per-click calls, and streaming answers each event.
- **B:** Incorrect for this question. A GPU shortens inference time enough to meet a tight latency target. Why the correct answer wins: An endpoint keeps capacity ready for per-click calls, and streaming answers each event.
- **C:** Correct. An endpoint keeps capacity ready for low-latency per-request predictions. In this case: An endpoint keeps capacity ready for per-click calls, and streaming answers each event.
- **D:** Correct. Streaming answers each event as it arrives rather than on a schedule. In this case: An endpoint keeps capacity ready for per-click calls, and streaming answers each event.
- **E:** Incorrect for this question. Batching amortises the per-request overhead when the caller can wait. Why the correct answer wins: An endpoint keeps capacity ready for per-click calls, and streaming answers each event.

### Question 52 — D

Answer: Batch the requests inside the client. Batching amortises the fixed per-request overhead across many rows. Batching amortises the per-request overhead when the caller can wait. Local study-map skill 4.1 (Batch and Online Inference), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Autoscaling adds replicas with the traffic and removes them afterwards. Why the correct answer wins: Batching amortises the fixed per-request overhead across many rows.
- **B:** Incorrect for this question. Concurrency fills each replica before another is started, which lowers cost per request. Why the correct answer wins: Batching amortises the fixed per-request overhead across many rows.
- **C:** Incorrect for this question. Batch prediction reads a file or table and writes predictions without holding serving capacity. Why the correct answer wins: Batching amortises the fixed per-request overhead across many rows.
- **D:** Correct. Batching amortises the per-request overhead when the caller can wait. In this case: Batching amortises the fixed per-request overhead across many rows.

### Question 53 — C

Answer: Use a prebuilt serving container. A prebuilt container implements the framework handler. A prebuilt container already implements the framework handler, so no serving code is written. Local study-map skill 4.2 (Packaging and Custom Containers), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Artifact Registry holds the image with IAM and vulnerability metadata. Why the correct answer wins: A prebuilt container implements the framework handler.
- **B:** Incorrect for this question. The routine runs the preprocessing and postprocessing inside the serving container. Why the correct answer wins: A prebuilt container implements the framework handler.
- **C:** Correct. A prebuilt container already implements the framework handler, so no serving code is written. In this case: A prebuilt container implements the framework handler.
- **D:** Incorrect for this question. A GPU shortens inference time enough to meet a tight latency target. Why the correct answer wins: A prebuilt container implements the framework handler.

### Question 54 — D

Answer: Push the serving image to Artifact Registry. Artifact Registry holds the image with IAM and vulnerability metadata. Local study-map skill 4.2 (Packaging and Custom Containers), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A prebuilt container already implements the framework handler, so no serving code is written. Why the correct answer wins: Artifact Registry holds the image with IAM and vulnerability metadata.
- **B:** Incorrect for this question. Autoscaling adds replicas with the traffic and removes them afterwards. Why the correct answer wins: Artifact Registry holds the image with IAM and vulnerability metadata.
- **C:** Incorrect for this question. The registry versions the model artifact and links it to its lineage and metrics. Why the correct answer wins: Artifact Registry holds the image with IAM and vulnerability metadata.
- **D:** Correct. In this case: Artifact Registry holds the image with IAM and vulnerability metadata.

### Question 55 — D

Answer: Register the model in Agent Platform Model Registry. The registry versions the artifact and links it to lineage. Local study-map skill 4.3 (Model Registry and Versioning), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. ML Metadata records which data and code produced which artifact. Why the correct answer wins: The registry versions the artifact and links it to lineage.
- **B:** Incorrect for this question. Experiments records parameters, metrics, and artifacts per run so runs can be compared. Why the correct answer wins: The registry versions the artifact and links it to lineage.
- **C:** Incorrect for this question. Artifact Registry holds the image with IAM and vulnerability metadata. Why the correct answer wins: The registry versions the artifact and links it to lineage.
- **D:** Correct. In this case: The registry versions the artifact and links it to lineage.

### Question 56 — B

Answer: Deploy the version and move the alias. An alias decouples the served version from the artifact id. An alias decouples the served version name from the artifact id, so a rollback is a pointer move. Local study-map skill 4.3 (Model Registry and Versioning), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. An in-place replacement exposes every request to the new version at once. Why the correct answer wins: An alias decouples the served version from the artifact id.
- **B:** Correct. An alias decouples the served version name from the artifact id, so a rollback is a pointer move. In this case: An alias decouples the served version from the artifact id.
- **C:** Incorrect for this question. The registry versions the model artifact and links it to its lineage and metrics. Why the correct answer wins: An alias decouples the served version from the artifact id.
- **D:** Incorrect for this question. A traffic split sends a defined share to each version on the same endpoint. Why the correct answer wins: An alias decouples the served version from the artifact id.

### Question 57 — C, E

Answers: Split traffic between two models in an A/B test; Roll out a canary with a small traffic share. A/B testing compares on one population, and a canary limits exposure. A/B testing compares two models on the same population with a traffic split. A canary limits the blast radius while the new model is compared with the old one. Local study-map skill 4.4 (Model Rollout Strategies), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Two identical deployments let the switch be reversed immediately. Why the correct answer wins: A/B testing compares on one population, and a canary limits exposure.
- **B:** Incorrect for this question. An in-place replacement exposes every request to the new version at once. Why the correct answer wins: A/B testing compares on one population, and a canary limits exposure.
- **C:** Correct. A canary limits the blast radius while the new model is compared with the old one. In this case: A/B testing compares on one population, and a canary limits exposure.
- **D:** Incorrect for this question. Shadow mode scores live traffic without serving its answers, so the comparison costs nothing to users. Why the correct answer wins: A/B testing compares on one population, and a canary limits exposure.
- **E:** Correct. A/B testing compares two models on the same population with a traffic split. In this case: A/B testing compares on one population, and a canary limits exposure.

### Question 58 — A

Answer: Run the new model in shadow mode. Shadow mode scores live traffic without serving its answers. Local study-map skill 4.4 (Model Rollout Strategies), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Shadow mode scores live traffic without serving its answers.
- **B:** Incorrect for this question. A canary limits the blast radius while the new model is compared with the old one. Why the correct answer wins: Shadow mode scores live traffic without serving its answers.
- **C:** Incorrect for this question. A/B testing compares two models on the same population with a traffic split. Why the correct answer wins: Shadow mode scores live traffic without serving its answers.
- **D:** Incorrect for this question. An in-place replacement exposes every request to the new version at once. Why the correct answer wins: Shadow mode scores live traffic without serving its answers.

### Question 59 — C

Answer: Share one transformation library between training and serving. Shared code removes the class of bug where paths differ. Shared code removes the class of bug where the two paths compute a feature differently. Local study-map skill 4.5 (Inference Preprocessing and Postprocessing), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: Shared code removes the class of bug where paths differ.
- **B:** Incorrect for this question. An alias decouples the served version name from the artifact id, so a rollback is a pointer move. Why the correct answer wins: Shared code removes the class of bug where paths differ.
- **C:** Correct. Shared code removes the class of bug where the two paths compute a feature differently. In this case: Shared code removes the class of bug where paths differ.
- **D:** Incorrect for this question. Feature Store keeps one definition that both training and serving read. Why the correct answer wins: Shared code removes the class of bug where paths differ.

### Question 60 — B

Answer: Keep the preprocessing inside the exported model. Preprocessing inside the artifact cannot drift. Local study-map skill 4.5 (Inference Preprocessing and Postprocessing), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Explanation metadata tells the endpoint which inputs to attribute over. Why the correct answer wins: Preprocessing inside the artifact cannot drift.
- **B:** Correct. In this case: Preprocessing inside the artifact cannot drift.
- **C:** Incorrect for this question. Shared code removes the class of bug where the two paths compute a feature differently. Why the correct answer wins: Preprocessing inside the artifact cannot drift.
- **D:** Incorrect for this question. Feature Store keeps one definition that both training and serving read. Why the correct answer wins: Preprocessing inside the artifact cannot drift.

### Question 61 — B

Answer: Use a dedicated endpoint. A dedicated endpoint gives the model its own capacity. Local study-map skill 4.6 (Endpoint Types and Access), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A private endpoint is reachable only from the VPC and shares no public surface. Why the correct answer wins: A dedicated endpoint gives the model its own capacity.
- **B:** Correct. In this case: A dedicated endpoint gives the model its own capacity.
- **C:** Incorrect for this question. Autoscaling adds replicas with the traffic and removes them afterwards. Why the correct answer wins: A dedicated endpoint gives the model its own capacity.
- **D:** Incorrect for this question. A shared endpoint removes the deployment step but gives no control over capacity or residency. Why the correct answer wins: A dedicated endpoint gives the model its own capacity.

### Question 62 — B

Answer: Deploy with a private endpoint only. A private endpoint is reachable only from the VPC. Local study-map skill 4.6 (Endpoint Types and Access), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A shared endpoint removes the deployment step but gives no control over capacity or residency. Why the correct answer wins: A private endpoint is reachable only from the VPC.
- **B:** Correct. In this case: A private endpoint is reachable only from the VPC.
- **C:** Incorrect for this question. A GPU shortens inference time enough to meet a tight latency target. Why the correct answer wins: A private endpoint is reachable only from the VPC.
- **D:** Incorrect for this question. A dedicated endpoint gives the model its own capacity instead of sharing a pool. Why the correct answer wins: A private endpoint is reachable only from the VPC.

### Question 63 — D

Answer: Attach a GPU to the serving replica. A GPU shortens inference time enough to meet the target. Local study-map skill 4.7 (Serving Hardware), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. CPU serving is the cheapest option for a small model with a generous latency budget. Why the correct answer wins: A GPU shortens inference time enough to meet the target.
- **B:** Incorrect for this question. An Edge TPU runs a quantised model on-device where the network cannot be relied on. Why the correct answer wins: A GPU shortens inference time enough to meet the target.
- **C:** Incorrect for this question. Concurrency fills each replica before another is started, which lowers cost per request. Why the correct answer wins: A GPU shortens inference time enough to meet the target.
- **D:** Correct. In this case: A GPU shortens inference time enough to meet the target.

### Question 64 — A

Answer: Serve on CPU only. CPU serving is the cheapest option when the budget is generous. CPU serving is the cheapest option for a small model with a generous latency budget. Local study-map skill 4.7 (Serving Hardware), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. CPU serving is the cheapest option for a small model with a generous latency budget. In this case: CPU serving is the cheapest option when the budget is generous.
- **B:** Incorrect for this question. An Edge TPU runs a quantised model on-device where the network cannot be relied on. Why the correct answer wins: CPU serving is the cheapest option when the budget is generous.
- **C:** Incorrect for this question. A GPU shortens inference time enough to meet a tight latency target. Why the correct answer wins: CPU serving is the cheapest option when the budget is generous.
- **D:** Incorrect for this question. An L4 GPU gives low-cost inference acceleration for a modest model. Why the correct answer wins: CPU serving is the cheapest option when the budget is generous.

### Question 65 — A, E

Answers: Enable autoscaling on the endpoint; Raise the concurrency per replica. Autoscaling follows the traffic, and concurrency lowers cost per request. Autoscaling adds replicas with the traffic and removes them afterwards. Concurrency fills each replica before another is started, which lowers cost per request. Local study-map skill 4.8 (Serving Throughput and Scaling), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. Autoscaling adds replicas with the traffic and removes them afterwards. In this case: Autoscaling follows the traffic, and concurrency lowers cost per request.
- **B:** Incorrect for this question. Batching amortises the per-request overhead when the caller can wait. Why the correct answer wins: Autoscaling follows the traffic, and concurrency lowers cost per request.
- **C:** Incorrect for this question. The ceiling caps how far the endpoint scales, and therefore the throughput it can absorb. Why the correct answer wins: Autoscaling follows the traffic, and concurrency lowers cost per request.
- **D:** Incorrect for this question. A minimum replica keeps capacity warm so the first request after a quiet period is fast. Why the correct answer wins: Autoscaling follows the traffic, and concurrency lowers cost per request.
- **E:** Correct. Concurrency fills each replica before another is started, which lowers cost per request. In this case: Autoscaling follows the traffic, and concurrency lowers cost per request.

### Question 66 — B

Answer: Raise the maximum replica count. The ceiling caps how far the endpoint scales. Local study-map skill 4.8 (Serving Throughput and Scaling), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Concurrency fills each replica before another is started, which lowers cost per request. Why the correct answer wins: The ceiling caps how far the endpoint scales.
- **B:** Correct. In this case: The ceiling caps how far the endpoint scales.
- **C:** Incorrect for this question. A minimum replica keeps capacity warm so the first request after a quiet period is fast. Why the correct answer wins: The ceiling caps how far the endpoint scales.
- **D:** Incorrect for this question. A GPU shortens inference time enough to meet a tight latency target. Why the correct answer wins: The ceiling caps how far the endpoint scales.

### Question 67 — D

Answer: Set a minimum replica count. A minimum replica keeps capacity warm. Local study-map skill 4.8 (Serving Throughput and Scaling), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The ceiling caps how far the endpoint scales, and therefore the throughput it can absorb. Why the correct answer wins: A minimum replica keeps capacity warm.
- **B:** Incorrect for this question. Batching amortises the per-request overhead when the caller can wait. Why the correct answer wins: A minimum replica keeps capacity warm.
- **C:** Incorrect for this question. Concurrency fills each replica before another is started, which lowers cost per request. Why the correct answer wins: A minimum replica keeps capacity warm.
- **D:** Correct. In this case: A minimum replica keeps capacity warm.

### Question 68 — C, E

Answers: Raise the concurrency per replica; Configure explanation metadata for the endpoint. Concurrency lowers the cost per request, and explanation metadata enables attributions. Concurrency fills each replica before another is started, which lowers cost per request. Explanation metadata tells the endpoint which inputs to attribute over. Local study-map skill 4.9 (Production Tuning), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A minimum replica keeps capacity warm so the first request after a quiet period is fast. Why the correct answer wins: Concurrency lowers the cost per request, and explanation metadata enables attributions.
- **B:** Incorrect for this question. An alias decouples the served version name from the artifact id, so a rollback is a pointer move. Why the correct answer wins: Concurrency lowers the cost per request, and explanation metadata enables attributions.
- **C:** Correct. Explanation metadata tells the endpoint which inputs to attribute over. In this case: Concurrency lowers the cost per request, and explanation metadata enables attributions.
- **D:** Incorrect for this question. Artifact Registry holds the image with IAM and vulnerability metadata. Why the correct answer wins: Concurrency lowers the cost per request, and explanation metadata enables attributions.
- **E:** Correct. Concurrency fills each replica before another is started, which lowers cost per request. In this case: Concurrency lowers the cost per request, and explanation metadata enables attributions.

### Question 69 — C

Answer: Attach a GPU to the serving replica. A GPU shortens inference time enough to meet the target. Local study-map skill 4.9 (Production Tuning), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 4 (serving and scaling models): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Concurrency fills each replica before another is started, which lowers cost per request. Why the correct answer wins: A GPU shortens inference time enough to meet the target.
- **B:** Incorrect for this question. The ceiling caps how far the endpoint scales, and therefore the throughput it can absorb. Why the correct answer wins: A GPU shortens inference time enough to meet the target.
- **C:** Correct. In this case: A GPU shortens inference time enough to meet the target.
- **D:** Incorrect for this question. Batching amortises the per-request overhead when the caller can wait. Why the correct answer wins: A GPU shortens inference time enough to meet the target.

### Question 70 — B

Answer: Gate the deployment on a model evaluation threshold. The gate promotes a model only when it beats the incumbent. Local study-map skill 5.1 (Data and Model Validation), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A validation step stops a bad batch before it reaches training. Why the correct answer wins: The gate promotes a model only when it beats the incumbent.
- **B:** Correct. In this case: The gate promotes a model only when it beats the incumbent.
- **C:** Incorrect for this question. Drift-triggered retraining responds to change instead of to the calendar. Why the correct answer wins: The gate promotes a model only when it beats the incumbent.
- **D:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: The gate promotes a model only when it beats the incumbent.

### Question 71 — A

Answer: Add an explicit data validation step. A validation step stops a bad batch before training. Local study-map skill 5.1 (Data and Model Validation), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: A validation step stops a bad batch before training.
- **B:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: A validation step stops a bad batch before training.
- **C:** Incorrect for this question. Rejecting rows into a side table makes a schema break visible instead of silent. Why the correct answer wins: A validation step stops a bad batch before training.
- **D:** Incorrect for this question. The gate promotes a model only when it beats the incumbent on the agreed metric. Why the correct answer wins: A validation step stops a bad batch before training.

### Question 72 — B, D

Answers: Keep the test set out of every tuning decision; Report precision-recall AUC for the rare class. A locked test set restores an unbiased estimate, and precision-recall AUC handles imbalance. A test set that has been used for tuning no longer estimates generalisation. Precision-recall AUC stays informative when the positive class is rare. Local study-map skill 5.1 (Data and Model Validation), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. MAPE expresses the error relative to the actual value, which business readers understand. Why the correct answer wins: A locked test set restores an unbiased estimate, and precision-recall AUC handles imbalance.
- **B:** Correct. Precision-recall AUC stays informative when the positive class is rare. In this case: A locked test set restores an unbiased estimate, and precision-recall AUC handles imbalance.
- **C:** Incorrect for this question. The matrix shows the false-positive and false-negative split the business will feel. Why the correct answer wins: A locked test set restores an unbiased estimate, and precision-recall AUC handles imbalance.
- **D:** Correct. A test set that has been used for tuning no longer estimates generalisation. In this case: A locked test set restores an unbiased estimate, and precision-recall AUC handles imbalance.
- **E:** Incorrect for this question. ROC AUC measures ranking quality across thresholds and hides class imbalance. Why the correct answer wins: A locked test set restores an unbiased estimate, and precision-recall AUC handles imbalance.

### Question 73 — D

Answer: Orchestrate the steps in Agent Platform Pipelines. Pipelines records lineage per artifact and caches the step output. Pipelines runs each step as a container with caching, lineage, and retry. Local study-map skill 5.2 (Pipeline Orchestration Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Kubeflow pipelines give a container-per-step pipeline that runs on the managed service or on GKE. Why the correct answer wins: Pipelines records lineage per artifact and caches the step output.
- **B:** Incorrect for this question. Ray fits a Python-native distributed workload that is not a container-per-step pipeline. Why the correct answer wins: Pipelines records lineage per artifact and caches the step output.
- **C:** Incorrect for this question. Airflow expresses cross-system dependencies and schedules outside the ML platform. Why the correct answer wins: Pipelines records lineage per artifact and caches the step output.
- **D:** Correct. Pipelines runs each step as a container with caching, lineage, and retry. In this case: Pipelines records lineage per artifact and caches the step output.

### Question 74 — C

Answer: Orchestrate with Managed Service for Apache Airflow. Airflow expresses cross-system dependencies that span unrelated services. Airflow expresses cross-system dependencies and schedules outside the ML platform. Local study-map skill 5.2 (Pipeline Orchestration Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance. Why the correct answer wins: Airflow expresses cross-system dependencies that span unrelated services.
- **B:** Incorrect for this question. Ray fits a Python-native distributed workload that is not a container-per-step pipeline. Why the correct answer wins: Airflow expresses cross-system dependencies that span unrelated services.
- **C:** Correct. Airflow expresses cross-system dependencies and schedules outside the ML platform. In this case: Airflow expresses cross-system dependencies that span unrelated services.
- **D:** Incorrect for this question. Pipelines runs each step as a container with caching, lineage, and retry. Why the correct answer wins: Airflow expresses cross-system dependencies that span unrelated services.

### Question 75 — B

Answer: Use Ray on Agent Platform for the distributed compute. Ray fits a Python-native distributed workload. Local study-map skill 5.2 (Pipeline Orchestration Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Airflow expresses cross-system dependencies and schedules outside the ML platform. Why the correct answer wins: Ray fits a Python-native distributed workload.
- **B:** Correct. In this case: Ray fits a Python-native distributed workload.
- **C:** Incorrect for this question. Pipelines runs each step as a container with caching, lineage, and retry. Why the correct answer wins: Ray fits a Python-native distributed workload.
- **D:** Incorrect for this question. Kubeflow pipelines give a container-per-step pipeline that runs on the managed service or on GKE. Why the correct answer wins: Ray fits a Python-native distributed workload.

### Question 76 — B

Answer: Trigger the build and deploy from Cloud Build. Cloud Build records the build and deploy steps. Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance. Local study-map skill 5.2 (Pipeline Orchestration Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: Cloud Build records the build and deploy steps.
- **B:** Correct. Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance. In this case: Cloud Build records the build and deploy steps.
- **C:** Incorrect for this question. The scheduler starts the pipeline on the cadence the retraining policy defines. Why the correct answer wins: Cloud Build records the build and deploy steps.
- **D:** Incorrect for this question. Manual retraining leaves the model stale whenever the trigger is forgotten. Why the correct answer wins: Cloud Build records the build and deploy steps.

### Question 77 — C

Answer: Register the feature in Agent Platform Feature Store. Feature Store serves one definition to both the backfill and the live call. Feature Store keeps one definition that both training and serving read. Local study-map skill 5.3 (Train and Serve Consistency), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: Feature Store serves one definition to both the backfill and the live call.
- **B:** Incorrect for this question. Shared code removes the class of bug where the two paths compute a feature differently. Why the correct answer wins: Feature Store serves one definition to both the backfill and the live call.
- **C:** Correct. Feature Store keeps one definition that both training and serving read. In this case: Feature Store serves one definition to both the backfill and the live call.
- **D:** Incorrect for this question. Preprocessing inside the artifact cannot drift between the two paths. Why the correct answer wins: Feature Store serves one definition to both the backfill and the live call.

### Question 78 — C, D

Answers: Read the historical features from the offline store; Serve the feature from the online store. The offline store returns point-in-time values, and the online store returns the latest value. The offline store returns point-in-time values for training. The online store returns the latest feature value at low latency for a single entity. Local study-map skill 5.3 (Train and Serve Consistency), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. In-memory processing is the simplest option and stops working once the data exceeds the worker memory. Why the correct answer wins: The offline store returns point-in-time values, and the online store returns the latest value.
- **B:** Incorrect for this question. Deduplicating at ingest stops duplicated records inflating the training set. Why the correct answer wins: The offline store returns point-in-time values, and the online store returns the latest value.
- **C:** Correct. The offline store returns point-in-time values for training. In this case: The offline store returns point-in-time values, and the online store returns the latest value.
- **D:** Correct. The online store returns the latest feature value at low latency for a single entity. In this case: The offline store returns point-in-time values, and the online store returns the latest value.
- **E:** Incorrect for this question. The registry versions the model artifact and links it to its lineage and metrics. Why the correct answer wins: The offline store returns point-in-time values, and the online store returns the latest value.

### Question 79 — B

Answer: Enable step caching. Caching skips an unchanged step on a rerun. Local study-map skill 5.3 (Train and Serve Consistency), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The gate promotes a model only when it beats the incumbent on the agreed metric. Why the correct answer wins: Caching skips an unchanged step on a rerun.
- **B:** Correct. In this case: Caching skips an unchanged step on a rerun.
- **C:** Incorrect for this question. Drift-triggered retraining responds to change instead of to the calendar. Why the correct answer wins: Caching skips an unchanged step on a rerun.
- **D:** Incorrect for this question. A validation step stops a bad batch before it reaches training. Why the correct answer wins: Caching skips an unchanged step on a rerun.

### Question 80 — D

Answer: Share one transformation library between training and serving. Shared code removes the class of bug where paths differ. Shared code removes the class of bug where the two paths compute a feature differently. Local study-map skill 5.3 (Train and Serve Consistency), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. An alias decouples the served version name from the artifact id, so a rollback is a pointer move. Why the correct answer wins: Shared code removes the class of bug where paths differ.
- **B:** Incorrect for this question. A validation step stops a bad batch before it reaches training. Why the correct answer wins: Shared code removes the class of bug where paths differ.
- **C:** Incorrect for this question. Feature Store keeps one definition that both training and serving read. Why the correct answer wins: Shared code removes the class of bug where paths differ.
- **D:** Correct. Shared code removes the class of bug where the two paths compute a feature differently. In this case: Shared code removes the class of bug where paths differ.

### Question 81 — B

Answer: Retrain on a fixed schedule. A fixed schedule is simple to reason about when data changes predictably. Local study-map skill 5.4 (Retraining Policy), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Metric-triggered retraining reacts to actual quality loss. Why the correct answer wins: A fixed schedule is simple to reason about when data changes predictably.
- **B:** Correct. In this case: A fixed schedule is simple to reason about when data changes predictably.
- **C:** Incorrect for this question. Drift-triggered retraining responds to change instead of to the calendar. Why the correct answer wins: A fixed schedule is simple to reason about when data changes predictably.
- **D:** Incorrect for this question. Manual retraining leaves the model stale whenever the trigger is forgotten. Why the correct answer wins: A fixed schedule is simple to reason about when data changes predictably.

### Question 82 — D

Answer: Retrain when drift crosses the threshold. Drift-triggered retraining responds to change instead of the calendar. Local study-map skill 5.4 (Retraining Policy), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Manual retraining leaves the model stale whenever the trigger is forgotten. Why the correct answer wins: Drift-triggered retraining responds to change instead of the calendar.
- **B:** Incorrect for this question. Metric-triggered retraining reacts to actual quality loss. Why the correct answer wins: Drift-triggered retraining responds to change instead of the calendar.
- **C:** Incorrect for this question. A fixed schedule is simple to reason about when the data changes predictably. Why the correct answer wins: Drift-triggered retraining responds to change instead of the calendar.
- **D:** Correct. In this case: Drift-triggered retraining responds to change instead of the calendar.

### Question 83 — C

Answer: Extend CI/CD into continuous training. Continuous training adds the retrain and the validate step to the same path. Local study-map skill 5.4 (Retraining Policy), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: Continuous training adds the retrain and the validate step to the same path.
- **B:** Incorrect for this question. An event trigger retrains when data lands instead of on a fixed clock. Why the correct answer wins: Continuous training adds the retrain and the validate step to the same path.
- **C:** Correct. In this case: Continuous training adds the retrain and the validate step to the same path.
- **D:** Incorrect for this question. Manual retraining leaves the model stale whenever the trigger is forgotten. Why the correct answer wins: Continuous training adds the retrain and the validate step to the same path.

### Question 84 — B

Answer: Trigger the pipeline from the arrival of new data. An event trigger retrains when data lands. Local study-map skill 5.5 (CI/CD/CT with Cloud Build), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The scheduler starts the pipeline on the cadence the retraining policy defines. Why the correct answer wins: An event trigger retrains when data lands.
- **B:** Correct. In this case: An event trigger retrains when data lands.
- **C:** Incorrect for this question. Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance. Why the correct answer wins: An event trigger retrains when data lands.
- **D:** Incorrect for this question. Manual retraining leaves the model stale whenever the trigger is forgotten. Why the correct answer wins: An event trigger retrains when data lands.

### Question 85 — C

Answer: Gate the deployment on a model evaluation threshold. The gate promotes a model only when it beats the incumbent. Local study-map skill 5.5 (CI/CD/CT with Cloud Build), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Drift-triggered retraining responds to change instead of to the calendar. Why the correct answer wins: The gate promotes a model only when it beats the incumbent.
- **B:** Incorrect for this question. A validation step stops a bad batch before it reaches training. Why the correct answer wins: The gate promotes a model only when it beats the incumbent.
- **C:** Correct. In this case: The gate promotes a model only when it beats the incumbent.
- **D:** Incorrect for this question. Caching skips an unchanged step on a rerun and shortens the pipeline. Why the correct answer wins: The gate promotes a model only when it beats the incumbent.

### Question 86 — D

Answer: Retrain when the production metric drops. Metric-triggered retraining reacts to actual quality loss. Local study-map skill 5.5 (CI/CD/CT with Cloud Build), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Drift-triggered retraining responds to change instead of to the calendar. Why the correct answer wins: Metric-triggered retraining reacts to actual quality loss.
- **B:** Incorrect for this question. A fixed schedule is simple to reason about when the data changes predictably. Why the correct answer wins: Metric-triggered retraining reacts to actual quality loss.
- **C:** Incorrect for this question. Manual retraining leaves the model stale whenever the trigger is forgotten. Why the correct answer wins: Metric-triggered retraining reacts to actual quality loss.
- **D:** Correct. In this case: Metric-triggered retraining reacts to actual quality loss.

### Question 87 — A

Answer: Orchestrate the steps in Agent Platform Pipelines. Pipelines runs the steps on managed infrastructure with lineage per artifact. Pipelines runs each step as a container with caching, lineage, and retry. Local study-map skill 5.2 (Pipeline Orchestration Choice), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 5 (automating and orchestrating ML pipelines): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. Pipelines runs each step as a container with caching, lineage, and retry. In this case: Pipelines runs the steps on managed infrastructure with lineage per artifact.
- **B:** Incorrect for this question. Kubeflow pipelines give a container-per-step pipeline that runs on the managed service or on GKE. Why the correct answer wins: Pipelines runs the steps on managed infrastructure with lineage per artifact.
- **C:** Incorrect for this question. Ray fits a Python-native distributed workload that is not a container-per-step pipeline. Why the correct answer wins: Pipelines runs the steps on managed infrastructure with lineage per artifact.
- **D:** Incorrect for this question. Airflow expresses cross-system dependencies and schedules outside the ML platform. Why the correct answer wins: Pipelines runs the steps on managed infrastructure with lineage per artifact.

### Question 88 — C, E

Answers: Screen the prompts and responses with Model Armor; Redact the pattern-matchable fields with a regex. Model Armor detects prompt injection, and a regex removes identifiers before the prompt leaves. Model Armor detects prompt injection, jailbreak attempts, and unsafe content. A regex removes a known identifier pattern before the prompt leaves the service. Local study-map skill 6.1 (Secure AI and Prompt Protection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A schema stops the model returning free text that downstream code cannot parse. Why the correct answer wins: Model Armor detects prompt injection, and a regex removes identifiers before the prompt leaves.
- **B:** Incorrect for this question. A system instruction states what the assistant must refuse, though it is not a security control on its own. Why the correct answer wins: Model Armor detects prompt injection, and a regex removes identifiers before the prompt leaves.
- **C:** Correct. A regex removes a known identifier pattern before the prompt leaves the service. In this case: Model Armor detects prompt injection, and a regex removes identifiers before the prompt leaves.
- **D:** Incorrect for this question. Safety filters block categories of harmful output at the model call. Why the correct answer wins: Model Armor detects prompt injection, and a regex removes identifiers before the prompt leaves.
- **E:** Correct. Model Armor detects prompt injection, jailbreak attempts, and unsafe content. In this case: Model Armor detects prompt injection, and a regex removes identifiers before the prompt leaves.

### Question 89 — A

Answer: Configure the model safety filters. Safety filters block categories of harmful output at the model call. Local study-map skill 6.1 (Secure AI and Prompt Protection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Safety filters block categories of harmful output at the model call.
- **B:** Incorrect for this question. A regex removes a known identifier pattern before the prompt leaves the service. Why the correct answer wins: Safety filters block categories of harmful output at the model call.
- **C:** Incorrect for this question. A schema stops the model returning free text that downstream code cannot parse. Why the correct answer wins: Safety filters block categories of harmful output at the model call.
- **D:** Incorrect for this question. Model Armor detects prompt injection, jailbreak attempts, and unsafe content. Why the correct answer wins: Safety filters block categories of harmful output at the model call.

### Question 90 — C

Answer: Constrain the response to a JSON schema. A schema stops the model returning free text. Local study-map skill 6.1 (Secure AI and Prompt Protection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Safety filters block categories of harmful output at the model call. Why the correct answer wins: A schema stops the model returning free text.
- **B:** Incorrect for this question. Model Armor detects prompt injection, jailbreak attempts, and unsafe content. Why the correct answer wins: A schema stops the model returning free text.
- **C:** Correct. In this case: A schema stops the model returning free text.
- **D:** Incorrect for this question. A system instruction states what the assistant must refuse, though it is not a security control on its own. Why the correct answer wins: A schema stops the model returning free text.

### Question 91 — A

Answer: Slice the evaluation metrics by the sensitive attribute. A sliced metric shows a gap the aggregate hides. Local study-map skill 6.2 (Responsible AI and Bias), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: A sliced metric shows a gap the aggregate hides.
- **B:** Incorrect for this question. The card states where the model may be used and where it must not. Why the correct answer wins: A sliced metric shows a gap the aggregate hides.
- **C:** Incorrect for this question. The card records provenance, intended use, and known gaps for the dataset. Why the correct answer wins: A sliced metric shows a gap the aggregate hides.
- **D:** Incorrect for this question. A per-group outcome rate is the first evidence of disparate impact. Why the correct answer wins: A sliced metric shows a gap the aggregate hides.

### Question 92 — A

Answer: Publish a model card with the intended use and limits. The card states where the model may be used. Local study-map skill 6.2 (Responsible AI and Bias), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: The card states where the model may be used.
- **B:** Incorrect for this question. A per-group outcome rate is the first evidence of disparate impact. Why the correct answer wins: The card states where the model may be used.
- **C:** Incorrect for this question. A sliced metric shows a gap that the aggregate metric hides. Why the correct answer wins: The card states where the model may be used.
- **D:** Incorrect for this question. The card records provenance, intended use, and known gaps for the dataset. Why the correct answer wins: The card states where the model may be used.

### Question 93 — A

Answer: Use integrated gradients for the image model. Integrated gradients attributes an image prediction to its pixels. Local study-map skill 6.3 (Explainability), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Integrated gradients attributes an image prediction to its pixels.
- **B:** Incorrect for this question. ML.GLOBAL_EXPLAIN ranks the features that matter most across the whole model. Why the correct answer wins: Integrated gradients attributes an image prediction to its pixels.
- **C:** Incorrect for this question. Sampled Shapley explains individual online predictions with a bounded compute cost. Why the correct answer wins: Integrated gradients attributes an image prediction to its pixels.
- **D:** Incorrect for this question. Shapley values attribute a prediction to its features with a consistent baseline. Why the correct answer wins: Integrated gradients attributes an image prediction to its pixels.

### Question 94 — B

Answer: Choose an inherently interpretable model. A linear or tree model can be read directly. Local study-map skill 6.3 (Explainability), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. Attribution shows which inputs drove the decision in the case the reviewer is examining. Why the correct answer wins: A linear or tree model can be read directly.
- **B:** Correct. In this case: A linear or tree model can be read directly.
- **C:** Incorrect for this question. Shapley values attribute a prediction to its features with a consistent baseline. Why the correct answer wins: A linear or tree model can be read directly.
- **D:** Incorrect for this question. Sampled Shapley explains individual online predictions with a bounded compute cost. Why the correct answer wins: A linear or tree model can be read directly.

### Question 95 — C

Answer: Route the monitoring alert to the owning team. An alert with no owner is a dashboard nobody reads. Local study-map skill 6.4 (Model Monitoring Configuration), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. The threshold expresses how much drift the business can absorb before someone acts. Why the correct answer wins: An alert with no owner is a dashboard nobody reads.
- **B:** Incorrect for this question. A percentile latency per version shows a regression that an average hides. Why the correct answer wins: An alert with no owner is a dashboard nobody reads.
- **C:** Correct. In this case: An alert with no owner is a dashboard nobody reads.
- **D:** Incorrect for this question. Continuous sampling catches quality regressions that drift metrics cannot see. Why the correct answer wins: An alert with no owner is a dashboard nobody reads.

### Question 96 — C

Answer: Enable Model Monitoring on the endpoint. Model Monitoring compares live traffic with the training profile. Model Monitoring compares live traffic with the training baseline and reports skew and drift. Local study-map skill 6.4 (Model Monitoring Configuration), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. An alert with no owner is a dashboard nobody reads. Why the correct answer wins: Model Monitoring compares live traffic with the training profile.
- **B:** Incorrect for this question. Redacted logs make a bad answer diagnosable without storing sensitive text. Why the correct answer wins: Model Monitoring compares live traffic with the training profile.
- **C:** Correct. Model Monitoring compares live traffic with the training baseline and reports skew and drift. In this case: Model Monitoring compares live traffic with the training profile.
- **D:** Incorrect for this question. A percentile latency per version shows a regression that an average hides. Why the correct answer wins: Model Monitoring compares live traffic with the training profile.

### Question 97 — A, D

Answers: Watch for training-serving skew; Watch for data drift. Skew compares live features with training features, and data drift is a change in the input distribution. Skew compares the live feature distribution with the training distribution. Data drift is a change in the input distribution after the model shipped. Local study-map skill 6.5 (Skew and Drift Types), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. Data drift is a change in the input distribution after the model shipped. In this case: Skew compares live features with training features, and data drift is a change in the input distribution.
- **B:** Incorrect for this question. Concept drift is a change in the relationship between the features and the target. Why the correct answer wins: Skew compares live features with training features, and data drift is a change in the input distribution.
- **C:** Incorrect for this question. Attribution drift is a change in which features drive the prediction. Why the correct answer wins: Skew compares live features with training features, and data drift is a change in the input distribution.
- **D:** Correct. Skew compares the live feature distribution with the training distribution. In this case: Skew compares live features with training features, and data drift is a change in the input distribution.
- **E:** Incorrect for this question. Without the labelled outcome, quality can only be inferred from the inputs and outputs. Why the correct answer wins: Skew compares live features with training features, and data drift is a change in the input distribution.

### Question 98 — D

Answer: Watch for concept drift. Concept drift is a change in the relationship between features and the target. Local study-map skill 6.5 (Skew and Drift Types), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Incorrect for this question. A shift in the output distribution is often the first visible symptom. Why the correct answer wins: Concept drift is a change in the relationship between features and the target.
- **B:** Incorrect for this question. Attribution drift is a change in which features drive the prediction. Why the correct answer wins: Concept drift is a change in the relationship between features and the target.
- **C:** Incorrect for this question. Data drift is a change in the input distribution after the model shipped. Why the correct answer wins: Concept drift is a change in the relationship between features and the target.
- **D:** Correct. In this case: Concept drift is a change in the relationship between features and the target.

### Question 99 — A

Answer: Score a sample of live answers with the evaluation rubric. Continuous sampling catches quality regressions that drift metrics cannot see. Local study-map skill 6.6 (Generative AI Monitoring), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: Continuous sampling catches quality regressions that drift metrics cannot see.
- **B:** Incorrect for this question. Model Monitoring compares live traffic with the training baseline and reports skew and drift. Why the correct answer wins: Continuous sampling catches quality regressions that drift metrics cannot see.
- **C:** Incorrect for this question. Token accounting attributes generative cost to the feature that caused it. Why the correct answer wins: Continuous sampling catches quality regressions that drift metrics cannot see.
- **D:** Incorrect for this question. A percentile latency per version shows a regression that an average hides. Why the correct answer wins: Continuous sampling catches quality regressions that drift metrics cannot see.

### Question 100 — A

Answer: Redact the pattern-matchable fields with a regex. A regex removes a known identifier pattern before the prompt leaves. Local study-map skill 6.1 (Secure AI and Prompt Protection), mapped to the official guide: Google Cloud Professional Machine Learning Engineer exam guide as of June 1, 2026. Primary reference: Professional Machine Learning Engineer exam guide, section 6 (monitoring AI solutions): https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf.

- **A:** Correct. In this case: A regex removes a known identifier pattern before the prompt leaves.
- **B:** Incorrect for this question. Model Armor detects prompt injection, jailbreak attempts, and unsafe content. Why the correct answer wins: A regex removes a known identifier pattern before the prompt leaves.
- **C:** Incorrect for this question. Safety filters block categories of harmful output at the model call. Why the correct answer wins: A regex removes a known identifier pattern before the prompt leaves.
- **D:** Incorrect for this question. A schema stops the model returning free text that downstream code cannot parse. Why the correct answer wins: A regex removes a known identifier pattern before the prompt leaves.
