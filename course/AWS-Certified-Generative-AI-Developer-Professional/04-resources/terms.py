"""Option bank for the AWS Certified Generative AI Developer - Professional (AIP-C01) sets.

Every option is a concrete AWS service choice, an architecture decision, a prompt or
retrieval technique, or a named operational practice, so an item can ask which one fits
a stated requirement instead of asking what a term means. Keys are authoring
identifiers only and never appear in an export.
"""

TERMS = {}


def t(key, label, meaning):
    if key in TERMS:
        raise ValueError(f"duplicate option key: {key}")
    TERMS[key] = (label, meaning)


# --- Foundation model access and selection --------------------------------
t('bedrock_ondemand', 'Call the model on demand through Amazon Bedrock',
  'On-demand Bedrock inference bills per token with no committed capacity, which suits spiky or unproven demand.')
t('bedrock_provisioned', 'Buy Amazon Bedrock provisioned throughput for the model',
  'Provisioned throughput reserves model units and gives a predictable token-per-minute ceiling.')
t('bedrock_batch', 'Run the work as an Amazon Bedrock batch inference job',
  'Batch inference trades turnaround time for a lower price on large offline volumes.')
t('cross_region_inference', 'Route the call through Amazon Bedrock cross-Region inference',
  'A cross-Region inference profile spreads traffic across Regions so a local capacity shortage is absorbed.')
t('model_distillation', 'Distil the large model into a smaller task-specific model',
  'Distillation transfers behaviour to a cheaper model for a narrow, high-volume task.')
t('lora_adapters', 'Fine-tune with low-rank adaptation adapters',
  'LoRA trains a small adapter instead of every weight, which cuts cost and keeps the base model reusable.')
t('full_finetune', 'Run a full fine-tune of every model weight',
  'A full fine-tune changes all weights, which is expensive and gives one model per task.')
t('custom_model_import', 'Import the customised model weights into Amazon Bedrock',
  'Custom model import brings your own weights under Bedrock inference and guardrail features.')
t('jumpstart_model', 'Deploy the model from Amazon SageMaker JumpStart',
  'JumpStart supplies prebuilt models and notebooks for hosting on SageMaker AI endpoints.')
t('sagemaker_endpoint', 'Host the model on a SageMaker AI real-time endpoint',
  'A SageMaker AI endpoint gives full control over the container, instance and scaling policy.')
t('model_eval_job', 'Compare the candidates with an Amazon Bedrock model evaluation job',
  'A Bedrock evaluation job scores candidate models on your prompts and metrics before you choose.')
t('tiered_routing', 'Send routine prompts to a small model and hard prompts to a large one',
  'Tiered routing spends the large model only on the requests that need it.')
t('single_frontier', 'Use one frontier model for every request',
  'One model for every request keeps the code simple but pays frontier prices for trivial prompts.')
t('model_cascade_api', 'Cascade calls from the cheap model to the strong model on low confidence',
  'A cascade escalates only the answers the first model cannot handle, which caps cost per request.')
t('appconfig_switch', 'Put the model identifier in AWS AppConfig and switch it without a deploy',
  'A configuration flag changes the model per request path without shipping new code.')
t('hardcoded_model_id', 'Hardcode one model identifier in the application source',
  'A hardcoded identifier forces a code change and a release to try another model.')

# --- Retrieval, embeddings, and vector stores ------------------------------
t('kb_managed', 'Use an Amazon Bedrock knowledge base with a managed vector store',
  'A managed knowledge base handles ingestion, chunking, embedding and sync with little code.')
t('opensearch_vector', 'Index the vectors in Amazon OpenSearch Service with k-NN search',
  'OpenSearch combines vector search with the filtering and sharding of a search engine.')
t('aurora_pgvector', 'Store the vectors in Amazon Aurora PostgreSQL with pgvector',
  'pgvector keeps embeddings beside relational rows so one query can filter and search together.')
t('dynamodb_vectors', 'Keep embeddings and metadata in Amazon DynamoDB',
  'DynamoDB serves key lookups fast and can hold vectors beside their metadata for small corpora.')
