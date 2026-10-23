# Microsoft AI-300 — Full-Length Mock Exam 3

Machine Learning Operations Engineer · 100 questions · expanded practice bank · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 84 multiple-choice (selection count stated where needed), 16 multi-select, and 4 case studies of 3 questions. 8 of the multiple-choice items ask you to choose the correct candidate sequence. Drag-and-drop sequencing UI, live lab environments, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. A regulatory submission requires that a scoring environment be reproducible from a dated definition. What should be published?

Domain: Design and implement an MLOps infrastructure

- A. Reference the floating latest tag for the environment image
- B. Build a versioned curated environment for the job
- C. Run the job from a compute instance notebook
- D. Print the metrics to the job log and read them from the console

### 2. A safety audit asks which patient cohort trained the deployed triage model. What should be registered?

Domain: Design and implement an MLOps infrastructure

- A. Register the data as a versioned data asset
- B. Reference the storage path with the account key inline in the job YAML
- C. Disable request logging to reduce storage cost
- D. Register a datastore that points at the storage account

### 3. A hospital group must stand up an isolated workspace for a new region under change control. What should be used?

Domain: Design and implement an MLOps infrastructure

- A. Rebuild the environment by hand from the notes in the ticket
- B. Create the workspace in the portal and record the steps in a wiki
- C. Define the workspace in a Bicep module deployed per environment
- D. Export an ARM template from the portal after building it by hand

### 4. Clinical data may not traverse public networks. What must the workspace and storage use?

Domain: Design and implement an MLOps infrastructure

- A. Reference the storage path with the account key inline in the job YAML
- B. Place a private endpoint on the workspace and its storage
- C. Set the connection string as a plain environment variable in the job
- D. Keep public network access enabled so notebooks connect easily

### 5. One module must produce three regional deployments differing only in location and capacity. What should vary?

Domain: Design and implement an MLOps infrastructure

- A. Rebuild the environment by hand from the notes in the ticket
- B. Export an ARM template from the portal after building it by hand
- C. Create the workspace in the portal and record the steps in a wiki
- D. Pass environment values through a Bicep parameter file per stage

### 6. Retraining must be triggered by a scheduler with no human in a notebook. What should be used?

Domain: Design and implement an MLOps infrastructure

- A. Create the workspace in the portal and record the steps in a wiki
- B. Run the job from a compute instance notebook
- C. Submit the job with az ml job create --file job.yaml
- D. Stream the job with az ml job stream to inspect logs

### 7. A pipeline must reach Azure with no stored secret that could be exfiltrated from the repository. What should authenticate it?

Domain: Design and implement an MLOps infrastructure

- A. Grant the pipeline service principal Owner on the subscription
- B. Store a service principal client secret as a GitHub repository secret
- C. Set the connection string as a plain environment variable in the job
- D. Authenticate the workflow with workload identity federation and no stored secret

### 8. A compromise of the staging pipeline must not permit changes in production. What limits it?

Domain: Design and implement an MLOps infrastructure

- A. Set the connection string as a plain environment variable in the job
- B. Keep public network access enabled so notebooks connect easily
- C. Create a service principal per environment with a least-privilege role assignment
- D. Grant the pipeline service principal Owner on the subscription

### 9. A served model must be identified exactly when a clinician disputes a decision. What pins it?

Domain: Design and implement an MLOps infrastructure

- A. Register the model and always deploy whichever version is latest
- B. Overwrite the existing model version instead of registering a new one
- C. Accept the behaviour because the aggregate score still looks healthy
- D. Register each candidate with a version and deploy one explicit version

### 10. A scoring container must read from storage without any credential in its configuration. What should it use?

Domain: Design and implement an MLOps infrastructure

- A. Set the connection string as a plain environment variable in the job
- B. Assign a managed identity to compute and grant it the storage role
- C. Reference the storage path with the account key inline in the job YAML
- D. Grant the pipeline service principal Owner on the subscription

### 11. A clinical environment must isolate assets and stay off the public network. Which two configurations apply? Select two.

Domain: Design and implement an MLOps infrastructure

- A. Create the workspace in the portal and record the steps in a wiki
- B. Place a private endpoint on the workspace and its storage
- C. Keep public network access enabled so notebooks connect easily
- D. Use one workspace for development, test, and production
- E. Create a separate Azure Machine Learning workspace per environment

### 12. A regional workspace must be reproducible and free of manual drift. Which two practices apply? Select two.

Domain: Design and implement an MLOps infrastructure

- A. Export an ARM template from the portal after building it by hand
- B. Rebuild the environment by hand from the notes in the ticket
- C. Deploy the module as a deployment stack so removed resources are cleaned up
- D. Create the workspace in the portal and record the steps in a wiki
- E. Define the workspace in a Bicep module deployed per environment

### 13. A reviewer must see that evaluation consumed the trained artifact from the same run. What provides that?

Domain: Implement machine learning model lifecycle and operations

- A. Define the steps as a pipeline job with explicit inputs and outputs
- B. Run the whole workflow as a single script job
- C. Run the job from a compute instance notebook
- D. Assign the work to a person instead of investigating the failure

### 14. Two candidate models achieved the same headline metric and the team must know which preprocessing each used. What should be tracked?

Domain: Implement machine learning model lifecycle and operations

- A. Print the metrics to the job log and read them from the console
- B. Assign the work to a person instead of investigating the failure
- C. Enable MLflow tracking so runs log to the workspace
- D. Disable request logging to reduce storage cost

### 15. A clinical reviewer must judge whether a version is appropriate before promotion. What should the version carry?

Domain: Implement machine learning model lifecycle and operations

- A. Register the model and always deploy whichever version is latest
- B. Accept the behaviour because the aggregate score still looks healthy
- C. Tag the registered model with the data asset and commit it came from
- D. Attach a description, metrics, and intended use to the model version

### 16. An auditor must rebuild a two-year-old model from scratch. What must be recorded at registration?

Domain: Implement machine learning model lifecycle and operations

- A. Attach a description, metrics, and intended use to the model version
- B. Overwrite the existing model version instead of registering a new one
- C. Print the metrics to the job log and read them from the console
- D. Tag the registered model with the data asset and commit it came from

### 17. A newly started container returns errors while it loads weights. What prevents traffic reaching it?

Domain: Implement machine learning model lifecycle and operations

- A. Pin a fixed instance count for a spiky workload
- B. Configure liveness and readiness probes on the deployment
- C. Deploy without probes and rely on the platform health check
- D. Monitor only the accuracy reported at deployment time

### 18. A new triage model must affect at most ten percent of decisions before review. What should be configured?

Domain: Implement machine learning model lifecycle and operations

- A. Split endpoint traffic 10/90 so the new deployment receives a canary share
- B. Keep the previous deployment in place so traffic can be moved back
- C. Replace the production deployment in a single step
- D. Deploy straight to production to save a day

### 19. A model must be withdrawn within fifteen minutes if a defect appears. What enables that?

Domain: Implement machine learning model lifecycle and operations

- A. Overwrite the existing model version instead of registering a new one
- B. Keep the previous deployment in place so traffic can be moved back
- C. Replace the production deployment in a single step
- D. Bake the model weights into the container image

### 20. A new scanner changed image statistics and nobody noticed a quality fall. What should be enabled?

Domain: Implement machine learning model lifecycle and operations

- A. Enable data drift monitoring against the training baseline
- B. Monitor only the accuracy reported at deployment time
- C. Retrain the model on the newer data
- D. Accept the behaviour because the aggregate score still looks healthy

### 21. A weekly drift report is produced and reviewed only when an incident occurs. What is missing?

Domain: Implement machine learning model lifecycle and operations

- A. Create an alert rule on the drift and latency metrics
- B. Assign the work to a person instead of investigating the failure
- C. Monitor only the accuracy reported at deployment time
- D. Disable request logging to reduce storage cost

### 22. The only quality number available is the one recorded on the deployment day. What is the gap?

Domain: Implement machine learning model lifecycle and operations

- A. Monitor only the accuracy reported at deployment time
- B. Enable data drift monitoring against the training baseline
- C. Create an alert rule on the drift and latency metrics
- D. Assign the work to a person instead of investigating the failure

### 23. A tuning exercise must stay inside a fixed GPU-hour budget across a wide space. What should be used?

Domain: Implement machine learning model lifecycle and operations

- A. Run a sweep job over a searched hyperparameter space
- B. Use automated ML to establish the tabular baseline
- C. Run a full grid sweep over every combination
- D. Increase the model size until the answers improve

### 24. Vision training runs intermittently and the team is billed for accelerators overnight. What should change?

Domain: Implement machine learning model lifecycle and operations

- A. Attach a GPU cluster with four always-on nodes
- B. Attach a CPU compute cluster for the data preparation step
- C. Attach a GPU cluster with a minimum of zero nodes
- D. Run the job from a compute instance notebook

### 25. A plant needs a credible first model for a tabular quality problem within a week. What fits?

Domain: Implement machine learning model lifecycle and operations

- A. Run the job from a compute instance notebook
- B. Run a sweep job over a searched hyperparameter space
- C. Run the whole workflow as a single script job
- D. Use automated ML to establish the tabular baseline

### 26. An audit needs lineage and a pinned artifact. Which two practices apply? Select two.

Domain: Implement machine learning model lifecycle and operations

- A. Define the steps as a pipeline job with explicit inputs and outputs
- B. Register the model and always deploy whichever version is latest
- C. Assign the work to a person instead of investigating the failure
- D. Register each candidate with a version and deploy one explicit version
- E. Run the whole workflow as a single script job

### 27. A release must be measured on a small share and reversible quickly. Which two controls apply? Select two.

Domain: Implement machine learning model lifecycle and operations

- A. Split endpoint traffic 10/90 so the new deployment receives a canary share
- B. Keep the previous deployment in place so traffic can be moved back
- C. Replace the production deployment in a single step
- D. Overwrite the existing model version instead of registering a new one
- E. Bake the model weights into the container image

### 28. A clinical model must reach production behind a measured gate. Which sequence is correct?

Domain: Implement machine learning model lifecycle and operations

- A. Train the candidate → evaluate against the gate → register the model version → deploy at a canary traffic share → shift all traffic after the metrics hold
- B. Register the model version → train the candidate → evaluate against the gate → shift all traffic
- C. Deploy at a canary traffic share → train the candidate → register the model version → evaluate against the gate
- D. Evaluate against the gate → train the candidate → shift all traffic → register the model version

### 29. Research and clinical teams need shared capacity but separate assets. What should be created?

Domain: Design and implement a GenAIOps infrastructure

- A. Create a Foundry hub and a project per team
- B. Give every team one project and one shared connection
- C. Create the workspace in the portal and record the steps in a wiki
- D. Use one workspace for development, test, and production

### 30. A flow broke when the model behind its deployment was replaced. What should the flow call?

Domain: Design and implement a GenAIOps infrastructure

- A. Hardcode the model family name inside the flow
- B. Select a model from the catalog and deploy it into the project
- C. Reference the deployment name from the flow rather than the model family name
- D. Paste the API key into a Python node inside the flow

### 31. A clinical assistant must apply harm thresholds to prompts and completions. What should be configured?

Domain: Design and implement a GenAIOps infrastructure

- A. Accept the behaviour because the aggregate score still looks healthy
- B. Evaluate toxicity against the threshold the audience requires
- C. Run adversarial jailbreak and prompt-injection cases before release
- D. Apply a content filter policy appropriate to the audience

### 32. A hospital runs a steady clinical assistant workload all day with predictable volume. What deployment option fits?

Domain: Design and implement a GenAIOps infrastructure

- A. Use the largest model for every request
- B. Start on pay-as-you-go while the volume is still unknown
- C. Reserve provisioned throughput for the steady high-volume workload
- D. Pin a fixed instance count for a spiky workload

### 33. A clinical summarization flow must be tested node by node before release. What should it be authored as?

Domain: Design and implement a GenAIOps infrastructure

- A. Run the flow as a batch job over the evaluation dataset
- B. Run the job from a compute instance notebook
- C. Author the flow as a directed acyclic graph with typed inputs and outputs
- D. Run the whole workflow as a single script job

### 34. Two summarization strategies must be compared on the same encounters. What should be used?

Domain: Design and implement a GenAIOps infrastructure

- A. Hardcode the model family name inside the flow
- B. Rewrite the prompt and deploy it immediately
- C. Author the flow as a directed acyclic graph with typed inputs and outputs
- D. Create a variant to compare two prompt strategies side by side

### 35. A flow must reference a model endpoint without storing its credential in the flow. What should be used?

Domain: Design and implement a GenAIOps infrastructure

- A. Reference the storage path with the account key inline in the job YAML
- B. Paste the API key into a Python node inside the flow
- C. Store the model credential as a project connection
- D. Set the connection string as a plain environment variable in the job

### 36. Clinical guidance changes monthly and answers must cite the current version. What should be used?

Domain: Design and implement a GenAIOps infrastructure

- A. Index the documents in Azure AI Search and query the index from the flow
- B. Increase the model size until the answers improve
- C. Fine-tune the model on the document set instead of retrieving
- D. Index every document the organization holds

### 37. A shared index serves several hospitals and each clinician may see only their own patients. What must be configured?

Domain: Design and implement a GenAIOps infrastructure

- A. Index every document the organization holds
- B. Keep public network access enabled so notebooks connect easily
- C. Set the connection string as a plain environment variable in the job
- D. Set document-level access in the index so retrieval respects entitlements

### 38. Retrieval cannot find device identifiers such as PX-9002. What should be used?

Domain: Design and implement a GenAIOps infrastructure

- A. Use vector search alone with no keyword component
- B. Increase the model size until the answers improve
- C. Use hybrid search with semantic ranking
- D. Fine-tune the model on the document set instead of retrieving

### 39. An answer cites the right protocol but the wrong step. What should change?

Domain: Design and implement a GenAIOps infrastructure

- A. Raise retrieval depth to the maximum for safety
- B. Index every document the organization holds
- C. Chunk documents by section with a small overlap
- D. Index each document as one large chunk

### 40. A guideline update is published and the assistant keeps quoting the previous version. What should be configured?

Domain: Design and implement a GenAIOps infrastructure

- A. Retrain the model on the newer data
- B. Chunk documents by section with a small overlap
- C. Index every document the organization holds
- D. Rebuild the index on a schedule after the source content changes

### 41. Retrieval returns an entire protocol document and the model quotes an unrelated paragraph. What caused it?

Domain: Design and implement a GenAIOps infrastructure

- A. Chunk documents by section with a small overlap
- B. Index each document as one large chunk
- C. Index every document the organization holds
- D. Retrain the model on the newer data

### 42. A prompt change must not reach clinicians until quality is measured. What should be in place?

Domain: Design and implement a GenAIOps infrastructure

- A. Assign the work to a person instead of investigating the failure
- B. Deploy straight to production to save a day
- C. Run the evaluation in continuous integration before the flow is promoted
- D. Rewrite the prompt and deploy it immediately

### 43. A validated process requires a documented record for each prompt change. Where should prompts live?

Domain: Design and implement a GenAIOps infrastructure

- A. Paste the API key into a Python node inside the flow
- B. Create a variant to compare two prompt strategies side by side
- C. Keep the prompt in its own file under version control
- D. Rewrite the prompt and deploy it immediately

### 44. A care-coordination agent can reach an ordering system that must stay out of scope. What should change?

Domain: Design and implement a GenAIOps infrastructure

- A. Register a scoped tool list for the agent
- B. Index every document the organization holds
- C. Increase the model size until the answers improve
- D. Expose every available tool so the agent can choose freely

### 45. A conversation carried one patient's details into the next. What should be configured?

Domain: Design and implement a GenAIOps infrastructure

- A. Index every document the organization holds
- B. Bound the agent memory to the current session
- C. Pass typed state between agent steps
- D. Expose every available tool so the agent can choose freely

### 46. A safety committee asks what evidence the evaluation was built on. What should it contain?

Domain: Implement generative AI quality assurance and observability

