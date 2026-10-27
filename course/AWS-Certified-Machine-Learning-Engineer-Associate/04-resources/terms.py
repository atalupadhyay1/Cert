"""Option bank for the AWS Certified Machine Learning Engineer – Associate (MLA-C02) sets.

Every option is a concrete AWS service choice, a modelling decision or a named
operational practice, so an item can ask which one fits a stated requirement
instead of asking what a term means. Keys are authoring identifiers only and never
appear in an export.
"""

TERMS = {}


def t(key, label, meaning):
    if key in TERMS:
        raise ValueError(f"duplicate option key: {key}")
    TERMS[key] = (label, meaning)


# --- Data ingestion and storage -------------------------------------------
t('s3_parquet', 'Land the dataset as Parquet in Amazon S3',
  'Columnar Parquet files in S3 are read in column subsets, which suits repeated training scans.')
t('s3_raw_json', 'Land the raw JSON events in Amazon S3 unchanged',
  'Raw JSON is readable but forces every query to parse whole records.')
t('s3_partitioned', 'Partition the S3 prefix by event date',
  'Date partitioning lets a query or a training job skip the prefixes it does not need.')
t('ebs_gp3', 'Attach a gp3 Amazon EBS volume to the training instance',
  'EBS is block storage bound to one instance, which suits a single host and not a fleet.')
t('efs_shared', 'Mount a shared Amazon EFS file system on every training host',
  'EFS gives many hosts one POSIX file system, which suits shared code and small data.')
t('fsx_lustre_high', 'Use Amazon FSx for Lustre for the training file system',
  'Lustre delivers the high throughput a multi-node training job needs from shared storage.')
t('dynamodb_lookup', 'Serve low-latency feature lookups from Amazon DynamoDB',
  'DynamoDB answers key lookups at single-digit millisecond latency.')
t('kinesis_streams', 'Ingest the events with Amazon Kinesis Data Streams',
  'Kinesis holds an ordered stream that several consumers can read at their own pace.')
t('msk_kafka', 'Ingest the events through Amazon MSK',
  'MSK runs managed Kafka, which suits teams already using Kafka clients and topics.')
t('firehose_delivery', 'Deliver the stream to Amazon S3 with Amazon Data Firehose',
  'Firehose batches the stream into S3 objects without a consumer to operate.')
t('kinesis_shards', 'Raise the Kinesis shard count to match the write rate',
  'Throughput on a data stream is capped per shard, so capacity follows the shard count.')
t('firehose_buffer', 'Increase the Firehose buffer size and interval',
  'A larger buffer trades delivery latency for fewer, bigger S3 objects.')
t('quota_increase', 'Request a service quota increase for the throttled resource',
  'A throttled call at a service limit is fixed by raising the limit that caused it.')
t('glue_etl', 'Transform the data with an AWS Glue ETL job',
  'Glue runs a managed Spark job against catalogued sources and writes the prepared output.')
t('emr_spark', 'Process the data with Spark on Amazon EMR',
  'EMR gives a managed Spark cluster sized for the processing job.')
t('databrew_recipe', 'Profile and clean the data with AWS Glue DataBrew',
  'DataBrew provides a visual recipe for profiling, cleaning and normalising columns.')
t('data_wrangler', 'Prepare the data in SageMaker Data Wrangler',
  'Data Wrangler builds a reusable preparation flow and can export it into a pipeline.')
t('glue_catalog', 'Register the tables in the AWS Glue Data Catalog',
  'The catalog gives every engine the same table definitions and schemas.')
t('dms_replicate', 'Replicate the operational tables with AWS Database Migration Service',
  'DMS copies and keeps replicating rows from the source database without custom extract code.')
t('lambda_transform', 'Transform each stream record with AWS Lambda',
  'A function per record suits lightweight enrichment and filtering of a stream.')
t('s3_glacier', 'Archive the raw corpus to an S3 Glacier storage class',
  'An archive class is priced for data that is kept but rarely read.')
t('s3_intelligent', 'Use S3 Intelligent-Tiering for the unevenly accessed corpus',
  'Intelligent-Tiering moves objects between access tiers as usage changes, with no rules to write.')