t('neptune_graph', 'Store the knowledge graph in Amazon Neptune',
  'Neptune answers relationship traversals that a similarity search cannot express.')
t('documentdb_docs', 'Keep the source documents in Amazon DocumentDB',
  'DocumentDB stores JSON documents in their original shape for retrieval and display.')
t('elasticache_cache', 'Cache frequent retrieval results in Amazon ElastiCache',
  'A cache in front of the index removes repeat lookups for popular questions.')
t('s3_documents', 'Keep the source corpus in Amazon S3 and index references into it',
  'S3 holds the authoritative documents while the index stores only chunks and pointers.')
t('metadata_filter', 'Filter the search by document metadata before the similarity ranking',
  'A metadata filter removes out-of-scope documents so the ranking only sees eligible chunks.')
t('namespace_partition', 'Partition the corpus into per-tenant namespaces',
  'Separate namespaces keep one tenant from retrieving another tenant content.')
t('fixed_chunking', 'Split documents into fixed-size token windows with overlap',
  'Fixed windows are predictable and cheap, and overlap preserves text that straddles a boundary.')
t('hierarchical_chunking', 'Split by document structure into sections and subsections',
  'Structural chunks follow headings, so a retrieved chunk carries a coherent argument.')
t('semantic_chunking', 'Split where the embedding similarity between sentences drops',
  'Semantic splitting places boundaries at topic shifts rather than at a character count.')
t('parent_child_chunks', 'Index small child chunks and return the larger parent to the model',
  'Parent-child retrieval matches on precise text and supplies surrounding context to the model.')
t('chunk_larger', 'Increase the chunk size so every answer fits in one chunk',
  'Larger chunks carry more context but dilute the embedding and crowd the prompt window.')
t('titan_embeddings', 'Generate embeddings with an Amazon Titan text embedding model',
  'A Titan embedding model gives a documented dimension and a stable vector space.')
t('multimodal_embedding', 'Embed text and images with one multimodal model',
  'A shared embedding space lets an image query match a text description.')
t('embedding_finetune', 'Fine-tune the embedding model on labelled query and passage pairs',
  'Domain-tuned embeddings move relevant passages closer for vocabulary the base model misses.')
t('reembed_on_change', 'Re-embed the corpus when the embedding model changes',
  'Vectors from two different models are not comparable, so the whole index must be rebuilt.')
t('mix_embedding_models', 'Keep old vectors and embed new documents with the newer model',
  'Mixing vector spaces silently breaks similarity, because distances no longer mean the same thing.')
t('hybrid_search', 'Combine keyword and vector retrieval and merge the ranked lists',
  'Hybrid retrieval catches exact identifiers that a vector search alone can miss.')
t('reranker', 'Rerank the retrieved passages with an Amazon Bedrock reranker',
  'A reranker scores the shortlist against the query and lifts precision before the prompt is built.')
t('query_expansion', 'Expand the user query into related terms before retrieval',
  'Expansion bridges vocabulary gaps between how users ask and how documents are written.')
t('query_decomposition', 'Break a multi-part question into separate retrievals',
  'Decomposition retrieves evidence for each sub-question instead of averaging them into one query.')
t('query_rewrite_history', 'Rewrite the query using the conversation history first',
  'History-aware rewriting turns a follow-up such as and the second one into a standalone query.')
t('top_k_higher', 'Raise the number of retrieved passages per query',
  'More passages raise recall and also lengthen the prompt and the cost per call.')
t('score_threshold', 'Drop passages below a relevance score threshold',
  'A threshold keeps marginal passages out of the prompt that would only add noise.')
t('index_incremental', 'Update the index incrementally when a source document changes',
  'Incremental updates keep the index current without re-embedding the whole corpus.')
t('index_scheduled', 'Rebuild the index on a schedule and accept staleness between runs',
  'Scheduled rebuilds are simple and leave a window in which answers lag the source.')
