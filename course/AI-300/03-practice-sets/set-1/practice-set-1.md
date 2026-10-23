# Microsoft AI-300 — Full-Length Mock Exam 1

Machine Learning Operations Engineer · 100 questions · expanded practice bank · passing target 700/1000

Blueprint-weighted mock exam. Item mix: 84 multiple-choice (selection count stated where needed), 16 multi-select, and 4 case studies of 3 questions. 8 of the multiple-choice items ask you to choose the correct candidate sequence. Drag-and-drop sequencing UI, live lab environments, and adaptive problem-solution sets cannot be reproduced in a CSV; see the README for the exact fidelity boundary.

Original educational content, not actual, recalled, or copied Microsoft exam items.

## Questions

### 1. A team must keep development experiments from touching the registered models that production serves. What should the platform lead create per environment?

Domain: Design and implement an MLOps infrastructure

- A. Create the workspace in the portal and record the steps in a wiki
- B. Create a separate Azure Machine Learning workspace per environment
- C. Use one workspace for development, test, and production
- D. Attach a GPU cluster with four always-on nodes

### 2. A team trains two models a week, each for about three hours, and wants to stop paying for accelerators between runs. Which compute configuration fits?

Domain: Design and implement an MLOps infrastructure

- A. Attach a GPU cluster with a minimum of zero nodes
- B. Attach a CPU compute cluster for the data preparation step
- C. Attach a GPU cluster with four always-on nodes
- D. Run the job from a compute instance notebook

### 3. Two runs of the same training script produced different results last month because a library version changed underneath them. What should the team pin?

Domain: Design and implement an MLOps infrastructure

- A. Print the metrics to the job log and read them from the console
- B. Build a versioned curated environment for the job
- C. Run the job from a compute instance notebook
- D. Reference the floating latest tag for the environment image

### 4. An auditor asks which exact data a model was trained on eight months ago. What should have been registered at training time?

Domain: Design and implement an MLOps infrastructure

- A. Register the data as a versioned data asset
- B. Print the metrics to the job log and read them from the console
- C. Register a datastore that points at the storage account
- D. Reference the storage path with the account key inline in the job YAML

### 5. A data-preparation step is copied and pasted into four pipelines and has drifted between them. What should the team create?

Domain: Design and implement an MLOps infrastructure

- A. Run the whole workflow as a single script job
- B. Package the preparation step as a reusable component
- C. Run the job from a compute instance notebook
- D. Create the workspace in the portal and record the steps in a wiki

### 6. A second region must be stood up with exactly the same workspace, storage, and Key Vault configuration as the first. What should be used?

Domain: Design and implement an MLOps infrastructure

- A. Define the workspace in a Bicep module deployed per environment
- B. Rebuild the environment by hand from the notes in the ticket
- C. Export an ARM template from the portal after building it by hand
- D. Create the workspace in the portal and record the steps in a wiki

### 7. One Bicep module must deploy to development, test, and production with different SKUs and names but an identical shape. What should hold the differences?

Domain: Design and implement an MLOps infrastructure

- A. Export an ARM template from the portal after building it by hand
- B. Pass environment values through a Bicep parameter file per stage
- C. Rebuild the environment by hand from the notes in the ticket
- D. Create the workspace in the portal and record the steps in a wiki

### 8. Resources were deleted by hand and the next deployment left the environment inconsistent with its template. What should the team deploy as?

Domain: Design and implement an MLOps infrastructure

- A. Rebuild the environment by hand from the notes in the ticket
- B. Export an ARM template from the portal after building it by hand
- C. Create the workspace in the portal and record the steps in a wiki
- D. Deploy the module as a deployment stack so removed resources are cleaned up

### 9. A training job must be submitted identically from a laptop and from a pipeline, with no notebook interaction. What should be used?

Domain: Design and implement an MLOps infrastructure

- A. Run the job from a compute instance notebook
- B. Create the workspace in the portal and record the steps in a wiki
- C. Stream the job with az ml job stream to inspect logs
- D. Submit the job with az ml job create --file job.yaml

### 10. A job is running and the engineer needs the failing step output as it happens. What should be used?

Domain: Design and implement an MLOps infrastructure

- A. Submit the job with az ml job create --file job.yaml
- B. Print the metrics to the job log and read them from the console
- C. Run the job from a compute instance notebook
- D. Stream the job with az ml job stream to inspect logs

### 11. A security review objects to a long-lived client secret stored in the repository that the workflow uses to reach Azure. What should replace it?

Domain: Design and implement an MLOps infrastructure

- A. Store a service principal client secret as a GitHub repository secret
- B. Set the connection string as a plain environment variable in the job
- C. Grant the pipeline service principal Owner on the subscription
- D. Authenticate the workflow with workload identity federation and no stored secret

### 12. A workflow must not deploy to production until a named approver has reviewed the run. What should be configured?

Domain: Design and implement an MLOps infrastructure

- A. Fan the tests out across a matrix of dependency versions
- B. Store a service principal client secret as a GitHub repository secret
- C. Use GitHub environment protection rules to gate the production deploy job
- D. Run the pipeline from a GitHub Actions workflow on merge to main

### 13. A regulator requires that training data traffic never leave the virtual network. What must be configured?

Domain: Design and implement an MLOps infrastructure

- A. Place a private endpoint on the workspace and its storage
- B. Reference the storage path with the account key inline in the job YAML
- C. Set the connection string as a plain environment variable in the job
- D. Keep public network access enabled so notebooks connect easily

### 14. A new environment must separate its assets and reference storage without embedding credentials. Which two steps apply? Select two.

Domain: Design and implement an MLOps infrastructure

- A. Attach a GPU cluster with four always-on nodes
- B. Create the workspace in the portal and record the steps in a wiki
- C. Reference the storage path with the account key inline in the job YAML
- D. Create a separate Azure Machine Learning workspace per environment
- E. Register a datastore that points at the storage account

### 15. A team is bootstrapping a workspace from code for the first time. Which sequence is correct?

Domain: Design and implement an MLOps infrastructure

- A. Authenticate the pipeline → run a smoke job → define the workspace in Bicep → deploy the module
- B. Run a smoke job against the workspace → deploy the module → authenticate the pipeline → define the workspace in Bicep
- C. Define the workspace in a Bicep module → authenticate the pipeline with workload identity federation → deploy the module to the environment → run a smoke job against the deployed workspace
- D. Deploy the module → define the workspace in Bicep → run a smoke job → authenticate the pipeline

### 16. A preprocessing step fails and the team must rerun only that step, reusing the outputs already produced. What should the workflow be?

Domain: Implement machine learning model lifecycle and operations

- A. Run the whole workflow as a single script job
- B. Create the workspace in the portal and record the steps in a wiki
- C. Define the steps as a pipeline job with explicit inputs and outputs
- D. Run the job from a compute instance notebook

### 17. A workflow is a single bash script that trains, evaluates, and deploys, and nobody can tell which stage failed. What should replace it?

Domain: Implement machine learning model lifecycle and operations

- A. Define the steps as a pipeline job with explicit inputs and outputs
- B. Run the job from a compute instance notebook
- C. Assign the work to a person instead of investigating the failure
- D. Run the whole workflow as a single script job

### 18. A team needs to find a learning rate and batch size combination without trying every pair. What should be used?

Domain: Implement machine learning model lifecycle and operations

- A. Run the job from a compute instance notebook
- B. Use automated ML to establish the tabular baseline
- C. Run a sweep job over a searched hyperparameter space
- D. Run a full grid sweep over every combination

### 19. Thirty combinations were run and the bill exceeded the monthly training budget for one experiment. What was the mistake?

Domain: Implement machine learning model lifecycle and operations

- A. Run a sweep job over a searched hyperparameter space
- B. Increase the model size until the answers improve
- C. Run a full grid sweep over every combination
- D. Retrain the model on the newer data

### 20. A tabular churn problem needs a credible baseline within a day before the team invests in custom modelling. What fits?

Domain: Implement machine learning model lifecycle and operations

- A. Use automated ML to establish the tabular baseline
- B. Run the whole workflow as a single script job
- C. Run the job from a compute instance notebook
- D. Run a sweep job over a searched hyperparameter space

### 21. Two experiments produced 0.81 and 0.84 AUC and nobody can confirm which preprocessing each used. What should have been enabled?

Domain: Implement machine learning model lifecycle and operations

- A. Print the metrics to the job log and read them from the console
- B. Enable MLflow tracking so runs log to the workspace
- C. Run the job from a compute instance notebook
- D. Create the workspace in the portal and record the steps in a wiki

### 22. Runs are logged locally on each engineer's machine and never appear in the workspace experiment list. What is misconfigured?

Domain: Implement machine learning model lifecycle and operations

- A. Print the metrics to the job log and read them from the console
- B. Run the job from a compute instance notebook
- C. Disable request logging to reduce storage cost
- D. Point the MLflow tracking URI at the workspace endpoint

### 23. Four hundred runs share one list and the team cannot compare the three preprocessing variants. What should be used?

Domain: Implement machine learning model lifecycle and operations

- A. Run the job from a compute instance notebook
- B. Enable MLflow tracking so runs log to the workspace
- C. Group the trials under a named experiment
- D. Disable request logging to reduce storage cost

### 24. A registration silently changed what production served because the deployment resolved whichever version was newest. What should the deployment reference?

Domain: Implement machine learning model lifecycle and operations

- A. Overwrite the existing model version instead of registering a new one
- B. Register each candidate with a version and deploy one explicit version
- C. Deploy straight to production to save a day
- D. Register the model and always deploy whichever version is latest

### 25. An audit asks which data asset and commit produced the model currently in production. What should be attached at registration?

Domain: Implement machine learning model lifecycle and operations

- A. Attach a description, metrics, and intended use to the model version
- B. Disable request logging to reduce storage cost
- C. Print the metrics to the job log and read them from the console
- D. Tag the registered model with the data asset and commit it came from

### 26. A reviewer must decide whether a candidate is fit for promotion before anyone looks at it. What should the version carry?

Domain: Implement machine learning model lifecycle and operations

- A. Register the model and always deploy whichever version is latest
- B. Attach a description, metrics, and intended use to the model version
- C. Accept the behaviour because the aggregate score still looks healthy
- D. Tag the registered model with the data asset and commit it came from

### 27. An application needs a synchronous answer within 200 milliseconds for individual requests. What should be deployed?

Domain: Implement machine learning model lifecycle and operations

- A. Send the overnight file through the online endpoint request by request
- B. Deploy to a managed online endpoint with an explicit model version
- C. Run the job from a compute instance notebook
- D. Deploy a batch endpoint for the overnight scoring job

### 28. Every model version currently requires a container rebuild before it can be promoted. What should change?

Domain: Implement machine learning model lifecycle and operations

- A. Mount the model artifact rather than baking it into the image
- B. Replace the production deployment in a single step
- C. Bake the model weights into the container image
- D. Overwrite the existing model version instead of registering a new one

### 29. A container starts, receives traffic before it finishes loading the model, and returns errors for two minutes. What is missing?

Domain: Implement machine learning model lifecycle and operations

- A. Monitor only the accuracy reported at deployment time
- B. Pin a fixed instance count for a spiky workload
- C. Configure liveness and readiness probes on the deployment
- D. Deploy without probes and rely on the platform health check

### 30. Nine hundred thousand records must be scored inside an overnight window. What should be deployed?

Domain: Implement machine learning model lifecycle and operations

- A. Deploy a batch endpoint for the overnight scoring job
- B. Deploy to a managed online endpoint with an explicit model version
- C. Run the job from a compute instance notebook
- D. Send the overnight file through the online endpoint request by request

### 31. A new version must reach a small share of requests so its error rate can be measured before wider release. What should be configured?

Domain: Implement machine learning model lifecycle and operations

- A. Keep the previous deployment in place so traffic can be moved back
- B. Split endpoint traffic 10/90 so the new deployment receives a canary share
- C. Replace the production deployment in a single step
- D. Deploy straight to production to save a day

### 32. A release must be reversible within five minutes without a rebuild. What should be in place?

Domain: Implement machine learning model lifecycle and operations

- A. Bake the model weights into the container image
- B. Overwrite the existing model version instead of registering a new one
- C. Replace the production deployment in a single step
- D. Keep the previous deployment in place so traffic can be moved back

### 33. A workload peaks at 4,000 requests a second for two hours and idles for sixteen. What should be configured?

Domain: Implement machine learning model lifecycle and operations

- A. Pin a fixed instance count for a spiky workload
- B. Set autoscale rules on the deployment with a deliberate minimum instance count
- C. Send the overnight file through the online endpoint request by request
- D. Deploy without probes and rely on the platform health check

### 34. Input distributions have shifted since a line was retooled, but nobody knows because only deployment-time accuracy is reported. What should be enabled?

Domain: Implement machine learning model lifecycle and operations

- A. Monitor only the accuracy reported at deployment time
- B. Retrain the model on the newer data
- C. Accept the behaviour because the aggregate score still looks healthy
- D. Enable data drift monitoring against the training baseline

### 35. A drift report is produced weekly and nobody notices when it crosses a threshold. What is missing?

Domain: Implement machine learning model lifecycle and operations

- A. Disable request logging to reduce storage cost
- B. Assign the work to a person instead of investigating the failure
- C. Create an alert rule on the drift and latency metrics
- D. Monitor only the accuracy reported at deployment time

### 36. A team wants runs that can be compared months later and that include the trained artifact. Which two practices apply? Select two.

Domain: Implement machine learning model lifecycle and operations

- A. Enable MLflow tracking so runs log to the workspace
- B. Disable request logging to reduce storage cost
- C. Print the metrics to the job log and read them from the console
- D. Log metrics and the model artifact explicitly in the training script
- E. Assign the work to a person instead of investigating the failure

### 37. An endpoint must handle bursts and must not receive traffic before the model is loaded. Which two configurations apply? Select two.

Domain: Implement machine learning model lifecycle and operations

- A. Pin a fixed instance count for a spiky workload
- B. Set autoscale rules on the deployment with a deliberate minimum instance count
- C. Configure liveness and readiness probes on the deployment
- D. Deploy without probes and rely on the platform health check
- E. Send the overnight file through the online endpoint request by request

### 38. A candidate model must reach production with a measured gate. Which sequence is correct?

Domain: Implement machine learning model lifecycle and operations

- A. Train the candidate → evaluate against the gate → register the model version → deploy at a canary traffic share → shift all traffic after the metrics hold
- B. Evaluate against the gate → train the candidate → shift all traffic → register the model version
- C. Deploy at a canary traffic share → train the candidate → register the model version → evaluate against the gate
- D. Register the model version → train the candidate → evaluate against the gate → shift all traffic

### 39. A team must release a version while keeping a fast rollback available. Which sequence is correct?

Domain: Implement machine learning model lifecycle and operations

- A. Deploy the new version to a second deployment → send a small traffic share to it → compare error rate and latency with the incumbent → move all traffic back if the metrics regress
- B. Compare error rate and latency → deploy the new version → send a small traffic share → replace the incumbent
- C. Replace the incumbent deployment → compare error rate and latency → deploy the new version to a second deployment → send traffic to it
- D. Send all traffic to the new deployment → deploy the new version → compare metrics → move traffic back

### 40. Four teams share one project and one model connection, and a change by one team degraded another's latency. What should be created per team?

Domain: Design and implement a GenAIOps infrastructure

- A. Use one workspace for development, test, and production
- B. Give every team one project and one shared connection
- C. Create the workspace in the portal and record the steps in a wiki
- D. Create a Foundry hub and a project per team

### 41. A chat workload has run at a steady 2 million tokens an hour for three months and cost is now material. What should be adopted?

Domain: Design and implement a GenAIOps infrastructure

- A. Start on pay-as-you-go while the volume is still unknown
- B. Reserve provisioned throughput for the steady high-volume workload
- C. Pin a fixed instance count for a spiky workload
- D. Use the largest model for every request

### 42. An assistant serves the public and the safety team requires harm thresholds applied to prompts and completions. What should be configured?

Domain: Design and implement a GenAIOps infrastructure

- A. Evaluate toxicity against the threshold the audience requires
- B. Run adversarial jailbreak and prompt-injection cases before release
- C. Accept the behaviour because the aggregate score still looks healthy
- D. Apply a content filter policy appropriate to the audience

### 43. A flow has eight steps in one Python file and the team cannot test any step alone. What should the flow be authored as?

Domain: Design and implement a GenAIOps infrastructure

- A. Run the whole workflow as a single script job
- B. Run the job from a compute instance notebook
- C. Author the flow as a directed acyclic graph with typed inputs and outputs
- D. Run the flow as a batch job over the evaluation dataset

### 44. Two prompt strategies must be compared without maintaining parallel forks of the flow. What should be used?

Domain: Design and implement a GenAIOps infrastructure

- A. Hardcode the model family name inside the flow
- B. Create a variant to compare two prompt strategies side by side
- C. Author the flow as a directed acyclic graph with typed inputs and outputs
- D. Rewrite the prompt and deploy it immediately

### 45. A prompt flow needs a model credential that is not stored in the flow file. Where should it live?

Domain: Design and implement a GenAIOps infrastructure