- A. Build the evaluation dataset from real queries with graded answers
- B. Assign the work to a person instead of investigating the failure
- C. Accept the behaviour because the aggregate score still looks healthy
- D. Generate the evaluation set from the prompt itself

### 47. Three thousand encounter summaries must be graded within a release cycle. What should be built?

Domain: Implement generative AI quality assurance and observability

- A. Generate the evaluation set from the prompt itself
- B. Rely on the LLM judge without checking it against human grades
- C. Assign the work to a person instead of investigating the failure
- D. Use an LLM judge with a rubric, calibrated against human grades

### 48. A draft states a dosage that no retrieved note contains. Which metric targets this?

Domain: Implement generative AI quality assurance and observability

- A. Score relevance of the answer to the question asked
- B. Score coherence for logical structure
- C. Score fluency for readability and language quality
- D. Score groundedness against the retrieved passages

### 49. An answer faithfully summarizes a passage about a different condition. Which metric catches it?

Domain: Implement generative AI quality assurance and observability

- A. Score groundedness against the retrieved passages
- B. Score fluency for readability and language quality
- C. Score relevance of the answer to the question asked
- D. Score similarity against a reference answer

### 50. A scanned referral contains text that instructs the assistant to ignore policy. What is the exposure?

Domain: Implement generative AI quality assurance and observability

- A. Run adversarial jailbreak and prompt-injection cases before release
- B. Test indirect injection through retrieved documents
- C. Disable request logging to reduce storage cost
- D. Evaluate toxicity against the threshold the audience requires

### 51. A clinician disputes an answer and the team must find which stage failed. What should be enabled?

Domain: Implement generative AI quality assurance and observability

- A. Enable distributed tracing and log the retrieval and model spans
- B. Rely on the LLM judge without checking it against human grades
- C. Disable request logging to reduce storage cost
- D. Log prompts and completions against the trace, within data policy

### 52. A defect must be replayed ninety days later within the retention policy. What must have been captured?

Domain: Implement generative AI quality assurance and observability

- A. Assign the work to a person instead of investigating the failure
- B. Enable distributed tracing and log the retrieval and model spans
- C. Log prompts and completions against the trace, within data policy
- D. Disable request logging to reduce storage cost

### 53. Clinicians downvote a specific class of answers that the dataset does not include. What should be built?

Domain: Implement generative AI quality assurance and observability

- A. Rely on the LLM judge without checking it against human grades
- B. Capture user feedback and review a sample of rated conversations weekly
- C. Run continuous evaluation on sampled production traffic
- D. Run the evaluation in continuous integration before the flow is promoted

### 54. A committee needs a credible evaluation basis. Which two properties matter? Select two.

Domain: Implement generative AI quality assurance and observability

- A. Assign the work to a person instead of investigating the failure
- B. Accept the behaviour because the aggregate score still looks healthy
- C. Build the evaluation dataset from real queries with graded answers
- D. Generate the evaluation set from the prompt itself
- E. Use a few hundred representative cases rather than a dozen

### 55. An assistant reads scanned documents and must resist override from both documents and users. Which two test types apply? Select two.

Domain: Implement generative AI quality assurance and observability

- A. Run adversarial jailbreak and prompt-injection cases before release
- B. Test indirect injection through retrieved documents
- C. Evaluate toxicity against the threshold the audience requires
- D. Disable request logging to reduce storage cost
- E. Score fluency for readability and language quality

### 56. A disputed answer must be explainable and reproducible. Which two practices apply? Select two.

Domain: Implement generative AI quality assurance and observability

- A. Rely on the LLM judge without checking it against human grades
- B. Enable distributed tracing and log the retrieval and model spans
- C. Disable request logging to reduce storage cost
- D. Assign the work to a person instead of investigating the failure
- E. Log prompts and completions against the trace, within data policy

### 57. A clinical answer must be supported and on point. Which two metrics apply? Select two.

Domain: Implement generative AI quality assurance and observability

- A. Score groundedness against the retrieved passages
- B. Score coherence for logical structure
- C. Score fluency for readability and language quality
- D. Score relevance of the answer to the question asked
- E. Score similarity against a reference answer

### 58. A clinician escalates a wrong answer and the team must explain it. Which sequence is correct?

Domain: Implement generative AI quality assurance and observability

- A. Add the case to the evaluation set → inspect the completion → open the failing request trace → inspect the retrieval span
- B. Inspect the retrieval span → retrain the model → open the trace → add the case to the evaluation set
- C. Retrain the model → open the trace → inspect the retrieval span → add the case to the evaluation set
- D. Open the failing request trace → inspect the retrieval span for the passages returned → inspect the prompt and completion for that call → add the case to the evaluation set

### 59. A hospital cannot attribute model spend to a department. What must be measured first?

Domain: Optimize generative AI systems and model performance

- A. Use the largest model for every request
- B. Cache identical requests and reuse the completion
- C. Accept the behaviour because the aggregate score still looks healthy
- D. Measure tokens per request and set a budget per endpoint

### 60. A cached answer still quotes guidance replaced last month. What should be configured?

Domain: Optimize generative AI systems and model performance

- A. Accept the behaviour because the aggregate score still looks healthy
- B. Set a time-to-live on the cache
- C. Disable request logging to reduce storage cost
- D. Cache identical requests and reuse the completion

### 61. Most clinical lookups are single-field questions and every call uses the largest model. What should change?

Domain: Optimize generative AI systems and model performance

- A. Retrain the model on the newer data
- B. Route simple requests to a smaller model
- C. Increase the model size until the answers improve
- D. Use the largest model for every request

### 62. One endpoint must serve both quick lookups and long case summaries. What should be added?

Domain: Optimize generative AI systems and model performance

- A. Cache identical requests and reuse the completion
- B. Route simple requests to a smaller model
- C. Use the largest model for every request
- D. Add a router that classifies the request and selects a model

### 63. Sixteen passages are retrieved per answer and most are irrelevant. What should change?

Domain: Optimize generative AI systems and model performance

- A. Increase the model size until the answers improve
- B. Retrieve fewer but better-ranked passages
- C. Index every document the organization holds
- D. Raise retrieval depth to the maximum for safety

### 64. A 5,500-token system prompt ships with every request and much of it repeats. What should be done?

Domain: Optimize generative AI systems and model performance

- A. Cache identical requests and reuse the completion
- B. Increase the model size until the answers improve
- C. Compress the system prompt and remove redundant instructions
- D. Raise retrieval depth to the maximum for safety

### 65. A stable extraction task carries a long instruction on every call. What can absorb it?

Domain: Optimize generative AI systems and model performance

- A. Fine-tune the model on the document set instead of retrieving
- B. Increase the model size until the answers improve
- C. Fine-tune on approved examples to shorten the standing prompt
- D. Compress the system prompt and remove redundant instructions

### 66. Steady clinical volume has run for six months and unit cost matters. What should be adopted?

Domain: Optimize generative AI systems and model performance

- A. Start on pay-as-you-go while the volume is still unknown
- B. Cache identical requests and reuse the completion
- C. Move steady traffic to provisioned throughput
- D. Increase the model size until the answers improve

### 67. A department needs attributable spend and current answers. Which two practices apply? Select two.

Domain: Optimize generative AI systems and model performance

- A. Use the largest model for every request
- B. Cache identical requests and reuse the completion
- C. Measure tokens per request and set a budget per endpoint
- D. Set a time-to-live on the cache
- E. Accept the behaviour because the aggregate score still looks healthy

### 68. A team must cut both retrieved context and standing instruction. Which two changes fit? Select two.

Domain: Optimize generative AI systems and model performance

- A. Retrieve fewer but better-ranked passages
- B. Cache identical requests and reuse the completion
- C. Increase the model size until the answers improve
- D. Compress the system prompt and remove redundant instructions
- E. Raise retrieval depth to the maximum for safety

### 69. A platform team must size a clinical assistant before peak season. Which sequence is correct?

Domain: Optimize generative AI systems and model performance

- A. Forecast the peak load → reserve provisioned throughput → measure the current rate → load test
- B. Measure the current request rate and token volume → forecast the peak and steady load → compare pay-as-you-go cost with provisioned throughput at that volume → load test the chosen configuration
- C. Reserve provisioned throughput → measure the request rate → forecast the load → load test the configuration
- D. Load test the configuration → reserve provisioned throughput → forecast the load → measure the request rate

### 70. A deployment must resolve a stable pointer that promotion can move without editing the deployment. What should be used?

Domain: Design and implement an MLOps infrastructure

- A. Register the model and always deploy whichever version is latest
- B. Promote versions through aliases such as candidate and production
- C. Register each candidate with a version and deploy one explicit version
- D. Overwrite the existing model version instead of registering a new one

### 71. Assets must be shared between two workspaces without copying them. What enables that?

Domain: Design and implement an MLOps infrastructure

- A. Rebuild the environment by hand from the notes in the ticket
- B. Package the preparation step as a reusable component
- C. Publish the component to the workspace registry
- D. Create the workspace in the portal and record the steps in a wiki

### 72. A job must reference data and dependencies without embedded secrets or floating tags. Which two practices apply? Select two.

Domain: Design and implement an MLOps infrastructure

- A. Register a datastore that points at the storage account
- B. Print the metrics to the job log and read them from the console
- C. Build a versioned curated environment for the job
- D. Reference the storage path with the account key inline in the job YAML
- E. Reference the floating latest tag for the environment image

### 73. A production deploy must be gated and must not use a stored secret. Which two controls apply? Select two.

Domain: Design and implement an MLOps infrastructure

- A. Fan the tests out across a matrix of dependency versions
- B. Authenticate the workflow with workload identity federation and no stored secret
- C. Use GitHub environment protection rules to gate the production deploy job
- D. Grant the pipeline service principal Owner on the subscription
- E. Store a service principal client secret as a GitHub repository secret

### 74. A feature-preparation step processes six gigabytes of CSV and needs no accelerator. What should it target?

Domain: Implement machine learning model lifecycle and operations

- A. Run the job from a compute instance notebook
- B. Attach a GPU cluster with a minimum of zero nodes
- C. Create the workspace in the portal and record the steps in a wiki
- D. Attach a CPU compute cluster for the data preparation step

### 75. A service runs at a genuinely constant 400 requests a second and needs predictable capacity. What fits?

Domain: Implement machine learning model lifecycle and operations

- A. Send the overnight file through the online endpoint request by request
- B. Pin a fixed instance count for a spiky workload
- C. Configure liveness and readiness probes on the deployment
- D. Set autoscale rules on the deployment with a deliberate minimum instance count

### 76. Four hundred runs share one list and three variants cannot be compared. What should be used?

Domain: Implement machine learning model lifecycle and operations

- A. Print the metrics to the job log and read them from the console
- B. Group the trials under a named experiment
- C. Enable MLflow tracking so runs log to the workspace
- D. Disable request logging to reduce storage cost

### 77. Every candidate requires a container build before it can be tested. What should change?

Domain: Implement machine learning model lifecycle and operations

- A. Mount the model artifact rather than baking it into the image
- B. Replace the production deployment in a single step
- C. Overwrite the existing model version instead of registering a new one
- D. Bake the model weights into the container image

### 78. A single script hides which stage failed and reruns everything to recover. What should replace it?

Domain: Implement machine learning model lifecycle and operations

- A. Run the whole workflow as a single script job
- B. Assign the work to a person instead of investigating the failure
- C. Run the job from a compute instance notebook
- D. Define the steps as a pipeline job with explicit inputs and outputs

### 79. A synchronous service must serve single requests and avoid errors during startup. Which two practices apply? Select two.

Domain: Implement machine learning model lifecycle and operations

- A. Pin a fixed instance count for a spiky workload
- B. Configure liveness and readiness probes on the deployment
- C. Deploy to a managed online endpoint with an explicit model version
- D. Deploy without probes and rely on the platform health check
- E. Deploy a batch endpoint for the overnight scoring job

### 80. A bulk rescoring job must avoid always-on capacity and stay reversible. Which two practices apply? Select two.

Domain: Implement machine learning model lifecycle and operations

- A. Keep the previous deployment in place so traffic can be moved back
- B. Deploy a batch endpoint for the overnight scoring job
- C. Send the overnight file through the online endpoint request by request
- D. Replace the production deployment in a single step
- E. Bake the model weights into the container image

### 81. A quality defect reaches production and the team must respond. Which sequence is correct?

Domain: Implement machine learning model lifecycle and operations

- A. Add a regression case → contain the incident → confirm the impact → fix the cause
- B. Contain the incident → add a regression case → fix the cause → confirm the impact
- C. Confirm the impact and scope from telemetry → contain the incident by shifting traffic or disabling the feature → fix the identified cause → add a regression case and update the gate
- D. Fix the identified cause → confirm the impact → contain the incident → add a regression case

### 82. A model has degraded and the team must find out why. Which sequence is correct?

Domain: Implement machine learning model lifecycle and operations

- A. Detect the drop from monitoring or alerts → compare live feature distributions with the training baseline → identify the changed upstream source → retrain on refreshed data and promote through the gate
- B. Identify the upstream source → retrain → detect the drop → compare distributions
- C. Retrain on refreshed data → detect the drop → compare distributions → promote through the gate
- D. Compare distributions → identify the upstream source → detect the drop → retrain on refreshed data

### 83. A pipeline must run against published assets and a pinned environment. Which sequence is correct?

Domain: Implement machine learning model lifecycle and operations

- A. Reference both from the pipeline YAML → build the environment → publish the component → run the pipeline
- B. Publish the component to the registry → build a versioned environment that pins its dependencies → reference both from the pipeline YAML → run the pipeline in the test environment
- C. Run the pipeline in the test environment → reference both from the pipeline YAML → publish the component → build the environment
- D. Build the environment → run the pipeline → publish the component → reference it in the YAML

### 84. A pilot assistant may be withdrawn after two months with unknown volume. What deployment option fits?

Domain: Design and implement a GenAIOps infrastructure

- A. Use the largest model for every request
- B. Pin a fixed instance count for a spiky workload
- C. Reserve provisioned throughput for the steady high-volume workload
- D. Start on pay-as-you-go while the volume is still unknown

### 85. A flow must be scored across three hundred evaluation cases before release. What should be run?

Domain: Design and implement a GenAIOps infrastructure

- A. Run the job from a compute instance notebook
- B. Run the flow as a batch job over the evaluation dataset
- C. Deploy the flow to a managed online endpoint
- D. Stream the job with az ml job stream to inspect logs

### 86. A clinical assistant must ground on current protocols. Which sequence is correct?

Domain: Design and implement a GenAIOps infrastructure

- A. Bind the index to the flow → create the search index → curate the documents → chunk and embed them
- B. Curate the source documents → chunk and embed them → create the search index → bind the index to the flow → evaluate retrieval and groundedness
- C. Chunk and embed the documents → evaluate retrieval → create the search index → curate the documents
- D. Create the search index → curate the source documents → evaluate retrieval → chunk and embed them

### 87. A released prompt change must be measured and reviewable. Which sequence is correct?

Domain: Design and implement a GenAIOps infrastructure

- A. Edit the prompt file in a branch → run the offline evaluation gate → review the diff and metric change in a pull request → deploy the approved version and watch the online metrics
- B. Deploy the approved version → edit the prompt in a branch → run the evaluation gate → review the diff
- C. Run the offline evaluation gate → deploy the version → review the diff → edit the prompt
- D. Review the diff and metric change → edit the prompt in a branch → deploy the version → run the evaluation gate

### 88. Thirty-two combinations were run at full overhead and the tuning bill exceeded the project budget. What should have been used?

Domain: Implement machine learning model lifecycle and operations

- A. Increase the model size until the answers improve
- B. Use automated ML to establish the tabular baseline
- C. Run a sweep job over a searched hyperparameter space
- D. Run a full grid sweep over every combination

---

## Case study — Beacon Financial

