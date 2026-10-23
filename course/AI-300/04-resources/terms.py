"""Original AI-300 option labels and explanations.

Every option in a question is a key in TERMS. The label is what the learner
reads; the meaning is the per-option rationale used in the CSV explanations.
"""

TERMS = {}


def t(key, label, meaning):
    if key in TERMS:
        raise ValueError(f'Duplicate term: {key}')
    TERMS[key] = (label, meaning)


# --- Domain 1: MLOps infrastructure ---------------------------------------
t('amlworkspace', 'Create a separate Azure Machine Learning workspace per environment',
  'A workspace is the top-level boundary for compute, datastores, jobs, and registered assets, so separating environments keeps development activity away from production assets.')
t('sharedworkspace', 'Use one workspace for development, test, and production',
  'A shared workspace mixes assets and identities across environments, so a test job can register over the model production is serving.')
t('computecpu', 'Attach a CPU compute cluster for the data preparation step',
  'A CPU cluster is cheaper per core and sufficient for tabular preparation, which gains nothing from an accelerator.')
t('computegpu', 'Attach a GPU cluster with a minimum of zero nodes',
  'A GPU cluster with a zero minimum scales to nothing when idle, which suits intermittent training without paying for accelerators between runs.')
t('computegpuon', 'Attach a GPU cluster with four always-on nodes',
  'Always-on GPU nodes bill continuously, including overnight and between experiments.')
t('serverless', 'Use serverless compute for the ad hoc job',
  'Serverless compute provisions per job and removes cluster management, which suits infrequent or unpredictable runs.')
t('instance', 'Run the job from a compute instance notebook',
  'A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target.')
t('datastore', 'Register a datastore that points at the storage account',
  'A datastore holds the connection and credential, so jobs reference data by name instead of an account key and physical path.')
t('inlinekey', 'Reference the storage path with the account key inline in the job YAML',
  'An inline key puts a credential in source control and ties the job to one physical path.')
t('dataasset', 'Register the data as a versioned data asset',
  'A versioned data asset records exactly which data a run used, which is what makes the model reproducible later.')
t('curatedenv', 'Build a versioned curated environment for the job',
  'A versioned environment pins the interpreter and packages, so the same job resolves the same dependencies months later.')
t('latesttag', 'Reference the floating latest tag for the environment image',
  'A floating tag resolves to a different image over time and silently breaks reproducibility.')
t('component', 'Package the preparation step as a reusable component',
  'A component gives the step a typed interface, so it can be reused in other pipelines and tested alone.')
t('registry', 'Publish the component to the workspace registry',
  'A registry shares assets across workspaces, which is how a pattern proven in development is reused in production.')
t('bicep', 'Define the workspace in a Bicep module deployed per environment',
  'Bicep gives a declarative, reviewable definition, so an environment can be recreated identically and configuration drift becomes visible.')
t('portal', 'Create the workspace in the portal and record the steps in a wiki',
  'Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting.')
t('armexport', 'Export an ARM template from the portal after building it by hand',
  'Exporting captures whatever exists, including accidental settings, and starts the estate from an unreviewed hand-built state.')
t('bicepparam', 'Pass environment values through a Bicep parameter file per stage',
  'A parameter file keeps one module per environment, so only the values differ and the shape stays identical.')
t('deploymentstack', 'Deploy the module as a deployment stack so removed resources are cleaned up',
  'A deployment stack tracks the resources it owns and can deny or delete changes made outside the template.')
t('azclijob', 'Submit the job with az ml job create --file job.yaml',
  'A declarative YAML job submitted through the CLI is repeatable and runs unchanged in continuous integration.')
t('azclistream', 'Stream the job with az ml job stream to inspect logs',
  'Streaming attaches to a running job log, which is a debugging step rather than a way to create or promote an asset.')
t('azmlonline', 'Create the endpoint first, then the deployment, with az ml online-endpoint and online-deployment',
  'A managed online endpoint must exist before a deployment is attached to it, and a deployment begins with zero traffic until one is assigned.')
t('ghworkflow', 'Run the pipeline from a GitHub Actions workflow on merge to main',
  'A workflow triggered by a merge makes the build, test, and deploy steps reviewable, repeatable, and attributable to a commit.')
t('ghoidc', 'Authenticate the workflow with workload identity federation and no stored secret',
  'Federated identity exchanges the workflow token for an Azure credential, so no long-lived secret exists to leak or rotate.')
t('ghsecret', 'Store a service principal client secret as a GitHub repository secret',
  'A stored client secret is long-lived and must be rotated; federation removes the secret entirely.')