t('s3_event_sync', 'Trigger re-indexing from Amazon S3 event notifications',
  'Event notifications start a sync as soon as a document lands or changes, which keeps lag to seconds.')
t('mcp_client', 'Expose retrieval through a Model Context Protocol server',
  'An MCP server gives agents one standard interface to the retrieval tool.')
t('function_calling', 'Expose retrieval as a function the model can call',
  'Function calling lets the model decide when a retrieval is needed and with which arguments.')

# --- Prompting and prompt governance --------------------------------------
t('prompt_management', 'Version the prompt in Amazon Bedrock Prompt Management',
  'Prompt Management stores versions and variables so the same template serves every environment.')
t('prompt_flows', 'Build the chain in Amazon Bedrock Prompt Flows',
  'Prompt Flows runs sequential and branching prompt steps as one managed workflow.')
t('prompt_in_code', 'Keep the prompt as a string constant in the application code',
  'A prompt in code needs a deployment for every wording change and leaves no version history.')
t('system_prompt_role', 'Put the role, tone, and boundaries in the system prompt',
  'The system prompt sets behaviour once and outranks stray instructions in the user turn.')
t('few_shot_examples', 'Add worked examples of the expected answer shape',
  'Examples show the model the output contract that instructions alone leave ambiguous.')
t('chain_of_thought', 'Ask the model to reason step by step before answering',
  'Explicit steps improve multi-step reasoning and expose where an answer went wrong.')
t('json_schema_output', 'Constrain the response with a JSON schema',
  'A schema makes the output machine-parseable and rejects prose that breaks the contract.')
t('structured_sections', 'Wrap context, instructions, and question in labelled sections',
  'Labeled sections stop retrieved text from being read as an instruction.')
t('output_length_cap', 'Cap the response length in the request',
  'A token cap bounds the cost of a runaway answer and the latency of every call.')
t('temperature_low', 'Lower the temperature for factual answers',
  'Low temperature narrows sampling so repeatable factual answers stay stable.')
t('temperature_high', 'Raise the temperature for creative variants',
  'Higher temperature widens sampling, which suits brainstorming and not factual lookup.')
t('prompt_approval', 'Require approval before a prompt version is promoted',
  'An approval step keeps an unreviewed prompt change out of production traffic.')
t('prompt_regression_suite', 'Run a prompt regression suite before promoting a version',
  'A fixed suite of prompts and expected properties catches a wording change that breaks behaviour.')
t('prompt_cache', 'Cache the stable prompt prefix with prompt caching',
  'Prompt caching reuses processed prefix tokens, which cuts latency and input cost on repeat calls.')

# --- Agentic systems ------------------------------------------------------
t('strands_agent', 'Build the agent with Strands Agents',
  'Strands gives an open-source agent loop with tools, memory, and model-agnostic wiring.')
t('agent_squad', 'Coordinate the specialists with AWS Agent Squad',
  'Agent Squad routes a request to the specialist agent that can handle it.')
t('agentcore_runtime', 'Run the agent on Amazon Bedrock AgentCore',
  'AgentCore supplies managed runtime, identity, memory, and observability for agents.')
t('step_functions_agent', 'Orchestrate the reasoning loop in AWS Step Functions',
  'A state machine makes each reasoning step visible, retryable, and bounded.')
t('lambda_tool', 'Implement the tool as an AWS Lambda function',
  'A Lambda tool is stateless, cheap at low volume, and scales per request.')
t('ecs_mcp_server', 'Run the MCP server on Amazon ECS',
  'A container gives a long-lived tool server dependencies and connection pooling.')
t('agent_memory_dynamodb', 'Keep conversation and task memory in Amazon DynamoDB',
  'DynamoDB gives the agent a durable per-session store keyed by session identifier.')
t('agent_memory_context', 'Keep memory only in the prompt of the current turn',
  'Prompt-only memory forgets everything the moment the context window is trimmed.')
t('react_pattern', 'Have the agent alternate reasoning and tool calls',
  'Interleaving thought and action lets the agent gather evidence before it answers.')
