"""Option bank for the Professional Machine Learning Engineer practice course.

One label and one meaning per answer or distractor. Keys are stable and
referenced by questions/*.txt; build.py rejects an unknown key.
"""
TERMS = {}


def t(key, label, meaning):
    if key in TERMS:
        raise ValueError(f'Duplicate term: {key}')
    TERMS[key] = (label, meaning)


# ------------------------------------------------------------- BigQuery ML
t('bqml_logistic', 'Create a BigQuery ML logistic regression model',
  'Logistic regression predicts a binary outcome and trains inside BigQuery with SQL.')
t('bqml_linear', 'Create a BigQuery ML linear regression model',
  'Linear regression predicts a continuous value such as revenue or demand.')
t('bqml_kmeans', 'Create a BigQuery ML k-means model',
  'K-means segments rows into unsupervised clusters without a labelled target.')
t('bqml_arima', 'Create a BigQuery ML ARIMA_PLUS time series model',
  'ARIMA_PLUS models seasonality and trend and returns a forecast interval per period.')
t('bqml_boosted', 'Create a BigQuery ML boosted tree classifier',
  'Boosted trees capture non-linear interactions in tabular data while staying in SQL.')
t('bqml_dnn', 'Create a BigQuery ML deep neural network',
  'The DNN model type fits non-linear patterns too complex for a linear model.')
t('bqml_automl', 'Create a BigQuery ML AutoML model',
  'The AutoML model type in BigQuery ML searches architectures without leaving SQL.')
t('bqml_transform', 'Declare the feature transformations in the TRANSFORM clause',
  'TRANSFORM keeps preprocessing inside the model, so prediction applies the same steps.')
t('bqml_predict', 'Score the rows with ML.PREDICT',
  'ML.PREDICT applies a trained model and returns the label and its probability.')
t('bqml_evaluate', 'Inspect the metrics with ML.EVALUATE',
  'ML.EVALUATE returns the model metrics against a labelled dataset.')
t('bqml_explain', 'Read the contribution of each feature with ML.EXPLAIN_PREDICT',
  'ML.EXPLAIN_PREDICT attributes each prediction to the features that moved it.')
t('bqml_global_explain', 'Summarise the model with ML.GLOBAL_EXPLAIN',
  'ML.GLOBAL_EXPLAIN ranks the features that matter most across the whole model.')
t('bqml_remote_gemini', 'Create a BigQuery ML remote model over Gemini',
  'A remote model calls the Gemini endpoint from SQL, so generation runs where the data lives.')
t('bqml_finetune', 'Fine-tune a Gemini model from BigQuery',
  'Fine-tuning adapts a foundation model to the domain using rows that stay in BigQuery.')
t('bqml_import', 'Import the TensorFlow model into BigQuery ML',
  'Importing brings an already-trained model into BigQuery so SQL can score it.')
t('bqml_connection', 'Create the Cloud resource connection for the remote model',
  'A remote model needs a connection and its service account before it can call an endpoint.')
t('bqml_slot_reservation', 'Reserve BigQuery slots for the training job',
  'Training consumes slots, so a reservation bounds the cost and the wait time.')
t('bqml_json', 'Store the predictions in a nested JSON column',
  'A nested column keeps per-row structured output such as labels and scores together.')

# ------------------------------------------------------------- AutoML and Agent Platform
t('automl_tabular', 'Train an Agent Platform AutoML tabular model',
  'AutoML tabular selects the architecture and tuning for a structured dataset.')
t('automl_image', 'Train an Agent Platform AutoML image model',
  'AutoML image trains classification or object detection from labelled images.')
t('automl_text', 'Train an Agent Platform AutoML text model',
  'AutoML text trains classification, extraction, or sentiment from labelled text.')
t('automl_forecast', 'Train an Agent Platform AutoML forecasting model',
  'AutoML forecasting builds a time series model with covariates and backtesting.')
t('automl_no_code', 'Use AutoML so the team needs no modelling code',
  'AutoML is the no-code path, which matters when the team has data skills but no ML engineers.')
t('automl_budget', 'Set a training budget in node hours',
  'A node-hour budget caps how long AutoML searches, which bounds the cost.')
t('automl_export', 'Export the AutoML model as an artifact',
  'Export produces a container-ready artifact that can be served outside the managed endpoint.')