- A. Set the connection string as a plain environment variable in the job
- B. Print the metrics to the job log and read them from the console
- C. Store the model credential as a project connection
- D. Paste the API key into a Python node inside the flow

### 46. A key was pasted into a Python node and has now appeared in a pull request diff. What was the defect?

Domain: Design and implement a GenAIOps infrastructure

- A. Store the model credential as a project connection
- B. Set the connection string as a plain environment variable in the job
- C. Paste the API key into a Python node inside the flow
- D. Reference the storage path with the account key inline in the job YAML

### 47. An assistant must answer from documents that change weekly and cite the current revision. What should be used?

Domain: Design and implement a GenAIOps infrastructure

- A. Increase the model size until the answers improve
- B. Fine-tune the model on the document set instead of retrieving
- C. Index every document the organization holds
- D. Index the documents in Azure AI Search and query the index from the flow

### 48. Retrieval misses product codes such as XJ-4471 even though the surrounding text matches. What should be used?

Domain: Design and implement a GenAIOps infrastructure

- A. Use hybrid search with semantic ranking
- B. Use vector search alone with no keyword component
- C. Increase the model size until the answers improve
- D. Fine-tune the model on the document set instead of retrieving

### 49. Answers cite the correct document but the wrong section of a 40-page policy. What should be changed?

Domain: Design and implement a GenAIOps infrastructure

- A. Raise retrieval depth to the maximum for safety
- B. Index each document as one large chunk
- C. Index every document the organization holds
- D. Chunk documents by section with a small overlap

### 50. The knowledge base changes every weekday and the assistant answers from four-month-old content. What should be configured?

Domain: Design and implement a GenAIOps infrastructure

- A. Index every document the organization holds
- B. Rebuild the index on a schedule after the source content changes
- C. Chunk documents by section with a small overlap
- D. Retrain the model on the newer data

### 51. A prompt change must be reviewable and revertible like any other code change. Where should the prompt live?

Domain: Design and implement a GenAIOps infrastructure

- A. Paste the API key into a Python node inside the flow
- B. Keep the prompt in its own file under version control
- C. Create a variant to compare two prompt strategies side by side
- D. Rewrite the prompt and deploy it immediately

### 52. A prompt edit reached production and reduced answer quality for a day. What was missing?

Domain: Design and implement a GenAIOps infrastructure

- A. Rewrite the prompt and deploy it immediately
- B. Run the evaluation in continuous integration before the flow is promoted
- C. Deploy straight to production to save a day
- D. Assign the work to a person instead of investigating the failure

### 53. An agent can reach a trade-execution stub that the workflow should never call. What should be changed?

Domain: Design and implement a GenAIOps infrastructure

- A. Index every document the organization holds
- B. Increase the model size until the answers improve
- C. Expose every available tool so the agent can choose freely
- D. Register a scoped tool list for the agent

### 54. A support agent carried one customer's facts into another customer's conversation. What should be changed?

Domain: Design and implement a GenAIOps infrastructure

- A. Expose every available tool so the agent can choose freely
- B. Bound the agent memory to the current session
- C. Pass typed state between agent steps
- D. Index every document the organization holds

### 55. A platform team must isolate team assets and keep flows stable when models are replaced. Which two practices apply? Select two.

Domain: Design and implement a GenAIOps infrastructure

- A. Reference the deployment name from the flow rather than the model family name
- B. Give every team one project and one shared connection
- C. Hardcode the model family name inside the flow
- D. Create a Foundry hub and a project per team
- E. Paste the API key into a Python node inside the flow

### 56. An assistant must ground on current documents and must not return content a user cannot access. Which two controls apply? Select two.

Domain: Design and implement a GenAIOps infrastructure

- A. Index the documents in Azure AI Search and query the index from the flow
- B. Fine-tune the model on the document set instead of retrieving
- C. Index every document the organization holds
- D. Keep public network access enabled so notebooks connect easily
- E. Set document-level access in the index so retrieval respects entitlements

### 57. A prompt change must be reviewable and must not reach traffic unevaluated. Which two practices apply? Select two.

Domain: Design and implement a GenAIOps infrastructure

- A. Rewrite the prompt and deploy it immediately
- B. Run the evaluation in continuous integration before the flow is promoted
- C. Deploy straight to production to save a day
- D. Paste the API key into a Python node inside the flow
- E. Keep the prompt in its own file under version control

### 58. A team is building a grounded flow from source documents for the first time. Which sequence is correct?

Domain: Design and implement a GenAIOps infrastructure

- A. Chunk and embed the documents → evaluate retrieval → create the search index → curate the documents
- B. Bind the index to the flow → create the search index → curate the documents → chunk and embed them
- C. Create the search index → curate the source documents → evaluate retrieval → chunk and embed them
- D. Curate the source documents → chunk and embed them → create the search index → bind the index to the flow → evaluate retrieval and groundedness

### 59. A flow needs access to several data sources without secrets. Which sequence is correct?

Domain: Design and implement a GenAIOps infrastructure

- A. Inventory the data sources the flow needs → assign the project a managed identity → grant the identity the narrowest role on each source → verify a grounded answer returns only permitted content
- B. Verify a grounded answer → assign the identity → grant the role → inventory the sources
- C. Assign the identity → verify the answer → inventory the sources → grant the role
- D. Grant the identity Owner on each source → inventory the data sources → verify the answer → assign a managed identity

### 60. A team needs an evaluation set that reflects what real users actually ask. What should it be built from?

Domain: Implement generative AI quality assurance and observability

- A. Build the evaluation dataset from real queries with graded answers
- B. Accept the behaviour because the aggregate score still looks healthy
- C. Generate the evaluation set from the prompt itself
- D. Assign the work to a person instead of investigating the failure

### 61. Grading must scale to thousands of cases without losing credibility. What should be built?

Domain: Implement generative AI quality assurance and observability

- A. Generate the evaluation set from the prompt itself
- B. Assign the work to a person instead of investigating the failure
- C. Use an LLM judge with a rubric, calibrated against human grades
- D. Rely on the LLM judge without checking it against human grades

### 62. An answer is fluent and on topic but states a policy clause that appears nowhere in the retrieved passages. Which metric catches this?

Domain: Implement generative AI quality assurance and observability

- A. Score groundedness against the retrieved passages
- B. Score relevance of the answer to the question asked
- C. Score coherence for logical structure
- D. Score fluency for readability and language quality

### 63. An answer is fully supported by a passage but does not answer the question that was asked. Which metric catches this?

Domain: Implement generative AI quality assurance and observability

- A. Score similarity against a reference answer
- B. Score fluency for readability and language quality
- C. Score relevance of the answer to the question asked
- D. Score groundedness against the retrieved passages

### 64. An answer is grammatically excellent and factually invented. Which metric would still score it well?

Domain: Implement generative AI quality assurance and observability

- A. Score coherence for logical structure
- B. Score relevance of the answer to the question asked
- C. Score groundedness against the retrieved passages
- D. Score fluency for readability and language quality

### 65. An assistant may serve the public and must be measured against a harmful-output standard. What should be evaluated?

Domain: Implement generative AI quality assurance and observability

- A. Score relevance of the answer to the question asked
- B. Score fluency for readability and language quality
- C. Evaluate toxicity against the threshold the audience requires
- D. Score similarity against a reference answer

### 66. A red-team exercise tries to make the assistant ignore its system prompt. What is being tested?

Domain: Implement generative AI quality assurance and observability

- A. Run adversarial jailbreak and prompt-injection cases before release
- B. Score fluency for readability and language quality
- C. Evaluate toxicity against the threshold the audience requires
- D. Accept the behaviour because the aggregate score still looks healthy

### 67. A scanned supplier document contains text telling the assistant to disregard its rules. What is this attack called?

Domain: Implement generative AI quality assurance and observability

- A. Disable request logging to reduce storage cost
- B. Run adversarial jailbreak and prompt-injection cases before release
- C. Test indirect injection through retrieved documents
- D. Evaluate toxicity against the threshold the audience requires

### 68. An answer is wrong and nobody knows whether retrieval or generation caused it. What should be enabled?

Domain: Implement generative AI quality assurance and observability

- A. Enable distributed tracing and log the retrieval and model spans
- B. Disable request logging to reduce storage cost
- C. Log prompts and completions against the trace, within data policy
- D. Rely on the LLM judge without checking it against human grades

### 69. Users are downvoting answers in a pattern the evaluation set does not contain. What should be built?

Domain: Implement generative AI quality assurance and observability

- A. Run continuous evaluation on sampled production traffic
- B. Run the evaluation in continuous integration before the flow is promoted
- C. Rely on the LLM judge without checking it against human grades
- D. Capture user feedback and review a sample of rated conversations weekly

### 70. An evaluation set must be credible to a regulator. Which two properties matter? Select two.

Domain: Implement generative AI quality assurance and observability

- A. Generate the evaluation set from the prompt itself
- B. Accept the behaviour because the aggregate score still looks healthy
- C. Use a few hundred representative cases rather than a dozen
- D. Build the evaluation dataset from real queries with graded answers
- E. Assign the work to a person instead of investigating the failure

### 71. An assistant retrieves external documents and must resist instruction override. Which two test types apply? Select two.

Domain: Implement generative AI quality assurance and observability

- A. Run adversarial jailbreak and prompt-injection cases before release
- B. Score fluency for readability and language quality
- C. Evaluate toxicity against the threshold the audience requires
- D. Test indirect injection through retrieved documents
- E. Disable request logging to reduce storage cost

### 72. A wrong answer must be diagnosable and reproducible. Which two practices apply? Select two.

Domain: Implement generative AI quality assurance and observability

- A. Enable distributed tracing and log the retrieval and model spans
- B. Log prompts and completions against the trace, within data policy
- C. Rely on the LLM judge without checking it against human grades
- D. Assign the work to a person instead of investigating the failure
- E. Disable request logging to reduce storage cost

### 73. A production answer was wrong and the team must find the cause. Which sequence is correct?

Domain: Implement generative AI quality assurance and observability

- A. Add the case to the evaluation set → inspect the completion → open the failing request trace → inspect the retrieval span
- B. Retrain the model → open the trace → inspect the retrieval span → add the case to the evaluation set
- C. Open the failing request trace → inspect the retrieval span for the passages returned → inspect the prompt and completion for that call → add the case to the evaluation set
- D. Inspect the retrieval span → retrain the model → open the trace → add the case to the evaluation set

### 74. Finance cannot attribute monthly model spend to a workload or a team. What should be introduced first?

Domain: Optimize generative AI systems and model performance

- A. Cache identical requests and reuse the completion
- B. Measure tokens per request and set a budget per endpoint
- C. Accept the behaviour because the aggregate score still looks healthy
- D. Use the largest model for every request

### 75. A portal sends the same 400 questions thousands of times a day with identical wording. What should be added?

Domain: Optimize generative AI systems and model performance

- A. Compress the system prompt and remove redundant instructions
- B. Cache identical requests and reuse the completion
- C. Add a router that classifies the request and selects a model
- D. Set a time-to-live on the cache

### 76. A cached answer still quotes a policy that was updated three weeks ago. What should be configured?

Domain: Optimize generative AI systems and model performance

- A. Accept the behaviour because the aggregate score still looks healthy
- B. Disable request logging to reduce storage cost
- C. Set a time-to-live on the cache
- D. Cache identical requests and reuse the completion

### 77. Nine of ten requests are simple field lookups that a small model handles well. What should be done?

Domain: Optimize generative AI systems and model performance

- A. Route simple requests to a smaller model
- B. Increase the model size until the answers improve
- C. Retrain the model on the newer data
- D. Use the largest model for every request

### 78. A workload mixes short classification requests with long analytical ones and needs one entry point. What should be added?

Domain: Optimize generative AI systems and model performance

- A. Route simple requests to a smaller model
- B. Use the largest model for every request
- C. Cache identical requests and reuse the completion
- D. Add a router that classifies the request and selects a model

### 79. Users complain that nothing appears for eight seconds even though the full answer arrives in ten. What should be changed?

Domain: Optimize generative AI systems and model performance

- A. Set a request timeout with a bounded retry and backoff
- B. Move non-urgent generation into a batch run
- C. Stream the response so the first token arrives sooner
- D. Cache identical requests and reuse the completion

### 80. Twelve passages are retrieved per answer, most are irrelevant, and token cost is high. What should change?

Domain: Optimize generative AI systems and model performance

- A. Increase the model size until the answers improve
- B. Retrieve fewer but better-ranked passages
- C. Index every document the organization holds
- D. Raise retrieval depth to the maximum for safety

### 81. A 6,000-token system prompt is sent on every request and much of it repeats the same instruction. What should be done?

Domain: Optimize generative AI systems and model performance

- A. Compress the system prompt and remove redundant instructions
- B. Raise retrieval depth to the maximum for safety
- C. Increase the model size until the answers improve
- D. Cache identical requests and reuse the completion

### 82. A cost optimization reduced tokens by 40 percent and no quality check was run. What must happen before release?

Domain: Optimize generative AI systems and model performance

- A. Re-run the evaluation after the cost optimization
- B. Rewrite the prompt and deploy it immediately
- C. Accept the behaviour because the aggregate score still looks healthy
- D. Ship the optimization and watch the support queue

### 83. Traffic has been steady for six months and cost per token is now the largest line in the budget. What should be done?

Domain: Optimize generative AI systems and model performance

- A. Cache identical requests and reuse the completion
- B. Move steady traffic to provisioned throughput
- C. Start on pay-as-you-go while the volume is still unknown
- D. Increase the model size until the answers improve

### 84. A team must attribute spend and remove repeated work. Which two actions apply? Select two.

Domain: Optimize generative AI systems and model performance

- A. Set a time-to-live on the cache
- B. Accept the behaviour because the aggregate score still looks healthy
- C. Use the largest model for every request
- D. Measure tokens per request and set a budget per endpoint
- E. Cache identical requests and reuse the completion

### 85. A mixed workload must cost less without lowering quality on hard cases. Which two actions apply? Select two.

Domain: Optimize generative AI systems and model performance

- A. Add a router that classifies the request and selects a model
- B. Route simple requests to a smaller model
- C. Cache identical requests and reuse the completion
- D. Retrain the model on the newer data
- E. Use the largest model for every request

### 86. A team must reduce model spend without losing quality. Which sequence is correct?

Domain: Optimize generative AI systems and model performance

- A. Find the largest driver → re-run the evaluation → measure the tokens → apply the optimization
- B. Measure cost and tokens per request → find the largest driver in the breakdown → apply the matching optimization → re-run the evaluation to confirm quality held
- C. Apply the optimization → measure the tokens per request → re-run the evaluation → find the largest driver
- D. Re-run the evaluation → apply the optimization → measure the tokens → find the largest driver

### 87. A team must cut both the retrieved context and the standing instruction without losing relevance. Which two changes fit? Select two.

Domain: Optimize generative AI systems and model performance

- A. Compress the system prompt and remove redundant instructions
- B. Raise retrieval depth to the maximum for safety
- C. Retrieve fewer but better-ranked passages
- D. Increase the model size until the answers improve
- E. Cache identical requests and reuse the completion

### 88. A platform team must choose between pay-as-you-go and provisioned throughput for a growing assistant. Which sequence is correct?

Domain: Optimize generative AI systems and model performance

- A. Load test the configuration → reserve provisioned throughput → forecast the load → measure the request rate
- B. Forecast the peak load → reserve provisioned throughput → measure the current rate → load test
- C. Reserve provisioned throughput → measure the request rate → forecast the load → load test the configuration
- D. Measure the current request rate and token volume → forecast the peak and steady load → compare pay-as-you-go cost with provisioned throughput at that volume → load test the chosen configuration

---

## Case study — Contoso Foundry

Contoso runs a customer-support assistant on Microsoft Foundry for 1,200 agents across three regions. The assistant retrieves from a 40,000-document knowledge base that the content team updates every weekday, and the team has noticed answers quoting a policy that was withdrawn four months ago. Two teams share a single Foundry project and the same model connection, and last month one team changed a deployment setting that silently degraded the other team's latency. Monthly spend has tripled since launch and nobody can attribute it to a feature or a team.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 89. Answers quote a policy withdrawn four months ago. Which two changes address it? Select two.

Domain: Design and implement a GenAIOps infrastructure

- A. Retrain the model on the newer data
- B. Index each document as one large chunk
- C. Index every document the organization holds
- D. Rebuild the index on a schedule after the source content changes
- E. Chunk documents by section with a small overlap

### 90. Retrieval misses exact policy identifiers in a 40,000-document base. What should be used?

Domain: Design and implement a GenAIOps infrastructure

- A. Use hybrid search with semantic ranking
- B. Increase the model size until the answers improve
- C. Fine-tune the model on the document set instead of retrieving
- D. Use vector search alone with no keyword component

### 91. Two teams share one project and one connection, and one team's change degraded the other. What should be introduced?

Domain: Design and implement a GenAIOps infrastructure

- A. Use one workspace for development, test, and production
- B. Give every team one project and one shared connection
- C. Create the workspace in the portal and record the steps in a wiki
- D. Create a Foundry hub and a project per team

---

## Case study — Fabrikam Retail AI