t('stopping_condition', 'Set an explicit step and budget limit on the agent loop',
  'A hard limit stops a loop that would otherwise consume tokens without converging.')
t('timeout_guard', 'Bound each tool call with a timeout and a fallback',
  'A timeout keeps one slow dependency from stalling the whole agent turn.')
t('human_approval', 'Require human approval before the agent performs the action',
  'An approval gate keeps an irreversible side effect under human control.')
t('iam_tool_scope', 'Scope the tool role to only the actions it needs',
  'A narrow role limits what a misdirected agent call can actually change.')
t('tool_schema_validation', 'Validate tool arguments against a schema before calling',
  'Schema validation rejects a malformed argument instead of sending it to the system of record.')
t('multi_agent_specialist', 'Give each domain its own agent with its own tools',
  'Specialist agents keep tool sets small and prompts focused on one domain.')
t('single_agent_all_tools', 'Give one agent every tool in the platform',
  'One agent with every tool makes tool choice ambiguous and permissions broad.')
t('ensemble_aggregation', 'Aggregate answers from several models with custom logic',
  'An aggregation step can compare candidate answers before one is returned.')

# --- Integration and API patterns ----------------------------------------
t('api_gateway', 'Front the model with Amazon API Gateway',
  'API Gateway adds authentication, throttling, request validation, and streaming to the model call.')
t('appsync_graphql', 'Expose the assistant through AWS AppSync',
  'AppSync gives a managed GraphQL API with subscriptions for live responses.')
t('eventbridge_route', 'Route domain events through Amazon EventBridge',
  'EventBridge decouples producers from the GenAI consumer with rules and filtering.')
t('sqs_buffer', 'Buffer the work in an Amazon SQS queue',
  'A queue absorbs bursts and lets a worker retry a failed model call.')
t('sns_fanout', 'Fan the result out with Amazon SNS',
  'SNS delivers one event to many subscribers without the caller tracking them.')
t('step_functions_workflow', 'Coordinate the steps in AWS Step Functions',
  'A state machine keeps multi-step work ordered, retryable, and auditable.')
t('lambda_handler', 'Implement the request handler as an AWS Lambda function',
  'Lambda runs per request without a server to size or patch.')
t('fargate_service', 'Run the service on AWS Fargate',
  'Fargate runs containers without managing instances and suits steady API traffic.')
t('eks_cluster', 'Run the workload on Amazon EKS',
  'EKS suits teams already operating Kubernetes with GPU and custom networking needs.')
t('app_runner', 'Deploy the web service on AWS App Runner',
  'App Runner builds and runs a container from source with managed scaling.')
t('amplify_frontend', 'Build the interface with AWS Amplify',
  'Amplify supplies declarative UI and hosting for the client that talks to the assistant.')
t('cloudfront_cache', 'Serve repeatable responses from Amazon CloudFront',
  'An edge cache answers identical requests without reaching the model.')
t('lambda_edge', 'Run the request shaping logic at the edge with Lambda@Edge',
  'Edge logic trims, redacts, or routes a request before it crosses to the model Region.')
t('websocket_stream', 'Stream tokens over WebSockets through API Gateway',
  'A WebSocket keeps one connection open for incremental tokens.')
t('sse_stream', 'Stream tokens as server-sent events',
  'Server-sent events deliver incremental text over ordinary HTTP.')
t('sync_call', 'Return the whole answer from one synchronous call',
  'A synchronous call is simplest and makes the user wait for the final token.')
t('async_sqs_model', 'Queue the prompt and return a job identifier for polling',
  'Asynchronous processing suits long generations that outlast an API timeout.')
t('exponential_backoff', 'Retry throttled calls with exponential backoff and jitter',
  'Backoff with jitter spreads retries so a throttled client does not stampede the service.')
t('fallback_model', 'Fall back to a second model when the first is unavailable',
  'A fallback keeps the feature available when one model or Region degrades.')
t('circuit_breaker', 'Open a circuit breaker after repeated dependency failures',
  'A circuit breaker stops sending traffic to a dependency that is already failing.')