t('s3_object_lock', 'Apply S3 Object Lock to the regulated training data',
  'Object Lock prevents the retained objects from being altered or deleted for the stated period.')
t('s3_lifecycle', 'Expire intermediate artefacts with an S3 lifecycle rule',
  'A lifecycle rule deletes the derived copies on a schedule, so storage does not grow forever.')

# --- Feature work ---------------------------------------------------------
t('feature_store_online', 'Publish the features to the SageMaker Feature Store online store',
  'The online store serves the latest feature values for low-latency inference lookups.')
t('feature_store_offline', 'Keep the point-in-time history in the Feature Store offline store',
  'The offline store keeps timestamped values so training reads the values that existed at the time.')
t('feature_group_ingest', 'Ingest the cleaned rows into a SageMaker Feature Group',
  'A feature group gives one definition that both training and inference read.')
t('one_hot', 'One-hot encode the categorical columns',
  'One-hot encoding turns unordered categories into separate binary columns.')
t('standard_scaler', 'Standardise the numeric columns before training',
  'Scaling puts the numeric columns on comparable ranges so no column dominates the fit.')
t('log_transform', 'Apply a log transform to the skewed amount column',
  'A log transform compresses the long tail of a heavily skewed amount distribution.')
t('bin_ages', 'Bin the continuous age column into ranges',
  'Binning trades resolution for robustness to small variations inside a range.')
t('fit_scaler_on_train', 'Fit the scaler on the training split only',
  'Fitting on the training split keeps holdout statistics out of the transformation.')
t('stratified_split', 'Stratify the train, validation and test splits by label',
  'Stratifying keeps the label proportions the same in every split.')
t('shuffle_epochs', 'Shuffle the rows before every epoch',
  'Shuffling stops the batch order from encoding an accidental pattern.')
t('smote', 'Generate synthetic minority samples to rebalance the classes',
  'Synthetic minority sampling gives the learner more examples of the rare class.')
t('class_weights', 'Set class weights instead of resampling',
  'Class weights raise the cost of a minority mistake without inventing rows.')
t('reweight_group', 'Reweight the under-represented group in the loss',
  'Reweighting the loss changes what the model is optimised for without discarding data.')
t('dedupe_rows', 'Remove duplicate rows before splitting',
  'Duplicates that straddle splits leak the same row into training and evaluation.')
t('impute_median', 'Impute missing numeric values with the median',
  'Median imputation is robust to a skewed distribution and keeps the row.')
t('clip_outliers', 'Clip extreme outliers to a defined percentile',
  'Clipping caps the influence of a few extreme values without deleting the records.')
t('drop_nulls', 'Drop every row that has any missing field',
  'Dropping rows discards information and can bias the set towards complete records.')
t('ground_truth', 'Send the unlabelled records to Amazon SageMaker Ground Truth',
  'Ground Truth manages the labelling workforce, instructions and quality checks.')
t('ground_truth_auto', 'Use automated data labelling with a human review sample in Ground Truth',
  'Active learning labels most records automatically and sends only uncertain ones to a person.')
t('augment_images', 'Augment the image set with rotations, crops and flips',
  'Augmentation adds plausible variation that the original photographs did not contain.')
t('text_augment', 'Apply domain-specific augmentation to the text corpus',
  'Domain paraphrases broaden wording coverage without changing the label.')
t('tokenize_model', 'Tokenise the text with the target model tokeniser',
  'Using the model own tokeniser keeps token counts and truncation consistent with inference.')
t('redact_pii', 'Mask and redact personal identifiers before training',
  'Removing the identifiers stops the model from learning or echoing personal data.')
t('validate_pairs', 'Validate each prompt-response pair before it enters the training set',
  'Pair validation catches truncated prompts, empty responses and mismatched labels.')
t('safety_screen', 'Screen the training text for unsafe content',
  'Safety screening keeps prohibited material out of the model weights.')
t('fixed_chunks', 'Split the documents into fixed-size overlapping chunks',
  'Overlapping fixed chunks bound the context size and avoid cutting a sentence in half.')
t('semantic_chunks', 'Chunk the documents on semantic boundaries such as headings',
  'Semantic chunks keep a coherent passage together, which improves what retrieval returns.')