Fabrikam Retail runs demand forecasting for 300 stores from three years of transaction data and wants the training pipeline reproducible. The data team consists of four engineers who currently create workspaces in the portal, name resources by hand, and store the storage account key in the job YAML. A new regulatory requirement says the training data must stay on the private network and every production model must be traceable to the exact data asset and commit that produced it. The forecasting model is retrained weekly and currently takes two days of manual effort per release.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 92. The forecasting pipeline must be reproducible. What should be registered so a past model can be rebuilt?

Domain: Implement generative AI quality assurance and observability

- A. Build the evaluation dataset from real queries with graded answers
- B. Generate the evaluation set from the prompt itself
- C. Accept the behaviour because the aggregate score still looks healthy
- D. Assign the work to a person instead of investigating the failure

### 93. The workspace must be recreated identically in a second region with different names. Which two practices apply? Select two.

Domain: Design and implement an MLOps infrastructure

- A. Pass environment values through a Bicep parameter file per stage
- B. Export an ARM template from the portal after building it by hand
- C. Define the workspace in a Bicep module deployed per environment
- D. Create the workspace in the portal and record the steps in a wiki
- E. Rebuild the environment by hand from the notes in the ticket

### 94. Four engineers deploy from a workflow and no long-lived secret may exist. What should authenticate the workflow?

Domain: Design and implement an MLOps infrastructure

- A. Set the connection string as a plain environment variable in the job
- B. Grant the pipeline service principal Owner on the subscription
- C. Authenticate the workflow with workload identity federation and no stored secret
- D. Store a service principal client secret as a GitHub repository secret

---

## Case study — Meridian Bank

Meridian Bank deploys a document-extraction model for mortgage applications and must satisfy an internal audit that asks how each model version was approved. The bank has separate development, test, and production subscriptions, and a single service principal with Contributor on all three is used by every pipeline. Audit found that a model version was overwritten in the registry last year, so the artifact that produced an approved decision can no longer be reproduced. The bank also wants every deployment to be reversible within five minutes.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 95. Audit must identify the exact artifact that produced an approved decision. What should the registry provide?

Domain: Design and implement an MLOps infrastructure

- A. Print the metrics to the job log and read them from the console
- B. Overwrite the existing model version instead of registering a new one
- C. Register each candidate with a version and deploy one explicit version
- D. Register the model and always deploy whichever version is latest

### 96. A reviewer must assess a candidate before promotion. Which two artifacts help? Select two.

Domain: Implement machine learning model lifecycle and operations

- A. Accept the behaviour because the aggregate score still looks healthy
- B. Register the model and always deploy whichever version is latest
- C. Overwrite the existing model version instead of registering a new one
- D. Attach a description, metrics, and intended use to the model version
- E. Tag the registered model with the data asset and commit it came from

### 97. A deployment must be reversible within five minutes. What makes that possible?

Domain: Implement machine learning model lifecycle and operations

- A. Keep the previous deployment in place so traffic can be moved back
- B. Deploy straight to production to save a day
- C. Overwrite the existing model version instead of registering a new one
- D. Replace the production deployment in a single step

---

## Case study — Tailwind Logistics

Tailwind Logistics operates a route-optimization model that scores 900,000 shipments a night and a real-time ETA endpoint that answers 4,000 requests per second at peak. The nightly scoring job currently loops over the online endpoint one record at a time and takes nine hours, which no longer fits the overnight window. The ETA endpoint runs on a fixed instance count that is sized for the peak and sits idle for sixteen hours a day. Twice this quarter a new model version was promoted directly to production and had to be withdrawn the same evening.

The next 3 questions refer to it. Read the scenario once, then answer all 3; each item restates the constraint it tests and is scored individually.

### 98. Nine hundred thousand shipments must be scored overnight. What should be deployed?

Domain: Implement machine learning model lifecycle and operations

- A. Send the overnight file through the online endpoint request by request
- B. Run the job from a compute instance notebook
- C. Deploy to a managed online endpoint with an explicit model version
- D. Deploy a batch endpoint for the overnight scoring job

### 99. The ETA endpoint is sized for peak and idle for sixteen hours. What should be configured?

Domain: Implement machine learning model lifecycle and operations

- A. Send the overnight file through the online endpoint request by request
- B. Pin a fixed instance count for a spiky workload
- C. Set autoscale rules on the deployment with a deliberate minimum instance count
- D. Deploy without probes and rely on the platform health check

### 100. New versions were promoted straight to production twice. Which two controls prevent that? Select two.

Domain: Implement machine learning model lifecycle and operations

- A. Bake the model weights into the container image
- B. Split endpoint traffic 10/90 so the new deployment receives a canary share
- C. Replace the production deployment in a single step
- D. Overwrite the existing model version instead of registering a new one
- E. Keep the previous deployment in place so traffic can be moved back

---

## Answer key and explanations

### Question 1 — B

Answer: Create a separate Azure Machine Learning workspace per environment. A workspace is the boundary for registered assets and jobs, so a separate workspace per environment keeps development activity away from production models. A workspace is the top-level boundary for compute, datastores, jobs, and registered assets, so separating environments keeps development activity away from production assets. Local study-map skill 1.1 (Workspace, Compute, and Datastore Provisioning), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A workspace is the boundary for registered assets and jobs, so a separate workspace per environment keeps development activity away from production models.
- **B:** Correct. A workspace is the top-level boundary for compute, datastores, jobs, and registered assets, so separating environments keeps development activity away from production assets. In this case: A workspace is the boundary for registered assets and jobs, so a separate workspace per environment keeps development activity away from production models.
- **C:** Incorrect for this question. A shared workspace mixes assets and identities across environments, so a test job can register over the model production is serving. Why the correct answer wins: A workspace is the boundary for registered assets and jobs, so a separate workspace per environment keeps development activity away from production models.
- **D:** Incorrect for this question. Always-on GPU nodes bill continuously, including overnight and between experiments. Why the correct answer wins: A workspace is the boundary for registered assets and jobs, so a separate workspace per environment keeps development activity away from production models.

### Question 2 — A

Answer: Attach a GPU cluster with a minimum of zero nodes. A GPU cluster with a zero minimum scales to nothing when idle and is available when a training run starts. A GPU cluster with a zero minimum scales to nothing when idle, which suits intermittent training without paying for accelerators between runs. Local study-map skill 1.1 (Workspace, Compute, and Datastore Provisioning), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Correct. A GPU cluster with a zero minimum scales to nothing when idle, which suits intermittent training without paying for accelerators between runs. In this case: A GPU cluster with a zero minimum scales to nothing when idle and is available when a training run starts.
- **B:** Incorrect for this question. A CPU cluster is cheaper per core and sufficient for tabular preparation, which gains nothing from an accelerator. Why the correct answer wins: A GPU cluster with a zero minimum scales to nothing when idle and is available when a training run starts.
- **C:** Incorrect for this question. Always-on GPU nodes bill continuously, including overnight and between experiments. Why the correct answer wins: A GPU cluster with a zero minimum scales to nothing when idle and is available when a training run starts.
- **D:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A GPU cluster with a zero minimum scales to nothing when idle and is available when a training run starts.

### Question 3 — B

Answer: Build a versioned curated environment for the job. A versioned curated environment fixes the interpreter and package set, so the same job resolves the same dependencies later. A versioned environment pins the interpreter and packages, so the same job resolves the same dependencies months later. Local study-map skill 1.2 (Data Assets, Environments, and Component Reuse), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: A versioned curated environment fixes the interpreter and package set, so the same job resolves the same dependencies later.
- **B:** Correct. A versioned environment pins the interpreter and packages, so the same job resolves the same dependencies months later. In this case: A versioned curated environment fixes the interpreter and package set, so the same job resolves the same dependencies later.
- **C:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A versioned curated environment fixes the interpreter and package set, so the same job resolves the same dependencies later.
- **D:** Incorrect for this question. A floating tag resolves to a different image over time and silently breaks reproducibility. Why the correct answer wins: A versioned curated environment fixes the interpreter and package set, so the same job resolves the same dependencies later.

### Question 4 — A

Answer: Register the data as a versioned data asset. A versioned data asset records the exact input, which is what makes the training run reproducible after the fact. A versioned data asset records exactly which data a run used, which is what makes the model reproducible later. Local study-map skill 1.2 (Data Assets, Environments, and Component Reuse), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Correct. A versioned data asset records exactly which data a run used, which is what makes the model reproducible later. In this case: A versioned data asset records the exact input, which is what makes the training run reproducible after the fact.
- **B:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: A versioned data asset records the exact input, which is what makes the training run reproducible after the fact.
- **C:** Incorrect for this question. A datastore holds the connection and credential, so jobs reference data by name instead of an account key and physical path. Why the correct answer wins: A versioned data asset records the exact input, which is what makes the training run reproducible after the fact.
- **D:** Incorrect for this question. An inline key puts a credential in source control and ties the job to one physical path. Why the correct answer wins: A versioned data asset records the exact input, which is what makes the training run reproducible after the fact.

### Question 5 — B

Answer: Package the preparation step as a reusable component. A component gives the step a typed interface and one implementation, so four pipelines consume the same versioned logic. A component gives the step a typed interface, so it can be reused in other pipelines and tested alone. Local study-map skill 1.2 (Data Assets, Environments, and Component Reuse), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. A single script hides intermediate artifacts, so a failed stage cannot be rerun without repeating everything. Why the correct answer wins: A component gives the step a typed interface and one implementation, so four pipelines consume the same versioned logic.
- **B:** Correct. A component gives the step a typed interface, so it can be reused in other pipelines and tested alone. In this case: A component gives the step a typed interface and one implementation, so four pipelines consume the same versioned logic.
- **C:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A component gives the step a typed interface and one implementation, so four pipelines consume the same versioned logic.
- **D:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A component gives the step a typed interface and one implementation, so four pipelines consume the same versioned logic.

### Question 6 — A

Answer: Define the workspace in a Bicep module deployed per environment. A declarative Bicep module reproduces the environment exactly and is reviewable as code. Bicep gives a declarative, reviewable definition, so an environment can be recreated identically and configuration drift becomes visible. Local study-map skill 1.3 (Infrastructure as Code with Bicep), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Correct. Bicep gives a declarative, reviewable definition, so an environment can be recreated identically and configuration drift becomes visible. In this case: A declarative Bicep module reproduces the environment exactly and is reviewable as code.
- **B:** Incorrect for this question. A hand rebuild cannot be reproduced exactly and drifts from the definition the team believed it had. Why the correct answer wins: A declarative Bicep module reproduces the environment exactly and is reviewable as code.
- **C:** Incorrect for this question. Exporting captures whatever exists, including accidental settings, and starts the estate from an unreviewed hand-built state. Why the correct answer wins: A declarative Bicep module reproduces the environment exactly and is reviewable as code.
- **D:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A declarative Bicep module reproduces the environment exactly and is reviewable as code.

### Question 7 — B

Answer: Pass environment values through a Bicep parameter file per stage. A parameter file per environment keeps one module and varies only the values. A parameter file keeps one module per environment, so only the values differ and the shape stays identical. Local study-map skill 1.3 (Infrastructure as Code with Bicep), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Exporting captures whatever exists, including accidental settings, and starts the estate from an unreviewed hand-built state. Why the correct answer wins: A parameter file per environment keeps one module and varies only the values.
- **B:** Correct. A parameter file keeps one module per environment, so only the values differ and the shape stays identical. In this case: A parameter file per environment keeps one module and varies only the values.
- **C:** Incorrect for this question. A hand rebuild cannot be reproduced exactly and drifts from the definition the team believed it had. Why the correct answer wins: A parameter file per environment keeps one module and varies only the values.
- **D:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A parameter file per environment keeps one module and varies only the values.

### Question 8 — D

Answer: Deploy the module as a deployment stack so removed resources are cleaned up. A deployment stack tracks the resources it owns and can deny or remove changes made outside the template. A deployment stack tracks the resources it owns and can deny or delete changes made outside the template. Local study-map skill 1.3 (Infrastructure as Code with Bicep), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. A hand rebuild cannot be reproduced exactly and drifts from the definition the team believed it had. Why the correct answer wins: A deployment stack tracks the resources it owns and can deny or remove changes made outside the template.
- **B:** Incorrect for this question. Exporting captures whatever exists, including accidental settings, and starts the estate from an unreviewed hand-built state. Why the correct answer wins: A deployment stack tracks the resources it owns and can deny or remove changes made outside the template.
- **C:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A deployment stack tracks the resources it owns and can deny or remove changes made outside the template.
- **D:** Correct. A deployment stack tracks the resources it owns and can deny or delete changes made outside the template. In this case: A deployment stack tracks the resources it owns and can deny or remove changes made outside the template.

### Question 9 — D