t('retry_forever', 'Retry the failed call until it succeeds',
  'Unbounded retries turn a short dependency outage into a long queue backlog.')
t('request_validation', 'Validate the request body before it reaches the model',
  'Early validation rejects malformed prompts and oversized payloads cheaply.')
t('api_rate_limit', 'Set per-client throttling at the API layer',
  'A per-client quota protects shared model capacity from one noisy caller.')
t('appflow_ingest', 'Move SaaS records in with Amazon AppFlow',
  'AppFlow copies data from supported SaaS sources without custom connectors.')
t('datasync_transfer', 'Transfer the on-premises corpus with AWS DataSync',
  'DataSync moves large file sets with verification and incremental transfer.')
t('transfer_family_sftp', 'Receive partner files over AWS Transfer Family',
  'Transfer Family accepts SFTP uploads into S3 without a server to run.')
t('outposts_local', 'Run the inference component on AWS Outposts',
  'Outposts keeps compute and data on premises where residency or latency demands it.')
t('wavelength_edge', 'Deploy the latency-critical part on AWS Wavelength',
  'Wavelength places compute at the edge of a carrier network for single-digit-millisecond round trips.')
t('codepipeline_release', 'Release the assistant through AWS CodePipeline',
  'A pipeline ties source, build, test, and deploy into one auditable flow.')
t('codebuild_test', 'Run the evaluation suite in AWS CodeBuild',
  'CodeBuild runs the tests and quality gates as part of the release.')
t('codedeploy_canary', 'Shift traffic with an AWS CodeDeploy canary deployment',
  'A canary exposes a small share of traffic to the new version before the rest follows.')
t('cdk_stack', 'Define the resources in AWS CDK',
  'CDK expresses the stack as code so environments are reproducible.')
t('cloudformation_template', 'Define the resources in AWS CloudFormation',
  'CloudFormation applies and rolls back a declared set of resources.')
t('gateway_abstraction', 'Put one internal GenAI gateway in front of every model call',
  'A gateway centralises credentials, quotas, logging, and model routing for all teams.')
t('direct_model_calls', 'Let each application call the model API directly',
  'Direct calls from every app scatter keys, quotas, and logging across teams.')

# --- Safety, privacy, and governance -------------------------------------
t('guardrails_content', 'Apply Amazon Bedrock Guardrails content filters',
  'Content filters score and block harmful input and output on the request path.')
t('guardrails_denied', 'Define denied topics in Amazon Bedrock Guardrails',
  'Denied topics refuse the subject areas the business has ruled out.')
t('guardrails_pii', 'Enable sensitive-information filters in Amazon Bedrock Guardrails',
  'PII filters detect and mask personal data in prompts and responses.')
t('guardrails_grounding', 'Enable the contextual grounding check in Guardrails',
  'The grounding check compares the response with the retrieved source and flags unsupported claims.')
t('guardrails_reasoning', 'Add automated reasoning checks for policy statements',
  'Reasoning checks verify a response against encoded policy rules rather than a similarity score.')
t('prompt_injection_filter', 'Screen inputs for instruction override and jailbreak patterns',
  'A pre-filter catches text that tries to replace the system instruction.')
t('input_sanitize', 'Strip control text and delimiters from retrieved content',
  'Sanitising retrieved text stops it from being parsed as an instruction.')
t('adversarial_suite', 'Run an adversarial prompt suite before each release',
  'A hostile test set finds regressions in refusal behaviour before users do.')
t('output_schema_check', 'Reject responses that fail the output schema',
  'A post-check refuses a malformed transfer before it reaches a downstream system.')
t('postprocess_validate', 'Validate the response against business rules before display',
  'A rule check catches an answer that is fluent but not permitted.')
t('text_to_sql', 'Translate the question into SQL and run it on the database',
  'Deterministic query generation avoids asking a model to compute figures from memory.')
t('grounding_citation', 'Require the answer to cite the retrieved passage',
  'A citation makes each claim traceable to a source the reader can check.')