t('parent_child_chunks', 'Index parent sections and retrieve their child chunks',
  'Small child chunks match a query precisely while the parent supplies full context.')
t('chunk_metadata', 'Store source, date and section metadata with each chunk',
  'Metadata lets retrieval filter by source or recency and lets answers cite the document.')
t('embed_bedrock', 'Generate the embeddings with an Amazon Bedrock embedding model',
  'A managed embedding model converts text into vectors without hosts to run.')
t('embed_multimodal', 'Embed the images and captions with one multimodal model',
  'A shared multimodal space lets an image query match a text description.')
t('embed_finetune', 'Fine-tune the embedding model on the domain question-answer pairs',
  'Domain tuning moves relevant passages closer to their questions in the vector space.')
t('rerank_retrieval', 'Add a reranking step after retrieval',
  'A reranker reorders the retrieved passages by relevance before they reach the model.')
t('hybrid_retrieval', 'Combine keyword and vector retrieval',
  'Hybrid retrieval catches exact identifiers that a vector search alone can miss.')
t('opensearch_knn', 'Index the vectors in Amazon OpenSearch Service with k-NN search',
  'OpenSearch provides a managed vector index with filtered k-nearest-neighbour search.')
t('pgvector', 'Store the vectors in Amazon RDS for PostgreSQL with pgvector',
  'pgvector keeps vectors beside relational rows the application already queries.')
t('s3_vectors', 'Keep the vectors in Amazon S3 with a vector index',
  'An S3-backed index suits a large, cost-sensitive corpus read less often.')
t('in_memory_faiss', 'Load every vector into the application process on each request',
  'Rebuilding the index per request cannot hold a large corpus or a latency target.')
t('clarify_bias', 'Measure bias with SageMaker Clarify before training',
  'Clarify reports label and feature bias metrics so the imbalance is quantified first.')
t('multimodal_balance', 'Rebalance the numeric, text and image assets in the set',
  'A modality with far fewer examples is under-trained even when the label mix looks even.')
t('glue_dq', 'Evaluate AWS Glue Data Quality rules on the prepared table',
  'Data Quality rules fail the job on nulls, duplicates or range violations before training starts.')
t('profile_baseline', 'Profile the incoming data and store the statistics as a baseline',
  'A stored profile is what later drift comparison is measured against.')
t('schema_contract', 'Enforce a schema contract on the ingested records',
  'A schema check rejects records whose fields changed shape before they corrupt the set.')

# --- Modelling ------------------------------------------------------------
t('xgboost_builtin', 'Train the tabular classifier with the XGBoost built-in algorithm',
  'Gradient-boosted trees are the usual strong baseline for tabular data.')
t('linear_learner', 'Train with the linear learner algorithm',
  'A linear model is cheap and interpretable when the relationship is close to linear.')
t('deepar', 'Forecast the series with the DeepAR algorithm',
  'DeepAR learns across many related time series and returns probabilistic forecasts.')
t('knn_builtin', 'Use the k-nearest-neighbours algorithm',
  'Nearest neighbours suit a small, low-dimensional similarity problem.')
t('random_cut_forest', 'Use Random Cut Forest for anomaly scoring',
  'Random Cut Forest assigns an anomaly score to each observation against the learned shape.')
t('blazing_text', 'Use BlazingText for text classification',
  'BlazingText trains fast text classifiers on labelled documents.')
t('jumpstart_model', 'Start from a SageMaker JumpStart model',
  'JumpStart supplies a pre-trained model and its deployment template.')
t('script_mode', 'Package the training code in script mode with a supported framework',
  'Script mode runs your own training script inside a managed framework container.')
t('custom_container', 'Bring a custom training container image',
  'A custom image is needed only when the managed framework images cannot carry the dependencies.')
t('glass_box_model', 'Choose an interpretable model for the regulated decision',
  'A decision that must be explained per applicant needs a model whose reasoning is inspectable.')
t('largest_model', 'Start with the largest available model for every request',
  'Sizing every request for the hardest case spends latency and money on easy requests.')
t('nova_model', 'Select an Amazon Nova foundation model in Amazon Bedrock',
  'Nova models are reached through the Bedrock API with no infrastructure to host.')