t('ghenv', 'Use GitHub environment protection rules to gate the production deploy job',
  'A protected environment requires approval before the job runs, which is the control that stops an unreviewed deployment.')
t('ghmatrix', 'Fan the tests out across a matrix of dependency versions',
  'A matrix runs the same tests across configurations in parallel, which catches dependency drift before release.')
t('spenv', 'Create a service principal per environment with a least-privilege role assignment',
  'Scoping identity per environment limits what a compromised development pipeline can reach.')
t('spowner', 'Grant the pipeline service principal Owner on the subscription',
  'Owner on the subscription lets a pipeline change any resource, so one bad commit can affect everything.')
t('managedidentity', 'Assign a managed identity to compute and grant it the storage role',
  'A managed identity removes credentials from code entirely and is granted only the role the step needs.')
t('privateendpoint', 'Place a private endpoint on the workspace and its storage',
  'A private endpoint removes public network access, so traffic stays on the virtual network.')
t('publicaccess', 'Keep public network access enabled so notebooks connect easily',
  'Public access broadens the attack surface and usually fails a regulated review.')
t('keyvault', 'Store connection strings in Key Vault and reference them by name',
  'Key Vault centralizes the secret, so rotation happens once and no value appears in code or job YAML.')
t('plainenv', 'Set the connection string as a plain environment variable in the job',
  'A plain environment variable appears in job definitions and logs, which exposes the secret.')

# --- Domain 2: ML lifecycle and operations --------------------------------
t('pipeline', 'Define the steps as a pipeline job with explicit inputs and outputs',
  'A pipeline job makes the dependency between steps explicit and records each output, which is what gives lineage.')
t('scriptjob', 'Run the whole workflow as a single script job',
  'A single script hides intermediate artifacts, so a failed stage cannot be rerun without repeating everything.')
t('sweep', 'Run a sweep job over a searched hyperparameter space',
  'A sweep samples the search space and records every trial, which finds an optimum systematically rather than by guesswork.')
t('sweepgrid', 'Run a full grid sweep over every combination',
  'A full grid multiplies cost by the number of combinations and is rarely needed once the promising region is known.')
t('automl', 'Use automated ML to establish the tabular baseline',
  'Automated ML tests preprocessing and algorithm combinations quickly, which is a reasonable baseline for tabular data.')
t('mlflow', 'Enable MLflow tracking so runs log to the workspace',
  'MLflow records parameters, metrics, and artifacts against a run, which is what makes experiments comparable.')
t('mlflowuri', 'Point the MLflow tracking URI at the workspace endpoint',
  'The tracking URI decides which workspace receives the run; without it, logging lands only on the local filesystem.')
t('mlflowlog', 'Log metrics and the model artifact explicitly in the training script',
  'Explicit logging captures the numbers and artifact a comparison needs; without it the run records only that it happened.')
t('printmetrics', 'Print the metrics to the job log and read them from the console',
  'Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires.')
t('experiment', 'Group the trials under a named experiment',
  'An experiment groups related runs, which is how variants of the same task are compared against each other.')
t('modellatest', 'Register the model and always deploy whichever version is latest',
  'Deploying whatever is latest lets an untested registration reach production with no promotion gate.')
t('modelversion', 'Register each candidate with a version and deploy one explicit version',
  'An explicit version pins what is served, so a new registration cannot silently change production behaviour.')
t('modeltags', 'Tag the registered model with the data asset and commit it came from',
  'Tags carry provenance, which is what an audit needs in order to rebuild the artifact.')
t('modelcard', 'Attach a description, metrics, and intended use to the model version',
  'Documented metrics and intended use let a reviewer decide whether the version is fit to promote.')
t('alias', 'Promote versions through aliases such as candidate and production',
  'An alias gives a stable pointer that a deployment can resolve, so promotion is a controlled switch rather than an edit.')
t('overwritemodel', 'Overwrite the existing model version instead of registering a new one',
  'Overwriting destroys the previous artifact and the audit trail that rollback depends on.')
t('onlineendpoint', 'Deploy to a managed online endpoint with an explicit model version',
  'A managed online endpoint serves real-time requests and manages the underlying infrastructure.')
t('batchendpoint', 'Deploy a batch endpoint for the overnight scoring job',
  'A batch endpoint scores a large file on a schedule and needs no always-on capacity.')
t('batchasonline', 'Send the overnight file through the online endpoint request by request',
  'Scoring a large file one request at a time pays for always-on capacity and is slow for bulk work.')
t('trafficsplit', 'Split endpoint traffic 10/90 so the new deployment receives a canary share',
  'A traffic split sends a small share to the new deployment, so a regression affects fewer requests and is measurable.')