Beacon Financial operates an agent that helps analysts assemble quarterly research notes by calling internal tools for prices, filings, and estimates. The agent has access to fourteen tools, including a trade-execution stub that should never be called from a research workflow, and an analyst discovered it could reach the stub by phrasing the request unusually. The firm needs a record of which tools the agent called for each note, and compliance wants a review before any new tool is exposed. Latency has also doubled since the tool list grew.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 89. Endpoint keys must rotate quarterly without redeploying flows. Where should they live?

Domain: Design and implement an MLOps infrastructure

- A. Store connection strings in Key Vault and reference them by name
- B. Print the metrics to the job log and read them from the console
- C. Reference the storage path with the account key inline in the job YAML
- D. Set the connection string as a plain environment variable in the job

### 90. Licensed market data may not be copied, but analysts need grounded answers from it. What should be used?

Domain: Design and implement a GenAIOps infrastructure

- A. Export the corpus to storage and index it as files
- B. Connect to the source through a federated connector and query it in place
- C. Paste the API key into a Python node inside the flow
- D. Build a knowledge-source connector that indexes the whole corpus into the project

### 91. Model-risk reviews ask how quality is tracked between formal validations. What should be added?

Domain: Implement generative AI quality assurance and observability

- A. Run continuous evaluation on sampled production traffic
- B. Accept the behaviour because the aggregate score still looks healthy
- C. Build the evaluation dataset from real queries with graded answers
- D. Run the evaluation in continuous integration before the flow is promoted

---

## Case study — Cobalt Retail

Cobalt Retail runs a product-description generator that produces 40,000 descriptions a month across three languages. The team wants to reduce cost per description, improve factual accuracy against supplier specifications, and cut the time from prompt change to release. Two experiments are planned: a smaller model for simple categories and provisioned throughput for the steady volume. The merchandising team refuses any change that lowers factual accuracy, and there is no written definition of what accuracy means for a description.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 92. One generator serves simple categories and complex specifications from a single endpoint. What should be added?

Domain: Optimize generative AI systems and model performance

- A. Cache identical requests and reuse the completion
- B. Use the largest model for every request
- C. Route simple requests to a smaller model
- D. Add a router that classifies the request and selects a model

### 93. Steady volume of forty thousand descriptions a month justifies a commitment. What should be adopted?

Domain: Optimize generative AI systems and model performance

- A. Cache identical requests and reuse the completion
- B. Move steady traffic to provisioned throughput
- C. Start on pay-as-you-go while the volume is still unknown
- D. Increase the model size until the answers improve

### 94. The team wants shorter prompts without losing factual accuracy. Which two practices apply? Select two.

Domain: Optimize generative AI systems and model performance

- A. Fine-tune the model on the document set instead of retrieving
- B. Compress the system prompt and remove redundant instructions
- C. Fine-tune on approved examples to shorten the standing prompt
- D. Re-run the evaluation after the cost optimization
- E. Increase the model size until the answers improve

---

## Case study — Redwood Manufacturing

Redwood Manufacturing operates a quality-inspection model at the end of three production lines and a batch reporting job that runs every shift. The model was trained on images from one plant and is being extended to two more with different lighting, and the platform team expects data drift. The inspection endpoint must answer within 120 milliseconds, and the reporting job must finish before the shift handover. The team currently deploys with a fixed instance count and has no rollback procedure beyond redeploying the previous image by hand.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 95. A third plant must get an identical inspection environment under change control. What should be used?

Domain: Design and implement an MLOps infrastructure

- A. Define the workspace in a Bicep module deployed per environment
- B. Export an ARM template from the portal after building it by hand
- C. Create the workspace in the portal and record the steps in a wiki
- D. Rebuild the environment by hand from the notes in the ticket

### 96. A model trained at one plant is extended to two others with different lighting. What should be enabled?

Domain: Implement machine learning model lifecycle and operations

- A. Enable data drift monitoring against the training baseline
- B. Retrain the model on the newer data
- C. Accept the behaviour because the aggregate score still looks healthy
- D. Monitor only the accuracy reported at deployment time

### 97. A new model reaches three lines with no rollback procedure. Which two controls apply? Select two.

Domain: Implement machine learning model lifecycle and operations

- A. Keep the previous deployment in place so traffic can be moved back
- B. Split endpoint traffic 10/90 so the new deployment receives a canary share
- C. Replace the production deployment in a single step
- D. Overwrite the existing model version instead of registering a new one
- E. Bake the model weights into the container image

---

## Case study — Solstice Energy

Solstice Energy runs a field-maintenance assistant grounded in equipment manuals and work orders across four regions. Manual revisions change quarterly, and engineers have been given answers quoting a superseded torque specification, which the safety team treats as a serious defect. The company must retain maintenance records for seven years and must be able to show which manual revision an answer relied on. A vendor has proposed fine-tuning the model on the manuals to improve accuracy, and the platform team is unsure whether that addresses the problem.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 98. A vendor proposes fine-tuning on the manuals instead of maintaining an index. What is the objection?

Domain: Optimize generative AI systems and model performance

- A. Set document-level access in the index so retrieval respects entitlements
- B. Rebuild the index on a schedule after the source content changes
- C. Fine-tune the model on the document set instead of retrieving
- D. Index the documents in Azure AI Search and query the index from the flow

### 99. Engineers receive answers citing a superseded torque specification. What should be configured?

Domain: Design and implement a GenAIOps infrastructure

- A. Retrain the model on the newer data
- B. Chunk documents by section with a small overlap
- C. Index every document the organization holds
- D. Rebuild the index on a schedule after the source content changes

### 100. The safety team treats an unsupported specification as a serious defect. Which metric targets it?

Domain: Implement generative AI quality assurance and observability

- A. Score fluency for readability and language quality
- B. Score coherence for logical structure
- C. Score relevance of the answer to the question asked
- D. Score groundedness against the retrieved passages

---

## Answer key and explanations

### Question 1 — B

Answer: Build a versioned curated environment for the job. A versioned curated environment pins the interpreter and packages for that date. A versioned environment pins the interpreter and packages, so the same job resolves the same dependencies months later. Local study-map skill 1.2 (Data Assets, Environments, and Component Reuse), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. A floating tag resolves to a different image over time and silently breaks reproducibility. Why the correct answer wins: A versioned curated environment pins the interpreter and packages for that date.
- **B:** Correct. A versioned environment pins the interpreter and packages, so the same job resolves the same dependencies months later. In this case: A versioned curated environment pins the interpreter and packages for that date.
- **C:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A versioned curated environment pins the interpreter and packages for that date.
- **D:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: A versioned curated environment pins the interpreter and packages for that date.

### Question 2 — A

Answer: Register the data as a versioned data asset. A versioned data asset records the exact cohort used by the run. A versioned data asset records exactly which data a run used, which is what makes the model reproducible later. Local study-map skill 1.2 (Data Assets, Environments, and Component Reuse), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Correct. A versioned data asset records exactly which data a run used, which is what makes the model reproducible later. In this case: A versioned data asset records the exact cohort used by the run.
- **B:** Incorrect for this question. An inline key puts a credential in source control and ties the job to one physical path. Why the correct answer wins: A versioned data asset records the exact cohort used by the run.
- **C:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: A versioned data asset records the exact cohort used by the run.
- **D:** Incorrect for this question. A datastore holds the connection and credential, so jobs reference data by name instead of an account key and physical path. Why the correct answer wins: A versioned data asset records the exact cohort used by the run.

### Question 3 — C

Answer: Define the workspace in a Bicep module deployed per environment. A reviewed Bicep module recreates the environment under change control. Bicep gives a declarative, reviewable definition, so an environment can be recreated identically and configuration drift becomes visible. Local study-map skill 1.3 (Infrastructure as Code with Bicep), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. A hand rebuild cannot be reproduced exactly and drifts from the definition the team believed it had. Why the correct answer wins: A reviewed Bicep module recreates the environment under change control.
- **B:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A reviewed Bicep module recreates the environment under change control.
- **C:** Correct. Bicep gives a declarative, reviewable definition, so an environment can be recreated identically and configuration drift becomes visible. In this case: A reviewed Bicep module recreates the environment under change control.
- **D:** Incorrect for this question. Exporting captures whatever exists, including accidental settings, and starts the estate from an unreviewed hand-built state. Why the correct answer wins: A reviewed Bicep module recreates the environment under change control.

### Question 4 — B

Answer: Place a private endpoint on the workspace and its storage. A private endpoint keeps traffic on the virtual network. A private endpoint removes public network access, so traffic stays on the virtual network. Local study-map skill 1.3 (Infrastructure as Code with Bicep), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. An inline key puts a credential in source control and ties the job to one physical path. Why the correct answer wins: A private endpoint keeps traffic on the virtual network.
- **B:** Correct. A private endpoint removes public network access, so traffic stays on the virtual network. In this case: A private endpoint keeps traffic on the virtual network.
- **C:** Incorrect for this question. A plain environment variable appears in job definitions and logs, which exposes the secret. Why the correct answer wins: A private endpoint keeps traffic on the virtual network.
- **D:** Incorrect for this question. Public access broadens the attack surface and usually fails a regulated review. Why the correct answer wins: A private endpoint keeps traffic on the virtual network.

### Question 5 — D

Answer: Pass environment values through a Bicep parameter file per stage. A parameter file per region holds the differences. A parameter file keeps one module per environment, so only the values differ and the shape stays identical. Local study-map skill 1.3 (Infrastructure as Code with Bicep), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. A hand rebuild cannot be reproduced exactly and drifts from the definition the team believed it had. Why the correct answer wins: A parameter file per region holds the differences.
- **B:** Incorrect for this question. Exporting captures whatever exists, including accidental settings, and starts the estate from an unreviewed hand-built state. Why the correct answer wins: A parameter file per region holds the differences.
- **C:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A parameter file per region holds the differences.
- **D:** Correct. A parameter file keeps one module per environment, so only the values differ and the shape stays identical. In this case: A parameter file per region holds the differences.

### Question 6 — C