t('titan_embeddings', 'Select a Titan embedding model in Amazon Bedrock',
  'A Titan embedding model turns text into vectors for search and clustering.')
t('claude_model', 'Select an Anthropic Claude model in Amazon Bedrock',
  'Claude models are available through Bedrock for long-context reasoning tasks.')
t('self_host_weights', 'Download open weights and host them on your own endpoint',
  'Self-hosting gives full control but puts model operations on your team.')
t('ft_lora', 'Fine-tune with parameter-efficient adapters such as LoRA',
  'Adapters train a small number of parameters, which lowers cost and the risk of forgetting.')
t('ft_full', 'Run full-parameter fine-tuning on the curated corpus',
  'Full fine-tuning updates every weight and needs more data, memory and care.')
t('continued_pretrain', 'Run continued pre-training on the domain corpus',
  'Continued pre-training adapts the model to domain vocabulary before task tuning.')
t('distillation', 'Distil the large model into a smaller student model',
  'Distillation transfers the large model behaviour into a cheaper model to serve.')
t('rag_over_ft', 'Build retrieval-augmented generation instead of fine-tuning',
  'Retrieval grounds answers in current documents without changing model weights.')
t('prompt_first', 'Start with task-specific prompt engineering before any training',
  'A well-structured prompt often meets the requirement without a training run.')
t('textract', 'Extract the form fields with Amazon Textract',
  'Textract reads forms and tables into structured fields without a custom model.')
t('comprehend', 'Detect entities and sentiment with Amazon Comprehend',
  'Comprehend provides managed entity, key-phrase and sentiment analysis.')
t('transcribe', 'Transcribe the calls with Amazon Transcribe',
  'Transcribe converts speech to text and can label speakers.')
t('rekognition', 'Detect objects and text in images with Amazon Rekognition',
  'Rekognition provides managed image and video analysis for common labels and text.')
t('amt', 'Tune hyperparameters with SageMaker automatic model tuning',
  'Automatic model tuning runs the search over a stated objective metric.')
t('bayesian_search', 'Use Bayesian search over a defined objective metric',
  'Bayesian search spends the trial budget on the region of the space that looks promising.')
t('random_search', 'Use random search over a small range',
  'Random search is a cheap baseline but ignores what earlier trials learned.')
t('grid_by_hand', 'Run a hand-written grid of training jobs',
  'A manual grid costs a job per combination and adapts to nothing.')
t('objective_metric', 'Define the tuning objective on the validation metric that matters',
  'The search optimises exactly the metric it is given, so the metric must match the goal.')
t('early_stopping', 'Enable early stopping on the validation metric',
  'Early stopping ends a trial once the validation metric stops improving.')
t('data_parallel', 'Split each batch across instances with data parallelism',
  'Data parallelism shortens wall-clock training when the model still fits on one device.')
t('model_parallel', 'Shard the model across instances with model parallelism',
  'Model parallelism is needed when the model weights do not fit on a single device.')
t('checkpoint_s3', 'Checkpoint to Amazon S3 so an interrupted job resumes',
  'Checkpoints let a reclaimed instance continue from the last saved state.')
t('managed_spot', 'Run training on managed Spot training capacity',
  'Spot capacity lowers the cost of a job that can checkpoint and resume.')
t('warm_pool', 'Keep a managed warm pool for the training cluster',
  'A warm pool removes the provisioning delay between consecutive training jobs.')
t('regularise', 'Add regularisation and reduce model capacity',
  'Regularisation and smaller capacity reduce variance when training error is far below validation.')
t('more_data', 'Add training data and keep a held-out validation split',
  'More representative data reduces variance without shrinking the model.')
t('train_longer', 'Increase model capacity and train for more epochs',
  'Raising capacity addresses underfitting where both training and validation error are high.')
t('replay_samples', 'Mix replay samples from the original distribution into fine-tuning',
  'Replay samples keep the earlier behaviour from being overwritten by the narrow new data.')
t('ensemble', 'Average several models into an ensemble',
  'An ensemble reduces variance from any single model fit.')