t('automl_split', 'Let AutoML choose the data split',
  'AutoML uses a reproducible default split when the dataset is large enough to do so.')
t('automl_manual_split', 'Define a manual split column with train, validation, and test',
  'A manual split is required when the split must follow time or a grouping column.')
t('automl_disable_early_stopping', 'Disable early stopping for the final run',
  'Turning early stopping off for the last run lets the model use the full budget.')
t('agent_platform', 'Use Gemini Enterprise Agent Platform',
  'Agent Platform is the current name for the managed ML platform that hosts training, pipelines, registry, and endpoints.')
t('model_registry', 'Register the model in Agent Platform Model Registry',
  'The registry versions the model artifact and links it to its lineage and metrics.')
t('model_garden', 'Select the model from Model Garden',
  'Model Garden lists first-party and open models with their deployment and licensing options.')
t('gemini_pro', 'Choose the larger Gemini model for quality',
  'The larger model gives the best reasoning quality at a higher cost per token.')
t('gemini_flash', 'Choose the smaller Gemini model for latency and cost',
  'The smaller model answers faster and cheaper, which suits high-volume simple tasks.')
t('gemini_multimodal', 'Send the image and the question in one multimodal request',
  'A multimodal request removes the need for a separate captioning or OCR stage.')
t('imagen', 'Generate the images with Imagen',
  'Imagen is the text-to-image model in the Google Cloud generative AI family.')
t('veo', 'Generate the video with Veo',
  'Veo is the text-to-video model family offered through the platform.')
t('embedding_api', 'Embed the documents with the text embedding model',
  'Embeddings turn text into vectors, which is what a retrieval step searches.')
t('open_model_garden', 'Deploy an open-weight model from Model Garden',
  'An open-weight model can be tuned and self-hosted when a proprietary endpoint does not fit.')

# ------------------------------------------------------------- industry APIs
t('document_ai', 'Use Document AI with a specialised processor',
  'A Document AI processor extracts structured fields from forms with layout awareness.')
t('vision_api', 'Use the Vision API',
  'The prebuilt Vision model labels, detects, and reads text without training a model.')
t('translate_api', 'Use the Translation API',
  'The translation model handles a large language set without custom training.')
t('speech_api', 'Use the Speech-to-Text API',
  'The speech model transcribes audio, including domain phrases through adaptation.')
t('video_intelligence', 'Use the Video Intelligence API',
  'Video Intelligence detects shots, labels, and explicit content in video.')
t('nlp_api', 'Use the Natural Language API',
  'The Natural Language API returns entities, sentiment, and syntax without a custom model.')
t('api_no_training', 'Call the prebuilt API rather than training a model',
  'When the task is a standard perception or language task, the prebuilt API is faster and cheaper than training.')

# ------------------------------------------------------------- Gemini app optimization
t('context_caching', 'Cache the long shared context',
  'Context caching bills the repeated prefix once instead of on every request.')
t('batch_prediction_api', 'Send the offline work through the batch API',
  'The batch path trades latency for a lower price on non-interactive requests.')
t('stream_response', 'Stream the response tokens to the client',
  'Streaming improves perceived latency without reducing total generation time.')
t('reduce_output_tokens', 'Constrain the output with a schema and a token limit',
  'A bounded output cuts both latency and cost per request.')
t('retrieval_grounding', 'Ground the answer in retrieved documents',
  'Grounding reduces unsupported answers and keeps the prompt short.')
t('regional_endpoint', 'Call the model in the region that serves the users',
  'A regional endpoint removes cross-region latency and satisfies residency rules.')
t('quota_increase', 'Request a quota increase for the model',
  'Throughput is capped by quota, so a quota ceiling cannot be solved by retries.')
t('fallback_model', 'Fall back to a smaller model when the primary is throttled',
  'A fallback keeps the application answering when the primary model returns resource-exhausted.')

# ------------------------------------------------------------- data preprocessing
t('bigquery_sql', 'Preprocess in BigQuery with SQL',
  'SQL over BigQuery is the cheapest option when the data already sits there and the logic is set-based.')
t('dataflow_pipeline', 'Preprocess with a Dataflow pipeline',
  'Dataflow runs the same Beam code in batch and streaming and scales without provisioning.')
t('dataproc_spark', 'Preprocess with Spark on Dataproc',
  'Spark suits large transformations the team already has as Scala or PySpark code.')