t('confidence_score', 'Return a confidence score with each answer',
  'A score lets the interface route low-confidence answers to a human.')
t('pii_comprehend', 'Detect personal data with Amazon Comprehend',
  'Comprehend identifies entities and PII so they can be masked before the model sees them.')
t('macie_scan', 'Scan the data store with Amazon Macie',
  'Macie finds sensitive data at rest so the corpus can be cleaned before indexing.')
t('mask_before_prompt', 'Mask personal data before the prompt is built',
  'Masking at the boundary keeps personal data out of the model request entirely.')
t('logging_off', 'Disable prompt logging for the workload',
  'Turning logging off removes the evidence needed for audit and troubleshooting.')
t('vpc_endpoint', 'Call the model through an interface VPC endpoint',
  'A private endpoint keeps model traffic off the public internet.')
t('private_subnet', 'Deploy the workload in private subnets',
  'Private subnets remove inbound internet routing from the compute tier.')
t('waf_rules', 'Put AWS WAF rules in front of the public endpoint',
  'WAF blocks known bad request patterns before they consume model capacity.')
t('cognito_auth', 'Authenticate users with Amazon Cognito',
  'Cognito issues scoped tokens so each request carries an identity.')
t('iam_role_task', 'Give the task an IAM role scoped to the resources it uses',
  'A scoped role issues temporary credentials with only the needed permissions.')
t('static_key_env', 'Store the model API key in an environment variable',
  'A key in an environment variable leaks through images, logs, and job definitions.')
t('secrets_manager', 'Store the credential in AWS Secrets Manager',
  'Secrets Manager rotates and audits the credential instead of freezing it in config.')
t('kms_cmk', 'Encrypt the corpus with a customer managed AWS KMS key',
  'A customer managed key gives the team its own rotation and access policy.')
t('s3_public_read', 'Make the document bucket publicly readable',
  'A public bucket exposes the corpus to everyone the index was meant to constrain.')
t('cloudtrail_log', 'Record control-plane activity in AWS CloudTrail',
  'CloudTrail records who changed models, keys, and guardrails.')
t('log_retention', 'Set an explicit CloudWatch Logs retention period',
  'A retention period bounds storage cost and matches the data policy.')
t('data_lineage', 'Record data lineage in the AWS Glue Data Catalog',
  'Lineage shows which corpus and version produced an answer.')
t('model_card', 'Publish a model card with the model version',
  'A model card documents intended use and known limits for reviewers.')
t('bias_metrics', 'Report fairness metrics per user segment',
  'Segment metrics expose a quality gap that an overall average hides.')
t('bias_drift_alert', 'Alert when fairness metrics move beyond a band',
  'A drift alert catches a fairness regression after a model or prompt change.')
t('human_escalation', 'Escalate low-confidence or high-impact answers to a person',
  'An escalation path keeps consequential answers with a human owner.')

# --- Cost, performance, and observability --------------------------------
t('context_pruning', 'Prune older turns from the context window',
  'Dropping stale turns cuts input tokens without losing the current instruction.')
t('summarise_history', 'Summarise the conversation before adding more turns',
  'A running summary keeps long sessions inside the window at low token cost.')
t('retrieval_top_n_small', 'Retrieve fewer passages per answer',
  'Fewer passages shrink the prompt, which lowers both cost and latency.')
t('semantic_cache', 'Cache answers by embedding similarity to earlier questions',
  'A semantic cache serves a near-duplicate question without a model call.')
t('exact_cache', 'Cache the response under a hash of the normalised request',
  'A hash cache is exact and avoids a false hit between similar questions.')
t('cache_without_ttl', 'Cache every answer with no expiry',
  'Answers without expiry keep serving text that the corpus has already corrected.')
t('stream_response', 'Stream tokens as they are generated',
  'Streaming lowers perceived latency without changing total generation time.')
t('parallel_calls', 'Issue independent model calls in parallel',
  'Parallel calls cut wall-clock time for sub-tasks that do not depend on each other.')