t('straightcut', 'Replace the production deployment in a single step',
  'A one-step replacement exposes every request to an unproven version with no measured canary.')
t('keepblue', 'Keep the previous deployment in place so traffic can be moved back',
  'A retained deployment makes rollback a traffic change rather than a rebuild and redeploy.')
t('autoscale', 'Set autoscale rules on the deployment with a deliberate minimum instance count',
  'Autoscale matches capacity to load, and the minimum sets the floor that protects latency during a burst.')
t('fixedscale', 'Pin a fixed instance count for a spiky workload',
  'A fixed count either wastes money at low load or throttles at peak.')
t('probes', 'Configure liveness and readiness probes on the deployment',
  'Liveness restarts an unhealthy container and readiness keeps traffic away until the container can actually serve.')
t('noprobe', 'Deploy without probes and rely on the platform health check',
  'Without probes, a container that starts but cannot load the model still receives traffic.')
t('modelmount', 'Mount the model artifact rather than baking it into the image',
  'Mounting keeps the artifact out of the image, so a new version does not require an image rebuild.')
t('bakeimage', 'Bake the model weights into the container image',
  'Baking the model ties every version to an image build, which slows promotion and bloats the registry.')
t('driftmonitor', 'Enable data drift monitoring against the training baseline',
  'Drift monitoring compares live input distributions with the training baseline, which is what catches silent degradation.')
t('driftalert', 'Create an alert rule on the drift and latency metrics',
  'An alert turns a metric into an action; without it a drift report is noticed only if someone reads it.')
t('accsnapshot', 'Monitor only the accuracy reported at deployment time',
  'Deployment-time accuracy is a snapshot; it says nothing about the data that arrives afterwards.')

# --- Domain 3: GenAIOps infrastructure ------------------------------------
t('foundryhub', 'Create a Foundry hub and a project per team',
  'A hub shares connections and capacity, and a project gives a team an isolated working boundary for its own assets.')
t('foundryshared', 'Give every team one project and one shared connection',
  'A single shared project mixes assets and permissions, so one team can change what another depends on.')
t('modelcatalog', 'Select a model from the catalog and deploy it into the project',
  'The catalog lists models with their capabilities; deploying one into the project makes it addressable by a deployment name.')
t('depname', 'Reference the deployment name from the flow rather than the model family name',
  'A flow calls a deployment, so the deployment name stays the stable reference when the underlying model changes.')
t('hardcodemodel', 'Hardcode the model family name inside the flow',
  'A family name is not an addressable endpoint; the flow needs a deployment to call.')
t('ptu', 'Reserve provisioned throughput for the steady high-volume workload',
  'Provisioned throughput reserves capacity, which gives predictable latency and cost at sustained volume.')
t('payg', 'Start on pay-as-you-go while the volume is still unknown',
  'Pay-as-you-go costs nothing when idle and needs no forecast, which suits an unproven workload.')
t('contentfilter', 'Apply a content filter policy appropriate to the audience',
  'A content filter policy sets the harm thresholds applied to prompts and completions for that deployment.')
t('flowdag', 'Author the flow as a directed acyclic graph with typed inputs and outputs',
  'A typed graph makes each step contract explicit, so the flow can be tested in isolation and composed with others.')
t('flowvariant', 'Create a variant to compare two prompt strategies side by side',
  'Variants keep the alternatives together, so the comparison is reproducible rather than remembered.')
t('flowconnection', 'Store the model credential as a project connection',
  'A project connection holds the endpoint and credential outside the flow, so the flow file stays secret-free.')
t('hardcodekey', 'Paste the API key into a Python node inside the flow',
  'A key inside a flow file is a secret in source control and cannot be rotated without editing the flow.')
t('flowdeploy', 'Deploy the flow to a managed online endpoint',
  'Deploying the flow exposes it as a service the application can call.')
t('flowbatch', 'Run the flow as a batch job over the evaluation dataset',
  'A batch run applies the flow to every row, which is how an evaluation dataset is scored.')
t('promptfile', 'Keep the prompt in its own file under version control',
  'A separate versioned prompt file makes every change reviewable and revertible.')
t('exportdata', 'Export the corpus to storage and index it as files',
  'Exporting licensed content into your own storage is the step the licence usually forbids, so the copy itself is the risk.')
t('graphconnector', 'Build a knowledge-source connector that indexes the whole corpus into the project',
  'Copying a licensed corpus into an index you host is a storage and licence decision, not just a connector setting.')
t('federated', 'Connect to the source through a federated connector and query it in place',
  'A federated connector answers from content where it already lives, so licensed material need not be copied into a store you are not entitled to build.')