t('in_memory_pandas', 'Preprocess in memory with pandas',
  'In-memory processing is the simplest option and stops working once the data exceeds the worker memory.')
t('dataplex', 'Catalog and profile the data with Dataplex',
  'Dataplex discovers, profiles, and applies policy across the lakehouse in one control plane.')
t('pii_dlp', 'De-identify the fields with Sensitive Data Protection',
  'Sensitive Data Protection finds and redacts, tokenizes, or format-preservingly encrypts PII.')
t('pii_hash', 'Hash the identifiers with a salted key before training',
  'A salted hash keeps the join key usable while removing the direct identifier.')
t('pii_drop', 'Drop the identifier columns before the training dataset is written',
  'Dropping the field removes the exposure entirely when the model does not need it.')
t('pii_bucket', 'Restrict the raw bucket to a privileged service account',
  'Restricting the bucket limits who can copy the raw data in the first place.')
t('data_split_time', 'Split the data by time rather than at random',
  'A time-based split prevents the model from learning from the future.')
t('data_split_group', 'Split by entity so one customer never spans train and test',
  'Grouping the split prevents leakage between the training and evaluation rows.')
t('data_leakage', 'Remove the post-outcome column from the features',
  'A column written after the outcome encodes the answer and inflates the score.')

# ------------------------------------------------------------- features and Feature Store
t('feature_store', 'Register the feature in Agent Platform Feature Store',
  'Feature Store keeps one definition that both training and serving read.')
t('feature_store_online', 'Serve the feature from the online store',
  'The online store returns the latest feature value at low latency for a single entity.')
t('feature_store_batch', 'Read the historical features from the offline store',
  'The offline store returns point-in-time values for training.')
t('feature_monitoring', 'Enable feature monitoring on the feature group',
  'Feature monitoring reports distribution changes per feature, not just per model.')
t('feature_cross', 'Add a crossed feature for the interacting pair',
  'A crossed feature lets a linear model express the interaction it cannot learn alone.')
t('feature_normalize', 'Normalise the numeric feature before training',
  'Scaling keeps one large-magnitude feature from dominating the gradient.')
t('feature_bucketize', 'Bucketize the continuous feature',
  'Bucketing converts a non-linear relationship into a form a linear model can fit.')

# ------------------------------------------------------------- notebooks and environments
t('workbench', 'Use an Agent Platform Workbench instance',
  'Workbench is the managed notebook instance inside the project VPC.')
t('colab_enterprise', 'Use Colab Enterprise',
  'Colab Enterprise adds managed runtimes, VPC connectivity, and IAM to the Colab experience.')
t('notebook_private_ip', 'Create the runtime with no public IP',
  'A private-IP runtime reaches the data through the VPC and cannot be opened from the internet.')
t('notebook_idle_shutdown', 'Set an idle shutdown schedule',
  'Idle shutdown stops paying for a notebook nobody is using.')
t('notebook_managed_container', 'Pin the runtime to a custom container image',
  'A pinned image makes the environment reproducible across users.')
t('notebook_shared_vpc', 'Attach the runtime to the shared VPC subnet',
  'The subnet attachment gives the notebook the route to internal data sources.')

# ------------------------------------------------------------- experiments and metadata
t('experiments', 'Log the run to Agent Platform Experiments',
  'Experiments records parameters, metrics, and artifacts per run so runs can be compared.')
t('ml_metadata', 'Track artifacts and lineage in ML Metadata',
  'ML Metadata records which data and code produced which artifact.')
t('kubeflow_pipelines', 'Express the workflow as a Kubeflow pipeline',
  'Kubeflow pipelines give a container-per-step pipeline that runs on the managed service or on GKE.')
t('pipeline_templates', 'Start from a Google-provided pipeline template',
  'A template encodes the validated step order, so the first pipeline is not bespoke.')
t('experiment_compare', 'Compare the runs on the validation metric',
  'Comparing on the validation metric keeps model selection independent of the test set.')
t('experiment_seed', 'Set the random seed in the training code',
  'A fixed seed makes a rerun reproducible when the rest of the environment is pinned.')

# ------------------------------------------------------------- evaluation
t('auc_pr', 'Report precision-recall AUC for the rare class',
  'Precision-recall AUC stays informative when the positive class is rare.')
t('roc_auc', 'Report ROC AUC',
  'ROC AUC measures ranking quality across thresholds and hides class imbalance.')