# --- Evaluation -----------------------------------------------------------
t('f1_metric', 'Report F1 on the holdout set',
  'F1 balances precision and recall, which suits an uneven class mix.')
t('auc_metric', 'Report ROC-AUC for the ranking task',
  'ROC-AUC measures how well the scores separate the classes across thresholds.')
t('rmse_metric', 'Report RMSE for the regression',
  'RMSE expresses the typical error in the target units and penalises large misses.')
t('pr_curve', 'Pick the threshold from the precision-recall curve',
  'The operating threshold should follow the cost of a false positive against a false negative.')
t('confusion_matrix', 'Inspect the confusion matrix on the minority class',
  'The confusion matrix shows which class the model keeps confusing.')
t('bleu_metric', 'Score the generated summaries with BLEU',
  'BLEU measures n-gram overlap with the reference summaries.')
t('rouge_metric', 'Score the generated summaries with ROUGE',
  'ROUGE measures recall of reference n-grams, which suits summarisation.')
t('bertscore', 'Score the answers with BERTScore',
  'BERTScore compares contextual embeddings, so a paraphrase can still score well.')
t('semantic_similarity', 'Measure semantic similarity to the reference answer',
  'Embedding similarity tolerates wording changes that an n-gram metric penalises.')
t('llm_judge', 'Use an LLM-as-a-judge rubric for the open-ended answers',
  'A rubric-driven judge scales qualitative review of free-text answers.')
t('human_review', 'Add a human review loop for a sample of answers',
  'Sampled expert review is how a judge rubric is validated and safety is confirmed.')
t('accuracy_only', 'Report accuracy alone on a 2 percent positive class',
  'Accuracy on a rare class is dominated by the majority and hides missed positives.')
t('bedrock_eval_job', 'Run an Amazon Bedrock model evaluation job',
  'Bedrock evaluation scores model output against built-in or custom metrics.')
t('baseline_and_drift', 'Record a performance baseline and monitor drift against it',
  'A stored baseline is the reference a drift monitor compares production against.')
t('shadow_compare', 'Compare a shadow variant against the production variant',
  'A shadow variant scores live traffic without serving its answers.')
t('ab_traffic_split', 'Split traffic between variants and compare the outcome metric',
  'A live split answers which variant performs better on the real population.')
t('mlflow_tracking', 'Log runs with MLflow on SageMaker AI',
  'Run logging keeps parameters, metrics and artefacts comparable across experiments.')
t('pin_versions', 'Pin the data snapshot, code version and hyperparameters for each run',
  'Pinned inputs are what makes an experiment reproducible later.')
t('shap_values', 'Explain the predictions with SHAP values',
  'SHAP attributes each prediction to its features in a consistent way.')
t('clarify_attribution', 'Use SageMaker Clarify for feature attribution',
  'Clarify reports which features drove the model output across the dataset.')
t('lower_learning_rate', 'Lower the learning rate and inspect the loss curve',
  'A diverging loss suggests the step size is too large for the batch and data.')
t('check_inputs', 'Check the input pipeline for label and feature errors',
  'A model that cannot beat a trivial baseline usually has broken inputs, not a bad optimiser.')
t('gradient_clip', 'Clip gradients and check for exploding values',
  'Gradient clipping stabilises training when the loss spikes without warning.')

# --- Deployment and orchestration ----------------------------------------
t('realtime_endpoint', 'Deploy a real-time SageMaker AI endpoint',
  'A real-time endpoint answers synchronous requests with a persistent host behind it.')
t('serverless_inference', 'Deploy a serverless inference endpoint',
  'Serverless inference scales to zero and suits intermittent, short requests.')
t('async_inference', 'Use asynchronous inference with results written to Amazon S3',
  'Asynchronous inference queues large or long requests and returns results through S3.')
t('batch_transform', 'Run a batch transform job over the stored records',
  'Batch transform scores a stored dataset with no endpoint to keep running.')
t('multi_model_endpoint', 'Host many small models behind one multi-model endpoint',
  'A multi-model endpoint loads models on demand from S3 behind shared hosting capacity.')
t('multi_container', 'Run several containers behind one endpoint',
  'A multi-container endpoint chains containers such as preprocessing and inference.')