t('searchindex', 'Index the documents in Azure AI Search and query the index from the flow',
  'An index supports retrieval at answer time, so the flow grounds on current content instead of on model memory.')
t('finetuneinstead', 'Fine-tune the model on the document set instead of retrieving',
  'Fine-tuning bakes a snapshot of the content into the model, so it goes stale as documents change.')
t('hybrid', 'Use hybrid search with semantic ranking',
  'Hybrid search combines keyword and vector matching, and semantic ranking reorders the top results, which improves recall on domain vocabulary and identifiers.')
t('vectoronly', 'Use vector search alone with no keyword component',
  'Vector-only retrieval misses exact identifiers and product codes, which is where keyword matching earns its place.')
t('chunksection', 'Chunk documents by section with a small overlap',
  'Section-sized chunks with overlap keep a passage coherent while staying small enough to be specific.')
t('chunkwhole', 'Index each document as one large chunk',
  'A whole-document chunk makes retrieval return an undifferentiated document, so the answer quotes the wrong part.')
t('indexschedule', 'Rebuild the index on a schedule after the source content changes',
  'Scheduled refresh keeps retrieval aligned with the source; without it the assistant answers from retired content.')
t('indexacl', 'Set document-level access in the index so retrieval respects entitlements',
  'Document-level access keeps retrieval within what the requesting user is allowed to see.')
t('bindindex', 'Bind the flow to the search index as its data source',
  'A bound data source is what the flow retrieves from; an unbound flow has nothing to ground on.')
t('agenttools', 'Register a scoped tool list for the agent',
  'A scoped tool list bounds what the agent can do, which is the main control over unintended actions.')
t('agentalltools', 'Expose every available tool so the agent can choose freely',
  'An open tool list widens the blast radius of a wrong tool choice.')
t('sessionmemory', 'Bound the agent memory to the current session',
  'Session-scoped memory keeps context within a conversation and stops one user facts leaking into another.')
t('typedstate', 'Pass typed state between agent steps',
  'Typed state makes each handoff explicit and testable instead of relying on free text.')

# --- Domain 4: QA and observability ---------------------------------------
t('goldenset', 'Build the evaluation dataset from real queries with graded answers',
  'A dataset drawn from real traffic with graded answers is what makes an evaluation number mean something.')
t('syntheticset', 'Generate the evaluation set from the prompt itself',
  'A set authored from the prompt repeats its assumptions, so it passes changes that real users would reject.')
t('samplesize', 'Use a few hundred representative cases rather than a dozen',
  'A small sample produces a confidence interval too wide to separate a real improvement from noise.')
t('groundedness', 'Score groundedness against the retrieved passages',
  'Groundedness asks whether the answer is supported by the retrieved context, which is the core anti-fabrication metric.')
t('relevance', 'Score relevance of the answer to the question asked',
  'Relevance asks whether the answer addresses what was asked, independently of whether it is true.')
t('fluency', 'Score fluency for readability and language quality',
  'Fluency measures readability and language quality, not factual support.')
t('coherence', 'Score coherence for logical structure',
  'Coherence measures whether the answer holds together logically, not whether it is grounded in a source.')
t('similarity', 'Score similarity against a reference answer',
  'Similarity compares the answer with a reference, which requires a reference answer for every case.')
t('retrievalrecall', 'Measure retrieval recall before scoring answer quality',
  'If retrieval never returned the passage, an answer-quality score is measuring the wrong component.')
t('judge', 'Use an LLM judge with a rubric, calibrated against human grades',
  'An LLM judge scales grading, and calibrating it against human grades is what keeps the score trustworthy.')
t('judgealone', 'Rely on the LLM judge without checking it against human grades',
  'An uncalibrated judge can reproduce a systematic error consistently and look stable while being wrong.')
t('offlinegate', 'Run the evaluation in continuous integration before the flow is promoted',
  'An offline gate stops a regression before it reaches production traffic.')
t('onlineeval', 'Run continuous evaluation on sampled production traffic',
  'Online evaluation catches the drift that a fixed offline dataset cannot represent.')
t('toxicity', 'Evaluate toxicity against the threshold the audience requires',
  'Toxicity evaluation measures harmful output against the standard that audience or regulation requires.')
t('jailbreak', 'Run adversarial jailbreak and prompt-injection cases before release',
  'Adversarial cases test whether instructions in the input or the content can override the system prompt.')
t('indirect', 'Test indirect injection through retrieved documents',
  'Indirect injection hides instructions in retrieved content, which is the vector a retrieval system most easily misses.')