t('confusion_matrix', 'Inspect the confusion matrix at the operating threshold',
  'The matrix shows the false-positive and false-negative split the business will feel.')
t('threshold_tuning', 'Choose the threshold from the cost of each error type',
  'The decision threshold follows the relative cost of a false positive and a false negative.')
t('rmse', 'Report RMSE for the regression target',
  'RMSE expresses the typical error in the units of the target.')
t('mape', 'Report MAPE when the error must be read as a percentage',
  'MAPE expresses the error relative to the actual value, which business readers understand.')
t('llm_judge', 'Score the answers with an LLM-as-a-judge rubric',
  'A rubric-driven judge scales the evaluation of free-text answers beyond human review.')
t('human_review', 'Sample the answers for expert human review',
  'Human review remains the reference standard for a sample the judge is calibrated against.')
t('groundedness', 'Measure groundedness against the retrieved context',
  'Groundedness checks whether each claim is supported by the documents that were retrieved.')
t('toxicity_metric', 'Measure the safety metrics on a fixed prompt set',
  'A fixed prompt set makes the safety score comparable between releases.')
t('test_set_lock', 'Keep the test set out of every tuning decision',
  'A test set that has been used for tuning no longer estimates generalisation.')

# ------------------------------------------------------------- model and product choice
t('model_arima', 'Choose a classical time series model',
  'A classical time series model suits a single series with strong seasonality and little covariate data.')
t('model_dnn', 'Choose a deep neural network',
  'A DNN suits a large tabular or unstructured dataset where interactions matter.')
t('model_llm', 'Choose a foundation model',
  'A foundation model suits an open-ended language or multimodal task where labelled data is scarce.')
t('model_tabnet', 'Use TabNet as the custom training algorithm',
  'TabNet gives an interpretable attentive tabular model inside custom training.')
t('bigquery_ml_product', 'Build the model in BigQuery ML',
  'BigQuery ML keeps training next to the data and removes a separate serving pipeline.')
t('automl_product', 'Train with Agent Platform AutoML',
  'AutoML removes architecture search and tuning from the team while keeping a managed endpoint.')
t('custom_product', 'Train a custom model on Agent Platform',
  'Custom training keeps full control of the framework and the loss.')
t('product_by_skill', 'Choose the product the team can actually operate',
  'A product the team cannot debug becomes an outage with a schedule.')

# ------------------------------------------------------------- interpretability
t('shap', 'Explain with Shapley values',
  'Shapley values attribute a prediction to its features with a consistent baseline.')
t('sampled_shapley', 'Use sampled Shapley on the endpoint',
  'Sampled Shapley explains individual online predictions with a bounded compute cost.')
t('integrated_gradients', 'Use integrated gradients for the image model',
  'Integrated gradients attributes an image prediction to the pixels that moved it.')
t('explainable_model', 'Choose an inherently interpretable model',
  'A linear or tree model can be read directly when regulation demands an explanation by construction.')
t('feature_attribution', 'Report the feature attributions to the reviewer',
  'Attribution shows which inputs drove the decision in the case the reviewer is examining.')

# ------------------------------------------------------------- deployment strategies
t('deployment_canary', 'Roll out a canary with a small traffic share',
  'A canary limits the blast radius while the new model is compared with the old one.')
t('deployment_ab', 'Split traffic between two models in an A/B test',
  'A/B testing compares two models on the same population with a traffic split.')
t('deployment_shadow', 'Run the new model in shadow mode',
  'Shadow mode scores live traffic without serving its answers, so the comparison costs nothing to users.')
t('deployment_blue_green', 'Deploy blue/green with an instant switch',
  'Two identical deployments let the switch be reversed immediately.')
t('deployment_rolling', 'Replace the model version in place',
  'An in-place replacement exposes every request to the new version at once.')

# ------------------------------------------------------------- training data and ingestion
t('gcs_tfrecord', 'Write the training data as TFRecord shards in Cloud Storage',
  'Sharded TFRecord is the efficient read format for distributed training.')
t('gcs_parquet', 'Write the training data as Parquet in Cloud Storage',
  'Parquet is columnar and cheap to scan for tabular training data.')
t('bigquery_source', 'Read the training data directly from BigQuery',
  'Reading from BigQuery avoids a copy and keeps the query pushdown.')