t('precompute_batch', 'Precompute answers for predictable questions on a schedule',
  'Precomputation moves repeatable work into a cheap batch window.')
t('latency_model', 'Choose a lower-latency model for the interactive path',
  'A smaller or latency-optimised model answers faster at some quality cost.')
t('capacity_plan', 'Plan capacity from measured tokens per minute',
  'Capacity sized from observed token throughput avoids both throttling and idle spend.')
t('cloudwatch_tokens', 'Publish token usage as CloudWatch metrics',
  'Token metrics per model and tenant show where spend and latency come from.')
t('invocation_logs', 'Turn on Amazon Bedrock model invocation logging',
  'Invocation logs capture the request, the response, and the token counts.')
t('logs_insights', 'Query the prompt and response logs with CloudWatch Logs Insights',
  'Logs Insights correlates a spike in errors with the prompts that caused it.')
t('xray_trace', 'Trace the request across services with AWS X-Ray',
  'A trace shows which hop in the chain added the latency.')
t('synthetics_canary', 'Probe the endpoint with CloudWatch Synthetics',
  'A synthetic canary detects an outage before a user reports it.')
t('grafana_dashboard', 'Build the operations view in Amazon Managed Grafana',
  'Grafana combines model, infrastructure, and business metrics on one screen.')
t('alarm_latency', 'Alarm on p95 latency and error rate',
  'A latency alarm fires on the symptom users feel.')
t('cost_anomaly', 'Detect spend spikes with AWS Cost Anomaly Detection',
  'Anomaly detection finds an unexpected token bill without a fixed threshold.')
t('cost_explorer_tag', 'Break down spend by application tag in AWS Cost Explorer',
  'Tag-based cost views attribute the token bill to the team that caused it.')
t('savings_plan_compute', 'Cover the steady compute with a Savings Plan',
  'A Savings Plan discounts the predictable part of the compute baseline.')
t('idle_endpoint', 'Keep a GPU endpoint running for occasional requests',
  'An idle endpoint bills for capacity that sits unused between requests.')
t('model_right_size', 'Right-size the model to the task difficulty',
  'A model no larger than the task needs is the largest single cost lever.')
t('token_budget_alert', 'Alert when a tenant crosses its monthly token budget',
  'A budget alert stops one tenant from consuming the shared quota.')

# --- Evaluation and troubleshooting --------------------------------------
t('human_rubric', 'Have reviewers score a sample against a written rubric',
  'A rubric with human scores gives a reference the automatic metrics can be checked against.')
t('llm_judge', 'Score candidate answers with a judge model on a fixed rubric',
  'A judge model scales subjective scoring and needs its own agreement check.')
t('judge_agreement', 'Measure the judge model against expert labels first',
  'Agreement with experts shows whether the judge can be trusted on this task.')
t('golden_dataset', 'Run the release against a curated golden question set',
  'A golden set with known answers catches a regression the moment it ships.')
t('rouge_bleu', 'Report ROUGE and BLEU against the reference answers',
  'Overlap metrics are cheap and reward wording that matches the references.')
t('bertscore', 'Report BERTScore for semantic similarity to the reference',
  'Embedding-based similarity credits a correct paraphrase that word overlap misses.')
t('semantic_similarity', 'Score answers by embedding similarity to the reference',
  'Similarity scoring is fast and tolerant of wording, but blind to a contradicted fact.')
t('faithfulness_metric', 'Measure whether each claim is supported by the retrieved context',
  'A faithfulness check separates a grounded answer from a fluent invention.')
t('context_precision', 'Measure whether the retrieved passages were relevant',
  'Retrieval precision explains a wrong answer that the model was given bad context for.')
t('context_recall', 'Measure whether the needed passage was retrieved at all',
  'Recall shows whether the answer was missing evidence before generation began.')
t('answer_relevance', 'Score how directly the answer addresses the question',
  'Relevance separates an off-topic answer from a factually wrong one.')
t('task_completion', 'Measure the share of agent tasks completed end to end',
  'Completion rate is the outcome metric for an agent that must actually finish work.')