t('provisioned_throughput', 'Buy provisioned throughput for the Bedrock model',
  'Provisioned throughput reserves model capacity for predictable, high-volume traffic.')
t('ondemand_bedrock', 'Call the Bedrock model on demand',
  'On-demand calls need no reservation and suit bursty, lower-volume traffic.')
t('custom_model_import', 'Import the fine-tuned weights with Bedrock custom model import',
  'Custom model import runs your own fine-tuned weights on Bedrock infrastructure.')
t('inference_recommender', 'Right-size the endpoint with SageMaker Inference Recommender',
  'Inference Recommender benchmarks instance types against the latency and throughput target.')
t('gpu_family', 'Choose a GPU instance family for the inference endpoint',
  'GPU instances suit deep models whose forward pass needs accelerator throughput.')
t('inferentia_family', 'Choose an Inferentia instance family for the endpoint',
  'Inferentia is built for cost-efficient inference of supported model architectures.')
t('graviton_family', 'Choose a Graviton instance family for the endpoint',
  'Graviton suits CPU inference of smaller models at a lower price per hour.')
t('target_tracking', 'Auto scale the endpoint on a target-tracking policy',
  'Target tracking holds a metric such as invocations per instance near a chosen value.')
t('step_scaling_policy', 'Auto scale on a step policy with CloudWatch alarms',
  'Step scaling adds capacity in bands as the alarm breaches, which suits sharp bursts.')
t('provisioned_concurrency', 'Keep provisioned concurrency ready for the burst window',
  'Provisioned concurrency pre-warms capacity so the burst does not meet a cold start.')
t('scale_to_zero', 'Scale the endpoint to zero outside business hours',
  'A scale-to-zero policy removes the idle cost when nothing calls the endpoint.')
t('gpu_metric_scaling', 'Scale on GPU utilisation rather than invocation count',
  'GPU utilisation reflects the real bottleneck when each request is expensive.')
t('interface_endpoint', 'Create an interface VPC endpoint for the service',
  'A private endpoint keeps the service traffic inside the VPC without a NAT gateway.')
t('private_subnets', 'Place the endpoint and model containers in private subnets',
  'Private subnets remove the inbound internet path to the model hosts.')
t('restrict_sg', 'Restrict the security group to the application subnet',
  'A security group scoped to the caller subnet allows only the intended traffic.')
t('open_ingress', 'Allow ingress from any address on the endpoint port',
  'An open ingress rule exposes the model to anything that can reach the VPC.')
t('nat_gateway', 'Route the private subnet through a NAT gateway',
  'A NAT gateway gives private hosts outbound access without accepting inbound traffic.')
t('codepipeline', 'Orchestrate the release with AWS CodePipeline',
  'CodePipeline sequences the build, test and deploy stages and records each outcome.')
t('codebuild', 'Build and test the model image with AWS CodeBuild',
  'CodeBuild runs the build and the automated tests in a clean managed environment.')
t('codedeploy', 'Shift traffic with AWS CodeDeploy',
  'CodeDeploy performs the traffic shift and can roll back on an alarm.')
t('codecommit', 'Keep the pipeline source in AWS CodeCommit',
  'CodeCommit is the managed Git repository the pipeline reads from.')
t('codeconnections', 'Connect the external repository with AWS CodeConnections',
  'CodeConnections lets the pipeline read a repository hosted elsewhere.')
t('sm_pipelines', 'Define the workflow as a SageMaker pipeline',
  'A SageMaker pipeline expresses the processing, training and registration steps as one DAG.')
t('step_functions', 'Orchestrate the steps with AWS Step Functions',
  'Step Functions coordinates long-running steps and service calls with retries and branching.')
t('eventbridge_schedule', 'Trigger the retraining run with an EventBridge schedule',
  'A schedule starts the pipeline on a fixed cadence without an external cron host.')
t('model_registry', 'Register the approved version in the SageMaker Model Registry',
  'The registry holds model versions and their approval status for deployment.')
t('approval_gate', 'Require a manual approval before the version is deployed',
  'An approval gate stops a model from reaching production on an automated pass alone.')