t('dataflow_ingest', 'Stream the new records through Dataflow into the training store',
  'A streaming path keeps the training data current without a nightly copy.')
t('ingest_dedup', 'Deduplicate on the event key in the ingestion step',
  'Deduplicating at ingest stops duplicated records inflating the training set.')
t('ingest_validate', 'Validate the schema and quarantine rejected rows',
  'Rejecting rows into a side table makes a schema break visible instead of silent.')

# ------------------------------------------------------------- custom training and tuning
t('custom_container', 'Run a custom container on Agent Platform',
  'A custom container carries its own framework and dependencies into the managed training job.')
t('python_package', 'Package the trainer as a Python package',
  'The prebuilt container installs the package, which is the lightest way to run custom code.')
t('distributed_reduction', 'Set the reduction server for the all-reduce',
  'The reduction server offloads gradient aggregation and shortens the training step.')
t('training_spot', 'Use Spot VMs for the training workers with checkpointing',
  'Spot workers cut the cost of a long job that can resume from a checkpoint.')
t('hyperparameter_tuning', 'Run a hyperparameter tuning job',
  'The tuning service searches the space in parallel and reports the best trial.')
t('tuning_bayesian', 'Choose Bayesian optimisation for the search',
  'Bayesian search spends fewer trials to reach a good configuration.')
t('tuning_budget', 'Cap the search with a trial count and a parallel budget',
  'The budget bounds both the cost and the wall-clock time of the search.')
t('tuning_early_stop', 'Enable early stopping of poor trials',
  'Early stopping frees capacity from trials that cannot win.')
t('tuning_custom_metric', 'Report the business metric from the trainer',
  'The search optimises the metric the trainer reports, so it must be the one that matters.')

# ------------------------------------------------------------- fine-tuning decisions
t('finetune_lora', 'Fine-tune with a parameter-efficient adapter',
  'A parameter-efficient adapter trains a small number of weights and keeps the base model intact.')
t('finetune_full', 'Fine-tune the full model',
  'Full fine-tuning updates every weight and needs the most data and accelerator memory.')
t('rag_instead', 'Ground the prompt with retrieval instead of fine-tuning',
  'Retrieval is the cheaper answer when the problem is missing knowledge rather than missing behaviour.')
t('prompt_engineering', 'Start with prompt and context engineering',
  'A better prompt is the cheapest experiment and often removes the need to tune at all.')
t('finetune_when_style', 'Fine-tune when the model must follow a house style or output contract',
  'Tuning changes behaviour; retrieval changes knowledge. Style and format are behaviour.')
t('distillation', 'Distil the large model into a smaller one',
  'Distillation moves the quality of the teacher into a model cheap enough to serve.')

# ------------------------------------------------------------- hardware and distributed
t('tpu_slice', 'Train on a TPU slice',
  'A TPU slice gives a tightly coupled accelerator fabric for large synchronous training.')
t('gpu_a100', 'Train on A100 GPUs',
  'A100 GPUs suit mixed-precision training where the framework expects CUDA.')
t('gpu_l4', 'Serve on L4 GPUs',
  'An L4 GPU gives low-cost inference acceleration for a modest model.')
t('cpu_only', 'Serve on CPU only',
  'CPU serving is the cheapest option for a small model with a generous latency budget.')
t('edge_tpu', 'Deploy to an Edge TPU device',
  'An Edge TPU runs a quantised model on-device where the network cannot be relied on.')
t('multi_worker', 'Configure the job as multi-worker with a chief',
  'Multi-worker gives each replica a shard of the data and a defined chief.')
t('data_parallel', 'Use data parallelism',
  'Data parallelism replicates the model and splits each batch across the workers.')
t('model_parallel', 'Use model parallelism',
  'Model parallelism splits the layers across devices when one model does not fit on one.')
t('batch_size_scale', 'Scale the batch size with the worker count',
  'A larger global batch keeps each worker busy after the split.')
t('checkpoint_restart', 'Checkpoint to Cloud Storage and resume from the last step',
  'A checkpoint turns a preemption into a delay rather than a restart.')

# ------------------------------------------------------------- training troubleshooting
t('oom_reduce_batch', 'Reduce the per-replica batch size',
  'The out-of-memory error is a memory-per-step problem, so the batch is the first lever.')
t('oom_gradient_checkpointing', 'Enable gradient checkpointing',
  'Checkpointing trades recomputation for activation memory.')