t('tool_call_accuracy', 'Measure whether the agent called the right tool with the right arguments',
  'Tool accuracy locates the failure inside the agent loop rather than at the answer.')
t('ab_test', 'Split traffic between two model versions and compare outcomes',
  'An A/B test measures the difference on real traffic before a full switch.')
t('canary_eval', 'Send a small traffic share to the new prompt and watch the metrics',
  'A canary limits the blast radius of a prompt or model change.')
t('shadow_traffic', 'Mirror production traffic to the new version and compare offline',
  'Shadow traffic compares answers with no user exposure.')
t('regression_gate', 'Block the release when evaluation drops below the threshold',
  'A quality gate stops a measurable regression from reaching production.')
t('pinned_version', 'Pin the model version instead of tracking the latest alias',
  'A pinned version keeps behaviour stable until an upgrade is evaluated.')
t('context_overflow', 'Trim or chunk the request when it exceeds the context window',
  'Overflow protection keeps the prompt inside the model limit instead of truncating silently.')
t('truncation_check', 'Log the token count and check for truncated prompts',
  'A truncation check shows whether the model ever saw the end of the instruction.')
t('diff_responses', 'Diff the new responses against the previous version',
  'A diff highlights the wording and structure changes behind a quality shift.')
t('trace_reasoning', 'Inspect the agent reasoning trace for the failed task',
  'The trace shows which step misread the request or the tool result.')
t('vector_drift', 'Monitor the embedding distribution for drift',
  'A shifted embedding distribution points at a changed corpus or model.')
t('schema_validation_logs', 'Validate response structure and log the failures',
  'Structure failures appear in the logs before a downstream parser breaks.')
t('synthetic_users', 'Replay scripted user journeys against the new version',
  'Scripted journeys exercise multi-turn paths that single prompts never reach.')
t('multi_model_eval', 'Evaluate several candidate models on the same prompt set',
  'A like-for-like comparison is what makes a model choice defensible.')
t('cost_quality_ratio', 'Compare quality per thousand tokens across candidates',
  'Quality per unit of spend separates a cheaper model that is good enough from a false economy.')
t('feedback_widget', 'Collect thumbs and comments in the interface',
  'In-product feedback supplies a continuous stream of real preference data.')
t('annotation_workflow', 'Route sampled answers to an annotation workflow',
  'A labelling workflow turns raw samples into scored examples for the next evaluation.')

# --- Ingestion, formatting, and enrichment --------------------------------
t('glue_data_quality', 'Enforce freshness and completeness rules with AWS Glue Data Quality',
  'Rule sets score each batch against thresholds and stop a bad batch before it is embedded.')
t('textract_ocr', 'Extract the text from scanned pages with Amazon Textract',
  'Textract returns text and form fields from an image so it can be indexed as text.')
t('transcribe_audio', 'Transcribe the call recordings with Amazon Transcribe',
  'Transcribe turns speech into timestamped text that retrieval can search.')
t('comprehend_entities', 'Extract entities with Amazon Comprehend before indexing',
  'Entity extraction puts product codes and names in metadata for exact filtering.')
t('bedrock_reformat', 'Normalise the text with a model call before indexing',
  'A reformatting pass cleans inconsistent headings and units before embedding.')
t('json_request_format', 'Send the request as the JSON body the model expects',
  'The model API requires the prompt, parameters, and model identifier in one JSON body.')
t('conversation_format', 'Format the turns as an alternating conversation structure',
  'A dialog-shaped request keeps speaker roles and prior turns in the order the model expects.')
t('raw_text_blob', 'Concatenate all fields into one unlabelled text block',
  'A single blob loses the field boundaries the model needs to answer precisely.')
t('data_masking', 'Mask direct identifiers before the record is stored',
  'Masking removes names and account numbers while keeping the record usable.')
t('q_developer', 'Generate and explain the integration code with Amazon Q Developer',
  'Q Developer drafts and explains SDK calls inside the editor, which speeds up the plumbing.')