Answer: Submit the job with az ml job create --file job.yaml. A declarative YAML job submitted through the CLI is repeatable and runs unchanged in continuous integration. A declarative YAML job submitted through the CLI is repeatable and runs unchanged in continuous integration. Local study-map skill 1.4 (Azure CLI and Declarative Job Automation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A declarative YAML job submitted through the CLI is repeatable and runs unchanged in continuous integration.
- **B:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A declarative YAML job submitted through the CLI is repeatable and runs unchanged in continuous integration.
- **C:** Incorrect for this question. Streaming attaches to a running job log, which is a debugging step rather than a way to create or promote an asset. Why the correct answer wins: A declarative YAML job submitted through the CLI is repeatable and runs unchanged in continuous integration.
- **D:** Correct. A declarative YAML job submitted through the CLI is repeatable and runs unchanged in continuous integration. In this case: A declarative YAML job submitted through the CLI is repeatable and runs unchanged in continuous integration.

### Question 10 — D

Answer: Stream the job with az ml job stream to inspect logs. Streaming attaches to the live job log, which is how a running failure is inspected. Streaming attaches to a running job log, which is a debugging step rather than a way to create or promote an asset. Local study-map skill 1.4 (Azure CLI and Declarative Job Automation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. A declarative YAML job submitted through the CLI is repeatable and runs unchanged in continuous integration. Why the correct answer wins: Streaming attaches to the live job log, which is how a running failure is inspected.
- **B:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: Streaming attaches to the live job log, which is how a running failure is inspected.
- **C:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: Streaming attaches to the live job log, which is how a running failure is inspected.
- **D:** Correct. Streaming attaches to a running job log, which is a debugging step rather than a way to create or promote an asset. In this case: Streaming attaches to the live job log, which is how a running failure is inspected.

### Question 11 — D

Answer: Authenticate the workflow with workload identity federation and no stored secret. Workload identity federation exchanges the workflow token for a credential, so no stored secret exists. Federated identity exchanges the workflow token for an Azure credential, so no long-lived secret exists to leak or rotate. Local study-map skill 1.5 (GitHub Actions CI/CD and Workload Identity Federation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. A stored client secret is long-lived and must be rotated; federation removes the secret entirely. Why the correct answer wins: Workload identity federation exchanges the workflow token for a credential, so no stored secret exists.
- **B:** Incorrect for this question. A plain environment variable appears in job definitions and logs, which exposes the secret. Why the correct answer wins: Workload identity federation exchanges the workflow token for a credential, so no stored secret exists.
- **C:** Incorrect for this question. Owner on the subscription lets a pipeline change any resource, so one bad commit can affect everything. Why the correct answer wins: Workload identity federation exchanges the workflow token for a credential, so no stored secret exists.
- **D:** Correct. Federated identity exchanges the workflow token for an Azure credential, so no long-lived secret exists to leak or rotate. In this case: Workload identity federation exchanges the workflow token for a credential, so no stored secret exists.

### Question 12 — C

Answer: Use GitHub environment protection rules to gate the production deploy job. A protected environment requires approval before the job runs. A protected environment requires approval before the job runs, which is the control that stops an unreviewed deployment. Local study-map skill 1.5 (GitHub Actions CI/CD and Workload Identity Federation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. A matrix runs the same tests across configurations in parallel, which catches dependency drift before release. Why the correct answer wins: A protected environment requires approval before the job runs.
- **B:** Incorrect for this question. A stored client secret is long-lived and must be rotated; federation removes the secret entirely. Why the correct answer wins: A protected environment requires approval before the job runs.
- **C:** Correct. A protected environment requires approval before the job runs, which is the control that stops an unreviewed deployment. In this case: A protected environment requires approval before the job runs.
- **D:** Incorrect for this question. A workflow triggered by a merge makes the build, test, and deploy steps reviewable, repeatable, and attributable to a commit. Why the correct answer wins: A protected environment requires approval before the job runs.

### Question 13 — A

Answer: Place a private endpoint on the workspace and its storage. A private endpoint removes public network access for the workspace and its storage. A private endpoint removes public network access, so traffic stays on the virtual network. Local study-map skill 1.7 (Network Isolation, Secrets, and Pipeline Identity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Correct. A private endpoint removes public network access, so traffic stays on the virtual network. In this case: A private endpoint removes public network access for the workspace and its storage.
- **B:** Incorrect for this question. An inline key puts a credential in source control and ties the job to one physical path. Why the correct answer wins: A private endpoint removes public network access for the workspace and its storage.
- **C:** Incorrect for this question. A plain environment variable appears in job definitions and logs, which exposes the secret. Why the correct answer wins: A private endpoint removes public network access for the workspace and its storage.
- **D:** Incorrect for this question. Public access broadens the attack surface and usually fails a regulated review. Why the correct answer wins: A private endpoint removes public network access for the workspace and its storage.

### Question 14 — D, E

Answers: Create a separate Azure Machine Learning workspace per environment; Register a datastore that points at the storage account. A dedicated workspace isolates assets, and a registered datastore holds the connection instead of a key in YAML. A workspace is the top-level boundary for compute, datastores, jobs, and registered assets, so separating environments keeps development activity away from production assets. A datastore holds the connection and credential, so jobs reference data by name instead of an account key and physical path. Local study-map skill 1.1 (Workspace, Compute, and Datastore Provisioning), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Always-on GPU nodes bill continuously, including overnight and between experiments. Why the correct answer wins: A dedicated workspace isolates assets, and a registered datastore holds the connection instead of a key in YAML.
- **B:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A dedicated workspace isolates assets, and a registered datastore holds the connection instead of a key in YAML.
- **C:** Incorrect for this question. An inline key puts a credential in source control and ties the job to one physical path. Why the correct answer wins: A dedicated workspace isolates assets, and a registered datastore holds the connection instead of a key in YAML.
- **D:** Correct. A workspace is the top-level boundary for compute, datastores, jobs, and registered assets, so separating environments keeps development activity away from production assets. In this case: A dedicated workspace isolates assets, and a registered datastore holds the connection instead of a key in YAML.
- **E:** Correct. A datastore holds the connection and credential, so jobs reference data by name instead of an account key and physical path. In this case: A dedicated workspace isolates assets, and a registered datastore holds the connection instead of a key in YAML.

### Question 15 — C

Answer: Define the workspace in a Bicep module → authenticate the pipeline with workload identity federation → deploy the module to the environment → run a smoke job against the deployed workspace. Definition comes first, then pipeline identity, then deployment, then a smoke job against what exists. Infrastructure is defined, then identity is established for the pipeline, then the environment exists, and only then can a job be submitted to it. Local study-map skill 1.4 (Azure CLI and Declarative Job Automation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Identity is established early, but the smoke job still precedes both the definition and the deployment. Why the correct answer wins: Definition comes first, then pipeline identity, then deployment, then a smoke job against what exists.
- **B:** Incorrect for this question. A job cannot run against infrastructure that has neither been defined nor deployed, and the pipeline has no identity yet. Why the correct answer wins: Definition comes first, then pipeline identity, then deployment, then a smoke job against what exists.
- **C:** Correct. Infrastructure is defined, then identity is established for the pipeline, then the environment exists, and only then can a job be submitted to it. In this case: Definition comes first, then pipeline identity, then deployment, then a smoke job against what exists.
- **D:** Incorrect for this question. The module is deployed before it is written, and authentication last means the pipeline could never have deployed anything. Why the correct answer wins: Definition comes first, then pipeline identity, then deployment, then a smoke job against what exists.

### Question 16 — C

Answer: Define the steps as a pipeline job with explicit inputs and outputs. A pipeline job records each step output, so a failed step can be retried without repeating the others. A pipeline job makes the dependency between steps explicit and records each output, which is what gives lineage. Local study-map skill 2.1 (Training Pipeline Authoring and Orchestration), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. A single script hides intermediate artifacts, so a failed stage cannot be rerun without repeating everything. Why the correct answer wins: A pipeline job records each step output, so a failed step can be retried without repeating the others.
- **B:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A pipeline job records each step output, so a failed step can be retried without repeating the others.
- **C:** Correct. A pipeline job makes the dependency between steps explicit and records each output, which is what gives lineage. In this case: A pipeline job records each step output, so a failed step can be retried without repeating the others.
- **D:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A pipeline job records each step output, so a failed step can be retried without repeating the others.

### Question 17 — D

Answer: Run the whole workflow as a single script job. Separate steps in a pipeline make the failing stage visible and its inputs explicit. A single script hides intermediate artifacts, so a failed stage cannot be rerun without repeating everything. Local study-map skill 2.1 (Training Pipeline Authoring and Orchestration), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. A pipeline job makes the dependency between steps explicit and records each output, which is what gives lineage. Why the correct answer wins: Separate steps in a pipeline make the failing stage visible and its inputs explicit.
- **B:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: Separate steps in a pipeline make the failing stage visible and its inputs explicit.
- **C:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: Separate steps in a pipeline make the failing stage visible and its inputs explicit.
- **D:** Correct. A single script hides intermediate artifacts, so a failed stage cannot be rerun without repeating everything. In this case: Separate steps in a pipeline make the failing stage visible and its inputs explicit.

### Question 18 — C

Answer: Run a sweep job over a searched hyperparameter space. A sweep samples the search space and records each trial, which finds a good region without exhaustive coverage. A sweep samples the search space and records every trial, which finds an optimum systematically rather than by guesswork. Local study-map skill 2.2 (Job Configuration, Compute Targets, and Sweeps), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A sweep samples the search space and records each trial, which finds a good region without exhaustive coverage.
- **B:** Incorrect for this question. Automated ML tests preprocessing and algorithm combinations quickly, which is a reasonable baseline for tabular data. Why the correct answer wins: A sweep samples the search space and records each trial, which finds a good region without exhaustive coverage.
- **C:** Correct. A sweep samples the search space and records every trial, which finds an optimum systematically rather than by guesswork. In this case: A sweep samples the search space and records each trial, which finds a good region without exhaustive coverage.
- **D:** Incorrect for this question. A full grid multiplies cost by the number of combinations and is rarely needed once the promising region is known. Why the correct answer wins: A sweep samples the search space and records each trial, which finds a good region without exhaustive coverage.

### Question 19 — C

Answer: Run a full grid sweep over every combination. A full grid multiplies cost by the number of combinations when a sampled sweep would have found the region. A full grid multiplies cost by the number of combinations and is rarely needed once the promising region is known. Local study-map skill 2.2 (Job Configuration, Compute Targets, and Sweeps), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. A sweep samples the search space and records every trial, which finds an optimum systematically rather than by guesswork. Why the correct answer wins: A full grid multiplies cost by the number of combinations when a sampled sweep would have found the region.
- **B:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: A full grid multiplies cost by the number of combinations when a sampled sweep would have found the region.
- **C:** Correct. A full grid multiplies cost by the number of combinations and is rarely needed once the promising region is known. In this case: A full grid multiplies cost by the number of combinations when a sampled sweep would have found the region.
- **D:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: A full grid multiplies cost by the number of combinations when a sampled sweep would have found the region.

### Question 20 — A

Answer: Use automated ML to establish the tabular baseline. Automated ML tests preprocessing and algorithm combinations quickly, which is a reasonable baseline. Automated ML tests preprocessing and algorithm combinations quickly, which is a reasonable baseline for tabular data. Local study-map skill 2.2 (Job Configuration, Compute Targets, and Sweeps), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. Automated ML tests preprocessing and algorithm combinations quickly, which is a reasonable baseline for tabular data. In this case: Automated ML tests preprocessing and algorithm combinations quickly, which is a reasonable baseline.
- **B:** Incorrect for this question. A single script hides intermediate artifacts, so a failed stage cannot be rerun without repeating everything. Why the correct answer wins: Automated ML tests preprocessing and algorithm combinations quickly, which is a reasonable baseline.
- **C:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: Automated ML tests preprocessing and algorithm combinations quickly, which is a reasonable baseline.
- **D:** Incorrect for this question. A sweep samples the search space and records every trial, which finds an optimum systematically rather than by guesswork. Why the correct answer wins: Automated ML tests preprocessing and algorithm combinations quickly, which is a reasonable baseline.

### Question 21 — B

Answer: Enable MLflow tracking so runs log to the workspace. MLflow records parameters, metrics, and artifacts against a run, which is what makes the runs comparable. MLflow records parameters, metrics, and artifacts against a run, which is what makes experiments comparable. Local study-map skill 2.3 (Experiment Tracking with MLflow), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: MLflow records parameters, metrics, and artifacts against a run, which is what makes the runs comparable.
- **B:** Correct. MLflow records parameters, metrics, and artifacts against a run, which is what makes experiments comparable. In this case: MLflow records parameters, metrics, and artifacts against a run, which is what makes the runs comparable.
- **C:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: MLflow records parameters, metrics, and artifacts against a run, which is what makes the runs comparable.
- **D:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: MLflow records parameters, metrics, and artifacts against a run, which is what makes the runs comparable.

### Question 22 — D

Answer: Point the MLflow tracking URI at the workspace endpoint. The tracking URI decides which workspace receives the run. The tracking URI decides which workspace receives the run; without it, logging lands only on the local filesystem. Local study-map skill 2.3 (Experiment Tracking with MLflow), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: The tracking URI decides which workspace receives the run.
- **B:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: The tracking URI decides which workspace receives the run.
- **C:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: The tracking URI decides which workspace receives the run.
- **D:** Correct. The tracking URI decides which workspace receives the run; without it, logging lands only on the local filesystem. In this case: The tracking URI decides which workspace receives the run.

### Question 23 — C

Answer: Group the trials under a named experiment. A named experiment groups related runs so variants are compared against each other. An experiment groups related runs, which is how variants of the same task are compared against each other. Local study-map skill 2.3 (Experiment Tracking with MLflow), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A named experiment groups related runs so variants are compared against each other.
- **B:** Incorrect for this question. MLflow records parameters, metrics, and artifacts against a run, which is what makes experiments comparable. Why the correct answer wins: A named experiment groups related runs so variants are compared against each other.
- **C:** Correct. An experiment groups related runs, which is how variants of the same task are compared against each other. In this case: A named experiment groups related runs so variants are compared against each other.
- **D:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: A named experiment groups related runs so variants are compared against each other.

### Question 24 — B

Answer: Register each candidate with a version and deploy one explicit version. An explicit model version pins what is served, so a new registration cannot change production behaviour. An explicit version pins what is served, so a new registration cannot silently change production behaviour. Local study-map skill 2.4 (Model Registration, Versioning, and Metadata), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: An explicit model version pins what is served, so a new registration cannot change production behaviour.
- **B:** Correct. An explicit version pins what is served, so a new registration cannot silently change production behaviour. In this case: An explicit model version pins what is served, so a new registration cannot change production behaviour.
- **C:** Incorrect for this question. Skipping the staged check saves a day and moves the discovery of a defect to a customer. Why the correct answer wins: An explicit model version pins what is served, so a new registration cannot change production behaviour.
- **D:** Incorrect for this question. Deploying whatever is latest lets an untested registration reach production with no promotion gate. Why the correct answer wins: An explicit model version pins what is served, so a new registration cannot change production behaviour.

### Question 25 — D

Answer: Tag the registered model with the data asset and commit it came from. Tags carry provenance, which is what an audit needs to rebuild an artifact. Tags carry provenance, which is what an audit needs in order to rebuild the artifact. Local study-map skill 2.4 (Model Registration, Versioning, and Metadata), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Documented metrics and intended use let a reviewer decide whether the version is fit to promote. Why the correct answer wins: Tags carry provenance, which is what an audit needs to rebuild an artifact.
- **B:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: Tags carry provenance, which is what an audit needs to rebuild an artifact.
- **C:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: Tags carry provenance, which is what an audit needs to rebuild an artifact.
- **D:** Correct. Tags carry provenance, which is what an audit needs in order to rebuild the artifact. In this case: Tags carry provenance, which is what an audit needs to rebuild an artifact.

### Question 26 — B

Answer: Attach a description, metrics, and intended use to the model version. A description, metrics, and intended use give a reviewer the basis for the decision. Documented metrics and intended use let a reviewer decide whether the version is fit to promote. Local study-map skill 2.4 (Model Registration, Versioning, and Metadata), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Deploying whatever is latest lets an untested registration reach production with no promotion gate. Why the correct answer wins: A description, metrics, and intended use give a reviewer the basis for the decision.
- **B:** Correct. Documented metrics and intended use let a reviewer decide whether the version is fit to promote. In this case: A description, metrics, and intended use give a reviewer the basis for the decision.
- **C:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: A description, metrics, and intended use give a reviewer the basis for the decision.
- **D:** Incorrect for this question. Tags carry provenance, which is what an audit needs in order to rebuild the artifact. Why the correct answer wins: A description, metrics, and intended use give a reviewer the basis for the decision.

### Question 27 — B

Answer: Deploy to a managed online endpoint with an explicit model version. A managed online endpoint serves real-time requests and manages the infrastructure. A managed online endpoint serves real-time requests and manages the underlying infrastructure. Local study-map skill 2.5 (Managed Online Endpoint Deployment), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Scoring a large file one request at a time pays for always-on capacity and is slow for bulk work. Why the correct answer wins: A managed online endpoint serves real-time requests and manages the infrastructure.
- **B:** Correct. A managed online endpoint serves real-time requests and manages the underlying infrastructure. In this case: A managed online endpoint serves real-time requests and manages the infrastructure.
- **C:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A managed online endpoint serves real-time requests and manages the infrastructure.
- **D:** Incorrect for this question. A batch endpoint scores a large file on a schedule and needs no always-on capacity. Why the correct answer wins: A managed online endpoint serves real-time requests and manages the infrastructure.

### Question 28 — A

Answer: Mount the model artifact rather than baking it into the image. Mounting the artifact keeps the model out of the image, so a new version does not require a rebuild. Mounting keeps the artifact out of the image, so a new version does not require an image rebuild. Local study-map skill 2.5 (Managed Online Endpoint Deployment), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. Mounting keeps the artifact out of the image, so a new version does not require an image rebuild. In this case: Mounting the artifact keeps the model out of the image, so a new version does not require a rebuild.
- **B:** Incorrect for this question. A one-step replacement exposes every request to an unproven version with no measured canary. Why the correct answer wins: Mounting the artifact keeps the model out of the image, so a new version does not require a rebuild.
- **C:** Incorrect for this question. Baking the model ties every version to an image build, which slows promotion and bloats the registry. Why the correct answer wins: Mounting the artifact keeps the model out of the image, so a new version does not require a rebuild.
- **D:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: Mounting the artifact keeps the model out of the image, so a new version does not require a rebuild.

### Question 29 — C

Answer: Configure liveness and readiness probes on the deployment. A readiness probe keeps traffic away until the container can actually serve. Liveness restarts an unhealthy container and readiness keeps traffic away until the container can actually serve. Local study-map skill 2.5 (Managed Online Endpoint Deployment), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Deployment-time accuracy is a snapshot; it says nothing about the data that arrives afterwards. Why the correct answer wins: A readiness probe keeps traffic away until the container can actually serve.
- **B:** Incorrect for this question. A fixed count either wastes money at low load or throttles at peak. Why the correct answer wins: A readiness probe keeps traffic away until the container can actually serve.
- **C:** Correct. Liveness restarts an unhealthy container and readiness keeps traffic away until the container can actually serve. In this case: A readiness probe keeps traffic away until the container can actually serve.
- **D:** Incorrect for this question. Without probes, a container that starts but cannot load the model still receives traffic. Why the correct answer wins: A readiness probe keeps traffic away until the container can actually serve.

### Question 30 — A

Answer: Deploy a batch endpoint for the overnight scoring job. A batch endpoint scores a large file on a schedule and needs no always-on capacity. A batch endpoint scores a large file on a schedule and needs no always-on capacity. Local study-map skill 2.6 (Batch Endpoints and Controlled Traffic Rollout), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. A batch endpoint scores a large file on a schedule and needs no always-on capacity. In this case: A batch endpoint scores a large file on a schedule and needs no always-on capacity.
- **B:** Incorrect for this question. A managed online endpoint serves real-time requests and manages the underlying infrastructure. Why the correct answer wins: A batch endpoint scores a large file on a schedule and needs no always-on capacity.
- **C:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A batch endpoint scores a large file on a schedule and needs no always-on capacity.
- **D:** Incorrect for this question. Scoring a large file one request at a time pays for always-on capacity and is slow for bulk work. Why the correct answer wins: A batch endpoint scores a large file on a schedule and needs no always-on capacity.

### Question 31 — B

Answer: Split endpoint traffic 10/90 so the new deployment receives a canary share. A traffic split sends a canary share to the new deployment while the incumbent keeps serving the rest. A traffic split sends a small share to the new deployment, so a regression affects fewer requests and is measurable. Local study-map skill 2.6 (Batch Endpoints and Controlled Traffic Rollout), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. Why the correct answer wins: A traffic split sends a canary share to the new deployment while the incumbent keeps serving the rest.
- **B:** Correct. A traffic split sends a small share to the new deployment, so a regression affects fewer requests and is measurable. In this case: A traffic split sends a canary share to the new deployment while the incumbent keeps serving the rest.
- **C:** Incorrect for this question. A one-step replacement exposes every request to an unproven version with no measured canary. Why the correct answer wins: A traffic split sends a canary share to the new deployment while the incumbent keeps serving the rest.
- **D:** Incorrect for this question. Skipping the staged check saves a day and moves the discovery of a defect to a customer. Why the correct answer wins: A traffic split sends a canary share to the new deployment while the incumbent keeps serving the rest.

### Question 32 — D

Answer: Keep the previous deployment in place so traffic can be moved back. A retained deployment makes rollback a traffic change rather than a redeploy. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. Local study-map skill 2.6 (Batch Endpoints and Controlled Traffic Rollout), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Baking the model ties every version to an image build, which slows promotion and bloats the registry. Why the correct answer wins: A retained deployment makes rollback a traffic change rather than a redeploy.
- **B:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: A retained deployment makes rollback a traffic change rather than a redeploy.
- **C:** Incorrect for this question. A one-step replacement exposes every request to an unproven version with no measured canary. Why the correct answer wins: A retained deployment makes rollback a traffic change rather than a redeploy.
- **D:** Correct. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. In this case: A retained deployment makes rollback a traffic change rather than a redeploy.

### Question 33 — B

Answer: Set autoscale rules on the deployment with a deliberate minimum instance count. Autoscale matches capacity to load, and a deliberate minimum protects latency during the burst. Autoscale matches capacity to load, and the minimum sets the floor that protects latency during a burst. Local study-map skill 2.7 (Autoscaling, Health Probes, and Rollback), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. A fixed count either wastes money at low load or throttles at peak. Why the correct answer wins: Autoscale matches capacity to load, and a deliberate minimum protects latency during the burst.
- **B:** Correct. Autoscale matches capacity to load, and the minimum sets the floor that protects latency during a burst. In this case: Autoscale matches capacity to load, and a deliberate minimum protects latency during the burst.
- **C:** Incorrect for this question. Scoring a large file one request at a time pays for always-on capacity and is slow for bulk work. Why the correct answer wins: Autoscale matches capacity to load, and a deliberate minimum protects latency during the burst.
- **D:** Incorrect for this question. Without probes, a container that starts but cannot load the model still receives traffic. Why the correct answer wins: Autoscale matches capacity to load, and a deliberate minimum protects latency during the burst.

### Question 34 — D

Answer: Enable data drift monitoring against the training baseline. Drift monitoring compares live inputs with the training baseline, which is what catches silent degradation. Drift monitoring compares live input distributions with the training baseline, which is what catches silent degradation. Local study-map skill 2.8 (Data and Model Drift Monitoring), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Deployment-time accuracy is a snapshot; it says nothing about the data that arrives afterwards. Why the correct answer wins: Drift monitoring compares live inputs with the training baseline, which is what catches silent degradation.
- **B:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: Drift monitoring compares live inputs with the training baseline, which is what catches silent degradation.
- **C:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: Drift monitoring compares live inputs with the training baseline, which is what catches silent degradation.
- **D:** Correct. Drift monitoring compares live input distributions with the training baseline, which is what catches silent degradation. In this case: Drift monitoring compares live inputs with the training baseline, which is what catches silent degradation.

### Question 35 — C

Answer: Create an alert rule on the drift and latency metrics. An alert turns the metric into an action rather than a document someone may read. An alert turns a metric into an action; without it a drift report is noticed only if someone reads it. Local study-map skill 2.8 (Data and Model Drift Monitoring), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: An alert turns the metric into an action rather than a document someone may read.
- **B:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: An alert turns the metric into an action rather than a document someone may read.
- **C:** Correct. An alert turns a metric into an action; without it a drift report is noticed only if someone reads it. In this case: An alert turns the metric into an action rather than a document someone may read.
- **D:** Incorrect for this question. Deployment-time accuracy is a snapshot; it says nothing about the data that arrives afterwards. Why the correct answer wins: An alert turns the metric into an action rather than a document someone may read.

### Question 36 — A, D

Answers: Enable MLflow tracking so runs log to the workspace; Log metrics and the model artifact explicitly in the training script. Tracking records the run against the workspace, and explicit logging stores the metrics and artifact. MLflow records parameters, metrics, and artifacts against a run, which is what makes experiments comparable. Explicit logging captures the numbers and artifact a comparison needs; without it the run records only that it happened. Local study-map skill 2.3 (Experiment Tracking with MLflow), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. MLflow records parameters, metrics, and artifacts against a run, which is what makes experiments comparable. In this case: Tracking records the run against the workspace, and explicit logging stores the metrics and artifact.
- **B:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: Tracking records the run against the workspace, and explicit logging stores the metrics and artifact.
- **C:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: Tracking records the run against the workspace, and explicit logging stores the metrics and artifact.
- **D:** Correct. Explicit logging captures the numbers and artifact a comparison needs; without it the run records only that it happened. In this case: Tracking records the run against the workspace, and explicit logging stores the metrics and artifact.
- **E:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: Tracking records the run against the workspace, and explicit logging stores the metrics and artifact.

### Question 37 — B, C

Answers: Set autoscale rules on the deployment with a deliberate minimum instance count; Configure liveness and readiness probes on the deployment. Autoscale matches capacity to load, and probes gate traffic until the container can serve. Autoscale matches capacity to load, and the minimum sets the floor that protects latency during a burst. Liveness restarts an unhealthy container and readiness keeps traffic away until the container can actually serve. Local study-map skill 2.7 (Autoscaling, Health Probes, and Rollback), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. A fixed count either wastes money at low load or throttles at peak. Why the correct answer wins: Autoscale matches capacity to load, and probes gate traffic until the container can serve.
- **B:** Correct. Autoscale matches capacity to load, and the minimum sets the floor that protects latency during a burst. In this case: Autoscale matches capacity to load, and probes gate traffic until the container can serve.
- **C:** Correct. Liveness restarts an unhealthy container and readiness keeps traffic away until the container can actually serve. In this case: Autoscale matches capacity to load, and probes gate traffic until the container can serve.
- **D:** Incorrect for this question. Without probes, a container that starts but cannot load the model still receives traffic. Why the correct answer wins: Autoscale matches capacity to load, and probes gate traffic until the container can serve.
- **E:** Incorrect for this question. Scoring a large file one request at a time pays for always-on capacity and is slow for bulk work. Why the correct answer wins: Autoscale matches capacity to load, and probes gate traffic until the container can serve.

### Question 38 — A

Answer: Train the candidate → evaluate against the gate → register the model version → deploy at a canary traffic share → shift all traffic after the metrics hold. Training, evaluation, registration, canary, and full traffic each depend on the artifact produced before them. Each step produces the artifact the next one needs: a trained model before an evaluation, a passing evaluation before registration, and a measured canary before full traffic. Local study-map skill 2.1 (Training Pipeline Authoring and Orchestration), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. Each step produces the artifact the next one needs: a trained model before an evaluation, a passing evaluation before registration, and a measured canary before full traffic. In this case: Training, evaluation, registration, canary, and full traffic each depend on the artifact produced before them.
- **B:** Incorrect for this question. There is nothing to evaluate before training, and shifting all traffic before registration removes the artifact a rollback would target. Why the correct answer wins: Training, evaluation, registration, canary, and full traffic each depend on the artifact produced before them.
- **C:** Incorrect for this question. A deployment needs a registered artifact, and the evaluation that justifies promotion happens before anything serves traffic. Why the correct answer wins: Training, evaluation, registration, canary, and full traffic each depend on the artifact produced before them.
- **D:** Incorrect for this question. Registration should record a model that already passed the gate, and full traffic without a canary exposes every request to an unproven version. Why the correct answer wins: Training, evaluation, registration, canary, and full traffic each depend on the artifact produced before them.

### Question 39 — A

Answer: Deploy the new version to a second deployment → send a small traffic share to it → compare error rate and latency with the incumbent → move all traffic back if the metrics regress. A second deployment preserves the incumbent for measurement and for the rollback itself. A separate deployment keeps the incumbent serving while the candidate is measured, which is what makes the rollback a traffic change. Local study-map skill 2.6 (Batch Endpoints and Controlled Traffic Rollout), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. A separate deployment keeps the incumbent serving while the candidate is measured, which is what makes the rollback a traffic change. In this case: A second deployment preserves the incumbent for measurement and for the rollback itself.
- **B:** Incorrect for this question. There is nothing to compare before the candidate exists and is receiving traffic. Why the correct answer wins: A second deployment preserves the incumbent for measurement and for the rollback itself.
- **C:** Incorrect for this question. Replacing the incumbent destroys the comparison baseline and the thing you would roll back to. Why the correct answer wins: A second deployment preserves the incumbent for measurement and for the rollback itself.
- **D:** Incorrect for this question. All traffic is shifted before the candidate is deployed, and the comparison comes after the exposure it was meant to prevent. Why the correct answer wins: A second deployment preserves the incumbent for measurement and for the rollback itself.

### Question 40 — D

Answer: Create a Foundry hub and a project per team. A hub shares capacity and connections while a project gives each team an isolated boundary. A hub shares connections and capacity, and a project gives a team an isolated working boundary for its own assets. Local study-map skill 3.1 (Foundry Hub, Project, and Shared Capacity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. A shared workspace mixes assets and identities across environments, so a test job can register over the model production is serving. Why the correct answer wins: A hub shares capacity and connections while a project gives each team an isolated boundary.
- **B:** Incorrect for this question. A single shared project mixes assets and permissions, so one team can change what another depends on. Why the correct answer wins: A hub shares capacity and connections while a project gives each team an isolated boundary.
- **C:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A hub shares capacity and connections while a project gives each team an isolated boundary.
- **D:** Correct. A hub shares connections and capacity, and a project gives a team an isolated working boundary for its own assets. In this case: A hub shares capacity and connections while a project gives each team an isolated boundary.

### Question 41 — B

Answer: Reserve provisioned throughput for the steady high-volume workload. Provisioned throughput trades a commitment for predictable latency and lower cost per token at sustained volume. Provisioned throughput reserves capacity, which gives predictable latency and cost at sustained volume. Local study-map skill 3.2 (Model Catalog Selection and Deployment Capacity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Pay-as-you-go costs nothing when idle and needs no forecast, which suits an unproven workload. Why the correct answer wins: Provisioned throughput trades a commitment for predictable latency and lower cost per token at sustained volume.
- **B:** Correct. Provisioned throughput reserves capacity, which gives predictable latency and cost at sustained volume. In this case: Provisioned throughput trades a commitment for predictable latency and lower cost per token at sustained volume.
- **C:** Incorrect for this question. A fixed count either wastes money at low load or throttles at peak. Why the correct answer wins: Provisioned throughput trades a commitment for predictable latency and lower cost per token at sustained volume.
- **D:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: Provisioned throughput trades a commitment for predictable latency and lower cost per token at sustained volume.

### Question 42 — D

Answer: Apply a content filter policy appropriate to the audience. A content filter policy sets the harm thresholds applied to each call. A content filter policy sets the harm thresholds applied to prompts and completions for that deployment. Local study-map skill 3.2 (Model Catalog Selection and Deployment Capacity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Toxicity evaluation measures harmful output against the standard that audience or regulation requires. Why the correct answer wins: A content filter policy sets the harm thresholds applied to each call.
- **B:** Incorrect for this question. Adversarial cases test whether instructions in the input or the content can override the system prompt. Why the correct answer wins: A content filter policy sets the harm thresholds applied to each call.
- **C:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: A content filter policy sets the harm thresholds applied to each call.
- **D:** Correct. A content filter policy sets the harm thresholds applied to prompts and completions for that deployment. In this case: A content filter policy sets the harm thresholds applied to each call.

### Question 43 — C

Answer: Author the flow as a directed acyclic graph with typed inputs and outputs. A typed directed acyclic graph gives each step an explicit contract that can be tested independently. A typed graph makes each step contract explicit, so the flow can be tested in isolation and composed with others. Local study-map skill 3.3 (Prompt Flow Authoring and DAG Composition), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. A single script hides intermediate artifacts, so a failed stage cannot be rerun without repeating everything. Why the correct answer wins: A typed directed acyclic graph gives each step an explicit contract that can be tested independently.
- **B:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A typed directed acyclic graph gives each step an explicit contract that can be tested independently.
- **C:** Correct. A typed graph makes each step contract explicit, so the flow can be tested in isolation and composed with others. In this case: A typed directed acyclic graph gives each step an explicit contract that can be tested independently.
- **D:** Incorrect for this question. A batch run applies the flow to every row, which is how an evaluation dataset is scored. Why the correct answer wins: A typed directed acyclic graph gives each step an explicit contract that can be tested independently.

### Question 44 — B

Answer: Create a variant to compare two prompt strategies side by side. Variants keep alternatives together so the comparison is reproducible. Variants keep the alternatives together, so the comparison is reproducible rather than remembered. Local study-map skill 3.3 (Prompt Flow Authoring and DAG Composition), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. A family name is not an addressable endpoint; the flow needs a deployment to call. Why the correct answer wins: Variants keep alternatives together so the comparison is reproducible.
- **B:** Correct. Variants keep the alternatives together, so the comparison is reproducible rather than remembered. In this case: Variants keep alternatives together so the comparison is reproducible.
- **C:** Incorrect for this question. A typed graph makes each step contract explicit, so the flow can be tested in isolation and composed with others. Why the correct answer wins: Variants keep alternatives together so the comparison is reproducible.
- **D:** Incorrect for this question. A prompt change shipped without an evaluation gate is an unmeasured change to a production system. Why the correct answer wins: Variants keep alternatives together so the comparison is reproducible.

### Question 45 — C

Answer: Store the model credential as a project connection. A project connection holds the endpoint and credential outside the flow. A project connection holds the endpoint and credential outside the flow, so the flow file stays secret-free. Local study-map skill 3.4 (Flow Connections, Secrets, and Runtime Identity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. A plain environment variable appears in job definitions and logs, which exposes the secret. Why the correct answer wins: A project connection holds the endpoint and credential outside the flow.
- **B:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: A project connection holds the endpoint and credential outside the flow.
- **C:** Correct. A project connection holds the endpoint and credential outside the flow, so the flow file stays secret-free. In this case: A project connection holds the endpoint and credential outside the flow.
- **D:** Incorrect for this question. A key inside a flow file is a secret in source control and cannot be rotated without editing the flow. Why the correct answer wins: A project connection holds the endpoint and credential outside the flow.

### Question 46 — C

Answer: Paste the API key into a Python node inside the flow. A key in a flow file is a secret in source control and cannot be rotated without editing the flow. A key inside a flow file is a secret in source control and cannot be rotated without editing the flow. Local study-map skill 3.4 (Flow Connections, Secrets, and Runtime Identity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. A project connection holds the endpoint and credential outside the flow, so the flow file stays secret-free. Why the correct answer wins: A key in a flow file is a secret in source control and cannot be rotated without editing the flow.
- **B:** Incorrect for this question. A plain environment variable appears in job definitions and logs, which exposes the secret. Why the correct answer wins: A key in a flow file is a secret in source control and cannot be rotated without editing the flow.
- **C:** Correct. A key inside a flow file is a secret in source control and cannot be rotated without editing the flow. In this case: A key in a flow file is a secret in source control and cannot be rotated without editing the flow.
- **D:** Incorrect for this question. An inline key puts a credential in source control and ties the job to one physical path. Why the correct answer wins: A key in a flow file is a secret in source control and cannot be rotated without editing the flow.

### Question 47 — D

Answer: Index the documents in Azure AI Search and query the index from the flow. An index supports retrieval at answer time, so the flow grounds on current content. An index supports retrieval at answer time, so the flow grounds on current content instead of on model memory. Local study-map skill 3.5 (Retrieval-Augmented Grounding with Azure AI Search), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: An index supports retrieval at answer time, so the flow grounds on current content.
- **B:** Incorrect for this question. Fine-tuning bakes a snapshot of the content into the model, so it goes stale as documents change. Why the correct answer wins: An index supports retrieval at answer time, so the flow grounds on current content.
- **C:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: An index supports retrieval at answer time, so the flow grounds on current content.
- **D:** Correct. An index supports retrieval at answer time, so the flow grounds on current content instead of on model memory. In this case: An index supports retrieval at answer time, so the flow grounds on current content.

### Question 48 — A

Answer: Use hybrid search with semantic ranking. Hybrid search keeps keyword matching for exact identifiers alongside vector similarity. Hybrid search combines keyword and vector matching, and semantic ranking reorders the top results, which improves recall on domain vocabulary and identifiers. Local study-map skill 3.5 (Retrieval-Augmented Grounding with Azure AI Search), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Correct. Hybrid search combines keyword and vector matching, and semantic ranking reorders the top results, which improves recall on domain vocabulary and identifiers. In this case: Hybrid search keeps keyword matching for exact identifiers alongside vector similarity.
- **B:** Incorrect for this question. Vector-only retrieval misses exact identifiers and product codes, which is where keyword matching earns its place. Why the correct answer wins: Hybrid search keeps keyword matching for exact identifiers alongside vector similarity.
- **C:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: Hybrid search keeps keyword matching for exact identifiers alongside vector similarity.
- **D:** Incorrect for this question. Fine-tuning bakes a snapshot of the content into the model, so it goes stale as documents change. Why the correct answer wins: Hybrid search keeps keyword matching for exact identifiers alongside vector similarity.

### Question 49 — D

Answer: Chunk documents by section with a small overlap. Section-sized chunks with overlap keep a passage specific enough to be the right citation. Section-sized chunks with overlap keep a passage coherent while staying small enough to be specific. Local study-map skill 3.6 (Chunking, Embeddings, and Index Refresh), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Retrieving more passages adds tokens and can bury the relevant passage among distractors. Why the correct answer wins: Section-sized chunks with overlap keep a passage specific enough to be the right citation.
- **B:** Incorrect for this question. A whole-document chunk makes retrieval return an undifferentiated document, so the answer quotes the wrong part. Why the correct answer wins: Section-sized chunks with overlap keep a passage specific enough to be the right citation.
- **C:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: Section-sized chunks with overlap keep a passage specific enough to be the right citation.
- **D:** Correct. Section-sized chunks with overlap keep a passage coherent while staying small enough to be specific. In this case: Section-sized chunks with overlap keep a passage specific enough to be the right citation.

### Question 50 — B

Answer: Rebuild the index on a schedule after the source content changes. A scheduled refresh keeps retrieval aligned with the current source. Scheduled refresh keeps retrieval aligned with the source; without it the assistant answers from retired content. Local study-map skill 3.6 (Chunking, Embeddings, and Index Refresh), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: A scheduled refresh keeps retrieval aligned with the current source.
- **B:** Correct. Scheduled refresh keeps retrieval aligned with the source; without it the assistant answers from retired content. In this case: A scheduled refresh keeps retrieval aligned with the current source.
- **C:** Incorrect for this question. Section-sized chunks with overlap keep a passage coherent while staying small enough to be specific. Why the correct answer wins: A scheduled refresh keeps retrieval aligned with the current source.
- **D:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: A scheduled refresh keeps retrieval aligned with the current source.

### Question 51 — B

Answer: Keep the prompt in its own file under version control. A separate versioned prompt file makes the change reviewable and revertible. A separate versioned prompt file makes every change reviewable and revertible. Local study-map skill 3.7 (Prompt and Flow Versioning with Evaluation Gates), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. A key inside a flow file is a secret in source control and cannot be rotated without editing the flow. Why the correct answer wins: A separate versioned prompt file makes the change reviewable and revertible.
- **B:** Correct. A separate versioned prompt file makes every change reviewable and revertible. In this case: A separate versioned prompt file makes the change reviewable and revertible.
- **C:** Incorrect for this question. Variants keep the alternatives together, so the comparison is reproducible rather than remembered. Why the correct answer wins: A separate versioned prompt file makes the change reviewable and revertible.
- **D:** Incorrect for this question. A prompt change shipped without an evaluation gate is an unmeasured change to a production system. Why the correct answer wins: A separate versioned prompt file makes the change reviewable and revertible.

### Question 52 — B

Answer: Run the evaluation in continuous integration before the flow is promoted. An evaluation gate before promotion stops a regression reaching traffic. An offline gate stops a regression before it reaches production traffic. Local study-map skill 3.7 (Prompt and Flow Versioning with Evaluation Gates), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. A prompt change shipped without an evaluation gate is an unmeasured change to a production system. Why the correct answer wins: An evaluation gate before promotion stops a regression reaching traffic.
- **B:** Correct. An offline gate stops a regression before it reaches production traffic. In this case: An evaluation gate before promotion stops a regression reaching traffic.
- **C:** Incorrect for this question. Skipping the staged check saves a day and moves the discovery of a defect to a customer. Why the correct answer wins: An evaluation gate before promotion stops a regression reaching traffic.
- **D:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: An evaluation gate before promotion stops a regression reaching traffic.

### Question 53 — D

Answer: Register a scoped tool list for the agent. A scoped tool list bounds what the agent can do. A scoped tool list bounds what the agent can do, which is the main control over unintended actions. Local study-map skill 3.8 (Agent Orchestration and Tool Binding), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: A scoped tool list bounds what the agent can do.
- **B:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: A scoped tool list bounds what the agent can do.
- **C:** Incorrect for this question. An open tool list widens the blast radius of a wrong tool choice. Why the correct answer wins: A scoped tool list bounds what the agent can do.
- **D:** Correct. A scoped tool list bounds what the agent can do, which is the main control over unintended actions. In this case: A scoped tool list bounds what the agent can do.

### Question 54 — B

Answer: Bound the agent memory to the current session. Session-scoped memory prevents facts crossing between conversations. Session-scoped memory keeps context within a conversation and stops one user facts leaking into another. Local study-map skill 3.8 (Agent Orchestration and Tool Binding), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. An open tool list widens the blast radius of a wrong tool choice. Why the correct answer wins: Session-scoped memory prevents facts crossing between conversations.
- **B:** Correct. Session-scoped memory keeps context within a conversation and stops one user facts leaking into another. In this case: Session-scoped memory prevents facts crossing between conversations.
- **C:** Incorrect for this question. Typed state makes each handoff explicit and testable instead of relying on free text. Why the correct answer wins: Session-scoped memory prevents facts crossing between conversations.
- **D:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: Session-scoped memory prevents facts crossing between conversations.

### Question 55 — A, D

Answers: Create a Foundry hub and a project per team; Reference the deployment name from the flow rather than the model family name. A hub with a project per team isolates assets, and referencing the deployment name keeps flows stable. A hub shares connections and capacity, and a project gives a team an isolated working boundary for its own assets. A flow calls a deployment, so the deployment name stays the stable reference when the underlying model changes. Local study-map skill 3.1 (Foundry Hub, Project, and Shared Capacity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Correct. A flow calls a deployment, so the deployment name stays the stable reference when the underlying model changes. In this case: A hub with a project per team isolates assets, and referencing the deployment name keeps flows stable.
- **B:** Incorrect for this question. A single shared project mixes assets and permissions, so one team can change what another depends on. Why the correct answer wins: A hub with a project per team isolates assets, and referencing the deployment name keeps flows stable.
- **C:** Incorrect for this question. A family name is not an addressable endpoint; the flow needs a deployment to call. Why the correct answer wins: A hub with a project per team isolates assets, and referencing the deployment name keeps flows stable.
- **D:** Correct. A hub shares connections and capacity, and a project gives a team an isolated working boundary for its own assets. In this case: A hub with a project per team isolates assets, and referencing the deployment name keeps flows stable.
- **E:** Incorrect for this question. A key inside a flow file is a secret in source control and cannot be rotated without editing the flow. Why the correct answer wins: A hub with a project per team isolates assets, and referencing the deployment name keeps flows stable.

### Question 56 — A, E

Answers: Index the documents in Azure AI Search and query the index from the flow; Set document-level access in the index so retrieval respects entitlements. Indexing the content enables grounding, and document-level access keeps retrieval within entitlement. An index supports retrieval at answer time, so the flow grounds on current content instead of on model memory. Document-level access keeps retrieval within what the requesting user is allowed to see. Local study-map skill 3.5 (Retrieval-Augmented Grounding with Azure AI Search), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Correct. An index supports retrieval at answer time, so the flow grounds on current content instead of on model memory. In this case: Indexing the content enables grounding, and document-level access keeps retrieval within entitlement.
- **B:** Incorrect for this question. Fine-tuning bakes a snapshot of the content into the model, so it goes stale as documents change. Why the correct answer wins: Indexing the content enables grounding, and document-level access keeps retrieval within entitlement.
- **C:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: Indexing the content enables grounding, and document-level access keeps retrieval within entitlement.
- **D:** Incorrect for this question. Public access broadens the attack surface and usually fails a regulated review. Why the correct answer wins: Indexing the content enables grounding, and document-level access keeps retrieval within entitlement.
- **E:** Correct. Document-level access keeps retrieval within what the requesting user is allowed to see. In this case: Indexing the content enables grounding, and document-level access keeps retrieval within entitlement.

### Question 57 — B, E

Answers: Keep the prompt in its own file under version control; Run the evaluation in continuous integration before the flow is promoted. A versioned prompt file makes the change reviewable, and the offline gate blocks a regression. A separate versioned prompt file makes every change reviewable and revertible. An offline gate stops a regression before it reaches production traffic. Local study-map skill 3.7 (Prompt and Flow Versioning with Evaluation Gates), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. A prompt change shipped without an evaluation gate is an unmeasured change to a production system. Why the correct answer wins: A versioned prompt file makes the change reviewable, and the offline gate blocks a regression.
- **B:** Correct. An offline gate stops a regression before it reaches production traffic. In this case: A versioned prompt file makes the change reviewable, and the offline gate blocks a regression.
- **C:** Incorrect for this question. Skipping the staged check saves a day and moves the discovery of a defect to a customer. Why the correct answer wins: A versioned prompt file makes the change reviewable, and the offline gate blocks a regression.
- **D:** Incorrect for this question. A key inside a flow file is a secret in source control and cannot be rotated without editing the flow. Why the correct answer wins: A versioned prompt file makes the change reviewable, and the offline gate blocks a regression.
- **E:** Correct. A separate versioned prompt file makes every change reviewable and revertible. In this case: A versioned prompt file makes the change reviewable, and the offline gate blocks a regression.

### Question 58 — D

Answer: Curate the source documents → chunk and embed them → create the search index → bind the index to the flow → evaluate retrieval and groundedness. Curation, chunking, indexing, binding, and evaluation each depend on the artifact produced before them. Content is prepared before it is indexed, the index exists before it is bound, and evaluation runs against a working flow. Local study-map skill 3.5 (Retrieval-Augmented Grounding with Azure AI Search), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Chunking precedes curation, so retired documents are embedded, and evaluation happens before there is an index to query. Why the correct answer wins: Curation, chunking, indexing, binding, and evaluation each depend on the artifact produced before them.
- **B:** Incorrect for this question. The flow is bound to an index that does not exist yet, and evaluation never happens at all. Why the correct answer wins: Curation, chunking, indexing, binding, and evaluation each depend on the artifact produced before them.
- **C:** Incorrect for this question. The index is created before its content is curated or embedded, and evaluation precedes the chunks it would retrieve. Why the correct answer wins: Curation, chunking, indexing, binding, and evaluation each depend on the artifact produced before them.
- **D:** Correct. Content is prepared before it is indexed, the index exists before it is bound, and evaluation runs against a working flow. In this case: Curation, chunking, indexing, binding, and evaluation each depend on the artifact produced before them.

### Question 59 — A

Answer: Inventory the data sources the flow needs → assign the project a managed identity → grant the identity the narrowest role on each source → verify a grounded answer returns only permitted content. The inventory defines scope, the identity replaces secrets, the grant is minimal, and verification proves the boundary. The sources define the scope, the identity replaces secrets, the grant is minimal, and the verification proves the boundary holds. Local study-map skill 3.1 (Foundry Hub, Project, and Shared Capacity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Correct. The sources define the scope, the identity replaces secrets, the grant is minimal, and the verification proves the boundary holds. In this case: The inventory defines scope, the identity replaces secrets, the grant is minimal, and verification proves the boundary.
- **B:** Incorrect for this question. Verification precedes the configuration it verifies, and the inventory comes last. Why the correct answer wins: The inventory defines scope, the identity replaces secrets, the grant is minimal, and verification proves the boundary.
- **C:** Incorrect for this question. The answer is verified before any role has been granted, and the sources are inventoried after the grant. Why the correct answer wins: The inventory defines scope, the identity replaces secrets, the grant is minimal, and verification proves the boundary.
- **D:** Incorrect for this question. A broad grant is made before the sources are known, and the identity is assigned after it has been granted permissions. Why the correct answer wins: The inventory defines scope, the identity replaces secrets, the grant is minimal, and verification proves the boundary.

### Question 60 — A

Answer: Build the evaluation dataset from real queries with graded answers. Real queries with graded answers are what make an evaluation number meaningful. A dataset drawn from real traffic with graded answers is what makes an evaluation number mean something. Local study-map skill 4.1 (Evaluation Dataset and Ground-Truth Design), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Correct. A dataset drawn from real traffic with graded answers is what makes an evaluation number mean something. In this case: Real queries with graded answers are what make an evaluation number meaningful.
- **B:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: Real queries with graded answers are what make an evaluation number meaningful.
- **C:** Incorrect for this question. A set authored from the prompt repeats its assumptions, so it passes changes that real users would reject. Why the correct answer wins: Real queries with graded answers are what make an evaluation number meaningful.
- **D:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: Real queries with graded answers are what make an evaluation number meaningful.

### Question 61 — C

Answer: Use an LLM judge with a rubric, calibrated against human grades. An LLM judge with a rubric, calibrated against human grades, scales while staying trustworthy. An LLM judge scales grading, and calibrating it against human grades is what keeps the score trustworthy. Local study-map skill 4.1 (Evaluation Dataset and Ground-Truth Design), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. A set authored from the prompt repeats its assumptions, so it passes changes that real users would reject. Why the correct answer wins: An LLM judge with a rubric, calibrated against human grades, scales while staying trustworthy.
- **B:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: An LLM judge with a rubric, calibrated against human grades, scales while staying trustworthy.
- **C:** Correct. An LLM judge scales grading, and calibrating it against human grades is what keeps the score trustworthy. In this case: An LLM judge with a rubric, calibrated against human grades, scales while staying trustworthy.
- **D:** Incorrect for this question. An uncalibrated judge can reproduce a systematic error consistently and look stable while being wrong. Why the correct answer wins: An LLM judge with a rubric, calibrated against human grades, scales while staying trustworthy.

### Question 62 — A

Answer: Score groundedness against the retrieved passages. Groundedness asks whether the answer is supported by the retrieved context. Groundedness asks whether the answer is supported by the retrieved context, which is the core anti-fabrication metric. Local study-map skill 4.2 (Groundedness and Relevance Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Correct. Groundedness asks whether the answer is supported by the retrieved context, which is the core anti-fabrication metric. In this case: Groundedness asks whether the answer is supported by the retrieved context.
- **B:** Incorrect for this question. Relevance asks whether the answer addresses what was asked, independently of whether it is true. Why the correct answer wins: Groundedness asks whether the answer is supported by the retrieved context.
- **C:** Incorrect for this question. Coherence measures whether the answer holds together logically, not whether it is grounded in a source. Why the correct answer wins: Groundedness asks whether the answer is supported by the retrieved context.
- **D:** Incorrect for this question. Fluency measures readability and language quality, not factual support. Why the correct answer wins: Groundedness asks whether the answer is supported by the retrieved context.

### Question 63 — C

Answer: Score relevance of the answer to the question asked. Relevance asks whether the answer addresses the question, independent of support. Relevance asks whether the answer addresses what was asked, independently of whether it is true. Local study-map skill 4.2 (Groundedness and Relevance Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. Similarity compares the answer with a reference, which requires a reference answer for every case. Why the correct answer wins: Relevance asks whether the answer addresses the question, independent of support.
- **B:** Incorrect for this question. Fluency measures readability and language quality, not factual support. Why the correct answer wins: Relevance asks whether the answer addresses the question, independent of support.
- **C:** Correct. Relevance asks whether the answer addresses what was asked, independently of whether it is true. In this case: Relevance asks whether the answer addresses the question, independent of support.
- **D:** Incorrect for this question. Groundedness asks whether the answer is supported by the retrieved context, which is the core anti-fabrication metric. Why the correct answer wins: Relevance asks whether the answer addresses the question, independent of support.

### Question 64 — D

Answer: Score fluency for readability and language quality. Fluency measures readability, not factual support. Fluency measures readability and language quality, not factual support. Local study-map skill 4.3 (Coherence, Fluency, and Similarity Metrics), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. Coherence measures whether the answer holds together logically, not whether it is grounded in a source. Why the correct answer wins: Fluency measures readability, not factual support.
- **B:** Incorrect for this question. Relevance asks whether the answer addresses what was asked, independently of whether it is true. Why the correct answer wins: Fluency measures readability, not factual support.
- **C:** Incorrect for this question. Groundedness asks whether the answer is supported by the retrieved context, which is the core anti-fabrication metric. Why the correct answer wins: Fluency measures readability, not factual support.
- **D:** Correct. Fluency measures readability and language quality, not factual support. In this case: Fluency measures readability, not factual support.

### Question 65 — C

Answer: Evaluate toxicity against the threshold the audience requires. Toxicity evaluation measures harmful output against the threshold the audience requires. Toxicity evaluation measures harmful output against the standard that audience or regulation requires. Local study-map skill 4.4 (Safety, Jailbreak, and Content Filter Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. Relevance asks whether the answer addresses what was asked, independently of whether it is true. Why the correct answer wins: Toxicity evaluation measures harmful output against the threshold the audience requires.
- **B:** Incorrect for this question. Fluency measures readability and language quality, not factual support. Why the correct answer wins: Toxicity evaluation measures harmful output against the threshold the audience requires.
- **C:** Correct. Toxicity evaluation measures harmful output against the standard that audience or regulation requires. In this case: Toxicity evaluation measures harmful output against the threshold the audience requires.
- **D:** Incorrect for this question. Similarity compares the answer with a reference, which requires a reference answer for every case. Why the correct answer wins: Toxicity evaluation measures harmful output against the threshold the audience requires.

### Question 66 — A

Answer: Run adversarial jailbreak and prompt-injection cases before release. Jailbreak testing measures resistance to instruction-override attempts. Adversarial cases test whether instructions in the input or the content can override the system prompt. Local study-map skill 4.4 (Safety, Jailbreak, and Content Filter Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Correct. Adversarial cases test whether instructions in the input or the content can override the system prompt. In this case: Jailbreak testing measures resistance to instruction-override attempts.
- **B:** Incorrect for this question. Fluency measures readability and language quality, not factual support. Why the correct answer wins: Jailbreak testing measures resistance to instruction-override attempts.
- **C:** Incorrect for this question. Toxicity evaluation measures harmful output against the standard that audience or regulation requires. Why the correct answer wins: Jailbreak testing measures resistance to instruction-override attempts.
- **D:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: Jailbreak testing measures resistance to instruction-override attempts.

### Question 67 — C

Answer: Test indirect injection through retrieved documents. Indirect injection hides instructions in retrieved content. Indirect injection hides instructions in retrieved content, which is the vector a retrieval system most easily misses. Local study-map skill 4.4 (Safety, Jailbreak, and Content Filter Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: Indirect injection hides instructions in retrieved content.
- **B:** Incorrect for this question. Adversarial cases test whether instructions in the input or the content can override the system prompt. Why the correct answer wins: Indirect injection hides instructions in retrieved content.
- **C:** Correct. Indirect injection hides instructions in retrieved content, which is the vector a retrieval system most easily misses. In this case: Indirect injection hides instructions in retrieved content.
- **D:** Incorrect for this question. Toxicity evaluation measures harmful output against the standard that audience or regulation requires. Why the correct answer wins: Indirect injection hides instructions in retrieved content.

### Question 68 — A

Answer: Enable distributed tracing and log the retrieval and model spans. Span-level tracing shows which stage produced the wrong answer. Span-level tracing shows which stage produced a wrong answer, which an aggregate score cannot. Local study-map skill 4.5 (Tracing, Logging, and Application Insights Observability), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Correct. Span-level tracing shows which stage produced a wrong answer, which an aggregate score cannot. In this case: Span-level tracing shows which stage produced the wrong answer.
- **B:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: Span-level tracing shows which stage produced the wrong answer.
- **C:** Incorrect for this question. Full prompt and completion logging is what lets a reviewer reproduce a bad answer. Why the correct answer wins: Span-level tracing shows which stage produced the wrong answer.
- **D:** Incorrect for this question. An uncalibrated judge can reproduce a systematic error consistently and look stable while being wrong. Why the correct answer wins: Span-level tracing shows which stage produced the wrong answer.

### Question 69 — D

Answer: Capture user feedback and review a sample of rated conversations weekly. Capturing and triaging feedback surfaces traffic the dataset does not represent. User feedback is the only signal about traffic that the evaluation set does not contain. Local study-map skill 4.6 (Online Feedback Loops and Continuous Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. Online evaluation catches the drift that a fixed offline dataset cannot represent. Why the correct answer wins: Capturing and triaging feedback surfaces traffic the dataset does not represent.
- **B:** Incorrect for this question. An offline gate stops a regression before it reaches production traffic. Why the correct answer wins: Capturing and triaging feedback surfaces traffic the dataset does not represent.
- **C:** Incorrect for this question. An uncalibrated judge can reproduce a systematic error consistently and look stable while being wrong. Why the correct answer wins: Capturing and triaging feedback surfaces traffic the dataset does not represent.
- **D:** Correct. User feedback is the only signal about traffic that the evaluation set does not contain. In this case: Capturing and triaging feedback surfaces traffic the dataset does not represent.

### Question 70 — C, D

Answers: Build the evaluation dataset from real queries with graded answers; Use a few hundred representative cases rather than a dozen. Real queries make the set representative, and a few hundred cases keep the confidence interval meaningful. A dataset drawn from real traffic with graded answers is what makes an evaluation number mean something. A small sample produces a confidence interval too wide to separate a real improvement from noise. Local study-map skill 4.1 (Evaluation Dataset and Ground-Truth Design), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. A set authored from the prompt repeats its assumptions, so it passes changes that real users would reject. Why the correct answer wins: Real queries make the set representative, and a few hundred cases keep the confidence interval meaningful.
- **B:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: Real queries make the set representative, and a few hundred cases keep the confidence interval meaningful.
- **C:** Correct. A small sample produces a confidence interval too wide to separate a real improvement from noise. In this case: Real queries make the set representative, and a few hundred cases keep the confidence interval meaningful.
- **D:** Correct. A dataset drawn from real traffic with graded answers is what makes an evaluation number mean something. In this case: Real queries make the set representative, and a few hundred cases keep the confidence interval meaningful.
- **E:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: Real queries make the set representative, and a few hundred cases keep the confidence interval meaningful.

### Question 71 — A, D

Answers: Run adversarial jailbreak and prompt-injection cases before release; Test indirect injection through retrieved documents. Direct jailbreak cases test the system prompt, and indirect cases test injected retrieved content. Adversarial cases test whether instructions in the input or the content can override the system prompt. Indirect injection hides instructions in retrieved content, which is the vector a retrieval system most easily misses. Local study-map skill 4.4 (Safety, Jailbreak, and Content Filter Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Correct. Adversarial cases test whether instructions in the input or the content can override the system prompt. In this case: Direct jailbreak cases test the system prompt, and indirect cases test injected retrieved content.
- **B:** Incorrect for this question. Fluency measures readability and language quality, not factual support. Why the correct answer wins: Direct jailbreak cases test the system prompt, and indirect cases test injected retrieved content.
- **C:** Incorrect for this question. Toxicity evaluation measures harmful output against the standard that audience or regulation requires. Why the correct answer wins: Direct jailbreak cases test the system prompt, and indirect cases test injected retrieved content.
- **D:** Correct. Indirect injection hides instructions in retrieved content, which is the vector a retrieval system most easily misses. In this case: Direct jailbreak cases test the system prompt, and indirect cases test injected retrieved content.
- **E:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: Direct jailbreak cases test the system prompt, and indirect cases test injected retrieved content.

### Question 72 — A, B

Answers: Enable distributed tracing and log the retrieval and model spans; Log prompts and completions against the trace, within data policy. Tracing locates the failing stage, and prompt logging allows the exact call to be replayed. Span-level tracing shows which stage produced a wrong answer, which an aggregate score cannot. Full prompt and completion logging is what lets a reviewer reproduce a bad answer. Local study-map skill 4.5 (Tracing, Logging, and Application Insights Observability), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Correct. Span-level tracing shows which stage produced a wrong answer, which an aggregate score cannot. In this case: Tracing locates the failing stage, and prompt logging allows the exact call to be replayed.
- **B:** Correct. Full prompt and completion logging is what lets a reviewer reproduce a bad answer. In this case: Tracing locates the failing stage, and prompt logging allows the exact call to be replayed.
- **C:** Incorrect for this question. An uncalibrated judge can reproduce a systematic error consistently and look stable while being wrong. Why the correct answer wins: Tracing locates the failing stage, and prompt logging allows the exact call to be replayed.
- **D:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: Tracing locates the failing stage, and prompt logging allows the exact call to be replayed.
- **E:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: Tracing locates the failing stage, and prompt logging allows the exact call to be replayed.

### Question 73 — C

Answer: Open the failing request trace → inspect the retrieval span for the passages returned → inspect the prompt and completion for that call → add the case to the evaluation set. The trace locates the stage, retrieval shows whether the passage existed, and the case becomes a regression test. The trace locates the failing stage, the retrieval span shows whether the passage was even present, and the case becomes a lasting regression test. Local study-map skill 4.6 (Online Feedback Loops and Continuous Evaluation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Incorrect for this question. The case is filed before the failure is understood, and the trace is opened after the completion has been read out of context. Why the correct answer wins: The trace locates the stage, retrieval shows whether the passage existed, and the case becomes a regression test.
- **B:** Incorrect for this question. Retraining before the failing stage is identified changes a component that may not be at fault. Why the correct answer wins: The trace locates the stage, retrieval shows whether the passage existed, and the case becomes a regression test.
- **C:** Correct. The trace locates the failing stage, the retrieval span shows whether the passage was even present, and the case becomes a lasting regression test. In this case: The trace locates the stage, retrieval shows whether the passage existed, and the case becomes a regression test.
- **D:** Incorrect for this question. The retrieval span cannot be read without the trace, and retraining still precedes the diagnosis. Why the correct answer wins: The trace locates the stage, retrieval shows whether the passage existed, and the case becomes a regression test.

### Question 74 — B

Answer: Measure tokens per request and set a budget per endpoint. Per-request token measurement is what makes cost attributable. Tokens are the billing unit, so per-request measurement is what makes cost attributable to a workload. Local study-map skill 5.1 (Token Cost, Caching, and Throughput Planning), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: Per-request token measurement is what makes cost attributable.
- **B:** Correct. Tokens are the billing unit, so per-request measurement is what makes cost attributable to a workload. In this case: Per-request token measurement is what makes cost attributable.
- **C:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: Per-request token measurement is what makes cost attributable.
- **D:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: Per-request token measurement is what makes cost attributable.

### Question 75 — B

Answer: Cache identical requests and reuse the completion. Caching removes repeated inference for identical input. Caching removes repeated inference for identical input, which is the cheapest saving available. Local study-map skill 5.1 (Token Cost, Caching, and Throughput Planning), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. A shorter system prompt reduces input tokens on every single call. Why the correct answer wins: Caching removes repeated inference for identical input.
- **B:** Correct. Caching removes repeated inference for identical input, which is the cheapest saving available. In this case: Caching removes repeated inference for identical input.
- **C:** Incorrect for this question. A router applies a cheap model where it suffices and keeps the stronger model for hard cases. Why the correct answer wins: Caching removes repeated inference for identical input.
- **D:** Incorrect for this question. A TTL keeps a cached answer from outliving the content it came from. Why the correct answer wins: Caching removes repeated inference for identical input.

### Question 76 — C

Answer: Set a time-to-live on the cache. A time-to-live stops a cached answer outliving the content it came from. A TTL keeps a cached answer from outliving the content it came from. Local study-map skill 5.1 (Token Cost, Caching, and Throughput Planning), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: A time-to-live stops a cached answer outliving the content it came from.
- **B:** Incorrect for this question. Disabling logging removes the evidence an investigation needs and usually breaches the retention policy. Why the correct answer wins: A time-to-live stops a cached answer outliving the content it came from.
- **C:** Correct. A TTL keeps a cached answer from outliving the content it came from. In this case: A time-to-live stops a cached answer outliving the content it came from.
- **D:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: A time-to-live stops a cached answer outliving the content it came from.

### Question 77 — A

Answer: Route simple requests to a smaller model. Routing simple requests to a smaller model cuts cost and latency for the majority of traffic. A smaller model answers a simple request at a fraction of the cost and latency. Local study-map skill 5.2 (Model Routing, Distillation, and Right-Sizing), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Correct. A smaller model answers a simple request at a fraction of the cost and latency. In this case: Routing simple requests to a smaller model cuts cost and latency for the majority of traffic.
- **B:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: Routing simple requests to a smaller model cuts cost and latency for the majority of traffic.
- **C:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: Routing simple requests to a smaller model cuts cost and latency for the majority of traffic.
- **D:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: Routing simple requests to a smaller model cuts cost and latency for the majority of traffic.

### Question 78 — D

Answer: Add a router that classifies the request and selects a model. A router classifies the request and selects a model appropriate to it. A router applies a cheap model where it suffices and keeps the stronger model for hard cases. Local study-map skill 5.2 (Model Routing, Distillation, and Right-Sizing), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. A smaller model answers a simple request at a fraction of the cost and latency. Why the correct answer wins: A router classifies the request and selects a model appropriate to it.
- **B:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: A router classifies the request and selects a model appropriate to it.
- **C:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: A router classifies the request and selects a model appropriate to it.
- **D:** Correct. A router applies a cheap model where it suffices and keeps the stronger model for hard cases. In this case: A router classifies the request and selects a model appropriate to it.

### Question 79 — C

Answer: Stream the response so the first token arrives sooner. Streaming delivers the first token sooner and improves perceived latency. Streaming improves perceived latency without changing total generation time. Local study-map skill 5.3 (Latency Budgets and Streaming Design), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. A bounded retry with backoff stops a failing dependency from multiplying load. Why the correct answer wins: Streaming delivers the first token sooner and improves perceived latency.
- **B:** Incorrect for this question. Batch work uses cheaper capacity and takes the work off the interactive path. Why the correct answer wins: Streaming delivers the first token sooner and improves perceived latency.
- **C:** Correct. Streaming improves perceived latency without changing total generation time. In this case: Streaming delivers the first token sooner and improves perceived latency.
- **D:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: Streaming delivers the first token sooner and improves perceived latency.

### Question 80 — B

Answer: Retrieve fewer but better-ranked passages. Fewer, better-ranked passages cut tokens and improve precision. Retrieval depth is a direct cost driver; fewer, better passages cut tokens and can improve precision. Local study-map skill 5.4 (Retrieval Tuning for Relevance and Cost), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: Fewer, better-ranked passages cut tokens and improve precision.
- **B:** Correct. Retrieval depth is a direct cost driver; fewer, better passages cut tokens and can improve precision. In this case: Fewer, better-ranked passages cut tokens and improve precision.
- **C:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: Fewer, better-ranked passages cut tokens and improve precision.
- **D:** Incorrect for this question. Retrieving more passages adds tokens and can bury the relevant passage among distractors. Why the correct answer wins: Fewer, better-ranked passages cut tokens and improve precision.

### Question 81 — A

Answer: Compress the system prompt and remove redundant instructions. Compressing the system prompt reduces input tokens on every call. A shorter system prompt reduces input tokens on every single call. Local study-map skill 5.5 (Prompt Compression and Context Discipline), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Correct. A shorter system prompt reduces input tokens on every single call. In this case: Compressing the system prompt reduces input tokens on every call.
- **B:** Incorrect for this question. Retrieving more passages adds tokens and can bury the relevant passage among distractors. Why the correct answer wins: Compressing the system prompt reduces input tokens on every call.
- **C:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: Compressing the system prompt reduces input tokens on every call.
- **D:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: Compressing the system prompt reduces input tokens on every call.

### Question 82 — A

Answer: Re-run the evaluation after the cost optimization. An optimization that lowers cost can lower quality, so the evaluation must be re-run. An optimization that lowers cost can lower quality, and re-running the evaluation is what proves the trade is acceptable. Local study-map skill 5.5 (Prompt Compression and Context Discipline), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Correct. An optimization that lowers cost can lower quality, and re-running the evaluation is what proves the trade is acceptable. In this case: An optimization that lowers cost can lower quality, so the evaluation must be re-run.
- **B:** Incorrect for this question. A prompt change shipped without an evaluation gate is an unmeasured change to a production system. Why the correct answer wins: An optimization that lowers cost can lower quality, so the evaluation must be re-run.
- **C:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: An optimization that lowers cost can lower quality, so the evaluation must be re-run.
- **D:** Incorrect for this question. The support queue is a lagging signal that reports damage after users have already experienced it. Why the correct answer wins: An optimization that lowers cost can lower quality, so the evaluation must be re-run.

### Question 83 — B

Answer: Move steady traffic to provisioned throughput. Provisioned throughput lowers cost per token at sustained volume. Provisioned throughput trades a commitment for a lower cost per token at sustained volume. Local study-map skill 5.7 (Batch Inference and Provisioned Capacity Optimization), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: Provisioned throughput lowers cost per token at sustained volume.
- **B:** Correct. Provisioned throughput trades a commitment for a lower cost per token at sustained volume. In this case: Provisioned throughput lowers cost per token at sustained volume.
- **C:** Incorrect for this question. Pay-as-you-go costs nothing when idle and needs no forecast, which suits an unproven workload. Why the correct answer wins: Provisioned throughput lowers cost per token at sustained volume.
- **D:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: Provisioned throughput lowers cost per token at sustained volume.

### Question 84 — D, E

Answers: Measure tokens per request and set a budget per endpoint; Cache identical requests and reuse the completion. Per-request token budgets attribute cost, and caching removes identical repeated inference. Tokens are the billing unit, so per-request measurement is what makes cost attributable to a workload. Caching removes repeated inference for identical input, which is the cheapest saving available. Local study-map skill 5.1 (Token Cost, Caching, and Throughput Planning), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. A TTL keeps a cached answer from outliving the content it came from. Why the correct answer wins: Per-request token budgets attribute cost, and caching removes identical repeated inference.
- **B:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: Per-request token budgets attribute cost, and caching removes identical repeated inference.
- **C:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: Per-request token budgets attribute cost, and caching removes identical repeated inference.
- **D:** Correct. Tokens are the billing unit, so per-request measurement is what makes cost attributable to a workload. In this case: Per-request token budgets attribute cost, and caching removes identical repeated inference.
- **E:** Correct. Caching removes repeated inference for identical input, which is the cheapest saving available. In this case: Per-request token budgets attribute cost, and caching removes identical repeated inference.

### Question 85 — A, B

Answers: Route simple requests to a smaller model; Add a router that classifies the request and selects a model. A smaller model serves simple requests, and a router keeps the stronger model for hard ones. A smaller model answers a simple request at a fraction of the cost and latency. A router applies a cheap model where it suffices and keeps the stronger model for hard cases. Local study-map skill 5.2 (Model Routing, Distillation, and Right-Sizing), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Correct. A router applies a cheap model where it suffices and keeps the stronger model for hard cases. In this case: A smaller model serves simple requests, and a router keeps the stronger model for hard ones.
- **B:** Correct. A smaller model answers a simple request at a fraction of the cost and latency. In this case: A smaller model serves simple requests, and a router keeps the stronger model for hard ones.
- **C:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: A smaller model serves simple requests, and a router keeps the stronger model for hard ones.
- **D:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: A smaller model serves simple requests, and a router keeps the stronger model for hard ones.
- **E:** Incorrect for this question. The largest model adds cost and latency to requests that do not need its capability. Why the correct answer wins: A smaller model serves simple requests, and a router keeps the stronger model for hard ones.

### Question 86 — B

Answer: Measure cost and tokens per request → find the largest driver in the breakdown → apply the matching optimization → re-run the evaluation to confirm quality held. Measurement attributes spend, the breakdown picks the lever, and the evaluation makes the saving safe. Measurement attributes the spend, the breakdown picks the lever, and the evaluation is what makes the saving safe. Local study-map skill 5.7 (Batch Inference and Provisioned Capacity Optimization), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. A driver is named before measurement, and the evaluation runs before the change exists. Why the correct answer wins: Measurement attributes spend, the breakdown picks the lever, and the evaluation makes the saving safe.
- **B:** Correct. Measurement attributes the spend, the breakdown picks the lever, and the evaluation is what makes the saving safe. In this case: Measurement attributes spend, the breakdown picks the lever, and the evaluation makes the saving safe.
- **C:** Incorrect for this question. An optimization is applied before anything has been measured or attributed. Why the correct answer wins: Measurement attributes spend, the breakdown picks the lever, and the evaluation makes the saving safe.
- **D:** Incorrect for this question. Evaluation precedes both the change it would validate and the measurement that motivates it. Why the correct answer wins: Measurement attributes spend, the breakdown picks the lever, and the evaluation makes the saving safe.

### Question 87 — A, C

Answers: Retrieve fewer but better-ranked passages; Compress the system prompt and remove redundant instructions. Fewer better-ranked passages cut retrieved tokens, and a compressed system prompt cuts input tokens on every call. Retrieval depth is a direct cost driver; fewer, better passages cut tokens and can improve precision. A shorter system prompt reduces input tokens on every single call. Local study-map skill 5.4 (Retrieval Tuning for Relevance and Cost), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Correct. A shorter system prompt reduces input tokens on every single call. In this case: Fewer better-ranked passages cut retrieved tokens, and a compressed system prompt cuts input tokens on every call.
- **B:** Incorrect for this question. Retrieving more passages adds tokens and can bury the relevant passage among distractors. Why the correct answer wins: Fewer better-ranked passages cut retrieved tokens, and a compressed system prompt cuts input tokens on every call.
- **C:** Correct. Retrieval depth is a direct cost driver; fewer, better passages cut tokens and can improve precision. In this case: Fewer better-ranked passages cut retrieved tokens, and a compressed system prompt cuts input tokens on every call.
- **D:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: Fewer better-ranked passages cut retrieved tokens, and a compressed system prompt cuts input tokens on every call.
- **E:** Incorrect for this question. Caching removes repeated inference for identical input, which is the cheapest saving available. Why the correct answer wins: Fewer better-ranked passages cut retrieved tokens, and a compressed system prompt cuts input tokens on every call.

### Question 88 — D

Answer: Measure the current request rate and token volume → forecast the peak and steady load → compare pay-as-you-go cost with provisioned throughput at that volume → load test the chosen configuration. Measurement and forecasting come before the commercial comparison, and the load test validates the choice. Measurement and forecasting come before the commercial comparison, and the load test validates the decision. Local study-map skill 5.7 (Batch Inference and Provisioned Capacity Optimization), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Model performance, capacity, and cost: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/provisioned-throughput

- **A:** Incorrect for this question. A load test needs a configuration chosen from the measurement and forecast, both of which come later. Why the correct answer wins: Measurement and forecasting come before the commercial comparison, and the load test validates the choice.
- **B:** Incorrect for this question. The forecast is made without a measurement baseline, and the commitment precedes the measurement entirely. Why the correct answer wins: Measurement and forecasting come before the commercial comparison, and the load test validates the choice.
- **C:** Incorrect for this question. Capacity is committed before the demand that justifies it has been measured. Why the correct answer wins: Measurement and forecasting come before the commercial comparison, and the load test validates the choice.
- **D:** Correct. Measurement and forecasting come before the commercial comparison, and the load test validates the decision. In this case: Measurement and forecasting come before the commercial comparison, and the load test validates the choice.

### Question 89 — D, E

Answers: Chunk documents by section with a small overlap; Rebuild the index on a schedule after the source content changes. Section-sized chunks make the citation specific, and a scheduled refresh keeps the index current. Section-sized chunks with overlap keep a passage coherent while staying small enough to be specific. Scheduled refresh keeps retrieval aligned with the source; without it the assistant answers from retired content. Local study-map skill 3.6 (Chunking, Embeddings, and Index Refresh), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. Retraining addresses a data or concept problem; it cannot repair a retrieval defect or a malformed prompt. Why the correct answer wins: Section-sized chunks make the citation specific, and a scheduled refresh keeps the index current.
- **B:** Incorrect for this question. A whole-document chunk makes retrieval return an undifferentiated document, so the answer quotes the wrong part. Why the correct answer wins: Section-sized chunks make the citation specific, and a scheduled refresh keeps the index current.
- **C:** Incorrect for this question. Indexing everything raises noise and cost, and can make content retrievable that should never be returned. Why the correct answer wins: Section-sized chunks make the citation specific, and a scheduled refresh keeps the index current.
- **D:** Correct. Scheduled refresh keeps retrieval aligned with the source; without it the assistant answers from retired content. In this case: Section-sized chunks make the citation specific, and a scheduled refresh keeps the index current.
- **E:** Correct. Section-sized chunks with overlap keep a passage coherent while staying small enough to be specific. In this case: Section-sized chunks make the citation specific, and a scheduled refresh keeps the index current.

### Question 90 — A

Answer: Use hybrid search with semantic ranking. Hybrid search keeps keyword matching for exact identifiers. Hybrid search combines keyword and vector matching, and semantic ranking reorders the top results, which improves recall on domain vocabulary and identifiers. Local study-map skill 3.5 (Retrieval-Augmented Grounding with Azure AI Search), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Correct. Hybrid search combines keyword and vector matching, and semantic ranking reorders the top results, which improves recall on domain vocabulary and identifiers. In this case: Hybrid search keeps keyword matching for exact identifiers.
- **B:** Incorrect for this question. Model size does not repair missing context; without the passage, a larger model still guesses. Why the correct answer wins: Hybrid search keeps keyword matching for exact identifiers.
- **C:** Incorrect for this question. Fine-tuning bakes a snapshot of the content into the model, so it goes stale as documents change. Why the correct answer wins: Hybrid search keeps keyword matching for exact identifiers.
- **D:** Incorrect for this question. Vector-only retrieval misses exact identifiers and product codes, which is where keyword matching earns its place. Why the correct answer wins: Hybrid search keeps keyword matching for exact identifiers.

### Question 91 — D

Answer: Create a Foundry hub and a project per team. A project per team isolates assets while a hub shares capacity. A hub shares connections and capacity, and a project gives a team an isolated working boundary for its own assets. Local study-map skill 3.1 (Foundry Hub, Project, and Shared Capacity), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Microsoft Foundry and prompt flow: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/architecture

- **A:** Incorrect for this question. A shared workspace mixes assets and identities across environments, so a test job can register over the model production is serving. Why the correct answer wins: A project per team isolates assets while a hub shares capacity.
- **B:** Incorrect for this question. A single shared project mixes assets and permissions, so one team can change what another depends on. Why the correct answer wins: A project per team isolates assets while a hub shares capacity.
- **C:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A project per team isolates assets while a hub shares capacity.
- **D:** Correct. A hub shares connections and capacity, and a project gives a team an isolated working boundary for its own assets. In this case: A project per team isolates assets while a hub shares capacity.

### Question 92 — A

Answer: Build the evaluation dataset from real queries with graded answers. A versioned data asset records the exact input used, which is what makes an old model reproducible. A dataset drawn from real traffic with graded answers is what makes an evaluation number mean something. Local study-map skill 4.1 (Evaluation Dataset and Ground-Truth Design), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Generative AI evaluation and safety: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-approach-gen-ai

- **A:** Correct. A dataset drawn from real traffic with graded answers is what makes an evaluation number mean something. In this case: A versioned data asset records the exact input used, which is what makes an old model reproducible.
- **B:** Incorrect for this question. A set authored from the prompt repeats its assumptions, so it passes changes that real users would reject. Why the correct answer wins: A versioned data asset records the exact input used, which is what makes an old model reproducible.
- **C:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: A versioned data asset records the exact input used, which is what makes an old model reproducible.
- **D:** Incorrect for this question. Replacing the automation resolves the symptom without discovering why the system failed. Why the correct answer wins: A versioned data asset records the exact input used, which is what makes an old model reproducible.

### Question 93 — A, C

Answers: Define the workspace in a Bicep module deployed per environment; Pass environment values through a Bicep parameter file per stage. A Bicep module defines the shape once, and a parameter file supplies the per-region values. Bicep gives a declarative, reviewable definition, so an environment can be recreated identically and configuration drift becomes visible. A parameter file keeps one module per environment, so only the values differ and the shape stays identical. Local study-map skill 1.3 (Infrastructure as Code with Bicep), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Correct. A parameter file keeps one module per environment, so only the values differ and the shape stays identical. In this case: A Bicep module defines the shape once, and a parameter file supplies the per-region values.
- **B:** Incorrect for this question. Exporting captures whatever exists, including accidental settings, and starts the estate from an unreviewed hand-built state. Why the correct answer wins: A Bicep module defines the shape once, and a parameter file supplies the per-region values.
- **C:** Correct. Bicep gives a declarative, reviewable definition, so an environment can be recreated identically and configuration drift becomes visible. In this case: A Bicep module defines the shape once, and a parameter file supplies the per-region values.
- **D:** Incorrect for this question. Manual portal steps are not reproducible, cannot be reviewed as code, and drift as soon as someone edits a setting. Why the correct answer wins: A Bicep module defines the shape once, and a parameter file supplies the per-region values.
- **E:** Incorrect for this question. A hand rebuild cannot be reproduced exactly and drifts from the definition the team believed it had. Why the correct answer wins: A Bicep module defines the shape once, and a parameter file supplies the per-region values.

### Question 94 — C

Answer: Authenticate the workflow with workload identity federation and no stored secret. Workload identity federation removes the stored secret entirely. Federated identity exchanges the workflow token for an Azure credential, so no long-lived secret exists to leak or rotate. Local study-map skill 1.5 (GitHub Actions CI/CD and Workload Identity Federation), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. A plain environment variable appears in job definitions and logs, which exposes the secret. Why the correct answer wins: Workload identity federation removes the stored secret entirely.
- **B:** Incorrect for this question. Owner on the subscription lets a pipeline change any resource, so one bad commit can affect everything. Why the correct answer wins: Workload identity federation removes the stored secret entirely.
- **C:** Correct. Federated identity exchanges the workflow token for an Azure credential, so no long-lived secret exists to leak or rotate. In this case: Workload identity federation removes the stored secret entirely.
- **D:** Incorrect for this question. A stored client secret is long-lived and must be rotated; federation removes the secret entirely. Why the correct answer wins: Workload identity federation removes the stored secret entirely.

### Question 95 — C

Answer: Register each candidate with a version and deploy one explicit version. An explicit version pins the artifact so it can be identified later. An explicit version pins what is served, so a new registration cannot silently change production behaviour. Local study-map skill 1.6 (Model Registry and Environment Promotion), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: Azure Machine Learning infrastructure and IaC: https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace

- **A:** Incorrect for this question. Printed metrics live in a log stream, cannot be compared across runs, and disappear when retention expires. Why the correct answer wins: An explicit version pins the artifact so it can be identified later.
- **B:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: An explicit version pins the artifact so it can be identified later.
- **C:** Correct. An explicit version pins what is served, so a new registration cannot silently change production behaviour. In this case: An explicit version pins the artifact so it can be identified later.
- **D:** Incorrect for this question. Deploying whatever is latest lets an untested registration reach production with no promotion gate. Why the correct answer wins: An explicit version pins the artifact so it can be identified later.

### Question 96 — D, E

Answers: Tag the registered model with the data asset and commit it came from; Attach a description, metrics, and intended use to the model version. Tags carry provenance, and the model card carries metrics and intended use. Tags carry provenance, which is what an audit needs in order to rebuild the artifact. Documented metrics and intended use let a reviewer decide whether the version is fit to promote. Local study-map skill 2.4 (Model Registration, Versioning, and Metadata), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. An aggregate can look healthy while one segment fails, which is exactly what segment-level evaluation is for. Why the correct answer wins: Tags carry provenance, and the model card carries metrics and intended use.
- **B:** Incorrect for this question. Deploying whatever is latest lets an untested registration reach production with no promotion gate. Why the correct answer wins: Tags carry provenance, and the model card carries metrics and intended use.
- **C:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: Tags carry provenance, and the model card carries metrics and intended use.
- **D:** Correct. Documented metrics and intended use let a reviewer decide whether the version is fit to promote. In this case: Tags carry provenance, and the model card carries metrics and intended use.
- **E:** Correct. Tags carry provenance, which is what an audit needs in order to rebuild the artifact. In this case: Tags carry provenance, and the model card carries metrics and intended use.

### Question 97 — A

Answer: Keep the previous deployment in place so traffic can be moved back. A retained deployment turns rollback into a traffic change. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. Local study-map skill 2.7 (Autoscaling, Health Probes, and Rollback), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Correct. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. In this case: A retained deployment turns rollback into a traffic change.
- **B:** Incorrect for this question. Skipping the staged check saves a day and moves the discovery of a defect to a customer. Why the correct answer wins: A retained deployment turns rollback into a traffic change.
- **C:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: A retained deployment turns rollback into a traffic change.
- **D:** Incorrect for this question. A one-step replacement exposes every request to an unproven version with no measured canary. Why the correct answer wins: A retained deployment turns rollback into a traffic change.

### Question 98 — D

Answer: Deploy a batch endpoint for the overnight scoring job. A batch endpoint scores a large file without always-on capacity. A batch endpoint scores a large file on a schedule and needs no always-on capacity. Local study-map skill 2.6 (Batch Endpoints and Controlled Traffic Rollout), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Scoring a large file one request at a time pays for always-on capacity and is slow for bulk work. Why the correct answer wins: A batch endpoint scores a large file without always-on capacity.
- **B:** Incorrect for this question. A compute instance is a single-user development machine; its state ends with the session and it is not a repeatable execution target. Why the correct answer wins: A batch endpoint scores a large file without always-on capacity.
- **C:** Incorrect for this question. A managed online endpoint serves real-time requests and manages the underlying infrastructure. Why the correct answer wins: A batch endpoint scores a large file without always-on capacity.
- **D:** Correct. A batch endpoint scores a large file on a schedule and needs no always-on capacity. In this case: A batch endpoint scores a large file without always-on capacity.

### Question 99 — C

Answer: Set autoscale rules on the deployment with a deliberate minimum instance count. Autoscale matches capacity to load with a floor that protects latency. Autoscale matches capacity to load, and the minimum sets the floor that protects latency during a burst. Local study-map skill 2.7 (Autoscaling, Health Probes, and Rollback), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Scoring a large file one request at a time pays for always-on capacity and is slow for bulk work. Why the correct answer wins: Autoscale matches capacity to load with a floor that protects latency.
- **B:** Incorrect for this question. A fixed count either wastes money at low load or throttles at peak. Why the correct answer wins: Autoscale matches capacity to load with a floor that protects latency.
- **C:** Correct. Autoscale matches capacity to load, and the minimum sets the floor that protects latency during a burst. In this case: Autoscale matches capacity to load with a floor that protects latency.
- **D:** Incorrect for this question. Without probes, a container that starts but cannot load the model still receives traffic. Why the correct answer wins: Autoscale matches capacity to load with a floor that protects latency.

### Question 100 — B, E

Answers: Split endpoint traffic 10/90 so the new deployment receives a canary share; Keep the previous deployment in place so traffic can be moved back. A canary share measures the candidate, and a retained deployment makes rollback a traffic change. A traffic split sends a small share to the new deployment, so a regression affects fewer requests and is measurable. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. Local study-map skill 2.5 (Managed Online Endpoint Deployment), mapped to the official guide: Microsoft AI-300 study guide, skills measured as of October 15, 2026 Primary reference: ML lifecycle, endpoints, and monitoring: https://learn.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment

- **A:** Incorrect for this question. Baking the model ties every version to an image build, which slows promotion and bloats the registry. Why the correct answer wins: A canary share measures the candidate, and a retained deployment makes rollback a traffic change.
- **B:** Correct. A traffic split sends a small share to the new deployment, so a regression affects fewer requests and is measurable. In this case: A canary share measures the candidate, and a retained deployment makes rollback a traffic change.
- **C:** Incorrect for this question. A one-step replacement exposes every request to an unproven version with no measured canary. Why the correct answer wins: A canary share measures the candidate, and a retained deployment makes rollback a traffic change.
- **D:** Incorrect for this question. Overwriting destroys the previous artifact and the audit trail that rollback depends on. Why the correct answer wins: A canary share measures the candidate, and a retained deployment makes rollback a traffic change.
- **E:** Correct. A retained deployment makes rollback a traffic change rather than a rebuild and redeploy. In this case: A canary share measures the candidate, and a retained deployment makes rollback a traffic change.