t('nan_learning_rate', 'Lower the learning rate',
  'A loss that becomes NaN usually reflects a step size too large for the data scale.')
t('data_shard_missing', 'Verify each worker reads a distinct shard',
  'Duplicated shards silently shrink the effective dataset and skew the loss.')
t('permission_error', 'Grant the training service account access to the bucket',
  'A permission error on the input is a missing IAM binding, not a model problem.')
t('version_mismatch', 'Pin the framework version in the container',
  'A framework mismatch between local and remote runs changes behaviour without changing the code.')
t('quota_error', 'Request accelerator quota for the region',
  'Accelerator quota is regional and blocks the job before the code runs.')

# ------------------------------------------------------------- serving
t('batch_inference', 'Run batch prediction',
  'Batch prediction reads a file or table and writes predictions without holding serving capacity.')
t('online_endpoint', 'Deploy to an online endpoint',
  'An endpoint keeps capacity ready for low-latency per-request predictions.')
t('streaming_predictions', 'Send the events to a streaming prediction path',
  'Streaming answers each event as it arrives rather than on a schedule.')
t('custom_prediction_routine', 'Add a custom prediction routine to the container',
  'The routine runs the preprocessing and postprocessing inside the serving container.')
t('prebuilt_container', 'Use a prebuilt serving container',
  'A prebuilt container already implements the framework handler, so no serving code is written.')
t('artifact_registry', 'Push the serving image to Artifact Registry',
  'Artifact Registry holds the image with IAM and vulnerability metadata.')
t('model_version_alias', 'Deploy the version and move the alias',
  'An alias decouples the served version name from the artifact id, so a rollback is a pointer move.')
t('endpoint_private', 'Deploy with a private endpoint only',
  'A private endpoint is reachable only from the VPC and shares no public surface.')
t('endpoint_dedicated', 'Use a dedicated endpoint',
  'A dedicated endpoint gives the model its own capacity instead of sharing a pool.')
t('endpoint_shared', 'Use a shared public endpoint',
  'A shared endpoint removes the deployment step but gives no control over capacity or residency.')
t('serving_min_replicas', 'Set a minimum replica count',
  'A minimum replica keeps capacity warm so the first request after a quiet period is fast.')
t('serving_max_replicas', 'Raise the maximum replica count',
  'The ceiling caps how far the endpoint scales, and therefore the throughput it can absorb.')
t('serving_concurrency', 'Raise the concurrency per replica',
  'Concurrency fills each replica before another is started, which lowers cost per request.')
t('serving_gpu', 'Attach a GPU to the serving replica',
  'A GPU shortens inference time enough to meet a tight latency target.')
t('serving_autoscaling', 'Enable autoscaling on the endpoint',
  'Autoscaling adds replicas with the traffic and removes them afterwards.')
t('serving_traffic_split', 'Split traffic between two deployed versions',
  'A traffic split sends a defined share to each version on the same endpoint.')
t('explanation_metadata', 'Configure explanation metadata for the endpoint',
  'Explanation metadata tells the endpoint which inputs to attribute over.')
t('request_batch', 'Batch the requests inside the client',
  'Batching amortises the per-request overhead when the caller can wait.')

# ------------------------------------------------------------- pipelines and automation
t('pipeline_agent_platform', 'Orchestrate the steps in Agent Platform Pipelines',
  'Pipelines runs each step as a container with caching, lineage, and retry.')
t('pipeline_airflow', 'Orchestrate with Managed Service for Apache Airflow',
  'Airflow expresses cross-system dependencies and schedules outside the ML platform.')
t('pipeline_ray', 'Use Ray on Agent Platform for the distributed compute',
  'Ray fits a Python-native distributed workload that is not a container-per-step pipeline.')
t('pipeline_cloud_build', 'Trigger the build and deploy from Cloud Build',
  'Cloud Build runs the pipeline steps for build, test, and deploy with recorded provenance.')
t('pipeline_schedule', 'Add a Cloud Scheduler trigger to the pipeline',
  'The scheduler starts the pipeline on the cadence the retraining policy defines.')
t('pipeline_event_trigger', 'Trigger the pipeline from the arrival of new data',
  'An event trigger retrains when data lands instead of on a fixed clock.')
t('pipeline_validation_step', 'Add an explicit data validation step',
  'A validation step stops a bad batch before it reaches training.')