t('prompt_management', 'Store the prompt templates in Amazon Bedrock Prompt Management',
  'Prompt Management versions templates so a prompt change is reviewable and reversible.')
t('agent_deploy', 'Deploy the agent with its action groups and knowledge base',
  'An agent needs its tools, knowledge base and instructions deployed together as one unit.')
t('agent_state', 'Persist the agent session state between turns',
  'Persisted session state keeps multi-turn context without resending the whole history.')
t('kb_sync', 'Schedule a knowledge base sync when documents change',
  'A sync re-indexes changed documents so retrieval does not serve stale passages.')
t('canary_release', 'Send a small share of traffic to the new version first',
  'A canary release limits the blast radius of a bad model to the canary share.')
t('blue_green', 'Stand the new version beside the old and switch traffic',
  'Blue/green keeps the previous version ready for an immediate switch back.')
t('linear_release', 'Shift traffic to the new version in equal steps',
  'A linear shift moves traffic gradually while the metrics are watched.')
t('all_at_once', 'Replace the production version in a single switch',
  'A single switch gives a bad model the whole traffic share at once.')
t('shadow_deploy', 'Mirror traffic to the new model without serving its answers',
  'Mirroring collects comparison data with no user impact.')
t('test_gate', 'Fail the pipeline when the evaluation threshold is missed',
  'A quality gate blocks a release whose measured metric is below the agreed bar.')
t('prompt_regression', 'Run a prompt regression suite before each release',
  'A prompt suite catches a template change that breaks previously correct answers.')
t('ecr_image', 'Store the container image in Amazon ECR',
  'ECR holds the versioned image that the training or hosting service pulls.')
t('ecs_service', 'Run the container on Amazon ECS',
  'ECS schedules the container on managed cluster capacity.')
t('eks_cluster', 'Run the container on Amazon EKS',
  'EKS runs the container under Kubernetes for teams already standardised on it.')
t('batch_job', 'Run the job on AWS Batch',
  'AWS Batch queues the job and provisions capacity for the run.')
t('lambda_inference', 'Serve the model from an AWS Lambda function',
  'Lambda suits a small model and spiky traffic but not a large model resident in memory.')
t('hyperpod_cluster', 'Run the workload on a SageMaker HyperPod cluster',
  'HyperPod keeps a resilient cluster for long distributed training runs.')
t('training_job', 'Submit a SageMaker training job',
  'A training job provisions the instances, runs the script and stores the artefacts.')
t('neo_compile', 'Compile the model with SageMaker Neo',
  'Neo compiles the model for the target hardware to cut inference latency.')

# --- Monitoring and cost --------------------------------------------------
t('data_drift_monitor', 'Enable a data drift monitor on the endpoint',
  'A data drift monitor compares the live request distribution against the training baseline.')
t('model_quality_monitor', 'Enable a model quality monitor with ground-truth labels',
  'A quality monitor scores live predictions once the true labels arrive.')
t('bias_drift_monitor', 'Enable a bias drift monitor',
  'A bias monitor watches whether the outcome distribution shifts for a protected group.')
t('attribution_drift_monitor', 'Enable feature attribution drift monitoring',
  'Attribution drift shows that the model now relies on different features than it did.')
t('cloudwatch_alarm', 'Alarm on the CloudWatch latency and error metrics',
  'An alarm on the endpoint metrics pages someone when the service degrades.')
t('cloudwatch_dashboard', 'Build a CloudWatch dashboard for the pipeline metrics',
  'A dashboard puts the operating metrics in one view for the team.')
t('logs_insights', 'Query the inference logs with CloudWatch Logs Insights',
  'Logs Insights filters and aggregates the request logs to find the failing pattern.')
t('genai_observability', 'Enable CloudWatch generative AI observability for the model calls',
  'Generative AI observability records prompts, token counts and latency per model call.')
t('agentcore_observability', 'Trace agent tool calls with Bedrock AgentCore Observability',
  'Agent tracing shows which tool call failed or stalled inside a multi-step task.')
t('xray_trace', 'Trace the pipeline service calls with AWS X-Ray',
  'X-Ray shows where a request spends its time across the services it touches.')