t('tracing', 'Enable distributed tracing and log the retrieval and model spans',
  'Span-level tracing shows which stage produced a wrong answer, which an aggregate score cannot.')
t('promptlogging', 'Log prompts and completions against the trace, within data policy',
  'Full prompt and completion logging is what lets a reviewer reproduce a bad answer.')
t('nologging', 'Disable request logging to reduce storage cost',
  'Disabling logging removes the evidence an investigation needs and usually breaches the retention policy.')
t('feedbackloop', 'Capture user feedback and review a sample of rated conversations weekly',
  'User feedback is the only signal about traffic that the evaluation set does not contain.')
t('feedbackignore', 'Collect user feedback but leave it unread in the dashboard',
  'Feedback that nobody triages is a record of dissatisfaction rather than an improvement loop.')

# --- Domain 5: optimization ----------------------------------------------
t('tokenbudget', 'Measure tokens per request and set a budget per endpoint',
  'Tokens are the billing unit, so per-request measurement is what makes cost attributable to a workload.')
t('cache', 'Cache identical requests and reuse the completion',
  'Caching removes repeated inference for identical input, which is the cheapest saving available.')
t('cachettl', 'Set a time-to-live on the cache',
  'A TTL keeps a cached answer from outliving the content it came from.')
t('promptcompress', 'Compress the system prompt and remove redundant instructions',
  'A shorter system prompt reduces input tokens on every single call.')
t('ragfewer', 'Retrieve fewer but better-ranked passages',
  'Retrieval depth is a direct cost driver; fewer, better passages cut tokens and can improve precision.')
t('ragmax', 'Raise retrieval depth to the maximum for safety',
  'Retrieving more passages adds tokens and can bury the relevant passage among distractors.')
t('smallmodel', 'Route simple requests to a smaller model',
  'A smaller model answers a simple request at a fraction of the cost and latency.')
t('bigmodel', 'Use the largest model for every request',
  'The largest model adds cost and latency to requests that do not need its capability.')
t('router', 'Add a router that classifies the request and selects a model',
  'A router applies a cheap model where it suffices and keeps the stronger model for hard cases.')
t('streaming', 'Stream the response so the first token arrives sooner',
  'Streaming improves perceived latency without changing total generation time.')
t('timeout', 'Set a request timeout with a bounded retry and backoff',
  'A bounded retry with backoff stops a failing dependency from multiplying load.')
t('batchoffline', 'Move non-urgent generation into a batch run',
  'Batch work uses cheaper capacity and takes the work off the interactive path.')
t('quantized', 'Use a quantized deployment for the high-throughput tier',
  'Quantization reduces memory and can raise throughput per unit of capacity at some quality cost.')
t('ftshorten', 'Fine-tune on approved examples to shorten the standing prompt',
  'Fine-tuning can absorb instructions and style into the weights, which shortens prompts for a stable task.')
t('ptumove', 'Move steady traffic to provisioned throughput',
  'Provisioned throughput trades a commitment for a lower cost per token at sustained volume.')
t('reevaluate', 'Re-run the evaluation after the cost optimization',
  'An optimization that lowers cost can lower quality, and re-running the evaluation is what proves the trade is acceptable.')
t('shipwatch', 'Ship the optimization and watch the support queue',
  'The support queue is a lagging signal that reports damage after users have already experienced it.')

# --- Recurring distractor concepts ---------------------------------------
t('retrain', 'Retrain the model on the newer data',
  'Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt.')
t('bigger', 'Increase the model size until the answers improve',
  'Model size does not repair missing context; without the passage, a larger model still guesses.')
t('promptonly', 'Rewrite the prompt and deploy it immediately',
  'A prompt change shipped without an evaluation gate is an unmeasured change to a production system.')
t('indexall', 'Index every document the organization holds',
  'Indexing everything raises noise and cost, and can make content retrievable that should never be returned.')
t('humanonly', 'Assign the work to a person instead of investigating the failure',
  'Replacing the automation resolves the symptom without discovering why the system failed.')
t('ignorealarm', 'Accept the behaviour because the aggregate score still looks healthy',
  'An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for.')
t('manualrecreate', 'Rebuild the environment by hand from the notes in the ticket',
  'A hand rebuild cannot be reproduced exactly and drifts from the definition the team believed it had.')
t('skipstaging', 'Deploy straight to production to save a day',
  'Skipping the staged check saves a day and moves the discovery of a defect to a customer.')

# Candidate orderings for the sequencing items live in their own module so the
# technical option bank stays readable.
from sequences import SEQUENCES

for _key, _value in SEQUENCES.items():
    if _key in TERMS:
        raise ValueError(f'Duplicate term: {_key}')
    TERMS[_key] = _value