t('pipeline_model_validation', 'Gate the deployment on a model evaluation threshold',
  'The gate promotes a model only when it beats the incumbent on the agreed metric.')
t('pipeline_cache', 'Enable step caching',
  'Caching skips an unchanged step on a rerun and shortens the pipeline.')
t('retrain_drift', 'Retrain when drift crosses the threshold',
  'Drift-triggered retraining responds to change instead of to the calendar.')
t('retrain_schedule', 'Retrain on a fixed schedule',
  'A fixed schedule is simple to reason about when the data changes predictably.')
t('retrain_metric_drop', 'Retrain when the production metric drops',
  'Metric-triggered retraining reacts to actual quality loss.')
t('retrain_manual', 'Retrain only on a manual request',
  'Manual retraining leaves the model stale whenever the trigger is forgotten.')
t('ci_cd_ct', 'Extend CI/CD into continuous training',
  'Continuous training adds the retrain and validate step to the same automated pipeline.')
t('train_serve_transform', 'Share one transformation library between training and serving',
  'Shared code removes the class of bug where the two paths compute a feature differently.')
t('train_serve_saved_model', 'Keep the preprocessing inside the exported model',
  'Preprocessing inside the artifact cannot drift between the two paths.')

# ------------------------------------------------------------- security and responsible AI
t('model_armor', 'Screen the prompts and responses with Model Armor',
  'Model Armor detects prompt injection, jailbreak attempts, and unsafe content.')
t('safety_filters', 'Configure the model safety filters',
  'Safety filters block categories of harmful output at the model call.')
t('regex_redact', 'Redact the pattern-matchable fields with a regex',
  'A regex removes a known identifier pattern before the prompt leaves the service.')
t('system_instruction', 'Put the boundary in the system instruction',
  'A system instruction states what the assistant must refuse, though it is not a security control on its own.')
t('output_schema', 'Constrain the response to a JSON schema',
  'A schema stops the model returning free text that downstream code cannot parse.')
t('bias_monitoring', 'Monitor the outcome rate across the protected groups',
  'A per-group outcome rate is the first evidence of disparate impact.')
t('fairness_slice', 'Slice the evaluation metrics by the sensitive attribute',
  'A sliced metric shows a gap that the aggregate metric hides.')
t('data_card', 'Document the dataset with a data card',
  'The card records provenance, intended use, and known gaps for the dataset.')
t('model_card', 'Publish a model card with the intended use and limits',
  'The card states where the model may be used and where it must not.')

# ------------------------------------------------------------- monitoring
t('model_monitoring', 'Enable Model Monitoring on the endpoint',
  'Model Monitoring compares live traffic with the training baseline and reports skew and drift.')
t('monitoring_training_serving_skew', 'Watch for training-serving skew',
  'Skew compares the live feature distribution with the training distribution.')
t('monitoring_data_drift', 'Watch for data drift',
  'Data drift is a change in the input distribution after the model shipped.')
t('monitoring_concept_drift', 'Watch for concept drift',
  'Concept drift is a change in the relationship between the features and the target.')
t('monitoring_attribution_drift', 'Watch for feature attribution drift',
  'Attribution drift is a change in which features drive the prediction.')
t('monitoring_prediction_drift', 'Watch the prediction distribution',
  'A shift in the output distribution is often the first visible symptom.')
t('monitoring_ground_truth', 'Join the delayed ground truth back to the predictions',
  'Without the labelled outcome, quality can only be inferred from the inputs and outputs.')
t('monitoring_threshold', 'Set the monitoring threshold from the acceptable error budget',
  'The threshold expresses how much drift the business can absorb before someone acts.')
t('monitoring_alert', 'Route the monitoring alert to the owning team',
  'An alert with no owner is a dashboard nobody reads.')
t('monitoring_genai_eval', 'Score a sample of live answers with the evaluation rubric',
  'Continuous sampling catches quality regressions that drift metrics cannot see.')
t('monitoring_token_usage', 'Track tokens and cost per request',
  'Token accounting attributes generative cost to the feature that caused it.')
t('monitoring_latency', 'Track p95 latency per model version',
  'A percentile latency per version shows a regression that an average hides.')
t('logging_prompt_response', 'Log the prompt and response with redaction',
  'Redacted logs make a bad answer diagnosable without storing sensitive text.')