t('cost_explorer_ml', 'Break the spend down by endpoint with AWS Cost Explorer',
  'Cost Explorer groups the bill by service and by tag so the expensive resource is visible.')
t('budgets_ml', 'Set an AWS Budget alert on the ML account',
  'A budget alerts when forecast or actual spend crosses the agreed amount.')
t('savings_plan_inference', 'Cover the steady inference load with a Savings Plan',
  'A Savings Plan discounts a predictable hourly spend on eligible compute.')
t('batch_for_offline', 'Move the offline scoring to batch transform',
  'Batch scoring removes the idle endpoint that an always-on deployment would keep.')
t('cap_output_tokens', 'Cap the output tokens per request',
  'Output tokens dominate generation cost, so a cap bounds the spend per call.')
t('trim_context', 'Trim the retrieved context sent to the model',
  'Sending fewer retrieved tokens lowers both cost and latency on every call.')
t('route_small_model', 'Route routine requests to a smaller model',
  'Routing easy requests to a cheaper model keeps the large model for hard cases.')
t('cache_embeddings', 'Cache embeddings for documents that have not changed',
  'Re-embedding an unchanged document is wasted spend on every refresh.')
t('compare_throughput', 'Compare provisioned throughput against on-demand spend',
  'The reservation only pays off when the steady volume exceeds the break-even point.')
t('instance_rightsize', 'Right-size the instance family against the measured latency',
  'Matching the family to the measured workload avoids paying for capacity the model cannot use.')
t('iam_execution_role', 'Give the training job a scoped IAM execution role',
  'An execution role grants the job only the permissions its inputs and outputs need.')
t('least_privilege_bucket', 'Attach a policy scoped to the one bucket prefix',
  'Scoping to the prefix stops a compromised job from reaching the rest of the data lake.')
t('scp_guardrail', 'Apply a service control policy at the organisation level',
  'A service control policy caps what any account beneath it can do.')
t('kms_cmk', 'Encrypt the artefacts with a customer managed KMS key',
  'A customer managed key lets the team control the key policy and revoke access.')
t('secrets_manager', 'Store the model API credential in AWS Secrets Manager',
  'Secrets Manager holds the credential centrally and can rotate it.')
t('bedrock_api_key', 'Issue a Bedrock API key for the calling application',
  'An API key gives short-lived programmatic access without embedding IAM credentials.')
t('cloudtrail', 'Record the API calls with AWS CloudTrail',
  'CloudTrail records who called which API, when and from where.')
t('aws_config', 'Track resource configuration with AWS Config',
  'Config records how each resource was configured and evaluates it against rules.')
t('inspector_scan', 'Scan the built image with Amazon Inspector',
  'Inspector reports known vulnerabilities in the image before it is deployed.')
t('codeguru_review', 'Review the pipeline code with Amazon CodeGuru',
  'CodeGuru reviews the source for defects and inefficiencies.')
t('guardrails', 'Apply Amazon Bedrock Guardrails to the model responses',
  'Guardrails filters denied topics, sensitive data and unsafe content in the response path.')
t('runtime_redaction', 'Redact personal data before the prompt reaches the model',
  'Redaction at the boundary keeps personal data out of the model request entirely.')
t('denied_topics', 'Configure a denied-topics policy for the assistant',
  'A denied-topics policy refuses the subject areas the business has ruled out.')
t('shared_endpoint_public', 'Give every team one public endpoint with a shared key',
  'A shared public endpoint with one key removes both attribution and least privilege.')

# --- Credential and governance choices -----------------------------------
t('group_policy', 'Attach one policy to an IAM group the engineers belong to',
  'A group policy keeps the shared permission set in one reviewable place.')
t('root_for_ml', 'Use the account root user for pipeline administration',
  'The root user cannot be limited by policy, so daily use magnifies any mistake.')
t('cross_account_role', 'Create a role the other account can assume',
  'A cross-account role issues temporary credentials without sharing a key.')
t('long_lived_key', 'Create a long-lived access key for the integration',
  'A long-lived key keeps working after the project ends unless someone retires it.')
t('vpc_only_bucket', 'Deny access to the bucket unless the request comes through the VPC endpoint',
  'A condition on the endpoint keeps the data off every path except the private one.')