Answer: Submit the job with az ml job create --file job.yaml. A declarative YAML job through the CLI runs unchanged from a scheduler or pipeline. A declarative YAML job submitted through the CLI is repeatable and runs unchanged in continuous integration. Local study-map skill 1.4 (Azure CLI and Declarative Job Automation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A declarative YAML job through the CLI runs unchanged from a scheduler or pipeline.
- **B:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A declarative YAML job through the CLI runs unchanged from a scheduler or pipeline.
- **C:** Correct. A declarative YAML job submitted through the CLI is repeatable and runs unchanged in continuous integration. In this case: A declarative YAML job through the CLI runs unchanged from a scheduler or pipeline.
- **D:** Incorrect for this question. Streaming attaches to a running job log, which is a debugging step rather than a way to create or promote an asset. Why the correct answer wins: A declarative YAML job through the CLI runs unchanged from a scheduler or pipeline.

### Question 7 — D

Answer: Authenticate the workflow with workload identity federation and no stored secret. Workload identity federation exchanges the workflow token for a credential. Federated identity exchanges the workflow token for an Azure credential, so no long-lived secret exists to leak or rotate. Local study-map skill 1.5 (GitHub Actions CI/CD and Workload Identity Federation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Owner on the subscription lets a pipeline change any resource, so one bad commit can affect everything. Why the correct answer wins: Workload identity federation exchanges the workflow token for a credential.
- **B:** Incorrect for this question. A stored client secret is long-lived and must be rotated; federation removes the secret entirely. Why the correct answer wins: Workload identity federation exchanges the workflow token for a credential.
- **C:** Incorrect for this question. A plain environment variable appears in job definitions and logs, which exposes the secret. Why the correct answer wins: Workload identity federation exchanges the workflow token for a credential.
- **D:** Correct. Federated identity exchanges the workflow token for an Azure credential, so no long-lived secret exists to leak or rotate. In this case: Workload identity federation exchanges the workflow token for a credential.

### Question 8 — C

Answer: Create a service principal per environment with a least-privilege role assignment. A service principal per environment with a least-privilege role contains the blast radius. Scoping identity per environment limits what a compromised development pipeline can reach. Local study-map skill 1.5 (GitHub Actions CI/CD and Workload Identity Federation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. A plain environment variable appears in job definitions and logs, which exposes the secret. Why the correct answer wins: A service principal per environment with a least-privilege role contains the blast radius.
- **B:** Incorrect for this question. Public access broadens the attack surface and usually fails a regulated review. Why the correct answer wins: A service principal per environment with a least-privilege role contains the blast radius.
- **C:** Correct. Scoping identity per environment limits what a compromised development pipeline can reach. In this case: A service principal per environment with a least-privilege role contains the blast radius.
- **D:** Incorrect for this question. Owner on the subscription lets a pipeline change any resource, so one bad commit can affect everything. Why the correct answer wins: A service principal per environment with a least-privilege role contains the blast radius.

### Question 9 — D

Answer: Register each candidate with a version and deploy one explicit version. An explicit model version identifies the served artifact. An explicit version pins what is served, so a new registration cannot silently change production behaviour. Local study-map skill 1.6 (Model Registry and Environment Promotion), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Deploying whatever is latest lets an untested registration reach production with no promotion gate. Why the correct answer wins: An explicit model version identifies the served artifact.
- **B:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: An explicit model version identifies the served artifact.
- **C:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: An explicit model version identifies the served artifact.
- **D:** Correct. An explicit version pins what is served, so a new registration cannot silently change production behaviour. In this case: An explicit model version identifies the served artifact.

### Question 10 — B

Answer: Assign a managed identity to compute and grant it the storage role. A managed identity removes the credential entirely. A managed identity removes credentials from code entirely and is granted only the role the step needs. Local study-map skill 1.7 (Network Isolation, Secrets, and Pipeline Identity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. A plain environment variable appears in job definitions and logs, which exposes the secret. Why the correct answer wins: A managed identity removes the credential entirely.
- **B:** Correct. A managed identity removes credentials from code entirely and is granted only the role the step needs. In this case: A managed identity removes the credential entirely.
- **C:** Incorrect for this question. An inline key puts a credential in source control and ties the job to one physical path. Why the correct answer wins: A managed identity removes the credential entirely.
- **D:** Incorrect for this question. Owner on the subscription lets a pipeline change any resource, so one bad commit can affect everything. Why the correct answer wins: A managed identity removes the credential entirely.

### Question 11 — B, E

Answers: Create a separate Azure Machine Learning workspace per environment; Place a private endpoint on the workspace and its storage. A dedicated workspace isolates assets, and a private endpoint removes public access. A workspace is the top-level boundary for compute, datastores, jobs, and registered assets, so separating environments keeps development activity away from production assets. A private endpoint removes public network access, so traffic stays on the virtual network. Local study-map skill 1.1 (Workspace, Compute, and Datastore Provisioning), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A dedicated workspace isolates assets, and a private endpoint removes public access.
- **B:** Correct. A private endpoint removes public network access, so traffic stays on the virtual network. In this case: A dedicated workspace isolates assets, and a private endpoint removes public access.
- **C:** Incorrect for this question. Public access broadens the attack surface and usually fails a regulated review. Why the correct answer wins: A dedicated workspace isolates assets, and a private endpoint removes public access.
- **D:** Incorrect for this question. A shared workspace mixes assets and identities across environments, so a test job can register over the model production is serving. Why the correct answer wins: A dedicated workspace isolates assets, and a private endpoint removes public access.
- **E:** Correct. A workspace is the top-level boundary for compute, datastores, jobs, and registered assets, so separating environments keeps development activity away from production assets. In this case: A dedicated workspace isolates assets, and a private endpoint removes public access.

### Question 12 — C, E

Answers: Define the workspace in a Bicep module deployed per environment; Deploy the module as a deployment stack so removed resources are cleaned up. Bicep defines the shape, and a deployment stack removes out-of-band changes. Bicep gives a declarative, reviewable definition, so an environment can be recreated identically and configuration drift becomes visible. A deployment stack tracks the resources it owns and can deny or delete changes made outside the template. Local study-map skill 1.3 (Infrastructure as Code with Bicep), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Exporting captures whatever exists, including accidental settings, and starts the estate from an unreviewed hand-built state. Why the correct answer wins: Bicep defines the shape, and a deployment stack removes out-of-band changes.
- **B:** Incorrect for this question. A hand rebuild cannot be reproduced exactly and drifts from the definition the team believed it had. Why the correct answer wins: Bicep defines the shape, and a deployment stack removes out-of-band changes.
- **C:** Correct. A deployment stack tracks the resources it owns and can deny or delete changes made outside the template. In this case: Bicep defines the shape, and a deployment stack removes out-of-band changes.
- **D:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: Bicep defines the shape, and a deployment stack removes out-of-band changes.
- **E:** Correct. Bicep gives a declarative, reviewable definition, so an environment can be recreated identically and configuration drift becomes visible. In this case: Bicep defines the shape, and a deployment stack removes out-of-band changes.

### Question 13 — A

Answer: Define the steps as a pipeline job with explicit inputs and outputs. A pipeline records step inputs and outputs, which is the lineage evidence. A pipeline job makes the dependency between steps explicit and records each output, which is what gives lineage. Local study-map skill 2.1 (Training Pipeline Authoring and Orchestration), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. A pipeline job makes the dependency between steps explicit and records each output, which is what gives lineage. In this case: A pipeline records step inputs and outputs, which is the lineage evidence.
- **B:** Incorrect for this question. A single script hides intermediate artifacts, so a failed stage cannot be rerun without repeating everything. Why the correct answer wins: A pipeline records step inputs and outputs, which is the lineage evidence.
- **C:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A pipeline records step inputs and outputs, which is the lineage evidence.
- **D:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: A pipeline records step inputs and outputs, which is the lineage evidence.

### Question 14 — C

Answer: Enable MLflow tracking so runs log to the workspace. MLflow records parameters and artifacts per run. MLflow records parameters, metrics, and artifacts against a run, which is what makes experiments comparable. Local study-map skill 2.3 (Experiment Tracking with MLflow), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: MLflow records parameters and artifacts per run.
- **B:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: MLflow records parameters and artifacts per run.
- **C:** Correct. MLflow records parameters, metrics, and artifacts against a run, which is what makes experiments comparable. In this case: MLflow records parameters and artifacts per run.
- **D:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: MLflow records parameters and artifacts per run.

### Question 15 — D

Answer: Attach a description, metrics, and intended use to the model version. A model card with metrics and intended use supports that judgement. Documented metrics and intended use let a reviewer decide whether the version is fit to promote. Local study-map skill 2.4 (Model Registration, Versioning, and Metadata), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Deploying whatever is latest lets an untested registration reach production with no promotion gate. Why the correct answer wins: A model card with metrics and intended use supports that judgement.
- **B:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: A model card with metrics and intended use supports that judgement.
- **C:** Incorrect for this question. Tags carry provenance, which is what an audit needs in order to rebuild the artifact. Why the correct answer wins: A model card with metrics and intended use supports that judgement.
- **D:** Correct. Documented metrics and intended use let a reviewer decide whether the version is fit to promote. In this case: A model card with metrics and intended use supports that judgement.

### Question 16 — D

Answer: Tag the registered model with the data asset and commit it came from. Tags carrying the data asset and commit are what make the rebuild possible. Tags carry provenance, which is what an audit needs in order to rebuild the artifact. Local study-map skill 2.4 (Model Registration, Versioning, and Metadata), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Documented metrics and intended use let a reviewer decide whether the version is fit to promote. Why the correct answer wins: Tags carrying the data asset and commit are what make the rebuild possible.
- **B:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: Tags carrying the data asset and commit are what make the rebuild possible.
- **C:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: Tags carrying the data asset and commit are what make the rebuild possible.
- **D:** Correct. Tags carry provenance, which is what an audit needs in order to rebuild the artifact. In this case: Tags carrying the data asset and commit are what make the rebuild possible.

### Question 17 — B

Answer: Configure liveness and readiness probes on the deployment. A readiness probe withholds traffic until the model can serve. Liveness restarts an unhealthy container and readiness keeps traffic away until the container can actually serve. Local study-map skill 2.5 (Managed Online Endpoint Deployment), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. A fixed count either wastes money at low load or throttles at peak. Why the correct answer wins: A readiness probe withholds traffic until the model can serve.
- **B:** Correct. Liveness restarts an unhealthy container and readiness keeps traffic away until the container can actually serve. In this case: A readiness probe withholds traffic until the model can serve.
- **C:** Incorrect for this question. Without probes, a container that starts but cannot load the model still receives traffic. Why the correct answer wins: A readiness probe withholds traffic until the model can serve.
- **D:** Incorrect for this question. Deployment-time accuracy is a snapshot; it says nothing about the data that arrives afterwards. Why the correct answer wins: A readiness probe withholds traffic until the model can serve.

### Question 18 — A

Answer: Split endpoint traffic 10/90 so the new deployment receives a canary share. A traffic split bounds exposure to a canary share. A traffic split sends a small share to the new deployment, so a regression affects fewer requests and is measurable. Local study-map skill 2.6 (Batch Endpoints and Controlled Traffic Rollout), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. A traffic split sends a small share to the new deployment, so a regression affects fewer requests and is measurable. In this case: A traffic split bounds exposure to a canary share.
- **B:** Incorrect for this question. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. Why the correct answer wins: A traffic split bounds exposure to a canary share.
- **C:** Incorrect for this question. A one-step replacement exposes every request to an unproven version with no measured canary. Why the correct answer wins: A traffic split bounds exposure to a canary share.
- **D:** Incorrect for this question. Skipping the staged check saves a day and moves the discovery of a defect to a customer. Why the correct answer wins: A traffic split bounds exposure to a canary share.

### Question 19 — B

Answer: Keep the previous deployment in place so traffic can be moved back. A retained deployment makes withdrawal a traffic change. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. Local study-map skill 2.6 (Batch Endpoints and Controlled Traffic Rollout), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: A retained deployment makes withdrawal a traffic change.
- **B:** Correct. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. In this case: A retained deployment makes withdrawal a traffic change.
- **C:** Incorrect for this question. A one-step replacement exposes every request to an unproven version with no measured canary. Why the correct answer wins: A retained deployment makes withdrawal a traffic change.
- **D:** Incorrect for this question. Baking the model ties every version to an image build, which slows promotion and bloats the registry. Why the correct answer wins: A retained deployment makes withdrawal a traffic change.

### Question 20 — A

Answer: Enable data drift monitoring against the training baseline. Drift monitoring compares live inputs with the training baseline. Drift monitoring compares live input distributions with the training baseline, which is what catches silent degradation. Local study-map skill 2.8 (Data and Model Drift Monitoring), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. Drift monitoring compares live input distributions with the training baseline, which is what catches silent degradation. In this case: Drift monitoring compares live inputs with the training baseline.
- **B:** Incorrect for this question. Deployment-time accuracy is a snapshot; it says nothing about the data that arrives afterwards. Why the correct answer wins: Drift monitoring compares live inputs with the training baseline.
- **C:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: Drift monitoring compares live inputs with the training baseline.
- **D:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: Drift monitoring compares live inputs with the training baseline.

### Question 21 — A

Answer: Create an alert rule on the drift and latency metrics. An alert converts the metric into action. An alert turns a metric into an action; without it a drift report is noticed only if someone reads it. Local study-map skill 2.8 (Data and Model Drift Monitoring), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. An alert turns a metric into an action; without it a drift report is noticed only if someone reads it. In this case: An alert converts the metric into action.
- **B:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: An alert converts the metric into action.
- **C:** Incorrect for this question. Deployment-time accuracy is a snapshot; it says nothing about the data that arrives afterwards. Why the correct answer wins: An alert converts the metric into action.
- **D:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: An alert converts the metric into action.

### Question 22 — A

Answer: Monitor only the accuracy reported at deployment time. A deployment-time snapshot says nothing about subsequent data. Deployment-time accuracy is a snapshot; it says nothing about the data that arrives afterwards. Local study-map skill 2.8 (Data and Model Drift Monitoring), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. Deployment-time accuracy is a snapshot; it says nothing about the data that arrives afterwards. In this case: A deployment-time snapshot says nothing about subsequent data.
- **B:** Incorrect for this question. Drift monitoring compares live input distributions with the training baseline, which is what catches silent degradation. Why the correct answer wins: A deployment-time snapshot says nothing about subsequent data.
- **C:** Incorrect for this question. An alert turns a metric into an action; without it a drift report is noticed only if someone reads it. Why the correct answer wins: A deployment-time snapshot says nothing about subsequent data.
- **D:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: A deployment-time snapshot says nothing about subsequent data.

### Question 23 — A

Answer: Run a sweep job over a searched hyperparameter space. A sampled sweep covers a wide space within a trial budget. A sweep samples the search space and records every trial, which finds an optimum systematically rather than by guesswork. Local study-map skill 2.2 (Job Configuration, Compute Targets, and Sweeps), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. A sweep samples the search space and records every trial, which finds an optimum systematically rather than by guesswork. In this case: A sampled sweep covers a wide space within a trial budget.
- **B:** Incorrect for this question. Automated ML tests preprocessing and algorithm combinations quickly, which is a reasonable baseline for tabular data. Why the correct answer wins: A sampled sweep covers a wide space within a trial budget.
- **C:** Incorrect for this question. A full grid multiplies cost by the number of combinations and is rarely needed once the promising region is known. Why the correct answer wins: A sampled sweep covers a wide space within a trial budget.
- **D:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: A sampled sweep covers a wide space within a trial budget.

### Question 24 — C

Answer: Attach a GPU cluster with a minimum of zero nodes. A GPU cluster with a zero minimum stops billing between runs. A GPU cluster with a zero minimum scales to nothing when idle, which suits intermittent training without paying for accelerators between runs. Local study-map skill 2.2 (Job Configuration, Compute Targets, and Sweeps), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Always-on GPU nodes bill continuously, including overnight and between experiments. Why the correct answer wins: A GPU cluster with a zero minimum stops billing between runs.
- **B:** Incorrect for this question. A CPU cluster is cheaper per core and sufficient for tabular preparation, which gains nothing from an accelerator. Why the correct answer wins: A GPU cluster with a zero minimum stops billing between runs.
- **C:** Correct. A GPU cluster with a zero minimum scales to nothing when idle, which suits intermittent training without paying for accelerators between runs. In this case: A GPU cluster with a zero minimum stops billing between runs.
- **D:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A GPU cluster with a zero minimum stops billing between runs.

### Question 25 — D

Answer: Use automated ML to establish the tabular baseline. Automated ML produces a defensible baseline quickly. Automated ML tests preprocessing and algorithm combinations quickly, which is a reasonable baseline for tabular data. Local study-map skill 2.2 (Job Configuration, Compute Targets, and Sweeps), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: Automated ML produces a defensible baseline quickly.
- **B:** Incorrect for this question. A sweep samples the search space and records every trial, which finds an optimum systematically rather than by guesswork. Why the correct answer wins: Automated ML produces a defensible baseline quickly.
- **C:** Incorrect for this question. A single script hides intermediate artifacts, so a failed stage cannot be rerun without repeating everything. Why the correct answer wins: Automated ML produces a defensible baseline quickly.
- **D:** Correct. Automated ML tests preprocessing and algorithm combinations quickly, which is a reasonable baseline for tabular data. In this case: Automated ML produces a defensible baseline quickly.

### Question 26 — A, D

Answers: Define the steps as a pipeline job with explicit inputs and outputs; Register each candidate with a version and deploy one explicit version. The pipeline records lineage, and the explicit version pins the artifact. A pipeline job makes the dependency between steps explicit and records each output, which is what gives lineage. An explicit version pins what is served, so a new registration cannot silently change production behaviour. Local study-map skill 2.1 (Training Pipeline Authoring and Orchestration), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. A pipeline job makes the dependency between steps explicit and records each output, which is what gives lineage. In this case: The pipeline records lineage, and the explicit version pins the artifact.
- **B:** Incorrect for this question. Deploying whatever is latest lets an untested registration reach production with no promotion gate. Why the correct answer wins: The pipeline records lineage, and the explicit version pins the artifact.
- **C:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: The pipeline records lineage, and the explicit version pins the artifact.
- **D:** Correct. An explicit version pins what is served, so a new registration cannot silently change production behaviour. In this case: The pipeline records lineage, and the explicit version pins the artifact.
- **E:** Incorrect for this question. A single script hides intermediate artifacts, so a failed stage cannot be rerun without repeating everything. Why the correct answer wins: The pipeline records lineage, and the explicit version pins the artifact.

### Question 27 — A, B

Answers: Split endpoint traffic 10/90 so the new deployment receives a canary share; Keep the previous deployment in place so traffic can be moved back. The traffic split bounds exposure, and the retained deployment enables reversal. A traffic split sends a small share to the new deployment, so a regression affects fewer requests and is measurable. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. Local study-map skill 2.6 (Batch Endpoints and Controlled Traffic Rollout), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. A traffic split sends a small share to the new deployment, so a regression affects fewer requests and is measurable. In this case: The traffic split bounds exposure, and the retained deployment enables reversal.
- **B:** Correct. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. In this case: The traffic split bounds exposure, and the retained deployment enables reversal.
- **C:** Incorrect for this question. A one-step replacement exposes every request to an unproven version with no measured canary. Why the correct answer wins: The traffic split bounds exposure, and the retained deployment enables reversal.
- **D:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: The traffic split bounds exposure, and the retained deployment enables reversal.
- **E:** Incorrect for this question. Baking the model ties every version to an image build, which slows promotion and bloats the registry. Why the correct answer wins: The traffic split bounds exposure, and the retained deployment enables reversal.

### Question 28 — A

Answer: Train the candidate → evaluate against the gate → register the model version → deploy at a canary traffic share → shift all traffic after the metrics hold. Each step consumes the artifact produced before it, ending with a measured canary. Each step produces the artifact the next one needs: a trained model before an evaluation, a passing evaluation before registration, and a measured canary before full traffic. Local study-map skill 2.1 (Training Pipeline Authoring and Orchestration), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. Each step produces the artifact the next one needs: a trained model before an evaluation, a passing evaluation before registration, and a measured canary before full traffic. In this case: Each step consumes the artifact produced before it, ending with a measured canary.
- **B:** Incorrect for this question. Registration should record a model that already passed the gate, and full traffic without a canary exposes every request to an unproven version. Why the correct answer wins: Each step consumes the artifact produced before it, ending with a measured canary.
- **C:** Incorrect for this question. A deployment needs a registered artifact, and the evaluation that justifies promotion happens before anything serves traffic. Why the correct answer wins: Each step consumes the artifact produced before it, ending with a measured canary.
- **D:** Incorrect for this question. There is nothing to evaluate before training, and shifting all traffic before registration removes the artifact a rollback would target. Why the correct answer wins: Each step consumes the artifact produced before it, ending with a measured canary.

### Question 29 — A

Answer: Create a Foundry hub and a project per team. A hub shares capacity while a project isolates each team's assets. A hub shares connections and capacity, and a project gives a team an isolated working boundary for its own assets. Local study-map skill 3.1 (Foundry Hub, Project, and Shared Capacity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Correct. A hub shares connections and capacity, and a project gives a team an isolated working boundary for its own assets. In this case: A hub shares capacity while a project isolates each team's assets.
- **B:** Incorrect for this question. A single shared project mixes assets and permissions, so one team can change what another depends on. Why the correct answer wins: A hub shares capacity while a project isolates each team's assets.
- **C:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A hub shares capacity while a project isolates each team's assets.
- **D:** Incorrect for this question. A shared workspace mixes assets and identities across environments, so a test job can register over the model production is serving. Why the correct answer wins: A hub shares capacity while a project isolates each team's assets.

### Question 30 — C

Answer: Reference the deployment name from the flow rather than the model family name. A deployment name is the stable reference. A flow calls a deployment, so the deployment name stays the stable reference when the underlying model changes. Local study-map skill 3.1 (Foundry Hub, Project, and Shared Capacity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. A family name is not an addressable endpoint; the flow needs a deployment to call. Why the correct answer wins: A deployment name is the stable reference.
- **B:** Incorrect for this question. The catalog lists models with their capabilities; deploying one into the project makes it addressable by a deployment name. Why the correct answer wins: A deployment name is the stable reference.
- **C:** Correct. A flow calls a deployment, so the deployment name stays the stable reference when the underlying model changes. In this case: A deployment name is the stable reference.
- **D:** Incorrect for this question. A key inside a flow file is a secret in source control and cannot be rotated without editing the flow. Why the correct answer wins: A deployment name is the stable reference.

### Question 31 — D

Answer: Apply a content filter policy appropriate to the audience. A content filter policy applies those thresholds to each call. A content filter policy sets the harm thresholds applied to prompts and completions for that deployment. Local study-map skill 3.2 (Model Catalog Selection and Deployment Capacity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: A content filter policy applies those thresholds to each call.
- **B:** Incorrect for this question. Toxicity evaluation measures harmful output against the standard that audience or regulation requires. Why the correct answer wins: A content filter policy applies those thresholds to each call.
- **C:** Incorrect for this question. Adversarial cases test whether instructions in the input or the content can override the system prompt. Why the correct answer wins: A content filter policy applies those thresholds to each call.
- **D:** Correct. A content filter policy sets the harm thresholds applied to prompts and completions for that deployment. In this case: A content filter policy applies those thresholds to each call.

### Question 32 — C

Answer: Reserve provisioned throughput for the steady high-volume workload. Provisioned throughput gives predictable latency and cost at sustained volume. Provisioned throughput reserves capacity, which gives predictable latency and cost at sustained volume. Local study-map skill 3.2 (Model Catalog Selection and Deployment Capacity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: Provisioned throughput gives predictable latency and cost at sustained volume.
- **B:** Incorrect for this question. Pay-as-you-go costs nothing when idle and needs no forecast, which suits an unproven workload. Why the correct answer wins: Provisioned throughput gives predictable latency and cost at sustained volume.
- **C:** Correct. Provisioned throughput reserves capacity, which gives predictable latency and cost at sustained volume. In this case: Provisioned throughput gives predictable latency and cost at sustained volume.
- **D:** Incorrect for this question. A fixed count either wastes money at low load or throttles at peak. Why the correct answer wins: Provisioned throughput gives predictable latency and cost at sustained volume.

### Question 33 — C

Answer: Author the flow as a directed acyclic graph with typed inputs and outputs. A typed directed acyclic graph makes each node independently testable. A typed graph makes each step contract explicit, so the flow can be tested in isolation and composed with others. Local study-map skill 3.3 (Prompt Flow Authoring and DAG Composition), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. A batch run applies the flow to every row, which is how an evaluation dataset is scored. Why the correct answer wins: A typed directed acyclic graph makes each node independently testable.
- **B:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A typed directed acyclic graph makes each node independently testable.
- **C:** Correct. A typed graph makes each step contract explicit, so the flow can be tested in isolation and composed with others. In this case: A typed directed acyclic graph makes each node independently testable.
- **D:** Incorrect for this question. A single script hides intermediate artifacts, so a failed stage cannot be rerun without repeating everything. Why the correct answer wins: A typed directed acyclic graph makes each node independently testable.

### Question 34 — D

Answer: Create a variant to compare two prompt strategies side by side. Variants hold the alternatives together for a reproducible comparison. Variants keep the alternatives together, so the comparison is reproducible rather than remembered. Local study-map skill 3.3 (Prompt Flow Authoring and DAG Composition), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. A family name is not an addressable endpoint; the flow needs a deployment to call. Why the correct answer wins: Variants hold the alternatives together for a reproducible comparison.
- **B:** Incorrect for this question. A prompt change shipped without an evaluation gate is an unmeasured change to a production system. Why the correct answer wins: Variants hold the alternatives together for a reproducible comparison.
- **C:** Incorrect for this question. A typed graph makes each step contract explicit, so the flow can be tested in isolation and composed with others. Why the correct answer wins: Variants hold the alternatives together for a reproducible comparison.
- **D:** Correct. Variants keep the alternatives together, so the comparison is reproducible rather than remembered. In this case: Variants hold the alternatives together for a reproducible comparison.

### Question 35 — C

Answer: Store the model credential as a project connection. A project connection holds the endpoint and credential externally. A project connection holds the endpoint and credential outside the flow, so the flow file stays secret-free. Local study-map skill 3.4 (Flow Connections, Secrets, and Runtime Identity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. An inline key puts a credential in source control and ties the job to one physical path. Why the correct answer wins: A project connection holds the endpoint and credential externally.
- **B:** Incorrect for this question. A key inside a flow file is a secret in source control and cannot be rotated without editing the flow. Why the correct answer wins: A project connection holds the endpoint and credential externally.
- **C:** Correct. A project connection holds the endpoint and credential outside the flow, so the flow file stays secret-free. In this case: A project connection holds the endpoint and credential externally.
- **D:** Incorrect for this question. A plain environment variable appears in job definitions and logs, which exposes the secret. Why the correct answer wins: A project connection holds the endpoint and credential externally.

### Question 36 — A

Answer: Index the documents in Azure AI Search and query the index from the flow. An index supports retrieval against current content. An index supports retrieval at answer time, so the flow grounds on current content instead of on model memory. Local study-map skill 3.5 (Retrieval-Augmented Grounding with Azure AI Search), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Correct. An index supports retrieval at answer time, so the flow grounds on current content instead of on model memory. In this case: An index supports retrieval against current content.
- **B:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: An index supports retrieval against current content.
- **C:** Incorrect for this question. Fine-tuning bakes a snapshot of the content into the model, so it goes stale as documents change. Why the correct answer wins: An index supports retrieval against current content.
- **D:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: An index supports retrieval against current content.

### Question 37 — D

Answer: Set document-level access in the index so retrieval respects entitlements. Document-level access keeps retrieval within entitlement. Document-level access keeps retrieval within what the requesting user is allowed to see. Local study-map skill 3.5 (Retrieval-Augmented Grounding with Azure AI Search), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: Document-level access keeps retrieval within entitlement.
- **B:** Incorrect for this question. Public access broadens the attack surface and usually fails a regulated review. Why the correct answer wins: Document-level access keeps retrieval within entitlement.
- **C:** Incorrect for this question. A plain environment variable appears in job definitions and logs, which exposes the secret. Why the correct answer wins: Document-level access keeps retrieval within entitlement.
- **D:** Correct. Document-level access keeps retrieval within what the requesting user is allowed to see. In this case: Document-level access keeps retrieval within entitlement.

### Question 38 — C

Answer: Use hybrid search with semantic ranking. Hybrid search retains keyword matching for exact identifiers. Hybrid search combines keyword and vector matching, and semantic ranking reorders the top results, which improves recall on domain vocabulary and identifiers. Local study-map skill 3.5 (Retrieval-Augmented Grounding with Azure AI Search), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Vector-only retrieval misses exact identifiers and product codes, which is where keyword matching earns its place. Why the correct answer wins: Hybrid search retains keyword matching for exact identifiers.
- **B:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: Hybrid search retains keyword matching for exact identifiers.
- **C:** Correct. Hybrid search combines keyword and vector matching, and semantic ranking reorders the top results, which improves recall on domain vocabulary and identifiers. In this case: Hybrid search retains keyword matching for exact identifiers.
- **D:** Incorrect for this question. Fine-tuning bakes a snapshot of the content into the model, so it goes stale as documents change. Why the correct answer wins: Hybrid search retains keyword matching for exact identifiers.

### Question 39 — C

Answer: Chunk documents by section with a small overlap. Section-sized chunks with overlap make the citation specific. Section-sized chunks with overlap keep a passage coherent while staying small enough to be specific. Local study-map skill 3.6 (Chunking, Embeddings, and Index Refresh), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Retrieving more passages adds tokens and can bury the relevant passage among distractors. Why the correct answer wins: Section-sized chunks with overlap make the citation specific.
- **B:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: Section-sized chunks with overlap make the citation specific.
- **C:** Correct. Section-sized chunks with overlap keep a passage coherent while staying small enough to be specific. In this case: Section-sized chunks with overlap make the citation specific.
- **D:** Incorrect for this question. A whole-document chunk makes retrieval return an undifferentiated document, so the answer quotes the wrong part. Why the correct answer wins: Section-sized chunks with overlap make the citation specific.

### Question 40 — D

Answer: Rebuild the index on a schedule after the source content changes. A scheduled refresh aligns retrieval with the source. Scheduled refresh keeps retrieval aligned with the source; without it the assistant answers from retired content. Local study-map skill 3.6 (Chunking, Embeddings, and Index Refresh), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: A scheduled refresh aligns retrieval with the source.
- **B:** Incorrect for this question. Section-sized chunks with overlap keep a passage coherent while staying small enough to be specific. Why the correct answer wins: A scheduled refresh aligns retrieval with the source.
- **C:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: A scheduled refresh aligns retrieval with the source.
- **D:** Correct. Scheduled refresh keeps retrieval aligned with the source; without it the assistant answers from retired content. In this case: A scheduled refresh aligns retrieval with the source.

### Question 41 — B

Answer: Index each document as one large chunk. Whole-document chunks are too coarse to locate relevant text. A whole-document chunk makes retrieval return an undifferentiated document, so the answer quotes the wrong part. Local study-map skill 3.6 (Chunking, Embeddings, and Index Refresh), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Section-sized chunks with overlap keep a passage coherent while staying small enough to be specific. Why the correct answer wins: Whole-document chunks are too coarse to locate relevant text.
- **B:** Correct. A whole-document chunk makes retrieval return an undifferentiated document, so the answer quotes the wrong part. In this case: Whole-document chunks are too coarse to locate relevant text.
- **C:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: Whole-document chunks are too coarse to locate relevant text.
- **D:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: Whole-document chunks are too coarse to locate relevant text.

### Question 42 — C

Answer: Run the evaluation in continuous integration before the flow is promoted. An offline evaluation gate blocks a regression before promotion. An offline gate stops a regression before it reaches production traffic. Local study-map skill 3.7 (Prompt and Flow Versioning with Evaluation Gates), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: An offline evaluation gate blocks a regression before promotion.
- **B:** Incorrect for this question. Skipping the staged check saves a day and moves the discovery of a defect to a customer. Why the correct answer wins: An offline evaluation gate blocks a regression before promotion.
- **C:** Correct. An offline gate stops a regression before it reaches production traffic. In this case: An offline evaluation gate blocks a regression before promotion.
- **D:** Incorrect for this question. A prompt change shipped without an evaluation gate is an unmeasured change to a production system. Why the correct answer wins: An offline evaluation gate blocks a regression before promotion.

### Question 43 — C

Answer: Keep the prompt in its own file under version control. A versioned prompt file is the change record. A separate versioned prompt file makes every change reviewable and revertible. Local study-map skill 3.7 (Prompt and Flow Versioning with Evaluation Gates), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. A key inside a flow file is a secret in source control and cannot be rotated without editing the flow. Why the correct answer wins: A versioned prompt file is the change record.
- **B:** Incorrect for this question. Variants keep the alternatives together, so the comparison is reproducible rather than remembered. Why the correct answer wins: A versioned prompt file is the change record.
- **C:** Correct. A separate versioned prompt file makes every change reviewable and revertible. In this case: A versioned prompt file is the change record.
- **D:** Incorrect for this question. A prompt change shipped without an evaluation gate is an unmeasured change to a production system. Why the correct answer wins: A versioned prompt file is the change record.

### Question 44 — A

Answer: Register a scoped tool list for the agent. A scoped tool list bounds what the agent may call. A scoped tool list bounds what the agent can do, which is the main control over unintended actions. Local study-map skill 3.8 (Agent Orchestration and Tool Binding), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Correct. A scoped tool list bounds what the agent can do, which is the main control over unintended actions. In this case: A scoped tool list bounds what the agent may call.
- **B:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: A scoped tool list bounds what the agent may call.
- **C:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: A scoped tool list bounds what the agent may call.
- **D:** Incorrect for this question. An open tool list widens the blast radius of a wrong tool choice. Why the correct answer wins: A scoped tool list bounds what the agent may call.

### Question 45 — B

Answer: Bound the agent memory to the current session. Session-scoped memory prevents facts crossing conversations. Session-scoped memory keeps context within a conversation and stops one user facts leaking into another. Local study-map skill 3.8 (Agent Orchestration and Tool Binding), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: Session-scoped memory prevents facts crossing conversations.
- **B:** Correct. Session-scoped memory keeps context within a conversation and stops one user facts leaking into another. In this case: Session-scoped memory prevents facts crossing conversations.
- **C:** Incorrect for this question. Typed state makes each handoff explicit and testable instead of relying on free text. Why the correct answer wins: Session-scoped memory prevents facts crossing conversations.
- **D:** Incorrect for this question. An open tool list widens the blast radius of a wrong tool choice. Why the correct answer wins: Session-scoped memory prevents facts crossing conversations.

### Question 46 — A

Answer: Build the evaluation dataset from real queries with graded answers. Real queries with graded answers make the result defensible. A dataset drawn from real traffic with graded answers is what makes an evaluation number mean something. Local study-map skill 4.1 (Evaluation Dataset and Ground-Truth Design), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Correct. A dataset drawn from real traffic with graded answers is what makes an evaluation number mean something. In this case: Real queries with graded answers make the result defensible.
- **B:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: Real queries with graded answers make the result defensible.
- **C:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: Real queries with graded answers make the result defensible.
- **D:** Incorrect for this question. A set authored from the prompt repeats its assumptions, so it passes changes that real users would reject. Why the correct answer wins: Real queries with graded answers make the result defensible.

### Question 47 — D

Answer: Use an LLM judge with a rubric, calibrated against human grades. An LLM judge calibrated against human grades scales the grading. An LLM judge scales grading, and calibrating it against human grades is what keeps the score trustworthy. Local study-map skill 4.1 (Evaluation Dataset and Ground-Truth Design), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. A set authored from the prompt repeats its assumptions, so it passes changes that real users would reject. Why the correct answer wins: An LLM judge calibrated against human grades scales the grading.
- **B:** Incorrect for this question. An uncalibrated judge can reproduce a systematic error consistently and look stable while being wrong. Why the correct answer wins: An LLM judge calibrated against human grades scales the grading.
- **C:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: An LLM judge calibrated against human grades scales the grading.
- **D:** Correct. An LLM judge scales grading, and calibrating it against human grades is what keeps the score trustworthy. In this case: An LLM judge calibrated against human grades scales the grading.

### Question 48 — D

Answer: Score groundedness against the retrieved passages. Groundedness measures whether the answer is supported by retrieved context. Groundedness asks whether the answer is supported by the retrieved context, which is the core anti-fabrication metric. Local study-map skill 4.2 (Groundedness and Relevance Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. Relevance asks whether the answer addresses what was asked, independently of whether it is true. Why the correct answer wins: Groundedness measures whether the answer is supported by retrieved context.
- **B:** Incorrect for this question. Coherence measures whether the answer holds together logically, not whether it is grounded in a source. Why the correct answer wins: Groundedness measures whether the answer is supported by retrieved context.
- **C:** Incorrect for this question. Fluency measures readability and language quality, not factual support. Why the correct answer wins: Groundedness measures whether the answer is supported by retrieved context.
- **D:** Correct. Groundedness asks whether the answer is supported by the retrieved context, which is the core anti-fabrication metric. In this case: Groundedness measures whether the answer is supported by retrieved context.

### Question 49 — C

Answer: Score relevance of the answer to the question asked. Relevance measures whether the answer addresses the question. Relevance asks whether the answer addresses what was asked, independently of whether it is true. Local study-map skill 4.2 (Groundedness and Relevance Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. Groundedness asks whether the answer is supported by the retrieved context, which is the core anti-fabrication metric. Why the correct answer wins: Relevance measures whether the answer addresses the question.
- **B:** Incorrect for this question. Fluency measures readability and language quality, not factual support. Why the correct answer wins: Relevance measures whether the answer addresses the question.
- **C:** Correct. Relevance asks whether the answer addresses what was asked, independently of whether it is true. In this case: Relevance measures whether the answer addresses the question.
- **D:** Incorrect for this question. Similarity compares the answer with a reference, which requires a reference answer for every case. Why the correct answer wins: Relevance measures whether the answer addresses the question.

### Question 50 — B

Answer: Test indirect injection through retrieved documents. Indirect injection hides instructions in retrieved content. Indirect injection hides instructions in retrieved content, which is the vector a retrieval system most easily misses. Local study-map skill 4.4 (Safety, Jailbreak, and Content Filter Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. Adversarial cases test whether instructions in the input or the content can override the system prompt. Why the correct answer wins: Indirect injection hides instructions in retrieved content.
- **B:** Correct. Indirect injection hides instructions in retrieved content, which is the vector a retrieval system most easily misses. In this case: Indirect injection hides instructions in retrieved content.
- **C:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: Indirect injection hides instructions in retrieved content.
- **D:** Incorrect for this question. Toxicity evaluation measures harmful output against the standard that audience or regulation requires. Why the correct answer wins: Indirect injection hides instructions in retrieved content.

### Question 51 — A

Answer: Enable distributed tracing and log the retrieval and model spans. Span-level tracing attributes the failure to retrieval or generation. Span-level tracing shows which stage produced a wrong answer, which an aggregate score cannot. Local study-map skill 4.5 (Tracing, Logging, and Application Insights Observability), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Correct. Span-level tracing shows which stage produced a wrong answer, which an aggregate score cannot. In this case: Span-level tracing attributes the failure to retrieval or generation.
- **B:** Incorrect for this question. An uncalibrated judge can reproduce a systematic error consistently and look stable while being wrong. Why the correct answer wins: Span-level tracing attributes the failure to retrieval or generation.
- **C:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: Span-level tracing attributes the failure to retrieval or generation.
- **D:** Incorrect for this question. Full prompt and completion logging is what lets a reviewer reproduce a bad answer. Why the correct answer wins: Span-level tracing attributes the failure to retrieval or generation.

### Question 52 — C

Answer: Log prompts and completions against the trace, within data policy. Prompts and completions logged against the trace allow replay. Full prompt and completion logging is what lets a reviewer reproduce a bad answer. Local study-map skill 4.5 (Tracing, Logging, and Application Insights Observability), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: Prompts and completions logged against the trace allow replay.
- **B:** Incorrect for this question. Span-level tracing shows which stage produced a wrong answer, which an aggregate score cannot. Why the correct answer wins: Prompts and completions logged against the trace allow replay.
- **C:** Correct. Full prompt and completion logging is what lets a reviewer reproduce a bad answer. In this case: Prompts and completions logged against the trace allow replay.
- **D:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: Prompts and completions logged against the trace allow replay.

### Question 53 — B

Answer: Capture user feedback and review a sample of rated conversations weekly. Capturing and triaging feedback surfaces traffic the dataset lacks. User feedback is the only signal about traffic that the evaluation set does not contain. Local study-map skill 4.6 (Online Feedback Loops and Continuous Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. An uncalibrated judge can reproduce a systematic error consistently and look stable while being wrong. Why the correct answer wins: Capturing and triaging feedback surfaces traffic the dataset lacks.
- **B:** Correct. User feedback is the only signal about traffic that the evaluation set does not contain. In this case: Capturing and triaging feedback surfaces traffic the dataset lacks.
- **C:** Incorrect for this question. Online evaluation catches the drift that a fixed offline dataset cannot represent. Why the correct answer wins: Capturing and triaging feedback surfaces traffic the dataset lacks.
- **D:** Incorrect for this question. An offline gate stops a regression before it reaches production traffic. Why the correct answer wins: Capturing and triaging feedback surfaces traffic the dataset lacks.

### Question 54 — C, E

Answers: Build the evaluation dataset from real queries with graded answers; Use a few hundred representative cases rather than a dozen. Real queries make it representative, and a few hundred cases keep the interval meaningful. A dataset drawn from real traffic with graded answers is what makes an evaluation number mean something. A small sample produces a confidence interval too wide to separate a real improvement from noise. Local study-map skill 4.1 (Evaluation Dataset and Ground-Truth Design), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: Real queries make it representative, and a few hundred cases keep the interval meaningful.
- **B:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: Real queries make it representative, and a few hundred cases keep the interval meaningful.
- **C:** Correct. A dataset drawn from real traffic with graded answers is what makes an evaluation number mean something. In this case: Real queries make it representative, and a few hundred cases keep the interval meaningful.
- **D:** Incorrect for this question. A set authored from the prompt repeats its assumptions, so it passes changes that real users would reject. Why the correct answer wins: Real queries make it representative, and a few hundred cases keep the interval meaningful.
- **E:** Correct. A small sample produces a confidence interval too wide to separate a real improvement from noise. In this case: Real queries make it representative, and a few hundred cases keep the interval meaningful.

### Question 55 — A, B

Answers: Test indirect injection through retrieved documents; Run adversarial jailbreak and prompt-injection cases before release. Indirect cases test retrieved content, and jailbreak cases test user input. Indirect injection hides instructions in retrieved content, which is the vector a retrieval system most easily misses. Adversarial cases test whether instructions in the input or the content can override the system prompt. Local study-map skill 4.4 (Safety, Jailbreak, and Content Filter Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Correct. Adversarial cases test whether instructions in the input or the content can override the system prompt. In this case: Indirect cases test retrieved content, and jailbreak cases test user input.
- **B:** Correct. Indirect injection hides instructions in retrieved content, which is the vector a retrieval system most easily misses. In this case: Indirect cases test retrieved content, and jailbreak cases test user input.
- **C:** Incorrect for this question. Toxicity evaluation measures harmful output against the standard that audience or regulation requires. Why the correct answer wins: Indirect cases test retrieved content, and jailbreak cases test user input.
- **D:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: Indirect cases test retrieved content, and jailbreak cases test user input.
- **E:** Incorrect for this question. Fluency measures readability and language quality, not factual support. Why the correct answer wins: Indirect cases test retrieved content, and jailbreak cases test user input.

### Question 56 — B, E

Answers: Enable distributed tracing and log the retrieval and model spans; Log prompts and completions against the trace, within data policy. Tracing identifies the stage, and prompt logging permits replay. Span-level tracing shows which stage produced a wrong answer, which an aggregate score cannot. Full prompt and completion logging is what lets a reviewer reproduce a bad answer. Local study-map skill 4.5 (Tracing, Logging, and Application Insights Observability), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. An uncalibrated judge can reproduce a systematic error consistently and look stable while being wrong. Why the correct answer wins: Tracing identifies the stage, and prompt logging permits replay.
- **B:** Correct. Span-level tracing shows which stage produced a wrong answer, which an aggregate score cannot. In this case: Tracing identifies the stage, and prompt logging permits replay.
- **C:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: Tracing identifies the stage, and prompt logging permits replay.
- **D:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: Tracing identifies the stage, and prompt logging permits replay.
- **E:** Correct. Full prompt and completion logging is what lets a reviewer reproduce a bad answer. In this case: Tracing identifies the stage, and prompt logging permits replay.

### Question 57 — A, D

Answers: Score groundedness against the retrieved passages; Score relevance of the answer to the question asked. Groundedness measures support, and relevance measures whether the question was answered. Groundedness asks whether the answer is supported by the retrieved context, which is the core anti-fabrication metric. Relevance asks whether the answer addresses what was asked, independently of whether it is true. Local study-map skill 4.2 (Groundedness and Relevance Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Correct. Groundedness asks whether the answer is supported by the retrieved context, which is the core anti-fabrication metric. In this case: Groundedness measures support, and relevance measures whether the question was answered.
- **B:** Incorrect for this question. Coherence measures whether the answer holds together logically, not whether it is grounded in a source. Why the correct answer wins: Groundedness measures support, and relevance measures whether the question was answered.
- **C:** Incorrect for this question. Fluency measures readability and language quality, not factual support. Why the correct answer wins: Groundedness measures support, and relevance measures whether the question was answered.
- **D:** Correct. Relevance asks whether the answer addresses what was asked, independently of whether it is true. In this case: Groundedness measures support, and relevance measures whether the question was answered.
- **E:** Incorrect for this question. Similarity compares the answer with a reference, which requires a reference answer for every case. Why the correct answer wins: Groundedness measures support, and relevance measures whether the question was answered.

### Question 58 — D

Answer: Open the failing request trace → inspect the retrieval span for the passages returned → inspect the prompt and completion for that call → add the case to the evaluation set. The trace locates the stage, retrieval shows whether the passage existed, and the case joins the regression set. The trace locates the failing stage, the retrieval span shows whether the passage was even present, and the case becomes a lasting regression test. Local study-map skill 4.6 (Online Feedback Loops and Continuous Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. The case is filed before the failure is understood, and the trace is opened after the completion has been read out of context. Why the correct answer wins: The trace locates the stage, retrieval shows whether the passage existed, and the case joins the regression set.
- **B:** Incorrect for this question. The retrieval span cannot be read without the trace, and retraining still precedes the diagnosis. Why the correct answer wins: The trace locates the stage, retrieval shows whether the passage existed, and the case joins the regression set.
- **C:** Incorrect for this question. Retraining before the failing stage is identified changes a component that may not be at fault. Why the correct answer wins: The trace locates the stage, retrieval shows whether the passage existed, and the case joins the regression set.
- **D:** Correct. The trace locates the failing stage, the retrieval span shows whether the passage was even present, and the case becomes a lasting regression test. In this case: The trace locates the stage, retrieval shows whether the passage existed, and the case joins the regression set.

### Question 59 — D

Answer: Measure tokens per request and set a budget per endpoint. Per-request token measurement is what lets spend be attributed to a department. Tokens are the billing unit, so per-request measurement is what makes cost attributable to a workload. Local study-map skill 5.1 (Token Cost, Caching, and Throughput Planning), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: Per-request token measurement is what lets spend be attributed to a department.
- **B:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: Per-request token measurement is what lets spend be attributed to a department.
- **C:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: Per-request token measurement is what lets spend be attributed to a department.
- **D:** Correct. Tokens are the billing unit, so per-request measurement is what makes cost attributable to a workload. In this case: Per-request token measurement is what lets spend be attributed to a department.

### Question 60 — B

Answer: Set a time-to-live on the cache. A TTL stops a cached answer outliving its source. A TTL keeps a cached answer from outliving the content it came from. Local study-map skill 5.1 (Token Cost, Caching, and Throughput Planning), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: A TTL stops a cached answer outliving its source.
- **B:** Correct. A TTL keeps a cached answer from outliving the content it came from. In this case: A TTL stops a cached answer outliving its source.
- **C:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: A TTL stops a cached answer outliving its source.
- **D:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: A TTL stops a cached answer outliving its source.

### Question 61 — B

Answer: Route simple requests to a smaller model. A smaller model serves simple requests at lower cost and latency. A smaller model answers a simple request at a fraction of the cost and latency. Local study-map skill 5.2 (Model Routing, Distillation, and Right-Sizing), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: A smaller model serves simple requests at lower cost and latency.
- **B:** Correct. A smaller model answers a simple request at a fraction of the cost and latency. In this case: A smaller model serves simple requests at lower cost and latency.
- **C:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: A smaller model serves simple requests at lower cost and latency.
- **D:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: A smaller model serves simple requests at lower cost and latency.

### Question 62 — D

Answer: Add a router that classifies the request and selects a model. A router classifies the request and selects a model. A router applies a cheap model where it suffices and keeps the stronger model for hard cases. Local study-map skill 5.2 (Model Routing, Distillation, and Right-Sizing), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: A router classifies the request and selects a model.
- **B:** Incorrect for this question. A smaller model answers a simple request at a fraction of the cost and latency. Why the correct answer wins: A router classifies the request and selects a model.
- **C:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: A router classifies the request and selects a model.
- **D:** Correct. A router applies a cheap model where it suffices and keeps the stronger model for hard cases. In this case: A router classifies the request and selects a model.

### Question 63 — B

Answer: Retrieve fewer but better-ranked passages. Fewer, better-ranked passages cut tokens and improve precision. Retrieval depth is a direct cost driver; fewer, better passages cut tokens and can improve precision. Local study-map skill 5.4 (Retrieval Tuning for Relevance and Cost), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: Fewer, better-ranked passages cut tokens and improve precision.
- **B:** Correct. Retrieval depth is a direct cost driver; fewer, better passages cut tokens and can improve precision. In this case: Fewer, better-ranked passages cut tokens and improve precision.
- **C:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: Fewer, better-ranked passages cut tokens and improve precision.
- **D:** Incorrect for this question. Retrieving more passages adds tokens and can bury the relevant passage among distractors. Why the correct answer wins: Fewer, better-ranked passages cut tokens and improve precision.

### Question 64 — C

Answer: Compress the system prompt and remove redundant instructions. Compressing the prompt cuts input tokens on every call. A shorter system prompt reduces input tokens on every single call. Local study-map skill 5.5 (Prompt Compression and Context Discipline), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: Compressing the prompt cuts input tokens on every call.
- **B:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: Compressing the prompt cuts input tokens on every call.
- **C:** Correct. A shorter system prompt reduces input tokens on every single call. In this case: Compressing the prompt cuts input tokens on every call.
- **D:** Incorrect for this question. Retrieving more passages adds tokens and can bury the relevant passage among distractors. Why the correct answer wins: Compressing the prompt cuts input tokens on every call.

### Question 65 — C

Answer: Fine-tune on approved examples to shorten the standing prompt. Fine-tuning can move stable instructions into the weights. Fine-tuning can absorb instructions and style into the weights, which shortens prompts for a stable task. Local study-map skill 5.6 (Fine-Tuning and Distillation for Quality), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. Fine-tuning bakes a snapshot of the content into the model, so it goes stale as documents change. Why the correct answer wins: Fine-tuning can move stable instructions into the weights.
- **B:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: Fine-tuning can move stable instructions into the weights.
- **C:** Correct. Fine-tuning can absorb instructions and style into the weights, which shortens prompts for a stable task. In this case: Fine-tuning can move stable instructions into the weights.
- **D:** Incorrect for this question. A shorter system prompt reduces input tokens on every single call. Why the correct answer wins: Fine-tuning can move stable instructions into the weights.

### Question 66 — C

Answer: Move steady traffic to provisioned throughput. Provisioned throughput lowers cost per token at sustained volume. Provisioned throughput trades a commitment for a lower cost per token at sustained volume. Local study-map skill 5.7 (Batch Inference and Provisioned Capacity Optimization), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. Pay-as-you-go costs nothing when idle and needs no forecast, which suits an unproven workload. Why the correct answer wins: Provisioned throughput lowers cost per token at sustained volume.
- **B:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: Provisioned throughput lowers cost per token at sustained volume.
- **C:** Correct. Provisioned throughput trades a commitment for a lower cost per token at sustained volume. In this case: Provisioned throughput lowers cost per token at sustained volume.
- **D:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: Provisioned throughput lowers cost per token at sustained volume.

### Question 67 — C, D

Answers: Measure tokens per request and set a budget per endpoint; Set a time-to-live on the cache. A token budget attributes cost, and a TTL keeps answers current. Tokens are the billing unit, so per-request measurement is what makes cost attributable to a workload. A TTL keeps a cached answer from outliving the content it came from. Local study-map skill 5.1 (Token Cost, Caching, and Throughput Planning), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: A token budget attributes cost, and a TTL keeps answers current.
- **B:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: A token budget attributes cost, and a TTL keeps answers current.
- **C:** Correct. Tokens are the billing unit, so per-request measurement is what makes cost attributable to a workload. In this case: A token budget attributes cost, and a TTL keeps answers current.
- **D:** Correct. A TTL keeps a cached answer from outliving the content it came from. In this case: A token budget attributes cost, and a TTL keeps answers current.
- **E:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: A token budget attributes cost, and a TTL keeps answers current.

### Question 68 — A, D

Answers: Retrieve fewer but better-ranked passages; Compress the system prompt and remove redundant instructions. Fewer passages cut retrieved tokens, and a compressed prompt cuts input tokens. Retrieval depth is a direct cost driver; fewer, better passages cut tokens and can improve precision. A shorter system prompt reduces input tokens on every single call. Local study-map skill 5.4 (Retrieval Tuning for Relevance and Cost), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Correct. Retrieval depth is a direct cost driver; fewer, better passages cut tokens and can improve precision. In this case: Fewer passages cut retrieved tokens, and a compressed prompt cuts input tokens.
- **B:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: Fewer passages cut retrieved tokens, and a compressed prompt cuts input tokens.
- **C:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: Fewer passages cut retrieved tokens, and a compressed prompt cuts input tokens.
- **D:** Correct. A shorter system prompt reduces input tokens on every single call. In this case: Fewer passages cut retrieved tokens, and a compressed prompt cuts input tokens.
- **E:** Incorrect for this question. Retrieving more passages adds tokens and can bury the relevant passage among distractors. Why the correct answer wins: Fewer passages cut retrieved tokens, and a compressed prompt cuts input tokens.

### Question 69 — B

Answer: Measure the current request rate and token volume → forecast the peak and steady load → compare pay-as-you-go cost with provisioned throughput at that volume → load test the chosen configuration. Measurement and forecasting come before the commercial comparison, and the load test validates it. Measurement and forecasting come before the commercial comparison, and the load test validates the decision. Local study-map skill 5.3 (Latency Budgets and Streaming Design), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. The forecast is made without a measurement baseline, and the commitment precedes the measurement entirely. Why the correct answer wins: Measurement and forecasting come before the commercial comparison, and the load test validates it.
- **B:** Correct. Measurement and forecasting come before the commercial comparison, and the load test validates the decision. In this case: Measurement and forecasting come before the commercial comparison, and the load test validates it.
- **C:** Incorrect for this question. Capacity is committed before the demand that justifies it has been measured. Why the correct answer wins: Measurement and forecasting come before the commercial comparison, and the load test validates it.
- **D:** Incorrect for this question. A load test needs a configuration chosen from the measurement and forecast, both of which come later. Why the correct answer wins: Measurement and forecasting come before the commercial comparison, and the load test validates it.

### Question 70 — B

Answer: Promote versions through aliases such as candidate and production. An alias gives a stable pointer that promotion moves. An alias gives a stable pointer that a deployment can resolve, so promotion is a controlled switch rather than an edit. Local study-map skill 1.6 (Model Registry and Environment Promotion), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Deploying whatever is latest lets an untested registration reach production with no promotion gate. Why the correct answer wins: An alias gives a stable pointer that promotion moves.
- **B:** Correct. An alias gives a stable pointer that a deployment can resolve, so promotion is a controlled switch rather than an edit. In this case: An alias gives a stable pointer that promotion moves.
- **C:** Incorrect for this question. An explicit version pins what is served, so a new registration cannot silently change production behaviour. Why the correct answer wins: An alias gives a stable pointer that promotion moves.
- **D:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: An alias gives a stable pointer that promotion moves.

### Question 71 — C

Answer: Publish the component to the workspace registry. A registry shares assets across workspaces. A registry shares assets across workspaces, which is how a pattern proven in development is reused in production. Local study-map skill 1.6 (Model Registry and Environment Promotion), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. A hand rebuild cannot be reproduced exactly and drifts from the definition the team believed it had. Why the correct answer wins: A registry shares assets across workspaces.
- **B:** Incorrect for this question. A component gives the step a typed interface, so it can be reused in other pipelines and tested alone. Why the correct answer wins: A registry shares assets across workspaces.
- **C:** Correct. A registry shares assets across workspaces, which is how a pattern proven in development is reused in production. In this case: A registry shares assets across workspaces.
- **D:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A registry shares assets across workspaces.

### Question 72 — A, C

Answers: Register a datastore that points at the storage account; Build a versioned curated environment for the job. A datastore holds the connection, and a curated environment pins dependencies. A datastore holds the connection and credential, so jobs reference data by name instead of an account key and physical path. A versioned environment pins the interpreter and packages, so the same job resolves the same dependencies months later. Local study-map skill 1.1 (Workspace, Compute, and Datastore Provisioning), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Correct. A datastore holds the connection and credential, so jobs reference data by name instead of an account key and physical path. In this case: A datastore holds the connection, and a curated environment pins dependencies.
- **B:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: A datastore holds the connection, and a curated environment pins dependencies.
- **C:** Correct. A versioned environment pins the interpreter and packages, so the same job resolves the same dependencies months later. In this case: A datastore holds the connection, and a curated environment pins dependencies.
- **D:** Incorrect for this question. An inline key puts a credential in source control and ties the job to one physical path. Why the correct answer wins: A datastore holds the connection, and a curated environment pins dependencies.
- **E:** Incorrect for this question. A floating tag resolves to a different image over time and silently breaks reproducibility. Why the correct answer wins: A datastore holds the connection, and a curated environment pins dependencies.

### Question 73 — B, C

Answers: Authenticate the workflow with workload identity federation and no stored secret; Use GitHub environment protection rules to gate the production deploy job. Federated identity removes the secret, and a protected environment adds approval. Federated identity exchanges the workflow token for an Azure credential, so no long-lived secret exists to leak or rotate. A protected environment requires approval before the job runs, which is the control that stops an unreviewed deployment. Local study-map skill 1.5 (GitHub Actions CI/CD and Workload Identity Federation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. A matrix runs the same tests across configurations in parallel, which catches dependency drift before release. Why the correct answer wins: Federated identity removes the secret, and a protected environment adds approval.
- **B:** Correct. Federated identity exchanges the workflow token for an Azure credential, so no long-lived secret exists to leak or rotate. In this case: Federated identity removes the secret, and a protected environment adds approval.
- **C:** Correct. A protected environment requires approval before the job runs, which is the control that stops an unreviewed deployment. In this case: Federated identity removes the secret, and a protected environment adds approval.
- **D:** Incorrect for this question. Owner on the subscription lets a pipeline change any resource, so one bad commit can affect everything. Why the correct answer wins: Federated identity removes the secret, and a protected environment adds approval.
- **E:** Incorrect for this question. A stored client secret is long-lived and must be rotated; federation removes the secret entirely. Why the correct answer wins: Federated identity removes the secret, and a protected environment adds approval.

### Question 74 — D

Answer: Attach a CPU compute cluster for the data preparation step. CPU compute is sufficient and cheaper per core. A CPU cluster is cheaper per core and sufficient for tabular preparation, which gains nothing from an accelerator. Local study-map skill 2.2 (Job Configuration, Compute Targets, and Sweeps), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: CPU compute is sufficient and cheaper per core.
- **B:** Incorrect for this question. A GPU cluster with a zero minimum scales to nothing when idle, which suits intermittent training without paying for accelerators between runs. Why the correct answer wins: CPU compute is sufficient and cheaper per core.
- **C:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: CPU compute is sufficient and cheaper per core.
- **D:** Correct. A CPU cluster is cheaper per core and sufficient for tabular preparation, which gains nothing from an accelerator. In this case: CPU compute is sufficient and cheaper per core.

### Question 75 — B

Answer: Pin a fixed instance count for a spiky workload. A fixed count is appropriate when load is constant. A fixed count either wastes money at low load or throttles at peak. Local study-map skill 2.7 (Autoscaling, Health Probes, and Rollback), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Scoring a large file one request at a time pays for always-on capacity and is slow for bulk work. Why the correct answer wins: A fixed count is appropriate when load is constant.
- **B:** Correct. A fixed count either wastes money at low load or throttles at peak. In this case: A fixed count is appropriate when load is constant.
- **C:** Incorrect for this question. Liveness restarts an unhealthy container and readiness keeps traffic away until the container can actually serve. Why the correct answer wins: A fixed count is appropriate when load is constant.
- **D:** Incorrect for this question. Autoscale matches capacity to load, and the minimum sets the floor that protects latency during a burst. Why the correct answer wins: A fixed count is appropriate when load is constant.

### Question 76 — B

Answer: Group the trials under a named experiment. A named experiment groups runs so variants compare. An experiment groups related runs, which is how variants of the same task are compared against each other. Local study-map skill 2.3 (Experiment Tracking with MLflow), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: A named experiment groups runs so variants compare.
- **B:** Correct. An experiment groups related runs, which is how variants of the same task are compared against each other. In this case: A named experiment groups runs so variants compare.
- **C:** Incorrect for this question. MLflow records parameters, metrics, and artifacts against a run, which is what makes experiments comparable. Why the correct answer wins: A named experiment groups runs so variants compare.
- **D:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: A named experiment groups runs so variants compare.

### Question 77 — A

Answer: Mount the model artifact rather than baking it into the image. Mounting the artifact decouples the model version from the image. Mounting keeps the artifact out of the image, so a new version does not require an image rebuild. Local study-map skill 2.5 (Managed Online Endpoint Deployment), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. Mounting keeps the artifact out of the image, so a new version does not require an image rebuild. In this case: Mounting the artifact decouples the model version from the image.
- **B:** Incorrect for this question. A one-step replacement exposes every request to an unproven version with no measured canary. Why the correct answer wins: Mounting the artifact decouples the model version from the image.
- **C:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: Mounting the artifact decouples the model version from the image.
- **D:** Incorrect for this question. Baking the model ties every version to an image build, which slows promotion and bloats the registry. Why the correct answer wins: Mounting the artifact decouples the model version from the image.

### Question 78 — A

Answer: Run the whole workflow as a single script job. Separate pipeline steps make the failure visible and rerunnable. A single script hides intermediate artifacts, so a failed stage cannot be rerun without repeating everything. Local study-map skill 2.1 (Training Pipeline Authoring and Orchestration), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. A single script hides intermediate artifacts, so a failed stage cannot be rerun without repeating everything. In this case: Separate pipeline steps make the failure visible and rerunnable.
- **B:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: Separate pipeline steps make the failure visible and rerunnable.
- **C:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: Separate pipeline steps make the failure visible and rerunnable.
- **D:** Incorrect for this question. A pipeline job makes the dependency between steps explicit and records each output, which is what gives lineage. Why the correct answer wins: Separate pipeline steps make the failure visible and rerunnable.

### Question 79 — B, C

Answers: Deploy to a managed online endpoint with an explicit model version; Configure liveness and readiness probes on the deployment. An online endpoint serves synchronous requests, and probes gate traffic until ready. A managed online endpoint serves real-time requests and manages the underlying infrastructure. Liveness restarts an unhealthy container and readiness keeps traffic away until the container can actually serve. Local study-map skill 2.5 (Managed Online Endpoint Deployment), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. A fixed count either wastes money at low load or throttles at peak. Why the correct answer wins: An online endpoint serves synchronous requests, and probes gate traffic until ready.
- **B:** Correct. Liveness restarts an unhealthy container and readiness keeps traffic away until the container can actually serve. In this case: An online endpoint serves synchronous requests, and probes gate traffic until ready.
- **C:** Correct. A managed online endpoint serves real-time requests and manages the underlying infrastructure. In this case: An online endpoint serves synchronous requests, and probes gate traffic until ready.
- **D:** Incorrect for this question. Without probes, a container that starts but cannot load the model still receives traffic. Why the correct answer wins: An online endpoint serves synchronous requests, and probes gate traffic until ready.
- **E:** Incorrect for this question. A batch endpoint scores a large file on a schedule and needs no always-on capacity. Why the correct answer wins: An online endpoint serves synchronous requests, and probes gate traffic until ready.

### Question 80 — A, B

Answers: Deploy a batch endpoint for the overnight scoring job; Keep the previous deployment in place so traffic can be moved back. A batch endpoint avoids always-on capacity, and a retained deployment preserves reversal. A batch endpoint scores a large file on a schedule and needs no always-on capacity. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. Local study-map skill 2.6 (Batch Endpoints and Controlled Traffic Rollout), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. In this case: A batch endpoint avoids always-on capacity, and a retained deployment preserves reversal.
- **B:** Correct. A batch endpoint scores a large file on a schedule and needs no always-on capacity. In this case: A batch endpoint avoids always-on capacity, and a retained deployment preserves reversal.
- **C:** Incorrect for this question. Scoring a large file one request at a time pays for always-on capacity and is slow for bulk work. Why the correct answer wins: A batch endpoint avoids always-on capacity, and a retained deployment preserves reversal.
- **D:** Incorrect for this question. A one-step replacement exposes every request to an unproven version with no measured canary. Why the correct answer wins: A batch endpoint avoids always-on capacity, and a retained deployment preserves reversal.
- **E:** Incorrect for this question. Baking the model ties every version to an image build, which slows promotion and bloats the registry. Why the correct answer wins: A batch endpoint avoids always-on capacity, and a retained deployment preserves reversal.

### Question 81 — C

Answer: Confirm the impact and scope from telemetry → contain the incident by shifting traffic or disabling the feature → fix the identified cause → add a regression case and update the gate. Impact is confirmed, the incident is contained, the cause is fixed, and a regression case joins the gate. Containment protects users before the root cause is chased, and the gate change stops the same defect returning. Local study-map skill 2.7 (Autoscaling, Health Probes, and Rollback), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. A regression case is added before the defect is understood, and containment precedes impact assessment. Why the correct answer wins: Impact is confirmed, the incident is contained, the cause is fixed, and a regression case joins the gate.
- **B:** Incorrect for this question. The scope of impact is confirmed last, so nobody knows what was affected while the fix was being written. Why the correct answer wins: Impact is confirmed, the incident is contained, the cause is fixed, and a regression case joins the gate.
- **C:** Correct. Containment protects users before the root cause is chased, and the gate change stops the same defect returning. In this case: Impact is confirmed, the incident is contained, the cause is fixed, and a regression case joins the gate.
- **D:** Incorrect for this question. The cause is fixed before impact is confirmed, and containment arrives after the fix it was meant to buy time for. Why the correct answer wins: Impact is confirmed, the incident is contained, the cause is fixed, and a regression case joins the gate.

### Question 82 — A

Answer: Detect the drop from monitoring or alerts → compare live feature distributions with the training baseline → identify the changed upstream source → retrain on refreshed data and promote through the gate. Detection precedes attribution, and retraining follows only once the changed source is known. Detection, attribution, and a refreshed candidate in that order address the cause rather than the symptom. Local study-map skill 2.8 (Data and Model Drift Monitoring), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. Detection, attribution, and a refreshed candidate in that order address the cause rather than the symptom. In this case: Detection precedes attribution, and retraining follows only once the changed source is known.
- **B:** Incorrect for this question. The source is named before any evidence exists, and detection comes last. Why the correct answer wins: Detection precedes attribution, and retraining follows only once the changed source is known.
- **C:** Incorrect for this question. Retraining before the drop is detected and attributed risks training on data that has the same defect. Why the correct answer wins: Detection precedes attribution, and retraining follows only once the changed source is known.
- **D:** Incorrect for this question. A distribution comparison needs a detected drop to compare against, so the trigger is out of order. Why the correct answer wins: Detection precedes attribution, and retraining follows only once the changed source is known.

### Question 83 — B

Answer: Publish the component to the registry → build a versioned environment that pins its dependencies → reference both from the pipeline YAML → run the pipeline in the test environment. Assets are published and pinned before the YAML references them. The reusable assets must exist and be versioned before a pipeline can reference them, and the run comes last. Local study-map skill 2.3 (Experiment Tracking with MLflow), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. The YAML references assets that have not been published or built yet. Why the correct answer wins: Assets are published and pinned before the YAML references them.
- **B:** Correct. The reusable assets must exist and be versioned before a pipeline can reference them, and the run comes last. In this case: Assets are published and pinned before the YAML references them.
- **C:** Incorrect for this question. The pipeline runs before its references exist, and the assets are published afterwards. Why the correct answer wins: Assets are published and pinned before the YAML references them.
- **D:** Incorrect for this question. The run precedes both the component publication and the YAML reference that would make it resolvable. Why the correct answer wins: Assets are published and pinned before the YAML references them.

### Question 84 — D

Answer: Start on pay-as-you-go while the volume is still unknown. Pay-as-you-go has no idle commitment, which suits a pilot of uncertain duration. Pay-as-you-go costs nothing when idle and needs no forecast, which suits an unproven workload. Local study-map skill 3.2 (Model Catalog Selection and Deployment Capacity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: Pay-as-you-go has no idle commitment, which suits a pilot of uncertain duration.
- **B:** Incorrect for this question. A fixed count either wastes money at low load or throttles at peak. Why the correct answer wins: Pay-as-you-go has no idle commitment, which suits a pilot of uncertain duration.
- **C:** Incorrect for this question. Provisioned throughput reserves capacity, which gives predictable latency and cost at sustained volume. Why the correct answer wins: Pay-as-you-go has no idle commitment, which suits a pilot of uncertain duration.
- **D:** Correct. Pay-as-you-go costs nothing when idle and needs no forecast, which suits an unproven workload. In this case: Pay-as-you-go has no idle commitment, which suits a pilot of uncertain duration.

### Question 85 — B

Answer: Run the flow as a batch job over the evaluation dataset. A batch run applies the flow to every row of the dataset. A batch run applies the flow to every row, which is how an evaluation dataset is scored. Local study-map skill 3.3 (Prompt Flow Authoring and DAG Composition), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A batch run applies the flow to every row of the dataset.
- **B:** Correct. A batch run applies the flow to every row, which is how an evaluation dataset is scored. In this case: A batch run applies the flow to every row of the dataset.
- **C:** Incorrect for this question. Deploying the flow exposes it as a service the application can call. Why the correct answer wins: A batch run applies the flow to every row of the dataset.
- **D:** Incorrect for this question. Streaming attaches to a running job log, which is a debugging step rather than a way to create or promote an asset. Why the correct answer wins: A batch run applies the flow to every row of the dataset.

### Question 86 — B

Answer: Curate the source documents → chunk and embed them → create the search index → bind the index to the flow → evaluate retrieval and groundedness. Curation, chunking, indexing, binding, and evaluation build on each other in that order. Content is prepared before it is indexed, the index exists before it is bound, and evaluation runs against a working flow. Local study-map skill 3.5 (Retrieval-Augmented Grounding with Azure AI Search), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. The flow is bound to an index that does not exist yet, and evaluation never happens at all. Why the correct answer wins: Curation, chunking, indexing, binding, and evaluation build on each other in that order.
- **B:** Correct. Content is prepared before it is indexed, the index exists before it is bound, and evaluation runs against a working flow. In this case: Curation, chunking, indexing, binding, and evaluation build on each other in that order.
- **C:** Incorrect for this question. Chunking precedes curation, so retired documents are embedded, and evaluation happens before there is an index to query. Why the correct answer wins: Curation, chunking, indexing, binding, and evaluation build on each other in that order.
- **D:** Incorrect for this question. The index is created before its content is curated or embedded, and evaluation precedes the chunks it would retrieve. Why the correct answer wins: Curation, chunking, indexing, binding, and evaluation build on each other in that order.

### Question 87 — A

Answer: Edit the prompt file in a branch → run the offline evaluation gate → review the diff and metric change in a pull request → deploy the approved version and watch the online metrics. The edit is measured before review, review precedes deployment, and online metrics confirm the result. The change is measured before review, review happens before deployment, and online metrics confirm the offline result. Local study-map skill 3.7 (Prompt and Flow Versioning with Evaluation Gates), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Correct. The change is measured before review, review happens before deployment, and online metrics confirm the offline result. In this case: The edit is measured before review, review precedes deployment, and online metrics confirm the result.
- **B:** Incorrect for this question. A version is deployed before it has been edited, evaluated, or reviewed. Why the correct answer wins: The edit is measured before review, review precedes deployment, and online metrics confirm the result.
- **C:** Incorrect for this question. The gate runs before the prompt is edited, so it measures the old wording and clears the way for an unreviewed deploy. Why the correct answer wins: The edit is measured before review, review precedes deployment, and online metrics confirm the result.
- **D:** Incorrect for this question. The diff cannot be reviewed before the edit, and deployment precedes the gate that would block it. Why the correct answer wins: The edit is measured before review, review precedes deployment, and online metrics confirm the result.

### Question 88 — D

Answer: Run a full grid sweep over every combination. A sampled sweep finds the promising region within a trial budget. A full grid multiplies cost by the number of combinations and is rarely needed once the promising region is known. Local study-map skill 2.2 (Job Configuration, Compute Targets, and Sweeps), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: A sampled sweep finds the promising region within a trial budget.
- **B:** Incorrect for this question. Automated ML tests preprocessing and algorithm combinations quickly, which is a reasonable baseline for tabular data. Why the correct answer wins: A sampled sweep finds the promising region within a trial budget.
- **C:** Incorrect for this question. A sweep samples the search space and records every trial, which finds an optimum systematically rather than by guesswork. Why the correct answer wins: A sampled sweep finds the promising region within a trial budget.
- **D:** Correct. A full grid multiplies cost by the number of combinations and is rarely needed once the promising region is known. In this case: A sampled sweep finds the promising region within a trial budget.

### Question 89 — A

Answer: Store connection strings in Key Vault and reference them by name. Key Vault holds the secret and rotation happens outside the flow definition. Key Vault centralizes the secret, so rotation happens once and no value appears in code or job YAML. Local study-map skill 1.7 (Network Isolation, Secrets, and Pipeline Identity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Correct. Key Vault centralizes the secret, so rotation happens once and no value appears in code or job YAML. In this case: Key Vault holds the secret and rotation happens outside the flow definition.
- **B:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: Key Vault holds the secret and rotation happens outside the flow definition.
- **C:** Incorrect for this question. An inline key puts a credential in source control and ties the job to one physical path. Why the correct answer wins: Key Vault holds the secret and rotation happens outside the flow definition.
- **D:** Incorrect for this question. A plain environment variable appears in job definitions and logs, which exposes the secret. Why the correct answer wins: Key Vault holds the secret and rotation happens outside the flow definition.

### Question 90 — B

Answer: Connect to the source through a federated connector and query it in place. A federated connector queries the source in place without copying it. A federated connector answers from content where it already lives, so licensed material need not be copied into a store you are not entitled to build. Local study-map skill 3.1 (Foundry Hub, Project, and Shared Capacity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Exporting licensed content into your own storage is the step the licence usually forbids, so the copy itself is the risk. Why the correct answer wins: A federated connector queries the source in place without copying it.
- **B:** Correct. A federated connector answers from content where it already lives, so licensed material need not be copied into a store you are not entitled to build. In this case: A federated connector queries the source in place without copying it.
- **C:** Incorrect for this question. A key inside a flow file is a secret in source control and cannot be rotated without editing the flow. Why the correct answer wins: A federated connector queries the source in place without copying it.
- **D:** Incorrect for this question. Copying a licensed corpus into an index you host is a storage and licence decision, not just a connector setting. Why the correct answer wins: A federated connector queries the source in place without copying it.

### Question 91 — A

Answer: Run continuous evaluation on sampled production traffic. Continuous evaluation on sampled traffic measures quality between validations. Online evaluation catches the drift that a fixed offline dataset cannot represent. Local study-map skill 4.6 (Online Feedback Loops and Continuous Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Correct. Online evaluation catches the drift that a fixed offline dataset cannot represent. In this case: Continuous evaluation on sampled traffic measures quality between validations.
- **B:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: Continuous evaluation on sampled traffic measures quality between validations.
- **C:** Incorrect for this question. A dataset drawn from real traffic with graded answers is what makes an evaluation number mean something. Why the correct answer wins: Continuous evaluation on sampled traffic measures quality between validations.
- **D:** Incorrect for this question. An offline gate stops a regression before it reaches production traffic. Why the correct answer wins: Continuous evaluation on sampled traffic measures quality between validations.

### Question 92 — D

Answer: Add a router that classifies the request and selects a model. A router selects a model appropriate to each request. A router applies a cheap model where it suffices and keeps the stronger model for hard cases. Local study-map skill 5.2 (Model Routing, Distillation, and Right-Sizing), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: A router selects a model appropriate to each request.
- **B:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: A router selects a model appropriate to each request.
- **C:** Incorrect for this question. A smaller model answers a simple request at a fraction of the cost and latency. Why the correct answer wins: A router selects a model appropriate to each request.
- **D:** Correct. A router applies a cheap model where it suffices and keeps the stronger model for hard cases. In this case: A router selects a model appropriate to each request.

### Question 93 — B

Answer: Move steady traffic to provisioned throughput. Provisioned throughput lowers unit cost at sustained volume. Provisioned throughput trades a commitment for a lower cost per token at sustained volume. Local study-map skill 5.7 (Batch Inference and Provisioned Capacity Optimization), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: Provisioned throughput lowers unit cost at sustained volume.
- **B:** Correct. Provisioned throughput trades a commitment for a lower cost per token at sustained volume. In this case: Provisioned throughput lowers unit cost at sustained volume.
- **C:** Incorrect for this question. Pay-as-you-go costs nothing when idle and needs no forecast, which suits an unproven workload. Why the correct answer wins: Provisioned throughput lowers unit cost at sustained volume.
- **D:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: Provisioned throughput lowers unit cost at sustained volume.

### Question 94 — C, D

Answers: Fine-tune on approved examples to shorten the standing prompt; Re-run the evaluation after the cost optimization. Fine-tuning can absorb stable instructions, and the evaluation confirms accuracy held. Fine-tuning can absorb instructions and style into the weights, which shortens prompts for a stable task. An optimization that lowers cost can lower quality, and re-running the evaluation is what proves the trade is acceptable. Local study-map skill 5.6 (Fine-Tuning and Distillation for Quality), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. Fine-tuning bakes a snapshot of the content into the model, so it goes stale as documents change. Why the correct answer wins: Fine-tuning can absorb stable instructions, and the evaluation confirms accuracy held.
- **B:** Incorrect for this question. A shorter system prompt reduces input tokens on every single call. Why the correct answer wins: Fine-tuning can absorb stable instructions, and the evaluation confirms accuracy held.
- **C:** Correct. Fine-tuning can absorb instructions and style into the weights, which shortens prompts for a stable task. In this case: Fine-tuning can absorb stable instructions, and the evaluation confirms accuracy held.
- **D:** Correct. An optimization that lowers cost can lower quality, and re-running the evaluation is what proves the trade is acceptable. In this case: Fine-tuning can absorb stable instructions, and the evaluation confirms accuracy held.
- **E:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: Fine-tuning can absorb stable instructions, and the evaluation confirms accuracy held.

### Question 95 — A

Answer: Define the workspace in a Bicep module deployed per environment. A reviewed Bicep module recreates the environment identically. Bicep gives a declarative, reviewable definition, so an environment can be recreated identically and configuration drift becomes visible. Local study-map skill 1.3 (Infrastructure as Code with Bicep), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Correct. Bicep gives a declarative, reviewable definition, so an environment can be recreated identically and configuration drift becomes visible. In this case: A reviewed Bicep module recreates the environment identically.
- **B:** Incorrect for this question. Exporting captures whatever exists, including accidental settings, and starts the estate from an unreviewed hand-built state. Why the correct answer wins: A reviewed Bicep module recreates the environment identically.
- **C:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A reviewed Bicep module recreates the environment identically.
- **D:** Incorrect for this question. A hand rebuild cannot be reproduced exactly and drifts from the definition the team believed it had. Why the correct answer wins: A reviewed Bicep module recreates the environment identically.

### Question 96 — A

Answer: Enable data drift monitoring against the training baseline. Drift monitoring compares live inputs with the training baseline. Drift monitoring compares live input distributions with the training baseline, which is what catches silent degradation. Local study-map skill 2.8 (Data and Model Drift Monitoring), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. Drift monitoring compares live input distributions with the training baseline, which is what catches silent degradation. In this case: Drift monitoring compares live inputs with the training baseline.
- **B:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: Drift monitoring compares live inputs with the training baseline.
- **C:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: Drift monitoring compares live inputs with the training baseline.
- **D:** Incorrect for this question. Deployment-time accuracy is a snapshot; it says nothing about the data that arrives afterwards. Why the correct answer wins: Drift monitoring compares live inputs with the training baseline.

### Question 97 — A, B

Answers: Split endpoint traffic 10/90 so the new deployment receives a canary share; Keep the previous deployment in place so traffic can be moved back. A canary share bounds exposure, and a retained deployment enables rollback. A traffic split sends a small share to the new deployment, so a regression affects fewer requests and is measurable. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. Local study-map skill 2.6 (Batch Endpoints and Controlled Traffic Rollout), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. In this case: A canary share bounds exposure, and a retained deployment enables rollback.
- **B:** Correct. A traffic split sends a small share to the new deployment, so a regression affects fewer requests and is measurable. In this case: A canary share bounds exposure, and a retained deployment enables rollback.
- **C:** Incorrect for this question. A one-step replacement exposes every request to an unproven version with no measured canary. Why the correct answer wins: A canary share bounds exposure, and a retained deployment enables rollback.
- **D:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: A canary share bounds exposure, and a retained deployment enables rollback.
- **E:** Incorrect for this question. Baking the model ties every version to an image build, which slows promotion and bloats the registry. Why the correct answer wins: A canary share bounds exposure, and a retained deployment enables rollback.

### Question 98 — C

Answer: Fine-tune the model on the document set instead of retrieving. Fine-tuning bakes a snapshot that goes stale as manuals are revised. Fine-tuning bakes a snapshot of the content into the model, so it goes stale as documents change. Local study-map skill 5.6 (Fine-Tuning and Distillation for Quality), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. Document-level access keeps retrieval within what the requesting user is allowed to see. Why the correct answer wins: Fine-tuning bakes a snapshot that goes stale as manuals are revised.
- **B:** Incorrect for this question. Scheduled refresh keeps retrieval aligned with the source; without it the assistant answers from retired content. Why the correct answer wins: Fine-tuning bakes a snapshot that goes stale as manuals are revised.
- **C:** Correct. Fine-tuning bakes a snapshot of the content into the model, so it goes stale as documents change. In this case: Fine-tuning bakes a snapshot that goes stale as manuals are revised.
- **D:** Incorrect for this question. An index supports retrieval at answer time, so the flow grounds on current content instead of on model memory. Why the correct answer wins: Fine-tuning bakes a snapshot that goes stale as manuals are revised.

### Question 99 — D

Answer: Rebuild the index on a schedule after the source content changes. A scheduled refresh keeps retrieval aligned with the current revision. Scheduled refresh keeps retrieval aligned with the source; without it the assistant answers from retired content. Local study-map skill 3.6 (Chunking, Embeddings, and Index Refresh), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: A scheduled refresh keeps retrieval aligned with the current revision.
- **B:** Incorrect for this question. Section-sized chunks with overlap keep a passage coherent while staying small enough to be specific. Why the correct answer wins: A scheduled refresh keeps retrieval aligned with the current revision.
- **C:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: A scheduled refresh keeps retrieval aligned with the current revision.
- **D:** Correct. Scheduled refresh keeps retrieval aligned with the source; without it the assistant answers from retired content. In this case: A scheduled refresh keeps retrieval aligned with the current revision.

### Question 100 — D

Answer: Score groundedness against the retrieved passages. Groundedness measures whether the answer is supported by retrieved context. Groundedness asks whether the answer is supported by the retrieved context, which is the core anti-fabrication metric. Local study-map skill 4.2 (Groundedness and Relevance Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. Fluency measures readability and language quality, not factual support. Why the correct answer wins: Groundedness measures whether the answer is supported by retrieved context.
- **B:** Incorrect for this question. Coherence measures whether the answer holds together logically, not whether it is grounded in a source. Why the correct answer wins: Groundedness measures whether the answer is supported by retrieved context.
- **C:** Incorrect for this question. Relevance asks whether the answer addresses what was asked, independently of whether it is true. Why the correct answer wins: Groundedness measures whether the answer is supported by retrieved context.
- **D:** Correct. Groundedness asks whether the answer is supported by the retrieved context, which is the core anti-fabrication metric. In this case: Groundedness measures whether the answer is supported by retrieved context.
